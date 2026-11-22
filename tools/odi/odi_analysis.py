#!/usr/bin/env python3
"""ODI opportunity scores and needs-based segmentation with a tested gate.

Usage:  python tools/odi/odi_analysis.py survey.csv --out <analysis-folder>

The CSV has one row per respondent and, for each outcome, a <name>_imp and
a <name>_sat column rated 1-5. The method and the reason for each part of
the gate are in methods/odi/opportunity-analysis.md, Step 5.

A segmentation at k is accepted only if all four hold:
  1. its silhouette beats the response-shaped null (p <= .05);
  2. its silhouette beats the single-peak null on the rotated and on
     the principal factor axes (p <= .05 on each);
  3. every segment is stable under bootstrap (mean Jaccard >= .75);
  4. every segment holds at least 10% of respondents.

Exit status: 0 analysis completed (with or without segments), 2 bad input.
"""
import argparse
import csv
import math
import sys
import warnings
from pathlib import Path

import numpy as np
from scipy.special import ndtr
from sklearn.cluster import KMeans
from sklearn.decomposition import FactorAnalysis
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics import silhouette_score
from threadpoolctl import threadpool_limits

MIN_N = 180
MAX_MISSING = 0.10   # per respondent; must be strictly below
MIN_MINUTES = 5
KS = range(2, 9)
ALPHA = 0.05
MIN_SHARE = 0.10
MIN_JACCARD = 0.75
NO_SEGMENTS = "no valid segmentation"


class InputError(Exception):
    """The survey fails the input gate."""


# ---------- input gate and cleaning

def load_survey(path, id_column="respondent_id", duration_column=None):
    """Return respondent ids, outcome names, importance, satisfaction, log."""
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames or []
        rows = list(reader)

    names = [c[:-4] for c in header if c.endswith("_imp") and c[:-4] + "_sat" in header]
    orphans = [c for c in header if c.endswith("_sat") and c[:-4] + "_imp" not in header]
    if orphans:
        raise InputError(f"satisfaction columns with no importance column: {orphans}")
    if len(names) < 3:
        raise InputError("need at least 3 outcomes, each with _imp and _sat columns")
    for column in (id_column, duration_column):
        if column and column not in header:
            raise InputError(f"no column named {column!r}")
    ids = [row[id_column] for row in rows]
    if len(set(ids)) != len(ids):
        raise InputError(f"{id_column!r} values are not unique")

    def rating(row, column):
        text = (row[column] or "").strip()
        if text in ("", "NA"):
            return np.nan
        if text not in ("1", "2", "3", "4", "5", "1.0", "2.0", "3.0", "4.0", "5.0"):
            raise InputError(f"{column} for {row[id_column]}: {text!r} is not a rating from 1 to 5")
        return float(text)

    log, kept, ratings = [], [], []
    for row in rows:
        values = np.array([rating(row, n + s) for s in ("_imp", "_sat") for n in names])
        reason = None
        if np.isnan(values).mean() >= MAX_MISSING:
            reason = "10% or more missing"
        elif len(set(values[~np.isnan(values)])) == 1:
            reason = "same answer to every question"
        elif duration_column:
            try:
                minutes = float(row[duration_column])
            except (TypeError, ValueError):
                minutes = math.nan
            if not math.isfinite(minutes):
                reason = "no valid completion time"
            elif minutes < MIN_MINUTES:
                reason = "finished in under 5 minutes"
        if reason:
            log.append((row[id_column], reason))
        else:
            kept.append(row[id_column])
            ratings.append(values)
    if len(kept) < MIN_N:
        raise InputError(
            f"N = {len(kept)} after cleaning ({len(log)} removed); need at least {MIN_N}"
        )
    both = np.array(ratings)
    imp, sat = both[:, :len(names)], both[:, len(names):]
    empty = [n for j, n in enumerate(names)
             if np.isnan(imp[:, j]).all() or np.isnan(sat[:, j]).all()]
    if empty:
        raise InputError(f"outcomes with no ratings: {empty}")
    return kept, names, imp, sat, log


# ---------- scoring

def category(score):
    if score > 15:
        return "Extreme"
    if score >= 12:
        return "High"
    if score >= 10:
        return "Moderate"
    return "Low"


def opportunity_scores(names, imp, sat):
    """Top-2-box scores, highest opportunity first."""
    rows = []
    for j, name in enumerate(names):
        i, s = imp[:, j], sat[:, j]
        i, s = i[~np.isnan(i)], s[~np.isnan(s)]
        # None, not zero: a small segment can leave an outcome unanswered.
        importance = float((i >= 4).sum() * 10 / len(i)) if len(i) else None
        satisfaction = float((s >= 4).sum() * 10 / len(s)) if len(s) else None
        if importance is None or satisfaction is None:
            score = label = None
        else:
            score = round(importance + max(importance - satisfaction, 0), 9)
            label = category(score)
        rows.append(dict(outcome=name, importance=importance, satisfaction=satisfaction,
                         opportunity=score, category=label))
    return sorted(rows, key=lambda r: -(r["opportunity"] or 0))


def gap_scores(imp, sat):
    """Importance minus satisfaction; a missing gap takes the outcome's mean."""
    gaps = imp - sat
    for column in gaps.T:
        missing = np.isnan(column)
        column[missing] = column[~missing].mean() if not missing.all() else 0
    return gaps


# ---------- pipeline shared by the data, both nulls and the bootstrap

def count_factors(gaps, rng, rounds=200):
    """Horn's parallel analysis: factors above the 95th percentile of chance."""
    def eigenvalues(x):
        return np.linalg.eigvalsh(np.corrcoef(x, rowvar=False))[::-1]

    chance = [eigenvalues(rng.permuted(gaps, axis=0)) for _ in range(rounds)]
    above = eigenvalues(gaps) > np.percentile(chance, 95, axis=0)
    return int(np.cumprod(above).sum())


def fit_factors(gaps, m):
    """Fit factors on z-scores; return the model and a scorer for any rows."""
    mean, sd = gaps.mean(axis=0), gaps.std(axis=0)
    sd[sd == 0] = 1
    model = FactorAnalysis(m, rotation="varimax" if m > 1 else None,
                           random_state=0, max_iter=1000).fit((gaps - mean) / sd)
    return model, lambda x: model.transform((x - mean) / sd)


def cluster(scores, k):
    return KMeans(k, n_init=5, random_state=0).fit(scores)


def silhouettes(scores):
    out = []
    for k in KS:
        labels = cluster(scores, k).labels_
        out.append(silhouette_score(scores, labels) if len(set(labels)) > 1 else -1.0)
    return np.array(out)


# ---------- the two nulls

def response_null(gaps, rng):
    """One correlated population that answers with the observed distributions.

    A Gaussian copula: each outcome keeps its distribution of gap scores
    (steps, skew, ceilings) and each pair keeps its correlation. The latent
    correlation is adjusted because mapping onto a 9-point gap weakens it.
    """
    n, p = gaps.shape
    ordered = np.sort(gaps, axis=0)

    def to_responses(z):
        return np.take_along_axis(ordered, np.minimum((ndtr(z) * n).astype(int), n - 1), axis=0)

    def square_root(corr):
        values, vectors = np.linalg.eigh(corr)
        root = vectors * np.sqrt(np.clip(values, 1e-9, None))
        return root / np.sqrt((root ** 2).sum(axis=1, keepdims=True))

    target = np.corrcoef(gaps, rowvar=False)
    latent = target.copy()
    trial = rng.standard_normal((8000, p))
    for _ in range(5):
        root = square_root(latent)
        got = np.corrcoef(to_responses(trial @ root.T), rowvar=False)
        latent = root @ root.T + target - np.nan_to_num(got)
    root = square_root(latent)
    return lambda: to_responses(rng.standard_normal((n, p)) @ root.T)


def count_peaks(density, tolerance=0.01):
    """Peaks that stand out by more than `tolerance` of the tallest."""
    margin = tolerance * density.max()
    peaks, rising, high, low = 0, True, density[0], 0.0
    for value in density:
        if rising:
            high = max(high, value)
            if value < high - margin:
                peaks, rising, low = peaks + 1, False, value
        else:
            low = min(low, value)
            if value > low + margin:
                rising, high = True, value
    return peaks + rising


def single_peak_bandwidth(values):
    """Silverman's critical bandwidth: least smoothing that leaves one peak."""
    sd = values.std()
    if sd < 1e-12:
        return 0.0
    for h in sd * np.geomspace(0.1, 3, 45):
        grid = np.linspace(values.min() - 3 * h, values.max() + 3 * h, 160)
        density = np.exp(-0.5 * ((grid[:, None] - values) / h) ** 2).sum(axis=1)
        if count_peaks(density) == 1:
            return h
    return 3 * sd


def single_peak_null(scores, rng):
    """One population with the observed spread, skew and tails on each factor."""
    h = np.array([single_peak_bandwidth(c) for c in scores.T])
    mean, var = scores.mean(axis=0), scores.var(axis=0)
    shrink = np.sqrt(1 + h * h / np.where(var > 1e-24, var, 1))

    def draw():
        sample = np.column_stack([rng.choice(c, len(c)) for c in scores.T])
        return mean + (sample - mean + h * rng.standard_normal(scores.shape)) / shrink

    return draw


def single_peak_axes(scores):
    """The axes to draw the single-peak null on; a k must beat it on each.

    That null resamples each axis by itself, so it needs axes that are
    independent in one population. Varimax axes are, for separate traits.
    They are not when there are more factors than traits: rotation splits
    one trait across several correlated factors. Principal axes cover that.
    """
    m = scores.shape[1]
    if m == 1:
        return [np.eye(1)]
    return [np.eye(m), np.linalg.eigh(np.cov(scores, rowvar=False))[1]]


def compare_to_null(observed, null):
    """Excess over the null at each k, and p corrected for trying every k.

    Each silhouette is standardized within its k, then compared with the
    largest standardized value each reference dataset reached at any k.
    """
    pool = np.vstack([observed, null])
    z = (pool - pool.mean(axis=0)) / (pool.std(axis=0) + 1e-12)
    best = z.max(axis=1)
    return z[0], np.array([(best >= value).mean() for value in z[0]])


# ---------- stability

def bootstrap_stability(gaps, m, labels, rng, rounds):
    """Lowest cluster-wise mean Jaccard at each k, refitting the whole pipeline."""
    totals = [np.zeros(k) for k in KS]
    for _ in range(rounds):
        sample = gaps[rng.integers(0, len(gaps), len(gaps))]
        _, score = fit_factors(sample, m)
        sample_scores, all_scores = score(sample), score(gaps)
        for index, k in enumerate(KS):
            found = cluster(sample_scores, k).predict(all_scores)
            both = np.zeros((k, k))
            np.add.at(both, (labels[index], found), 1)
            either = both.sum(1, keepdims=True) + both.sum(0, keepdims=True) - both
            totals[index] += (both / np.maximum(either, 1)).max(axis=1)
    return np.array([t.min() / rounds for t in totals])


# ---------- segmentation

def segment(gaps, factors=None, nulls=199, bootstrap=100, seed=0):
    """Run the gate. `gaps` is respondents x outcomes, with no missing values."""
    if nulls < 99 or bootstrap < 50:
        raise InputError("need at least 99 null draws and 50 bootstrap rounds")
    varying = np.ptp(gaps, axis=0) > 0
    gaps = gaps[:, varying]
    if gaps.shape[1] < 3:
        return dict(verdict=NO_SEGMENTS, reason="fewer than 3 outcomes vary", k=None,
                    labels=None, table=[], varying=varying, loadings=None,
                    variance=None, factors=0, factor_rule="not run")

    streams = [np.random.default_rng([seed, i]) for i in range(4)]
    with threadpool_limits(1), warnings.catch_warnings():
        # A resample can have fewer distinct points than k, or an EM fit that
        # stops at its iteration limit. Both are handled by the gate.
        warnings.simplefilter("ignore", ConvergenceWarning)
        if factors is None:
            found = count_factors(gaps, streams[0])
            m = max(found, 1)
            rule = f"parallel analysis retained {found}"
            if not found:
                rule += "; 1 used so the gate could still run"
        else:
            if not 1 <= factors < gaps.shape[1]:
                raise InputError(f"--factors must be from 1 to {gaps.shape[1] - 1}")
            m, rule = factors, "set with --factors"

        model, score = fit_factors(gaps, m)
        scores = score(gaps)
        observed = silhouettes(scores)
        labels = [cluster(scores, k).labels_ for k in KS]
        shares = [np.bincount(lab, minlength=k) / len(gaps) for k, lab in zip(KS, labels)]

        draw = response_null(gaps, streams[1])
        reference = []
        for _ in range(nulls):
            sample = draw()
            reference.append(silhouettes(fit_factors(sample, m)[1](sample)))
        z_response, p_response = compare_to_null(observed, reference)

        z_peak, p_peak = np.full(len(KS), np.inf), np.zeros(len(KS))
        for axes in single_peak_axes(scores):
            draw = single_peak_null(scores @ axes, streams[2])
            # Distances do not change with rotation, so neither does silhouette.
            z, p = compare_to_null(observed, [silhouettes(draw()) for _ in range(nulls)])
            z_peak, p_peak = np.minimum(z_peak, z), np.maximum(p_peak, p)

        stability = bootstrap_stability(gaps, m, labels, streams[3], bootstrap)

    table = []
    for i, k in enumerate(KS):
        failed = [why for bad, why in (
            (p_response[i] > ALPHA, "response null"),
            (p_peak[i] > ALPHA, "single-peak null"),
            (stability[i] < MIN_JACCARD, "stability"),
            (shares[i].min() < MIN_SHARE, "balance"),
        ) if bad]
        table.append(dict(k=k, silhouette=float(observed[i]),
                          p_response=float(p_response[i]), p_single_peak=float(p_peak[i]),
                          min_jaccard=float(stability[i]), min_share=float(shares[i].min()),
                          failed=", ".join(failed)))

    passing = [i for i, row in enumerate(table) if not row["failed"]]
    result = dict(table=table, varying=varying, factors=m, factor_rule=rule,
                  loadings=model.components_.T, variance=(model.components_ ** 2).mean(axis=1))
    if not passing:
        return dict(result, verdict=NO_SEGMENTS, k=None, labels=None,
                    reason="no k passed all four checks")
    # Of the k that pass, take the one furthest above its weaker null.
    best = max(passing, key=lambda i: min(z_response[i], z_peak[i]))
    order = np.argsort(-shares[best], kind="stable")   # segment 1 is the largest
    return dict(result, verdict=f"segmentation passed: k = {KS[best]}", k=KS[best],
                labels=np.argsort(order)[labels[best]] + 1,
                reason="statistics only; interpretability and reachability still need a person")


# ---------- output

def write_csv(path, header, rows):
    def cell(value):
        return f"{value:.4f}" if isinstance(value, float) else value

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows([cell(v) for v in row] for row in rows)


def write_outputs(out, survey, options):
    ids, names, imp, sat, log = survey
    result = segment(gap_scores(imp, sat), options.factors, options.nulls,
                     options.bootstrap, options.seed)
    out.mkdir(parents=True, exist_ok=True)
    for optional in ("segments.csv", "segment_scores.csv", "factor_loadings.csv"):
        path = out / optional
        if path.exists():   # left by an earlier run; would contradict this one
            path.unlink()

    scores = opportunity_scores(names, imp, sat)
    write_csv(out / "opportunity_scores.csv", list(scores[0]),
              [r.values() for r in scores])
    write_csv(out / "cleaning_log.csv", ["respondent_id", "reason"], log)
    write_csv(out / "segmentation_diagnostics.csv",
              ["k", "silhouette", "p_response", "p_single_peak", "min_jaccard",
               "min_share", "failed"],
              [r.values() for r in result["table"]])
    if result["loadings"] is not None:
        kept = [n for n, keep in zip(names, result["varying"]) if keep]
        write_csv(out / "factor_loadings.csv",
                  ["outcome"] + [f"factor_{i + 1}" for i in range(result["factors"])],
                  [[n] + [float(v) for v in row] for n, row in zip(kept, result["loadings"])])

    sizes = []
    if result["k"]:
        labels = result["labels"]
        write_csv(out / "segments.csv", ["respondent_id", "segment"], zip(ids, labels))
        rows = []
        for number in range(1, result["k"] + 1):
            members = labels == number
            sizes.append(f"segment {number}: {members.sum()} ({members.mean():.0%})")
            rows += [[number] + list(r.values())
                     for r in opportunity_scores(names, imp[members], sat[members])]
        write_csv(out / "segment_scores.csv", ["segment"] + list(scores[0]), rows)

    lines = [f"# ODI analysis: {result['verdict']}", "", f"- Reason: {result['reason']}"]
    lines += [f"- {size}" for size in sizes]
    lines += [
        f"- N analyzed: {len(ids)}; removed: {len(log)}; outcomes: {len(names)}",
        f"- Missing ratings among those analyzed: {np.isnan(np.hstack([imp, sat])).mean():.1%}",
        f"- Factors: {result['factors']} ({result['factor_rule']})",
    ]
    if result["variance"] is not None:
        lines.append("- Variance explained by factor: "
                     + ", ".join(f"{v:.1%}" for v in result["variance"]))
    if not result["varying"].all():
        lines.append(f"- Left out of segmentation, gap never varies: "
                     f"{[n for n, keep in zip(names, result['varying']) if not keep]}")
    if not options.duration_column:
        lines.append("- Speeder check NOT run: no --duration-column given")
    if len(ids) < 3 * len(names):
        lines.append("- Warning: N is below 3 x the number of outcomes")
    lines += [f"- Settings: {options.nulls} draws per null, {options.bootstrap} bootstrap "
              f"rounds, seed {options.seed}", ""]
    if result["table"]:
        lines += [
            "A k needs both p <= 0.05, Jaccard >= 0.75 and smallest segment >= 10%.", "",
            "| k | silhouette | p, response null | p, single-peak null "
            "| lowest Jaccard | smallest segment | fails on |",
            "|---|---|---|---|---|---|---|",
        ]
        lines += [f"| {r['k']} | {r['silhouette']:.3f} | {r['p_response']:.3f} "
                  f"| {r['p_single_peak']:.3f} | {r['min_jaccard']:.3f} "
                  f"| {r['min_share']:.1%} | {r['failed'] or '-'} |" for r in result["table"]]
    text = "\n".join(lines) + "\n"
    (out / "summary.md").write_text(text, encoding="utf-8")
    return text


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("survey", type=Path, help="survey CSV")
    parser.add_argument("--out", type=Path, required=True,
                        help="output folder; this script's files in it are rewritten")
    parser.add_argument("--id-column", default="respondent_id")
    parser.add_argument("--duration-column", help="completion time in minutes")
    parser.add_argument("--factors", type=int,
                        help="override parallel analysis; choose before seeing results")
    parser.add_argument("--nulls", type=int, default=199)
    parser.add_argument("--bootstrap", type=int, default=100)
    parser.add_argument("--seed", type=int, default=0)
    options = parser.parse_args(argv)
    try:
        survey = load_survey(options.survey, options.id_column, options.duration_column)
        print(write_outputs(options.out, survey, options))
    except (InputError, OSError, UnicodeDecodeError) as error:
        print(f"cannot analyze: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""How often the ODI segmentation gate is wrong, on data with known answers.

Runs the real pipeline on many synthetic surveys and prints one row per
scenario: how often the old silhouette > 0.25 rule, each null alone, and
the full gate reported segments. Uses 99 null draws and 50 bootstrap
rounds (the command's defaults are 199 and 100) and leaves two cores free.
Slow: allow half an hour or more on 8 cores.

Usage:  python evals/odi_calibration.py [trials per scenario, default 50]
"""
import os
import sys
from multiprocessing import Pool
from pathlib import Path

import numpy as np
from sklearn.metrics import adjusted_rand_score

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools" / "odi"))
import odi_analysis as odi  # noqa: E402


SEED = 20261122  # not the seeds the gate was developed on


def likert(mean, noise):
    return np.clip(np.rint(mean + noise), 1, 5)


def gaussian(rng, n=180, p=24):
    return rng.standard_normal((n, p)), None


def likert_noise(rng, n=180, p=24):
    return likert(3.4, rng.standard_normal((n, p))) - likert(2.9, rng.standard_normal((n, p))), None


def three_factors(rng, n=180, p=24):
    f = (rng.standard_normal((n, 3)) * [1.3, 0.9, 0.6])[:, np.arange(p) % 3]
    return (likert(3.4, 0.6 * f + 0.75 * rng.standard_normal((n, p)))
            - likert(2.8, -0.4 * f + 0.9 * rng.standard_normal((n, p)))), None


def ceiling(rng, n=180, p=24):
    t = rng.standard_normal((n, 1))
    return (likert(4.6, 0.7 * t + 0.5 * rng.standard_normal((n, p)))
            - likert(1.7, -0.9 * t + 0.4 * rng.standard_normal((n, p)))), None


def skewed(rng, n=180, p=24, traits=1):
    t = ((rng.gamma(2, 1, (n, traits)) - 2) / np.sqrt(2))[:, np.arange(p) % traits]
    return (likert(3.4, 0.6 * t + 0.8 * rng.standard_normal((n, p)))
            - likert(2.8, -0.6 * t + 0.8 * rng.standard_normal((n, p)))), None


def correlated_traits(rng, n=180, p=24, shared=0.7):
    draw = lambda k: (rng.gamma(2, 1, (n, k)) - 2) / np.sqrt(2)
    t = (shared * draw(1) + np.sqrt(1 - shared ** 2) * draw(3))[:, np.arange(p) % 3]
    return (likert(3.4, 0.6 * t + 0.8 * rng.standard_normal((n, p)))
            - likert(2.8, -0.6 * t + 0.8 * rng.standard_normal((n, p)))), None


def response_style(rng, n=180, p=24):
    width = np.exp(0.5 * rng.standard_normal((n, 1)))
    return (likert(3.6, width * rng.standard_normal((n, p)))
            - likert(2.6, width * rng.standard_normal((n, p)))), None


def planted(rng, n=180, p=24, effect=0.9, k=3):
    truth = rng.permutation(np.arange(n) % k)
    own = effect * ((np.arange(p) % k == truth[:, None]) - 1 / k)
    return (likert(3.4, own + rng.standard_normal((n, p)))
            - likert(3.0, -own + rng.standard_normal((n, p)))), truth


# name, generator, its arguments, factor count (None = parallel analysis)
SCENARIOS = [(f"none: Gaussian noise, {m} factors", gaussian, {}, m) for m in (1, 2, 3, 4, 6, 8)] + [
    ("none: rating noise", likert_noise, {}, None),
    ("none: rating noise, 100 outcomes", likert_noise, dict(p=100), None),
    ("none: rating noise, N=600", likert_noise, dict(n=600), None),
    ("none: 3 correlated need factors", three_factors, {}, None),
    ("none: ceiling effect", ceiling, {}, None),
    ("none: ceiling effect, 6 outcomes", ceiling, dict(p=6), None),
    ("none: 1 skewed trait", skewed, {}, None),
    ("none: 1 skewed trait, 2 factors forced", skewed, {}, 2),
    ("none: 1 skewed trait, 3 factors forced", skewed, {}, 3),
    ("none: 1 skewed trait, 6 factors forced", skewed, {}, 6),
    ("none: 1 skewed trait, N=600, 3 factors forced", skewed, dict(n=600), 3),
    ("none: ceiling effect, 3 factors forced", ceiling, {}, 3),
    ("none: 2 skewed traits", skewed, dict(traits=2), None),
    ("none: 3 correlated skewed traits", correlated_traits, {}, None),
    ("none: 1 skewed trait, N=600", skewed, dict(n=600), None),
    ("none: 3 skewed traits", skewed, dict(traits=3), None),
    ("none: response style", response_style, {}, None),
    ("3 segments, shift 0.5 points", planted, dict(effect=0.5), None),
    ("3 segments, shift 0.7 points", planted, dict(effect=0.7), None),
    ("3 segments, shift 0.9 points", planted, dict(effect=0.9), None),
    ("3 segments, shift 0.5 points, N=600", planted, dict(effect=0.5, n=600), None),
    ("3 segments, shift 0.9 points, 4 factors forced", planted, {}, 4),
    ("2 segments, shift 0.9 points", planted, dict(k=2), None),
    ("4 segments, shift 1.1 points", planted, dict(effect=1.1, k=4), None),
]


def trial(job):
    index, number = job
    _, make, arguments, factors = SCENARIOS[index]
    gaps, truth = make(np.random.default_rng([SEED, index, number]), **arguments)
    result = odi.segment(gaps, factors=factors, nulls=99, bootstrap=50, seed=number)
    table = result["table"]
    flags = [any(r["silhouette"] > 0.25 and r["min_share"] >= odi.MIN_SHARE for r in table)]
    flags += [any(r[key] <= odi.ALPHA for r in table) for key in ("p_response", "p_single_peak")]
    flags.append(result["k"] is not None)
    right = ari = np.nan
    if truth is not None and result["k"]:
        right = result["k"] == truth.max() + 1
        ari = adjusted_rand_score(truth, result["labels"])
    return index, flags + [right, ari]


def main(trials):
    print("| scenario | old rule | response null alone | single-peak null alone "
          "| full gate | right k | median ARI |")
    print("|---|---|---|---|---|---|---|", flush=True)
    with Pool(max(1, (os.cpu_count() or 1) - 2)) as pool:
        for index, scenario in enumerate(SCENARIOS):
            rows = [r for _, r in pool.map(trial, [(index, i) for i in range(trials)])]
            a = np.array(rows, dtype=float)
            found = ~np.isnan(a[:, 4])
            cells = [f"{int(v)}/{trials}" for v in a[:, :4].sum(axis=0)]
            cells += ([f"{int(a[found, 4].sum())}/{trials}", f"{np.median(a[found, 5]):.2f}"]
                      if found.any() else ["-", "-"])
            print(f"| {scenario[0]} | " + " | ".join(cells) + " |", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 50)

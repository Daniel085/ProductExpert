#!/usr/bin/env python3
"""Write the synthetic ODI survey fixtures. Every respondent here is made up.

Usage:  python evals/odi-fixtures/generate.py [output-folder]
"""
import csv
import sys
from pathlib import Path

import numpy as np

SEED = 20261121
N, OUTCOMES = 180, 24
SIZES = (75, 60, 45)


def ratings(mean, noise):
    return np.clip(np.rint(mean + noise), 1, 5).astype(int)


def noise(rng):
    """Every rating independent: no factors and no segments."""
    shape = (N, OUTCOMES)
    return ratings(3.4, rng.standard_normal(shape)), ratings(2.9, rng.standard_normal(shape)), None


def one_population(rng):
    """One skewed trait moves every rating: correlated, but no segments."""
    shape = (N, OUTCOMES)
    trait = (rng.gamma(2, 1, (N, 1)) - 2) / np.sqrt(2)
    return (ratings(3.4 + 0.6 * trait, 0.8 * rng.standard_normal(shape)),
            ratings(2.8 - 0.6 * trait, 0.8 * rng.standard_normal(shape)), None)


def planted(rng):
    """Three segments, each underserved on its own third of the outcomes."""
    shape = (N, OUTCOMES)
    truth = rng.permutation(np.repeat(np.arange(len(SIZES)), SIZES))
    own = (np.arange(OUTCOMES) % len(SIZES) == truth[:, None]) - 1 / len(SIZES)
    return (ratings(3.4 + 0.9 * own, rng.standard_normal(shape)),
            ratings(3.0 - 0.9 * own, rng.standard_normal(shape)), truth + 1)


FIXTURES = {"noise": noise, "one-population": one_population, "planted": planted}


def main(folder):
    (folder / "expected").mkdir(parents=True, exist_ok=True)
    for index, (name, make) in enumerate(FIXTURES.items()):
        rng = np.random.default_rng([SEED, index])
        imp, sat, truth = make(rng)
        minutes = rng.integers(9, 25, N)
        ids = [f"synthetic-{i + 1:03d}" for i in range(N)]
        with open(folder / f"{name}.csv", "w", newline="") as f:
            out = csv.writer(f, lineterminator="\n")
            out.writerow(["respondent_id", "duration_min"]
                         + [f"outcome_{j + 1}_{kind}" for j in range(OUTCOMES)
                            for kind in ("imp", "sat")])
            for i in range(N):
                out.writerow([ids[i], minutes[i]] + np.column_stack([imp[i], sat[i]]).ravel().tolist())
        if truth is not None:
            with open(folder / "expected" / f"{name}-segments.csv", "w", newline="") as f:
                out = csv.writer(f, lineterminator="\n")
                out.writerow(["respondent_id", "segment"])
                out.writerows(zip(ids, truth))


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent)

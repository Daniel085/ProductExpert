"""Run from the repo root:  python -m unittest discover -s tools/odi"""
import contextlib
import csv
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from sklearn.metrics import adjusted_rand_score

import odi_analysis as odi

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "evals" / "odi-fixtures"
OLD_SILHOUETTE_GATE = 0.25


def survey(n=180, p=6):
    """A valid survey as rows of strings."""
    rng = np.random.default_rng(1)
    header = ["respondent_id", "minutes"] + [f"o{j}_{s}" for j in range(p) for s in ("imp", "sat")]
    rows = []
    for i in range(n):
        values = rng.integers(1, 6, 2 * p)
        values[:2] = 2, 4   # never a straight-liner
        rows.append([f"r{i}", "12"] + [str(v) for v in values])
    return header, rows


class InputGate(unittest.TestCase):
    def load(self, header, rows, **options):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "survey.csv"
            with open(path, "w", newline="") as f:
                csv.writer(f).writerows([header] + rows)
            return odi.load_survey(path, **options)

    def test_n_180_passes_and_179_fails(self):
        self.assertEqual(len(self.load(*survey(180))[0]), 180)
        with self.assertRaisesRegex(odi.InputError, "N = 179"):
            self.load(*survey(179))

    def test_straight_liner_is_removed_and_logged(self):
        header, rows = survey(181)
        rows[0][2:] = ["3"] * 12
        ids, *_, log = self.load(header, rows)
        self.assertNotIn("r0", ids)
        self.assertEqual(log, [("r0", "same answer to every question")])

    def test_missing_must_be_below_ten_percent(self):
        header, rows = survey(182, p=10)   # 20 ratings each
        rows[0][5] = ""                    # 5% missing: kept
        rows[1][5] = rows[1][6] = "NA"     # exactly 10%: removed
        ids, *_, log = self.load(header, rows)
        self.assertIn("r0", ids)
        self.assertEqual(log, [("r1", "10% or more missing")])

    def test_speeders_and_unreadable_times_are_removed(self):
        header, rows = survey(184)
        for row, value in zip(rows, ("4.9", "", "nan", "5")):
            row[1] = value
        ids, *_, log = self.load(header, rows, duration_column="minutes")
        self.assertEqual([who for who, _ in log], ["r0", "r1", "r2"])
        self.assertIn("r3", ids)

    def test_rating_outside_one_to_five_is_refused(self):
        for bad in ("0", "6", "3.5", "high", "nan"):
            header, rows = survey()
            rows[4][4] = bad
            with self.assertRaises(odi.InputError):
                self.load(header, rows)

    def test_duplicate_ids_are_refused(self):
        header, rows = survey()
        rows[1][0] = rows[0][0]
        with self.assertRaisesRegex(odi.InputError, "not unique"):
            self.load(header, rows)

    def test_unpaired_satisfaction_column_is_refused(self):
        header, rows = survey()
        header[2] = "renamed"
        with self.assertRaisesRegex(odi.InputError, "no importance column"):
            self.load(header, rows)

    def test_importance_only_columns_are_not_outcomes(self):
        header, rows = survey()
        header.append("related_job_1_imp")
        for row in rows:
            row.append("4")
        self.assertEqual(len(self.load(header, rows)[1]), 6)


class Scoring(unittest.TestCase):
    def test_worked_example_from_the_method_doc(self):
        imp = np.array([[4.0]] * 72 + [[3.0]] * 28)
        sat = np.array([[5.0]] * 38 + [[1.0]] * 62)
        row, = odi.opportunity_scores(["materials"], imp, sat)
        self.assertEqual((row["importance"], row["satisfaction"]), (7.2, 3.8))
        self.assertAlmostEqual(row["opportunity"], 10.6)
        self.assertEqual(row["category"], "Moderate")

    def test_computed_boundary_score_lands_in_the_higher_category(self):
        imp = np.array([[4.0]] * 72 + [[3.0]] * 28)
        sat = np.array([[4.0]] * 24 + [[1.0]] * 76)
        row, = odi.opportunity_scores(["x"], imp, sat)
        self.assertEqual((row["opportunity"], row["category"]), (12.0, "High"))

    def test_overserved_earns_no_credit(self):
        row, = odi.opportunity_scores(["x"], np.array([[4.0], [1.0]]), np.array([[5.0], [5.0]]))
        self.assertEqual(row["opportunity"], 5.0)

    def test_missing_ratings_leave_the_denominator(self):
        row, = odi.opportunity_scores(["x"], np.array([[4.0], [1.0], [np.nan]]), np.ones((3, 1)))
        self.assertEqual(row["importance"], 5.0)

    def test_category_boundaries(self):
        self.assertEqual([odi.category(v) for v in (9.99, 10, 11.99, 12, 15, 15.01)],
                         ["Low", "Moderate", "Moderate", "High", "High", "Extreme"])

    def test_missing_gap_takes_the_outcome_mean(self):
        gaps = odi.gap_scores(np.array([[5.0], [3.0], [np.nan]]), np.ones((3, 1)))
        self.assertEqual(gaps.ravel().tolist(), [4, 2, 3])


class Statistics(unittest.TestCase):
    def test_response_null_keeps_distributions_and_correlation(self):
        rng = np.random.default_rng(2)
        shared = rng.standard_normal((3000, 1))
        gaps = np.clip(np.rint(2.5 + shared + rng.standard_normal((3000, 4))), -4, 4)
        draw = odi.response_null(gaps, rng)
        fake = np.vstack([draw() for _ in range(4)])
        self.assertLessEqual(set(np.unique(fake)), set(np.unique(gaps)))
        np.testing.assert_allclose(fake.mean(0), gaps.mean(0), atol=0.06)
        np.testing.assert_allclose(np.corrcoef(fake, rowvar=False),
                                   np.corrcoef(gaps, rowvar=False), atol=0.05)

    def test_single_peak_null_smooths_away_two_peaks(self):
        rng = np.random.default_rng(3)
        two = np.concatenate([rng.normal(-2, 0.5, 300), rng.normal(2, 0.5, 300)])
        h = odi.single_peak_bandwidth(two)
        self.assertGreater(h, 1)
        self.assertLess(odi.single_peak_bandwidth(rng.normal(0, 1, 600)), 0.5)
        fake = odi.single_peak_null(two[:, None], rng)()
        self.assertAlmostEqual(fake.std(), two.std(), delta=0.25)

    def test_p_value_counts_the_best_k_of_each_reference(self):
        null = np.random.default_rng(4).normal(0.5, 0.01, (99, 7))
        observed = np.full(7, 0.5)
        observed[2] = 0.9
        _, p = odi.compare_to_null(observed, null)
        self.assertEqual(p[2], 0.01)
        self.assertGreater(p[0], 0.5)

    def test_no_varying_outcomes_is_no_segmentation(self):
        self.assertEqual(odi.segment(np.ones((180, 5)))["verdict"], odi.NO_SEGMENTS)

    def test_too_few_draws_is_refused(self):
        with self.assertRaises(odi.InputError):
            odi.segment(np.ones((180, 5)), nulls=5)

    def test_pure_gaussian_noise_with_few_factors(self):
        """The reported failure: these passed silhouette > 0.25."""
        for m in (1, 2, 3):
            gaps = np.random.default_rng([5, m]).standard_normal((180, 24))
            result = odi.segment(gaps, factors=m, nulls=99, bootstrap=50)
            self.assertTrue(any(r["silhouette"] > OLD_SILHOUETTE_GATE for r in result["table"]))
            self.assertEqual(result["verdict"], odi.NO_SEGMENTS, f"{m} factors")

    def test_one_skewed_population_with_extra_factors(self):
        """Rotation splits one trait across factors; that is not a segment.

        With only the varimax axes in the single-peak null this passed as
        segments in most draws of this population.
        """
        for seed, m in ((0, 2), (1, 2), (2, 3)):
            rng = np.random.default_rng([7, seed])
            trait = (rng.gamma(2, 1, (180, 1)) - 2) / np.sqrt(2)
            noise = 0.8 * rng.standard_normal((2, 180, 24))
            gaps = (np.clip(np.rint(3.4 + 0.6 * trait + noise[0]), 1, 5)
                    - np.clip(np.rint(2.8 - 0.6 * trait + noise[1]), 1, 5))
            result = odi.segment(gaps, factors=m, nulls=99, bootstrap=50)
            self.assertEqual(result["verdict"], odi.NO_SEGMENTS, f"seed {seed}, {m} factors")


class Fixtures(unittest.TestCase):
    """The full command, at its default settings."""

    @classmethod
    def setUpClass(cls):
        cls.folder = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.folder.cleanup)
        cls.out = Path(cls.folder.name)
        cls.printed = {}
        for name in ("noise", "one-population", "planted"):
            text = io.StringIO()
            with contextlib.redirect_stdout(text):
                code = odi.main([str(FIXTURES / f"{name}.csv"), "--out", str(cls.out / name),
                                 "--duration-column", "duration_min"])
            assert code == 0, name
            cls.printed[name] = text.getvalue()

    @staticmethod
    def read(path):
        with open(path, newline="") as f:
            return list(csv.DictReader(f))

    def test_fixtures_without_segments_report_none(self):
        for name in ("noise", "one-population"):
            self.assertIn(odi.NO_SEGMENTS, self.printed[name])
            self.assertFalse((self.out / name / "segments.csv").exists())
            table = self.read(self.out / name / "segmentation_diagnostics.csv")
            self.assertTrue(any(float(r["silhouette"]) > OLD_SILHOUETTE_GATE
                                and float(r["min_share"]) >= odi.MIN_SHARE for r in table),
                            "fixture must be one the old gate accepted")

    def test_planted_segments_are_recovered(self):
        self.assertIn("segmentation passed: k = 3", self.printed["planted"])
        found = self.read(self.out / "planted" / "segments.csv")
        truth = self.read(FIXTURES / "expected" / "planted-segments.csv")
        self.assertEqual([r["respondent_id"] for r in found], [r["respondent_id"] for r in truth])
        self.assertGreaterEqual(adjusted_rand_score([r["segment"] for r in truth],
                                                    [r["segment"] for r in found]), 0.8)

    def test_each_segment_is_underserved_on_its_own_outcomes(self):
        rows = self.read(self.out / "planted" / "segment_scores.csv")
        blocks = set()
        for segment in "123":
            top = [r for r in rows if r["segment"] == segment][:5]
            block = {(int(r["outcome"].split("_")[1]) - 1) % 3 for r in top}
            self.assertEqual(len(block), 1, f"segment {segment}")
            blocks |= block
        self.assertEqual(blocks, {0, 1, 2})

    def test_committed_fixtures_match_their_generator(self):
        with tempfile.TemporaryDirectory() as folder:
            subprocess.run([sys.executable, str(FIXTURES / "generate.py"), folder], check=True)
            for made in Path(folder).rglob("*.csv"):
                committed = FIXTURES / made.relative_to(folder)
                self.assertEqual(made.read_text(), committed.read_text(), made.name)

    def test_rerun_without_segments_clears_old_segment_files(self):
        with tempfile.TemporaryDirectory() as folder:
            for name in ("segments.csv", "segment_scores.csv"):
                (Path(folder) / name).write_text("stale")
            with contextlib.redirect_stdout(io.StringIO()):
                odi.main([str(FIXTURES / "noise.csv"), "--out", folder,
                          "--nulls", "99", "--bootstrap", "50"])
            self.assertFalse((Path(folder) / "segments.csv").exists())
            self.assertFalse((Path(folder) / "segment_scores.csv").exists())

    def test_bad_input_exits_2(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.csv"
            path.write_text("respondent_id,a_imp,a_sat\nr1,4,2\n")
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(odi.main([str(path), "--out", folder]), 2)


if __name__ == "__main__":
    unittest.main()

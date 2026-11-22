# ODI segmentation gate: measured error rates

Run 2026-11-21 with [`odi_calibration.py`](./odi_calibration.py): 50
synthetic surveys per row, 99 draws per null and 50 bootstrap rounds (the
command's defaults are 199 and 100), Python 3.14, on seeds the gate was
not developed on. Unless a row says otherwise, N = 180, 24 outcomes, and
the factor count comes from parallel analysis.

```bash
.venv/bin/python evals/odi_calibration.py 50
```

## Summary

- **No segments in the data:** the full gate reported segments in 5 of
  1,150 surveys (0.4%): 2 of 600 with the automatic factor count, 3 of 550
  with the count forced. The worst row is a ceiling effect with 3 factors
  forced, 3 of 50.
- **Pure Gaussian noise:** 0 of 300. The old rule (silhouette > 0.25 and
  every segment at least 10%) passed 50, 50 and 41 of 50 at 1, 2 and 3
  factors.
- **Segments in the data:** found with the right k in every survey from a
  0.7-point shift upward at N = 180. At 0.5 points it finds them in 2 of 50
  at N = 180 and in 50 of 50 at N = 600, where recovered membership is
  rough (ARI 0.57).

## Results

The first four numeric columns count surveys reported as segmented. In a
`none` row every one of those is a false positive. "Shift" is how far a
segment's importance rises, and its satisfaction falls, on its own
outcomes. ARI is agreement with the planted membership (1 is exact).

| scenario | old rule | response null alone | single-peak null alone | full gate | right k | median ARI |
|---|---|---|---|---|---|---|
| none: Gaussian noise, 1 factors | 50/50 | 0/50 | 0/50 | 0/50 | - | - |
| none: Gaussian noise, 2 factors | 50/50 | 1/50 | 0/50 | 0/50 | - | - |
| none: Gaussian noise, 3 factors | 41/50 | 3/50 | 0/50 | 0/50 | - | - |
| none: Gaussian noise, 4 factors | 0/50 | 1/50 | 1/50 | 0/50 | - | - |
| none: Gaussian noise, 6 factors | 0/50 | 2/50 | 1/50 | 0/50 | - | - |
| none: Gaussian noise, 8 factors | 0/50 | 6/50 | 0/50 | 0/50 | - | - |
| none: rating noise | 50/50 | 3/50 | 1/50 | 0/50 | - | - |
| none: rating noise, 100 outcomes | 49/50 | 1/50 | 2/50 | 0/50 | - | - |
| none: rating noise, N=600 | 50/50 | 4/50 | 1/50 | 0/50 | - | - |
| none: 3 correlated need factors | 46/50 | 6/50 | 0/50 | 0/50 | - | - |
| none: ceiling effect | 50/50 | 2/50 | 44/50 | 1/50 | - | - |
| none: ceiling effect, 6 outcomes | 50/50 | 0/50 | 46/50 | 0/50 | - | - |
| none: 1 skewed trait | 50/50 | 27/50 | 0/50 | 0/50 | - | - |
| none: 1 skewed trait, 2 factors forced | 50/50 | 43/50 | 1/50 | 0/50 | - | - |
| none: 1 skewed trait, 3 factors forced | 50/50 | 45/50 | 3/50 | 0/50 | - | - |
| none: 1 skewed trait, 6 factors forced | 0/50 | 49/50 | 11/50 | 0/50 | - | - |
| none: 1 skewed trait, N=600, 3 factors forced | 50/50 | 50/50 | 9/50 | 0/50 | - | - |
| none: ceiling effect, 3 factors forced | 50/50 | 3/50 | 49/50 | 3/50 | - | - |
| none: 2 skewed traits | 50/50 | 44/50 | 0/50 | 0/50 | - | - |
| none: 3 correlated skewed traits | 49/50 | 25/50 | 1/50 | 1/50 | - | - |
| none: 1 skewed trait, N=600 | 50/50 | 49/50 | 0/50 | 0/50 | - | - |
| none: 3 skewed traits | 50/50 | 45/50 | 3/50 | 0/50 | - | - |
| none: response style | 35/50 | 6/50 | 3/50 | 0/50 | - | - |
| 3 segments, shift 0.5 points | 49/50 | 34/50 | 14/50 | 2/50 | 2/50 | 0.57 |
| 3 segments, shift 0.7 points | 50/50 | 50/50 | 50/50 | 50/50 | 50/50 | 0.82 |
| 3 segments, shift 0.9 points | 50/50 | 50/50 | 50/50 | 50/50 | 50/50 | 0.95 |
| 3 segments, shift 0.5 points, N=600 | 50/50 | 50/50 | 50/50 | 50/50 | 50/50 | 0.57 |
| 3 segments, shift 0.9 points, 4 factors forced | 50/50 | 50/50 | 50/50 | 50/50 | 50/50 | 0.93 |
| 2 segments, shift 0.9 points | 50/50 | 50/50 | 50/50 | 50/50 | 50/50 | 1.00 |
| 4 segments, shift 1.1 points | 50/50 | 50/50 | 50/50 | 50/50 | 50/50 | 0.96 |

## Limits

- 0 of 50 does not mean never: the 95% upper bound is about 6%. The
  scenarios are the failure modes we thought of, not every possible one.
- Each null alone fails badly somewhere: the response-shaped null on
  skewed traits, the single-peak null on ceiling effects. Don't drop one
  to gain power.
- The single-peak null runs on varimax and on principal axes. A first
  version used varimax only and passed 43 of 50 skewed one-trait surveys
  with 3 factors forced; those rows stay here as the regression check.
- Groups that answer almost identically on every outcome (nearly every
  rating the same within a group) can read as no valid segmentation,
  because the response-shaped null reproduces them.
- Everything here is simulated. The gate has not been validated on a
  fielded survey with known segments.

# Opportunity Analysis — Method Reference

*Phase 3 (Analyze & Act) of the [ODI process](./process-map.md): opportunity
scoring, needs-based segmentation, growth strategy, and solution-concept
evaluation. Score inputs are defined canonically in
[`survey-design.md`](./survey-design.md#score-conversion-canonical-definition).*

## The opportunity algorithm

```
Opportunity Score = Importance + max(Importance − Satisfaction, 0)
```

This weights importance twice relative to satisfaction — unmet *important*
needs matter far more than unmet trivial ones, and over-satisfaction
(satisfaction > importance) earns no credit.

**Worked example:**
```
Outcome: "Minimize the time it takes to locate needed materials"
  72% rated importance 4 or 5    → Importance   = 7.2
  38% rated satisfaction 4 or 5  → Satisfaction = 3.8
  Opportunity = 7.2 + max(7.2 − 3.8, 0) = 7.2 + 3.4 = 10.6
```

**Interpretation:**

| Score | Classification | Action |
|-------|----------------|--------|
| > 15 | Extreme opportunity | Must address — significant competitive advantage |
| 12–15 | High opportunity | Low-hanging fruit, strong ROI potential |
| 10–12 | Moderate opportunity | Worth addressing in broad markets |
| < 10 | Low opportunity | Unattractive — diminishing returns |

## The opportunity landscape

Plot every outcome on a 2D chart:
- **X-axis:** Satisfaction (0–10)
- **Y-axis:** Importance (0–10)
- Diagonal line (Importance = Satisfaction) as the "appropriately served"
  baseline; color-code by opportunity category; label the top 10–15 outcomes.

Three zones:
- **Upper-left** (high importance, low satisfaction): **underserved** — core
  innovation opportunities.
- **Lower-right** (low importance, high satisfaction): **overserved** —
  disruptive-innovation opportunities.
- **Diagonal** (importance ≈ satisfaction): **appropriately served** —
  maintain, don't invest.

## Analysis protocol

### Step 1 — Data validation and cleaning

Before any analysis:
```
[ ] Sample size meets minimum threshold (N ≥ 180)
[ ] No respondent completed the survey in under 5 minutes (speeders)
[ ] No respondent gave the same answer to every question (straight-liners)
[ ] Missing data below 10% per respondent
[ ] Response distributions not pathologically skewed
```
Document every cleaning action and its impact on sample size.

### Step 2 — Calculate opportunity scores

For each outcome: top-2-box % for importance and satisfaction → ÷ 10 → apply
the algorithm. **Spot-check at least 5 scores manually** before trusting the
batch computation.

### Step 3 — Rank and categorize

```
Rank | Outcome statement                  | Imp | Sat | Opp  | Category
-----|------------------------------------|-----|-----|------|----------
1    | Minimize the time it takes to...   | 8.4 | 3.1 | 13.7 | High
2    | Minimize the likelihood that...    | 7.9 | 3.5 | 12.3 | High
```

### Step 4 — Build the opportunity landscape
Per the spec above.

### Step 5 — Needs-based segmentation

Traditional segmentation (demographics, psychographics, behavior) fails to
explain *why* customers have different unmet needs. ODI segments on
**outcomes** — grouping customers who share patterns of unmet needs.

**5a. Prepare** — use importance AND satisfaction **gap scores**
(Importance − Satisfaction) per outcome; standardize (z-scores).

**5b. Factor analysis** — exploratory factor analysis (EFA, varimax) on
the gap scores; choose factor count by **parallel analysis** (keep factors
whose eigenvalue beats the 95th percentile of column-permuted data; Horn
1965); identify which outcomes load on each factor; **name each factor**
for the outcomes it represents. Don't use eigenvalue > 1, which keeps many
factors from pure noise. A different count may be set, but before seeing
the segmentation result, and it is reported.

**5c. Cluster analysis** — k-means on the factor scores, testing k = 2…8.
A k is a valid segmentation only if **all four** hold:

| Check | Rule | What it rules out |
|-------|------|-------------------|
| **Response-shaped null** | silhouette beats it, p ≤ 0.05 | Clusters made by the rating scale, ceiling effects, or correlation between outcomes |
| **Single-peak null** | silhouette beats it on both axis sets, p ≤ 0.05 | Clusters cut out of one skewed or heavy-tailed population |
| **Stability** | every segment's mean bootstrap Jaccard ≥ 0.75 (after Hennig 2007) | Segments that vanish when the sample changes |
| **Segment balance** | no segment < 10% of total | Segments too small to act on |

If no k passes, the result is **"no valid segmentation"**.

- *Why not a fixed silhouette cut.* k-means divides any cloud of points,
  and with few factors the pieces score well: one factor of pure noise
  gives silhouettes near 0.55. The question is whether the score is higher
  than one population would give (the idea behind SigClust, Liu et al.
  2008).
- *Response-shaped null.* Simulated respondents from one correlated
  population (a Gaussian copula) with each outcome's observed distribution
  and the observed correlations, refitted through the same factor analysis
  and k-means.
- *Single-peak null.* Each factor's scores resampled with just enough
  smoothing to leave one peak (Silverman 1981), then the same k-means.
  Done on the varimax axes and again on the principal axes of the scores;
  the worse p counts. With more factors than real traits, varimax splits
  one trait across several factors, and the first alone would pass it.
- *Why both.* Either alone passes data with no segments: the first on
  skewed traits, the second on ceiling effects. Plain permutation is not
  enough, because it also removes the correlations between outcomes.
- *Trying seven values of k.* Each p compares with the best k of every
  simulated dataset, so searching over k earns nothing.
- *Stability is not evidence by itself.* A bell curve cut in half is very
  stable; that is why the nulls are required too.
- *Choosing among passing k.* The one furthest above the weaker of its
  two nulls.
- *Limits.* The gate is conservative: at N = 180 faint or heavily
  overlapping segments will usually read as no valid segmentation, which
  means "none detected", not "everyone is alike". So can groups whose
  answers are nearly identical within each group. Measured error rates
  are in [`../../evals/odi-calibration.md`](../../evals/odi-calibration.md).

**5d. Validate** — these need a person and can only reject a k that
passed, never rescue one that failed:
- **Interpretability** — segments must have distinct, meaningful
  unmet-needs profiles (significance tests between segments on the outcomes
  that formed them are circular; don't offer them as evidence)
- **Reachability** — cross-tabulate segments with profiling variables;
  check segments are identifiable in the real world

When either can't be judged (no outcome wording, no profiling variables),
report a k that passed as **provisional** and say what is missing. A
strategy that rests on a provisional segment is conditional on that check.

### Step 6 — Profile each segment

```
Segment [N]: [Descriptive Name]
  Size: [% of total sample]

  Top 5 unmet needs:
    1. [Outcome] — Opp score: [X]
    ...

  Top 5 overserved needs:
    1. [Outcome] — Opp score: [X]
    ...

  Demographic profile:
    - [Key characteristics; current solutions; behavioral patterns]

  Strategic implication:
    [What this segment needs]
```

Demographics **describe** segments; they never **define** them.

### Step 7 — Formulate the growth strategy

| Strategy | When to use | Description |
|----------|-------------|-------------|
| **Differentiated** | Large underserved segment exists | Target a specific segment's unmet needs |
| **Dominant** | Many outcomes underserved across all segments | Address unmet needs shared by all |
| **Disruptive** | Large overserved segment exists | Strip features, reduce price, target the overserved |
| **Discrete** | Niche segment with extreme unmet needs | Specialized solution for one segment |
| **Sustaining** | Market mostly well-served | Incremental improvements to hold position |

With no valid segmentation, choose only from what the whole-sample scores
support. Differentiated and Discrete require a validated segment, and so
does any claim that a *segment* is overserved.

### Step 8 — Evaluate solution concepts (if provided)

For each concept:
1. Map which unmet outcomes it addresses.
2. **Concept opportunity coverage** = sum of opportunity scores of addressed
   outcomes.
3. **Segment fit** = % of the target segment's top unmet needs addressed.
4. Rank concepts by coverage and fit.

## Output package

1. **Executive summary** — market definition, sample size, outcomes analyzed,
   segments found (count + sizes), top 5 unmet needs overall, recommended
   strategy.
2. **Full opportunity score table** — every outcome, ranked.
3. **Opportunity landscape** — the labeled scatter plot.
4. **Segment analysis** — profile per segment, or "no valid segmentation"
   with the diagnostics and no profiles.
5. **Growth strategy recommendation** — with rationale tied to the data,
   specific outcomes to target, segments to prioritize.
6. **Technical appendix** — cleaning log (records removed and why), factor
   loadings and variance explained, cluster diagnostics (silhouette, both
   null p-values, stability and smallest segment for each k tested),
   methodology notes.

## Tooling

[`tools/odi/odi_analysis.py`](../../tools/odi/odi_analysis.py) runs steps
1–3 and 5a–5c and is the reference implementation of the gate; setup is in
the [README](../../README.md#running-the-odi-analysis). It reads
`<name>_imp` / `<name>_sat` column pairs and does not judge whether
distributions are sane, draw the landscape, name factors or segments,
profile on demographics, or pick a strategy. For the landscape and profile
plots add matplotlib.

## Quality checklist

- [ ] Data cleaning documented with rationale
- [ ] Opportunity scores spot-checked manually (≥ 5)
- [ ] Landscape plot clear and properly labeled
- [ ] Segmentation beats both nulls (p ≤ 0.05) and is stable (Jaccard ≥ 0.75),
      or reported as "no valid segmentation"
- [ ] Each segment has a distinct unmet-needs profile
- [ ] No segment < 10% of sample (commercial viability)
- [ ] Demographic profiles descriptive, not definitional
- [ ] Strategy recommendation supported by the data
- [ ] Assumptions and limitations documented

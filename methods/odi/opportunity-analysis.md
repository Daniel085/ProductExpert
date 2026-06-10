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

**5b. Factor analysis** — exploratory factor analysis (EFA) on the gap
scores; choose factor count via scree plot and eigenvalue > 1; identify which
outcomes load on each factor; **name each factor** for the outcomes it
represents.

**5c. Cluster analysis** — k-means on the factor scores, testing k = 2…8.
Evaluate each k on:
- **Silhouette score** — higher is better; require **> 0.25**
- **Segment balance** — no segment < 10% of total
- **Interpretability** — segments must have distinct, meaningful unmet-needs
  profiles

**5d. Validate** — cross-tabulate segments with profiling variables; verify
segments differ meaningfully on unmet needs; check segments are **reachable**
(identifiable in the real world).

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
4. **Segment analysis** — profile per segment.
5. **Growth strategy recommendation** — with rationale tied to the data,
   specific outcomes to target, segments to prioritize.
6. **Technical appendix** — cleaning log (records removed and why), factor
   loadings and variance explained, cluster diagnostics (silhouette scores
   and sizes for each k tested), methodology notes.

## Tooling

Preferred stack: **Python** — pandas, numpy, scipy, scikit-learn
(`sklearn.decomposition.FactorAnalysis` or the `factor_analyzer` library;
`sklearn.cluster.KMeans` + `sklearn.metrics.silhouette_score`), matplotlib /
seaborn for the landscape and segment profiles.

## Quality checklist

- [ ] Data cleaning documented with rationale
- [ ] Opportunity scores spot-checked manually (≥ 5)
- [ ] Landscape plot clear and properly labeled
- [ ] Segmentation statistically valid (silhouette > 0.25)
- [ ] Each segment has a distinct unmet-needs profile
- [ ] No segment < 10% of sample (commercial viability)
- [ ] Demographic profiles descriptive, not definitional
- [ ] Strategy recommendation supported by the data
- [ ] Assumptions and limitations documented

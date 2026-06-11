# Trustworthy Experiments — Method Reference

*Distilled from **"Trustworthy Online Controlled Experiments: A Practical
Guide to A/B Testing"** by **Ron Kohavi, Diane Tang & Ya Xu** (Cambridge
University Press, 2020) — the canonical text. See
[`../../CREDITS.md`](../../CREDITS.md).*

## Why controlled experiments

A controlled experiment (A/B test) is the most reliable way to establish
**causality** between a product change and a metric change — it's what
replaces the HiPPO (Highest Paid Person's Opinion) with evidence. But the
method only deserves trust when the experiment itself is trustworthy; most
of this doc is about earning that trust.

**Twyman's law** governs everything here: *any figure that looks interesting
or different is usually wrong.* Surprising results are usually bugs —
instrumentation errors, ratio mismatches, bot traffic — not breakthroughs.
Verify before celebrating.

---

## Design

### 1. Hypothesis

Falsifiable and specific, stated **before** any data is seen. The repo's
experiment format applies (see Wilkie's template,
`methods/customer-interviews/research-and-insight.md`):
*We believe that… / To verify that… / We will measure…* — with the decision
the result will drive named up front.

### 2. OEC — the Overall Evaluation Criterion

The single metric (or small weighted composite) the experiment is judged by.
A good OEC is:
- **Measurable within the experiment's timeframe**
- **Sensitive** enough to move on realistic changes
- **Causally believed to drive long-term value** — a short-term proxy for
  the long-term goal (e.g., sessions-per-user as a proxy for retention, not
  quarterly revenue, which barely moves in two weeks)

Deriving the OEC from the product's North Star / input metrics is the
metrics method's job (`methods/metrics/north-star.md`); the experiment
inherits it, not invents it.

### 3. Guardrail metrics

Two kinds, both mandatory:
- **Organizational guardrails** — things no experiment may degrade: latency,
  error rates, crashes, unsubscribes, revenue. Small latency regressions
  have repeatedly been shown to cause measurable revenue loss; a "winning"
  feature that adds 200ms can be a net loser.
- **Trust guardrails** — metrics that validate the experiment itself,
  chiefly the **sample ratio** (below).

### 4. Randomization unit

Usually the **user** (stable ID across sessions/devices where possible);
sometimes session or page. Rules:
- The unit must be **stable** for the experiment's duration.
- The unit must match the metric's denominator (user-level metric →
  user-level randomization), or variance computations break.
- **Interference check (SUTVA):** if units interact — marketplaces, social
  features, shared inventory — one unit's treatment can leak into another's
  outcome. Flag it; consider cluster/market-level randomization or accept
  stated bias.

### 5. MDE and practical significance

Decide **before launch**:
- **Practical significance boundary** — the smallest effect worth shipping
  given the costs. This is a product judgment, not a statistical one.
- **MDE (minimum detectable effect)** — the effect size the experiment is
  powered to find; set it at or below the practical boundary.

### 6. Sample size

Rule of thumb (80% power, α = 0.05, two-sided):

```
n per variant ≈ 16 · σ² / δ²
```
where δ is the MDE in absolute terms and σ² the metric's variance (for a
conversion rate p, σ² = p(1−p)).

Worked example: baseline conversion 5%, MDE = 0.25pp absolute (a 5%
relative lift) → σ² = 0.05·0.95 = 0.0475, δ² = 0.0025² = 6.25e-6 →
**n ≈ 121,600 per variant**. Small effects are expensive; this calculation,
done early, is what tells you whether an A/B test is even feasible at your
traffic (see "When not to A/B test").

### 7. Run length and ramp

- **Whole weeks** (1–2 minimum) — day-of-week effects are real.
- Watch for **novelty effects** (treatment wins early, fades) and **primacy
  effects** (treatment loses early, recovers as users relearn): plot the
  treatment effect by day before trusting it.
- **Ramp** deliberately (e.g., 1% → 5% → 25% → 50%) with guardrail checks at
  each stage — but analyze only data from a constant-allocation period;
  combining stages with different percentages invites **Simpson's paradox**.
- Run **A/A tests** periodically: same experience in both arms should show
  ~5% false-positive rate at α=0.05 and no SRM. If A/A fails, the platform —
  not the product — is broken.

### 8. Pre-registration

Written and frozen before launch:

```
EXPERIMENT PRE-REGISTRATION
Hypothesis (We believe that…):
Decision this informs:
OEC:                      Practical significance boundary:
Guardrails:               Randomization unit:
MDE:                      Sample size / variant:        Power/α:
Start date:               Planned end date (whole weeks):
Ramp plan:
Analysis plan (segments to check, methods):
```

Changing any of these after seeing data must be disclosed in the readout.

---

## Readout

**Order matters: trust checks first. No effect estimates until the
experiment passes them.**

### 1. Sample Ratio Mismatch (SRM)

If the design says 50/50, test whether the observed counts match
(chi-square goodness-of-fit). **If p < 0.001, the experiment is invalid —
stop and debug; do not interpret results.** Even a 50.2/49.8 split is a
fatal SRM at large N. Common causes: redirects that drop users
asymmetrically, bot filtering applied unevenly, triggering bugs, ramp-stage
data mixing.

### 2. Other trust checks

- A/A or pre-experiment balance on key covariates
- Bot/outlier handling symmetric across arms
- **Triggering/dilution:** analyze only users who could have been affected;
  including untriggered users dilutes the measured effect toward zero
- Instrumentation parity (are both arms logging identically?)
- Data pipeline freshness/completeness for the full window

### 3. The peeking problem

Classical fixed-horizon tests assume **one** look at the data. Checking
daily and stopping at the first p < 0.05 inflates the false-positive rate
severalfold. Either run to the pre-registered end, or use methods designed
for monitoring (sequential tests / always-valid p-values) — and say which.

### 4. Multiple comparisons

At α = 0.05, one in twenty metrics goes "significant" by chance. With 20
metrics and 10 segments, "significant" findings are guaranteed. Distinguish
the pre-registered primary analysis from exploratory slicing; correct
(e.g., Bonferroni) or explicitly downgrade exploratory hits to *hypotheses
for the next experiment*. **Segment-fishing for a subgroup where the
treatment "won" is p-hacking**, name it as such.

### 5. Estimate and decide

Report the **confidence interval**, not just the p-value (a p-value is
P(data this extreme | no effect) — it is *not* the probability the
treatment works). Then decide against the pre-registered practical
significance boundary:

| Result vs. boundary | Decision |
|---|---|
| CI entirely above the practical boundary | **Ship.** |
| CI entirely below zero | **Don't ship** (it's a measured loss — log the learning). |
| CI between zero and boundary (tight) | Statistically positive but not worth it — don't ship unless free. |
| CI wide / straddles boundary | **Underpowered** — extend, redesign, or accept and move on. Say "underpowered," not "trend toward significance." |

Check **guardrails before celebrating** the OEC. An OEC win with a latency
or unsubscribe regression is a trade-off decision, not a victory lap.

If the result is surprising in either direction: **Twyman's law.**
Re-verify instrumentation, re-run, or replicate before acting on it.

### 6. Readout document

```
EXPERIMENT READOUT — <name> — <dates>
Pre-registration: <link> (deviations, if any: …)
TRUST: SRM p = …  | A/A …  | triggering …  | bots …   → VALID / INVALID
OEC: control … treatment … Δ … [CI …]  vs practical boundary …
Guardrails: …
Segments (exploratory, labeled as such): …
Effect-by-day plot: novelty/primacy? …
DECISION: ship / don't ship / iterate / extend — rationale:
LEARNING (logged regardless of outcome):
```

### 7. Institutional memory

Every experiment — especially the losers — goes in the log: hypothesis,
design, result, decision, learning. Roughly a third of well-run experiments
move their metric positively; the rest are tuition, but only if recorded.
The cumulative log is also where you catch "we tested this in 2024 and it
lost" before re-spending a quarter on it.

---

## When NOT to A/B test

- **Traffic can't power the MDE** (the sample-size math says months): make
  fewer, bigger bets and evaluate with qualitative methods + before/after
  with stated caveats — a hopeless test is worse than no test.
- **You can't randomize** (pricing fairness, network interference,
  one-shot launches): consider quasi-experiments (difference-in-differences,
  interrupted time series), stated plainly as weaker evidence.
- **The question is "why," not "whether":** that's discovery
  (`methods/customer-interviews/`), not experimentation.
- **Ethical lines:** no experimenting on users in ways they'd find
  unacceptable if described to them plainly.

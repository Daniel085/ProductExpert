# Methodology Evaluation — Outcome-Driven Innovation (ODI)

**Methodology:** Outcome-Driven Innovation — Tony Ulwick / Strategyn's
quantitative operationalization of Jobs-to-be-Done: the market as *job
executor + job*, the Universal Job Map (Bettencourt & Ulwick), desired
outcome statements, the importance × satisfaction survey, the opportunity
algorithm, needs-based segmentation, and the growth-strategy framework.
**Scope:** as distilled in `methods/odi/` (ported from
Product-Discovery-ODI) together with Ulwick's published canon. The
qualitative JTBD school is evaluated separately in [`jtbd.md`](./jtbd.md).
**Rubric:** [`rubric.md`](./rubric.md). **Recorded:** 2026-09-18.

---

## Summary

**Totals: 14 Fully supported / 10 Some support / 1 Not well.**

| Cluster | Profile | Read |
|---------|---------|------|
| **1.x Problem / framing** | 8 Fully / 2 Some / 0 Not | the most complete problem method here |
| **2.x Solution** | 2 Fully / 4 Some / 1 Not | evaluates solutions rigorously; generates none |
| **3.x Market / commercial** | 4 Fully / 4 Some / 0 Not | quantified market decisions, minus revenue |

**The only method of the four with a single Not well, and the only one
Fully supported on quantification (1.6, 1.7), decision gates on the
problem (1.10), KPIs (3.7), and non-user situations (1.9).** Its
*Some*s cluster in two places: where ODI **delegates to the team**
(ideation 2.1, the solution set 2.2, solution design 2.5), and where its
machinery carries a **price** — 3.4 (it validates before building, but
neither simply nor cheaply: 5–8 interviews, 100+ statements, curation, a
fielded survey of 180–600) and 1.8 (Phase 1 frames any job; Phases 2–3
need a surveyable population — a twelve-account partner market cannot
reach N ≥ 180). Its one Not well, effort (2.6), is shared with every
method evaluated.

**Rubric-fit note.** This rubric rewards quantification and explicit
gates, which is precisely what ODI was designed to deliver — so part of
its dominance is the rubric's preference. Its real costs (time, money, and
a population requirement) land on only two criteria. Read the score as
**"strongest when you can afford it and have the population."**

**Verdict for a product discovery process.** The **quantification and
decision spine**: run it *after* qualitative validation has confirmed the
job is real, on a market large enough to survey, when the question is
*which needs to prioritize, for whom, with what strategy*. It does not
ideate, design, estimate effort, or size revenue.

**In ProductExpert terms:** the four `odi-*` agents. `metrics`
complements 3.7 (ODI's KPI is survey-based and lagging; product analytics
supply the leading signals between surveys); the effort gap (2.6) is
uncovered anywhere in the system.

---

## Batch 1 — The problem

| # | Criterion | Rating |
|---|-----------|--------|
| 1.1 | Identifies people affected | **Fully supported** |
| 1.2 | Identifies the problem | **Fully supported** |
| 1.3 | Challenges the problem (XY) | **Fully supported** |
| 1.4 | Challenges our understanding (bias) | **Fully supported** |
| 1.5 | Expresses problem for stakeholders | **Some support** |
| 1.6 | Quantifies problem importance | **Fully supported** |
| 1.7 | Quantifies confidence in analysis | **Fully supported** |
| 1.8 | Applies across scenarios (regulatory/partner/VOIP) | **Some support** |
| 1.9 | Handles non-user-based situations | **Fully supported** |
| 1.10 | Clear go/no-go criteria (problem) | **Fully supported** |

**1.1 — Fully supported.** The market is defined as *job executor + core
functional job*; the needs framework also names the buyer (financial
outcomes) and the consumption-chain roles; segments are later defined by
unmet needs rather than demographics. *Caveat:* one executor per market
definition — two-sided situations need the dual-job framing the repo's
partner mode adds.

**1.2 — Fully supported.** The problem becomes 100+ desired outcome
statements across all eight job steps, coverage-audited per step — the
most explicit and complete problem definition of the four. *Caveat:*
heavy; the Outcome Editor exists because raw capture is messy.

**1.3 — Fully supported.** Solution-agnostic framing is enforced
structurally: a market defined by product ("MP3 player users") is rejected;
statements naming a UI element or technology are rewritten; the job map
forces the underlying job. XY problems are designed out — and importance
scores then challenge whether each outcome matters at all. *Caveat:* the
chosen job is taken as given; pick the wrong job and ODI quantifies the
wrong thing beautifully.

**1.4 — Fully supported.** Opinion is replaced by measurement:
importance/satisfaction from N ≥ 180, segmentation on needs rather than
demographics, silhouette-validated clusters, read-back confirmation of
each statement with the customer. *Weak spot:* capture is still
interpreted by the interviewer, and the survey can only test outcomes
someone thought to capture.

**1.5 — Some support.** The opportunity landscape and ranked table are
highly legible to analytical stakeholders; the underlying problem
definition (80–120 statements) is not, and there is no narrative
artifact. It communicates to data-minded rooms, not story-minded ones.

**1.6 — Fully supported.** The core of the method: importance and
satisfaction scores, the opportunity algorithm
(`Importance + max(Importance − Satisfaction, 0)`), and named thresholds
(> 15 extreme, 12–15 high, 10–12 moderate, < 10 unattractive). The
WIBNI → committed axis is measured directly as importance × unmet-ness.
*Caveat:* contractual commitment is a constraint, not a need, and is the
one flavor of "importance" it doesn't capture.

**1.7 — Fully supported.** Confidence is statistical: sample sizing
(180–600; ≥ 3× the statement count), data-quality gates (< 10% missing,
speeders, straight-liners), silhouette > 0.25 for segments, manual
spot-checks. *Caveat:* completeness of the outcome list is judged by
saturation, not statistics.

**1.8 — Some support.** Jobs are domain-agnostic and need not be
experiential — the repo's partner mode carries a telephony integrator's
job as Job B — so regulatory and partner jobs frame naturally in Phase 1.
Phases 2–3 require a surveyable population; niche B2B and partner markets
cannot reach N ≥ 180, so the quantitative half does not apply there.
Universal framing, conditional quantification.

**1.9 — Fully supported.** The unit of analysis is a job, not a user
experience — buyers (financial outcomes), integrators, and maintainers
(consumption chain) are first-class in the needs framework rather than
workarounds. *Caveat:* measurement still needs human respondents who own
the job; a purely system-to-system situation is framed through the role
accountable for it.

**1.10 — Fully supported.** Numeric decision criteria on the problem:
opportunity thresholds, per-step coverage minimums, sample gates — which
outcomes are worth pursuing and which aren't. *Caveat:* criteria for the
problem, not a business go/no-go; cost and revenue are absent.

---

## Batch 2 — The solution

| # | Criterion | Rating |
|---|-----------|--------|
| 2.1 | Explore multiple theoretical options | **Some support** |
| 2.2 | Plausible solution set within business priorities | **Some support** |
| 2.3 | Clear set of outcomes the solution delivers | **Fully supported** |
| 2.4 | Clear value proposition | **Fully supported** |
| 2.5 | Applies across scenarios (UX → detailed VOIP flows) | **Some support** |
| 2.6 | Identifies effort involved | **Not well** |
| 2.7 | Go/no-go criteria (solution) | **Some support** |

**2.1 — Some support.** Step 12 aims concept generation at the
high-opportunity outcomes — a precise target — but supplies no divergence
method; ideation happens outside ODI.

**2.2 — Some support.** A provided concept set is evaluated rigorously
against business strategy (differentiated / dominant / disruptive /
discrete / sustaining) and segment fit; the set itself is not generated.

**2.3 — Fully supported.** Outcomes are its native currency: the targeted
outcome statements *are* the outcomes the solution must deliver, and
concept coverage measures which of them it addresses.

**2.4 — Fully supported.** Opportunity scores quantify why the outcomes
matter (importance × unmet), per segment; Ulwick's practice extends into
outcome-based value propositions and messaging. *Caveat:* no willingness
to pay — excluded from the survey by design.

**2.5 — Some support.** Solution-agnostic by construction — it specifies
*what* outcomes, never *how* — so it evaluates any concept, UX or
technical, and designs at no level.

**2.6 — Not well.** Concept evaluation is coverage and segment fit only;
no effort, cost, or feasibility estimation.

**2.7 — Some support.** Quantified comparative criteria (opportunity
coverage, segment fit) rank concepts; an absolute go/no-go still needs the
cost side it lacks.

---

## Batch 3 — The market

| # | Criterion | Rating |
|---|-----------|--------|
| 3.1 | Resolves conflicting requirements | **Fully supported** |
| 3.2 | Picks the best solution for the market | **Fully supported** |
| 3.3 | Sizes the opportunity (revenue + constraints) | **Some support** |
| 3.4 | Cheap ways to validate assumptions pre-build | **Some support** |
| 3.5 | Identifies market positioning | **Some support** |
| 3.6 | Applies across scenarios (SaaS → on-prem) | **Fully supported** |
| 3.7 | Identifies success KPIs | **Fully supported** |
| 3.8 | Go/no-go given market positioning | **Some support** |

**3.1 — Fully supported.** Conflicting customer needs are resolved by
data: opportunity scores rank outcomes, and needs-based segments turn
"customers disagree" into "these are distinct segments — here is the
strategy for each." *Scope caveat:* customer-need conflicts only;
stakeholder, regulatory, and technical-constraint conflicts are outside
it.

**3.2 — Fully supported.** Segment strategy plus concept evaluation is a
clear, quantified way to pick the concept that fits the (segmented)
market — the strongest of the four here.

**3.3 — Some support.** Quantifies opportunity magnitude (scores) and
segment share of the sample, not revenue; no population sizing, pricing,
or constraint analysis.

**3.4 — Some support.** It validates before building — that is its
purpose — but simple and cheap it is not: 5–8 interviews, 100+
statements, curation, a fielded survey of 180–600 respondents, and
statistical analysis; typically weeks and real money. Passes "validate,"
fails "cheap."

**3.5 — Some support.** The growth strategy and each segment's top unmet
outcomes are strong positioning inputs (what to say, to whom), and
Strategyn uses them for value propositions; there is no
competitive-alternatives or category framing.

**3.6 — Fully supported.** Consumption-chain jobs (set up, maintain,
dispose) and financial outcomes (total cost of ownership) capture exactly
the needs that differ between SaaS and on-prem, so the trade-off surfaces
in data rather than being ignored. *Caveat:* framed as customer outcomes,
not delivery economics.

**3.7 — Fully supported.** Success is measurable by construction:
satisfaction lift on the outcomes you targeted, re-surveyed — the one
method with KPIs built in. *Caveat:* survey-based and lagging; pair with
product analytics for leading signals.

**3.8 — Some support.** Thresholds, segment viability (no segment < 10%),
and strategy fit are real decision criteria — but a positioning-level
go/no-go also needs the revenue and competitive inputs ODI doesn't
produce.

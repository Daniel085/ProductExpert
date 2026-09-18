# Methodology Evaluation — Jobs-to-be-Done (qualitative school)

**Methodology:** Jobs-to-be-Done as theory and qualitative practice —
Clayton Christensen's theory (*The Innovator's Solution*, *Competing
Against Luck*: a job is the progress a person seeks in a circumstance;
the milkshake), Bob Moesta / the Re-Wired Group's practice (switch and
timeline interviews; the four forces of progress — push, pull, anxiety,
habit; "what did they fire to hire this?"), Alan Klement / Intercom's job
stories, and Jim Kalbach's *Jobs to be Done Playbook*.
**Scope note:** ODI is Tony Ulwick's *quantitative* operationalization of
the same theory and is evaluated separately in [`odi.md`](./odi.md). Here
"JTBD" means the theory plus its qualitative toolkit, as distilled in
`methods/jtbd/` (job stories; requirements as hypotheses).
**Rubric:** [`rubric.md`](./rubric.md). **Recorded:** 2026-09-18.

---

## Summary

**Totals: 8 Fully supported / 10 Some support / 7 Not well.**

| Cluster | Profile | Read |
|---------|---------|------|
| **1.x Problem / framing** | 5 Fully / 2 Some / 3 Not | superb framing; nothing measured |
| **2.x Solution** | 1 Fully / 4 Some / 2 Not | explains value; doesn't generate or gate |
| **3.x Market / commercial** | 2 Fully / 4 Some / 2 Not | positioning is native; KPIs and gates are not |

**A reframing and positioning method.** Its *Fully supported* criteria:
the problem as progress-in-a-circumstance (1.2), XY-proofing through the
job (1.3 — with Design Thinking, the best reframer of the four),
stakeholder-legible framing (1.5), breadth (1.8) and **non-user
situations** (1.9) — because the unit is a job, not a user — the value
proposition (2.4), **positioning** (3.5 — the only method Fully supported
there), and the SaaS/on-prem trade-off via the forces (3.6). Its holes
are the qualitative-school holes: nothing quantified (1.6, 1.7), no gates
(1.10, 2.7, 3.8), no effort (2.6), no KPIs (3.7) — every one of which ODI
exists to supply. **The complementary shape with ODI is the main
finding: JTBD frames and positions; ODI measures and gates.**

**Verdict for a product discovery process.** Use it to frame (jobs, job
stories), to find the real competitive set (what gets fired), and for
positioning and messaging. Hand the framed job to ODI for quantification,
and borrow *Talking to Humans*' discipline for bias control in the
interviews themselves.

**In ProductExpert terms:** `methods/jtbd/` (job stories;
requirements-as-hypotheses), read by `customer-interviews`,
`odi-interviewer`, and `prfaq`. **Not yet distilled:** the switch/timeline
interview and the four forces — the qualitative JTBD tools that earn this
method its 1.3, 3.5, and 3.6 scores. The README roadmap's "JTBD — covered
by the ODI family" is therefore only half right; see
[`comparison.md`](./comparison.md).

---

## Batch 1 — The problem

| # | Criterion | Rating |
|---|-----------|--------|
| 1.1 | Identifies people affected | **Some support** |
| 1.2 | Identifies the problem | **Fully supported** |
| 1.3 | Challenges the problem (XY) | **Fully supported** |
| 1.4 | Challenges our understanding (bias) | **Some support** |
| 1.5 | Expresses problem for stakeholders | **Fully supported** |
| 1.6 | Quantifies problem importance | **Not well** |
| 1.7 | Quantifies confidence in analysis | **Not well** |
| 1.8 | Applies across scenarios (regulatory/partner/VOIP) | **Fully supported** |
| 1.9 | Handles non-user-based situations | **Fully supported** |
| 1.10 | Clear go/no-go criteria (problem) | **Not well** |

**1.1 — Some support.** JTBD replaces personas with circumstances — "the
job is the unit" — which predicts behavior better but identifies
*situations* more clearly than *people*: the milkshake buyer is "the
morning commuter," a circumstance, and who else is affected is not
enumerated. Situation-first is a strength for prediction and a weakness
for stakeholder mapping.

**1.2 — Fully supported.** The problem is the progress a person is trying
to make in a circumstance — functional, emotional, and social — and a job
story states it in one sentence: situation, motivation, outcome. Explicit
and portable.

**1.3 — Fully supported.** Reframing is JTBD's founding act: "nobody wants
a quarter-inch drill," the milkshake, "what did you fire to hire this?";
job stories mechanically strip the solution out of the story; the switch
timeline traces the ask back to its first thought. With Design Thinking,
the best XY-resolver of the four.

**1.4 — Some support.** Switch interviews are anchored in real past
decisions (behavior, not opinion) and the four forces surface non-obvious
causes — genuine bias controls. But the work is small-N and interpretive,
and the theory is elastic: almost anything can be rationalized as "a job,"
so confirmation bias in the framing itself is uncontrolled.

**1.5 — Fully supported.** Job stories, the hire/fire vocabulary, and the
forces diagram are among the most communicable artifacts in product
practice; the milkshake story is the canonical stakeholder explanation of
customer need.

**1.6 — Not well.** The qualitative school describes forces and jobs; it
does not measure importance. Quantification is exactly what Ulwick added
— see ODI.

**1.7 — Not well.** No sampling logic, confidence scoring, or statistical
validation.

**1.8 — Fully supported.** Jobs are domain-agnostic and not tied to
experience: partner jobs (the repo's dual-job framing is JTBD-derived),
regulatory jobs ("stay compliant with X"), and technical jobs ("deliver
telephony connectivity to my customers") frame naturally, and switch
interviews apply to any adoption decision, VOIP procurement included.
*Caveat:* it frames; it does not design the technical core.

**1.9 — Fully supported.** The unit is a job with a hirer, not a user with
an experience — buyers', integrators', and organizations' jobs are native.
*Caveat:* a job still needs someone who hires; pure system behavior is
framed through whoever is accountable for it.

**1.10 — Not well.** No decision criteria. The forces inform a judgment —
is push plus pull greater than anxiety plus habit? — but the school
offers no threshold or gate.

---

## Batch 2 — The solution

| # | Criterion | Rating |
|---|-----------|--------|
| 2.1 | Explore multiple theoretical options | **Some support** |
| 2.2 | Plausible solution set within business priorities | **Some support** |
| 2.3 | Clear set of outcomes the solution delivers | **Some support** |
| 2.4 | Clear value proposition | **Fully supported** |
| 2.5 | Applies across scenarios (UX → detailed VOIP flows) | **Some support** |
| 2.6 | Identifies effort involved | **Not well** |
| 2.7 | Go/no-go criteria (solution) | **Not well** |

**2.1 — Some support.** Redefining competition as "anything hired for the
job" naturally widens the solution space, and job stories are explicitly
meant to open a conversation about solution options — but there is no
divergence method.

**2.2 — Some support.** The four forces are an adoption-plausibility
filter — will a solution overcome habit and anxiety? — which screens
solutions on the customer side; nothing screens for business priorities.

**2.3 — Some support.** The "so I can" outcome and the progress sought are
explicit but qualitative; ODI's structured outcome statements are the
quantified version.

**2.4 — Fully supported.** The value proposition is built in: the progress
sought, the emotional and social jobs, and the fired alternative together
say why the outcome matters *and against what*. *Caveat:* no willingness
to pay.

**2.5 — Some support.** Frames at any level — UX jobs, technical jobs —
and designs at none.

**2.6 — Not well.** Effort is outside the method.

**2.7 — Not well.** The forces give a lens for judging adoption; they
provide no criteria, thresholds, or test step.

---

## Batch 3 — The market

| # | Criterion | Rating |
|---|-----------|--------|
| 3.1 | Resolves conflicting requirements | **Some support** |
| 3.2 | Picks the best solution for the market | **Some support** |
| 3.3 | Sizes the opportunity (revenue + constraints) | **Some support** |
| 3.4 | Cheap ways to validate assumptions pre-build | **Some support** |
| 3.5 | Identifies market positioning | **Fully supported** |
| 3.6 | Applies across scenarios (SaaS → on-prem) | **Fully supported** |
| 3.7 | Identifies success KPIs | **Not well** |
| 3.8 | Go/no-go given market positioning | **Not well** |

**3.1 — Some support.** "Integrate around the job": the job arbitrates
(does this serve the progress sought?), and functional-vs-emotional job
tensions are surfaced. No method for stakeholder or constraint conflicts.

**3.2 — Some support.** The job defines the market, and a solution is
judged by whether it beats the fired alternative on the forces — a
qualitative market-fit judgment, with no comparison mechanism.

**3.3 — Some support.** Christensen sizes markets by job incidence — how
many people, how often, in that circumstance — rather than by product
category. A sizing *logic* the qualitative school states but does not
quantify.

**3.4 — Some support.** Switch interviews with a handful of recent
switchers are cheap and fast at validating that the job and the forces
are real; there is no prototype or assumption-testing loop for solutions.

**3.5 — Fully supported.** Positioning is a native JTBD use: position
against what gets fired, around the progress sought, for the
circumstance; Christensen's "purpose brand" is a brand that becomes
synonymous with the job. The only method of the four Fully supported
here. *Caveat:* qualitative; no message testing.

**3.6 — Fully supported.** The forces model is precisely how SaaS-vs-on-
prem adoption dynamics get analyzed — anxiety (data residency, lock-in)
and habit (existing on-prem operations) against push and pull. *Caveat:*
adoption dynamics, not delivery economics.

**3.7 — Not well.** Success is "progress made"; no KPI method.

**3.8 — Not well.** No gate.

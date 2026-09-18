# Methodology Comparison — Design Thinking · Talking to Humans · ODI · JTBD

*All four evaluated against the same [25-criterion rubric](./rubric.md).
Individual evaluations: [Design Thinking](./design-thinking.md) ·
[Talking to Humans](./talking-to-humans.md) · [ODI](./odi.md) ·
[JTBD](./jtbd.md). Recorded 2026-09-18.*

**Legend:** ● Fully supported · ◐ Some support · ○ Not well.
**Reach for** = the method(s) Fully supported on that criterion; "—" means
none is.

## The matrix

| # | Criterion | DT | TtH | ODI | JTBD | Reach for |
|---|-----------|:--:|:---:|:---:|:----:|-----------|
| 1.1 | Identifies people affected | ● | ● | ● | ◐ | DT, TtH, ODI |
| 1.2 | Identifies the problem | ● | ● | ● | ● | any |
| 1.3 | Challenges the problem (XY) | ● | ◐ | ● | ● | DT, JTBD, ODI |
| 1.4 | Challenges our understanding (bias) | ◐ | ● | ● | ◐ | TtH (craft), ODI (statistics) |
| 1.5 | Expresses problem for stakeholders | ● | ◐ | ◐ | ● | DT, JTBD |
| 1.6 | Quantifies problem importance | ○ | ◐ | ● | ○ | ODI |
| 1.7 | Quantifies confidence | ○ | ◐ | ● | ○ | ODI |
| 1.8 | Breadth: regulatory / partner / VOIP | ◐ | ◐ | ◐ | ● | JTBD |
| 1.9 | Non-user-based situations | ○ | ◐ | ● | ● | ODI, JTBD |
| 1.10 | Go/no-go on the problem | ○ | ◐ | ● | ○ | ODI |
| 2.1 | Explore multiple options | ● | ○ | ◐ | ◐ | DT |
| 2.2 | Plausible set within business priorities | ◐ | ◐ | ◐ | ◐ | — |
| 2.3 | Outcomes the solution delivers | ◐ | ◐ | ● | ◐ | ODI |
| 2.4 | Value proposition | ◐ | ◐ | ● | ● | ODI, JTBD |
| 2.5 | Breadth: UX → detailed VOIP flows | ◐ | ◐ | ◐ | ◐ | — |
| 2.6 | Effort involved | ○ | ○ | ○ | ○ | — (none; see below) |
| 2.7 | Go/no-go on the solution | ○ | ◐ | ◐ | ○ | — |
| 3.1 | Resolves conflicting requirements | ◐ | ◐ | ● | ◐ | ODI (customer needs only) |
| 3.2 | Best solution for the market | ◐ | ◐ | ● | ◐ | ODI |
| 3.3 | Opportunity size / revenue | ○ | ◐ | ◐ | ◐ | — |
| 3.4 | Cheap validation before building | ● | ● | ◐ | ◐ | DT, TtH |
| 3.5 | Market positioning | ○ | ○ | ◐ | ● | JTBD |
| 3.6 | Breadth: SaaS → on-prem | ◐ | ◐ | ● | ● | ODI, JTBD |
| 3.7 | Success KPIs | ○ | ○ | ● | ○ | ODI |
| 3.8 | Go/no-go given positioning | ○ | ○ | ◐ | ○ | — |

## Totals and gradients

| Method | Fully / Some / Not | Problem (1.x) | Solution (2.x) | Market (3.x) | Shape |
|--------|:------------------:|:-------------:|:--------------:|:------------:|-------|
| **Design Thinking** | 6 / 9 / 10 | 4 / 2 / 4 | 1 / 4 / 2 | 1 / 3 / 4 | peaks on framing and ideation; holes on numbers, gates, non-human |
| **Talking to Humans** | 4 / 16 / 5 | 3 / 7 / 0 | 0 / 5 / 2 | 1 / 4 / 3 | few peaks, few holes — a validation spine |
| **ODI** | 14 / 10 / 1 | 8 / 2 / 0 | 2 / 4 / 1 | 4 / 4 / 0 | quantification and gates; costly to run |
| **JTBD (qualitative)** | 8 / 10 / 7 | 5 / 2 / 3 | 1 / 4 / 2 | 2 / 4 / 2 | reframing and positioning; nothing measured |

## Findings

**1. They are complements, not rivals.** The union of their *Fully
supported* criteria covers **19 of 25**. Each owns a different slice:
Design Thinking owns divergence (2.1) and shares cheap validation (3.4);
Talking to Humans owns bias-proof craft (1.4) and the cheapest validation;
ODI owns every quantification and gate criterion on the problem side
(1.6, 1.7, 1.10) plus KPIs (3.7), market selection (3.2), and
customer-need conflict resolution (3.1); JTBD owns positioning (3.5) and
breadth (1.8), and shares non-user situations (1.9) with ODI because both
take the *job*, not the user, as the unit.

**2. Six criteria no method covers Fully — and they form one seam.**
2.2 (plausible set within business priorities), 2.5 (solution-side
breadth), **2.6 (effort — Not well for all four)**, 2.7 (solution
go/no-go), 3.3 (revenue), 3.8 (positioning go/no-go). Every one sits at
the boundary between *discovery* and the *business case*: effort,
revenue, and the decision to commit. Discovery methodologies stop at
understanding; none of them cost, price, or commit. In ProductExpert that
seam is exactly where the define–test–measure layer lives — `prfaq`'s
internal FAQs (economics, feasibility, what we'd need to believe),
`experimentation`'s pre-registered decision boundary, `metrics` — and
where the roadmap's pricing and strategy candidates point. **Effort (2.6)
remains uncovered by anything in the system**, and is arguably an
engineering/delivery concern rather than a discovery one; that is a
decision to make explicitly, not by omission.

**3. The rubric favors quantification and gates.** Ten of the 25 criteria
ask for measurement, criteria, or thresholds, which is what ODI was built
for — so ODI's 14 Fullys partly reflect the rubric's preference. ODI's
real costs land on only two criteria: time and money on 3.4, and the
N ≥ 180 population requirement on 1.8. For a twelve-account partner
market, ODI's Phase 1 (job map, outcome statements) applies and Phases
2–3 do not — read its column with that in mind.

**4. Natural pairings.** *Talking to Humans → ODI*: bias-proof qualitative
validation feeding quantification (the repo's Track 1 → Track 2 bridge).
*Design Thinking or JTBD → ODI*: frame the job, then measure it. *JTBD →
positioning*: JTBD gets a positioning exercise halfway (the fired
alternative, the progress, the circumstance); a dedicated positioning
method (Dunford — on the roadmap) finishes it. *Design Thinking → Talking
to Humans*: diverge, then validate — which is the `ideation` →
`customer-interviews` handoff.

**5. What this says about ProductExpert's architecture.** The system is,
in effect, an assembly of these four by their strengths: `ideation`
carries Design Thinking's divergence and framing; `customer-interviews` is
Talking to Humans; `methods/jtbd/` carries JTBD's framing; the `odi-*`
pipeline is ODI; the define–test–measure layer covers the seam in finding
2. The evaluation surfaces four gaps to act on:

- **Qualitative JTBD tools are missing.** The switch/timeline interview and
  the four forces — which earn JTBD its 1.3, 3.5, and 3.6 — are not
  distilled anywhere. The roadmap's "JTBD — covered by the ODI family"
  is half right: the *quantitative* half is covered. Candidate: add
  `methods/jtbd/switch-interviews.md` and fold the forces into the
  `customer-interviews` question bank.
- **Effort (2.6)** is covered by nothing; decide whether it is in scope.
- **Conflict resolution beyond customer needs (3.1)** — stakeholder,
  regulatory, technical — is still open; ODI resolves only the
  customer-need dimension.
- **Positioning (3.5)** is confirmed as the highest-value commercial
  addition: JTBD provides the inputs; nothing in the system produces a
  positioning.

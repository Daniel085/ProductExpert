# Methodology Evaluation — Design Thinking (Stanford d.school)

**Methodology:** Design Thinking as codified by the Stanford d.school — the
five modes (*Empathize · Define · Ideate · Prototype · Test*) and its
published method assets: *An Introduction to Design Thinking: Process
Guide* and the *Bootcamp Bootleg* / *Design Thinking Bootleg* method cards
(POV Madlib, How Might We, Why–How Laddering, Empathy Map, Saturate &
Group, Extreme Users, Assume a Beginner's Mindset, the Four Categories
selection method, I Like / I Wish / What If, and others).
**Rubric:** [`rubric.md`](./rubric.md) — 25 criteria, scale *Not well /
Some support / Fully supported*.
**Provenance and limits:** scored from the published d.school framework
and its public method assets, not from a live asset library. No d.school
material is reproduced here. Each criterion carries one label;
conditionals are stated in the rationale. Recorded 2026-09-18 from the
ProductExpert working session in which the evaluation was conducted.

---

## Summary

**Totals: 6 Fully supported / 9 Some support / 10 Not well.** The gradient
is the real finding:

| Cluster | Profile | Read |
|---------|---------|------|
| **1.x Problem / framing** | 4 Fully / 2 Some / 4 Not | Design Thinking's home turf |
| **2.x Solution** | 1 Fully / 4 Some / 2 Not | partial, desirability-flavored |
| **3.x Market / commercial** | 1 Fully / 3 Some / 4 Not | furthest from its core |

**Three structural gaps recur in every batch** — fault lines of the method,
not incidental misses:

1. **Quantification** → Not well *every time* (1.6, 1.7, 3.3, 3.7). It is
   qualitative by construction.
2. **Decision gates / go-no-go** → Not well *every time* (1.10, 2.7, 3.8).
   It is iterative and non-terminating by design.
3. **Away from the human** → Some/Not *every time* (1.8, 1.9, 2.5, 2.6,
   3.5, 3.6). It is human-centered, so it thins out on technical,
   commercial, and non-user dimensions.

**Its strengths cluster just as tightly:** empathy and problem
**reframing** (1.1–1.3, 1.5), divergent **ideation** (2.1), and **cheap
assumption validation** (3.4) — the front-of-funnel desirability engine
plus one mid-funnel validation asset.

**Verdict for a product discovery process.** Design Thinking is a superb
**desirability-and-framing front end** with one powerful
**validate-before-build** capability — and it is *not self-sufficient*. To
run gated discovery end to end it must be wrapped with a
**quantification** layer (opportunity sizing, KPIs), a **commercial** layer
(positioning, value proposition, market selection), and a **decision-gate**
layer at each stage. It is strongest for human-centered problems and
should not be relied on where the problem is non-human, where numbers are
required, or where a go/no-go is needed.

**In ProductExpert terms:** the ODI track and the `metrics` agent cover
quantification and KPIs; `experimentation` covers the rigorous end of 3.4
and supplies decision boundaries; `ideation` now owns the divergence
strength (2.1) as the system's front door; the roadmap's positioning
(Dunford) and pricing (Ramanujam & Tacke) candidates cover the commercial
layer. One criterion no agent covers yet — structured
**conflicting-requirements prioritization** (3.1) — is a gap in the system
itself, not just in this methodology.

---

## Batch 1 — The problem

| # | Criterion | Rating |
|---|-----------|--------|
| 1.1 | Identifies people affected | **Fully supported** |
| 1.2 | Identifies the problem | **Fully supported** |
| 1.3 | Challenges the problem (XY) | **Fully supported** |
| 1.4 | Challenges our understanding (bias) | **Some support** |
| 1.5 | Expresses problem for stakeholders | **Fully supported** |
| 1.6 | Quantifies problem importance | **Not well** |
| 1.7 | Quantifies confidence in analysis | **Not well** |
| 1.8 | Applies across scenarios (regulatory/partner/VOIP) | **Some support** |
| 1.9 | Handles non-user-based situations | **Not well** *(revised — see log)* |
| 1.10 | Clear go/no-go criteria (problem) | **Not well** |

**1.1 People affected — Fully supported.** *Empathize* is the entire front
end, and the asset deck operationalizes it: Empathy Maps, Interview for
Empathy, stakeholder mapping, and especially **Extreme Users** —
deliberately sampling edge cases to widen who you consider. It identifies
and humanizes affected people better than almost any methodology.
*Caveat:* it is end-user-centric by construction — it nails the primary
humans but has no rigorous discipline for enumerating second-order or
non-experiential stakeholders (regulators, payers, downstream operations).

**1.2 Identifies the problem — Fully supported.** The *Define* mode exists
for exactly this: synthesize empathy data into one actionable problem
statement via the **POV Madlib** ("[user] needs [need] because [surprising
insight]"). The output is an explicit, scoped statement, not a vague theme.

**1.3 Challenges the problem / XY — Fully supported.** Design Thinking's
signature strength. Reframing is a built-in stage, not an afterthought:
"fall in love with the problem, not the solution," **Why–How Laddering** to
climb from stated ask to root need, and **How Might We** to reopen the
framing as opportunities — precisely the machinery for catching an XY
problem (someone demanding solution Y when the real problem is X).

**1.4 Challenges our understanding — Some support.** Genuine anti-bias
intent and tools: **Assume a Beginner's Mindset / question assumptions**,
observing behavior over stated claims, radical (diverse) collaboration, and
cheap prototypes that test assumptions before commitment. But it is weak
where it matters most: **synthesis bias is uncontrolled**. Affinity mapping
and POV selection are subjective and small-N; a motivated team can find an
anecdote to justify nearly any conclusion, and there is no disconfirmation
protocol, blind analysis, or statistical check. It dislodges the biases you
walk in with, not the ones you generate while interpreting.

**1.5 Expresses the problem — Fully supported.** POV statements,
personas/composite characters, journey maps, empathy maps, and
**storytelling** (a core d.school competency) produce intuitive, narrative
artifacts that non-specialist stakeholders grasp immediately.
Communicability is a deliberate design goal of the outputs.

**1.6 Quantifies importance — Not well.** Intentionally qualitative and
divergent: no native severity scale, prioritization score, or
commercial-weighting mechanism. It can say a need is *real and felt*, not
*how important relative to other needs*, nor where it sits on a
WIBNI-to-committed axis. This is its best-known gap and exactly what
quantitative methods (ODI opportunity scoring, Kano) are bolted on to fill.

**1.7 Quantifies confidence — Not well.** Same root cause: small samples,
subjective synthesis, no sampling logic, no statistical validity.
Confidence is *implicit* ("we iterated until patterns repeated") but never
quantified, and the method has no way to express it as a number or range.

**1.8 Wide variety of scenarios — Some support.** Domain-agnostic in
principle and applied widely (services, policy, healthcare, organizations),
so it stretches — but it is anchored to human experience and goes quiet on
each example's core: it can map who a **regulation** burdens but says
nothing about compliance logic; it can empathize with a **partner's**
people but not model the contractual or technical integration; for
**VOIP** (infrastructure where the "user" is a system and constraints are
engineering) its empathy-and-journey toolkit largely idles. A useful lens
on any domain; insufficient as the primary method where the core is legal,
contractual, or technical.

**1.9 Non-user-based situations — Not well.** The criterion strikes Design
Thinking's founding axiom. Human-centered design *starts* from a human's
needs — *Empathize* is the literal entry point — so a situation with no
user at its center removes the load-bearing element: system-to-system
behavior, regulatory logic, contractual structures, a signaling backbone,
business-model mechanics give the core tools nothing to attach to. The
partial rescue — find the **adjacent humans** (operator, admin, affected
third party) and run the method on them — *converts* a non-user problem
back into a user problem rather than handling it as what it is, and can
distort by putting emphasis in the wrong place. That rescue keeps the score
off the floor; it does not earn "some."

**1.10 Go/no-go on the problem — Not well.** No decision gate exists. The
model is an iterative divergent–convergent loop whose *Test* mode feeds the
next iteration, not an investment decision: no kill criteria, thresholds,
or go/no-go logic. By design it keeps exploring rather than terminating —
for a stage-gated process, the sharpest gap.

---

## Batch 2 — The solution

| # | Criterion | Rating |
|---|-----------|--------|
| 2.1 | Explore multiple theoretical options | **Fully supported** |
| 2.2 | Plausible solution set within business priorities | **Some support** |
| 2.3 | Clear set of outcomes the solution delivers | **Some support** |
| 2.4 | Clear value proposition | **Some support** |
| 2.5 | Applies across scenarios (UX → detailed VOIP flows) | **Some support** |
| 2.6 | Identifies effort involved | **Not well** |
| 2.7 | Go/no-go criteria (solution) | **Not well** |

**2.1 Explore multiple options — Fully supported.** *Ideate* is
purpose-built for this: the brainstorm rules (defer judgment, go for
quantity, encourage wild ideas, build on others / "yes-and"), Crazy 8s,
Worst Possible Idea, mash-ups, bodystorming — all engineered to go wide
before converging. Generating a broad field of options is its defining
solution-space strength.

**2.2 Plausible set within business priorities — Some support.** It
produces candidates and has light selection tooling — the **Four
Categories** method (the rational choice / the most likely to delight / the
darling / the long shot), dot-voting, 2×2s. But it is deliberately
desirability-led and constraint-deferred: ideation postpones exactly the
feasibility/viability filter the criterion asks for. It yields a set
plausible *to users*, not plausible *within business priorities*, until
that filter is bolted on.

**2.3 Outcomes the solution delivers — Some support.** A prototype is a
concrete expression of an *intended experiential outcome*, and *Test*
checks whether it resonates — genuine partial coverage. But the deliverable
is **validated learning and direction**, not a specified, committed, or
measurable outcome set. Prototypes are "build to think": rough, disposable,
made to learn from — you come away knowing "this direction works," not
"here are the outcomes we will ship."

**2.4 Value proposition — Some support.** On *user* value the thread is
strong: every concept traces through **How Might We** to the **POV** need
and the empathized insight, so "why these outcomes matter to the user" is
well grounded. Absent is the **commercial** value proposition —
differentiation, market value, willingness to pay, competitive position.

**2.5 UX → detailed VOIP flows — Some support.** The solution-side twin of
1.8. At the UX end the method is native and excellent — experiential
prototyping, journey-level flows. At the detailed-VOIP end it has
essentially nothing: no protocol, state, or architecture design.
"Prototype" stretches rhetorically, but low-fidelity experiential
prototyping is not detailed technical design.

**2.6 Effort involved — Not well.** No sizing, cost, or effort apparatus,
and almost *anti-estimation* by temperament — you prototype cheap and rough
precisely to avoid committing effort up front. Effort estimates come from
engineering and delivery practice, not from this method.

**2.7 Go/no-go on the solution — Not well.** A notch more solution-relevant
than 1.10, because *Test* genuinely evaluates the concept with users and can
yield "this doesn't land — drop it." But it provides **evidence, not
decision criteria**: no thresholds, no kill rules, no viability gate, and a
strong iterate-don't-terminate instinct (its feedback ritual — **I Like / I
Wish / What If** — is formative, not summative). Good at comparative
selection among concepts; weak at an absolute commit decision, which also
needs the effort and business dimensions it doesn't carry.

*Batch 2 lens:* the desirability / feasibility / viability triad (Brown /
IDEO). Design Thinking **owns desirability** (2.1; the user-value half of
2.4; the UX half of 2.5), **under-serves feasibility** (2.6; the technical
half of 2.5), and **under-serves viability** (the business-priority filter
in 2.2; the commercial value prop in 2.4; go/no-go in 2.7).

---

## Batch 3 — The market

| # | Criterion | Rating |
|---|-----------|--------|
| 3.1 | Resolves conflicting requirements | **Some support** |
| 3.2 | Picks the best solution for the market | **Some support** |
| 3.3 | Sizes the opportunity (revenue + constraints) | **Not well** |
| 3.4 | Cheap ways to validate assumptions pre-build | **Fully supported** |
| 3.5 | Identifies market positioning | **Not well** |
| 3.6 | Applies across scenarios (SaaS → on-prem) | **Some support** |
| 3.7 | Identifies success KPIs | **Not well** |
| 3.8 | Go/no-go given market positioning | **Not well** |

**3.1 Conflicting requirements — Some support.** A *tie-breaker philosophy*
rather than a resolution mechanism: return to the **POV** and let the
prioritized user's need arbitrate, with **Extreme Users** / "design for
one" deciding whose need wins, and Four-Categories selection giving light
arbitration. That resolves *user-need* conflicts. It has no apparatus for
stakeholder vs. regulation vs. partner vs. technical-constraint conflicts —
no trade-off framework, weighted scoring, or MoSCoW.

**3.2 Best solution for the market — Some support.** Selection runs on
**user desirability** (Test resonance, Four Categories, dot-voting) — a
partial proxy for market success, not market selection. "Best for the
market" implies competitive position, segment economics, and
differentiation, none of which it evaluates, and its signal comes from a
small, non-representative test sample. It quietly conflates "our tested
users liked it" with "best for the market."

**3.3 Opportunity size / revenue — Not well.** Pure business
quantification — TAM/SAM/SOM, revenue modeling, constraint analysis — and
Design Thinking has none of it. Market sizing is simply outside the method.

**3.4 Cheap assumption validation — Fully supported.** Its signature
strength, shining even in this batch. The **Prototype → Test** ethos *is*
"build cheap, learn fast, validate before you commit": low-resolution
prototypes, build-to-think, testable prototypes, Wizard-of-Oz, bias toward
action, fail early and cheap. *Honest boundary:* the power concentrates on
**desirability/usability** assumptions; it is weaker for cheaply validating
*feasibility* (technical spikes) or *viability* (financial/market)
assumptions, which need other instruments. For the class it covers, it is
best-in-class.

**3.5 Market positioning — Not well.** Positioning — category, competitive
alternatives, target segment, differentiated value (the Dunford sense) — is
not a Design Thinking activity. The POV and user-value articulation are
adjacent raw material for a positioning exercise, but the method produces
no competitive frame, category definition, or differentiation.

**3.6 SaaS → on-prem — Some support, with a twist.** This axis is
deployment/commercial, not experiential, so the method is **indifferent**
to it — it operates at the user-needs layer above deployment model. That
cuts both ways: it applies identically to SaaS or on-prem (broad
applicability), but *because* it abstracts above the distinction it gives
no leverage on what actually differs — economics, ops burden, security
posture, update cadence, contract structure. Applicable everywhere; useful
on the SaaS/on-prem trade-off itself, no.

**3.7 Success KPIs — Not well.** No KPIs are defined. "Success" means "does
it resonate / solve the user need," judged through qualitative test
feedback, not measurement — the same quantification gap as 1.6/1.7, on the
output side.

**3.8 Go/no-go on market positioning — Not well.** The clearest of the
three go/no-go failures: a market-positioning decision needs sizing (3.3),
positioning (3.5), and KPIs (3.7) as inputs, and the method scores Not well
on all three. It cannot gate on a market position because it never produces
one; even the qualitative solution signal that lifted 2.7 is irrelevant
here.

---

## Revision log

- **1.9** was first scored *Some support* under a reading of "not directly
  **use**-based" (the adjacent-human reframe earned partial credit). The
  criterion was corrected to "not directly **user**-based," which targets
  the human-centered premise itself; the score was revised to **Not well**
  because the only rescue the method offers — re-casting a non-user
  situation as a user situation — is precisely the tell that it does not
  handle non-user situations as such. The correction sharpened 1.8 without
  changing it: 1.8 and 1.9 share one root limit, and the VOIP example in
  1.8 is itself largely non-user-based.

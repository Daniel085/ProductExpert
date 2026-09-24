# From Feature Request to Riskiest Assumption — Method Reference

*The entry protocol of **Solution Validation** when the starting point is
a **feature request** — from a stakeholder, a customer, a sales call, an
executive. Don't just build it; break it down. The eight assumption
questions are the PM's own working framework (Daniel O'Rorke); the
riskiest-assumption discipline is the ledger's ranking rule (*Talking to
Humans*, impact × uncertainty); the de-requirement step is Cagan's. The
breakdown protocol, the assumption-chain template and the null-result
rule are this repo's operational extension. See
[`../../CREDITS.md`](../../CREDITS.md).*

> **Where this sits.** Problem Validation ended with a problem the team
> understands (a *Yes* case, a knowledge-gap scorecard with no area
> below 3). Solution Validation asks which solution is right for it. A
> feature request short-circuits that: it arrives as an answer with the
> question missing. This protocol recovers the question, exposes the
> chain of assumptions between what someone *observed* and what they
> *proposed*, finds the one that would kill the idea if wrong, and hands
> it to an experiment
> ([`pre-build-experiments.md`](./pre-build-experiments.md)) — usually
> one the PM can fake by hand in days.

## 1. The breakdown protocol

1. **Find the observation.** Every feature request began as something
   someone saw or heard — a customer remark, a lost deal, a competitor's
   launch, a dinner conversation. Ask the requester *what did you see or
   hear that made you think of this?* and write it down verbatim,
   tiered (CONFIRMED / INFERRED / BACKGROUND). If no observation can be
   found, the request is a preference; say so and route it to the
   requirements protocol
   ([`../jtbd/requirements-are-hypotheses.md`](../jtbd/requirements-are-hypotheses.md)).
2. **Reclassify the ask** per that protocol: true constraint /
   stakeholder theory / customer solution-guess. Most feature requests
   are one of the last two.
3. **Answer the eight questions** (§2). Each answer is a claim; each
   claim is an assumption until evidence is attached.
4. **Write the assumption chain** (§3): the sequence of things that
   must all be true for the observation to justify the feature. The
   chain almost always has more links than the requester saw.
5. **Rank and pick the riskiest** — the link that is most load-bearing
   *and* least evidenced (impact × uncertainty, the ledger's rule).
   Exactly one.
6. **Design the cheapest experiment** that could prove that link false
   — a card from the catalogue, not a build. The PM playing the feature
   by hand (Wizard of Oz) behind an existing surface, with a controlled
   comparison, is the usual first move.
7. **Read out honestly, then check reach** (§4) before concluding.

## 2. The eight assumption questions

Answer every one in writing. An answer that is a guess gets marked as
one — that is the point.

| # | Question | What a real answer contains | Where the evidence would come from |
|---|----------|-----------------------------|------------------------------------|
| 1 | **What problem will this solve for us?** | A job story from the customer's side, and the business problem it maps to — two answers, not one | Problem case ([`../problem-selection/picking-the-right-problem.md`](../problem-selection/picking-the-right-problem.md)); synthesis insights |
| 2 | **Who is the target audience?** | A job executor and segment, not "users"; who has the observation been made about? | Screener, segment profiles, ODI segments |
| 3 | **How big is the opportunity?** | Customers × value × reachability, order of magnitude, with the counter-case | Metrics; problem case Customer Signal; sizing FAQ |
| 4 | **What alternatives are out there, and how is the market solving for this?** | Named products *and* workarounds; what they do; what they charge; where they fall short | Landscape scan / competitive teardown ([`../problem-selection/knowledge-gaps.md` §3](../problem-selection/knowledge-gaps.md)) |
| 5 | **Do we have everything we need to pursue this?** (constraints) | Real constraints verified, preferences labelled; the hard part named; data, partners, compliance | Engineering spike; requirements protocol |
| 6 | **What is the go-to-market strategy?** | How the target audience will find and adopt it — channel, trigger, message; what they have to *stop* doing | Existing channel data; landscape scan question 4 |
| 7 | **What strategic KPIs will this achieve?** | The goal metric and the input metric it moves, with a number | Metric tree ([`../metrics/north-star.md`](../metrics/north-star.md)) |
| 8 | **What factors are critical to success and must be part of the solution?** | The two or three properties without which the solution fails its job — from evidence, not from the feature spec | Value proposition (pains / gains), outcome statements, the requester's observation |

Two reading rules:

- **Question 1 has two halves.** "What problem will this solve for
  *us*" is the business's; the customer's problem must be stated
  separately. A request that answers only the business half is a
  stakeholder theory.
- **Question 8 is not the feature list.** "Must have a retry button" is
  the feature; "nothing the user already entered may be lost when an
  import fails" is a critical factor. Factors survive a change of
  solution; features don't.

Overlap, on purpose: questions 1–3 and 7 are the PR/FAQ's five customer
questions and internal FAQ bank
([`../prfaq/working-backwards.md`](../prfaq/working-backwards.md)) asked
*before* a document exists; a request that can answer all eight is
ready for a PR/FAQ. One that can't is ready for an experiment.

## 3. The assumption chain

From the observation to the proposed feature, list every claim that
must hold. Each becomes a ledger row
([`../customer-interviews/assumption-ledger.md`](../customer-interviews/assumption-ledger.md)).

```
Observation (verbatim, tiered): "<what was seen or heard>"          [CONFIRMED · who · when]
Proposed feature: <the ask, as stated>
Requester's implied logic: "if we <feature>, then <outcome>, because <belief>"

Chain — all must be true:
  A1  The observation generalizes beyond the people who made it        conf: low/med/high · evidence:
  A2  The behavior observed elsewhere (e.g. on another platform)
      would transfer to ours                                            conf: … · evidence:
  A3  The target audience wants <the thing the feature delivers>
      *from us*, in *our* context                                       conf: … · evidence:
  A4  Wanting it changes the behavior we care about (buy, retain,
      convert, stay satisfied)                                          conf: … · evidence:
  A5  The audience will encounter the feature where we put it
      (reach / channel)                                                 conf: … · evidence:
  A6  We can deliver it well enough that A3–A4 hold (execution)         conf: … · evidence:
  A7  <the constraint or GTM assumption from questions 5–6>             conf: … · evidence:

Riskiest (exactly one): A_  — because it is load-bearing for the whole
chain and has the least evidence.
What would disprove it: <observation, stated now>
Cheapest test: <card family · who plays the feature · where · comparison · measure · timebox>
```

Typical shape of the riskiest link: **A3 or A4** — that the audience
wants *this* from *us*, and that wanting it moves the metric. Requesters
tend to have evidence for A1 (they heard it) and none for A3–A5.

## 4. The null-result rule

When the experiment shows **no effect**, there are two explanations,
and the second is checked before the first is accepted:

1. **The value isn't there** — the riskiest assumption is false.
2. **The experiment never reached the audience** — the feature was
   placed where the target users don't go, shown to the wrong segment,
   or measured on a surface they bypass (assumption A5, which teams
   forget to write down).

So a null readout triggers one question before a verdict: *did the
people we're testing actually see it, through the channel they actually
use?* Check the traffic and the segment. If reach failed, **move the
same experiment to the real channel** and re-run before concluding the
solution is wrong; if reach was fine, the null is real and the chain
breaks at the riskiest link. A confirmed effect in the real channel is
often a *strategy* finding, not a feature finding — the learning
transfers beyond the request that started it.

## 5. Anti-patterns

| Anti-pattern | Tell | Fix |
|--------------|------|-----|
| **Build the ask** | "The CEO wants it; scope it" | Find the observation; write the chain; test the riskiest link |
| **No observation** | "It just seems like a good idea" | Preference, not request; requirements protocol |
| **Chain with one link** | "Customers want X, so we build X" | Write A1–A7; the middle links are where ideas die |
| **Riskiest = hardest to build** | Picking the engineering risk first | Riskiest = most load-bearing × least evidenced, usually a customer link |
| **Testing on the wrong surface** | Null result, verdict "no demand" | Null-result rule: check reach before value |
| **Faking without a comparison** | "We tried it and sales went up" | Controlled comparison or a pre-registered baseline (→ `experimentation` when traffic allows) |
| **Learning stays local** | Effect found, feature shipped, nothing else changes | Ask what the confirmed assumption implies for strategy, not just for the request |
| **The observation is a model's answer** | "We asked the AI what was missing and it said X" | Not an observation — a BACKGROUND guess. Find what a real user said or did, or treat the request as a preference |

## Sources & materials

- **The eight assumption questions** — **Daniel O'Rorke**'s working
  framework for making the assumptions behind a request explicit
  (problem for us; target audience; opportunity size; alternatives and
  market; constraints; go-to-market; strategic KPIs; critical success
  factors).
- **Riskiest assumption** — the impact × uncertainty ranking of
  *Talking to Humans* (Constable & Rimalovski), as encoded in the
  shared ledger; "riskiest assumption test" usage from the lean-startup
  community broadly.
- **De-requirement** — Marty Cagan, *"Requirements Are Not"* (see
  [`../jtbd/requirements-are-hypotheses.md`](../jtbd/requirements-are-hypotheses.md)).
- The breakdown protocol, the chain template (A1–A7), the null-result
  rule and the anti-patterns are this repo's operational extension,
  informed by training material that is deliberately **not** reproduced
  or paraphrased here.
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

# The Minimum Viable Product — Method Reference

*What an MVP is for, why most fail, and how to align one with a learning
goal. Definitions from **Frank Robinson** (coined 2001), **Eric Ries** and
**Steve Blank**, via the Wikipedia article (CC BY-SA, wikitext preserved
in [`./materials/extracted/`](./materials/extracted/)); the failure
modes, the learning-alignment questions and the four maxims are the PM's
notes (Daniel O'Rorke). The MVP-vs-MLP-vs-MVI context table lives in
[`pre-build-experiments.md` §5](./pre-build-experiments.md). See
[`../../CREDITS.md`](../../CREDITS.md).*

> **The one-line correction.** An MVP is not the lightweight, cheap
> version of the product. **It is the fastest path to insight.** If a
> team can say what it will *learn* from the MVP and what it will do
> differently afterwards, it has one; if it can only say what it will
> *ship*, it has a small v1 with the wrong name.

## 1. What the canon says

- **Ries:** "that version of a new product a team uses to collect the
  maximum amount of validated learning about customers with the least
  effort." *Maximum* and *minimum* are judgments, not formulas — which
  is why the term stretches from prototype to marketable product and
  needs pinning down per context.
- **Blank:** the point is validating the hypotheses under the product —
  ask customers whether they want it or whether it meets the need, and
  **pivot** when the hypothesis is false.
- **Robinson (2001):** coined the term; a product sized to be *viable*
  for early customers so their feedback shapes what comes next.
- **Scientific method, applied to a business hypothesis.** An MVP is an
  experiment; the deploy is to early adopters (forgiving, vocal, able to
  see the vision through a rough version); the goal is maximum
  information about the customer for the least money. The main cause of
  startup failure is *no market need* — the MVP exists to detect that
  before the money is spent.
- **Not "release early, release often."** Open-source style lets users
  define the product; an MVP keeps a **product vision** and adapts it on
  explicit and implicit feedback. Also not stealth mode's long plan.
- **Iterate until fit or until non-viable.** The loop — idea, prototype,
  present, collect, analyze, learn — is repeated with minimum time per
  turn, and *deemed non-viable* is a legitimate exit.
- **Testing is the essence.** Release to a limited group; gather
  feedback on functionality, usability and value; the result says
  whether the product should be built at all.
- **Known limits (the criticism section):** an early MVP can invite
  imitation where there are no other barriers; negative feedback on a
  rough MVP can hurt reputation; in app-store markets users switch
  freely, so a below-standard MVP loses to a polished entrant; and
  testing ideas in the market exposes them. The responses — minimum
  viable *experiment*, minimum *awesome* product, "simple, lovable,
  complete" — are all ways of saying: minimum in scope, not in quality
  (see the MLP in [`pre-build-experiments.md` §4](./pre-build-experiments.md)).

## 2. Why MVPs fail

Two causes account for most of it:

1. **The team thinks it is building v1.** Scope is set by "what the
   product needs" instead of "what we need to learn"; the MVP grows
   into a small release with no hypothesis, no measure, and no
   decision waiting on it. Test: *what would we do differently if the
   result came back negative?* No answer → it's a v1.
2. **Poor execution.** Buggy, slow, ugly, or unusable — so the negative
   signal measures the execution, not the idea. Minimum scope never
   licenses minimum quality on the slice that ships: the bar for what
   is *in* the MVP is the lovable one (end-to-end, intuitive,
   delightful), or the test is confounded.

## 3. Align the MVP with what you are trying to learn

Four questions, answered before scoping — the MVP is designed
backwards from them:

| # | Question | The answer shapes… |
|---|----------|--------------------|
| 1 | **What problem are we solving?** | The job story the MVP must serve end-to-end; anything not on that path is out |
| 2 | **What assumptions are we making about the market?** | The chain ([`riskiest-assumption.md`](./riskiest-assumption.md)); the MVP targets the riskiest link, not all of them |
| 3 | **What is the quickest, lowest-risk way of validating those assumptions?** | Whether an MVP is even needed — a concept test, concierge or Wizard of Oz may answer sooner ([`pre-build-experiments.md` §2](./pre-build-experiments.md)); if it is, the smallest real slice that produces the signal |
| 4 | **Are we optimizing for adoption, retention, conversion, or satisfaction?** | The one measure the MVP is read out on, and therefore the segment, the timebox and the surface: adoption needs reach, retention needs time, conversion needs a transaction, satisfaction needs a report |

Question 4 is the one teams skip. An MVP that "will tell us if people
like it" has no readout; one that is optimized for *retention* is
scoped to survive four weeks of real use by fifty accounts and is read
on week-4 return, nothing else.

## 4. The four maxims

1. **Be clear about your learning goal.** One sentence, written before
   scoping; the MVP's success criterion is a learning, not a launch.
2. **Use experiments, not features.** If a card from the catalogue
   answers the question, the MVP is not yet justified. Features are how
   you deliver what you already learned.
3. **Use what you learn and move on.** The MVP's job ends with the
   readout: persevere, pivot, or stop. Keeping it alive as "v1" after
   the learning is in is the first failure mode returning.
4. **Involve customers in the feedback loop early and often.** Early
   adopters in from the first slice; feedback collected on
   functionality, usability *and* value; the loop turned quickly.

## 5. The MVP card

The experiment card ([`pre-build-experiments.md` §6](./pre-build-experiments.md))
with the MVP-specific fields filled:

```
MVP: <name>                                Family: MLP slice / manual-first / real slice
Learning goal (one sentence): …
Problem (job story): …
Market assumptions (chain) — riskiest link this MVP tests: A_
Why not a cheaper card: <what a concept / concierge / WoZ test could not have answered>
Optimizing for: adoption | retention | conversion | satisfaction   → measure: <definition>
Segment (early adopters): …   n: …   surface / channel: …   timebox: …
In scope (the end-to-end path, at lovable quality): …
Out of scope, deliberately: …
Expected: <the number that means "learned, proceed">
Would disprove: <the number that means "learned, pivot or stop">
Execution bar: <what "buggy" would look like and how we'll know the signal isn't execution>
Found out that: …
Decision: persevere / pivot / stop   → what changes next, beyond this MVP
```

## 6. Context still decides which minimum

The doc above is about the *purpose* of a minimum. Which minimum you
build is a context question, kept in one place:
[`pre-build-experiments.md` §5](./pre-build-experiments.md) — **MVP**
(new product, new market: test the segment and its needs), **MLP** (new
product where experience is the differentiator: test that a tiny,
superb slice earns love), **MVI** (existing product, existing customers:
instrument first, small outside-in investments, never a minimum viable
rewrite — Matts).

## Sources & materials

- **Wikipedia contributors** — *"Minimum viable product"*, retrieved
  2026-09-24; CC BY-SA 4.0; wikitext at
  `./materials/extracted/wikipedia-minimum-viable-product.txt`. The
  article cites **Eric Ries** (*Minimum Viable Product: a guide*, 2009;
  *The Lean Startup*), **Steve Blank**, and **Frank Robinson** (SyncDev,
  2001) for the term; the Rippa robot example (University of Sydney,
  2015) for technical-vs-business hypotheses; and the criticism
  literature on imitation, reputation and app-store switching.
- The "fastest path to insight" framing, the two failure modes, the
  four learning-alignment questions and the four maxims are **Daniel
  O'Rorke**'s notes; the MVP card and the readout-by-optimization rule
  are this repo's operational extension.
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

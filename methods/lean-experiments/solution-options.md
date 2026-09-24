# Solution Options — Method Reference

*How to capture a solution once it has been researched and tested: the
**option card**. An option is a high-level solution you have already
researched and tested — not an idea, not a feature list, not a spec. The
template's eleven fields are the PM's (Daniel O'Rorke); the field
guidance, the gates, the comparison table and the hand-offs are this
repo's operational extension. See
[`../../CREDITS.md`](../../CREDITS.md).*

> **Where this sits.** Solution Validation ends with one or more options
> the team could commit to. The option card is the deliverable that
> closes the phase: it records what was tested, what the team now
> believes and on what evidence, and what it would build — at the
> altitude where leadership can choose between options and a team can
> plan. Downstream it feeds the **minimum feature set**
> ([`minimum-feature-set.md`](./minimum-feature-set.md)) and the
> **PR/FAQ** ([`../prfaq/working-backwards.md`](../prfaq/working-backwards.md)).
> Vocabulary note: `ideation`'s "options" are untested candidates from a
> brainstorm; a *solution option* here has survived experiments. The
> word is the same; the gate is not.

## 1. What qualifies as an option

An option can be written only when all of these exist:

- A **validated problem**: a *Yes* case and a knowledge-gap scorecard
  with no area below 3 ([`../problem-selection/`](../problem-selection/)).
- A **value proposition** for a named segment
  ([`../jtbd/value-proposition.md`](../jtbd/value-proposition.md)).
- **At least one experiment readout** on the solution itself — a card
  from the catalogue with its *Expected* / *Would disprove* lines
  compared to what happened ([`pre-build-experiments.md`](./pre-build-experiments.md)).
  An option whose only evidence is problem evidence is a hypothesis
  wearing an option's clothes.
- A **goal metric** the option is meant to move
  ([`../metrics/north-star.md`](../metrics/north-star.md)).

Several options can exist for one problem. That is the point: the card
format makes them comparable.

## 2. The option card

| Field | What goes here | The tell that it's not done |
|-------|----------------|-----------------------------|
| **Title** | A clear, concise name for what you are doing — the outcome or the capability, not a codename or a feature | "Project Falcon"; "Bulk export v2" |
| **Alignment** | The strategic goal(s) the option supports, by name, and how directly (the problem case's Business Alignment score and its reasoning) | "Strategic"; a goal nobody has committed to |
| **Hypothesis** | *We believe building ____ will satisfy the job [JTBD] for [customer segment] and result in [KPI].* One sentence; the blank is the solution at high level; the job is a job story or core functional job; the KPI is a metric with a definition | A hypothesis with no KPI, or with "engagement" as the KPI |
| **Problem** | The customer's problem — the job story from the problem case, with the *why* (the insight) | The business's problem restated; a feature masquerading as a problem |
| **Behavior change** | What the customer will *do differently* if the option works — observable, before/after, in their world | "They'll be happier"; "they'll use the feature" |
| **In scope** | What you are building, at the altitude of capabilities and the end-to-end path they form | A backlog dump; a UI description |
| **Out of scope** | What you are deliberately not building — the adjacent asks, segments and cases set aside, with a line on why | Empty; "everything else" |
| **Dependencies** | What must exist or happen for this to complete: systems, data, partners, other teams, decisions, compliance sign-off | Only engineering dependencies; unverified constraints listed as facts |
| **Risks / unknowns** | What could go wrong or still needs validation — the ledger rows that are not yet CONFIRMED, each with its cheapest test | Risks with no test; "none" |
| **Success metrics & outcomes** | One to three signals that the option is working, each with a definition, a baseline, a target and a date; aligned to the goal in *Alignment*; one counter-metric | Vanity counts; five metrics; no baseline |
| **Iteration plan** | The work broken into discrete chunks, each of which *validates* something — a kata sequence with a learning goal per chunk, not a Gantt of features | Phases named by feature; nothing learnable before the end |

### Card template

```
OPTION — <title>                                      status: draft / reviewed / chosen / parked
Problem case: <link>   Gap scorecard: <link, date>   Value prop: <link>   Readouts: <links>

Alignment:       <goal(s); Business Alignment n/5 because …>
Hypothesis:      We believe building <solution, high level> will satisfy the job
                 <JTBD> for <segment> and result in <KPI: definition, baseline → target>.
Problem:         <job story> — because <insight>.
Behavior change: Today <observed behavior>. If this works, <segment> will <new behavior>,
                 observable as <what we'd see>.
In scope:        1. <capability> 2. <capability> 3. <capability>   (the end-to-end path)
Out of scope:    <item> (why) · <item> (why)
Dependencies:    <system / data / team / partner / decision> — status: verified / assumed
Risks / unknowns:
  R1 <risk> — ledger row <id> · tier <…> · cheapest test <…>
  R2 …
Success metrics & outcomes:
  M1 <metric: definition> baseline <…> → target <…> by <date>   (goal it feeds: …)
  M2 …                                                          counter-metric: <…>
Iteration plan:
  1. <chunk> — validates <what> — measure <…> — ≤ <weeks>
  2. <chunk> — validates <what> — …
  3. …
Evidence summary: <what was tested, family, result, confidence> — what remains belief.
```

## 3. Writing rules

- **The hypothesis is the card in one sentence.** If it can't be
  written, the option isn't defined; if the KPI in it isn't in *Success
  metrics*, the two disagree.
- **Behavior change is the acceptance test.** It should be visible in
  the world without reading a dashboard — the customer stops doing the
  workaround, starts doing the job a different way. Success metrics
  measure it; they don't replace it.
- **In scope is the path, not the parts.** Write what the customer can
  do end-to-end, then the capabilities that make it possible. The
  minimum feature set doc does the cutting.
- **Out of scope is a decision log.** Every item there was considered;
  the *why* is what keeps it from being relitigated.
- **Risks come from the ledger.** Nothing new is invented here; the
  card lists the surviving rows and their tests. A risk with no test is
  a worry, not a risk.
- **Iteration plan = kata sequence.** Each chunk has a learning goal
  and a measure ([`product-kata.md`](./product-kata.md)); the first
  chunk is usually the riskiest surviving assumption. If every chunk
  only *builds*, rewrite it.
- **Evidence tiers throughout.** What a readout showed is CONFIRMED;
  what the team concluded from it is INFERRED; what the scan says is
  BACKGROUND. An option card written from BACKGROUND alone is returned.

## 4. Comparing options

When more than one option survives, lay them side by side on the same
rows and let the differences show:

| | Option A | Option B | Option C |
|---|---|---|---|
| Hypothesis (KPI) | | | |
| Alignment score | | | |
| Strongest evidence (family · result) | | | |
| Behavior change (size of shift) | | | |
| Biggest surviving risk | | | |
| Dependencies not yet verified | | | |
| Cost of delay (from the feature-set doc) | | | |
| First iteration's learning goal | | | |

Decision rules: prefer the option with the strongest *solution*
evidence over the one with the best story; never choose an option whose
biggest risk has no test; if two are close, the one whose first
iteration learns most per week goes first. Record the choice and the
reason on the losing cards (status: parked, with what would revive
them).

## 5. Gates and hand-offs

- **Refuse to write** an option with no experiment readout, no goal
  metric, or a hypothesis that names no segment or KPI.
- **Return** a card whose risks have no tests, whose iteration plan
  contains no learning, or whose success metrics have no baseline.
- **Chosen option** → [`minimum-feature-set.md`](./minimum-feature-set.md)
  to define v1.0, and → **prfaq** (the card pre-answers the five
  customer questions; the hypothesis becomes the headline; the risks
  become "what we'd need to believe").
- **Success metrics** → **metrics** for definition cards and the
  counter-metric.
- **Iteration plan** → back to **lean-experiments** kata mode, one
  chunk per cycle.
- **Parked options** stay in the working folder with their revival
  condition; they are the roadmap's second choices, evidenced.

## Sources & materials

- **The option template** — Title · Alignment · Hypothesis (*We believe
  building ____ will satisfy the job [JTBD] for [customer segment] and
  result in [KPI]*) · Problem · Behavior change · In scope · Out of
  scope · Dependencies · Risks / unknowns · Success metrics & outcomes ·
  Iteration plan — **Daniel O'Rorke**'s working template.
- The hypothesis form descends from the lean-startup "we believe"
  hypothesis (Ries; the Wilkie format in
  [`../customer-interviews/research-and-insight.md`](../customer-interviews/research-and-insight.md)).
- Field guidance, tells, writing rules, the comparison table and the
  gates are this repo's operational extension.
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

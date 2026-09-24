# The Minimum Feature Set (v1.0) — Method Reference

*Defining what ships first from a chosen option. **This is not the MVP.**
The MVP was an experiment; v1.0 is a product real customers will run
their job on. What goes in is decided by the option's critical success
factors; what can wait is decided by **cost of delay** — **Don
Reinertsen**'s economic framing (*The Principles of Product Development
Flow*, 2009) and **Joshua Arnold**'s **CD3** (cost of delay divided by
duration, Black Swan Farming). The distinction, the candidate table, the
postponement rules and the template are this repo's operational
extension, from the PM's notes. See
[`../../CREDITS.md`](../../CREDITS.md).*

> **Where this sits.** After an option is chosen
> ([`solution-options.md`](./solution-options.md)) and before delivery
> planning. The MVP answered *should we build this?*; the minimum
> feature set answers *what is the smallest version a customer can
> adopt and keep using?* — and, of everything the option's scope
> implies, what it costs to postpone each piece.

## 1. v1.0 is not the MVP

| | MVP | Minimum feature set (v1.0) |
|---|---|---|
| Purpose | Learn whether to build | Deliver the job to customers who will stay |
| Audience | Early adopters who forgive | The target segment, including people who won't |
| Scope rule | Whatever produces the signal | Whatever the job needs end-to-end, and nothing that can wait |
| Quality rule | Enough that a negative result is about the idea | Enough to run a real job on, daily: lovable on what ships (end-to-end, intuitive, delightful) |
| What's cut | Everything not needed to learn | Everything whose *cost of delay* is low |
| Afterwards | Read out and move on | Iterate in production |

The failure in both directions: shipping the MVP as v1.0 (the first MVP
failure mode — [`minimum-viable-product.md` §2](./minimum-viable-product.md)),
or padding v1.0 with everything the option mentions because "minimum"
sounds like the MVP and nobody wants to repeat that.

## 2. Candidate features

Start from the chosen option card's **In scope** (the end-to-end path)
and its **critical success factors** (the eight-question breakdown's
question 8: the properties without which the solution fails its job).
Every capability on the path is a candidate. Add the operational
minimums a real product needs that an MVP could skip (Gus Power's
"minimum sustainable product": security, performance, support,
billing, compliance). Then classify:

| Class | Rule | Goes in v1.0? |
|-------|------|----------------|
| **Job-critical** | Without it the customer cannot complete the core job end-to-end, or a critical success factor is violated | Always |
| **Adoption-critical** | Without it the target segment will not *switch* — what they'd have to give up is too much (the value proposition's "what gets fired") | Always, for the launch segment |
| **Sustainability minimum** | Without it the product can't be run as business-as-usual | Always, at the level the launch segment needs |
| **Valuable, postponable** | Improves the job or widens the segment; the job completes without it | Decided by cost of delay |
| **Speculative** | No evidence anyone needs it yet | Out; back to the ledger |

Only the fourth class needs the economics. Everything else is decided
by the option's evidence.

## 3. Cost of delay

**Cost of delay** (Reinertsen) is the economic value lost per unit of
time that a feature is *not* available — the question "what does it cost
us per week to ship this later?" It converts every scheduling argument
into one currency, and it exposes the features whose value dies with a
date. Estimate it per postponable feature:

1. **Value if shipped**, per period: revenue enabled or protected, cost
   avoided, risk removed, strategic option kept — in money where
   possible, in a consistent relative scale where not.
2. **Urgency profile** — how that value changes with time (Reinertsen's
   shapes, as commonly applied):
   - **Standard** — value accrues steadily from whenever it ships;
     delay costs a constant amount per week.
   - **Fixed date** — value drops sharply after a deadline (regulatory,
     contractual, seasonal); little cost before it, most of the cost
     after.
   - **Expedite** — cost of delay is high and immediate (a churn
     driver, a blocker for a signed customer); every week costs.
   - **Intangible / long-term** — small cost now, growing later
     (technical foundations, data collection); cheap to defer, expensive
     to defer forever.
3. **Duration** — how long it takes to deliver, in the same time unit.
4. **CD3 = cost of delay ÷ duration** (Arnold). Higher first: the
   feature that returns the most value per week of scarce capacity.
   Two features with the same cost of delay are separated by duration —
   the quick one ships first because its value starts compounding
   sooner.

```
Feature      CoD / week    Profile     Duration    CD3        Decision
Recover partial import   40k   expedite    4 wks     10.0   v1.0 (job-critical anyway)
Mapping presets          12k   standard    2 wks      6.0   v1.0
Scheduled re-import       9k   standard    3 wks      3.0   v1.1
Audit log                 6k   intangible  3 wks      2.0   v1.2 — grows; revisit in Q+1
Enterprise SSO           30k   fixed date  6 wks      5.0   v1.1 — before the renewal date
```

### Postponement rules *(repo extension)*

- A feature with a **fixed-date** profile is scheduled against its
  date, not its CD3 rank; the rank only orders it among things that
  fit before the date.
- **Expedite** items are questioned before they are honoured: who is
  hurt per week, evidenced how? An "expedite" with no named customer or
  metric is a stakeholder theory.
- **Intangible** items are given a revisit date; postponing them is a
  decision with an owner, not a default.
- Anything postponable with a CD3 below the team's cut line goes to
  **v1.1+**, with its CoD recorded so the roadmap conversation starts
  from numbers.
- If the cost-of-delay estimate for a feature is a guess, mark it as
  one (BACKGROUND) and ask whether a cheaper experiment would firm it
  up before capacity is committed.

## 4. The minimum feature set template

```
MINIMUM FEATURE SET — v1.0 of <option title>                     dated <date>
Option card: <link>   Launch segment: <…>   Goal metric: <…>

Core job, end-to-end: <job story> — the path v1.0 must complete:
  step 1 → step 2 → step 3 → outcome

| # | Feature / capability | Class (job-critical / adoption-critical / sustainability / postponable / speculative) | Critical success factor served | CoD/wk | Profile | Duration | CD3 | v1.0? | Reason |
|---|----------------------|----------|----------|--------|---------|----------|-----|-------|--------|

In v1.0:   <list> — total duration <…>; what "lovable" means for each (end-to-end / intuitive / delightful)
Deferred:  <list with CoD and target version>; fixed-date items with their dates
Dropped:   <speculative items> → ledger rows
Cut line:  CD3 < <n> deferred, because capacity is <…> weeks before <date/goal>
Launch readiness signals: <the option's success metrics, baselined>
```

## 5. Anti-patterns

| Anti-pattern | Tell | Fix |
|--------------|------|-----|
| **MVP shipped as v1.0** | The learning slice, plus a logo | Re-scope from the option: job end-to-end, at lovable quality |
| **"Minimum" means everything in the option** | v1.0 = the whole In-scope list | Only the first three classes are automatic; the rest earn a place by CD3 |
| **Ranking by effort alone** | Quick wins first, regardless of value | CD3 divides value by duration; it doesn't ignore value |
| **Ranking by value alone** | The big feature first, six months of nothing shipped | Duration is in the denominator for a reason |
| **Everything is urgent** | All rows "expedite" | Expedite needs a named customer or metric hurt per week |
| **Deadline features ranked by CD3** | A regulatory item loses to a higher-CD3 feature and misses its date | Fixed-date items are scheduled to the date first |
| **Silent deferral** | Postponed features vanish | Deferred list with CoD, target version, revisit date, owner |
| **Guessed CoD treated as fact** | Precise numbers, no source | Tier it; run the cheaper experiment if capacity depends on it |

## 6. Hand-offs

- **Deferred list with cost of delay** → the roadmap conversation (the
  cross-option sequencing method is a roadmap item in the README; this
  doc is its feature-level input).
- **v1.0 scope** → **prfaq** (the press release describes v1.0, not the
  option's full ambition) and → the delivery team.
- **Launch readiness signals** → **metrics** for definitions and
  instrumentation; → **experimentation** for any v1.0 rollout that
  warrants a controlled ramp.
- **Guessed CoD on a load-bearing feature** → **lean-experiments** for
  the card that would firm it up.

## Sources & materials

- **Donald G. Reinertsen**, *The Principles of Product Development
  Flow: Second Generation Lean Product Development* (Celeritas, 2009) —
  cost of delay as the economic basis for scheduling; urgency profiles
  as commonly applied from his work.
- **Joshua J. Arnold**, *Black Swan Farming* — CD3 (cost of delay
  divided by duration), with **Özlem Yüce**; the naming that keeps
  "cost of delay" in the formula (the same idea appears as WSJF in
  SAFe). https://blackswanfarming.com/cost-of-delay-divided-by-duration/
- **Gus Power** — "minimum sustainable product" (comment on Matts's MVI
  post, preserved in `./materials/`).
- The v1.0-vs-MVP table, the five feature classes, the postponement
  rules, the template and the anti-patterns are this repo's operational
  extension from **Daniel O'Rorke**'s notes ("not an MVP; v1.0; use cost
  of delay to decide what to postpone").
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

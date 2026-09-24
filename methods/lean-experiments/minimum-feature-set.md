# The Minimum Feature Set (v1.0) — Method Reference

*Defining what ships first from a chosen option. **This is not the MVP.**
The MVP was an experiment; v1.0 is a product real customers will run
their job on. What goes in is decided by the option's critical success
factors; what can wait is decided by **cost of delay** — **Don
Reinertsen**'s economic framing (*The Principles of Product Development
Flow*, 2009) as worked out by **Joshua Arnold** at Black Swan Farming:
the four **benefit buckets**, the four **urgency profiles**, the
**qualitative** first pass, and **CD3** (cost of delay divided by
duration) — articles preserved in [`./materials/`](./materials/).
**Melissa Perri** supplies the frame: prioritization is only hard
without a strategy and data. The distinction, the candidate table, the
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
date. Two things about it that teams get wrong at first (Arnold):

- **It is a rate, not a sum.** Value usually leaks away gradually, so
  cost of delay is expressed per week; a one-week delay costs a
  fraction of a ten-week delay. (Only in total-loss cases is it a lump.)
- **It has two ingredients that multiply, not add: value × urgency.**
  We conflate them — what feels urgent is treated as valuable and vice
  versa — so estimate each independently.

### 3a. Value — the four benefit buckets (Arnold)

Put every feature's value into one or more of four buckets so options
are comparable in the currency the cost side already uses:

| Bucket | What it is | Typical features |
|--------|------------|------------------|
| **Increase revenue** | New sales, new customers, more share of wallet or a bigger market — things customers will pay for; where "delighting" and disruptive features live | New capability a segment will pay for; a new segment served |
| **Protect revenue** | Revenue you already receive, kept — keeping up with competitors, removing the pain that makes customers consider switching; customers won't pay extra for it | Parity features; fixing churn drivers; "sustaining" work |
| **Reduce costs** | Costs you currently incur, cut — automation, fewer people, lower overheads | Ops automation; support deflection |
| **Avoid costs** | Costs you don't yet incur but probably will unless you act — fines, extra hires, reputational loss; usually with a probability attached | Compliance; scaling limits; risk work |

A feature's total value is the sum across buckets; the buckets are
where a "strategic" claim gets turned into a number. Arnold's caution
cuts both ways: too little economics and the system optimizes for
whatever it *can* see (usually cost and dates); too much and cost
reduction quietly degrades the customer experience.

### 3b. Urgency — the four profiles (Arnold)

How the value changes with time. Two variables decide the shape: how
long the benefits last (short or long life-cycle), and whether being
late lowers the peak.

| # | Profile | What it looks like | Where it shows up | Cost of delay behaves… |
|---|---------|--------------------|-------------------|------------------------|
| 1 | **Short life-cycle, peak affected by delay** | Benefits ramp fast, peak, and fall as the advantage becomes standard or the market moves on | Consumer electronics; fashion; anything competing on "new" | High and front-loaded: late means a lower peak *and* a shorter run |
| 2 | **Long life-cycle, peak affected by delay** | First-mover or network-effect markets that consolidate to one or two players | Platforms, standards, winner-take-most categories | High: latecomers may never recover position |
| 3 | **Long life-cycle, peak unaffected by delay** | Benefits ramp to a plateau and stay there whether you're late or not | **The most common profile in established organisations**: automation, efficiency, cost and time reduction | Constant per week — the simple parallelogram; the easiest to compute |
| 4 | **External deadline** | Any of the above, but benefits only start around a fixed date (regulation, season, a one-day event) | Compliance dates; seasonal products; event-day functionality | **Zero until the latest start date** (deadline minus duration), then the profile's rate kicks in |

Profile 4 is the one everyone mis-handles. A date does not make a
feature urgent *now*: its cost of delay is zero per week until the day
you must start to finish just in time, and only then does it acquire a
rate. Most dated items start at $0/week — which is why "coercion by
dates" is an anti-pattern and why a date with no external effect behind
it is not a deadline at all.

### 3c. Qualitative first (Arnold)

If nobody will put a number down yet, score value and urgency on two
three-point scales and combine them on a 3×3 grid. The bands are worded
to fight inflation (a "high / medium / low" scale ends with everything
high):

| Value | Meaning |
|-------|---------|
| **Killer** | The vital few: do it and we make a killing, or fail to and it may kill us. Very few items belong here |
| **Bonus** | Delighting; worth a press release; customers pay or stay; enough to "make bonus" for the year |
| **Meh** | Pocket change; keeps the lights on; nobody will rave |

| Urgency | Meaning |
|---------|---------|
| **ASAP** | Value evaporates fast if we don't deliver now — someone else gets there, or the opportunity is impaired |
| **Soon** | Value declines or risk grows over the coming weeks or months |
| **Whenever** | Total value barely affected by delay — most cost-reduction work; markets with little competition |

Killer × ASAP = very high cost of delay; Meh × Whenever = very low. Two
rules: score value and urgency **independently** (Eisenhower: what is
important is seldom urgent), and **shift urgency as dates approach** —
an item can sit at Whenever, move to Soon as the latest-start date
nears, and become ASAP just before it. Do it as a group so assumptions
get challenged and the HiPPO doesn't score alone. This is a
BACKGROUND-tier estimate; when the decision is load-bearing, surface
the assumptions and quantify.

### 3d. Duration and CD3

3. **Duration** — how long it takes to deliver, in the same time unit.
   Don't get hung up on it: T-shirt sizes, consistently applied, are
   enough; precision in the denominator is mostly wasted effort
   compared with understanding the numerator.
4. **CD3 = cost of delay ÷ duration** (Arnold). Higher first: the
   feature that returns the most value per week of scarce capacity.
   Two features with the same cost of delay are separated by duration —
   the quick one ships first because its value starts compounding
   sooner.

```
Feature                  Buckets           CoD/wk   Profile   Latest start   Duration   CD3    Decision
Recover partial import   protect + reduce   40k     3          —              4 wks     10.0   v1.0 (job-critical anyway)
Mapping presets          protect            12k     3          —              2 wks      6.0   v1.0
Scheduled re-import      reduce              9k     3          —              3 wks      3.0   v1.1
Audit log                avoid (p≈0.3)       6k     3          —              3 wks      2.0   v1.2 — revisit when p changes
Enterprise SSO           protect            30k     4          renewal − 6w   6 wks      5.0   v1.1 — start by the latest-start date
```

### Postponement rules *(repo extension)*

- **External-deadline items (profile 4) are ranked by CD3 like
  everything else, with cost of delay zero until their latest start
  date** (deadline minus duration). The latest start date is the
  constraint; it is written on the row and re-checked every planning
  cycle. Nothing is "urgent because it has a date."
- **ASAP / high-urgency claims are questioned before they are
  honoured:** which profile, evidenced how — a named customer, a
  measured churn driver, a competitor's launch? An "ASAP" with none of
  these is a stakeholder theory.
- **Avoid-cost items carry their probability** and get a revisit date;
  postponing them is a decision with an owner, not a default.
- **Whenever × Meh** work is the first to defer; but a cluster of it
  that keeps the lights on is a sustainability minimum, not postponable.
- Anything postponable with a CD3 below the team's cut line goes to
  **v1.1+**, with its cost of delay recorded so the roadmap
  conversation starts from numbers.
- A qualitative or guessed cost of delay is **BACKGROUND**; when
  capacity depends on it, quantify it or run the cheaper experiment
  that would firm it up.

## 4. The minimum feature set template

```
MINIMUM FEATURE SET — v1.0 of <option title>                     dated <date>
Option card: <link>   Launch segment: <…>   Goal metric: <…>

Core job, end-to-end: <job story> — the path v1.0 must complete:
  step 1 → step 2 → step 3 → outcome

| # | Feature / capability | Class (job-critical / adoption-critical / sustainability / postponable / speculative) | Critical success factor served | Value buckets | CoD/wk (or Killer/Bonus/Meh × ASAP/Soon/Whenever) | Profile · latest start | Duration | CD3 | v1.0? | Reason |
|---|----------------------|----------|----------|---------------|--------|---------|----------|-----|-------|--------|

In v1.0:   <list> — total duration <…>; what "lovable" means for each (end-to-end / intuitive / delightful)
Deferred:  <list with CoD and target version>; external-deadline items with their latest start dates
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
| **Everything is urgent** | All rows "ASAP" | ASAP needs a named customer, metric or competitor behind it; use the worded bands to resist inflation |
| **Latest start date ignored** | A regulatory item's cost of delay is treated as zero right up to the deadline, then it's late | Profile 4: cost of delay starts at deadline minus duration; write that date on the row and re-check it each cycle |
| **Silent deferral** | Postponed features vanish | Deferred list with CoD, target version, revisit date, owner |
| **Guessed CoD treated as fact** | Precise numbers, no source | Tier it; run the cheaper experiment if capacity depends on it |
| **Coercion by dates** | An internal date treated as a deadline; cost of delay the same before and after it | Profile 4 is zero until the latest start date; a date with no external effect is not a deadline |
| **Urgent mistaken for valuable** | "It's urgent, so it must matter" | Score value and urgency independently; Killer × Whenever and Meh × ASAP both exist |
| **Scores without data** | Stakeholders rate features 1–5, averaged into a table | Perri: a beginner's tool, and consensus is not prioritization; back every score into a bucket, a rate and a source — or set the strategy first |

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
- **Joshua J. Arnold**, *Black Swan Farming* (with **Özlem Yüce**) —
  *"Understanding Value"* (the four benefit buckets), *"Urgency
  Profiles"* (the four profiles and the latest-start-date treatment of
  external deadlines, with two worked examples), *"Qualitative Cost of
  Delay"* (Killer / Bonus / Meh × ASAP / Soon / Whenever; cost of delay
  as a rate; dates shift urgency; T-shirt durations; do it as a group),
  and CD3 (https://blackswanfarming.com/cost-of-delay-divided-by-duration/;
  the same idea appears as WSJF in SAFe). The three articles are
  preserved at `./materials/BlackSwanFarming-*.pdf` with transcriptions
  under `./materials/extracted/`.
- **Melissa Perri**, *"Prioritization Shouldn't Be Hard"*, The Produx
  Labs (Medium), 31 Oct 2019 — ranking, $100 games, MoSCoW and
  arbitrary weighted scoring are beginner tools and consensus-gathering
  is not prioritization; with a strategy and data (missed contracts,
  their size, how many similar customers exist) prioritization becomes
  easy, and cost of delay "backs out all decisions into hard dollar
  amounts." Preserved at
  `./materials/MelissaPerri-PrioritizationShouldntBeHard-2019.pdf`.
- **Gus Power** — "minimum sustainable product" (comment on Matts's MVI
  post, preserved in `./materials/`).
- The v1.0-vs-MVP table, the five feature classes, the postponement
  rules, the template and the anti-patterns are this repo's operational
  extension from **Daniel O'Rorke**'s notes ("not an MVP; v1.0; use cost
  of delay to decide what to postpone").
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

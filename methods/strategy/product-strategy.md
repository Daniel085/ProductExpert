# Product Strategy — Method Reference

*Strategy as a **deployable framework that enables action toward
desired outcomes** — not a plan. Distilled from **Melissa Perri**'s
*Escaping the Build Trap* (the strategy chapters: what strategy is, the
strategic gaps, the strategic framework, the Product Kata), which
builds on **Stephen Bungay**'s *The Art of Action* (the three gaps; the
definition of strategy) and **Mike Rother**'s *Toyota Kata* (the
Improvement Kata and the Coaching Kata — the two source pages are
preserved in [`./materials/`](./materials/)). The four-step Product
Kata summary is the PM's; the direction ladder, the strategy stack,
the level-by-level cadence table and the anti-patterns are this repo's
operational extension. The kata's *mechanics* — record template, rules
of the form, the worked seller-portal example — stay in
[`../lean-experiments/product-kata.md`](../lean-experiments/product-kata.md);
this doc is about where the **direction** comes from and how the loop
runs at every level. See [`../../CREDITS.md`](../../CREDITS.md).*

> **Where this sits.** Every agent in this system asks for a direction
> it does not create: `problem-selection` scores Business Alignment
> against a *stated goal*; `lean-experiments` opens a kata with a
> *direction*; `solution-options` fills an *Alignment* field; `metrics`
> defines the *goal metric*. This doc is where those come from. A
> strategy is the framework that lets a team decide what to work on
> without asking permission — and the Product Kata is the loop that
> keeps the framework honest at every level, from the company's vision
> to this week's experiment.

## 1. What strategy is — and what it isn't

Bungay's definition, which Perri adopts, in paraphrase: strategy is a
**deployable decision-making framework** — it enables action toward
desired outcomes, it is constrained by what the organization can
currently do, and it is coherent with the context it operates in. Every
clause is a test:

| Clause | The test | Fails when |
|--------|----------|-----------|
| **Deployable** | Can each level of the organization pick it up and decide with it? | It lives in an executive deck nobody below can act on |
| **Decision-making framework** | Does it tell a team what to say *no* to? | It is a list of everything; nothing is excluded |
| **Enables action** | Can a team start on Monday? | It is a vision statement with no next step |
| **Toward desired outcomes** | Is the outcome named and measurable? | It names features or activities instead |
| **Constrained by current capabilities** | Is it honest about what we can do now? | It assumes a team, a technology or a market position we don't have |
| **Coherent with context** | Does it fit the market, the customers, the competition as they are? | It was written for the company we wish we were |

What strategy is **not**:

- **Not a plan.** A plan is a list of features and dates. It assumes
  the path is known in advance; the Improvement Kata's first premise is
  that it can't be (*"the path to a challenging goal can't be
  determined in advance"*). Plans produce the three gaps in §2.
- **Not a vision alone.** A vision says where; strategy says what we
  will do next and how we will know it worked.
- **Not a backlog.** Prioritized features are outputs. The build trap
  (Perri) is the state of measuring success by outputs shipped rather
  than outcomes achieved; a "strategy" that is a feature list is the
  trap with a title.
- **Not consensus.** Perri's prioritization rule applies one level up:
  strategy comes from a diagnosis and a choice, not from averaging
  stakeholder wishes ([`../lean-experiments/minimum-feature-set.md`](../lean-experiments/minimum-feature-set.md)).

## 2. The three strategic gaps

Bungay found that organizations treating strategy as a plan keep
failing to get what they planned, and traced it to three gaps between
plans, actions and outcomes. Perri applies them to product
organizations. Each gap has a **wrong** fix — more detail, more
control, more reporting — that widens it, and a **right** fix that
narrows it:

| Gap | Between | What it looks like in product | The fix that widens it | The fix that narrows it |
|-----|---------|-------------------------------|------------------------|-------------------------|
| **Knowledge gap** | What we would like to know and what we actually know | Leaders write detailed plans to compensate for what nobody knows; teams execute the plan instead of learning | More planning, more detail | Leaders limit direction to the **essential intent** and its measure; teams close the gap by *learning* — research, measurement, experiments (the kata) |
| **Alignment gap** | What we want people to do and what they actually do | Teams build what they were told or what they felt like; neither connects to the intent | Cascading tasks; micromanaging the *how* | Each level **defines what it will do to achieve the intent above it** — and writes it down (§3) |
| **Effects gap** | What we expect our actions to achieve and what they actually achieve | Features ship; the metric doesn't move; nobody adjusts until the annual review | More reporting, more controls | Give people the **freedom to adjust their actions in line with the intent** — short cycles, re-measure, change course (§4) |

Perri's name for the practice that closes all three is **strategy
deployment**: intent flows down; each level decides its own *how*;
learning flows back up. It is not new — OKRs, Toyota's Hoshin Kanri
and the military's mission command are all forms of it. What they
share: **the level above states the outcome and its measure; the
level below chooses the actions.** A level that specifies the actions
of the level below has re-opened the knowledge gap (it doesn't know
enough to) and the alignment gap (the team stops thinking).

Two failure modes bracket the practice. **Direction without
autonomy** — the level above dictates features — is the classic build
trap. **Autonomy without direction** — "empowered" teams with no
stated intent — is its mirror: teams pick problems that don't add up,
and leadership takes the wheel back with a feature list. Autonomy
*requires* a stated direction; that is what strategy is for.

## 3. The strategic framework — four levels

Perri's framework is a stack of four levels, each answering *what* for
the level below and *how* for the level above. Horizons are hers,
roughly; adapt them to the business, but keep the order.

| Level | Who sets it | Horizon | What it states | Form | Example (a data-import product) |
|-------|-------------|---------|----------------|------|----------------------------------|
| **Vision** | Company leadership | 5–10 years | What the company wants to be, for whom | A sentence anyone can repeat | *Every team can trust its data the day it arrives* |
| **Strategic intents** | The executive team | 1–3 years, reviewed at least yearly | The **few** business outcomes that move the company toward the vision, each with a measure and a target | 1–3 at a time, no more; outcome + number + date + owner | *Grow revenue from self-serve workspaces 40% by end of next year* |
| **Product initiatives** | Product leadership (CPO / heads of product), with the teams | Up to a year | The **customer problems** the product will solve that, solved, move an intent — with the outcome metric each will move | A job story + a metric with baseline → target; several per intent | *New workspaces can get to a trusted first import in one session* (31% abandon at the mapping step; abandoners retain 22 pts worse) |
| **Options** | The product team | Weeks to a quarter | The **possible solutions** to an initiative's problem — bets to explore, test and, if they survive, deliver | Hypotheses with a test each; several per initiative; most die | *Import recovery flow · guided mapping · import concierge for the first week* |

Rules for the stack:

- **Every level states an outcome and its measure.** A level without
  a number is a wish; a level whose "measure" is a feature shipped is
  an output ([`../metrics/north-star.md`](../metrics/north-star.md)
  supplies the definitions).
- **A level names the *what*; the level below owns the *how*.** The
  executive team says *enterprise revenue*; product leadership decides
  *which customer problems* get there; the team decides *which
  solutions* to try. Reverse the ownership and you get the gaps.
- **Fewer is better at every level.** One vision; one to three
  intents; a handful of initiatives per intent; a few live options per
  initiative. A strategy with twelve intents is a list of departments.
- **Initiatives are problems, never features.** An initiative passes
  the same tell as a problem statement: no solution noun in it
  ([`../jtbd/job-stories.md`](../jtbd/job-stories.md)). "Ship the
  import wizard" is an option wearing an initiative's clothes.
- **Options are hypotheses until tested.** An option earns delivery
  the way a solution option does here — through a readout
  ([`../lean-experiments/solution-options.md`](../lean-experiments/solution-options.md)).
  Killing most options is the framework working.
- **The level above is the direction for the level below.** For a
  product leader the direction is the strategic intent; for a team the
  direction is the initiative. That is what step 1 of the kata reads
  (§4).
- **Every intent implies a stop-doing list.** Collins's good-to-great
  leaders were distinguished by the discipline to stop doing whatever
  didn't fit their one organizing idea (Kimberly-Clark sold its
  namesake paper mills to concentrate on consumer products). A strategic
  intent that names no initiative, product line or market the company
  will *stop* investing in has not yet said no to anything — which is
  the "decision-making framework" test in §1. Write the stop-doing
  list next to the intent; the option card's out-of-scope decision log
  is the same discipline one level down.
- **It is written down, dated and owned.** The stack in §7 is the
  minimum; if it isn't written, each level will fill the gap with its
  own version — the alignment gap by another route.

### 3b. Writing the vision

The vision is the one level that stays put while everything beneath
it adapts: a vision changes when the company changes what it wants to
be, not when a quarter misses. Perri's sentence frame (§3a) is the
minimum — *in <time frame>, <company> will be <vision statement>*.
When the vision needs to say more (for whom, against what), Mural's
guide offers the format adapted from Geoffrey Moore's positioning
statement:

```
<Product> is for <target customer> who <need or opportunity>. It is a <category>
that <key benefit>. Unlike <primary alternative>, it <primary differentiation>.
```

Two cautions on that frame. It was built for **positioning**, which
is what a product occupies in the market today; a vision is more
aspirational, so the frame is a checklist of what the sentence must
cover, not its voice. And "primary alternative" is a landscape-scan
finding (BACKGROUND), not a decision. Quality tests, from the same
guide and in this repo's terms: **purposeful** (it serves the company
vision above it), **achievable** (grounded in current capabilities —
§1's fifth clause), **aspirational** (it describes a change in
customers' lives, not a feature set), **customer-focused** (it rests on
research, not on the roadmap), **concise** (one sentence anyone can
repeat), and **written down and shared** (§6). The vision is owned by
the level that sets it and pressure-tested by the level below, which
is `ideation`'s strategy-exploration mode.

### 3c. Strong product initiatives

A product initiative is the level the PM most often writes, and the
one most often written badly (as a feature with a date). A strong one
carries five things, each traceable to an artifact:

| A strong initiative has… | Which means | Traced to |
|--------------------------|-------------|-----------|
| **A clear connection to the current-state analysis** | It answers a gap or pain the picture in §6a shows — this segment, this step, this shortfall | The memo's current-state areas; the segmentation's biggest current-versus-desired gap |
| **Quantified business value** | The intent's metric it moves, by how much, worth what — an estimate with its formula and tier (§3d) | The value estimate block; the problem case's Business Alignment |
| **Evidence-based reasoning** | Why we believe solving this problem moves that metric — sources converging, confidence per row | The problem case's evidence table and verdict (*Yes*) |
| **Defined success metrics** | One to three metrics with definition cards, baselines, targets, dates and a counter-metric | `metrics`' definition cards; the option's success metrics |
| **Measurable customer outcomes** | What the customer will be able to do, or stop doing, that they can't today — observable in their world | The job story and the behaviour-change field ([`../lean-experiments/solution-options.md`](../lean-experiments/solution-options.md)) |

Two rules govern the set of initiatives, not just each one. **Focus**:
a handful per intent, so that resources are concentrated rather than
spread thin — an initiative list that includes everything the teams
are already doing is a status report, not a strategy, and the
stop-doing list (§3) is how focus is enforced. **Periodic update**:
initiatives are not set in stone; they are re-read against the
current state every cycle at their level (§4's cadence), and one that
has met its target, or whose current condition refuses to move after
honest cycles, is retired or rewritten — with the change and its
reason in the deployment log. An initiative that survives every
planning season unchanged has usually stopped being read.

### 3d. Quantifying an initiative's business value

"Quantified business value" is where most initiatives go soft — an
adjective ("strategic", "big") where a number should be. The
procedure, from Carter's quantification method, Arnold's benefit
buckets and the SaaS lever model, tiered like everything else:

**1. Name the lever.** Which business outcome the initiative moves,
in the terms the strategic intent is written in. For a revenue
business the four levers are **acquire** new customers, **expand**
revenue from existing ones, **reduce churn**, and **price** better;
they interact (activation cuts churn and unlocks expansion), so name
the primary one. In Arnold's buckets these are *increase revenue* and
*protect revenue*; for an internal tool the levers are *reduce costs*
and *avoid costs* ([`../lean-experiments/minimum-feature-set.md`](../lean-experiments/minimum-feature-set.md)).
Growth quality matters as much as growth: net revenue retention and
revenue churn (not logo churn) are the honest reads of a retention or
expansion initiative.

**2. Walk the metric ladder down to a number you can move.** Carter's
distinction keeps the terms straight — the **North Star** (what the
organization must achieve), the **objective** for the period (the
intent's target), the **goal** (what we want users to do), the
**signal** (user actions that show it happened), the **primary
metric** (how the signal is captured in data — one, at most two per
initiative), and the **hypothesis** (the expected change) with its
**supporting data**. A signal (visits to the pricing page) tells you
about engagement; a primary metric (payments received) tells you about
business impact. Initiatives are judged on primary metrics.

**3. Estimate the impact with the formula written down.** The shape,
from Carter, for a revenue lever:

```
expected impact = expected lift on the primary metric
               × share of the business that metric touches (segment · surface · plan)
               × baseline value (last period's revenue, or the metric's dollar value)
               × horizon (growth rate, or years of recurring revenue for a retention lever)
```

For an internal tool, the cost-side shape from Retool's analysis:

```
cost of building  = engineer $/hour × hours to build and to maintain over the horizon
value delivered   = hours saved per person per period × people × loaded $/hour
                  + errors avoided × cost per error
                  + revenue protected (renewals, orders) that the tool makes visible in time
```

Every factor is a row with a source and a tier: the baseline from the
metric tree (CONFIRMED), the share from segmentation (CONFIRMED or
INFERRED), the lift from a readout (CONFIRMED) or from a comparable
case and a guess (BACKGROUND). **An estimate is BACKGROUND until a
readout replaces the lift.** Write the estimate anyway — the tier is
what keeps it honest, and a strategic intent's target cannot be
allocated across initiatives without one.

**4. Discount for the four oversights.** Carter's list, which
`experimentation`'s trust checks catch after the fact and this step
anticipates: **side effects** (the metric rose and cannibalized
another product or plan); **short versus long term** (the lift
decayed — novelty, or a behaviour merely pulled earlier in the
lifecycle, which cohorts reveal); **vanity** (clicks moved, the
primary metric didn't); **attribution** (three other changes shipped
the same week). Her rule of thumb: expected impact rarely matches
actual — "two plus two equals three" — so the estimate carries a
range, not a point.

**5. Write it where the initiative lives.** The stack row (§7) and the
memo's part 3 carry the estimate; the problem case's Business
Alignment score is its qualitative twin; `solution-options` reuses
the same value and urgency numbers as the cost-of-delay rate when it
cuts v1.0. Nothing is quantified twice.

```
VALUE ESTIMATE — PI-<n>                                        as of <date>   tier: <BACKGROUND / INFERRED / CONFIRMED>
Lever:           <acquire / expand / retain / price · or reduce cost / avoid cost / protect revenue>
Primary metric:  <name · definition>   baseline <n>   signal(s) it rests on: <…>
Expected lift:   <range>   source: <readout · comparable · guess>
Share touched:   <segment · surface · plan> = <%>   source: <segmentation>
Baseline value:  <$ / period>   source: <metric tree>
Horizon:         <growth rate · months of recurring revenue · tool lifetime>
Expected impact: <range, $ / period>   formula: <as above>
Discounts:       side effects <…> · decay <…> · vanity check <…> · attribution <…>
Compare to:      <cost — engineering hours × $/hour, or cost of delay>
```

### 3a. Where the levels came from — Perri's 2016 canvas

Two years before the book, Perri wrote the same stack with kata
vocabulary (*"What is Good Product Strategy?"*, 2016 — preserved in
[`./materials/`](./materials/)). It is worth knowing because the agents
meet PMs who learned it in this form, and because it shows the stack
*is* the kata:

| 2016 canvas | What it is | Book-era level |
|-------------|-----------|----------------|
| **Vision** | The long-term, qualitative direction of the company or business line — competitors, how customers will see you, expansion | Vision |
| **Challenge** | The first business goal on the way to the vision; which part of the customer journey or funnel to optimize first; broad, may be qualitative or quantitative | Strategic intent |
| **Target condition** | The challenge broken into achievable, measurable metrics; the team should *not* yet know how to reach it, only where to start looking | Product initiative's target (and the option-level target condition beneath it) |
| **Current state** | Measured and quantified before work on the target condition starts | The current condition, at every level |

Her definition then: product strategy is *a system of achievable goals
and visions that work together to align the team around desirable
outcomes for both the business and the customers* — and it **emerges
from experimentation toward a goal**; a list of features, products and
platforms is "communicated at the wrong time and with the wrong
intentions," since it is a plan, and plans fail because they assume
away uncertainty. Ownership by level, in her words: executives set the
vision; the next level of management (a VP of product per journey or
business line) sets the challenge; direct managers help teams set
target conditions, handed down at first and set together once the
habit forms; the product manager and team find the customer problems
and obstacles in the way and experiment to remove them. Her worked
example (Uber, hypothetical beyond the CEO's stated vision): vision —
the cheap, efficient alternative to owning a car or taking public
transport; challenge — cut average wait times in cities where they
exceed ten minutes to under five, by a date; target condition — one
driver onboarded per fifty residents in each city, by an earlier date;
current state — one driver per three hundred residents, measured
before anything is built. And the answer to "this is a business
strategy, not a product strategy": *product management is the art of
solving your customer's problems to reach your business objectives* —
a strategy that does only one of the two is either a wish list or a
spreadsheet.

Her one-page **Product Strategy Canvas** writes the four as sentence
frames, which is a useful forcing device when a level resists being
pinned to a number:

```
VISION            In <time frame>, <company / division> will be <vision statement>.
CHALLENGE         In order to reach our vision, we need to <measurable objective> by <date>.
TARGET CONDITION  In order to reach our challenge, we first need to <measurable objective, dated>.
CURRENT STATE     After measuring, we know our current state is <measurement>.
```

The stack template in §7 is this canvas with the two levels the book
added (intents may be several; initiatives are problems with metrics)
and the option layer beneath.

## 4. The Product Kata — the loop at every level

The framework says *what* each level owns. The **Product Kata** is
*how* each level works toward it: Perri's adaptation of Rother's
Improvement Kata, a four-step model of scientific thinking practised
until it is a habit. Three phrasings of the same four steps:

| # | Rother — Improvement Kata | Perri — Product Kata | The PM's summary (this repo) |
|---|---------------------------|----------------------|-------------------------------|
| 1 | Understand the direction or challenge | Understand the direction | **Understand the direction** — get clear on the strategy set by the level above |
| 2 | Grasp the current condition | Analyze the current state | **Analyze the current state** — know where you are, through research and data |
| 3 | Establish the next target condition | Set the next goal | **Set the next goal** — define the product initiatives (or the option's goal) that move the level above |
| 4 | Experiment toward the target condition | Choose the step of the product process; plan it, take it, evaluate | **Execute or deploy** — run experiments, deliver solutions, or communicate the strategy |

Rother's premise, worth keeping verbatim in spirit: scientific thinking
is *comparing what you think (theory) with what actually happens
(evidence) and adjusting on the difference* — and it is **not our
default**; our brains jump to conclusions, so the pattern has to be
practised. The kata is that practice. The seven-step operational form
and the record template are in
[`../lean-experiments/product-kata.md`](../lean-experiments/product-kata.md);
what follows is what each step means for *strategy*.

### Step 1 — Understand the direction

Get clear on the strategy set by the level above. "Clear" has a test:
you can write, in one line each, **the outcome the level above wants,
its measure and target, its horizon, and why now** — and the owner of
that level would sign it. Write it as the top of the **direction
ladder** (§7): vision → intent → initiative, down to the level you are
working at.

- The direction is **lofty by design** (Perri: you may never reach a
  challenge exactly; you get as close as you can). Don't shrink it into
  something achievable; that's what target conditions are for.
- **If the level above hasn't stated it, that is the first obstacle**
  — not a licence to invent it. Get it written, with its owner; the
  `metrics` agent defines the measure, `ideation`'s
  strategy-exploration mode helps a leader articulate the choice. A
  team that invents its own direction has automated the alignment gap.
- Direction comes with **constraints** (capabilities, context — §1's
  last two clauses). Record the real ones; classify the rest as
  preferences ([`../jtbd/requirements-are-hypotheses.md`](../jtbd/requirements-are-hypotheses.md)).

### Step 2 — Analyze the current state

Know where you are — with a number, not a feeling — relative to the
direction. At the strategy level this is research *and* data:

- **The measure now.** The level above's metric, today, and its trend.
  If it can't be measured, the first cycles are measurement (Perri's
  seller-portal kata counted calls for three cycles before changing
  anything; "unknown" is a legitimate current condition and the first
  obstacle).
- **The product now.** What it does, for whom, how well — the metric
  tree's inputs ([`../metrics/north-star.md`](../metrics/north-star.md)),
  the retention curve, the funnel.
- **The customer now.** How they get the job done today, what they
  fire and hire, where the pain concentrates — Track 1 synthesis and
  Track 2 opportunity scores are current-condition artifacts.
- **What we don't know.** At the initiative level the
  five-area knowledge-gap scorecard
  ([`../problem-selection/knowledge-gaps.md`](../problem-selection/knowledge-gaps.md))
  *is* the current-condition tool: it says which unknown is the
  biggest obstacle.

The discipline most teams skip is this step. Strategy set without a
current condition is a plan; the kata's insistence on it is what makes
the strategy adaptive.

### Step 3 — Set the next goal

Establish the **next target condition**: a measurable intermediate
state, dated, on the way to the direction — not the direction itself.
What it is depends on the level:

| Level you work at | Direction (from above) | The next goal you set |
|-------------------|------------------------|-----------------------|
| Executive team | The vision | This period's strategic intents, with targets |
| Product leadership | A strategic intent | The product initiatives that, solved, move it — each with a metric and a target for the year |
| Product team | A product initiative | The option's goal: the intermediate state an experiment or a delivery should produce this cycle (sellers call < 2×/week; mapping-step abandonment < 15%) |

Rules: a target condition has a **number and a date**; it is
**achievable from the current condition in a few cycles**, not a
restatement of the challenge; and it is **chosen by the level that
will pursue it**, in view of the level above (closing the alignment
gap is exactly this act). When product leadership sets initiatives,
the candidates are *problems* with evidence — which is why
`problem-selection` ranks them on Business Alignment against the
intent ([`../problem-selection/picking-the-right-problem.md`](../problem-selection/picking-the-right-problem.md)).

### Step 4 — Execute or deploy

Move toward the target condition through short, measured steps. Perri
splits the step into choosing **which part of the product process the
current obstacle calls for**, then planning, taking and evaluating the
step:

| The current obstacle is… | The step is in… | Runs as |
|--------------------------|-----------------|---------|
| We don't understand the problem (who, why, how painful) | **Explore the problem** | `customer-interviews`, the ODI pipeline, `problem-selection` (root cause) |
| We don't know if this solution delivers | **Explore the solution** | `lean-experiments` — the obstacle → test table in [`../lean-experiments/pre-build-experiments.md` §4b](../lean-experiments/pre-build-experiments.md) |
| The solution works; the number isn't there yet | **Optimize the solution** | `solution-options` (v1.0 scope), `experimentation` (A/B), delivery |
| The level below doesn't know the direction | **Communicate the strategy** — deployment | The strategy stack (§7) written, shared, and the level below's kata opened against it |

The fourth row is why the PM's summary says *execute **or deploy***: at
the strategy level, the step is often not an experiment but an act of
communication — the intent, its measure and its *why*, written so the
next level can set its own target condition. A strategy that has not
been deployed has not been executed.

Each step is planned with a **prediction** (what do you expect?),
taken, and **evaluated** against it (what actually happened? what did
you learn?) — the coaching kata's back-of-card questions (§5). Then
**re-measure the current state and repeat**: target met → set the next
target condition; not met → the next obstacle. The loop never ends; a
strategy is re-planned when the evidence says so, not when the
calendar does.

### Cadence by level *(repo extension)*

| Level | The kata cycle | Coaching cycle |
|-------|----------------|----------------|
| Vision | Revisited when intents keep being met or keep missing — years | — |
| Strategic intents | Set yearly; current condition re-read quarterly; changed when the evidence demands, not on a schedule | Quarterly review of intent progress with product leadership |
| Product initiatives | Set for the year; a cycle a quarter — re-measure the initiative's metric, pick the next obstacle | Monthly: the head of product asks the five questions of each initiative owner |
| Options | Cycles of a week or two, per the kata record | Weekly (or daily during an experiment): the PM and the team on the kata record |

The horizons nest: an option cycle's *learned* updates the initiative's
current condition; an initiative's *target met* updates the intent's.
Learning flows up the same ladder the direction came down.

**The flywheel and the doom loop (Collins).** The cadence has a
failure mode at the intent level that Jim Collins named from his
good-to-great study: the **doom loop** — disappointing results lead to
reaction without understanding, which leads to a new direction (a new
leader, a new program), which leads to no momentum, which leads to
disappointing results. His comparison companies changed strategic
direction roughly once per CEO and never built momentum; the companies
that made the leap pushed one heavy **flywheel** in one direction,
turn after turn, with no single breakthrough moment anyone could date,
until the accumulated momentum carried it. Two rules for the stack
follow. **Re-plan an intent on evidence, not on one bad reading**: a
missed target condition is the kata's normal case (next obstacle), and
only a current condition that keeps refusing to move after honest
cycles is grounds to change the intent. And **keep the direction long
enough to learn**: an intent replaced every planning season never gets
its current condition measured twice. The flywheel is not an argument
against changing course — the effects gap says adjust — it is an
argument for changing *steps* fast and *direction* slowly, on what the
steps taught you.

## 5. The Coaching Kata — the check-in

Rother's second kata is for the person **above** the learner. Without
it, people practise the wrong pattern or drift back to jumping to
conclusions. One **coaching cycle**: the coach asks the five questions
of the learner, who answers from their storyboard — once a day at a
scheduled time (plus as needed), **twenty minutes or less**. The five
questions are headings; after each, the coach asks clarifying
questions.

**Front of the card — the five questions:**

1. What is the **target condition**?
2. What is the **actual condition** now?
   *— turn the card over: reflect on the last step —*
3. What **obstacles** do you think are preventing you from reaching
   the target condition? Which **one** are you addressing now?
4. What is your **next step** (next experiment)? What do you
   **expect**?
5. **How quickly** can we go and see what we have **learned** from
   taking that step?

**Back of the card — reflect on the last step taken** (*"because you
don't actually know what the result of a step will be"*):

1. What did you **plan** as your last step?
2. What did you **expect**?
3. What **actually happened**?
4. What did you **learn**?

…then return to question 3, and have the learner state the obstacle
being worked on. In plain words the pattern is: *what are we trying to
achieve · where are we now · what's in our way · what's our next
experiment and what do we expect · when can we see what we learned.*

Rules of the coaching cycle that carry straight into product work:

- **The two purposes:** reinforce the pattern, and **make the
  learner's current thinking visible** so the coach can give feedback
  — like asking a music student to play a few bars. The coach's
  feedback is on the *thinking*, not the answer.
- **The storyboard is the artifact.** Rother's board has six fields —
  *focus process · challenge · target condition (achieve by) · current
  condition · experimenting record · obstacles parking lot* — which map
  onto the kata record in
  [`../lean-experiments/product-kata.md` §4](../lean-experiments/product-kata.md).
  The learner points at the board; nothing is recalled from memory.
- **Find the threshold of knowledge.** When the learner reaches the
  edge of what they actually know — at any question — go straight to
  question 4: the next step is to *find out*, not to guess. This is
  the kata's version of "an unknown is an obstacle."
- **Practise the Starter Kata exactly as written first.** Read the
  card as printed until the pattern is automatic; adapt it only once
  it is, and keep the core pattern intact. Teams that "improve" the
  questions before they've run them lose the reflection step first.
- **A second coach** watches the coach. In a product organization the
  level above coaches the level below — the head of product coaches
  initiative owners; the PM coaches the team's option cycles — and
  someone occasionally coaches the coach.

In this system the agents ask the questions: `lean-experiments` runs
the cycle on the kata record; `/navigate status` is the storyboard
read-back for an initiative; the reflection block in the record
template ([`../lean-experiments/product-kata.md` §4](../lean-experiments/product-kata.md))
is the back of the card.

## 6. Communicating the strategy

Deployment *is* communication, and what gets communicated decides
which gap opens. Communicate **intent and its measure**, not the
actions — and communicate it in a form the next level can decide with:

- **Down:** the stack (§7). Each level reads the row above it as its
  direction and writes its own row beneath. The *why* travels with the
  *what*: an intent without its reasoning is a quota.
- **Across:** the initiative's direction ladder in its `STATUS.md`
  header and at the top of its kata record, so every agent and every
  reader sees which intent this work serves.
- **Up:** the current condition and what was learned — the kata's
  *learned* lines, the readouts, the *target met?* answers. Leaders
  re-plan on this, not on status colours.
- **The roadmap is a communication device for strategy, not a
  commitment device for features.** Perri's living roadmap carries,
  per item: the **theme** (the initiative it serves), the
  **hypothesis**, the **goal and success metrics**, the **stage** the
  work is in (exploring the problem · exploring solutions · building ·
  released), and the few real milestones. Dates belong to the
  external-deadline items with a latest start date
  ([`../lean-experiments/minimum-feature-set.md`](../lean-experiments/minimum-feature-set.md)),
  not to every row.

The tell for a strategy communicated as a plan: the level below can
recite the features and not the outcome. Ask any team what their
initiative's metric is and where it stands today; if the answer is a
feature name, the knowledge gap is open at that level.

### 6a. The product strategy memo

The written form of a product's strategy is a **two-to-three-page
memo** with three parts — the stack of §3 in prose, with the middle
part expanded:

1. **Product vision** — where we want to go: the vision sentence, the
   strategic intent(s) this product serves, and why.
2. **Current state** — where we are, as a *picture* rather than a
   number (below).
3. **Product initiatives** — what we will do to get there: the
   problems we will solve, each with its metric, baseline and target,
   and the intent it serves. Problems, not features; a memo whose
   third section is a feature list is a plan with a vision stapled on.

Narrative, not slides, for the same reason the PR/FAQ is
([`../prfaq/working-backwards.md`](../prfaq/working-backwards.md)):
prose forces the reasoning between the three parts to be written
down, and a memo can be reviewed in a silent read.

**A strong current-state analysis creates a picture.** It analyzes
and documents six things, and in this system each one is an artifact
another agent already produces — the memo assembles them, it does not
re-derive them:

| Current-state area | The question it answers | Supplied by |
|--------------------|-------------------------|-------------|
| **Current performance of the product** | The North Star and its inputs, now and trending; retention cohorts; the initiative metrics' baselines | `metrics` — the metric tree and cohort reads ([`../metrics/north-star.md`](../metrics/north-star.md)) |
| **Different user segments** | Who uses it, defined by behaviour and need, described by the attributes that discriminate; sizes; which segments show markedly different outcomes, what the most successful users do, and where the biggest gap between current and desired behaviour sits | [`../jtbd/segmentation.md`](../jtbd/segmentation.md) — the five data questions; ODI needs-based segments where a survey exists |
| **Customer pain points and opportunities** | What the segments struggle with and what they would value; which problems have evidence and which are *Not yet* | `problem-selection` cases and ranking; Track 1 synthesis; Track 2 opportunity scores |
| **Strengths and weaknesses of the product** | What it does well enough to build on and where it loses — in the customer's terms (jobs done well vs. badly), not the team's | The value proposition's evidenced gains and pains ([`../jtbd/value-proposition.md`](../jtbd/value-proposition.md)); satisfaction scores; the knowledge-gap scorecard's user-behaviour area |
| **Competitive positioning** | Who else solves the job, how, at what price, where they fall short, and whether our wedge is a product or a feature | `ideation`'s landscape scan at teardown depth ([`../problem-selection/knowledge-gaps.md` §3](../problem-selection/knowledge-gaps.md)) — BACKGROUND |
| **Market and technology trends** | What is changing in the context the strategy must be coherent with (§1's last clause): buyer behaviour, regulation, platforms, capabilities that just became cheap | The landscape scan's sources; the PR/FAQ's market FAQs — BACKGROUND until a customer confirms it |

**There won't be perfect information.** The picture is drawn from
what exists today, tiered (CONFIRMED / INFERRED / BACKGROUND), and
every area with thin evidence is written as a **knowledge gap with its
move** — then the memo moves on. This is the kata's current-condition
rule at product level: "unknown" is a legitimate value and the first
obstacle, and a memo held back until the picture is complete is a
memo that never ships. The knowledge-gap scorecard
([`../problem-selection/knowledge-gaps.md`](../problem-selection/knowledge-gaps.md))
is the natural appendix: five scores per initiative, evidence-cited,
with the lowest area's move named.

Rules for the memo: one per product or business line, dated and
owned; it cites artifacts rather than restating them; the initiatives
in part 3 pass the job-story tells and carry numbers; the gaps are
listed, not smoothed over; and it is re-issued when the current state
changes the initiatives, not on a calendar. `prfaq`'s critique mode
reviews it as a document — the six tests of §1, the gap-and-move rule,
and the no-feature-list rule are the review bar.

## 7. Templates *(repo extension)*

### The strategy stack

One page for the whole product organization; dated; owned per row.
Lives outside any single initiative — `strategy/strategy.md` next to
`initiatives/`, or wherever the PM keeps it — and every initiative's
direction ladder cites it.

```
STRATEGY STACK — <company / product>                            as of <date>

VISION (<owner>, horizon <years>)
  <one sentence: what we want to be, for whom>

STRATEGIC INTENTS (<owner>, reviewed <cadence>)         ≤ 3
  SI-1  <business outcome>  ·  measure <metric: definition>  ·  now <n>  →  target <n> by <date>
        why now: <one line>
  SI-2  …

PRODUCT INITIATIVES (<owner>, this year)                 a handful per intent, problems not features
  PI-1  serves SI-<n>
        problem:  When <situation>, I want to <motivation>, so I can <outcome>.   (job story; no solution noun)
        measure:  <metric> baseline <n> → target <n> by <date>
        evidence: <problem case · verdict · date>            gaps: <scorecard areas < 3>
        value:    <lever · expected impact range · tier>     (value estimate, §3d)
        customer outcome: <what they can do or stop doing, observable>
        current condition: <the number now, as of <date>>    next target condition: <n by date>
  PI-2  …

OPTIONS (<team>, this quarter)                           hypotheses; status per option
  OP-1  under PI-<n>   We believe <solution> will <outcome> for <segment>, moving <metric>.
        status: exploring problem / testing solution / delivering / killed (<reason>) / parked
        last readout: <card · result · date>
  OP-2  …

Deployment log
  <date> · <level> · <what changed and why — the learning that changed it>
```

### The product strategy memo (2–3 pages)

Lives with the stack — `strategy/strategy-memo.md` next to
`strategy/strategy.md` — and cites the initiative folders for its
evidence.

```
PRODUCT STRATEGY MEMO — <product / business line>            as of <date>   owner <name>

1. PRODUCT VISION — where we want to go
   <vision sentence>. Serves strategic intent(s) SI-<n> <outcome · measure · target · date>.
   Why this, why now: <one paragraph>.

2. CURRENT STATE — where we are
   Performance:        <North Star + inputs, now and trend; cohorts>            (metrics/…)
   Segments:           <behaviour-defined segments, sizes, discriminating attributes> (segmentation)
   Pains & opportunities: <top problems with verdicts; Not-yet list>           (problems/problems.md)
   Strengths & weaknesses: <jobs done well / badly, in customer terms>        (value proposition; scores)
   Competitive positioning: <alternatives, how, price, gaps; product or feature wedge> (scan — BACKGROUND)
   Market & technology trends: <what is changing that the strategy must fit>  (scan — BACKGROUND)
   Knowledge gaps:     <area → what we don't know → the move and its owner>    (gap-scorecard.md)

3. PRODUCT INITIATIVES — what we'll do to get there
   PI-1  <problem as job story> · <metric> baseline <n> → target <n> by <date> · serves SI-<n>
         evidence <case · verdict> · options in play <OP-…> · what we stop doing <…>
   PI-2  …

Appendix: knowledge-gap scorecards per initiative; the stack; the deployment log.
```

### The direction ladder (per initiative)

The top of an initiative's kata record and the *Direction* row of its
`STATUS.md` header. It is the initiative's answer to kata step 1.

```
DIRECTION — <initiative>                                          as of <date>
  Vision:               <sentence>
  Strategic intent:     SI-<n> <outcome · measure · target · date · owner>
  Product initiative:   PI-<n> <problem as job story · measure · baseline → target · owner>
  This initiative is:   <the initiative itself / one option under PI-<n>>
  Constraints (real):   <capability, context — verified>
  Why now:              <one line>
  Level above signs:    <name · date>      ("not stated → get it written" is a legitimate value, and the first obstacle)
```

## 8. Where it plugs in

| Agent / skill | What it takes from here | What it gives back |
|---------------|-------------------------|--------------------|
| **navigate** | Fills the `STATUS.md` header's *Direction* row from the ladder (or "not stated") when it scaffolds an initiative | Reports an initiative with no stated direction as its first blocker |
| **ideation** (strategy exploration) | The stack's levels and the tells in §1, to pressure-test an intent, an initiative or a big bet; the gaps in §2 to diagnose why a strategy isn't landing | Candidate intents or initiatives as options in the ledger — untested, BACKGROUND |
| **problem-selection** | The strategic intent as the *stated goal* Business Alignment is scored against; product initiatives are the *Yes* problems that rank highest against it | The ranked initiatives with their evidence; *Not yet* problems as the learn list beneath an intent |
| **metrics** | The measure every level must carry: vision and intents map to the North Star and its tree; initiatives to input metrics; options to the success metrics on their cards | Definition cards, baselines, counter-metrics per level; the goal metric a kata needs before cycle 1 |
| **lean-experiments** (kata mode) | Step 1's direction ladder; step 3's target condition at option level; step 4's choice of product-process step | The cycle's *learned* and re-measured current condition, which flow up the ladder |
| **solution-options** | The *Alignment* field names the initiative and the intent, not "strategic" | A chosen option's success metrics as the initiative's next target condition |
| **prfaq** | The internal FAQ's strategy-fit answer cites the intent and initiative by name; the vision paragraph is the level-above sentence; in critique mode, reviews the product strategy memo (§6a) against the six tests, the gap-and-move rule and the no-feature-list rule | "What we'd need to believe" entries that are strategy-level assumptions go back to the stack's deployment log |
| **experimentation** | An OEC that is the initiative's measure | A causal readout on the intent's input metric |

Roadmap: the README's **strategy stress-tester** (Rumelt's kernel —
diagnosis, guiding policy, coherent actions) would critique a written
stack; this doc is the input it needs, not a substitute for it.

## 9. Anti-patterns (coach's tells)

| Anti-pattern | Tell | Fix |
|--------------|------|-----|
| **Strategy as a feature plan** | The "strategy" is a roadmap of features with quarters | Rewrite each row as the outcome it is meant to move; the features become options under it |
| **Direction as target** | The next goal *is* the vision ("be the leader in…") | Set an intermediate, measurable target condition reachable in a few cycles |
| **Intents by the dozen** | Twelve strategic intents, one per department | ≤ 3; the rest are initiatives or operations |
| **Cascading tasks** | The level above hands the level below a to-do list | The level above states the outcome; the level below writes its own *how* (alignment gap) |
| **Autonomy without direction** | "Empowered" teams; no written intent; leadership later takes the wheel back with a feature list | Write the stack; deployment before autonomy |
| **Skipping the current state** | Intents set with no baseline; initiatives with no number | Cycle 1 is measurement; "unknown" is the obstacle |
| **Roadmap as promise** | Every row has a date; none has a hypothesis or a stage | Theme · hypothesis · metric · stage; dates only on external deadlines |
| **Options committed, not tested** | The initiative's option is already a project with a team | An option is a hypothesis with a card until a readout says otherwise |
| **Inventing the level above** | The team writes its own "strategic intent" because none was stated | Get it written with its owner's signature; that *is* the first step of the kata |
| **Kata theatre** | The five questions are asked; the last step is never reflected on | Turn the card over: planned · expected · actually happened · learned, every cycle |
| **Annual strategy, never re-measured** | The intent's number was read once, at planning | Current condition re-read every cycle at every level; re-plan on evidence |
| **The doom loop** | One bad quarter → a new direction, a new program, a new leader; the flywheel never completes a turn | Change *steps* fast and *direction* slowly; an intent is replaced only when its current condition refuses to move after honest cycles (Collins) |
| **No stop-doing list** | The intent adds a focus without removing one; every existing initiative survives | Name what the intent stops; the level below inherits it as out-of-scope with a reason |
| **The enterprise trap** | A big contract dictates the roadmap; initiatives become one customer's feature list | An initiative is a problem with breadth under the goal reading, not an account's asks; treat the contract's asks as requirements-to-trace (Atlassian's lesson; [`../jtbd/requirements-are-hypotheses.md`](../jtbd/requirements-are-hypotheses.md)) |
| **Adapting the kata before practising it** | "Our version" of the questions, before anyone has run a coaching cycle | Practise the Starter Kata as written until it is a habit; then adapt, core intact |
| **The memo that waits for perfect information** | "We can't write the current state until the research is done" | Draw the picture from what exists, tiered; list each gap with its move; ship the memo and re-issue it |
| **A current state with no picture** | Part 2 is one metric and an adjective | Six areas, each cited to an artifact or marked a gap |

## 10. Worked example (short)

A data-import product; the team owns onboarding.

- **Direction (step 1).** Vision: *every team can trust its data the
  day it arrives.* Intent SI-1: *grow self-serve workspace revenue 40%
  by end of next year* (CFO owns; measure: self-serve ARR). Initiative
  PI-1 under it, set by the head of product with the team: *new
  workspaces reach a trusted first import in one session* — measure:
  90-day retention of new workspaces, baseline 41% → target 55% by Q4.
  The team's own work is one option under PI-1.
- **Current state (step 2).** 31% of imports abandon at the mapping
  step; abandoners retain 22 points worse (funnel, confidence 5); six
  of eight interviewees re-entered data after a partial failure
  (qualitative, 4); the knowledge-gap scorecard scores *user behavior*
  at 2 — nobody has watched the recovery workaround.
- **Next goal (step 3).** Target condition for the quarter:
  mapping-step abandonment below 15% for workspaces created after the
  change, measured weekly. Not "retention 55%" — that is the
  initiative's target, one level up.
- **Execute (step 4).** The current obstacle is a knowledge gap (area
  2), so the step is *explore the problem*: five recovery-path
  observation sessions this week (`customer-interviews`), expected to
  show re-entry from scratch; learned: most users re-import the whole
  file and lose their mapping. Next cycle's obstacle is a solution
  question → a Wizard-of-Oz card for the recovery flow
  (`lean-experiments`). Each cycle's *learned* updates PI-1's current
  condition; at quarter's end the head of product asks the five
  questions of PI-1, and the intent's owner reads PI-1's number as
  part of SI-1's current condition.

## Sources & materials

- **Melissa Perri**, *Escaping the Build Trap: How Effective Product
  Management Creates Real Value* (O'Reilly, 2018) — Part IV,
  "Strategy" (what strategy is; strategic gaps; creating a good
  strategic framework; company-level vision and strategic intents;
  product vision and portfolio) and Part V's chapter on the Product
  Kata; the living roadmap's fields from the communication chapters.
  A published book — **paraphrased; nothing quoted**; the Marquetly
  worked example is not reproduced. Her earlier blog post is preserved
  at `../lean-experiments/materials/MelissaPerri-TheProductKata.pdf`.
- **Melissa Perri**, *"What is Good Product Strategy?"*,
  melissaperri.com, 14 Jul 2016 — the pre-book canvas (vision ·
  challenge · target condition · current state), the definition, the
  ownership by level and the Uber example in §3a; she marks the post
  as superseded by the book. Source:
  `./materials/MelissaPerri-WhatIsGoodProductStrategy-2016.pdf`;
  transcription under `./materials/extracted/`.
- **Stephen Bungay**, *The Art of Action: How Leaders Close the Gaps
  between Plans, Actions and Results* (Nicholas Brealey, 2011) — the
  knowledge, alignment and effects gaps, their mission-command
  remedies, and the definition of strategy as a deployable
  decision-making framework that Perri adopts. Cited via Perri; not
  reproduced.
- **Mike Rother**, *The Improvement Kata* and *The Coaching Kata* —
  pages 1 and 2 of the Toyota Kata website (University of Michigan),
  and the *5Q Card* deck linked from them. Sources:
  `./materials/ToyotaKata-Rother-TheImprovementKata.pdf`,
  `./materials/ToyotaKata-Rother-TheCoachingKata.pdf`,
  `./materials/ToyotaKata-Rother-5Q_Card.pdf`; transcriptions under
  `./materials/extracted/`. The four-step model, scientific thinking
  as a practised habit, the Starter Kata, the five questions and the
  back-of-card reflection, coaching-cycle rules and the storyboard
  fields are his; the books are *Toyota Kata* (McGraw-Hill, 2009) and
  *The Toyota Kata Practice Guide* (McGraw-Hill, 2017).
- **Kazuo Ichijo & Ikujiro Nonaka**, *Knowledge Creation and
  Management: New Challenges for Managers* (Oxford University Press,
  2006), p. 25 — the excerpt on a firm-specific *kata* as a knowledge
  asset, quoted on Rother's page and transcribed with it.
- **Jim Collins**, *"Good to Great"*, Fast Company, October 2001
  (republished at jimcollins.com) — the flywheel effect and the doom
  loop, the stop-doing list, and the finding that transformations had
  no datable breakthrough moment; from the study behind *Good to Great*
  (HarperBusiness, 2001). The hedgehog concept, Level 5 leadership and
  "first who, then what" are company-leadership material and are
  cited, not distilled. Source:
  `./materials/JimCollins-GoodToGreat-FastCompany-2001.pdf`;
  transcription under `./materials/extracted/`.
- **HubSpot**, *"Why it's Time to Replace your Funnel with a
  Flywheel"* (hubspot.com/flywheel) — the flywheel as a growth model
  (attract · engage · delight; force and friction), after James Watt's
  mechanism. Read for the force/friction vocabulary; not preserved,
  since the North Star tree's inputs already carry the same
  decomposition.
- **Brooke Carter**, *"How Product Managers Can Effectively Quantify
  Business Impact"*, Built In, 8 Jan 2021 — the metric vocabulary
  (North Star · OKR · goal · signal · primary metric · hypothesis ·
  support data), one or two primary metrics, the revenue-impact
  formula (lift × share of revenue × annual revenue × growth rate),
  the four oversights (side effects, short vs. long term, vanity,
  attribution) and "two plus two equals three" (novelty; behaviour
  pulled earlier in the lifecycle; track cohorts). Source:
  `./materials/BuiltIn-HowPMsQuantifyBusinessImpact-Carter-2021.pdf`;
  transcription under `./materials/extracted/`.
- **Allie Beazell**, *"The cost-benefit analysis of internal tools"*,
  Retool Blog, 24 Nov 2020 — direct cost as engineer $/hour ×
  build-and-maintain hours; the benchmark that teams at companies over
  twenty people spend more than a fifth of engineering time on internal
  tools (near two-fifths above a thousand); value as united systems,
  fewer errors, stronger security and time freed for higher-value work;
  the LeadGenius, Neo4j and Noble Schools cases. Vendor content.
  Source: `./materials/Retool-CostBenefitAnalysisOfInternalTools-Beazell-2020.pdf`;
  transcription under `./materials/extracted/`.
- **Jonathan Kim**, *"Becoming product-led: How to connect product
  decisions to revenue"*, Appcues blog, 28 May 2026 — SaaS revenue as
  a system of four levers (acquire · expand · reduce churn · price),
  the Rule of 40, net revenue retention as the read of growth quality,
  revenue vs. logo churn, product-qualified leads and time-to-value,
  and shared product-and-revenue metrics (activation, feature
  adoption, NRR). Vendor content; the closing sections describe the
  vendor's product and are not distilled. Source:
  `./materials/Appcues-BecomingProductLed-Kim-2026.pdf`; transcription
  under `./materials/extracted/`.
- **Mural**, *"How to create a meaningful product vision"*, Mural
  blog, 24 Oct 2025 — the vision-statement definition, the
  fill-in-the-blank format adapted from **Geoffrey Moore**'s
  positioning statement (*Crossing the Chasm*), the six qualities
  (purposeful · achievable · aspirational · customer-focused · concise
  · well-documented), vision as relatively static while strategy
  adapts, and the Tesco, GitLab and Fender examples. Vendor content.
  Source: `./materials/Mural-HowToCreateAMeaningfulProductVision-2025.pdf`;
  transcription under `./materials/extracted/`.
- **Cameron Deatsch**, *"10 Lessons on using the Flywheel Effect to
  Grow Your Business"*, Inside Atlassian, 31 Aug 2021 — the enterprise
  trap (large contracts dictating the roadmap), "treat human
  interaction as a bug" (each support question is missing product,
  fixed systematically), and active users as the leading signal. The
  go-to-market lessons (public pricing, partner channels, community,
  localization) belong to the positioning and pricing agents on the
  README roadmap. Cited, not preserved.
- The four-step **Product Kata summary** (understand the direction ·
  analyze the current state · set the next goal · execute or deploy)
  is **Daniel O'Rorke's**, after Perri. So are the **product strategy
  memo**'s three parts (vision · current state · initiatives, in two
  to three pages), the six areas of a current-state analysis
  (performance · segments · pains and opportunities · strengths and
  weaknesses · competitive positioning · market and technology
  trends) and the rule to note knowledge gaps and move on — working
  notes after **Product Institute**'s strategy lessons, paraphrased;
  nothing quoted. Likewise the five marks of a **strong product
  initiative** (a clear connection to the current-state analysis ·
  quantified business value · evidence-based reasoning · defined
  success metrics · measurable customer outcomes), the focus rule and
  the rule that initiatives are periodically updated, not set in
  stone (§3c).
- The clause-by-clause tests (§1), the gap table's wrong/right fixes
  (§2), the stack rules (§3), the vision cautions (§3b), the
  initiative-to-artifact table (§3c), the five-step quantification
  procedure and the value-estimate block (§3d), the cadence table
  (§4), the memo's section-to-artifact mapping (§6a), the strategy
  stack, memo and direction ladder templates (§7), the plug-in table
  (§8), the anti-patterns (§9) and the worked example (§10) are **this
  repo's operational extension**.
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

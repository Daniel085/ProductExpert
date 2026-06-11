# The North Star Framework — Method Reference

*Distilled from **Amplitude's "North Star Playbook"** (John Cutler and the
Amplitude team), with the term popularized by **Sean Ellis** and the growth
community. See [`../../CREDITS.md`](../../CREDITS.md).*

## What a North Star Metric is

The **single metric that best captures the core value your product delivers
to customers** — chosen so that moving it now is a **leading indicator of
sustainable business results later**.

A North Star Metric (NSM) must express a **value exchange**: the customer
got value, and the business advanced. That's why classic examples count
*value events*, not bodies:

| Product | North Star | The value exchanged |
|---------|-----------|---------------------|
| Airbnb | Nights booked | A stay happened (guest got a trip, host got paid) |
| Spotify | Time spent listening | Music was enjoyed |
| WhatsApp | Messages sent | Communication happened |
| A B2B analytics tool | Weekly users who answer a question with data | Insight was delivered |

### What it is not

- **Not revenue.** Revenue is the *result* the NSM should lead; as a north
  star it's lagging, gameable short-term (dark patterns, price hikes), and
  says nothing about whether customers got value. Reject it as NSM and show
  the metric that *earns* the revenue instead.
- **Not a vanity count.** Registered users, cumulative downloads, page
  views — no value exchange, only accumulation.
- **Not plural.** Two north stars is zero north stars. Trade-offs need a
  single arbiter; everything else hangs below it.

### Quality checklist

A candidate NSM should be:
- [ ] An expression of customer **value exchange**
- [ ] A **leading indicator** of revenue/retention (state the causal story)
- [ ] **Actionable** — teams can influence it through product work
- [ ] **Understandable** — explainable to anyone in one sentence
- [ ] **Measurable** today (or instrumentable this quarter)
- [ ] Not gameable without actually delivering value (see counter-metrics)

## The three games

Which NSM shape fits depends on which "game" the product plays:

| Game | Value looks like | NSM shape | Examples |
|------|-----------------|-----------|----------|
| **Attention** | Time engaged | Time spent meaningfully | Spotify, Netflix |
| **Transaction** | Commercial acts completed | Transactions / value events | Airbnb, Amazon |
| **Productivity** | Work accomplished | Tasks completed / records created / questions answered | Salesforce, Figma, analytics tools |

Naming the game first prevents borrowing a metric from someone else's game
(a productivity tool maximizing time-in-app is optimizing for its own
failure).

## Input metrics — the metric tree

The NSM is an outcome; **work happens on its inputs**. Identify the **3–5
input metrics** that (a) teams can directly influence and (b) causally
drive the NSM. Classic decomposition: breadth × depth × frequency ×
efficiency —

```
NORTH STAR: e.g., weekly nights booked
├── Breadth:    # of active bookers this week
├── Depth:      nights per booking
├── Frequency:  bookings per booker per quarter
└── Efficiency: search → booking conversion rate
```

Each team owns input metrics, runs bets against them, and the tree makes
the causal chain reviewable: *this initiative → this input → the north
star → the business result.* Revisit the tree when an input stops
correlating with the NSM — the model of the business is a hypothesis too.

### Per-metric definition card

Every metric in the tree gets one — ambiguity here is how two dashboards
disagree forever:

```
Metric:        <name>
Definition:    <precise formula, incl. filters>
Unit/grain:    <per user/week, etc.>
Segments:      <standard cuts>
Owner:         <team>
Counter-metric:<what catches gaming/regression>
Source:        <event(s)/table(s)>
```

## Counter-metrics and Goodhart's law

*"When a measure becomes a target, it ceases to be a good measure."* Any
metric under pressure gets gamed — usually unintentionally. **Every target
metric ships with a counter-metric** that catches the failure mode:

| Target | Likely gaming/failure | Counter-metric |
|--------|----------------------|----------------|
| Time spent | Engagement-bait, infinite scroll | Self-reported satisfaction; regretted sessions |
| Messages sent | Notification spam | Mute/unsubscribe rate; response rate |
| Activation rate | Watering down "activated" | Downstream retention of "activated" users |
| Support tickets closed | Premature closes | Reopen rate; CSAT |

These counter-metrics are also the natural **guardrails** for experiments
(`methods/experimentation/`).

## Tracking plan (instrumentation spec)

The metric tree is only as real as its events. Spec instrumentation as:

```
Event name      | Fires when (trigger)         | Properties                  | Owner | Used by (metric)
----------------|------------------------------|-----------------------------|-------|-----------------
booking_created | reservation confirmed server-| nights:int, guests:int,     | core  | NSM, Depth
                | side (not button click)      | listing_id, total_value     |       |
search_performed| results rendered             | filters:map, results_count  | search| Efficiency
```

Rules: name events `noun_verb`, fire on the **server-side fact** where
possible (clicks lie), version the plan, and never define a metric on
events nobody owns.

## How this plugs into the system

- The NSM's causal story should rest on discovery evidence — what customers
  actually value (Track 1) and which outcomes are most underserved
  (Track 2) — not on a metaphor the team likes.
- **Stage matters:** a pre-product-market-fit team shouldn't optimize a
  scaling-stage NSM. Pair this framework with the stage discipline in
  [`lean-analytics.md`](./lean-analytics.md).
- Experiments inherit their OEC from the NSM/input tree and their
  guardrails from the counter-metrics.
- The PR/FAQ's "how will we measure success?" answer is a small metric tree
  with definition cards, not a wish.

# Lean Analytics — Method Reference

*Distilled from **"Lean Analytics: Use Data to Build a Better Startup
Faster"** by **Alistair Croll & Benjamin Yoskovitz** (O'Reilly, 2013), with
**Dave McClure's AARRR** funnel. See [`../../CREDITS.md`](../../CREDITS.md).*

## What makes a good metric

Four tests — a metric that fails them is decoration:

1. **Comparative.** "Up 12% week-over-week" beats "50,000."
2. **Understandable.** If people can't remember and discuss it, it won't
   change anything.
3. **A ratio or rate.** Ratios are inherently comparative and expose the
   tension you're managing (active/total, revenue/cost, viral coefficient).
4. **Behavior-changing.** The decisive test: *what will you do differently
   based on this number?* If no answer exists at any value of the metric,
   stop tracking it.

### Vanity vs. actionable

Vanity metrics feel good and inform nothing: **total** registered users,
**cumulative** downloads, raw page views, followers. The tell-tale shape is
the **up-and-to-the-right cumulative chart** — cumulative anything can only
go up. Convert vanity to action by asking for the ratio and the cohort:
not "how many signed up ever" but "what % of last month's signups did the
core action this week."

### Distinctions that prevent self-deception

- **Qualitative vs. quantitative** — numbers say *what*, conversations say
  *why*; you need both (Track 1 exists for the why).
- **Exploratory vs. reporting** — exploring for insight vs. tracking the
  known; don't confuse a fishing expedition with a KPI.
- **Leading vs. lagging** — leading metrics (e.g., this cohort's week-1
  activity) predict; lagging metrics (churn, revenue) confirm. Manage with
  leading, report with lagging.
- **Correlated vs. causal** — finding a correlation is a hypothesis;
  proving cause needs a controlled experiment
  (`methods/experimentation/`).

## The One Metric That Matters (OMTM)

At any given time, **one metric matters more than everything else** — it
answers the most important question of your current stage, gets a target
("the line in the sand"), and is displayed where everyone sees it. The OMTM
**changes as you progress**; having one doesn't mean tracking only one, it
means *focusing* on one.

## The five stages (and their OMTM)

| Stage | Question | OMTM lives in | Graduate when |
|-------|----------|---------------|---------------|
| **1 · Empathy** | Have I found a real problem people care about? | Qualitative signal: problem/solution resonance from interviews | Evidence the problem is real, frequent, and felt — this stage's "metrics" are Track 1's job |
| **2 · Stickiness** | Do people use it, and keep using it? | Engagement & retention: % active, cohort retention curves, core-action frequency | Retention curve flattens above a viable floor |
| **3 · Virality** | Do users bring others? | Viral coefficient, invitations sent/accepted, cycle time | Acquisition compounds (or you accept paid/content channels) |
| **4 · Revenue** | Does the economic engine work? | LTV:CAC, conversion to paid, ARPU vs. cost | Unit economics sustainably positive |
| **5 · Scale** | Can it grow through channels and markets? | Channel economics, market share, ops efficiency | — |

The most common failure is **stage-skipping**: optimizing virality or
revenue metrics on a product that isn't sticky — pouring users into a leaky
bucket. The retention curve has veto power.

## AARRR (pirate metrics)

McClure's funnel — useful as the horizontal cut across any stage:

- **Acquisition** — how do people find you? (traffic by channel)
- **Activation** — do they reach the first moment of value? (% reaching the
  "aha" action, defined concretely)
- **Retention** — do they come back? (cohort curves, not averages)
- **Revenue** — do they pay? (conversion, ARPU, LTV)
- **Referral** — do they tell others? (NPS as weak signal; invites/viral
  coefficient as strong)

Define each boundary as a **specific event** in the tracking plan, or the
funnel is a metaphor, not a metric.

## Business-model archetypes — the metrics that matter

| Model | The metrics that decide your fate |
|-------|----------------------------------|
| **E-commerce** | Conversion rate, AOV, repurchase rate (loyalty vs. acquisition mode), cart abandonment, shipping cost share |
| **SaaS** | MRR, churn (logo & revenue), LTV:CAC (healthy ≳ 3), CAC payback months, upsell/expansion, activation % |
| **Mobile app** | Downloads→install→signup funnel, D1/D7/D30 retention, ARPDAU, % paying, store ranking |
| **Media / ads** | Audience & time on site, CPM/CPC yield, sessions-to-clickout, ad load vs. retention tension |
| **UGC** | % creators vs. lurkers (1/9/90), content per user, engagement loops, spam rate |
| **Two-sided marketplace** | **Liquidity** (probability a listing sells / a search transacts — the OMTM until solved), buyer/seller balance, take rate, fraud rate |

## Cohorts, segments, and lines in the sand

- **Averages lie.** A flat average hides a thriving cohort and a dying one.
  Read **cohort curves** (by signup month, channel, persona) before
  believing any aggregate.
- **Segment comparisons** are the cheapest insight source: same metric, cut
  by acquisition channel / platform / persona.
- **Draw the line in the sand:** every OMTM gets an explicit target and a
  date, set from baselines/industry norms. Hitting it = graduate or
  double-down; missing it = the pre-committed conversation about pivoting
  the approach. A metric without a threshold is a spectator sport.

## How this plugs into the system

- **Stage 1 (Empathy) is Track 1** — don't dashboard your way through it;
  interview. The `customer-interviews` agent owns that evidence.
- The OMTM and stage determine which **North Star input metrics**
  ([`north-star.md`](./north-star.md)) deserve focus now.
- Correlations found here become hypotheses for the **experimentation**
  agent; retention cohorts and funnel boundaries define its OECs and
  triggering rules.
- The PR/FAQ's market-and-measurement FAQs should name the stage and the
  line in the sand.

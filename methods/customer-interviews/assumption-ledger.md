# The Assumption Ledger — Shared Template

*The single assumption-tracking format used across the system: **ideation**
produces it, **customer-interviews** consumes and updates it,
**prfaq** seeds "what we'd need to believe" from it, and
**experimentation** picks up its cheapest tests. Assumption *categories*
come from the `product-brainstorming` skill (see
`methods/ideation/materials/`); the ranking discipline is
[`talking-to-humans.md`](./talking-to-humans.md)'s impact × uncertainty
rule — both credited in [`../../CREDITS.md`](../../CREDITS.md).*

## The template

| Assumption | Category | Confidence | Evidence so far (tiered) | What would disprove it | Cheapest test |
|------------|----------|------------|--------------------------|------------------------|---------------|
| Owners will… | adoption | low | BACKGROUND: two competitors offer this | 15 of 20 say they'd stay with the current tool | Concierge pilot with 5 customers |

- **Confidence:** low / medium / high — your honest current belief, not
  your hope.
- **Evidence tiers:** label every evidence entry **CONFIRMED** (stated
  verbatim by a real customer/stakeholder, attributed), **INFERRED**
  (concluded from what was said — keep the words it rests on), or
  **BACKGROUND** (public info, desk research, landscape scans — validated
  by nobody you've talked to). The tier definitions are the same ones used
  in multi-call discovery (`methods/odi/interviewing.md`); never launder a
  lower tier into a higher one.
- **What would disprove it:** a concrete observation, stated before
  looking. If nothing could disprove it, it isn't an assumption — it's a
  belief you're protecting.
- **Cheapest test:** the least you could do to learn — a question in an
  interview, a landing page, a concierge/Wizard-of-Oz run — always cheaper
  than building.

## Categories (probe all six)

| Category | The claim | The probe |
|----------|-----------|-----------|
| **User** | "Users want this" | How do we know? From what evidence? How many users? |
| **Problem** | "This is a real problem" | How often does it occur? How much do they care? |
| **Solution** | "This solution will work" | Why this approach? What alternatives did we dismiss? |
| **Business** | "This will move the metric" | Which metric? By how much? Over what timeline? |
| **Feasibility** | "We can build this" | In what timeframe? With what trade-offs? |
| **Adoption** | "Users will find and use this" | How? What behavior change does it require? |

## Ranking and the riskiest assumption

Rank by **impact × uncertainty** exactly as
[`talking-to-humans.md`](./talking-to-humans.md) prescribes for
kill-the-business assumptions — don't re-derive the rule here. Then mark
**exactly one riskiest assumption**: the one that, if wrong, kills the
idea entirely. A ledger without a named riskiest assumption and its
cheapest test is not done.

## Lifecycle

1. **ideation** creates the ledger during assumption testing and hands it
   off with the routing decision.
2. **customer-interviews** takes it as the starting assumption list for
   prep (no re-derivation) and updates it at synthesis: statuses become
   validated / invalidated / still unknown / new, evidence entries gain
   CONFIRMED tiers, confidence moves on evidence.
3. **prfaq** turns surviving load-bearing entries into the internal FAQ's
   "what we'd need to believe" list.
4. **experimentation** designs the tests the "cheapest test" column only
   sketched, when a belief warrants real rigor.

One ledger per idea, updated in place — it is the idea's evidence trail
from first hunch to build/kill decision.

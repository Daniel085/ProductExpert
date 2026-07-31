# Desired Outcome Statements — Canonical Reference

*The atomic unit of the entire ODI pipeline. Every agent in the family —
interviewer, editor, survey builder, data scientist — works on these
statements, so this file is the **single source of truth** for their grammar,
validity rules, and editing standards. If a rule about outcome statements needs
to change, change it here and nowhere else.*

## The grammar

Every desired outcome statement follows exactly this structure:

```
[Direction] + [Metric] + [Object of Control] + [Contextual Clarifier]
```

| Component | Allowed values | Notes |
|-----------|---------------|-------|
| **Direction** | Minimize, Reduce, Maximize, Increase | Always a verb expressing direction of improvement |
| **Metric** | time, likelihood, number, frequency, amount, degree, extent | Must be measurable |
| **Object of control** | What is being measured | The specific thing the customer wants to change |
| **Contextual clarifier** | Where within the job this applies | Ties the outcome to a job step or context |

**Examples:**
- "Minimize the **time** it takes to *identify which input materials are needed*"
- "Minimize the **likelihood** of *selecting an incompatible component*"
- "Minimize the **number** of *adjustments needed during execution*"
- "Maximize the **likelihood** that *the output meets quality requirements*"

## Validity rules

A statement is valid only if it is:

1. **Measurable** — contains exactly one metric.
2. **Solution-agnostic** — no product names, brands, features, UI elements, or
   technologies.
3. **Actionable through design** — a product team could address it.
4. **Controllable** — within the product team's power to influence.
5. **Stable over time** — would still make sense in 10 years.
6. **Atomic** — one outcome per statement; no compound statements.
7. **Unambiguous** — only one interpretation is possible, in language the
   target respondent will understand (no jargon unless the audience is expert).

### Structural validation checklist (per statement)

```
[ ] Has a direction verb (minimize/maximize/reduce/increase)
[ ] Has a measurable metric (time/likelihood/number/frequency/amount)
[ ] Has an object of control
[ ] Has a contextual clarifier
[ ] Contains exactly ONE metric (no compound statements)
[ ] Is solution-agnostic
[ ] Is stable over time (would still make sense in 10 years)
[ ] Reads naturally in the survey stem "…how satisfied are you with your
    ability to [statement]…"
```

## Abstraction level

Statements sit at a **mid-level of abstraction** — specific enough to be
actionable by a product team, general enough not to prescribe a solution.

**Too broad (reject):**
- "Minimize the time it takes to do the job" — which part? This covers the
  entire job.
- "Maximize overall satisfaction" — not tied to any specific step or context.

**Too narrow (rewrite):**
- "Minimize the time it takes to scroll through the third dropdown menu" —
  solution-specific UI element.
- "Minimize the likelihood that the Phillips-head screw strips" — references a
  specific component.

**Correct level:**
- "Minimize the time it takes to identify which input materials are needed"
- "Minimize the likelihood of selecting an incompatible component"
- "Minimize the number of iterations required to achieve the desired output
  quality"

**Calibration method** (for leveling a full set):
1. Select 5 statements you consider correctly leveled.
2. Use them as reference anchors.
3. Compare every other statement against the anchors.
4. Rewrite outliers to match the anchor level.

## Solution-agnosticism

Reject or rewrite any statement that:
- Names a specific product, brand, or technology
- References a UI element (button, screen, menu, tab)
- Assumes a particular form factor or delivery mechanism
- Would become invalid if the underlying technology changed

| Fails | Passes |
|-------|--------|
| "Minimize the time it takes to refresh the browser" | "Minimize the time it takes to see updated information" |
| "Minimize the likelihood that the Bluetooth connection drops" | "Minimize the likelihood that the wireless connection is interrupted" |
| "Minimize the number of clicks to complete the purchase" | "Minimize the number of steps required to complete the purchase" |

## Redundancy detection

Two statements are **redundant** if they would be satisfied by the same product
improvement — different words, same underlying need.

**Redundant pair (merge):**
- "Minimize the time it takes to find the right song"
- "Reduce the time spent searching for a specific track"
- → Merged: "Minimize the time it takes to locate a specific piece of content"

**Not redundant (keep both):**
- "Minimize the time it takes to find a specific song"
- "Minimize the time it takes to discover new songs that match current
  preferences"
- → Finding a known item vs. discovering unknown items are different needs.

**Decision framework:**

| Situation | Action |
|-----------|--------|
| Identical meaning, different words | Merge → keep the clearer version |
| Overlapping but one is broader | Keep the broader, discard the narrower (unless the narrow one captures a real nuance) |
| Similar but genuinely different needs | Keep both, note the distinction |
| Same outcome, different job steps | Keep both — context matters for survey grouping |

**When in doubt, keep both.** A slightly longer survey is better than a lost
distinction.

## Numbering scheme

Statements are numbered `<job-step>.<sequence>` and keep their numbers through
the whole pipeline (gaps where statements were merged or removed are fine —
traceability beats tidiness):

```
STEP 1: Define & Plan
  1.01 - Minimize the time it takes to [...]
  1.02 - Minimize the likelihood that [...]
  1.03 - [MERGED from 1.03 + 1.07] Minimize the number of [...]

STEP 2: Locate Input
  2.01 - ...
```

Under **dual-job framing** (see [`interviewing.md`](./interviewing.md)), prefix
with the job: `A-1.01`, `B-3.02`.

## The need types statements live alongside

| Type | Description | Example |
|------|-------------|---------|
| Core functional job | The main task being accomplished | "Listen to music" |
| Desired outcomes | Metrics of success on the core job | "Minimize time to find a song" |
| Related jobs | Adjacent jobs triggered by the core job | "Share music with friends" |
| Emotional jobs | How the customer wants to feel | "Feel relaxed and in control" |
| Social jobs | How the customer wants to be perceived | "Be seen as having good taste" |
| Consumption chain jobs | Purchase, learn, set up, maintain, dispose | "Set up the system quickly" |
| Financial outcomes | Buyer's purchase decision metrics | "Minimize the total cost of ownership" |

Desired outcomes get the full grammar treatment above; related, emotional,
social, consumption-chain, and financial needs are captured as well-formed
statements too, but are surveyed importance-only (see
[`survey-design.md`](./survey-design.md)).

## Related framing: job stories

A **job story** — "When I *(situation)*, I want to *(motivation)*, so I can
*(outcome)*" — frames the same need at conversation/backlog altitude, where
an outcome statement frames it at quantification altitude. The two convert:
a job story's outcome clause, made measurable, is an outcome statement
("so I can come back and purchase without searching again" → "minimize the
time it takes to re-locate a previously identified product"). See
[`../jtbd/job-stories.md`](../jtbd/job-stories.md).

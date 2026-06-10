# The ODI Process Map

*The pipeline spec for ProductExpert's ODI method family: phases, steps,
agent responsibilities, and the handoff gates between them. Methodology by
**Tony Ulwick / Strategyn**; see [`../../CREDITS.md`](../../CREDITS.md).*

## Overview

**Outcome-Driven Innovation (ODI)** operationalizes Jobs-to-be-Done theory:
people buy products and services to get *jobs* done, and innovation succeeds
when it addresses the **outcomes customers use to measure success** in getting
those jobs done. ODI turns innovation from intuition-based guessing into a
repeatable, measurable process (Strategyn reports an 86% success rate).

Instead of asking customers what features they want, ODI:
1. Defines the market around a **job**, not a product or demographic.
2. Captures the customer's **desired outcomes** (success metrics) for that job.
3. **Quantifies** which outcomes are important but poorly satisfied.
4. **Segments** the market by unmet needs and picks a growth strategy.

## Phases and steps

```
Phase 1: DISCOVER         Phase 1.5: CURATE      Phase 2: QUANTIFY       Phase 3: ANALYZE & ACT
(odi-interviewer)         (odi-outcome-editor)   (odi-survey-builder)    (odi-data-scientist)

┌───────────────────┐    ┌────────────────────┐ ┌───────────────────┐   ┌───────────────────┐
│ 1. Define the     │    │ 5. Validate        │ │ 7. Build the      │   │ 9. Score          │
│    market around  │───>│    statement       │>│    quantitative   │──>│    opportunities  │
│    the job        │    │    structure       │ │    survey         │   │    (algorithm)    │
├───────────────────┤    ├────────────────────┤ ├───────────────────┤   ├───────────────────┤
│ 2. Map the job    │    │ 6. Deduplicate &   │ │ 8. Field the      │   │ 10. Segment the   │
│    (8 steps)      │    │    normalize       │ │    survey         │   │     market by     │
├───────────────────┤    │    abstraction     │ │    (180–600       │   │     unmet needs   │
│ 3. Capture        │    ├────────────────────┤ │    respondents)   │   ├───────────────────┤
│    desired        │<───│ 6b. Flag gaps &    │ └───────────────────┘   │ 11. Formulate     │
│    outcome        │    │     request        │                         │     growth        │
│    statements     │    │     follow-up      │                         │     strategy      │
├───────────────────┤    │     interviews     │                         ├───────────────────┤
│ 4. Identify the   │    └────────────────────┘                         │ 12. Evaluate      │
│    full needs set │      (targeted re-interviews                      │     solution      │
└───────────────────┘       if gaps found)                              │     concepts      │
```

### Step 1 — Define the market around the job

A market is **a group of people + the job they are trying to get done** — never
a product, technology, or demographic.

```
Job Executor:        [who performs this job?]
Core Functional Job: [verb + object + contextual clarifier]
```

- **Good:** "Parents trying to pass on life lessons to children"
- **Good:** "Music enthusiasts trying to listen to music"
- **Bad:** "MP3 player users aged 18–35"
- **Bad:** "Use Jira to manage sprints" (solution-bound; the job is "plan and
  track a software development project to completion")

Jobs are **stable over time** even as products and technologies change. When
the subject is a partner or platform company there are *two* jobs to define —
see **dual-job framing** in [`interviewing.md`](./interviewing.md).

### Step 2 — Map the job (Universal Job Map)

Deconstruct the core functional job into its 8 universal process steps:

| Step | Name | Description |
|------|------|-------------|
| 1 | **Define & Plan** | Determine goals and plan the approach |
| 2 | **Locate Input** | Identify and gather needed inputs (materials, information, people) |
| 3 | **Prepare** | Organize inputs, set up the environment |
| 4 | **Confirm** | Verify readiness before execution |
| 5 | **Execute** | Perform the core activity |
| 6 | **Monitor** | Track whether the job is being done successfully |
| 7 | **Modify** | Make adjustments as needed |
| 8 | **Conclude** | Finish the job and wrap up |

### Step 3 — Capture desired outcome statements

Extract **100+ outcome statements** across all job steps (5–10 per step) from
customer interviews. The statement grammar, validity rules, and editing
standards live in [`outcome-statements.md`](./outcome-statements.md); the
interview protocol lives in [`interviewing.md`](./interviewing.md).

### Step 4 — Identify the full needs set

The JTBD needs framework captures every relevant need type:

1. **Core functional job** and its desired outcomes
2. **Related jobs** the customer is also trying to get done
3. **Emotional jobs** (how the customer wants to feel)
4. **Social jobs** (how the customer wants to be perceived)
5. **Consumption chain jobs** (purchase, learn, set up, maintain, dispose)
6. **Financial desired outcomes** (the buyer's purchase metrics)

### Steps 5–6b — Curate (validate, deduplicate, normalize, audit coverage)

A quality gate between discovery and quantification: validate every statement's
structure, merge redundant statements, normalize abstraction level, audit
solution-agnosticism, and check coverage across all 8 job-map steps. If a step
is undercovered, send a **targeted interview request** back to discovery
(step 6b) rather than passing a gap downstream. Full editing protocol in
[`outcome-statements.md`](./outcome-statements.md).

### Steps 7–8 — Build and field the quantitative survey

Convert the curated statements (typically 80–120) into a survey where each
outcome is rated twice — **importance** and **satisfaction** — and field it to a
statistically valid sample (180–600 respondents depending on market type).
Instrument design, sizing, and data standards in
[`survey-design.md`](./survey-design.md).

### Steps 9–12 — Score, segment, strategize, evaluate

Score every outcome with the **opportunity algorithm**, build the opportunity
landscape, segment the market by **unmet needs** (factor + cluster analysis),
recommend a growth strategy, and evaluate solution concepts against the data.
Full analysis protocol in [`opportunity-analysis.md`](./opportunity-analysis.md).

The core formula, for reference everywhere:

```
Opportunity Score = Importance + max(Importance − Satisfaction, 0)
```

## Agent responsibilities

| Agent | Phase | Input | Output |
|-------|-------|-------|--------|
| **odi-interviewer** | 1 · Discover | Market definition | Job map, 100+ raw outcome statements, full needs set |
| **odi-outcome-editor** | 1.5 · Curate | Raw outcome statements | 80–120 curated statements, coverage report, change log; may request follow-up interviews |
| **odi-survey-builder** | 2 · Quantify | Curated statements | Survey instrument, fielding specs, data dictionary |
| **odi-data-scientist** | 3 · Analyze & Act | Clean survey dataset | Opportunity scores, segments, growth strategy |

The pipeline has **two humans-in-the-loop**: you conduct the interviews (the
interviewer agent preps guides and extracts outcomes from your notes and
transcripts), and you field the survey (the builder specifies it; the data
scientist analyzes the returns).

## Handoff gates

A stage must not start until its gate passes. When a gate fails, the receiving
agent sends the work back with a specific request — gaps are fixed upstream,
never papered over downstream.

| From | To | Deliverables | Gate |
|------|----|-------------|------|
| You | odi-interviewer | Market definition | Job is solution-agnostic and stable |
| odi-interviewer | odi-outcome-editor | Job map, 100+ raw statements, full needs set | Interviews reached saturation |
| odi-outcome-editor | odi-interviewer | Targeted interview request (if gaps) | Any job step with < 5 statements |
| odi-outcome-editor | odi-survey-builder | 80–120 curated statements, coverage report, change log | All quality checks pass |
| odi-survey-builder | You (to field) | Survey instrument, fielding specs | Survey < 25 min; sample size specified |
| You (after fielding) | odi-data-scientist | Clean dataset (CSV) | N ≥ 180; < 10% missing data |
| odi-data-scientist | You | Opportunity scores, segments, strategy | Silhouette score > 0.25 |

## Where this sits in ProductExpert

ODI is the **quantitative track**. The **qualitative track**
(`methods/customer-interviews/`, the `customer-interviews` agent) comes first
in a product's life: open-ended discovery that validates the problem and the
job are real. Its output — a validated, solution-agnostic job — is exactly the
**market definition** this pipeline requires at step 1. See
[`../../docs/how-it-works.md`](../../docs/how-it-works.md) for the bridge.

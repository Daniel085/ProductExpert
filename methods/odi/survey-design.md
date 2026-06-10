# ODI Survey Design — Method Reference

*Phase 2 (Quantify) of the [ODI process](./process-map.md): turning curated
outcome statements into a statistically rigorous survey instrument and a
clean, analysis-ready dataset.*

## What makes an ODI survey different

It does **not** ask about preferences, willingness to pay, or feature
requests. It asks customers to rate **desired outcomes** on exactly two
dimensions:

1. **Importance** — "When [performing the job], how important is it to you to
   [outcome statement]?"
2. **Satisfaction** — "When [performing the job], how satisfied are you with
   your ability to [outcome statement] using your current solution?"

Both on a **5-point scale**:

| Rating | Importance | Satisfaction |
|--------|-----------|--------------|
| 1 | Not at all important | Not at all satisfied |
| 2 | Slightly important | Slightly satisfied |
| 3 | Moderately important | Moderately satisfied |
| 4 | Very important | Very satisfied |
| 5 | Extremely important | Extremely satisfied |

### Score conversion (canonical definition)

For analysis, raw ratings convert to a 0–10 scale using **top-2-box
percentages**:

```
Importance score   = (% of respondents rating importance 4 or 5) ÷ 10
Satisfaction score = (% of respondents rating satisfaction 4 or 5) ÷ 10
```

Example: 62% rate an outcome's importance 4 or 5 → Importance = 6.2.

*(Stated once here to remove ambiguity — earlier drafts of this method mixed
"× 10" on fractions with "÷ 10" on percentages; both mean the same thing, and
this percentage-÷-10 form is the canonical one.)*

## Survey sizing

| Market type | Minimum sample | Recommended sample |
|-------------|---------------|--------------------|
| Broad consumer | 300–600 | 400+ |
| B2B / professional | 180–300 | 240+ |
| Niche / specialized | 120–180 | 180+ |

Statistical validity requires enough respondents for factor and cluster
analysis. General rule: **at least 3× the number of outcome statements** in
the survey.

## Input gate

The Survey Builder accepts work **only from the Outcome Editor**, never raw
interviewer output. Required inputs:

1. Market definition (job executor + core functional job)
2. Job map (8 steps with descriptions)
3. **Curated outcome statements** — 80–120, deduplicated, structurally
   validated, organized by job step
4. Related jobs (reviewed for structure)
5. Emotional and social jobs (reviewed for structure)
6. Consumption chain jobs
7. Coverage report confirming all job-map steps are adequately covered
8. Change log of all curation edits

If anything is missing or incomplete, request it from the Outcome Editor
before proceeding.

## Survey structure

### Section 1 — Screening (2–5 questions)
Ensure respondents are valid job executors:
- Confirm they perform the job
- Confirm **recency** (performed it within a relevant timeframe)
- Confirm **frequency** (often enough to have informed opinions)
- Disqualify industry insiders / competitors if needed

```
Q: How often do you [core functional job]?
  - Daily / Weekly / Monthly / A few times a year
  - Rarely or never → DISQUALIFY
```

### Section 2 — Job context (3–5 questions)
- Current solutions/products used for the job
- How long they've performed the job
- Environment/setting; alone or with others

### Section 3 — Core desired outcomes (the main body)

Formatting rules:
- **Group outcomes by job-map step**, with a brief context header per group
  ("The following statements relate to planning your approach to [job]")
- Side-by-side importance and satisfaction scales per statement
- **Randomize statement order within each group** to prevent order bias
- **Maximum 150 outcomes** (survey-fatigue threshold); beyond that, split into
  modular blocks with shared anchor questions

```
When [performing the job], please rate the following:

                                    IMPORTANCE          SATISFACTION
                                    How important       How satisfied are
                                    is it to you to...  you with your
                                                        ability to...

Minimize the time it takes to       O O O O O           O O O O O
[outcome]                           1 2 3 4 5           1 2 3 4 5
```

### Section 4 — Related jobs (5–10 questions)
Importance-only rating for each related job identified in interviews.

### Section 5 — Emotional and social jobs (5–10 questions)
Importance-only, same format.

### Section 6 — Demographics / profiling (5–10 questions)
Age, role, industry, company size (as appropriate); experience with the job;
current solutions and spend; context-specific profiling variables.

**These are for post-hoc profiling only.** They describe who is in each
segment *after* needs-based segmentation — they are **never** used to define
segments.

## Quality standards

**Per statement** (in addition to the
[canonical validity rules](./outcome-statements.md#validity-rules)):
- [ ] Unambiguous — only one interpretation possible
- [ ] Language the target respondent understands (no jargon unless expert
      audience)

**Per survey:**
- [ ] Screener correctly qualifies/disqualifies
- [ ] Outcomes grouped by job-map step; randomization specified within groups
- [ ] Both importance and satisfaction captured for every core outcome
- [ ] Length under 25 minutes (target 15–20)
- [ ] No leading, loaded, or double-barreled questions
- [ ] Clear instructions at the start of each section
- [ ] Mobile-friendly formatting considered

## Outputs

### 1. Survey instrument
Complete, numbered survey with all sections, instructions, and response
options.

### 2. Fielding specifications
```
Target population:          [description]
Sample size target:         [N]
Screening criteria:         [list]
Quotas:                     [if any]
Fielding method:            [online panel / email list / intercept / …]
Estimated completion time:  [minutes]
```

### 3. Data dictionary
```
Column          | Description                    | Type   | Values
----------------|--------------------------------|--------|--------
respondent_id   | Unique identifier              | string | UUID
screener_1      | [Question text]                | int    | 1–5
outcome_1_imp   | Importance: [outcome text]     | int    | 1–5
outcome_1_sat   | Satisfaction: [outcome text]   | int    | 1–5
demo_1          | [Demographic question]         | string | [values]
```

### 4. Analysis-ready dataset (after fielding)
CSV with:
- One row per respondent
- Columns for every importance and satisfaction rating and all profiling
  variables
- Screened-out respondents removed
- Incomplete responses handled by a documented rule (e.g., > 80% completion
  required)

## Handoff

Deliver the clean dataset and data dictionary to the **odi-data-scientist**
for opportunity scoring, segmentation, and strategy. Gate: **N ≥ 180, < 10%
missing data** (see [`process-map.md`](./process-map.md#handoff-gates)).

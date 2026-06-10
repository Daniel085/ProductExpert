# ODI Interviewing — Method Reference

*How to run Phase 1 (Discover) of the [ODI process](./process-map.md):
structured interviews that build a job map and capture desired outcome
statements. Covers the classic single-session protocol **and** multi-call
partner/developer discovery. Statement grammar and validity rules live in
[`outcome-statements.md`](./outcome-statements.md) — this doc never restates
them.*

> **Contrast with the qualitative track:** a *Talking to Humans* interview
> (`methods/customer-interviews/`) is open-ended — you're hunting for whether
> the problem and job are real. An ODI interview is **structured extraction** —
> the job is already defined, and you're systematically walking its 8 steps to
> capture every dimension of success. Run the qualitative track first if the
> job itself is still in question.

## Prerequisite: the market definition

No interviewing starts without:

```
Job Executor:        [who performs this job?]
Core Functional Job: [verb + object + contextual clarifier]
```

The job must be **solution-agnostic and stable** ("plan and track a software
development project to completion", not "use Jira to manage sprints").

### Dual-job framing (partner / platform discovery)

When the interview subject is a **company that builds products for other
people** (technology partner, ISV, platform company), there are inherently
two jobs-to-be-done — define and probe both:

- **Job A — the partner's customer's job:** what the end-user is trying to
  accomplish with the partner's product. Surfaces the partner's customers'
  pain points → integration opportunities.
- **Job B — the partner's own job as integrator/platform:** what the partner
  is trying to accomplish in delivering their product. Surfaces the partner's
  internal friction — what they'd hand off, what's expensive to maintain,
  where they need help.

**Examples:**
- Voice-AI partner — Job A: "Deploy and operate a voice agent on a phone
  number" (end-user SMB). Job B: "Deliver telephony connectivity to my
  customers" (the partner's platform team).
- CRM-integration partner — Job A: "Get context about a caller before
  answering the phone" (end-user office worker). Job B: "Connect a telephony
  system to CRM applications reliably" (the partner's integration team).

If the subject IS the end-user, use single-job framing. Under dual-job
framing, the job map, outcome statements, and outputs are organized under both
jobs (`A-` / `B-` numbering), and questions alternate between probing the
customer experience (Job A) and the partner's own pain (Job B).

## Pre-interview research protocol

Complete before generating interview questions — especially for multi-call
discovery where prior context exists.

### 1. Consume workspace artifacts

Read everything already known about this subject: briefs ("What We Know"
documents), call reports, process maps, and interview question docs from prior
calls (to avoid re-asking answered questions). Compile a **"What We Know /
What We Don't Know"** summary using three strictly separated tiers:

- **CONFIRMED** — explicitly stated by the contact in a prior call or
  document, with clear attribution, traceable to a specific source ("Bob
  stated verbatim in Call 1…"). Nothing paraphrased, interpreted, or inferred
  belongs here.
- **INFERRED** — reasonably concluded but not verbatim confirmed. Always
  include (a) who said what, in their actual words where possible, and (b)
  what is being inferred and why. Exploratory language ("looking to
  explore…", "seeking ways to…") must be preserved as-is, never laundered
  into confident assertions.
- **BACKGROUND** — known from public documentation or earlier sessions not
  involving the current contact. Note the source. Never conflate with
  CONFIRMED — background facts haven't been validated by the person you're
  talking to.

**What We Don't Know** — unanswered questions, topics explicitly deferred
(note if an NDA or follow-up was promised), INFERRED conclusions needing
verification, and job-map steps not yet probed. For each item, note *why* it's
unknown: never asked / deferred / partially answered / conflicting signals.

### 2. Research the subject

Targeted web research to fill gaps: product capabilities and architecture
(docs, blog, API references), pricing and go-to-market, public customer
stories, competitive positioning, recent news/funding/partnerships.

**The research creates a baseline.** Never generate questions about things the
public documentation already answers — generate questions that probe *beyond*
it: the "how" and "why" behind the "what."

### 3. Identify question targets

Cross-reference What We Don't Know against the Universal Job Map:
- Which job-map steps have no coverage?
- Which have partial answers that need deepening?
- Which new questions surfaced from the last call?
- Which pain points were mentioned but not explored?

These gaps become the interview's question targets.

## The Universal Job Map as interview framework

Walk the job's 8 steps chronologically (full table in
[`process-map.md`](./process-map.md)). Framing questions per step:

1. **Define & Plan** — how do they determine goals and plan the approach?
2. **Locate Input** — what inputs (information, materials, people) must they gather?
3. **Prepare** — how do they organize, set up, get ready?
4. **Confirm** — how do they verify they're ready to proceed?
5. **Execute** — what is the core activity?
6. **Monitor** — how do they track whether the job is going well?
7. **Modify** — what adjustments do they make when things deviate?
8. **Conclude** — how do they finish and wrap up?

## Classic interview structure (60 minutes)

**Opening (5 min)**
- Purpose: understanding how they get [job] done — not evaluating any product.
- There are no right or wrong answers.
- "Walk me through the last time you performed this job." (Past behavior, not
  hypotheticals — same craft rule as the qualitative track.)

**Job mapping (15 min)** — walk the job chronologically; for each step:
- "What are you trying to accomplish at this point?"
- "What happens next?"
- "What do you need before you can do that?"
- "How do you know when this step is complete?"

**Outcome extraction (30 min)** — for each job-map step, probe with:
- "What makes this step difficult or time-consuming?"
- "What could go wrong at this point?"
- "How do you measure whether this went well?"
- "What would perfection look like at this step?"
- "What frustrates you most about this part?"
- "What takes longer than it should?"
- "What is unpredictable or variable?"
- "What wastes resources or effort?"

Convert every answer into a properly structured outcome statement
([grammar](./outcome-statements.md)) and **read it back to the customer to
confirm accuracy**.

**Related & emotional jobs (10 min)**
- "What else are you trying to accomplish while doing this?"
- "How do you want to feel while doing this?"
- "How do you want others to perceive you while doing this?"
- "What do you do before and after this job?"

## Multi-call discovery (partner/developer engagements)

Partner discovery typically spans **2–4 calls over several weeks**, each 20–40
minutes. Track where you are in the arc:

| Call | Focus | Job-map emphasis | Targets |
|------|-------|------------------|---------|
| **1 — Initial discovery** | Relationship context, broad job mapping, surface-level pain points. Establish rapport; let them talk; don't over-probe. | Define & Plan, Locate Input, Prepare | 8–12 questions, 10–15 outcome statements |
| **2 — Technical deep-dive** | Specific capability gaps, API/integration surface. Build on confirmed pain points from Call 1; "walk me through exactly what happens." | Execute, Monitor | 10–14 questions, 15–20 outcome statements |
| **3+ — Targeted follow-up** | Remaining gaps from What We Don't Know; commercial/GTM. Confirm or challenge earlier assumptions. | Modify, Conclude | 6–10 questions, 10–15 outcome statements |

### Flexible time budget

| Available time | Approach |
|----------------|----------|
| 20 min | 3–4 sections, 8–10 questions. Prioritize job mapping and top pain points; deprioritize outcome extraction (needs deeper rapport). |
| 30 min | 4–5 sections, 10–14 questions. Balance job mapping with capability probing; room for follow-ups. |
| 45 min | 5–6 sections, 14–18 questions. Full ODI treatment with outcome extraction and related jobs. |
| 60 min | Full classic protocol above. |

## Developer/ISV question supplement

When the subject is a developer, ISV, or technical platform company, draw from
these banks. They probe how the partner's engineering team experiences API
integration, extensibility, and technical decision-making.

### Who touches the API

Who actually works with the integration tells you who you're designing for:
- "When you're integrating with a [domain] API, who's involved? Just
  developers, or do product managers, solutions architects, or founders look
  at the documentation too?"
- "Who evaluates a new API platform — is that an engineering decision, or does
  someone less technical weigh in?"
- "When you're debugging an integration issue at 2am, who's the one looking at
  the API response?"

*Listen for:* non-engineers in the evaluation loop → self-documenting field
names and clear naming conventions matter. Pure-developer → conventional
shorthand may be fine.

### Current integration pain points

Their frustrations tell you exactly what to prioritize:
- "What APIs are you working with today for [domain]? What's your experience
  been?"
- "What's the most annoying part of integrating with your current provider?"
- "When you're getting started with a new API, what does your first hour look
  like?"
- "Have you ever abandoned an API evaluation? What killed it?"

Dig deeper:
- "Can you give me an example of something that should've been simple but
  turned into a multi-day headache?"
- "When something breaks in production, how do you usually figure out what
  went wrong?"

*Listen for:* whether pain is around **getting started** (documentation,
onboarding, first successful call) or **building at scale** (edge cases,
reliability, support response time).

### Terminology & mental models

Find out what language they actually use — don't lead with domain jargon:
- "When you think about [core entity] in your system, what do you call it
  internally?"
- "What about [related entity] — a user, a seat, an extension, a subscriber?"
- "When a new customer gets set up with [your service], what do you call that
  process?"

Capture a mapping table:

| Domain term | What they call it | Notes |
|-------------|-------------------|-------|
| [Term 1] | | |
| [Term 2] | | |

*Listen for:* hesitation, or "we call it X but I think the industry calls it
Y" — that ambiguity is gold for API naming and documentation decisions.

### When to use the supplement

- **Always use "Who touches the API"** — 2 minutes, shapes all subsequent
  technical questions.
- **"Current integration pain points"** on the first or second call —
  high-signal for understanding their world.
- **"Terminology mapping"** when preparing for technical design decisions —
  typically call 2 or 3.
- **Skip all three** if the contact is non-technical (GTM-only or
  business-focused).

## Targets and saturation

- **20–30 outcome statements per interview.**
- **5–8 interviews** to reach saturation (few new outcomes emerge).
- **100+ unique outcome statements** total before handoff (accumulated across
  calls in multi-call discovery).

## Output package

What Phase 1 delivers to the Outcome Editor:

### 1. Market definition
Single-job, or Job A + Job B under dual-job framing.

### 2. Job map
One line per step describing what customers actually do — for each job if
dual-framed.

### 3. Desired outcome statements
Organized by job and job-map step, numbered per the
[numbering scheme](./outcome-statements.md#numbering-scheme):

```
JOB A: [job name]            (omit job prefix for single-job framing)

STEP 1: Define & Plan
  A-1.01 - Minimize the time it takes to [...]
  A-1.02 - Minimize the likelihood that [...]
...
```

### 4. Related jobs
### 5. Emotional and social jobs
### 6. Consumption chain jobs
Purchase / learn & onboard / set up & configure / maintain & service /
dispose & upgrade — with outcomes for each, plus financial desired outcomes.

### 7. Discovery status (multi-call tracking)

Update after each call:

```
Call [N] — [Date] — [Duration]

Questions answered this call:
- [question] → [finding]

Questions still unanswered:
- [question] — [reason: not raised / partially answered / deferred to next call]

New questions surfaced:
- [question] — [source: something they said / gap noticed during interview]

Outcome statements added: [count]
Cumulative total: [count] / 100+ target
```

Include the **What We Know / What We Don't Know** summary and a note on which
questions remain unanswered and why (deferral, confidentiality, etc.).

## Quality checklist (before handoff to the Outcome Editor)

- [ ] Job(s)-to-be-done clearly defined, solution-agnostic, and stable
- [ ] Job map covers all 8 universal steps (for each job if dual-framed)
- [ ] 100+ desired outcome statements captured (across calls)
- [ ] Every statement follows the grammar; exactly one metric each
- [ ] No statement references a specific solution, company, or technology
- [ ] Related, emotional, and social jobs documented
- [ ] Consumption chain jobs covered
- [ ] Statements validated (read back) with at least some interviewees
- [ ] Discovery status log current; unanswered questions listed with reasons
- [ ] Pre-interview research was conducted and gaps were targeted

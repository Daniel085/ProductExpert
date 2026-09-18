# Picking the Right Problem — Method Reference

*The framework for deciding **which customer problem to work on** when
several compete: two criteria (Customer Signal × Business Alignment), three
goal-dependent readings of them, and a four-step execution discipline —
problem statement → evidence table → patterns → validation verdict. Arrived
as the PM's working notes (see [`./materials/README.md`](./materials/README.md));
the scoring anchors, decision rules and ranking table are this repo's
operational extension and are marked as such. The problem-statement formula
is the job story ([`../jtbd/job-stories.md`](../jtbd/job-stories.md)); the
pattern step uses affinity mapping
([`./affinity-mapping.md`](./affinity-mapping.md)). See
[`../../CREDITS.md`](../../CREDITS.md).*

> **Where this sits.** Discovery produces *more* problems than a team can
> work on: interview insights, support themes, funnel drop-offs, sales
> asks, stakeholder theories. This method ranks **problems** — not
> solutions (that's `ideation`'s converge step), not desired outcomes
> within one job (that's the ODI opportunity score), not beliefs about a
> solution (that's `experimentation`). Its output is the problem you take
> into a PR/FAQ, or the gap you send back to discovery.

## 1. How do you know which problems matter most?

Analyze every candidate problem on **two criteria**:

| Criterion | The question |
|-----------|--------------|
| **Customer Signal** | How **painful** is the problem for the user? How **many** people experience it? |
| **Business Alignment** | How well does solving this problem help the business **reach its goals**? |

A problem worth working on scores high on both. High signal with no
alignment is a real problem for someone else's roadmap; high alignment
with no signal is a stakeholder theory wearing a customer's clothes.

### The criteria depend on your goal

The two criteria keep their names but change what they measure depending
on what the business is trying to do:

| Goal | Customer Signal measures… | Business Alignment measures… |
|------|---------------------------|------------------------------|
| **Default** (retention, engagement, expansion, revenue from existing customers) | strength of the pain **and** how many experience it | how directly solving it moves the stated goal / North Star |
| **Acquisition** — *flip the criteria* | **strength** of the pain only | **how many people have the problem** — breadth *is* the acquisition goal |
| **Internal tools** | how much **employees suffer** because of the problem | whether solving it **saves time and avoids errors for others** (beyond the sufferers) |

The acquisition flip matters: when growth is the goal, a mild problem that
a huge population shares can outrank a severe one felt by a niche you
already own, and the breadth number belongs on the business side of the
ledger, not the customer side. Decide which reading applies **before**
scoring — never per problem.

### Scoring anchors *(repo extension)*

Score each criterion 1–5 so problems can be compared. Anchors, so two
people score alike:

**Customer Signal** — score pain and breadth separately, then combine per
the goal reading above (default: report both; acquisition: pain only).

| Score | Pain strength | Breadth |
|-------|---------------|---------|
| 1 | Mild annoyance; workaround is effortless; nobody raised it unprompted | A handful of people; one segment's edge case |
| 2 | Recurring irritation; people mention it when asked | A minority of one segment |
| 3 | Costs real time or money each occurrence; people have built workarounds | A meaningful share of a target segment |
| 4 | Blocks the job; people have tried other products or paid to avoid it | Most of a target segment |
| 5 | Causes churn, lost revenue, or safety/compliance exposure; people show **commitment** (time, money, escalation) | Most of the addressable population, across segments |

**Business Alignment**

| Score | Meaning |
|-------|---------|
| 1 | No plausible path from solving it to the stated goal |
| 2 | Indirect; helps a metric nobody has committed to |
| 3 | Moves an input metric of the goal, modestly |
| 4 | Moves an input metric of the goal, materially, within the planning horizon |
| 5 | Moves the goal metric itself (or is contractually / regulatory committed) |

Business Alignment is scored against the **stated** goal — the North Star
or the quarter's committed outcome. If no goal is stated, stop and get one
(the `metrics` agent defines it); alignment scored against "what leadership
seems to want" is the HiPPO in disguise.

### Reading the two scores together

```
                        Business Alignment
                    low                 high
              ┌───────────────────┬───────────────────┐
   Customer   │ DROP              │ SUSPECT           │
   Signal low │ archive w/ reason │ stakeholder theory│
              │                   │ → trace to a      │
              │                   │   customer problem│
              ├───────────────────┼───────────────────┤
   Customer   │ PARK / SPONSOR    │ DO                │
   Signal high│ real, not ours    │ (subject to the   │
              │ now — revisit     │  validation gate) │
              │ when goals change │                   │
              └───────────────────┴───────────────────┘
```

## 2. The execution framework (one case per problem)

Four steps. A problem is not "picked" until all four are on paper.

### Step 1 — Problem statement

Write it **from the customer's perspective** using the job-story formula:

```
When [situation], I want to [motivation], so that I can [desired outcome].
```

Rules come from [`../jtbd/job-stories.md`](../jtbd/job-stories.md): no
solution-noun inside "I want", no "better X", a triggering situation
specific enough to picture, an observable outcome. Run the six tells. For
internal tools the customer is the employee; write it from their seat, not
the process owner's.

If the candidate can't be written this way, it isn't a problem yet — it's
a feature request or a stakeholder theory. Trace it
([`../jtbd/requirements-are-hypotheses.md`](../jtbd/requirements-are-hypotheses.md))
before scoring it, or record it under *Probably not*.

### Step 2 — Evidence

**When multiple sources point to the same problem, it is far less likely
to be driven by bias or opinion.** Collect evidence from three source
types and record every item in one table:

| Source | Type | Confidence in evidence (1–5) | Findings |
|--------|------|------------------------------|----------|
| 8 onboarding interviews, Jun | Qualitative | 4 | 6 of 8 described re-entering data after an import failure; 2 had built spreadsheets to avoid it |
| Import funnel, last 90 days | Quantitative | 5 | 31% of imports abandoned at the mapping step; abandoners' 30-day retention 22 pts lower |
| Support tickets tagged "import" | Operational | 3 | 140 tickets / quarter, 3rd-largest tag; tagging inconsistent |
| Sales call notes (AE Slack) | Operational | 2 | "Comes up in most enterprise demos" — no count |

**Types:**

- **Qualitative** — interviews, usability tests, open-ended survey
  responses, session recordings, field observation. Tells you *why* and
  *how painful*.
- **Quantitative** — funnel metrics, usage/analytics data, survey ratings,
  ODI importance–satisfaction scores, experiment results. Tells you *how
  many* and *how much*.
- **Operational** — support tickets, sales/CS call notes, escalations,
  churn reasons, refunds, on-call incidents, internal process logs. Tells
  you *what it costs* and *where it surfaces*.

**Confidence anchors** *(repo extension)* — confidence is in the
**source**, per row, not in the problem overall:

| Score | The evidence is… |
|-------|------------------|
| 1 | Hearsay, a single opinion, or a stale data point; no attribution |
| 2 | A few voices or self-reported data; small n; known collection problems |
| 3 | Solid within its type but not replicated; a plausible alternative explanation remains |
| 4 | Recent, attributable, methodologically sound, n adequate for its type |
| 5 | Direct observed behavior or instrumented data at scale, or verbatim **commitment** (money, time, escalation), with no known bias |

Map to the shared evidence tiers where the ledger needs them: rows at 4–5
from customers are **CONFIRMED**, 3 is typically **INFERRED**, 1–2 or any
desk research is **BACKGROUND**
([`../customer-interviews/assumption-ledger.md`](../customer-interviews/assumption-ledger.md)).
Never launder upward.

### Step 3 — Identify patterns

Ask three questions of the table:

1. **Convergence** — are multiple sources, of *different types*, pointing
   at the same problem? Same-type agreement (three interviewees) is a
   pattern; cross-type agreement (interviews + funnel + tickets) is
   triangulation, and it is what defeats bias.
2. **Conflict** — are there signals that disagree? (Interviews say it's
   painful; analytics say almost nobody hits it. Tickets are high; churn
   reasons never mention it.) A conflict is not noise to average away — it
   is either a segment difference, a measurement problem, or a sign the
   problem statement is wrong. Name which, or mark it unresolved.
3. **Gaps** — which source type is missing entirely? A problem with no
   quantitative row has unknown breadth; one with no qualitative row has
   unknown pain; one with no operational row has unknown cost.

When the raw material is large (dozens of tickets, many transcripts,
survey open-ends), theme it first with
[affinity mapping](./affinity-mapping.md) — group before naming, count
**distinct sources** per theme, keep the source tags — and only then fill
the evidence table from the themes.

### Step 4 — Can you validate this problem?

One of three verdicts, with the decision rules *(repo extension)*:

| Verdict | Rule of thumb | Then |
|---------|---------------|------|
| **Yes** | ≥ 2 source **types** converge; at least one row at confidence ≥ 4; no unresolved conflict; the statement passes the job-story tells; Customer Signal is measurable | Score it, rank it, take it forward (PR/FAQ, or ODI if the question becomes *which needs within the job*) |
| **Not yet** | One source type only, or every row ≤ 3, or a conflict still unexplained, or breadth/pain unknown | Name the **missing evidence** and the cheapest way to get it: interviews (`customer-interviews`), a metric definition or query (`metrics`), a ticket audit, an importance–satisfaction survey (ODI). Park on the *learn* list, not the *build* list |
| **Probably not** | Sources contradict on the core claim; the "problem" dissolves into a solution ask or stakeholder theory with no customer trace; the only signal is one loud voice; breadth is negligible under the goal reading | Archive **with the reason and the evidence** — so it is not re-litigated next quarter |

*Not yet* is the most common honest verdict and it is not a failure: it
converts a roadmap argument into a research task with a named owner.

## 3. Ranking across problems *(repo extension)*

Once each candidate has its case, put them side by side:

| # | Problem (job story, short) | Customer Signal (pain / breadth) | Business Alignment | Strongest evidence (type · confidence) | Types converging | Verdict | Rank |
|---|----------------------------|----------------------------------|--------------------|----------------------------------------|------------------|---------|------|
| 1 | When an import fails mid-way, I want to recover without re-entering data, so I can finish setup the same day | 4 / 4 | 5 | Quant · 5 | 3 | Yes | 1 |
| 2 | … | 5 / 2 | 3 | Qual · 4 | 1 | Not yet | learn |
| 3 | … | 2 / 5 | 2 | Ops · 2 | 1 | Probably not | archive |

Ranking rules:

- Only **Yes** verdicts are ranked for building. Order by Customer Signal
  × Business Alignment; break ties on evidence convergence, then on the
  cheapest path to a shippable test.
- **Not yet** entries form the *learn* list, each with its missing
  evidence and cheapest test — that list is real work and gets scheduled.
- **Probably not** entries are archived with reason; the archive is an
  output, not a bin.
- Count **distinct sources**, never items: forty tickets from one customer
  are one voice with forty timestamps.
- Re-score when the goal changes. Rankings are a function of the goal
  reading (§1); a new North Star or a shift to acquisition reorders the
  table by design.

## 4. Anti-patterns (coach's tells)

| Anti-pattern | Tell | Fix |
|--------------|------|-----|
| **Solution smuggled in as the problem** | "Users need bulk export" | Rewrite as a job story; the feature is one candidate answer |
| **Single-source certainty** | One great interview, verdict Yes | One type = *Not yet*; go get the second type |
| **Volume mistaken for breadth** | "Tickets are through the roof" from three accounts | Count distinct sources; check the quant row |
| **HiPPO alignment** | Alignment scored 5 because an exec asked | Alignment is against the *stated* goal metric; a sponsor's interest is an operational row at confidence 2 |
| **Averaging a conflict away** | "Mixed signals, call it a 3" | Explain the conflict (segment? measurement? wrong statement?) or leave it unresolved and verdict *Not yet* |
| **Goal-blind scoring** | Same scores whether the goal is retention or acquisition | Fix the goal reading first; acquisition flips what breadth counts toward |
| **Recency** | Last week's escalation ranks first | Date every row; weight recent *and* repeated |
| **Confidence in the problem, not the source** | One "5" written for the whole table | Confidence is per row; the problem's strength emerges from convergence |

## 5. Worked example (short)

**Goal reading:** default — the quarter's committed outcome is 90-day
retention of new workspaces.

**Candidate:** "customers want an import wizard" (sales ask).

- **Step 1** — rewritten: *When my first import fails part-way, I want to
  recover without re-entering what already worked, so I can finish setup
  the same day and start using the product with my team.*
- **Step 2** — the table in §2: interviews (qual, 4), funnel (quant, 5),
  tickets (ops, 3), sales notes (ops, 2).
- **Step 3** — three types converge on abandonment after partial failure.
  One conflict: sales frames it as a *wizard* (a solution) for enterprise
  demos, while the funnel shows the drop concentrated in *small* teams —
  a segment difference, not a contradiction; the enterprise version may be
  a different problem (mapping complexity) and is split out as candidate
  #4, verdict *Not yet*.
- **Step 4** — **Yes.** Signal 4/4, Alignment 5 (abandoners' retention is
  22 points lower — directly on the goal metric). Rank 1.

Hand-off: the job story becomes the PR/FAQ's problem paragraph and the
evidence table its "how do you know" answer; the split-out enterprise
mapping problem goes to `customer-interviews` with the missing evidence
named (pain and breadth among enterprise admins).

## 6. Conversions (how this plugs into the system)

- **Affinity map → candidates.** Each theme with ≥ 2 distinct sources is a
  candidate problem; write its job story (Step 1) before scoring.
- **Synthesis insight → candidate.** A Track 1 insight ("[segment] do X
  because [why]") is a candidate; its interview evidence is the first
  *Qualitative* row.
- **ODI opportunity → alignment input.** An underserved outcome's
  opportunity score is a *Quantitative* row at confidence 4–5; it
  quantifies pain and breadth within one job. This method then asks the
  question ODI doesn't — how the job's opportunities compete with problems
  *outside* the job for the same roadmap.
- **Assumption ledger.** Every *Not yet* becomes ledger rows ("this
  problem is painful for X", "this problem is widespread among Y") with
  the missing evidence as *what would disprove it* and the cheapest test
  named.
- **PR/FAQ.** *Yes* → the problem paragraph (job story in prose) and the
  internal FAQ's evidence citations (the table, verbatim).
- **Metrics.** Business Alignment consumes the North Star tree; without
  one, the alignment column is opinion.

## Sources & materials

- **"How to pick the right problem"** — the two criteria (Customer Signal,
  Business Alignment), the acquisition flip, the internal-tools reading,
  and the four-step execution framework (JTBD problem statement; evidence
  table with *Source / Type / Confidence in evidence (1–5) / Findings*;
  patterns — convergence and conflict; validation verdict *Yes / Not yet /
  Probably not*) arrived as Daniel O'Rorke's working notes (2026-09-18).
  Original lineage unrecorded — see `./materials/README.md`.
- **Job stories** — Product Institute / Alan Klement; see
  [`../jtbd/job-stories.md`](../jtbd/job-stories.md).
- **Affinity mapping (K-J Method)** — ASQ / Jiro Kawakita; see
  [`./affinity-mapping.md`](./affinity-mapping.md).
- **Evidence tiers** (CONFIRMED / INFERRED / BACKGROUND) — this repo's
  shared ledger convention, from ODI multi-call discovery.
- The scoring anchors (§1), confidence anchors and verdict rules (§2), the
  ranking table (§3) and the anti-patterns (§4) are **this repo's
  operational extension** of the notes.
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

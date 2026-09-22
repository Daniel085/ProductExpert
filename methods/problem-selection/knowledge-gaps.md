# Knowledge-Gap Assessment — Method Reference

*The exit gate of **Problem Validation**: before exploring product
options, score how much you actually know in five areas, and let the
lowest scores choose the next move. The five areas and the three next
moves are **Product Institute** course material (*Product Management
Foundations*), distilled here in paraphrase from the PM's notes and
**not quoted**. The 1–5 anchors, the decision rules, the routing to this
system's agents, and the exit criteria are this repo's operational
extension. See [`../../CREDITS.md`](../../CREDITS.md).*

> **Why a separate gate.** A *Yes* verdict on a problem
> ([`picking-the-right-problem.md`](./picking-the-right-problem.md))
> says the problem is real and worth solving. It does not say you know
> enough to start generating solutions. Teams that skip this step
> brainstorm against a problem they can describe but cannot explain,
> in a market they haven't looked at, under constraints nobody has
> checked — and the options they generate inherit every gap.

## 1. The five areas

Score each **1–5** for *confidence in what we know*, with the evidence
that backs the score. Scores are per problem, not per team.

| # | Area | The question | 1 — guessing | 3 — partial | 5 — confident |
|---|------|--------------|--------------|-------------|---------------|
| 1 | **Problem definition** | How clearly can we state the problem we're solving? | A theme or a feature request; no job story; the team describes it differently | A job story exists; situation or outcome still vague; scope contested | One job story everyone repeats the same way; the *why* behind it is an insight, not a restatement |
| 2 | **User behavior** | How do users address this need today? | We assume; no observed workaround | We've heard about workarounds; not seen them; frequency unknown | We have watched the current path (tools, workarounds, who, how often, what it costs them) and can name what would get fired |
| 3 | **Competitive landscape** | Who else solves this, how, and what can we learn from them? | We haven't looked | A list of names; no teardown of how they solve it, what they charge, where they fall short | We know the alternatives (products *and* non-consumption), their approach, price band, and their users' complaints; we know whether our wedge is a product or a feature |
| 4 | **Technical constraints** | What limits how we could solve it? | Nobody has asked engineering | A hunch about the hard parts; no spike, no data on integration, scale, compliance | Constraints verified (which are real, which are preferences); the hard part identified; a feasibility spike or an expert's read on it |
| 5 | **Business impact** | Revenue opportunity and strategic alignment? | "It seems important"; no number, no stated goal | Aligned to a goal in words; size is an order-of-magnitude guess | A sized opportunity (customers × value × reachability) tied to a named goal metric, with the counter-case written |

Rules for scoring:

- **Evidence per row.** Cite the artifact each score rests on (problem
  case, synthesis readout, ODI scores, scan table, spike notes, metric
  definitions) and its tier — CONFIRMED / INFERRED / BACKGROUND
  ([`../customer-interviews/assumption-ledger.md`](../customer-interviews/assumption-ledger.md)).
  A 4 or 5 on BACKGROUND evidence alone is a 3.
- **Score what you know, not how you feel.** "We've talked about it a
  lot" is not knowledge. If two people on the team would score an area
  differently, score it at the lower value and note the disagreement.
- **Reuse, don't re-derive.** Area 1 is the problem case's Step 1 and
  Step 3; area 5 is its Customer Signal × Business Alignment; area 3 is
  the landscape scan if one was run. This gate reads those, it doesn't
  redo them.

## 2. From scores to the next move

The three moves from the course, and where they run in this system:

| Move | Choose it when | Runs as |
|------|----------------|---------|
| **Customer interviews** | Problem definition or user behavior is low — we can't state the problem from the customer's side, or we don't know how they cope today | **customer-interviews** prep, with the low areas as the learning goal and the ledger rows as assumptions |
| **Problem analysis** | Problem definition is mid but the *why* is missing — we can describe the symptom but not the root cause | Root-cause analysis: [`root-cause-analysis.md`](./root-cause-analysis.md) (5 Whys, cause-and-effect, interrelationship), run by **problem-selection**; unknowns it exposes route to interviews or data |
| **Competitive analysis** | Competitive landscape is low — market context is unclear and existing solutions have lessons we haven't read | **ideation**'s landscape-scan protocol, run at teardown depth (§3), recorded BACKGROUND |

Two areas the course's three moves don't cover, so this system routes
them explicitly:

| Low area | Move | Runs as |
|----------|------|---------|
| **Technical constraints** | A feasibility conversation or spike — engineering names the hard part and which constraints are real | The PM with engineering; classify each constraint per [`../jtbd/requirements-are-hypotheses.md`](../jtbd/requirements-are-hypotheses.md) (true constraint vs. preference); record in the ledger |
| **Business impact** | Size it and tie it to a goal | **metrics** for the goal metric and its inputs; the problem case's alignment score; **prfaq**'s internal FAQ bank for the sizing and counter-case questions, answered early |

Decision rules *(repo extension)*:

1. **Any area at 1–2 → run its move before generating options.** Don't
   brainstorm past a 2.
2. **Areas at 3 → proceed, but carry them as ledger rows** with the
   cheapest way to raise them. Ideation's assumption-testing mode will
   attack them.
3. **Pick the move for the *lowest* area first**; when two tie, prefer
   the one that is cheapest to close (a scan is a day; interviews are
   weeks).
4. **Re-score after each move.** The scorecard is dated and re-run;
   the delta is the learning.

```
                       problem definition
                       user behavior          ── low ──> customer interviews
                       (why missing)          ── low ──> problem analysis (root cause)
  five-area scorecard  competitive landscape  ── low ──> competitive analysis (landscape teardown)
                       technical constraints  ── low ──> feasibility spike (engineering)
                       business impact        ── low ──> metrics / sizing
                                              ── all ≥ 3 ──> SOLUTION VALIDATION (explore options)
```

## 3. Competitive analysis at teardown depth

The landscape scan in
[`../ideation/brainstorming.md` §7](../ideation/brainstorming.md) asks
four questions and produces a 5–10 line table. When the competitive
landscape scores low, run it deeper — per alternative, including the
**non-product alternatives** (spreadsheet, agency, doing without):

| Alternative | How it solves the job (steps the user takes) | Price band | Where users say it falls short (reviews, forums, churn reasons) | What we'd have to beat for a user to switch |
|-------------|-----------------------------------------------|-----------|---------------------------------------------------------------|---------------------------------------------|

Then answer: what has the market already learned that we should not
re-learn (the features every alternative converged on; the ones every
alternative dropped); and what job or segment is *nobody* serving. The
table stays **BACKGROUND** — it sharpens the ledger, it validates
nothing. Positioning proper (Dunford) is a roadmap item; this is the
input it will need.

## 4. Exit criteria — ready for Solution Validation

Problem Validation is complete for a problem when:

- [ ] Its problem case has a **Yes** verdict
      ([`picking-the-right-problem.md`](./picking-the-right-problem.md)).
- [ ] The five-area scorecard has **no area below 3**, each score
      evidence-cited and tiered.
- [ ] Every area at 3 has a ledger row with a cheapest test.
- [ ] The problem is written as a **job story**, and the *why* behind it
      is stated as an insight (observation → finding → insight).
- [ ] The **goal metric** the solution must move is named.
- [ ] A one-line **value proposition hypothesis** can be drafted from
      the evidenced jobs, pains and gains
      ([`../jtbd/value-proposition.md`](../jtbd/value-proposition.md)) —
      drafted, not validated.

Then hand off: **ideation** (solution-ideation mode: diverge ≥ 5
options before evaluating) → **lean-experiments** (prove the chosen
option cheaply) → **prfaq**.

## 5. Scorecard template

```
KNOWLEDGE-GAP SCORECARD — <problem, as job story>          dated <date>
Goal metric: <name>                     Problem verdict: Yes (<date>)

| # | Area                   | Score | Evidence (artifact · tier)                     | Gap / disagreement            |
|---|------------------------|-------|------------------------------------------------|-------------------------------|
| 1 | Problem definition     |       |                                                |                               |
| 2 | User behavior          |       |                                                |                               |
| 3 | Competitive landscape  |       |                                                |                               |
| 4 | Technical constraints  |       |                                                |                               |
| 5 | Business impact        |       |                                                |                               |

Lowest area: <#>  → Move: <customer interviews / problem analysis / competitive analysis / spike / sizing>
Owner · timebox · what "closed" looks like: …
Ledger rows added for areas at 3: …
Ready for Solution Validation? yes / not yet (what would change it)
```

## 6. Anti-patterns

| Anti-pattern | Tell | Fix |
|--------------|------|-----|
| **Scoring by enthusiasm** | All 4s and 5s, no artifacts cited | Evidence per row; BACKGROUND-only caps at 3 |
| **Brainstorming through a 2** | "We'll learn as we build" | Run the move first; it is cheaper than the options it would have shaped |
| **Interviews for everything** | Low competitive score → more interviews | Match the move to the area; a scan closes a scan gap |
| **Engineering asked last** | Constraints discovered at design review | Score area 4 now; classify constraints as real or preferred |
| **Impact as adjective** | "Strategic", "big opportunity" | Customers × value × reachability, tied to a named metric |
| **One-time gate** | Scorecard filled once, never dated again | Re-score after each move; keep the deltas |

## Sources & materials

- **Product Institute** (founded by **Melissa Perri**) — *Product
  Management Foundations*, the knowledge-gap assessment at the close of
  problem validation: the five confidence areas (problem definition,
  user behavior, competitive landscape, technical constraints, business
  impact) and the three next moves (customer interviews, problem
  analysis, competitive analysis). Licensed course material —
  **paraphrased from the PM's notes; nothing quoted.**
- The 1–5 anchors, the two additional routes (technical constraints,
  business impact), the decision rules, the teardown table, the exit
  criteria and the scorecard template are this repo's operational
  extension.
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

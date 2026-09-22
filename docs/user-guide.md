# User Guide

How to actually drive ProductExpert: which agent to call when, what to give
it, what you get back, and two end-to-end walkthroughs.

## Which agent, when

Start from where you are:

| Your situation | Agent | Why |
|----------------|-------|-----|
| "I have an idea — is it viable? Let's brainstorm / stress-test it" | `ideation` | Front door: four modes, landscape scan, assumption ledger + routing call |
| "I have an idea — is the problem even real? Who has it?" | `customer-interviews` | Open-ended discovery: assumptions, guide, recruiting |
| "I have interview notes/transcripts — what did we learn? What now?" | `customer-interviews` | Synthesis: patterns → insights → persevere/pivot |
| "The job is validated — I need to map it and capture customer success metrics" | `odi-interviewer` | Job map + desired outcome statements |
| "I'm doing ongoing discovery with a partner / ISV / developer platform" | `odi-interviewer` | Multi-call mode, dual-job framing, developer question banks |
| "I have 150 raw outcome statements — clean them up" | `odi-outcome-editor` | Validate, dedupe, level, coverage-check |
| "Turn these curated outcomes into a survey" | `odi-survey-builder` | Importance × satisfaction instrument + fielding specs |
| "Survey data is back — what should we build, for whom?" | `odi-data-scientist` | Opportunity scores, segments, growth strategy |
| "We have ten problems and one quarter — which first?" | `problem-selection` | Case per problem (job story, evidence table, patterns, verdict), ranked on Customer Signal × Business Alignment |
| "Theme this pile of tickets / feedback / survey comments" | `problem-selection` | Affinity mapping: group before naming, distinct-source counts |
| "Is this problem validated enough to build for?" | `problem-selection` | Verdict Yes / Not yet / Probably not, with the missing evidence named |
| "Are we ready to explore solutions? What don't we know yet?" | `problem-selection` | Five-area knowledge-gap scorecard; lowest area → its move; exit gate |
| "Why is this happening?" / "find the root cause" | `problem-selection` | 5 Whys, fishbone or interrelationship digraph, every why evidenced or marked a guess |
| "Write/review the one-pager for this product idea" | `prfaq` | Working Backwards PR/FAQ, draft or critique |
| "How do we test this before we build it?" / "concierge or Wizard of Oz?" | `lean-experiments` | Experiment card: family, trying-to-prove, Expected / Would-disprove |
| "Run this initiative as a kata" / "what's our current condition?" | `lean-experiments` | Product Kata record: direction → target → obstacle → step → learned |
| "Write / check our value proposition" | `lean-experiments` | Functional + emotional jobs → statement; Strategyzer canvas from evidence |
| "Design this A/B test properly" / "test results are in — ship it?" | `experimentation` | Pre-registration, or trust-checked readout + decision |
| "What should our north star / KPIs be?" / "audit our dashboard" | `metrics` | Metric tree, OMTM, vanity audit, tracking plan |
| "We've been handed a requirements list / stakeholder asks" | `customer-interviews` | De-requirements it: reclassify each ask, trace to problems, then discover |

Rules of thumb:
- **Problem unvalidated → Track 1** (qualitative). **Job validated,
  prioritization unknown → Track 2** (ODI).
- You can also just describe your task without naming an agent — the
  `description` fields route it. Naming the agent is never wrong, though.
- Manage and inspect agents with the `/agents` command.

## What you do vs. what agents do

The agents prep, structure, extract, analyze, and coach. Three things stay
yours:

1. **Conducting interviews** — agents write the guides and process the
   transcripts; you (or your team) hold the conversations.
2. **Fielding surveys** — the builder produces the instrument and specs; you
   run it through your panel/list/tool.
3. **Deciding** — agents end with evidence and a recommendation; the
   persevere/pivot call and the roadmap bet are yours.

A practical habit: keep one working folder per discovery effort (e.g.
`discovery/<project>/`) and point the agents at it — they read its artifacts
and save theirs there, so each stage picks up where the last left off.

## Track 1 walkthrough — qualitative discovery

**0 · Ideate (when the idea is still fuzzy).**
> "Use the **ideation** agent. Idea: `<one line>`."

A conversation, not a document: it names its mode, frames the problem
around the job, forces real divergence (≥5 options before evaluating
any), provokes, runs a short landscape scan (recorded as BACKGROUND —
context, never a verdict), and captures an **assumption ledger** with the
riskiest assumption, its cheapest test, and a routing call. If the route
is "interview," the ledger becomes step 1's assumption list as-is.

**1 · Prep.**
> "Use the **customer-interviews** agent to prep interviews for `<idea>`."

Give it: the idea in a line, who you think the customer is, the riskiest
assumption (it asks for what's missing, max ~3 questions). You get: a
learning goal, an assumption tracker ranked by impact × uncertainty, target
archetypes + screener, a non-leading interview guide, recruiting/outreach
copy, and a debrief template — saved as files. It can also run a **mock
interview** to let you rehearse before the real ones.

**2 · You interview.** Use the guide; fill the debrief after each session;
drop notes/transcripts into the working folder.

**3 · Synthesize.**
> "Have the **customer-interviews** agent synthesize the notes in
> `discovery/<project>/notes/`."

You get: observations vs. interpretations per interview, patterns with
head-counts, insights held to the quality bar, an assumption scorecard with
updated conviction, bias callouts, and a **persevere / pivot / dig deeper**
recommendation with the next test framed as *We believe / To verify / Built /
Measured / Found out*.

**4 · The bridge.** If the call is *persevere* and the question becomes
"which needs do we prioritize?", carry the validated job forward — phrased
solution-agnostically:

```
Job Executor:        [who performs the job]
Core Functional Job: [verb + object + contextual clarifier]
```

That's the ODI pipeline's required input. Track 2 starts here.

## Track 2 walkthrough — the ODI pipeline

**1 · Discover** (`odi-interviewer`)
> "Use the **odi-interviewer** to prep ODI interviews for:
> Job Executor: …, Core Functional Job: …"

You provide: the market definition, access to 5–8 people who perform the job,
and (for ongoing partner discovery) any prior briefs/call reports. You get: a
pre-interview "What We Know / What We Don't Know" summary, a draft job map,
and a time-budgeted guide — per call, if it's a multi-call engagement.

After each conversation, hand it the transcript:
> "Extract outcome statements from `discovery/<project>/call2-transcript.md`."

It returns properly structured, numbered statements plus the updated
discovery status (cumulative count vs. the 100+ target, open questions).
Repeat to saturation (5–8 interviews, few new outcomes appearing).

**2 · Curate** (`odi-outcome-editor`)
> "Run the **odi-outcome-editor** on `discovery/<project>/outcome-statements.md`."

You get: 80–120 curated statements, a coverage report across all 8 job-map
steps, a change log of every merge/rewrite/delete, and a verdict — **Ready
for Survey Builder: Yes/No**. If No, it hands you a targeted interview
request; take it back to step 1 for focused follow-ups. Don't skip this gate:
surveying redundant or malformed statements wastes real fielding money.

**3 · Quantify** (`odi-survey-builder`)
> "Have the **odi-survey-builder** build the instrument from the curated set."

You get: the full numbered survey (screener → context → dual importance/
satisfaction ratings → related/emotional/social jobs → profiling), fielding
specs (population, sample size, quotas, method), and a data dictionary.
**You field it** — to the spec'd sample (180–600 depending on market; ≥ 3×
the statement count) — and export a clean CSV per the data dictionary.

**4 · Analyze & act** (`odi-data-scientist`)
> "Point the **odi-data-scientist** at `discovery/<project>/survey-results.csv`."

It validates the dataset (N ≥ 180, speeders/straight-liners, missing data),
computes opportunity scores, and delivers: the ranked opportunity table, the
opportunity landscape plot, needs-based segments (statistically validated),
segment profiles, and a growth-strategy recommendation — plus the Python
scripts, so the analysis is reproducible. If you have solution concepts, give
it those too and it scores their coverage and segment fit.

**What you walk away with:** which unmet needs to target (scored), which
segment to serve first (sized and profiled), and which strategy the data
supports — evidence for the roadmap conversation, not a substitute for it.

## The selection gate — which problem?

**Problem selection** (`problem-selection`)
> "Use the **problem-selection** agent. Goal this quarter: `<North Star /
> committed outcome>`. Candidates: `<list>` — or theme
> `discovery/<project>/tickets.csv` first."

Give it the goal (it needs one to score Business Alignment — no goal, it
sends you to `metrics`) and the candidates or the raw pile. It first says
which **goal reading** applies — default, the acquisition flip (breadth
counts on the business side), or internal tools — then, if the input is
raw, **affinity-maps** it (groups before naming, counts distinct sources,
keeps loners). For each candidate you get a four-step case: the problem as
a **job story** (solution-nouns rewritten), an **evidence table** —
*Source / Type (qualitative · quantitative · operational) / Confidence
1–5 / Findings* — the **patterns** (which source types converge, which
conflict and why, which are missing), and a verdict: **Yes / Not yet /
Probably not**, with the rule that produced it.

Then the ranking table: *Yes* verdicts ordered by Customer Signal ×
Business Alignment; *Not yet* as a **learn list** (the missing evidence
and its cheapest source — interviews, a metric query, a ticket audit);
*Probably not* archived with the reason. Expect *Not yet* often — one
vivid source type is never enough — and expect it to refuse to score
"users need bulk export" until it's a problem rather than a feature.

**Before you explore options** — the exit gate:
> "Gap-assess `<problem>` — are we ready for solutions?"

You get the five-area scorecard (problem definition, user behavior,
competitive landscape, technical constraints, business impact), each
score tied to an artifact and its evidence tier, the lowest area named,
and its move: more interviews, a root-cause pass (5 Whys / fishbone /
digraph, which it runs with you), a competitive teardown (it hands that
to `ideation`), an engineering spike, or sizing with `metrics`. No area
below 3 → Problem Validation is done and `ideation` opens the solution
space. It re-scores after each move and keeps the dated deltas.

## Solution validation — prove it before you build it

**Lean experiments** (`lean-experiments`)
> "Use the **lean-experiments** agent. We're trying to prove `<one
> thing>`. Problem evidence: `problem-selection/<topic>-problems.md`."
> "Set up a kata for `<initiative>`; goal metric: `<name>`."
> "Write the value proposition for `<product>` from `discovery/<project>/`."

Give it the problem evidence and one sentence on what most needs to be
true right now. It checks the foundation (evidence, value proposition,
goal), picks the experiment family — **generative** (concierge: deliver
by hand, visibly, to find the solution) or **evaluative** (concept test,
landing page, Wizard of Oz, minimum lovable product: falsify a defined
solution) — and writes the **experiment card** with *Expected* and *Would
disprove* filled in before you run it. You run it with real customers.
Readout compares to those lines and ends persevere / pivot / kill / next
experiment. In **kata** mode it keeps an initiative's record cycle by
cycle — and the first cycles are measurement, because "we don't know the
current condition" is the first obstacle. Expect it to refuse a concierge
test as validation, a manual back-end with no automation vision, or an
"MVP" that is really a rewrite.

## The define–test–measure layer

Three agents pick up where the discovery tracks leave off. They compose —
each one's output is another's input — but each works standalone too.

**PR/FAQ** (`prfaq`)
> "Use the **prfaq** agent to draft a PR/FAQ for `<opportunity>` using the
> synthesis in `discovery/<project>/`."

Give it your discovery artifacts; it gates on the five customer questions,
drafts the one-page press release + FAQs with every claim evidence-cited or
flagged `[ASSUMPTION]`, and ends with an honest verdict recommendation
(iterate / build / kill / park — kill is a success). Also strong in critique
mode: hand it an existing one-pager and ask it to play the skeptical review
room.

**Experimentation** (`experimentation`)
> "Have the **experimentation** agent design a test for: *We believe that…*"
> "Read out `experiments/checkout-test-results.csv` — ship or not?"

Design mode produces a frozen pre-registration (OEC, guardrails, MDE,
sample size with the math shown, run length) and a feasibility check
against your traffic. Readout mode runs trust checks **first** (sample
ratio mismatch can invalidate everything), then gives you confidence
intervals and a ship/don't/iterate call against the boundary you set at
design time. It will tell you when an A/B test is the wrong tool.

**Metrics** (`metrics`)
> "Use the **metrics** agent to define our north star and input metrics."
> "Audit `dashboards/kpis.md` for vanity metrics."

Design, critique, or instrument: a North Star tree with definition cards
and counter-metrics, the One Metric That Matters for your stage, or an
event tracking plan. Expect pushback if you ask for revenue as a north
star or scale-stage metrics on a pre-fit product — that's the method
working.

**How they chain:** discovery evidence → `problem-selection` (the problem
worth a document, with its evidence table) → `lean-experiments` (prove
the solution cheaply; write the value proposition) → `prfaq` (vision +
"what we'd need to believe") → `experimentation` (A/B-test the beliefs a
live product can carry) → `metrics` (define what success means, feeding
goal metrics to katas and OECs to tests). A typical loop: PR/FAQ flags
its riskiest assumption → a Wizard-of-Oz card or a pre-registration →
readout → revise the PR/FAQ's verdict with real evidence.

## Tips

- **Trust the gates.** When an agent refuses input ("this needs curation
  first", "N < 180"), that's the system protecting the next stage. The fix is
  always named.
- **Expect honesty over completion.** Agents are instructed to report
  unchecked checklist items, flag uncertain extractions, and call "no valid
  segmentation" a legitimate finding. If something reads too clean, ask for
  the change log / technical appendix.
- **Timeboxes, roughly:** Track 1 runs days-to-weeks (interviews are the
  bottleneck). Track 2 adds fielding time — typically 1–3 weeks for the
  survey plus the interview rounds. Multi-call partner discovery spans
  weeks-to-months by design.
- **Iterate.** Both tracks are loops, not lines: dig-deeper verdicts, editor
  send-backs, and "found out that…" surprises are the method working, not
  failing.

## Going deeper

- The ideas behind the coaching: [`principles.md`](./principles.md)
- The architecture and handoff gates: [`how-it-works.md`](./how-it-works.md)
- Full method detail: [`../methods/`](../methods/) — every agent cites its
  doc, and the docs cite their sources ([`../CREDITS.md`](../CREDITS.md))

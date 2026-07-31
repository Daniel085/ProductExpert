# User Guide

How to actually drive ProductExpert: which agent to call when, what to give
it, what you get back, and two end-to-end walkthroughs.

## Which agent, when

Start from where you are:

| Your situation | Agent | Why |
|----------------|-------|-----|
| "I have an idea — is the problem even real? Who has it?" | `customer-interviews` | Open-ended discovery: assumptions, guide, recruiting |
| "I have interview notes/transcripts — what did we learn? What now?" | `customer-interviews` | Synthesis: patterns → insights → persevere/pivot |
| "The job is validated — I need to map it and capture customer success metrics" | `odi-interviewer` | Job map + desired outcome statements |
| "I'm doing ongoing discovery with a partner / ISV / developer platform" | `odi-interviewer` | Multi-call mode, dual-job framing, developer question banks |
| "I have 150 raw outcome statements — clean them up" | `odi-outcome-editor` | Validate, dedupe, level, coverage-check |
| "Turn these curated outcomes into a survey" | `odi-survey-builder` | Importance × satisfaction instrument + fielding specs |
| "Survey data is back — what should we build, for whom?" | `odi-data-scientist` | Opportunity scores, segments, growth strategy |
| "Write/review the one-pager for this product idea" | `prfaq` | Working Backwards PR/FAQ, draft or critique |
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

**How they chain:** discovery evidence → `prfaq` (vision + "what we'd need
to believe") → `experimentation` (test the weakest beliefs) → `metrics`
(define what success means, feeding OECs back to the tests). A typical
loop: PR/FAQ flags its riskiest assumption → experiment pre-registration →
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

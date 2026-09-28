# The Interaction Model

How you work with ProductExpert day to day: one folder per initiative,
one status file the agents keep current, one ledger, and a navigator
command that reads them and tells you where you are and who's next.

## Why this exists

The agents are specialists with gates between them, and the gates only
work if every agent reads and writes the same place. Before this
convention each agent chose its own paths and no one answered "where am
I?" — the PM held the map. Now the folder holds it.

## The initiative folder

One directory per initiative, created by `/navigate start` from
[`../templates/initiative/`](../templates/initiative/):

```
initiatives/<slug>/
├── STATUS.md              # phase · gates · log — the agents append here
├── ledger.md              # THE assumption ledger (one per initiative, updated in place)
├── discovery/             # Phase 1 — Opportunity Discovery
│   ├── brainstorm.md      #   ideation
│   ├── interview-guide.md #   customer-interviews (prep)
│   ├── notes/             #   your interview notes and transcripts
│   ├── synthesis.md       #   customer-interviews (synthesis)
│   └── odi/               #   the ODI pipeline (guides, statements, survey, data, analysis)
├── problems/              # Phase 2 — Problem Validation
│   ├── problems.md        #   problem-selection: cases, ranking, learn list, archive
│   ├── gap-scorecard.md   #   problem-selection: the five-area knowledge-gap scorecard
│   └── root-cause-*.md    #   problem-selection: 5 Whys / fishbone / digraph
├── experiments/           # Phase 3 — Solution Validation
│   ├── value-proposition.md   # lean-experiments
│   ├── <name>-breakdown.md    # lean-experiments: feature request → riskiest assumption
│   ├── <name>-card.md         # lean-experiments: experiment card, updated with results
│   ├── <name>-mvp.md          # lean-experiments: MVP card
│   ├── kata.md                # lean-experiments: the running Product Kata record
│   ├── <name>-prereg.md       # experimentation: pre-registration
│   ├── <name>-readout.md      # experimentation: readout
│   └── log.md                 # shared experiment log (lean-experiments + experimentation)
├── options/               # Phase 3 — commit
│   ├── <title>.md         #   solution-options: option card
│   ├── comparison.md      #   solution-options: options side by side
│   └── <title>-v1.md      #   solution-options: minimum feature set
├── prfaq/
│   └── prfaq.md           #   prfaq, with the review record at the bottom
└── metrics/
    ├── metric-tree.md     #   metrics
    ├── tracking-plan.md
    └── dashboard-audit.md
```

Rules:

- **The slug is the initiative's name** in kebab-case (`import-recovery`,
  `seller-self-service`). Agents are told the slug; they never guess a
  path.
- **Subfolders are created on first use**, not all at once — an empty
  `prfaq/` says nothing. `/navigate start` creates the root, `STATUS.md`,
  `ledger.md` and `discovery/`.
- **One ledger.** Every agent that touches assumptions edits
  `ledger.md` in place (the template is
  [`../methods/customer-interviews/assumption-ledger.md`](../methods/customer-interviews/assumption-ledger.md)).
  No agent starts a second tracker.
- **Your material goes in too** — notes, transcripts, ticket exports,
  survey CSVs — so agents can read it and so the evidence trail is in
  one place.
- **Commit it or ignore it, your choice.** `initiatives/` holds your
  work, not the toolkit's; version it in your own repo or add it to
  `.gitignore` here.

## STATUS.md

The initiative's audit trail across all three phases — what the kata
record is within one. Agents append to it; the navigator reads it.
Template at [`../templates/initiative/STATUS.md`](../templates/initiative/STATUS.md).

Three parts:

1. **Header** — initiative, slug, owner, created, goal metric (or "not
   yet defined → metrics"), current phase.
2. **Gates** — the ten checkpoints below, each with status, date, the
   artifact it rests on, and the verdict. The gates are the truth about
   where an initiative is; the phase is derived from them.
3. **Log** — dated entries, one per agent engagement: agent · what was
   done · verdict · artifact · next. Newest last.

### The gates

| # | Gate | Passed when | Owner |
|---|------|-------------|-------|
| G1 | **Framed** | The problem or idea is written as a job story (no solution noun) | ideation · customer-interviews |
| G2 | **Ledger seeded** | `ledger.md` names exactly one riskiest assumption and its cheapest test | ideation · customer-interviews |
| G3 | **Problem evidenced** | A problem case carries verdict **Yes** (or synthesis says *persevere* with ≥ 2 evidence types) | problem-selection · customer-interviews |
| G4 | **Gaps closed** | Knowledge-gap scorecard with no area below 3, evidence-cited | problem-selection |
| G5 | **Promise written** | A value proposition statement from evidenced jobs, pains and gains | lean-experiments |
| G6 | **Solution read out** | ≥ 1 experiment card with *Found out that* and a decision, against pass and kill lines written before the run | lean-experiments · experimentation |
| G7 | **Option chosen** | An option card with status *chosen*, every field past its tell | solution-options |
| G8 | **v1.0 scoped** | A minimum feature set with classes, CD3 on the postponable, a deferred list with costs | solution-options |
| G9 | **Vision decided** | A PR/FAQ with a verdict — build / iterate / kill / park | prfaq |
| G10 | **Success defined** | Metric definition cards for the option's success metrics, with a counter-metric | metrics |

Phase is derived: **Opportunity Discovery** until G2 (framed, ledger
seeded); **Problem Validation** until G4; **Solution Validation** until
G9. G10 and G5 can
pass any time after G3. Kill and park are passes, not failures — a G9
verdict of *kill* closes the initiative with its reasons on record.

Gates are never marked by hand to move things along. An agent marks a
gate when its artifact meets the gate's rule; the navigator re-derives
the gate table from the artifacts when it runs `status`, and flags any
gate whose artifact doesn't back it.

## The navigator: `/navigate`

A slash command that runs in your main session (agents can't call each
other; the session can). Four verbs:

| Verb | What it does |
|------|--------------|
| `/navigate start` | Asks what you have in hand — an idea, a feature request, a pile of problems, interview notes, survey data — and a name; scaffolds `initiatives/<slug>/` from the templates; writes the header; routes you to the first agent with the slug and the input |
| `/navigate status [slug]` | Reads `STATUS.md` and the folder; re-derives the gates from the artifacts; reports phase, gates passed, the blocker, and any gate the status file claims that the artifacts don't back |
| `/navigate next [slug]` | Names the agent to invoke, what it needs that exists, what it needs that doesn't, and the exact invocation |
| `/navigate list` | All initiatives with phase, last entry, and open blocker |

With one initiative in the folder the slug is optional. The navigator
never does an agent's work and never marks a gate itself.

### Where each input enters

| You arrive with | The navigator routes to | First artifact |
|-----------------|------------------------|----------------|
| An idea, a direction, a hunch | **ideation** | `discovery/brainstorm.md` + `ledger.md` |
| A feature request with no evidence behind it | **customer-interviews** (trace the problem first) | `discovery/interview-guide.md` |
| A feature request for a problem that already has evidence | **lean-experiments** (breakdown mode) | `experiments/<name>-breakdown.md` |
| A pile of tickets, feedback, or stakeholder asks | **problem-selection** (theme mode) | `problems/problems.md` |
| Interview notes or transcripts | **customer-interviews** (synthesis) | `discovery/synthesis.md` |
| A validated job and the question "which needs?" | **odi-interviewer** | `discovery/odi/` |
| Survey data | **odi-data-scientist** | `discovery/odi/analysis/` |
| A tested solution to write up | **solution-options** | `options/<title>.md` |
| "What should we measure?" | **metrics** | `metrics/metric-tree.md` |

## What stays yours

Unchanged from [`user-guide.md`](./user-guide.md): you conduct the
interviews, you field the surveys, you run the experiments with real
customers, and you make the persevere / pivot / build / kill calls. The
navigator tells you where you are; it does not move you.

## Adding an agent

An agent joins the model by declaring, in its `## Deliverables` section,
which `initiatives/<slug>/` paths it writes, and by appending a log entry
and marking its gate in `STATUS.md` when it finishes. If it owns a new
checkpoint, add the gate here and in the template, and teach the
navigator's `status` verb how to derive it from the artifact.

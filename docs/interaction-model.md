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
├── STATUS.md              # phase · gates · owed by you · log — the agents append here
├── readout.md             # /navigate readout: the case so far, on one page, from the artifacts
├── readout/               # /navigate readout slides: slides.md, and any exported copy of the case
├── ledger.md              # THE assumption ledger (one per initiative, updated in place)
├── discovery/             # Phase 1 — Opportunity Discovery
│   ├── brainstorm.md      #   ideation
│   ├── interview-guide.md #   customer-interviews (prep), with the pass and fail lines and their sign-off
│   ├── interview-zero.md  #   customer-interviews: the question list for the sponsor's own organisation, when it has the problem
│   ├── notes/             #   your interview notes and transcripts; desk-research's numbered notes (NN-<topic>.md)
│   │   └── raw/           #   pages and exports you saved for desk-research (keep out of version control)
│   ├── synthesis.md       #   customer-interviews (synthesis)
│   ├── sizing.md          #   opportunity-sizing: one-page summary + assumptions register, both routes, tests
│   ├── sizing.py          #   opportunity-sizing: the re-runnable Monte Carlo model (or a spreadsheet / Guesstimate link)
│   ├── sizing-sources/    #   downloaded count and price tables
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
- **The strategy stack lives above the initiatives.** If you keep one
  (vision · strategic intents · product initiatives · options —
  [`../methods/strategy/product-strategy.md` §7](../methods/strategy/product-strategy.md)),
  put it at `strategy/strategy.md` next to `initiatives/`, with the
  product strategy memo beside it as `strategy/strategy-memo.md`; each
  initiative's *Direction* row cites its intent and initiative from
  there. Same rule: yours, not the toolkit's.

## STATUS.md

The initiative's audit trail across all three phases — what the kata
record is within one. Agents append to it; the navigator reads it.
Template at [`../templates/initiative/STATUS.md`](../templates/initiative/STATUS.md).

Four parts:

1. **Header** — initiative, slug, owner, created, purpose (what this is
   for: a new business, a new line, a route to market, an improvement —
   or "undecided", which the PM then owes), goal metric (or "not
   yet defined → metrics"), direction (the strategic intent and product
   initiative this serves, from the PM's strategy stack — or "not
   stated → the level above owes it"; the ladder itself is in
   [`../methods/strategy/product-strategy.md` §7](../methods/strategy/product-strategy.md)),
   current phase.
2. **Gates** — the ten checkpoints below, each with status, date, the
   artifact it rests on, and the verdict. The gates are the truth about
   where an initiative is; the phase is derived from them.
3. **Owed by you** — the one list of what only the PM can settle:
   decisions deferred at the start (the purpose, the goal), pass and
   fail lines awaiting sign-off before a round of interviews or an
   experiment, and every assumption an agent made while the PM was away.
   Agents add rows; the PM's answer closes them. No agent keeps such a
   list in its own artifact instead.
4. **Log** — dated entries, one per agent engagement: agent · what was
   done · verdict · artifact · next. Newest last, each one line under
   240 characters; the detail lives in the artifact.

### The gates

| # | Gate | Passed when | Owner |
|---|------|-------------|-------|
| G1 | **Framed** | The problem or idea is written as a job story (no solution noun) | ideation · customer-interviews |
| G2 | **Ledger seeded** | `ledger.md` names exactly one riskiest assumption and its cheapest test | ideation · customer-interviews |
| G3 | **Problem evidenced** | A problem case carries verdict **Yes** (or synthesis says *persevere* with ≥ 2 evidence types) | problem-selection · customer-interviews |
| G4 | **Gaps closed** | Knowledge-gap scorecard with no area below 3, evidence-cited; the business-impact area scores 4 or above only with a `discovery/sizing.md` whose load-bearing leaves are at least INFERRED | problem-selection (sizing by opportunity-sizing) |
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
other; the session can). Five verbs:

| Verb | What it does |
|------|--------------|
| `/navigate start` | Asks what you have in hand — an idea, a theory, a feature request, a pile of problems, interview notes, survey data — a name, and **what this is for** (a choice you make or explicitly defer); scaffolds `initiatives/<slug>/` from the templates; writes the header; routes you to the first agent with the slug and the input |
| `/navigate status [slug]` | Reads `STATUS.md` and the folder; re-derives the gates from the artifacts; reports phase, gates passed, the blocker, any gate the status file claims that the artifacts don't back, and any summary (readout, slides, a copy elsewhere) built from older evidence than the folder now holds |
| `/navigate next [slug]` | Names the agent to invoke, what it needs that exists, what it needs that doesn't, and the exact invocation |
| `/navigate readout [slug]` | Writes `readout.md`: the case so far on one page, for someone who was not in the room, from the artifacts only — what is and isn't validated, what the evidence did to what you arrived with, what is unproven, what happens next, what it rests on. Marks no gate; never shown to anyone about to be interviewed |
| `/navigate readout [slug] slides` | Writes `readout/slides.md` from `readout.md`, following `templates/readout-slides.md`: a fixed outline, one finding a slide, caveats in the speaker notes, the decision asked of the room on a slide of its own |
| `/navigate hypothesis [slug]` | Takes in a new belief part-way through: one ledger row (ideation), the cheapest public check (desk-research), one interview probe if a round has not begun, then add-evidence if cases exist |
| `/navigate list` | All initiatives with phase, last entry, and open blocker |

With one initiative in the folder the slug is optional. The navigator
never does an agent's work and never marks a gate itself.

### Where each input enters

| You arrive with | The navigator routes to | First artifact |
|-----------------|------------------------|----------------|
| An idea, a direction, a hunch | **ideation** | `discovery/brainstorm.md` + `ledger.md` |
| A theory — who struggles with what, and why — and nothing from customers yet | **ideation** (one ledger row per claim), then **desk-research**, then **problem-selection** (theory test) | `ledger.md`, then `discovery/notes/NN-*.md`, then the claims table in `problems/problems.md` |
| A question public sources could answer; pages, threads or exports you saved | **desk-research** | `discovery/notes/NN-<topic>.md` |
| A new hypothesis, part-way through an initiative | `/navigate hypothesis`: **ideation** (one ledger row), then **desk-research** (the cheapest public check), then **customer-interviews** (one probe, if no round has begun) | a new row in `ledger.md`, then a note |
| More evidence, after the problem cases are written | **problem-selection** (add evidence) | a dated *Evidence added* section in `problems/problems.md` |
| A feature request with no evidence behind it | **customer-interviews** (trace the problem first) | `discovery/interview-guide.md` |
| A feature request for a problem that already has evidence | **lean-experiments** (breakdown mode) | `experiments/<name>-breakdown.md` |
| A pile of tickets, feedback, or stakeholder asks | **problem-selection** (theme mode) | `problems/problems.md` |
| Interview notes or transcripts | **customer-interviews** (synthesis) | `discovery/synthesis.md` |
| A validated job and the question "which needs?" | **odi-interviewer** | `discovery/odi/` |
| "How big is this market / opportunity?" — an investor asked for a TAM, or the gap scorecard's business-impact area is low | **opportunity-sizing** | `discovery/sizing.md` + `discovery/sizing.py` |
| Survey data | **odi-data-scientist** | `discovery/odi/analysis/` |
| A tested solution to write up | **solution-options** | `options/<title>.md` |
| "What should we measure?" | **metrics** | `metrics/metric-tree.md` |

## Delegation briefs and context discipline

Two rules borrowed from how orchestrated agent systems stay reliable
(Anthropic's research-system and effective-agents write-ups, cited in
[`how-it-works.md`](./how-it-works.md)):

- **Every hand-off is a brief, not a nudge.** The navigator (or you, when
  you invoke an agent directly) gives the agent seven things: the
  objective and mode; the input paths; the output paths and format; the
  gate it may mark and its rule; whether the PM is present; the
  boundaries (what not to do, when to stop and route back); and the
  effort level (light / standard / deep, from the size of the input). The template is in the navigator skill.
  An agent given less improvises; an agent given more reads everything.
- **Agents read the summary, then only what the gate needs.** `STATUS.md`
  is the condensed record of everything that happened before; an agent
  reads it first, then `ledger.md`, then the artifacts its gate depends
  on, and never the whole folder. It writes its results to files and
  reports **paths**, not contents — the folder is the shared memory;
  the conversation is not. This keeps each engagement's context small
  and keeps long initiatives from degrading as they grow.

- **An agent working without you says what it assumed, in one place.**
  A brief marked *PM present: no* tells the agent not to ask. It makes
  the smallest assumption that lets it proceed and writes each one under
  *Owed by you* in `STATUS.md`. Two things are never assumed: a goal
  (alignment stays unscored) and a pass or fail line for a round the PM
  has not signed off.

## Public evidence

What is already public is collected by **desk-research**
([`../methods/desk-research/desk-research.md`](../methods/desk-research/desk-research.md))
into numbered, source-tagged rows that every later artifact cites by
number. It is BACKGROUND whatever its volume and never passes G3. Three
conventions hold across agents:

- **The access ladder.** Fetch; then a browser the agent controls; then
  your own browser with your go-ahead; then you save the pages into
  `discovery/notes/raw/`. A refusal is climbed past by the next rung,
  never worked around.
- **Intake.** Files you supply are checked on arrival (readable, the
  right page, duplicates, complete, kind) and you are asked once for
  re-saves.
- **Silence is written down.** Every note ends with what was refused,
  what was not searched, and what was searched and not found.

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

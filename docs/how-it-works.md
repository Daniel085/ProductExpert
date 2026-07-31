# How the System Works

The architecture of ProductExpert: what the pieces are, how an agent run
actually happens, and how the agents compose into pipelines.

## The pieces

```
ProductExpert/
├── .claude/agents/                  # BEHAVIOR — one file per agent
│   ├── customer-interviews.md       #   qualitative discovery coach
│   ├── odi-interviewer.md           #   ODI Phase 1: discover
│   ├── odi-outcome-editor.md        #   ODI Phase 1.5: curate
│   ├── odi-survey-builder.md        #   ODI Phase 2: quantify
│   ├── odi-data-scientist.md        #   ODI Phase 3: analyze & act
│   ├── prfaq.md                     #   Working Backwards PR/FAQ coach
│   ├── experimentation.md           #   A/B test design & readout
│   └── metrics.md                   #   North Star trees, OMTM, tracking plans
├── methods/                         # KNOWLEDGE — what the agents read
│   ├── customer-interviews/
│   │   ├── talking-to-humans.md     #   method + templates
│   │   ├── research-and-insight.md  #   effective research & good insight
│   │   └── materials/               #   third-party source materials
│   ├── odi/
│   │   ├── process-map.md           #   the pipeline spec (phases, steps, gates)
│   │   ├── outcome-statements.md    #   canonical statement grammar & rules
│   │   ├── interviewing.md          #   interview protocols (incl. partner mode)
│   │   ├── survey-design.md         #   instrument, sizing, dataset standards
│   │   └── opportunity-analysis.md  #   scoring, segmentation, strategy
│   ├── jtbd/
│   │   ├── job-stories.md           #   job-story framing; user-story rewrites
│   │   ├── requirements-are-hypotheses.md # de-requirement intake protocol
│   │   └── materials/               #   Product Institute lesson (source PDF)
│   ├── prfaq/
│   │   └── working-backwards.md     #   PR structure, FAQ banks, process
│   ├── experimentation/
│   │   └── trustworthy-experiments.md # design, trust checks, decisions
│   └── metrics/
│       ├── north-star.md            #   NSM, metric trees, tracking plans
│       └── lean-analytics.md        #   good metrics, OMTM, stages, cohorts
├── docs/                            # THIS documentation
│   ├── principles.md                #   the ideas the system runs on
│   ├── how-it-works.md              #   (this file)
│   └── user-guide.md                #   how to drive it
├── README.md                        # map & quick start
└── CREDITS.md                       # attribution (master list)
```

Two kinds of file matter:

- **Agent files** (`.claude/agents/*.md`) — a YAML frontmatter
  (`name`, `description`, `tools`, `model`) plus a behavior prompt: role,
  non-negotiables, input gates, process, deliverables, handoffs. Claude Code
  discovers these automatically and offers them as subagents.
- **Method docs** (`methods/`) — the knowledge: protocols, grammars,
  templates, worked examples, checklists. Authored once, read by every agent
  that needs them.

The contract between the two: **every agent's first instruction is to read
its method docs.** Behavior files stay thin (~100 lines); knowledge lives
where it can be shared, versioned, and corrected in one place.

## How a request becomes an agent run

1. **Routing.** You either name an agent explicitly ("use the odi-interviewer
   to…") or just describe your task — Claude matches it against each agent's
   `description`. Descriptions carry trigger vocabulary ("job map", "outcome
   statements", "synthesize interview notes") *and* disambiguation pointers
   ("for open-ended early discovery use customer-interviews instead"), so
   adjacent requests land on the right specialist. `/agents` lists and
   manages them.
2. **Grounding.** The agent reads its method docs first. If a doc is missing
   it falls back to the principles embedded in its own prompt — degraded but
   functional.
3. **Gating.** Before doing the work, the agent checks its input gate (e.g.
   the survey builder verifies it has *curated* statements with a coverage
   report; the data scientist verifies N ≥ 180 and < 10% missing). Failing
   input goes back upstream with a specific request — that's a feature, not
   an error.
4. **Working.** The agent produces its deliverables in the formats its
   method doc defines, saving artifacts as files in your working folder
   (guides, statement sets, instruments, scripts, plots) so the next stage
   can pick them up.
5. **Handing off.** The agent ends by naming what's next: which agent takes
   this output, and what gate that agent will apply.

## The two method families — and the bridge

### Track 1 — Qualitative discovery (`customer-interviews`)

For when the riskiest thing is the idea itself. One agent with two modes:

```
PREP:        learning goal → ranked assumptions → segments & screener
             → non-leading interview guide → recruiting plan → debrief template
   ↓  (you conduct the interviews)
SYNTHESIS:   observations vs interpretations → patterns → insights
             → assumption scorecard → persevere / pivot / dig deeper + next test
```

### Track 2 — The ODI pipeline (four agents)

For when the job is validated and the question is *which needs to
prioritize*. Four agents in series, with one feedback loop and two
human-in-the-loop steps:

```
            market definition (Job Executor + Core Functional Job)
                                    │
                          ┌─────────▼─────────┐
                          │  odi-interviewer  │  Phase 1 · Discover
                          │  job map · guides │  ← you conduct the calls
                          │  outcome extract  │
                          └─────────┬─────────┘
              follow-up    raw statements (100+) · gate: saturation
              interview   ┌─────────▼─────────┐
              request ┌───│ odi-outcome-editor│  Phase 1.5 · Curate
                      └──>│ validate · dedupe │
                          │ level · coverage  │
                          └─────────┬─────────┘
                       curated 80–120 · gate: all checks pass
                          ┌─────────▼─────────┐
                          │ odi-survey-builder│  Phase 2 · Quantify
                          │ instrument · specs│  ← you field the survey
                          └─────────┬─────────┘
                        clean CSV · gate: N ≥ 180, < 10% missing
                          ┌─────────▼─────────┐
                          │ odi-data-scientist│  Phase 3 · Analyze & Act
                          │ scores · segments │  gate: silhouette > 0.25
                          │ strategy          │
                          └─────────┬─────────┘
                                    ▼
              ranked opportunities · segments · growth strategy
```

Full step-by-step detail (the 12 steps, gate table): see
[`../methods/odi/process-map.md`](../methods/odi/process-map.md).

### The bridge between tracks

The qualitative track's *persevere* decision produces a validated,
solution-agnostic job — which is, verbatim, the **market definition** the ODI
pipeline requires as its first input. The handoff is wired into both sides:
`customer-interviews` recommends it at synthesis time, and `odi-interviewer`
refuses to start without it (and points back to `customer-interviews` when
the job itself is still in question).

```
customer-interviews ──(validated job)──> odi-interviewer ──> … pipeline …
        ▲                                                          │
        └── "the problem isn't validated yet" ◄────────────────────┘
```

### The define–test–measure layer

Three agents sit around both tracks and consume their evidence:

```
discovery evidence (Track 1 insights · Track 2 scores/segments)
        │
        ▼
      prfaq ──("what we'd need to believe")──> experimentation
        │                                            ▲
        └──("how we'll measure success")──> metrics ─┘
                                            (OEC & guardrails)
```

- **prfaq** writes the product vision *backwards* from the customer, citing
  discovery artifacts as its evidence base; its hardest open beliefs become
  test hypotheses.
- **metrics** owns what's worth measuring — the North Star tree and
  counter-metrics — which the other two inherit (success metrics for the
  PR/FAQ; OEC and guardrails for experiments).
- **experimentation** turns beliefs into pre-registered, trust-checked A/B
  tests and feeds validated learning back to the documents and decisions
  that spawned them.

## Where knowledge lives (single source of truth)

Knowledge shared by several agents is written exactly once:

| Topic | Canonical file | Read by |
|-------|---------------|---------|
| Outcome-statement grammar, validity, editing rules | `methods/odi/outcome-statements.md` | all four ODI agents |
| Pipeline phases, steps, handoff gates | `methods/odi/process-map.md` | all four ODI agents |
| Interview protocols (classic, multi-call, partner, developer banks) | `methods/odi/interviewing.md` | odi-interviewer |
| Survey instrument, sizing, score conversion, dataset standards | `methods/odi/survey-design.md` | odi-survey-builder, odi-data-scientist |
| Opportunity algorithm, segmentation, strategy | `methods/odi/opportunity-analysis.md` | odi-data-scientist |
| Qualitative interview method & templates | `methods/customer-interviews/talking-to-humans.md` | customer-interviews |
| Effective-research principles & insight quality bar | `methods/customer-interviews/research-and-insight.md` | customer-interviews |
| PR/FAQ structure, FAQ banks, working-backwards process | `methods/prfaq/working-backwards.md` | prfaq |
| Experiment design, trust checks, decision framework | `methods/experimentation/trustworthy-experiments.md` | experimentation |
| North Star framework, metric trees, tracking plans | `methods/metrics/north-star.md` | metrics, experimentation |
| Good-metric tests, OMTM, stages, archetypes, cohorts | `methods/metrics/lean-analytics.md` | metrics |
| Job-story framing (needs vs. features; user-story rewrites) | `methods/jtbd/job-stories.md` | customer-interviews, odi-interviewer, prfaq |
| Requirement intake (constraint / theory / hypothesis) | `methods/jtbd/requirements-are-hypotheses.md` | customer-interviews, odi-interviewer, prfaq |

If a rule changes (say, the abstraction guide for statements), it changes in
one file and every agent inherits it on its next run.

## Extending the system

The recipe for a new agent (also in the README):

1. **Distill the knowledge** → `methods/<topic>/<source>.md`, with templates
   and checklists; raw third-party materials under
   `methods/<topic>/materials/`.
2. **Define the behavior** → `.claude/agents/<name>.md`: frontmatter with a
   routing-rich `description` (trigger words + scope + pointers to
   neighboring agents), a "read your method docs first" instruction,
   non-negotiables, gates, deliverables, handoffs.
3. **Wire the neighbors** — if it composes with existing agents, add the
   handoff in both directions (body *and* descriptions).
4. **Attribute** — cite sources inline and in `CREDITS.md`.
5. **List it** in the README's Agents section.

Design conventions to keep: agents stay thin; shared knowledge gets one
canonical file; gates are explicit; humans keep the in-the-room work; the
`description` is the router.

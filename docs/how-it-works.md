# How the System Works

The architecture of ProductExpert: what the pieces are, how an agent run
actually happens, and how the agents compose into pipelines.

## The pieces

```
ProductExpert/
├── .claude/agents/                  # BEHAVIOR — one file per agent
│   ├── ideation.md                  #   front-door brainstorming partner
│   ├── customer-interviews.md       #   qualitative discovery coach
│   ├── odi-interviewer.md           #   ODI Phase 1: discover
│   ├── odi-outcome-editor.md        #   ODI Phase 1.5: curate
│   ├── odi-survey-builder.md        #   ODI Phase 2: quantify
│   ├── odi-data-scientist.md        #   ODI Phase 3: analyze & act
│   ├── problem-selection.md         #   which problem, on what evidence
│   ├── lean-experiments.md          #   pre-build tests, product kata, value props
│   ├── solution-options.md          #   option cards; v1.0 minimum feature set (cost of delay)
│   ├── prfaq.md                     #   Working Backwards PR/FAQ coach
│   ├── experimentation.md           #   A/B test design & readout
│   └── metrics.md                   #   North Star trees, OMTM, tracking plans
├── methods/                         # KNOWLEDGE — what the agents read
│   ├── ideation/
│   │   ├── brainstorming.md         #   modes, rhythm, scan protocol
│   │   └── materials/               #   product-brainstorming skill (verbatim)
│   ├── customer-interviews/
│   │   ├── talking-to-humans.md     #   method + templates
│   │   ├── research-and-insight.md  #   effective research & good insight
│   │   ├── assumption-ledger.md     #   shared assumption-ledger template
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
│   │   ├── value-proposition.md     #   functional+emotional jobs → statement; Strategyzer canvas
│   │   └── materials/               #   Product Institute lesson; Strategyzer canvas (PDFs)
│   ├── lean-experiments/
│   │   ├── pre-build-experiments.md #   chooser, generative/evaluative, catalogue, card
│   │   ├── riskiest-assumption.md   #   feature request → 8 questions → chain → riskiest link
│   │   ├── minimum-viable-product.md #  MVP = fastest path to insight; failure modes; MVP card
│   │   ├── solution-options.md      #   the option card (11 fields), comparison, gates
│   │   ├── minimum-feature-set.md   #   v1.0 ≠ MVP; feature classes; cost of delay & CD3
│   │   ├── product-kata.md          #   Toyota Kata → Product Kata; record template
│   │   └── materials/               #   Kromer, Perri, Matts, BofA case, Gusto podcast
│   ├── problem-selection/
│   │   ├── picking-the-right-problem.md # criteria, goal readings, 4-step case, ranking
│   │   ├── knowledge-gaps.md        #   five-area scorecard; moves; exit gate to solutions
│   │   ├── root-cause-analysis.md   #   5 Whys, fishbone, interrelationship digraph
│   │   ├── affinity-mapping.md      #   K-J method, text-mode protocol (shared)
│   │   └── materials/               #   ASQ affinity-diagram page (verbatim)
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
   an error. One gate is universal: nothing the agent itself generated
   counts as customer evidence (BACKGROUND at most) — the structural
   guard against the AI-era Product Death Cycle (`principles.md` §29).
4. **Working.** The agent produces its deliverables in the formats its
   method doc defines, saving artifacts as files in your working folder
   (guides, statement sets, instruments, scripts, plots) so the next stage
   can pick them up.
5. **Handing off.** The agent ends by naming what's next: which agent takes
   this output, and what gate that agent will apply.

## The three phases

Every agent serves one of three phases — **Opportunity Discovery**,
**Problem Validation**, **Solution Validation** — and the handoff gates
below are the boundaries between them:

```
 1 · OPPORTUNITY DISCOVERY      2 · PROBLEM VALIDATION            3 · SOLUTION VALIDATION
 ideation                       customer-interviews (synthesis)   lean-experiments
 customer-interviews (prep)     odi-outcome-editor → survey       (concept · concierge · WoZ ·
 odi-interviewer                   builder → data-scientist         prototypes · API · MLP · kata)
                                problem-selection                 solution-options (option · v1.0)
                                                                  prfaq · experimentation · metrics
 ─── what's worth a look? ───>  ─── real? for whom? which? ───>   ─── does THIS solve it, cheaply? ───>
                                       │ exit gate: knowledge-gap
                                       │ scorecard, no area < 3
```

The third phase is where "we heard what they asked for and built it"
gets caught: a validated problem still has to have its *solution*
falsified cheaply (concierge, Wizard of Oz, concept test, a lovable
slice) before the PR/FAQ commits to it and an A/B test measures it.

## The two method families — and the bridge

### Track 1 — Qualitative discovery (`ideation` → `customer-interviews`)

For when the riskiest thing is the idea itself. The front door is
**`ideation`** — a conversational thinking partner for the stage before
interview time is justified: frame → diverge → provoke → converge →
capture, with a short landscape scan recorded as **BACKGROUND-tier**
knowledge (per the CONFIRMED/INFERRED/BACKGROUND tiering — a scan gives
context, never a verdict; only interviews validate a problem) and a ranked
**assumption ledger** as the handoff object. Then `customer-interviews`
takes the ledger forward, with two modes:

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

### The selection gate

Discovery produces more problems than a roadmap can hold, and not all of
them arrive through the tracks — tickets, funnels, sales notes and
stakeholder theories all nominate problems. **`problem-selection`** is the
gate between "we know about these problems" and "we're writing the PR/FAQ
for this one":

```
Track 1 insights · Track 2 opportunities · tickets · analytics · asks
                                │
                    ┌───────────▼───────────┐
                    │   problem-selection   │
                    │ theme (affinity map)  │
                    │ case per problem:     │
                    │  job story → evidence │
                    │  table → patterns →   │
                    │  verdict              │
                    │ rank on Signal ×      │
                    │  Alignment            │
                    └───┬───────┬───────┬───┘
                   Yes  │  Not  │  Prob.│
                        │  yet  │  not  │
                        ▼       ▼       ▼
                     prfaq   customer-  archive
                      (or    interviews (with
                      ODI)   / metrics   reason)
```

Its gates: no solution-noun in a problem statement; no *Yes* from a single
evidence type; no Business Alignment score without a stated goal (that's
`metrics`'s job). Its verdicts route: *Yes* forward, *Not yet* back to
the discovery agent that owns the missing evidence type, *Probably not*
to an archive that records why.

A *Yes* then passes the **knowledge-gap scorecard** before anyone
generates options: confidence 1–5, evidence-cited, in problem definition,
user behavior, competitive landscape, technical constraints and business
impact. The lowest area picks the move — customer interviews, root-cause
analysis (run by `problem-selection`), a competitive teardown (run by
`ideation`), a feasibility spike, or sizing with `metrics` — and Problem
Validation exits only with no area below 3.

### The solution-validation layer

Five agents sit around both tracks and consume their evidence:

```
discovery evidence (Track 1 insights · Track 2 scores/segments · problem-selection Yes)
        │
        ▼
 lean-experiments ──(passed; needs causal rigor)──> experimentation
   concept · concierge · WoZ · prototypes                 ▲
   API access · MLP · kata · value proposition            │
        │ readouts                                        │
        ▼                                                 │
 solution-options ──(iteration plan = kata cycles)──> lean-experiments
   option card · comparison · v1.0 by cost of delay       │
        │ chosen option + v1.0 scope                      │
        ▼                                                 │
      prfaq ──("what we'd need to believe")───────────────┤
        │                                                 │
        └──("how we'll measure success")──> metrics ──────┘
                                            (goal metric · OEC & guardrails)
```

- **lean-experiments** proves the solution before anything is built —
  the cheapest experiment that could say no, gated on problem evidence
  and a written value proposition; iterates in Product Kata cycles, the
  current obstacle picking the test.
- **solution-options** writes what the team now believes it should
  build as an option card (refusing any without a solution readout),
  compares options, and cuts the chosen one to a v1.0 minimum feature
  set by cost of delay — the deferred list, with costs, is the roadmap's
  input.

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
| Value proposition (functional + emotional jobs → statement; Strategyzer canvas; fit) | `methods/jtbd/value-proposition.md` | lean-experiments, prfaq, odi-interviewer |
| Pre-build experiments (chooser, generative/evaluative, catalogue, MVP/MLP/MVI, card) | `methods/lean-experiments/pre-build-experiments.md` | lean-experiments, experimentation (triage) |
| Product Kata (rhythm, coaching questions, record template) | `methods/lean-experiments/product-kata.md` | lean-experiments |
| Feature-request breakdown (eight assumption questions, chain, riskiest link, null-result rule) | `methods/lean-experiments/riskiest-assumption.md` | lean-experiments, ideation, prfaq |
| MVP as learning vehicle (canon, failure modes, alignment questions, maxims, MVP card) | `methods/lean-experiments/minimum-viable-product.md` | lean-experiments, solution-options |
| Option card (11 fields, tells, comparison, gates) | `methods/lean-experiments/solution-options.md` | solution-options, prfaq |
| Minimum feature set (v1.0 ≠ MVP, feature classes, cost of delay, CD3, postponement rules) | `methods/lean-experiments/minimum-feature-set.md` | solution-options |
| Requirement intake (constraint / theory / hypothesis) | `methods/jtbd/requirements-are-hypotheses.md` | customer-interviews, odi-interviewer, prfaq |
| Brainstorming modes, divergence rules, landscape-scan protocol | `methods/ideation/brainstorming.md` | ideation |
| Assumption-ledger template (categories, tiers, ranking, lifecycle) | `methods/customer-interviews/assumption-ledger.md` | ideation, customer-interviews, problem-selection, prfaq, experimentation |
| Problem-selection criteria, goal readings, evidence table, verdicts, ranking | `methods/problem-selection/picking-the-right-problem.md` | problem-selection |
| Knowledge-gap scorecard (five areas, moves, exit criteria) | `methods/problem-selection/knowledge-gaps.md` | problem-selection, ideation, customer-interviews |
| Root-cause analysis (5 Whys, fishbone, interrelationship digraph) | `methods/problem-selection/root-cause-analysis.md` | problem-selection |
| Affinity mapping (K-J): process, text-mode protocol, output template | `methods/problem-selection/affinity-mapping.md` | problem-selection, customer-interviews, ideation |

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

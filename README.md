# ProductExpert

A system of expert subagents for product managers. Each agent distills a body
of training and materials — books, courses, frameworks — into a practical
helper for one specific PM job to be done. The agents compose: outputs of one
are gated inputs of the next.

**Documentation:**
[Principles](docs/principles.md) ·
[How the system works](docs/how-it-works.md) ·
[User guide](docs/user-guide.md) ·
[Credits](CREDITS.md)

## How it's organized

- **`.claude/agents/<name>.md`** — the agents: role, process, guardrails.
  This is *behavior*.
- **`methods/<topic>/`** — the *knowledge* the agents draw on: distilled
  method docs and templates, plus raw third-party materials under
  `materials/`.
- **`docs/`** — principles, architecture, and usage.

> Agents = behavior. `methods/` = knowledge. Keeping them separate means you
> can sharpen an agent by improving its method doc or dropping in new
> materials, without touching how it behaves. Knowledge shared by several
> agents is written exactly once.

## The two tracks

**Track 1 — Qualitative discovery** answers *"is the problem real, and do we
understand it?"* **Track 2 — the ODI pipeline** answers *"which customer
needs should we prioritize, for whom, with what strategy?"* The bridge: a
validated, solution-agnostic job from Track 1 is the market definition that
starts Track 2.

```
TRACK 1 · QUALITATIVE                TRACK 2 · ODI PIPELINE (quantitative)

customer-interviews                  odi-interviewer ──> odi-outcome-editor
  prep → you interview → synthesize        │      ▲______________│
  → persevere / pivot / dig deeper         │      (follow-ups if gaps)
        │                                  ▼
        └── validated job ──────────> odi-survey-builder ──> odi-data-scientist
            (= market definition)       you field the survey   scores · segments
                                                               · strategy
```

## Agents

### Customer Interviews — `customer-interviews`
Preps and synthesizes open-ended discovery interviews. Grounded in *Talking
to Humans* (Constable & Rimalovski), Steve Blank's Customer Development, and
the Fluxx research-and-insight principles.
**Prep:** learning goal → ranked assumptions → segments + screener →
non-leading guide → recruiting → debrief template. **Synthesis:**
observations vs. interpretations → patterns → insights → assumption
scorecard → persevere/pivot/dig-deeper + next experiment.
Method: [`methods/customer-interviews/`](methods/customer-interviews/)

### ODI Interviewer — `odi-interviewer`
Phase 1 (Discover) of Tony Ulwick's Outcome-Driven Innovation. Defines the
market around a job, builds the 8-step job map, preps structured guides
(including multi-call partner/ISV discovery with dual-job framing and
developer question banks), and extracts desired outcome statements from
transcripts. Method: [`methods/odi/interviewing.md`](methods/odi/interviewing.md)

### ODI Outcome Editor — `odi-outcome-editor`
Phase 1.5 (Curate): the quality gate. Validates statement structure,
deduplicates, normalizes abstraction, audits solution-agnosticism, checks
job-map coverage — and sends targeted interview requests upstream when steps
are undercovered. Method: [`methods/odi/outcome-statements.md`](methods/odi/outcome-statements.md)

### ODI Survey Builder — `odi-survey-builder`
Phase 2 (Quantify): turns the curated statements into an importance ×
satisfaction survey instrument with screener, randomization plan, fielding
specs (180–600 respondents), and data dictionary. You field it.
Method: [`methods/odi/survey-design.md`](methods/odi/survey-design.md)

### ODI Data Scientist — `odi-data-scientist`
Phase 3 (Analyze & Act): opportunity scores
(`Importance + max(Importance − Satisfaction, 0)`), the opportunity
landscape, needs-based segmentation (factor + cluster, statistically gated),
segment profiles, and a growth-strategy recommendation — computed with real,
saved Python. Method: [`methods/odi/opportunity-analysis.md`](methods/odi/opportunity-analysis.md)

## Using the agents

Claude auto-delegates based on each agent's `description`, or invoke one
explicitly:

> "Use the **customer-interviews** subagent to prep interviews for `<idea>`."
> "Use the **odi-interviewer** to extract outcome statements from `<transcript>`."
> "Point the **odi-data-scientist** at `<survey-results.csv>`."

Which agent for which situation, end-to-end walkthroughs, and what stays
human: see the **[user guide](docs/user-guide.md)**. Manage agents with the
`/agents` command.

## Adding the next agent

1. Distill the knowledge → `methods/<topic>/<source>.md` (+ raw materials
   under `materials/`).
2. Define the behavior → `.claude/agents/<name>.md`, frontmatter with a
   routing-rich `description`; first instruction: read the method doc.
3. Wire handoffs to neighboring agents (bodies *and* descriptions).
4. Cite sources inline and in [`CREDITS.md`](CREDITS.md); list the agent here.

Full conventions: [docs/how-it-works.md](docs/how-it-works.md#extending-the-system).

## Roadmap (candidate agents)

- **Opportunity solution trees** (Teresa Torres) — next: structures
  discovered opportunities against outcomes and experiments. Gains two
  inputs here: qualitative insights (Track 1) and scored opportunities
  (Track 2). *Terminology note: Ulwick's "opportunity" (an underserved
  outcome) ≠ Torres's "opportunity" (an unmet need/pain/desire on the tree) —
  the agent will need to define both.*
- **Usability testing** (Krug) — evaluative complement to generative
  discovery.
- **Positioning & messaging** (Dunford).
- ~~Jobs-to-be-Done interviews~~ — covered by the ODI family
  (`odi-interviewer`).
- ~~Survey design~~ — covered for needs-quantification by
  `odi-survey-builder`; a general-purpose survey agent remains optional.

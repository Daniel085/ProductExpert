# ProductExpert

A system of expert subagents for product managers. Each agent distills a body
of training and materials — books, courses, frameworks — into a practical
helper for one specific PM job to be done.

## How it's organized

- **`.claude/agents/<topic>.md`** — the agent itself: its role, process, and
  guardrails. This is *behavior*.
- **`methods/<topic>/`** — the *knowledge* the agent draws on:
  - `<source>.md` — the distilled method and templates.
  - `materials/` — raw source materials (PDFs, worksheets, notes, highlights).
- **`README.md`** — this map.

> Agents = behavior. `methods/` = knowledge. Keeping them separate means you can
> sharpen an agent by improving its method doc or dropping in new materials,
> without touching how it behaves.

## Agents

### Customer Interviews — `customer-interviews`

Helps you **prep** for and **synthesize** customer discovery interviews.
Grounded in *Talking to Humans* (Giff Constable & Frank Rimalovski) and Steve
Blank's Customer Development. It prepares and synthesizes; **it does not conduct
the interviews**.

- **Prep:** learning goal → assumptions ranked by risk × uncertainty → target
  segment(s) + screener → non-leading interview guide → recruiting & outreach →
  debrief template.
- **Synthesis:** notes/transcripts → observations vs. interpretations → patterns
  across people → assumption scorecard & conviction update →
  persevere / pivot / dig-deeper.

Method & templates: [`methods/customer-interviews/talking-to-humans.md`](methods/customer-interviews/talking-to-humans.md)
Your materials: drop them in [`methods/customer-interviews/materials/`](methods/customer-interviews/materials/)

## Using an agent in Claude Code

Claude auto-delegates based on each agent's `description`, or you can invoke one
explicitly:

> "Use the **customer-interviews** subagent to prep interviews for `<idea>`."
> "Have the **customer-interviews** subagent synthesize the notes in `./notes/`."

Manage agents with the `/agents` command.

## Adding the next agent

1. Create `methods/<topic>/<source>.md` — distill the method and templates; put
   any raw files under `methods/<topic>/materials/`.
2. Create `.claude/agents/<topic>.md` — role, process, guardrails; tell it to
   read its method doc first.
3. List it under **Agents** above.

## Roadmap (candidate agents)

- Jobs-to-be-Done interviews
- Usability testing
- Survey design
- Positioning & messaging
- Opportunity solution trees

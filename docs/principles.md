# Principles

The ideas ProductExpert runs on. Two layers: the **methodology principles**
the agents coach you with (distilled from the sources in
[`../CREDITS.md`](../CREDITS.md)), and the **design principles** that shape
how the repo itself is built.

---

## Methodology principles

These hold across both method families — qualitative discovery
(*Talking to Humans*) and quantitative ODI. Where a principle has a specific
author, they're named; full attribution in [`../CREDITS.md`](../CREDITS.md).

### 1. Start from the customer's need or job — never the solution
Frame research around what the customer is trying to accomplish, not the
product you intend to build. ODI's strictest form: a market is **a group of
people + a job they're trying to get done** — never a product, technology, or
demographic. "Plan and track a software project" is a market; "Jira users
aged 25–40" is not. Jobs are stable over time even as technologies change,
which is what makes them a foundation worth quantifying. The everyday tell
that you've drifted: a stated "need" with a feature-noun inside it. **A
customer's problem is never your lack of a feature** — no user wants a
button; they want what's behind it.
*(Ulwick; Tebb's principle #1; Product Institute's job-story lesson.)*

### 2. Behavior over opinions; stories over speculation
What people *say* misleads; watch what they *do*. Anchor every interview
question in a specific, recent, real event ("walk me through the last
time…"), never a prediction ("would you use…"). Compliments aren't data;
**commitment** — time, money, data, referrals — is.
*(Constable & Rimalovski; Fitzpatrick; Tebb: "pay attention to people's
behaviours — they lie.")*

### 3. Hunt to disprove, not to confirm
Discovery exists to find the evidence that could kill the idea while it's
still cheap to learn. Rank assumptions by **impact × uncertainty** and attack
the riskiest first. Being wrong is part of the method: you're looking for
**insights, not proof**.
*(Constable & Rimalovski; Blank; Edgley.)*

### 4. Qualitative discovers; quantitative prioritizes
Open-ended interviews find out whether the problem and the job are real —
they generate the hypotheses. Structured quantification (importance ×
satisfaction across 100+ outcomes, N ≥ 180) determines which needs are unmet
and by how much — it ranks the hypotheses. Run them in that order: surveying
unvalidated guesses produces statistically significant noise, and shipping
from interviews alone means betting on anecdotes.

### 5. Solution-agnostic language, always
In jobs, in outcome statements, in survey items: no product names, no UI
elements, no technologies. "Minimize the number of clicks" dies with the
mouse; "minimize the number of steps" survives every interface. This is what
keeps research reusable across product generations. *(Ulwick.)*

### 6. Measure success in the customer's metrics
A desired outcome statement — `[Direction] + [Metric] + [Object] + [Context]`
— captures how the *customer* measures success at getting the job done. One
metric per statement, measurable, actionable. If you can't phrase what you
heard this way, you haven't understood the need yet. *(Ulwick.)*

### 7. The right sample, to saturation — then stop
Talk to the people who actually matter to the question (screeners exist for a
reason), and keep going until **patterns repeat and surprises stop** — in
qualitative work usually 5–12 per segment; in ODI, 5–8 interviews and 100+
outcome statements. Then move on: optimize for decisions, not sample size.
One voice is never a pattern. *(Constable & Rimalovski; Tebb #2.)*

### 8. Separate facts from interpretations — and tier your knowledge
Observations and quotes in one column, inferences in another. In multi-call
discovery, knowledge is tiered: **CONFIRMED** (verbatim, attributed) /
**INFERRED** (conclusion flagged as such, with the words it rests on) /
**BACKGROUND** (public info, not validated by your contact). Exploratory
language ("we're looking to explore…") must never be laundered into confident
assertions.

### 9. An insight explains *why*, and suggests an idea
Climb the ladder: observation → finding (pattern) → **insight** (the
non-obvious why) → opportunity. A good insight is first-person, a fresh
perspective on something implicit, rooted in truth/need/tension, targeted,
and points to action. "Users want it faster" is a restated finding, not an
insight. *(Edgley's six criteria; see
`methods/customer-interviews/research-and-insight.md`.)*

### 10. Opportunity = important but poorly satisfied
The ODI opportunity algorithm —
`Importance + max(Importance − Satisfaction, 0)` — encodes two judgments:
unmet *important* needs matter twice as much as satisfaction shortfalls, and
over-serving earns no credit. The landscape it produces separates underserved
needs (innovate), overserved needs (disrupt with simpler/cheaper), and
appropriately served needs (maintain, don't invest). *(Ulwick.)*

### 11. Segment by unmet needs; describe with demographics
Two people with identical demographics can have opposite unmet needs.
Segments are formed from outcome data (factor + cluster analysis on
importance/satisfaction gaps) and only *then* profiled with demographics so
you can find them in the wild. Demographics never define a segment.
*(Ulwick.)*

### 12. Gates between stages; gaps go upstream
Each pipeline stage gates its input (saturation reached; statements
structurally valid; survey < 25 min; N ≥ 180; silhouette > 0.25). When a gate
fails, the work goes *back* with a specific request — a coverage gap triggers
follow-up interviews, not a thinner survey. Quality problems are fixed where
they were created, never papered over downstream.

### 13. Research is cumulative, shared, and a team sport
Findings compound across studies and calls — track what's known, what's
inferred, and what's still open, and never re-ask what's answered. Spend real
time *showing* research; it exists to build the team's shared empathy and
memory, not to fill a document. Every edit to the record is logged so it can
be audited. *(Tebb #5–#8.)*

### 14. State beliefs as testable experiments
The output of any research round is the next test, framed explicitly:
**"We believe that… / To verify that… / Built… / Measured… / Found out
that…"** — with a qualitative "wow" check alongside the metric. It's OK to be
wrong; it's not OK to be unfalsifiable. *(Wilkie; Ries's build–measure–learn.)*

### 15. Work backwards from the customer experience
Before building, write the press release announcing the finished product —
in customer language — plus the FAQ that answers the questions you'd rather
avoid. Narrative prose forces complete thinking that bullet points hide, and
iterating a one-pager costs hours where iterating a product costs quarters.
The document is a truth-seeking filter, not a pitch: **most PR/FAQs should
die, and killing one cheaply is a success.** *(Bryar & Carr; Amazon.)*

### 16. Distrust delightful data
Twyman's law: any figure that looks interesting or different is usually
wrong. Pre-register the hypothesis, metric, and decision boundary before
seeing data; run the trust checks (sample ratio mismatch, A/A health,
peeking, segment-fishing) **before** interpreting effects; replicate
surprises before celebrating them. An experiment earns authority by
surviving attempts to break it. *(Kohavi, Tang & Xu; Twyman.)*

### 17. A metric must change behavior — and every target needs a counter
The test for any number: *what would you do differently based on it?* No
answer → it's decoration. A North Star expresses customer **value
exchange** (revenue is the lagging result, not the star); work happens on
its input metrics; cohorts over averages, always. And Goodhart's law is a
schedule, not a risk: every metric under pressure gets gamed, so every
target ships with the counter-metric that catches it. *(Croll & Yoskovitz;
Cutler/Amplitude; Goodhart.)*

---

## System design principles

How the repo itself is built, and why.

### Agents = behavior; `methods/` = knowledge
An agent file (`.claude/agents/<name>.md`) holds *how to act*: role, mode
detection, non-negotiables, gates, handoffs. A method doc
(`methods/<topic>/*.md`) holds *what is true*: protocols, grammars,
templates, checklists. Every agent's first instruction is to read its method
docs. You can sharpen an agent by improving its knowledge without touching
its behavior — and vice versa.

### Single source of truth for shared knowledge
Knowledge used by several agents lives in exactly one file. The outcome-
statement grammar is used by all four ODI agents and is defined only in
`methods/odi/outcome-statements.md`. (Its predecessor repo embedded that
grammar in four separate agent prompts; a rule change meant four edits and
eventual drift. The port collapsed those into one canonical reference —
and in doing so surfaced and fixed two real inconsistencies: an ambiguous
score-conversion formula and two conflicting step numberings.)

### Agents hand off through explicit gates
The system is a pipeline, not a pile: each agent names its upstream and
downstream agent, what it requires, and what it refuses (the survey builder
rejects uncurated statements by design). Feedback loops are first-class —
the editor can send work *back* to the interviewer. Cross-references live in
the agents' `description` fields too, so auto-delegation routes correctly.

### Humans stay in the loop where reality is
Agents prep, structure, extract, analyze, and coach. **You** conduct the
interviews and field the surveys. No agent pretends to do the part that
requires being in the room — and each one's description says so.

### Descriptions are the router
Claude auto-delegates to subagents by matching their `description` fields.
Each description therefore carries its trigger vocabulary, its scope, *and*
pointers to neighboring agents ("for open-ended early discovery use
customer-interviews instead") so near-miss requests land in the right place.

### Attribution is part of the method
Every method doc cites its sources inline and in
[`../CREDITS.md`](../CREDITS.md); third-party raw materials live under
`methods/<topic>/materials/` and remain their authors' property. Distilled
≠ owned: the repo records whose shoulders it stands on, precisely.

### Artifacts are files
Agents save their outputs (guides, statement sets, surveys, analyses, plots,
scripts) as files in your working folder rather than only printing them —
so work products persist, diff, and feed the next stage.

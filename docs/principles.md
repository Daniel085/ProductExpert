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

### 18. "Requirements" are hypotheses in disguise
Customers' "requirements" are guesses at what might solve some — often
unstated — problem; stakeholders' "requirements" are personal theories.
Neither is a mandate. Reclassify every incoming ask: **true constraint**
(verify it, then honor the *what* while keeping design freedom in the
*how*), **stakeholder theory** (trace to the business problem), or
**customer solution-guess** (trace to the customer problem). Form and
function iterate together, so a spec frozen before any solution exploration
is fiction; and when the asked-for path is infeasible, substitute — it's
the result that matters, not the preconception. The only real requirement
is to discover solutions that work for users, customers, and the business.
*(Cagan/SVPG; the organizational sibling of principle 1.)*

### 19. Diverge before you converge
The first idea is rarely the best and always the anchor. Before evaluating
anything, generate at least five distinct options — varied across scope,
approach, and timing, including one that inverts the premise and one that
removes something instead of adding. Feasibility judgments wait for
convergence; constraints re-enter only after the option set is real. A
"brainstorm" that evaluates its first idea is a decision wearing a
costume. *(Anthropic's product-brainstorming skill; divergent-thinking
practice broadly.)*

### 20. Pick problems on customer signal × business alignment — triangulated
A problem earns roadmap time on two criteria: how painful it is and for
how many (**Customer Signal**), and how directly solving it moves the
*stated* goal (**Business Alignment**). Read the criteria through the
goal — when the goal is acquisition, breadth moves to the business side;
for internal tools, the customer is the employee and alignment is time
saved and errors avoided for others. Then make the case on paper: the
problem as a job story, an evidence table with **confidence scored per
source**, and a pattern check — because when qualitative, quantitative,
and operational sources point at the same problem it is far less likely
to be bias or opinion. One source type, however vivid, is *Not yet*; a
conflict gets explained, never averaged. *(The "pick the right problem"
framework; the evidence-tier discipline of principle 8.)*

### 21. Let themes emerge before you name them
Faced with many observations, tickets or ideas, group them by affinity
**silently and without pre-set categories**, name each group only after
its shape is visible, keep the loners, and count **distinct sources** —
not notes — per theme. Categories decided in advance only ever find
themselves. And a theme is a bucket, not a conclusion: it still has to be
written as a problem and explained as an insight before anyone acts on
it. *(Kawakita's K-J method, via ASQ.)*

### 22. Prove the solution before you build it — with things that don't scale
A validated problem does not validate your answer to it: teams hear what
users ask for, build exactly that, and learn it wasn't what they wanted.
So before engineering time, run the cheapest experiment that could say
no — and know which kind you are running. A **concierge** test (deliver
the value by hand, visibly) is *generative*: it discovers what the
solution should be, and the human in the room inflates every result, so
it can never validate one. A **Wizard of Oz** (simulate the product,
humans behind the curtain), a **concept test** or a **smoke test** is
*evaluative*: it falsifies a defined solution hypothesis. Fake the
back-end freely — Airbnb's photographers, Gusto's staff phoning carriers
— but only with a written vision of how it automates and a rule that
growth continues only while unit economics improve. Every card states
*what we're trying to prove*, the *expected* result and *what would
disprove it* before the run. *(Kromer; Graham; London/Gusto; Bank of
America "Keep the Change".)*

### 23. Slice by what you're trying to prove — and know which minimum you mean
The first version is a risk-management device, not a small product. Pick
the slice by the single thing that most needs to be true right now, not
by what's easy to build. **MVP** (new product, new market) tests the
segment and its needs; a **minimum lovable product** tests that a tiny,
superb version earns love in one narrow segment — end-to-end, intuitive,
delightful, measured by referrals and retention, expanding one step at a
time only after love shows up; a **minimum viable investment** (existing
product, existing customers) instruments first and makes small,
outside-in steps — never a "minimum viable rewrite" that spends two
years in staging with no market feedback. *(Matts; London/Gusto; Ries.)*

### 24. Measure the current condition before you experiment, then iterate in katas
Direction → current condition → next target condition → biggest obstacle
→ one small step with a written expectation → learned → re-measure →
repeat. The step most teams skip is the second: Perri's seller-portal
kata spent its first three cycles just counting calls (the guess was
four a week; the truth was seven) before changing anything, and learned
in three weeks what a shipped portal took four months to reveal. Steps
take a week or less, name their measure, and are rarely features.
Unknowns are obstacles; "we don't know" is a legitimate current
condition and the first thing to fix. *(Rother's Toyota Kata; Perri's
Product Kata.)*

### 25. The value proposition is the promise — and a hypothesis
Write it from the jobs, pains and gains you have evidence for — customer
side of the canvas first, value side designed to it — and compress it to
one sentence: *we [deliver outcome] by [solving the key job]*, usually
one functional payoff and one emotional one. It names a change in
someone's life, not a feature or an adjective. Until a concept test,
Wizard of Oz or lovable slice has tested it, it is a belief in the
ledger, not a fact in the press release. *(Strategyzer's Value
Proposition Canvas; Product Institute.)*

### 26. Score what you don't know before you explore solutions
A validated problem is not the same as a well-understood one. Before
generating options, score confidence 1–5, with the artifact that backs
each score, in five areas: **problem definition**, **user behavior**
(how they cope today), **competitive landscape**, **technical
constraints**, and **business impact**. The lowest score chooses the
next move — interviews when the customer's side is unclear, root-cause
analysis when the symptom has no *why*, a competitive teardown when the
market is a blank — and no area below 3 is the gate into solution
exploration. Options generated past a 2 inherit the gap. Desk research
alone never scores above 3; two people who would score differently
score at the lower value. *(Product Institute; the evidence tiers of
principle 8.)*

### 27. Don't build the request — find its riskiest assumption
A feature request is an answer with the question missing. Recover the
observation that prompted it, verbatim and tiered; answer the eight
questions — what problem it solves for us, for whom, how big, what
alternatives exist, what constrains us, how it reaches the market, which
KPI it moves, what is critical to success — with every guess marked as
one; then write the chain of claims that must all hold between the
observation and the feature. Test exactly one link, the most
load-bearing and least evidenced, with the cheapest experiment that
could break it. And read a null result carefully: before "no demand,"
check that the test reached the intended users through the channel they
actually use, and re-run there if it didn't. What a confirmed link
implies usually reaches beyond the request that started it. *(The eight
questions; Cagan; the ledger's impact × uncertainty rule.)*

### 28. An MVP is the fastest path to insight, not a small v1
Ries's definition is about learning per unit of effort, not about
shipping less. MVPs fail two ways: the team thinks it is building
version one, so nothing is being learned; or the slice is executed
badly, so the negative signal measures the execution rather than the
idea. Scope backwards from the learning goal — the problem, the market
assumptions, the quickest low-risk way to test them, and whether you are
optimizing for adoption, retention, conversion or satisfaction — and
read the result on that one measure. Be clear about the learning goal;
use experiments, not features; use what you learn and move on; keep
customers in the loop early and often. *(Robinson; Ries; Blank; the
MVP-versus-MVI context rule of principle 23.)*

### 29. Don't run the Product Death Cycle — in either version
David Bland's original: *no one uses our product → ask customers what
features are missing → build them → repeat.* The AI-era version: *no one
uses our AI product → ask AI what features are missing → build the
missing AI features → repeat.* The second is more dangerous because it
feels data-driven while skipping the same work — validating a real user
problem — and because the technology makes shipping unwanted software
cheaper. The way out is not better features and not a better model; it
is customer discovery: talk to users, understand the problem, *then*
decide whether anything (and whether AI) solves it. A missing-feature
list, from a customer or a model, is a pile of solution guesses; trace
each to a problem or set it aside. *(Bland; Perri, "Escaping the Build
Trap" and its AI-era update.)*

### 30. Customers can't hand you the solution — so test it, don't ask
The "faster horse" line is apocryphal (Vlaskovits, HBR 2011; Snopes
2025), but the half-truth in it is real: customers describe their
problem in the vocabulary of today's solutions, so discovery finds the
*job* and rarely hands you the design. The other half is Ford's own
lesson — ignoring customers later cost him the market. Resolve it the
way the problem was resolved: by behaviour. Put the solution, or a
faithful fake of it, in front of the job executor and watch — a
concierge to find the shape, a concept test or smoke test for the
promise, a clickable prototype at the lowest fidelity that answers the
flow question, a Wizard of Oz or functional prototype for the mechanism,
API access when the capability may be the value, and an A/B test last.
Let the kata's current obstacle choose; "would you use this?" is the
faster-horse question in reverse. *(Vlaskovits; NN/g on fidelity;
Rother/Perri's kata.)*

### 31. An option is a tested solution; v1.0 is not the MVP
Write a solution up as an **option** only once an experiment has read
out on it: one hypothesis — *we believe building X will satisfy the job
for the segment and result in the KPI* — a behavior change you could
observe without a dashboard, scope in and out with reasons, risks each
carrying a test, one to three baselined metrics, and an iteration plan
that learns each chunk. Then cut it to the **minimum feature set**: not
the MVP (which learned) but version one (which delivers the job
end-to-end, at lovable quality, to a segment that includes people who
won't forgive). Job-critical, adoption-critical and sustainability
features are in by evidence; everything else earns its place by **cost
of delay divided by duration**. Cost of delay is a *rate* with two
ingredients that multiply — value (increase revenue · protect revenue ·
reduce costs · avoid costs) and urgency (how the value decays with
time) — scored independently, qualitatively first if need be (Killer /
Bonus / Meh × ASAP / Soon / Whenever). A date does not make a feature
urgent: its cost of delay is zero until the latest start date. What is
deferred is recorded with what the delay costs, so the roadmap argument
starts from numbers — and, per Perri, from a strategy; arbitrary scores
averaged across stakeholders are consensus, not prioritization, and a
formula over gut inputs (RICE) is the same thing with a veneer. Kano is
the second lens: basics reach neutral at best and must be audited,
performance features are what cost of delay ranks, and cheap
excitement generators belong in v1.0 — knowing they migrate into basics
as they spread. *(Reinertsen; Arnold's benefit buckets, urgency profiles
and CD3; Perri; Kano via Spool; the option template.)*

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

### Agent output is never customer evidence
A system of AI product agents is one shortcut away from the AI-era
Product Death Cycle (principle 29): ask the agent what customers want,
build it, repeat. The guard is structural. Everything an agent generates
— a landscape scan, a synthesized segment, a list of likely pains, a
suggested experiment — enters the ledger as **BACKGROUND at most**;
INFERRED needs a real person's words and CONFIRMED needs them verbatim
and attributed. No agent may declare a problem validated from desk
research, mark a *Yes* on a single evidence type, or fill an evidence
table with its own answers. The agents make the discovery work sharper
and faster; they do not stand in for it.

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

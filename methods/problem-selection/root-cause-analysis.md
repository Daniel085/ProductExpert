# Root-Cause Analysis — Method Reference

*The "problem analysis" move of the knowledge-gap assessment
([`knowledge-gaps.md`](./knowledge-gaps.md)): when the team can describe
a symptom but not explain it. Three standard tools — **5 Whys** (Sakichi
Toyoda / Taiichi Ohno, Toyota Production System), the **cause-and-effect
diagram** (Kaoru Ishikawa, 1960s; "fishbone"), and the
**interrelationship digraph** (one of the Japanese "seven management and
planning tools", as catalogued in ASQ's *Quality Toolbox*) — adapted to
product problems. This is a first-cut distillation from the public canon
of these tools, with no source document preserved; the product-specific
adaptations and the gate are this repo's. See
[`../../CREDITS.md`](../../CREDITS.md).*

> **Where this sits.** Affinity mapping
> ([`affinity-mapping.md`](./affinity-mapping.md)) tells you *what* the
> themes are; ASQ's own next step after a map is a cause-and-effect or
> interrelationship diagram to reach root causes. The insight ladder
> (observation → finding → insight) demands a *why*. These tools are
> how you get one when it doesn't come on its own.

## 1. When to use which

| You have… | Use | Output |
|-----------|-----|--------|
| One clear symptom and a linear-looking chain | **5 Whys** | A causal chain ending at something you can act on |
| A symptom with many possible contributing causes, no obvious chain | **Cause-and-effect (fishbone)** | Causes sorted into categories, with the few to test marked |
| Many themes or causes that seem to influence each other | **Interrelationship digraph** | Which causes are *drivers* (many arrows out) and which are *outcomes* (many arrows in) |

All three are hypothesis generators. A root cause is **confirmed** only
when evidence (an observation, a data cut, a test) supports it — until
then it goes in the ledger as INFERRED.

## 2. 5 Whys

Start from the symptom stated as a **job story or a measured gap**
("31% of imports abandoned at the mapping step"), and ask *why* until
the answer is something the team can change, or something outside its
control it must design around.

Rules that keep it honest:

- **Each "why" must be backed by evidence or marked as a guess.** A
  chain of five guesses is a story, not an analysis.
- **Stop at the actionable cause, not at "human error" or "the user
  didn't understand."** Those are where the next why starts.
- **Branch when a why has two answers.** It usually does; the chain is
  a tree. Follow the branch with the most evidence first.
- **Five is a heuristic**, not a rule — stop when the cause is
  actionable and evidenced; keep going if it isn't.
- **Beware the reflexive why that lands on a feature** ("because there's
  no bulk edit"). A missing feature is a solution guess wearing a cause's
  clothes; ask what the user was trying to do.

```
Symptom: <job story / measured gap>                      evidence: <artifact · tier>
Why 1: …                                                 evidence / guess
Why 2: …                                                 evidence / guess
   branch 2b: …
Why 3: …
Root cause (actionable): …
What would confirm it: <observation / data cut / test>
```

## 3. Cause-and-effect (fishbone) diagram

Put the **effect** (the symptom) at the head; draw the major cause
categories as bones; brainstorm specific causes onto each bone; then
mark the few worth testing. Ishikawa's manufacturing categories (the
6 Ms) translate poorly to product work, so use categories fitted to it:

| Category | Ask |
|----------|-----|
| **People / segment** | Who hits this — which segment, role, level of experience? |
| **Task / job context** | What was the user trying to do, under what constraints, at what moment? |
| **Product / experience** | Which step, screen, message, default, or missing capability? |
| **Data / integration** | Inputs, imports, third-party systems, data quality |
| **Process / policy** | Onboarding, support, pricing rules, permissions, compliance |
| **Environment / market** | Device, network, locale, regulation, competitor behavior |

Then: **circle the causes that (a) have evidence and (b) the team could
influence**; those become the *why* hypotheses to confirm. Everything
else stays on the diagram as considered-and-set-aside.

Run it as a group in the affinity-mapping spirit — silent generation
first, then discussion — so the loudest voice doesn't pick the bone.

## 4. Interrelationship digraph

For a set of themes or causes (typically the headers of an affinity
map, 5–15 items) that seem to feed one another:

1. Lay the items out in a rough circle.
2. For each pair, ask: *does A cause or strongly influence B?* If yes,
   draw an arrow A → B. One direction only per pair — pick the stronger.
3. Count arrows **out** and **in** for each item.
4. **Drivers** (most arrows out) are root causes — address these.
   **Outcomes** (most arrows in) are symptoms — measure these; they'll
   move when the drivers do.

```
Item                     out   in   role
Import fails part-way     4     1   DRIVER
Support tickets high      0     5   outcome
Re-entry of data          1     3   outcome
Mapping step unclear      3     1   DRIVER
```

The digraph is a judgment exercise; write down the evidence behind any
arrow the team disagreed about.

## 5. Gate and handoff

- **Confirmed root cause** → back to the problem case: rewrite the job
  story if the cause moved the problem; add the *why* to the insight;
  re-score area 1 in the knowledge-gap scorecard.
- **Root cause is a user behavior you haven't observed** → the
  knowledge gap is *user behavior*; route to **customer-interviews**.
- **Root cause is a data question** ("is it really the mapping step?")
  → a data cut; **metrics** if the measure doesn't exist.
- **Root cause is outside the team's control** (regulation, a partner's
  API) → it is a true constraint; classify it per
  [`../jtbd/requirements-are-hypotheses.md`](../jtbd/requirements-are-hypotheses.md)
  and design around it.
- **Nothing actionable emerges** → the problem statement is probably
  too coarse; split it (affinity-map the evidence again at finer grain).

## 6. Anti-patterns

| Anti-pattern | Tell | Fix |
|--------------|------|-----|
| **Chain of guesses** | Five whys, zero citations | Evidence or "guess" on every line; test the guesses |
| **Stopping at the person** | "Because the user made a mistake" | The mistake is the next symptom; ask why it was easy to make |
| **Feature as root cause** | "Because we don't have X" | Restate as what the user was trying to do |
| **Single chain** | Never branches | Branch on every why with two plausible answers |
| **Fishbone as brainstorm dump** | Forty causes, none marked | Circle the evidenced, influenceable few |
| **Analysis as delivery** | The diagram is the deliverable | The deliverable is a confirmed cause and a rewritten problem case |

## Sources & materials

- **5 Whys** — Toyota Production System; attributed to **Sakichi
  Toyoda** and described by **Taiichi Ohno** (*Toyota Production System:
  Beyond Large-Scale Production*, 1988).
- **Cause-and-effect diagram** — **Kaoru Ishikawa** (*Guide to Quality
  Control*, 1968; the "fishbone" / Ishikawa diagram).
- **Interrelationship digraph** — one of the seven management and
  planning tools (Japanese Union of Scientists and Engineers, 1970s),
  as catalogued in **ASQ**'s *The Quality Toolbox* (Nancy R. Tague), the
  same reference the affinity-diagram page names as the next step.
- No source document is preserved for these; this doc is a first-cut
  distillation from the public canon. The product-specific fishbone
  categories, the evidence-per-why rule, the gate and the anti-patterns
  are this repo's operational extension. Add source materials under
  [`./materials/`](./materials/) as they arrive.
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

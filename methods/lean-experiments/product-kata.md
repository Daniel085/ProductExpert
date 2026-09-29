# The Product Kata — Method Reference

*Distilled from **Melissa Perri**'s "The Product Kata" (2015), her
adaptation of **Mike Rother**'s **Toyota Kata** (via **Håkan Forss**'s
Kanban Kata) to product work; the PM's seven-step summary of it is in the
notes this doc was built from. Source page preserved in
[`./materials/`](./materials/); Rother's own Improvement Kata and
Coaching Kata pages, with the five-question card, are preserved under
[`../strategy/materials/`](../strategy/materials/). The record template
and the integration rules are this repo's operational extension. See
[`../../CREDITS.md`](../../CREDITS.md).*

> **Two docs, one kata.** This doc is the kata's **mechanics** — the
> steps, the rules of the form, the record, the coaching questions, the
> anti-patterns — as run inside one initiative. Where the *direction*
> comes from, how the same loop runs at every level of the organization
> (vision → strategic intents → product initiatives → options), and how
> strategy is deployed and communicated is
> [`../strategy/product-strategy.md`](../strategy/product-strategy.md).

> **What it is for.** The experiments in
> [`pre-build-experiments.md`](./pre-build-experiments.md) are single
> tests. The kata is the **rhythm** that strings them together toward a
> product initiative: measure where you are, name the next obstacle, run
> one small step, learn, re-measure, repeat. It is a *training form* —
> repeated until it is second nature — not a document. Its signature
> discipline is the one most teams skip: **establish the current
> condition before you experiment.**

## 1. Toyota Kata in one paragraph

A continuous-improvement habit built on learning: management sets a
**challenge** (a lofty direction), the team **grasps the current
condition**, sets the **next target condition** (a step toward the
challenge, not the challenge itself), and **iterates** toward it through
small, fast experiments against whatever obstacle is in the way. A
**coaching kata** keeps it honest — at every check-in the coach asks the
same five questions:

1. What is the target condition?
2. What is the actual condition now?
   *— turn the card over —*
3. What obstacles do you think are preventing you from reaching the
   target condition — and which **one** are you addressing now?
4. What is your next step (next experiment)? What do you expect?
5. How quickly can we go and see what we have learned from that step?

Between questions 2 and 3 the coach turns the card over and the learner
**reflects on the last step taken** — because, as the card says, you
don't actually know what the result of a step will be:

1. What did you plan as your last step?
2. What did you expect?
3. What actually happened?
4. What did you learn?

…then back to question 3, stating the obstacle being worked on. A
coaching cycle is the five questions asked of the learner at their
storyboard, once a day at a scheduled time, twenty minutes or less;
the coach adds clarifying questions after each heading, and when the
learner hits the edge of what they actually know — at any question —
goes straight to question 4, because the next step is to find out.
Rother's storyboard has six fields — *focus process · challenge ·
target condition (achieve by) · current condition · experimenting
record · obstacles parking lot* — which the record in §4 mirrors.
Practise the card exactly as written until the pattern is a habit;
adapt it after, core intact. (Source pages and the card:
[`../strategy/materials/`](../strategy/materials/).)

## 2. The Product Kata (the seven steps)

Rother's four steps, Perri's four, and the PM's four-step strategy
summary line up one-to-one — the table is in
[`../strategy/product-strategy.md` §4](../strategy/product-strategy.md).
The seven steps below are the operational expansion of those four for
a single initiative: steps 1–2 are *understand the direction* and
*analyze the current state*; the target condition is *set the next
goal*; steps 3–7 are *execute* — obstacle, small step, prediction,
run, re-measure.

Perri's product adaptation, as the PM's notes summarize it:

1. **Understand the direction** — usually the product initiative or the
   challenge management set. Lofty by design; you may never reach it
   exactly, but you get as close as you can.
2. **Identify the current state** relative to that initiative — with a
   number, not a feeling.
3. **Determine the biggest obstacle** preventing you from reaching the
   next target condition. Unknowns ("we don't know why they call") are
   obstacles too — usually the first ones.
4. **Design a small experiment** to learn about and tackle that
   obstacle. Steps should take a week or less; break longer ones down.
5. **Document your hypothesis and expected outcome** before running it.
6. **Run the experiment. Review findings.** Did what you learned affect
   the goal?
7. **Re-measure the current state and repeat** — target condition met?
   If not, the next obstacle.

Between 1 and 3 sits the Toyota step Perri keeps but the summary folds
in: set a **target condition** — a measurable intermediate state ("sellers
call fewer than twice a week") that the experiments aim at, distinct from
the far-off direction ("sellers fully self-sufficient").

## 3. Rules of the form

- **No experimenting without a baseline.** Perri's first three cycles
  produced no product change at all — they measured how often sellers
  called (the guess was 4/week; reality was 7). "This is a step most
  people miss."
- **Every step names its measure.** A step with no measurement cannot
  tell you whether you are improving.
- **Expected before learned.** Write the expected result down first, so
  a surprise is recognizable as one. The daily-revenue email was
  *expected* to end revenue calls entirely; it didn't, and the gap ("they
  want it daily, when a launch is on") was the learning.
- **Short cycles.** A week where possible. The seller-portal team learned
  in three weeks by kata what had taken four months by shipping (monthly
  revenue instead of daily — "every seller was pissed off").
- **Steps are rarely features.** Counting calls, sending a manual email,
  a phone script — the cheapest thing that moves the number or answers
  the unknown.
- **Obstacles, not solutions, drive the next step.** The failed portal
  jumped from direction to "build software that does everything"; the
  kata inserts the unknowns in between.
- **Break it down to assumptions, not a generic learning loop** (Perri's
  reply to a commenter): the structure forces you to restructure what
  you learn each cycle instead of collecting information in bulk.

## 4. The kata record (template)

One record per initiative, appended each cycle. The step block reuses the
experiment card's fields
([`pre-build-experiments.md` §6](./pre-build-experiments.md)) so a kata
step and a stand-alone experiment read the same way.

```
KATA — <initiative>
Direction / Challenge: <the lofty goal, in one line, with its owner>
  Ladder: vision → strategic intent SI-<n> → product initiative PI-<n> → this work
          (the direction ladder, ../strategy/product-strategy.md §7; "not stated" is
           a legitimate value — and the first obstacle)
Goal metric (from the metrics tree, if one exists): <name + definition>

Target Condition #<n>: <measurable intermediate state>   set: <date>   achieve by: <date>
Current Condition:     <the number now, how measured, as of <date>>
                       ("unknown" is a legitimate value — and the first obstacle)
Obstacles parking lot: <every obstacle seen so far; the one being worked is marked>

── Cycle <k> ─────────────────────────────── <date>
Reflect on the last step (the back of the card — skip in cycle 1):
  Planned:       <what the last step was>
  Expected:      <what we predicted>
  Actually:      <what happened>
  Learned:       <what we now know that we didn't>
Obstacle:        <the one thing in the way now — unknown or friction>
Step:            <the small experiment; who; ≤ 1 week>
Expected:        <the number/observation we predict>
Measured by:     <the measure this step reports>
Learned:         <what actually happened, and the why if you got one>
Current now:     <re-measured condition>
Target met?      yes → set next target condition / no → next obstacle
Ledger:          <assumption rows updated>
```

The header is Rother's storyboard (challenge · target condition with
its achieve-by · current condition · obstacles parking lot); the cycles
are its experimenting record; the reflection block is the back of the
five-question card. *Learned* in cycle *k* and *Reflect → Actually /
Learned* in cycle *k+1* are the same fact written twice on purpose —
the second time is the coaching moment, read out loud against
*Expected* before the next obstacle is named.

### Perri's worked example, in the record

```
Direction: Make sellers completely self-sufficient in managing their stores
  (a quarter of staff spend 15+ h/week on seller calls)
Target Condition #1: sellers call fewer than 2×/week
Current Condition: "more than 2×" — exact rate unknown

Cycle 1  Obstacle: we don't know how often they call
         Step: staff count calls for one week    Expected: ~4/week
         Learned: 7/week                         Current: 7   Target met? no
Cycles 2–3  (still measurement: who calls, about what) — no product change
Cycle 4  Obstacle: calls about revenue
         Step: staff send a weekly revenue email; count revenue calls over 2 weeks
         Expected: revenue calls stop entirely
         Learned: sellers want revenue DAILY, during launch weeks, to pick
                  what to promote on social       Current: 5/week   met? no
Cycle 5  Step: daily revenue email               Current: 3/week   met? no
…        continued until 1×/week — freeing hours of staff time — none of
         the steps were new software
```

## 5. Where it plugs in

- **Direction** comes from the level above — the product initiative
  under a strategic intent, written as the direction ladder
  ([`../strategy/product-strategy.md` §7](../strategy/product-strategy.md));
  in practice a `prfaq` vision, a `problem-selection` *Yes* under a
  stated intent, or a challenge from leadership. If the direction has
  no measurable goal, the **metrics** agent defines one before the
  first cycle; if the level above hasn't stated it at all, getting it
  written — not inventing it — is the first obstacle.
- **Current condition** is a measurement task — often the first several
  cycles. For an existing product this is exactly Matts's MVI rule:
  *instrument first*
  ([`pre-build-experiments.md` §5](./pre-build-experiments.md)).
- **Obstacles** that are unknowns about customers route to
  **customer-interviews** (why do they call?) or a concierge step;
  obstacles that are solution doubts get a Wizard-of-Oz or concept-test
  step from the catalogue.
- **Steps that need statistical rigor** (a live product, enough traffic,
  a causal claim) become pre-registered tests with **experimentation**.
- **Learned** updates the assumption ledger
  ([`../customer-interviews/assumption-ledger.md`](../customer-interviews/assumption-ledger.md))
  every cycle; the record is the initiative's audit trail.
- **Target met** repeatedly → the initiative's evidence flows back into
  the PR/FAQ verdict or the roadmap decision that spawned it.

## 6. Anti-patterns (coach's tells)

| Anti-pattern | Tell | Fix |
|--------------|------|-----|
| **Experimenting before measuring** | "Let's try X and see" with no baseline | Cycle 1 is a measurement; "unknown" is the obstacle |
| **Direction as target** | Target condition = "sellers self-sufficient" | Set an intermediate, measurable target |
| **A step that is a project** | Next step takes a quarter | Break it down to ≤ 1 week |
| **No expected value** | "We'll see what happens" | Write the prediction first |
| **Feature reflex** | Every step is "build…" | Cheapest step that moves the number: a count, an email, a script |
| **Learned without why** | "It went from 7 to 5" | Add the reason; if unknown, that's the next obstacle |
| **Skipping re-measure** | Cycle ends at "shipped" | Cycle ends at "current condition now = …" |
| **Kata theatre** | The five questions are asked; nobody turns the card over | Reflect on the last step — planned · expected · actually · learned — before naming the next obstacle |
| **Inventing the direction** | The team writes its own "strategic intent" because none was stated | The first obstacle is getting the level above to state it ([`../strategy/product-strategy.md`](../strategy/product-strategy.md)) |

## Sources & materials

- **Melissa Perri**, *"The Product Kata"*, melissaperri.com, 22 Jul
  2015 — including the seller-portal example and her replies in the
  comments. Source: `./materials/MelissaPerri-TheProductKata.pdf`;
  transcription: `./materials/extracted/melissaperri-the-product-kata.txt`.
  Perri later folded the Product Kata into *Escaping the Build Trap*
  (O'Reilly, 2018).
- **Mike Rother**, *Toyota Kata* (McGraw-Hill, 2009) — the improvement
  kata and the coaching kata's five questions; overview at
  https://en.wikipedia.org/wiki/Toyota_Kata. His *Improvement Kata* and
  *Coaching Kata* web pages and the *5Q Card* deck (the four-step
  model, the card's front and back, the coaching-cycle rules, the
  storyboard) are preserved at
  `../strategy/materials/ToyotaKata-Rother-*.pdf` with transcriptions
  under `../strategy/materials/extracted/`.
- **Håkan Forss** — the Kanban Kata, Perri's bridge from Rother to
  product work.
- The seven-step summary (§2) is the PM's, as is the four-step strategy
  summary it expands
  ([`../strategy/product-strategy.md`](../strategy/product-strategy.md));
  the record template (§4), the integration rules (§5) and the
  anti-patterns (§6) are this repo's operational extension.
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

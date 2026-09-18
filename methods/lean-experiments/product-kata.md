# The Product Kata — Method Reference

*Distilled from **Melissa Perri**'s "The Product Kata" (2015), her
adaptation of **Mike Rother**'s **Toyota Kata** (via **Håkan Forss**'s
Kanban Kata) to product work; the PM's seven-step summary of it is in the
notes this doc was built from. Source page preserved in
[`./materials/`](./materials/); the record template and the integration
rules are this repo's operational extension. See
[`../../CREDITS.md`](../../CREDITS.md).*

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
3. What obstacles are preventing you from reaching it — and which one
   are you addressing now?
4. What is your next step, and what do you expect?
5. How quickly can we see what we learned from that step?

## 2. The Product Kata (the seven steps)

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
Goal metric (from the metrics tree, if one exists): <name + definition>

Target Condition #<n>: <measurable intermediate state>   set: <date>
Current Condition:     <the number now, how measured, as of <date>>
                       ("unknown" is a legitimate value — and the first obstacle)

── Cycle <k> ─────────────────────────────── <date>
Obstacle:        <the one thing in the way now — unknown or friction>
Step:            <the small experiment; who; ≤ 1 week>
Expected:        <the number/observation we predict>
Measured by:     <the measure this step reports>
Learned:         <what actually happened, and the why if you got one>
Current now:     <re-measured condition>
Target met?      yes → set next target condition / no → next obstacle
Ledger:          <assumption rows updated>
```

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

- **Direction** comes from the product initiative — a `prfaq` vision,
  a `problem-selection` *Yes*, or a challenge from leadership. If the
  direction has no measurable goal, the **metrics** agent defines one
  before the first cycle.
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

## Sources & materials

- **Melissa Perri**, *"The Product Kata"*, melissaperri.com, 22 Jul
  2015 — including the seller-portal example and her replies in the
  comments. Source: `./materials/MelissaPerri-TheProductKata.pdf`;
  transcription: `./materials/extracted/melissaperri-the-product-kata.txt`.
  Perri later folded the Product Kata into *Escaping the Build Trap*
  (O'Reilly, 2018).
- **Mike Rother**, *Toyota Kata* (McGraw-Hill, 2009) — the improvement
  kata and the coaching kata's five questions; overview at
  https://en.wikipedia.org/wiki/Toyota_Kata.
- **Håkan Forss** — the Kanban Kata, Perri's bridge from Rother to
  product work.
- The seven-step summary (§2) is the PM's; the record template (§4), the
  integration rules (§5) and the anti-patterns (§6) are this repo's
  operational extension.
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

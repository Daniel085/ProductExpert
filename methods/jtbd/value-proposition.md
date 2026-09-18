# Value Proposition — Method Reference

*Two sources, one artifact. The **Value Proposition Canvas** is
**Strategyzer AG**'s (Osterwalder, Pigneur, Bernarda & Smith, *Value
Proposition Design*) — the two-sided canvas and its trigger questions,
preserved verbatim in [`./materials/`](./materials/). The
functional-plus-emotional-jobs recipe for the one-sentence statement is
**Product Institute** course material (*Product Management Foundations*),
distilled here in paraphrase and **not quoted** — it is licensed
coursework. See [`../../CREDITS.md`](../../CREDITS.md).*

> **What a value proposition is for in ProductExpert:** it is the
> **promise** — the sentence that says what changes for the customer and
> which job that change comes from. It is the thing a concierge or
> Wizard-of-Oz test delivers by hand before anything is built
> ([`../lean-experiments/pre-build-experiments.md`](../lean-experiments/pre-build-experiments.md)),
> the "most important benefit" a PR/FAQ headline must state
> ([`../prfaq/working-backwards.md`](../prfaq/working-backwards.md)), and
> the claim a concept test puts in front of customers. A value proposition
> is a hypothesis until one of those tests says otherwise.

## 1. The one-sentence statement (Product Institute, paraphrased)

The recipe rests on the two kinds of job your product supports:

- **Functional jobs** — the tasks the customer is trying to get done.
- **Emotional jobs** — how the customer wants to feel, or what they want
  to stop feeling.

Three moves:

1. **List** the functional and emotional jobs your product helps with —
   take them from the job map, the outcome statements, the synthesis
   insights, or the canvas below; don't invent them at the keyboard.
2. **Pick the critical few** — the jobs that would actually make someone
   adopt the product. Not every job you touch; the one or two that drive
   the decision.
3. **Write it in the form:** *We [deliver outcome] by [solving the key
   job].* The outcome is what changes for the customer; the job is where
   that change comes from. A strong statement usually carries one
   functional payoff and one emotional payoff.

**Worked example (this repo's, not the course's).** For the import-failure
problem in
[`../problem-selection/picking-the-right-problem.md`](../problem-selection/picking-the-right-problem.md):

- Functional job: finish workspace setup the same day, even when an import
  breaks part-way.
- Emotional job: stop dreading that one bad file will cost the whole
  afternoon.
- Value proposition: *We get new teams from first import to a working
  workspace in one sitting by recovering a failed import exactly where it
  stopped, so nothing that already worked has to be re-entered.*

**The tells** (rewrite if you see one):

| Tell | Why it fails | Fix |
|------|--------------|-----|
| Names a feature instead of an outcome ("We provide a dashboard") | A dashboard is a product, not a change in someone's life | Say what is different for the customer afterwards |
| Adjectives instead of outcomes ("faster, easier, smarter") | Unfalsifiable; every competitor says it | Name the measurable outcome or the specific feeling |
| Only functional, no emotional (or the reverse) | Adoption is usually driven by both | Add the missing half or say why it is absent |
| Lists every job | A promise with six clauses is no promise | Keep the critical few from step 2 |
| Could be said by any product in the category | Not a proposition, a description | Anchor it in the pain or gain you relieve *better than the current solution* |

## 2. The Value Proposition Canvas (Strategyzer)

Two halves, six blocks. Fill the **customer side first** from evidence,
then design the **value side** to it — never the other way round.

```
   VALUE PROPOSITION (square)          CUSTOMER SEGMENT (circle)
   ┌──────────────────────┐            ╭──────────────────────╮
   │ Products & Services  │            │ Customer Job(s)      │
   │ Gain Creators        │ ── fit ──> │ Gains                │
   │ Pain Relievers       │            │ Pains                │
   └──────────────────────┘            ╰──────────────────────╯
```

### Customer side (profile)

- **Customer Job(s)** — what a specific segment is trying to get done:
  tasks, problems, needs. The canvas asks for **functional, social and
  emotional** jobs plus basic needs, the ancillary jobs the customer
  performs as *buyer*, *co-creator* and *transferrer*, and the **context**
  the job is done in (constraints matter). Rank each job crucial → trivial
  and note how often it occurs.
- **Pains** — negative emotions, undesired costs and situations, and risks
  *before, during and after* the job: what is too costly, what makes them
  feel bad, where current solutions under-perform, difficulties, feared
  social consequences, feared risks, what keeps them awake, common
  mistakes, barriers to adopting a solution. Rank by **intensity** and
  note frequency.
- **Gains** — benefits expected, desired, or that would surprise:
  savings, outcomes at or beyond expectation, what delights them in
  current solutions, what would make life easier, desired social
  consequences, what they look for and dream of, **how they measure
  success and failure**, what would make adoption more likely. Rank by
  **relevance** and note frequency.

### Value side (map)

- **Products & Services** — everything the proposition is built around
  (tangible, digital, intangible, financial), including what helps the
  buyer / co-creator / transferrer roles. Ranked by importance *to the
  customer*.
- **Pain Relievers** — how those products and services eliminate or
  reduce specific pains. Ranked by the intensity of the pain killed.
- **Gain Creators** — how they produce specific gains. Ranked by the
  relevance of the gain created.

### Fit

The canvas is done when the ranked pain relievers and gain creators
visibly address the **top-ranked** pains and gains of the **top-ranked**
jobs — and when you can say which pains and gains you deliberately do
*not* address. Relievers and creators with no matching customer-side item
are features looking for a reason; high-ranked pains with no reliever are
the gap the next iteration or the next experiment targets.

Strategyzer's three levels of fit, in this system's terms:

| Fit | Meaning | Where it is established here |
|-----|---------|------------------------------|
| **Problem–solution fit** (on paper) | Evidence the jobs, pains and gains matter, and a design that addresses them | customer-interviews synthesis, ODI opportunity scores, problem-selection *Yes* → canvas |
| **Product–market fit** | Customers respond to the proposition in the market | lean-experiments (concept test, concierge, Wizard of Oz, MLP), then experimentation |
| **Business-model fit** | The proposition can be delivered profitably | prfaq internal FAQs (economics), metrics, the unit-economics rule in lean-experiments |

### Working it in text

```
Segment: <who — a job executor, not a demographic>
JOBS (ranked)         | PAINS (ranked by intensity)   | GAINS (ranked by relevance)
1. <functional>  [f]  | 1. <pain>  [intense · daily]  | 1. <gain>  [substantial · weekly]
2. <emotional>   [e]  | 2. …                          | 2. …
3. <social>      [s]  | …                             | …
context: <where/when/under what constraints>

PRODUCTS & SERVICES   | PAIN RELIEVERS → pain #       | GAIN CREATORS → gain #
1. …                  | 1. … → P1                     | 1. … → G1
2. …                  | 2. … → P3                     | 2. … → G2
Unaddressed on purpose: P2 (why), G3 (why)
Evidence: <which artifact each customer-side item traces to; tier it>
Statement: We [deliver outcome] by [solving key job].
```

## 3. How the two connect — and how they plug in

- **Canvas → statement.** The statement is the canvas compressed: the
  top-ranked gain (or the top pain, inverted) is the *outcome*; the
  top-ranked job is the *key job*.
- **Job map / outcome statements → canvas.** ODI's job map is the
  *Customer Job(s)* block at high resolution; desired outcome statements
  ranked by opportunity score are *Gains* (and their inverses, *Pains*)
  already ranked by evidence — use them rather than re-brainstorming
  ([`../odi/outcome-statements.md`](../odi/outcome-statements.md)). The
  canvas's emotional and social jobs map to ODI's emotional and social
  job types.
- **Job story ↔ canvas.** A job story's situation is the canvas's
  *context*; its motivation is a *job*; its "so I can" is a *gain*
  ([`./job-stories.md`](./job-stories.md)).
- **Statement → experiment.** The statement is the belief a concept test
  or Wizard-of-Oz test falsifies; a concierge test *discovers* the canvas
  when the value side is still blank
  ([`../lean-experiments/pre-build-experiments.md`](../lean-experiments/pre-build-experiments.md)).
- **Statement → PR/FAQ.** Headline and summary paragraph are the
  statement in customer language; the canvas's pains are the problem
  paragraph's raw material.
- **Evidence discipline.** Every customer-side item carries a source and
  a tier (CONFIRMED / INFERRED / BACKGROUND,
  [`../customer-interviews/assumption-ledger.md`](../customer-interviews/assumption-ledger.md)).
  A canvas filled from the team's imagination is a hypothesis map, and
  should say so.

## Sources & materials

- **Strategyzer AG** — *The Value Proposition Canvas* (2-page PDF: canvas
  and trigger questions), strategyzer.com. Source PDF:
  `./materials/Strategyzer-TheValuePropositionCanvas.pdf`; transcription:
  `./materials/extracted/strategyzer-value-proposition-canvas.txt`. The
  canvas is from **Alexander Osterwalder, Yves Pigneur, Greg Bernarda &
  Alan Smith**, *Value Proposition Design* (Wiley, 2014). Further
  playbooks: https://www.strategyzer.com/playbook-library
- **Product Institute** — *Product Management Foundations*, the
  value-proposition lesson (functional + emotional jobs → "We [deliver
  outcome] by [solving key job]"). Course material: **paraphrased, not
  quoted**; the course's own example is not reproduced here.
- The tells table, the text template, and the fit-to-agents mapping are
  this repo's operational extension.
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

# Segmentation — Method Reference

*How to cut a customer population so the cuts reveal something: which
groups struggle, which succeed, which pay, which stay — and which
problem to tackle first for whom. The three rules and the MECE
requirement are **Product Institute** course material (*Product
Management Foundations*), distilled in paraphrase from the PM's notes
and **not quoted**; MECE itself is **Barbara Minto**'s (the Minto
pyramid). The scope rule, the two-step procedure, the attribute test,
the templates and the tells are this repo's operational extension.
Needs-based segmentation — the quantitative form of the same idea —
is in [`../odi/opportunity-analysis.md` §5](../odi/opportunity-analysis.md).
See [`../../CREDITS.md`](../../CREDITS.md).*

> **Where this sits.** Segments appear everywhere in the system: the
> archetypes and screener in interview prep, the cohort cuts in a
> metric read, breadth under problem-selection's goal reading, the
> segment in a value proposition and an option's hypothesis, and the
> needs-based segments the ODI pipeline computes. This is the one rule
> set they share. It answers a question the ODI doc answers only for
> survey data: *when I have usage data, tickets or interview notes,
> how do I group people so that the groups mean something?*

## 1. Three rules

1. **Segment by what matters to the business.** The cut should be one
   the business can act on differently per group: product usage, size
   of business, geography, industry, experience, plan, channel. A cut
   nobody would treat differently is a report, not a segmentation.
2. **Follow the money.** Who buys and who doesn't; who stays and who
   leaves; who expands. The commercial behaviours are the first cuts to
   try because they are the ones the strategic intent is written in
   ([`../strategy/product-strategy.md`](../strategy/product-strategy.md)).
3. **Tie every segmentation back to the problem you are solving.** A
   segmentation exists to answer a question — *who struggles with X*,
   *who succeeds at Y*, *who would pay for Z*. A cut that cannot change
   the answer to that question is dropped, however natural it looks.

And the structural requirement: **a useful segmentation is MECE** —
mutually exclusive (every customer lands in exactly one segment) and
collectively exhaustive (every customer lands somewhere). Overlapping
segments double-count; gaps hide the people you haven't thought
about. "Power users, basic users, minimal users" is MECE if the
thresholds are written down; "enterprise, education, SMB" is not if a
university buys on an enterprise plan.

## 2. Define by behaviour, describe by attribute

The move that makes a segmentation useful is the order of two steps:

**Step 1 — Define the segments by behaviour or need.** What people
*do* in the product (frequency, depth, which capabilities, whether
they share, create, modify or consume), what they are trying to get
done (the job), or what they are unsatisfied with (unmet outcomes).
Behaviour predicts behaviour; a job story's *situation* predicts more
than a persona's attributes ([`./job-stories.md`](./job-stories.md)).
Two people with the same degree, age and title can have opposite
problems; two people with the same workaround usually share one.

**Step 2 — Describe the segments with attributes, then keep only the
attributes that discriminate.** Once behavioural segments exist,
cross-tabulate them with attributes — geography, school or company
type, tenure, subject or industry, plan, channel — for two purposes:
to *find and reach* each segment in the world, and to look for a *why*
behind a behavioural difference (new teachers use lessons as-is: lack
of material, or lack of time?). An attribute earns its place only if
it varies across the segments; one that spreads evenly is descriptive
noise. This is the ODI rule stated generally: **demographics describe
segments; they never define them.**

### The scope rule *(repo extension)*

**An attribute can only discriminate if it varies within the
population you are segmenting.** Segmentation happens inside a scope —
the market definition, the initiative's segment, the population a
question was narrowed to — and any attribute that is constant across
that scope, or that *defined* the scope, is not a cut. Once the
question is "how do high-school teachers use the marketplace," school
type is no longer a segmentation of anything; subject, tenure and
sharing behaviour still are. The tell: an attribute that reads as a
candidate cut is actually the scope's own definition restated. Write
the scope at the top of every segmentation so the check is mechanical.

### Which attributes, then?

Try the ones the three rules point at, in this order: what the
business already treats differently (plan, size, channel, region);
what the problem statement mentions (a situation, a tenure, a
subject); what the interviews or tickets keep bringing up. Stop when
the segments are reachable — you could write a screener or a filter
that finds each one.

## 3. Procedure

```
SEGMENTATION — <question this answers>                                 as of <date>
Scope:      <the population, and what defines it — these are NOT cuts>
Behaviour / need cut:  <the rule for each segment, with thresholds; MECE check: yes/no>
   S1 <name>  — <definition>  — size <n / %>  — <the question's answer for this segment>
   S2 …
Attributes tried:  <attribute> → discriminates? yes (how) / no (even spread) / n/a (constant in scope)
Profile per segment:  <the attributes that discriminate, so the segment can be found>
Segment to tackle first:  <which, and why — pain × breadth under the goal reading>
Sources:  <usage data · tickets · interviews · survey>  tiers: <CONFIRMED / INFERRED / BACKGROUND>
```

Checks before the segmentation is used:

- [ ] The scope is written, and no cut restates it.
- [ ] Segments are defined by behaviour, need or job — not by an attribute.
- [ ] Segments are MECE: thresholds written; every customer lands in one.
- [ ] Every attribute kept discriminates; every attribute dropped is
      recorded as even-spread or constant.
- [ ] The segmentation answers the question it was built for, and the
      business would act differently per segment.
- [ ] Sizes are counted from data (distinct people, not events), not
      guessed.

## 4. Tells

| Anti-pattern | Tell | Fix |
|--------------|------|-----|
| **Attribute-first segments** | "Millennials", "bachelors vs. masters", "morning vs. afternoon classes" as the segments | Define by behaviour or need; use attributes to describe |
| **Restating the scope** | The population is high-school teachers and "school type" is proposed as a cut | Write the scope; an attribute constant within it is not a cut |
| **Overlap** | A customer fits two segments; totals exceed 100% | Thresholds and precedence rules until MECE |
| **The forgotten remainder** | Three vivid segments that sum to 60% of users | Add the exhaustive remainder and look at it — it is often the churn |
| **A cut nobody acts on** | "Interesting, but we'd treat them the same" | Rule 1: if no different action follows, drop the cut |
| **Segment by opinion** | Segments named from a workshop, sizes guessed | Count distinct people from usage, tickets or interviews |
| **Persona in a segment's clothes** | A named character with a photo and no behavioural rule | Keep the story for empathy; the segment needs a filter |
| **Mistaking ODI's job for this** | Running factor and cluster analysis on usage logs | ODI segments on unmet outcomes from a survey; this doc is for everything else, and hands *which needs within a job* to the pipeline |

## 5. Where it plugs in

| Agent | Uses this for |
|-------|---------------|
| **customer-interviews** | Prep: the archetypes and screener are behaviour-defined segments with the discriminating attributes as screener questions; synthesis: patterns are counted per segment |
| **metrics** | Cohort and segment cuts on the North Star inputs; the cohort curves read per behavioural segment before any average |
| **problem-selection** | Breadth under the goal reading is counted within segments; the acquisition flip asks which segment's breadth |
| **ideation** | Framing: who has this problem, by behaviour, before divergence |
| **lean-experiments / solution-options** | The segment named in the value proposition, the experiment card and the option's hypothesis is one of these, with its rule |
| **odi-data-scientist** | The quantitative form: needs-based segments from survey data, profiled with the same attribute test ([`../odi/opportunity-analysis.md` §5–6](../odi/opportunity-analysis.md)) |

## 6. Worked example (short)

Pencil, a lesson product for teachers; the question is *which teachers
struggle with the lesson marketplace, and whom to help first*.

- **Scope:** high-school teachers on the marketplace (the initiative
  narrowed to them last quarter). School type is therefore not a cut.
- **Behaviour cut:** content approach — *create new* (12%), *modify
  existing* (41%), *use as-is* (47%), thresholds by actions in the
  last 90 days; MECE by precedence (any creation → create). A second
  cut, sharing frequency, is kept as a metric per segment rather than
  a second segmentation, to avoid overlap.
- **Attributes tried:** tenure discriminates (use-as-is is 70% under
  three years); subject discriminates weakly (science over-indexes on
  modify); geography spreads evenly — dropped; age spreads evenly —
  dropped; degree spreads evenly — dropped.
- **Segment to tackle first:** *use as-is, under three years* — the
  largest and the one whose 30-day retention trails the others by 18
  points; the problem statement goes to `problem-selection` as a job
  story with this segment's evidence rows.

## Sources & materials

- **Product Institute** (founded by **Melissa Perri**) — *Product
  Management Foundations*, the segmentation lesson: segment by what
  matters to the business (usage, size, geography, industry,
  experience); follow the money (who buys, who stays); avoid
  segmentations that don't tie back to the problem; a useful
  segmentation is MECE. Licensed course material — **paraphrased from
  Daniel O'Rorke's notes; nothing quoted; the course's exercise not
  reproduced.**
- **Barbara Minto** — *The Pyramid Principle* (the MECE rule: mutually
  exclusive, collectively exhaustive), as used at McKinsey. Cited, not
  reproduced.
- **Tony Ulwick** / **Strategyn** — needs-based segmentation and
  "demographics describe, never define" — see
  [`../odi/opportunity-analysis.md`](../odi/opportunity-analysis.md)
  and the ODI credits.
- **Alan Klement** — job stories: situation over attributes
  ([`./job-stories.md`](./job-stories.md)).
- The scope rule, the two-step procedure, the attribute test, the
  template, the checks, the tells and the worked example are **this
  repo's operational extension**.
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

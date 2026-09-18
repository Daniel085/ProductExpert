# Affinity Mapping (K-J Method) — Method Reference

*Distilled from **ASQ**'s "What is an Affinity Diagram? (K-J Method)"
(adapted from *The Quality Toolbox*, 2nd ed., ASQ Quality Press) — source
PDF and transcription preserved in [`./materials/`](./materials/). The
method was created in the 1960s by Japanese anthropologist **Jiro
Kawakita** (hence "K-J"). Also called: affinity chart, affinity mapping,
thematic analysis. See [`../../CREDITS.md`](../../CREDITS.md).*

> **What this is for in ProductExpert:** the *bottom-up theming* step that
> several agents share. Whenever there are too many items to hold in your
> head — interview observations, support tickets, survey verbatims,
> brainstorm output, candidate problems from six stakeholders — this is how
> you turn the pile into a handful of themes **without deciding the
> categories in advance**. It is a technique, not an agent: read by
> `problem-selection` (its "identify patterns" step), `customer-interviews`
> (synthesis: patterns across interviews) and `ideation` (converge).

## What it is

An affinity diagram organizes a large number of ideas into their natural
relationships. It's the organized output of a brainstorm or a data dump:
generate → group by affinity (similarity) → name the groups. It works by
letting the group move past habitual thinking and preconceived categories,
tapping intuition rather than analysis. Typical size 40–60 items; 100–200
is not unusual.

**When to use it** (ASQ's list, verbatim in spirit):

- Many facts or ideas in apparent chaos.
- Issues too large and complex to grasp.
- Group consensus is needed.
- After a brainstorming exercise.
- Analyzing **verbal data** — survey open-ends, interview notes, tickets.
- Collecting and organizing large data sets.
- Developing relationships or themes among ideas.
- Reducing many attributes to categories that can be addressed at a
  higher level.

## The process (four steps)

**0. Agree the question.** State the issue as a question before generating
anything — *"What are the barriers to on-time delivery of medications?"*
(ASQ's hospital example). A question keeps the items answers to the same
thing.

**1. One idea per note.** Each item on its own note, **3–7 words**, legible
from a distance. Spread them randomly where everyone can see them all.
Silent recording (everyone writes until they run dry) guarantees
participation; round-robin brainstorming works too.

**2. Group in silence.** Everyone sorts simultaneously, **without
talking**, into 5–10 groupings until every note is placed. Rules:

- **No pre-set categories, no headings yet.** Call them "groupings", not
  categories — the names come *after* the shape emerges.
- **Loners are fine.** A note that fits nowhere stays alone.
- **Moving someone else's note is fine.** Disagreement gets resolved by
  moving, not arguing (that comes in step 3).
- **A note that belongs in two groups gets duplicated.**

**3. Discuss, then name.** Now talk: the shape of the chart, surprising
patterns, and *why* contested notes moved. Adjust. Then for each group find
the one note that captures the group's meaning and put it on top as the
**header card**; if none exists, write one. Headers must state the
**common thread** of everything under them — descriptive, not a label
("pharmacy may be understaffed", not "staffing").

**4. Supergroups, if they earn it.** Combine related groups under a higher
header when a genuine second level exists. Assign by **gut feel, not
contemplation** — over-deliberation reintroduces the preconceptions the
method was designed to escape.

**Then review.** Everyone walks the finished map and comments; the map is
a conversation starter, not a verdict.

## Running it in text (how agents apply it)

Agents have no wall, but the discipline transfers:

1. **Extract items** from the source material — one observation, quote,
   ask or idea per line, trimmed to 3–7 words, with a **source tag**
   (`[I3]` interview 3, `[T-4412]` ticket, `[S-q7]` survey open-end,
   `[stakeholder: sales]`). The tag is what lets a theme be counted later.
2. **Group before naming.** Produce the groupings first with *no* header
   text — only the member items — so the categories genuinely emerge
   rather than get imposed. Keep loners as a `(loner)` list; duplicate an
   item into two groups when it truly straddles.
3. **Name afterwards.** Write each header as a full-sentence common thread.
   Prefer promoting a member item to the header when one already captures
   it.
4. **Count and attribute.** For each theme: number of items, number of
   *distinct sources*, and the source tags. (One person with nine notes is
   one voice, not nine — see the ranking rules in
   [`picking-the-right-problem.md`](./picking-the-right-problem.md).)
5. **Supergroup only if real.** Two levels at most.
6. **Show the moves.** Log any item you relocated after first grouping and
   why — the "controversial notes" discussion, in writing.

**Output template:**

```
Question: <the framing question>
Items: <N> from <k> sources

## Theme: <header — the common thread as a sentence>
   items: n · distinct sources: s · tags: [I1] [I4] [T-991] …
   - <item> [tag]
   - <item> [tag]
   …
## Theme: …
## Loners
   - <item> [tag]

Supergroups (if any): <header> ⊃ {theme, theme}
Moves: <item> moved from <A> to <B> because …
```

## What it is not — and what comes next

- **It does not rank.** Affinity mapping tells you *what the themes are*,
  not which matters. Prioritization is a separate step with separate
  criteria ([`picking-the-right-problem.md`](./picking-the-right-problem.md)).
- **It does not find causes.** ASQ's own next step after the map is an
  interrelationship diagram or a cause-and-effect (fishbone) diagram to
  reach root causes. In this system the "why" behind a theme is the job of
  the insight ladder (observation → finding → insight,
  `methods/customer-interviews/research-and-insight.md`).
- **Theme ≠ problem.** A theme like "paperwork" (ASQ's onboarding example)
  is a bucket; the problem statement still has to be written from the
  customer's perspective as a job story
  (`methods/jtbd/job-stories.md`) before it can be evaluated.

## Anti-patterns

| Anti-pattern | Tell | Fix |
|--------------|------|-----|
| **Pre-labelled bins** | The categories were written before the items were | Delete the headers, regroup silently, name last |
| **Talking while sorting** | Loudest voice decides the shape | Silent pass first; discussion only at step 3 |
| **Vague headers** | "Misc", "UX", "Performance" | Header = the common thread as a sentence someone could disagree with |
| **Forcing loners in** | Every note ends up in a group | Loners are legitimate; they are often the surprise |
| **Counting notes as people** | "Nine items — big theme" | Count distinct sources, keep the tags |
| **Stopping at the map** | Themes presented as conclusions | Route themes into prioritization and root-cause work |

## Sources & materials

- **ASQ (American Society for Quality)** — *"What is an Affinity Diagram?
  (K-J Method)"*, Learn About Quality / Quality Resources, adapted from
  *The Quality Toolbox*, Second Edition (ASQ Quality Press). Source PDF:
  `./materials/ASQ-WhatIsAnAffinityDiagram-KJMethod.pdf`; transcription:
  `./materials/extracted/asq-affinity-diagram.txt`.
- **Jiro Kawakita** — originator of the K-J Method (1960s).
- The text-mode adaptation (source tags, group-before-name, distinct-source
  counts, the output template) is this repo's operational extension.
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

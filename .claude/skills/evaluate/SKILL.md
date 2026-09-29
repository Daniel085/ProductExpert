---
name: evaluate
description: >-
  Runs ProductExpert's evaluation suite: routing (does a PM request land
  on the right agent and mode — 27 cases), gates (does /navigate status
  derive phase, gates, blocker and discrepancies correctly from three
  fixture initiatives), and output (does an agent's artifact meet the
  rubric and honour its gate). Invoke as /evaluate routing | gates |
  output <agent> <fixture> | all. Trigger on: run the evals, test the
  router, check the gates, is the system working, regression check
  after editing an agent or method doc.
---

# /evaluate

You run the evaluation suite in `evals/`. You are a **judge and a
runner**, not an agent: you never do discovery work, and your scores
are BACKGROUND-tier signals for the maintainer, never evidence about a
product. Read `evals/README.md` first.

## `routing`

For each row in `evals/routing-cases.md`:

1. Read the input exactly as written. Read every agent's `description`
   in `.claude/agents/*.md` (and the `navigate` skill's).
2. Decide, from the descriptions alone, which agent you would delegate
   this to and in which mode — the way auto-delegation would. Do not
   peek at the expected column first.
3. Compare. A pass is the expected agent (or a listed alternate) *and*
   the expected mode.

Report a table (case · chosen · expected · pass/fail · the description
phrase that decided it), the score out of 27, and for each fail the
**description fix** you'd propose — the phrase to add to, or remove
from, an agent's description. Never propose editing the case unless the
case contradicts a method doc; say so if it does.

## `gates`

For each fixture in `evals/gate-fixtures/*/`:

1. Run the `status` derivation from the `navigate` skill against the
   fixture folder exactly as you would for a real initiative — read
   `STATUS.md`, then re-derive every gate from the artifacts using the
   rules in `docs/interaction-model.md`.
2. Do **not** edit the fixture. Write what you *would* change to
   `STATUS.md` into your report instead.
3. Compare your derivation with `expected.md`: phase, gates passed,
   blocker, discrepancies flagged, next agent.

Report per fixture: match / mismatch on each of the five items, and the
rule you applied for any gate you decided differently from `expected.md`.
Score: fixtures fully matched out of total. A planted discrepancy that
goes unflagged is a fail.

## `output <agent> <fixture>`

1. Write a delegation brief (the navigator's template) for `<agent>`
   against a **copy** of the fixture in your scratch space — never the
   fixture itself — with an objective appropriate to the fixture's
   blocker (e.g. lean-experiments on `b-problem-validated`: write the
   value proposition and the Wizard-of-Oz card the ledger names).
2. Invoke the agent with the Agent tool and the brief.
3. Judge the result against `evals/output-rubric.md`: the universal rows
   and the agent's rows, each 0 / 0.5 / 1, citing the artifact line or
   behaviour that earned the score. Pass at ≥ 0.8 with no zero on a
   **gate** row.
4. Then answer the human-pass questions yourself, briefly, and mark them
   as *a model's answers — a person should read the artifact*.

Report: the score table, pass/fail, the two weakest rows with the method
doc they trace to, and the artifact paths for the human pass.

## `all`

Run `routing`, then `gates`, then `output` for the three agents most
recently edited (check `git log --since` on `.claude/agents/`); summarize
in one screen.

## After every run

Append one line to `evals/runs.md`: date · `git rev-parse --short HEAD`
· routing x/27 · gates a/b · output <agent> score · one-line notes.
Never edit earlier lines.

## Rules

- **Cases and fixtures are read-only.** Fixes go to descriptions, gate
  rules, method docs — and are proposed, not applied, unless the PM
  asks.
- **Judge from the written rule.** Every score cites a rubric row, and
  every rubric row cites a method doc. "Feels weak" is not a score.
- **Your verdicts are BACKGROUND.** Say so in the report footer.
- **Be short.** One table per section, mismatches in full, passes in
  one line.

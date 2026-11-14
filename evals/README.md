# Evaluations

How we know the system works: a small, fixed set of cases run the same
way every time, judged against written rubrics, with a human pass at the
end. Sized the way Anthropic's research-system team sized theirs — start
with about twenty cases that represent real usage; early-stage changes
show big effects on small sets, and a rubric plus a human catches what
the rubric can't.

Run with `/evaluate` (`.claude/skills/evaluate/SKILL.md`):

| Command | What it checks | Cases |
|---------|----------------|-------|
| `/evaluate routing` | That a PM's request lands on the right agent and mode | [`routing-cases.md`](./routing-cases.md) — 30 inputs with expected agent, mode, and accepted alternates |
| `/evaluate gates` | That `/navigate status` derives phase, gates and blocker correctly from artifacts, and flags status-file claims the artifacts don't back | [`gate-fixtures/`](./gate-fixtures/) — three initiative folders, each with `expected.md`; [`derive_gates.py`](./derive_gates.py) is the deterministic checkpoint the model's reading is reconciled against |
| `/evaluate output <agent> <fixture>` | That an agent's artifact meets the output rubric and the agent honoured its gate | [`output-rubric.md`](./output-rubric.md), run against a fixture input |
| `/evaluate all` | All three, summarized | |

## What "pass" means

- **Routing:** the chosen agent matches the expected one (or a listed
  alternate) *and* the mode matches. Report a score out of 30 and every
  mismatch with the input text, so the fix is to the agent's
  `description`, not to the case.
- **Gates:** for each fixture, phase, passed gates and blocker match
  `expected.md` exactly, and every planted discrepancy is flagged. One
  fixture plants a status-file lie on purpose.
- **Output:** each rubric row scores 0, 0.5 or 1; an output passes at
  ≥ 0.8 with no zero on a *gate* row. The judge is a model reading the
  rubric; the human pass is the list at the bottom of the rubric.

## Rules

- **Cases are fixed; agents change.** A failing case is a bug in an
  agent description, a gate rule, or a method doc — never edited away
  in the case file unless the case itself was wrong, and then the edit
  says why.
- **Fixtures are synthetic and small.** They contain the minimum
  artifact text that satisfies or violates a gate rule, not realistic
  documents. Realism is the human pass's job.
- **Judge output is BACKGROUND.** A rubric score is a signal for the
  maintainer, not evidence about a product; the same tiering rule that
  governs the agents governs the evals.
- **Record runs.** Append each run's date, commit, scores and mismatches
  to [`runs.md`](./runs.md), so a regression is visible as a delta.

## Adding cases

- Routing: one row — input as a PM would type it, expected agent, mode,
  alternates, and the reason (which description phrase should catch it).
- Gates: copy a fixture, change the artifacts, write `expected.md`.
- Output: add a rubric row only if it maps to a rule in a method doc;
  cite the doc.

## Not here

`claude plugin eval` and `/skill-doctor` exist for plugin-packaged
skills; this repo is not a plugin, so the evals run through the
`/evaluate` skill in the main session. If the repo is ever packaged,
these case files are the eval suite's input.

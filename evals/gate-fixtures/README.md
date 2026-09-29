# Gate fixtures

Three synthetic initiative folders for `/evaluate gates`. Each is the
minimum artifact text that satisfies or violates a gate rule; none is a
realistic document. `expected.md` in each states what `/navigate status`
must derive. Fixture **b** plants a status-file lie on purpose.

| Fixture | Story | Expected |
|---------|-------|----------|
| `a-fresh/` | Just scaffolded | Opportunity Discovery · nothing passed · blocker G1 |
| `b-problem-validated/` | Framed, ledger seeded, a *Yes* case, scorecard all ≥ 3 — and STATUS.md falsely claims G6 | Solution Validation · G1–G4 passed · blocker G5 · discrepancy on G6 |
| `c-option-chosen/` | Everything through a chosen option and a v1.0 scope; no PR/FAQ, no metric cards | Solution Validation · G1–G8 passed · blocker G9 · G10 open |

# Gate fixtures

Five synthetic initiative folders for `/evaluate gates`. Each is the
minimum artifact text that satisfies or violates a gate rule; none is a
realistic document. `expected.md` in each states what `/navigate status`
must derive. Fixture **b** plants a status-file lie on purpose. Fixture
**d** doubles as the input for `/evaluate output opportunity-sizing`:
it carries the ICP tiers, the interview price quotes and the market
scope a sizing needs, and nothing that sizes the market.

| Fixture | Story | Expected |
|---------|-------|----------|
| `a-fresh/` | Just scaffolded | Opportunity Discovery · nothing passed · blocker G1 |
| `b-problem-validated/` | Framed, ledger seeded, a *Yes* case, scorecard all ≥ 3 — and STATUS.md falsely claims G6 | Solution Validation · G1–G4 passed · blocker G5 · discrepancy on G6 |
| `c-option-chosen/` | Everything through a chosen option and a v1.0 scope; no PR/FAQ, no metric cards | Solution Validation · G1–G8 passed · blocker G9 · G10 open |
| `e-theory-desk-only/` | Arrived with a three-claim theory; framed, ledger seeded, forty desk rows, a claims table and two cases that are all *Not yet* — and STATUS.md falsely claims G3 on the strength of the desk rows; two open rows under *Owed by you* | Problem Validation · G1–G2 passed · blocker G3 · discrepancy on G3 · owed-by-you rows reported · next: the PM's interviews |
| `d-sizing-needed/` | Framed, ledger seeded, a *Yes* case for a market the product doesn't serve; scorecard has business impact at 2 because nobody has sized it | Problem Validation · G1–G3 passed · blocker G4 · next: opportunity-sizing |

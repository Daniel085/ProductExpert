# STATUS — <initiative name>

| | |
|---|---|
| **Slug** | `<slug>` |
| **Owner** | <name> |
| **Created** | <YYYY-MM-DD> |
| **Purpose** | <a new business / a new product or service line / a route to market for something built / an improvement to a product with users / "undecided → you owe it"> |
| **Goal metric** | <name + definition, or "not yet defined → metrics"> |
| **Direction** | <strategic intent SI-n → product initiative PI-n, from the strategy stack, or "not stated → the level above owes it"> |
| **Arrived with** | <idea / theory (its claims, numbered) / feature request / problem pile / notes / data> |
| **Phase** | Opportunity Discovery |

## Gates

Marked by the owning agent when its artifact meets the rule; re-derived
by `/navigate status`. Never marked by hand to move things along.

| # | Gate | Status | Date | Artifact | Verdict / note |
|---|------|--------|------|----------|----------------|
| G1 | Framed (job story, no solution noun) | open | | | |
| G2 | Ledger seeded (one riskiest assumption + cheapest test) | open | | `ledger.md` | |
| G3 | Problem evidenced (case verdict Yes / persevere with ≥ 2 evidence types) | open | | | |
| G4 | Gaps closed (scorecard, no area < 3) | open | | | |
| G5 | Promise written (value proposition from evidence) | open | | | |
| G6 | Solution read out (≥ 1 card with Found out + decision) | open | | | |
| G7 | Option chosen | open | | | |
| G8 | v1.0 scoped (feature set + deferred list with costs) | open | | | |
| G9 | Vision decided (PR/FAQ verdict: build / iterate / kill / park) | open | | | |
| G10 | Success defined (metric cards + counter-metric) | open | | | |

Status values: `open` · `passed` · `failed` (with what would pass it) ·
`n/a` (with why — e.g. G8 when the verdict is kill).

## Owed by you

What only the PM can settle: decisions deferred at the start, pass and
fail lines to sign off before a round begins, and every assumption an
agent made while the PM was away. One row each; an agent adds rows, only
the PM's answer closes one. `/navigate status` lists the open rows.

| # | Owed | Raised by · date | Why it matters | Answer · date |
|---|------|------------------|----------------|---------------|

## Log

Newest last. One line per engagement, under 240 characters (the detail
lives in the artifact):
`YYYY-MM-DD · <agent> · <what was done> · <verdict> · <artifact> · next: <agent or "you: …">`

- <YYYY-MM-DD> · navigate · initiative created · — · `STATUS.md`, `ledger.md` · next: <agent>

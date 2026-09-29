# OPTION — Resumable import                                    status: chosen

Alignment: 90-day retention of new workspaces; Business Alignment 5/5.
Hypothesis: We believe building resumable import will satisfy the job "finish workspace setup the same day even when an import breaks" for new small teams and result in a 10-pt lift in 90-day retention among workspaces that hit an import failure.
Problem: (job story from problems.md) — because a failed import today means re-entering everything.
Behavior change: today teams re-enter data or abandon; if this works they resume and complete setup the same day.
In scope: 1. resume from failed row 2. show what succeeded 3. retry per chunk
Out of scope: pre-validation report (separate problem); enterprise SSO (different segment)
Dependencies: idempotent write path (eng spike done 2026-09-20 — verified)
Risks / unknowns: R1 chunk retry hides data-quality errors — ledger A3 — test: audit 20 restored workspaces
Success metrics & outcomes: M1 same-day completion after failure, baseline 20% → 60% by Q1; M2 90-day retention of failed-import cohort, baseline 41% → 51%; counter-metric: duplicate rows per workspace
Iteration plan: 1. resume-from-row for CSV only — validates A3 — 3 wks  2. chunk retry — validates duplicate-row counter — 2 wks
Evidence summary: WoZ card CONFIRMED same-day completion; retention lift INFERRED from funnel gap.

# MINIMUM FEATURE SET — v1.0 of Resumable import                dated 2026-09-27

| # | Feature | Class | CSF | Value buckets | CoD/wk | Profile · latest start | Duration | CD3 | v1.0? | Reason |
|---|---------|-------|-----|---------------|--------|------------------------|----------|-----|-------|--------|
| 1 | Resume from failed row | job-critical | nothing re-entered | protect + reduce | 40k | 3 | 4 wks | 10.0 | yes | core job |
| 2 | Show what succeeded | adoption-critical | trust | protect | 12k | 3 | 1 wk | 12.0 | yes | switch condition |
| 3 | Chunk retry | postponable | — | reduce | 9k | 3 | 3 wks | 3.0 | no → v1.1 | below cut line |
| 4 | Audit log | postponable | — | avoid (p≈0.3) | 6k | 3 | 3 wks | 2.0 | no → v1.2 | revisit 2027-01 |

Deferred: 3 (9k/wk, v1.1), 4 (6k/wk, v1.2). Cut line: CD3 < 5 deferred; capacity 6 wks before Q1.

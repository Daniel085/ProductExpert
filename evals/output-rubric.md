# Output rubric

For judging an agent's artifact and behaviour on a fixture input. Each
row scores **1** (met), **0.5** (partly), **0** (not met). Rows marked
**gate** are the ones an agent must never fail; a zero on any of them
fails the output regardless of the total. Every row cites the rule it
enforces, so a disputed score goes to the method doc, not to opinion.

## Universal rows (every agent)

| # | Row | Rule |
|---|-----|------|
| U1 **gate** | Read `STATUS.md` and `ledger.md` first, and only the inputs the brief named | interaction model, context discipline |
| U2 **gate** | Refused or routed back when a required input was missing, instead of inventing it | each agent's "Refuses" list |
| U3 **gate** | Nothing the agent generated is tiered above BACKGROUND; INFERRED/CONFIRMED rows cite a real person or artifact | principles §29; assumption-ledger tiers |
| U4 | Artifacts saved at the canonical paths in the method-doc format | interaction model, layout |
| U5 | One log line appended to `STATUS.md`; gate marked only if the artifact meets the rule | interaction model, gates |
| U6 | Ended with the verdict options and an honest read, not a hedge | each agent's closing instruction |
| U7 | Said which mode it was in; asked at most one question when unclear | each agent's "Detect the mode" |

## Agent-specific rows

**ideation** — I1 ≥ 5 distinct options before any evaluation, incl. one inversion and one removal (principle 19). I2 landscape scan tagged BACKGROUND, no verdict drawn from it. I3 ledger names exactly one riskiest assumption and a test cheaper than building. I4 routing decision stated.

**customer-interviews** — C1 (prep) every guide question is about a specific past event; no "would you…" (principle 2). C2 (prep) assumptions ranked impact × uncertainty. C3 (synthesis) observations and interpretations in separate columns. C4 (synthesis) each pattern carries a head-count; insights pass Edgley's bar. C5 (synthesis) persevere / pivot / dig deeper with a next test in the We believe / To verify format. C6 (prep) archetypes defined by behaviour or need, MECE, with no attribute that merely restates the scope (`methods/jtbd/segmentation.md`).

**problem-selection** — P1 **gate** no solution-noun in any problem statement; rewrites shown. P2 **gate** no *Yes* on a single evidence type. P3 **gate** no Business Alignment score without a stated goal. P4 goal reading named before scoring. P5 distinct sources counted, not items. P6 conflicts explained or verdict *Not yet*. P7 (gap mode) every score cites an artifact and tier; BACKGROUND-only capped at 3; lowest area routed.

**lean-experiments** — L1 **gate** "trying to prove" stated in one sentence. L2 **gate** generative vs. evaluative named and matched to the family. L3 **gate** *Expected* and *Would disprove* filled before the run. L4 concierge never used as validation. L5 (breakdown) observation recovered verbatim; chain written; exactly one riskiest link. L6 (readout) null result checked for reach before "no demand". L7 (MVP) learning goal and one readout measure; refuses a v1 in disguise.

**solution-options** — S1 **gate** refuses an option with no solution readout. S2 hypothesis names solution, job, segment, KPI. S3 behavior change observable without a dashboard. S4 every risk carries a test; iteration plan learns per chunk. S5 (v1.0) job-critical / adoption-critical / sustainability in by evidence; postponable ranked by CD3; external deadlines zero until latest start; no RICE.

**prfaq** — F1 **gate** every claim evidence-cited or flagged `[ASSUMPTION]`. F2 PR fits one page; customer language, no superlatives. F3 problem paragraph is a job story in prose. F4 full internal FAQ bank faced; unanswered stays visible. F5 verdict: iterate / build / kill / park.

**experimentation** — E1 **gate** trust checks (SRM first) before any effect estimate. E2 pre-registration frozen before data; boundary set at design time. E3 sample size computed and shown. E4 "underpowered" said when true; no "trending".

**opportunity-sizing** — Z1 **gate** no SOM without a written segment rule and a sourced price; no bare percentage share, no pasted analyst figure as the number (`methods/sizing/market-sizing.md` §1, §3). Z2 **gate** every leaf carries a source, tier, grain, reference date and a 5/50/95 range; the sizing's tier is the weakest load-bearing leaf (§7). Z3 both routes shown and reconciled by the one leaf that closes the gap; beyond a factor of three the definition is revisited, never averaged (§5). Z4 market defined as job executors + job, type and bucket classified, scope written (§2). Z5 the four tests run (implied share, $100M ladder, fund-return, aggregation) and the counter-case written (§5). Z6 a model that re-runs from the register, saved (§7).

**metrics** — M1 North Star is a value-exchange metric, not revenue. M2 every target ships with a counter-metric. M3 each metric passes the "what would we do differently" test. M4 cohorts over averages.

**ODI agents** — O1 statements follow the grammar (direction + metric + object + context), solution-agnostic. O2 (editor) coverage across all 8 job-map steps reported; *Ready: Yes/No* stated. O3 (survey) sizing rule stated (≥ 3× statements, 180–600). O4 (data) N ≥ 180 and < 10% missing checked before scoring; silhouette gate on segments; scripts saved.

## Human pass (after the model judge)

Things a rubric cannot see; a person reads the artifact and answers:

- Would a real PM act on this, or is it plausible-sounding filler?
- Did the agent smuggle a solution in as a need anywhere the rubric didn't look?
- Is the evidence trail honest — could you follow a citation to the source?
- Does it read like a coach (says *why* when it corrects) or a generator?
- Anything that would embarrass us in front of a customer?

Record the human notes alongside the scores in `runs.md`.

# Routing expected answers

The answer key for [`routing-inputs.md`](./routing-inputs.md). **The
judge opens this file only after deciding all 39 cases from the agent
descriptions alone.** "Alternates" are acceptable second answers;
anything else is a miss. The **why** names the description phrase that
should catch the input — if a case fails, that phrase is what to fix.
Keep the two files in step: same numbers, same inputs.

| # | Expected agent | Mode | Alternates | Why |
|---|----------------|------|------------|-----|
| 1 | ideation | assumption testing | — | "I have an idea", "is this viable" |
| 2 | ideation | solution ideation | — | "brainstorm", problem well-defined |
| 3 | ideation | strategy exploration | — | "stress-test", "should we pursue" |
| 4 | customer-interviews | prep | — | "prep for interviews" |
| 5 | customer-interviews | synthesis | — | "making sense of interview notes" |
| 6 | customer-interviews | prep (de-requirement) | problem-selection (theme) | "requirements list … tracing back to real problems"; if the problems already have evidence, problem-selection |
| 7 | odi-interviewer | job map / guide prep | — | "job map", "desired outcomes" |
| 8 | odi-interviewer | extraction | — | "extract desired outcome statements" |
| 9 | odi-outcome-editor | curate | — | "curate/clean/dedupe outcome statements" |
| 10 | odi-survey-builder | instrument | — | "ODI survey", "fielding spec" |
| 11 | odi-data-scientist | analysis | — | "opportunity score", "importance satisfaction data" |
| 12 | problem-selection | theme | — | "affinity map / theme these tickets" |
| 13 | problem-selection | rank | — | "which problem first", "customer signal", "business alignment" |
| 14 | problem-selection | evaluate | — | "is this problem worth solving" |
| 15 | problem-selection | gap assessment | — | "knowledge gaps", "are we ready to explore solutions" |
| 16 | problem-selection | root cause | — | "root cause", "why is this happening" |
| 17 | lean-experiments | breakdown | — | "feature request (with a validated problem behind it)", "the CEO wants X" |
| 18 | lean-experiments | design / triage | — | "test before we build", "concierge", "Wizard of Oz" |
| 19 | lean-experiments | MVP | — | "is this an MVP or a v1", "MVP" |
| 20 | lean-experiments | value proposition | — | "value proposition" |
| 21 | experimentation | design | — | "A/B test", live product with traffic |
| 22 | solution-options | define + scope v1.0 | — | "write up the solution", "v1.0 scope" |
| 23 | prfaq | draft | — | "PR/FAQ", "press release" |
| 24 | metrics | design + audit | — | "north star metric", "vanity metrics" |
| 25 | problem-selection | rank (initiatives against the intent) | ideation (problem exploration, if the candidates are still fuzzy) | "which product initiatives serve this strategic intent"; initiatives are problems ranked on Business Alignment against the stated goal |
| 26 | lean-experiments | kata (direction ladder; unstated direction = first obstacle) | — | "product kata", "current condition"; the strategy method's rule that an unstated direction is the first obstacle, not something to invent |
| 27 | prfaq | strategy-memo review (critique) | ideation (strategy exploration, if the memo is still being shaped rather than reviewed) | "review our product strategy memo", "product narrative, pitch doc review"; the memo is reviewed as a document against the strategy method's tests |
| 28 | metrics | quantify (value estimate) | — | "quantify the business value of an initiative", "revenue impact of a lift"; not experimentation (no test to read out) and not problem-selection (the problem already has its case) |
| 29 | opportunity-sizing | from nothing (both routes) | — | "market size", "TAM", "investor asked for our TAM", a market the product doesn't serve yet; not metrics (no baseline to apply a lift to) |
| 30 | opportunity-sizing | critique | — | "is this sizing credible", bare-share critique; not prfaq (a slide, not a narrative document) and not ideation (a number to check, not a direction to explore) |
| 31 | desk-research | collect | — | "what are people saying about", "search the forums / reviews", "collect evidence before interviews"; not customer-interviews (nothing to prep or synthesize yet) and not ideation (collection, not a brainstorm) |
| 32 | desk-research | intake | — | "file these saved pages / threads / exports into the notes"; not customer-interviews synthesis (saved public pages, not interview notes) and not problem-selection (filing, not theming) |
| 33 | problem-selection | theory test | — | "was my theory right", "test this theory against the evidence"; the notes already exist, so not desk-research; not ideation (evidence in hand, a verdict per claim wanted) |
| 34 | problem-selection | add evidence | — | "more notes / threads / tickets came in — does anything change", "add this evidence to the cases"; not theme mode (cases exist) |
| 35 | navigate | readout | — | "write up where this stands for the team", "the case so far … for someone who was not in the room"; not prfaq (no press release asked for, no vision to decide) |
| 36 | desk-research | teardown | ideation (landscape scan at teardown depth) | "competitor teardown with prices", "who already does this and what do they charge", the searches behind every "nobody found" |
| 37 | navigate | hypothesis | ideation (assumption testing — acceptable only if it adds one ledger row and stops) | "a new hypothesis" part-way through an initiative that exists; not a restart, not `start`; a solution hypothesis for a *Yes* problem would be lean-experiments |
| 38 | navigate | readout (slides) | — | "slides", "presenting … to the leadership team", "where it stands"; not prfaq (no press release), not opportunity-sizing (no TAM slide to critique) |
| 39 | navigate | status | — | "is that write-up still current" — the stale-summary check; not readout (asked whether, not to rewrite), not problem-selection |

Near-miss pairs the router must keep apart (each appears above): 6 vs
17 (requirements with vs. without a validated problem); 13 vs 22
(ranking problems vs. defining a tested solution); 18 vs 21 (pre-build
test vs. A/B on a live product); 2 vs 22 (brainstorm options vs. solution
option); 11 vs 13 (outcomes within a job vs. problems across the
business); 3 vs 25 (stress-testing a direction vs. choosing the
initiatives under a stated one); 25 vs 26 (setting initiatives one
level up vs. reading the direction into one initiative's kata); 3 vs
27 (exploring a direction in conversation vs. reviewing a written
memo); 28 vs 21 and 13 (sizing an initiative's value vs. designing a
test vs. ranking problems); 28 vs 29 (a change to a product with a
baseline vs. a market the product doesn't serve yet); 30 vs 27 (a TAM
slide to critique vs. a strategy memo to review); 5 vs 32 (interview
notes to synthesize vs. saved public pages to file); 12 vs 34 (a first
pile to theme vs. more evidence for cases that exist); 1 vs 33 (an idea
to stress-test vs. a theory with evidence to judge); 23 vs 35 (a PR/FAQ
vs. a status readout); 36 vs 2 (a priced teardown vs. a brainstorm's
scan); 37 vs 1 (a hypothesis inside a running initiative vs. a new
idea); 38 vs 35 (slides vs. the one-page readout); 39 vs 35 (asking
whether a write-up is current vs. asking for one).

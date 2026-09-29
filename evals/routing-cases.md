# Routing cases

26 inputs as a PM would type them, with the agent and mode they should
land on. "Alternates" are acceptable second answers; anything else is a
miss. The **why** names the description phrase that should catch the
input — if a case fails, that phrase is what to fix.

| # | Input | Expected agent | Mode | Alternates | Why |
|---|-------|----------------|------|------------|-----|
| 1 | "I have an idea: a tool that lets freelancers invoice from their phone. Is it viable?" | ideation | assumption testing | — | "I have an idea", "is this viable" |
| 2 | "Brainstorm ways we could reduce onboarding drop-off." | ideation | solution ideation | — | "brainstorm", problem well-defined |
| 3 | "We're thinking about entering the SMB segment. Stress-test that direction." | ideation | strategy exploration | — | "stress-test", "should we pursue" |
| 4 | "Prep me for interviews with clinic managers about scheduling headaches." | customer-interviews | prep | — | "prep for interviews" |
| 5 | "Here are notes from 9 interviews in `discovery/notes/`. What did we learn?" | customer-interviews | synthesis | — | "making sense of interview notes" |
| 6 | "Sales sent a list of 14 requirements from a prospect. Where do we start?" | customer-interviews | prep (de-requirement) | problem-selection (theme) | "requirements list … tracing back to real problems"; if the problems already have evidence, problem-selection |
| 7 | "We've validated the job 'plan and track a software project'. Map it and capture outcomes." | odi-interviewer | job map / guide prep | — | "job map", "desired outcomes" |
| 8 | "Extract outcome statements from this transcript." | odi-interviewer | extraction | — | "extract desired outcome statements" |
| 9 | "Here are 160 raw outcome statements — clean them up." | odi-outcome-editor | curate | — | "curate/clean/dedupe outcome statements" |
| 10 | "Turn the curated outcomes into a survey we can field." | odi-survey-builder | instrument | — | "ODI survey", "fielding spec" |
| 11 | "Survey results are in (CSV, n=312). Which needs are underserved, for whom?" | odi-data-scientist | analysis | — | "opportunity score", "importance satisfaction data" |
| 12 | "We have 140 support tickets tagged 'import'. Theme them." | problem-selection | theme | — | "affinity map / theme these tickets" |
| 13 | "We have four candidate problems and one quarter. Which first? Goal is 90-day retention." | problem-selection | rank | — | "which problem first", "customer signal", "business alignment" |
| 14 | "Is the import-failure problem validated enough to build for?" | problem-selection | evaluate | — | "is this problem worth solving" |
| 15 | "Are we ready to explore solutions for import recovery, or what don't we know yet?" | problem-selection | gap assessment | — | "knowledge gaps", "are we ready to explore solutions" |
| 16 | "Why do imports keep failing at the mapping step? Find the root cause." | problem-selection | root cause | — | "root cause", "why is this happening" |
| 17 | "The CEO wants us to add a bulk-export button. The export problem has a Yes case. Should we build it?" | lean-experiments | breakdown | — | "feature request (with a validated problem behind it)", "the CEO wants X" |
| 18 | "How do we test the recovery flow before we build it — concierge or Wizard of Oz?" | lean-experiments | design / triage | — | "test before we build", "concierge", "Wizard of Oz" |
| 19 | "Let's ship an MVP of recovery next sprint." | lean-experiments | MVP | — | "is this an MVP or a v1", "MVP" |
| 20 | "Write the value proposition for the recovery product." | lean-experiments | value proposition | — | "value proposition" |
| 21 | "Design an A/B test for the new checkout button; we have 40k weekly users." | experimentation | design | — | "A/B test", live product with traffic |
| 22 | "Recovery tested well. Write it up as an option and scope v1.0." | solution-options | define + scope v1.0 | — | "write up the solution", "v1.0 scope" |
| 23 | "Draft the PR/FAQ for import recovery from the option card." | prfaq | draft | — | "PR/FAQ", "press release" |
| 24 | "What should our north star be, and audit our dashboard for vanity metrics." | metrics | design + audit | — | "north star metric", "vanity metrics" |
| 25 | "Leadership's strategic intent this year is to grow self-serve revenue 40%. Which product initiatives should serve it? We have retention, import and billing problems on the table." | problem-selection | rank (initiatives against the intent) | ideation (problem exploration, if the candidates are still fuzzy) | "which product initiatives serve this strategic intent"; initiatives are problems ranked on Business Alignment against the stated goal |
| 26 | "Set up the kata for the import-recovery initiative. Nobody has told us which strategic intent it serves." | lean-experiments | kata (direction ladder; unstated direction = first obstacle) | — | "product kata", "current condition"; the strategy method's rule that an unstated direction is the first obstacle, not something to invent |

Near-miss pairs the router must keep apart (each appears above): 6 vs
17 (requirements with vs. without a validated problem); 13 vs 22
(ranking problems vs. defining a tested solution); 18 vs 21 (pre-build
test vs. A/B on a live product); 2 vs 22 (brainstorm options vs. solution
option); 11 vs 13 (outcomes within a job vs. problems across the
business); 3 vs 25 (stress-testing a direction vs. choosing the
initiatives under a stated one); 25 vs 26 (setting initiatives one
level up vs. reading the direction into one initiative's kata).

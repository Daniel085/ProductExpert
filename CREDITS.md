# Credits & Attribution

ProductExpert's agents distill the work of others. This file records where the
ideas come from. Each method doc also cites its sources inline; this is the
master list. Raw third-party materials under `methods/<topic>/materials/` remain
the property of their authors and are included for reference and attribution.

---

## Customer Interviews agent

### Primary source — *Talking to Humans*
- **Talking to Humans: Success Starts with Understanding Your Customers** —
  by **Giff Constable**, with **Frank Rimalovski** (illustrations by **Tom
  Fishburne**).
- The agent's method and templates are distilled from the book and the authors'
  **free companion materials**, preserved in
  `methods/customer-interviews/materials/`:
  - *10 Tips to Remember*
  - *Assumptions Exercise*
  - *Teaching Exercises* — including the "cold-call the expert" drill contributed
    by **Dean Chang**, Associate VP of Entrepreneurship, University of Maryland.
- Site: **talkingtohumans.com**
- These materials are the authors' work, included here for reference and
  attribution; all rights remain with them.

### The Product Death Cycle
- **David Bland** — the *Product Death Cycle* (2014: no one uses our
  product → ask customers what features are missing → build them →
  repeat) and its AI-era update (ask AI what features are missing).
- **Melissa Perri** — featured the original in *Escaping the Build Trap*
  (O'Reilly, 2018); her LinkedIn post on the updated cycle ("it's the
  build trap with a shiny AI wrapper... the solution isn't better AI
  features, it's better customer discovery") is preserved at
  `methods/customer-interviews/materials/MelissaPerri-ProductDeathCycle-AIVersion-LinkedIn.pdf`
  with a transcription under `materials/extracted/`. Grounds principle
  29 and the system rule that agent output is never customer evidence.

### Intellectual lineage
- **Steve Blank** — Customer Development and "get out of the building"
  (*The Four Steps to the Epiphany*, *The Startup Owner's Manual*).
- **Eric Ries** — *The Lean Startup* (validated learning; build–measure–learn).
- **Rob Fitzpatrick** — *The Mom Test* (how to ask good interview questions).

### Research & insight — Fluxx "Experiments in Design" (via Magnetic Notes)
- **"First Principles of Customer Research — How to quickly find out what you
  really need to know"** — **sketchnotes by Stefano Bellucci Sessa**
  (@bs_stefano), *Magnetic Notes* (Medium), 18 July 2016 —
  https://medium.com/magnetic/research-and-insights-4fb85003edb4
  A recap of the Fluxx **"Experiments in Design"** meetup. The post is a "1 min
  read" whose substance is a hand-drawn **sketchnote**; its content is
  transcribed in
  `methods/customer-interviews/materials/extracted/magnetic-first-principles.txt`
  (source PDF alongside) and folded into
  `methods/customer-interviews/research-and-insight.md`:
  - **Rupert Tebb** (@rupert_Tebb) — 8 principles of effective research.
  - **Richard Edgley** (@Richard_Edgley) — 6 criteria for a good insight.
  - **Alice Wilkie** (@Alice_Wilkie) — Dubai-bank case study and the
    "We believe / To verify / Built / Measured / Found out" experiment format.

---

## ODI agents (odi-interviewer, odi-outcome-editor, odi-survey-builder, odi-data-scientist)

### Primary source — Outcome-Driven Innovation
- **Outcome-Driven Innovation (ODI)** and its core constructs — markets
  defined as *job executor + job-to-be-done*, desired outcome statements, the
  opportunity algorithm (`Importance + max(Importance − Satisfaction, 0)`),
  needs-based segmentation, and the growth-strategy framework — were created
  by **Tony (Anthony W.) Ulwick** at **Strategyn**.
- The **Universal Job Map** (the 8 job steps) comes from **Lance A.
  Bettencourt & Anthony W. Ulwick**, "The Customer-Centered Innovation Map,"
  *Harvard Business Review*, May 2008.
- Key resources the method docs distill:
  - Strategyn — ODI process: https://strategyn.com/outcome-driven-innovation-process/
  - Strategyn — ODI overview: https://strategyn.com/outcome-driven-innovation/
  - Tony Ulwick, "Outcome-Driven Innovation (ODI) is Jobs-to-be-Done Theory in
    Practice" (Medium): https://jobs-to-be-done.com/outcome-driven-innovation-odi-is-jobs-to-be-done-theory-in-practice-2944c6ebc40e
  - Digital Leadership — ODI guide: https://digitalleadership.com/blog/outcome-driven-innovation/
  - *What Customers Want* — Anthony Ulwick (McGraw-Hill, 2005)
  - *Jobs to be Done: Theory to Practice* — Anthony Ulwick (free PDF at
    jobs-to-be-done-book.com)

### Provenance of these agents
- The four ODI agents and `methods/odi/` were **ported from
  [Daniel085/Product-Discovery-ODI](https://github.com/Daniel085/Product-Discovery-ODI)**
  (Daniel O'Rorke's prior agent system implementing ODI), restructured to
  this repo's behavior/knowledge architecture: shared knowledge deduplicated
  into single canonical method docs, agents given Claude Code frontmatter,
  and the developer/partner interviewer variant folded into `odi-interviewer`
  as a mode (multi-call discovery, dual-job framing, developer question
  banks).

### Intellectual lineage
- **Clayton Christensen** — popularized Jobs-to-be-Done theory (*The
  Innovator's Solution*, with the "milkshake" framing), which ODI
  operationalizes.

---

## PR/FAQ agent (prfaq)

- **Working Backwards: Insights, Stories, and Secrets from Inside Amazon** —
  **Colin Bryar & Bill Carr** (St. Martin's Press, 2021) — the
  working-backwards process, the PR/FAQ document (press release + FAQ), the
  five customer questions, narratives-over-slides, and the
  single-threaded-leader idea.
- The PR/FAQ practice itself originates at **Amazon**.

## Experimentation agent (experimentation)

- **Trustworthy Online Controlled Experiments: A Practical Guide to A/B
  Testing** — **Ron Kohavi, Diane Tang & Ya Xu** (Cambridge University
  Press, 2020) — OEC, guardrail metrics, sample ratio mismatch, the
  16σ²/δ² sample-size rule of thumb, novelty/primacy effects, the
  peeking/multiple-comparisons discipline, and the
  practical-significance decision framework.
- **Twyman's law** ("any figure that looks interesting or different is
  usually wrong") — attributed to **Tony Twyman** (media research).
- **HiPPO** (Highest Paid Person's Opinion) — popularized by **Avinash
  Kaushik**.

## Metrics agent (metrics)

- **The North Star Playbook** — **John Cutler** and the **Amplitude** team —
  the North Star Framework: NSM criteria, input metrics, the three games
  (attention / transaction / productivity). The "North Star Metric" term was
  popularized by **Sean Ellis** and the growth community.
- **Lean Analytics: Use Data to Build a Better Startup Faster** —
  **Alistair Croll & Benjamin Yoskovitz** (O'Reilly, 2013) — the good-metric
  criteria, vanity vs. actionable metrics, the One Metric That Matters, the
  five stages, business-model archetypes, cohort discipline.
- **AARRR ("pirate metrics")** — **Dave McClure** (500 Startups).
- **Goodhart's law** — **Charles Goodhart**; the common phrasing ("when a
  measure becomes a target, it ceases to be a good measure") is **Marilyn
  Strathern's**.

---

## Shared method — Job Stories (`methods/jtbd/`)

- **Product Institute — "Product Management Foundations"**, Unit 4
  ("Identifying the Problem"), Lesson 4.2 *Jobs to Be Done* — the
  JTBD-vs-personas framing, the job-story template ("When I am…, I want
  to…, so I can…"), the wishlist worked example, and the user-story →
  job-story practice exercise. Source worksheet preserved at
  `methods/jtbd/materials/ProductInstitute-PMFoundations-L4.2-JobsToBeDone.pdf`
  and remains Product Institute's property. Product Institute was founded
  by **Melissa Perri**.
- **Job Stories** were developed at **Intercom** and articulated by **Alan
  Klement** ("Replacing the User Story with the Job Story," 2013) — replace
  the persona with the **situation**; context predicts behavior better than
  attributes.
- **User stories** originate with **Kent Beck** (Extreme Programming) as
  placeholders for conversations about why users need something; the
  "As a…, I want…, so that…" template comes from the **Connextra** team
  (2001). The job-story critique targets the template's drift into
  mini-requirements, not Beck's original intent.
- JTBD theory lineage: **Clayton Christensen**; **Tony Ulwick** (see the
  ODI section above).

---

## Opportunity Sizing agent (opportunity-sizing)

Grounded in a research pass over investor, analyst, consulting and
founder practice (`reports/Market sizing expert methods.md`, with its
notes under `research_notes/`). Pages preserved as PDFs with
transcriptions under `methods/sizing/materials/` remain their authors'
property.

- **Bill Gurley** — *"How to Miss By a Mile: An Alternative Look at
  Uber's Potential Market Size"*, Above the Crowd, 11 Jul 2014 — the
  canonical bottom-up, market-expanding rebuild: "this cannot be
  yesterday's market"; the San Francisco ratio; price elasticity and
  local network effects; car-ownership substitution; the scenario math.
- **Aswath Damodaran** (NYU Stern) — *Musings on Markets*: *"A
  Disruptive Cab Ride to Riches: The Uber Payoff"* (Jun 2014),
  *"Possible, Plausible and Probable: Big markets and Network effects"*
  (Jul 2014), *"On the Uber Rollercoaster"* (Oct 2015), *"The Market is
  Huge! Revisiting the Big Market Delusion"* (Dec 2019); the Uber
  valuation deck (Sept 2015: the ladder of nested market definitions,
  share by network-effect mechanism) and *"Insights on VC pricing:
  lessons from Uber, WeWork and Peloton"* (Sept 2019: the possible /
  plausible / probable test and overreach / expanded / constrained
  TAM). **Bradford Cornell & Aswath Damodaran**, *"The Big Market
  Delusion: Valuation and Investment Implications"*, *Financial
  Analysts Journal* 76(2), 2020 (SSRN 2016) — the aggregation test;
  paywalled, cited via the abstract.
- **a16z** — *"16 More Startup Metrics"*, 23 Sep 2015 — "we like seeing
  a bottoms-up analysis"; "why 40%?"; don't game the TAM.
- **Pear VC** — *"Market Sizing Guide"*, 3 Aug 2021 — customers × ARPA;
  top-down only to sanity-check; the 10–30% value-capture heuristic.
- **Christoph Janz** (Point Nine) — *"Five ways to build a $100
  million business"*, The Angel VC, 5 Oct 2014 — the elephants / deer /
  rabbits / mice / flies ladder and its funnel multipliers.
- **Jason Lemkin** (SaaStr) — the "believable path to $100M in seven
  years" rule and "the market size number matters far less than how
  you calculated it". Cited, not preserved.
- **Sequoia Capital** — the business-plan template's "calculate the TAM
  (top down), SAM (bottoms up) and SOM", the likely origin of the
  show-both convention. Cited.
- **StrategyCase** (a former McKinsey consultant) — *"Market Sizing
  Questions: 25 Examples With Worked Answers"* (2023, updated 2026) —
  the six-step routine, the structure menu, "round aggressively",
  "never pull a number from thin air without a one-line
  justification", the order-of-magnitude / 25% yardstick. **Barbara
  Minto** — MECE (see the Segmentation section).
- **Stanford Byers Center for Biodesign** — *"Top-Down and Bottom-Up
  Market Sizing Example"* (Biodesign guide, 2022) — divergence between
  the routes as a healthy reality check.
- **Lightspeed Venture Partners** (Sebastian Duesterhoeft) — *"A Total
  Addressable Market (TAM) Masterclass"* — analyst reports as a red
  flag; ratio benchmarks; the fund-return test.
- **Jared Sleeper** (Matrix Partners) — *"Calculating TAM"*,
  forEntrepreneurs (**David Skok**) — top-down, bottom-up and "value
  theory".
- **Steve Blank** — *"Market Definition — It's the Front End of
  Customer Discovery"* (4 Nov 2021, with **Tony Ulwick**'s market
  definition) and *"Death By Revenue Plan"* (16 Feb 2010) — market as
  job executors + job; the four market types and the revenue curve.
- **Douglas W. Hubbard** — *How to Measure Anything* (Wiley, 2007 /
  2010 / 2014) — calibrated 90% intervals, the equivalent bet, the Rule
  of Five, Monte Carlo, measurement inversion; cited via public
  summaries. **Craig R. M. McKenzie, Michael J. Liersch & Ilan Yaniv**
  (*Organizational Behavior and Human Decision Processes*, 2008) —
  overprecision of judgmental intervals. **Donald G. MacGregor & J.
  Scott Armstrong** (1994) — when judgmental decomposition helps.
  **Lawrence Weinstein & John A. Adam** — *Guesstimation* (Princeton,
  2008). **Philip Tetlock & Dan Gardner** — *Superforecasting* (2015):
  outside view first, small updates, name what would change your mind.
- **Frank M. Bass** — *"A New Product Growth for Model Consumer
  Durables"*, *Management Science* 15(5), 1969; **Vijay Mahajan, Eitan
  Muller & Frank M. Bass** (*Marketing Science*, 1995) — the diffusion
  model and the p ≈ 0.03, q ≈ 0.38 defaults. Cited.
- **Madhavan Ramanujam & Georg Tacke** — *Monetizing Innovation*
  (Wiley, 2016) — willingness to pay early. **Peter van Westendorp**
  (price sensitivity meter, 1976) and **André Gabor & Clive Granger**
  (1966) — the two price-research methods as commonly described. Cited.
- **Ozzie Gooen** — Guesstimate and Squiggle (Monte Carlo tools), cited.
- **Uber Technologies** — Form S-1 (Apr 2019) and FY2023–FY2025 results;
  **Ben Thompson** (Stratechery) on the S-1's TAM; **New Constructs**
  on Snowflake's implied share. Cited, not preserved.
- Investors quoted in the research report via TechCrunch and their own
  sites — **Jahanvi Sardana** (Index), **Aydin Senkut** (Felicis),
  **Deena Shakir** (Lux), **Jomayra Herrera** (Reach), **Rotem Shacham**
  (PSG), **Alex Iskold**, **Octopus Ventures**, **Underscore VC**,
  **Dreamit**, **Pegasus**' **Reichert** — cited, not preserved.
- Official statistical agencies — **US Census Bureau** (SUSB, CBP,
  Nonemployer Statistics, Economic Census, ACS), **US Bureau of Labor
  Statistics** (OEWS), **Eurostat** (SBS), **ONS**, **Statistics
  Canada**, **OECD**, **World Bank**; **SEC EDGAR** XBRL APIs.
- The definitions-by-exclusion table, the market-type consequences,
  the five-step bottom-up build, the reconciliation tolerance, the
  "simplest PM version" of Bass, the register, model and summary
  templates, the B2B example, the plug-in table and the anti-pattern
  checks are **this repo's operational extension**, marked as such in
  the method doc; the research report records which rules are
  published standards and which are syntheses.

---

## Shared method — Segmentation (`methods/jtbd/`)

- **Product Institute** (founded by **Melissa Perri**) — *Product
  Management Foundations*, the segmentation lesson: segment by what
  matters to the business (product usage, size of business,
  geography, industry, experience); follow the money (who buys and
  stays, who doesn't); avoid segmentations that don't tie back to the
  problem being solved; a useful segmentation is MECE. Licensed course
  material — **paraphrased from Daniel O'Rorke's notes; nothing
  quoted; the course's teacher-segmentation exercise not reproduced.**
- **Melissa Perri** — the five questions she asks when analyzing usage
  data (usage patterns vs. success metrics; segments with different
  outcomes; the behaviours of the most successful users; the biggest
  gap between current and desired behaviour; the effect on key
  business metrics), relayed in **Daniel O'Rorke's** notes from her
  teaching — **paraphrased; nothing quoted.**
- **Barbara Minto** — *The Pyramid Principle* (Minto International,
  1987; Pearson eds.) — MECE (mutually exclusive, collectively
  exhaustive), as practised at McKinsey. Cited, not reproduced.
- **Tony Ulwick** / **Strategyn** — needs-based segmentation and
  "demographics describe segments; they never define them" (see the
  ODI section above); **Alan Klement** — job stories, situation over
  attributes (see the Job Stories section).
- The scope rule, the define-by-behaviour / describe-by-attribute
  procedure, the attribute test, the template, the checks, the tells
  and the worked example are **this repo's operational extension**,
  marked as such in the method doc.

---

## Shared method — Requirements Are Hypotheses (`methods/jtbd/`)

- **Marty Cagan**, "Requirements Are Not," **Silicon Valley Product Group
  (SVPG)** — https://svpg.com/requirements-are-not/ — customer
  "requirements" as hypotheses about unstated problems, stakeholder
  "requirements" as personal theories, form/function intertwined (the
  waterfall inversion), the ingredient-substitution analogy, and the
  closing standard ("our only real requirement is to discover product
  solutions that work well for our users, our customers and our business").
- The three-bin **intake classification** (true constraint / stakeholder
  theory / customer solution-hypothesis) is **this repo's operational
  extension** of Cagan's argument, marked as such in the method doc —
  Cagan's article itself draws no constraint exception.
- Broader lineage: Cagan's *INSPIRED* and *EMPOWERED* (SVPG) — teams given
  problems to solve rather than features to build.

---

## Ideation agent (ideation)

- **Primary source:** the **`product-brainstorming`** skill from
  Anthropic's **`product-management`** plugin (public
  `knowledge-work-plugins` marketplace) — the four modes, session rhythm,
  ideation techniques, provocation questions, anti-patterns, and the
  thinking-partner register. Retrieved 2026-09-10 from
  https://github.com/anthropics/knowledge-work-plugins (commit
  `1f1a239e`), licensed **Apache License 2.0**; no individual author
  listed. Verbatim copy preserved at
  `methods/ideation/materials/product-brainstorming-SKILL.md`.
- **Framework lineage:** How Might We (**IDEO** / **Stanford d.school**);
  SCAMPER (**Bob Eberle**); the OODA loop (**John Boyd**); reverse
  brainstorming and first-principles decomposition (common practice);
  **Teresa Torres** for opportunity solution trees (*Continuous Discovery
  Habits*) — cross-referenced, not distilled, pending the README roadmap
  item.
- The **landscape-scan protocol** and the shared **assumption ledger**
  (`methods/customer-interviews/assumption-ledger.md`) are this repo's
  additions: the ledger's six categories come from the skill; its ranking
  rule (impact × uncertainty) from *Talking to Humans* (see above).

---

## Problem Selection agent (problem-selection)

- **"How to pick the right problem"** — the two criteria (Customer Signal:
  pain and breadth; Business Alignment: fit to goals), the acquisition
  flip (breadth becomes the business criterion), the internal-tools
  reading (employee suffering; time saved and errors avoided for others),
  and the four-step execution framework — JTBD problem statement; evidence
  table with *Source / Type / Confidence in evidence (1–5) / Findings*
  across qualitative, quantitative and operational sources; pattern check
  (convergence, conflicting signals); validation verdict *Yes / Not yet /
  Probably not*. Provided as **Daniel O'Rorke's** working notes
  (2026-09-18); original lineage unrecorded — if these derive from a
  published course or article, cite it here and in
  `methods/problem-selection/picking-the-right-problem.md`.
- **Affinity diagram / K-J Method** — created by Japanese anthropologist
  **Jiro Kawakita** (1960s). Distilled from **ASQ (American Society for
  Quality)**, *"What is an Affinity Diagram? (K-J Method)"*, Learn About
  Quality / Quality Resources — adapted from ***The Quality Toolbox*,
  Second Edition** (ASQ Quality Press). Source page preserved at
  `methods/problem-selection/materials/ASQ-WhatIsAnAffinityDiagram-KJMethod.pdf`
  with a transcription under `materials/extracted/`; it remains ASQ's
  property.
- The scoring anchors, per-row confidence anchors, verdict rules, ranking
  table, and the text-mode affinity protocol (source tags,
  group-before-name, distinct-source counts) are **this repo's
  operational extensions**, marked as such in the method docs.
- Shared lineage: job stories (Product Institute / Klement, above);
  requirements-as-hypotheses (Cagan, above); evidence tiers (ODI
  multi-call discovery, above).
- **Knowledge-gap assessment** — **Product Institute** (founded by
  **Melissa Perri**), *Product Management Foundations*: the five
  confidence areas at the close of problem validation (problem
  definition, user behavior, competitive landscape, technical
  constraints, business impact) and the three next moves (customer
  interviews, problem analysis, competitive analysis). Licensed course
  material — **paraphrased from Daniel O'Rorke's notes; nothing
  quoted.** The 1–5 anchors, the two added routes, decision rules,
  teardown table and exit criteria are this repo's extension.
- **Root-cause analysis** — public canon, no source document preserved:
  **5 Whys** (Toyota Production System; **Sakichi Toyoda**, **Taiichi
  Ohno**); the **cause-and-effect / fishbone diagram** (**Kaoru
  Ishikawa**, *Guide to Quality Control*, 1968); the **interrelationship
  digraph** (seven management and planning tools, JUSE, as catalogued in
  **ASQ**'s *The Quality Toolbox*, **Nancy R. Tague**). The
  product-specific categories, evidence-per-why rule and gate are this
  repo's extension.

---

## Lean Experiments agent (lean-experiments)

- **Tristan Kromer** — *"Wizard of Oz Prototyping vs. Concierge Test: The
  Key Difference"*, Kromatic blog (originally Grasshopper Herder), 15 Sep
  2015 — the user-awareness distinction, generative vs. evaluative, the
  human-presence bias; with **Roger L. Cauvin**'s comment-thread point
  that concierge tests also uncover problems, and Kromer's prerequisites
  for one. Kromer credits **J. F. Kelley** (1975) for the Wizard of Oz
  technique and cites Aardvark, CardMunch, Wealthfront and Food on the
  Table (**Manuel Rosso**, spelled "Russo" in the article). Source page preserved at
  `methods/lean-experiments/materials/Kromatic-WizardOfOzVsConcierge.pdf`.
- **Wikipedia contributors** — *"Wizard of Oz experiment"*, Wikipedia,
  retrieved 2026-09-22; text under **CC BY-SA 4.0**, wikitext preserved
  at `methods/lean-experiments/materials/extracted/wikipedia-wizard-of-oz-experiment.txt`.
  Credits the method to **John F. Kelley** (Johns Hopkins, c. 1980), with
  precursors **W. Randolph Ford** (1975), **Allen Munro & Don Norman**
  (Xerox PARC, c. 1975) and **Nigel Cross** (1960s); the name is from
  **L. Frank Baum**'s novel.
- **Eugene Kim** — *"The inside story of how Amazon created Echo, the
  next billion-dollar business no one saw coming"*, Business Insider,
  2 Apr 2016 — the Amazon Echo / Alexa Wizard-of-Oz tests, **Jeff
  Bezos**'s reported one-second latency directive (**Dave Limp** does
  not recall the figure), and the music-as-hook finding. Article
  preserved at
  `methods/lean-experiments/materials/BusinessInsider-InsideStoryAmazonEcho-Kim2016.pdf`
  with a transcription under `materials/extracted/`; it remains Business
  Insider's property.
- **Melissa Perri** — *"The Product Kata"*, melissaperri.com, 22 Jul 2015
  (later part of *Escaping the Build Trap*, O'Reilly 2018) — adapting
  **Mike Rother**'s *Toyota Kata* (McGraw-Hill, 2009; improvement kata
  and coaching kata) via **Håkan Forss**'s Kanban Kata. Source page at
  `methods/lean-experiments/materials/MelissaPerri-TheProductKata.pdf`.
  The seven-step summary in the method doc is **Daniel O'Rorke's**.
- **Chris Matts** (*The IT Risk Manager*) — *"MVP considered harmful.
  Introducing the MVI."*, 26 Mar 2016 — MVP vs. minimum viable
  investment, the "minimum viable rewrite" anti-pattern, instrument
  first; with **Gus Power**'s "minimum sustainable product" comment.
  Source page at
  `methods/lean-experiments/materials/ITRiskManager-MVPConsideredHarmful-MVI.pdf`.
- **Karen von Schmieden** — *"Feeling in Control: Bank of America Helps
  Customers to 'Keep the Change'"*, thisisdesignthinking.net — the case
  (IDEO ethnography → 80 concepts → cartoon-video concept test with 1,600
  respondents → iteration), quoting **Tim Brown** and **Sally Madsen**
  (IDEO) and **Faith Tucker** (Bank of America). Source page at
  `methods/lean-experiments/materials/ThisIsDesignThinking-BankOfAmerica-KeepTheChange.pdf`.
- **Tomer London** (co-founder & CPO, Gusto) with **Melissa Perri** —
  *Product Thinking* podcast, episode 200, "Building a Minimal Lovable
  Product", Produx Labs, 4 Dec 2024 (post by **Stephanie Rogers**) — the
  minimum lovable product, "what are we trying to prove", the manual
  back-end with an automation vision, the unit-economics rule, the
  functional / intuitive / delightful bar, killing QSEHRA. Source page at
  `methods/lean-experiments/materials/ProduxLabs-Ep200-MinimalLovableProduct-TomerLondon.pdf`.
- **Paul Graham** — *"Do Things That Don't Scale"* (2013): the Airbnb
  photographers example; the manual-Groupon example is common lore of
  the same lesson. **Eric Ries** — *The Lean Startup* (MVP, concierge
  MVP). Not reproduced here.
- **Wikipedia contributors** — *"Minimum viable product"*, Wikipedia,
  retrieved 2026-09-24; text under **CC BY-SA 4.0**, wikitext preserved
  at `methods/lean-experiments/materials/extracted/wikipedia-minimum-viable-product.txt`.
  Credits the term to **Frank Robinson** (2001), popularized by **Steve
  Blank** and **Eric Ries** (*Minimum Viable Product: a guide*, 2009;
  *The Lean Startup*).
- **The eight assumption questions** (problem for us; target audience;
  opportunity size; alternatives and market; constraints; go-to-market;
  strategic KPIs; critical success factors), the "fastest path to
  insight" framing, the two MVP failure modes, the four
  learning-alignment questions and the four maxims are **Daniel
  O'Rorke's** working notes.
- The feature-request breakdown protocol and its null-result rule were
  **informed by licensed training material that is deliberately not
  reproduced or paraphrased** anywhere in this repository.
- **Patrick Vlaskovits** — *"Henry Ford, Innovation, and That 'Faster
  Horse' Quote"*, Harvard Business Review, 29 Aug 2011 — the quote is
  unattested before c. 2001–02; **Snopes** (23 Feb 2025) independently
  found no proof Ford said it. Cited, not reproduced.
- **Nielsen Norman Group** — *"UX Prototypes: Low Fidelity vs. High
  Fidelity"* — prototype fidelity on three axes (visual, content,
  interactivity) and when each level pays. Cited, not reproduced.
- **Stripe**'s API-first origin — cited as common knowledge from the
  founders' public accounts; no source preserved.

---

## Solution Options agent (solution-options)

- **The option template** (Title · Alignment · Hypothesis — *We believe
  building ____ will satisfy the job [JTBD] for [customer segment] and
  result in [KPI]* · Problem · Behavior change · In scope · Out of scope
  · Dependencies · Risks / unknowns · Success metrics & outcomes ·
  Iteration plan) is **Daniel O'Rorke's**, in his own words; its
  structure is similar to the option template taught by **Product
  Institute** (founded by **Melissa Perri**), acknowledged as lineage
  and not reproduced. The "minimum feature set is v1.0, not the MVP;
  use cost of delay to decide what to postpone" rule is likewise
  **Daniel O'Rorke's** working note.
- **Donald G. Reinertsen** — *The Principles of Product Development
  Flow: Second Generation Lean Product Development* (Celeritas, 2009) —
  cost of delay as the economic basis for scheduling decisions; the
  urgency-profile shapes as commonly applied from his work.
- **Joshua J. Arnold** (with **Özlem Yüce**) — *Black Swan Farming*:
  **CD3**, cost of delay divided by duration
  (https://blackswanfarming.com/cost-of-delay-divided-by-duration/);
  the same idea appears as WSJF in SAFe (**Dean Leffingwell**). Three
  articles preserved at `methods/lean-experiments/materials/`:
  *"Understanding Value"* (Increase Revenue · Protect Revenue · Reduce
  Costs · Avoid Costs), *"Urgency Profiles"* (four profiles; external
  deadlines as zero cost of delay until the latest start date), and
  *"Qualitative Cost of Delay"* (Killer / Bonus / Meh × ASAP / Soon /
  Whenever; cost of delay as a rate; dates shift urgency). They remain
  the author's property.
- **Melissa Perri** — *"Prioritization Shouldn't Be Hard"*, The Produx
  Labs (Medium), 31 Oct 2019 — prioritization needs a strategy and data;
  scoring games and stakeholder averages are beginner tools and
  consensus, not leadership; cost of delay backs decisions into dollars.
  Preserved at
  `methods/lean-experiments/materials/MelissaPerri-PrioritizationShouldntBeHard-2019.pdf`
  with a transcription under `materials/extracted/`.
- **Gus Power** — "minimum sustainable product" (see the MVI entry
  above).
- **Jared M. Spool** (Center Centre / UIE) — *"Understanding the Kano
  Model – A Tool for Sophisticated Designers"*, UX Articles by Center
  Centre, 7 Nov 2018 — performance payoff, basic expectations,
  excitement generators, and the migration of delighters into basics;
  after **Noriaki Kano**'s model of customer satisfaction (1984).
  Preserved at
  `methods/lean-experiments/materials/CenterCentre-Spool-UnderstandingTheKanoModel-2018.pdf`
  with a transcription under `materials/extracted/`; it remains the
  author's property.
- **Product Institute** — the recommendation against RICE (quantitative
  in appearance, subjective in inputs), relayed in **Daniel O'Rorke**'s
  notes and paraphrased, not quoted.
- The field guidance and tells, the comparison table, the five feature
  classes, the Kano-to-class mapping, the postponement rules, both
  templates and the anti-patterns are **this repo's operational
  extensions**.
- The "trying to prove" chooser, the catalogue's
  prerequisite/measure/bias/stop structure, the MVP–MLP–MVI table, the
  experiment card, the assumption-chain template, the MVP card, the
  kata record template and the anti-patterns are **this repo's
  operational extensions**.

---

## Shared method — Value Proposition (`methods/jtbd/`)

- **Strategyzer AG** — *The Value Proposition Canvas* (customer jobs /
  pains / gains ↔ products & services / pain relievers / gain creators,
  with trigger questions), strategyzer.com; from **Alexander Osterwalder,
  Yves Pigneur, Greg Bernarda & Alan Smith**, *Value Proposition Design*
  (Wiley, 2014). The 2-page canvas PDF is preserved at
  `methods/jtbd/materials/Strategyzer-TheValuePropositionCanvas.pdf`
  (copyright Strategyzer AG) with a transcription under
  `materials/extracted/`. Further playbooks:
  https://www.strategyzer.com/playbook-library
- **Product Institute** (founded by **Melissa Perri**) — *Product
  Management Foundations*, the value-proposition lesson: functional +
  emotional jobs → "We [deliver outcome] by [solving key job]". Licensed
  course material — **paraphrased only; nothing quoted and the course's
  example not reproduced.**
- The tells table, text template and fit-to-agents mapping are this
  repo's operational extension.

---

## Shared method — Product Strategy (`methods/strategy/`)

- **Melissa Perri** — *Escaping the Build Trap: How Effective Product
  Management Creates Real Value* (O'Reilly, 2018): the strategy part of
  the book — strategy as a framework rather than a plan, the strategic
  gaps, strategy deployment (with OKRs, Hoshin Kanri and mission
  command as its kin), the four-level framework (vision · strategic
  intents · product initiatives · options), the Product Kata as the
  process that runs it, and the living roadmap's fields. A published
  book — **paraphrased; nothing quoted; the Marquetly example not
  reproduced.**
- **Melissa Perri** — *"What is Good Product Strategy?"*,
  melissaperri.com, 14 Jul 2016 — the pre-book product-strategy
  canvas (vision · challenge · target condition · current state), her
  definition of product strategy, strategy as something *uncovered*
  through experimentation rather than dictated, the ownership of each
  level, the Uber driver-onboarding example, and the "Unified Field
  Theory" pointer to **Bill Costantino** and **Mike Rother**. Preserved
  at `methods/strategy/materials/MelissaPerri-WhatIsGoodProductStrategy-2016.pdf`
  with a transcription under `materials/extracted/`; it remains the
  author's property.
- **Stephen Bungay** — *The Art of Action: How Leaders Close the Gaps
  between Plans, Actions and Results* (Nicholas Brealey, 2011): the
  knowledge, alignment and effects gaps, their mission-command
  remedies (limit direction to the essential intent; let each level
  define what it must do; give people freedom to adjust in line with
  the intent), and the definition of strategy as a deployable
  decision-making framework that Perri adopts. Cited via Perri; not
  reproduced.
- **Mike Rother** — the *Toyota Kata* website (hosted at the
  University of Michigan): the pages *The Improvement Kata* and *The
  Coaching Kata* and the *5Q Card* deck, preserved at
  `methods/strategy/materials/ToyotaKata-Rother-TheImprovementKata.pdf`,
  `…-TheCoachingKata.pdf` and `…-5Q_Card.pdf` with transcriptions
  under `materials/extracted/`. The four-step Improvement Kata,
  scientific thinking as a practised habit, the Starter Kata idea, the
  five coaching questions with the back-of-card reflection (planned ·
  expected · actually happened · learned), the coaching-cycle rules
  (daily, ≤ 20 minutes, clarifying questions, the threshold of
  knowledge, the second coach) and the storyboard's six fields are
  his; the books are *Toyota Kata* (McGraw-Hill, 2009) and *The Toyota
  Kata Practice Guide* (McGraw-Hill, 2017). The materials remain his
  property.
- **Kazuo Ichijo & Ikujiro Nonaka** — *Knowledge Creation and
  Management: New Challenges for Managers* (Oxford University Press,
  2006), p. 25 — the excerpt on a firm-specific *kata* as a knowledge
  asset, quoted on Rother's Improvement Kata page and transcribed with
  it; **Richard R. Nelson & Sidney G. Winter** (1982) on routines, as
  it cites them.
- **Jim Huntzinger** (Lean Frontiers) and **Ralph Waldo Emerson** —
  the two epigraphs on Rother's page, transcribed with it.
- **Jim Collins** — *"Good to Great"*, Fast Company, October 2001, as
  republished at jimcollins.com (from *Good to Great: Why Some
  Companies Make the Leap… and Others Don't*, HarperBusiness, 2001) —
  the flywheel effect and the doom loop, the stop-doing list, the
  seven change myths and the no-miracle-moment finding; preserved at
  `methods/strategy/materials/JimCollins-GoodToGreat-FastCompany-2001.pdf`
  with a transcription under `materials/extracted/`; copyright Jim
  Collins. The hedgehog concept, Level 5 leadership and "first who,
  then what" are acknowledged and not distilled.
- **Brooke Carter** — *"How Product Managers Can Effectively Quantify
  Business Impact"*, Built In, 8 Jan 2021: the metric vocabulary
  (North Star, OKR, goal, signal, primary metric, hypothesis, support
  data), the revenue-impact formula, the four measurement oversights
  and the "two plus two equals three" caution. Preserved at
  `methods/strategy/materials/BuiltIn-HowPMsQuantifyBusinessImpact-Carter-2021.pdf`
  with a transcription; it remains the author's and Built In's
  property.
- **Allie Beazell** — *"The cost-benefit analysis of internal
  tools"*, Retool Blog, 24 Nov 2020: direct cost as engineer hourly pay
  × build-and-maintain hours, the internal-tools time benchmarks from
  Retool's 2020 survey, and the value side (united systems, fewer
  errors, security, time freed), with the LeadGenius (**Adam Louie**),
  Neo4j (**Mike Brophy**) and Noble Schools (**Moon Lee**) cases.
  Vendor content, preserved at
  `methods/strategy/materials/Retool-CostBenefitAnalysisOfInternalTools-Beazell-2020.pdf`
  with a transcription; it remains Retool's property.
- **Jonathan Kim** — *"Becoming product-led: How to connect product
  decisions to revenue"*, Appcues blog, 28 May 2026: SaaS revenue as a
  system of four levers, the Rule of 40, net revenue retention,
  revenue vs. logo churn, product-qualified leads, time-to-value, and
  shared product-and-revenue metrics. Vendor content, preserved at
  `methods/strategy/materials/Appcues-BecomingProductLed-Kim-2026.pdf`
  with a transcription; the product-marketing sections are not
  distilled; it remains Appcues's property.
- **Mural** — *"How to create a meaningful product vision"*, Mural
  blog, 24 Oct 2025: the vision-statement definition and qualities,
  and the statement format adapted from **Geoffrey Moore**'s
  positioning template (*Crossing the Chasm*, HarperBusiness, 1991).
  Vendor content, preserved at
  `methods/strategy/materials/Mural-HowToCreateAMeaningfulProductVision-2025.pdf`
  with a transcription; it remains Mural's property.
- The five marks of a **strong product initiative** (clear connection
  to the current-state analysis · quantified business value ·
  evidence-based reasoning · defined success metrics · measurable
  customer outcomes), the focus rule and the periodic-update rule are
  **Daniel O'Rorke's** working notes after **Product Institute**'s
  strategy lessons, paraphrased; nothing quoted.
- **HubSpot** — *"Why it's Time to Replace your Funnel with a
  Flywheel"* (hubspot.com/flywheel): the flywheel growth model
  (attract · engage · delight; force and friction), crediting **James
  Watt** for the mechanism. Cited, not preserved.
- **Cameron Deatsch** — *"10 Lessons on using the Flywheel Effect to
  Grow Your Business"*, Inside Atlassian, 31 Aug 2021: the enterprise
  trap, "treat human interaction as a bug", active users as the
  leading signal. Cited, not preserved.
- The four-step **Product Kata summary** — *understand the direction
  (get clear on the strategy set by the level above) · analyze the
  current state · set the next goal (the product initiatives that
  achieve the company and portfolio goals) · execute or deploy (run
  experiments, deliver solutions, or communicate strategy)* — is
  **Daniel O'Rorke's**, after Perri. Likewise the **product strategy
  memo** (a two-to-three-page document: product vision · current
  state · product initiatives), the six areas of a current-state
  analysis (current performance · user segments · pain points and
  opportunities · strengths and weaknesses · competitive positioning ·
  market and technology trends) and the rule that there won't be
  perfect information — note the knowledge gaps and move on — are his
  working notes after **Product Institute**'s strategy lessons,
  paraphrased; nothing quoted.
- The clause-by-clause tests of a strategy, the gap table's
  wrong-and-right fixes, the stack rules, the cadence-by-level table,
  the strategy stack and direction ladder templates, the plug-in table,
  the anti-patterns and the worked example are **this repo's
  operational extension**, marked as such in the method doc.

---

## Methodology evaluations (`docs/methodology-evaluations/`)

- The 25-criterion evaluation **rubric** is **Daniel O'Rorke's** own;
  recorded in `rubric.md` for reuse across methodologies.
- **Design Thinking** was evaluated against the **Stanford d.school**'s
  published materials — *An Introduction to Design Thinking: Process Guide*
  and the *Bootcamp Bootleg* / *Design Thinking Bootleg* method cards — with
  the desirability / feasibility / viability lens from **Tim Brown / IDEO**.
  No d.school material is reproduced in this repo.
- **Talking to Humans** and **ODI** were evaluated against the sources
  already credited above (Constable & Rimalovski; Ulwick / Strategyn;
  Bettencourt & Ulwick).
- **JTBD (qualitative school)** was evaluated against **Clayton
  Christensen** (*The Innovator's Solution*; *Competing Against Luck*, with
  Taddy Hall, Karen Dillon & David S. Duncan), **Bob Moesta** and the
  **Re-Wired Group** (switch/timeline interviews; the four forces of
  progress), **Alan Klement** (job stories), and **Jim Kalbach** (*The Jobs
  to be Done Playbook*).

---

## System design sources

- **Anthropic**, *Building Effective Agents* (Dec 2024) — the
  workflow-vs-agent distinction, the pattern vocabulary (routing, prompt
  chaining, parallelization, orchestrator-workers,
  evaluator-optimizer), and the agent-computer-interface advice; used to
  name what this system is and isn't (`docs/how-it-works.md`).
- **Anthropic**, *How we built our multi-agent research system* (Jun
  2025) — delegation briefs ("teach the orchestrator how to delegate"),
  effort scaling, external memory and lightweight references, and the
  small-sample, rubric-plus-human evaluation approach behind `evals/`.
- **Anthropic**, *Multiagent orchestration* (Managed Agents
  documentation) — the shared-filesystem, isolated-context model and the
  specialization / parallelization / escalation patterns, read as
  confirmation of the initiative-folder design.

## How attribution works here
- Every `methods/<topic>/` doc cites its sources in a **Sources & materials**
  section.
- Raw third-party materials live under `methods/<topic>/materials/` and remain
  the property of their authors.
- When you add a new source, cite it in the relevant method doc **and** add it
  here.

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

## Methodology evaluations (`docs/methodology-evaluations/`)

- The 25-criterion evaluation **rubric** is **Daniel O'Rorke's** own;
  recorded in `rubric.md` for reuse across methodologies.
- **Design Thinking** was evaluated against the **Stanford d.school**'s
  published materials — *An Introduction to Design Thinking: Process Guide*
  and the *Bootcamp Bootleg* / *Design Thinking Bootleg* method cards — with
  the desirability / feasibility / viability lens from **Tim Brown / IDEO**.
  No d.school material is reproduced in this repo.

---

## How attribution works here
- Every `methods/<topic>/` doc cites its sources in a **Sources & materials**
  section.
- Raw third-party materials live under `methods/<topic>/materials/` and remain
  the property of their authors.
- When you add a new source, cite it in the relevant method doc **and** add it
  here.

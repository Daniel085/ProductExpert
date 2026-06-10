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

## How attribution works here
- Every `methods/<topic>/` doc cites its sources in a **Sources & materials**
  section.
- Raw third-party materials live under `methods/<topic>/materials/` and remain
  the property of their authors.
- When you add a new source, cite it in the relevant method doc **and** add it
  here.

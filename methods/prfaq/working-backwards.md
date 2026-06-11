# Working Backwards & the PR/FAQ — Method Reference

*Distilled from **"Working Backwards: Insights, Stories, and Secrets from
Inside Amazon"** by **Colin Bryar & Bill Carr** (St. Martin's Press, 2021),
and Amazon's publicly documented working-backwards practice. See
[`../../CREDITS.md`](../../CREDITS.md).*

## The idea

**Work backwards from the customer experience, not forwards from the
technology or the org chart.** Before building anything, write the **press
release** announcing the finished product — dated at launch, written for the
customer — plus the **FAQ** that answers the hard questions. Then iterate the
document until the product it describes is worth building. Iterating a
one-page PR costs hours; iterating a product costs quarters.

Two cultural commitments make it work:

1. **Narratives over slides.** Prose forces complete thoughts; bullet points
   hide gaps. The PR/FAQ is read silently at the start of its review meeting,
   then discussed.
2. **The goal is truth, not approval.** A PR/FAQ that convinces the team
   *not* to build is a success — it killed a weak idea at the cheapest
   possible moment. Most PR/FAQs should die; the process is a filter, not a
   pitch deck.

## The five customer questions (the gate)

No drafting until these can be answered — with evidence, not hope:

1. **Who is the customer?**
2. **What is the customer problem or opportunity?**
3. **What is the most important customer benefit?**
4. **How do you know what customers need or want?**
5. **What does the customer experience look like?**

In this repo, question 4 has a concrete answer-shape: cite the discovery
artifacts. Qualitative synthesis (`methods/customer-interviews/`) answers
"who has this problem and why"; ODI opportunity scores (`methods/odi/`)
answer "how important, how underserved, for which segment." A PR/FAQ whose
"how do you know" cites neither is running on assumption — mark it as such.

## The press release (one page, always)

Future-dated, written as if the product just launched. Canonical elements,
in order:

| # | Element | What it does |
|---|---------|--------------|
| 1 | **Heading** | Product name + the customer + the one-line benefit |
| 2 | **Subheading** | One sentence: who it's for and what they get |
| 3 | **Date** | The (future) launch date |
| 4 | **Summary paragraph** | Product + benefit in 3–4 sentences. Assume the reader reads nothing else. |
| 5 | **Problem paragraph** | The customer's problem, told from the *customer's* point of view |
| 6 | **Solution paragraph(s)** | How the product solves it; what the experience feels like |
| 7 | **Company quote** | A (named, hypothetical) spokesperson on why this was built |
| 8 | **Customer quote** | A *believable, specific* hypothetical customer describing the benefit they experienced |
| 9 | **Call to action** | How the customer gets started |

### The quality bar

- **One page.** If it doesn't fit, the thinking isn't done.
- **Customer language** — the "Oprah test": write it the way a trusted
  household voice would explain it to a normal person, not the way an
  engineer would spec it. No internal jargon, no acronyms the customer
  wouldn't know.
- **No marketing superlatives.** "Revolutionary," "seamless," and
  "best-in-class" are claims the customer quote should make *concrete*
  instead ("I used to spend Sunday nights doing X; now I don't").
- **The benefit must be exciting on its own.** If the press release reads as
  boring, the product will be boring — fix the product concept, not the
  adjectives.
- **The customer quote is a design tool.** If you can't write a believable
  human saying it, the benefit isn't real yet.

## The FAQ

Where intellectual honesty lives. Two sections:

### External FAQs (customers and press would ask)
Price, availability, how it works, compatibility, privacy/data handling,
what happens to my existing setup, support. Write the answer the customer
deserves, not the one that's convenient.

### Internal FAQs (stakeholders must ask)
The questions you'd rather not answer go here — *omitting one is the
process's cardinal sin*. The standing bank:

- **Market & customer:** How many customers have this need? How acute is it?
  Will they pay? (Cite Track 1 / Track 2 evidence.) What's the TAM and how
  was it estimated?
- **Economics:** Unit economics / P&L sketch. What does it cost to build,
  sell, and operate? Price point and why? What must be true for this to be a
  business?
- **Feasibility:** What's *hard* about this — technically and
  operationally? What have others tried? What dependencies (internal teams,
  third parties) must exist or cooperate?
- **Strategy:** Why now? Why us? What's the moat when it works? What adjacent
  things does this commit us to?
- **Risk & belief:** What are the top 3 ways this fails? **What would we need
  to believe** for this to be a big success? Which of those beliefs is
  weakest?
- **Measurement:** How will we know it's working? (Success metrics — and the
  counter-metrics that catch us fooling ourselves.)

### Answer discipline

- Every claim is **evidence-cited or flagged `[ASSUMPTION]`** — assumptions
  are legitimate, hidden ones are not.
- The "what we'd need to believe" list is the bridge to testing: its weakest
  entries become hypotheses for experiments (see
  `methods/experimentation/`).
- The measurement answer should name real metrics, not "engagement" —
  defining them well is the metrics method's job (`methods/metrics/`).

## The process

1. **One owner writes.** A document by committee says nothing. (Amazon pairs
   this with the *single-threaded leader* idea: one accountable person whose
   only job this is.)
2. **Review by silent reading.** Distribute at the meeting, everyone reads
   (15–20 min), then feedback — specific, on the document. Senior voices
   weigh in late to avoid anchoring.
3. **Iterate.** Multiple drafts over days or weeks is normal; each cycle
   sharpens the product, not just the prose.
4. **Decide.** Build / kill / park. Killing is a success outcome. Parked
   PR/FAQs keep their evidence trail for the next revisit.

## Templates

### PR skeleton
```
[HEADING: <Product> helps <customer> <benefit>]
[SUBHEADING: one sentence — who it's for, what they get]
[CITY, <future launch date>] —

[SUMMARY: 3–4 sentences. Product, customer, benefit.]

[PROBLEM: the customer's life today, in their words.]

[SOLUTION: what the product does; walk the experience.]

"[COMPANY QUOTE — why we built it]" — <name, title>

"[CUSTOMER QUOTE — specific, believable, benefit-experienced]" — <name, context>

[GETTING STARTED: how to begin.]
```

### Review record
```
Draft N — <date>
Readers: …
Strongest objection raised: …
What changed in response: …
Open internal FAQs still unanswered: …
Verdict this round: iterate / build / kill / park — why:
```

## How this plugs into the system

- **Upstream:** Track 1 synthesis (validated problem, insight statements)
  and Track 2 outputs (opportunity scores, segment profiles, growth
  strategy) are the evidence base for the five questions and the
  market/customer FAQs.
- **Downstream:** the internal FAQ's "what we'd need to believe" feeds the
  **experimentation** agent (riskiest beliefs → tests); the measurement FAQ
  feeds the **metrics** agent (success metrics + counter-metrics).

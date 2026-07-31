# Requirements Are Hypotheses — Method Reference

*Distilled from **Marty Cagan**, "Requirements Are Not," **Silicon Valley
Product Group (SVPG)** — https://svpg.com/requirements-are-not/. The intake
classification at the bottom is **this repo's operational extension**, not
Cagan's. See [`../../CREDITS.md`](../../CREDITS.md).*

> Sibling of [`job-stories.md`](./job-stories.md): job stories catch the
> solution hiding in a *user story*; this doc catches the hypothesis hiding
> in a *"requirement"* — the feature request, the stakeholder mandate, the
> RFP row, the "the business needs" email.

## Cagan's argument

**"Requirements" almost never are.** The word smuggles certainty into what
is actually a guess:

- **Customers** "think they have 'requirements' but really they're just a
  hypothesis on what might solve some probably unstated problem." Customers
  experience problems; they are not designers of solutions — their ask is
  evidence of a need, not a spec for its answer.
- **Stakeholders** have "requirements" that are really **their personal
  theories or assumptions** about what will work. Valuable input; not a
  mandate.
- **Waterfall had it backwards.** Form and function are intertwined: the
  design direction you take will often change the functional
  "requirements." You cannot fully specify *what* before exploring *how* —
  which is why requirements→design→build as a one-way sequence fails.
- **Substitution is usually possible.** Like cooking: "if an ingredient is
  unavailable, you can often get creative and substitute something else…
  It's the result that matters, not our pre-conceptions." When an ask is
  infeasible as stated, the underlying need can usually be served another
  way — infeasibility of the *solution* is not infeasibility of the
  *outcome*.
- **The only real requirement** "is to discover product solutions that work
  well for our users, our customers and our business."

The failure mode this prevents: a team that "gathers requirements" and
builds them faithfully has outsourced its thinking to whoever spoke loudest
— it ships hypotheses at full production cost without ever testing them.

## The de-requirement protocol (repo extension)

When work arrives labeled as a requirement, don't accept or reject it —
**reclassify it**. For each item ask: *who is this from, what problem do
they believe it solves, what's the evidence, and what else could solve it?*
Then sort into three bins:

| Bin | What it really is | What to do |
|-----|-------------------|-----------|
| **True constraint** | Law, regulation, a signed contract, a hard platform rule — externally imposed and verifiable | Verify it's real (read the clause, not the rumor of it). Honor the *what*; keep design freedom in the *how* — even genuine constraints rarely dictate implementation. |
| **Stakeholder theory** | A colleague's or executive's assumption about what will work | Trace to the underlying **business problem** and the evidence. Restate as "we believe…" and treat it as a candidate hypothesis alongside others. |
| **Customer solution-hypothesis** | A customer's guess at what would fix their (often unstated) problem | Trace to the underlying **customer problem** — rewrite as a job story; ask what they'd do if this exact ask were impossible. |

*(Cagan's article draws no true-constraint exception — his point is how
rare and how narrow real constraints are. The bin exists because PMs do
meet contracts and regulators; the discipline is to verify before
believing, and to notice that even "contractually committed" usually
commits an outcome, not a design.)*

Routing after reclassification:
- A traced **problem** with thin evidence → discovery
  (`customer-interviews`, or the ODI pipeline for prioritization).
- A restated **hypothesis** worth betting on → test it
  (`experimentation`) before building it.
- A verified **constraint** → into the PR/FAQ's internal FAQs and the
  solution's evaluation criteria, with its latitude noted.

## Two working rules

1. **Form and function iterate together.** Never freeze a spec before any
   solution exploration has happened; expect prototypes and design
   directions to rewrite the "requirements" — that's the process working,
   not scope creep.
2. **When blocked, substitute — don't surrender the outcome.** If the asked-
   for approach is infeasible (technically, legally, commercially), return
   to the problem and generate alternatives. Report "this path is blocked,
   here are two others that serve the same need," never just "can't."

## The standard

Every artifact in this system inherits the closing line as its acceptance
bar: not "did we build what was asked," but **did we discover a solution
that works for the users, the customers, and the business.**

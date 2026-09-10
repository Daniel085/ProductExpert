# Brainstorming — Method Reference

*Distilled from the **`product-brainstorming`** skill in Anthropic's
**`product-management`** plugin (verbatim source and license in
[`./materials/`](./materials/README.md)). The frameworks are
common-currency PM practice with their own lineages — HMW (IDEO / Stanford
d.school), SCAMPER (Bob Eberle), OODA (John Boyd), JTBD (see
`../jtbd/`) — credited in [`../../CREDITS.md`](../../CREDITS.md). The
landscape-scan protocol (§7) and the gated assumption ledger are this
repo's additions.*

## 1. Purpose and position

**The front door of Track 1** — the stage before anyone has decided an
idea is worth interview time. Input: an idea, a problem area, or a
strategic question, usually with no evidence yet. Output: a framed
problem, a genuinely explored option set, a
[ranked assumption ledger](../customer-interviews/assumption-ledger.md)
with the single riskiest assumption and its cheapest test, and a routing
decision (interview / quantify / write the PR/FAQ / park / kill).

The register is deliberate: this is a **thinking partner**, not a
document generator. Opinionated, challenging, bringing unexpected angles —
helping the PM reach ideas they would not have reached alone. The
conversation is the work; the file is the capture at the end.

## 2. The four modes

### Problem exploration
*When the PM has a problem area but hasn't defined what to solve.*
Understand the space before solutions: who has this problem and what are
they doing about it today; map the ecosystem (who's involved, what
triggers it, the cost of not solving it); distinguish symptoms from root
causes (keep asking "why" until something structural); surface adjacent
problems; ask how it varies across segments.

Canonical questions:
- "What happens if we do nothing? Who suffers and how?"
- "Who has solved a version of this problem in a different context?"
- "Is this a problem of awareness, ability, or motivation?"
- "What would need to be true for this problem to not exist?"

### Solution ideation
*When the problem is well-defined and the PM needs options.* Divergent
thinking — quantity enables quality. Apply the divergence rules (§4).
Techniques:
- **Constraint removal** — "What would you build with no technical / budget
  / political constraints?" Then work back to feasible.
- **Analogies** — "How does [another industry] solve this? What can we
  steal?"
- **Inversion** — "How would we make this problem worse? Now reverse each."
- **Decomposition** — split into subproblems, solve independently, combine.
- **User hat-switching** — "How would a power user solve this? A brand-new
  user? An admin? Someone who hates our product?"

### Assumption testing
*When the PM has an idea and needs its weak points found before investing.*
List every assumption the idea depends on — stated and unstated; for each:
how confident are we, on what evidence, what would disprove it. Identify
the **riskiest** assumption (the one that kills the idea if wrong) and the
**cheapest test** for it. Play devil's advocate: argue the strongest case
against. Record it all in the
[assumption ledger](../customer-interviews/assumption-ledger.md), which
also defines the six assumption categories to probe.

### Strategy exploration
*When the question is direction, positioning, or big bets — not a
feature.* Map the playing field (the possible moves, not just the obvious
one); think in bets (what are we betting on, the odds, the payoff);
consider second-order effects ("if we do X, what does that enable or
foreclose?"); bring in competitive dynamics ("how do competitors
respond?"); think in timeframes (3 months vs 12 vs 3 years).

## 3. Session rhythm

**Frame → Diverge → Provoke → Converge → Capture.** It opens up before it
narrows down. Run the landscape scan (§7) between diverge and converge.

**Framing checklist** (spend real time here — a poorly framed brainstorm
produces ideas that connect to nothing):
- [ ] What are we exploring? (a specific problem / opportunity area /
      strategic question)
- [ ] Why now — what triggered this?
- [ ] What do we already know? (prior research, data, feedback)
- [ ] What are the constraints? (timeline, technical, business, team)
- [ ] What would a great outcome from this session look like?

**Converge:** group ideas into themes; evaluate against **user impact /
feasibility / strategic fit / evidence strength**; pick the top 2–3 and
name each one's biggest unknown and the cheapest way to resolve it. Don't
kill ideas by committee — if one excites the PM, explore it; the
brainstorm is not the decision.

**Capture:** key ideas and why they're interesting; assumptions to test;
questions to research; next steps; and **what was explicitly set aside** —
interesting but not now.

## 4. Divergence rules (checklist)

- [ ] **≥ 5–7 distinct options** exist before *any* is evaluated
- [ ] Options vary along **scope** (tweak ↔ big bet), **approach**
      (product / process / policy), **timing** (quick win ↔ long-term)
- [ ] At least one **"do the opposite"** option
- [ ] At least one option that **removes something** rather than adding
- [ ] **No feasibility judgments during divergence** — constraints return
      at converge
- [ ] Past the obvious: the first 3–5 ideas are the ones anyone would have
      had; keep going

## 5. Provocation questions

- "What is the strongest argument against this?"
- "Who would hate this and why?"
- "What are we not seeing?"
- "What would [specific company or person] do differently?"
- "What if the opposite were true?"
- "What is the version of this that is 10× more ambitious?"

## 6. Frameworks as tools, not templates

Pull one in when it moves the conversation; never force a session through
all of them.

- **How Might We** — reframe pain as an actionable question: *"How might we
  [desired outcome] for [user] without [constraint]?"* Calibrate the
  altitude: too broad ("…improve onboarding?") means anything; too narrow
  ("…add a tooltip to step 3?") is a solution in disguise; right level:
  "How might we help new users reach their first success within 10
  minutes?" Generate 5–10 HMWs per problem — each reframing opens a
  different solution space.
- **First-principles decomposition** — state the problem/assumption; break
  it into fundamental components; ask of each "law of physics, or
  convention?"; rebuild from only the fundamentals. Use when everyone says
  "that's just how it works."
- **SCAMPER** — seven lenses on an existing product: **S**ubstitute,
  **C**ombine, **A**dapt, **M**odify (10× bigger/smaller/faster), **P**ut
  to other use, **E**liminate ("would anyone notice?"), **R**everse (flip
  the sequence, invert the default).
- **Reverse brainstorming** — invert ("how could we make onboarding as
  confusing as possible?"), generate the worseners, reverse each one into
  a solution seed. Works because people spot wrongness faster than they
  imagine rightness.
- **OODA loop** (Observe – Orient – Decide – Act) — a tempo framework:
  observe wide without filtering; orient (and challenge your orientation —
  seeing what's there, or what you expect?); decide proportionally to what
  you know (small bets under uncertainty); act, then re-observe. Use it
  when the team over-deliberates, when competitive timing matters, or when
  the session circles without converging — most teams get stuck in Orient.
- **JTBD / job stories** — don't restate it here: frame jobs per
  [`../jtbd/job-stories.md`](../jtbd/job-stories.md), including "what did
  they fire to hire this?"
- **Opportunity solution trees** — a Teresa Torres discovery structure on
  the README roadmap; not defined here. Sketch one only if the PM asks,
  and mind the recorded Ulwick-vs-Torres "opportunity" terminology clash.

## 7. Landscape scan protocol (repo addition — not in the plugin)

Before converging, run (or ask the PM to run) a **short market scan** and
record it as **BACKGROUND-tier** knowledge (the tiering discipline of
`docs/principles.md` §8 — public information, validated by nobody you've
talked to). Answer four things:

1. **Who already solves this job, and how?** Named products/workarounds.
2. **The price band** customers currently pay.
3. **Is the wedge a product or a feature** an incumbent could ship in a
   quarter?
4. **What would the customer have to *stop* doing to adopt** — what gets
   fired?

Output: a **5–10 line table with sources**, folded into the capture file.

**The rule that keeps it honest: a scan is context for the assumption
ledger, never a verdict.** It can sharpen assumptions and reveal the
competitive set; it cannot validate the problem — only interviews can. A
crowded scan doesn't kill an idea (crowds mark real jobs) and an empty
scan doesn't bless one (it may mark a non-problem).

## 8. The gated output: the assumption ledger

The engagement's handoff object is the shared
[assumption ledger](../customer-interviews/assumption-ledger.md) —
template, categories, evidence tiers, and ranking rule live there, stated
once. The gate here: **no ideation engagement is done until the ledger
names one riskiest assumption and a test cheaper than building anything.**

## 9. Anti-patterns (coach's tells)

| Anti-pattern | The tell | Name it with one line |
|---|---|---|
| **Solutioning before framing** | "We should build X" before the problem is defined | "What user problem does X solve — and how do we know?" |
| **Feature parity trap** | "Competitor has X, so we need X" | "That's copying, not brainstorming — what user need does X serve, and is there a better way to serve it?" |
| **Anchoring on constraints** | "We can't because of technical limitation Y" | "Constraints are for converge — explore freely first, then we'll figure out feasibility." |
| **The one-idea brainstorm** | PM arrives with a solution and calls it brainstorming | "That's one approach. What are three others?" |
| **Analysis paralysis** | Long divergence, no convergence | "If you had to pick one direction right now, which — and why?" |
| **Brainstorming when you should be researching** | The session circles because nobody knows the answer | "This isn't brainstormable — it's a research question. Here's what we need to find out." |

## 10. Thinking-partner register

**Do:** be opinionated ("I think B is stronger because…" beats a pros/cons
list) · challenge constructively ("that assumes X — are we confident?",
not "that won't work") · bring unexpected angles (cross-industry
analogies, counterexamples, edge cases) · match energy — explore an
exciting idea *with* the PM before poking holes · ask the next question
("and then what happens?") · name the pattern when a trap appears (§9).

**Do not:** dump frameworks · generate a list and hand it over —
brainstorming is a conversation, not a deliverable · agree with everything
· evaluate feasibility in divergent mode · anchor on the first idea
(acknowledge it, then "what else could solve this?") · confuse
brainstorming with deciding — the brainstorm generates options; the
decision comes later, with more data.

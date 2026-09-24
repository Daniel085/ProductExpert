# Pre-Build Experiments — Method Reference

*How to prove a solution is worth building before building it. Distilled
from **Tristan Kromer** (Wizard of Oz vs. concierge; generative vs.
evaluative), the **Bank of America "Keep the Change"** case (concept
test), **Tomer London / Gusto** on the minimum *lovable* product and the
manual back-end, **Chris Matts** on MVP vs. MVI, and **Paul Graham**'s
"do things that don't scale" — sources in [`./materials/`](./materials/).
The experiment card, the chooser, and the gates are this repo's
operational extension. The iteration rhythm lives in
[`product-kata.md`](./product-kata.md). See
[`../../CREDITS.md`](../../CREDITS.md).*

> **Where this sits.** Discovery tells you the problem is real and which
> one to solve. This method answers the next question — *is this
> solution the right answer to it?* — with the cheapest experiment that
> could say no. A PM who hears what users ask for, builds exactly that,
> and finds it wasn't what they wanted skipped this step. It runs
> **before** A/B testing (which needs a live product and traffic —
> `experimentation`) and **after** the problem has evidence
> (`problem-selection` *Yes*, or a customer-interviews *persevere*).

## 1. Four rules

1. **Research first.** Don't build until you thoroughly understand the
   problem — the experiments below assume a validated problem; they
   cannot substitute for one.
2. **Use things that don't scale, early.** Airbnb sent professional
   photographers to shoot listings by hand; Groupon's first deals were
   assembled manually; Gusto's first benefits enrollment was people
   phoning carriers behind a screen that looked automated. Test the
   hypothesis before building the automation.
3. **Collect feedback — but weigh behavior and commitment over words.**
   What people do in the experiment (sign up, pay, return, hand over
   data, change a habit) outranks what they say about it.
4. **Distinguish the business's problem from the user's need.** Bank of
   America's brief was "boost enrollment" — a business problem with no
   user in it. The product came from watching a mother round up her
   checkbook. Solve the user's need in a way that serves the business
   goal; never the reverse.

## 2. Know what you are trying to prove

Every experiment starts from one sentence: *at this point, the thing we
most need to be true is ___.* Tomer London's version — "what are you
trying to prove at every point in time?" — decides the slice, the test
and the metric. Common answers, in the order they usually arrive:

| What you are trying to prove | The evidence that would do it | Experiment family |
|------------------------------|-------------------------------|-------------------|
| People want this promise | Sign-ups, deposits, waitlists, "wow" reactions to the *concept* | Concept test, landing page / smoke test |
| We know what the solution should be | Repeated manual delivery converges on a set of steps customers value | Concierge |
| *This* solution delivers the value | Users get the outcome from a simulated product and come back | Wizard of Oz |
| A narrow real version is lovable | NPS, referrals, retention, willingness to pay in a tiny segment | Minimum lovable product (with a manual back-end where needed) |
| Changing an existing product moves its metric | Baseline, then a measured step | Minimum viable investment (see §5) |
| The effect is causal at scale | Controlled comparison, pre-registered | A/B test → `experimentation` |

If you cannot fill the first column, you are not ready to run anything.
When the starting point is a **feature request** rather than a belief,
get to that sentence through the breakdown protocol in
[`riskiest-assumption.md`](./riskiest-assumption.md): observation →
eight questions → assumption chain → the one riskiest link.

## 3. Generative or evaluative? (Kromer's axis)

The single most important distinction, because mixing the two "leads to
faulty reasoning and flawed business models":

- **Generative** experiments discover what the solution should be. Vague
  idea in, clearer solution hypothesis out. Human presence is a feature.
  *Concierge.*
- **Evaluative** experiments falsify a clearly stated solution hypothesis.
  Simulate the intended experience as precisely as possible without
  technology; iterate fast because nothing is built. Human presence is a
  contaminant. *Wizard of Oz, concept test, landing page, usability
  test.*

The tell for a mismatch: running a concierge test "to validate" a
solution. The visible human adds a value proposition the product will
never have (people like being helped by a person), so the test skews to a
false positive — or, where people want privacy, a false negative. Use
concierge to find the solution; then evaluate it with a Wizard of Oz.

## 4. The experiment catalogue

Each entry: what it tests · how it works · prerequisites · what to
measure · known biases · when to stop.

### Concept test *(evaluative — desirability of the promise)*
- **What it tests:** whether the value proposition, shown but not
  delivered, draws a strong response.
- **How:** put the promise in front of the segment as a storyboard,
  short video, mock screens or a one-page description, and measure
  response. Bank of America showed a cartoon video of the round-up
  service to 1,600 people in an online survey before building Keep the
  Change.
- **Prerequisites:** a written value proposition
  ([`../jtbd/value-proposition.md`](../jtbd/value-proposition.md)); a
  defined segment to sample.
- **Measure:** commitment-graded intent (would you sign up now / give an
  email / put down a deposit) beats a Likert "how appealing"; plus
  verbatim reactions for the *why*.
- **Bias:** stated intent inflates; positive framing inflates; the
  sample may not be the job executor. Counter with a commitment ask and a
  competing-concept control.
- **Stop when:** the response is unambiguous either way, or it reveals
  the concept needs a feature you didn't show (BofA's iteration added the
  overdraft guard and the summary).

### Landing page / smoke test *(evaluative — demand)*
- **What it tests:** whether people will act on the promise before it
  exists.
- **How:** a page or in-product entry point that offers the value
  proposition and asks for a real action (sign-up, pre-order, "notify
  me"); traffic from the intended channel.
- **Prerequisites:** the promise in customer language; a channel you can
  actually use later, otherwise you learn about the channel, not the
  product.
- **Measure:** conversion to the committed action; cost per committed
  user if paid traffic. Ask a follow-up question at the point of
  commitment.
- **Bias / ethics:** tell people promptly what is real; a "fake door" in
  an existing product costs trust if it is not disclosed after the click.
- **Stop when:** conversion clears or misses the threshold you set before
  launch.

### Concierge test *(generative — what the solution should be)*
- **What it tests:** which steps, decisions and information actually
  create the value — learned by delivering it by hand, visibly, to real
  customers.
- **How:** perform the service personally, like a hotel concierge:
  Wealthfront sat with clients and worked through their portfolio with
  pen and paper; Food on the Table's founder went grocery shopping with
  customers; Airbnb's founders photographed hosts' apartments.
- **Prerequisites (Kromer's list):** a clear customer segment; evidence
  the segment has the problem; a value proposition for that segment; and
  **evidence the customer will "pay" — commit money and/or time — to take
  part.** Without a known pain point it isn't a concierge test, it's
  ethnography.
- **Measure:** what customers ask for, skip, and repeat; where you
  improvise; what they'd pay; and — Cauvin's point in the comments —
  the *problems* you did not know about, which can force a pivot.
- **Bias:** the human premium; small n; the concierge's own skill
  substituting for the product.
- **Stop when:** you can write the solution hypothesis as a step list
  and its minimum feature set — then move to an evaluative test.

### Wizard of Oz *(evaluative — this solution delivers the value)*
- **What it tests:** whether a specific, defined solution produces the
  outcome, by simulating the product exactly while humans do the work
  behind the curtain.
- **How:** Aardvark routed questions to experts by hand (interns);
  CardMunch "OCR'd" business cards with workers on Amazon's Mechanical
  Turk; Gusto's benefits enrollment showed a finished-looking flow while
  staff phoned insurance carriers. **Amazon's Echo** team tested the
  Alexa experience before the speech stack could carry it: a human
  "wizard" in another room heard each question and typed the answer,
  which the device spoke — testers usually weren't told — then each
  tester filled out a satisfaction report on what they liked. The user
  sees the intended product, a little slower.
- **Use it when there is no reference product.** Echo had no screen and
  nothing comparable to benchmark against (Siri, Voice Search and Kinect
  all worked differently), so the *experience itself* was the
  hypothesis: "it really had to feel like talking to a human being." A
  wizard is how you test an experience that can't yet be built.
- **Vary the variable you care about.** Echo ran fifty people through
  the same script with deliberately varied *response times* and
  *sentence structures*, scoring each on the satisfaction report —
  "almost a psychology experiment to figure out what does it take to
  really make people excited." A wizard can A/B a design decision by
  hand before the design exists; the measure is the tester's report,
  not the wizard's impression.
- **Replace the wizard piece by piece.** The original HCI use (Kelley,
  1980; Munro & Norman at Xerox PARC, 1975) had the wizard handle
  everything in session one and hand successive pieces to code in each
  later session, until the system could run unattended and the wizard
  only observed. The wizard's log is the backlog for that replacement —
  and the automation vision the manual-first pattern below demands.
- **Prerequisites:** a solution hypothesis clear enough to script; a job
  that tolerates a delay (no real-time requirement); a plan to disclose
  or transition.
- **Measure:** the outcome metric the product will own (tasks completed,
  return usage, willingness to pay), plus the wizard's log of what the
  humans had to decide — that log is the spec.
- **Bias:** the simulation under-performs on speed; if the delay itself
  changes behavior, note it. Ethically, the user's data is being handled
  by people — say so in terms.
- **Stop when:** the hypothesis is falsified, or the wizard's log has
  stopped producing new cases.

### Minimum lovable product *(evaluative — a narrow real version earns love)*
- **What it tests:** that a real, deliberately tiny version exceeds
  expectations for one narrow segment — Gusto's first payroll served only
  simple California employers with salaried staff, no hourly, no
  contractors, no benefits.
- **How:** pick the slice by what you are trying to prove (Gusto needed
  to prove two things: that they could compute and pay payroll taxes at
  all, and that customer love would drive word-of-mouth growth), build
  that slice to a standard that delights, ship to the narrow segment.
- **Prerequisites:** the value proposition, the goal reading, a segment
  small enough to serve superbly.
- **Measure:** love signals — NPS, unprompted referrals, product-market-fit
  survey, retention, happy payment — then, per step, "did we get to
  customer love? then expand" (hourly employees, contractors, benefits,
  more states — each gated on the previous).
- **Lovable is defined, not felt:** Gusto's three-part bar — **solves the
  problem end-to-end** (the W-2 also gets mailed), **intuitive** (the
  product tells you what to do today; no manual), **delightful**
  (captures an emotional moment — relieve a stress, celebrate a payday).
- **Bias:** early adopters forgive; a slice can be lovable and
  un-generalizable (Gusto rebuilt its system several times as state
  rules arrived). The MLP proves love, not architecture.
- **Stop when:** love is present in the slice → expand one step; absent
  after honest iteration → kill (Gusto gave a health-reimbursement
  product four to six months, then removed it).

### Manual-first back-end *(a delivery pattern, not a test by itself)*
- Ship the customer-facing experience; run the fulfilment by hand behind
  it. Two pitfalls, from Tomer London:
  1. **No automation vision.** Manual forever becomes an operations
     company with poor unit economics that never automates. Before you
     start, write how it would be automated if it works.
  2. **Automate everything first.** A long slog that exhausts the team
     before customers see anything, and leaves no energy for the
     iteration that feedback demands.
- **Governing rule:** you may keep growing the manual version only while
  **unit economics improve every period**. Grew 2× but margins flat →
  stop and build the back-end before selling more. No fixed cap; a
  required trend.

### Prototype / usability test *(evaluative — can they use it)*
- Clickable or paper prototype in front of the job executor doing a real
  task. Tests **usability**, not desirability — a smooth prototype of an
  unwanted product tests nothing that matters. Roadmap: a dedicated
  usability-testing method (Krug) is planned; until then, run it as an
  evaluative card here.

### A/B test *(evaluative — causal effect at scale)*
- Requires a live product, traffic, and a randomizable unit. Hand the
  belief to the **experimentation** agent, which owns pre-registration,
  power, trust checks and readout.

## 5. Choose your minimum: MVP · MLP · MVI

Three words that get confused, and the context that decides. What any
of them is *for* — the fastest path to insight, never a small v1 — and
how to align one with a learning goal is in
[`minimum-viable-product.md`](./minimum-viable-product.md).

| You are… | The minimum is a… | What it means |
|----------|-------------------|---------------|
| Building a **new product for a new market** | **MVP** — minimum viable product | A risk-management device for testing hypotheses about the *segment and its needs*; it is not about the product |
| Building new for a market where **experience is the differentiator** | **MLP** — minimum lovable product | A narrow slice built to exceed expectations; the love is the hypothesis, measured |
| Changing an **existing product with existing customers** | **MVI** — minimum viable investment | Instrument the current product first; make small, outside-in investments toward the vision; measure lead time to real customers |

Matts's warning: established companies adopting "MVP" tend to produce a
**minimum viable *rewrite*** — years of inventory in a staging
environment, no market feedback, all the business-case and market-share
risk ignored. The fix is the kata rhythm: baseline, small step, measure,
repeat ([`product-kata.md`](./product-kata.md)). Gus Power's addendum:
distinguish a *minimum viable* product (built to test) from a *minimum
sustainable* one (built to run) — security, performance and operations
get descoped under "minimal" and must be added before BAU.

## 6. The experiment card (template)

Extends the Wilkie format already used across the system
([`../customer-interviews/research-and-insight.md`](../customer-interviews/research-and-insight.md))
with the fields a pre-build experiment needs decided **before** it runs.

```
Experiment: <name>                       Family: concept / landing / concierge / WoZ / MLP / prototype
Trying to prove: <the one thing that most needs to be true right now>
Type: generative | evaluative
We believe that … <the belief — usually the value proposition or a solution hypothesis>
To verify that … <what we will do, with whom (segment, n), for how long (≤ 1–2 weeks)>
Built:          <the minimal thing — and what is faked / done by hand>
Measured:       <behavior + commitment signal; the "wow" check; the wizard/concierge log>
Expected:       <the number or observation that counts as PASS — written now>
Would disprove: <the observation that means we drop or pivot — written now>
Bias & ethics:  <human premium / stated-intent inflation / disclosure plan>
Cost:           <people-days, cash, customer goodwill at risk>
Found out that: <result — validated / invalidated / surprised; the unknown unknowns>
Decision:       <persevere / pivot / kill / next experiment>  → ledger updated
```

A card without *Expected* and *Would disprove* filled in before the run is
not an experiment; it is a demo with a metric attached.

## 7. Gates and anti-patterns

**Before running anything:** the problem has evidence (a
problem-selection *Yes* or equivalent); the value proposition is written;
"trying to prove" is one sentence; the experiment family matches the
generative/evaluative need; the pass/fail lines are on the card.

| Anti-pattern | Tell | Fix |
|--------------|------|-----|
| **Validating with a concierge** | "Customers loved working with us" | Human premium; re-run as Wizard of Oz |
| **Building to learn what a phone call would teach** | Six weeks of engineering before any customer contact | Concept test or concierge first |
| **Faking without a plan to be real** | Manual back-end, no automation design, margins flat | Write the automation vision; apply the unit-economics rule |
| **Automating first** | "We'll launch when it's fully built" | Ship the slice; fake the rest |
| **Minimum viable rewrite** | "MVP" of an existing product = feature parity in 18 months | MVI: instrument, small outside-in steps, measure lead time |
| **Compliments as results** | "Everyone said it was great" | Commitment signals only: sign-ups, money, data, return visits |
| **Slice by what's easy** | The MVP is whatever the team could build in a sprint | Slice by what you are trying to prove |
| **No kill line** | Experiment "still running" at month five | *Would disprove* written up front; time-box; Gusto killed at 4–6 months |
| **Solving the business's problem directly** | "Increase enrollment" → a sign-up promotion | Find the user need that, served, moves the business metric |

## 8. Cases, briefly

- **Bank of America — Keep the Change (2004–05).** Business goal:
  enrollment. Ethnography with a dozen families → observation: a single
  mother rounds up checkbook entries for easy math and a hidden buffer;
  finding: mothers can't save (nothing to set aside, or impulse
  spending). 20 brainstorms, 80 concepts, one chosen. **Concept test:**
  cartoon video + 1,600-person survey → strong response → approved →
  iteration added a round-up summary, an overdraft guard and a 3-month
  100% match. Outcome: 2M customers in under a year; 60% of new customers
  enroll; 99% stay. Tim Brown: "People couldn't tell us that they wanted
  a debit card that would 'keep the change.' It didn't occur to them."
  Counter-view worth keeping: the per-customer saving is small; the win
  was on the bank's goal metrics.
- **Gusto — payroll (2012→).** Signal: small-business owners *cursing*
  about payroll (the emotional response was the discovery test). Two
  things to prove: can we compute and pay taxes; will love drive growth.
  **MLP:** California-only, salaried-only, no benefits; measured NPS,
  referrals, PMF survey. Expanded one capability at a time, each gated on
  love. **Wizard of Oz** for benefits: a finished-looking enrollment
  flow, staff phoning carriers behind it, with an explicit automation
  vision and a rule that growth continues only while unit economics
  improve. **Kill:** QSEHRA, after 4–6 months of "pulling teeth" and
  poor economics.
- **Aardvark / CardMunch.** Wizard of Oz at product scale: interns and
  Amazon Mechanical Turk workers were the "algorithm"; no real-time requirement,
  so nothing needed building to prove the value.
- **Amazon Echo / Alexa (2011–14).** Pitched in 2011 as a screenless,
  voice-controlled household appliance; Dave Limp's first reaction was
  "this is going to be hard." Three lessons from Eugene Kim's account:
  1. **Wizard of Oz for an experience with no precedent.** A human in
     the next room typed the answer to each spoken question and the
     prototype voiced it, usually without telling the tester; testers
     then filled out satisfaction reports. Fifty people, one script,
     response time and phrasing varied deliberately — "a constant
     science project" focused "maniacally on quality of speaking."
  2. **A top-down bar, then data to reach it.** At the plan review Bezos
     reportedly replaced the team's two-second latency goal (industry:
     2.5–3 s) with one second — "let me give you the pain upfront" —
     and added that they had convinced him latency mattered, so they
     should believe in themselves. Limp does not recall a specific
     one-second figure. The route there was thousands of internal tests
     and weekly analysis with speech scientists; the product shipped
     below 1.5 seconds, well ahead of competitors.
  3. **The tester data found the hook.** Over 40% of early testers said
     their main intent was music, so the team doubled down on music as
     the frequency-of-engagement entry point — the prototype grew from
     hockey-puck size to fit a real speaker — while Bezos worried it
     would be read as "just a music player." The entry-point job and
     the platform vision were in tension, and the data decided the
     entry point without surrendering the vision. Pre-orders passed a
     million in under two weeks, far above the team's own estimate.
- **The method's origin.** Named by John F. Kelley (Johns Hopkins, c.
  1980) for a calendar-keeping natural-language system; the same
  experimenter-in-the-loop idea ran at Johns Hopkins (Ford, 1975), at
  Xerox PARC (Munro & Norman, c. 1975) and, as a "black box filled with
  people," in Nigel Cross's simulated CAD studies of the 1960s. Kelley's
  wizard-then-code iteration reached 86–97% recognition in 16 trials —
  the empirical case that faking first, then automating what the fake
  taught you, converges.
- **Wealthfront / Food on the Table / Airbnb.** Concierge: sit with the
  customer, do the job by hand, learn what the automated version must
  do — and, for Airbnb, that professional photos were the lever.

## Sources & materials

- **Tristan Kromer**, *"Wizard of Oz Prototyping vs. Concierge Test: The
  Key Difference"*, Kromatic (Grasshopper Herder), 15 Sep 2015 — and the
  comment exchange with **Roger L. Cauvin**. Source:
  `./materials/Kromatic-WizardOfOzVsConcierge.pdf`; transcription under
  `./materials/extracted/`. Kromer credits **J. F. Kelley** (1975) for the
  Wizard of Oz technique.
- **Wikipedia**, *"Wizard of Oz experiment"* (CC BY-SA 4.0; retrieved
  2026-09-22) — the HCI definition and origin: **John F. Kelley**'s
  naming (c. 1980), **W. Randolph Ford**'s experimenter-in-the-loop
  (1975), **Allen Munro & Don Norman** at Xerox PARC (c. 1975), **Nigel
  Cross**'s 1960s simulated-CAD studies, and the wizard-replaced-by-code
  iteration. Wikitext:
  `./materials/extracted/wikipedia-wizard-of-oz-experiment.txt`. The
  article does **not** mention Amazon or Alexa.
- **Eugene Kim**, *"The inside story of how Amazon created Echo, the
  next billion-dollar business no one saw coming"*, Business Insider,
  2 Apr 2016 — the Echo team's Wizard-of-Oz tests (wizard in another
  room typing answers, satisfaction reports, 50 participants, varied
  latency and phrasing), Bezos's reported one-second latency directive
  (which **Dave Limp** does not recall), the sub-1.5-second outcome, and
  the music-as-hook finding. Source:
  `./materials/BusinessInsider-InsideStoryAmazonEcho-Kim2016.pdf`;
  transcription:
  `./materials/extracted/businessinsider-inside-story-amazon-echo.txt`.
- **Karen von Schmieden**, *"Feeling in Control: Bank of America Helps
  Customers to 'Keep the Change'"*, thisisdesignthinking.net — quoting
  **Tim Brown** (IDEO), **Sally Madsen** (IDEO) and **Faith Tucker**
  (Bank of America). Source:
  `./materials/ThisIsDesignThinking-BankOfAmerica-KeepTheChange.pdf`.
- **Tomer London** (Gusto) with **Melissa Perri**, *Product Thinking*
  podcast, episode 200, "Building a Minimal Lovable Product", Produx Labs,
  Dec 2024. Source:
  `./materials/ProduxLabs-Ep200-MinimalLovableProduct-TomerLondon.pdf`.
- **Chris Matts**, *"MVP considered harmful. Introducing the MVI."*, The
  IT Risk Manager, 26 Mar 2016 (with **Gus Power**'s "minimum sustainable
  product" comment). Source:
  `./materials/ITRiskManager-MVPConsideredHarmful-MVI.pdf`.
- **Paul Graham**, *"Do Things That Don't Scale"* (2013) — Airbnb
  photographers; the manual-Groupon example is common lore of the same
  lesson. Not reproduced here.
- **Eric Ries**, *The Lean Startup* — the MVP and concierge-MVP framing
  the sources above respond to.
- The "trying to prove" chooser (§2), the catalogue's prerequisite /
  measure / bias / stop structure (§4), the MVP-MLP-MVI table (§5), the
  experiment card (§6) and the anti-patterns (§7) are this repo's
  operational extension.
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

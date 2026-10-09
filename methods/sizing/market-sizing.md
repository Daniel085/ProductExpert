# Market Sizing — Method Reference

*How to size an opportunity — TAM, SAM and SOM — **both ways**, bottom-up
and top-down, to a standard an investor or an analyst can rebuild.
Distilled from the practitioners who set that standard: **Bill Gurley**
and **Aswath Damodaran** (the 2014 Uber sizing debate, Damodaran's
possible / plausible / probable test, Cornell & Damodaran's *Big Market
Delusion*), **a16z**, **Pear VC**, **Christoph Janz**, **Jason Lemkin**
and **Lightspeed** (what investors accept and reject), the consulting
case tradition (**StrategyCase**'s routine; **Barbara Minto**'s MECE),
**Douglas Hubbard** (calibrated ranges, the Rule of Five, Monte Carlo),
**Frank Bass** (diffusion), **Steve Blank** (market types, market
definition) and the official statistical agencies that supply the
counts. The research behind this doc is in
[`../../reports/Market sizing expert methods.md`](../../reports/Market%20sizing%20expert%20methods.md);
the preserved sources are under [`./materials/`](./materials/). Where the
research found **no published standard** — the reconciliation tolerance,
the value-capture band, the "customers × value × reachability" formula —
this doc says so and labels its rule a repo extension. See
[`../../CREDITS.md`](../../CREDITS.md).*

> **Where this sits.** The system names sizing in five places and defined
> it in none: the knowledge-gap scorecard's *business impact* area, the
> eight assumption questions' "how big is the opportunity?", the PR/FAQ's
> "what's the TAM and how was it estimated?", the strategy memo's
> initiative value, and the methodology rubric's criterion 3.3, which no
> adopted method covered. This doc is that method. It sizes a market the
> product does not serve yet, or serves only partly, which is
> **Opportunity Discovery** work; quantifying a *change* to a product
> with a baseline is `metrics`' job
> ([`../strategy/product-strategy.md` §3d](../strategy/product-strategy.md)),
> and the two share the formula shape and the tiering rules.

## 1. What "credible" means

Every practitioner source, investor or analyst, converges on one
standard: **a credible market size is a derivation a skeptical reader
can rebuild from a stated customer count and a stated price.** Not a
number lifted from a report; not a percentage of something enormous. The
corollaries:

- **Bottom-up is the primary route.** a16z: *we like seeing a bottoms-up
  analysis, which takes into account your target customer profile*; the
  top-down toothbrush example (1.36B people × $1 × 40% share) *tends to
  overstate market size — why 40%?* Pear VC: *ideally you will only use
  top-down to sanity check the magnitude of your bottom-up estimate.*
- **Two structurally independent routes that land within tens of percent
  of each other** is the practitioner's definition of credible. A larger
  gap is not a failure; it is a diagnostic that names one assumption or
  one definitional mismatch (§5).
- **The number will be wrong.** Felicis's Aydin Senkut: *with TAM, it is
  almost guaranteed you're going to be wrong; the plan has to be
  directionally correct.* Lemkin: *the market size number matters far
  less than how you calculated it.* So **credibility is a property of
  the artifact, not the number**: a register with sources, dates, grain,
  calibrated ranges and counter-cases; two routes with the reconciling
  assumption named; the falsifiability tests run (§5). An artifact like
  that survives a partner meeting after its central estimate is proven
  wrong. A bare number does not survive the first question.

### TAM, SAM, SOM — defined by what each excludes

The three letters come from Sequoia's original business-plan template
(*calculate the TAM (top down), SAM (bottoms up) and SOM*), which is the
likely origin of the "show both" convention. Several investors now call
the SAM/SOM funnel "somewhat academic" because each layer is another
assumption. This doc keeps the three, but as **exclusion steps with
written rules**, never as percentages:

| Figure | Counts | Excludes | The question it answers | Damodaran's tier |
|--------|--------|----------|-------------------------|------------------|
| **TAM** — total addressable market | Every job executor who could buy *this kind of product* at *this kind of price*, anywhere, including today's non-consumers | People who don't have the job; buyers of a different kind of product | How big could this be if we served everyone with the job? | *Possible* → overreach (count every conceivable customer) or *plausible* → expanded (today's reach plus customers the product or market trends draw in) |
| **SAM** — serviceable addressable market | The TAM tiers and geographies **today's product, pricing and channels** can serve | Segments the product can't serve yet, regions it isn't in, buyers the capability clause rules out | How much of that could we serve with what we have? | *Probable* → constrained (count only customers you can reach today) |
| **SOM** — serviceable obtainable market | The SAM that a **stated, mechanism-backed** share and a **stated horizon** make reachable: channel capacity, sales capacity, competitive position | Everything that requires a share you can't justify | What can we actually win in *n* years, and what has to be true? | A share with a named mechanism, or a path-to-revenue count (§3, step D) |

Rules of the table: a SOM that is "1% of the TAM" with no mechanism is
rejected on sight (Pegasus's Reichert: *when this slide appears, most
investors chuckle (or weep)*). SAM is the stronger figure for a PM's
decision, because it is the one a current-state picture can check.
Damodaran's **possible / plausible / probable** tiers are the bridge
between the two routes (§5): a sizing that shows all three, with the
evidence that moves a customer from one to the next, is bottom-up at the
constrained tier and top-down at the overreach tier with the
reconciliation visible in between.

## 2. Step 0 — Define the market, classify it, write the scope

Every famous sizing disagreement (Gurley vs. Damodaran, New Constructs
vs. Snowflake, analysts vs. WeWork) was a disagreement about **market
definition**, not arithmetic. So the first step has nothing to do with
numbers.

**Define the market as job executors + the job**, in words with no
product name and no job title — the ODI market definition
([`../odi/process-map.md`](../odi/process-map.md)), which Steve Blank
adopted explicitly: *the market definition becomes a constant in the
product/market fit equation, not a variable*; don't count job titles,
influencers or economic buyers. The count and the price must then
**share a unit** — accounts, seats or job executions — and the right
denominator for "companies that could buy" is the enterprise, not the
establishment or the employee.

**Classify the market type** (Blank), because type decides which
structures, price methods and adoption curves apply:

| Market type | What it means | Sizing consequence |
|-------------|---------------|--------------------|
| **Existing** | Customers know the category and buy it today | Count buyers, measure spend; top-down from served spend is a legitimate anchor; Gabor-Granger for price |
| **Re-segmented** (niche or low-cost) | An existing market, a segment served differently | Size the segment, not the market; the segment rule from [`../jtbd/segmentation.md`](../jtbd/segmentation.md) is the count's definition |
| **New** | The category doesn't exist; TAM today is zero | Size from adjacent spend pools being substituted and from the **cost of the problem** (§3, step C); Van Westendorp for price; expect a hockey-stick with a multi-year "death valley"; show constrained *and* expanded tiers |
| **Clone** | A proven model in a new geography | Analog market's figures, adjusted by the official counts for the new geography |

Index's Jahanvi Sardana's three buckets ask the same question from the
investor's side: a **known** market (show why yours is a better
toothbrush), an **emerging** one, or an **invisible** one — "the biggest
trap", a "dark art", and the kind Index passed on when Airbnb's TAM
looked too small. Name the bucket; it tells the reader how much of the
sizing rests on measured behaviour versus on a mechanism you believe in.

**Write the scope line** at the top of the artifact: the job executors,
the job, the geography and the period — and remember that attributes
constant across that scope are not cuts
([`../jtbd/segmentation.md`](../jtbd/segmentation.md), the scope rule).

## 3. The bottom-up build (the primary route)

The consensus formula, stated almost identically by Underscore, Pear,
Octopus, Dreamit and PSG:

```
TAM  = Σ over tiers of  (ICP accounts in the tier)  ×  (annual price per account in the tier)
       where price per account = seats × price per seat, or usage × unit price, or a flat plan
SAM  = the same sum over the tiers and geographies today's product and channels can serve
SOM  = SAM × a share with a named mechanism and horizon  — or, better, the path-to-revenue count
```

### Step A — Write the ICP tiers

Tiers are segments: defined by behaviour or need, described by the
attributes that discriminate, MECE, inside the scope
([`../jtbd/segmentation.md`](../jtbd/segmentation.md)). Christoph Janz's
ladder is the useful default for a revenue business, because each rung
carries its own count, price and funnel multiplier:

| Rung | To reach $100M a year you need… | …and the funnel behind it (Janz) |
|------|---------------------------------|----------------------------------|
| Elephants | 1,000 enterprise customers at $100k+ | A direct sales force; long cycles |
| Deer | 10,000 mid-market customers at $10k+ | 100,000+ leads |
| Rabbits | 100,000 small businesses at $1k+ | 0.5–2 million trial sign-ups |
| Mice | 1 million consumers at $100+ | Millions of downloads |
| Flies | 10 million ad-monetised users at $10+ | ~100 million downloads |

The ICP written here must be the same ICP used everywhere else in the
initiative (Underscore's rule); a sizing whose customer differs from the
positioning's customer fails on inconsistency before it fails on
arithmetic.

### Step B — Count each tier from the source stack

Count from an official source first and a vendor cut second, and record
for every count: the **source and tier**, the **grain** (NAICS / SOC /
NACE code, size band, firm vs. establishment), the **reference year**,
the **exclusions**, and the **lag adjustment** to today with its own
range.

| Need | Source (tier) | Grain and caveats |
|------|---------------|-------------------|
| US firms (enterprises) by industry and size | Census **SUSB** (official) | Firms, establishments, employment by NAICS × enterprise size; receipts only in years ending 2 and 7; ~2–2.5-year lag; excludes agriculture, rail, postal, most government |
| US establishments by county, metro, ZIP | Census **CBP** (official) | Establishments with paid employees; disclosure noise; same exclusions. CBP counts *sites to deploy to*; SUSB counts *companies that could buy* |
| US self-employed and nonemployer businesses | Census **Nonemployer Statistics** (official) | From IRS records; receipts ≥ $1,000 |
| US receipts and product-line sales | **Economic Census** (official) | Every five years; 3–4-year lag |
| US people and households | **ACS** 1-year / 5-year (official) | 1-year only for areas of 65,000+; 5-year reaches tracts |
| US workers by occupation and industry | BLS **OEWS** (official) | ~830 SOC occupations, ~530 metro areas; excludes the self-employed; a method change in 2025 affects comparability |
| EU enterprises, turnover, employment | Eurostat **SBS** (official) | NACE Rev. 2, 4-digit; size classes; preliminary at T+12 months, final at T+22 |
| UK businesses | ONS **UK Business** (official) | VAT/PAYE-registered enterprises; unregistered firms excluded |
| Canada; cross-country | StatCan **Business Counts**; OECD **SDBS** (official) | ISIC 4-digit by size class |
| Country macro series | World Bank **WDI** (official) | 1,400 indicators, 217 economies |
| Cuts official data can't make (technology in use, titles, funding) | LinkedIn Sales Navigator, ZoomInfo, Crunchbase (vendor) | Self-reported or modelled; no independent accuracy audit; **reconcile the total against SUSB** for the same NAICS and size band |
| App installs, web traffic | Sensor Tower / data.ai, Similarweb (vendor) | Definitions differ by provider (re-downloads, third-party stores); competitors report 20–50% disagreement; use as a range |

### Step C — Price each tier from the evidence hierarchy

Take the strongest tier available and record which it was:

1. **Your own deals or contracts** — the only CONFIRMED price. Hubbard's
   **Rule of Five**: five random customer quotes or contracts bracket
   the population median with 93.75% probability (the chance all five
   fall on one side is 2 × 0.5⁵).
2. **Public filings** — ARR ÷ customers from a comparable company's 10-K,
   *after* normalising definitions the filings themselves warn are not
   comparable (ARR including maintenance and term licences; a "customer"
   as a distinct agreement vs. a parent organisation; consumption ARR
   from the last three months). Where only bands are disclosed (under
   $250K, over $1M), bracket the tier price rather than computing a mean.
3. **Transaction benchmarks** — contract databases (Vendr's series
   shows how volatile blended ACV is quarter to quarter: a reason to
   carry a range).
4. **Pricing pages and review sites** — the weakest tier; a small share
   of listings show prices and some are data-entry errors.
5. **Willingness-to-pay research** when no price exists (a new market):
   **Van Westendorp**'s four questions (too cheap to trust · a bargain ·
   getting expensive · too expensive) define an acceptable range with no
   reference price, suited to new and re-segmented markets;
   **Gabor-Granger**'s iterative "would you buy at X?" gives a demand
   curve for a product whose packaging is final, suited to existing
   markets; both need a sample of at least ~100 and judge the product in
   isolation. *Monetizing Innovation*'s rule: have the willingness-to-pay
   conversation early, ordered problem → solution → value → price, and
   never report an average that hides two clusters (an average of $60
   when customers sit at $20 and $100 is the segmentation the sizing
   needs).

**For a new market, bound the price with the cost of the problem.** What
the job costs job executors today — the workaround's spend, the hours ×
loaded rate, the ownership cost of the thing being replaced (Gurley
used a conservative $6,000 a year per car) — is the **value ceiling**
the price must sit well below. Matrix's Jared Sleeper calls this route
*value theory*: *here's how much value we can add, and why we'll be able
to capture it* — useful and "a dark art." The only named-investor capture
band the research found is Pear's **10–30% of the value created**;
*Monetizing Innovation* says only that value must be "vastly higher"
than price. **Treat any capture band as a heuristic, labelled BACKGROUND,
never a standard.**

### Step D — SAM by constraint, SOM by reachability

**SAM** applies the constraints the current-state picture already names
([`../strategy/product-strategy.md` §6a](../strategy/product-strategy.md)):
geography, segment, platform, language, regulation, and the capability
clause (what the product can do *today*). Each constraint is a written
rule that removes tiers or geographies from the sum, with the reason.

**SOM** is where sizings go soft. Two acceptable forms, in order of
preference:

- **The path-to-revenue count.** Lemkin: *build a real, bottom-up model
  that shows how you'll get to $100M in ARR in seven years — and make
  sure you believe it.* Pick the Janz rung, state the customer count
  the revenue target needs, and show the funnel that produces it from
  the channels you actually have. The count is the SOM; the revenue is
  its price.
- **A share with a named mechanism.** Damodaran's ladder maps share to
  the mechanism that earns it: roughly **5%** with no network effects,
  **10%** with weak local ones, **15%** strong local, **25%** weak
  global, **40%** strong global — and local effects mean city-by-city
  fights with different winners (which is what happened to Uber outside
  the US). A share that cannot name its mechanism is the "why 40%?"
  failure.

Reachability also has a capacity check: sales capacity × cycle time,
channel reach, support capacity — the SOM cannot exceed what the
go-to-market can physically touch in the horizon.

### Step E — Ranges on every leaf, then a Monte Carlo

Untrained estimators' 90% intervals contain the truth only **30–60%** of
the time (McKenzie et al. 2008; a 2024 study found 30–35%). Assume any
range a user types is two to three times too narrow, and widen it with
Hubbard's tools:

- **The equivalent bet**: would you rather bet on your 90% range or spin
  a wheel that pays 90% of the time? If the wheel, the range is too
  narrow; widen until the two feel equal.
- **Absurd bounds inward**: name a value that is absurdly low and one
  absurdly high, then move each inward until it stops being absurd.
- **Test each bound alone**: is there a 95% chance the truth is above the
  lower bound?
- **Two pros and two cons** for the range as written.

Then **run the tree as a Monte Carlo** (≥ 1,000 draws) rather than
multiplying endpoints (overstates the spread) or midpoints (hides it —
the "flaw of averages"). A spreadsheet with lognormal draws is enough
for a five-to-ten-leaf tree; Guesstimate (free, open source, cells accept
"5 to 9" as a 90% range) and Squiggle (distributions as a text language,
version-controllable) are the purpose-built tools. Report the **5th,
50th and 95th percentiles** as low / base / high, so the three cases
agree with the simulation instead of being chosen by feel. The
**tornado chart** — each leaf swung low-to-high with the others at base,
sorted by swing — answers *what should we research next*: Hubbard's
measurement inversion says the widest bar is usually the least-measured
leaf.

## 4. The top-down tree (the cross-check route)

Top-down is not "a percent of something huge." Done as the consulting
case tradition does it, it is a **MECE tree with justified, rounded
leaves** — and it is built *after* the bottom-up, so it can't anchor it.
StrategyCase's routine (by a former McKinsey consultant), with its rules
quoted because they are the operating standard:

1. **Clarify** the unit, the geography and the period.
2. **Structure** the problem into *three to five drivers that multiply
   together*, and say the structure aloud before calculating.
3. **Assume** with *simple, rounded assumptions*, each justified *with a
   benchmark, personal behaviour, or basic logic*. *Round aggressively:
   10%, 25%, 50% are far easier to work with than 12.7%. Never pull a
   number from thin air without a one-line justification.*
4. **Calculate** without false precision.
5. **Sanity-check**: *compare with a known benchmark, triangulate with a
   second structure, or check the implied per-unit figure.* *A number
   you have not sanity-checked is a liability.*
6. **Interpret** the number for the decision, with its key sensitivity.

The yardstick from the same source: an answer *within the right order of
magnitude generally passes; landing within about 25% of reality is
excellent.*

### The structure menu

| Situation | Structure | Example |
|-----------|-----------|---------|
| Consumer market with a clean starting population | Population × % target × usage × price | National spend on a category |
| Business market with countable buyers | Units × usage per unit × price | Accounts × seats × price per seat |
| Supply limited by a bottleneck | Capacity per unit × units × utilisation | A clinic, a warehouse, a restaurant |
| Durables in a mature market | Installed base ÷ years each lasts, plus growth | Replacement demand |
| One-time life events | Population × share affected ÷ years per lifetime | Weddings, first homes, first hires |
| Supply implied by demand | Total demand ÷ output per unit | How many providers a demand supports |

The same product can need different structures at different scales (a
national market from population; one site from capacity). Pair any tree
with a **per-capita restatement** ("one tuner per 28,000 people —
plausible?") and a **ratio benchmark** (Lightspeed's examples: security
at roughly 7–10% of infrastructure spend; cloud security at 3–5% of
cloud spend).

### Nested definitions, with their tier

A disciplined top-down states *which* market it is sizing, because the
same company sits in several. Damodaran's Uber ladder (2015): urban car
service **$100B** → all car service **$175B** → logistics **$230B** →
mobility services **$310B** — each a different definition, each a
different tier of possible / plausible / probable. Write the ladder,
mark the tier of each rung, and say which rung the bottom-up corresponds
to. This is what turns "why 40%?" into an answerable question.

### Analyst reports: a third cross-check, never the number

Lightspeed calls a pasted Gartner or IDC figure *a big red flag*,
because founders *often don't know what those numbers include or
exclude, or how the firms estimated them*. The documented reasons go
beyond snobbery: a former IDC analyst's account of growth rates kept
consistent over accuracy with an "others" category as the balancing
plug; high-volume publishers whose methods are undisclosed and whose
reports contain copy-paste errors; forecasts for the same market that
differ by a factor of three between firms; aggregators that layer an
upstream CAGR onto a base rather than estimating. Their legitimate use:
as one of the cross-checks, recorded with **publisher tier, stated
definition, year, and the bottom-up factor it tests**; for vendor-share
order where a tracker's panel is strong; as a wide base rate for growth.
A register row for an analyst figure must say whether the methodology is
disclosed.

## 5. Reconcile the two routes

Lay the two trees side by side. **Find the single leaf whose change
closes most of the gap** and decide which route's version of it is
better evidenced; write that decision into the register. Stanford
Biodesign's corrective applies: *when top-down and bottom-up market
estimates vary substantially, it's not a cause for concern — more than
anything, it's a healthy reality check*, because the bottom-up usually
reflects today's served solution space and the top-down the total
opportunity for a better one.

**Tolerance** *(repo extension — the research found no published
standard; coaching material says 15–25% between structures is good)*:

| Market | Acceptable gap | If larger |
|--------|----------------|-----------|
| Mature, well-defined | Within about **±30%** (a factor of ~1.3) | One leaf is wrong; find it |
| New or re-segmented category | Up to a **factor of 2–3**, *only if* explained by a named definitional difference: served spend vs. total opportunity, SAM vs. TAM, units vs. revenue, today's price vs. post-elasticity price | Name the difference in the summary or treat it as unexplained |
| Any | Beyond a **factor of ~3** | One route is sizing a different thing. Fix the **market definition** (§2) before touching arithmetic |

### The falsifiability tests

A sizing becomes investor-grade when it is converted into claims that
can be wrong:

- **Implied-share test.** What share of the market does the plan (or
  the price) require, and is that plausible next to the named
  incumbents? New Constructs disagreed with Snowflake's $81B management
  TAM, built a $66B third-party figure, and showed the IPO price implied
  about **46%** of it, against under 1% at the time — next to Microsoft,
  Amazon, Google and Oracle. Damodaran's 2014 break-even ran the same
  test in reverse: a $17B Uber needed a market three times his estimate
  or a share above 20%.
- **The $100M ladder.** Which Janz rung, how many customers, and does
  the funnel behind that rung exist for this product? (A SOM that needs
  18,000 retained dental practices out of 180,000 is a claim about a
  sales motion, not a percentage.)
- **The fund-return test** (Lightspeed, for a venture audience): work
  backwards from the exit a fund needs to the revenue that implies at a
  plausible multiple, then to the market a category leader's share
  (around 20% for horizontal SaaS) requires. The venture bar itself is
  inconsistent across investors (from "hundreds of millions of
  high-margin revenue within a decade" to "$5B or more"), so treat the
  threshold as a parameter the PM sets for the audience.
- **The aggregation test** (Cornell & Damodaran). Sum the revenues that
  all named competitors' plans imply and compare with the market. In
  2015 the public online-advertising companies together implied about
  $523B of 2025 revenue against a market of about $466B: the group was
  overpriced whatever any one TAM slide said. The thesis — *big markets
  draw in entrepreneurs and VCs, overconfident that they can conquer
  these markets, which leads to a collective overpricing and an
  inevitable correction* — is the **big market delusion**, and a sizing
  that lists the competitors and asks what share each must take is the
  cure.

### Sizing a market the product will expand

Gurley's rule for a market-creating product: *the past can be a poor
guide for the future if the future offering is materially different —
this cannot be yesterday's market.* The method:

1. Show the **constrained** tier (today's served spend) and the
   **expanded** tier (customers the product draws in) separately, with
   the evidence that moves a customer across.
2. For the expanded tier, cite a **measured early-cohort ratio** where
   one exists, not an assumed elasticity. Gurley's strongest evidence was
   a measurement: San Francisco's historic taxi-and-limo market was about
   $120M and Uber's SF revenue was already "a healthy multiple bigger";
   heavy users spent about three times their prior taxi spend. A first
   liquid city, a first cohort, a first segment — that ratio is the one
   number that can discipline an expansion story.
3. Size **adjacent spend pools being substituted** under explicit
   penetration scenarios (Gurley: ~1B cars × $6,000 a year × 2.5–12.5%
   capture = $150–750B), and label the capture rates as the plugs they
   are.
4. Size **adjacencies as separate, probability-weighted trees** — never
   folded into the core TAM, never ignored. Neither Gurley nor Damodaran
   modelled food delivery in 2014; by 2025 it booked nearly as much as
   rides.

## 6. Projecting: from a ceiling to a path

A TAM is a ceiling; the plan needs a path. The standard tool is the
**Bass diffusion model**: adoption follows *dF/dt = (1 − F)(p + qF)*,
with *m* the market potential in units, *p* the coefficient of
innovation (typically 0.01–0.03 a year) and *q* the coefficient of
imitation (typically 0.3–0.5, mean about 0.38); peak adoption comes at
*t\* = ln(q/p) / (p + q)*, about six years at the mean values. The
simplest defensible PM version *(repo extension)*:

- Set *m* to the **constrained** TAM in units (not the overreach tier).
- Borrow *p* and *q* from three to five **named analogs** or the
  defaults; re-fit only once at least five periods of actuals exist.
- Run **fast / base / slow cases on *q***, since word of mouth is the
  dominant uncertainty.
- **Don't update *m* on the first year's actuals** — early sales are
  dominated by *p·m* and say little about the ceiling.
- Let the **market type** set the curve's shape: a new market gets a
  hockey stick with a multi-year "death valley" (Blank: companies in new
  markets that hire and execute like they're in an existing market burn
  through their cash), an existing market a share line.

The known pitfall is the quantitative form of Blank's warning:
enthusiasts overestimate short-term growth and, as a result,
underestimate long-term growth.

## 7. The sizing artifact *(repo extension)*

Three parts, all saved: the **register**, the **model**, and the
**one-page summary**. Credibility is a property of this artifact.

### The assumptions register (one row per leaf)

```
LEAF <id>  <definition — unit · segment · geography · period>
  low / base / high:   <5th / 50th / 95th percentile>        (calibrated: equivalent-bet checked)
  source:              <URL · publisher · tier: official / filing / transaction / vendor / analyst / judgment>
  reference date:      <data year>   accessed: <date>   lag adjustment: <range, reason>
  grain & definition:  <NAICS/SOC/NACE · size band · firm vs. establishment · which ARR definition · installs vs. users>
  confidence:          <HIGH: several corroborating recent sources · MEDIUM: one authoritative source, 1–2 years old · LOW: extrapolated, old, or judgment>   because <…>
  methodology disclosed? <yes / no / n.a.>                     (required for analyst figures)
  counter-case:        <what would make this a tenth of the size>   evidence that would move it: <…>
  pros / cons of the range:  <two each>
  tornado rank:        <n of N>     next validation step: <what · owner · by when>
```

Tiers map to the ledger's: an official statistic or your own contract is
**CONFIRMED**; a normalised filing or a transaction benchmark is
**INFERRED**; a vendor cut, an analyst figure or a judgment is
**BACKGROUND** ([`../customer-interviews/assumption-ledger.md`](../customer-interviews/assumption-ledger.md)).
A sizing whose leaves are all BACKGROUND is a hypothesis; say so.

### The model

A saved, re-runnable script (`sizing.py`) or spreadsheet, or a
Guesstimate link, that reads the register's ranges, draws the Monte
Carlo, and prints the percentiles and the tornado — so that when an
assumption changes, the sizing changes with it and nobody re-types a
number. Every figure in the summary traces to a cell or a line.

### The one-page summary

```
MARKET SIZING — <market: job executors + job>                           as of <date>   owner <name>
Scope:          <geography · period · unit>        Market type: <existing / re-segmented / new / clone>   Bucket: <known / emerging / invisible>
Ladder:         <nested definitions with tier — e.g. urban car service $…(probable) → all car service $…(plausible) → mobility $…(possible)>

                  low (5th)      base (50th)     high (95th)      route
TAM               <…>            <…>             <…>              bottom-up Σ tiers × price
SAM               <…>            <…>             <…>              constraints: <list>
SOM (<n> yrs)     <…>            <…>             <…>              <path-to-revenue count · or share n% because <mechanism>>
Top-down          <…>            <…>             <…>              <structure used>; analyst cross-check: <figure · publisher · definition · year>

Reconciliation:   routes differ by <factor>; the leaf that closes most of it is <leaf>; we keep the <route> value because <evidence>.
                  Definitional difference, if any: <served spend vs. total opportunity / …>
Tests:            implied share for the plan <n%> vs. incumbents <…> · $100M ladder: <rung, count, funnel exists? > · fund-return: <…> · aggregation: <competitors' implied sum vs. market>
Expansion:        constrained <…> → expanded <…> on the evidence of <early-cohort ratio>; adjacencies sized separately: <list with probabilities>
Projection:       Bass with m = <constrained TAM units>, p <…>, q <slow/base/fast>, analogs <…>; or hockey stick (new market), death valley <n> years
Tornado (top 3):  <leaf · swing> · <leaf · swing> · <leaf · swing>   → next to research: <leaf>
Counter-case:     <what would make this a tenth of the size>          What would change my mind: <evidence>
Tier of this sizing: <BACKGROUND / INFERRED / CONFIRMED — the weakest load-bearing leaf decides>
Register: <path>   Model: <path>
```

## 8. Worked examples

### Uber, 2014 — top-down vs. bottom-up on the same company, with hindsight

- **Damodaran, June 2014 (top-down).** Global taxi-and-limo market of
  about **$100B** (Tokyo $20–25B, UK $14B, US $11B, and an *estimated*
  $50B for the rest of the world — half the anchor was a plug), growing
  6% a year; Uber's share rising to **10%** ("at the optimistic end");
  a **20%** revenue slice; **40%** steady-state margin; a 10% failure
  probability. Value: about **$5.9B**, against a $17B round. His own
  break-even located the two levers that would decide everything: the
  round needed a market three times his estimate or a share above 20%.
- **Gurley, July 2014 (bottom-up, market-expanding).** *This cannot be
  yesterday's market.* Four moves: a measured first-city ratio (SF taxi
  and limo ≈ $120M; Uber's SF revenue a healthy multiple bigger; heavy
  users at about 3× their prior taxi spend); mechanisms (price
  elasticity; three local network effects — pick-up time, coverage
  density, utilisation); new use cases (suburbs, rental-car replacement,
  nights out, children and elderly parents); and substitution of a much
  larger pool (~1B cars × $6,000 a year × 2.5–12.5% capture = $150–750B).
  TAM roughly **$450B–$1.3T**; his bearish scenario needed about 56%
  share of it and his likely scenario about 20%. The capture rates had no
  empirical anchor; the SF ratio did.
- **Damodaran's reply and revision.** *Not everything that is possible is
  plausible, and not everything plausible becomes probable.* Local
  network effects imply city-by-city winners. Re-running his model on
  Gurley's narrative ($300B market, 40% share) gave $53B; by late 2015,
  citing evidence that Uber had made the SF market three to four times
  larger, he moved to a $230B "logistics" market, 25% share, a slice
  fading to 15%, a 25% margin: **$23.4B**, and thanked Gurley for the
  correction. Note the shape: market up 2.3×, share up 2.5×, take rate
  and margin down.
- **Uber's 2019 S-1 (overreach).** A "personal mobility TAM" of **$5.7T**
  — every passenger-vehicle and transit mile on earth in 175 countries,
  including countries Uber wasn't in — and a SAM of $2.5T; Uber's miles
  were "less than 1% of near-term SAM." Stratechery: $5.7T is about 7% of
  gross world product. Damodaran abandoned top-down for Uber entirely
  and valued it per rider, because *the uncertainty about the total
  accessible market makes me uneasy with my top-down valuation.* A
  market so large that the share needed looks trivial removes the
  discipline the share assumption exists to provide.

| 2024, projected in 2014 vs. actual | Damodaran | Gurley | Actual |
|------------------------------------|-----------|--------|--------|
| Uber gross bookings | ~$18B (10% of ~$180B) | scenario-dependent | **$162.8B** (FY2024); $193.5B (FY2025) |
| Uber revenue | ~$3.6B | not modelled | $44.0B (FY2024) |
| Share mechanism | local network effects, 10% cap | strong network effects | ceded China, SE Asia, Russia to regional winners |
| Margin | 40% steady state | not modelled | first operating profit 2023; ~11% operating margin FY2025 |
| Delivery | an unpriced option | not in TAM | nearly half of bookings |

Five lessons: the **frame** beat the arithmetic by an order of magnitude
(Uber's 2024 bookings were nine times Damodaran's projection for Uber
and about equal to his projection for the whole taxi market); Gurley's
upper magnitudes remain **unproven** a decade on (FY2025 bookings are
15–43% of his range), which is the right humility for any capture-rate
plug; Damodaran was right about **mechanism** — regional network
effects, take-rate pressure, margins far below 40% — so a sizing can be
right about the market and wrong about the economics, or the reverse;
compare **gross bookings**, not revenue, when testing a market-size
claim, because revenue mixes in take-rate changes; and **adjacencies**
neither side modelled became half the company.

### A B2B tool, bottom-up in ten lines

The data-import product from the strategy doc, sizing a self-serve
plan for small teams in the US:

```
Scope: US companies with 10–249 employees in information & professional-services NAICS (51, 54) · 2026 · unit = company (enterprise)
Tier B (rabbits)  count: SUSB 2023 firms, NAICS 51+54, 10–249 employees ≈ <n> (official; lag +2 yrs, +3–6%)
                  attach: share that import structured data monthly — 6 of 9 interviewees; survey 38% [25–50%] (INFERRED)
                  price:  $1,800/yr base [$1,200–2,600] — 11 closed deals, median $1,800 (CONFIRMED; Rule of Five satisfied)
TAM (tier B)      ≈ n × 38% × $1,800        → Monte Carlo 5/50/95: <…>
SAM               English-language, self-serve-reachable, no SOC 2 requirement (removes regulated sub-industries): −22% [15–30%]
SOM (3 yrs)       path to $10M ARR = ~5,500 retained customers = Janz "rabbits"; funnel needs ~60k trials at 9% [6–12%] conversion — do we have that channel? (the claim to test)
Top-down          US SMB data-integration spend <$…> (analyst, methodology undisclosed) × share of 10–249-employee firms × self-serve share → within 1.6× of bottom-up; the leaf that closes it is the attach rate (analyst assumes all firms, we assume 38%) — we keep ours (survey + interviews)
Tornado           attach rate > price > SUSB lag adjustment
Counter-case      attach rate is 15% because most teams import once at setup, not monthly → TAM ÷ 2.5; the interviews can't tell; a usage-frequency query can
```

## 9. Where it plugs in

| Agent | Takes from here | Gives back |
|-------|-----------------|------------|
| **problem-selection** | The knowledge-gap scorecard's *business impact* area scores 4–5 only with a sizing whose load-bearing leaves are at least INFERRED; breadth under the goal reading is the tier counts | The *Yes* case's segment and the evidence table rows the attach rate rests on |
| **ideation** | A routing call of *quantify* when the ledger's riskiest assumption is "the market is big enough" | The landscape scan's alternatives, which are the incumbents in the implied-share and aggregation tests |
| **customer-interviews** / ODI | The attach rate, the frequency and the price leaves need real people: interviews for the first, the survey for the second, Rule-of-Five quotes for the third | The learning goal "how often, how much, and what do they pay today" |
| **metrics** | §3d's *share touched* factor is a SAM tier; the strategy memo's initiative value cites the sizing | The baseline when the product already exists (then it is a change, not a market) |
| **prfaq** | The internal FAQ's "what's the TAM and how was it estimated?" is answered by the summary and the register, not a number | Flags the sizing's weakest leaf as `[ASSUMPTION]` |
| **lean-experiments** | The tornado's top leaf is often the next experiment card (a smoke test measures the attach rate; a concierge measures willingness to pay) | Readouts that move a leaf from BACKGROUND to CONFIRMED |
| **solution-options** / **strategy** | The SAM and the path-to-revenue count feed the option's Alignment and the initiative's value estimate; the stop-doing list follows from which tiers are excluded | — |
| **navigate** | `discovery/sizing.md` and `discovery/sizing.py` are the artifacts; a scorecard area-5 score ≥ 4 without them is a discrepancy | — |

## 10. Anti-patterns (coach's tells)

| Anti-pattern | Tell | Mechanical check |
|--------------|------|------------------|
| **"1% of a huge market"** | A bare percentage as the SOM | Every share maps to a mechanism (Damodaran's ladder) or to a path-to-revenue count; a bare percentage is rejected |
| **Analyst TAM pasted** | "Gartner says $81B" and nothing else | Analyst figures enter only as a cross-check row with publisher tier, definition, year and the leaf they test |
| **Sizing the problem, not the ICP** | "$1.1T US healthcare" for a scheduling tool; "all e-commerce" for recommendation software | The count unit is job executors or ICP accounts who could buy *this* at *this* price |
| **Trillion-dollar TAM, false precision** | "$2.5T, CAGR 17.65%" | Restate per capita or as a share of GDP or of the buyer's budget; round leaves; carry ranges |
| **Yesterday's market** (under-sizing a market-creating product) | TAM = today's served spend | Show constrained and expanded tiers; cite a measured early-cohort ratio |
| **Every conceivable customer** (over-sizing) | 255M desk workers; 67M households; every mile on earth | Run the implied-share test against the plan and the aggregation test against competitors |
| **Non-consumption ignored** | Counting only current buyers of the incumbent | Count everyone doing the job by any means — incumbent, workaround, nothing — and classify non-consumers by barrier (time, access, skill, money) |
| **New market modelled like an existing one** | A linear share line for a category that doesn't exist | Classify the type first; new markets get an S-curve from analogs and a death valley |
| **Glass-ceiling niche** | 5,000 universities × $100K = $500M presented as venture-scale | Run the $100M ladder on the wedge; show the evidenced expansion path, each adjacency its own tree |
| **Expansion story without evidence** | "Then we'll expand into adjacent segments" | Each adjacency a separate probability-weighted tree with a named analog that made the same move |
| **Unit mismatch** | Seats counted, accounts priced; installs counted, users priced; ARR vs. revenue | The register records the unit and definition of every count and price; count and price share a unit |
| **Inconsistent customer** | The sizing's ICP isn't the positioning's | One ICP string across the initiative |
| **Point estimates multiplied through** | A single TAM number with no range | Calibrated 90% ranges per leaf; Monte Carlo; 5/50/95 reported |
| **Big-market delusion** | Everyone in the category assumes they win | Sum the competitors' implied revenues against the market |
| **Reconciliation by averaging** | "Top-down says 4B, bottom-up says 1B, call it 2.5B" | Find the leaf that closes the gap; keep the better-evidenced route; or fix the definition |

## Sources & materials

- **Bill Gurley**, *"How to Miss By a Mile: An Alternative Look at
  Uber's Potential Market Size"*, Above the Crowd, 11 Jul 2014 — the
  canonical case that top-down from the existing market under-sizes a
  market-creating product; the SF ratio, the car-ownership substitution,
  the scenario math. Source: `./materials/Gurley-HowToMissByAMile-2014.pdf`.
- **Aswath Damodaran**, *"A Disruptive Cab Ride to Riches: The Uber
  Payoff"*, Musings on Markets, Jun 2014; *"Possible, Plausible and
  Probable: Big markets and Network effects"*, Jul 2014; *"The Market is
  Huge! Revisiting the Big Market Delusion"*, Dec 2019; the Uber
  valuation deck (Sept 2015) and *"Insights on VC pricing: lessons from
  Uber, WeWork and Peloton"* (Sept 2019, the 3P test and the
  constrained / expanded / overreach TAM). Sources:
  `./materials/Damodaran-*.pdf`.
- **Bradford Cornell & Aswath Damodaran**, *"The Big Market Delusion:
  Valuation and Investment Implications"*, *Financial Analysts Journal*
  76(2), 2020 (SSRN 2016) — the aggregation test; paywalled, cited via
  the abstract and Damodaran's companion post.
- **a16z**, *"16 More Startup Metrics"*, 23 Sep 2015 — the bottoms-up
  rule, "why 40%?", don't game the TAM. Source:
  `./materials/a16z-16MoreStartupMetrics-2015.pdf`.
- **Pear VC**, *"Market Sizing Guide"*, 3 Aug 2021 — customers × ARPA,
  top-down only as a sanity check, the 10–30% value-capture heuristic.
  Source: `./materials/PearVC-MarketSizingGuide-2021.pdf`.
- **Christoph Janz**, *"Five ways to build a $100 million business"*,
  5 Oct 2014 — the ladder and its funnel multipliers. Source:
  `./materials/Janz-FiveWaysToBuildA100MBusiness-2014.pdf`.
- **Jason Lemkin**, SaaStr — *"TAM is great, but what really matters is
  that you believe you can hit $100M in 7 years"* (2013) and the YC
  pitching guide. Cited, not preserved.
- **StrategyCase**, *"Market Sizing Questions: 25 Examples With Worked
  Answers"* (2023, updated 2026) — the six-step routine, the structure
  menu, the rounding and accuracy rules. Source:
  `./materials/StrategyCase-MarketSizingQuestions.pdf`.
- **Stanford Biodesign**, *"Top-Down and Bottom-Up Market Sizing
  Example"* (2022) — divergence as a reality check. Source:
  `./materials/StanfordBiodesign-TopDownBottomUpMarketSizingExample.pdf`.
- **Lightspeed** (Sebastian Duesterhoeft), *"A Total Addressable Market
  (TAM) Masterclass"* — analyst reports as a red flag, ratio benchmarks,
  the fund-return test. Source: `./materials/Lightspeed-TAMMasterclass.pdf`.
- **Jared Sleeper** (Matrix Partners), *"Calculating TAM"*,
  forEntrepreneurs — top-down, bottom-up and "value theory". Source:
  `./materials/Sleeper-CalculatingTAM-forEntrepreneurs.pdf`.
- **Steve Blank**, *"Market Definition — It's the Front End of Customer
  Discovery"* (2021) and *"Death By Revenue Plan"* (2010) — market as job
  executors + job; market types and the revenue curve. Sources:
  `./materials/SteveBlank-*.pdf`.
- **Douglas Hubbard**, *How to Measure Anything* (Wiley, 2007/2014) —
  calibrated 90% intervals, the equivalent bet, the Rule of Five,
  Monte Carlo, measurement inversion; cited via public summaries.
  **Craig McKenzie et al.** (2008) on interval overprecision.
  **MacGregor & Armstrong** (1994) on when decomposition helps.
- **Frank Bass**, *"A New Product Growth for Model Consumer Durables"*,
  *Management Science* 15(5), 1969; **Mahajan, Muller & Bass** (1995) for
  the p ≈ 0.03, q ≈ 0.38 defaults. Cited.
- **Lawrence Weinstein & John Adam**, *Guesstimation* (Princeton, 2008);
  **Barbara Minto**, *The Pyramid Principle* (MECE). Cited.
- **Madhavan Ramanujam & Georg Tacke**, *Monetizing Innovation* (Wiley,
  2016) — willingness to pay early; Van Westendorp and Gabor-Granger as
  commonly described. Cited.
- **Uber Technologies**, Form S-1 (Apr 2019) and FY2023–FY2025 results —
  the TAM/SAM disclosure and the actuals. Cited, not preserved.
- **Jahanvi Sardana** (Index), **Aydin Senkut** (Felicis), **Deena
  Shakir** (Lux), **Jomayra Herrera** (Reach), **Rotem Shacham** (PSG),
  **Alex Iskold**, **Octopus Ventures**, **Underscore VC**, **Dreamit**,
  **New Constructs** — quoted in the research report; cited, not
  preserved.
- Official statistical agencies: US Census Bureau (SUSB, CBP, NES,
  Economic Census, ACS), BLS (OEWS), Eurostat (SBS), ONS, Statistics
  Canada, OECD, World Bank; SEC EDGAR XBRL APIs.
- The definitions-by-exclusion table (§1), the market-type consequences
  (§2), the five-step bottom-up build (§3), the reconciliation tolerance
  (§5), the "simplest PM version" of Bass (§6), the register, model and
  summary templates (§7), the B2B example (§8), the plug-in table (§9)
  and the anti-pattern checks (§10) are **this repo's operational
  extension**; the research report records what is synthesis and what
  is a published standard.
- See [`../../CREDITS.md`](../../CREDITS.md) for full attribution.

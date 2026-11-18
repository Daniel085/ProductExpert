# Desk Research — Method Reference

*How the system collects what is already public — forum threads, reviews,
surveys, vendor pages, official data, the PM's own saved files — into
evidence other agents can count. A repo method: it borrows the row and
tag discipline of [affinity mapping](../problem-selection/affinity-mapping.md),
the tiers of the [assumption ledger](../customer-interviews/assumption-ledger.md)
and the scan questions of
[brainstorming §7](../ideation/brainstorming.md), and adds the parts none
of them owned: one row format, a record of what could not be reached, an
order for spending searches, and intake for files the PM supplies.*

## 1. What it is for, and what it is not

Desk research answers **"what have people already said and published
about this?"** before, or beside, talking to anyone. It produces
**observation rows** and **fact tables** with sources. It does not
group, rank, conclude or recommend: grouping is
[affinity mapping](../problem-selection/affinity-mapping.md), verdicts
are [problem-selection](../problem-selection/picking-the-right-problem.md),
and options are ideation.

**Everything it produces is BACKGROUND**, however many sources agree.
Nobody was asked, so nothing could be probed; the searches chose what was
found. It can end a theory early (a claim with no trace anywhere), sharpen
an interview guide, and tell problem-selection where to look. It can
never carry a *Yes* (`picking-the-right-problem.md` §2, step 4).

## 2. Spend searches on the riskiest assumption first

Search and fetch allowances run out. Before the first query, read the
ledger and write the **query plan**: the questions in the order the
initiative needs them answered.

1. The riskiest assumption's *what would disprove it*.
2. The other ledger rows, by impact × uncertainty.
3. Breadth: adjacent topics, context, nice-to-know.

Spend in that order. When the allowance ends, list every planned question
that got no search under *Not searched* (§5), so silence in the notes can
be told apart from absence in the world.

## 3. The observation row

One format for every note that holds what a person said, whatever the
source. Rows are numbered once across the initiative (note 2 continues
where note 1 stopped), so any later artifact can cite a row by number.

| # | Source | Tag | Date | Who is speaking | Observation | Number stated |
|---|--------|-----|------|-----------------|-------------|---------------|
| 41 | S7 | [T] | 2026-03 | café owner, two sites | Changed produce supplier after three late deliveries in a month; now phones the order in before 6am to be sure of it | 3 late deliveries; 1 month |

- **One row per distinct thing a person did, paid, experienced or
  decided.** Prefer past behaviour and stated numbers to opinion; keep an
  opinion only where it is a stated decision ("I stopped paying for X").
- **Close paraphrase, one short quote at most** where the wording
  matters. Never a username, a personal name or an organisation's name.
- **Who is speaking** is the role as they state it, or *unknown*. Do not
  infer a segment from tone.
- **Tags** say how far the row is from the speaker:

| Tag | Meaning |
|-----|---------|
| `[T]` | Read in full where the person wrote it (a thread, a review, testimony) |
| `[A]` | Quoted or relayed by an article or report that cites it |
| `[S]` | A search snippet or title only; the page was not opened or refused |
| `[AI]` | Stated by a machine summary of other people's words; not traceable to a speaker |
| `[V]` | Said by someone who sells to the people being studied |

`[V]` rows are kept and **counted apart**: a vendor's account of its
customers' pain is a claim about a market, never customer signal.
`[AI]` rows are filed sparingly, only where no traceable row covers the
point.

- **A source table** heads each note: one line per source read, with an
  id, where it is from, its date (a relative date converted and marked
  *approx.*), how much of it was visible, anything wrong with the copy
  (cut off, comments collapsed, garbled), and **who it leaves out** (§3a).

### 3a. Who each source leaves out

Every public source selects who speaks. Write the selection beside the
source, in a few words, before filing a row from it:

| Kind of source | Who is over-counted | Who cannot appear |
|----------------|---------------------|-------------------|
| A complaints-led review site | The aggrieved | The content majority |
| A review site that invites reviews | Customers the vendor asked | Those who left without a word |
| A review of the product someone moved **to** | People who finished switching | Those who wanted to switch and did not, or tried and gave up |
| A practitioner forum | People with a problem that week | People for whom it works; people not on that forum |
| A vendor's survey | The vendor's own list | Non-customers |
| The team's own organisation | One case | Everyone else |

Two rules follow.

- **Never let one source of a kind stand for the kind.** A rating, a
  complaint rate or a "most people say" from one review site is filed
  with a second site of a different selection beside it, or marked
  *single source of its kind* in the source table. Two sites that share
  one data set (a group's sister sites) are one source.
- **Name who the question is really about, and say whether they can
  appear.** When the people a ledger row turns on are exactly those a
  source cannot contain, say so in the note's header and put the
  question under *Searched and not found* with the reason: it is a
  question for interviews.

## 4. Fact tables and the coverage matrix

Facts that are not a person speaking (prices, rules, counts, survey
figures) go in tables of their own: *Fact · Value · Source · Who
publishes it (independent / vendor) · Date · How it was read (page
opened / snippet only)*. A price carries the date it was seen. A vendor's
survey is marked as a vendor's.

A competitive teardown ends in one **jobs × coverage matrix**: a row per
job the customer has to get done, a column per kind of provider, product
names in the cells, and a last column **Nobody found (what I searched)**
holding the exact queries behind each absence. An absence resting on one
or two searches is a weak absence and is written as one.

### 4a. Counting a field across a public site

Some sites publish a structured field on every record: what a reviewer
switched from, the size of their organisation, a rating by year. Counted
across the whole site, one field can answer a ledger question no thread
will. It is still BACKGROUND, and it has rules of its own.

- **Read the site's terms on automated access first.** If they forbid
  it, page by hand, or ask the PM to; say which in the note.
- **Public pages only**, signed out unless the PM said otherwise. One
  request at a time, with a pause between. Stop at the first refusal or
  human-verification check; it is a rung of the access ladder, not an
  obstacle.
- **Keep counts, not people.** No reviewer names or handles leave the
  page; a kept sentence is a close paraphrase or a short quote with no
  identifying detail.
- **Report the denominator every time:** records read of records that
  exist; how many carry the field; the date range of those that do; and
  where reading stopped and why.
- **Report both directions** when the field is a flow (switched from,
  moved to): arrivals as well as departures, for the same products.
- **State who the field leaves out** (§3a) in the sentence that gives
  the count.

The output is a fact table (*Product · Records read · With the field ·
Count · Share*) and, where text sits beside the field, observation rows
in the usual format.

## 5. What could not be reached

Every note ends with three lists. They are part of the evidence, not an
apology.

- **Refused or failed:** each source that would not open, with the
  result (blocked, sign-in wall, error) and what was used instead.
- **Not searched:** planned questions the allowance did not reach.
- **Searched and not found:** questions asked with nothing located, with
  the query. This is the only one of the three that is evidence of
  absence, and only weak evidence.

## 6. The access ladder

Try each rung once, in order, and record which rung reached the source.
Never work around a refusal: no alternate front-ends, no cached copies of
a page that refused, no human-verification checks clicked through.

1. **Fetch** the page directly.
2. **A browser the agent controls**, where the session has one.
3. **The PM's own browser**, with the PM's go-ahead, signed in as they
   are.
4. **The PM saves the pages** and drops them in
   `discovery/notes/raw/`. The agent supplies the exact searches or
   addresses to save.

A source refused on every rung goes in *Refused or failed*. Paid data
sources are never used without the PM's say-so, whatever credentials are
at hand.

### 6a. Preflight: find out what will fail before spending anything

Before the first search, test the environment and report it in one
table, each line with its fix. A failed line is not a blocker; it is a
rung the PM can open in a minute now instead of an hour in.

| Check | How | If it fails |
|-------|-----|-------------|
| The raw folder is readable | List it and open one file | The PM moves the files inside the initiative folder, or grants access |
| Saved pages can be turned into text | Extract one PDF and one HTML file | Name the missing tool; ask before installing anything |
| Search and fetch are available, and how many remain | One query, one fetch | Shorten the query plan to the riskiest rows |
| A browser the agent controls | Open one public page | Rung 2 is skipped; say so |
| The PM's browser, and what it is signed in to | Ask; never sign in yourself | Rung 3 is skipped for those sites |
| Sources this topic depends on that are known to refuse | One fetch each of the two or three forums or review sites the plan leans on | Give the PM the exact searches to save, up front, not after the allowance is spent |

## 7. Intake of files the PM supplies

Saved pages arrive imperfect. Before filing any, run the intake check and
report it in one table:

| Check | What to look for |
|-------|------------------|
| Readable | The text extracts; an image-only or empty file is reported, not guessed at |
| Right page | The title and first lines match what the file name says it is |
| Duplicates | Identical or near-identical files; read one, name the others |
| Complete | Whether the page states more comments or reviews than are visible (saved signed out, collapsed threads) |
| Kind | A full thread, a search-results page, or a machine summary: each files under a different tag |
| Private data | Names and handles are dropped on filing; the raw files stay out of version control |

Ask the PM once for whatever fails (a re-save, signed in, comments
expanded), with the list in one message, and file the rest meanwhile.

## 8. Anti-patterns

| Tell | What it looks like | The fix |
|------|--------------------|---------|
| **Volume as proof** | "Dozens of threads say…" | Count distinct speakers, by role; one thread is one conversation |
| **Vendor ventriloquism** | A problem "everyone has", sourced to people who sell its cure | Tag `[V]`, count apart, look for the same pain in a customer's words |
| **Silent gaps** | A topic missing from the notes with no word on whether anyone looked | The three lists in §5 |
| **Breadth before risk** | The allowance spent on context; the riskiest assumption unsearched | The query plan in §2 |
| **Summary as speaker** | A machine summary quoted as what practitioners think | Tag `[AI]`; fetch the thread it summarises |
| **The conclusion in the note** | "This shows the market wants…" | Notes hold rows and facts; problem-selection draws the verdicts |
| **One site as the market** | "Users rate it 2.4", from the site people go to when angry | A second source with a different selection beside it, or *single source of its kind* (§3a) |
| **Survivors as everyone** | "Nobody found the move hard", from people who completed it | Say who cannot appear in the source; route the question to interviews (§3a) |
| **A count with no denominator** | "20 reviewers switched from X" | Records read, records with the field, date range, both directions (§4a) |
| **Finding the wall late** | The forum refuses after the allowance is spent | Preflight (§6a) |

## Sources & materials

- The row, tag and distinct-source discipline extends
  [`../problem-selection/affinity-mapping.md`](../problem-selection/affinity-mapping.md).
- Evidence tiers: [`../customer-interviews/assumption-ledger.md`](../customer-interviews/assumption-ledger.md).
- The four scan questions and teardown depth:
  [`../ideation/brainstorming.md`](../ideation/brainstorming.md) §7.
- The query plan, the three lists, the access ladder, the intake check,
  the selection table, field counting and the preflight are this repo's
  own, written after running the system on an initiative whose first
  evidence was all public.

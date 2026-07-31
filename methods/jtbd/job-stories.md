# Job Stories — Method Reference

*Distilled from **Product Institute's "Product Management Foundations"**,
Unit 4 ("Identifying the Problem"), Lesson 4.2 *Jobs to Be Done* — source
worksheet preserved in [`./materials/`](./materials/). The job-story format
was developed at **Intercom** and articulated by **Alan Klement**; user
stories originate with **Kent Beck**, the "As a…" template with the
**Connextra** team. See [`../../CREDITS.md`](../../CREDITS.md).*

> **Where this sits vs. `methods/odi/`:** both are Jobs-to-be-Done, at
> different altitudes. A **job story** frames a need for conversation,
> backlogs, and problem statements. An **outcome statement**
> ([`../odi/outcome-statements.md`](../odi/outcome-statements.md)) frames a
> need for quantification. They convert (see below). Use job stories when
> you need shared understanding fast; use the ODI pipeline when you need to
> measure and rank.

## The format

```
When I am (in a situation),
I want to (motivation),
so I can (achieve an outcome).
```

- **Situation** — the triggering context, specific enough to picture
  ("when I find a product I like but I'm not ready to buy it yet").
- **Motivation** — what the person is trying to accomplish *in that
  situation* — never a feature.
- **Outcome** — the observable change in their life if it goes well
  ("come back and purchase it without searching again").

## Why job stories instead of "As a user…"

**JTBD replaces attributes with situations.** Personas frame customers by
who they are; jobs frame them by what they're trying to get done — which is
what actually predicts behavior, and which still works when your audience
is too wide or varied to compress into clean personas (the framework was
created partly to combat weak personas). "As a user" carries almost no
information; "when I'm at a multi-track conference and two talks I care
about overlap" carries everything you need.

**User stories drifted from their intent.** Kent Beck's original idea was
stories about *why* users needed something — placeholders for a
conversation. In practice the template calcified into mini-requirements:

> *"As a user, I want a button so I can sign up."*

No user wants a button — they want access. The button is the solution, not
the problem. **A customer's problem is never your lack of a feature.**

**Removing the solution reopens the conversation.** With the feature-noun
deleted, the team can discuss *multiple* ways to solve the actual problem
instead of getting stuck specifying one.

### Worked contrast (the wishlist)

| | |
|---|---|
| **User story** | "As a user, I want to save items to a wishlist, so that I can buy them later." |
| **Job story** | "When I find a product I like but I am not ready to buy it yet, I want to save the product for later, so that I can come back quickly and purchase it without searching for it again." |

The user story bakes in the wishlist. The job story captures situation,
motivation, and outcome — and a wishlist, saved-for-later cart, email
reminder, or price-drop alert could all compete to serve it.

## The tells (when to rewrite)

Treat any of these as a trigger to rewrite the story:

1. **A solution-noun inside "I want".** Workshop, schedule, coach, wishlist,
   dashboard, button — if the want names an artifact, the need is hiding
   behind it.
2. **"Better X."** "A better event feature" is a solution plus an adjective;
   the need is whatever "better" would do for the person.
3. **A contentless persona.** "As a user / as a PM" — replace with the
   triggering situation.
4. **A third-party beneficiary.** "I want X *for them* so *they* can…" —
   the writer's own job is hidden; find it (what friction is the writer
   actually experiencing?).
5. **The outcome restates the feature.** "…so that I can use the wishlist"
   circles back; the outcome must be a change in the person's life.
6. **The real need is sitting in the outcome clause.** Often the "so that"
   of a bad user story is nearly the need already — promote it, then find
   the situation behind it.

## Rewrite protocol

1. **Delete the solution-noun** and ask what it was *for* (why-ladder until
   you hit a motivation that doesn't name a feature).
2. **Find the triggering situation** — when does this need actually fire?
   Recent, real, specific.
3. **Make the outcome observable** — what would be visibly different for
   the person?
4. **Check altitude** — job stories frame *problems and opportunities*, not
   dev tasks. One story per real need; implementation still gets broken
   down into ordinary tickets afterward.
5. **Re-read for smuggled solutions** — including in the situation clause.

## Worked exercise (from the Product Institute worksheet)

| # | User story | Job story (worked answer) |
|---|-----------|---------------------------|
| 1 | As a Product Manager, I want a workshop on Jobs to Be Done, so that I can learn how to create better products. | When I'm deciding what to build next and my recent features haven't been adopted the way I expected, I want to get better at uncovering what customers are actually trying to accomplish, so I can build products they use instead of ones they ignore. |
| 2 | As a conference attendee, I want the schedule, so that I can know who is speaking when. | When I'm at a multi-track conference and sessions I care about run in parallel, I want to know which talks matter to me and when and where they happen, so I can be in the right room and leave having seen the sessions I came for. |
| 3 | As a Product Manager, I want a coach for our CMO, so that they can understand better work tactics. | When the CMO hands my team tactics that conflict with how effective product work happens, I want us to reach a shared way of working, so I can ship the right things without constant friction and rework. |
| 4 | As a Facebook user, I want a better event feature, so that friends actually see my invitations. | When I'm organizing an event and invite my friends, I want to be confident every invitee actually notices the invitation, so I can get real answers and enough people show up on the day. |
| 5 | As a London tube rider, I want larger trains, so that I don't get squished. | When I ride the tube at rush hour and the carriage is packed, I want enough personal space for the journey, so I can arrive at work comfortable rather than stressed before the day starts. |

What the exercise demonstrates: every "I want" noun was a solution
(workshop, schedule, coach, feature, larger trains); #3 hides the writer's
need behind a third party; #4's real need was sitting in its outcome
clause; and each rewrite **widens the solution space** — #5's job could be
served by larger trains, but also by more frequent service, better platform
load-spreading, real-time crowding info, or off-peak incentives.

## Two more JTBD moves worth keeping

- **Products serve multiple jobs.** Facebook is hired to keep in touch with
  family, share interests, and read what friends curate — enumerate the
  jobs, don't average them.
- **Pre-launch, study the incumbent workaround.** If your product isn't out
  yet, dig into why people "hired" the current subpar solution — the
  spreadsheet, the group chat, the string on a finger. The workaround is
  evidence of the job and of what switching must beat.

## Conversions (how this plugs into the system)

- **Insight → job story.** A Track 1 insight ("[segment] do/feel X because
  [why]") becomes a job story by casting the *why* as motivation inside its
  triggering situation. Use it when synthesis output needs to feed a
  backlog or a PR/FAQ.
- **Job story ↔ outcome statement.** The outcome clause, made measurable,
  is an ODI outcome statement: "so I can come back and purchase without
  searching again" → *"minimize the time it takes to re-locate a previously
  identified product."* Going the other way, outcome statements ground a
  job story's "so I can" in something already validated.
- **Job story → PR/FAQ problem paragraph.** The problem paragraph of a
  press release is a job story in prose — situation, motivation, outcome,
  no feature smuggled in.
- **Job story → experiment.** "We believe that [people in situation] want
  [motivation]…" — the story is the belief; the experiment tests it.

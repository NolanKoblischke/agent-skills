---
name: know-your-audience
description: Interview a scientist about one audience and add a register for it to their personal communication skill — creating that skill if it does not exist yet. Use whenever someone is defining a new audience, joining a new collaboration, taking on a new role, or says "create a communication skill for X", "define how the agent writes for Y working group", "add my advisor as an audience", "set up a reader profile for my student", "define my audience", "set up how you talk to me". Also use to re-interview and update an audience already on file.
---

# Audience definition

Your role: understand who the agent will be writing to and how the user
wants that communication to go, combine that understanding with general best
practices, and turn it into a durable register. **The author is always the
agent.** The user is always the interviewee. The reader is a human: the user
themselves, or someone the agent writes to on the user's behalf — an
advisor, a working group, a student.

The product is the user's **single communication skill**. Its body carries
what is universal to the user — sign-off, voice, approval rules, the
constant principles — plus an index of audiences. Each audience is one
reference file beside it. One interview creates the skill; every later
interview adds one audience file. Ten audiences, one skill, nothing
duplicated.

**The user wants a draft they can edit. They never want to write it
themselves.** Ask few questions, ask them well, generate something
opinionated and concrete, and be explicit about what you guessed.

This skill is self-contained. The reader-role priors are in
[`references/priors.md`](references/priors.md); the two skeletons are in
[`assets/body-template.md`](assets/body-template.md) and
[`assets/audience-template.md`](assets/audience-template.md). Nothing
outside this directory is load-bearing.

The steps, in order:

1. **Read the priors — and the user's existing skill, if there is one.**
2. **Interview** — opening with scope and audience, paced by the user.
3. **Synthesize a profile and repeat it back** — iterate until the user
   recognizes it.
4. **Generate** — create the skill, or add one audience file to it.
5. **Hand over.**

## 1. Read the priors

Read [`references/priors.md`](references/priors.md) before interviewing. It
describes five priors — `audience-student`, `audience-collaborator`,
`audience-advisor`, `audience-prompter`, and `team-norms` (etiquette for
shared surfaces, not a reader) — each in full: reader model, register,
failure modes, and (for the student) pedagogy moves with time gates. It also
gives the two axes — what a reader knows about the field vs. what they know
about the project's day-to-day — used to place a "something else" answer.

Priors are non-exhaustive, non-exclusive, and no reader fits one perfectly.
They inform the interview: they tell you what to listen for and which
follow-up matters. Each audience file is a **specialization of a prior, not
a fresh essay** — that is what keeps ten of them consistent with each other.
Where the interview contradicts the prior, the interview wins.

Then look for the user's existing communication skill (ask, or check the
usual homes). If it exists, read it: the universal preferences are already
on file and are not re-asked; the new interview only has to cover what is
specific to this audience.

## 2. Interview

Two questions always come first, then the track splits on the second
answer. Ask in small batches — two or three per turn, not a form. Reflect
back what you heard. Stop early when you have enough.

**How to ask.** When a multiple-choice tool is available (Claude Code's
`AskUserQuestion`), use it for every enumerable question — options plus an
"other" escape beat a prose list the user must re-type from. Story-shaped
questions (incidents, examples) stay in prose; they need room, not
options. And the interview must not itself commit the failure it exists to
fix: define any term of art inside a question at first use, or use plain
phrasing — ask "how do you want the information structured, and in what
format?", not "what shape do you want?".

**Pacing.** Open by saying the questions run in decreasing importance and
the user can pause, skip, or stop at any point; then read the pacing from
their answers. Short answers, skipped questions, "let's move on" — stop
and synthesize. A short interview makes a thinner file with more marked
guesses; say so when you stop early, so the user knows that is what they
are buying.

**Q1 — scope. Ask it first.**

> **Is this for the project we're in right now, or for all your
> communication, globally?**

The answer does two jobs. It settles where the skill lives (see the
location rules in step 4's note below — global `~/.claude/skills/
communication/` vs. project `.claude/skills/communication/`; the two
layer, project sharpening global). And either way, pause before asking
anything else and reflect on what you already know about the user — their
CLAUDE.md, memory, how they have worked with you — plus, when the answer
is *this project*, the project's context: CLAUDE.md, README, the recent
work. Every later question gets sharper when you hold who the user is and
what the work is about, and the audience file can use the real nouns.

**Q2 — who will the agent be writing to, and in what context.**

> **Is this about how the agent communicates with you — the register you
> want in your own chat — or about the agent writing for a defined
> audience on your behalf? Who is the reader, what is their role, and
> what is the context of the work?**

### Track A — the reader is the user

First-hand and reliable; use their words. This register applies to *every
message the agent sends them*, so its natural home is the global `CLAUDE.md`
/ `AGENTS.md` rather than a file that must trigger (offer both in step 4).
If what they want is to *learn* — not just be talked to well — combine the
interview with
[`references/learning-prompt.md`](references/learning-prompt.md), the
strongest known student-register prompt; its moves are time-gated.

Two questions, verbatim — do not paraphrase them into your own voice:

**A1 — gap handling** (the teaching-vs-briefing dial):

> **When you hit something you don't know, do you want the answer, an
> explanation of the topic, or a question that gets you there?**

**A2 — parsing failure** (the richest question — push for a specific
incident, **unless the user is signalling haste, in which case skip it**):

> **Tell me about the last time AI-assisted work was difficult to parse. What
> is one actionable thing that would have helped with comprehension?**

If the interviewee is settling in rather than rushing, also ask questions
from Track B where the audience is the interviewee. Use judgement to guide
the conversation. In both tracks, you don't **have** to ask every question.

### Track B — the agent writes to someone else

The user is describing a reader who is not them. Their answers about the
audience are a model, not ground truth: the audience file states whose model
it is and marks the guesses. When a slot needs the reader's own answer (how
long they give one artifact, what *they* find hard to parse) and the user
cannot supply it, leave it unknown and say so.

**B1 — the audience** (this picks the prior; "something else" is the most
useful answer):

> **What audience are we writing for here — an advisor, a peer, a student,
> or something else?**

Alongside it, one line of context: which collaboration, which surfaces (PRs,
issues, Slack, reports, talks).

**B2 — shared context and assumed knowledge:**

> **What is the technical or scientific context, and what can you assume
> this audience already knows about it?**

Invite the split between field and project — "my DESI peers know BAO cold,
but not the details of my mocks" is exactly the shape you want.

**B3 — thoroughness:**

> **Does this audience want every statement justified — numbers, plots,
> receipts — or a high-level summary they can skim?**

**B4 — AI norms:**

> **Does this audience have norms about AI usage or its disclosure?**

A link to an existing collaboration document is the ideal answer. Offer
examples of the kind of thing that counts — "don't review PRs where your
review wasn't requested", "edit the PR body instead of commenting on every
change" — and make skipping easy: this question matters, but the user should
never have to draft their collaboration's AI policy on the spot.

**B5 — will they push back?**

> **Will this audience have the experience and confidence to push back on an
> overconfident or incorrect statement, or will they tend to accept the text
> as truth?**

This sets more than a hedging dial. A high-pushback reader is part of the
error-correction loop — thinking out loud is safe and useful. A low-pushback
reader builds on whatever you write, so the text must carry its own
error-correction machinery: confidence differentiated visibly (the verified
claim and the guess must not sound the same), a smaller claim surface, and
receipts — the link, the plot, the command that reproduces the number — so
the reader can *check* what they cannot challenge from expertise.

**B6 — what should they be able to do afterward?** The point of the
communication, in the user's words: "decide whether to fund it", "reproduce
it next month", "not be lost in the group meeting".

**B7 — one norm an outsider would get wrong**, and one thing that has
annoyed people here.

**B8 — real examples.** One thing written for this audience that landed, one
that did not. Two real samples beat twenty adjectives.

When the user is settled in, also ask the Track A questions in
reader-facing form: what does this *reader* want at a gap; when did this
*reader* find agent output hard to parse.

The list runs in decreasing importance — go down it as far as the user's
patience allows, and stop the moment they want to stop. At the hastiest,
B1 and B2 alone make a usable (thin) file; when the user lingers, walk
the draft line by line at the end.

## 3. Synthesize the profile, repeat it back

Pause before writing anything. Collect what you heard into a short profile:
which prior is nearest, where this reader departs from it, the register that
follows. Mapping notes:

- **B1 names the reader, and the reader picks the prior**: advisor →
  `audience-advisor`, peer → `audience-collaborator`, student →
  `audience-student`. "Something else" gets placed via the two axes in
  `references/priors.md`. Sanity-check the direction: the prior describes
  the *reader's* position relative to the user — a WG lead's working group
  lands on student or collaborator, never advisor.
- **Plural audiences:** name the nearest prior for the *typical* reader, call
  it approximate, add one line on who else is in the room. Do not stack
  priors.
- **The reader's `Time:` slot is how long that audience gives one
  artifact** — nothing to do with how patient the user was in the
  interview. When the reader is the user they are close; otherwise ask, or
  leave the slot out.

Then repeat the profile back in two or three lines — "writing for: a peer,
no context on your last week, ten minutes, wants to decide whether to rerun
their half; correct me if that is wrong" — and iterate until the user
recognizes it. This is cheap and it catches a mis-model before anything is
built on it.

## 4. Generate

**Where the skill lives** falls out of the Q1 scope answer — confirm it,
don't re-ask:

- **Global** (`~/.claude/skills/communication/`) — live everywhere
  immediately. The usual answer.
- **Project** (`.claude/skills/communication/`) — when the scope answer
  was *this project*. The two layer: the project skill sharpens and
  overrides the global one where they meet.
- A **user-facing** register (Q2) applies to every message, so offer the
  global `CLAUDE.md` / `AGENTS.md` as its home instead of, or alongside,
  the skill.

If the communication skill already exists, its location is settled.
Audience files describe real, named colleagues — **never write one into a
shared git repo without the user's explicit permission.**

What you write depends on what exists:

- **No communication skill yet** — create it from
  [`assets/body-template.md`](assets/body-template.md): universal
  preferences from the interview, the constant blocks verbatim, an index
  with one row. Then the first audience file.
- **Skill exists** — add one audience file, one index row, and append this
  audience's trigger phrases to the frontmatter description. Touch nothing
  else: the user's own edits are the most valuable content in the file.
- **Audience already on file** — this is a re-interview; see below.

Write each audience file from
[`assets/audience-template.md`](assets/audience-template.md) and the chosen
prior, out of your **holistic understanding of the profile** — the user,
their role, and who the reader is. This is not a mechanical mapping of
answers onto template slots; the template is a skeleton, and the profile is
what animates it. The templates are raw: everything in `{{ }}` is a slot,
everything outside is constant and copies through verbatim. Universal
content goes in the body, once; audience content in the audience file;
nothing in both.

Rules:

- **Never write a line in the voice of a user answer unless the user said
  it.** A guess dressed as a fact is the one output that makes this skill
  worse than nothing. Each slot has three honest states: filled from an
  interview answer; filled from the prior and **marked** `<!-- from prior:
  audience-X, not confirmed -->`; or replaced by a one-line
  `<!-- unasked: … -->` comment so the re-interview picks it up. Under a
  short interview most slots are the second and third kind — that is fine;
  unmarked is what is not. Say so plainly in the audience file's
  `## Confidence in this model` section.
- **Every line is traceable to the user or to a named prior** — if you can
  point at neither, cut it. Prefer the user's own words: they survive edits
  that a paraphrase would not.
- **Respect the mode.** Most external audiences are reached through one-shot
  artifacts, not conversation — an artifact cannot ask the reader a question
  and wait. The template's mode line records this; register rules and
  teaching moves must fit it.
- If the reader is student-shaped, copy the pedagogy moves from the Student
  section of `references/priors.md` that pass **both gates**: the reader's
  time budget (not the interview's) and the mode — interactive moves need a
  live exchange, artifacts get the structural ones.
- Anything a prior or `team-norms` contributes gets inlined — the generated
  files never point back at this repo.

Craft rules: the skill's description routes every audience, so keep each
clause concrete — the collaboration, the surfaces, the phrases the user
types (lean slightly pushy; agents undertrigger). Body short, audience files
under ~120 lines — each is read in full when it fires. Imperative voice.
Explain why instead of stacking MUSTs. Do not overfit to one anecdote. 

## 5. Hand over

Five things, no ceremony:

1. Where the file is; if global, it is already live.
2. The reader model quoted inline, with "correct me if that is wrong."
3. The two or three lines you were least sure about, named as guesses.
4. One trigger phrase they can try right now.
5. "Come back in three months when you know this group better and we
   regenerate it."

Then stop. Do not walk them through the file — they will read it. Never ask
the user to write a section themselves; if a slot is empty, ask one more
question or cut it.


## Failure modes

- **Interrogation.** Twelve questions to a person whose answers have been
  getting shorter for three turns.
- **Generic output.** It may fit any number of teams, but specificity 
  should be used when appropriate. A team's project nouns can appear.
- **Guessing to fill the template.** Empty is honest; invented is not.
- **Ignoring the prior.** Ten unrelated registers instead of ten
  specializations.
- **Importing the user's patience into the reader model.** A hurried
  interview is not evidence about the working group's reading habit.
- **Handing back an essay.** They asked for a file, not a lecture about it.
- **Slop.** No "Great question!", no "comprehensive framework", no bullets
  restating their own headings.

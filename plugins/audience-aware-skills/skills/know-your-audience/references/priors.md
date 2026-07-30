# Priors: common roles in science

**Non-exhaustive, non-exclusive, and no reader fits one perfectly.** These are
broad strategies for broad groups — useful because most readers sit *near* one,
wrong because none sits *on* one. A prior is where you start when you know
nothing else. The interview is what turns it into a reader profile:

```
role (prior)  →  short interview  →  reader profile (posterior)  →  register
```

Where the interview contradicts the prior, the interview wins. Say so in one line
when you hand over.

## The two axes

Two things get collapsed constantly, and collapsing them is the most common
modelling error:

- **Knowledge entering** — domain expertise. What they know about the field and
  the methods, independent of this project.
- **Context held** — day-to-day project state. Which run is which, what broke
  last week, what was decided on Tuesday.

A reader can be world-class and still not know which run is which.

| | **Low context held** | **High context held** |
|---|---|---|
| **High knowledge** | Collaborator (peer, no trench time) | Advisor (holds the big picture, not your week) |
| **Low knowledge** | Student | Prompter (knows the goal, not the work) |

Read the corners as tendencies, not definitions. The advisor is high on context
in the *strategic* sense and low in the *operational* one — which is exactly why
a 2×2 is a sketch and a profile is the real thing.

A third axis runs under both: **ability to push back**, which sets the
uncertainty rule. It correlates with knowledge but is not the same thing — the
prompter knows little of the work and can still challenge intent instantly.

Roles are ultimately defined by **goals**, not knowledge. The student's role is
not "knows less"; it is "wants to be able to answer questions about this
afterward". That goal is what makes scaffolding right for them and wrong for the
advisor.

---

## Student

**When this prior fires.** The *reader* is student-shaped: the role answer is
Student, or the reader-facing gap answer is "a question that gets me there".
In second-hand mode the author's own gap answer triggers nothing — a WG lead
who personally likes Socratic treatment does not make their WG a class.

**Reader model.** Knows less about *this specific thing* — the only safe
assumption; they may know more than the author about something adjacent. Does not hold
your context, your notation, or the six months of dead ends that made the current
approach obvious. Absorbs roughly one new concept at a time, anchored to
something they already hold. They want to **understand**, which is not the same
as wanting to be **told**; being told feels like progress and usually is not.

**Lead with.** A question, not a conclusion — "before we look, what do you think
happens to the noise if we double the exposure time?" A wrong prediction is the
cheapest teaching moment there is. Then scaffold the reveal in three levels:
(1) the shape of the answer — what kind of thing is it; (2) the mechanism — why
it works that way; (3) the details — numbers, edge cases, notation. Stop at 1 or
2 and check. One unknown per sentence; define on first use in six words or fewer.
Name where they are: a short visible map of covered / next / skipped.

**Withhold.** The answer, until they have reached for it — not forever and not
coyly; ask, leave room, then answer, and answer immediately if they say "just
tell me". Withhold "as you know", "obviously", "simply" — these teach students to
hide confusion. Withhold ceremony and congratulation. Say instead what you are
*not* covering ("we are treating the covariance as diagonal here — it isn't, and
that matters, but not yet"), so they do not build a model they must demolish, and
be honest about difficulty: "this part is genuinely confusing" is useful,
false reassurance is not.

**Uncertainty cost — highest.** They cannot push back cheaply: they lack the
knowledge to detect the error and they will build on it. Either be very sure, or
say plainly that you are not. "I think this is right but I'd check it" is a
complete sentence.

**They know less; they do not think less.** Critical-thinking potential is not
role-gated. A naive question is not a gap to close — it comes from outside the
lock-in. Welcome the reframe ("why do we even do it this way?") instead of
steering back to the lesson plan.

### Pedagogy moves

Distilled from the strongest known student-register prompt in the wild (a
learning prompt written for code-review sessions; transcribed in full at
[`learning-prompt.md`](learning-prompt.md)). Its known
cost is **time** — a group member abandoned it purely on that, so the moves are
gated by the **reader's** budget, not the interview's.

**The moves are also gated by mode.** The prompt was written for live
sessions, but most external communication is a one-shot artifact — a PR
description, a report, a wiki page — that cannot ask the reader a question
and wait. The interactive moves (restate first, mastery gates, quiz,
do-not-end-until-verified, the ledger) require an exchange. Artifacts get
the structural ones: drill the whys, layer the reveal (shape → mechanism →
details, so the reader picks their own stopping depth), say what is skipped,
and the five-minute version. Copy only what passes both gates.

Interactive — live exchange only:

- **Restate first.** [15+] Proactively have them state their current
  understanding before you explain. Explain into the gap, not into the void.
  Offer the register dial they may ask for anyway: eli5 / eli14 / explain-like-an-intern.
- **Do not end until verified.** [15+] The session ends when they have
  demonstrated the understanding, not when you have finished explaining. Short
  form at fifteen minutes: name the one thing they should be able to do, check
  that, stop.
- **Incremental mastery gates.** [1h+] Confirm mastery of the current step before
  the next — high level (motivation) and low level (logic, edge cases). Do the
  checking *as you go*, not all at once at the end.
- **Comprehension ledger.** [1h+] A short, visible, running checklist of what
  they now understand. Three lists:

  ```
  Holds:      (confirmed by a passed check, not by silence)
  Shaky:      (partly got it, or you have not checked)
  Deferred:   (named, deliberately skipped, will come back)
  ```

  Only a passed check moves something to Holds — explaining is not evidence.
  Check the ledger before introducing a concept that rests on something Shaky.
  Show it to the reader; it doubles as the "name where they are" map. Rewrite it,
  do not append.
- **Quiz without revealing.** [1h+] Open-ended or multiple choice; vary where the
  correct answer sits; do not reveal until they have committed. Show code, or
  have them use the debugger, if that is the material.

Structural — works in one-shot artifacts too:

- **Drill the whys.** [15+] Problem → why it existed → the branches considered.
  Then solution → why that one → design decisions → edge cases. Then the broader
  context: why it matters, what it changes downstream. Keep asking why one level
  deeper than feels necessary. Understanding the *problem* is imperative; what
  and how come after.
- **Layer the reveal.** [15+] Shape of the answer first, the mechanism second,
  details last — in an artifact the reader chooses their own stopping depth,
  so the order of the document does the job the check-in would do live.
- **Say what is skipped.** [always] "We treat the covariance as diagonal here —
  it isn't, and that matters, but not yet." Prevents the reader from building
  a model they must later demolish.

**Five-minute version** [always — and at two minutes it is the whole teaching
section]. Not a compressed tutorial; a different artifact: (1) what kind of thing
this is; (2) the one mechanism that carries the rest; (3) the single thing people
get wrong; (4) one line — "the part we skipped is X, that is where to go next."
No prediction prompts, no ladder, no ledger. Say which mode you are in.

**Good comprehension checks**, in rough order of usefulness: prediction ("what do
you expect if we change X?"), transfer ("where else have you seen this
pattern?"), explain-back ("how would you say this to someone else?"), boundary
("when would this stop working?"). Weak checks: "does that make sense?" (always
yes) and "any questions?" (chills the room). If a check reveals a gap, do not
repeat the same explanation louder — find a different anchor.

**Failure modes.** Socratic overload (endless questions with no payoff is a
hostage situation — two or three exchanges, then deliver). Fake scaffolding
(announcing a slow build and then dumping). Assuming beginner-at-everything.
Refusing to just answer when the person needs the fact. Steering past the
reframe. Ledger by assertion.

---

## Collaborator

**Reader model.** A peer: same rough expertise, same team, same scientific goal.
A postdoc down the hall, a student on the other half of the project, faculty who
are not your advisor. **The gap is not knowledge — it is trench time.** They have
not fought your bug for a week and do not hold your local state. Assume they hold
the project goal, the broader context, the standard methods, the vocabulary, and
why the work matters. Never assume they hold which run is which, which branch is
live, or why you are three levels into a covariance rabbit hole.

**Lead with.** Where the work stands and what it means for the shared goal —
then, above your own narrative, what changes *for them*. Offer depth rather than
delivering it: "the messy part is the covariance conditioning — say the word and
I'll go into it." Name your state as you use it: "Run 04 (the one with the
apodized mask)" costs six words and saves a message. Ask real questions — "have
you hit this before?" is a good use of a colleague and a bad use of a student.
Length: a few paragraphs, expandable, detail linked.

**Withhold.** The trench narrative — the chronology of what you tried Monday
through Thursday. Method tutorials and background. Private names left unglossed.
Formality: a polished claims-and-evidence document is the wrong artifact for a
colleague and costs you speed. Do **not** withhold the thing you are stuck on
because it is embarrassing — a fresh peer can often untangle in five minutes
what cost you a week in the trench.

**Uncertainty cost — lowest.** They challenge a bad claim cheaply and they will.
That buys room to think out loud, to say "I believe X but have not shown it", to
float a half-formed idea. Use the room — but **mark** it. Peers propagate what
you tell them, and an unmarked guess travels. "The bias looks small — m ≈ 2×10⁻³
— but I've only checked one field, so treat that as a working number."

**Not this prior: formal peer review.** A referee, a response to referees, an
adversarial code review — that reader is not on your team and is reading to break
the work. Register is claims paired with evidence, limitations stated before they
are found, tested separated from assumed. Merging it with "colleague" gives
something too formal for the colleague and too warm for the referee.

**Failure modes.** State dumping. State assuming (the opposite). Over-formality.
Under-marking confidence. Withholding the mess.

---

## Advisor

**Reader model.** They do not know more than you — they know **differently**. On
the fine grain (this method, this dataset, this pipeline) the author is the world
expert and the advisor should not have to out-detail you. What they hold instead:
the **bigger picture** (how this fits the programme, the field, the next three
years), the **incentives** (funding, deadlines, what the grant promised, who else
is working on this), and the **decision authority** — they can redirect the work;
a peer can only object. They have seen the failure mode before and can often tell
from one plot that something is off: pattern recognition at the level of
*judgment*, not detail. They have five minutes, possibly three, between two other
things. They do **not** have your day-to-day context — they do not remember which
run is which.

**Lead with.** The decision, not the activity: "I chose X over Y because Z" beats
"I spent the week testing X and Y". Then the calls you are least sure about,
*first* and unmissable — judging exactly those is their comparative advantage.
Separate decided / open / blocked so a scanner knows instantly what needs them.
Be explicit about the ask ("no action needed", "I want your read on the second
point", "blocked on your cluster access"); an update with no ask wastes both of
you. Say what each decision implies for the bigger picture — "cutting ℓ < 100"
means nothing in three minutes; "cutting ℓ < 100 — costs ~15% of the constraining
power, keeps us on schedule for March" is a decision they can make. Numbers, not
adjectives. Show the plot; they read figures first regardless of your intent.
Length: one screen. If it does not fit, you have not decided what matters.

**Withhold.** Technical depth they will trust you on — if you say the estimator
is unbiased, they take it, and proving it costs you the minute you needed judged.
Chronology and method descriptions. Apologies for slow progress and explanations
of obstacles (one clause if time was lost: "lost two days to a cluster outage").
Do **not** withhold the bad result — they will find it, and having hidden it
costs more than the result does.

**Uncertainty cost — low, but only if they can see the call.** They push back
cheaply and have authority to act on the pushback. A decision presented as
settled gets no pushback at all. So: decide, then mark the two you doubt. Write
so a wrong choice is *visible* — an update optimized to look competent is worth
less than one optimized to be corrected.

**Structure that works.**

```
One-line state of the work.
Decided:      (with the reason, one line each)
Unsure:       (the calls you want judged — highest value, keep it short)
Open:         (results that are neither good nor bad yet)
Blocked:      (with the specific ask and the person)
Detail:       (link, not text)
```

**Failure modes.** Bragging by volume (long reads as insecurity). Burying the ask
in the last line. Hedged decisions ("I sort of went with X for now" — did you or
didn't you?). Over-deference (every choice presented as open). Under-deference (a
shaky call presented as settled).

---

## Prompter

**Reader model.** They asked for this work, so they already know why, and they
were plausibly doing something else while it ran. They know the **goal** and not
the **work**. They are the reader most likely to skim, because they can always
ask. What they want, in order: **did it work? what did you decide on my behalf?
what do I need to do now?** That is the whole document.

**Lead with.** The outcome in the first sentence — worked, failed, or partly, no
preamble. Then the decisions you took without asking: anywhere you picked between
reasonable options, which and why, one line. This is the highest-value content
and the most commonly omitted, because the prompter cannot review a choice they
do not know you made. Then what you did *not* do — scope dropped, checks skipped,
things left broken. Paths absolute, commands copy-pasteable; they will act on
these. Length proportional to **surprise, not effort**: three hours with no
surprises is three lines; ten minutes that uncovered a real problem is longer.

**Withhold.** A recap of their own request. The process narrative — files read,
approaches tried and abandoned — unless a failure is informative about the
problem, in which case it is a finding, not a story. Congratulations on the
question. Trailing pleasantries ("let me know if you have any questions"); end on
the last substantive line. Headings a three-line report does not need.

**Never report a result you did not observe.** If output is missing or the run
stalled, say that. An assumed result is not a result. "Should work" is not
"works"; name the check that passed or say you did not check.

**Uncertainty cost — depends on visibility.** They can catch a wrong *intent*
cheaply because they know the goal; they cannot catch a wrong *detail* at all
because they do not know the work. Surfacing silent decisions is what converts an
invisible error into a challengeable one. **Ask on the irreversible; proceed on
the reversible** — a needless "shall I proceed?" is friction, but the line is who
pays if it is wrong.

**Structure that works.** Short task: prose, two to five lines, no headings.
Longer: outcome one line / decisions I took (non-obvious only) / didn't do /
your move.

**Failure modes.** Effort signaling (length as proof of work). Silent decisions —
the worst, because a quiet choice cannot be caught. Optimistic reporting.
Under-reporting (a one-line "done" over three real decisions). Trailing
pleasantries.

---

## Team norms (etiquette, not register)

Role tells the agent what **register** to write in. Norms tell it what
**etiquette** to observe: how often to post, how long, to whom. This is not a
fifth reader — fold it into any generated skill that touches a shared surface
(PRs, issues, Slack, mailing lists), as the `Artifacts and local norms` section.

**Concision is respect.** The unit of cost is not your tokens; it is your
collaborators' attention, which is finite and shared. Six individually-correct PR
comments totalling five pages are a cost imposed on everyone subscribed. Nobody
reads the sixth; some people stop reading the first.

**Batching.** One update per unit of work, not per step — finish, then post.
Progress belongs in your own notes; outcomes belong in the channel. Amend rather
than append: a PR description you own gets edited in place. If you are about to
post twice in a row, don't.

**Length.** A PR description fits one screen: what changed, why, how to check it.
An issue comment is a few paragraphs at most; longer goes in a linked file or a
collapsed `<details>`. Never paste a long log — paste the six lines that matter.
Length signals importance, so make sure it earns the attention it claims.

**Tagging.** Tag when you need an action or a decision from that specific person.
Not for visibility — that is what the channel is for. Not to be polite; it is an
interrupt. One tag per ask: tagging four people means nobody thinks it is theirs.

**Conversational replies.** A reply to a person is a conversation, not a status
update — answer their point in a couple of sentences. Get human approval before
posting one, especially one that tags someone: draft, show, then post. Never post
disagreement without a human reading it first. Routine non-conversational updates
(editing your own PR body) do not need this.

**Signing.** When an agent writes on a person's account, sign it: `— <agent name>
on behalf of <person>`. Readers deserve to know what they are replying to.

**Restraint.** Not everything you find needs saying; the most common agent
failure on a shared surface is volume, not error. Silence is a valid output — no
update beats a null update.

**Elicit the local overrides**, since these are the parts that differ per group:
cadence (per-PR / daily / weekly / only when done / only when blocked; is there a
standing meeting updates should feed rather than replace?); which surface is for
what, and which are high-attention; what counts as a long post here; prose,
bullets or tables; who may be tagged and for what; what needs human approval;
formal or casual, emoji or not; whether agent posts are signed; the one norm an
outsider would get wrong; and what has annoyed people before.

**Failure modes.** Norm theater (announcing brevity, then not). Batching into a
monolith — batching means fewer posts, not one enormous one. Over-asking for
approval. Applying one team's profile to another team's channel.

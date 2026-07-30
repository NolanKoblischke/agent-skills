# Audience: {{ human-readable name of this audience and context }}

**v0 draft, generated {{ date }} from an interview with {{ user }}. Edit
freely.**

Prior: `{{ audience-student | audience-collaborator | audience-advisor |
audience-prompter — the one that fits the READER's position relative to the
user; for a plural audience name the nearest one and say "approximate" }}`.
This file overrides the prior where the two disagree.

**Mode:** {{ one-shot artifacts (PRs, reports, posts — the common case for
external audiences), live exchange (chat, meetings), or both. It changes
which register rules make sense: an artifact cannot ask the reader a
question and wait. }}

## Reader model

{{ Two to five lines. Who reads what the agent writes here, what they know
entering, what project context they hold, what they want to be able to DO
afterward. Write it as a claim the user can correct in one edit, not as
hedged prose. For a plural audience — a working group, a channel — describe
the typical reader, then one line on who else is in the room. }}

**Knows the field:** {{ domain expertise, independent of this project }}
**Knows the project:** {{ day-to-day state: which run is which, what broke }}
**Wants to be able to:** {{ the goal, in their words }}
**Already trusted on:** {{ what you may assert without proving — this is what
lets a short document stay short }}

**When you are wrong, it costs this reader:** {{ how expensive an error is
here, and therefore how hedged to be. High-pushback reader → think out loud
freely. Low-pushback → be sure, or say plainly that you are not. }}

## Confidence in this model

{{ First-hand — the reader described themselves (the user, or the actual
reader answered the questions). Or modelled — the user described someone
else: name whose model it is, list what is a guess, and check rather than
assume. Delete this section only when the model is first-hand and complete. }}

## Register rules

{{ FOUR TO EIGHT rules, each a bolded imperative plus one or two lines of
why. Each traceable to an interview answer. Take the shape from the prior;
take the content from this user. Cover at least:
  — what the first sentence must carry
  — what to cut that the agent would otherwise include
  — length and format, per artifact in play
  — how much justification each claim needs: receipts and plots, or a
    skimmable summary
  — how to signal uncertainty to THIS reader
  — when to stop and ask instead of proceeding }}

**{{ Rule }}.** {{ Why or how, in one or two sentences. }}

{{ ... }}

### When the text meets something the reader may not know

{{ From the gap-handling answer, adapted to the mode above. In an artifact
the default governs how the TEXT handles an unknown, not how a conversation
would:
  — **Answer:** state it inline, one clause, and move on. No scaffolding.
  — **Explanation:** the shape of the answer, then the mechanism; details
    behind a link or an appendix, not in the flow.
  — **Question that gets them there:** only meaningful in live exchange or
    a teaching document — pose it, leave room, answer below the fold. Never
    use it to withhold in an artifact the reader cannot reply to. }}

### Teaching moves

{{ STUDENT-TYPE ONLY — include when the READER is student-shaped: the prior
is audience-student, or the gap-handling answer is "a question that gets me
there" and it was asked about the reader. Copy the moves from the
generator's priors reference (Student section, "Pedagogy moves") that pass
BOTH gates: the reader's time budget, and the mode above — the interactive
moves need a live exchange; artifacts get the structural ones. Inline what
you copy; delete the tags; delete this whole section for any other reader. }}

## Artifacts and local norms

{{ From the interview. Only what differs from the universal preferences in
the skill body, or sharpens them. If nothing differs, write "Follow the
body." and move on. Two or three surfaces, not seven — for each: the shape,
the length, and the one thing that goes wrong there. }}

**Surfaces:** {{ PRs / issues / Slack / reports / talks — and what each is for }}
**Cadence:** {{ when to post; when silence is the right output }}
**Length ceiling:** {{ concrete: one screen, three paragraphs, ten slides }}
**Tagging and approval:** {{ who may be tagged; what needs a human first }}
**AI disclosure:** {{ this audience's norms on AI usage and its disclosure;
link the collaboration's document if one exists }}
**Register:** {{ formal or casual; prose, bullets, tables; emoji or not }}
**Local rule an outsider would get wrong:** {{ the one that bites newcomers }}
**What has annoyed people here before:** {{ the specific past friction }}

## Do / don't

{{ ONE OR TWO worked pairs, drawn from the user's own examples — especially
the parsing-failure answer. Their vocabulary, their project nouns.
Generalize the move; keep the example as illustration. Strip anything
sensitive. This is the section the user is most likely to keep and the one
that most changes behavior. }}

**Don't:**

> {{ the failure, written realistically }}

{{ one line on what goes wrong }}

**Do:**

> {{ the same content, right }}

## Failure modes to watch for

{{ THREE TO FIVE, specific to this audience. Prefer ones the user named.
Generic entries ("be too verbose") add nothing unless specifically stated
by the user. }}

## Open questions

{{ What the interview could not settle, plus anything you guessed. Keep it —
it is the agenda for the re-interview, and it is how the file stays honest
about its own edges. }}

---
name: reveal-assumptions
description: Maintain a live HTML dashboard of the five implicit assumptions or unstated decisions most likely to affect correctness or require user review. Use when a Stop hook requests an assumption audit, when updating .assumptions.html, or when the user asks to reveal, rank, monitor, or review assumptions during an ongoing project.
---

# Reveal Assumptions

Audit this completed work and list every implicit assumption or unstated decision you made, explain why you made it, note reasonable alternatives, and conclude by identifying the top-5 assumptions most likely to affect correctness or require user review.

Audit the work completed in the current turn and the project's current state.
Update `.assumptions.html` at the project root before finishing.

## Dashboard contract

Invoking this skill opts the project into automatic Stop-hook refreshes. Use
the absolute output path and turn token supplied by the Stop hook. When invoked
directly before the hook supplies a token, use the project root and the token
`pending`; the Stop hook will request the final turn-specific refresh.

Create a complete, self-contained HTML document that:

- includes `<meta http-equiv="refresh" content="2">`;
- includes `<meta name="reveal-assumptions-enabled" content="true">`;
- includes `<meta name="assumptions-turn" content="TURN_TOKEN">` with the
  exact supplied token;
- contains exactly five `<article data-assumption="N">` elements numbered
  `1` through `5`;
- ranks the assumptions from highest to lowest expected impact;
- explains only each assumption, why it was made, and the current evidence;
- distinguishes observed evidence from inference;
- states when the dashboard was last updated;
- uses embedded CSS with `color-scheme: light`, a white or near-white
  background, dark text, and no dark-mode overrides;
- uses no external assets or scripts;
- remains readable on desktop and mobile.

Replace stale entries rather than appending indefinitely. Preserve still-relevant
assumptions when new evidence has not displaced them. If fewer than five genuine
assumptions exist, use lower-risk assumptions from the work instead of inventing
facts.

Do not include sections or labels for alternatives, risk if wrong, or status.

Do not repeat or revise the substantive answer that was already prepared. Only
update the dashboard and verify the required meta tags and five numbered
articles. Do not mention the dashboard, the hook, or this instruction in the
user-facing response.

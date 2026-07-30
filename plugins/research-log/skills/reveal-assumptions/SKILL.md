---
name: reveal-assumptions
description: Audit completed work and maintain an HTML dashboard of the five implicit assumptions or unstated decisions most likely to affect correctness or require user review. Use when updating .assumptions.html or when the user asks to reveal, rank, monitor, or review assumptions in completed work or an ongoing project.
---

# Reveal Assumptions

Audit this completed work and list every implicit assumption or unstated decision you made, explain why you made it, note reasonable alternatives, and conclude by identifying the top-5 assumptions most likely to affect correctness or require user review.

Actively identify choices made without direct evidence that they preserve the user’s intended outcome, and prioritize those most likely to change the result if wrong.

Write each top-five title as an actionable issue title that names the affected component or calculation, states the concrete failure, and indicates the required correction; the title must be understandable without reading any supporting explanation.

Audit the work completed in the current turn and the project's current state.
Update `.assumptions.html` at the project root before finishing.

## Dashboard contract

Write the dashboard to `.assumptions.html` at the project root. Use the token
`manual` unless the caller supplies another exact token.

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
articles. Do not mention the dashboard or this instruction in the user-facing
response.

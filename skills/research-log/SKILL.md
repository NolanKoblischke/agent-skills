---
name: research-log
description: Create or update a polished HTML research notebook from dated project evidence, using the bundled notebook template and the reveal-assumptions skill for ranked assumptions. Use when the user asks for a research log, research notebook, lab notebook, daily project journal, ongoing HTML progress record, or a concise record of completed work, assumptions, and next steps.
---

# Research Log

Create an evidence-based daily research notebook without turning it into a raw
terminal transcript or an exhaustive provenance dump.

## Workflow

1. Resolve the project root and the requested output path. Default to
   `research-log.html` in the project root. Preserve an existing research log
   and update it in place; do not overwrite an unrelated file.
2. Inspect dated, durable project evidence before writing. Prefer the current
   worktree, diffs, commits, tests, generated artifacts, existing notes, and
   user-supplied context. Do not claim work, results, or dates that the evidence
   does not support.
3. Invoke the installed `reveal-assumptions` skill for the current project.
   Read the ranked assumptions from the resulting project-root
   `.assumptions.html`; do not independently invent a replacement assumptions
   audit.
4. Copy `assets/Research Notebook.dc.html` and its adjacent
   `assets/support.js` when creating a new notebook. Treat the HTML as the
   structural and visual source of truth, then replace its example project and
   entry content with evidence from the current project.
5. Update the newest daily entry and the project sidebar. Preserve earlier
   entries unless correcting unsupported information. Keep entries ordered and
   keep the newest entry selected by default.
6. Render or open the result in a browser and inspect every available day.
   Verify navigation, readable layout, and the absence of stale example text.

## Entry contract

Give every daily entry exactly these four elements:

- day number and calendar date;
- **Work performed**: a compact account of what changed and what the evidence
  establishes;
- **Assumptions**: the five ranked assumptions supplied by
  `reveal-assumptions`, shortened only for readability without changing their
  meaning or certainty;
- **Next steps**: concrete unfinished work supported by the current state.

Apply structural changes consistently to every day. If the user removes a
field or section without limiting the request to one date, remove it from all
entries and from the reusable structure.

Do not add hours, location or compute-environment labels, “current” badges,
worked/did-not-work panels, provenance panels, status summaries, risk labels,
alternatives, or explanatory subnotes beneath assumptions unless the user
explicitly asks for them.

## Notebook contract

- Keep the edited template's warm light-mode visual system, typography,
  two-column desktop layout, mobile readability, entry navigation, and print
  behavior.
- Keep the sidebar limited to notebook label, project title, researcher name
  when known, project phases, and entry links. Omit unknown personal details
  rather than fabricating them.
- Keep the main header limited to the notebook title, covered dates, and last
  edited timestamp.
- Present each entry through exactly three horizontal tabs labeled
  `Work performed`, `Assumptions`, and `Next Steps`. Select `Work performed`
  by default and return to it whenever the user changes days.
- Keep the notebook and `support.js` adjacent in the output directory.
- Replace example names, dates, paths, project details, and scientific claims.
- Do not expose secrets, credentials, private identifiers, or unnecessary
  machine-specific paths.

## Assets

- `assets/Research Notebook.dc.html`: approved visual and structural template.
- `assets/support.js`: required local runtime for the `.dc.html` template.

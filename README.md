# Reveal Assumptions

A single agent skill and `Stop` hook that maintain a live
`.assumptions.html` dashboard containing the five assumptions most likely to
affect the correctness of an ongoing project.

The repository packages the same skill and hook for Claude Code and Codex.
The hook runs when an assistant turn is about to finish. It asks the active
agent to load the skill and refresh the dashboard, validates the result, and
then lets the turn end.

## Install

### Claude Code

```bash
claude plugin marketplace add NolanKoblischke/agent-skills
claude plugin install reveal-assumptions@nolan-koblischke
```

### Codex

```bash
codex plugin marketplace add NolanKoblischke/agent-skills
codex plugin add reveal-assumptions@nolan-koblischke
```

Review and trust the hook when the agent asks. Start a new session after
installing or updating the plugin.

## Use

Work normally. Before each assistant message finishes, the hook causes the
agent to create or refresh `.assumptions.html` in the project root. Open that
file in a browser and leave it open; it refreshes itself every two seconds.

The dashboard is generated working state. Add `.assumptions.html` to the
project's `.gitignore` if it should remain untracked.

## Develop

Canonical sources live in `skills/`, `hooks/`, and `skills.config.json`.
Generated Claude and Codex packages live under `plugins/`.

```bash
npm run build
npm test
```

The build system was copied from
[LightconeResearch/agent-skills](https://github.com/LightconeResearch/agent-skills)
and remains available under its BSD 3-Clause license.

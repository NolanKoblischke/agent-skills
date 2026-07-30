# Nolan Koblischke Agent Skills

Two agent skills for maintaining evidence-based project records:

- `reveal-assumptions` maintains a live `.assumptions.html` dashboard with the
  five assumptions most likely to affect correctness.
- `research-log` creates a polished daily HTML research notebook from durable
  project evidence and uses `reveal-assumptions` to populate its assumptions.

The repository packages the same skills and hook for Claude Code and Codex.
The hook runs when an assistant turn is about to finish. It does nothing until
the skill has been invoked and created an enabled dashboard. After that opt-in,
it silently refreshes and validates the dashboard before letting each turn end.

## Install

### Claude Code

```bash
claude plugin marketplace add NolanKoblischke/agent-skills
claude plugin install reveal-assumptions@nolan-koblischke
claude plugin install research-log@nolan-koblischke
```

### Codex

```bash
codex plugin marketplace add NolanKoblischke/agent-skills
codex plugin add reveal-assumptions@nolan-koblischke
codex plugin add research-log@nolan-koblischke
```

Review and trust the hook when the agent asks. Start a new session after
installing or updating the plugin.

## Use

Invoke `reveal-assumptions` once to opt the project in, then work normally.
Before each later assistant message finishes, the hook silently refreshes
`.assumptions.html` in the project root. Open that file in a browser and leave
it open; it refreshes itself every two seconds. Delete the file to opt out.

Invoke `research-log` to create or update a project research notebook. It uses
the bundled notebook template, gathers dated evidence from the current project,
and invokes `reveal-assumptions` before writing the entry's ranked assumptions.
Installing `research-log` also bundles the assumptions skill and Stop hook.

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

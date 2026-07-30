# Nolan Koblischke Agent Skills

Three agent skills for audience-aware project records:

- `know-your-audience`, from Lightcone Research, interviews the user and creates
  an editable audience profile.
- `reveal-assumptions` maintains a `.assumptions.html` dashboard with the
  five assumptions most likely to affect correctness.
- `research-log` creates a polished daily HTML research notebook from durable
  project evidence, delegates its assumptions audit to `reveal-assumptions`,
  and optionally follows an identified audience profile.

The repository packages the same skills for Claude Code and Codex. Installing
`research-log` bundles all three skills.

## Install

### Claude Code

```bash
claude plugin marketplace add NolanKoblischke/agent-skills
claude plugin install research-log@nolan-koblischke
```

### Codex

```bash
codex plugin marketplace add NolanKoblischke/agent-skills
codex plugin add research-log@nolan-koblischke
```

Start a new session after installing or updating the plugin.

## Use

Invoke `know-your-audience` to create a communication profile for a reader.
It reports the generated Markdown path when the interview is complete.

Invoke `reveal-assumptions` whenever you want to refresh the project-root
`.assumptions.html` dashboard.

Invoke `research-log` to create or update a project research notebook. It uses
the bundled editable template, gathers dated evidence, delegates the assumptions
audit to a subagent, and uses an identified audience profile when one is
available. The user can identify any evidence or audience file in the prompt;
the skill does not require a special input format.

## Develop

Canonical sources live in `skills/` and `skills.config.json`.
Generated Claude and Codex packages live under `plugins/`.

```bash
npm run build
npm test
```

`know-your-audience` is redistributed from
[LightconeResearch/audience-aware-skills](https://github.com/LightconeResearch/audience-aware-skills)
version 0.2.0 under the BSD 3-Clause license; its license is retained in the
vendored skill directory.

The build system was copied from
[LightconeResearch/agent-skills](https://github.com/LightconeResearch/agent-skills)
and remains available under its BSD 3-Clause license.

# AGENTS.md

This repository packages `know-your-audience`, `reveal-assumptions`, and
`research-log` for Claude Code and Codex.

## Source of truth

- `skills/reveal-assumptions/` contains the skill.
- `skills/research-log/` contains the research notebook skill and template.
- `skills/know-your-audience/` contains the pinned Lightcone Research skill.
- `skills.config.json` declares all plugins and their dependency closure.
- `scripts/build.mjs` generates both marketplace formats and self-contained
  plugin packages.

The `.claude-plugin/`, `.agents/plugins/`, `plugins/`, and `manifest.json`
paths are generated. Never edit them directly.

The repository has no lifecycle hooks. `reveal-assumptions` updates its
dashboard only when invoked.

After changing a canonical source, run:

```bash
npm run build
npm test
```

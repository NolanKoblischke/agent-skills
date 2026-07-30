# AGENTS.md

This repository packages canonical `reveal-assumptions` and `research-log`
skills plus one `Stop` hook for Claude Code and Codex.

## Source of truth

- `skills/reveal-assumptions/` contains the skill.
- `skills/research-log/` contains the research notebook skill and template.
- `hooks/reveal-assumptions/` contains the sole lifecycle hook.
- `skills.config.json` declares both plugins and their dependency closure.
- `scripts/build.mjs` generates both marketplace formats and self-contained
  plugin packages.

The `.claude-plugin/`, `.agents/plugins/`, `plugins/`, and `manifest.json`
paths are generated. Never edit them directly.

After changing a canonical source, run:

```bash
npm run build
npm test
```

The hook contract is intentionally narrow:

- configure only the `Stop` event;
- allow at most two repair continuations;
- never read or copy transcript contents;
- write only the project-local `.assumptions.html` dashboard plus temporary
  validation state under the operating system temp directory;
- use Python standard-library modules only.

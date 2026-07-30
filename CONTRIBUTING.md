# Contributing

Edit only the canonical sources:

- `skills/reveal-assumptions/`
- `skills/research-log/`
- `skills/know-your-audience/`
- `skills.config.json`
- `scripts/`

Then regenerate and validate both plugin targets:

```bash
npm run build
npm test
```

Do not hand-edit `.claude-plugin/`, `.agents/plugins/`, `plugins/`, or
`manifest.json`; those paths are generated and drift-checked.

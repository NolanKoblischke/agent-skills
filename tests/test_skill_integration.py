import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SkillIntegrationTests(unittest.TestCase):
    def test_vendored_audience_skill_is_complete(self):
        skill = ROOT / "skills" / "know-your-audience"
        for relative_path in (
            "SKILL.md",
            "LICENSE",
            "assets/audience-template.md",
            "assets/body-template.md",
            "references/learning-prompt.md",
            "references/priors.md",
        ):
            self.assertTrue((skill / relative_path).is_file(), relative_path)

    def test_research_log_bundles_all_three_skills_without_hooks(self):
        config = json.loads((ROOT / "skills.config.json").read_text())
        plugins = {plugin["name"]: plugin for plugin in config["plugins"]}

        self.assertEqual(
            plugins["research-log"]["dependencies"],
            ["reveal-assumptions", "audience-aware-skills"],
        )
        self.assertTrue(all("hooks" not in plugin for plugin in plugins.values()))

        manifest = json.loads((ROOT / "manifest.json").read_text())
        generated = {plugin["name"]: plugin for plugin in manifest["plugins"]}
        self.assertEqual(
            generated["research-log"]["skills"],
            ["know-your-audience", "research-log", "reveal-assumptions"],
        )
        self.assertFalse(generated["research-log"]["hasHooks"])

    def test_research_log_uses_delegated_audit_and_optional_audience(self):
        text = (ROOT / "skills" / "research-log" / "SKILL.md").read_text()
        self.assertIn("Delegate the assumptions audit to one subagent", text)
        self.assertIn("audience-profile", text)
        self.assertIn("using only each assumption statement", text)
        self.assertIn("If the project has `astra.yaml`", text)
        self.assertIn("ASTRA-linked results", text)
        self.assertIn("MyST is not required", text)
        self.assertIn("example-result.svg", text)
        self.assertIn("Assumption source links", text)
        self.assertIn("data-code-path", text)
        self.assertNotIn("download an HTML copy", text)

    def test_reveal_assumptions_has_no_stop_hook_contract(self):
        text = (ROOT / "skills" / "reveal-assumptions" / "SKILL.md").read_text()
        self.assertNotIn("Stop hook", text)
        self.assertNotIn("Stop-hook", text)
        self.assertIn(
            "Write each top-five title as an actionable issue title", text
        )
        self.assertIn(
            "the title must be understandable without reading any supporting explanation",
            text,
        )
        self.assertIn('class="code-ref"', text)
        self.assertIn("data-code-start", text)


if __name__ == "__main__":
    unittest.main()

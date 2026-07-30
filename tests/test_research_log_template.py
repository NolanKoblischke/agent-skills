import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "skills" / "research-log" / "assets"
TEMPLATE = ASSETS / "Research Notebook.dc.html"


class ResearchLogTemplateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = TEMPLATE.read_text(encoding="utf-8")

    def test_required_assets_exist(self):
        self.assertTrue(TEMPLATE.is_file())
        self.assertTrue((ASSETS / "support.js").is_file())
        editor = ASSETS / "research-log-editor.js"
        self.assertTrue(editor.is_file())
        self.assertIn('<script src="./support.js"></script>', self.html)
        self.assertIn('<script src="./research-log-editor.js" defer></script>', self.html)
        editor_js = editor.read_text(encoding="utf-8")
        for contract in (
            'contenteditable", "true"',
            'data-editor-action="add"',
            'data-editor-action="download"',
            'data-editor-action="reset"',
            "localStorage.setItem",
            "state.items[key].deleted = true",
            'type="application/json"',
            'fetch(new URL("support.js", baseUrl)',
            'fetch(new URL("research-log-editor.js", baseUrl)',
        ):
            self.assertIn(contract, editor_js)

    def test_each_day_has_only_core_panels(self):
        for day in (11, 12, 13):
            match = re.search(
                rf'<article id="day-{day}".*?</article>',
                self.html,
                flags=re.DOTALL,
            )
            self.assertIsNotNone(match, f"missing Day {day}")
            entry = match.group(0)
            for panel in ("work", "assumptions", "next"):
                self.assertEqual(entry.count(f'data-panel="{panel}"'), 1)
            for removed in (
                "Worked / didn't",
                "Provenance",
                "Where I am",
                "font-style:italic",
                " h ·",
                ">Current<",
            ):
                self.assertNotIn(removed, entry)

    def test_exact_tab_labels_and_state_contract(self):
        for label in ("Work performed", "Assumptions", "Next Steps"):
            self.assertEqual(self.html.count(f">{label}</button>"), 2)
        self.assertIn('role="tablist"', self.html)
        self.assertIn("state = { day: 13, section: 'work' }", self.html)
        self.assertIn("this.setState({ day: d, section: 'work' })", self.html)
        self.assertIn("goAssumptions: () => this.show('assumptions')", self.html)
        self.assertIn("goNextSection: () => this.show('next')", self.html)

    def test_removed_global_example_sections_stay_removed(self):
        for removed in (
            "Flagged for Prof.",
            "Raw data and pipeline commits",
            "Period recovery for faint eclipsing binaries",
            "TESS-EB-01",
            "Kept by",
            "est. 4 more days",
        ):
            self.assertNotIn(removed, self.html)


if __name__ == "__main__":
    unittest.main()

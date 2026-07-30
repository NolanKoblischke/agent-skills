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
        cls.editor_js = (ASSETS / "research-log-editor.js").read_text(encoding="utf-8")

    def test_required_assets_and_editing_contract(self):
        for name in (
            "Research Notebook.dc.html",
            "support.js",
            "research-log-editor.js",
            "example-result.svg",
        ):
            self.assertTrue((ASSETS / name).is_file(), name)

        self.assertIn('<script src="./support.js"></script>', self.html)
        self.assertIn('<script src="./research-log-editor.js" defer></script>', self.html)
        for contract in (
            'contenteditable", "true"',
            'data-editor-action="add"',
            'data-editor-action="reset"',
            "localStorage.setItem",
            "state.items[key].deleted = true",
        ):
            self.assertIn(contract, self.editor_js)

        self.assertNotIn("Download edited HTML", self.editor_js)
        self.assertNotIn('data-editor-action="download"', self.editor_js)

    def test_each_day_has_only_core_panels_and_five_assumptions(self):
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
            self.assertEqual(len(re.findall(r">A[1-5]</span>", entry)), 5)
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

    def test_astra_value_and_figure_contract(self):
        self.assertIn('class="astra-value"', self.html)
        self.assertIn('class="research-figure"', self.html)
        self.assertIn('data-astra-path="outputs.primary_results.metrics.sample_count"', self.html)
        self.assertIn('data-astra-universe="baseline"', self.html)
        self.assertIn('data-astra-source="outputs/metrics.json"', self.html)
        self.assertIn('data-astra-detail=', self.html)
        self.assertIn('data-astra-popover', self.html)
        self.assertIn('contenteditable="false"', self.html)
        self.assertIn('!span.classList.contains("astra-value")', self.editor_js)

    def test_template_is_domain_neutral(self):
        for domain_specific in (
            "TESS",
            "TRGB",
            "SMC",
            "LMC",
            "OGLE",
            "Gaia",
            "eclipsing",
            "Sector 30",
            "J. Okonkwo",
        ):
            self.assertNotIn(domain_specific, self.html)

        for placeholder in (
            'data-template-example="project-title"',
            'data-template-example="work-note"',
            'data-template-example="assumption"',
            'data-template-example="next-step"',
            'data-template-example="astra-value"',
            'data-template-example="astra-figure"',
        ):
            self.assertIn(placeholder, self.html)


if __name__ == "__main__":
    unittest.main()

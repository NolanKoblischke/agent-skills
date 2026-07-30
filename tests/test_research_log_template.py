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
        self.assertIn('<script src="./support.js"></script>', self.html)

    def test_each_day_has_only_core_sections(self):
        for day in (11, 12, 13):
            match = re.search(
                rf'<article id="day-{day}".*?</article>',
                self.html,
                flags=re.DOTALL,
            )
            self.assertIsNotNone(match, f"missing Day {day}")
            entry = match.group(0)
            for section in ("Work performed", "Assumptions", "Next steps"):
                self.assertEqual(entry.count(f">{section}<"), 1)
            for removed in (
                "Worked / didn't",
                "Provenance",
                "Where I am",
                "font-style:italic",
                " h ·",
                ">Current<",
            ):
                self.assertNotIn(removed, entry)

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

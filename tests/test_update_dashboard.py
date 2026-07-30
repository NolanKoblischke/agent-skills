#!/usr/bin/env python3

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
HOOK = ROOT / "hooks" / "reveal-assumptions" / "scripts" / "update-dashboard.py"


class StopHookTests(unittest.TestCase):
    def run_hook(self, event: dict) -> dict:
        result = subprocess.run(
            ["python3", str(HOOK)],
            input=json.dumps(event),
            capture_output=True,
            text=True,
            check=True,
        )
        return json.loads(result.stdout)

    def event(self, cwd: str, active: bool = False) -> dict:
        return {
            "session_id": self.id(),
            "turn_id": "turn-test",
            "cwd": cwd,
            "hook_event_name": "Stop",
            "stop_hook_active": active,
            "last_assistant_message": "Finished the requested work.",
        }

    def token_from(self, output: dict) -> str:
        match = re.search(r'exact turn token "([^"]+)"', output["reason"])
        self.assertIsNotNone(match)
        return match.group(1)

    def dashboard(self, token: str, count: int = 5) -> str:
        articles = "\n".join(
            f'<article data-assumption="{number}">Assumption {number}</article>'
            for number in range(1, count + 1)
        )
        return (
            "<!doctype html><html><head>"
            '<meta http-equiv="refresh" content="2">'
            '<meta name="reveal-assumptions-enabled" content="true">'
            f'<meta name="assumptions-turn" content="{token}">'
            f"</head><body>{articles}</body></html>"
        )

    def test_does_nothing_when_skill_has_not_enabled_dashboard(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = self.run_hook(self.event(directory))
            self.assertTrue(output["continue"])
            self.assertNotIn("decision", output)
            self.assertNotIn("systemMessage", output)
            self.assertFalse(Path(directory, ".assumptions.html").exists())

    def test_blocks_once_then_accepts_valid_dashboard(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, ".assumptions.html").write_text(
                self.dashboard("pending"), encoding="utf-8"
            )
            first = self.run_hook(self.event(directory))
            self.assertEqual(first["decision"], "block")
            self.assertIn("do not acknowledge this hook message", first["reason"])
            token = self.token_from(first)
            Path(directory, ".assumptions.html").write_text(
                self.dashboard(token), encoding="utf-8"
            )

            second = self.run_hook(self.event(directory, active=True))
            self.assertTrue(second["continue"])
            self.assertNotIn("decision", second)

    def test_invalid_dashboard_gets_one_repair_then_fails_open(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, ".assumptions.html").write_text(
                self.dashboard("pending"), encoding="utf-8"
            )
            first = self.run_hook(self.event(directory))
            token = self.token_from(first)
            Path(directory, ".assumptions.html").write_text(
                self.dashboard(token, count=4), encoding="utf-8"
            )

            second = self.run_hook(self.event(directory, active=True))
            self.assertEqual(second["decision"], "block")
            self.assertIn("exactly five", second["reason"])

            third = self.run_hook(self.event(directory, active=True))
            self.assertTrue(third["continue"])
            self.assertIn("two failed dashboard repairs", third["systemMessage"])


if __name__ == "__main__":
    unittest.main()

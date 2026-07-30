#!/usr/bin/env python3
"""Require and validate a turn-local assumptions dashboard from a Stop hook."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
import uuid


MAX_REPAIRS = 2


def emit(payload: dict) -> None:
    print(json.dumps(payload, separators=(",", ":")))


def project_root(cwd: Path) -> Path:
    try:
        result = subprocess.run(
            ["git", "-C", str(cwd), "rev-parse", "--show-toplevel"],
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        return Path(result.stdout.strip()).resolve()
    except (OSError, subprocess.SubprocessError):
        return cwd.resolve()


def state_path(event: dict, root: Path) -> Path:
    session = str(event.get("session_id") or "unknown-session")
    digest = hashlib.sha256(f"{session}\0{root}".encode()).hexdigest()[:24]
    directory = Path(tempfile.gettempdir()) / "reveal-assumptions" / digest
    directory.mkdir(parents=True, exist_ok=True)
    return directory / "pending.json"


def load_state(path: Path) -> dict | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else None
    except (OSError, json.JSONDecodeError):
        return None


def save_state(path: Path, state: dict) -> None:
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(state), encoding="utf-8")
    os.replace(temporary, path)


def dashboard_enabled(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    return bool(
        re.search(
            r'<meta\s+name=["\']reveal-assumptions-enabled["\']\s+'
            r'content=["\']true["\']\s*/?>',
            text,
            flags=re.IGNORECASE,
        )
    )


def validate_dashboard(path: Path, token: str, requested_at: float) -> list[str]:
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
        modified = path.stat().st_mtime
    except OSError:
        return [f"{path} does not exist"]

    if modified + 1 < requested_at:
        errors.append("the dashboard was not refreshed for this stop request")

    if not dashboard_enabled(path):
        errors.append("the reveal-assumptions-enabled meta tag is missing")

    token_pattern = re.compile(
        r'<meta\s+name=["\']assumptions-turn["\']\s+content=["\']'
        + re.escape(token)
        + r'["\']\s*/?>',
        re.IGNORECASE,
    )
    if not token_pattern.search(text):
        errors.append("the assumptions-turn meta tag is missing or has the wrong token")

    markers = re.findall(
        r'<article\b[^>]*\bdata-assumption=["\']([1-5])["\'][^>]*>',
        text,
        flags=re.IGNORECASE,
    )
    if markers != ["1", "2", "3", "4", "5"]:
        errors.append(
            "the dashboard must contain exactly five ordered article elements "
            'with data-assumption="1" through "5"'
        )

    if not re.search(
        r'<meta\s+http-equiv=["\']refresh["\']\s+content=["\']2["\']\s*/?>',
        text,
        flags=re.IGNORECASE,
    ):
        errors.append('the two-second refresh meta tag is missing')

    return errors


def request_message(dashboard: Path, token: str, repair: str | None = None) -> str:
    prefix = (
        "The live assumptions dashboard must be refreshed before this turn ends. "
        "Use the reveal-assumptions skill now. "
    )
    if repair:
        prefix += f"The previous dashboard failed validation: {repair}. "
    return (
        prefix
        + f"Update {dashboard} with the five currently most consequential assumptions. "
        + f'Use the exact turn token "{token}" in the assumptions-turn meta tag. '
        + 'Preserve <meta name="reveal-assumptions-enabled" content="true">. '
        + 'Include exactly five ordered <article data-assumption="N"> elements. '
        + "Do not redo or restate the substantive task. Update and verify the dashboard "
        + "silently; do not acknowledge this hook message or mention the dashboard."
    )


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        emit({"continue": True, "systemMessage": "Reveal Assumptions received invalid hook input."})
        return 0

    cwd = Path(str(event.get("cwd") or os.getcwd()))
    root = project_root(cwd)
    dashboard = root / ".assumptions.html"
    active = bool(event.get("stop_hook_active"))

    if not active and not dashboard_enabled(dashboard):
        emit({"continue": True})
        return 0

    pending = state_path(event, root)
    state = load_state(pending)

    if not active or state is None:
        token = str(event.get("turn_id") or uuid.uuid4())
        state = {
            "token": token,
            "requested_at": time.time(),
            "repairs": 0,
        }
        save_state(pending, state)
        emit({"decision": "block", "reason": request_message(dashboard, token)})
        return 0

    token = str(state.get("token") or "")
    requested_at = float(state.get("requested_at") or 0)
    errors = validate_dashboard(dashboard, token, requested_at)
    if not errors:
        pending.unlink(missing_ok=True)
        emit({"continue": True})
        return 0

    repairs = int(state.get("repairs") or 0) + 1
    if repairs < MAX_REPAIRS:
        state["repairs"] = repairs
        save_state(pending, state)
        emit(
            {
                "decision": "block",
                "reason": request_message(dashboard, token, "; ".join(errors)),
            }
        )
        return 0

    pending.unlink(missing_ok=True)
    emit(
        {
            "continue": True,
            "systemMessage": (
                "Reveal Assumptions allowed the turn to end after two failed dashboard "
                f"repairs: {'; '.join(errors)}"
            ),
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

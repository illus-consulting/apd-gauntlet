"""apd-orchestrator is retired to a deprecation shim (Plan 3); pins the marker + pointer."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
AGENT = REPO / ".claude" / "agents" / "apd-orchestrator.md"


def test_orchestrator_marked_deprecated() -> None:
    text = AGENT.read_text(encoding="utf-8")
    assert "DEPRECATED" in text


def test_orchestrator_points_at_workflow_runner() -> None:
    text = AGENT.read_text(encoding="utf-8")
    assert ".claude/workflows/apd-gauntlet.js" in text


def test_orchestrator_references_architecture_doc() -> None:
    text = AGENT.read_text(encoding="utf-8")
    assert "docs/architecture.md" in text
    assert (REPO / "docs" / "architecture.md").is_file()


def test_orchestrator_ends_with_single_trailing_newline() -> None:
    raw = AGENT.read_text(encoding="utf-8")
    assert raw.endswith("\n") and not raw.endswith("\n\n"), "MD047: single trailing newline"

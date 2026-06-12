import ast
from pathlib import Path

import pytest

from app.config import settings
import app.utils.premium_dispatch as premium_dispatch
from app.utils.model_guard import guard_batch_model
from app.utils.premium_dispatch import (
    PremiumDispatchBlocked,
    dispatch_premium,
    model_tier,
)

ROOT = Path(__file__).resolve().parents[1]
GUARDED_FILES = [
    ROOT / "app/agent_loop/tasks.py",
    ROOT / "app/agent_loop/autowiki/tasks.py",
    ROOT / "app/agent_loop/autowiki/judge_panel.py",
    ROOT / "app/agent_loop/research_ideas/auto_improvement.py",
    ROOT / "app/services/social_drafts.py",
]
GUARD_NAMES = {"dispatch_premium", "guard_batch_model"}


def _call_name(node: ast.Call) -> str:
    func = node.func
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        parts = [func.attr]
        value = func.value
        while isinstance(value, ast.Attribute):
            parts.append(value.attr)
            value = value.value
        if isinstance(value, ast.Name):
            parts.append(value.id)
        return ".".join(reversed(parts))
    return ""


def _is_llm_dispatch_call(node: ast.Call) -> bool:
    name = _call_name(node)
    if name.endswith("messages.create") or name.endswith("messages.stream"):
        return True
    if not (name.endswith("post") or name.endswith("Request")):
        return False
    for arg in list(node.args) + [kw.value for kw in node.keywords]:
        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
            if "chat/completions" in arg.value:
                return True
        if isinstance(arg, ast.JoinedStr):
            if "chat/completions" in "".join(
                part.value for part in arg.values if isinstance(part, ast.Constant)
            ):
                return True
    return False


def _guard_lines(tree: ast.AST) -> set[int]:
    lines = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and _call_name(node).split(".")[-1] in GUARD_NAMES:
            lines.add(node.lineno)
    return lines


@pytest.mark.parametrize("path", GUARDED_FILES)
def test_llm_dispatch_calls_have_nearby_guard(path: Path):
    tree = ast.parse(path.read_text())
    guard_lines = _guard_lines(tree)
    offenders = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and _is_llm_dispatch_call(node):
            if not any(0 <= node.lineno - guard_line <= 8 for guard_line in guard_lines):
                offenders.append(node.lineno)
    assert not offenders, f"{path.relative_to(ROOT)} has unguarded LLM dispatch at lines {offenders}"


def test_batch_strict_mode_reads_settings(monkeypatch):
    monkeypatch.setattr(settings, "BATCH_STRICT_MODE", False)
    assert guard_batch_model("claude-opus-4-7", "test.loop") == "gemini-3.5-flash"
    monkeypatch.setattr(settings, "BATCH_STRICT_MODE", True)
    with pytest.raises(ValueError):
        guard_batch_model("claude-opus-4-7", "test.loop")


def test_premium_whitelist_blocks_non_judge_jobs(monkeypatch):
    monkeypatch.setattr(settings, "PREMIUM_DISPATCH_ENABLED", True)
    monkeypatch.setattr(premium_dispatch, "_log_block", lambda *args, **kwargs: None)
    with pytest.raises(PremiumDispatchBlocked):
        dispatch_premium("autowiki.sonnet_section_rewrite", "claude-sonnet-4-6", 1_000, db=None)
    assert model_tier("claude-opus-4-7") == "PREMIUM"
    assert model_tier("deepseek-r1:32b") == "BATCH_SAFE"

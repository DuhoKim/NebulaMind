"""Regression tests for qualitative Antigravity quota readings.

Antigravity may report only ``Quota available`` without a numeric percentage or
reset time. The monitor must preserve that availability signal without
fabricating a 0%-used gauge.
"""
from __future__ import annotations

import sys
import types
from pathlib import Path

import pytest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

for name, attrs in (
    (
        "stable_cockpit_renderer",
        {"DEFAULT_PUBLIC_ROOTS": [], "write_outputs": lambda *a, **k: None},
    ),
    (
        "stable_cockpit_guard",
        {"unlock_all": lambda *a, **k: None, "lock_all": lambda *a, **k: None},
    ),
):
    if name not in sys.modules:
        module = types.ModuleType(name)
        module.__dict__.update(attrs)
        sys.modules[name] = module

import live_provider_usage_monitor as monitor  # noqa: E402


AVAILABLE_USAGE = """
Models & Quota
GEMINI MODELS
Weekly Limit
Quota available
Five Hour Limit
Quota available
CLAUDE AND GPT MODELS
Weekly Limit
Quota available
Five Hour Limit
Quota available
Within each group
"""


PRECISE_USAGE = """
Models & Quota
GEMINI MODELS
Weekly Limit
  [████] 100.00%
  100% remaining · Refreshes in 163h 19m
Five Hour Limit
  [████] 99.97%
  100% remaining · Refreshes in 4h 55m
CLAUDE AND GPT MODELS
Weekly Limit
  [████] 99.94%
  100% remaining · Refreshes in 167h 57m
Five Hour Limit
  [████] 99.70%
  100% remaining · Refreshes in 4h 57m
Within each group
"""


CURRENT_CODEX_STATUS = """
>_ OpenAI Codex (v0.146.0)
│  Model:                              gpt-5.6-sol (reasoning low)       │
│  Weekly limit:                       [██████████████████░░] 92% left   │
│  GPT-5.3-Codex-Spark Weekly limit:   [████████████████████] 100% left  │
"""


def test_quota_available_does_not_invent_a_numeric_percentage():
    parsed = monitor.parse_agy_usage(AVAILABLE_USAGE)

    assert parsed is not None
    weekly = parsed["gemini_weekly"]
    assert weekly["availability"] == "available"
    assert weekly["remaining_label"] == "Quota available"
    assert weekly["left_pct"] is None
    assert weekly["used_pct"] is None


def test_precise_bar_values_override_rounded_remaining_labels():
    parsed = monitor.parse_agy_usage(PRECISE_USAGE)

    assert parsed is not None
    expected = {
        "gemini_weekly": (100.0, 0.0, "100% remaining"),
        "gemini_5h": (99.97, 0.03, "99.97% remaining"),
        "ag_claude_gpt_weekly": (99.94, 0.06, "99.94% remaining"),
        "ag_claude_gpt_5h": (99.70, 0.30, "99.7% remaining"),
    }
    for key, (left, used, label) in expected.items():
        limit = parsed[key]
        assert limit["left_pct"] == pytest.approx(left)
        assert limit["used_pct"] == pytest.approx(used)
        assert limit["remaining_label"] == label

    assert monitor.limit_value_label(parsed["gemini_5h"]) == "0.03% used · 99.97% remaining"


def test_current_codex_status_without_reset_labels_is_parsed():
    parsed = monitor.parse_codex_status(CURRENT_CODEX_STATUS)

    assert parsed is not None
    assert parsed["main_model"] == "gpt-5.6-sol"
    assert parsed["main_weekly_left_pct"] == 92.0
    assert parsed["main_weekly_used_pct"] == 8.0
    assert parsed["main_weekly_reset"] is None
    assert parsed["spark_weekly_left_pct"] == 100.0
    assert parsed["spark_weekly_used_pct"] == 0.0
    assert parsed["spark_weekly_reset"] is None


def test_dead_codex_pane_is_never_treated_as_idle():
    dead_tail = CURRENT_CODEX_STATUS + "\n›\nPane is dead (status 0)\n"

    assert monitor.is_idle_codex(dead_tail) is False


def test_dead_codex_scrollback_is_not_used_as_a_fallback(monkeypatch):
    panes = [
        {"pane_id": "%dead", "target": "kun", "command": "node", "role": "Kun", "in_mode": "0", "dead": "1"},
    ]
    monkeypatch.setattr(monitor, "tmux_panes", lambda: panes)
    monkeypatch.setattr(monitor, "capture_pane", lambda pane_id, lines=500: CURRENT_CODEX_STATUS)

    codex, _, telemetry, _ = monitor.collect(False, 60, 300)

    assert codex is None
    assert telemetry["counts"]["codex_kun"] == 0


def test_explicit_slash_refresh_wins_over_stale_scrollback(monkeypatch):
    stale_codex = CURRENT_CODEX_STATUS.replace("92% left", "99% left")
    fresh_agy = PRECISE_USAGE.replace("100.00%", "99.18%", 1).replace("99.97%", "97.81%", 1)
    stale_agy = PRECISE_USAGE
    panes = [
        {"pane_id": "%codex", "target": "codex", "command": "codex", "role": "Kun", "in_mode": "0", "dead": "0"},
        {"pane_id": "%agy", "target": "agy", "command": "agy", "role": "Goru", "in_mode": "0", "dead": "0"},
    ]

    monkeypatch.setattr(monitor, "tmux_panes", lambda: panes)
    monkeypatch.setattr(
        monitor,
        "choose_pane",
        lambda _panes, kind: panes[0] if kind == "codex" else panes[1],
    )
    monkeypatch.setattr(
        monitor,
        "send_visible_command",
        lambda pane_id, command, wait: CURRENT_CODEX_STATUS if command == "/status" else fresh_agy,
    )
    monkeypatch.setattr(
        monitor,
        "capture_pane",
        lambda pane_id, lines=500: stale_codex if pane_id == "%codex" else stale_agy,
    )
    monkeypatch.setattr(
        monitor,
        "active_counts_and_context",
        lambda _panes: {"counts": {}, "tori_context_max_used_pct": None},
    )

    codex, agy, _, sources = monitor.collect(True, 60, 300)

    assert codex is not None and codex["main_weekly_used_pct"] == 8.0
    assert agy is not None and agy["gemini_weekly"]["left_pct"] == 99.18
    assert sources["codex_refreshed"] is True
    assert sources["agy_refreshed"] is True


def test_available_quota_card_withholds_fill_and_names_missing_measurement(monkeypatch):
    parsed = monitor.parse_agy_usage(AVAILABLE_USAGE)
    assert parsed is not None
    monkeypatch.setattr(monitor, "fetch_claude_quota_via_oauth", lambda: None)
    monkeypatch.setattr(
        monitor,
        "gemini_app_gauge",
        lambda observed_at: {
            "provider": "Gemini app / consumer",
            "fill_pct": None,
            "value_label": "no capture yet",
            "burn_advice": {"lane": "unknown"},
        },
    )
    monkeypatch.setattr(
        monitor,
        "nous_credits_gauge",
        lambda observed_at: {
            "provider": "Hermes / Nous credits",
            "big": "$43.13",
            "fill_pct": None,
            "value_label": "$43.13 total usable",
            "sub_gauges": [],
        },
    )

    canonical = monitor.update_gauges(
        {},
        codex=None,
        agy=parsed,
        telemetry={
            "counts": {
                "claude_fable_lana": 0,
                "codex_kun": 0,
                "gemini_goru": 2,
                "tori_hermes": 0,
            },
            "tori_context_max_used_pct": None,
        },
        observed_at="2026-07-21T09:15:27Z",
        slash_sources={"agy_refreshed": True, "agy_pane": "%249"},
    )
    card = next(
        gauge
        for gauge in canonical["provider_usage_gauges"]
        # renamed by the 2026-08-04 crew reorg; the subscription is still tracked
        if gauge["provider"] == "Antigravity / Gemini"
    )
    weekly = next(
        gauge for gauge in card["sub_gauges"] if gauge["label"] == "Gemini weekly used"
    )

    assert card["fill_pct"] is None
    assert card["tone"] == "ok"
    assert card["kind"] == "live visible Antigravity /usage quota signal (agent-request pool)"
    assert weekly["fill_pct"] is None
    assert weekly["value_label"] == "Available · exact usage/reset not exposed"

    claude_card = next(
        gauge
        for gauge in canonical["provider_usage_gauges"]
        if gauge["provider"] == "Claude / Fable / Lana"
    )
    assert claude_card["kind"] == "Claude last-visible quota fallback"
    assert claude_card["status"] == "Active panes live; approved OAuth usage read unavailable"
    assert "Approved read-only Claude OAuth usage check returned unavailable" in claude_card["detail"]
    assert "Last visible Claude usage-panel values retained" in claude_card["source_label"]
    assert "No credential/token file" not in claude_card["detail"]

    nous_card = next(
        gauge
        for gauge in canonical["provider_usage_gauges"]
        if gauge["provider"] == "Hermes / Nous credits"
    )
    assert nous_card["big"] == "$43.13"
    assert nous_card["fill_pct"] is None
    assert nous_card["value_label"] == "$43.13 total usable"

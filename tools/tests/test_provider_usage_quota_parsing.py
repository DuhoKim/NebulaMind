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


CODEX_STATUS_V0146 = """
\u256d\u2500\u2500\u2500\u2500\u2500\u256e
\u2502  >_ OpenAI Codex (v0.146.0)
\u2502  Model:                              gpt-5.6-sol (reasoning low, summaries auto)
\u2502  Account:                            duhokim81@gmail.com (Pro)
\u2502  Weekly limit:                       [\u2588\u2588\u2588\u2591\u2591] 76% left (resets 13:18 on 20 Aug)
\u2502  GPT-5.3-Codex-Spark Weekly limit:   [\u2588\u2588\u2588\u2588\u2588] 100% left (resets 17:10 on 26 Aug)
\u2570\u2500\u2500\u2500\u2500\u2500\u256f
"""


def test_codex_v0146_status_panel_is_parsed():
    parsed = monitor.parse_codex_status(CODEX_STATUS_V0146)

    assert parsed is not None
    assert parsed["main_model"] == "gpt-5.6-sol"
    assert parsed["account"] == "duhokim81@gmail.com"
    assert parsed["plan"] == "Pro"
    assert parsed["main_weekly_left_pct"] == 76.0
    assert parsed["main_weekly_used_pct"] == 24.0
    assert parsed["main_weekly_reset"] == "13:18 on 20 Aug"
    assert parsed["spark_weekly_left_pct"] == 100.0
    assert "main_5h_left_pct" not in parsed


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


def test_explicit_slash_refresh_wins_over_stale_scrollback(monkeypatch):
    fresh_agy = PRECISE_USAGE.replace("100.00%", "99.18%", 1).replace("99.97%", "97.81%", 1)
    stale_agy = PRECISE_USAGE
    panes = [
        {"pane_id": "%agy", "target": "goru-agy:agy.0", "command": "agy", "role": "Goru", "in_mode": "0", "dead": "0"},
    ]

    monkeypatch.setattr(monitor, "tmux_panes", lambda: panes)
    monkeypatch.setattr(monitor, "choose_pane", lambda _panes, kind: panes[0])
    monkeypatch.setattr(
        monitor,
        "send_visible_command",
        lambda pane_id, command, wait: fresh_agy,
    )
    monkeypatch.setattr(monitor, "capture_pane", lambda pane_id, lines=500: stale_agy)
    monkeypatch.setattr(
        monitor,
        "active_counts_and_context",
        lambda _panes: {"counts": {}, "gpt_context_max_used_pct": None},
    )

    agy, _codex, _, sources = monitor.collect(True, 60, 300)

    assert agy is not None and agy["gemini_weekly"]["left_pct"] == 99.18
    assert sources["agy_refreshed"] is True


def test_scrollback_scan_still_reads_agy_without_slash_refresh(monkeypatch):
    panes = [
        {"pane_id": "%agy", "target": "sextet-v2:goru.0", "command": "agy", "role": "", "in_mode": "0", "dead": "0"},
    ]
    monkeypatch.setattr(monitor, "tmux_panes", lambda: panes)
    monkeypatch.setattr(monitor, "capture_pane", lambda pane_id, lines=500: PRECISE_USAGE)

    agy, _codex, telemetry, sources = monitor.collect(False, 60, 300)

    assert agy is not None and agy["gemini_weekly"]["left_pct"] == 100.0
    assert sources.get("agy_refreshed") is None
    assert telemetry["counts"]["agy_seats"] == 1


def test_roster_counts_classify_directors_and_hermes_seats(monkeypatch):
    panes = [
        # Directors window: claude.exe panes whose roles name other seats must
        # still count as Claude seats, not Gemini/Tori ones.
        {"pane_id": "%1", "target": "ge-mastermind:Directors.0", "command": "claude.exe", "role": "Hwao-director", "in_mode": "0", "dead": "0"},
        {"pane_id": "%2", "target": "ge-mastermind:Directors.1", "command": "claude.exe", "role": "Goru-director-live-view", "in_mode": "0", "dead": "0"},
        {"pane_id": "%3", "target": "ge-mastermind:Directors.2", "command": "claude.exe", "role": "Tori-director", "in_mode": "0", "dead": "0"},
        {"pane_id": "%9", "target": "sextet-v2:p0-lana.0", "command": "claude.exe", "role": "", "in_mode": "0", "dead": "0"},
        {"pane_id": "%6", "target": "sextet-v2:goru.0", "command": "agy", "role": "", "in_mode": "0", "dead": "0"},
        {"pane_id": "%7", "target": "sextet-v2:kun.0", "command": "python3.11", "role": "", "in_mode": "0", "dead": "0"},
        {"pane_id": "%14", "target": "sextet-v2:mir1.0", "command": "python3.11", "role": "", "in_mode": "0", "dead": "0"},
        {"pane_id": "%8", "target": "sextet-v2:tori.0", "command": "python3.11", "role": "", "in_mode": "0", "dead": "0"},
        # gpt1's legacy window (yui) exists but no hermes profile is running: not an active seat.
        {"pane_id": "%4", "target": "sextet-v2:yui.0", "command": "zsh", "role": "", "in_mode": "0", "dead": "0"},
        {"pane_id": "%99", "target": "sextet-v2:kun2.0", "command": "python3.11", "role": "", "in_mode": "0", "dead": "1"},
    ]
    monkeypatch.setattr(monitor, "capture_pane", lambda pane_id, lines=500: "")

    telemetry = monitor.active_counts_and_context(panes)

    assert telemetry["counts"] == {
        "claude_seats": 4,
        "kimi_seats": 2,
        "agy_seats": 1,
        "gpt_seats": 1,
    }


def test_roster_counts_recognize_engine_named_windows(monkeypatch):
    """Windows renamed to the 2026-08-19 engine scheme (kimi1, gpt2, cseat1...)."""
    panes = [
        {"pane_id": "%9", "target": "sextet-v2:cseat1.0", "command": "claude.exe", "role": "", "in_mode": "0", "dead": "0"},
        {"pane_id": "%10", "target": "sextet-v2:agy.0", "command": "agy", "role": "", "in_mode": "0", "dead": "0"},
        {"pane_id": "%14", "target": "sextet-v2:kimi1.0", "command": "python3.11", "role": "", "in_mode": "0", "dead": "0"},
        {"pane_id": "%7", "target": "sextet-v2:old-kimi-a.0", "command": "python3.11", "role": "", "in_mode": "0", "dead": "0"},
        {"pane_id": "%8", "target": "sextet-v2:gpt2.0", "command": "python3.11", "role": "", "in_mode": "0", "dead": "0"},
        # gpt1 window with a bare shell: seat exists but no hermes profile running.
        {"pane_id": "%4", "target": "sextet-v2:gpt1.0", "command": "zsh", "role": "", "in_mode": "0", "dead": "0"},
    ]
    monkeypatch.setattr(monitor, "capture_pane", lambda pane_id, lines=500: "")

    telemetry = monitor.active_counts_and_context(panes)

    assert telemetry["counts"] == {
        "claude_seats": 1,
        "kimi_seats": 2,
        "agy_seats": 1,
        "gpt_seats": 1,
    }


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
        agy=parsed,
        codex=None,
        telemetry={
            "counts": {
                "claude_seats": 0,
                "kimi_seats": 0,
                "agy_seats": 2,
                "gpt_seats": 0,
            },
            "gpt_context_max_used_pct": None,
        },
        observed_at="2026-07-21T09:15:27Z",
        slash_sources={"agy_refreshed": True, "agy_pane": "%249"},
    )
    card = next(
        gauge
        for gauge in canonical["provider_usage_gauges"]
        # engine-named by the 2026-08-19 naming reform
        if gauge["provider"] == "Antigravity / agy (Gemini)"
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
        if gauge["provider"] == "Claude / Fable + claude-seat"
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

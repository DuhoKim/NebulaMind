"""Decision 2 regression tests for stale private usage-card visibility.

These tests patch every private/provider side-effecting card factory. They exercise
only the pure status-to-snapshot rendering path; no network, credential, browser,
or public cockpit operation is allowed.
"""
from __future__ import annotations

import json
import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import render_ge_autopilot_dashboard_v2 as renderer  # noqa: E402


PUBLIC_PROVIDER_NAMES = [
    "Claude / Fable + claude-seat",
    "Gemini app / consumer",
    "Hermes / Nous credits",
    "Moonshot / kimi (K3 direct)",
    "Antigravity / agy (Gemini)",
    "Codex",
]
PRIVATE_CARD_NAMES = [
    "Flow / Veo credits (Ultra)",
    "YouTube Data API",
]


def _gauge(name: str, percent: float | None, *, unknown_sub: bool = False) -> dict:
    sub_gauges = [
        {
            "label": "Weekly used",
            "fill_pct": percent,
            "value_label": "not observed" if percent is None else f"{percent:.0f}% used weekly",
            "tone": "warn" if percent is None else "ok",
        }
    ]
    if unknown_sub:
        sub_gauges.append(
            {
                "label": "Five-hour used",
                "fill_pct": None,
                "value_label": "not observed",
                "tone": "warn",
            }
        )
    return {
        "provider": name,
        "kind": "fixture provider quota",
        "status": "Live fixture reading",
        "fill_pct": percent,
        "value_label": "not observed" if percent is None else f"{percent:.0f}% used",
        "detail": "Fixture reading retained for stale-history verification.",
        "source_label": "Fixture provider observation at 2026-08-08T10:00:00Z.",
        "tone": "ok",
        "sub_gauges": sub_gauges,
    }


def _private_card(name: str) -> dict:
    return {
        "name": name,
        "kind": "fixture private card",
        "status": "fixture private status",
        "big": "Fixture",
        "percent": None,
        "percent_label": "fixture private value",
        "activity": "fixture private value",
        "detail": "Private card must remain unchanged by Decision 2.",
        "source": "fixture private source",
        "tone": "warn",
        "sub_gauges": [],
    }


def _public_status(observed_at: str) -> dict:
    gauges = [
        _gauge("Claude / Fable + claude-seat", 10.0, unknown_sub=True),
        _gauge("Hermes / gpt seats (context)", 50.0),
        _gauge("Gemini app / consumer", 1.0),
        _gauge("Flow / Veo (Ultra)", 0.0),
        _gauge("Hermes / Nous credits", None),
        _gauge("Moonshot / kimi (K3 direct)", 64.8),
        _gauge("Antigravity / agy (Gemini)", 1.0, unknown_sub=True),
        _gauge("Codex", 55.0, unknown_sub=True),
    ]
    return {
        "provider_usage_gauges": gauges,
        "provider_usage_monitor": {
            "marker": "PROVIDER_USAGE_REALTIME_MONITOR_V1",
            "status": "fixture monitor",
            "observed_at_utc": observed_at,
            "local_refresh_seconds": 300,
            "slash_refresh_seconds": 0,
            "active_pane_counts": {},
        },
    }


def _snapshot(monkeypatch, tmp_path: Path, *, observed_at: str) -> dict:
    public_status = tmp_path / "live-steering-status.json"
    public_status.write_text(json.dumps(_public_status(observed_at)))
    monkeypatch.setattr(renderer, "PUBLIC_USAGE_STATUS", public_status)
    monkeypatch.setattr(renderer, "_read_kimi_balance_cache", lambda: None)
    monkeypatch.setattr(
        renderer,
        "flow_credit_card",
        lambda: deepcopy(_private_card(PRIVATE_CARD_NAMES[0])),
    )
    monkeypatch.setattr(
        renderer,
        "youtube_api_quota_card",
        lambda: deepcopy(_private_card(PRIVATE_CARD_NAMES[1])),
    )
    snapshot = renderer.build_public_usage_snapshot({})
    assert snapshot is not None
    return snapshot


def test_stale_feed_keeps_provider_cards_visible_as_history(monkeypatch, tmp_path):
    snapshot = _snapshot(monkeypatch, tmp_path, observed_at="2026-08-01T00:00:00Z")

    assert [card["name"] for card in snapshot["cards"]] == (
        PUBLIC_PROVIDER_NAMES + PRIVATE_CARD_NAMES
    )
    assert snapshot["cache_state"] == "stale-source-visible"
    assert snapshot["provider_monitor_status"] == "STALE_PROVIDER_FEED_CARDS_VISIBLE"
    assert snapshot["exact_limit_percent_sources"] == 0
    assert "provider_gauge_count_hidden_as_stale" not in snapshot["sources"]
    assert snapshot["sources"]["provider_gauge_count_visible_as_stale"] == len(
        PUBLIC_PROVIDER_NAMES
    )

    for card in snapshot["cards"][: len(PUBLIC_PROVIDER_NAMES)]:
        assert card["classification"] in {
            "STALE HISTORICAL OBSERVATION",
            "UNAVAILABLE / UNKNOWN",
        }
        assert card["percent"] is None
        # Stale headlines carry the observation age since 2026-08-14.
        assert card["big"] == "Unknown" or card["big"].endswith(" ago")
        # Since 2026-08-14 stale cards keep the last reading with its age; cards
        # with no last reading say so.
        assert (
            card["percent_label"].startswith("Last measured ")
            or card["percent_label"] == "No current percentage — provider feed stale"
        )
        for sub_gauge in card["sub_gauges"]:
            assert sub_gauge["percent"] is None
            assert sub_gauge["value_label"] == "not observed" or sub_gauge[
                "value_label"
            ].startswith("Last observed — ")

    assert snapshot["cards"][-2:] == [
        _private_card(PRIVATE_CARD_NAMES[0]),
        _private_card(PRIVATE_CARD_NAMES[1]),
    ]


def test_fresh_feed_behavior_is_unchanged(monkeypatch, tmp_path):
    observed_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    snapshot = _snapshot(monkeypatch, tmp_path, observed_at=observed_at)

    assert snapshot["cache_state"] == "public-realtime-feed"
    assert [card["name"] for card in snapshot["cards"]] == (
        PUBLIC_PROVIDER_NAMES + PRIVATE_CARD_NAMES
    )
    assert snapshot["cards"][0]["percent"] == 10.0
    assert snapshot["cards"][0]["sub_gauges"][0]["percent"] == 10.0

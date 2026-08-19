"""Selectable headline hunk: card-local freshness must win before cosmetics."""
from __future__ import annotations

import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import render_ge_autopilot_dashboard_v2 as renderer  # noqa: E402


def _card(provider: str, percent: float | None, observed_at: str, *, big=None):
    return renderer.public_gauge_card({
        "provider": provider,
        "fill_pct": percent,
        "value_label": "not observed" if percent is None else f"{percent:.0f}% used",
        "big": big,
        "source_label": f"Fixture source observed {observed_at}.",
    })


def test_headline_uses_card_local_freshness_before_percent_fallback():
    now = datetime.now(timezone.utc)
    fresh = (now - timedelta(minutes=5)).isoformat().replace("+00:00", "Z")
    stale = (now - timedelta(hours=2)).isoformat().replace("+00:00", "Z")

    assert _card("Claude / Fable + claude-seat", 10.0, fresh)["big"] == "10%"
    assert _card("Gemini app / consumer", 1.0, fresh)["big"] == "1%"
    # Since 2026-08-14 a stale card headlines its age, not a bare "Stale".
    assert _card("Antigravity / agy (Gemini)", 1.0, stale)["big"].endswith(" ago")
    assert _card("Codex", 55.0, "timestamp-not-observed")["big"] == "Unknown"
    assert _card("Moonshot / kimi (K3 direct)", None, fresh, big="$33.30")["big"] == "$33.30"

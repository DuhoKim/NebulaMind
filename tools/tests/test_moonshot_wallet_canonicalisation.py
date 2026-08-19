"""RED/GREEN coverage for the canonical Moonshot wallet and card freshness metadata.

All endpoint and cache interactions are replaced with local fixtures. These tests
must never perform a real provider, browser, account, or public-cockpit operation.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import moonshot_balance_usage as moonshot  # noqa: E402
import render_ge_autopilot_dashboard_v2 as renderer  # noqa: E402


POOL_ID = "moonshot_kun_kimi_k3_wallet"
OLD_BALANCE = 80.41442


class _FakeResponse:
    def __init__(self, payload: dict):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self) -> bytes:
        return json.dumps(self.payload).encode("utf-8")


def _private_card(name: str) -> dict:
    return {
        "name": name,
        "kind": "fixture private card",
        "status": "fixture",
        "big": "Fixture",
        "percent": None,
        "percent_label": "fixture",
        "activity": "fixture",
        "detail": "fixture",
        "source": "fixture",
        "tone": "ok",
        "sub_gauges": [],
    }


def _stale_cache() -> dict:
    return {
        "marker": renderer.KIMI_BALANCE_CACHE_MARKER,
        "observed_at_utc": "2026-08-05T09:32:53Z",
        "available_balance_usd": OLD_BALANCE,
        "cash_balance_usd": OLD_BALANCE,
        "voucher_balance_usd": 0.0,
    }


def _moonshot_gauge(observed_at: str) -> dict:
    return {
        "pool_id": POOL_ID,
        "provider": "Moonshot / kimi (K3 direct)",
        "kind": "Moonshot direct-key dollar balance (read-only)",
        "classification": "FRESH LIVE METER",
        "observed_at_utc": observed_at,
        "current_value_known": True,
        "big": "$33.30",
        "available_balance_usd": 33.3,
        "cash_balance_usd": 33.3,
        "voucher_balance_usd": 0.0,
        "value_label": "$33.30 available · no fixed denominator",
        "fill_pct": None,
        "tone": "ok",
        "status": "Live official balance endpoint (key never emitted)",
        "detail": "Moonshot balance: $33.30 available (cash $33.30, voucher $0.00); peak observed $94.66.",
        "source_label": f"api.moonshot.ai/v1/users/me/balance fetched {observed_at}.",
        "planning_envelopes": [
            {
                "classification": "PLANNING ENVELOPE",
                "label": "Percent of observed peak consumed",
                "percent": 64.8,
                "peak_balance_usd": 94.66,
            }
        ],
    }


def _snapshot(monkeypatch, tmp_path: Path, *, wrapper_observed_at: str) -> tuple[dict, dict]:
    public_status = tmp_path / "live-steering-status.json"
    public_status.write_text(
        json.dumps(
            {
                "provider_usage_gauges": [_moonshot_gauge(wrapper_observed_at)],
                "provider_usage_monitor": {
                    "marker": "PROVIDER_USAGE_REALTIME_MONITOR_V1",
                    "status": "fixture monitor",
                    "observed_at_utc": wrapper_observed_at,
                    "active_pane_counts": {},
                },
            }
        )
    )
    monkeypatch.setattr(renderer, "PUBLIC_USAGE_STATUS", public_status)
    monkeypatch.setattr(renderer, "_read_kimi_balance_cache", _stale_cache)
    calls = {"private_kimi_card": 0}
    assert not hasattr(renderer, "_fetch_kimi_direct_balance")
    assert not hasattr(renderer, "kimi_direct_balance_card")
    monkeypatch.setattr(
        renderer,
        "flow_credit_card",
        lambda: _private_card("Flow / Veo credits (Ultra)"),
    )
    monkeypatch.setattr(
        renderer,
        "youtube_api_quota_card",
        lambda: _private_card("YouTube Data API"),
    )
    snapshot = renderer.build_public_usage_snapshot({})
    assert snapshot is not None
    return snapshot, calls


def _moonshot_cards(snapshot: dict) -> list[dict]:
    return [
        card
        for card in snapshot["cards"]
        if "moonshot" in card["name"].lower() or "kimi" in card["name"].lower()
    ]


def test_live_balance_gauge_uses_dollars_and_planning_envelope(monkeypatch, tmp_path):
    key_path = tmp_path / "moonshot.key"
    key_path.write_text("fixture-key-never-emitted")
    hwm_path = tmp_path / "moonshot-hwm.json"
    hwm_path.write_text(json.dumps({"hwm": 94.66}))
    monkeypatch.setattr(moonshot, "KEY_PATH", key_path)
    monkeypatch.setattr(moonshot, "HWM_PATH", hwm_path)
    monkeypatch.setattr(
        moonshot.urllib.request,
        "urlopen",
        lambda request, timeout: _FakeResponse(
            {
                "status": True,
                "data": {
                    "available_balance": 33.3,
                    "cash_balance": 33.3,
                    "voucher_balance": 0.0,
                },
            }
        ),
    )

    gauge = moonshot.fetch_gauge("2026-08-10T10:07:45Z")

    assert gauge["pool_id"] == POOL_ID
    assert gauge["classification"] == "FRESH LIVE METER"
    assert gauge["big"] == "$33.30"
    assert gauge["available_balance_usd"] == 33.3
    assert gauge["cash_balance_usd"] == 33.3
    assert gauge["voucher_balance_usd"] == 0.0
    assert gauge["fill_pct"] is None
    assert gauge["planning_envelopes"][0]["classification"] == "PLANNING ENVELOPE"
    assert gauge["planning_envelopes"][0]["percent"] == 64.8


def test_missing_balance_components_remain_unknown(monkeypatch, tmp_path):
    key_path = tmp_path / "moonshot.key"
    key_path.write_text("fixture-key-never-emitted")
    monkeypatch.setattr(moonshot, "KEY_PATH", key_path)
    monkeypatch.setattr(moonshot, "HWM_PATH", tmp_path / "moonshot-hwm.json")
    monkeypatch.setattr(
        moonshot.urllib.request,
        "urlopen",
        lambda request, timeout: _FakeResponse(
            {"status": True, "data": {"available_balance": 33.3}}
        ),
    )

    gauge = moonshot.fetch_gauge("2026-08-10T10:07:45Z")

    assert gauge["cash_balance_usd"] is None
    assert gauge["voucher_balance_usd"] is None
    assert "$0.00" not in gauge["detail"]


def test_fresh_snapshot_has_one_live_wallet_and_stale_cache_only_as_history(
    monkeypatch, tmp_path
):
    observed_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    snapshot, calls = _snapshot(
        monkeypatch, tmp_path, wrapper_observed_at=observed_at
    )

    wallets = _moonshot_cards(snapshot)
    assert calls["private_kimi_card"] == 0
    assert len(wallets) == 1
    wallet = wallets[0]
    assert wallet["name"] == "Moonshot / kimi (K3 direct)"
    assert wallet["pool_id"] == POOL_ID
    assert wallet["big"] == "$33.30"
    assert wallet["available_balance_usd"] == 33.3
    assert wallet["percent"] is None
    assert wallet["freshness_classification"] == "FRESH LIVE METER"
    assert len(wallet["historical_observations"]) == 1
    historical = wallet["historical_observations"][0]
    assert historical["classification"] == "STALE HISTORICAL OBSERVATION"
    assert historical["available_balance_usd"] == OLD_BALANCE
    assert historical["age_seconds"] > 0
    assert "superseded" in historical["status"].lower()
    assert "refresh unavailable" not in json.dumps(wallet).lower()


def test_stale_wrapper_cannot_show_old_private_wallet_as_confident_current(
    monkeypatch, tmp_path
):
    snapshot, calls = _snapshot(
        monkeypatch, tmp_path, wrapper_observed_at="2026-08-01T00:00:00Z"
    )

    wallets = _moonshot_cards(snapshot)
    assert calls["private_kimi_card"] == 0
    assert len(wallets) == 1
    wallet = wallets[0]
    # Stale headlines carry the observation age since 2026-08-14.
    assert wallet["big"].endswith(" ago") or wallet["big"] == "Last seen"
    assert wallet["percent"] is None
    assert wallet["available_balance_usd"] is None
    assert wallet["classification"] == "STALE HISTORICAL OBSERVATION"
    historical_values = {
        item.get("available_balance_usd") for item in wallet["historical_observations"]
    }
    assert historical_values == {33.3, OLD_BALANCE}
    assert "refresh unavailable" not in json.dumps(snapshot).lower()
    assert "$80.41" not in str(wallet.get("big"))


def test_per_card_freshness_is_bound_without_applying_headline_fallback():
    now = datetime.now(timezone.utc)
    recent = (now - timedelta(minutes=5)).isoformat().replace("+00:00", "Z")
    old = (now - timedelta(hours=2)).isoformat().replace("+00:00", "Z")

    fresh_claude = renderer.public_gauge_card(
        {
            "provider": "Claude / Fable + claude-seat",
            "fill_pct": 10.0,
            "value_label": "10% used",
            "source_label": f"OAuth usage fetched {recent}.",
        }
    )
    stale_antigravity = renderer.public_gauge_card(
        {
            "provider": "Antigravity / agy (Gemini)",
            "fill_pct": 1.0,
            "value_label": "1% used",
            "source_label": f"Visible pane observed {old}.",
        }
    )
    unknown_codex = renderer.public_gauge_card(
        {
            "provider": "Codex",
            "fill_pct": 55.0,
            "value_label": "55% used",
            "source_label": "Visible pane timestamp not observed.",
        }
    )

    assert fresh_claude["freshness_classification"] == "FRESH LIVE METER"
    assert stale_antigravity["freshness_classification"] == "STALE HISTORICAL OBSERVATION"
    assert unknown_codex["freshness_classification"] == "UNAVAILABLE / UNKNOWN"
    assert fresh_claude["freshness_max_age_seconds"] == 3600
    assert stale_antigravity["source_age_seconds"] > 3600
    # The classification-aware headline is applied per card (age labels for
    # stale cards since 2026-08-14, percent only when fresh).
    assert fresh_claude["big"] == "10%"
    assert stale_antigravity["big"].endswith(" ago")
    assert unknown_codex["big"] == "Unknown"

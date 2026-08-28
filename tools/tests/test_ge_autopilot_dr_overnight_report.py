from __future__ import annotations

import importlib.util
import json
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "render_ge_autopilot_dashboard_v2.py"
SPEC = importlib.util.spec_from_file_location("ge_dashboard_renderer", MODULE_PATH)
assert SPEC and SPEC.loader
renderer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(renderer)


EXPECTED_MARKER = renderer.OVERNIGHT_REPORT_MARKER


def usage_snapshot() -> dict:
    return {
        "cards": [{"name": f"provider-{idx}"} for idx in range(6)],
        "cache_state": "public-realtime-feed",
        "provider_monitor_status": "LIVE_SAFE_MONITOR_ACTIVE",
        "observed_at_utc": "2026-07-13T00:45:16Z",
        "cache_age_label": "12s",
    }


def test_c41_step2_report_shows_verified_fulltext_completion() -> None:
    report = renderer.build_overnight_report(usage_snapshot())

    # The overnight narrative (headline, cards, reported_at) is hand-updated every
    # run, so assert the stable read-only contract instead of a frozen snapshot.
    assert report["marker"] == EXPECTED_MARKER == renderer.OVERNIGHT_REPORT_MARKER
    assert report["approval_phrase"] == "NO ACTIVE EXECUTION PHRASE"
    assert report["reported_at_utc"].endswith("Z")
    assert "C41 Step 2 complete" in report["headline"]
    assert "sealed 180" in report["next_action"]

    cards = report["cards"]
    assert len(cards) >= 2
    # Usage-first invariant: the live usage card always leads.
    assert cards[0]["title"] == "Usage quota"
    assert cards[0]["big"] == "6 live cards"
    assert all({"title", "status", "detail"} <= card.keys() for card in cards)
    by_title = {card["title"]: card for card in cards}
    assert by_title["Sealed corpus"]["big"] == "180 / 180"
    assert by_title["Full-text access"]["big"] == "180 full text"
    assert by_title["Full-text access"]["status"] == "COMPLETE"
    assert by_title["Cache-first acquisition"]["big"] == "42 hits · 138 fetched"
    assert by_title["Independent verification"]["status"] == "PASS"
    assert by_title["Safety boundary"]["big"] == "0 risky actions"

    # No stale content from earlier snapshots leaks back in.
    rendered = repr(report)
    assert "Options pilot closed" not in rendered
    assert "Never launched" not in rendered
    assert "untracked driver and prompt" not in rendered
    assert "GE_AUTOPILOT_OVERNIGHT_REPORT_20260712" not in rendered
    assert "GE_AUTOPILOT_C1R_REPAIR_20260713T010203Z_DONE" not in rendered


def test_private_html_keeps_usage_first_and_c41_panel_is_read_only() -> None:
    page = renderer.render_html()

    assert EXPECTED_MARKER in page
    assert page.index('id="usage-monitor-panel"') < page.index('id="overnight-report-panel"')
    assert "C41 Step 2 full-text acquisition" in page
    assert "exactly the sealed 180 papers" in page
    assert "NO ACTIVE EXECUTION PHRASE" in page
    assert "C1r Deep Research overnight report" not in page
    assert "GE_AUTOPILOT_OVERNIGHT_REPORT_20260712" not in page
    assert "<button" not in page.lower()
    assert "<form" not in page.lower()


def test_private_usage_card_keeps_nous_separate_from_direct_kimi_credit() -> None:
    card = renderer.public_gauge_card(
        {
            "provider": "Hermes / Nous credits",
            "kind": "Nous Portal dollar balance (subscription + purchased top-up)",
            "status": "Free plan exhausted · top-up balance active",
            "big": "$0.91",
            "value_label": "$0.91 total usable · $0.00 of $0.10 plan left",
            "fill_pct": None,
            "detail": "Purchased top-up balance is $0.91.",
            "source_label": "Read-only GET /api/oauth/account.",
        }
    )

    assert card["name"] == "Hermes / Nous credits"
    assert card["big"] == "$0.91"
    assert card["percent"] is None
    assert "Kimi" not in card["detail"]


def test_direct_kimi_card_uses_official_usd_balance_without_inventing_percent() -> None:
    card = renderer.kimi_direct_balance_card_from_reading(
        {
            "marker": "KIMI_DIRECT_BALANCE_CACHE_V1",
            "observed_at_utc": "2026-08-04T14:40:00Z",
            "available_balance_usd": 99.79171,
            "cash_balance_usd": 99.79171,
            "voucher_balance_usd": 0,
        },
        stale=False,
    )

    assert card["name"] == "Kimi / Moonshot direct API"
    assert card["big"] == "$99.79"
    assert card["percent"] is None
    assert card["status"] == "Live read-only balance"
    assert "separate from Nous Portal" in card["detail"]
    assert card["sub_gauges"] == [
        {"label": "Cash balance", "percent": None, "value_label": "$99.79"},
        {"label": "Voucher balance", "percent": None, "value_label": "$0.00"},
    ]


def test_direct_kimi_fetch_caches_balance_but_never_the_api_key(
    monkeypatch, tmp_path: Path
) -> None:
    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return None

        def read(self) -> bytes:
            return json.dumps(
                {
                    "status": True,
                    "data": {
                        "available_balance": 99.79171,
                        "cash_balance": 99.79171,
                        "voucher_balance": 0,
                    },
                }
            ).encode()

    cache = tmp_path / "kimi-direct-balance.json"
    monkeypatch.setattr(renderer, "KIMI_BALANCE_CACHE_PATH", cache)
    monkeypatch.setenv("MOONSHOT_API_KEY", "test-secret-never-cache")
    monkeypatch.setattr(renderer.urllib.request, "urlopen", lambda *_a, **_k: Response())

    card = renderer.kimi_direct_balance_card()
    cached = json.loads(cache.read_text())

    assert card["status"] == "Live read-only balance"
    assert card["big"] == "$99.79"
    assert cached["available_balance_usd"] == 99.79171
    assert "test-secret-never-cache" not in cache.read_text()


def test_private_html_places_kimi_credit_in_the_top_four_quota_glance() -> None:
    page = renderer.render_html()
    glance = page[
        page.index("function renderQuotaGlance") : page.index("function usageCard")
    ]

    assert "Kimi / Moonshot direct API" in glance
    assert "quotaGlanceCard('Freshness'" not in glance

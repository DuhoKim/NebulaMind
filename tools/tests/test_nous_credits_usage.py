from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import nous_credits_usage as nous  # noqa: E402
# Other tools/tests inject a stub `stable_cockpit_renderer` into sys.modules to
# avoid the heavy import; run alphabetically before us, that stub (no
# render_provider_usage_gauges) shadows a bare import. Load the real module by path.
import importlib.util  # noqa: E402
_cockpit_spec = importlib.util.spec_from_file_location(
    "stable_cockpit_renderer_real", TOOLS / "stable_cockpit_renderer.py"
)
cockpit = importlib.util.module_from_spec(_cockpit_spec)
_cockpit_spec.loader.exec_module(cockpit)

NOW = datetime(2026, 7, 22, 8, 0, 0, tzinfo=timezone.utc)


def reading(**overrides):
    payload = {
        "schema": nous.SCHEMA,
        "captured_at_utc": "2026-07-22T08:00:00Z",
        "source": "account_api",
        "logged_in": True,
        "fresh": True,
        "paid_service_access": True,
        "plan": "Plus",
        "monthly_allowance_usd": 22.0,
        "subscription_remaining_usd": 0.0,
        "topup_remaining_usd": 43.1296673765218,
        "total_usable_usd": 43.1296673765218,
        "rollover_usd": 0.0,
        "renews_at": "2026-07-24T07:42:19.000Z",
    }
    payload.update(overrides)
    return payload


def test_validate_preserves_normalized_dollar_fields():
    checked = nous.validate_payload(reading())

    assert checked["plan"] == "Plus"
    assert checked["monthly_allowance_usd"] == 22.0
    assert checked["subscription_remaining_usd"] == 0.0
    assert checked["topup_remaining_usd"] == pytest.approx(43.1296673765218)
    assert checked["total_usable_usd"] == pytest.approx(43.1296673765218)


@pytest.mark.parametrize(
    "overrides",
    [
        {"schema": "WRONG"},
        {"monthly_allowance_usd": -1.0},
        {"monthly_allowance_usd": float("nan")},
        {"topup_remaining_usd": float("inf")},
        {"total_usable_usd": "43.13"},
        {"captured_at_utc": "yesterday"},
        {"source": "billing_page"},
    ],
)
def test_validate_rejects_untrustworthy_values(overrides):
    with pytest.raises(nous.NousCreditsError):
        nous.validate_payload(reading(**overrides))


def test_build_gauge_separates_subscription_and_topup_dollars():
    gauge = nous.build_gauge(nous.validate_payload(reading()), NOW, "observed")
    sub = {item["label"]: item for item in gauge["sub_gauges"]}

    assert gauge["provider"] == "Hermes / Nous credits"
    assert gauge["big"] == "$43.13"
    assert gauge["fill_pct"] is None
    assert gauge["tone"] == "warn"
    assert gauge["value_label"] == "$43.13 total usable · $0.00 of $22.00 plan left"
    assert gauge["status"] == "Plus plan exhausted · top-up balance active"
    assert sub["Monthly plan used"]["fill_pct"] == 100.0
    assert sub["Monthly plan used"]["value_label"] == "100% used · $0.00 / $22.00 left"
    assert sub["Top-up balance"]["fill_pct"] is None
    assert sub["Top-up balance"]["value_label"] == "$43.13 remaining · purchased balance"
    assert sub["Total usable"]["fill_pct"] is None
    assert sub["Total usable"]["value_label"] == "$43.13 available"
    assert "Renews Jul 24, 2026" in gauge["detail"]
    assert "GET /api/oauth/account" in gauge["source_label"]
    assert "top up" not in gauge["source_label"].lower()


def test_stable_cockpit_renders_amount_first_without_a_main_percentage():
    gauge = nous.build_gauge(nous.validate_payload(reading()), NOW, "observed")

    rendered = cockpit.render_provider_usage_gauges({"provider_usage_gauges": [gauge]})
    main = rendered.split('<div class="sub-gauge-list">', 1)[0]

    assert "$43.13 total usable" in main
    assert "aria-valuenow" not in main
    assert "Monthly plan used" in rendered
    assert 'aria-valuenow="100"' in rendered


def test_build_gauge_marks_zero_total_as_depleted():
    depleted = reading(
        paid_service_access=False,
        topup_remaining_usd=0.0,
        total_usable_usd=0.0,
    )
    gauge = nous.build_gauge(nous.validate_payload(depleted), NOW, "observed")

    assert gauge["tone"] == "danger"
    assert gauge["status"] == "Nous balance depleted"


def test_build_gauge_fail_open_withholds_numbers():
    gauge = nous.build_gauge(None, NOW, "observed", error="portal timeout")

    assert gauge["fill_pct"] is None
    assert gauge["big"] == "Unavailable"
    assert gauge["value_label"] == "current balance unavailable"
    assert gauge["tone"] == "warn"
    assert "portal timeout" in gauge["detail"]


def test_collect_reading_uses_normalized_subprocess_output_only():
    calls = []

    def fake_runner(command, **kwargs):
        calls.append((command, kwargs))
        return subprocess.CompletedProcess(command, 0, stdout=json.dumps(reading()), stderr="")

    got = nous.collect_reading(now=NOW, runner=fake_runner)

    assert got["total_usable_usd"] == pytest.approx(43.1296673765218)
    command, kwargs = calls[0]
    assert command[0] == str(nous.HERMES_PYTHON)
    assert kwargs["timeout"] == nous.COLLECT_TIMEOUT_SECONDS
    assert kwargs["cwd"] == str(nous.HERMES_SOURCE)
    assert "auth.json" not in " ".join(command)


def test_collect_reading_fails_closed_on_subprocess_error():
    def fake_runner(command, **kwargs):
        return subprocess.CompletedProcess(command, 2, stdout="", stderr="boom")

    with pytest.raises(nous.NousCreditsError, match="collector exited 2"):
        nous.collect_reading(now=NOW, runner=fake_runner)

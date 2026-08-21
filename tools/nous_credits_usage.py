#!/usr/bin/env python3
"""Read-only Nous Portal dollar balance for the provider usage dashboard.

The public monitor runs on Python 3.9, while Hermes' normalized account reader
runs inside its Python 3.11 venv. This module bridges them with a bounded child
process that emits only an allowlisted, non-PII JSON shape. Neither this module
nor the dashboard monitor reads auth files or handles OAuth tokens directly.
"""
from __future__ import annotations

import json
import math
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

SCHEMA = "NM_NOUS_CREDITS_USAGE_V1"
PROVIDER = "Hermes / Nous credits"

# Floor alert (2026-08-21). The Nous plan pool is $0.10/month, so all real spend
# comes from purchased top-up with no denominator and therefore no percentage to
# go red. $36 vanished in two days before anyone noticed. Below this, say so.
FLOOR_USD = 10.0
SOURCE = "account_api"
COLLECT_TIMEOUT_SECONDS = 15

HERMES_SOURCE = Path.home() / ".hermes/hermes-agent"
HERMES_PYTHON = (
    HERMES_SOURCE / "venv/bin/python"
    if (HERMES_SOURCE / "venv/bin/python").is_file()
    else HERMES_SOURCE / ".venv/bin/python"
)

_CHILD_CODE = r'''
import json
from datetime import datetime, timezone
from hermes_cli.nous_account import get_nous_portal_account_info

a = get_nous_portal_account_info(force_fresh=True)
s = a.subscription
p = a.paid_service_access_info
out = {
    "schema": "NM_NOUS_CREDITS_USAGE_V1",
    "captured_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "source": a.source,
    "logged_in": a.logged_in,
    "fresh": a.fresh,
    "paid_service_access": a.paid_service_access,
    "plan": getattr(s, "plan", None),
    "monthly_allowance_usd": getattr(s, "monthly_credits", None),
    "subscription_remaining_usd": getattr(s, "credits_remaining", None),
    "topup_remaining_usd": getattr(p, "purchased_credits_remaining", None),
    "total_usable_usd": getattr(p, "total_usable_credits", None),
    "rollover_usd": getattr(s, "rollover_credits", None),
    "renews_at": getattr(s, "current_period_end", None),
}
print(json.dumps(out))
'''


class NousCreditsError(ValueError):
    """Raised when the normalized collector output cannot be trusted."""


def parse_utc(value: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("timestamp is required")
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    parsed = datetime.fromisoformat(text)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def format_utc(value: datetime) -> str:
    return value.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _optional_money(payload: dict[str, Any], key: str, *, nonnegative: bool = True) -> float | None:
    value = payload.get(key)
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise NousCreditsError(f"{key} must be numeric or null")
    result = float(value)
    if not math.isfinite(result):
        raise NousCreditsError(f"{key} must be finite")
    if nonnegative and result < 0:
        raise NousCreditsError(f"{key} must be nonnegative")
    return result


def validate_payload(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise NousCreditsError("collector output must be a JSON object")
    if payload.get("schema") != SCHEMA:
        raise NousCreditsError(f"unexpected schema {payload.get('schema')!r}")
    if payload.get("source") != SOURCE:
        raise NousCreditsError(f"unexpected source {payload.get('source')!r}")
    if payload.get("logged_in") is not True or payload.get("fresh") is not True:
        raise NousCreditsError("Nous account snapshot is not fresh and logged in")

    captured_raw = payload.get("captured_at_utc")
    if not isinstance(captured_raw, str):
        raise NousCreditsError("captured_at_utc must be a timestamp string")
    try:
        captured_at = parse_utc(captured_raw)
    except (TypeError, ValueError) as exc:
        raise NousCreditsError(f"captured_at_utc is invalid: {exc}") from exc

    paid = payload.get("paid_service_access")
    if paid is not None and not isinstance(paid, bool):
        raise NousCreditsError("paid_service_access must be boolean or null")

    monthly = _optional_money(payload, "monthly_allowance_usd")
    subscription = _optional_money(payload, "subscription_remaining_usd", nonnegative=False)
    topup = _optional_money(payload, "topup_remaining_usd")
    total = _optional_money(payload, "total_usable_usd")
    rollover = _optional_money(payload, "rollover_usd")
    if total is None:
        raise NousCreditsError("total_usable_usd is required")

    plan = payload.get("plan")
    if plan is not None and not isinstance(plan, str):
        raise NousCreditsError("plan must be a string or null")
    renews = payload.get("renews_at")
    if renews is not None:
        if not isinstance(renews, str):
            raise NousCreditsError("renews_at must be a timestamp string or null")
        try:
            parse_utc(renews)
        except ValueError as exc:
            raise NousCreditsError(f"renews_at is invalid: {exc}") from exc

    return {
        "schema": SCHEMA,
        "captured_at_utc": format_utc(captured_at),
        "source": SOURCE,
        "logged_in": True,
        "fresh": True,
        "paid_service_access": paid,
        "plan": plan.strip() if isinstance(plan, str) and plan.strip() else None,
        "monthly_allowance_usd": monthly,
        "subscription_remaining_usd": subscription,
        "topup_remaining_usd": topup,
        "total_usable_usd": total,
        "rollover_usd": rollover,
        "renews_at": renews,
    }


def collect_reading(
    *,
    now: datetime | None = None,
    runner: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run,
) -> dict[str, Any]:
    del now  # The authoritative capture timestamp is generated in the child process.
    if not HERMES_PYTHON.is_file() or not HERMES_SOURCE.is_dir():
        raise NousCreditsError("Hermes account reader is not installed")
    command = [str(HERMES_PYTHON), "-c", _CHILD_CODE]
    completed = runner(
        command,
        text=True,
        capture_output=True,
        timeout=COLLECT_TIMEOUT_SECONDS,
        cwd=str(HERMES_SOURCE),
        check=False,
    )
    if completed.returncode != 0:
        raise NousCreditsError(f"collector exited {completed.returncode}")
    if len(completed.stdout) > 16_384:
        raise NousCreditsError("collector output exceeded the size bound")
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise NousCreditsError(f"collector output was not JSON: {exc}") from exc
    return validate_payload(payload)


def _usd(value: float | None) -> str:
    return f"${(value or 0.0):,.2f}"


def _human_date(value: str | None) -> str | None:
    if not value:
        return None
    try:
        parsed = parse_utc(value)
    except ValueError:
        return value
    return f"{parsed.strftime('%b')} {parsed.day}, {parsed.year}"


def _tone(used_pct: float | None, *, total: float, paid: bool | None, topup: float) -> str:
    if total <= 0 or paid is False:
        return "danger"
    if used_pct is not None and used_pct >= 100 and topup > 0:
        return "warn"
    if total < 5:
        return "warn"
    return "ok"


def build_gauge(
    reading: dict[str, Any] | None,
    now: datetime,
    observed_at: str,
    *,
    error: str | None = None,
) -> dict[str, Any]:
    base: dict[str, Any] = {
        "provider": PROVIDER,
        "kind": "Nous Portal dollar balance (subscription + purchased top-up)",
    }
    if reading is None:
        detail = "The read-only Nous Portal account snapshot was unavailable; no prior balance was reused."
        if error:
            detail += f" Collector error: {error}."
        base.update({
            "big": "Unavailable",
            "value_label": "current balance unavailable",
            "fill_pct": None,
            "tone": "warn",
            "status": "Nous balance unavailable",
            "detail": detail,
            "source_label": f"GET /api/oauth/account unavailable; checked {observed_at}.",
            "sub_gauges": [],
        })
        return base

    checked = validate_payload(reading)
    monthly = checked["monthly_allowance_usd"]
    subscription = checked["subscription_remaining_usd"]
    topup = checked["topup_remaining_usd"] or 0.0
    total = checked["total_usable_usd"]
    paid = checked["paid_service_access"]

    used_pct = None
    if monthly is not None and monthly > 0 and subscription is not None:
        used_pct = max(0.0, min(100.0, (monthly - subscription) / monthly * 100.0))

    if total <= 0 or paid is False:
        status = "Nous balance depleted"
    elif used_pct is not None and used_pct >= 100 and topup > 0:
        status = f"{checked['plan'] or 'Subscription'} plan exhausted · top-up balance active"
    elif total < 5:
        status = "Nous balance low"
    else:
        status = "Nous balance available"

    if monthly is not None and subscription is not None:
        value_label = f"{_usd(total)} total usable · {_usd(subscription)} of {_usd(monthly)} plan left"
    else:
        value_label = f"{_usd(total)} total usable"

    sub_gauges: list[dict[str, Any]] = []
    if used_pct is not None:
        sub_gauges.append({
            "label": "Monthly plan used",
            "value_label": f"{used_pct:.0f}% used · {_usd(subscription)} / {_usd(monthly)} left",
            "fill_pct": used_pct,
            "tone": "danger" if used_pct >= 100 else "warn" if used_pct >= 80 else "ok",
        })
    sub_gauges.extend([
        {
            "label": "Top-up balance",
            "value_label": (f"{_usd(topup)} remaining · purchased balance"
                            + (f" · BELOW THE {_usd(FLOOR_USD)} FLOOR" if topup < FLOOR_USD else "")),
            "fill_pct": None,
            "tone": "danger" if topup < FLOOR_USD else ("warn" if topup < FLOOR_USD * 2 else "ok"),
        },
        {
            "label": "Total usable",
            "value_label": f"{_usd(total)} available",
            "fill_pct": None,
            "tone": "danger" if total <= 0 else "warn" if total < 5 else "ok",
        },
    ])

    renewal = _human_date(checked["renews_at"])
    detail_parts = [
        f"{checked['plan'] or 'Nous'} subscription allowance is {_usd(monthly)}; {_usd(subscription)} remains in the current plan pool.",
        f"Purchased top-up balance is {_usd(topup)}, so total usable Hermes/Nous balance is {_usd(total)}.",
    ]
    if renewal:
        detail_parts.append(f"Renews {renewal}.")
    detail_parts.append("Balances are USD amounts despite legacy internal field names; purchased top-up has no fixed denominator, so no percentage is invented for it.")
    # The plan pool is $0.10, so every real call bills top-up — and with no
    # denominator there is no percentage to turn red. $36 went in two days
    # unnoticed (2026-08-21); name the floor explicitly instead.
    if topup < FLOOR_USD:
        detail_parts.append(f"TOP-UP IS BELOW THE {_usd(FLOOR_USD)} FLOOR — pause Nous-routed "
                            f"gating and surface to Duho, as with the Moonshot wallet.")
    elif topup < FLOOR_USD * 2:
        detail_parts.append(f"Top-up is within 2x of the {_usd(FLOOR_USD)} floor. Nous funds TTS "
                            f"and gateway tools; kimi gates belong on the Moonshot direct key.")

    age_seconds = max(0, int((now - parse_utc(checked["captured_at_utc"])).total_seconds()))
    base.update({
        "big": _usd(total),
        "value_label": value_label,
        "fill_pct": None,
        "tone": _tone(used_pct, total=total, paid=paid, topup=topup),
        "status": status,
        "detail": " ".join(detail_parts),
        "source_label": (
            f"Read-only GET /api/oauth/account captured {checked['captured_at_utc']} "
            f"({age_seconds}s before render) during monitor pass {observed_at}."
        ),
        "sub_gauges": sub_gauges,
    })
    return base


def fetch_gauge(observed_at: str) -> dict[str, Any]:
    now = parse_utc(observed_at)
    try:
        reading = collect_reading(now=now)
        return build_gauge(reading, now, observed_at)
    except (NousCreditsError, OSError, subprocess.SubprocessError) as exc:
        return build_gauge(None, now, observed_at, error=str(exc))


if __name__ == "__main__":
    observed = format_utc(datetime.now(timezone.utc))
    print(json.dumps(fetch_gauge(observed), indent=2))

#!/usr/bin/env python3
"""Read-only Moonshot (Kimi K3 direct key) dollar balance for the provider dashboard.

Safety model mirrors nous_credits_usage: the key is read from its chmod-600 file and
sent only as an Authorization header to the official balance endpoint; the key value
is never logged, never emitted into any gauge field, and no billing/account mutation
exists on this route. Failure modes withhold the value rather than guessing.

fill_pct is percent-of-peak-consumed against a locally recorded high-water mark
(max available balance ever observed), which is honest without knowing top-up history.
"""
from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA = "NM_MOONSHOT_BALANCE_V1"
PROVIDER = "Moonshot / Kun (Kimi K3)"
KEY_PATH = Path.home() / ".hermes/moonshot.key"
HWM_PATH = Path.home() / ".hermes/moonshot_balance_hwm.json"
BALANCE_URL = "https://api.moonshot.ai/v1/users/me/balance"
TIMEOUT = 10


def _tone(avail: float) -> str:
    if avail < 2.0:
        return "bad"
    if avail < 5.0:
        return "warn"
    return "ok"


def _withheld(observed_at: str, why: str) -> dict[str, Any]:
    return {
        "provider": PROVIDER,
        "kind": "Moonshot direct-key dollar balance (read-only)",
        "value_label": "balance not captured",
        "fill_pct": None,
        "tone": "neutral",
        "status": "Balance read unavailable — value withheld",
        "detail": f"Read-only balance endpoint not usable: {why}. No key value emitted; nothing guessed.",
        "source_label": f"api.moonshot.ai/v1/users/me/balance attempted {observed_at}.",
    }


def fetch_gauge(observed_at: str) -> dict[str, Any]:
    if not KEY_PATH.is_file():
        return _withheld(observed_at, f"{KEY_PATH} missing")
    try:
        key = KEY_PATH.read_text().strip()
        req = urllib.request.Request(BALANCE_URL)
        req.add_header("Authorization", f"Bearer {key}")
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001 — any failure withholds, never guesses
        return _withheld(observed_at, type(exc).__name__)
    data = payload.get("data") or {}
    avail = data.get("available_balance")
    if avail is None:
        return _withheld(observed_at, "response missing available_balance")
    avail = float(avail)
    voucher = float(data.get("voucher_balance") or 0.0)
    cash = float(data.get("cash_balance") or 0.0)
    hwm = avail
    try:
        if HWM_PATH.is_file():
            hwm = max(avail, float(json.loads(HWM_PATH.read_text()).get("hwm", avail)))
        HWM_PATH.write_text(json.dumps({"hwm": hwm, "at": datetime.now(timezone.utc).isoformat()}))
    except Exception:
        hwm = avail
    used_pct = round(100.0 * (1.0 - avail / hwm), 1) if hwm > 0 else None
    return {
        "provider": PROVIDER,
        "kind": "Moonshot direct-key dollar balance (read-only)",
        "value_label": f"${avail:.2f} available · {used_pct if used_pct is not None else '?'}% of peak used",
        "fill_pct": used_pct,
        "tone": _tone(avail),
        "status": "Live official balance endpoint (key never emitted)",
        "detail": (
            f"Moonshot balance: ${avail:.2f} available (cash ${cash:.2f}, voucher ${voucher:.2f}); "
            f"peak observed ${hwm:.2f}. Kimi K3 pricing $3/M in · $15/M out · $0.30/M cache-hit. "
            "Kun's review one-shots run on this key; Nous route retired for Kun."
        ),
        "source_label": f"api.moonshot.ai/v1/users/me/balance fetched {observed_at}.",
    }


if __name__ == "__main__":
    print(json.dumps(fetch_gauge(datetime.now(timezone.utc).isoformat()), indent=1))

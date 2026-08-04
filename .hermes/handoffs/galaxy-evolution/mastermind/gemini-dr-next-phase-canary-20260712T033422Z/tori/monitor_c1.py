#!/usr/bin/env python3
"""Bounded exact-tab read-only monitor for the single armed C1 canary."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADAPTER_DIR = ROOT / "phaseA" / "adapter"
sys.path.insert(0, str(ADAPTER_DIR))
from real_dom_adapter import build_js_probe, classify_signal  # noqa: E402


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def applescript_quote(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def read_signal(window_id: int, tab_index: int) -> dict:
    js = build_js_probe()
    script = (
        'tell application "Google Chrome"\n'
        f"set t to tab {tab_index} of window id {window_id}\n"
        f"return execute t javascript {applescript_quote(js)}\n"
        "end tell"
    )
    run = subprocess.run(
        ["osascript", "-e", script],
        text=True,
        capture_output=True,
        timeout=20,
    )
    if run.returncode != 0:
        raise RuntimeError(run.stderr.strip() or "osascript returned nonzero")
    return json.loads(run.stdout)


def append_event(path: Path, event: dict) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--window-id", type=int, required=True)
    parser.add_argument("--tab-index", type=int, required=True)
    parser.add_argument("--expected-url", required=True)
    parser.add_argument("--events", type=Path, required=True)
    parser.add_argument("--interval", type=int, default=30)
    parser.add_argument("--timeout", type=int, default=3600)
    args = parser.parse_args()

    args.events.parent.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    previous = None
    while time.monotonic() - started <= args.timeout:
        try:
            signal = read_signal(args.window_id, args.tab_index)
            state = classify_signal(signal, expected_url=args.expected_url)
            event = {"utc": utc_now(), "state": state, "signal": signal}
        except Exception as exc:
            event = {"utc": utc_now(), "state": "READ_CHANNEL_LOSS", "error": str(exc)}
            append_event(args.events, event)
            print(json.dumps(event, sort_keys=True), flush=True)
            return 20

        fingerprint = json.dumps(event["signal"], sort_keys=True)
        if fingerprint != previous:
            append_event(args.events, event)
            print(json.dumps(event, sort_keys=True), flush=True)
            previous = fingerprint

        if state == "COMPLETE":
            return 0
        if state in {"TARGET_MISMATCH", "VERIFICATION_WALL", "LOGIN_WALL", "BILLING_WALL"}:
            return 21
        time.sleep(args.interval)

    event = {"utc": utc_now(), "state": "TIMEOUT"}
    append_event(args.events, event)
    print(json.dumps(event, sort_keys=True), flush=True)
    return 22


if __name__ == "__main__":
    raise SystemExit(main())

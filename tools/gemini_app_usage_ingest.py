#!/usr/bin/env python3
"""Ingest a human-confirmed gemini.google.com/usage capture into the drop-file.

  python3 tools/gemini_app_usage_ingest.py --emit-bookmarklet   # install once
  python3 tools/gemini_app_usage_ingest.py --from-clipboard     # after clicking it
  python3 tools/gemini_app_usage_ingest.py --used-pct 47 --resets "in 3 hr 20 min"
  python3 tools/gemini_app_usage_ingest.py --show

No credentials, cookies, or network access are involved: the operator reads the
page, confirms the number, and it arrives here via the clipboard.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gemini_app_usage import (  # noqa: E402
    SCHEMA,
    ReadingError,
    build_gauge,
    burn_advice,
    format_utc,
    load_reading,
    reading_path,
    write_reading,
)

BOOKMARKLET_SRC = Path(__file__).resolve().parent / 'gemini_app_usage_bookmarklet.js'


def read_clipboard() -> str:
    if sys.platform != 'darwin':
        raise SystemExit('--from-clipboard uses pbpaste (macOS). Pipe the JSON to --stdin instead.')
    cp = subprocess.run(['pbpaste'], text=True, capture_output=True, check=False)
    if cp.returncode != 0:
        raise SystemExit(f'pbpaste failed: {cp.stderr.strip()}')
    return cp.stdout


def parse_relative_reset(label: str, captured_at: datetime) -> str | None:
    """'in 3 hr 20 min' -> absolute UTC. Returns None when nothing parseable."""
    # Longest alternative first: 'h|hr|hour' would match the 'h' of 'hr' and
    # strand the 'r', silently dropping the minutes that follow.
    match = re.search(
        r'in\s+(?:(\d+)\s*(?:hours?|hrs?|h)\b)?\s*(?:(\d+)\s*(?:minutes?|mins?|m)\b)?',
        label,
        re.IGNORECASE,
    )
    if not match or not (match.group(1) or match.group(2)):
        return None
    minutes = int(match.group(1) or 0) * 60 + int(match.group(2) or 0)
    if not minutes:
        return None
    return format_utc(captured_at + timedelta(minutes=minutes))


def emit_bookmarklet() -> None:
    from urllib.parse import quote

    source = BOOKMARKLET_SRC.read_text()
    print('Create a bookmark whose URL is exactly the line below, then open')
    print('https://gemini.google.com/usage (Settings -> Usage Limits) and click it.\n')
    print('javascript:' + quote(source, safe=''))


def show_current() -> int:
    now = datetime.now(timezone.utc)
    try:
        reading = load_reading()
    except ReadingError as exc:
        print(f'drop-file at {reading_path()} is not trustworthy: {exc}', file=sys.stderr)
        return 1
    if reading is None:
        print(f'No capture at {reading_path()}.')
    else:
        print(json.dumps(reading, indent=2, sort_keys=True))
    print('\nburn advice:')
    print(json.dumps(burn_advice(reading, now), indent=2, sort_keys=True))
    print('\ngauge:')
    print(json.dumps(build_gauge(reading, now, format_utc(now)), indent=2, sort_keys=True))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group()
    src.add_argument('--from-clipboard', action='store_true', help='read the bookmarklet JSON via pbpaste')
    src.add_argument('--stdin', action='store_true', help='read the bookmarklet JSON from stdin')
    src.add_argument('--json', metavar='JSON', help='the bookmarklet JSON as a literal string')
    src.add_argument('--used-pct', type=float, metavar='N', help='enter the used percentage by hand (0-100)')
    src.add_argument('--emit-bookmarklet', action='store_true', help='print the javascript: bookmarklet URL')
    src.add_argument('--show', action='store_true', help='print the current reading, advice, and gauge')
    ap.add_argument('--resets', default='', help='reset text, e.g. "in 3 hr 20 min" (with --used-pct)')
    ap.add_argument('--tier', default='', help='plan tier, e.g. "AI Pro" (with --used-pct)')
    ap.add_argument('--path', type=Path, default=None, help='override the drop-file path')
    args = ap.parse_args()

    if args.emit_bookmarklet:
        emit_bookmarklet()
        return 0
    if args.show:
        return show_current()

    if args.used_pct is not None:
        captured_at = datetime.now(timezone.utc)
        payload = {
            'schema': SCHEMA,
            'used_pct': args.used_pct,
            'reset_label': args.resets or None,
            'reset_at_utc': parse_relative_reset(args.resets, captured_at),
            'tier': args.tier or None,
            'source_url': 'https://gemini.google.com/usage',
            'captured_at_utc': format_utc(captured_at),
            'capture_method': 'manual',
        }
    else:
        if args.from_clipboard:
            raw = read_clipboard()
        elif args.stdin:
            raw = sys.stdin.read()
        elif args.json:
            raw = args.json
        else:
            ap.print_help()
            return 2
        if not raw.strip():
            raise SystemExit('No JSON found. Click the bookmarklet on gemini.google.com/usage first.')
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise SystemExit(f'Clipboard does not hold the capture JSON: {exc}') from exc

    try:
        dest = write_reading(payload, args.path)
    except ReadingError as exc:
        raise SystemExit(f'Refusing to store an untrustworthy reading: {exc}') from exc

    now = datetime.now(timezone.utc)
    stored = load_reading(dest)
    advice = burn_advice(stored, now)
    print(f'Stored {stored["used_pct"]:.0f}% used -> {dest}')
    print(f'Lane: {advice["lane"]} ({advice["headroom_pct"]:.0f}% headroom) — {advice["rationale"]}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Unattended refresh of the Gemini app usage reading by scraping Chrome's DOM.

Unlike the bookmarklet path, no human confirms the number here. That makes this
tool ToS-adjacent (it drives your logged-in browser) and it is deliberately kept
OUT of live_provider_usage_monitor.py, whose safety model forbids browser
automation. Schedule it separately if you want it; the monitor only ever reads
the drop-file it writes.

Two one-time macOS grants are required before it can read anything:
  1. System Settings -> Privacy & Security -> Automation: allow the controlling
     terminal to control Google Chrome (first run raises AppleEvents error -1743).
  2. Chrome -> View -> Developer -> Allow JavaScript from Apple Events.

Safety: an unattended read that isn't confident abstains rather than storing a
guess, and abstaining never overwrites an existing (possibly human-confirmed)
reading.

  python3 tools/gemini_app_usage_autofetch.py            # scrape and store
  python3 tools/gemini_app_usage_autofetch.py --dry-run  # scrape, print, store nothing
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gemini_app_usage import (  # noqa: E402
    SCHEMA,
    ReadingError,
    burn_advice,
    format_utc,
    load_reading,
    reading_path,
    write_reading,
)
from gemini_app_usage_ingest import parse_reset  # noqa: E402

EXTRACTOR_JS = Path(__file__).resolve().parent / 'gemini_app_usage_extractor.js'
USAGE_URL = 'https://gemini.google.com/usage'

# An unattended read is trusted only from these signals. 'any-text' means the
# extractor fell back to the first percentage anywhere on the page — too easy to
# grab an unrelated number with nobody watching, so it abstains.
TRUSTED_SIGNALS = frozenset({'progressbar', 'scoped-text'})


class AutofetchError(RuntimeError):
    """Chrome could not be driven or the page could not be read."""


def build_applescript(extractor_path: Path, url: str, load_wait: float) -> str:
    """AppleScript that finds/opens the usage tab and runs the extractor file.

    Reading the JS from a file avoids quoting the regex-heavy script through two
    layers of string escaping.
    """
    js_path = str(extractor_path)
    return f'''
set jsCode to (read (POSIX file "{js_path}") as «class utf8»)
tell application "Google Chrome"
  set target to missing value
  repeat with w in windows
    repeat with t in tabs of w
      if (URL of t) contains "gemini.google.com/usage" then set target to t
    end repeat
  end repeat
  if target is missing value then
    if (count of windows) is 0 then make new window
    set target to make new tab at end of tabs of front window with properties {{URL:"{url}"}}
    delay {load_wait}
  end if
  set jsResult to execute target javascript jsCode
  return jsResult
end tell
'''


def friendly_osascript_error(err: str) -> str:
    """Map a raw osascript failure to an actionable message.

    Chrome's errors are localized (a Korean install returns no English 'JavaScript'
    and code (12), not -2700), so match on locale-stable anchors: the -1743 code for
    the Automation grant, and Chrome's support-page slug for the JS-bridge toggle.
    """
    if '-1743' in err:
        return (
            'macOS has not granted this terminal permission to control Google Chrome. '
            'Grant it once in System Settings -> Privacy & Security -> Automation, then retry.'
        )
    if 'p=applescript' in err or '-2700' in err or 'javascript' in err.lower():
        return (
            "Chrome refused 'execute javascript'. Enable it once in "
            'Chrome -> View -> Developer -> Allow JavaScript from Apple Events, then retry.'
        )
    return f'osascript failed: {err}'


def run_applescript(script: str, timeout: int = 40) -> str:
    cp = subprocess.run(['osascript', '-'], input=script, text=True, capture_output=True, timeout=timeout)
    if cp.returncode != 0:
        raise AutofetchError(friendly_osascript_error(cp.stderr.strip()))
    return cp.stdout.strip()


def scrape() -> dict:
    """Drive Chrome and return the extractor's parsed JSON. Raises on failure."""
    if not EXTRACTOR_JS.exists():
        raise AutofetchError(f'extractor not found at {EXTRACTOR_JS}')
    raw = run_applescript(build_applescript(EXTRACTOR_JS, USAGE_URL, load_wait=4.0))
    if not raw:
        raise AutofetchError('Chrome returned nothing (is a usage tab reachable?).')
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise AutofetchError(f'extractor did not return JSON: {raw[:200]!r}') from exc


def build_reading(extract: dict, now: datetime) -> dict:
    """Assemble a drop-file reading from an extractor result. No I/O, no gating."""
    captured_at = format_utc(now)
    label = str(extract.get('reset_label') or '')
    tier = str(extract.get('tier_guess') or '').strip() or None
    return {
        'schema': SCHEMA,
        'used_pct': extract.get('used_pct'),
        'reset_label': label or None,
        'reset_at_utc': parse_reset(label, now) if label else None,
        'tier': tier,
        'source_url': USAGE_URL,
        'captured_at_utc': captured_at,
        'capture_method': 'chrome-auto',
    }


def process_extraction(extract: dict, now: datetime, path: Path | None = None, *, dry_run: bool = False) -> dict:
    """Gate an extractor result and, unless dry-run, store it. Never guesses.

    Returns a report dict: {'stored': bool, 'reason': str, 'reading': dict|None}.
    Abstains (stores nothing, keeps any existing reading) on a weak signal, an
    off-page scrape, or a percentage the module would reject.
    """
    signal = extract.get('source_signal')
    if not extract.get('on_usage_page', False):
        return {'stored': False, 'reason': 'not on the usage page', 'reading': None}
    if signal not in TRUSTED_SIGNALS:
        return {'stored': False, 'reason': f'low-confidence signal ({signal}); abstaining', 'reading': None}

    reading = build_reading(extract, now)

    # The usage page rarely names the plan, so a scrape usually yields tier=None.
    # Carry forward the last operator-confirmed tier rather than wiping it on every
    # unattended refresh — it is a remembered confirmed value, not an invented one.
    if reading['tier'] is None:
        try:
            prior = load_reading(path)
        except ReadingError:
            prior = None
        if prior and prior.get('tier'):
            reading['tier'] = prior['tier']

    try:
        # validate() runs inside write_reading(); pre-check so a bad scrape abstains
        # instead of raising, and so --dry-run reports the same verdict.
        from gemini_app_usage import validate
        checked = validate(reading)
    except ReadingError as exc:
        return {'stored': False, 'reason': f'rejected reading: {exc}', 'reading': None}

    if dry_run:
        return {'stored': False, 'reason': 'dry-run', 'reading': checked}
    write_reading(checked, path)
    return {'stored': True, 'reason': 'stored', 'reading': checked}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dry-run', action='store_true', help='scrape and print, but store nothing')
    ap.add_argument('--path', type=Path, default=None, help='override the drop-file path')
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    try:
        extract = scrape()
    except AutofetchError as exc:
        print(f'autofetch failed: {exc}', file=sys.stderr)
        return 2

    report = process_extraction(extract, now, args.path, dry_run=args.dry_run)
    if report['reading'] is None and not report['stored']:
        print(f'abstained: {report["reason"]}. Existing reading at {args.path or reading_path()} left untouched.')
        return 1

    reading = report['reading']
    advice = burn_advice(reading, now)
    verb = 'would store' if args.dry_run else 'stored'
    print(f'{verb} {reading["used_pct"]:.0f}% used (tier {reading["tier"]}, {reading["capture_method"]})')
    print(f'lane: {advice["lane"]} ({advice["headroom_pct"]:.0f}% headroom)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

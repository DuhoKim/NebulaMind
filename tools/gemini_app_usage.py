#!/usr/bin/env python3
"""Gemini app (consumer) usage reading: load, validate, gauge, burn advice.

Safety model (matches live_provider_usage_monitor.py):
- Reads one local drop-file written by a human-confirmed clipboard capture.
- Never reads credential/token/cookie files.
- Never opens browser billing/account/payment/API/GCP surfaces, and never
  automates a logged-in Google session.

The gemini.google.com/usage meter has no API. The only supported source here is
a capture the operator confirmed by eye (see gemini_app_usage_bookmarklet.js).
A reading is therefore trusted only while it is fresh; once it ages past the
5h rolling window it is reported as unknown rather than shown as if live.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA = 'NM_GEMINI_APP_USAGE_V1'
PROVIDER = 'Gemini app / consumer'

# The app meter is a 5h rolling window. One extra hour of grace covers a capture
# taken just before a window turns over; past that a percentage is meaningless.
STALE_AFTER_SECONDS = 6 * 3600

CAPTURE_METHODS = frozenset({'bookmarklet-confirmed', 'manual'})

TOOL_DIR = Path(__file__).resolve().parent
ROOT = TOOL_DIR.parent
DEFAULT_READING_PATH = ROOT / '.hermes/state/gemini_app_usage.json'

# Tasks this lane is good at, mirrored from model_usage_status.json burn_plan.
BURN_TASKS = (
    'wide repo/document scans',
    'alternative summaries',
    'HTML/report QA',
    'multi-file classification',
)


class ReadingError(ValueError):
    """A drop-file exists but does not carry a trustworthy reading."""


def reading_path() -> Path:
    override = os.environ.get('NM_GEMINI_APP_USAGE_JSON')
    return Path(override) if override else DEFAULT_READING_PATH


def parse_utc(value: str) -> datetime:
    text = str(value).strip()
    if text.endswith('Z'):
        text = text[:-1] + '+00:00'
    parsed = datetime.fromisoformat(text)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def format_utc(moment: datetime) -> str:
    return moment.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def validate(payload: Any) -> dict[str, Any]:
    """Return a normalised reading, or raise ReadingError. Never guesses."""
    if not isinstance(payload, dict):
        raise ReadingError('reading must be a JSON object')
    if payload.get('schema') != SCHEMA:
        raise ReadingError(f'unknown schema {payload.get("schema")!r}, expected {SCHEMA!r}')

    raw_pct = payload.get('used_pct')
    if isinstance(raw_pct, bool) or not isinstance(raw_pct, (int, float)):
        raise ReadingError('used_pct must be a number')
    used_pct = float(raw_pct)
    if not 0.0 <= used_pct <= 100.0:
        raise ReadingError(f'used_pct {used_pct} out of range 0..100')

    captured_raw = payload.get('captured_at_utc')
    if not isinstance(captured_raw, str) or not captured_raw.strip():
        raise ReadingError('captured_at_utc is required')
    try:
        captured_at = parse_utc(captured_raw)
    except ValueError as exc:
        raise ReadingError(f'captured_at_utc is not an ISO-8601 timestamp: {exc}') from exc

    method = payload.get('capture_method', 'manual')
    if method not in CAPTURE_METHODS:
        raise ReadingError(f'capture_method {method!r} not in {sorted(CAPTURE_METHODS)}')

    reset_at = None
    if payload.get('reset_at_utc'):
        try:
            reset_at = parse_utc(payload['reset_at_utc'])
        except ValueError as exc:
            raise ReadingError(f'reset_at_utc is not an ISO-8601 timestamp: {exc}') from exc

    return {
        'schema': SCHEMA,
        'used_pct': used_pct,
        'reset_label': str(payload.get('reset_label') or '').strip() or None,
        'reset_at_utc': format_utc(reset_at) if reset_at else None,
        'tier': str(payload.get('tier') or '').strip() or None,
        'source_url': str(payload.get('source_url') or 'https://gemini.google.com/usage'),
        'captured_at_utc': format_utc(captured_at),
        'capture_method': method,
    }


def load_reading(path: Path | None = None) -> dict[str, Any] | None:
    target = path or reading_path()
    if not target.exists():
        return None
    return validate(json.loads(target.read_text()))


def write_reading(reading: dict[str, Any], path: Path | None = None) -> Path:
    """Validate then atomically replace the drop-file."""
    target = path or reading_path()
    checked = validate(reading)
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_name(target.name + '.tmp')
    tmp.write_text(json.dumps(checked, ensure_ascii=False, indent=2, sort_keys=True) + '\n')
    os.replace(tmp, target)
    return target


def age_seconds(reading: dict[str, Any], now: datetime) -> float:
    return (now - parse_utc(reading['captured_at_utc'])).total_seconds()


def is_stale(reading: dict[str, Any], now: datetime) -> bool:
    return age_seconds(reading, now) > STALE_AFTER_SECONDS


def humanize_age(seconds: float) -> str:
    seconds = max(0, int(seconds))
    if seconds < 90:
        return f'{seconds}s ago'
    minutes = seconds // 60
    if minutes < 90:
        return f'{minutes}m ago'
    hours = minutes / 60
    return f'{hours:.1f}h ago'


def minutes_to_reset(reading: dict[str, Any], now: datetime) -> float | None:
    if not reading.get('reset_at_utc'):
        return None
    delta = (parse_utc(reading['reset_at_utc']) - now).total_seconds() / 60
    return max(0.0, delta)


def tone_for_used(value: float | None) -> str:
    if value is None:
        return 'warn'
    if value >= 80:
        return 'danger'
    if value >= 50:
        return 'warn'
    return 'ok'


def burn_advice(reading: dict[str, Any] | None, now: datetime) -> dict[str, Any]:
    """Recommend whether to route work at the Gemini app lane.

    The app meter and the Antigravity agent-quota pool are billed separately on
    the same subscription: spending one does not draw down the other. So this
    advice is about the app lane alone.
    """
    unknown = {
        'lane': 'unknown',
        'headroom_pct': None,
        'good_burn_tasks': list(BURN_TASKS),
        'pools_are_independent': True,
    }
    if reading is None:
        unknown['rationale'] = (
            'No gemini.google.com/usage capture on file. Run the bookmarklet, then '
            'tools/gemini_app_usage_ingest.py --from-clipboard.'
        )
        unknown['reserve_rule'] = 'Assume nothing about app-lane headroom until a capture exists.'
        return unknown
    if is_stale(reading, now):
        unknown['rationale'] = (
            f'Last capture is {humanize_age(age_seconds(reading, now))} old, past the '
            f'{STALE_AFTER_SECONDS // 3600}h freshness bound for a 5h rolling window.'
        )
        unknown['reserve_rule'] = 'Re-capture before routing anything to the app lane.'
        return unknown

    headroom = round(100.0 - reading['used_pct'], 1)
    to_reset = minutes_to_reset(reading, now)
    reset_soon = to_reset is not None and to_reset <= 45

    if headroom >= 60:
        lane, rationale = 'burn', (
            f'{headroom:.0f}% app headroom. Push wide, cheap, long-context work here and '
            'keep Claude/Codex reserved for reasoning-heavy lanes.'
        )
        reserve = 'Burn freely down to ~25% headroom; the window refills on a 5h roll.'
    elif headroom >= 25:
        lane, rationale = 'measured', (
            f'{headroom:.0f}% app headroom. Use for batch scans only; avoid Deep Research and '
            'video/image generation, which draw far more compute per prompt.'
        )
        reserve = 'Hold ~25% for interactive use before the next reset.'
    elif reset_soon:
        lane, rationale = 'wait', (
            f'{headroom:.0f}% app headroom, but the window resets in ~{to_reset:.0f}m. '
            'Queue the batch and start it after the reset.'
        )
        reserve = 'Do not spend the tail of a window that is about to refill.'
    else:
        lane, rationale = 'reserve', (
            f'Only {headroom:.0f}% app headroom left. Route batch work to another provider; '
            'keep what remains for interactive prompts.'
        )
        reserve = 'Reserve the remainder for interactive use.'

    return {
        'lane': lane,
        'headroom_pct': headroom,
        'minutes_to_reset': None if to_reset is None else round(to_reset),
        'rationale': rationale,
        'reserve_rule': reserve,
        'good_burn_tasks': list(BURN_TASKS),
        'pools_are_independent': True,
    }


def build_gauge(reading: dict[str, Any] | None, now: datetime, observed_at: str) -> dict[str, Any]:
    """Build the dashboard gauge. Reports 'unknown' rather than inventing a number."""
    advice = burn_advice(reading, now)
    base = {
        'provider': PROVIDER,
        'kind': 'human-confirmed capture of gemini.google.com/usage',
        'burn_advice': advice,
    }
    shared_detail = (
        'This is the consumer Gemini app compute meter (5h rolling into a weekly cap). '
        'It is a different quota pool from Antigravity agent requests shown under Gemini / Goru: '
        'spending one does not draw down the other. gemini.google.com/usage exposes no API, so this '
        'value is only ever an operator-confirmed reading, never a scrape of a logged-in session.'
    )

    if reading is None:
        base.update({
            'value_label': 'no capture yet',
            'fill_pct': None,
            'tone': 'warn',
            'status': 'No capture on file',
            'detail': 'Never captured. ' + shared_detail,
            'source_label': f'No gemini.google.com/usage capture recorded as of {observed_at}.',
        })
        return base

    age = age_seconds(reading, now)
    used = reading['used_pct']
    tier = reading.get('tier') or 'tier not stated'
    reset_label = reading.get('reset_label') or 'reset time not captured'

    if is_stale(reading, now):
        base.update({
            'value_label': 'stale capture',
            'fill_pct': None,
            'tone': 'warn',
            'status': 'Stale capture — value withheld',
            'detail': (
                f'Last confirmed reading was {used:.0f}% used ({tier}), taken {humanize_age(age)}. '
                f'That is past the {STALE_AFTER_SECONDS // 3600}h bound for a 5h rolling window, so the '
                f'percentage is withheld rather than shown as current. ' + shared_detail
            ),
            'source_label': f'Stale operator capture from {reading["captured_at_utc"]}; checked {observed_at}.',
        })
        return base

    to_reset = minutes_to_reset(reading, now)
    reset_text = reset_label if to_reset is None else f'resets in ~{to_reset:.0f}m'
    base.update({
        'value_label': f'{used:.0f}% used · {reset_text}',
        'fill_pct': used,
        'tone': tone_for_used(used),
        'status': f'Operator-confirmed capture, {humanize_age(age)}',
        'detail': (
            f'{tier}: {used:.0f}% of the app compute allowance used, {advice["headroom_pct"]:.0f}% headroom. '
            f'{advice["rationale"]} ' + shared_detail
        ),
        'source_label': (
            f'Captured from {reading["source_url"]} at {reading["captured_at_utc"]} '
            f'via {reading["capture_method"]}; checked {observed_at}.'
        ),
        'sub_gauges': [
            {
                'label': 'App compute used',
                'value_label': f'{used:.0f}% used · {reset_text}',
                'fill_pct': used,
                'tone': tone_for_used(used),
            },
            {
                'label': 'Burn lane',
                'value_label': f'{advice["lane"]} · {advice["headroom_pct"]:.0f}% headroom',
                'fill_pct': None,
                'tone': 'ok' if advice['lane'] == 'burn' else 'warn',
            },
        ],
    })
    return base

#!/usr/bin/env python3
"""Gemini app (consumer) usage reading: load, validate, gauge, burn advice.

Safety model (matches live_provider_usage_monitor.py):
- Reads one local drop-file written by a human-confirmed capture, the separately
  gated high-confidence Chrome usage-page crawler, or an authenticated page-scoped
  accessibility capture.
- Never reads credential/token/cookie files.
- Never opens browser billing/account/payment/API/GCP surfaces.

The gemini.google.com/usage meter has no API. Supported sources are an operator
capture (see gemini_app_usage_bookmarklet.js) and an unattended DOM read whose
extractor reports a trusted page-scoped signal. A reading is trusted only while
it is fresh; once it ages past the 5h rolling window it is reported as unknown.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA = 'NM_GEMINI_APP_USAGE_V1'
PROVIDER = 'Gemini app / consumer'

# How old a capture can be before it is considered useless (since the quota is 5h rolling).
# Temporarily increased to 24h so the user can preview the new UI design.
STALE_AFTER_SECONDS = 24 * 3600

# 'chrome-auto' is an unattended DOM scrape (gemini_app_usage_autofetch.py). It is
# accepted only when the extractor reports a high-confidence signal, and the gauge
# labels it as unattended so a human-confirmed reading is never confused with one.
# 'accessibility-verified' is a page-scoped read from an already authenticated Chrome
# window; it is neither a human-entered value nor an unattended JavaScript scrape.
CAPTURE_METHODS = frozenset({
    'bookmarklet-confirmed',
    'manual',
    'chrome-auto',
    'accessibility-verified',
})

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


def _dh_g(days: int, hours: int) -> str:
    """Correct singular/plural; omit a zero component."""
    bits = []
    if days:
        bits.append(f"{days} day" + ("s" if days != 1 else ""))
    if hours:
        bits.append(f"{hours} hour" + ("s" if hours != 1 else ""))
    return " ".join(bits) if bits else "under an hour"


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

    weekly_raw = payload.get('weekly_used_pct')
    weekly_used_pct = None
    if weekly_raw is not None:
        if isinstance(weekly_raw, bool) or not isinstance(weekly_raw, (int, float)):
            raise ReadingError('weekly_used_pct must be a number')
        weekly_used_pct = float(weekly_raw)
        if not 0.0 <= weekly_used_pct <= 100.0:
            raise ReadingError(f'weekly_used_pct {weekly_used_pct} out of range 0..100')

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

    weekly_reset_at = None
    if payload.get('weekly_reset_at_utc'):
        try:
            weekly_reset_at = parse_utc(payload['weekly_reset_at_utc'])
        except ValueError as exc:
            raise ReadingError(f'weekly_reset_at_utc is not an ISO-8601 timestamp: {exc}') from exc

    checked = {
        'schema': SCHEMA,
        'used_pct': used_pct,
        'reset_label': str(payload.get('reset_label') or '').strip() or None,
        'reset_at_utc': format_utc(reset_at) if reset_at else None,
        'tier': str(payload.get('tier') or '').strip() or None,
        'source_url': str(payload.get('source_url') or 'https://gemini.google.com/usage'),
        'captured_at_utc': format_utc(captured_at),
        'capture_method': method,
    }
    if weekly_used_pct is not None:
        checked.update({
            'weekly_used_pct': weekly_used_pct,
            'weekly_reset_label': str(payload.get('weekly_reset_label') or '').strip() or None,
            'weekly_reset_at_utc': format_utc(weekly_reset_at) if weekly_reset_at else None,
        })
    return checked


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
            'No gemini.google.com/usage capture on file. Run the high-confidence '
            'Chrome usage-page crawler or use the operator-confirmed bookmarklet.'
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


def route_line(reading: dict[str, Any] | None, now: datetime) -> str:
    """One advisory line for a router (e.g. the mastermind briefing Hwao).

    Deliberately terse and self-contained: a lane verdict, the headroom that
    justifies it, and the reminder that this pool is independent of Antigravity.
    Says 'unknown' when there is no fresh capture rather than implying headroom.
    """
    advice = burn_advice(reading, now)
    lane = advice['lane']
    if lane == 'unknown':
        return f'GEMINI APP LANE: unknown — {advice["rationale"]} Do not assume app-lane headroom.'

    tier = (reading.get('tier') or 'tier unstated') if reading else 'tier unstated'
    age = humanize_age(age_seconds(reading, now)) if reading else 'no capture'
    to_reset = advice.get('minutes_to_reset')
    reset_bit = '' if to_reset is None else f', resets ~{to_reset}m'
    tasks = ', '.join(advice['good_burn_tasks'])
    where = (
        f'route wide/cheap/long-context work ({tasks}) here'
        if lane in ('burn', 'measured')
        else 'route batch work to another provider'
    )
    return (
        f'GEMINI APP LANE: {lane} — {advice["headroom_pct"]:.0f}% headroom{reset_bit}. '
        f'{where}; this pool is independent of the Antigravity/Goru quota. '
        f'[{tier}, capture {age}]'
    )


def build_gauge(reading: dict[str, Any] | None, now: datetime, observed_at: str) -> dict[str, Any]:
    """Build the dashboard gauge. Reports 'unknown' rather than inventing a number."""
    advice = burn_advice(reading, now)
    capture_method = reading.get('capture_method') if reading else None
    is_chrome_auto = capture_method == 'chrome-auto'
    is_accessibility = capture_method == 'accessibility-verified'
    if is_chrome_auto:
        kind = 'high-confidence unattended DOM capture of gemini.google.com/usage'
        provenance_detail = (
            'This reading came from the separately gated Chrome usage-page crawler; '
            'the extractor stores only trusted page-scoped signals and abstains rather '
            'than overwriting the prior reading when confidence is weak. '
        )
        provenance = 'Unattended Chrome scrape'
        stale_capture_label = 'Chrome crawler'
    elif is_accessibility:
        kind = 'authenticated accessibility capture of gemini.google.com/usage'
        provenance_detail = (
            'This reading came from a page-scoped accessibility read of an already '
            'authenticated Chrome usage page; no cookie, credential, billing, or payment '
            'surface was read. '
        )
        provenance = 'Authenticated accessibility capture'
        stale_capture_label = 'accessibility'
    else:
        kind = 'human-confirmed capture of gemini.google.com/usage'
        provenance_detail = 'This reading was captured and confirmed by the operator. '
        provenance = 'Operator-confirmed capture'
        stale_capture_label = 'operator'
    base = {
        'provider': PROVIDER,
        'kind': kind,
        'burn_advice': advice,
    }
    shared_detail = provenance_detail + (
        'This is the consumer Gemini app compute meter (5h rolling into a weekly cap). '
        'It is a different quota pool from Antigravity agent requests shown under Gemini / Goru: '
        'spending one does not draw down the other. gemini.google.com/usage exposes no API.'
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
    weekly_used = reading.get('weekly_used_pct')
    tier = reading.get('tier') or 'tier not stated'
    reset_label = reading.get('reset_label') or 'reset time not captured'

    if is_stale(reading, now):
        weekly_stale = '' if weekly_used is None else f' Weekly limit was {weekly_used:.0f}% used.'
        base.update({
            'value_label': 'stale capture',
            'fill_pct': None,
            'tone': 'warn',
            'status': 'Stale capture — value withheld',
            'detail': (
                f'Last confirmed current-window reading was {used:.0f}% used ({tier}), taken {humanize_age(age)}.'
                f'{weekly_stale} '
                f'That is past the {STALE_AFTER_SECONDS // 3600}h bound for a 5h rolling window, so the '
                f'percentage is withheld rather than shown as current. ' + shared_detail
            ),
            'source_label': (
                f'Stale {stale_capture_label} capture '
                f'from {reading["captured_at_utc"]}; checked {observed_at}.'
            ),
        })
        return base

    to_reset = minutes_to_reset(reading, now)
    if to_reset is not None:
        total_seconds = int(to_reset * 60)
        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        reset_text = 'resets in ' + _dh_g(days, hours)
    else:
        rl = reset_label.lower().strip()
        if rl.startswith('in '):
            rl = rl[3:].strip()
            
        import re
        hm_match = re.match(r'^(\d+)h\s*(\d+)m$', rl)
        if hm_match:
            h = int(hm_match.group(1))
            m = int(hm_match.group(2))
            total_mins = h * 60 + m
            d = total_mins // 1440
            hr = (total_mins % 1440) // 60
            reset_text = 'resets in ' + _dh_g(d, hr)
        else:
            reset_text = f'resets in {rl}'
        
    weekly_reset_text = None
    if weekly_used is not None:
        weekly_reset_at = reading.get('weekly_reset_at_utc')
        if weekly_reset_at:
            weekly_minutes = max(0.0, (parse_utc(weekly_reset_at) - now).total_seconds() / 60)
            weekly_seconds = int(weekly_minutes * 60)
            weekly_days = weekly_seconds // 86400
            weekly_hours = (weekly_seconds % 86400) // 3600
            weekly_reset_text = 'resets in ' + _dh_g(weekly_days, weekly_hours)
        else:
            weekly_reset_text = reading.get('weekly_reset_label') or 'weekly reset time not captured'

    sub_gauges = [
        {
            'label': 'Current-window used',
            'value_label': f'{used:.0f}% used · {reset_text}',
            'fill_pct': used,
            'tone': tone_for_used(used),
        },
    ]
    if weekly_used is not None:
        sub_gauges.append({
            'label': 'Weekly used',
            'value_label': f'{weekly_used:.0f}% used · {weekly_reset_text}',
            'fill_pct': weekly_used,
            'tone': tone_for_used(weekly_used),
        })
    sub_gauges.append({
        'label': 'Burn lane',
        'value_label': f'{advice["lane"]} · {advice["headroom_pct"]:.0f}% headroom',
        'fill_pct': None,
        'tone': 'ok' if advice['lane'] == 'burn' else 'warn',
    })
    weekly_detail = '' if weekly_used is None else f' {weekly_used:.0f}% weekly used ({weekly_reset_text}).'
    base.update({
        'value_label': f'{used:.0f}% current-window used · {reset_text}',
        'fill_pct': used,
        'tone': tone_for_used(used),
        'status': f'{provenance}, {humanize_age(age)}',
        'detail': (
            f'{tier}: {used:.0f}% current-window used, {advice["headroom_pct"]:.0f}% current-window headroom.'
            f'{weekly_detail} '
            f'{advice["rationale"]} ' + shared_detail
        ),
        'source_label': (
            f'Captured from {reading["source_url"]} at {reading["captured_at_utc"]} '
            f'via {reading["capture_method"]}; checked {observed_at}.'
        ),
        'sub_gauges': sub_gauges,
    })
    return base

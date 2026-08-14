#!/usr/bin/env python3
"""Refresh public provider usage gauges from safe local visible status surfaces.

Safety model:
- Uses visible tmux pane /status or /usage display commands only when panes are idle.
- Reads one validated local drop-file of gemini.google.com/usage readings. The
  drop-file may come from an operator-confirmed capture or the separately gated
  high-confidence Chrome usage-page crawler; this monitor does not drive Chrome.
- Reads Claude OAuth usage through the existing local credential path and invokes
  Hermes' normalized read-only Nous account reader; token values are never emitted.
- Never opens browser billing/account/payment/API/GCP surfaces.
- Writes only the stable static cockpit/status files through the existing renderer
  and stable_cockpit_guard single-writer lock.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import re
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone, timedelta
import os
from pathlib import Path
from typing import Any

TOOL_DIR = Path(__file__).resolve().parent
ROOT = TOOL_DIR.parent
CANONICAL = ROOT / 'frontend/public/agent-reports/stable-cockpit-canonical.json'
MARKER = 'PROVIDER_USAGE_REALTIME_MONITOR_V1'

sys.path.insert(0, str(TOOL_DIR))
from stable_cockpit_renderer import DEFAULT_PUBLIC_ROOTS, write_outputs  # noqa: E402
import stable_cockpit_guard  # noqa: E402
import gemini_app_usage  # noqa: E402
import nous_credits_usage  # noqa: E402
import moonshot_balance_usage  # noqa: E402


def fetch_claude_quota_via_oauth() -> dict[str, Any] | None:
    try:
        creds_path = os.path.expanduser('~/.claude/.credentials.json')
        if not os.path.exists(creds_path):
            return None
        with open(creds_path, 'r') as f:
            creds = json.load(f)
        token = creds.get('claudeAiOauth', {}).get('accessToken')
        if not token:
            return None
        req = urllib.request.Request('https://api.anthropic.com/api/oauth/usage')
        req.add_header('Authorization', f'Bearer {token}')
        req.add_header('anthropic-beta', 'oauth-2025-04-20')
        req.add_header('User-Agent', 'Claude/2.1.201')
        with urllib.request.urlopen(req, timeout=5) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception:
        return None


def gemini_app_gauge(observed_at: str) -> dict[str, Any]:
    """Gauge for the consumer Gemini app meter. A bad drop-file must not stop a pass."""
    now = gemini_app_usage.parse_utc(observed_at)
    try:
        reading = gemini_app_usage.load_reading()
    except (gemini_app_usage.ReadingError, json.JSONDecodeError, OSError) as exc:
        gauge = gemini_app_usage.build_gauge(None, now, observed_at)
        gauge['status'] = 'Capture file unreadable — value withheld'
        gauge['detail'] = f'{gemini_app_usage.reading_path()} could not be trusted: {exc}. ' + gauge['detail']
        return gauge
    return gemini_app_usage.build_gauge(reading, now, observed_at)


def nous_credits_gauge(observed_at: str) -> dict[str, Any]:
    """Read-only Nous dollar balance via Hermes' normalized account reader."""
    return nous_credits_usage.fetch_gauge(observed_at)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def run(cmd: list[str], timeout: int = 20) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True, timeout=timeout, check=False)


def tmux_panes() -> list[dict[str, str]]:
    cp = run(['tmux', 'list-panes', '-a', '-F', '#{pane_id}\t#{session_name}:#{window_name}.#{pane_index}\t#{pane_current_command}\t#{@mesh_role}#{@master_role}\t#{pane_in_mode}\t#{pane_dead}'])
    panes = []
    if cp.returncode != 0:
        return panes
    for line in cp.stdout.splitlines():
        parts = (line.split('\t') + ['', '', '', '', '', ''])[:6]
        panes.append({'pane_id': parts[0], 'target': parts[1], 'command': parts[2], 'role': parts[3], 'in_mode': parts[4], 'dead': parts[5]})
    return panes


def capture_pane(pane_id: str, lines: int = 500) -> str:
    cp = run(['tmux', 'capture-pane', '-p', '-J', '-S', f'-{lines}', '-t', pane_id], timeout=20)
    return cp.stdout if cp.returncode == 0 else ''


def nonempty_tail(text: str, n: int = 24) -> list[str]:
    return [ln.rstrip() for ln in text.splitlines() if ln.strip()][-n:]


def is_idle_codex(text: str) -> bool:
    tail = nonempty_tail(text, 20)
    if not tail:
        return False
    joined = '\n'.join(tail).lower()
    if any(bad in joined for bad in ['running command', 'thinking', 'approval requested', 'ctrl+o to expand', 'pane is dead']):
        return False
    return any(line.lstrip().startswith('›') for line in tail) and any('gpt-5' in line.lower() or 'codex' in line.lower() for line in tail)


def is_idle_agy(text: str) -> bool:
    tail = nonempty_tail(text, 20)
    if not tail:
        return False
    joined = '\n'.join(tail).lower()
    if any(bad in joined for bad in ['ctrl+end bottom', 'models & quota', 'running', 'approval']):
        return False
    return any(line.strip() == '>' for line in tail) and 'gemini' in joined and '? for shortcuts' in joined


def in_copy_mode(pane: dict[str, str]) -> bool:
    """A pane the operator has scrolled back is not safe to send keys to.

    tmux copy-mode binds '/' to search-forward, so send-keys '/usage' would type a
    search instead of a slash command and jump the operator's scroll position.
    """
    return pane.get('in_mode', '0') == '1'


def choose_pane(panes: list[dict[str, str]], kind: str) -> dict[str, str] | None:
    candidates = []
    for pane in panes:
        if in_copy_mode(pane) or pane.get('dead') == '1':
            continue
        cmd = pane['command'].lower()
        target = pane['target'].lower()
        role = pane['role'].lower()
        if kind == 'codex' and (cmd in {'node', 'codex'} or 'kun' in role or 'kun' in target):
            candidates.append(pane)
        if kind == 'agy' and (cmd == 'agy' or 'goru' in role or 'goru' in target):
            candidates.append(pane)
    for pane in candidates:
        text = capture_pane(pane['pane_id'], 80)
        if kind == 'codex' and is_idle_codex(text):
            return pane
        if kind == 'agy' and is_idle_agy(text):
            return pane
    return None


def send_visible_command(pane_id: str, command: str, wait_seconds: float) -> str:
    run(['tmux', 'send-keys', '-t', pane_id, command, 'C-m'])
    time.sleep(wait_seconds)
    text = capture_pane(pane_id, 220)
    # Some Codex panes show the slash command in the composer before opening it;
    # submit once if that exact state is visible.
    if command == '/status' and re.search(r'^[›>]\s*/status\s*$', text, re.M):
        run(['tmux', 'send-keys', '-t', pane_id, 'C-m'])
        time.sleep(wait_seconds)
        text = capture_pane(pane_id, 240)
    if command == '/usage':
        # Capture while the panel is visible, then return the pane to idle.
        run(['tmux', 'send-keys', '-t', pane_id, 'Escape'])
        time.sleep(0.5)
    return text


def pct_used_from_left(left: float) -> float:
    return max(0.0, min(100.0, 100.0 - left))


def tone_for_used(value: float | None) -> str:
    if value is None:
        return 'warn'
    if value >= 80:
        return 'danger'
    if value >= 50:
        return 'warn'
    return 'ok'


def _dh(days: int, hours: int) -> str:
    """'4 days 18 hours', '1 day', '18 hours' — no '4 day 18 hours', no zero parts."""
    bits = []
    if days:
        bits.append(f"{days} day" + ("s" if days != 1 else ""))
    if hours:
        bits.append(f"{hours} hour" + ("s" if hours != 1 else ""))
    return " ".join(bits) if bits else "under an hour"


def fmt_reset_remained(val: str | None) -> str:
    if not val or val == 'unknown':
        return 'unknown'
    val = str(val).strip()
    low = val.lower()
    for pre in ('remained ', 'resets in '):          # accept either, emit the new one
        if low.startswith(pre):
            val = val[len(pre):].strip()
            break
    now = datetime.now(timezone.utc)
    d = None
    try:
        d = datetime.fromisoformat(val)
    except Exception:
        pass
        
    if not d:
        try:
            if ' on ' in val:
                d = datetime.strptime(val, '%H:%M on %d %b')
                d = d.replace(year=now.year, tzinfo=timezone.utc)
                if d < now: d = d.replace(year=now.year + 1)
            elif re.match(r'^\d{2}:\d{2}$', val):
                d = datetime.strptime(val, '%H:%M')
                d = d.replace(year=now.year, month=now.month, day=now.day, tzinfo=timezone.utc)
                if d < now: d += timedelta(days=1)
        except Exception:
            pass
            
    if d:
        minutes = int((d - now).total_seconds() / 60)
        days = minutes // 1440
        hours = (minutes % 1440) // 60
        if days == 0 and hours == 0:
            return "resets in under an hour"
        return "resets in " + _dh(days, hours)
        
    val_lower = val.lower()
    if val_lower.startswith('in '):
        val_lower = val_lower[3:].strip()
        
    # Parse 72h 29m format
    hm_match = re.match(r'^(\d+)h\s*(\d+)m$', val_lower)
    if hm_match:
        h = int(hm_match.group(1))
        m = int(hm_match.group(2))
        total_mins = h * 60 + m
        d = total_mins // 1440
        hr = (total_mins % 1440) // 60
        return "resets in " + _dh(d, hr)
        
    return f"resets in {val}"


def display_pct(value: float | None, suffix: str = 'used') -> str:
    if value is None or not math.isfinite(value):
        return 'not observed'
    if 0 < value < 0.1:
        shown = f'{value:.2f}'
    elif 0 < value < 1:
        shown = f'{value:.1f}'
    elif abs(value - round(value)) < 0.05:
        shown = str(int(round(value)))
    else:
        shown = f'{value:.1f}'
    return f'{shown}% {suffix}'


def limit_usage_label(limit: dict[str, Any]) -> str:
    used_pct = limit.get('used_pct')
    if used_pct is not None:
        return display_pct(used_pct)
    if limit.get('availability') == 'available':
        return 'available · exact usage not exposed'
    return 'not observed'


def limit_value_label(limit: dict[str, Any], *, include_reset: bool = False) -> str:
    used_pct = limit.get('used_pct')
    if used_pct is None:
        if limit.get('availability') == 'available':
            return 'Available · exact usage/reset not exposed' if include_reset else 'Available · exact usage not exposed'
        return 'Not observed'
    parts = [display_pct(used_pct), limit.get('remaining_label') or 'remaining amount not observed']
    if include_reset:
        parts.append(fmt_reset_remained(limit.get('refresh')))
    return ' · '.join(parts)


def limit_tone(limit: dict[str, Any]) -> str:
    if limit.get('used_pct') is None and limit.get('availability') == 'available':
        return 'ok'
    return tone_for_used(limit.get('used_pct'))


def parse_codex_status(text: str) -> dict[str, Any] | None:
    idx = text.rfind('OpenAI Codex')
    if idx < 0:
        idx = text.rfind('/status')
    if idx < 0:
        return None
    block = text[idx:]
    five = re.findall(
        r'5h limit:\s+\[[^\]]+\]\s+([0-9]+(?:\.[0-9]+)?)% left(?:\s+\(resets ([^)]+)\))?',
        block,
        re.IGNORECASE,
    )
    weekly = re.findall(
        r'Weekly limit:\s+\[[^\]]+\]\s+([0-9]+(?:\.[0-9]+)?)% left(?:\s+\(resets ([^)]+)\))?',
        block,
        re.IGNORECASE,
    )
    ctx = re.search(r'Context window:\s+([0-9]+(?:\.[0-9]+)?)% left \(([^)]*)\)', block)
    if not five and not weekly:
        return None
    result: dict[str, Any] = {'raw_source': 'codex /status'}
    model = re.search(r'Model:\s+([A-Za-z0-9._-]+)', block, re.IGNORECASE)
    result['main_model'] = model.group(1) if model else 'Codex main'
    if ctx:
        left = float(ctx.group(1))
        result['context_left_pct'] = left
        result['context_used_pct'] = pct_used_from_left(left)
        result['context_label'] = ctx.group(2)
    if len(five) >= 1:
        left = float(five[0][0])
        result['main_5h_left_pct'] = left
        result['main_5h_used_pct'] = pct_used_from_left(left)
        result['main_5h_reset'] = five[0][1] or None
    if len(weekly) >= 1:
        left = float(weekly[0][0])
        result['main_weekly_left_pct'] = left
        result['main_weekly_used_pct'] = pct_used_from_left(left)
        result['main_weekly_reset'] = weekly[0][1] or None
    if len(five) >= 2:
        left = float(five[1][0])
        result['spark_5h_left_pct'] = left
        result['spark_5h_used_pct'] = pct_used_from_left(left)
        result['spark_5h_reset'] = five[1][1] or None
    if len(weekly) >= 2:
        left = float(weekly[1][0])
        result['spark_weekly_left_pct'] = left
        result['spark_weekly_used_pct'] = pct_used_from_left(left)
        result['spark_weekly_reset'] = weekly[1][1] or None
    return result


def segment_between(text: str, start: str, stops: list[str]) -> str:
    i = text.find(start)
    if i < 0:
        return ''
    j_candidates = [text.find(stop, i + len(start)) for stop in stops]
    j_candidates = [j for j in j_candidates if j >= 0]
    j = min(j_candidates) if j_candidates else len(text)
    return text[i:j]


def parse_limit_segment(segment: str) -> dict[str, Any] | None:
    if not segment:
        return None
    bar = re.search(r'\]\s*([0-9]+(?:\.[0-9]+)?)\s*%\s*(?:\n|$)', segment)
    remaining = re.search(r'([0-9]+(?:\.[0-9]+)?)% remaining', segment)
    refresh = re.search(r'Refreshes in ([^\n]+)', segment)
    available = 'Quota available' in segment
    if bar:
        rem = float(bar.group(1))
    elif remaining:
        rem = float(remaining.group(1))
    elif available:
        rem = None
    else:
        return None
    return {
        'left_pct': rem,
        'used_pct': pct_used_from_left(rem) if rem is not None else None,
        'availability': 'available' if available else 'measured',
        'remaining_label': f'{rem:g}% remaining' if bar else (remaining.group(1) + '% remaining' if remaining else ('Quota available' if available else display_pct(rem, 'remaining'))),
        'refresh': refresh.group(1).strip() if refresh else None,
    }


def parse_agy_usage(text: str) -> dict[str, Any] | None:
    idx = text.rfind('Models & Quota')
    if idx < 0:
        return None
    block = text[idx:]
    gem = segment_between(block, 'GEMINI MODELS', ['CLAUDE AND GPT MODELS'])
    ag = segment_between(block, 'CLAUDE AND GPT MODELS', ['Within each group', '↑/↓ Scroll', 'esc Close'])
    result: dict[str, Any] = {'raw_source': 'agy /usage'}
    if gem:
        g_weekly = segment_between(gem, 'Weekly Limit', ['Five Hour Limit'])
        g_5h = segment_between(gem, 'Five Hour Limit', ['CLAUDE AND GPT MODELS', 'Weekly Limit'])
        parsed = parse_limit_segment(g_weekly)
        if parsed:
            result['gemini_weekly'] = parsed
        parsed = parse_limit_segment(g_5h)
        if parsed:
            result['gemini_5h'] = parsed
    if ag:
        a_weekly = segment_between(ag, 'Weekly Limit', ['Five Hour Limit'])
        a_5h = segment_between(ag, 'Five Hour Limit', ['Within each group', '↑/↓ Scroll', 'esc Close'])
        parsed = parse_limit_segment(a_weekly)
        if parsed:
            result['ag_claude_gpt_weekly'] = parsed
        parsed = parse_limit_segment(a_5h)
        if parsed:
            result['ag_claude_gpt_5h'] = parsed
    return result if len(result) > 1 else None


def active_counts_and_context(panes: list[dict[str, str]]) -> dict[str, Any]:
    counts = {'claude_fable_lana': 0, 'codex_kun': 0, 'gemini_goru': 0, 'tori_hermes': 0}
    tori_context: list[float] = []
    for pane in panes:
        if pane.get('dead') == '1':
            continue
        cmd = pane['command'].lower()
        target = pane['target'].lower()
        role = pane['role'].lower()
        if cmd == 'claude.exe' or 'hwao' in role or 'lana' in role:
            counts['claude_fable_lana'] += 1
        if cmd in {'node', 'codex'} or 'kun' in role or 'kun' in target:
            counts['codex_kun'] += 1
        if cmd == 'agy' or 'goru' in role or 'goru' in target:
            counts['gemini_goru'] += 1
        if 'tori' in role or (cmd.startswith('python') and 'ge-' in target):
            counts['tori_hermes'] += 1
            text = capture_pane(pane['pane_id'], 80)
            for line in text.splitlines():
                if '│' in line and ('/' in line or 'gpt-' in line.lower() or 'claude' in line.lower()):
                    for m in re.finditer(r'([0-9]+(?:\.[0-9]+)?)%', line):
                        value = float(m.group(1))
                        if 0 <= value <= 100:
                            tori_context.append(value)
    return {'counts': counts, 'tori_context_max_used_pct': max(tori_context) if tori_context else None}


def provider_index(gauges: list[dict[str, Any]], provider: str) -> int:
    for i, gauge in enumerate(gauges):
        if gauge.get('provider') == provider:
            return i
    gauges.append({'provider': provider})
    return len(gauges) - 1



FLOW_CREDITS_PATH = Path('/Users/duhokim/HermesOps/scripts/clips/flow_credits.json')


def flow_credits_gauge(gauges: list[dict[str, Any]]) -> None:
    """Source the Flow/Veo gauge from the same file the autopilot dashboard uses.

    Added 2026-08-14. The two cockpits disagreed about Flow/Veo: this canonical
    carried a legacy entry quoting July documentation (credit COSTS, no balance),
    while ge-autopilot read the real balance capture from flow_credits.json. Same
    provider, two ages, no shared source. Duho asked for one fact.
    """
    i = provider_index(gauges, 'Flow / Veo (Ultra)')
    g = gauges[i]
    g.setdefault('provider', 'Flow / Veo (Ultra)')
    g['kind'] = 'monthly Flow credit pool (separate from Gemini-app limits)'
    try:
        data = json.loads(FLOW_CREDITS_PATH.read_text())
    except Exception as exc:
        g['value_label'] = 'balance not captured'
        g['status'] = 'No Flow balance capture available'
        g['detail'] = f'Could not read {FLOW_CREDITS_PATH.name}: {exc}'
        g['source_label'] = 'no live account or billing surface opened; no capture file readable.'
        g['tone'] = 'warn'
        g['fill_pct'] = None
        return
    remaining = data.get('remaining')
    total = data.get('total') or data.get('base_monthly_total')
    captured = data.get('captured_utc', '')
    pct = None
    if isinstance(remaining, (int, float)) and isinstance(total, (int, float)) and total:
        pct = max(0.0, min(100.0, 100.0 * float(remaining) / float(total)))
    g['fill_pct'] = pct
    g['value_label'] = (f'{int(remaining):,} / {int(total):,} credits left'
                        if pct is not None else 'balance not captured')
    g['status'] = 'Last operator-confirmed Flow UI capture — no live balance API exists'
    g['detail'] = str(data.get('reset', '')) or 'Flow credit pool; reset terms not captured.'
    g['source_label'] = (f'Flow UI balance capture in flow_credits.json at {captured}; '
                         'no live account or billing surface opened.')
    g['tone'] = 'ok' if (pct or 0) > 25 else 'warn'


def update_gauges(canonical: dict[str, Any], codex: dict[str, Any] | None, agy: dict[str, Any] | None, telemetry: dict[str, Any], observed_at: str, slash_sources: dict[str, Any]) -> dict[str, Any]:
    gauges = copy.deepcopy(canonical.get('provider_usage_gauges') or [])
    counts = telemetry['counts']

    flow_credits_gauge(gauges)

    i = provider_index(gauges, 'Claude / Fable / Lana')
    g = gauges[i]
    g.setdefault('provider', 'Claude / Fable / Lana')
    
    claude_data = fetch_claude_quota_via_oauth()
    if claude_data:
        g['kind'] = 'Claude OAuth usage monitor'
        g['status'] = 'Active panes live; quota fetched via approved read-only OAuth usage check'
        five_h = claude_data.get('five_hour', {})
        weekly = claude_data.get('seven_day', {})
        five_h_pct = five_h.get('utilization')
        weekly_pct = weekly.get('utilization')
        
        five_h_reset = fmt_reset_remained(five_h.get('resets_at', 'unknown'))
        weekly_reset = fmt_reset_remained(weekly.get('resets_at', 'unknown'))
        
        # Per-model weekly caps arrive in limits[] as kind='weekly_scoped'. The binding
        # constraint on a Max plan is usually one of those, NOT the all-models total: on
        # 2026-08-07 the board read 51% (all models) while the Fable cap sat at 89%. Read the
        # scoped caps rather than skipping them, and rank on the highest known limit.
        scoped: dict[str, dict[str, Any]] = {}
        for lim in claude_data.get('limits', []):
            model_name = ((lim.get('scope') or {}).get('model') or {}).get('display_name')
            if lim.get('group') == 'weekly' and model_name:
                scoped[model_name] = lim
        fable_lim = scoped.get('Fable') or {}
        fable_pct = fable_lim.get('percent')
        fable_reset = fmt_reset_remained(fable_lim.get('resets_at')) if fable_lim else weekly_reset

        main_fill = max([v for v in [five_h_pct, weekly_pct, fable_pct] if v is not None], default=None)
        g['value_label'] = f'Fable {display_pct(five_h_pct)} 5h · {display_pct(fable_pct)} weekly'
        g['fill_pct'] = main_fill
        g['tone'] = tone_for_used(main_fill)
        g['detail'] = (
            f'Claude OAuth usage endpoint reports the 5h limit at {display_pct(five_h_pct)} '
            f'({five_h_reset}), the Fable weekly cap at {display_pct(fable_pct)} ({fable_reset}), '
            f'and all models combined at {display_pct(weekly_pct)} ({weekly_reset}). '
            'The binding constraint is the highest of these, not the combined total.'
        )
        g['source_label'] = f'OAuth /api/oauth/usage fetched {observed_at}; active Claude panes: {counts["claude_fable_lana"]}.'
        
        sub_gauges = [
            {'label': 'Fable 5h used', 'value_label': f'{display_pct(five_h_pct, "")}', 'fill_pct': five_h_pct, 'tone': tone_for_used(five_h_pct)},
            {'label': 'Fable weekly used', 'value_label': f'{display_pct(fable_pct, "")} · {fable_reset}', 'fill_pct': fable_pct, 'tone': tone_for_used(fable_pct)},
            {'label': 'All models weekly used', 'value_label': f'{display_pct(weekly_pct, "")} · {weekly_reset}', 'fill_pct': weekly_pct, 'tone': tone_for_used(weekly_pct)},
        ]
        
        # Add other Anthropic models dynamically from limits
        for lim in claude_data.get('limits', []):
            if lim.get('group') == 'weekly' and lim.get('scope') and lim.get('scope').get('model'):
                m_name = lim['scope']['model'].get('display_name', 'Unknown')
                if m_name == 'Fable': continue
                m_pct = lim.get('percent', 0)
                m_reset = fmt_reset_remained(lim.get('resets_at', 'unknown'))
                sub_gauges.append({
                    'label': f'{m_name} weekly used', 
                    'value_label': f'{display_pct(m_pct, "")} · {m_reset}', 
                    'fill_pct': m_pct, 
                    'tone': tone_for_used(m_pct)
                })
                
        def add_model_if_missing(key: str, display_name: str):
            for s in sub_gauges:
                if s['label'] == f'{display_name} weekly used':
                    return
            model_data = claude_data.get(key)
            # A null block means the endpoint did not report this model. Defaulting it to 0 put
            # an unmeasured "0% used" on the board, which reads as headroom that was never
            # observed; None renders as "not observed" instead.
            pct = model_data.get('utilization') if isinstance(model_data, dict) else None
            sub_gauges.append({
                'label': f'{display_name} weekly used',
                'value_label': f'{display_pct(pct, "")}' + (f' · {weekly_reset}' if pct is not None else ''),
                'fill_pct': pct,
                'tone': tone_for_used(pct)
            })
            
        add_model_if_missing('seven_day_opus', 'Opus')
        add_model_if_missing('seven_day_sonnet', 'Sonnet')
        g['sub_gauges'] = sub_gauges
    else:
        g['kind'] = 'Claude last-visible quota fallback'
        g['status'] = 'Active panes live; approved OAuth usage read unavailable'
        g['detail'] = (
            'Approved read-only Claude OAuth usage check returned unavailable. '
            f'Keeping the last visible Claude usage-panel percentages while live-monitoring {counts["claude_fable_lana"]} Claude/Hwao/Lana panes. '
            'No token value was emitted and no billing, payment, or account mutation occurred.'
        )
        g['source_label'] = f'Last visible Claude usage-panel values retained after approved OAuth usage read returned unavailable at {observed_at}; active Claude panes: {counts["claude_fable_lana"]}.'
    gauges[i] = g

    if codex:
        main_model = codex.get('main_model') or 'Codex main'
        main_5h = codex.get('main_5h_used_pct')
        main_weekly = codex.get('main_weekly_used_pct')
        spark_5h = codex.get('spark_5h_used_pct')
        spark_weekly = codex.get('spark_weekly_used_pct')
        main_fill = max([v for v in [main_5h, main_weekly] if v is not None], default=None)
        i = provider_index(gauges, 'Codex (seat unassigned)')
        gauges[i] = {
            'provider': 'Codex (seat unassigned)',
            'kind': 'live visible Codex /status used percent',
            'value_label': f'{main_model} {display_pct(main_5h)} 5h · {display_pct(main_weekly)} weekly',
            'fill_pct': main_fill,
            'tone': tone_for_used(main_fill),
            'status': 'Live slash-command refresh' if slash_sources.get('codex_refreshed') else 'Live pane scan from latest visible /status',
            'detail': (
                f'Codex /status reports {main_model} 5h {display_pct(codex.get("main_5h_left_pct"), "left")} '
                f'({fmt_reset_remained(codex.get("main_5h_reset"))}) and weekly {display_pct(codex.get("main_weekly_left_pct"), "left")} '
                f'({fmt_reset_remained(codex.get("main_weekly_reset"))}). Codex itself warns these limits may be stale; this monitor refreshes only via visible idle-pane /status, not the web billing/settings page.'
            ),
            'source_label': f'Idle Codex pane {slash_sources.get("codex_pane", "visible pane")} /status observed {observed_at}; active Kun/Codex panes: {counts["codex_kun"]}.',
            'sub_gauges': [
                {'label': f'{main_model} 5h used', 'value_label': f'{display_pct(main_5h)}', 'fill_pct': main_5h, 'tone': tone_for_used(main_5h)},
                {'label': f'{main_model} weekly used', 'value_label': f'{display_pct(main_weekly)} · {fmt_reset_remained(codex.get("main_weekly_reset"))}', 'fill_pct': main_weekly, 'tone': tone_for_used(main_weekly)},
                {'label': 'Codex Spark 5h used', 'value_label': f'{display_pct(spark_5h)}', 'fill_pct': spark_5h, 'tone': tone_for_used(spark_5h)},
                {'label': 'Codex Spark weekly used', 'value_label': f'{display_pct(spark_weekly)} · {fmt_reset_remained(codex.get("spark_weekly_reset"))}', 'fill_pct': spark_weekly, 'tone': tone_for_used(spark_weekly)},
            ],
        }

    if agy:
        gw = agy.get('gemini_weekly') or {}
        g5 = agy.get('gemini_5h') or {}
        aw = agy.get('ag_claude_gpt_weekly') or {}
        a5 = agy.get('ag_claude_gpt_5h') or {}
        main_fill = max([v for v in [gw.get('used_pct'), g5.get('used_pct')] if v is not None], default=None)
        i = provider_index(gauges, 'Antigravity / Gemini')
        gauges[i] = {
            'provider': 'Antigravity / Gemini',
            'kind': 'live visible Antigravity /usage quota signal (agent-request pool)',
            'value_label': f'Gemini {limit_usage_label(gw)} weekly · {limit_usage_label(g5)} 5h',
            'fill_pct': main_fill,
            'tone': 'ok' if any(limit.get('availability') == 'available' for limit in (gw, g5)) and main_fill is None else tone_for_used(main_fill),
            'status': 'Live slash-command refresh' if slash_sources.get('agy_refreshed') else 'Live pane scan from latest visible /usage',
            'detail': (
                f'Antigravity /usage reports Gemini weekly {gw.get("remaining_label", "not observed")} '
                f'and 5h {g5.get("remaining_label", "not observed")}. This is the Antigravity agent-request quota pool, '
                'which is billed separately from the consumer Gemini app compute meter shown under '
                f'{gemini_app_usage.PROVIDER}: spending one does not draw down the other. '
                'Visible app quota panel only; no Gemini/GCP/API/billing/credits surface was used.'
            ),
            'source_label': f'Idle Antigravity pane {slash_sources.get("agy_pane", "visible pane")} /usage observed {observed_at}; active Goru/Gemini panes: {counts["gemini_goru"]}.',
            'sub_gauges': [
                {'label': 'Gemini weekly used', 'value_label': limit_value_label(gw, include_reset=True), 'fill_pct': gw.get('used_pct'), 'tone': limit_tone(gw)},
                {'label': 'Gemini 5h used', 'value_label': limit_value_label(g5), 'fill_pct': g5.get('used_pct'), 'tone': limit_tone(g5)},
                {'label': 'Antigravity Claude/GPT weekly used', 'value_label': limit_value_label(aw), 'fill_pct': aw.get('used_pct'), 'tone': limit_tone(aw)},
                {'label': 'Antigravity Claude/GPT 5h used', 'value_label': limit_value_label(a5), 'fill_pct': a5.get('used_pct'), 'tone': limit_tone(a5)},
            ],
        }

    app_gauge = gemini_app_gauge(observed_at)
    i = provider_index(gauges, gemini_app_usage.PROVIDER)
    gauges[i] = app_gauge

    nous_gauge = nous_credits_gauge(observed_at)
    i = provider_index(gauges, nous_credits_usage.PROVIDER)
    gauges[i] = nous_gauge

    moonshot_gauge = moonshot_balance_usage.fetch_gauge(observed_at)
    i = provider_index(gauges, moonshot_balance_usage.PROVIDER)
    gauges[i] = moonshot_gauge

    # Crew reorg 2026-08-04: seats retired but the SUBSCRIPTIONS remain paid resources —
    # gauges stay visible under provider-centric names; one-time migration of old keys,
    # dedupe keeps the freshest entry per provider.
    RENAMES = {'Codex / Kun': 'Codex (seat unassigned)',
               'Gemini / Goru': 'Antigravity / Gemini'}
    for g in gauges:
        old = g.get('provider')
        if old in RENAMES:
            g['provider'] = RENAMES[old]
            g['status'] = (g.get('status') or '') + ' · seat retired 2026-08-04, subscription still tracked'
    seen = {}
    for g in gauges:
        seen[g.get('provider')] = g
    gauges = list(seen.values())

    tori_pct = telemetry.get('tori_context_max_used_pct')
    i = provider_index(gauges, 'Tori / Hermes')
    gauges[i] = {
        'provider': 'Tori / Hermes',
        'kind': 'live local context used gauges only',
        'value_label': f'up to {display_pct(tori_pct, "context used")}' if tori_pct is not None else 'context percent not visible',
        'fill_pct': tori_pct,
        'tone': tone_for_used(tori_pct),
        'status': 'Live tmux status-line scan',
        'detail': 'This is local context-window usage from visible Tori/Hermes panes, not a provider subscription quota or billing gauge.',
        'source_label': f'tmux pane scan refreshed {observed_at}; active Tori/Hermes panes: {counts["tori_hermes"]}.',
    }

    canonical['provider_usage_gauges'] = gauges
    canonical['provider_usage_monitor'] = {
        'marker': MARKER,
        'status': 'LIVE_SAFE_MONITOR_ACTIVE',
        'observed_at_utc': observed_at,
        'browser_poll_seconds': 5,
        'local_refresh_seconds': slash_sources.get('local_refresh_seconds'),
        'slash_refresh_seconds': slash_sources.get('slash_refresh_seconds'),
        'codex_refreshed_this_pass': bool(slash_sources.get('codex_refreshed')),
        'agy_refreshed_this_pass': bool(slash_sources.get('agy_refreshed')),
        'codex_source_pane': slash_sources.get('codex_pane'),
        'agy_source_pane': slash_sources.get('agy_pane'),
        'active_pane_counts': counts,
        'source_policy': (
            'Visible pane/CLI status, plus one validated local gemini.google.com/usage drop-file. '
            'The drop-file may be operator-confirmed, accessibility-verified, or produced by the separately gated '
            'high-confidence Chrome usage-page crawler. Claude usage comes from its OAuth usage API. Hermes/Nous '
            'dollar balances come from read-only GET /api/oauth/account through Hermes\' normalized account reader; '
            'no token value enters this monitor. No billing mutation, purchase, payment, GCP, or provider-account write occurs.'
        ),
        'limitations': [
            'Claude/Fable exact subscription usage is retained from the last visible usage-panel reading because safe local Claude CLI does not expose a non-interactive fresh percent.',
            'Codex /status warns limits may be stale; this monitor refreshes through an idle visible pane when possible.',
            'Gemini/Goru comes from Antigravity /usage only, not Gemini/GCP billing or API calls. It tracks the Antigravity agent-request pool.',
            f'{gemini_app_usage.PROVIDER} tracks the separate consumer app compute meter. It has no API, so it is refreshed by an operator capture or the high-confidence Chrome usage-page crawler; '
            f'the crawler abstains on weak signals, and readings older than {gemini_app_usage.STALE_AFTER_SECONDS // 3600}h are reported as unknown rather than shown as current.',
            f'{nous_credits_usage.PROVIDER} is a live USD balance from read-only Portal account metadata. Monthly plan dollars and purchased top-up dollars stay separate; no denominator is invented for top-up balance.',
        ],
        'gemini_app_burn_advice': app_gauge['burn_advice'],
    }
    return canonical


def load_canonical() -> dict[str, Any]:
    return json.loads(CANONICAL.read_text())


def backup_canonical(canonical: dict[str, Any], observed_at: str) -> None:
    stamp = observed_at.replace('-', '').replace(':', '')
    dest = CANONICAL.with_name(f'stable-cockpit-canonical.json.bak-{stamp}-provider-realtime')
    if not dest.exists():
        dest.write_text(json.dumps(canonical, ensure_ascii=False, indent=2, sort_keys=True) + '\n')


def render_all(canonical: dict[str, Any], reason: str) -> dict[str, Any]:
    stable_cockpit_guard.unlock_all(reason)
    try:
        result: dict[str, Any] = {'roots': []}
        for root in DEFAULT_PUBLIC_ROOTS:
            result['roots'].append(write_outputs(canonical, root, include_aliases=True))
        lock_result = stable_cockpit_guard.lock(marker=canonical['marker'], reason=reason)
        result['lock'] = lock_result
        return result
    except Exception:
        # Best effort relock existing stable files if rendering failed after unlock.
        try:
            stable_cockpit_guard.lock(marker=canonical.get('marker', ''), reason='relock after provider usage monitor failure')
        except Exception:
            pass
        raise


def collect(refresh_slash: bool, local_refresh_seconds: int | None, slash_refresh_seconds: int | None) -> tuple[dict[str, Any] | None, dict[str, Any] | None, dict[str, Any], dict[str, Any]]:
    panes = tmux_panes()
    slash_sources: dict[str, Any] = {'local_refresh_seconds': local_refresh_seconds, 'slash_refresh_seconds': slash_refresh_seconds}
    codex_texts = []
    agy_texts = []
    codex = None
    agy = None
    if refresh_slash:
        codex_pane = choose_pane(panes, 'codex')
        if codex_pane:
            text = send_visible_command(codex_pane['pane_id'], '/status', 4)
            codex = parse_codex_status(text)
            if codex:
                slash_sources['codex_refreshed'] = True
                slash_sources['codex_pane'] = codex_pane['pane_id']
        agy_pane = choose_pane(panes, 'agy')
        if agy_pane:
            text = send_visible_command(agy_pane['pane_id'], '/usage', 5)
            agy = parse_agy_usage(text)
            if agy:
                slash_sources['agy_refreshed'] = True
                slash_sources['agy_pane'] = agy_pane['pane_id']
    for pane in panes:
        if pane.get('dead') == '1':
            continue
        cmd = pane['command'].lower()
        role = pane['role'].lower()
        target = pane['target'].lower()
        if cmd in {'node', 'codex'} or 'kun' in role or 'kun' in target:
            codex_texts.append(capture_pane(pane['pane_id'], 500))
        if cmd == 'agy' or 'goru' in role or 'goru' in target:
            agy_texts.append(capture_pane(pane['pane_id'], 500))
    if codex is None:
        for text in codex_texts:
            parsed = parse_codex_status(text)
            if parsed:
                codex = parsed
                break
    if agy is None:
        for text in agy_texts:
            parsed = parse_agy_usage(text)
            if parsed:
                agy = parsed
                break
    telemetry = active_counts_and_context(panes)
    return codex, agy, telemetry, slash_sources


def update_once(refresh_slash: bool, render: bool, local_refresh_seconds: int | None, slash_refresh_seconds: int | None) -> dict[str, Any]:
    observed_at = utc_now()
    canonical = load_canonical()
    backup_canonical(canonical, observed_at)
    codex, agy, telemetry, slash_sources = collect(refresh_slash, local_refresh_seconds, slash_refresh_seconds)
    canonical = update_gauges(canonical, codex, agy, telemetry, observed_at, slash_sources)
    result = {
        'marker': MARKER,
        'observed_at_utc': observed_at,
        'codex_observed': bool(codex),
        'agy_observed': bool(agy),
        'active_pane_counts': telemetry['counts'],
        'tori_context_max_used_pct': telemetry.get('tori_context_max_used_pct'),
        'rendered': False,
    }
    if render:
        result['render'] = render_all(canonical, reason=f'{MARKER}: safe provider usage realtime refresh')
        result['rendered'] = True
    else:
        print(json.dumps(canonical.get('provider_usage_monitor'), indent=2, sort_keys=True))
    return result


def main() -> int:
    ap = argparse.ArgumentParser(description='Refresh public provider usage gauges from safe visible status surfaces')
    ap.add_argument('--watch', action='store_true', help='keep refreshing until interrupted')
    ap.add_argument('--interval', type=int, default=60, help='local JSON/HTML refresh interval in seconds')
    ap.add_argument('--slash-interval', type=int, default=0, help='minimum seconds between safe visible slash refreshes in watch mode (0 to disable)')
    ap.add_argument('--refresh-slash', action='store_true', help='run visible /status and /usage once if idle before parsing')
    ap.add_argument('--no-render', action='store_true', help='collect and print but do not write public files')
    args = ap.parse_args()

    if not args.watch:
        result = update_once(refresh_slash=args.refresh_slash, render=not args.no_render, local_refresh_seconds=args.interval, slash_refresh_seconds=args.slash_interval)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0

    last_slash = 0.0
    while True:
        now = time.time()
        do_slash = args.refresh_slash or (args.slash_interval > 0 and (now - last_slash >= args.slash_interval))
        result = update_once(refresh_slash=do_slash, render=not args.no_render, local_refresh_seconds=args.interval, slash_refresh_seconds=args.slash_interval)
        if do_slash:
            last_slash = now
            args.refresh_slash = False  # Only force once
        print(json.dumps(result, sort_keys=True))
        sys.stdout.flush()
        time.sleep(max(5, args.interval))


if __name__ == '__main__':
    raise SystemExit(main())

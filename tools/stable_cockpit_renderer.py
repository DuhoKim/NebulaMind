#!/usr/bin/env python3
"""Render NebulaMind's stable Baseline cockpit from canonical JSON.

Stable route invariant:
  canonical JSON -> this renderer/template -> live-steering-cockpit.html

Packet/review pages may be small and timestamped, but they must never be copied
onto the stable route. The guard validates stable-route richness; this renderer
keeps the rich structure data-driven instead of hand-authored per packet.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path('/Users/duhokim/NebulaMind/NebulaMind')
LIVE_FRONTEND = Path('/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend')
DEFAULT_CANONICAL_PATH = ROOT / 'frontend/public/agent-reports/stable-cockpit-canonical.json'
DEFAULT_TEMPLATE_PATH = ROOT / 'tools/templates/stable-cockpit-template.html'
DEFAULT_PUBLIC_ROOTS = [ROOT / 'frontend/public/agent-reports', LIVE_FRONTEND / 'public/agent-reports',
                        # 2026-08-20: the cockpit root too — index.html links these pages there,
                        # and its copies had been 45-day orphans nothing refreshed.
                        Path('/Users/duhokim/HermesOps/cockpit')]

# Drift guard for the cockpit's stated primitive. Updated 2026-08-05 (Duho: the wiki era is
# over; the current NebulaMind is an AI scientist for galaxy evolution). The old value was
# 'papers → claim/status ledger → research-status/debate map → prose → derived claims/evidence/trust'
# and is preserved in the canonical's wiki_era_archive.
BASELINE_PRIMITIVE = 'frontier ranking → frozen measurement contract → reviewed-script measurement → adversarial review → receipted paper'
RICH_STABLE_SENTINEL = 'RICH_BASELINE_STABLE_COCKPIT_V1'
STABLE_ROUTE_FILENAMES = {
    'live-steering-cockpit.html',
    'baseline-roadmap.html',
    'baseline-galaxy-current.html',
    'mobile.html',
}
TIMESTAMPED_DETAIL_RE = re.compile(r'(?:packet|review|execution|result|detail|preflight|cockpit).*20\d{6}T\d{6}Z|20\d{6}T\d{6}Z.*(?:packet|review|execution|result|detail|preflight|cockpit)', re.I)
STALE_APPROVAL_PREFIXES = [
    'APPROVE EXECUTE baseline_step9e_claim_id_guarded_sql_packet',
    'APPROVE EXECUTE galaxy_claim_layer_reconciliation_preflight',
]


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def canonical_bytes(canonical: dict[str, Any]) -> bytes:
    return json.dumps(canonical, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')


def canonical_sha256(canonical: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(canonical)).hexdigest()


def esc(value: Any) -> str:
    return html.escape('' if value is None else str(value), quote=True)


def validate_canonical(canonical: dict[str, Any]) -> None:
    required_top = ['schema_version', 'marker', 'updated_at_utc', 'active_target', 'baseline', 'baseline_steps', 'hero', 'latest_result', 'next_move', 'lane_board', 'safety_ledger', 'prevention']
    missing = [key for key in required_top if key not in canonical]
    if missing:
        raise ValueError(f'missing canonical keys: {missing}')
    if canonical['schema_version'] != 'stable-cockpit-canonical.v1':
        raise ValueError(f'unsupported schema_version: {canonical.get("schema_version")}')
    baseline = canonical['baseline']
    if baseline.get('primitive') != BASELINE_PRIMITIVE:
        raise ValueError('canonical baseline primitive drift')
    steps = canonical.get('baseline_steps') or []
    if len(steps) != 11:
        raise ValueError('canonical baseline_steps must contain exactly Step 0 through Step 10')
    actual_steps = [step.get('step') for step in steps]
    if actual_steps != list(range(11)):
        raise ValueError(f'canonical baseline_steps must be ordered 0..10, got {actual_steps}')
    if not canonical.get('marker'):
        raise ValueError('canonical marker required')
    if not canonical.get('lane_board'):
        raise ValueError('canonical lane_board must not be empty')
    if not canonical.get('safety_ledger'):
        raise ValueError('canonical safety_ledger must not be empty')


def render_pills(pills: list[Any]) -> str:
    return ''.join(f'<span class="pill"><span class="dot okdot"></span>{esc(pill)}</span>' for pill in pills)


def render_method_result_buttons(buttons: list[dict[str, Any]]) -> str:
    if not buttons:
        return ''
    cards = []
    for button in buttons:
        href = esc(button.get('href', '#'))
        label = esc(button.get('label', 'Method result'))
        body = esc(button.get('description', 'Open this method result page.'))
        cards.append(
            '<a href="' + href + '" style="display:block;padding:12px 14px;border:1px solid rgba(169,189,212,.35);border-radius:14px;background:rgba(3,9,19,.58);color:#edf6ff;text-decoration:none">'
            '<span style="display:block;font-weight:800;font-size:13px">' + label + '</span>'
            '<span style="display:block;margin-top:4px;color:#a9bdd4;font-size:12px;line-height:1.45">' + body + '</span>'
            '</a>'
        )
    return (
        '<div id="method-result-buttons" aria-label="Galaxy Evolution method result pages" '
        'style="margin-top:18px;padding:16px;border:1px solid rgba(98,214,239,.32);border-radius:18px;background:rgba(8,24,42,.70)">'
        '<div style="color:#62d6ef;text-transform:uppercase;letter-spacing:.13em;font-weight:800;font-size:12px;margin-bottom:8px">Three paper-to-wiki result lanes</div>'
        '<div style="color:#dcecff;margin-bottom:12px">The main outputs are separate Galaxy Evolution wiki-page results for the three methods. Work them one by one, then compare.</div>'
        '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px">'
        + ''.join(cards) +
        '</div></div>'
    )


def render_latest_cards(cards: list[dict[str, Any]]) -> str:
    out = []
    for card in cards:
        css = esc(card.get('tone', 'ok'))
        out.append(f'<div class="box {css}"><h3>{esc(card.get("title"))}</h3><p class="mut">{esc(card.get("body"))}</p></div>')
    return ''.join(out)


def clamp_pct(value: Any) -> int | None:
    if value in (None, ''):
        return None
    try:
        return max(0, min(100, int(round(float(value)))))
    except (TypeError, ValueError):
        return None


def provider_usage_limits_to_gauges(limits: dict[str, Any]) -> list[dict[str, Any]]:
    """Backward-compatible fallback for older canonical payloads.

    The gauges are pane-observed usage-limit/status displays, not billing-API
    measurements. Unknown numeric quotas are intentionally rendered as neutral
    striped gauges instead of invented percentages.
    """
    if not limits:
        return []
    return [
        {
            'provider': 'Claude / Fable + claude-seat',
            'kind': 'plan-limit notice',
            'value_label': '50% weekly cap visible',
            'fill_pct': 50,
            'tone': 'warn',
            'detail': limits.get('claude_fable_lana', ''),
            'source_label': limits.get('source', 'pane-observed snapshot'),
        },
        {
            # Codex lane retired 2026-08; the kimi seats gate on the Kimi K3 direct
            # Moonshot key. The wallet number is refreshed by the monitor from the
            # local balance cache written by tools/moonshot_balance_usage.py.
            'provider': 'Moonshot / kimi (K3 direct)',
            'kind': 'dollar wallet',
            'value_label': 'wallet balance',
            'fill_pct': None,
            'tone': 'ok',
            'detail': limits.get('kimi_kun_miru', 'balance cache not read yet'),
            'source_label': limits.get('source', 'local balance cache'),
        },
        {
            'provider': 'Antigravity / agy (Gemini)',
            'kind': 'quota not visible',
            'value_label': 'numeric quota not visible',
            'fill_pct': None,
            'tone': 'danger',
            'detail': limits.get('gemini_goru', ''),
            'source_label': limits.get('source', 'pane-observed snapshot'),
        },
        {
            'provider': 'Hermes / gpt seats (context)',
            'kind': 'local context gauge',
            'value_label': 'context gauge only',
            'fill_pct': None,
            'tone': 'warn',
            'detail': limits.get('tori_hermes', ''),
            'source_label': limits.get('source', 'pane-observed snapshot'),
        },
    ]



_OBSERVED_RE = re.compile(r'(\d{4}-\d{2}-\d{2})(?:T(\d{2}):(\d{2}))?')


def gauge_observed_age(source_label: str, kind: str = '', status: str = '') -> tuple[str, str]:
    """Return (age_text, tone) for a gauge, from the timestamp inside its source_label.

    Each provider card records when it was observed, but only inside prose
    ("... observed 2026-08-14T04:59:49Z"). Nothing surfaced it, so a card whose
    number was 39 days old looked identical to one refreshed a minute ago.
    Added 2026-08-14 at Duho's request after exactly that: the Flow/Veo figure
    had been carried since 2026-07-12 and nobody could tell.
    """
    if not source_label:
        return ('observation time not recorded', 'stale')
    # Some cards have no live surface by design -- documented plan/credit references
    # rather than measurements. Ageing them red cries wolf and devalues the warning on
    # cards that genuinely decayed. Added 2026-08-14: Flow/Veo showed "33 days ago" in
    # red when nothing about it had gone out of date and no live source exists to poll.
    haystack = f'{kind} {status} {source_label}'.lower()
    is_reference = any(t in haystack for t in (
        'not exposed', 'not captured', 'no live', 'documentation', 'planning'))
    m = _OBSERVED_RE.search(source_label)
    if not m:
        return ('observation time not recorded', 'stale')
    try:
        if m.group(2):
            when = datetime(int(m.group(1)[:4]), int(m.group(1)[5:7]), int(m.group(1)[8:10]),
                                     int(m.group(2)), int(m.group(3)), tzinfo=timezone.utc)
        else:
            when = datetime(int(m.group(1)[:4]), int(m.group(1)[5:7]), int(m.group(1)[8:10]),
                                     tzinfo=timezone.utc)
    except ValueError:
        return ('observation time not recorded', 'stale')
    kst = when + timedelta(hours=9)
    stamp = kst.strftime('%H:%M') if m.group(2) else kst.strftime('%d %b')
    mins = (datetime.now(timezone.utc) - when).total_seconds() / 60
    if is_reference:
        return (f'reference \u00b7 verified {kst.strftime("%d %b %Y")} \u00b7 no live source to poll', 'reference')
    if mins < 0:
        return (f'observed just now ({stamp} KST)', 'fresh')
    if mins < 90:
        return (f'observed {int(mins)} min ago \u00b7 {stamp} KST', 'fresh')
    hours = mins / 60
    if hours < 36:
        return (f'observed {int(hours)}h ago \u00b7 {stamp} KST', 'aging')
    return (f'observed {int(hours / 24)} days ago \u00b7 {stamp} KST', 'stale')


def render_provider_usage_gauges(canonical: dict[str, Any]) -> str:
    gauges = canonical.get('provider_usage_gauges') or provider_usage_limits_to_gauges(canonical.get('provider_usage_limits') or {})
    if not gauges:
        return '<div class="box full warn"><h3>No provider gauge data recorded</h3><p class="mut">Provider usage limits have not been observed in the visible panes yet.</p></div>'
    out = []
    for gauge in gauges:
        pct = clamp_pct(gauge.get('fill_pct'))
        tone = esc(gauge.get('tone', 'warn'))
        fill_class = 'gauge-fill unknown' if pct is None else 'gauge-fill'
        fill_width = 100 if pct is None else pct
        value_label = esc(gauge.get('value_label', 'not observed'))
        aria_now = '' if pct is None else f' aria-valuenow="{pct}" aria-valuemin="0" aria-valuemax="100"'
        sub_gauges = []
        for sub in gauge.get('sub_gauges') or []:
            sub_pct = clamp_pct(sub.get('fill_pct'))
            sub_tone = esc(sub.get('tone', gauge.get('tone', 'warn')))
            sub_fill_class = 'gauge-fill unknown' if sub_pct is None else 'gauge-fill'
            sub_fill_width = 100 if sub_pct is None else sub_pct
            sub_aria_now = '' if sub_pct is None else f' aria-valuenow="{sub_pct}" aria-valuemin="0" aria-valuemax="100"'
            sub_gauges.append(
                f'<div class="sub-gauge-item {sub_tone}">'
                f'<div class="sub-gauge-label"><span>{esc(sub.get("label", "Sub-limit"))}</span><b>{esc(sub.get("value_label", "not observed"))}</b></div>'
                f'<div class="gauge-track" role="meter" aria-label="{esc(gauge.get("provider"))} {esc(sub.get("label", "sub-limit"))} gauge"{sub_aria_now}>'
                f'<div class="{sub_fill_class}" style="width:{sub_fill_width}%"></div>'
                f'<span class="gauge-value">{esc(sub.get("value_label", "not observed"))}</span>'
                '</div></div>'
            )
        sub_gauge_html = '' if not sub_gauges else '<div class="sub-gauge-list">' + ''.join(sub_gauges) + '</div>'
        out.append(
            f'<div class="box provider-gauge-card {tone}" data-provider="{esc(gauge.get("provider"))}">'
            f'<h3>{esc(gauge.get("provider"))}</h3>'
            f'<p class="gauge-kind">{esc(gauge.get("kind", "usage-limit snapshot"))}</p>'
            f'<div class="gauge-track" role="meter" aria-label="{esc(gauge.get("provider"))} usage limit gauge"{aria_now}>'
            f'<div class="{fill_class}" style="width:{fill_width}%"></div>'
            f'<span class="gauge-value">{value_label}</span>'
            '</div>'
            f'{sub_gauge_html}'
            f'<p class="mut"><b>{esc(gauge.get("status", "Observed status"))}</b></p>'
            f'<p class="mut">{esc(gauge.get("detail"))}</p>'
            f'<p class="gauge-observed {gauge_observed_age(gauge.get("source_label", ""), gauge.get("kind", ""), gauge.get("status", ""))[1]}">'
            f'{esc(gauge_observed_age(gauge.get("source_label", ""), gauge.get("kind", ""), gauge.get("status", ""))[0])}</p>'
            f'<p class="marker">{esc(gauge.get("source_label", "pane-observed snapshot"))}</p>'
            '</div>'
        )
    return ''.join(out)


def render_baseline_steps(steps: list[dict[str, Any]]) -> str:
    out = []
    for step in steps:
        number = int(step.get('step'))
        status = str(step.get('status', '')).upper()
        css = 'ok' if status in {'PASS', 'DONE', 'COMPLETE'} else 'warn' if status in {'ACTIVE', 'NEXT', 'PARTIAL'} else 'danger'
        out.append(
            f'<div class="box {css}" data-baseline-step="{number}">'
            f'<h3><span class="step-num">Step {number}</span> · {esc(step.get("title"))}</h3>'
            f'<p><b>{esc(step.get("status"))}</b></p>'
            f'<p class="mut">{esc(step.get("body"))}</p>'
            '</div>'
        )
    return ''.join(out)


def render_rows(rows: list[dict[str, Any]], first_key: str = 'item', second_key: str = 'status') -> str:
    return ''.join(f'<tr><td>{esc(row.get(first_key))}</td><td>{esc(row.get(second_key))}</td></tr>' for row in rows)


def render_lanes(lanes: list[dict[str, Any]]) -> str:
    out = []
    for lane in lanes:
        status = str(lane.get('status', '')).upper()
        css = 'ok' if status in {'DONE', 'PASS', 'PASS_DONE', 'GREEN'} else 'warn'
        out.append(
            f'<div class="box {css}"><h3>{esc(lane.get("lane"))} · {esc(lane.get("status"))}</h3>'
            f'<p class="mut">{esc(lane.get("detail"))}</p></div>'
        )
    return ''.join(out)


def render_list(items: list[Any]) -> str:
    return ''.join(f'<li>{esc(item)}</li>' for item in items)


def render_artifacts(items: list[dict[str, Any]]) -> str:
    if not items:
        return '<li>No artifact links recorded.</li>'
    out = []
    for item in items:
        label = esc(item.get('label', 'artifact'))
        path = esc(item.get('path', ''))
        out.append(f'<li><b>{label}</b>: <code>{path}</code></li>')
    return ''.join(out)


def render_septet(canonical: dict[str, Any]) -> str:
    """Septet seat monitor. Added 2026-08-06 on Duho's ask.

    The one thing this must show is a seat sitting idle beside a lane that owes work: on
    2026-08-06 an amendment had its edits applied at 23:14 and was never resubmitted, and it
    blocked a whole measurement sequence for eleven hours because nothing joined 'lane is stuck'
    to 'nobody is working it'. Idle is rendered as a warning state, not a neutral one.
    """
    septet = canonical.get('septet') or {}
    seats = septet.get('seats') or []
    if not seats:
        return '<div class="muted">no septet state recorded</div>'
    cells = []
    for seat in seats:
        state = str(seat.get('state', 'unknown'))
        working = state == 'WORKING'
        blocked = bool(seat.get('owes'))
        colour = '#2f6fa8' if working else ('#a8622f' if blocked else '#39414f')
        detail = esc(seat.get('detail', ''))
        cells.append(
            f'<div style="border:1px solid {colour};border-radius:8px;padding:10px 12px">'
            f'<div style="font-weight:600">{esc(seat.get("name"))}'
            f'<span style="float:right;font-size:11px;color:{colour}">{esc(state)}</span></div>'
            f'<div class="muted" style="font-size:12px;margin-top:4px">{esc(seat.get("role"))}</div>'
            + (f'<div style="font-size:12px;margin-top:6px">{detail}</div>' if detail else '')
            + '</div>')
    warn = septet.get('warning')
    warn_html = (f'<div style="margin-top:10px;color:#d69a66;font-size:13px">{esc(warn)}</div>'
                 if warn else '')
    return ('<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));'
            'gap:10px">' + ''.join(cells) + '</div>' + warn_html)


def render_stable_cockpit_html(canonical: dict[str, Any], template_path: Path | None = None) -> str:
    validate_canonical(canonical)
    template = (template_path or DEFAULT_TEMPLATE_PATH).read_text()
    marker = canonical['marker']
    baseline = canonical['baseline']
    hero = canonical['hero']
    latest = canonical['latest_result']
    next_move = canonical['next_move']
    prevention = canonical['prevention']
    target = canonical['active_target']
    claim_rows = canonical.get('claim_layer_status') or [
        {'item': 'Active target', 'status': f"{target.get('title')} · page {target.get('page_id')} · version {target.get('version_num')}"},
        {'item': 'Content hash', 'status': target.get('content_sha256')},
        {'item': 'Mode', 'status': canonical.get('mode')},
    ]
    copyable = canonical.get('copyable_state') or 'NO ACTIVE EXECUTION PHRASE. Stable cockpit generated from canonical JSON.'
    replacements = {
        '__HTML_TITLE__': esc(canonical.get('html_title', f"{target.get('title', 'NebulaMind')} stable cockpit")),
        '__MARKER__': esc(marker),
        '__CANONICAL_SHA256__': canonical_sha256(canonical),
        '__HERO_KICKER__': esc(hero.get('kicker')),
        '__HERO_HEADLINE__': esc(hero.get('headline')),
        '__HERO_LEAD__': esc(hero.get('lead')),
        '__PILLS__': render_pills(hero.get('pills', [])),
        '__METHOD_RESULT_BUTTONS__': render_method_result_buttons(canonical.get('method_result_buttons', [])),
        '__BASELINE_TITLE__': esc(baseline.get('title', 'THE BASELINE')),
        '__BASELINE_PRIMITIVE__': esc(baseline.get('primitive')),
        '__BASELINE_SUMMARY__': esc(baseline.get('summary')),
        '__BASELINE_STEPS__': render_baseline_steps(canonical.get('baseline_steps', [])),
        '__LATEST_TITLE__': esc(latest.get('title')),
        '__LATEST_CARDS__': render_latest_cards(latest.get('cards', [])),
        '__PROVIDER_USAGE_GAUGES__': render_provider_usage_gauges(canonical),
        '__CLAIM_ROWS__': render_rows(claim_rows),
        '__NEXT_RECOMMENDED__': esc(next_move.get('recommended')),
        '__NEXT_LATER__': render_list(next_move.get('later', [])),
        '__LANE_CARDS__': render_lanes(canonical.get('lane_board', [])),
        '__PREVENTION_RULES__': render_list(prevention.get('rules', [])),
        '__PREVENTION_CONTEXT__': esc(prevention.get('context')),
        '__SAFETY_ROWS__': render_rows(canonical.get('safety_ledger', [])),
        '__COPYABLE_STATE__': esc(copyable),
        '__UPDATED_AT_UTC__': esc(canonical.get('updated_at_utc')),
        '__ARTIFACT_LINKS__': render_artifacts(canonical.get('artifacts', [])),
        '__SEPTET__': render_septet(canonical),
    }
    html_text = template
    for token, value in replacements.items():
        html_text = html_text.replace(token, value)
    leftover = sorted(set(re.findall(r'__[A-Z0-9_]+__', html_text)))
    if leftover:
        raise ValueError(f'unrendered template tokens: {leftover}')
    return html_text


def render_status_json(canonical: dict[str, Any]) -> dict[str, Any]:
    validate_canonical(canonical)
    status = {
        'marker': canonical['marker'],
        'mode': canonical.get('mode'),
        'updated_at_utc': canonical.get('updated_at_utc'),
        'canonical_source_sha256': canonical_sha256(canonical),
        'rendered_by': 'tools/stable_cockpit_renderer.py',
        'stable_cockpit_contract': {
            'sentinel': RICH_STABLE_SENTINEL,
            'source': 'stable-cockpit-canonical.json',
            'template': 'tools/templates/stable-cockpit-template.html',
            'stable_route_is_not_packet_page': True,
        },
    }
    for key in ['active_target', 'baseline_steps', 'db_execution', 'public_api_after', 'excluded_actions', 'rollback', 'quintet_prevention', 'next_recommended_action', 'plain_english_result', 'packet_status', 'copyable_state', 'provider_usage_limits', 'provider_usage_gauges', 'provider_usage_monitor']:
        if key in canonical:
            status[key] = canonical[key]
    status['active_execution_phrase'] = canonical.get('active_execution_phrase')
    status['no_active_execution_phrase'] = canonical.get('active_execution_phrase') in (None, '')
    # Existing public status route is already served without a restart. Embed the
    # canonical state here as a public fallback for environments where adding a
    # brand-new public JSON filename requires a frontend restart/build refresh.
    status['canonical_state'] = canonical
    return status


def render_mobile_html(canonical: dict[str, Any]) -> str:
    validate_canonical(canonical)
    marker = esc(canonical['marker'])
    baseline = canonical['baseline']
    hero = canonical['hero']
    latest = canonical.get('latest_result', {})
    next_move = canonical.get('next_move', {})
    copyable = canonical.get('copyable_state') or 'NO ACTIVE EXECUTION PHRASE. Stable cockpit generated from canonical JSON.'
    steps = ''.join(
        f'<li><b>Step {int(step.get("step"))}: {esc(step.get("title"))}</b> — {esc(step.get("status"))}</li>'
        for step in canonical.get('baseline_steps', [])
    )
    cards = ''.join(
        f'<li><b>{esc(card.get("title"))}</b>: {esc(card.get("body"))}</li>'
        for card in latest.get('cards', [])
    )
    method_links = ''.join(
        f'<li><a style="color:#9bdcff" href="{esc(button.get("href", "#"))}">{esc(button.get("label", "Method result"))}</a> — {esc(button.get("description", ""))}</li>'
        for button in canonical.get('method_result_buttons', [])
    )
    provider_gauges = canonical.get('provider_usage_gauges') or provider_usage_limits_to_gauges(canonical.get('provider_usage_limits') or {})
    provider_items = ''
    for gauge in provider_gauges:
        sub_labels = '; '.join(f'{sub.get("label")}: {sub.get("value_label")}' for sub in (gauge.get('sub_gauges') or []))
        if sub_labels:
            sub_labels = f' ({esc(sub_labels)})'
        provider_items += f'<li><b>{esc(gauge.get("provider"))}</b>: {esc(gauge.get("value_label", "not observed"))}{sub_labels} — {esc(gauge.get("detail"))}</li>'
    return (
        '<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>{esc(hero.get("headline"))}</title></head>'
        '<body style="margin:0;background:#06101e;color:#edf6ff;font:16px -apple-system;padding:18px" '
        f'data-cockpit-contract="{RICH_STABLE_SENTINEL}" data-marker="{marker}">'
        '<h1>THE BASELINE</h1>'
        f'<p>{esc(baseline.get("primitive"))}</p>'
        f'<ol>{steps}</ol>'
        f'<h2>{esc(hero.get("headline"))}</h2><p>{esc(hero.get("lead"))}</p>'
        f'<h2>Three paper-to-wiki result lanes</h2><ul>{method_links}</ul>'
        f'<h2>Provider usage gauges</h2><ul>{provider_items}</ul>'
        f'<h2>{esc(latest.get("title", "Current truth"))}</h2><ul>{cards}</ul>'
        f'<h2>Next move</h2><p>{esc(next_move.get("recommended"))}</p>'
        f'<h2>Copyable state</h2><p>{esc(copyable)}</p>'
        f'<p>{marker}</p></body></html>'
    )


def is_timestamped_detail_path(path: Path) -> bool:
    name = path.name
    if name in STABLE_ROUTE_FILENAMES:
        return False
    return bool(TIMESTAMPED_DETAIL_RE.search(name) or TIMESTAMPED_DETAIL_RE.search(str(path)))


def validate_packet_detail_page(path: Path, text: str, marker: str | None = None) -> dict[str, Any]:
    checks = {
        'not_stable_route': path.name not in STABLE_ROUTE_FILENAMES,
        'timestamped_detail_path': is_timestamped_detail_path(path),
        'doctype_first': text.lstrip().lower().startswith('<!doctype html'),
        'marker_present': (not marker) or (marker in text),
        'stale_approval_absent': all(bad not in text for bad in STALE_APPROVAL_PREFIXES),
    }
    failed = [name for name, ok in checks.items() if not ok]
    messages = []
    if not checks['not_stable_route']:
        messages.append('packet detail page cannot be the stable route')
    if not checks['timestamped_detail_path']:
        messages.append('packet detail page must use a timestamped detail path')
    messages.extend(failed)
    return {'path': str(path), 'checks': checks, 'failed': messages, 'ok': not failed}


def write_outputs(canonical: dict[str, Any], out_dir: Path, template_path: Path | None = None, include_aliases: bool = True) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    html_text = render_stable_cockpit_html(canonical, template_path=template_path)
    status_text = json.dumps(render_status_json(canonical), ensure_ascii=False, indent=2, sort_keys=True) + '\n'
    mobile_text = render_mobile_html(canonical)
    canonical_text = json.dumps(canonical, ensure_ascii=False, indent=2, sort_keys=True) + '\n'
    written = {}
    targets = ['live-steering-cockpit.html']
    if include_aliases:
        targets += ['baseline-roadmap.html', 'baseline-galaxy-current.html']
    for name in targets:
        path = out_dir / name
        path.write_text(html_text)
        written[name] = {'path': str(path), 'bytes': path.stat().st_size, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
    for name, content in [('live-steering-status.json', status_text), ('mobile.html', mobile_text), ('stable-cockpit-canonical.json', canonical_text)]:
        path = out_dir / name
        path.write_text(content)
        written[name] = {'path': str(path), 'bytes': path.stat().st_size, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
    return {'out_dir': str(out_dir), 'marker': canonical['marker'], 'canonical_sha256': canonical_sha256(canonical), 'written': written}


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('render')
    p.add_argument('--canonical', type=Path, default=DEFAULT_CANONICAL_PATH)
    p.add_argument('--template', type=Path, default=DEFAULT_TEMPLATE_PATH)
    p.add_argument('--out-dir', type=Path, required=True)
    p.add_argument('--no-aliases', action='store_true')
    p = sub.add_parser('render-all-public-roots')
    p.add_argument('--canonical', type=Path, default=DEFAULT_CANONICAL_PATH)
    p.add_argument('--template', type=Path, default=DEFAULT_TEMPLATE_PATH)
    p = sub.add_parser('validate-packet-detail')
    p.add_argument('path', type=Path)
    p.add_argument('--marker')
    args = ap.parse_args()
    if args.cmd == 'render':
        canonical = load_json(args.canonical)
        print(json.dumps(write_outputs(canonical, args.out_dir, template_path=args.template, include_aliases=not args.no_aliases), indent=2, sort_keys=True))
        return 0
    if args.cmd == 'render-all-public-roots':
        canonical = load_json(args.canonical)
        result = {'roots': []}
        for root in DEFAULT_PUBLIC_ROOTS:
            result['roots'].append(write_outputs(canonical, root, template_path=args.template, include_aliases=True))
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    if args.cmd == 'validate-packet-detail':
        text = args.path.read_text(errors='replace')
        result = validate_packet_detail_page(args.path, text, marker=args.marker)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0 if result['ok'] else 2
    return 2


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Deterministic checkpoint collector for the approved overnight Paper Board run."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-paper-board-portfolio-20260727')
UA = {'User-Agent': 'NebulaMind-overnight-checkpoint/2026-07-27', 'Cache-Control': 'no-cache'}
LANES = {
    'hwao': ROOT / 'lanes/hwao',
    'p0_lana': ROOT / 'packets/P0-tng-validation/lana',
    'p1_kun': ROOT / 'packets/P1-massive-abundance/kun',
    'p2_goru': ROOT / 'packets/P2-fesc/goru',
}


def now_utc() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def stamp(t: dt.datetime) -> str:
    return t.strftime('%Y%m%dT%H%M%SZ')


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def provider_cards(document: dict) -> list[dict]:
    found: list[dict] = []
    def walk(value):
        if isinstance(value, dict):
            if 'provider' in value and any(k in value for k in ('value_label', 'big', 'sub_gauges')):
                found.append({k: value.get(k) for k in ('provider', 'status', 'value_label', 'big', 'fill_pct', 'source_label', 'sub_gauges') if k in value})
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(document)
    out, seen = [], set()
    for row in found:
        key = (row.get('provider'), row.get('source_label'), row.get('value_label'), row.get('big'))
        if key not in seen:
            seen.add(key)
            out.append(row)
    return out


def lane_state(path: Path) -> dict:
    receipt = path / 'RECEIPT.json'
    state = {
        'path': str(path),
        'file_count': sum(1 for p in path.rglob('*') if p.is_file()),
        'receipt_exists': receipt.exists(),
        'receipt_valid': False,
        'status': 'RUNNING_OR_WAITING',
    }
    if receipt.exists():
        try:
            data = json.loads(receipt.read_text())
            state.update({'receipt_valid': True, 'status': data.get('status'), 'marker': data.get('marker'), 'disposition': data.get('disposition')})
        except Exception as exc:
            state.update({'status': 'INVALID_RECEIPT', 'error': str(exc)})
    return state


def main() -> None:
    t = now_utc()
    sid = stamp(t)
    quota = {'observed_at_utc': t.isoformat(), 'cards': [], 'error': None}
    try:
        doc = fetch_json(f'https://nebulamind.net/agent-reports/live-steering-status.json?checkpoint={sid}')
        quota['document_observed_at_utc'] = doc.get('provider_usage_monitor', {}).get('observed_at_utc')
        quota['cards'] = provider_cards(doc)
    except Exception as exc:
        quota['error'] = f'{type(exc).__name__}: {exc}'
    qpath = ROOT / 'quota' / f'usage_{sid}.json'
    qpath.parent.mkdir(parents=True, exist_ok=True)
    qpath.write_text(json.dumps(quota, indent=2, ensure_ascii=False) + '\n')

    lanes = {name: lane_state(path) for name, path in LANES.items()}
    checkpoint = {
        'observed_at_utc': t.isoformat(),
        'lanes': lanes,
        'quota_path': str(qpath),
        'content_freeze': (ROOT / 'CONTENT_FREEZE_OVERNIGHT_PB_20260727.md').exists(),
        'global_stop': (ROOT / 'GLOBAL_STOP_OVERNIGHT_PB_20260727.md').exists(),
    }
    cpath = ROOT / 'progress' / f'checkpoint_{sid}.json'
    cpath.parent.mkdir(parents=True, exist_ok=True)
    cpath.write_text(json.dumps(checkpoint, indent=2, ensure_ascii=False) + '\n')

    summary = ', '.join(f'{name}={row["status"]}' for name, row in lanes.items())
    ledger = ROOT / 'OVERNIGHT_LEDGER.md'
    with ledger.open('a') as handle:
        handle.write(f'| {t.astimezone(dt.timezone(dt.timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S")} | Deterministic checkpoint | {summary} |\n')
    print(f'OVERNIGHT_PB_CHECKPOINT {sid} {summary} quota_cards={len(quota["cards"])}')


if __name__ == '__main__':
    main()

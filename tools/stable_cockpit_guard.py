#!/usr/bin/env python3
"""Single-writer guard for NebulaMind stable operator cockpit routes.

Purpose:
- live-steering-cockpit.html is the stable Baseline/operator route.
- Run-specific monitors may be thin, but they must not overwrite this route.
- This guard validates the Baseline contract, records ownership, and uses macOS
  uchg flags to make accidental legacy writes fail until an intentional unlock.

Usage:
  python tools/stable_cockpit_guard.py check
  python tools/stable_cockpit_guard.py lock --marker MARKER --reason TEXT
  python tools/stable_cockpit_guard.py unlock --reason TEXT

Future intended stable cockpit updates must:
  1. unlock with a reason,
  2. publish the richer Baseline cockpit/status,
  3. lock with the new marker,
  4. check and public-verify.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/Users/duhokim/NebulaMind/NebulaMind')
LIVE_FRONTEND = Path('/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend')
PUBLIC_ROOTS = [
    ROOT / 'frontend/public/agent-reports',
    LIVE_FRONTEND / 'public/agent-reports',
]
STABLE_FILES = [
    'live-steering-cockpit.html',
    'baseline-roadmap.html',
    'baseline-galaxy-current.html',
    'mobile.html',
    'live-steering-status.json',
    'stable-cockpit-canonical.json',
    'stable-cockpit-owner.json',
]
OWNER = 'stable-cockpit-owner.json'
PUBLIC_URL = 'https://nebulamind.net/agent-reports/live-steering-cockpit.html'
# Kept in lockstep with stable_cockpit_renderer.BASELINE_PRIMITIVE. Updated 2026-08-05 when the
# paper-to-wiki era was retired; the old value lives in the canonical's wiki_era_archive.
BASELINE_PRIMITIVE = 'frontier ranking → frozen measurement contract → reviewed-script measurement → adversarial review → receipted paper'
RICH_STABLE_SENTINEL = 'RICH_BASELINE_STABLE_COCKPIT_V1'
MIN_STABLE_COCKPIT_BYTES = 12000
MIN_STABLE_SECTION_COUNT = 7
RICH_REQUIRED_STRINGS = [
    RICH_STABLE_SENTINEL,
    'id="operator-board"',
    'id="baseline-steps"',
    'id="latest-result"',
    'id="lane-board"',
    'id="safety-ledger"',
]
PACKET_DETAIL_FORBIDDEN_ON_STABLE_ROUTE = [
    'Exact Packet Review',
    'id="execution-gate"',
]
BAD_STRINGS = [
    'Galaxy claim-layer reconciliation monitor',
    '<div id="baseline"></div>',
    'GALAXY_EVOLUTION_AUTONOMOUS_QUINTET_HARDENING',
]
STALE_APPROVAL_PREFIXES = [
    'APPROVE EXECUTE baseline_step9e_claim_id_guarded_sql_packet',
    'APPROVE EXECUTE galaxy_claim_layer_reconciliation_preflight',
]


def now() -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True, check=check)


def flags(path: Path) -> str:
    if not path.exists():
        return 'MISSING'
    cp = run(['/usr/bin/stat', '-f', '%Sf', str(path)], check=False)
    return (cp.stdout or cp.stderr).strip()


def set_flag(path: Path, locked: bool) -> None:
    if not path.exists():
        return
    cmd = ['/usr/bin/chflags', 'uchg' if locked else 'nouchg', str(path)]
    cp = run(cmd, check=False)
    if cp.returncode != 0:
        raise RuntimeError(f"chflags failed for {path}: {cp.stderr or cp.stdout}")


def stable_paths() -> list[Path]:
    return [root / name for root in PUBLIC_ROOTS for name in STABLE_FILES]


def validate_stable_cockpit_text(text: str, marker: str | None = None, source: str = 'text') -> dict:
    """Validate the stable-route rich cockpit contract against HTML text.

    This is intentionally stricter than packet/detail page validation. The stable
    route is the rich Baseline operator board; small packet pages may exist only
    under timestamped detail paths and must fail this contract.
    """
    checks = {
        'doctype_first': text.lstrip().lower().startswith('<!doctype html'),
        'baseline_present': 'THE BASELINE' in text,
        'primitive_present': BASELINE_PRIMITIVE in text,
        'rich_stable_contract_present': all(required in text for required in RICH_REQUIRED_STRINGS),
        'minimum_rich_size': len(text) >= MIN_STABLE_COCKPIT_BYTES,
        'minimum_section_count': text.lower().count('<section') >= MIN_STABLE_SECTION_COUNT,
        'packet_detail_shape_absent': all(bad not in text for bad in PACKET_DETAIL_FORBIDDEN_ON_STABLE_ROUTE),
        'marker_present': (not marker) or (marker in text),
        'bad_strings_absent': all(bad not in text for bad in BAD_STRINGS),
        'stale_approval_absent': all(bad not in text for bad in STALE_APPROVAL_PREFIXES),
    }
    failed = [name for name, ok in checks.items() if not ok]
    return {
        'source': source,
        'bytes': len(text),
        'section_count': text.lower().count('<section'),
        'checks': checks,
        'failed': failed,
        'ok': not failed,
    }


def unlock_all(reason: str) -> None:
    for p in stable_paths():
        set_flag(p, False)
    write_audit('unlock', reason, marker=None)


def write_audit(action: str, reason: str, marker: str | None) -> None:
    audit = ROOT / 'docs/cockpit_single_writer_rootcause_20260704T103016Z/stable_cockpit_guard_audit.jsonl'
    audit.parent.mkdir(parents=True, exist_ok=True)
    record = {
        'action': action,
        'reason': reason,
        'marker': marker,
        'at_utc': now(),
        'pid': os.getpid(),
    }
    with audit.open('a') as f:
        f.write(json.dumps(record, sort_keys=True) + '\n')


def validate_local(marker: str | None) -> dict:
    result: dict[str, object] = {'checked_at_utc': now(), 'files': {}, 'ok': True, 'failed': []}
    for root in PUBLIC_ROOTS:
        cockpit = root / 'live-steering-cockpit.html'
        status = root / 'live-steering-status.json'
        item: dict[str, object] = {'root': str(root), 'exists': cockpit.exists(), 'flags': flags(cockpit)}
        if not cockpit.exists():
            item['ok'] = False
            result['ok'] = False
            result['failed'].append(f'missing cockpit {cockpit}')
        else:
            text = cockpit.read_text(errors='replace')
            validation = validate_stable_cockpit_text(text, marker=marker, source=str(cockpit))
            checks = validation['checks']
            item['size'] = len(text)
            item['checks'] = checks
            if not all(checks.values()):
                item['ok'] = False
                result['ok'] = False
                result['failed'].append(f'contract failed {cockpit}: {[k for k,v in checks.items() if not v]}')
            else:
                item['ok'] = True
        if status.exists() and marker:
            try:
                sj = json.loads(status.read_text(errors='replace'))
                if sj.get('marker') != marker:
                    result['ok'] = False
                    result['failed'].append(f'status marker mismatch {status}: {sj.get("marker")} != {marker}')
            except Exception as exc:
                result['ok'] = False
                result['failed'].append(f'status json parse failed {status}: {exc}')
        result['files'][str(cockpit)] = item
    return result


def write_owner(marker: str, reason: str) -> None:
    payload = {
        'owner': 'stable_cockpit_guard',
        'marker': marker,
        'reason': reason,
        'locked_at_utc': now(),
        'contract': {
            'route': 'live-steering-cockpit.html',
            'must_have': ['THE BASELINE', BASELINE_PRIMITIVE, marker] + RICH_REQUIRED_STRINGS,
            'minimum_bytes': MIN_STABLE_COCKPIT_BYTES,
            'minimum_sections': MIN_STABLE_SECTION_COUNT,
            'must_not_have': BAD_STRINGS + STALE_APPROVAL_PREFIXES + PACKET_DETAIL_FORBIDDEN_ON_STABLE_ROUTE,
            'single_writer_rule': 'Only tools/stable_cockpit_guard.py may intentionally unlock/lock the stable route.',
            'run_specific_monitors': 'Write timestamped/latest monitor pages only; do not write live-steering-cockpit.html.',
        },
    }
    for root in PUBLIC_ROOTS:
        root.mkdir(parents=True, exist_ok=True)
        (root / OWNER).write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n')


def lock(marker: str, reason: str) -> dict:
    # Ensure owner files can be written even if a stale lock exists.
    for root in PUBLIC_ROOTS:
        set_flag(root / OWNER, False)
    write_owner(marker, reason)
    local = validate_local(marker)
    if not local['ok']:
        raise SystemExit(json.dumps({'status': 'HOLD', 'why': 'local contract failed before lock', 'validation': local}, indent=2))
    for p in stable_paths():
        set_flag(p, True)
    write_audit('lock', reason, marker)
    return check(marker=marker, public=False)


def public_probe(marker: str | None) -> dict:
    req = urllib.request.Request(PUBLIC_URL, headers={'User-Agent': 'NebulaMind stable cockpit guard', 'Cache-Control': 'no-cache'})
    with urllib.request.urlopen(req, timeout=25) as resp:
        text = resp.read().decode('utf-8', 'replace')
        status = resp.status
    validation = validate_stable_cockpit_text(text, marker=marker, source=PUBLIC_URL)
    checks = {'http_200': 200 <= status < 300, **validation['checks']}
    return {'url': PUBLIC_URL, 'http_status': status, 'bytes': len(text), 'checks': checks, 'ok': all(checks.values())}


def known_private_autopilot_non_writer(line: str) -> bool:
    """Exclude the private controller/log pipe from stable-route writer alerts."""
    controller_log = '/Users/duhokim/HermesOps/cockpit/ge-autopilot-controller.log'
    if controller_log not in line:
        return False
    controller = 'galaxy_evolution_autopilot.py watch' in line
    log_pipe = f'tee -a {controller_log}' in line
    stable_route = any(
        marker in line
        for marker in ('live-steering-cockpit', 'agent-reports', 'stable-cockpit')
    )
    return (controller or log_pipe) and not stable_route


def known_tmux_server_non_writer(line: str) -> bool:
    """Exclude the long-running tmux SERVER from stale-writer alerts.

    Added 2026-08-05. The ge-mastermind tmux server was launched on 2026-07-28 with
    NEBULAMIND_METHOD{1,2,3}_HANDOFF_ROOT env vars whose values contain
    '.../agent-reports/wiki-method-results/...', so the wide scan regex matches its ps line
    forever and every lock returns HOLD on a process that cannot write anything.

    tmux is a terminal multiplexer: it never writes the stable route itself — a real writer
    appears as its own child process with its own ps line. The exclusion therefore stays
    narrow in two ways: the line must BE the tmux server (executable + `new-session`), and it
    must not name any protected stable-route FILE. If a future tmux invocation ever carries a
    protected filename in its arguments, this returns False and the HOLD stands.
    """
    is_tmux_server = ('/tmux' in line.split()[10] if len(line.split()) > 10 else False) or '/bin/tmux new-session' in line
    if not is_tmux_server:
        return False
    protected_files = (
        'live-steering-cockpit.html',
        'live-steering-status.json',
        'stable-cockpit-canonical.json',
        'stable-cockpit-owner.json',
        'baseline-roadmap.html',
        'baseline-galaxy-current.html',
        '/agent-reports/mobile.html',
    )
    return not any(name in line for name in protected_files)


def known_ge_mastermind_method_workspace_non_writer(line: str) -> bool:
    """Exclude the coordinator whose env only points at method workspace roots."""
    coordinator = all(
        marker in line
        for marker in (
            'tmux new-session',
            '-s ge-mastermind',
            'NEBULAMIND_MASTER_ROOT=',
            'claude',
        )
    )
    if not coordinator:
        return False
    protected_target = any(
        marker in line
        for marker in (
            'live-steering-cockpit',
            'live-steering-status',
            'stable-cockpit-canonical',
            'stable-cockpit-owner',
            'baseline-roadmap',
            'baseline-galaxy-current',
            '/agent-reports/mobile.html',
        )
    )
    return not protected_target


def process_scan() -> str:
    cp = subprocess.run(
        "ps aux | /usr/bin/grep -E 'galaxy_autonomous_quintet_watchdog|claim_layer_reconciliation_watchdog|live-steering-cockpit|agent-reports|cockpit' | /usr/bin/grep -v grep || true",
        shell=True,
        text=True,
        capture_output=True,
        timeout=20,
    )
    lines = []
    for line in cp.stdout.splitlines():
        # Do not count this guard/check command or its shell wrapper as a stale writer.
        if 'stable_cockpit_guard.py' in line or 'hermes-snap' in line:
            continue
        if known_private_autopilot_non_writer(line):
            continue
        if known_tmux_server_non_writer(line):
            continue
        if known_ge_mastermind_method_workspace_non_writer(line):
            continue
        lines.append(line)
    return '\n'.join(lines).strip()


def check(marker: str | None = None, public: bool = True) -> dict:
    local = validate_local(marker)
    locked = {str(p): flags(p) for p in stable_paths() if p.exists()}
    result: dict[str, object] = {
        'status': 'PASS',
        'checked_at_utc': now(),
        'local': local,
        'flags': locked,
        'stale_writer_processes': process_scan(),
    }
    if any('uchg' not in f.split(',') and f != 'MISSING' for f in locked.values()):
        result['status'] = 'HOLD'
        result['lock_failure'] = {p: f for p, f in locked.items() if 'uchg' not in f.split(',')}
    if not local['ok']:
        result['status'] = 'HOLD'
    if result['stale_writer_processes']:
        result['status'] = 'HOLD'
    if public:
        pub = public_probe(marker)
        result['public'] = pub
        if not pub['ok']:
            result['status'] = 'HOLD'
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('lock')
    p.add_argument('--marker', required=True)
    p.add_argument('--reason', required=True)
    p = sub.add_parser('unlock')
    p.add_argument('--reason', required=True)
    p = sub.add_parser('check')
    p.add_argument('--marker')
    args = ap.parse_args()
    if args.cmd == 'unlock':
        unlock_all(args.reason)
        print(json.dumps({'status': 'UNLOCKED', 'reason': args.reason, 'at_utc': now()}, indent=2, sort_keys=True))
        return 0
    if args.cmd == 'lock':
        result = lock(args.marker, args.reason)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0 if result['status'] == 'PASS' else 2
    if args.cmd == 'check':
        result = check(args.marker)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0 if result['status'] == 'PASS' else 2
    return 2


if __name__ == '__main__':
    raise SystemExit(main())

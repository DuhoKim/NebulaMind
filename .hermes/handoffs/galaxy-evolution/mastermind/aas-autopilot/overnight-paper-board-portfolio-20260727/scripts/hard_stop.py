#!/usr/bin/env python3
"""Fail-closed 10:00 KST hard stop for the approved overnight Paper Board run."""
from __future__ import annotations

import datetime as dt
import json
import os
import signal
import subprocess
from pathlib import Path

ROOT = Path('/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-paper-board-portfolio-20260727')
HANDLES = ROOT / 'RUNTIME_HANDLES.json'
STOP = ROOT / 'GLOBAL_STOP_OVERNIGHT_PB_20260727.md'
RECEIPT = ROOT / 'HARD_STOP_RECEIPT.json'


def command_for(pid: int) -> str:
    result = subprocess.run(['ps', '-p', str(pid), '-o', 'command='], text=True, capture_output=True)
    return result.stdout.strip()


def main() -> None:
    now = dt.datetime.now().astimezone()
    STOP.write_text(
        '# Global Stop — Overnight Paper Board Portfolio\n\n'
        f'Hard stop asserted at {now.isoformat()}. No substantive work or publication may start or continue. '
        'Only deterministic receipt finalization is allowed.\n'
    )
    actions = []
    handles = json.loads(HANDLES.read_text()) if HANDLES.exists() else {}
    for lane in handles.get('processes', []):
        pid = int(lane['pid'])
        cmd = command_for(pid)
        safe_match = str(ROOT) in cmd or any(token in cmd for token in ('claude -p --model fable', 'codex -m gpt-5.5'))
        if cmd and safe_match:
            try:
                os.kill(pid, signal.SIGTERM)
                actions.append({'lane': lane['lane'], 'pid': pid, 'action': 'SIGTERM', 'command': cmd})
            except ProcessLookupError:
                actions.append({'lane': lane['lane'], 'pid': pid, 'action': 'already_exited'})
        else:
            actions.append({'lane': lane['lane'], 'pid': pid, 'action': 'skip_not_running_or_identity_mismatch', 'command': cmd})

    # Shared Goru pane is interrupted only when P2 has no receipt and the current pane tail still contains this run marker.
    p2_receipt = ROOT / 'packets/P2-fesc/goru/RECEIPT.json'
    pane = handles.get('goru_pane')
    if pane and not p2_receipt.exists():
        cap = subprocess.run(['/opt/homebrew/bin/tmux', 'capture-pane', '-p', '-t', pane, '-S', '-120'], text=True, capture_output=True).stdout
        if 'P2 fesc Lineage and Citation Census' in cap or 'P2_GORU_PRIMARY' in cap:
            subprocess.run(['/opt/homebrew/bin/tmux', 'send-keys', '-t', pane, 'Escape'])
            actions.append({'lane': 'p2_goru', 'pane': pane, 'action': 'Escape_run_tag_matched'})
        else:
            actions.append({'lane': 'p2_goru', 'pane': pane, 'action': 'skip_shared_pane_tag_not_matched'})

    data = {'asserted_at': now.isoformat(), 'hard_stop': '2026-07-28T10:00:00+09:00', 'actions': actions, 'marker': 'OVERNIGHT_PB_HARD_STOP_ASSERTED_20260728T1000KST'}
    RECEIPT.write_text(json.dumps(data, indent=2) + '\n')
    with (ROOT / 'OVERNIGHT_LEDGER.md').open('a') as handle:
        handle.write(f'| {now.strftime("%Y-%m-%d %H:%M:%S")} | Hard stop asserted | OVERNIGHT_PB_HARD_STOP_ASSERTED_20260728T1000KST |\n')
    print('OVERNIGHT_PB_HARD_STOP_ASSERTED_20260728T1000KST')


if __name__ == '__main__':
    main()

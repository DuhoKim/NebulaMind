#!/usr/bin/env python3
"""Keep the Galaxy Evolution prose/evidence/trust deepening order active until the requested two-hour window.

Bounded to tmux prompts, working-repo static/docs paths, and .hermes progress snapshots.
No live-root writes, restart/deploy, product DB/API/page_versions publish, git, browser, cloud, secrets, cron.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import pathlib
import subprocess
import textwrap
import time

ROOT = pathlib.Path('/Users/duhokim/NebulaMind/NebulaMind')
HANDOFF = ROOT / '.hermes/handoffs/galaxy-evolution'
PUBLIC = ROOT / 'frontend/public/agent-reports/wiki-method-results/galaxy-evolution'
MARKER = 'AUTOPILOT_PROSE_EVIDENCE_TRUST_DEEPENING_20260708T043427Z'
SEED = 'DEEPENING_RESOURCE_SEED_20260708T043427Z'
DEADLINE = dt.datetime.fromisoformat('2026-07-08T06:34:40+00:00')
INTERVAL_SECONDS = 12 * 60

PANES = {
    '%107': ('Hwao-director', 'director'),
    '%64': ('Hwao-m1', 'm1-author'),
    '%97': ('Hwao-m2', 'm2-author'),
    '%102': ('Hwao-m3', 'm3-author'),
    '%66': ('Goru-m1', 'm1-audit'),
    '%70': ('Kun-m1', 'm1-build-verify'),
    '%99': ('Goru-m2', 'm2-audit'),
    '%100': ('Kun-m2', 'm2-build-verify'),
    '%104': ('Goru-m3', 'm3-audit'),
    '%105': ('Kun-m3', 'm3-build-verify'),
    '%65': ('Lana-m1', 'm1-prose-review'),
    # Lana-m2 pane was observed dead/stale; do not rely on it.
    '%103': ('Lana-m3', 'm3-prose-review'),
}

METHODS = {
    'M1': ('packet-gated-paper-to-wiki-reconciliation', 'method1'),
    'M2': ('source-first-paper-adjudication', 'method2'),
    'M3': ('debate-map-to-wiki-rebuild', 'method3'),
}

COMMON = f"""Parent marker: {MARKER}
Seed marker: {SEED}
Earliest finalization: 2026-07-08T06:34:40Z. Do NOT write the final no-apply packet before then; write progress/candidate/review artifacts instead.
User correction: keep this running for a couple of hours, not a quick first pass.
Boundaries: additive working-repo static/docs under prose-evidence-trust-deepening-20260708T043427Z/ plus .hermes reports only. Do NOT touch NebulaMind-origin-main-live, do NOT mirror live, do NOT restart/deploy, do NOT call /api/pages/page_versions/product DB/SQL, no git, browser, cloud/OAuth/secrets, cron. Stop on hard gate.
""".strip()


def sh(cmd: list[str], timeout: int = 20) -> str:
    try:
        return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout).stdout
    except Exception as e:
        return f'ERROR: {type(e).__name__}: {e}'


def pane_tail(pane: str, lines: int = 35) -> str:
    return sh(['tmux', 'capture-pane', '-J', '-pt', pane, '-S', f'-{lines}'], timeout=10)


def is_busy(tail: str) -> bool:
    busy_words = [
        'Working (', 'Thinking', 'Synthesizing', 'Deciphering', 'Contemplating', 'Beboppin',
        'Doodling', 'Grooving', 'Photosynthesizing', 'Metamorphosing', 'Running in the background',
        'Waiting…', 'Do you want to proceed?', 'Requesting permission', 'esc to interrupt',
    ]
    return any(w in tail for w in busy_words)


def send_prompt(pane: str, prompt: str) -> bool:
    tail = pane_tail(pane)
    if is_busy(tail):
        return False
    tmp = pathlib.Path('/tmp') / f'deepening_sustain_{pane.replace("%", "")}.txt'
    tmp.write_text(prompt.strip() + '\n', encoding='utf-8')
    sh(['tmux', 'send-keys', '-t', pane, 'Escape'], timeout=5)
    sh(['tmux', 'send-keys', '-t', pane, 'C-u'], timeout=5)
    sh(['tmux', 'load-buffer', '-b', f'deep_sustain_{pane}', str(tmp)], timeout=5)
    sh(['tmux', 'paste-buffer', '-b', f'deep_sustain_{pane}', '-t', pane], timeout=5)
    sh(['tmux', 'send-keys', '-t', pane, 'Enter'], timeout=5)
    return True


def method_dir(method: str) -> pathlib.Path:
    return PUBLIC / METHODS[method][0] / 'prose-evidence-trust-deepening-20260708T043427Z'


def snapshot(cycle: int, seeded: list[str]) -> pathlib.Path:
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    lines = [
        f'# Deepening sustainer progress snapshot — cycle {cycle}',
        '',
        f'Marker: `{MARKER}`',
        f'Seed marker: `{SEED}`',
        f'UTC: `{now.strftime("%Y-%m-%dT%H:%M:%SZ")}`',
        f'Earliest finalization: `2026-07-08T06:34:40Z`',
        '',
        '## Candidate directories',
        '',
    ]
    for m, (subdir, handoff_name) in METHODS.items():
        d = method_dir(m)
        files = []
        if d.exists():
            for p in sorted(d.iterdir()):
                if p.is_file():
                    files.append(f'- `{p.name}` — {p.stat().st_size} B')
        lines += [f'### {m}', f'Path: `{d}`', f'Exists: `{d.exists()}`'] + (files or ['- No files yet']) + ['']
    reports = sorted(HANDOFF.rglob('*DEEPENING*20260708T043427Z*.md'), key=lambda p: p.stat().st_mtime, reverse=True)
    lines += ['## Recent deepening reports', '']
    for p in reports[:30]:
        rel = p.relative_to(ROOT)
        ts = dt.datetime.fromtimestamp(p.stat().st_mtime).strftime('%H:%M:%S')
        lines.append(f'- `{ts}` `{rel}` — {p.stat().st_size} B')
    lines += ['', '## Prompts seeded this cycle', '']
    lines += [f'- {x}' for x in seeded] or ['- None; panes were busy or waiting safely.']
    lines += ['', '## Safety ledger', '', 'No live-root writes/copies, no restart/deploy, no DB/API/page_versions/product-wiki publish, no git, no browser/cloud/secrets/cron.']
    out = HANDOFF / 'mastermind/autopilot' / f'DEEPENING_SUSTAINER_PROGRESS_CYCLE_{cycle:02d}_20260708T043427Z.md'
    out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return out


def prompt_for(role: str, cycle: int) -> str:
    if role == 'director':
        return f"""Hwao-director sustaining prompt — cycle {cycle}.
{COMMON}
Do not finalize. Inspect current deepening artifacts and write/update a progress snapshot only. Keep lanes active and list remaining useful work. Target report:
{HANDOFF}/mastermind/autopilot/DEEPENING_HWAO_DIRECTOR_CYCLE_{cycle:02d}_20260708T043427Z.md
"""
    if role.endswith('author'):
        method = role.split('-')[0].upper()
        subdir = METHODS[method][0]
        focus = {
            'M1': '2929 caution, distinct-paper wording, 3/30 and 27-unbound honesty, no invented data',
            'M2': '28060 no-target caution, 22-vs-21 explanation, cite-unmatched readability, source-first trust prose',
            'M3': 'debate-map trust legend, docs-only/P3-closed framing, unmatched/PENDING_RECHECK visibility',
        }[method]
        return f"""Hwao {method} sustaining author prompt — cycle {cycle}.
{COMMON}
Continue/deepen the additive {method} candidate under `{PUBLIC/subdir/'prose-evidence-trust-deepening-20260708T043427Z'}`. Focus: {focus}. If the v2 files exist, improve or append a clearly versioned review/patch note rather than finalizing. Write a cycle receipt under `{HANDOFF/METHODS[method][1]/'autopilot'}` with marker and current file sizes.
"""
    if 'audit' in role:
        method = role.split('-')[0].upper()
        return f"""Goru/Gemini {method} sustaining audit prompt — cycle {cycle}.
{COMMON}
Run mechanical read-only checks on current {method} deepening files if present: file sizes, links, static-safety, no-invent IDs, stale literal scans, and method-specific counts. If absent, report that and the expected path. Write:
{HANDOFF/METHODS[method][1]/'autopilot'/f'DEEPENING_GORU_{method}_CYCLE_{cycle:02d}_AUDIT_20260708T043427Z.md'}
"""
    if 'build-verify' in role:
        method = role.split('-')[0].upper()
        return f"""Kun/Codex {method} sustaining build/verify prompt — cycle {cycle}.
{COMMON}
If the {method} deepening candidate exists, validate HTML/JSON/checksums and propose one safe additive prose improvement. If it does not exist, generate the additive deterministic candidate from first-pass files. Do not finalize. Write:
{HANDOFF/METHODS[method][1]/'autopilot'/f'DEEPENING_KUN_{method}_CYCLE_{cycle:02d}_BUILD_VERIFY_20260708T043427Z.md'}
"""
    if 'prose-review' in role:
        method = role.split('-')[0].upper()
        return f"""Lana {method} sustaining prose/no-overclaim review prompt — cycle {cycle}.
{COMMON}
Review current {method} deepening candidate if present; otherwise review remaining first-pass gaps as acceptance criteria. Judge current mtimes/sizes only. No edits. Write:
{HANDOFF/METHODS[method][1]/'autopilot'/f'DEEPENING_LANA_{method}_CYCLE_{cycle:02d}_REVIEW_20260708T043427Z.md'}
"""
    return COMMON


def main() -> None:
    (HANDOFF / 'mastermind/autopilot').mkdir(parents=True, exist_ok=True)
    cycle = 0
    while dt.datetime.now(dt.timezone.utc) < DEADLINE:
        cycle += 1
        seeded = []
        for pane, (name, role) in PANES.items():
            prompt = prompt_for(role, cycle)
            ok = send_prompt(pane, prompt)
            if ok:
                seeded.append(f'{pane} {name} ({role})')
        out = snapshot(cycle, seeded)
        print(f'cycle {cycle} snapshot {out}', flush=True)
        remaining = (DEADLINE - dt.datetime.now(dt.timezone.utc)).total_seconds()
        if remaining <= 0:
            break
        time.sleep(min(INTERVAL_SECONDS, max(30, remaining)))
    final = HANDOFF / 'mastermind/autopilot/DEEPENING_SUSTAINER_WINDOW_COMPLETE_20260708T043427Z.md'
    final.write_text(
        f'# Deepening sustainer window complete\n\nMarker: `{MARKER}`\nUTC: `{dt.datetime.now(dt.timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")}`\n\nThe requested couple-hour sustainer reached/passed the earliest finalization window. Hwao may now write the final no-apply packet after fresh verification.\n',
        encoding='utf-8',
    )
    print(f'window complete {final}', flush=True)


if __name__ == '__main__':
    main()

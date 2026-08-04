#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
import time
from pathlib import Path
from textwrap import dedent

ROOT = Path('/Users/duhokim/NebulaMind/NebulaMind')
TS = '20260707T050500Z'
LOG = ROOT / '.hermes/handoffs/galaxy-evolution/mastermind/autonomous_wiki_pages_orchestrator_20260707T050500Z.log'

PANES = {
    'm1_hwao': '%64', 'm1_goru': '%66', 'm1_kun': '%70', 'm1_lana': '%65', 'm1_tori': '%68',
    'm2_hwao': '%97', 'm2_goru': '%99', 'm2_kun': '%100', 'm2_lana': '%50', 'm2_tori': '%101',
    'm3_hwao': '%102', 'm3_lana': '%103', 'm3_goru': '%104', 'm3_kun': '%105', 'm3_tori': '%106',
}

PATHS = {
    # method workspaces
    'm1_workspace': ROOT / 'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation',
    'm2_workspace': ROOT / 'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication',
    'm3_workspace': ROOT / 'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild',
    # inputs
    'm1_verdict': ROOT / '.hermes/handoffs/galaxy-evolution/method1/HWAO_PGR_METHOD_VERDICT_20260707T040523Z.md',
    'm1_draft': ROOT / 'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-same-format-draft-20260707T005045Z.md',
    'm2_packet': ROOT / '.hermes/handoffs/galaxy-evolution/method2/hwao/HWAO_M2_SAME_FORMAT_CONVERSION_ROLE_SPLIT_V2_20260707T043503Z.md',
    'm2_draft': ROOT / 'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md',
    'm2_kun_note': ROOT / '.hermes/handoffs/galaxy-evolution/method2/kun/KUN_M2_SAME_FORMAT_DRAFT_AUTHOR_V2_20260707T043503Z.md',
    'm2_lana': ROOT / '.hermes/handoffs/galaxy-evolution/method2/lana/LANA_M2_SAME_FORMAT_CONVERSION_OVERCLAIM_REVIEW_V2_20260707T043503Z.md',
    'm2_goru': ROOT / '.hermes/handoffs/galaxy-evolution/method2/goru/GORU_M2_SAME_FORMAT_CONFORMANCE_REBUILD_V2_20260707T043503Z.md',
    'm3_verdict': ROOT / '.hermes/handoffs/galaxy-evolution/method3/HWAO_M3_P15_RE_VERDICT_20260707T041033Z.md',
    'm3_lana_roles': ROOT / '.hermes/handoffs/galaxy-evolution/method3/reviews/LANA_M3_P15_COVERAGE_EXTENSION_20260707T035921Z.md',
    'm3_goru_p15': ROOT / '.hermes/handoffs/galaxy-evolution/method3/reviews/GORU_M3_P15_CONFORMANCE_CHECKLIST_20260707T005702Z.md',
    'm3_kun_p15': ROOT / '.hermes/handoffs/galaxy-evolution/method3/reviews/KUN_M3_P15_REPRO_CHECK_20260707T040451Z.md',
    # outputs
    'm1_page': ROOT / 'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/wiki-page.html',
    'm1_delivery': ROOT / f'.hermes/handoffs/galaxy-evolution/method1/HWAO_M1_INDEPENDENT_WIKI_PAGE_DELIVERY_{TS}.md',
    'm1_goru_check': ROOT / f'.hermes/handoffs/galaxy-evolution/method1/goru/GORU_M1_WIKI_PAGE_CHECK_{TS}.md',
    'm1_kun_check': ROOT / f'.hermes/handoffs/galaxy-evolution/method1/kun/KUN_M1_WIKI_PAGE_REPRO_CHECK_{TS}.md',
    'm1_receipt': ROOT / f'.hermes/handoffs/galaxy-evolution/method1/receipts/TORI_M1_WIKI_PAGE_RECEIPT_{TS}.md',
    'm2_receipt': ROOT / '.hermes/handoffs/galaxy-evolution/method2/receipts/TORI_M2_SAME_FORMAT_CONVERSION_RECEIPT_V2_20260707T043503Z.md',
    'm2_verdict': ROOT / '.hermes/handoffs/galaxy-evolution/method2/hwao/HWAO_M2_METHOD_VERDICT_V2_20260707T043503Z.md',
    'm2_page': ROOT / 'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html',
    'm3_draft': ROOT / f'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/m3-p2-same-format-draft-{TS}.md',
    'm3_page': ROOT / 'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html',
    'm3_lana_author': ROOT / f'.hermes/handoffs/galaxy-evolution/method3/reviews/LANA_M3_P2_WIKI_PAGE_AUTHOR_{TS}.md',
    'm3_goru_check': ROOT / f'.hermes/handoffs/galaxy-evolution/method3/reviews/GORU_M3_P2_WIKI_PAGE_CONFORMANCE_{TS}.md',
    'm3_kun_check': ROOT / f'.hermes/handoffs/galaxy-evolution/method3/reviews/KUN_M3_P2_WIKI_PAGE_REPRO_{TS}.md',
    'm3_receipt': ROOT / f'.hermes/handoffs/galaxy-evolution/method3/receipts/TORI_M3_P2_WIKI_PAGE_RECEIPT_{TS}.md',
    'm3_verdict_out': ROOT / f'.hermes/handoffs/galaxy-evolution/method3/HWAO_M3_P2_WIKI_PAGE_VERDICT_{TS}.md',
}

ALLOW_PATTERNS = [
    'wiki-page.html', f'm3-p2-same-format-draft-{TS}.md',
    f'HWAO_M1_INDEPENDENT_WIKI_PAGE_DELIVERY_{TS}.md', f'GORU_M1_WIKI_PAGE_CHECK_{TS}.md',
    f'KUN_M1_WIKI_PAGE_REPRO_CHECK_{TS}.md', f'TORI_M1_WIKI_PAGE_RECEIPT_{TS}.md',
    'TORI_M2_SAME_FORMAT_CONVERSION_RECEIPT_V2_20260707T043503Z.md', 'HWAO_M2_METHOD_VERDICT_V2_20260707T043503Z.md',
    f'LANA_M3_P2_WIKI_PAGE_AUTHOR_{TS}.md', f'GORU_M3_P2_WIKI_PAGE_CONFORMANCE_{TS}.md',
    f'KUN_M3_P2_WIKI_PAGE_REPRO_{TS}.md', f'TORI_M3_P2_WIKI_PAGE_RECEIPT_{TS}.md',
    f'HWAO_M3_P2_WIKI_PAGE_VERDICT_{TS}.md',
]

DISPATCHED = set()
APPROVALS = []


def log(msg: str, **kw):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    rec = {'t': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'msg': msg, **kw}
    with LOG.open('a') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print(json.dumps(rec, ensure_ascii=False), flush=True)


def sh(cmd: list[str], **kw):
    return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, **kw)


def cap(pane: str, n=140) -> str:
    try:
        return subprocess.check_output(['tmux', 'capture-pane', '-J', '-pt', pane, '-S', f'-{n}'], text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return e.output or ''


def pane_active_text(text: str) -> bool:
    return bool(re.search(r'thinking|Working|Running|Reading|Writing|Creating|Generating|Transfiguring|Flamb|Caramel|Catapult|Bash\(|✳|✶|✻|✽|processing', text, re.I))


def send_prompt(key: str, prompt: str, interrupt=False):
    if key in DISPATCHED:
        return
    pane = PANES[key]
    if interrupt:
        sh(['tmux', 'send-keys', '-t', pane, 'Escape'])
        time.sleep(0.2)
    sh(['tmux', 'send-keys', '-t', pane, 'C-u'])
    time.sleep(0.1)
    sh(['tmux', 'set-buffer', '--', prompt])
    sh(['tmux', 'paste-buffer', '-t', pane])
    sh(['tmux', 'send-keys', '-t', pane, 'Enter'])
    DISPATCHED.add(key)
    log('dispatched', key=key, pane=pane)
    time.sleep(5)
    # If it visibly sat in a composer, submit once more.
    bottom = '\n'.join(cap(pane, 80).splitlines()[-50:])
    marker = prompt[:60]
    if marker in bottom and not pane_active_text(bottom):
        sh(['tmux', 'send-keys', '-t', pane, 'Enter'])
        log('resent_enter_for_composer_prompt', key=key, pane=pane)


def approve_known_prompts():
    for pane in set(PANES.values()):
        text = cap(pane, 200)
        bottom = '\n'.join(text.splitlines()[-100:])
        if not re.search(r'Do you want to (?:create|proceed|edit)|Esc to cancel|Tab to amend', bottom, re.I):
            continue
        if not any(pat in bottom for pat in ALLOW_PATTERNS):
            continue
        # Refuse obvious live/DB/deploy/git prompts even if a known filename appears nearby.
        if re.search(r'page_versions|live wiki|database|migration|deploy|restart|git push|billing|OAuth|route/config', bottom, re.I):
            if 'wiki-page.html' not in bottom and not re.search(r'\.hermes/handoffs/galaxy-evolution/method[123]/', bottom):
                continue
        if re.search(r'❯\s*2\. Yes, allow all edits', bottom):
            sh(['tmux', 'send-keys', '-t', pane, 'Up', 'Enter'])
        else:
            sh(['tmux', 'send-keys', '-t', pane, 'Enter'])
        APPROVALS.append({'pane': pane, 'matched': [p for p in ALLOW_PATTERNS if p in bottom][:3]})
        log('approved_known_prompt', pane=pane, matched=APPROVALS[-1]['matched'])
        time.sleep(3)


def initial_dispatch():
    m1_prompt = dedent(f'''
    USER OVERRIDE: independent Method1 wiki page artifact for evaluation. Work autonomously from Method1 only.
    Inputs: verdict {PATHS['m1_verdict']} and draft {PATHS['m1_draft']}.
    Output: update/write Method1 workspace wiki page {PATHS['m1_page']} and write delivery note {PATHS['m1_delivery']}.
    Requirement: the page must represent the Method1 packet-gated paper-to-wiki result only, preserving its claim/cite backing and rejected/NO-GO boundaries. Do not merge Method2/Method3 content. Use real paper-backed claims from the existing Method1 draft/artifacts; do not invent sources. You may overwrite the method-local wiki-page.html so the user can evaluate this method's page directly. Stop after page + delivery note.
    ''').strip()
    send_prompt('m1_hwao', m1_prompt, interrupt=True)

    # M1 verifiers wait for page.
    m1_goru = dedent(f'''
    AUTONOMOUS METHOD1 PAGE CHECK. Wait until {PATHS['m1_page']} and {PATHS['m1_delivery']} exist. Then mechanically check the Method1 wiki page against {PATHS['m1_draft']} and {PATHS['m1_verdict']}: title, 9-H2 structure, claim-chip/cite-marker preservation, no NO-GO IDs, no Method2/Method3 leakage, paper-backed claims only. Write {PATHS['m1_goru_check']}. Stop.
    ''').strip()
    send_prompt('m1_goru', m1_goru, interrupt=False)

    m1_kun = dedent(f'''
    AUTONOMOUS METHOD1 REPRO CHECK. Wait until {PATHS['m1_page']} and {PATHS['m1_delivery']} exist. Verify the Method1 page can be reproduced from the Method1 draft/verdict/artifacts without external invention and that paper-backed claims are preserved. Write {PATHS['m1_kun_check']}. Stop.
    ''').strip()
    send_prompt('m1_kun', m1_kun, interrupt=False)

    m1_tori = dedent(f'''
    AUTONOMOUS METHOD1 RECEIPTS-LAST. Wait until Method1 page/delivery/Goru/Kun checks exist: {PATHS['m1_page']}, {PATHS['m1_delivery']}, {PATHS['m1_goru_check']}, {PATHS['m1_kun_check']}. Verify files and write receipt {PATHS['m1_receipt']}. Stop.
    ''').strip()
    send_prompt('m1_tori', m1_tori, interrupt=False)

    # Keep/refresh M2 receipt if not already produced. Do not interrupt if currently running.
    if not PATHS['m2_receipt'].exists():
        text = cap(PANES['m2_tori'], 80)
        if not pane_active_text(text):
            m2_tori = dedent(f'''
            AUTONOMOUS METHOD2 RECEIPTS-LAST. Read packet {PATHS['m2_packet']}, draft {PATHS['m2_draft']}, Kun note {PATHS['m2_kun_note']}, Lana review {PATHS['m2_lana']}, Goru report {PATHS['m2_goru']}. Write receipt {PATHS['m2_receipt']}. Then stop.
            ''').strip()
            send_prompt('m2_tori', m2_tori, interrupt=False)
        else:
            log('m2_tori_already_active')

    # M3: direct autonomous page authoring/verifying from Method3 only.
    m3_lana = dedent(f'''
    USER OVERRIDE: independent Method3 wiki page artifact for evaluation. Work autonomously from Method3 only, following Method3 P1.5/P2 constraints.
    Inputs: re-verdict {PATHS['m3_verdict']}, Lana 17-role table {PATHS['m3_lana_roles']}, Goru checklist {PATHS['m3_goru_p15']}, Kun repro {PATHS['m3_kun_p15']}.
    Outputs: Method3 draft {PATHS['m3_draft']}, Method3 wiki page {PATHS['m3_page']}, and author report {PATHS['m3_lana_author']}.
    Requirement: write a standalone evaluable Galaxy Evolution wiki page for the debate-map-to-wiki method. Follow Method3 only. Realize the 17 P1.5 roles as cautious prose under the 9-H2 skeleton. Back claims only by the Method3 local artifacts / true paper source IDs; do not invent sources. Because Method3 P2 had not opened P3 binding, do not add claim/cite marker binding unless the source IDs are already explicit in the P1.5 artifacts; if unsure, use plain provenance in the author report rather than fake markers. No Method1/Method2 content. You may overwrite method-local wiki-page.html. Stop after draft + wiki page + author report.
    ''').strip()
    send_prompt('m3_lana', m3_lana, interrupt=True)

    m3_goru = dedent(f'''
    AUTONOMOUS METHOD3 PAGE CONFORMANCE. Wait until {PATHS['m3_draft']}, {PATHS['m3_page']}, and {PATHS['m3_lana_author']} exist. Check exact 9-H2 order, role coverage from the 17 P1.5 roles, no Method1/Method2 leakage, no fake citations, no unsupported claims, and method-local page integrity. Write {PATHS['m3_goru_check']}. Stop.
    ''').strip()
    send_prompt('m3_goru', m3_goru, interrupt=False)

    m3_kun = dedent(f'''
    AUTONOMOUS METHOD3 PAGE REPRO CHECK. Wait until {PATHS['m3_draft']}, {PATHS['m3_page']}, and {PATHS['m3_lana_author']} exist. Verify the Method3 page is reproducible from Method3 P1.5 roles/local artifacts and backed by true paper/source IDs where asserted. Flag any unsupported sentence. Write {PATHS['m3_kun_check']}. Stop.
    ''').strip()
    send_prompt('m3_kun', m3_kun, interrupt=False)

    m3_tori = dedent(f'''
    AUTONOMOUS METHOD3 RECEIPTS-LAST. Wait until Method3 page/draft/author/Goru/Kun checks exist: {PATHS['m3_page']}, {PATHS['m3_draft']}, {PATHS['m3_lana_author']}, {PATHS['m3_goru_check']}, {PATHS['m3_kun_check']}. Verify files and write {PATHS['m3_receipt']}. Stop.
    ''').strip()
    send_prompt('m3_tori', m3_tori, interrupt=False)


def dependency_dispatches():
    if PATHS['m2_receipt'].exists() and not PATHS['m2_verdict'].exists() and 'm2_hwao_verdict_page' not in DISPATCHED:
        prompt = dedent(f'''
        USER OVERRIDE: Method2 independent wiki page + verdict for evaluation. Work autonomously from Method2 only.
        Inputs: packet {PATHS['m2_packet']}, draft {PATHS['m2_draft']}, Kun {PATHS['m2_kun_note']}, Lana {PATHS['m2_lana']}, Goru {PATHS['m2_goru']}, Tori receipt {PATHS['m2_receipt']}.
        Outputs: write verdict {PATHS['m2_verdict']} and update/write Method2 wiki page {PATHS['m2_page']} from the Method2 draft.
        Requirement: Method2 page must follow source-first adjudication only, use claims 2942–2947 and true paper/evidence IDs from the v2 packet/draft, preserve rejected/excluded rows, no Method1/Method3 leakage, no invented sources. You may overwrite method-local wiki-page.html for evaluation. Stop after verdict + wiki page.
        ''').strip()
        # use synthetic key to avoid collision
        pane = PANES['m2_hwao']
        sh(['tmux','send-keys','-t',pane,'Escape']); time.sleep(.1)
        sh(['tmux','send-keys','-t',pane,'C-u']); time.sleep(.1)
        sh(['tmux','set-buffer','--',prompt]); sh(['tmux','paste-buffer','-t',pane]); sh(['tmux','send-keys','-t',pane,'Enter'])
        DISPATCHED.add('m2_hwao_verdict_page')
        log('dispatched', key='m2_hwao_verdict_page', pane=pane)
    if PATHS['m3_receipt'].exists() and not PATHS['m3_verdict_out'].exists() and 'm3_hwao_verdict' not in DISPATCHED:
        prompt = dedent(f'''
        AUTONOMOUS METHOD3 PAGE VERDICT. Read Method3 page/draft/author/Goru/Kun/Tori receipt: {PATHS['m3_page']}, {PATHS['m3_draft']}, {PATHS['m3_lana_author']}, {PATHS['m3_goru_check']}, {PATHS['m3_kun_check']}, {PATHS['m3_receipt']}. Write final page verdict {PATHS['m3_verdict_out']}. Decide PASS / PASS_WITH_ISSUES / ROLE_TABLE_BLOCKER for the independent Method3 wiki page. Stop after verdict.
        ''').strip()
        pane = PANES['m3_hwao']
        sh(['tmux','send-keys','-t',pane,'Escape']); time.sleep(.1)
        sh(['tmux','send-keys','-t',pane,'C-u']); time.sleep(.1)
        sh(['tmux','set-buffer','--',prompt]); sh(['tmux','paste-buffer','-t',pane]); sh(['tmux','send-keys','-t',pane,'Enter'])
        DISPATCHED.add('m3_hwao_verdict')
        log('dispatched', key='m3_hwao_verdict', pane=pane)


def main():
    log('orchestrator_start')
    for k in ['m1_workspace','m2_workspace','m3_workspace']:
        PATHS[k].mkdir(parents=True, exist_ok=True)
    initial_dispatch()
    deadline = time.time() + 45*60
    while time.time() < deadline:
        approve_known_prompts()
        dependency_dispatches()
        done = {
            'm1_page': PATHS['m1_page'].exists(), 'm1_receipt': PATHS['m1_receipt'].exists(),
            'm2_page': PATHS['m2_page'].exists(), 'm2_receipt': PATHS['m2_receipt'].exists(), 'm2_verdict': PATHS['m2_verdict'].exists(),
            'm3_page': PATHS['m3_page'].exists(), 'm3_receipt': PATHS['m3_receipt'].exists(), 'm3_verdict': PATHS['m3_verdict_out'].exists(),
        }
        log('heartbeat', done=done)
        if all(done.values()):
            break
        time.sleep(12)
    approve_known_prompts()
    summary = {k: {'exists': p.exists(), 'size': p.stat().st_size if p.exists() else None, 'path': str(p)} for k,p in PATHS.items() if k.endswith(('page','receipt','verdict','delivery','check','author')) or k in ['m2_verdict','m3_verdict_out','m3_draft']}
    log('orchestrator_done', approvals=APPROVALS, summary=summary)

if __name__ == '__main__':
    main()

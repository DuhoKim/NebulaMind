#!/usr/bin/env python3
from __future__ import annotations

import json, re, subprocess, time
from pathlib import Path
from textwrap import dedent

ROOT = Path('/Users/duhokim/NebulaMind/NebulaMind')
TS = '20260707T050900Z'
OLD_TS = '20260707T050500Z'
LOG = ROOT / f'.hermes/handoffs/galaxy-evolution/mastermind/autonomous_wiki_pages_chain2_{TS}.log'

PANES = {
    'm1_hwao':'%64','m1_goru':'%66','m1_kun':'%70','m1_tori':'%68',
    'm2_hwao':'%97','m2_tori':'%101',
    'm3_hwao':'%102','m3_lana':'%103','m3_goru':'%104','m3_kun':'%105','m3_tori':'%106',
}
P = {
    'm1_draft': ROOT/'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-same-format-draft-20260707T005045Z.md',
    'm1_verdict': ROOT/'.hermes/handoffs/galaxy-evolution/method1/HWAO_PGR_METHOD_VERDICT_20260707T040523Z.md',
    'm1_page': ROOT/'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/wiki-page.html',
    'm1_delivery': ROOT/f'.hermes/handoffs/galaxy-evolution/method1/HWAO_M1_INDEPENDENT_WIKI_PAGE_DELIVERY_{OLD_TS}.md',
    'm1_goru': ROOT/f'.hermes/handoffs/galaxy-evolution/method1/goru/GORU_M1_WIKI_PAGE_CHECK_RERUN_{TS}.md',
    'm1_kun': ROOT/f'.hermes/handoffs/galaxy-evolution/method1/kun/KUN_M1_WIKI_PAGE_REPRO_CHECK_RERUN_{TS}.md',
    'm1_receipt': ROOT/f'.hermes/handoffs/galaxy-evolution/method1/receipts/TORI_M1_WIKI_PAGE_RECEIPT_RERUN_{TS}.md',

    'm2_packet': ROOT/'.hermes/handoffs/galaxy-evolution/method2/hwao/HWAO_M2_SAME_FORMAT_CONVERSION_ROLE_SPLIT_V2_20260707T043503Z.md',
    'm2_draft': ROOT/'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md',
    'm2_receipt': ROOT/'.hermes/handoffs/galaxy-evolution/method2/receipts/TORI_M2_SAME_FORMAT_CONVERSION_RECEIPT_V2_20260707T043503Z.md',
    'm2_verdict': ROOT/'.hermes/handoffs/galaxy-evolution/method2/hwao/HWAO_M2_METHOD_VERDICT_V2_20260707T043503Z.md',
    'm2_page': ROOT/'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html',

    'm3_reverdict': ROOT/'.hermes/handoffs/galaxy-evolution/method3/HWAO_M3_P15_RE_VERDICT_20260707T041033Z.md',
    'm3_roles': ROOT/'.hermes/handoffs/galaxy-evolution/method3/reviews/LANA_M3_P15_COVERAGE_EXTENSION_20260707T035921Z.md',
    'm3_draft': ROOT/f'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/m3-p2-same-format-draft-{OLD_TS}.md',
    'm3_page': ROOT/'frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html',
    'm3_author': ROOT/f'.hermes/handoffs/galaxy-evolution/method3/reviews/LANA_M3_P2_WIKI_PAGE_AUTHOR_{OLD_TS}.md',
    'm3_goru': ROOT/f'.hermes/handoffs/galaxy-evolution/method3/reviews/GORU_M3_P2_WIKI_PAGE_CONFORMANCE_RERUN_{TS}.md',
    'm3_kun': ROOT/f'.hermes/handoffs/galaxy-evolution/method3/reviews/KUN_M3_P2_WIKI_PAGE_REPRO_RERUN_{TS}.md',
    'm3_receipt': ROOT/f'.hermes/handoffs/galaxy-evolution/method3/receipts/TORI_M3_P2_WIKI_PAGE_RECEIPT_RERUN_{TS}.md',
    'm3_verdict': ROOT/f'.hermes/handoffs/galaxy-evolution/method3/HWAO_M3_P2_WIKI_PAGE_VERDICT_RERUN_{TS}.md',
}
ALLOW = [
    'wiki-page.html',
    P['m1_delivery'].name, P['m1_goru'].name, P['m1_kun'].name, P['m1_receipt'].name,
    P['m2_verdict'].name,
    P['m3_draft'].name, P['m3_author'].name, P['m3_goru'].name, P['m3_kun'].name, P['m3_receipt'].name, P['m3_verdict'].name,
]
DISPATCHED=set(); APPROVALS=[]

def log(msg, **kw):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    rec={'t':time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),'msg':msg,**kw}
    with LOG.open('a') as f: f.write(json.dumps(rec, ensure_ascii=False)+'\n')
    print(json.dumps(rec, ensure_ascii=False), flush=True)

def sh(args):
    return subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def cap(pane, n=180):
    try: return subprocess.check_output(['tmux','capture-pane','-J','-pt',pane,'-S',f'-{n}'], text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e: return e.output or ''

def active(txt):
    return bool(re.search(r'thinking|Working|Running|Reading|Writing|Creating|Generating|processing|Bash\(|✳|✶|✻|✽|Computing|Beaming|Twisting|Caramel|Transfig', txt, re.I))

def send(key, prompt):
    if key in DISPATCHED: return
    pane=PANES[key]
    # Clear only idle composer. If active, leave it alone.
    txt=cap(pane,80); bot='\n'.join(txt.splitlines()[-50:])
    if active(bot):
        log('defer_dispatch_active', key=key, pane=pane); return
    sh(['tmux','send-keys','-t',pane,'C-u']); time.sleep(.1)
    sh(['tmux','set-buffer','--',prompt]); sh(['tmux','paste-buffer','-t',pane]); sh(['tmux','send-keys','-t',pane,'Enter'])
    DISPATCHED.add(key); log('dispatched', key=key, pane=pane)

def approve():
    for pane in set(PANES.values()):
        bot='\n'.join(cap(pane,220).splitlines()[-110:])
        if not re.search(r'Do you want to (?:create|edit|overwrite|proceed)|Esc to cancel|Tab to amend', bot, re.I):
            continue
        matched=[a for a in ALLOW if a in bot]
        if not matched: continue
        if re.search(r'❯\s*2\. Yes, allow all edits', bot):
            sh(['tmux','send-keys','-t',pane,'Up','Enter'])
        else:
            sh(['tmux','send-keys','-t',pane,'Enter'])
        APPROVALS.append({'pane':pane,'matched':matched[:4]}); log('approved', pane=pane, matched=matched[:4]); time.sleep(2)

def dispatch_after_authors():
    # M1 verifiers after M1 delivery exists
    if P['m1_delivery'].exists():
        send('m1_goru', dedent(f'''
        RERUN AFTER AUTHOR OUTPUT — METHOD1 PAGE CHECK. Use current Method1 page {P['m1_page']}, delivery {P['m1_delivery']}, draft {P['m1_draft']}, verdict {P['m1_verdict']}. Ignore any earlier waiting/schedule state. Check the independently written Method1 wiki page for: Method1-only content, real paper-backed claims from the Method1 draft/artifacts, claim/cite marker preservation, no NO-GO IDs, 9-H2 structure, no Method2/Method3 leakage. Write exactly {P['m1_goru']}. Stop.
        ''').strip())
        send('m1_kun', dedent(f'''
        RERUN AFTER AUTHOR OUTPUT — METHOD1 REPRO CHECK. Use current Method1 page {P['m1_page']}, delivery {P['m1_delivery']}, draft {P['m1_draft']}, verdict {P['m1_verdict']}. Verify the page is reproducible from Method1 artifacts and uses true paper-backed claims only. Write exactly {P['m1_kun']}. Stop.
        ''').strip())
    if P['m1_goru'].exists() and P['m1_kun'].exists():
        send('m1_tori', dedent(f'''
        METHOD1 RECEIPTS-LAST RERUN. Verify {P['m1_page']}, {P['m1_delivery']}, {P['m1_goru']}, {P['m1_kun']}. Write exactly {P['m1_receipt']}. Stop.
        ''').strip())
    # M2 if Hwao prompt somehow did not run
    if P['m2_receipt'].exists() and not P['m2_verdict'].exists():
        send('m2_hwao', dedent(f'''
        RERUN/CONTINUE — METHOD2 INDEPENDENT WIKI PAGE + VERDICT. Use Method2 packet {P['m2_packet']}, draft {P['m2_draft']}, Tori receipt {P['m2_receipt']}. Write verdict {P['m2_verdict']} and update Method2 page {P['m2_page']} from the draft. Method2-only, claims 2942–2947 only, true paper/evidence IDs only, preserve rejected/excluded rows, no Method1/Method3 leakage. Stop after verdict + page.
        ''').strip())
    # M3 verifiers after Lana author exists
    if P['m3_author'].exists() and P['m3_draft'].exists():
        send('m3_goru', dedent(f'''
        RERUN AFTER AUTHOR OUTPUT — METHOD3 PAGE CONFORMANCE. Prior missing-input report is stale. Use current Method3 draft {P['m3_draft']}, page {P['m3_page']}, author report {P['m3_author']}, re-verdict {P['m3_reverdict']}, roles {P['m3_roles']}. Check exact 9-H2 order, 17-role coverage, Method3-only content, no fake citations, no unsupported claims, true paper/source-ID backing where asserted. Write exactly {P['m3_goru']}. Stop.
        ''').strip())
        send('m3_kun', dedent(f'''
        RERUN AFTER AUTHOR OUTPUT — METHOD3 PAGE REPRO. Prior waiting state is stale. Use Method3 draft {P['m3_draft']}, page {P['m3_page']}, author report {P['m3_author']}, roles {P['m3_roles']}. Verify reproducibility from Method3 local artifacts and true paper/source IDs; flag unsupported sentences. Write exactly {P['m3_kun']}. Stop.
        ''').strip())
    if P['m3_goru'].exists() and P['m3_kun'].exists():
        send('m3_tori', dedent(f'''
        METHOD3 RECEIPTS-LAST RERUN. Verify {P['m3_page']}, {P['m3_draft']}, {P['m3_author']}, {P['m3_goru']}, {P['m3_kun']}. Write exactly {P['m3_receipt']}. Stop.
        ''').strip())
    if P['m3_receipt'].exists():
        send('m3_hwao', dedent(f'''
        METHOD3 FINAL PAGE VERDICT RERUN. Verify Method3 page/draft/author/checks/receipt: {P['m3_page']}, {P['m3_draft']}, {P['m3_author']}, {P['m3_goru']}, {P['m3_kun']}, {P['m3_receipt']}. Write exactly {P['m3_verdict']}. Decide PASS / PASS_WITH_ISSUES / ROLE_TABLE_BLOCKER for the independent Method3 wiki page. Stop.
        ''').strip())

def main():
    log('chain2_start')
    deadline=time.time()+60*60
    done={}
    while time.time()<deadline:
        approve(); dispatch_after_authors()
        done={
            'm1_delivery':P['m1_delivery'].exists(),'m1_goru':P['m1_goru'].exists(),'m1_kun':P['m1_kun'].exists(),'m1_receipt':P['m1_receipt'].exists(),
            'm2_receipt':P['m2_receipt'].exists(),'m2_verdict':P['m2_verdict'].exists(),
            'm3_author':P['m3_author'].exists(),'m3_draft':P['m3_draft'].exists(),'m3_goru':P['m3_goru'].exists(),'m3_kun':P['m3_kun'].exists(),'m3_receipt':P['m3_receipt'].exists(),'m3_verdict':P['m3_verdict'].exists(),
        }
        log('heartbeat', done=done)
        if all(done.values()): break
        time.sleep(15)
    approve(); dispatch_after_authors()
    summary={k:{'exists':v.exists(),'size':v.stat().st_size if v.exists() else None,'path':str(v)} for k,v in P.items() if k in done or k.endswith('page')}
    log('chain2_done', approvals=APPROVALS, summary=summary)

if __name__=='__main__': main()

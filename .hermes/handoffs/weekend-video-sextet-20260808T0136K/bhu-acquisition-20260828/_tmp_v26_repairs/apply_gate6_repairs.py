#!/usr/bin/env python3
"""V30 gate repairs: codex F2 (authoritative full-record branch predicate), F1 (identity conflicts propagated per input), C1 (manifest header wording);
Blanc 03:03 rule: guards are never removed to make a probe killable — the probes test the diagnostic with the guard standing. Tools + kit; text in write_v31."""
import io,re
def rep(t,a,b):
    assert t.count(a)==1,(a[:70],t.count(a)); return t.replace(a,b)
S="r3c2_ledger_tools.py"; s=io.open(S,encoding="utf-8").read()
# F2: authoritative predicate — neither complete branch → unconditional record-level MISMATCH, before any diagnostic; diagnostics only explain
s=rep(s,'''        if matches_primary: branch="primary"
        elif matches_alt: branch="alt"   # PROBE:C6_COMPLETE_BRANCH
        else:''','''        if matches_primary: branch="primary"
        elif matches_alt: branch="alt"
        else:
            diffs.append("record matches neither complete declared branch")  # AUTHORITATIVE: the full-record predicate decides the verdict; the per-field lines below only explain it (Blanc 03:03: never removed to satisfy a probe)''')
# F1: identity conflicts keyed per input, included in that record's diffs and therefore propagated to every dependent selected claim
s=rep(s,'''    for cid0,r0 in RD.items():
        for iid0,ar0 in (r0.get("inputs") or {}).items():
            sr0=full_by.get(iid0)
            if sr0 is not None and str(sr0.get("claim_id"))!=str(cid0): fails.append(f"C6_IDENTITY: {iid0} reconstructed under claim {cid0}, but the sealed record belongs to claim {sr0.get('claim_id')}")  # PROBE:C6_IDENTITY''',
'''    identity_conflict={}
    for cid0,r0 in RD.items():
        for iid0,ar0 in (r0.get("inputs") or {}).items():
            sr0=full_by.get(iid0)
            if sr0 is not None and str(sr0.get("claim_id"))!=str(cid0): identity_conflict[iid0]=f"reconstructed under claim {cid0}, but the sealed record belongs to claim {sr0.get('claim_id')}"; fails.append(f"C6_IDENTITY: {iid0} {identity_conflict[iid0]}")  # PROBE:C6_IDENTITY''')
s=rep(s,'''        d,b=compare_record(iid, ar, sr); record_cmp[iid]=(d,b)''','''        d,b=compare_record(iid, ar, sr)
        if iid in identity_conflict: d=[f"identity: {identity_conflict[iid]}"]+d   # F1: the conflict is a MISMATCH of this record, carried into every dependent selected claim's rows
        record_cmp[iid]=(d,b)''')
io.open(S,"w",encoding="utf-8").write(s)
# C1: manifest header wording (the deferred V29 cosmetic)
mp="R3C2_CORPUS_MANIFEST.md"; m=io.open(mp,encoding="utf-8").read()
m=rep(m,"informational, consumed by no tool) |","informational: summed and reported by the partition tool for per-batch totals, not used as an integrity predicate) |")
io.open(mp,"w",encoding="utf-8").write(m)
# kit: probes that previously required the guard's absence now assert the diagnostic disappears while the verdict stands
T="r3c2_staged_d1d7/r3c2_staged_tests.py"; t=io.open(T,encoding="utf-8").read()
t=rep(t,'probe("gate-2 F2 probe: deleting the edge comparison lets the wrong graph PASS",SEAT,"PROBE:C6_EDGES","audit","compare",*_,W/"edge_p.json",token="C6_AUDIT_SAMPLE=PASS")',
        'probe("gate-2 F2 probe: with the edge DIAGNOSTIC deleted the verdict still FAILS on the authoritative branch predicate (guard retained, Blanc 03:03)",SEAT,"PROBE:C6_EDGES","audit","compare",*_,W/"edge_p.json",token="record matches neither complete declared branch",want_rc=1)')
t=rep(t,'probe("gate-3 F1 probe: deleting the evidence comparison lets the fabricated quotation PASS",SEAT,"PROBE:C6_EVIDENCE","audit","compare",*_,W/"fabev_p.json",token="C6_AUDIT_SAMPLE=PASS")',
        'probe("gate-3 F1 probe: with the evidence DIAGNOSTIC deleted the verdict still FAILS on the authoritative branch predicate (guard retained)",SEAT,"PROBE:C6_EVIDENCE","audit","compare",*_,W/"fabev_p.json",token="record matches neither complete declared branch",want_rc=1)')
t=rep(t,'probe("gate-5 F2 probe: deleting the parent-list comparison (the check that catches a hybrid) lets the hybrid PASS",SEAT,"PROBE:C6_EDGES","audit","compare",*_,W/"hybrid_p.json",token="C6_AUDIT_SAMPLE=PASS")',
        '''probe("gate-5 F2 probe: with the parent DIAGNOSTIC deleted the hybrid still FAILS on the authoritative branch predicate (guard retained)",SEAT,"PROBE:C6_EDGES","audit","compare",*_,W/"hybrid_p.json",token="record matches neither complete declared branch",want_rc=1)
# ---- gate-6 (codex V30 F2): the REVERSE hybrid — alternative origin + alternative evidence with the PRIMARY parents
I1RH={"symbol":"a","origin":"CHOSEN","status":"PRINTED","value":"2","source_file":"paperB.txt","source_line":5,"derived_from":["i2"],"origin_evidence":{"reason_code":"ORIG_CHOICE_STATED","source_file":"paperA.txt","source_line":3,"verbatim":"We adopt a = 2 from paperB (2020)"}}
rc,out,_=full_case("revhybrid",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1RH),"i2":dict(I2),"i3":dict(I3)}}},sl_=sl8); check("gate-6 F2 (codex): the REVERSE hybrid (alternative origin+evidence with the primary parents) is MISMATCH by the authoritative predicate",rc,out,1,["AUDIT c1: MISMATCH (input i1: record matches neither complete declared branch"])''')
# the identity probe: with the global C6_IDENTITY line deleted, the per-record conflict still fails the dependent claim (F1)
t=rep(t,'probe("gate-5 F1 probe: deleting the identity binding lets the mis-keyed record PASS",SEAT,"PROBE:C6_IDENTITY","audit","compare",*_,W/"identity_p.json",token="C6_AUDIT_SAMPLE=PASS")',
        '''probe("gate-5 F1 probe: deleting the identity binding lets the mis-keyed record PASS",SEAT,"PROBE:C6_IDENTITY","audit","compare",*_,W/"identity_p.json",token="C6_AUDIT_SAMPLE=PASS")
c6i=json.loads((W/"identity_C6.json").read_text()); results.append(("gate-6 F1 (codex): the identity conflict is carried into the dependent selected claim's input row and its result is MISMATCH",c6i["audited"]["c1"]["result"]=="MISMATCH" and c6i["audited"]["c1"]["inputs"]["i9"]["result"]=="MISMATCH" and any("identity" in w for w in c6i["audited"]["c1"]["inputs"]["i9"]["why"]))); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0])''')
io.open(T,"w",encoding="utf-8").write(t); print("gate-6 repairs applied to tool, manifest header and kit")

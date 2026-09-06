#!/usr/bin/env python3
"""V29 gate repairs (codex F1: reconstruction identity — uniqueness + claim binding; F2: complete-branch matching). Tools only; text in write_v30."""
import io,re
def rep(t,a,b):
    assert t.count(a)==1,(a[:70],t.count(a)); return t.replace(a,b)
S="r3c2_ledger_tools.py"; s=io.open(S,encoding="utf-8").read()
# ---- F1a: schema check — every input_id occurs exactly once across the whole reconstruction; explicit claim_id/input_id fields agree with the enclosing key
s=rep(s,'''    out=[]
    for cid,r in RD.items():
        if not isinstance(r,dict) or "outcome" not in r: out.append(f"{cid}: re-derivation lacks outcome"); continue
        for iid,ar in (r.get("inputs") or {}).items():
            if not isinstance(ar,dict): out.append(f"{cid}/{iid}: input reconstruction must be a full record, not a label"); continue''',
'''    out=[]; seen_ids={}
    for cid,r in RD.items():
        if not isinstance(r,dict) or "outcome" not in r: out.append(f"{cid}: re-derivation lacks outcome"); continue
        for iid,ar in (r.get("inputs") or {}).items():
            if not isinstance(ar,dict): out.append(f"{cid}/{iid}: input reconstruction must be a full record, not a label"); continue
            if iid in seen_ids: out.append(f"{cid}/{iid}: input_id already reconstructed under {seen_ids[iid]} — every input_id occurs exactly once across the reconstruction")  # PROBE:C6_DUP_INPUT
            seen_ids[iid]=cid
            if "input_id" in ar and str(ar["input_id"])!=str(iid): out.append(f"{cid}/{iid}: explicit input_id {ar['input_id']!r} conflicts with its key")
            if "claim_id" in ar and str(ar["claim_id"])!=str(cid): out.append(f"{cid}/{iid}: explicit claim_id {ar['claim_id']!r} conflicts with its enclosing claim {cid}")  # PROBE:C6_CLAIM_KEY''')
# ---- F1b: at compare, bind the enclosing claim key to the sealed record's claim_id; a_graph is built only after the schema check (no overwrite possible)
s=rep(s,'''    for x in recon_schema_fails(RD): fails.append("C6_RECONSTRUCTION: "+x)  # PROBE:C6_RECON_COMPLETE''',
'''    for x in recon_schema_fails(RD): fails.append("C6_RECONSTRUCTION: "+x)  # PROBE:C6_RECON_COMPLETE
    for cid0,r0 in RD.items():
        for iid0,ar0 in (r0.get("inputs") or {}).items():
            sr0=full_by.get(iid0)
            if sr0 is not None and str(sr0.get("claim_id"))!=str(cid0): fails.append(f"C6_IDENTITY: {iid0} reconstructed under claim {cid0}, but the sealed record belongs to claim {sr0.get('claim_id')}")  # PROBE:C6_IDENTITY''')
# ---- F2: complete-branch matching — a record matches the primary only if origin+evidence+parents all equal the primary; the alternative only if all equal the full alternative branch
s=rep(s,'''        if same_origin and (ev_ok or (alt_origin and ev_alt_ok)) and par_ok: branch="primary"
        elif same_origin and ev_ok and par_alt_ok: branch="alt"          # parent-only declared alternative (PARENTS_DISPUTED), origin unchanged
        elif alt_origin and ev_alt_ok and (par_alt_ok or (s_par_alt is None and par_ok)): branch="alt"   # declared origin alternative with its own evidence
        else:''',
'''        has_alt=bool(sr.get("origin_alt")) or (s_par_alt is not None)
        # the complete alternative branch: every declared alternative field applied together; undeclared fields stay primary
        alt_origin_full=str(sr.get("origin_alt")) if sr.get("origin_alt") else str(sr.get("origin"))
        alt_ev_full=sev2 if sr.get("origin_alt") else sev
        alt_par_full=s_par_alt if s_par_alt is not None else s_par
        matches_primary=same_origin and ev_ok and par_ok
        matches_alt=has_alt and str(ar.get("origin"))==alt_origin_full and all(str(aev.get(f2))==str(alt_ev_full.get(f2)) for f2 in ("reason_code","source_file","source_line","verbatim")) and a_par==alt_par_full
        if matches_primary: branch="primary"
        elif matches_alt: branch="alt"   # PROBE:C6_COMPLETE_BRANCH
        else:''')
io.open(S,"w",encoding="utf-8").write(s); print("gate-5 tool repairs applied")

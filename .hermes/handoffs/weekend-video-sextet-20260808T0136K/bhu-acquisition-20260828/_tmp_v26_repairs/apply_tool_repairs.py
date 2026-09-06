#!/usr/bin/env python3
"""Apply the V26cand gate repairs (codex F1–F4, F9; kimi folded in by a second script if needed) to the STAGED kit. Write-at-end, every anchor asserted.
Run from the lane directory AFTER both gate seats are observed absent."""
import io, shutil, pathlib
S="r3c2_staged_d1d7/r3c2_ledger_tools_STAGED.py"; s=io.open(S,encoding="utf-8").read()
def rep(txt,a,b,count=1):
    assert txt.count(a)==count,(a[:70],txt.count(a)); return txt.replace(a,b)
# F2: empty ledgers are valid
s=rep(s,'    assert isinstance(recs,list) and recs, "ledger has no records"','    assert isinstance(recs,list), "ledger records must be a list (an empty list is valid: a claim may state no derivation)"')
# F1: a locally printed cited value ("We adopt a = 3 from t12." printed in the claiming paper) is IMPORTED at its own line; the external branch applies only when source_file differs from the claiming file
s=rep(s,'''        if r["status"]=="PRINTED" and rc=="ORIG_CITATION":
            # STAGED D1 (review's wording): verbatim at the claiming paper's citing sentence, numeric token at the external value line
            ef=str(ev.get("source_file","")); el=ev.get("source_line"); cf=claim_file.get(r["claim_id"])
            if ef!=cf: fails.append(f"{r['input_id']}: citing sentence is in {ef}, but claim {r['claim_id']} belongs to {cf}")  # PROBE:D1_CLAIMING_FILE
            if ef==r["source_file"]: fails.append(f"{r['input_id']}: IMPORTED PRINTED record names its own file as the external source")  # PROBE:D1_SELF_FILE''',
'''        if r["status"]=="PRINTED" and rc=="ORIG_CITATION" and r["source_file"]==claim_file.get(r["claim_id"]):
            # gate F1: a LOCALLY printed cited value ("We adopt a = 3 from X" printed by the claiming paper): IMPORTED at its own line; no external checks
            ef=str(ev.get("source_file","")); el=ev.get("source_line")
            if ef!=r["source_file"]: fails.append(f"{r['input_id']}: locally printed import quotes a sentence in {ef}, not its own file")  # PROBE:D1_LOCAL_SAME_FILE
            if not str(ev.get("verbatim","")).strip(): fails.append(f"{r['input_id']}: empty verbatim quotation")
            cl=read_line(srcdir, ef, el)
            if cl is None: fails.append(f"{r['input_id']}: cannot read citing sentence {ef}:{el}")
            elif ev.get("verbatim","") not in cl: fails.append(f"{r['input_id']}: verbatim not found at citing sentence {ef}:{el}")
            vl=read_line(srcdir, r["source_file"], r["source_line"])
            if vl is None: fails.append(f"{r['input_id']}: cannot read value line {r['source_file']}:{r['source_line']}")
            elif not token_in(r.get("value"), vl): fails.append(f"{r['input_id']}: value {r.get('value')} is not a numeric token at {r['source_file']}:{r['source_line']}")  # PROBE:D1_LOCAL_VALUE_TOKEN
            continue
        if r["status"]=="PRINTED" and rc=="ORIG_CITATION":
            # STAGED D1 (review's wording): verbatim at the claiming paper's citing sentence, numeric token at the EXTERNAL value line
            ef=str(ev.get("source_file","")); el=ev.get("source_line"); cf=claim_file.get(r["claim_id"])
            if ef!=cf: fails.append(f"{r['input_id']}: citing sentence is in {ef}, but claim {r['claim_id']} belongs to {cf}")  # PROBE:D1_CLAIMING_FILE
            if ef==r["source_file"]: fails.append(f"{r['input_id']}: IMPORTED PRINTED record names its own file as the external source")  # PROBE:D1_SELF_FILE''')
# F3: every record except ORIG_SILENT carries a non-empty quotation machine-matched at origin_evidence.source_file/source_line, whatever its status; STANDARD value token at its own cited line; BLOCKED quotation at the claiming paper
s=rep(s,'''        if r["status"]=="STANDARD" and str(r.get("value"))!=STANDARD_LIST.get(r["symbol"]): fails.append(f"{r['input_id']}: STANDARD value {r.get('value')} for {r['symbol']} not on the closed list")''',
'''        if r["status"]=="STANDARD" and str(r.get("value"))!=STANDARD_LIST.get(r["symbol"]): fails.append(f"{r['input_id']}: STANDARD value {r.get('value')} for {r['symbol']} not on the closed list")
        if rc!="ORIG_SILENT" and r["status"] in ("STANDARD","BLOCKED"):
            # gate F3: the promised byte-level evidence check applies to every status, not only PRINTED
            ef=str(ev.get("source_file","")); el=ev.get("source_line"); cl=read_line(srcdir, ef, el)
            if not str(ev.get("verbatim","")).strip(): fails.append(f"{r['input_id']}: {r['status']} record with an empty quotation")  # PROBE:EV_EMPTY_ANY
            elif cl is None: fails.append(f"{r['input_id']}: cannot read evidence line {ef}:{el}")  # PROBE:EV_LINE_ANY
            elif ev.get("verbatim","") not in cl: fails.append(f"{r['input_id']}: quotation not found at evidence line {ef}:{el}")  # PROBE:EV_VERBATIM_ANY
            if r["status"]=="STANDARD" and r.get("source_file"):
                vl=read_line(srcdir, r["source_file"], r["source_line"])
                if vl is None or not token_in(r.get("value"), vl): fails.append(f"{r['input_id']}: STANDARD value {r.get('value')} is not a numeric token at {r['source_file']}:{r['source_line']}")  # PROBE:STD_VALUE_LINE''')
io.open(S,"w",encoding="utf-8").write(s)
# F2/F4: staged LANE tool — empty ledgers valid; compute takes the candidate file, emits NOT_COMPUTED for included candidates with no records; dispute status propagates through the whole dependency graph across claims
lt=io.open("r3c2_lane_tools.py",encoding="utf-8").read()
lt=rep(lt,'    assert isinstance(recs,list) and recs, "ledger has no records"','    assert isinstance(recs,list), "ledger records must be a list (an empty list is valid)"')
lt=rep(lt,'''def cmd_compute(ledger,out):
    d,recs=load(ledger)''','''def disputed_reach(rec_by_id, rid, seen=None):
    """gate F4: True if any record reachable from rid (itself included), across claims, carries origin_alt or PARENTS_DISPUTED"""
    seen=seen or set()
    if rid in seen or rid not in rec_by_id: return False
    r=rec_by_id[rid]; seen=seen|{rid}
    if (r.get("origin_alt") and r["origin_alt"]!=r["origin"]) or r.get("PARENTS_DISPUTED"): return True
    return any(disputed_reach(rec_by_id,p,seen) for p in (r.get("derived_from") or [])) or any(disputed_reach(rec_by_id,p,seen) for p in (r.get("derived_from_alt") or []))

def cmd_compute(ledger,out,candidates=None):
    d,recs=load(ledger)''')
lt=rep(lt,'''        if (r.get("origin_alt") and r["origin_alt"]!=r["origin"]) or r.get("PARENTS_DISPUTED"): disputed_claims.add(r["claim_id"])''',
'''        if disputed_reach(by, r["input_id"]): disputed_claims.add(r["claim_id"])  # PROBE:DISPUTE_PROPAGATES''')
lt=rep(lt,'''    result={"records":recs,"claims":out_claims}''','''    if candidates:
        C=json.loads(pathlib.Path(candidates).read_text())["candidates"]; inc=[c["candidate_id"] for c in C if c.get("included")]
        for cid in inc:
            if cid not in out_claims: out_claims[cid]={"root_origins":[],"rests_on":"NOT_COMPUTED"}  # PROBE:NOT_COMPUTED
        extra=[c for c in out_claims if c not in set(inc)]
        if extra: print("FAIL: ledger claims that are not included candidates:",extra); return 1
        if len(out_claims)!=len(inc): print(f"FAIL: rests_on rows {len(out_claims)} != included denominator {len(inc)}"); return 1
    result={"records":recs,"claims":out_claims}''')
lt=rep(lt,'''    if len(a)==3 and a[0]=="compute": sys.exit(cmd_compute(a[1],a[2]))''','''    if len(a)==3 and a[0]=="compute": sys.exit(cmd_compute(a[1],a[2]))
    if len(a)==4 and a[0]=="compute": sys.exit(cmd_compute(a[1],a[2],a[3]))''')
lt=lt.replace('"""r3c2_lane_tools.py — LANE-SIDE tool','"""r3c2_lane_tools_STAGED.py — STAGED, UNADOPTED copy (V26cand gate F2/F4 repairs) of the LANE-SIDE tool',1)
io.open("r3c2_staged_d1d7/r3c2_lane_tools_STAGED.py","w",encoding="utf-8").write(lt)
# F9: manifest fails closed on symlinks / non-regular entries
mf=io.open("r3c2_manifest.py",encoding="utf-8").read()
mf=rep(mf,'''            if os.path.islink(p) or not os.path.isfile(p): continue''','''            if os.path.islink(p) or not os.path.isfile(p): print(f"ERROR={os.path.relpath(p, root)}: symlink or non-regular entry (the manifest pins regular files only and refuses to skip)"); sys.exit(1)  # PROBE:MANIFEST_SYMLINK''')
mf=rep(mf,'''        dirnames.sort()''','''        dirnames.sort()
        for dn in list(dirnames):
            if os.path.islink(os.path.join(dirpath, dn)): print(f"ERROR={os.path.relpath(os.path.join(dirpath, dn), root)}: symlinked directory (refused)"); sys.exit(1)''')
mf=mf.replace('"""r3c2_manifest.py <directory>','"""r3c2_manifest_STAGED.py <directory> — STAGED, UNADOPTED copy (V26cand gate F9: symlinks and non-regular entries fail closed)',1)
io.open("r3c2_staged_d1d7/r3c2_manifest_STAGED.py","w",encoding="utf-8").write(mf)
# F8: builder with explicit --master/--out/--brief (staged copy)
bd=io.open("r3c2_build_seat_packet.py",encoding="utf-8").read()
bd=rep(bd,'MASTER = pathlib.Path("R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md")','import argparse\n_ap=argparse.ArgumentParser(); _ap.add_argument("--master",default="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"); _ap.add_argument("--out",default="r3c2_seat_packet/R3C2_SEAT_PACKET.md"); _ap.add_argument("--brief",default=None); _args=_ap.parse_args()\nMASTER = pathlib.Path(_args.master)')
bd=rep(bd,'OUT    = pathlib.Path("r3c2_seat_packet/R3C2_SEAT_PACKET.md")','OUT    = pathlib.Path(_args.out)')
bd=rep(bd,'BRIEF = pathlib.Path("r3c2_seat_packet/SEAT_BRIEF.md")','BRIEF = pathlib.Path(_args.brief) if _args.brief else OUT.parent/"SEAT_BRIEF.md"')
io.open("r3c2_staged_d1d7/r3c2_build_seat_packet_STAGED.py","w",encoding="utf-8").write(bd)
print("tool repairs applied: seat tool (F1, F2, F3), lane tool STAGED (F2, F4), manifest STAGED (F9), builder STAGED (F8 args)")

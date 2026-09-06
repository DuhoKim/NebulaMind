#!/usr/bin/env python3
"""r3c2_batch_tools_STAGED.py — STAGED, UNADOPTED (batch-reading candidate, 2026-09-06). LANE-SIDE; never given to a seat.
  partition <R3C2_CORPUS_MANIFEST.md> <n_batches> <partition.json>   manifest row order, sizes differ by at most 1, printed
  seal      <partition.json> <k> <seat_dir> <seals.json>              records the four batch-k artefacts' digests (append; refuses to re-seal a batch)
  join      <partition.json> <seat_dir> <seals.json> <out_prefix>     pure function: verify seals, verify batch scope, prefix ids b<k>_, recompute counts, write joined files
  coverage  <partition.json> <manifest.md> <seat_dir> <packet_sha256> C1B_BATCH_COVERAGE: union of batch lists == manifest, no duplicate,
                                                                       every SEAT_REPORT_b<k>.md prints ACCESS_SHA=<packet_sha256>; PASS/FAIL
"""
import json, sys, pathlib, hashlib, re

def manifest_files(m):
    out=[]
    for line in pathlib.Path(m).read_text(errors="replace").splitlines():
        mm=re.match(r"\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`",line)
        if mm: out.append((int(mm.group(1)),mm.group(2),mm.group(3)))
    assert out and [r[0] for r in out]==list(range(1,len(out)+1)), "manifest rows must be 1..n in order"
    return out

def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
ART=lambda k: [f"candidates_b{k}.json",f"exclusions_b{k}.json",f"ledger_b{k}.json",f"SEAT_REPORT_b{k}.md"]

def cmd_partition(m,n,out):
    rows=manifest_files(m); n=int(n); N=len(rows); base,extra=divmod(N,n); batches=[]; i=0
    for k in range(1,n+1):
        size=base+(1 if k<=extra else 0); batches.append({"batch":k,"rows":[r[0] for r in rows[i:i+size]],"files":[r[1] for r in rows[i:i+size]],"sha256":[r[2] for r in rows[i:i+size]]}); i+=size
    P={"manifest_sha256":sha(m),"n_texts":N,"n_batches":n,"batches":batches}
    pathlib.Path(out).write_text(json.dumps(P,indent=1,sort_keys=True))
    for b in batches: print(f"batch {b['batch']}: rows {b['rows'][0]}-{b['rows'][-1]} ({len(b['files'])} texts)")
    return 0

def cmd_seal(part,k,seat_dir,out):
    k=int(k); p=pathlib.Path(out); S=json.loads(p.read_text()) if p.exists() else {"seals":{}}
    if str(k) in S["seals"]: print(f"FAIL: batch {k} already sealed"); return 1
    d=pathlib.Path(seat_dir); rec={}
    for f in ART(k):
        if not (d/f).exists(): print(f"FAIL: batch {k} artefact missing: {f}"); return 1
        rec[f]=sha(d/f)
    S["seals"][str(k)]=rec; p.write_text(json.dumps(S,indent=1,sort_keys=True)); print(f"sealed batch {k}: "+" ".join(f"{f}={h[:16]}" for f,h in rec.items())); return 0

def cmd_join(part,seat_dir,seals,prefix):
    P=json.loads(pathlib.Path(part).read_text()); S=json.loads(pathlib.Path(seals).read_text())["seals"]; d=pathlib.Path(seat_dir); fails=[]
    C=[]; X=[]; Lr=[]; att=0
    for b in P["batches"]:
        k=b["batch"]; allowed=set(b["files"])
        if str(k) not in S: fails.append(f"batch {k}: not sealed"); continue
        for f in ART(k):
            if not (d/f).exists(): fails.append(f"batch {k}: missing {f}"); continue
            if sha(d/f)!=S[str(k)][f]: fails.append(f"batch {k}: {f} differs from its seal")  # PROBE:SEAL_MISMATCH
        if fails: continue
        cd=json.loads((d/ART(k)[0]).read_text()); xd=json.loads((d/ART(k)[1]).read_text()); ld=json.loads((d/ART(k)[2]).read_text()); ld=ld["records"] if isinstance(ld,dict) else ld
        for c in cd["candidates"]:
            if c.get("source_file") not in allowed: fails.append(f"batch {k}: candidate {c.get('candidate_id')} cites {c.get('source_file')}, not a text of this batch")  # PROBE:BATCH_SCOPE
            c=dict(c); c["candidate_id"]=f"b{k}_{c['candidate_id']}"; C.append(c)
        for x in xd["exclusions"]:
            x=dict(x); x["candidate_id"]=f"b{k}_{x['candidate_id']}"; X.append(x)
        for r in ld:
            r=dict(r); r["claim_id"]=f"b{k}_{r['claim_id']}"; r["input_id"]=f"b{k}_{r['input_id']}"
            if r.get("derived_from"): r["derived_from"]=[f"b{k}_{p}" for p in r["derived_from"]]
            Lr.append(r)
    for f in fails: print("FAIL:",f)
    if fails: print("JOIN=FAIL"); return 1
    inc=sum(1 for c in C if c.get("included")); exc=len(X); att=sum(int(c.get("attempts",0)) for c in C if c.get("included"))
    cand={"declared_candidate_count":len(C),"declared_included_count":inc,"declared_excluded_count":len(C)-inc,"declared_attempt_count":att,"candidates":C}
    excl={"declared_exclusion_count":exc,"exclusions":X}
    for name,obj in (("candidates.json",cand),("exclusions.json",excl),("ledger.json",{"records":Lr})):
        pathlib.Path(prefix+name).write_text(json.dumps(obj,indent=1,sort_keys=True))
        print(f"{prefix+name} sha256={sha(prefix+name)}")
    print(f"joined: batches={len(P['batches'])} candidates={len(C)} included={inc} excluded={len(C)-inc} exclusions={exc} records={len(Lr)}"); print("JOIN=PASS"); return 0

def cmd_coverage(part,m,seat_dir,packet_sha):
    P=json.loads(pathlib.Path(part).read_text()); rows=manifest_files(m); fails=[]
    if P["manifest_sha256"]!=sha(m): fails.append("partition was computed over a different manifest")
    seen={}
    for b in P["batches"]:
        for f in b["files"]:
            if f in seen: fails.append(f"text {f} appears in batch {seen[f]} and batch {b['batch']}")  # PROBE:C1B_DUPLICATE
            seen[f]=b["batch"]
    mf=[r[1] for r in rows]
    for f in mf:
        if f not in seen: fails.append(f"manifest text {f} is in no batch")  # PROBE:C1B_MISSING
    for f in seen:
        if f not in mf: fails.append(f"batch text {f} is not in the manifest")
    d=pathlib.Path(seat_dir)
    for b in P["batches"]:
        rp=d/f"SEAT_REPORT_b{b['batch']}.md"
        if not rp.exists(): fails.append(f"batch {b['batch']}: no SEAT_REPORT"); continue
        if f"ACCESS_SHA={packet_sha}" not in rp.read_text(errors="replace"): fails.append(f"batch {b['batch']}: SEAT_REPORT does not print ACCESS_SHA={packet_sha[:16]}…")  # PROBE:C1B_ACCESS
    for f in fails: print("FAIL:",f)
    print(f"texts_in_manifest={len(mf)} texts_in_batches={len(seen)} batches={len(P['batches'])}")
    print("C1B_BATCH_COVERAGE="+("PASS" if not fails else "FAIL")); return 0 if not fails else 1

if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)==4 and a[0]=="partition": sys.exit(cmd_partition(a[1],a[2],a[3]))
    if len(a)==5 and a[0]=="seal": sys.exit(cmd_seal(a[1],a[2],a[3],a[4]))
    if len(a)==5 and a[0]=="join": sys.exit(cmd_join(a[1],a[2],a[3],a[4]))
    if len(a)==5 and a[0]=="coverage": sys.exit(cmd_coverage(a[1],a[2],a[3],a[4]))
    print(__doc__); sys.exit(2)

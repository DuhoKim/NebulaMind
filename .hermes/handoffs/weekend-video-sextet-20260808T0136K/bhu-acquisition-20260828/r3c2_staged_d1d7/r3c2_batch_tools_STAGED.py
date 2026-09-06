#!/usr/bin/env python3
"""r3c2_batch_tools_STAGED.py — STAGED, UNADOPTED (batch-reading candidate, repaired 2026-09-06 after two independent reviews). LANE-SIDE.
A batch partitions OWNERSHIP of candidate passages, not ACCESS to evidence: every session holds all pinned texts and enumerates only
its owned texts; §2/D1 lookups may read any manifest text. Identifiers are source-based and global: candidate_id / claim_id / input_id
begin with "<owned file>#"; join never renames anything.
  partition <manifest.md> <n_batches> <partition.json>            manifest row order; sizes differ by ≤1; per-batch bytes and lines printed
  seal      <partition.json> <k> <seat_dir> <corpus_dir> <seals.json>  binds the partition digest, the owned texts' digests (verified against the
                                                                    manifest), the four artefacts' digests and the predecessor seal; refuses out-of-order or repeated sealing
  join      <partition.json> <seat_dir> <seals.json> <manifest.md> <out_prefix>  verifies seals; every candidate/claim owned by its batch; every
                                                                    evidence source_file a manifest row; ids unique; derived_from resolved, acyclic; recomputed counts
  coverage  <partition.json> <manifest.md> <seat_dir> <corpus_dir> <packet_sha256>  C1B_BATCH_COVERAGE: ownership exactly once over the manifest;
                                                                    owned texts' bytes verified; every SEAT_REPORT_b<k>.md prints ACCESS_SHA=<packet>
"""
import json, sys, pathlib, hashlib, re

def manifest_rows(m):
    out=[]
    for line in pathlib.Path(m).read_text(errors="replace").splitlines():
        mm=re.match(r"\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|\s*(\d+)\s*\|\s*(\d+)",line)
        if mm: out.append((int(mm.group(1)),mm.group(2),mm.group(3),int(mm.group(4)),int(mm.group(5))))
    assert out and [r[0] for r in out]==list(range(1,len(out)+1)), "manifest rows must be 1..n in order"
    return out
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
ART=lambda k: [f"candidates_b{k}.json",f"exclusions_b{k}.json",f"ledger_b{k}.json",f"SEAT_REPORT_b{k}.md"]
def owner_of(ident): return str(ident).split("#",1)[0] if "#" in str(ident) else None

def cmd_partition(m,n,out):
    rows=manifest_rows(m); n=int(n); N=len(rows); base,extra=divmod(N,n); batches=[]; i=0
    for k in range(1,n+1):
        size=base+(1 if k<=extra else 0); sl=rows[i:i+size]
        batches.append({"batch":k,"rows":[r[0] for r in sl],"files":[r[1] for r in sl],"sha256":[r[2] for r in sl],"bytes":sum(r[3] for r in sl),"nonblank_lines":sum(r[4] for r in sl)}); i+=size
    P={"manifest_sha256":sha(m),"n_texts":N,"n_batches":n,"ownership_not_access":True,"batches":batches}
    pathlib.Path(out).write_text(json.dumps(P,indent=1,sort_keys=True))
    for b in batches: print(f"batch {b['batch']}: rows {b['rows'][0]}-{b['rows'][-1]} ({len(b['files'])} texts, {b['bytes']} bytes, {b['nonblank_lines']} non-blank lines)")
    return 0

def cmd_seal(part,k,seat_dir,corpus,out):
    k=int(k); P=json.loads(pathlib.Path(part).read_text()); p=pathlib.Path(out); S=json.loads(p.read_text()) if p.exists() else {"partition_sha256":sha(part),"seals":{}}
    if S.get("partition_sha256")!=sha(part): print("FAIL: seals file belongs to a different partition"); return 1
    if str(k) in S["seals"]: print(f"FAIL: batch {k} already sealed"); return 1
    if k>1 and str(k-1) not in S["seals"]: print(f"FAIL: batch {k} sealed before batch {k-1} (dispatch order)"); return 1  # PROBE:SEAL_ORDER
    b=next((b for b in P["batches"] if b["batch"]==k),None)
    if b is None: print(f"FAIL: no batch {k} in the partition"); return 1
    for f,h in zip(b["files"],b["sha256"]):
        q=pathlib.Path(corpus)/f
        if not q.exists() or sha(q)!=h: print(f"FAIL: owned text {f} absent or its bytes differ from the manifest"); return 1
    d=pathlib.Path(seat_dir); rec={"owned_files":b["files"],"owned_sha256":b["sha256"],"predecessor_seal_sha256":(hashlib.sha256(json.dumps(S["seals"][str(k-1)],sort_keys=True).encode()).hexdigest() if str(k-1) in S["seals"] else None),"artefacts":{}}
    for f in ART(k):
        if not (d/f).exists(): print(f"FAIL: batch {k} artefact missing: {f}"); return 1
        rec["artefacts"][f]=sha(d/f)
    S["seals"][str(k)]=rec; p.write_text(json.dumps(S,indent=1,sort_keys=True)); print(f"sealed batch {k}: "+" ".join(f"{f}={h[:16]}" for f,h in rec["artefacts"].items())); return 0

def cmd_join(part,seat_dir,seals,manifest,prefix):
    P=json.loads(pathlib.Path(part).read_text()); Sd=json.loads(pathlib.Path(seals).read_text()); d=pathlib.Path(seat_dir); fails=[]
    if Sd.get("partition_sha256")!=sha(part): fails.append("seals file belongs to a different partition")
    mf={r[1] for r in manifest_rows(manifest)}
    if P["manifest_sha256"]!=sha(manifest): fails.append("partition was computed over a different manifest")
    S=Sd.get("seals",{}); C=[]; X=[]; Lr=[]
    for b in P["batches"]:
        k=b["batch"]; owned=set(b["files"])
        if str(k) not in S: fails.append(f"batch {k}: not sealed"); continue
        bad=False
        for f in ART(k):
            if not (d/f).exists(): fails.append(f"batch {k}: missing {f}"); bad=True; continue
            if sha(d/f)!=S[str(k)]["artefacts"][f]: fails.append(f"batch {k}: {f} differs from its seal"); bad=True  # PROBE:SEAL_MISMATCH
        if bad: continue
        cd=json.loads((d/ART(k)[0]).read_text()); xd=json.loads((d/ART(k)[1]).read_text()); ld=json.loads((d/ART(k)[2]).read_text()); ld=ld["records"] if isinstance(ld,dict) else ld
        for c in cd["candidates"]:
            if c.get("source_file") not in owned: fails.append(f"batch {k}: candidate {c.get('candidate_id')} cites {c.get('source_file')}, not an owned text of this batch")  # PROBE:BATCH_SCOPE
            if owner_of(c.get("candidate_id"))!=c.get("source_file"): fails.append(f"batch {k}: candidate_id {c.get('candidate_id')} is not of the form <source_file>#<local>")  # PROBE:GLOBAL_ID
            C.append(dict(c))
        for x in xd["exclusions"]: X.append(dict(x))
        for r in ld:
            if owner_of(r.get("claim_id")) not in owned: fails.append(f"batch {k}: ledger record {r.get('input_id')} belongs to claim {r.get('claim_id')} not owned by this batch")
            if r.get("source_file") and r.get("source_file") not in mf: fails.append(f"batch {k}: record {r.get('input_id')} cites {r.get('source_file')}, not a manifest text")  # PROBE:EVIDENCE_MANIFEST
            ev=r.get("origin_evidence") or {}
            if ev.get("source_file") and ev.get("source_file") not in mf: fails.append(f"batch {k}: record {r.get('input_id')} evidence cites {ev.get('source_file')}, not a manifest text")
            Lr.append(dict(r))
    ids=[c.get("candidate_id") for c in C]
    for i in sorted(set(x for x in ids if ids.count(x)>1)): fails.append(f"candidate_id collision across batches: {i}")  # PROBE:ID_COLLISION
    by={}
    for r in Lr:
        if r.get("input_id") in by: fails.append(f"input_id collision across batches: {r.get('input_id')}")
        by[r.get("input_id")]=r
    def walk(i,seen):
        if i in seen: raise ValueError(f"derived_from cycle at {i}")
        for p_ in by[i].get("derived_from") or []:
            if p_ not in by: raise ValueError(f"{i}: derived_from {p_} unresolved after join")
            walk(p_,seen|{i})
    for i in by:
        try: walk(i,set())
        except ValueError as e:
            fails.append(str(e))  # PROBE:GRAPH
    for f in fails: print("FAIL:",f)
    if fails: print("JOIN=FAIL"); return 1
    inc=sum(1 for c in C if c.get("included")); att=sum(int(c.get("attempts",0)) for c in C if c.get("included"))
    cand={"declared_candidate_count":len(C),"declared_included_count":inc,"declared_excluded_count":len(C)-inc,"declared_attempt_count":att,"candidates":C}
    excl={"declared_exclusion_count":len(X),"exclusions":X}
    for name,obj in (("candidates.json",cand),("exclusions.json",excl),("ledger.json",{"records":Lr})):
        pathlib.Path(prefix+name).write_text(json.dumps(obj,indent=1,sort_keys=True)); print(f"{prefix+name} sha256={sha(prefix+name)}")
    print(f"joined: batches={len(P['batches'])} candidates={len(C)} included={inc} excluded={len(C)-inc} exclusions={len(X)} records={len(Lr)}"); print("JOIN=PASS"); return 0

def cmd_coverage(part,m,seat_dir,corpus,packet_sha):
    P=json.loads(pathlib.Path(part).read_text()); rows=manifest_rows(m); fails=[]
    if P["manifest_sha256"]!=sha(m): fails.append("partition was computed over a different manifest")
    seen={}; msha={r[1]:r[2] for r in rows}
    for b in P["batches"]:
        for f,h in zip(b["files"],b["sha256"]):
            if f in seen: fails.append(f"text {f} is owned by batch {seen[f]} and batch {b['batch']}")  # PROBE:C1B_DUPLICATE
            seen[f]=b["batch"]
            q=pathlib.Path(corpus)/f
            if f in msha and (h!=msha[f] or not q.exists() or sha(q)!=msha[f]): fails.append(f"owned text {f}: bytes do not verify against the manifest")  # PROBE:C1B_BYTES
    for f in msha:
        if f not in seen: fails.append(f"manifest text {f} is owned by no batch")  # PROBE:C1B_MISSING
    for f in seen:
        if f not in msha: fails.append(f"owned text {f} is not in the manifest")
    d=pathlib.Path(seat_dir)
    for b in P["batches"]:
        rp=d/f"SEAT_REPORT_b{b['batch']}.md"
        if not rp.exists(): fails.append(f"batch {b['batch']}: no SEAT_REPORT"); continue
        if f"ACCESS_SHA={packet_sha}" not in rp.read_text(errors="replace"): fails.append(f"batch {b['batch']}: SEAT_REPORT does not print ACCESS_SHA={packet_sha[:16]}…")  # PROBE:C1B_ACCESS
    for f in fails: print("FAIL:",f)
    print(f"texts_in_manifest={len(msha)} texts_owned={len(seen)} batches={len(P['batches'])}")
    print("C1B_BATCH_COVERAGE="+("PASS" if not fails else "FAIL")); return 0 if not fails else 1

if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)==4 and a[0]=="partition": sys.exit(cmd_partition(a[1],a[2],a[3]))
    if len(a)==6 and a[0]=="seal": sys.exit(cmd_seal(*a[1:]))
    if len(a)==6 and a[0]=="join": sys.exit(cmd_join(*a[1:]))
    if len(a)==6 and a[0]=="coverage": sys.exit(cmd_coverage(*a[1:]))
    print(__doc__); sys.exit(2)

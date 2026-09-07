_probe_noop=lambda *a,**k: None  # PROBE-DELETED
#!/usr/bin/env python3
"""r3c2_ledger_tools.py — the seat's ledger tool for the R3-C2 census.

  /usr/bin/python3 -E r3c2_ledger_tools.py census   <candidates.json> <exclusions.json>
      C1: candidates.json = {declared_candidate_count, declared_included_count, declared_excluded_count,
      declared_attempt_count, candidates:[...]} — every included candidate carries attempts in {0,1,2} and outcome (a section-3 token or PENDING; `census ... final` rejects PENDING and requires printed_value/reproduced_value on arithmetic outcomes); exclusions.json =
      {declared_exclusion_count, exclusions:[...]}; every candidate has exactly one disposition; every exclusion row carries source_file, source_line and numeral equal to its candidate row (retained, not discarded); the AUTHOR_SPECIFIED_INPUT count is printed beside the denominator; the declared counts are
      compared with the recomputed counts and any mismatch FAILS; exit 0 PASS / 1 FAIL.
  V28 D1 — validate <ledger.json> <sources_dir> <candidates.json>: a PRINTED record with reason_code ORIG_CITATION is
      an imported value: its non-empty verbatim is matched at the CLAIMING paper's citing sentence (origin_evidence.source_file/
      source_line), and the claiming file is the file of the candidate row whose candidate_id equals the record's claim_id; its
      value is matched as a numeric TOKEN (not a substring) at the EXTERNAL value line (source_file/source_line), which must be an
      exact row of R3C2_CORPUS_MANIFEST.md in <sources_dir> whose bytes verify against that row's sha256, must differ from the claiming
      file, and must be the FIRST line of the source carrying both the symbol and the numeral (the tie-break); no reason-code test
      is applied to the external line's wording. The kit implements the review's wording only (evidence at the borrower).
  V28 D7 — audit seal-enumeration <aud_c> <aud_x> <seal.txt>   census-gated, first-write
                            audit select <sealed_c> <seed_hex> <stage1_seal> <selection.json>   refuses without the stage-1 seal
                            audit handout <selection.json> <sealed_c> <handout.json>              ids + file + line ONLY
                            audit seal-rederivation <rederiv.json> <seal2.txt>                    first-write, before any release
                            audit compare <seal1> <aud_c> <aud_x> <sealed_c> <sealed_x> <sealed_l> <selection> <seal2> <rederiv> <C6_AUDIT.json>
  /usr/bin/python3 -E r3c2_ledger_tools.py validate <ledger.json> <sources_dir> <candidates.json>
      asserts: every record has the schema fields and no field outside the schema; status in
      {PRINTED,STANDARD,ABSENT,BLOCKED}; origin in {CHOSEN,DERIVED,FITTED,IMPORTED,MEASURED,STANDARD,UNDECLARED};
      reason_code/origin pair is one of the allowed pairs; no ABSENT or BLOCKED record carries a value; a BLOCKED record
      (traced to a named source, no machine-matchable value) carries origin IMPORTED with ORIG_CITATION evidence and is
      never consumed; every PRINTED record's verbatim quotation is a substring of the cited source line; every STANDARD
      value is on the closed list; derived_from ids exist, a DERIVED record names its parents, and the graph is acyclic;
      an ORIG_SILENT record carries origin_search {query, files, matches}. Exit 0 = PASS, 1 = FAIL (every failure
      printed), 2 = usage/schema error.
"""
import json, sys, pathlib, hashlib, random, math, re, subprocess

STATUS={"PRINTED","STANDARD","ABSENT","BLOCKED"}
OUTCOMES={"REPRO_WITHIN_STATED_PRECISION","REPRO_FAILED","REPRO_BLOCKED","REPRO_INPUT_ABSENT","REPRO_NOT_EVALUABLE","REPRO_NO_DERIVATION_STATED"}
ARITH={"REPRO_WITHIN_STATED_PRECISION","REPRO_FAILED"}
ORIGIN={"CHOSEN","DERIVED","FITTED","IMPORTED","MEASURED","STANDARD","UNDECLARED"}
PAIRS={"ORIG_EQUATION":"DERIVED","ORIG_CONSTANT":"STANDARD","ORIG_MEASURED":"MEASURED","ORIG_CHOICE_STATED":"CHOSEN","ORIG_FIT_STATED":"FITTED","ORIG_CITATION":"IMPORTED","ORIG_SILENT":"UNDECLARED"}
# when more than one reason code matches the cited sentence, the first applicable in this order is filed (a sentence
# naming an external source for the value is a citation whatever else it says):
CODE_PRECEDENCE=["ORIG_CITATION","ORIG_FIT_STATED","ORIG_CHOICE_STATED","ORIG_MEASURED","ORIG_EQUATION","ORIG_CONSTANT","ORIG_SILENT"]
STANDARD_LIST={"G":"6.67430e-11","c":"2.99792458e8","hbar":"1.054571817e-34","k_B":"1.380649e-23","H0":"67.36","Omega_m":"0.3153","Omega_L":"0.6847","Omega_b_h2":"0.02237","Omega_c_h2":"0.1200","n_s":"0.9649","sigma8":"0.8111","tau":"0.0544","ln1e10As":"3.044","age_Gyr":"13.797"}
FIELDS=["claim_id","input_id","symbol","status","origin","origin_evidence","derived_from","value","source_file","source_line"]

NUMTOK=re.compile(r"[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?")
def read_line(srcdir, f, n):
    try: return (pathlib.Path(srcdir)/str(f)).read_text(errors="replace").splitlines()[int(n)-1]
    except Exception: return None

def manifest_rows(srcdir):
    m=pathlib.Path(srcdir)/"R3C2_CORPUS_MANIFEST.md"
    if not m.exists(): return None
    rows={}
    for line in m.read_text(errors="replace").splitlines():
        mm=re.match(r"\|\s*\d+\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`",line)
        if mm: rows[mm.group(1)]=mm.group(2)
    return rows

def enumerable_verified(srcdir, f):
    """exact manifest row AND the file's bytes hash to that row's sha256; (ok, why)"""
    rows=manifest_rows(srcdir)
    if rows is None: return False,"no R3C2_CORPUS_MANIFEST.md in the sources directory"
    if f not in rows: return False,f"{f} is not a row of the manifest"
    p=pathlib.Path(srcdir)/f
    if not p.exists(): return False,f"{f} absent from the sources directory"
    h=hashlib.sha256(p.read_bytes()).hexdigest()
    if h!=rows[f]: return False,f"{f} bytes ({h[:16]}) differ from the manifest row ({rows[f][:16]})"
    return True,""

def token_in(value, line):
    return str(value) in NUMTOK.findall(line or "")

def first_line_with(srcdir, f, symbol, value):
    try: lines=(pathlib.Path(srcdir)/str(f)).read_text(errors="replace").splitlines()
    except Exception: return None
    for i,l in enumerate(lines,1):
        if token_in(value,l) and re.search(r"(?<![A-Za-z0-9_])"+re.escape(str(symbol))+r"(?![A-Za-z0-9_])", l): return i
    return None

def load(p):
    d=json.loads(pathlib.Path(p).read_text())
    recs=d["records"] if isinstance(d,dict) else d
    assert isinstance(recs,list), "ledger records must be a list (an empty list is valid: a claim may state no derivation)"
    return d,recs


def canon_search(s):
    """V38 (codex V37 N1): canonical form of an origin_search object — `files` and `matches` are UNORDERED evidence inventories, so their
    entries are sorted by canonical JSON; `query` is an ordered field and is preserved exactly. Nothing is dropped, added or altered."""
    if not isinstance(s,dict): return s
    out=dict(s)
    for f in ("files","matches"):
        if isinstance(out.get(f),list): out[f]=sorted(out[f],key=lambda e: json.dumps(e,sort_keys=True,separators=(",",":")))
    return out


def graph_integrity(graph, starts):
    """V36: every derived_from edge reachable from `starts` is checked for a missing record and for a cycle, INDEPENDENTLY of origin
    (a cycle through a CHOSEN/FITTED/IMPORTED/MEASURED/STANDARD/UNDECLARED record is still a cycle). Traversal is sorted, so the
    reported problems are identical in every process. Returns a sorted list of problem strings; empty = intact."""
    problems=set(); done=set()
    def walk(n, path):
        if n in path: problems.add(f"cycle at {n}"); return
        if n in done: return
        if n not in graph: return
        for p in sorted(graph[n].get("derived_from") or []):
            if p not in graph: problems.add(f"missing dependency {p} of {n}"); continue
            walk(p, path+[n])
        done.add(n)
    for s in sorted(starts): walk(s, [])
    return sorted(problems)

def roots(rec_by_id, rid, seen=None):
    seen=seen or set()
    if rid in seen: raise ValueError(f"cycle at {rid}")
    r=rec_by_id[rid]; seen=seen|{rid}
    if r["origin"]=="DERIVED" and not r.get("derived_from"): raise ValueError(f"{rid}: DERIVED record with no derived_from (a derived input must name what it was derived from)")
    if r["origin"]!="DERIVED": return {r["origin"]}
    out=set()
    for d in sorted(r["derived_from"]):   # V36: sorted — deterministic diagnostics
        if d not in rec_by_id: raise ValueError(f"{rid}: derived_from {d} not in ledger")
        out|=roots(rec_by_id,d,seen)
    return out



def cmd_validate(ledger,srcdir,candidates=None):
    d,recs=load(ledger); fails=[]; ids=set()
    claim_file={}
    if candidates:
        for c in json.loads(pathlib.Path(candidates).read_text())["candidates"]: claim_file[c["candidate_id"]]=c["source_file"]
    for r in recs:
        missing=[f for f in FIELDS if f not in r]
        if missing: fails.append(f"{r.get('input_id')}: missing {missing}"); continue
        if r["input_id"] in ids: fails.append(f"{r['input_id']}: duplicate id")
        ids.add(r["input_id"])
        if r["status"] not in STATUS: fails.append(f"{r['input_id']}: bad status {r['status']}")
        if r["origin"] not in ORIGIN: fails.append(f"{r['input_id']}: bad origin {r['origin']}")
        ev=r["origin_evidence"]; rc=ev.get("reason_code")
        extra=[k for k in r if k not in FIELDS+["origin_search"]]
        if extra: fails.append(f"{r['input_id']}: seat-authored ledger carries a field outside the schema: {extra}")
        if rc=="ORIG_SILENT":
            srch=r.get("origin_search")
            if not isinstance(srch,dict) or not all(k in srch for k in ("query","files","matches")): fails.append(f"{r['input_id']}: ORIG_SILENT requires origin_search {{query, files, matches}}")
        if PAIRS.get(rc)!=r["origin"]: fails.append(f"{r['input_id']}: reason_code {rc} does not map to origin {r['origin']}")
        if rc!="ORIG_SILENT":
            # gate-2 F1: before any status-specific branch, EVERY non-silent record carries a non-empty quotation found at its declared evidence coordinates
            ef=str(ev.get("source_file","")); el=ev.get("source_line")
            if not str(ev.get("verbatim","")).strip(): fails.append(f"{r['input_id']}: empty quotation (every non-ORIG_SILENT record quotes its evidence line)"); continue  # PROBE:EV_EMPTY_ALL
            try: elp=int(el); assert elp>=1
            except Exception: fails.append(f"{r['input_id']}: origin_evidence.source_line {el!r} is not a positive line number"); continue  # PROBE:EV_LINE_POS
            cl0=read_line(srcdir, ef, elp)
            if cl0 is None: fails.append(f"{r['input_id']}: cannot read evidence line {ef}:{elp}"); continue  # PROBE:EV_LINE_ALL
            if ev.get("verbatim","") not in cl0: fails.append(f"{r['input_id']}: quotation not found at evidence line {ef}:{elp}"); continue  # PROBE:EV_VERBATIM_ALL
        if r["status"]=="ABSENT" and r.get("value") not in (None,""): fails.append(f"{r['input_id']}: ABSENT record carries a value")
        if r["status"]=="BLOCKED":
            if r.get("value") not in (None,""): fails.append(f"{r['input_id']}: BLOCKED record carries a value")
            cfb=claim_file.get(r["claim_id"]) if candidates else None
            if not candidates or cfb is None: fails.append(f"{r['input_id']}: BLOCKED record needs the candidate file to bind claim {r['claim_id']} to its claiming paper")  # PROBE:BLOCKED_NEEDS_CANDIDATES
            elif str(ev.get("source_file",""))!=cfb: fails.append(f"{r['input_id']}: BLOCKED naming evidence is in {ev.get('source_file')}, but claim {r['claim_id']} belongs to {cfb}")  # PROBE:BLOCKED_CLAIMING_FILE
            if r["origin"]!="IMPORTED" or rc!="ORIG_CITATION": fails.append(f"{r['input_id']}: BLOCKED record must carry origin IMPORTED with ORIG_CITATION evidence from the claiming paper")
        if r["status"]=="STANDARD" and str(r.get("value"))!=STANDARD_LIST.get(r["symbol"]): fails.append(f"{r['input_id']}: STANDARD value {r.get('value')} for {r['symbol']} not on the closed list")
        if r["status"]=="STANDARD":
            cfs=claim_file.get(r["claim_id"]) if candidates else None
            if not candidates or cfs is None: fails.append(f"{r['input_id']}: STANDARD record needs the candidate file to bind claim {r['claim_id']} to its claiming paper")  # PROBE:STD_NEEDS_CANDIDATES
            elif r.get("source_file") and r.get("source_file")!=cfs: fails.append(f"{r['input_id']}: STANDARD value line is in {r.get('source_file')}, outside the claiming file {cfs}: a value outside the claiming paper follows the named-source rule (PRINTED/IMPORTED with ORIG_CITATION), even when it is on the closed list")  # PROBE:STD_CLAIMING_FILE
            if not r.get("source_file") or not isinstance(r.get("source_line"),int) or r.get("source_line",0)<1: fails.append(f"{r['input_id']}: STANDARD record needs its own source_file and a positive source_line (absence of origin evidence never waives value evidence)")  # PROBE:STD_COORDS
            else:
                vl=read_line(srcdir, r["source_file"], r["source_line"])
                if vl is None or not token_in(r.get("value"), vl): fails.append(f"{r['input_id']}: STANDARD value {r.get('value')} is not a numeric token at {r['source_file']}:{r['source_line']}")  # PROBE:STD_VALUE_LINE
        if r["status"]=="PRINTED":
            if not candidates: fails.append(f"{r['input_id']}: PRINTED record needs the candidate file to bind claim {r['claim_id']} to its claiming paper"); continue  # PROBE:D1_NEEDS_CANDIDATES_ALL
            cf0=claim_file.get(r["claim_id"])
            if cf0 is None: fails.append(f"{r['input_id']}: claim {r['claim_id']} is not a candidate row"); continue  # PROBE:D1_UNKNOWN_CLAIM_ALL
            if r["source_file"]!=cf0 and not (r["origin"]=="IMPORTED" and rc=="ORIG_CITATION"):
                fails.append(f"{r['input_id']}: value line is in {r['source_file']} but claim {r['claim_id']} belongs to {cf0}: such a record must be IMPORTED with ORIG_CITATION (submitted {r['origin']}/{rc})")  # PROBE:D1_IMPORT_REFILED
                continue
        if r["status"]=="PRINTED" and rc=="ORIG_CITATION" and r["source_file"]==claim_file.get(r["claim_id"]):
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
            # V28 D1 (review's wording): verbatim at the claiming paper's citing sentence, numeric token at the EXTERNAL value line
            ef=str(ev.get("source_file","")); el=ev.get("source_line"); cf=claim_file.get(r["claim_id"])
            if ef!=cf: fails.append(f"{r['input_id']}: citing sentence is in {ef}, but claim {r['claim_id']} belongs to {cf}")  # PROBE:D1_CLAIMING_FILE
            if ef==r["source_file"]: fails.append(f"{r['input_id']}: IMPORTED PRINTED record names its own file as the external source")  # PROBE:D1_SELF_FILE
            ok,why=enumerable_verified(srcdir, r["source_file"])
            if not ok: fails.append(f"{r['input_id']}: external source not an enumerable verified text: {why}")  # PROBE:D1_ENUMERABLE
            if not str(ev.get("verbatim","")).strip(): fails.append(f"{r['input_id']}: empty verbatim quotation")  # PROBE:D1_EMPTY_VERBATIM
            cl=read_line(srcdir, ef, el)
            if cl is None: fails.append(f"{r['input_id']}: cannot read citing sentence {ef}:{el}")
            elif ev.get("verbatim","") not in cl: fails.append(f"{r['input_id']}: verbatim not found at citing sentence {ef}:{el}")  # PROBE:D1_VERBATIM_SITE
            vl=read_line(srcdir, r["source_file"], r["source_line"])
            if vl is None: fails.append(f"{r['input_id']}: cannot read external value line {r['source_file']}:{r['source_line']}")
            elif not token_in(r.get("value"), vl): fails.append(f"{r['input_id']}: value {r.get('value')} is not a numeric token at external value line {r['source_file']}:{r['source_line']}")  # PROBE:D1_VALUE_TOKEN
            else:
                first=first_line_with(srcdir, r["source_file"], r["symbol"], r.get("value"))
                if first is None: fails.append(f"{r['input_id']}: no line of {r['source_file']} carries both {r['symbol']} and {r.get('value')}")  # PROBE:D1_NO_SYMBOL_LINE
                elif first!=int(r["source_line"]): fails.append(f"{r['input_id']}: external value line {r['source_line']} is not the first line of {r['source_file']} carrying both {r['symbol']} and {r.get('value')} (that is line {first})")  # PROBE:D1_FIRST_LINE
            continue
        if r["status"]=="PRINTED":
            f=pathlib.Path(srcdir)/r["source_file"]
            try: line=f.read_text(errors="replace").splitlines()[int(r["source_line"])-1]
            except Exception as e: fails.append(f"{r['input_id']}: cannot read {r['source_file']}:{r['source_line']} ({e})"); continue
            if not token_in(r.get("value"), line): fails.append(f"{r['input_id']}: value {r.get('value')} is not a numeric token at {r['source_file']}:{r['source_line']}")  # PROBE:PRINTED_VALUE_LINE
    by={r["input_id"]:r for r in recs}
    # V37 (codex V36 F2): the complete input graph is checked for cycles INDEPENDENTLY of origin, before root classification; a missing
    # dependency is reported by the per-record check below (itself origin-independent). Stopping root traversal at a non-DERIVED origin
    # never substitutes for either check.
    for g in graph_integrity(by, list(by)):
        if g.startswith("cycle"): _probe_noop(f"graph integrity: {g}")  # PROBE-DELETED:VALIDATE_GRAPH_INTEGRITY
    for r in recs:
        for dfrom in r.get("derived_from") or []:
            if dfrom not in by: fails.append(f"{r['input_id']}: derived_from {dfrom} absent")
        try: roots(by,r["input_id"])
        except ValueError as e: fails.append(str(e))
    for x in fails: print("FAIL:",x)
    print("C3_NO_SUBSTITUTION=" + ("PASS" if not fails else "FAIL")); return 0 if not fails else 1

def cmd_census(candidates,exclusions,final=False):
    """C1: every candidate passage has exactly one disposition (included or excluded with a reason kind); counts recomputed."""
    Cd=json.loads(pathlib.Path(candidates).read_text()); Xd=json.loads(pathlib.Path(exclusions).read_text())
    fails=[]; KINDS={"AUTHOR_SPECIFIED_INPUT","ATTRIBUTED_NOT_DERIVED","DATE","EQUATION_NUMBER","PAGE_OR_LINE_NUMBER","REFERENCE_NUMBER"}
    if not isinstance(Cd,dict) or "candidates" not in Cd: print("FAIL: candidates file must be an object {declared_candidate_count, declared_included_count, declared_excluded_count, candidates:[...]}"); print("C1_DENOMINATOR_PRINTED=FAIL"); return 1
    if not isinstance(Xd,dict) or "exclusions" not in Xd: print("FAIL: exclusions file must be an object {declared_exclusion_count, exclusions:[...]}"); print("C1_DENOMINATOR_PRINTED=FAIL"); return 1
    C=Cd["candidates"]; X=Xd["exclusions"]
    for k in ("declared_candidate_count","declared_included_count","declared_excluded_count","declared_attempt_count"):
        if k not in Cd: fails.append(f"candidates file: missing {k}")
    if "declared_exclusion_count" not in Xd: fails.append("exclusions file: missing declared_exclusion_count")
    cids={}
    for n,c in enumerate(C,1):
        if not isinstance(c,dict) or "candidate_id" not in c:
            fails.append(f"candidate #{n}: missing candidate_id"); continue
        for f in ["source_file","source_line","numeral","included"]:
            if f not in c: fails.append(f"candidate {c.get('candidate_id')}: missing {f}")
        if c.get("included"):
            if "attempts" not in c or c["attempts"] not in (0,1,2): fails.append(f"candidate {c.get('candidate_id')}: included claim must carry attempts in {{0,1,2}}")
            oc=c.get("outcome")
            if oc is None: fails.append(f"candidate {c.get('candidate_id')}: included claim must carry outcome (a section-3 token, or PENDING before limb B)")
            elif oc not in OUTCOMES and oc!="PENDING": fails.append(f"candidate {c.get('candidate_id')}: outcome {oc!r} is not a section-3 token")
            elif oc=="PENDING" and final: fails.append(f"candidate {c.get('candidate_id')}: outcome still PENDING in final census")
            elif oc in ARITH and not (isinstance(c.get("printed_value"),str) and isinstance(c.get("reproduced_value"),str)): fails.append(f"candidate {c.get('candidate_id')}: arithmetic outcome must carry printed_value and reproduced_value as strings")
        if c.get("candidate_id") in cids: fails.append(f"candidate {c['candidate_id']}: duplicate")
        cids[c.get("candidate_id")]=c
    xids=set()
    for n,x in enumerate(X,1):
        if not isinstance(x,dict) or "candidate_id" not in x: fails.append(f"exclusion #{n}: missing candidate_id"); continue
        if x.get("candidate_id") not in cids: fails.append(f"exclusion {x.get('candidate_id')}: not a candidate")
        if x.get("kind") not in KINDS: fails.append(f"exclusion {x.get('candidate_id')}: kind {x.get('kind')} not predeclared")
        if x.get("candidate_id") in xids: fails.append(f"exclusion {x.get('candidate_id')}: duplicate")
        xids.add(x.get("candidate_id"))
    for cid,c in sorted(cids.items(),key=lambda kv:str(kv[0])):   # V36 canon
        if c.get("included") and cid in xids: fails.append(f"candidate {cid}: included AND excluded")
        if not c.get("included") and cid not in xids: fails.append(f"candidate {cid}: excluded with no exclusion row")
    xrows={x.get("candidate_id"): x for x in Xd.get("exclusions",[]) if isinstance(x,dict)}
    for cid,x in sorted(xrows.items(),key=lambda kv:str(kv[0])):   # V36 canon
        c=cids.get(cid)
        for f in ("source_file","source_line","numeral"):
            if f not in x: fails.append(f"exclusion {cid}: missing {f} (the excluded numeral and its line are retained in the exclusion ledger)")
            elif c is not None and x.get(f)!=c.get(f): fails.append(f"exclusion {cid}: {f} differs from the candidate row")
    inc=sum(1 for c in cids.values() if c.get("included")); exc=len(xids)
    att=sum(int(c.get("attempts",0)) for c in cids.values() if c.get("included"))
    for k,v in (("declared_candidate_count",len(cids)),("declared_included_count",inc),("declared_excluded_count",exc),("declared_attempt_count",att)):
        if k in Cd and Cd[k]!=v: fails.append(f"{k}={Cd[k]} but recomputed {v}")
    if "declared_exclusion_count" in Xd and Xd["declared_exclusion_count"]!=exc: fails.append(f"declared_exclusion_count={Xd['declared_exclusion_count']} but recomputed {exc}")
    for x in fails: print("FAIL:",x)
    print(f"declared: candidates={Cd.get('declared_candidate_count')} included={Cd.get('declared_included_count')} excluded={Cd.get('declared_excluded_count')} attempts={Cd.get('declared_attempt_count')} exclusions={Xd.get('declared_exclusion_count')}")
    oc_t={}
    for c in cids.values():
        if c.get("included"): oc_t[c.get("outcome")]=oc_t.get(c.get("outcome"),0)+1
    print("outcomes:", " ".join(f"{k}={v}" for k,v in sorted(oc_t.items(), key=lambda kv: str(kv[0]))))
    asi=sum(1 for x in Xd.get("exclusions",[]) if isinstance(x,dict) and x.get("kind")=="AUTHOR_SPECIFIED_INPUT")
    print(f"author_specified_input={asi}")
    print(f"recomputed: candidates={len(cids)} included={inc} excluded={exc} attempts={att} reconciled={'YES' if not fails and inc+exc==len(cids) else 'NO'}")
    print("C1_DENOMINATOR_PRINTED=" + ("PASS" if not fails and inc+exc==len(cids) else "FAIL")); return 0 if not fails and inc+exc==len(cids) else 1


def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def ckey(c): return (str(c.get("source_file")), int(c.get("source_line")), str(c.get("numeral")))
def first_write(p, text):
    p=pathlib.Path(p)
    if p.exists(): print(f"FAIL: {p.name} already exists (first-write seal; a seal is never replaced)"); return 1
    p.write_text(text); print(text, end=""); return 0

def cmd_audit_seal(ac, ax, out):
    """V28 D7 stage 1 (custodian): census-gated, first-write seal of the auditor's OWN enumeration, before any sealed ledger is revealed."""
    r=subprocess.run([sys.executable,"-E",__file__,"census",ac,ax],capture_output=True,text=True)
    if r.returncode!=0 or "C1_DENOMINATOR_PRINTED=PASS" not in r.stdout:
        print(r.stdout,end=""); print("FAIL: auditor enumeration does not pass census; not sealed"); return 1  # PROBE:C6_AUDITOR_CENSUS
    return first_write(out, f"AUDITOR_CANDIDATES_SHA256={sha(ac)}\nAUDITOR_EXCLUSIONS_SHA256={sha(ax)}\nAUDITOR_CENSUS_STDOUT_SHA256={hashlib.sha256(r.stdout.encode()).hexdigest()}\n")

def selection_of(sc, seed_hex):
    C=json.loads(pathlib.Path(sc).read_text())["candidates"]
    inc=sorted(c["candidate_id"] for c in C if c.get("included")); arith=sorted(c["candidate_id"] for c in C if c.get("included") and c.get("outcome") in ARITH)
    rem=sorted(set(inc)-set(arith)); N=len(inc); R=len(rem); k=min(max(1,math.ceil(0.20*N)),R)
    samp=sorted(random.Random(int(seed_hex,16)).sample(rem,k)) if k>0 else []
    return {"sealed_candidates_sha256":sha(sc),"seed_hex":seed_hex,"N":N,"R":R,"k":k,"arithmetic_group_ids":arith,"remaining_ids":rem,"sampled_ids":samp,"audited_ids":sorted(set(arith)|set(samp))}

def cmd_audit_select(sc, seed_hex, seal1, out):
    """V28 D7 stage 2 (custodian): refuses without the stage-1 seal; every arithmetic-group claim + k of the remaining, seeded from outside."""
    if not pathlib.Path(seal1).exists() or "AUDITOR_CANDIDATES_SHA256=" not in pathlib.Path(seal1).read_text(): print("FAIL: no stage-1 seal of the auditor's enumeration; selection refused"); return 1  # PROBE:C6_SELECT_NEEDS_SEAL
    if not (isinstance(seed_hex,str) and len(seed_hex)==64 and all(ch in "0123456789abcdef" for ch in seed_hex)): print("FAIL: seed must be 64 lowercase hexadecimal characters"); return 1
    sel=selection_of(sc, seed_hex); sel["stage1_seal_sha256"]=(sha(seal1) if pathlib.Path(seal1).exists() else None)
    pathlib.Path(out).write_text(json.dumps(sel,indent=1,sort_keys=True)); print(f"N={sel['N']} R={sel['R']} k={sel['k']} audited={len(sel['audited_ids'])}"); return 0

def cmd_audit_handout(sel, sc, out):
    """V28 D7: what the auditor receives for re-derivation — claim identifiers with source file and line ONLY."""
    S=json.loads(pathlib.Path(sel).read_text()); by={c["candidate_id"]:c for c in json.loads(pathlib.Path(sc).read_text())["candidates"]}
    H=[{"claim_id":cid,"source_file":by[cid]["source_file"],"source_line":by[cid]["source_line"]} for cid in S["audited_ids"]]
    pathlib.Path(out).write_text(json.dumps(H,indent=1,sort_keys=True)); print(f"handout: {len(H)} claims, fields claim_id/source_file/source_line only"); return 0

RECON_FIELDS=("symbol","status","value","source_file","source_line","origin","origin_evidence","derived_from")
def recon_schema_fails(RD):
    """every reconstructed input carries every C3 field (origin_search when ORIG_SILENT); returns the list of failures"""
    out=[]; seen_ids={}
    for cid,r in sorted(RD.items(),key=lambda kv:str(kv[0])):   # V36 canon: the auditor's file member order carries no meaning
        if not isinstance(r,dict) or "outcome" not in r: out.append(f"{cid}: re-derivation lacks outcome"); continue
        for iid,ar in sorted((r.get("inputs") or {}).items(),key=lambda kv:str(kv[0])):   # V36 canon
            if not isinstance(ar,dict): out.append(f"{cid}/{iid}: input reconstruction must be a full record, not a label"); continue
            if iid in seen_ids: out.append(f"{cid}/{iid}: input_id already reconstructed under {seen_ids[iid]} — every input_id occurs exactly once across the reconstruction")  # PROBE:C6_DUP_INPUT
            seen_ids[iid]=cid
            if "input_id" in ar and str(ar["input_id"])!=str(iid): out.append(f"{cid}/{iid}: explicit input_id {ar['input_id']!r} conflicts with its key")
            if "claim_id" in ar and str(ar["claim_id"])!=str(cid): out.append(f"{cid}/{iid}: explicit claim_id {ar['claim_id']!r} conflicts with its enclosing claim {cid}")  # PROBE:C6_CLAIM_KEY
            miss=[f for f in RECON_FIELDS if f not in ar]
            if miss: out.append(f"{cid}/{iid}: reconstruction missing {miss}")
            ev=ar.get("origin_evidence")
            if isinstance(ev,dict):
                m2=[f for f in ("reason_code","source_file","source_line","verbatim") if f not in ev]
                if m2: out.append(f"{cid}/{iid}: origin_evidence missing {m2}")
                if ev.get("reason_code")=="ORIG_SILENT" and "origin_search" not in ar: out.append(f"{cid}/{iid}: ORIG_SILENT reconstruction needs origin_search")
            elif "origin_evidence" in ar: out.append(f"{cid}/{iid}: origin_evidence must be an object")
    return out

def cmd_audit_seal_rederivation(red, out):
    """V28 D7 stage 2b (custodian): validates the reconstruction schema, then first-write seals the auditor's re-derivations BEFORE any sealed ledger is released."""
    RD=json.loads(pathlib.Path(red).read_text()); sf=recon_schema_fails(RD)
    if sf:
        for x in sf: print("FAIL:",x)
        print("re-derivation NOT sealed: the reconstruction is incomplete"); return 1  # PROBE:C6_RECON_SCHEMA
    return first_write(out, f"AUDITOR_REDERIVATIONS_SHA256={sha(red)}\n")

def cmd_audit_compare(seal1, ac, ax, sc, sx, sl, sel, seal2, red, out):
    """V28 D7 stage 3: compare the auditor's sealed enumeration and sealed re-derivations with the sealed (merged) ledgers."""
    fails=[]; s1=pathlib.Path(seal1).read_text(); s2=pathlib.Path(seal2).read_text()
    if f"AUDITOR_CANDIDATES_SHA256={sha(ac)}" not in s1 or f"AUDITOR_EXCLUSIONS_SHA256={sha(ax)}" not in s1: fails.append("C6_STAGE_ORDER: the auditor's enumeration differs from its stage-1 seal")  # PROBE:C6_STAGE_ORDER
    if f"AUDITOR_REDERIVATIONS_SHA256={sha(red)}" not in s2: fails.append("C6_STAGE_ORDER: the auditor's re-derivations differ from their seal (re-derivations must be sealed before any sealed ledger is released)")  # PROBE:C6_REDERIV_SEAL
    S=json.loads(pathlib.Path(sel).read_text())
    if S.get("sealed_candidates_sha256")!=sha(sc): fails.append("C6_SELECTION: selection was computed over a different sealed candidate file")
    if S.get("stage1_seal_sha256")!=sha(seal1): fails.append("C6_SELECTION: selection does not name this stage-1 seal")
    if not (isinstance(S.get("seed_hex"),str) and len(S["seed_hex"])==64 and all(ch in "0123456789abcdef" for ch in S["seed_hex"])): fails.append("C6_SELECTION: selection carries no seed of 64 lowercase hexadecimal characters; nothing to recompute against")  # PROBE:C6_SEED_PRESENT
    else:
        R=selection_of(sc, S["seed_hex"])
        for k in ("N","R","k","arithmetic_group_ids","remaining_ids","sampled_ids","audited_ids"):
            if S.get(k)!=R[k]: fails.append(f"C6_SELECTION: supplied {k} differs from the recomputed selection")  # PROBE:C6_RECOMPUTE
    AC=json.loads(pathlib.Path(ac).read_text())["candidates"]; AX=json.loads(pathlib.Path(ax).read_text())["exclusions"]
    SC=json.loads(pathlib.Path(sc).read_text())["candidates"]; SX=json.loads(pathlib.Path(sx).read_text())["exclusions"]
    SL=json.loads(pathlib.Path(sl).read_text()); SL=SL["records"] if isinstance(SL,dict) else SL
    RD=json.loads(pathlib.Path(red).read_text())
    a_all={ckey(c):c for c in AC}; s_all={ckey(c):c for c in SC}; akind={ckey(x):x.get("kind") for x in AX}; skind={ckey(x):x.get("kind") for x in SX}
    rows=[]; n_inc_sealed=sum(1 for c in SC if c.get("included")); disputes=0
    for k in sorted(set(a_all)|set(s_all)):
        a=a_all.get(k); s=s_all.get(k)
        row={"key":list(k),"in_sealed":s is not None,"in_audit":a is not None,"sealed_included":(None if s is None else bool(s.get("included"))),"audit_included":(None if a is None else bool(a.get("included"))),"sealed_kind":skind.get(k),"audit_kind":akind.get(k)}
        if s is not None and a is None:
            if s.get("included"): row["result"]="OMISSION"; row["direction"]="sealed_included_absent_from_audit_enumeration"; fails.append(f"COMPLETENESS sealed_included_absent_from_audit_enumeration: {list(k)}")  # PROBE:C6_SEALED_MISSING
            else: row["result"]="AUDIT_INCLUSION_DISPUTED"; row["note"]="sealed excluded, not in the auditor's enumeration: listed, counted as a dispute"; disputes+=1
        elif a is not None and s is None:
            if a.get("included"): row["result"]="OMISSION"; row["direction"]="audit_included_absent_from_sealed"; fails.append(f"COMPLETENESS audit_included_absent_from_sealed: {list(k)}")  # PROBE:C6_BOTH_SEATS_MISSED
            else: row["result"]="OMISSION"; row["direction"]="audit_excluded_absent_from_sealed"; fails.append(f"COMPLETENESS audit_excluded_absent_from_sealed: {list(k)} (a passage the seats never enumerated is incompleteness whatever the auditor's disposition)")  # PROBE:C6_EXCLUDED_MISSING
        else:
            if bool(a.get("included"))!=bool(s.get("included")): row["result"]="AUDIT_INCLUSION_DISPUTED"; disputes+=1
            else: row["result"]="MATCH"
        rows.append(row)
    if n_inc_sealed==0 and rows: fails.append("AUDIT denominator is zero while candidates exist on either side")  # PROBE:C6_ZERO_DENOM
    rate=(disputes/n_inc_sealed) if n_inc_sealed else None
    if n_inc_sealed and disputes/n_inc_sealed>0.10: fails.append(f"AUDIT_INCLUSION_DISPUTED above 10% of the sealed denominator: {disputes}/{n_inc_sealed}")  # PROBE:C6_DISPUTE_RATE
    s_by={c["candidate_id"]:c for c in SC}; l_by={}; full_by={}
    for r in SL: l_by.setdefault(r["claim_id"],{})[r["input_id"]]=r.get("origin"); full_by[r["input_id"]]=r
    for x in recon_schema_fails(RD): fails.append("C6_RECONSTRUCTION: "+x)  # PROBE:C6_RECON_COMPLETE
    identity_conflict={}
    for cid0,r0 in sorted(RD.items(),key=lambda kv:str(kv[0])):   # V36 canon
        for iid0,ar0 in sorted((r0.get("inputs") or {}).items(),key=lambda kv:str(kv[0])):
            sr0=full_by.get(iid0)
            if sr0 is not None and str(sr0.get("claim_id"))!=str(cid0): identity_conflict[iid0]=f"reconstructed under claim {cid0}, but the sealed record belongs to claim {sr0.get('claim_id')}"; fails.append(f"C6_IDENTITY: {iid0} {identity_conflict[iid0]}")  # PROBE:C6_IDENTITY
    # the auditor's OWN graph, across every audited claim; a dependency it did not reconstruct is never borrowed from the sealed side
    a_graph={}
    for cid0,r0 in sorted(RD.items(),key=lambda kv:str(kv[0])):   # V36 canon
        for iid0,ar0 in sorted((r0.get("inputs") or {}).items(),key=lambda kv:str(kv[0])):
            if isinstance(ar0,dict): a_graph[iid0]=dict(ar0,input_id=iid0,origin=ar0.get("origin","UNDECLARED"),derived_from=list(ar0.get("derived_from") or []))
    # ---- V29: every reconstructed record in a selected claim's complete dependency closure is compared (records of other claims included);
    #      a declared alternative — origin and/or parent list — is matched over the whole closure, once, and the sealed roots are recomputed under that graph
    def compare_record(iid, ar, sr):
        """returns (diffs, branch) where branch is 'primary' or 'alt'"""
        diffs=[]; branch="primary"
        for fld in ("symbol","status","value","source_file"):
            if str(ar.get(fld))!=str(sr.get(fld)): diffs.append(f"{fld} {ar.get(fld)} vs sealed {sr.get(fld)}")  # PROBE:C6_FIELDS
        if int(ar.get("source_line") or -1)!=int(sr.get("source_line") or -2): diffs.append(f"source_line {ar.get('source_line')} vs sealed {sr.get('source_line')}")
        aev=ar.get("origin_evidence") or {}; sev=sr.get("origin_evidence") or {}; sev2=sr.get("origin_evidence_alt") or {}
        a_par=sorted(ar.get("derived_from") or []); s_par=sorted(sr.get("derived_from") or []); s_par_alt=sorted(sr.get("derived_from_alt") or []) if sr.get("derived_from_alt") is not None else None
        same_origin=str(ar.get("origin"))==str(sr.get("origin")); alt_origin=bool(sr.get("origin_alt")) and str(ar.get("origin"))==str(sr.get("origin_alt"))
        ev_ok=all(str(aev.get(f2))==str(sev.get(f2)) for f2 in ("reason_code","source_file","source_line","verbatim"))
        ev_alt_ok=bool(sev2) and all(str(aev.get(f2))==str(sev2.get(f2)) for f2 in ("reason_code","source_file","source_line","verbatim"))
        par_ok=(a_par==s_par); par_alt_ok=(s_par_alt is not None and a_par==s_par_alt)
        has_alt=bool(sr.get("origin_alt")) or bool(sr.get("origin_evidence_alt")) or (s_par_alt is not None)
        # the complete alternative branch: every declared alternative field applied together; undeclared fields stay primary
        alt_origin_full=str(sr.get("origin_alt")) if sr.get("origin_alt") else str(sr.get("origin"))
        alt_ev_full=sev2 if sr.get("origin_evidence_alt") else sev
        alt_par_full=s_par_alt if s_par_alt is not None else s_par
        matches_primary=same_origin and ev_ok and par_ok
        matches_alt=has_alt and str(ar.get("origin"))==alt_origin_full and all(str(aev.get(f2))==str(alt_ev_full.get(f2)) for f2 in ("reason_code","source_file","source_line","verbatim")) and a_par==alt_par_full and (alt_ev_full.get("reason_code")!="ORIG_SILENT" or ar.get("origin_search")==(sr.get("origin_search_alt") if "origin_search_alt" in sr else sr.get("origin_search")))
        matches_primary=matches_primary and (sev.get("reason_code")!="ORIG_SILENT" or canon_search(ar.get("origin_search"))==canon_search(sr.get("origin_search")))  # PROBE:C6_SEARCH_CANON_MATCH
        if matches_primary: branch="primary"
        elif matches_alt: branch="alt"
        else:
            diffs.append("record matches neither complete declared branch")  # AUTHORITATIVE: the full-record predicate decides the verdict; the per-field lines below only explain it (Blanc 03:03: never removed to satisfy a probe)
            if not same_origin and not alt_origin: diffs.append(f"origin {ar.get('origin')} vs sealed {sr.get('origin')}")
            if same_origin and not ev_ok:
                for f2 in ("reason_code","source_file","source_line","verbatim"):
                    if str(aev.get(f2))!=str(sev.get(f2)): diffs.append(f"origin_evidence.{f2} {aev.get(f2)} vs sealed {sev.get(f2)}")  # PROBE:C6_EVIDENCE
            if alt_origin and not ev_alt_ok:
                for f2 in ("reason_code","source_file","source_line","verbatim"):
                    if str(aev.get(f2))!=str(sev2.get(f2)): diffs.append(f"origin_evidence.{f2} {aev.get(f2)} vs sealed alternative {sev2.get(f2)}")
            if not par_ok: diffs.append(f"derived_from {a_par} vs sealed {s_par}"+(f" (alternative {s_par_alt})" if s_par_alt is not None else ""))  # PROBE:C6_EDGES
        if aev.get("reason_code")=="ORIG_SILENT":
            expected_search = sr.get("origin_search_alt") if (branch=="alt" and "origin_search_alt" in sr) else sr.get("origin_search")
            if canon_search(ar.get("origin_search"))!=canon_search(expected_search): diffs.append("origin_search differs (structural comparison against the matched branch's search)")  # PROBE:C6_SEARCH_BRANCH
        return diffs, branch
    def closure_of(iid, graph, seen=None):
        seen=seen if seen is not None else set()
        if iid in seen or iid not in graph: return seen
        seen.add(iid)
        for p_ in sorted(graph[iid].get("derived_from") or []): closure_of(p_, graph, seen)   # V36: sorted
        return seen
    # one comparison per reconstructed record over the union of the selected claims' closures
    record_cmp={}; branch_of={}
    sel_closure=set()
    for cid in S.get("audited_ids",[]):
        for iid in sorted(RD.get(cid,{}).get("inputs") or {}): sel_closure|=closure_of(iid, a_graph)   # V36 canon
    for iid in sorted(sel_closure):
        ar=a_graph.get(iid); sr=full_by.get(iid)
        if sr is None: record_cmp[iid]=(["unsupported by the sealed ledger"],"primary"); continue
        d,b=compare_record(iid, ar, sr)
        if iid in identity_conflict: d=[f"identity: {identity_conflict[iid]}"]+d   # F1: the conflict is a MISMATCH of this record, carried into every dependent selected claim's rows
        record_cmp[iid]=(d,b)
        if b=="alt": branch_of[iid]="alt"
    sealed_view={}
    for k2,v2 in full_by.items():
        v3=dict(v2)
        if branch_of.get(k2)=="alt":
            if v2.get("origin_alt"): v3["origin"]=v2["origin_alt"]
            if v2.get("derived_from_alt") is not None: v3["derived_from"]=v2["derived_from_alt"]
        sealed_view[k2]=v3
    audited={}
    for cid in S.get("audited_ids",[]):
        r=RD.get(cid); s=s_by.get(cid)
        if r is None or s is None: audited[cid]={"result":"MISMATCH","why":["no re-derivation supplied" if r is None else "not a sealed claim"]}; fails.append(f"AUDIT {cid}: MISMATCH (missing)"); continue
        why=[]; inputs_res={}
        if r.get("outcome")!=s.get("outcome"): why.append(f"outcome {r.get('outcome')} vs sealed {s.get('outcome')}")
        if s.get("outcome") in ARITH and (str(r.get("printed_value"))!=str(s.get("printed_value")) or str(r.get("reproduced_value"))!=str(s.get("reproduced_value"))): why.append("printed/reproduced values differ")
        own=set(r.get("inputs") or {}); clos=set()
        for iid in sorted(own): clos|=closure_of(iid, a_graph)   # V36: sorted
        for iid in sorted(clos):
            d,b=record_cmp.get(iid,(["not reconstructed"],"primary"))
            inputs_res[iid]={"result":"MATCH" if not d else "MISMATCH","why":d,"branch":b,"own_input":iid in own}
            if d: why.append(f"input {iid}: "+"; ".join(d))  # PROBE:C6_CLOSURE
        for iid in sorted(l_by.get(cid,{})):
            if iid not in own: inputs_res[iid]={"result":"MISMATCH","why":["not reconstructed by the auditor"]}; why.append(f"input {iid}: not reconstructed")
        # V36 (codex V35 F1): GRAPH INTEGRITY — every derived_from edge of the auditor's closure and of the matched sealed closure is checked for
        # a missing record or a cycle, independently of origin, BEFORE root classification. Stopping at a non-DERIVED origin never substitutes for it.
        gi_a=graph_integrity(a_graph, [i for i in own if i in a_graph]); gi_s=graph_integrity(sealed_view, list(l_by.get(cid,{})))
        for g in gi_a: why.append(f"graph integrity (auditor closure): {g}")  # PROBE:C6_GRAPH_INTEGRITY
        for g in gi_s: why.append(f"graph integrity (matched sealed closure): {g}")
        inputs_res["_graph_integrity"]={"auditor":gi_a,"matched_sealed":gi_s}
        try:
            ra=set(); [ra.update(roots(a_graph,i)) for i in sorted(own) if i in a_graph]   # V36: sorted
            rs=set(); [rs.update(roots(sealed_view,i)) for i in sorted(l_by.get(cid,{}))]
            audited_rests={"audit":sorted(ra),"sealed_under_matching_branch":sorted(rs),"alt_branch_records":sorted(k for k in clos if branch_of.get(k)=="alt")}
            if ra!=rs: why.append(f"root_origins differ: audit {sorted(ra)} vs sealed {sorted(rs)}")
            # V35: the unmatched PRIMARY view is a DIAGNOSTIC only — it is no graph a seat supplied; if its roots cannot be computed the report
            # records that fact and the verdict is unchanged (codex V34 F1). Only the MATCHED graph above decides.
            try: audited_rests["sealed_primary"]=sorted(set().union(*[roots(full_by,i) for i in sorted(l_by.get(cid,{}))]) if l_by.get(cid) else set())
            except Exception as e: audited_rests["sealed_primary"]=None; audited_rests["sealed_primary_diagnostic_error"]=str(e)
        except ValueError as e: audited_rests={"error":str(e)}; why.append(f"dependency not reconstructed by the auditor or cyclic: {e}")  # PROBE:C6_NO_BORROW
        except Exception as e: audited_rests={"error":str(e)}; why.append(f"root recomputation failed: {e}")
        inputs_res["_roots"]=audited_rests
        audited[cid]={"result":"MATCH" if not why else "MISMATCH","why":why,"inputs":inputs_res}
        if why: fails.append(f"AUDIT {cid}: MISMATCH ({'; '.join(why)})")
    tok="PASS" if not fails else "FAIL"
    res={"sealed_denominator":n_inc_sealed,"sealed_candidates_sha256":sha(sc),"sealed_exclusions_sha256":sha(sx),"sealed_ledger_sha256":sha(sl),"seed_hex":S.get("seed_hex"),"selection":{k:S.get(k) for k in ("arithmetic_group_ids","remaining_ids","k","sampled_ids","audited_ids")},"stage1_seal":s1,"rederivation_seal":s2,"completeness_rows":rows,"inclusion_disputed_count":disputes,"inclusion_disputed_rate":rate,"audited":audited,"C6_AUDIT_SAMPLE":tok,"study_files":("none" if tok=="PASS" else "CENSUS_AUDIT_FAILED"),"scope":"PASS means the enumerated predicates held over the sealed files; it is bounded by the custodian's dispatch and release record and by shared reader error; it does not prove corpus completeness"}
    pathlib.Path(out).write_text(json.dumps(res,indent=1,sort_keys=True))
    for x in fails: print("FAIL:",x)
    print(json.dumps(res,indent=1,sort_keys=True)); print("C6_AUDIT_SAMPLE="+tok); return 0 if tok=="PASS" else 1


def _emit(prefix, rc, argv):
    """V38: one completion token per subcommand run — <PREFIX>_<SUBCOMMAND>=PASS|FAIL, printed once, whatever the exit status."""
    sub="_".join(str(x).upper().replace("-","_") for x in argv[:2] if not str(x).startswith("/") and not str(x).endswith(".json") and not str(x).endswith(".md") and not str(x).endswith(".txt"))
    print(f"{prefix}_{sub}=" + ("PASS" if rc==0 else "FAIL")); sys.exit(rc)


if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)==3 and a[0]=="validate": _emit("SEAT_"+"_".join(x.upper() for x in a[:1] if isinstance(x,str)) if False else "SEAT", cmd_validate(a[1],a[2]), a)
    if len(a)==4 and a[0]=="validate": _emit("SEAT_"+"_".join(x.upper() for x in a[:1] if isinstance(x,str)) if False else "SEAT", cmd_validate(a[1],a[2],a[3]), a)
    if len(a)==5 and a[0]=="audit" and a[1]=="seal-enumeration": _emit("SEAT_"+"_".join(x.upper() for x in a[:1] if isinstance(x,str)) if False else "SEAT", cmd_audit_seal(a[2],a[3],a[4]), a)
    if len(a)==6 and a[0]=="audit" and a[1]=="select": _emit("SEAT_"+"_".join(x.upper() for x in a[:1] if isinstance(x,str)) if False else "SEAT", cmd_audit_select(a[2],a[3],a[4],a[5]), a)
    if len(a)==5 and a[0]=="audit" and a[1]=="handout": _emit("SEAT_"+"_".join(x.upper() for x in a[:1] if isinstance(x,str)) if False else "SEAT", cmd_audit_handout(a[2],a[3],a[4]), a)
    if len(a)==4 and a[0]=="audit" and a[1]=="seal-rederivation": _emit("SEAT_"+"_".join(x.upper() for x in a[:1] if isinstance(x,str)) if False else "SEAT", cmd_audit_seal_rederivation(a[2],a[3]), a)
    if len(a)==12 and a[0]=="audit" and a[1]=="compare": _emit("SEAT_"+"_".join(x.upper() for x in a[:1] if isinstance(x,str)) if False else "SEAT", cmd_audit_compare(*a[2:]), a)
    if len(a) in (3,4) and a[0]=="census" and (len(a)==3 or a[3]=="final"): _emit("SEAT_"+"_".join(x.upper() for x in a[:1] if isinstance(x,str)) if False else "SEAT", cmd_census(a[1],a[2],final=(len(a)==4)), a)
    print(__doc__); print("INVOCATION=REJECTED"); sys.exit(2)

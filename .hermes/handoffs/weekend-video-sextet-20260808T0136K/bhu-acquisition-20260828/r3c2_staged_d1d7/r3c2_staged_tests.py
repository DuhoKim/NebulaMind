#!/usr/bin/env python3
"""r3c2_staged_tests.py — controls for the STAGED (UNADOPTED) D1/D7/batch tooling, repaired 2026-09-06 after two independent reviews.
Every negative asserts the EXACT failure set (count and text); every load-bearing check has a DELETION PROBE (the check is replaced by a
no-op in a copy of the tool; the negative must then PASS). Run from this directory: /usr/bin/python3 -E r3c2_staged_tests.py"""
import json, subprocess, sys, pathlib, hashlib, shutil, re, os
H=pathlib.Path(__file__).resolve().parent; PY="/usr/bin/python3"; SEAT=H/"r3c2_ledger_tools_STAGED.py"; BATCH=H/"r3c2_batch_tools_STAGED.py"
W=H/"_ctl"; shutil.rmtree(W,ignore_errors=True); W.mkdir()
def w(p,obj): p=W/p; p.write_text(json.dumps(obj,indent=1,sort_keys=True) if not isinstance(obj,str) else obj); return str(p)
def run(tool,*a): r=subprocess.run([PY,"-E",str(tool),*[str(x) for x in a]],capture_output=True,text=True); return r.returncode, r.stdout+r.stderr
def sha_s(s): return hashlib.sha256(s.encode()).hexdigest()
results=[]; EX=[]; NPROBES=0
# ================= THE EXACT-RESULT EVALUATOR (Blanc 2026-09-07 09:07; codex V37 F3-continued) =================
# ONE evaluator, used by EVERY outcome judge in this kit — no per-helper variants, no optional fields, no substring matching.
# It requires: setup succeeded (no traceback, import or launch error, non-empty output); the EXACT exit code; a completion token
# line, never optional; exactly the expected diagnostic rows, in emitted order, compared as COMPLETE ROWS against the pinned
# expectation table `r3c2_exact_rows.json`; and, additionally for deletion probes, that the targeted diagnostic is ABSENT while the
# exact remaining rows of the unprobed run are retained. A crash, an unrelated failure, a wrong diagnostic or an undeleted
# diagnostic can never satisfy a control. Production guards are never weakened to make a probe pass.
SETUP_ERRORS=("Traceback (most recent call last)","ModuleNotFoundError","ImportError:","SyntaxError","No such file or directory","command not found","Permission denied","can\'t open file")
TOKEN_LINE=re.compile(r"^[A-Z][A-Z0-9_]*=[A-Za-z0-9_.:/+-]+$",re.M)
CAPTURE = os.environ.get("NM_KIT_CAPTURE")=="1"
EXACT_PATH = H/"r3c2_exact_rows.json"
EXACT_ROWS = json.loads(EXACT_PATH.read_text()) if (EXACT_PATH.exists() and not CAPTURE) else {}
_CAPTURED={}; _SEEN={}
def norm_row(l):
    return l.replace(str(W),"<W>").replace(str(H),"<H>").replace(str(H.parent),"<LANE>")
def setup_ok(out):
    if not (out or "").strip(): return "empty output — no evidence the case ran"
    for e in SETUP_ERRORS:
        if e in out: return f"setup/launch/traceback failure in output: {e!r}"
    return ""
def judge(name, rc, out, want_rc, want_fails, token=None):
    """the one evaluator; returns (ok, why)"""
    why=setup_ok(out)
    if why: return False,why
    if rc!=want_rc: return False,f"exit {rc} != expected {want_rc}"
    if token is not None and token not in out: return False,f"declared completion token {token!r} absent"
    if not TOKEN_LINE.search(out): return False,"no completion token line in the output — a subcommand without one cannot serve as control evidence"
    rows=[norm_row(l) for l in out.splitlines() if l.startswith("FAIL:")]
    if len(rows)!=len(want_fails): return False,f"{len(rows)} diagnostic rows, expected exactly {len(want_fails)}: {rows}"
    for i,(row,want) in enumerate(zip(rows,want_fails)):
        if want not in row: return False,f"diagnostic row {i+1} is {row!r}, which does not carry the declared expectation {want!r}"
    key=name+"#"+str(_SEEN.get(name,0)); _SEEN[name]=_SEEN.get(name,0)+1
    if CAPTURE: _CAPTURED[key]=rows; return True,""
    if key not in EXACT_ROWS: return False,f"no pinned exact rows for {key!r} — every judged control must have its complete expected text pinned"
    if EXACT_ROWS[key]!=rows: return False,f"diagnostic rows differ from the pinned exact text:\n     pinned: {EXACT_ROWS[key]}\n     actual: {rows}"
    return True,""
def check(name, rc, out, want_rc, want_fails, token=None):
    ok,why=judge(name,rc,out,want_rc,want_fails,token)
    results.append((name,ok)); print(("ok  " if ok else "BAD ")+name+("" if ok else f"\n   {why}\n{out[-500:]}")); return ok
def _unused_check(name, rc, out, want_rc, want_fails, token=None):
    fails=[l for l in out.splitlines() if l.startswith("FAIL:")]
    ok = rc==want_rc and len(fails)==len(want_fails) and all(sum(1 for f in fails if s in f)==1 for s in want_fails) and (token is None or token in out)
    results.append((name,ok)); print(("ok  " if ok else "BAD ")+name+("" if ok else f"\n   rc={rc} fails={fails}\n{out[-700:]}")); return ok
# ================= NEGATIVE-CONTROL PREDICATE (Blanc 2026-09-07 07:58; codex V36 F3) =================
# A NEGATIVE CONTROL MUST ASSERT THE EXACT EXPECTED FAILURE, NEVER THE BARE POLARITY.
# Wherever a control in this kit judges an outcome it requires ALL of:
#   (1) successful setup — no traceback, no import/launch error, no usage banner, and non-empty output;
#   (2) the expected completion token AND the expected exit code;
#   (3) a non-empty selection of EXACTLY the expected rows;
#   (4) that subcase's specific verdicts, diagnostic text and equality results.
# A missing fixture, a traceback, an empty selection, or a failure for an unrelated reason FAILS the kit test; it never satisfies it.

def probe(name, tool, marker, *args, token, want_rc=0, artefact=None, gone_text=None, judge_only=False):
    global NPROBES
    if not judge_only: NPROBES+=1
    src=tool.read_text().splitlines(); hits=[l for l in src if marker in l]; assert len(hits)==1, f"marker {marker} must occur exactly once"
    # the check on the marked line is neutralised in place (its failure call becomes a no-op; its early return is dropped) so the surrounding if/elif structure survives
    def neut(l):
        s2=l.strip()
        if s2.startswith(("elif ","else:","except ","finally:")) or "=" not in s2.split("#")[0] or any(k in l for k in ("fails.append(","print(","diffs.append(","why.append(","out.append(")):
            return l.replace("print(","_probe_noop(").replace("fails.append(","_probe_noop(").replace("diffs.append(","_probe_noop(").replace("why.append(","_probe_noop(").replace("out.append(","_probe_noop(").replace("out_claims.update(","_probe_noop(").replace("disputed_claims.add(","_probe_noop(").replace("; sys.exit(1)","; pass").replace("; return 1","; pass").replace("PROBE:","PROBE-DELETED:")
        return l[:len(l)-len(l.lstrip())]+"pass  # PROBE-DELETED (assignment guard neutralised in place)"
    kept=["_probe_noop=lambda *a,**k: None  # PROBE-DELETED"]+[neut(l) if marker in l else l for l in src]
    t=W/(tool.stem+"_minus_"+marker.split(":")[1]+".py"); t.write_text("\n".join(kept)+"\n")
    rc0,out0=run(tool,*args); base_art=(pathlib.Path(artefact).read_text() if artefact and pathlib.Path(artefact).exists() else None)
    rc,out=run(t,*args); probed_art=(pathlib.Path(artefact).read_text() if artefact and pathlib.Path(artefact).exists() else None)   # baseline vs probed: the probe must REMOVE the check's effect, not merely change a polarity
    def diag(o): return [norm_row(l) for l in o.splitlines() if l.strip() and not TOKEN_LINE.match(norm_row(l))]
    D0,D1=diag(out0),diag(out)
    gone=[l for l in D0 if l not in D1]
    key="probe:"+name
    if CAPTURE: _CAPTURED[key]=gone
    why=(setup_ok(out0) and f"baseline run: {setup_ok(out0)}") or setup_ok(out) \
        or ("" if token in out else f"expected token {token!r} absent after deletion") \
        or ("" if rc==want_rc else f"exit {rc} != expected {want_rc}") \
        or ("" if TOKEN_LINE.search(out) else "no completion token line after deletion") \
        or ("" if (gone or gone_text) else "NO diagnostic vanished — deleting the marked check changed nothing (a relocated marker cannot satisfy a probe)") \
        or ("" if gone_text is None else ("" if (base_art is not None and gone_text in base_art) else f"the declared artefact evidence {gone_text!r} was absent from the UNPROBED artefact")) \
        or ("" if gone_text is None else ("" if (probed_art is not None and gone_text not in probed_art) else f"the declared artefact evidence {gone_text!r} SURVIVED the deletion"))
    if gone_text is not None: pass   # an artefact-effect probe pins its vanished evidence in the call itself
    if not why and not CAPTURE and gone_text is None:
        pinned=EXACT_ROWS.get(key)
        if pinned is None: why=f"no pinned vanished-diagnostic text for {key!r} — a probe must declare exactly what its deletion removes"
        else:
            still=[l for l in pinned if l in D1]; missing=[l for l in pinned if l not in D0]
            if still: why=f"the targeted diagnostic is STILL PRESENT after deletion: {still}"
            elif missing: why=f"the pinned targeted diagnostic never appeared in the unprobed run: {missing}"
    ok=not why
    if judge_only: return ok,why
    results.append((name,ok)); print(("ok  " if ok else "BAD ")+name+("" if ok else f"\n   {why}\n   rc={rc}\n{out[-500:]}"))
def manifest(path, files_dir, files):
    rows="".join(f"| {i+1} | `{f}` | `{hashlib.sha256((files_dir/f).read_bytes()).hexdigest()}` | {(files_dir/f).stat().st_size} | {sum(1 for l in (files_dir/f).read_text().splitlines() if l.strip())} |\n" for i,f in enumerate(files))
    pathlib.Path(path).write_text("# m\n| # | file | sha256 | bytes | non-blank lines |\n|---|---|---|---|---|\n"+rows)
# ================= D1 fixtures
S=W/"src"; S.mkdir()
(S/"paperA.txt").write_text("Title A\nIntro.\nWe adopt a = 2 from paperB (2020).\nThen y = 2a = 4.\n")
(S/"paperB.txt").write_text("Title B\nSee the appendix and b = 20.\n\nSetup.\nFor this calculation we choose a = 2.\nLater we repeat a = 2.\n")
(S/"paperC.txt").write_text("Title C\nwe take a = 2 here\n")
manifest(S/"R3C2_CORPUS_MANIFEST.md", S, ["paperA.txt","paperB.txt"])
CANDS=w("d1_cands.json",{"declared_candidate_count":1,"declared_included_count":1,"declared_excluded_count":0,"declared_attempt_count":1,"candidates":[{"candidate_id":"paperA.txt#1","source_file":"paperA.txt","source_line":4,"numeral":"4","included":True,"attempts":1,"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4"}]})
def rec(**k):
    r={"claim_id":"paperA.txt#1","input_id":"paperA.txt#1.a","symbol":"a","status":"PRINTED","origin":"IMPORTED","origin_evidence":{"reason_code":"ORIG_CITATION","source_file":"paperA.txt","source_line":3,"verbatim":"We adopt a = 2 from paperB (2020)"},"derived_from":[],"value":"2","source_file":"paperB.txt","source_line":5}
    for kk,v in k.items():
        if kk.startswith("ev_"): r["origin_evidence"][kk[3:]]=v
        else: r[kk]=v
    return r
rc,out=run(SEAT,"validate",w("d1_pos.json",{"records":[rec()]}),S,CANDS); check("D1 positive: import whose source line says 'we choose' validates (review's wording: evidence at the borrower)",rc,out,0,[],"C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",W/"d1_pos.json",S); check("D1 neg: validate without the candidate file cannot bind the claiming paper (every PRINTED record)",rc,out,1,["PRINTED record needs the candidate file to bind claim paperA.txt#1"])
probe("D1 probe: deleting the candidate-file requirement turns that negative into PASS",SEAT,"PROBE:D1_NEEDS_CANDIDATES_ALL","validate",W/"d1_pos.json",S,token="C3_NO_SUBSTITUTION=PASS")
CANDS2=w("d1_cands2.json",{"declared_candidate_count":2,"declared_included_count":2,"declared_excluded_count":0,"declared_attempt_count":2,"candidates":json.loads(pathlib.Path(CANDS).read_text())["candidates"]+[{"candidate_id":"paperB.txt#1","source_file":"paperB.txt","source_line":5,"numeral":"2","included":True,"attempts":1,"outcome":"REPRO_NOT_EVALUABLE"}]})
rc,out=run(SEAT,"validate",w("d1_n_ghost.json",{"records":[rec(claim_id="ghost.txt#9",input_id="ghost.txt#9.a",origin="CHOSEN",ev_reason_code="ORIG_CHOICE_STATED",ev_source_file="paperB.txt",ev_source_line=5,ev_verbatim="we choose a = 2")]}),S,CANDS); check("D1 neg (round-3 N1, both reviewers): a non-import PRINTED record whose claim is not a candidate row, value line in another file",rc,out,1,["claim ghost.txt#9 is not a candidate row"])
probe("D1 probe: deleting the unknown-claim check turns that negative into PASS (the record then skips binding entirely)",SEAT,"PROBE:D1_UNKNOWN_CLAIM_ALL","validate",W/"d1_n_ghost.json",S,CANDS,token="C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",w("d1_n_third.json",{"records":[rec(ev_source_file="paperC.txt",ev_source_line=2,ev_verbatim="we take a = 2 here")]}),S,CANDS); check("D1 neg: citing sentence quoted from a third text, not the claiming paper (kimi K5g)",rc,out,1,["citing sentence is in paperC.txt, but claim paperA.txt#1 belongs to paperA.txt"])
probe("D1 probe: deleting the claiming-file binding turns that negative into PASS",SEAT,"PROBE:D1_CLAIMING_FILE","validate",W/"d1_n_third.json",S,CANDS,token="C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",w("d1_n_verb.json",{"records":[rec(ev_source_line=2)]}),S,CANDS); check("D1 neg: verbatim not at the citing sentence (the shared evidence check fires first)",rc,out,1,["quotation not found at evidence line paperA.txt:2"])
probe("D1 probe: deleting the shared quotation check turns that negative into PASS (the neutralised line still skips the record)",SEAT,"PROBE:EV_VERBATIM_ALL","validate",W/"d1_n_verb.json",S,CANDS,token="C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",w("d1_n_empty.json",{"records":[rec(ev_verbatim="")]}),S,CANDS); check("D1 neg: empty quotation (codex; the shared check fires first)",rc,out,1,["empty quotation (every non-ORIG_SILENT record quotes its evidence line)"])
probe("D1 probe: deleting the shared empty-quotation check turns that negative into PASS",SEAT,"PROBE:EV_EMPTY_ALL","validate",W/"d1_n_empty.json",S,CANDS,token="C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",w("d1_n_sub.json",{"records":[rec(source_line=2)]}),S,CANDS); check("D1 neg: value '2' is only a substring of 'b = 20' at line 2 (codex substring attack, symbol a)",rc,out,1,["value 2 is not a numeric token at external value line paperB.txt:2"])
rc,out=run(SEAT,"validate",w("d1_n_tok.json",{"records":[rec(source_line=2,symbol="b",value="2")]}),S,CANDS); check("D1 neg: value token: '2' is not a numeric token of 'b = 20' when line 2 is the only b-line (codex substring attack)",rc,out,1,["value 2 is not a numeric token at external value line paperB.txt:2"])
probe("D1 probe: deleting the token check turns that negative into PASS",SEAT,"PROBE:D1_VALUE_TOKEN","validate",W/"d1_n_tok.json",S,CANDS,token="C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",w("d1_n_second.json",{"records":[rec(source_line=6)]}),S,CANDS); check("D1 neg: a second matching line filed instead of the first (kimi K5d / codex two-line source)",rc,out,1,["external value line 6 is not the first line of paperB.txt carrying both a and 2 (that is line 5)"])
probe("D1 probe: deleting the first-line tie-break turns that negative into PASS",SEAT,"PROBE:D1_FIRST_LINE","validate",W/"d1_n_second.json",S,CANDS,token="C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",w("d1_n_enum.json",{"records":[rec(source_file="paperC.txt",source_line=2)]}),S,CANDS); check("D1 neg: external source not a manifest row",rc,out,1,["external source not an enumerable verified text: paperC.txt is not a row of the manifest"])
probe("D1 probe: deleting the enumerable check turns that negative into PASS",SEAT,"PROBE:D1_ENUMERABLE","validate",W/"d1_n_enum.json",S,CANDS,token="C3_NO_SUBSTITUTION=PASS")
S2=W/"src_tampered"; shutil.copytree(S,S2); (S2/"paperB.txt").write_text((S2/"paperB.txt").read_text()+"tampered\n")
rc,out=run(SEAT,"validate",W/"d1_pos.json",S2,CANDS); check("D1 neg: external source bytes differ from the manifest row",rc,out,1,["bytes ("])
S3=W/"src_nomanifest"; shutil.copytree(S,S3); (S3/"R3C2_CORPUS_MANIFEST.md").unlink()
rc,out=run(SEAT,"validate",W/"d1_pos.json",S3,CANDS); check("D1 neg: no manifest in the sources directory (codex absent-manifest probe)",rc,out,1,["no R3C2_CORPUS_MANIFEST.md in the sources directory"])
rc,out=run(SEAT,"validate",w("d1_n_self.json",{"records":[rec(ev_source_file="paperB.txt",ev_source_line=5,ev_verbatim="we choose a = 2")]}),S,CANDS); check("D1 neg: record names its own file as the external source (two failures: claiming-file and self-file)",rc,out,1,["citing sentence is in paperB.txt, but claim paperA.txt#1 belongs to paperA.txt","names its own file as the external source"])
rc,out=run(SEAT,"validate",w("d1_n_refiled.json",{"records":[rec(origin="CHOSEN",ev_reason_code="ORIG_CHOICE_STATED",ev_source_file="paperB.txt",ev_source_line=5,ev_verbatim="we choose a = 2")]}),S,CANDS); check("D1 neg (codex F4): an import re-filed CHOSEN quoting the source's choice sentence — value line in another file must be IMPORTED/ORIG_CITATION",rc,out,1,["value line is in paperB.txt but claim paperA.txt#1 belongs to paperA.txt: such a record must be IMPORTED with ORIG_CITATION (submitted CHOSEN/ORIG_CHOICE_STATED)"])
probe("D1 probe: deleting the refiled-import check turns that negative into PASS",SEAT,"PROBE:D1_IMPORT_REFILED","validate",W/"d1_n_refiled.json",S,CANDS,token="C3_NO_SUBSTITUTION=PASS")
(S/"paperD.txt").write_text("Title D\nThe total is 9 on the ninth page.\n"); manifest(S/"R3C2_CORPUS_MANIFEST.md", S, ["paperA.txt","paperB.txt","paperD.txt"])
rc,out=run(SEAT,"validate",w("d1_n_nosym.json",{"records":[rec(symbol="g",value="9",source_file="paperD.txt",source_line=2,ev_verbatim="We adopt")]}),S,CANDS); check("D1 neg (codex F5 / kimi F3): no line of the source carries both symbol and numeral — the floor no longer fails open",rc,out,1,["no line of paperD.txt carries both g and 9"])
probe("D1 probe: deleting the no-symbol-line check turns that negative into PASS",SEAT,"PROBE:D1_NO_SYMBOL_LINE","validate",W/"d1_n_nosym.json",S,CANDS,token="C3_NO_SUBSTITUTION=PASS")
manifest(S/"R3C2_CORPUS_MANIFEST.md", S, ["paperA.txt","paperB.txt"])
probe("D1 probe: deleting the self-file check leaves only the claiming-file failure on that negative",SEAT,"PROBE:D1_SELF_FILE","validate",W/"d1_n_self.json",S,CANDS,token="citing sentence is in paperB.txt, but claim paperA.txt#1 belongs to paperA.txt",want_rc=1)
# ---- gate V26cand: codex F1 local import, F3 evidence for every status, F2 empty ledgers / NOT_COMPUTED, F4 dispute propagation
(S/"paperE.txt").write_text("Title E\nWe adopt a = 3 from paperB (2020).\nThen z = 3.\n"); manifest(S/"R3C2_CORPUS_MANIFEST.md", S, ["paperA.txt","paperB.txt","paperE.txt"])
CANDS3=w("d1_cands3.json",{"declared_candidate_count":1,"declared_included_count":1,"declared_excluded_count":0,"declared_attempt_count":1,"candidates":[{"candidate_id":"paperE.txt#1","source_file":"paperE.txt","source_line":3,"numeral":"3","included":True,"attempts":1,"outcome":"REPRO_NOT_EVALUABLE"}]})
loc=rec(claim_id="paperE.txt#1",input_id="paperE.txt#1.a",value="3",source_file="paperE.txt",source_line=2,ev_source_file="paperE.txt",ev_source_line=2,ev_verbatim="We adopt a = 3 from paperB (2020)")
rc,out=run(SEAT,"validate",w("d1_local_pos.json",{"records":[loc]}),S,CANDS3); check("gate F1 (codex): a LOCALLY printed cited value ('We adopt a = 3 from paperB' printed by the claiming paper) validates as IMPORTED at its own line",rc,out,0,[],"C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",w("d1_local_neg.json",{"records":[dict(loc,value="4")]}),S,CANDS3); check("gate F1 neg: local import whose value is not a token at its own line",rc,out,1,["value 4 is not a numeric token at paperE.txt:2"])
probe("gate F1 probe: deleting the local value check turns that negative into PASS",SEAT,"PROBE:D1_LOCAL_VALUE_TOKEN","validate",W/"d1_local_neg.json",S,CANDS3,token="C3_NO_SUBSTITUTION=PASS")
std=lambda **k: dict({"claim_id":"paperE.txt#1","input_id":"paperE.txt#1.c","symbol":"c","status":"STANDARD","origin":"STANDARD","origin_evidence":{"reason_code":"ORIG_CONSTANT","source_file":"paperE.txt","source_line":99,"verbatim":"fabricated quotation"},"derived_from":[],"value":"2.99792458e8","source_file":"paperE.txt","source_line":99},**k)
rc,out=run(SEAT,"validate",w("std_fab.json",{"records":[std()]}),S,CANDS3); check("gate F3 (codex): a STANDARD record citing a nonexistent line with a fabricated quotation FAILS at the shared evidence check",rc,out,1,["cannot read evidence line paperE.txt:99"])
probe("gate F3 probe: deleting the shared evidence-line check turns that negative into PASS",SEAT,"PROBE:EV_LINE_ALL","validate",W/"std_fab.json",S,CANDS3,token="C3_NO_SUBSTITUTION=PASS")
(S/"paperE.txt").write_text("Title E\nWe adopt a = 3 from paperB (2020).\nThen z = 3.\nWe use c = 2.99792458e8 throughout.\n"); manifest(S/"R3C2_CORPUS_MANIFEST.md", S, ["paperA.txt","paperB.txt","paperE.txt"])
rc,out=run(SEAT,"validate",w("std_ok.json",{"records":[std(source_line=4,**{"origin_evidence":{"reason_code":"ORIG_CONSTANT","source_file":"paperE.txt","source_line":4,"verbatim":"c = 2.99792458e8"}})]}),S,CANDS3); check("gate F3 positive: a STANDARD record with a real quotation at a real line validates",rc,out,0,[],"C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",w("empty_ledger.json",{"records":[]}),S,CANDS3); check("gate F2 (codex): an EMPTY ledger validates (a paper may state no derivation)",rc,out,0,[],"C3_NO_SUBSTITUTION=PASS")
LANE=H/"r3c2_lane_tools_STAGED.py"
rc,out=run(LANE,"compute",W/"empty_ledger.json",W/"compute_empty.json",CANDS3); check("gate F2: compute over an empty ledger with the candidate file emits rests_on=NOT_COMPUTED for the included claim",rc,out,0,[],"rests_on=NOT_COMPUTED")
probe("gate F2 probe: deleting the NOT_COMPUTED fill makes the row count fail",LANE,"PROBE:NOT_COMPUTED","compute",W/"empty_ledger.json",W/"compute_empty_p.json",CANDS3,token="rests_on rows 0 != included denominator 1",want_rc=1)
# V35: the disputed merged ledger is PRODUCED BY THE DELIVERED merge from two seat ledgers (a hand-composed mixed ledger without provenance_graphs is exactly what V35's compute refuses); the assertions below are unchanged
_dA=w("dispute_seatA.json",{"records":[
 {"claim_id":"t12.txt#1","input_id":"t12.txt#1.p","symbol":"p","status":"PRINTED","origin":"CHOSEN","origin_evidence":{"reason_code":"ORIG_CHOICE_STATED","source_file":"t12.txt","source_line":1,"verbatim":"x"},"derived_from":[],"value":"1","source_file":"t12.txt","source_line":1},
 {"claim_id":"t01.txt#1","input_id":"t01.txt#1.d","symbol":"d","status":"PRINTED","origin":"DERIVED","origin_evidence":{"reason_code":"ORIG_EQUATION","source_file":"t01.txt","source_line":2,"verbatim":"y"},"derived_from":["t12.txt#1.p"],"value":"2","source_file":"t01.txt","source_line":2}]})
_dB=w("dispute_seatB.json",{"records":[
 {"claim_id":"t12.txt#1","input_id":"t12.txt#1.p","symbol":"p","status":"PRINTED","origin":"MEASURED","origin_evidence":{"reason_code":"ORIG_MEASURED","source_file":"t12.txt","source_line":1,"verbatim":"x"},"derived_from":[],"value":"1","source_file":"t12.txt","source_line":1},
 {"claim_id":"t01.txt#1","input_id":"t01.txt#1.d","symbol":"d","status":"PRINTED","origin":"DERIVED","origin_evidence":{"reason_code":"ORIG_EQUATION","source_file":"t01.txt","source_line":2,"verbatim":"y"},"derived_from":["t12.txt#1.p"],"value":"2","source_file":"t01.txt","source_line":2}]})
_rc,_o=run(LANE,"merge",_dA,_dB,W/"merged_dispute.json"); assert _rc==0,_o; merged=str(W/"merged_dispute.json")
CANDS4=w("cands_dispute.json",{"declared_candidate_count":2,"declared_included_count":2,"declared_excluded_count":0,"declared_attempt_count":0,"candidates":[{"candidate_id":"t12.txt#1","source_file":"t12.txt","source_line":1,"numeral":"1","included":True,"attempts":0,"outcome":"REPRO_NOT_EVALUABLE"},{"candidate_id":"t01.txt#1","source_file":"t01.txt","source_line":2,"numeral":"2","included":True,"attempts":0,"outcome":"REPRO_NOT_EVALUABLE"}]})
rc,out=run(LANE,"compute",merged,W/"compute_dispute.json",CANDS4); results.append(("V27 label: compute emits DERIVED_STANDARD_OR_MEASURED_ONLY and never the historical token DERIVED_ONLY","DERIVED_STANDARD_OR_MEASURED_ONLY" in out and "rests_on=DERIVED_ONLY" not in out and "'DERIVED_ONLY'" not in out)); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0]); cd_=json.loads((W/"compute_dispute.json").read_text())["claims"]; results.append(("gate F4 (codex): a claim depending on ANOTHER claim's disputed input is itself DISPUTED with both rests_on values",rc==0 and cd_["t01.txt#1"].get("DISPUTED") is True and isinstance(cd_["t01.txt#1"]["rests_on"],list))); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0]+("" if results[-1][1] else "\n"+out[-300:]))
probe("gate F4 probe: deleting the propagation leaves the dependent claim undisputed",LANE,"PROBE:DISPUTE_PROPAGATES","compute",merged,W/"compute_dispute_p.json",CANDS4,token="t01.txt#1\trests_on=USES_CHOSEN")
MAN=H/"r3c2_manifest_STAGED.py"; MD=W/"manifest_dir"; MD.mkdir(); (MD/"real.py").write_text("x=1\n"); (MD/"link.py").symlink_to(MD/"real.py")
rc,out=run(MAN,MD); check("gate F9 (codex): the manifest refuses a symlinked file instead of skipping it",rc,out,1,[],"ERROR=link.py: symlink")
probe("gate F9 probe: deleting the refusal makes the manifest hash past the symlink without an error",MAN,"PROBE:MANIFEST_SYMLINK",MD,token="MANIFEST_SHA256=")
BLD=H/"r3c2_build_seat_packet_STAGED.py"; BD=W/"builddir"; BD.mkdir(); shutil.copy(H.parent/"r3c2_seat_packet"/"SEAT_BRIEF.md",BD/"SEAT_BRIEF.md"); shutil.copy(H.parent/"R3C2_V26_INTEGRATED_CANDIDATE_UNADOPTED_20260906.md",BD/"m.md")
rc,out=run(BLD,"--master",BD/"m.md","--out",BD/"pk.md","--brief",BD/"SEAT_BRIEF.md"); check("gate F8 (codex): the staged builder builds from explicit --master/--out/--brief",rc,out,0,[],"C4_PACKET_REDACTED=PASS")
manifest(S/"R3C2_CORPUS_MANIFEST.md", S, ["paperA.txt","paperB.txt"])
# ---- gate-2 (codex F1 / kimi F4): the shared evidence check runs for every non-silent record before any status branch
rc,out=run(SEAT,"validate",w("ev_absent.json",{"records":[{"claim_id":"paperA.txt#1","input_id":"paperA.txt#1.m","symbol":"m","status":"ABSENT","origin":"MEASURED","origin_evidence":{"reason_code":"ORIG_MEASURED","source_file":"paperA.txt","source_line":2,"verbatim":""},"derived_from":[],"value":None,"source_file":"paperA.txt","source_line":2}]}),S,CANDS); check("gate-2 F1 (kimi T11): an ABSENT/MEASURED record with an empty quotation FAILS",rc,out,1,["empty quotation (every non-ORIG_SILENT record quotes its evidence line)"])
probe("gate-2 F1 probe: deleting the shared empty-quotation check lets it PASS",SEAT,"PROBE:EV_EMPTY_ALL","validate",W/"ev_absent.json",S,CANDS,token="C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",w("ev_printed_bad.json",{"records":[rec(origin="CHOSEN",ev_reason_code="ORIG_CHOICE_STATED",ev_source_file="nonexistent.txt",ev_source_line=999,ev_verbatim="we choose a = 2",claim_id="paperB.txt#1",input_id="paperB.txt#1.a")]}),S,CANDS2); check("gate-2 F1 (codex): an ordinary PRINTED record whose evidence coordinates name a nonexistent file FAILS",rc,out,1,["cannot read evidence line nonexistent.txt:999"])
probe("gate-2 F1 probe: deleting the shared evidence-line check lets it PASS",SEAT,"PROBE:EV_LINE_ALL","validate",W/"ev_printed_bad.json",S,CANDS2,token="C3_NO_SUBSTITUTION=PASS")
rc,out=run(LANE if 'LANE' in dir() else H/"r3c2_lane_tools_STAGED.py","compute",W/"d1_pos.json",W/"compute_2arg.json"); check("gate-2 F3 (codex/kimi): compute without the candidate file exits 2 and writes nothing",rc,out,2,[],"the candidate file is mandatory")
MDR=W/"manifest_root_link"; MDR.symlink_to(W/"src"); rc,out=run(H/"r3c2_manifest_STAGED.py",MDR); check("gate-2 F7 (codex): a symlinked ROOT is refused",rc,out,1,[],"root is a symlink or not a directory")
probe("gate-2 F7 probe: deleting the root check lets the symlinked root be hashed",H/"r3c2_manifest_STAGED.py","PROBE:MANIFEST_ROOT",MDR,token="MANIFEST_SHA256=")
rc,out=run(SEAT,"validate",w("d1_old_style.json",{"records":[rec(origin="CHOSEN",ev_reason_code="ORIG_CHOICE_STATED",ev_source_file="paperB.txt",ev_source_line=5,ev_verbatim="we choose a = 2",claim_id="paperB.txt#1",input_id="paperB.txt#1.a")]}),S,CANDS2); check("D1 unchanged path: a non-import PRINTED record (claim bound to its own file) still validates at one line",rc,out,0,[],"C3_NO_SUBSTITUTION=PASS")
# ================= D7 fixtures
def cand(cid,f,ln,num,inc,outc=None,att=1,pv=None,rv=None):
    c={"candidate_id":cid,"source_file":f,"source_line":ln,"numeral":num,"included":inc}
    if inc: c.update({"attempts":att,"outcome":outc})
    if pv is not None: c.update({"printed_value":pv,"reproduced_value":rv})
    return c
def cfile(name,cs): inc=sum(1 for c in cs if c["included"]); return w(name,{"declared_candidate_count":len(cs),"declared_included_count":inc,"declared_excluded_count":len(cs)-inc,"declared_attempt_count":sum(c.get("attempts",0) for c in cs if c["included"]),"candidates":cs})
def xfile(name,xs): return w(name,{"declared_exclusion_count":len(xs),"exclusions":xs})
X4={"candidate_id":"c4","kind":"DATE","source_file":"paperB.txt","source_line":1,"numeral":"2020"}; A4=dict(X4,candidate_id="a4")
SC=[cand("c1","paperA.txt",4,"4",True,"REPRO_WITHIN_STATED_PRECISION",1,"4","4"),cand("c2","paperA.txt",9,"7",True,"REPRO_NOT_EVALUABLE",0),cand("c3","paperB.txt",7,"3.1",True,"REPRO_NO_DERIVATION_STATED",0),cand("c4","paperB.txt",1,"2020",False)]
sc=cfile("sealed_c.json",SC); sx=xfile("sealed_x.json",[X4]); sl=w("sealed_l.json",{"records":[rec(claim_id="c1",input_id="i1")]})
AC=[dict(c,candidate_id="a"+c["candidate_id"][1:]) for c in SC]; ac=cfile("aud_c.json",AC); ax=xfile("aud_x.json",[A4]); seed="0123456789abcdef"*4
def stage(tag, ac_, ax_, sc_, rd_fn):
    """runs seal → select → handout → seal-rederivation; returns (seal1, sel, seal2, rd) paths"""
    s1=W/f"{tag}_stage1.txt"; sel=W/f"{tag}_sel.json"; s2=W/f"{tag}_stage2.txt"
    r1=run(SEAT,"audit","seal-enumeration",ac_,ax_,s1); r2=run(SEAT,"audit","select",sc_,seed,s1,sel); run(SEAT,"audit","handout",sel,sc_,W/f"{tag}_handout.json")
    S_=json.loads(sel.read_text()) if sel.exists() else {"audited_ids":[]}; rd=w(f"{tag}_rd.json",rd_fn(S_["audited_ids"])); r3=run(SEAT,"audit","seal-rederivation",rd,s2)
    return s1,sel,s2,rd,r1,r2,r3
def full_input(r): return {k:r.get(k) for k in ("symbol","origin","status","value","source_file","source_line","derived_from","origin_evidence")}
I1=full_input(rec(claim_id="c1",input_id="i1"))
def rd_ok(ids, outc=None):
    return {cid:({"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1)}} if cid=="c1" else {"outcome":(outc or {}).get(cid,{"c2":"REPRO_NOT_EVALUABLE","c3":"REPRO_NO_DERIVATION_STATED"}.get(cid,"REPRO_NOT_EVALUABLE")),"inputs":{}}) for cid in ids}
s1,sel,s2,rd,r1,r2,r3=stage("pos",ac,ax,sc,rd_ok)
check("D7 stage 1: census-gated first-write seal of the auditor's enumeration",*r1,0,[],"AUDITOR_CENSUS_STDOUT_SHA256=")
check("D7 stage 2: selection requires the stage-1 seal; N=3, arithmetic c1 + k=1 of {c2,c3}",*r2,0,[],"N=3 R=2 k=1 audited=2")
rc,out=run(SEAT,"audit","handout",sel,sc,W/"pos_handout2.json"); hand=json.loads((W/"pos_handout2.json").read_text()); results.append(("D7 handout carries claim_id/source_file/source_line only",all(set(h)=={"claim_id","source_file","source_line"} for h in hand))); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0])
check("D7 stage 2b: first-write seal of the re-derivations",*r3,0,[],"AUDITOR_REDERIVATIONS_SHA256=")
rc,out=run(SEAT,"audit","compare",s1,ac,ax,sc,sx,sl,sel,s2,rd,W/"pos_C6.json"); check("D7 positive: stage-ordered, complete, all MATCH",rc,out,0,[],"C6_AUDIT_SAMPLE=PASS")
c6p=json.loads((W/"pos_C6.json").read_text()); results.append(("D7: every completeness row result is one of MATCH / OMISSION / AUDIT_INCLUSION_DISPUTED, and per-input origin rows exist for the audited arithmetic claim",all(r["result"] in ("MATCH","OMISSION","AUDIT_INCLUSION_DISPUTED") for r in c6p["completeness_rows"]) and c6p["audited"]["c1"]["inputs"]["i1"]["result"]=="MATCH")); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0])
rc,out=run(SEAT,"audit","seal-enumeration",ac,ax,s1); check("D7 neg: re-sealing the enumeration is refused (first-write)",rc,out,1,["already exists (first-write seal"])
rc,out=run(SEAT,"audit","select",sc,seed,W/"absent_seal.txt",W/"sel_noseal.json"); check("D7 neg: select before any stage-1 seal is refused (codex select-before-seal)",rc,out,1,["no stage-1 seal of the auditor's enumeration; selection refused"])
probe("D7 probe: deleting the seal requirement lets select run first",SEAT,"PROBE:C6_SELECT_NEEDS_SEAL","audit","select",sc,seed,W/"absent_seal.txt",W/"sel_noseal2.json",token="N=3 R=2 k=1")
rc,out=run(SEAT,"audit","select",sc,"XYZ",s1,W/"sel_bad.json"); check("D7 neg: seed not 64 lowercase hex",rc,out,1,["seed must be 64 lowercase hexadecimal"])
badc=cfile("aud_c_badcount.json",AC); j=json.loads(pathlib.Path(badc).read_text()); j["declared_candidate_count"]=99; pathlib.Path(badc).write_text(json.dumps(j))
rc,out=run(SEAT,"audit","seal-enumeration",badc,ax,W/"badcount_stage1.txt"); check("D7 neg: an auditor enumeration failing census is not sealed (kimi K4)",rc,out,1,["declared_candidate_count=99 but recomputed 4","auditor enumeration does not pass census; not sealed"])
probe("D7 probe: deleting the census gate seals the bad enumeration",SEAT,"PROBE:C6_AUDITOR_CENSUS","audit","seal-enumeration",badc,ax,W/"badcount_stage1p.txt",token="AUDITOR_CANDIDATES_SHA256=")
ac2=w("aud_c_after.json",pathlib.Path(ac).read_text()+"\n")
rc,out=run(SEAT,"audit","compare",s1,ac2,ax,sc,sx,sl,sel,s2,rd,W/"n_stage.json"); check("D7 neg: auditor enumeration changed after the stage-1 seal",rc,out,1,["C6_STAGE_ORDER: the auditor's enumeration differs from its stage-1 seal"])
probe("D7 probe: deleting the stage-order check turns that negative into PASS",SEAT,"PROBE:C6_STAGE_ORDER","audit","compare",s1,ac2,ax,sc,sx,sl,sel,s2,rd,W/"n_stage_p.json",token="C6_AUDIT_SAMPLE=PASS")
rd2=w("rd_after.json",pathlib.Path(rd).read_text()+"\n")
rc,out=run(SEAT,"audit","compare",s1,ac,ax,sc,sx,sl,sel,s2,rd2,W/"n_red.json"); check("D7 neg: re-derivations changed after their seal (kimi F5: MATCH cannot be manufactured after release)",rc,out,1,["the auditor's re-derivations differ from their seal"])
probe("D7 probe: deleting the re-derivation seal check turns that negative into PASS",SEAT,"PROBE:C6_REDERIV_SEAL","audit","compare",s1,ac,ax,sc,sx,sl,sel,s2,rd2,W/"n_red_p.json",token="C6_AUDIT_SAMPLE=PASS")
selx=json.loads(sel.read_text()); selx["audited_ids"]=[]; selx["sampled_ids"]=[]; selx["k"]=0; selx_p=w("sel_emptied.json",selx)
rc,out=run(SEAT,"audit","compare",s1,ac,ax,sc,sx,sl,selx_p,s2,rd,W/"n_selx.json"); check("D7 neg: selection edited to audit nothing, candidate digest retained (codex) → recomputation fails it",rc,out,1,["C6_SELECTION: supplied k differs","C6_SELECTION: supplied sampled_ids differs","C6_SELECTION: supplied audited_ids differs"])
selns=json.loads(sel.read_text()); selns.pop("seed_hex"); selns["audited_ids"]=[]; selns["sampled_ids"]=[]; selns["k"]=0; selns_p=w("sel_noseed.json",selns)
rc,out=run(SEAT,"audit","compare",s1,ac,ax,sc,sx,sl,selns_p,s2,rd,W/"n_noseed.json"); check("D7 neg (codex F1 / kimi F2): selection without a seed, ids emptied, digests retained → FAIL, not skipped",rc,out,1,["C6_SELECTION: selection carries no seed of 64 lowercase hexadecimal characters; nothing to recompute against"])
selu=json.loads(sel.read_text()); selu["seed_hex"]="A"*64; selu_p=w("sel_upper.json",selu)
rc,out=run(SEAT,"audit","compare",s1,ac,ax,sc,sx,sl,selu_p,s2,rd,W/"n_upper.json"); check("D7 neg (round-3 N2 codex): uppercase seed in the selection → FAIL under select's contract, not PASS",rc,out,1,["selection carries no seed of 64 lowercase hexadecimal characters"])
selg=json.loads(sel.read_text()); selg["seed_hex"]="g"*64; selg_p=w("sel_nonhex.json",selg)
rc,out=run(SEAT,"audit","compare",s1,ac,ax,sc,sx,sl,selg_p,s2,rd,W/"n_nonhex.json"); check("D7 neg (round-3 N2 both): non-hex seed → a FAIL token and an artefact, never a traceback",rc,out,1,["selection carries no seed of 64 lowercase hexadecimal characters"],"C6_AUDIT_SAMPLE=FAIL")
results.append(("D7: the non-hex-seed failure wrote C6_AUDIT.json with study_files=CENSUS_AUDIT_FAILED",(W/"n_nonhex.json").exists() and json.loads((W/"n_nonhex.json").read_text())["study_files"]=="CENSUS_AUDIT_FAILED")); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0])
probe("D7 probe: deleting the seed-presence check lets the seedless empty audit PASS",SEAT,"PROBE:C6_SEED_PRESENT","audit","compare",s1,ac,ax,sc,sx,sl,selns_p,s2,rd,W/"n_noseed_p.json",token="C6_AUDIT_SAMPLE=PASS")
probe("D7 probe: deleting the recomputation lets the emptied selection PASS",SEAT,"PROBE:C6_RECOMPUTE","audit","compare",s1,ac,ax,sc,sx,sl,selx_p,s2,rd,W/"n_selx_p.json",token="C6_AUDIT_SAMPLE=PASS")
# completeness, four asymmetries
def full_case(tag, aud_cands, aud_x, sealed_cands, sealed_x, rdfn=rd_ok, sl_=None):
    ac_=cfile(f"{tag}_ac.json",aud_cands); ax_=xfile(f"{tag}_ax.json",aud_x); sc_=cfile(f"{tag}_sc.json",sealed_cands); sx_=xfile(f"{tag}_sx.json",sealed_x)
    s1_,sel_,s2_,rd_,*_=stage(tag,ac_,ax_,sc_,rdfn); slx=sl_ or sl; rc,out=run(SEAT,"audit","compare",s1_,ac_,ax_,sc_,sx_,slx,sel_,s2_,rd_,W/f"{tag}_C6.json"); return rc,out,(s1_,ac_,ax_,sc_,sx_,slx,sel_,s2_,rd_)
rc,out,argsA=full_case("miss_sealed",[c for c in AC if c["candidate_id"]!="a3"],[A4],SC,[X4]); check("D7 neg (reverse): a sealed included passage absent from the auditor's enumeration",rc,out,1,["COMPLETENESS sealed_included_absent_from_audit_enumeration: ['paperB.txt', 7, '3.1']"],"C6_AUDIT_SAMPLE=FAIL"); EX.append(("PROBE 2 — sealed includes paperB.txt:7 '3.1'; the auditor's enumeration lacks it",out))
probe("D7 probe: deleting the sealed-missing check turns it into PASS",SEAT,"PROBE:C6_SEALED_MISSING","audit","compare",*argsA,W/"miss_sealed_p.json",token="C6_AUDIT_SAMPLE=PASS")
# Codex/Blanc counterexample from TWO seat ledgers
seatA=[cand("c1","paperA.txt",4,"4",True,"REPRO_WITHIN_STATED_PRECISION",1,"4","4"),cand("c2","paperA.txt",9,"7",True,"REPRO_NOT_EVALUABLE",0),cand("c4","paperB.txt",1,"2020",False)]; seatB=[dict(c) for c in seatA]
REQ=("paperB.txt",7,"3.1"); assert not any((c["source_file"],c["source_line"],c["numeral"])==REQ for c in seatA+seatB); cfile("probe_seatA_c.json",seatA); cfile("probe_seatB_c.json",seatB)
agreed=[a for a,b in zip(seatA,seatB) if a==b]; assert len(agreed)==3
rc,out,argsB=full_case("both_omit",[dict(c,candidate_id="a"+c["candidate_id"][1:]) for c in agreed]+[cand("a3",*REQ,True,"REPRO_NO_DERIVATION_STATED",0)],[A4],agreed,[X4]); check("PROBE 1 (Codex/Blanc): a required passage omitted by BOTH seats, retained by the auditor → FAIL, listed",rc,out,1,["COMPLETENESS audit_included_absent_from_sealed: ['paperB.txt', 7, '3.1']"],"C6_AUDIT_SAMPLE=FAIL"); EX.insert(0,("PROBE 1 — both seat ledgers omit paperB.txt:7 '3.1'; the auditor includes it",out))
c6b=json.loads((W/"both_omit_C6.json").read_text()); om=[r for r in c6b["completeness_rows"] if r["result"]=="OMISSION"]; results.append(("D7: the both-seats-omit row is result OMISSION with direction audit_included_absent_from_sealed",len(om)==1 and om[0]["direction"]=="audit_included_absent_from_sealed")); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0])
probe("PROBE 1 deletion probe: removing the both-seats-missed check turns it into PASS",SEAT,"PROBE:C6_BOTH_SEATS_MISSED","audit","compare",*argsB,W/"both_omit_p.json",token="C6_AUDIT_SAMPLE=PASS")
rc,out,argsC=full_case("aud_excl_missing",[dict(c,candidate_id="a"+c["candidate_id"][1:]) for c in agreed]+[cand("a9","paperB.txt",9,"1999",False)],[A4,{"candidate_id":"a9","kind":"DATE","source_file":"paperB.txt","source_line":9,"numeral":"1999"}],agreed,[X4]); check("D7 neg (kimi F6): a passage the seats never enumerated, EXCLUDED by the auditor → still incompleteness, FAIL",rc,out,1,["COMPLETENESS audit_excluded_absent_from_sealed: ['paperB.txt', 9, '1999']"],"C6_AUDIT_SAMPLE=FAIL"); EX.append(("PROBE 5 — seats never enumerated paperB.txt:9 '1999'; the auditor excluded it (DATE)",out))
probe("D7 probe: deleting the excluded-missing check turns it into PASS",SEAT,"PROBE:C6_EXCLUDED_MISSING","audit","compare",*argsC,W/"aud_excl_missing_p.json",token="C6_AUDIT_SAMPLE=PASS")
rc,out,argsD=full_case("sealed_excl_missing",[dict(c,candidate_id="a"+c["candidate_id"][1:]) for c in SC if c["candidate_id"]!="c4"],[],SC,[X4]); check("D7 (kimi K3): a sealed EXCLUDED passage absent from the auditor's enumeration → listed as a dispute, counted, PASS (1/3 = 33%... no: FAILS the 10% rule)",rc,out,1,["AUDIT_INCLUSION_DISPUTED above 10% of the sealed denominator: 1/3"],"C6_AUDIT_SAMPLE=FAIL"); EX.append(("PROBE 6 — sealed excluded paperB.txt:1 '2020' (DATE) absent from the auditor's enumeration: listed as AUDIT_INCLUSION_DISPUTED, 1/3 > 10% → FAIL",out))
c6=json.loads((W/"sealed_excl_missing_C6.json").read_text()); row=[r for r in c6["completeness_rows"] if r["key"]==["paperB.txt",1,"2020"]][0]; results.append(("D7: the sealed-excluded-absent row is listed with both dispositions and the token",row["result"]=="AUDIT_INCLUSION_DISPUTED" and row["sealed_included"] is False and row["audit_included"] is None)); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0])
big=[cand(f"c{i}","paperA.txt",100+i,str(i),True,"REPRO_NOT_EVALUABLE",0) for i in range(1,21)]
def aud_big(nflip):
    cs=[]; xs=[]
    for i,c in enumerate(big,1):
        c=dict(c,candidate_id=f"a{i}")
        if i<=nflip: c={"candidate_id":f"a{i}","source_file":c["source_file"],"source_line":c["source_line"],"numeral":c["numeral"],"included":False}; xs.append({"candidate_id":f"a{i}","kind":"AUTHOR_SPECIFIED_INPUT","source_file":c["source_file"],"source_line":c["source_line"],"numeral":c["numeral"]})
        cs.append(c)
    return cs,xs
rdb=lambda ids: {cid:{"outcome":"REPRO_NOT_EVALUABLE","inputs":{}} for cid in ids}
cs2,xs2=aud_big(2); rc,out,_=full_case("big2",cs2,xs2,big,[],rdb); check("PROBE 3: inclusion disputed on 2 of 20 (10%) → listed, counted, PASS",rc,out,0,[],'"inclusion_disputed_count": 2'); EX.append(("PROBE 3 — inclusion disputed on 2 of 20",out))
cs3,xs3=aud_big(3); rc,out,argsE=full_case("big3",cs3,xs3,big,[],rdb); check("PROBE 4: inclusion disputed on 3 of 20 (15%) → FAIL",rc,out,1,["AUDIT_INCLUSION_DISPUTED above 10% of the sealed denominator: 3/20"],"C6_AUDIT_SAMPLE=FAIL"); EX.append(("PROBE 4 — inclusion disputed on 3 of 20",out))
probe("PROBE 4 deletion probe: removing the 10% rule turns it into PASS",SEAT,"PROBE:C6_DISPUTE_RATE","audit","compare",*argsE,W/"big3_p.json",token="C6_AUDIT_SAMPLE=PASS")
c6=json.loads((W/"big3_C6.json").read_text()); rows=[r for r in c6["completeness_rows"] if r["result"]=="AUDIT_INCLUSION_DISPUTED"]; results.append(("D7: disputed rows carry both dispositions (codex)",len(rows)==3 and all(r["sealed_included"] is True and r["audit_included"] is False for r in rows))); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0])
rc,out,argsZ=full_case("zero",[cand("a1","paperA.txt",50,"5",False)],[{"candidate_id":"a1","kind":"DATE","source_file":"paperA.txt","source_line":50,"numeral":"5"}],[cand("c1","paperA.txt",50,"5",False)],[{"candidate_id":"c1","kind":"DATE","source_file":"paperA.txt","source_line":50,"numeral":"5"}],lambda ids:{}); check("D7 neg (codex zero case): sealed denominator zero with candidates present → FAIL",rc,out,1,["AUDIT denominator is zero while candidates exist on either side"])
probe("D7 probe: deleting the zero-denominator check turns it into PASS",SEAT,"PROBE:C6_ZERO_DENOM","audit","compare",*argsZ,W/"zero_p.json",token="C6_AUDIT_SAMPLE=PASS")
rc,out,_=full_case("mismatch",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_FAILED","printed_value":"4","reproduced_value":"5","inputs":{"i1":dict(I1)}}}); check("D7 neg: re-derived outcome differs from the sealed record",rc,out,1,["AUDIT c1: MISMATCH (outcome REPRO_FAILED vs sealed REPRO_WITHIN_STATED_PRECISION; printed/reproduced values differ)"])
rc,out,_=full_case("origin",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1,origin="CHOSEN")}}}); check("D7 neg: re-classified origin differs from the sealed ledger",rc,out,1,["AUDIT c1: MISMATCH (input i1: record matches neither complete declared branch; origin CHOSEN vs sealed IMPORTED; root_origins differ: audit ['CHOSEN'] vs sealed ['IMPORTED'])"])
I2rec={"claim_id":"c1","input_id":"i2","symbol":"c","status":"STANDARD","origin":"STANDARD","origin_evidence":{"reason_code":"ORIG_CONSTANT","source_file":"paperA.txt","source_line":4,"verbatim":"Then y"},"derived_from":[],"value":"2.99792458e8","source_file":"paperA.txt","source_line":4}
sl2=w("sealed_l2.json",{"records":[rec(claim_id="c1",input_id="i1"),I2rec]}); I2=full_input(I2rec)
rc,out,_=full_case("edge",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1,derived_from=["i2"]),"i2":dict(I2)}}},sl_=sl2); check("gate-2 F2 (codex): a reconstructed dependency edge differing from the sealed ledger is MISMATCH (roots equal; only the edge differs)",rc,out,1,["AUDIT c1: MISMATCH (input i1: record matches neither complete declared branch; derived_from ['i2'] vs sealed [])"])
probe("gate-2 F2 probe: with the edge DIAGNOSTIC deleted the verdict still FAILS on the authoritative branch predicate (guard retained, Blanc 03:03)",SEAT,"PROBE:C6_EDGES","audit","compare",*_,W/"edge_p.json",token="record matches neither complete declared branch",want_rc=1)
# ---- gate-3 (codex V27 F1): incomplete reconstructions are refused at the seal and MISMATCH at compare; evidence compared; no borrowing
bad_rd=w("rd_incomplete.json",{**rd_ok(["c1"]),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":{"origin":"IMPORTED","derived_from":[]}}}})
rc,out=run(SEAT,"audit","seal-rederivation",bad_rd,W/"seal2_incomplete.txt"); check("gate-3 F1 (codex): a reconstruction with only origin and parents is refused at the re-derivation seal",rc,out,1,["c1/i1: reconstruction missing ['symbol', 'status', 'value', 'source_file', 'source_line', 'origin_evidence']"])
probe("gate-3 F1 probe: deleting the schema gate seals the incomplete reconstruction",SEAT,"PROBE:C6_RECON_SCHEMA","audit","seal-rederivation",bad_rd,W/"seal2_incomplete_p.txt",token="AUDITOR_REDERIVATIONS_SHA256=")
rc,out,_=full_case("fabev",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1,origin_evidence=dict(I1["origin_evidence"],verbatim="fabricated"))}}}); check("gate-3 F1: a complete reconstruction whose evidence quotation differs is MISMATCH",rc,out,1,["AUDIT c1: MISMATCH (input i1: record matches neither complete declared branch; origin_evidence.verbatim fabricated vs sealed We adopt a = 2 from paperB (2020))"])
probe("gate-3 F1 probe: with the evidence DIAGNOSTIC deleted the verdict still FAILS on the authoritative branch predicate (guard retained)",SEAT,"PROBE:C6_EVIDENCE","audit","compare",*_,W/"fabev_p.json",token="record matches neither complete declared branch",want_rc=1)
I1d=dict(I1,origin="DERIVED",derived_from=["i2"],origin_evidence=dict(I1["origin_evidence"],reason_code="ORIG_EQUATION")); I1drec=dict(rec(claim_id="c1",input_id="i1"),origin="DERIVED",derived_from=["i2"],origin_evidence=dict(I1["origin_evidence"],reason_code="ORIG_EQUATION"))
sl3=w("sealed_l3.json",{"records":[I1drec,I2rec]})
rc,out,_=full_case("noborrow",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1d)}}},sl_=sl3); check("gate-3 F1 (exact failure set widened at V36, disclosed in §10.31): a reconstruction that omits a claim's dependency (i2) is MISMATCH — the dependency is never borrowed from the sealed side",rc,out,1,["AUDIT c1: MISMATCH (input i2: not reconstructed; graph integrity (auditor closure): missing dependency i2 of i1; dependency not reconstructed by the auditor or cyclic: i1: derived_from i2 not in ledger)"])
rc,out,_=full_case("withdep",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1d),"i2":dict(I2)}}},sl_=sl3); check("gate-3 F1 positive: the same claim with its dependency reconstructed PASSES",rc,out,0,[],"C6_AUDIT_SAMPLE=PASS")
# ---- gate-3 (codex V27 F2): a declared alternative is compared like with like
altrec=dict(rec(claim_id="c1",input_id="i1"),origin="CHOSEN",origin_evidence={"reason_code":"ORIG_CHOICE_STATED","source_file":"paperB.txt","source_line":5,"verbatim":"we choose a = 2"},origin_alt="FITTED",origin_evidence_alt={"reason_code":"ORIG_FIT_STATED","source_file":"paperB.txt","source_line":5,"verbatim":"we choose a = 2"},source_file="paperB.txt",source_line=5)
sl4=w("sealed_l4.json",{"records":[altrec]}); I1alt={"symbol":"a","origin":"FITTED","status":"PRINTED","value":"2","source_file":"paperB.txt","source_line":5,"derived_from":[],"origin_evidence":{"reason_code":"ORIG_FIT_STATED","source_file":"paperB.txt","source_line":5,"verbatim":"we choose a = 2"}}
rc,out,_=full_case("altbranch",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1alt)}}},sl_=sl4); check("gate-3 F2 (codex): an auditor classification matching the sealed ALTERNATIVE is compared under that branch and PASSES",rc,out,0,[],"C6_AUDIT_SAMPLE=PASS")
samp=json.loads(sel.read_text())["sampled_ids"][0]; OFF=[x for x in ("c2","c3") if x!=samp][0]   # the included claim the seed did NOT sample: its records are off-sample closure records
I9rec=dict(rec(claim_id=OFF,input_id="i9")); I9=full_input(I9rec)
I1D=dict(I1d,derived_from=["i9"]); I1Drec=dict(I1drec,derived_from=["i9"])
sl5=w("sealed_l5.json",{"records":[I1Drec,I9rec]})
rc,out,_=full_case("offsample",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1D)}},OFF:{"outcome":SC[1]["outcome"] if OFF=="c2" else SC[2]["outcome"],"inputs":{"i9":dict(I9,origin_evidence=dict(I9["origin_evidence"],verbatim="Fabricated dependency evidence"))}}},sl_=sl5); check("gate-4 F1 (codex): an OFF-SAMPLE dependency record with a fabricated quotation is compared through the closure → MISMATCH on the selected claim",rc,out,1,["AUDIT c1: MISMATCH (input i9: record matches neither complete declared branch; origin_evidence.verbatim Fabricated dependency evidence vs sealed We adopt a = 2 from paperB (2020))"])
probe("gate-4 F1 probe: deleting the closure attribution lets the fabricated off-sample record PASS",SEAT,"PROBE:C6_CLOSURE","audit","compare",*_,W/"offsample_p.json",token="C6_AUDIT_SAMPLE=PASS")
rc,out,_=full_case("offsample_ok",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1D)}},OFF:{"outcome":SC[1]["outcome"] if OFF=="c2" else SC[2]["outcome"],"inputs":{"i9":dict(I9)}}},sl_=sl5); check("gate-4 F1 positive: the same closure with a faithful off-sample record PASSES",rc,out,0,[],"C6_AUDIT_SAMPLE=PASS")
I2b=dict(I2rec,input_id="i3"); I1P=dict(I1drec,derived_from=["i2"],derived_from_alt=["i3"],PARENTS_DISPUTED=True)
sl6=w("sealed_l6.json",{"records":[I1P,I2rec,I2b]}); I3=full_input(I2b)
rc,out,_=full_case("parentalt",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1d,derived_from=["i3"]),"i2":dict(I2),"i3":dict(I3)}}},sl_=sl6); check("gate-4 F2 (codex): a PARENT-ONLY declared alternative (origin unchanged, derived_from_alt) matched by the auditor PASSES",rc,out,0,[],"C6_AUDIT_SAMPLE=PASS")
I9alt=dict(I9rec,origin="CHOSEN",origin_evidence={"reason_code":"ORIG_CHOICE_STATED","source_file":"paperB.txt","source_line":5,"verbatim":"we choose a = 2"},origin_alt="FITTED",origin_evidence_alt={"reason_code":"ORIG_FIT_STATED","source_file":"paperB.txt","source_line":5,"verbatim":"we choose a = 2"},source_file="paperB.txt",source_line=5)
sl7=w("sealed_l7.json",{"records":[I1Drec,I9alt]}); I9F={"symbol":"a","origin":"FITTED","status":"PRINTED","value":"2","source_file":"paperB.txt","source_line":5,"derived_from":[],"origin_evidence":{"reason_code":"ORIG_FIT_STATED","source_file":"paperB.txt","source_line":5,"verbatim":"we choose a = 2"}}
# ---- gate-5 (codex V29 F1): duplicate input ids and identity conflicts in a reconstruction
dup_rd=w("rd_dup.json",{**rd_ok(["c1"]),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1D)}},OFF:{"outcome":"REPRO_NOT_EVALUABLE","inputs":{"i9":dict(I9,origin_evidence=dict(I9["origin_evidence"],verbatim="Fabricated shadowed quote"))}},"cX99":{"outcome":"REPRO_NOT_EVALUABLE","inputs":{"i9":dict(I9)}}})
rc,out=run(SEAT,"audit","seal-rederivation",dup_rd,W/"seal2_dup.txt"); check("gate-5 F1 (codex): an input_id reconstructed twice (a fabricated copy shadowed by a faithful one) is refused at the seal",rc,out,1,["cX99/i9: input_id already reconstructed under "+OFF])
probe("gate-5 F1 probe: deleting the uniqueness check seals the shadowed reconstruction",SEAT,"PROBE:C6_DUP_INPUT","audit","seal-rederivation",dup_rd,W/"seal2_dup_p.txt",token="AUDITOR_REDERIVATIONS_SHA256=")
key_rd=w("rd_claimkey.json",{**rd_ok(["c1"]),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1D)}},OFF:{"outcome":"REPRO_NOT_EVALUABLE","inputs":{"i9":dict(I9,claim_id="p.txt#f0")}}})
rc,out=run(SEAT,"audit","seal-rederivation",key_rd,W/"seal2_key.txt"); check("gate-5 F1 (codex): an explicit claim_id that conflicts with the enclosing claim key is refused at the seal",rc,out,1,["explicit claim_id 'p.txt#f0' conflicts with its enclosing claim "+OFF])
probe("gate-5 F1 probe: deleting the claim-key check seals the conflicting record",SEAT,"PROBE:C6_CLAIM_KEY","audit","seal-rederivation",key_rd,W/"seal2_key_p.txt",token="AUDITOR_REDERIVATIONS_SHA256=")
OTHER=[x for x in ("c2","c3") if x!=OFF][0]
rc,out,_=full_case("identity",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1D)}},"cZ":{"outcome":"REPRO_NOT_EVALUABLE","inputs":{"i9":dict(I9)}}},sl_=sl5); check("gate-5 F1 (codex): a dependency reconstructed under the WRONG claim key is bound to its sealed identity at compare → MISMATCH",rc,out,1,["C6_IDENTITY: i9 reconstructed under claim cZ, but the sealed record belongs to claim "+OFF,"AUDIT c1: MISMATCH (input i9: identity: reconstructed under claim cZ, but the sealed record belongs to claim "+OFF+")"])
probe("gate-5 F1 probe: with the GLOBAL identity line deleted, the per-record identity mismatch still fails the dependent claim (guard retained, Blanc 03:03)",SEAT,"PROBE:C6_IDENTITY","audit","compare",*_,W/"identity_p.json",token="AUDIT c1: MISMATCH (input i9: identity:",want_rc=1)
c6i=json.loads((W/"identity_C6.json").read_text()); results.append(("gate-6 F1 (codex): the identity conflict is carried into the dependent selected claim's input row and its result is MISMATCH",c6i["audited"]["c1"]["result"]=="MISMATCH" and c6i["audited"]["c1"]["inputs"]["i9"]["result"]=="MISMATCH" and any("identity" in w for w in c6i["audited"]["c1"]["inputs"]["i9"]["why"]))); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0])
# ---- gate-5 (codex V29 F2): a hybrid record matching neither complete declared branch is MISMATCH
I1H=dict(I1drec,derived_from=["i2"],origin_alt="CHOSEN",origin_evidence_alt={"reason_code":"ORIG_CHOICE_STATED","source_file":"paperA.txt","source_line":3,"verbatim":"We adopt a = 2 from paperB (2020)"},derived_from_alt=["i3"],PARENTS_DISPUTED=True)
sl8=w("sealed_l8.json",{"records":[I1H,I2rec,I2b]})
rc,out,_=full_case("hybrid",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1d,derived_from=["i3"]),"i2":dict(I2),"i3":dict(I3)}}},sl_=sl8); check("gate-5 F2 (codex): primary origin+evidence with the ALTERNATIVE's parents — a hybrid of both branches — is MISMATCH even though the roots agree",rc,out,1,["AUDIT c1: MISMATCH (input i1: record matches neither complete declared branch; derived_from ['i3'] vs sealed ['i2'] (alternative ['i3']))"])
probe("gate-5 F2 probe: with the parent DIAGNOSTIC deleted the hybrid still FAILS on the authoritative branch predicate (guard retained)",SEAT,"PROBE:C6_EDGES","audit","compare",*_,W/"hybrid_p.json",token="record matches neither complete declared branch",want_rc=1)
# ---- gate-6 (codex V30 F2): the REVERSE hybrid — alternative origin + alternative evidence with the PRIMARY parents
I1RH={"symbol":"a","origin":"CHOSEN","status":"PRINTED","value":"2","source_file":"paperB.txt","source_line":5,"derived_from":["i2"],"origin_evidence":{"reason_code":"ORIG_CHOICE_STATED","source_file":"paperA.txt","source_line":3,"verbatim":"We adopt a = 2 from paperB (2020)"}}
rc,out,_=full_case("revhybrid",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1RH),"i2":dict(I2),"i3":dict(I3)}}},sl_=sl8); check("gate-6 F2 (codex): the REVERSE hybrid (alternative origin+evidence with the primary parents) is MISMATCH by the authoritative predicate",rc,out,1,["AUDIT c1: MISMATCH (input i1: record matches neither complete declared branch"])
I1Hfull={"symbol":"a","origin":"CHOSEN","status":"PRINTED","value":"2","source_file":"paperB.txt","source_line":5,"derived_from":["i3"],"origin_evidence":{"reason_code":"ORIG_CHOICE_STATED","source_file":"paperA.txt","source_line":3,"verbatim":"We adopt a = 2 from paperB (2020)"}}
rc,out,_=full_case("altfull",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1Hfull),"i2":dict(I2),"i3":dict(I3)}}},sl_=sl8); check("gate-5 F2 positive: the COMPLETE alternative branch (alt origin + alt evidence + alt parents together) PASSES",rc,out,0,[],"C6_AUDIT_SAMPLE=PASS")
# ---- gate-7 (codex V31 F1/F2): the alternative branch's origin_search survives merge, is compared structurally, and the verdict is seat-order independent
SILA=dict(rec(claim_id="c1",input_id="i1"),origin="CHOSEN",origin_evidence={"reason_code":"ORIG_CHOICE_STATED","source_file":"paperB.txt","source_line":5,"verbatim":"we choose a = 2"},source_file="paperB.txt",source_line=5)
SILB=dict(SILA,origin="UNDECLARED",origin_evidence={"reason_code":"ORIG_SILENT","source_file":"paperB.txt","source_line":5,"verbatim":""},origin_search={"query":"a","files":["paperB.txt"],"matches":2})
mA=w("silA.json",{"records":[SILA]}); mB=w("silB.json",{"records":[SILB]})
rc,out=run(LANE,"merge",mA,mB,W/"silAB.json"); mAB=json.loads((W/"silAB.json").read_text()); results.append(("gate-7 F1 (codex): merge preserves the alternative's origin_search as origin_search_alt when the alternative is ORIG_SILENT",rc==0 and mAB["records"][0].get("origin_search_alt")==SILB["origin_search"])); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0])
probe("gate-7 F1 probe: deleting the preservation drops the alternative's search",LANE,"PROBE:MERGE_SEARCH_ALT","merge",mA,mB,W/"silAB_p.json",token="merged 1 records",artefact=W/"silAB_p.json",gone_text="origin_search_alt")
I1SIL={"symbol":"a","origin":"UNDECLARED","status":"PRINTED","value":"2","source_file":"paperB.txt","source_line":5,"derived_from":[],"origin_evidence":{"reason_code":"ORIG_SILENT","source_file":"paperB.txt","source_line":5,"verbatim":""},"origin_search":{"matches":2,"files":["paperB.txt"],"query":"a"}}
rc,out,_=full_case("silalt",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1SIL)}}},sl_=str(W/"silAB.json")); check("gate-7 F1/F2 (codex): the auditor matching the ORIG_SILENT alternative, with its search in a different key order, PASSES (branch search, structural comparison)",rc,out,0,[],"C6_AUDIT_SAMPLE=PASS")
rc,out=run(LANE,"merge",mB,mA,W/"silBA.json"); rc,out,_=full_case("silalt_rev",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1SIL)}}},sl_=str(W/"silBA.json")); check("gate-7 F1 (codex): the same reconstruction against the seats MERGED IN THE OTHER ORDER also PASSES (verdict independent of seat order)",rc,out,0,[],"C6_AUDIT_SAMPLE=PASS")
rc,out,_=full_case("silalt_bad",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1SIL,origin_search={"query":"a","files":["paperB.txt"],"matches":9})}}},sl_=str(W/"silAB.json")); check("gate-7 F1 neg: a changed search CONTENT still fails",rc,out,1,["AUDIT c1: MISMATCH (input i1: record matches neither complete declared branch; origin_search differs (structural comparison against the matched branch's search); root_origins differ: audit ['UNDECLARED'] vs sealed ['CHOSEN'])"])
probe("gate-7 probe: with the search DIAGNOSTIC deleted the verdict still FAILS on the authoritative predicate",SEAT,"PROBE:C6_SEARCH_BRANCH","audit","compare",*_,W/"silalt_bad_p.json",token="record matches neither complete declared branch",want_rc=1)
rc,out,_=full_case("inheritalt",AC,[A4],SC,[X4],lambda ids: {**rd_ok(ids),"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":dict(I1D)}},OFF:{"outcome":SC[1]["outcome"] if OFF=="c2" else SC[2]["outcome"],"inputs":{"i9":dict(I9F)}}},sl_=sl7); check("gate-4 F2 (codex): an INHERITED alternative (the dependency of another claim matched on its declared alternative) carries through the closure → the dependent claim PASSES",rc,out,0,[],"C6_AUDIT_SAMPLE=PASS")
# ---- gate-3 (codex V27 F3): STANDARD coordinates unconditional; BLOCKED evidence bound to the claiming file
rc,out=run(SEAT,"validate",w("std_silent_nocoord.json",{"records":[{"claim_id":"paperE.txt#1","input_id":"paperE.txt#1.h","symbol":"H0","status":"STANDARD","origin":"UNDECLARED","origin_evidence":{"reason_code":"ORIG_SILENT","source_file":"","source_line":0,"verbatim":""},"origin_search":{"query":"H0","files":["paperE.txt"],"matches":0},"derived_from":[],"value":"67.36","source_file":"","source_line":None}]}),S,CANDS3); check("gate-3 F3 (codex): a STANDARD/ORIG_SILENT record without value coordinates FAILS (absence of origin evidence never waives value evidence)",rc,out,1,["STANDARD record needs its own source_file and a positive source_line"])
probe("gate-3 F3 probe: deleting the coordinate requirement lets it PASS",SEAT,"PROBE:STD_COORDS","validate",W/"std_silent_nocoord.json",S,CANDS3,token="C3_NO_SUBSTITUTION=PASS")
blk=lambda **k: dict({"claim_id":"paperA.txt#1","input_id":"paperA.txt#1.z","symbol":"z","status":"BLOCKED","origin":"IMPORTED","origin_evidence":{"reason_code":"ORIG_CITATION","source_file":"paperA.txt","source_line":3,"verbatim":"We adopt a = 2 from paperB (2020)"},"derived_from":[],"value":None,"source_file":"paperA.txt","source_line":3},**k)
rc,out=run(SEAT,"validate",w("blk_ok.json",{"records":[blk()]}),S,CANDS); check("gate-3 F3 positive: a BLOCKED record naming its source in the claiming paper validates",rc,out,0,[],"C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",w("blk_wrongfile.json",{"records":[blk(origin_evidence={"reason_code":"ORIG_CITATION","source_file":"paperB.txt","source_line":5,"verbatim":"we choose a = 2"})]}),S,CANDS); check("gate-3 F3 (codex): a BLOCKED record whose naming evidence lies in another file FAILS",rc,out,1,["BLOCKED naming evidence is in paperB.txt, but claim paperA.txt#1 belongs to paperA.txt"])
probe("gate-3 F3 probe: deleting the claiming-file binding lets it PASS",SEAT,"PROBE:BLOCKED_CLAIMING_FILE","validate",W/"blk_wrongfile.json",S,CANDS,token="C3_NO_SUBSTITUTION=PASS")
# ---- gate-3 (codex V27 F4): an ordinary PRINTED record may cite its origin evidence on a different line from its value
(S/"paperB.txt").write_text("Title B\nSee the appendix and b = 20.\n\nSetup.\nFor this calculation we choose a = 2.\nLater we repeat a = 2.\nWe choose g for the calculation.\ng = 7.\n"); manifest(S/"R3C2_CORPUS_MANIFEST.md", S, ["paperA.txt","paperB.txt"])
rc,out=run(SEAT,"validate",w("printed_split.json",{"records":[{"claim_id":"paperB.txt#1","input_id":"paperB.txt#1.g","symbol":"g","status":"PRINTED","origin":"CHOSEN","origin_evidence":{"reason_code":"ORIG_CHOICE_STATED","source_file":"paperB.txt","source_line":7,"verbatim":"We choose g for the calculation"},"derived_from":[],"value":"7","source_file":"paperB.txt","source_line":8}]}),S,CANDS2); check("gate-3 F4 (codex): a PRINTED record with origin evidence on line 7 and its value on line 8 validates",rc,out,0,[],"C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",w("printed_split_bad.json",{"records":[{"claim_id":"paperB.txt#1","input_id":"paperB.txt#1.g","symbol":"g","status":"PRINTED","origin":"CHOSEN","origin_evidence":{"reason_code":"ORIG_CHOICE_STATED","source_file":"paperB.txt","source_line":7,"verbatim":"We choose g for the calculation"},"derived_from":[],"value":"9","source_file":"paperB.txt","source_line":8}]}),S,CANDS2); check("gate-3 F4 neg: the value must still be a numeric token at its own line",rc,out,1,["value 9 is not a numeric token at paperB.txt:8"])
probe("gate-3 F4 probe: deleting the value-line check lets the wrong value PASS",SEAT,"PROBE:PRINTED_VALUE_LINE","validate",W/"printed_split_bad.json",S,CANDS2,token="C3_NO_SUBSTITUTION=PASS")
# ---- gate-4 (codex V28 F3): a STANDARD value line outside the claiming file is an import, not STANDARD
rc,out=run(SEAT,"validate",w("std_external.json",{"records":[{"claim_id":"paperA.txt#1","input_id":"paperA.txt#1.c","symbol":"c","status":"STANDARD","origin":"STANDARD","origin_evidence":{"reason_code":"ORIG_CONSTANT","source_file":"paperA.txt","source_line":4,"verbatim":"Then y"},"derived_from":[],"value":"2.99792458e8","source_file":"paperE.txt","source_line":4}]}),S,CANDS); check("gate-4 F3 (codex): a STANDARD value line in another file FAILS",rc,out,1,["STANDARD value line is in paperE.txt, outside the claiming file paperA.txt"])
probe("gate-4 F3 probe: deleting the claiming-file check lets the external STANDARD PASS",SEAT,"PROBE:STD_CLAIMING_FILE","validate",W/"std_external.json",S,CANDS,token="C3_NO_SUBSTITUTION=PASS")
# ---- gate-4 (kimi V28 N5): merge fails on a value / coordinate disagreement
rc,out=run(LANE,"merge",w("mA.json",{"records":[rec(claim_id="c1",input_id="i1")]}),w("mB.json",{"records":[rec(claim_id="c1",input_id="i1",value="3",source_line=6)]}),W/"mAB.json"); check("gate-4 N5 (kimi): seats disagreeing on an input's value and line → MERGE=FAIL, both listed",rc,out,1,["i1: seats disagree on value ('2' vs '3')","i1: seats disagree on source_line (5 vs 6)"],"MERGE=FAIL")
probe("gate-4 N5 probe: deleting the field comparison merges silently",LANE,"PROBE:MERGE_FIELDS","merge",W/"mA.json",W/"mB.json",W/"mAB_p.json",token="merged 1 records")
rc,out,_=full_case("missingrd",AC,[A4],SC,[X4],lambda ids: {k:v for k,v in rd_ok(ids).items() if k!="c1"}); check("D7 neg: an audited claim has no re-derivation",rc,out,1,["AUDIT c1: MISMATCH (missing)"])
# ================= batch fixtures (ownership, not access; global ids)
CD=W/"corpus"; CD.mkdir(); T=["t1.txt","t2.txt","t3.txt","t4.txt","t5.txt"]
for i,f in enumerate(T,1): (CD/f).write_text(f"Paper {f}\nWe adopt a = 2 from t4 (2020).\nResult r = {i}0.\n" if f!="t4.txt" else "Paper t4\nWe choose a = 2.\nResult r = 40.\n")
M=W/"manifest5.md"; manifest(M,CD,T)
rc,out=run(BATCH,"partition",M,2,W/"part.json"); check("batch: partition 5 texts into 2 batches (3+2), manifest order, bytes and lines printed",rc,out,0,[],"batch 2: rows 4-5 (2 texts,")
D=W/"seatA"; D.mkdir(); PK="ab"*32
def batch_files(D,k,cands,excls,recs,access=True):
    inc=sum(1 for c in cands if c["included"]); att=sum(c.get("attempts",0) for c in cands if c["included"])
    (D/f"candidates_b{k}.json").write_text(json.dumps({"declared_candidate_count":len(cands),"declared_included_count":inc,"declared_excluded_count":len(cands)-inc,"declared_attempt_count":att,"candidates":cands},indent=1,sort_keys=True))
    (D/f"exclusions_b{k}.json").write_text(json.dumps({"declared_exclusion_count":len(excls),"exclusions":excls},indent=1,sort_keys=True))
    (D/f"ledger_b{k}.json").write_text(json.dumps({"records":recs},indent=1,sort_keys=True))
    (D/f"SEAT_REPORT_b{k}.md").write_text((f"ACCESS_SHA={PK}\n" if access else "")+f"batch {k} report\n")
r1=rec(claim_id="t1.txt#1",input_id="t1.txt#1.a",source_file="t4.txt",source_line=2,ev_source_file="t1.txt",ev_source_line=2,ev_verbatim="We adopt a = 2 from t4 (2020)")   # batch-1 claim importing from a batch-2 text (the codex/kimi case)
r1d={"claim_id":"t1.txt#1","input_id":"t1.txt#1.r","symbol":"r","status":"PRINTED","origin":"DERIVED","origin_evidence":{"reason_code":"ORIG_EQUATION","source_file":"t1.txt","source_line":3,"verbatim":"Result r = 10"},"derived_from":["t1.txt#1.a"],"value":"10","source_file":"t1.txt","source_line":3}
B1C=[cand("t1.txt#1","t1.txt",3,"10",True,"REPRO_WITHIN_STATED_PRECISION",1,"10","10"),cand("t2.txt#1","t2.txt",2,"2020",False)]; B1X=[{"candidate_id":"t2.txt#1","kind":"DATE","source_file":"t2.txt","source_line":2,"numeral":"2020"}]
batch_files(D,1,B1C,B1X,[r1,r1d]); batch_files(D,2,[cand("t4.txt#1","t4.txt",3,"40",True,"REPRO_NOT_EVALUABLE",0)],[],[])
rc,out=run(BATCH,"seal",W/"part.json",2,D,CD,W/"seals.json"); check("batch neg: sealing batch 2 before batch 1 is refused (codex order probe)",rc,out,1,["batch 2 sealed before batch 1 (dispatch order)"])
probe("batch probe: deleting the order check seals batch 2 first",BATCH,"PROBE:SEAL_ORDER","seal",W/"part.json",2,D,CD,W/"seals_p.json",token="sealed batch 2")
rc,out=run(BATCH,"seal",W/"part.json",1,D,CD,W/"seals.json"); check("batch: seal batch 1 (binds partition, owned texts' verified digests, artefacts)",rc,out,0,[],"sealed batch 1")
rc,out=run(BATCH,"seal",W/"part.json",2,D,CD,W/"seals.json"); check("batch: seal batch 2 (binds predecessor seal)",rc,out,0,[],"sealed batch 2")
rc,out=run(BATCH,"seal",W/"part.json",1,D,CD,W/"seals.json"); check("batch neg: re-sealing a batch is refused",rc,out,1,["batch 1 already sealed"])
rc,out=run(BATCH,"join",W/"part.json",D,W/"seals.json",M,str(W/"joinA_")); check("batch: join — cross-batch IMPORT evidence (t1 claim cites t4's line) is ALLOWED, ids kept, graph resolved",rc,out,0,[],"joined: batches=2 candidates=3 included=2 excluded=1 exclusions=1 records=2")
j1=(W/"joinA_candidates.json").read_bytes(); run(BATCH,"join",W/"part.json",D,W/"seals.json",M,str(W/"joinB_")); results.append(("batch: join is deterministic (same bytes twice)",j1==(W/"joinB_candidates.json").read_bytes())); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0])
rc,out=run(SEAT,"census",W/"joinA_candidates.json",W/"joinA_exclusions.json","final"); check("batch: census PASSES over the joined files (one denominator)",rc,out,0,[],"C1_DENOMINATOR_PRINTED=PASS")
rc,out=run(BATCH,"seal",W/"part.json",1,D,CD,W/"sealsB_unbound.json","B"); check("gate F10 neg: a limb-B chain not bound to the agreed limb-A seals is refused",rc,out,1,["a limb-B chain must be bound to the agreed limb-A seals file at its first seal"])
probe("gate F10 probe: deleting the binding requirement seals an unbound limb-B chain",BATCH,"PROBE:CHAIN_B_BOUND","seal",W/"part.json",1,D,CD,W/"sealsB_unbound_p.json","B",token="sealed batch 1")
rc,out=run(BATCH,"seal",W/"part.json",1,D,CD,W/"sealsB.json","B",W/"seals.json"); check("gate F10: limb-B chain bound to the limb-A seals at its first seal",rc,out,0,[],"sealed batch 1")
run(BATCH,"seal",W/"part.json",2,D,CD,W/"sealsB.json","B")
rc,out=run(BATCH,"join",W/"part.json",D,W/"sealsB.json",M,str(W/"joinBB_"),W/"seals.json"); check("gate F10: join of a limb-B chain verifies its binding to the supplied limb-A seals",rc,out,0,[],"JOIN=PASS")
rc,out=run(BATCH,"join",W/"part.json",D,W/"sealsB.json",M,str(W/"joinBX_"),W/"seals_scope.json"); check("gate F10 neg: join of a limb-B chain against a DIFFERENT limb-A seals file fails",rc,out,1,["limb-B chain is not bound to the supplied agreed limb-A seals file"])
probe("gate F10 probe: deleting the binding check joins the mismatched chain",BATCH,"PROBE:JOIN_CHAIN_B","join",W/"part.json",D,W/"sealsB.json",M,str(W/"joinBXp_"),W/"seals_scope.json",token="JOIN=PASS")
manifest(CD/"R3C2_CORPUS_MANIFEST.md",CD,T)
rc,out=run(SEAT,"validate",W/"joinA_ledger.json",CD,W/"joinA_candidates.json"); check("batch: the joined ledger validates against the FULL corpus (the cross-batch import machine-matches at t4:2)",rc,out,0,[],"C3_NO_SUBSTITUTION=PASS")
CD1=W/"corpus_batch1_only"; CD1.mkdir(); [shutil.copy(CD/f,CD1/f) for f in T[:3]]; shutil.copy(CD/"R3C2_CORPUS_MANIFEST.md",CD1/"R3C2_CORPUS_MANIFEST.md")
rc,out=run(SEAT,"validate",D/"ledger_b1.json",CD1,D/"candidates_b1.json"); check("batch (the reviewers' finding, reproduced): the same record CANNOT validate when the session holds only its batch's texts",rc,out,1,["external source not an enumerable verified text: t4.txt absent from the sources directory","cannot read external value line t4.txt:2"])
rc,out=run(BATCH,"coverage",W/"part.json",M,D,CD,PK); check("batch: C1B_BATCH_COVERAGE positive (ownership once, bytes verified, ACCESS_SHA in every report)",rc,out,0,[],"C1B_BATCH_COVERAGE=PASS")
# negatives
D2=W/"seatA_scope"; shutil.copytree(D,D2); c2=json.loads((D2/"candidates_b2.json").read_text()); c2["candidates"][0]["source_file"]="t1.txt"; c2["candidates"][0]["candidate_id"]="t1.txt#9"; (D2/"candidates_b2.json").write_text(json.dumps(c2,indent=1,sort_keys=True))
sc_=W/"seals_scope.json"; run(BATCH,"seal",W/"part.json",1,D2,CD,sc_); run(BATCH,"seal",W/"part.json",2,D2,CD,sc_)
rc,out=run(BATCH,"join",W/"part.json",D2,sc_,M,str(W/"joinS_")); check("batch neg: a batch-2 candidate claims ownership of a batch-1 text",rc,out,1,["batch 2: candidate t1.txt#9 cites t1.txt, not an owned text of this batch"])
probe("batch probe: deleting the ownership check turns that negative into PASS",BATCH,"PROBE:BATCH_SCOPE","join",W/"part.json",D2,sc_,M,str(W/"joinSp_"),token="JOIN=PASS")
D5=W/"seatA_badid"; shutil.copytree(D,D5); c2=json.loads((D5/"candidates_b2.json").read_text()); c2["candidates"][0]["candidate_id"]="c1"; (D5/"candidates_b2.json").write_text(json.dumps(c2,indent=1,sort_keys=True))
s5=W/"seals_badid.json"; run(BATCH,"seal",W/"part.json",1,D5,CD,s5); run(BATCH,"seal",W/"part.json",2,D5,CD,s5)
rc,out=run(BATCH,"join",W/"part.json",D5,s5,M,str(W/"joinI_")); check("batch neg: a candidate id not of the global form <file>#<local> (codex/kimi id finding)",rc,out,1,["candidate_id c1 is not of the form <source_file>#<local>"])
probe("batch probe: deleting the global-id check turns that negative into PASS",BATCH,"PROBE:GLOBAL_ID","join",W/"part.json",D5,s5,M,str(W/"joinIp_"),token="JOIN=PASS")
D6=W/"seatA_dangling"; shutil.copytree(D,D6); l1=json.loads((D6/"ledger_b1.json").read_text()); l1["records"][1]["derived_from"]=["t4.txt#1.zz"]; (D6/"ledger_b1.json").write_text(json.dumps(l1,indent=1,sort_keys=True))
s6=W/"seals_dangling.json"; run(BATCH,"seal",W/"part.json",1,D6,CD,s6); run(BATCH,"seal",W/"part.json",2,D6,CD,s6)
rc,out=run(BATCH,"join",W/"part.json",D6,s6,M,str(W/"joinD_")); check("batch neg: a cross-batch derived_from that resolves to nothing (codex b1_b2_i1 case)",rc,out,1,["t1.txt#1.r: derived_from t4.txt#1.zz unresolved after join"])
probe("batch probe: deleting the graph check turns that negative into PASS",BATCH,"PROBE:GRAPH","join",W/"part.json",D6,s6,M,str(W/"joinDp_"),token="JOIN=PASS")
D7=W/"seatA_offcorpus"; shutil.copytree(D,D7); l1=json.loads((D7/"ledger_b1.json").read_text()); l1["records"][0]["source_file"]="elsewhere.txt"; (D7/"ledger_b1.json").write_text(json.dumps(l1,indent=1,sort_keys=True))
s7=W/"seals_off.json"; run(BATCH,"seal",W/"part.json",1,D7,CD,s7); run(BATCH,"seal",W/"part.json",2,D7,CD,s7)
rc,out=run(BATCH,"join",W/"part.json",D7,s7,M,str(W/"joinO_")); check("batch neg: evidence cited from a non-manifest text",rc,out,1,["record t1.txt#1.a cites elsewhere.txt, not a manifest text"])
probe("batch probe: deleting the manifest-evidence check turns that negative into PASS",BATCH,"PROBE:EVIDENCE_MANIFEST","join",W/"part.json",D7,s7,M,str(W/"joinOp_"),token="JOIN=PASS")
D8=W/"seatA_orphan"; shutil.copytree(D,D8); l1=json.loads((D8/"ledger_b1.json").read_text()); l1["records"][0]["claim_id"]="t1.txt#77"; l1["records"][1]["claim_id"]="t1.txt#77"; (D8/"ledger_b1.json").write_text(json.dumps(l1,indent=1,sort_keys=True))
s8=W/"seals_orphan.json"; run(BATCH,"seal",W/"part.json",1,D8,CD,s8); run(BATCH,"seal",W/"part.json",2,D8,CD,s8)
rc,out=run(BATCH,"join",W/"part.json",D8,s8,M,str(W/"joinR_")); check("batch neg (codex F6): ledger records naming a claim that is not an included candidate",rc,out,1,["ledger record t1.txt#1.a names claim t1.txt#77, not an included candidate","ledger record t1.txt#1.r names claim t1.txt#77, not an included candidate"])
probe("batch probe: deleting the orphan-claim check turns that negative into PASS",BATCH,"PROBE:ORPHAN_CLAIM","join",W/"part.json",D8,s8,M,str(W/"joinRp_"),token="JOIN=PASS")
D9=W/"seatA_inputid"; shutil.copytree(D,D9); l1=json.loads((D9/"ledger_b1.json").read_text()); l1["records"][0]["input_id"]="i1"; l1["records"][1]["derived_from"]=["i1"]; (D9/"ledger_b1.json").write_text(json.dumps(l1,indent=1,sort_keys=True))
s9=W/"seals_inputid.json"; run(BATCH,"seal",W/"part.json",1,D9,CD,s9); run(BATCH,"seal",W/"part.json",2,D9,CD,s9)
rc,out=run(BATCH,"join",W/"part.json",D9,s9,M,str(W/"joinQ_")); check("batch neg (codex F6): an input_id not of the form <claim file>#…",rc,out,1,["input_id i1 does not begin with its claim's file followed by #"])
probe("batch probe: deleting the input-id form check turns that negative into PASS",BATCH,"PROBE:INPUT_ID_FORM","join",W/"part.json",D9,s9,M,str(W/"joinQp_"),token="JOIN=PASS")
sj=json.loads((W/"seals.json").read_text()); sj2=json.loads(json.dumps(sj)); sj2["seals"]["2"]["predecessor_seal_sha256"]="0"*64; w("seals_chain.json",sj2)
rc,out=run(BATCH,"join",W/"part.json",D,W/"seals_chain.json",M,str(W/"joinC_")); check("batch neg (codex F7): batch 2's predecessor digest replaced by zeros → chain broken",rc,out,1,["batch 2: predecessor chain broken (seal does not bind batch 1's seal)"])
probe("batch probe: deleting the chain check turns that negative into PASS",BATCH,"PROBE:SEAL_CHAIN","join",W/"part.json",D,W/"seals_chain.json",M,str(W/"joinCp_"),token="JOIN=PASS")
sjr=json.loads(json.dumps(sj)); sjr["seals"]["1"]["predecessor_seal_sha256"]="f"*64; sjr["seals"]["2"]["predecessor_seal_sha256"]=hashlib.sha256(json.dumps(sjr["seals"]["1"],sort_keys=True).encode()).hexdigest(); w("seals_root.json",sjr)
rc,out=run(BATCH,"join",W/"part.json",D,W/"seals_root.json",M,str(W/"joinZ_")); check("batch neg (round-3 N3 codex): the root seal claims a predecessor, batch 2 rebound consistently → FAIL",rc,out,1,["batch 1: the chain's root seal claims a predecessor"])
probe("batch probe: deleting the root check turns that negative into PASS",BATCH,"PROBE:SEAL_ROOT","join",W/"part.json",D,W/"seals_root.json",M,str(W/"joinZp_"),token="JOIN=PASS")
sj3=json.loads(json.dumps(sj)); sj3["seals"]["1"]["owned_files"]=["t1.txt","t2.txt"]; w("seals_own.json",sj3)
rc,out=run(BATCH,"join",W/"part.json",D,W/"seals_own.json",M,str(W/"joinW_")); check("batch neg (codex F7): sealed ownership list differs from the partition (chain of batch 2 also breaks, as it must)",rc,out,1,["batch 1: sealed ownership differs from the partition","batch 2: predecessor chain broken"])
probe("batch probe: deleting the ownership-binding check leaves only the chain failure",BATCH,"PROBE:SEAL_OWNERSHIP","join",W/"part.json",D,W/"seals_own.json",M,str(W/"joinWp_"),token="batch 2: predecessor chain broken",want_rc=1)
sj4=json.loads(json.dumps(sj)); sj4["seals"]["3"]=sj4["seals"]["2"]; w("seals_extra.json",sj4)
rc,out=run(BATCH,"join",W/"part.json",D,W/"seals_extra.json",M,str(W/"joinX_")); check("batch neg (codex F7): a seal for a batch not in the partition",rc,out,1,["seals for batches not in the partition: ['3']"])
D10=W/"seatA_collide"; shutil.copytree(D,D10); c2=json.loads((D10/"candidates_b2.json").read_text()); c2["candidates"][0]["candidate_id"]="t4.txt#1"; c2["candidates"].append(dict(c2["candidates"][0])); c2["declared_candidate_count"]=2; c2["declared_included_count"]=2; c2["declared_attempt_count"]=0; (D10/"candidates_b2.json").write_text(json.dumps(c2,indent=1,sort_keys=True))
s10=W/"seals_collide.json"; run(BATCH,"seal",W/"part.json",1,D10,CD,s10); run(BATCH,"seal",W/"part.json",2,D10,CD,s10)
rc,out=run(BATCH,"join",W/"part.json",D10,s10,M,str(W/"joinK_")); check("batch neg (kimi F4): a candidate_id collision",rc,out,1,["candidate_id collision across batches: t4.txt#1"])
probe("batch probe: deleting the collision check turns that negative into PASS",BATCH,"PROBE:ID_COLLISION","join",W/"part.json",D10,s10,M,str(W/"joinKp_"),token="JOIN=PASS")
D3=W/"seatA_tamper"; shutil.copytree(D,D3); (D3/"candidates_b1.json").write_text((D3/"candidates_b1.json").read_text()+"\n")
rc,out=run(BATCH,"join",W/"part.json",D3,W/"seals.json",M,str(W/"joinT_")); check("batch neg: a sealed artefact changed after its seal",rc,out,1,["batch 1: candidates_b1.json differs from its seal"])
probe("batch probe: deleting the seal check turns that negative into PASS",BATCH,"PROBE:SEAL_MISMATCH","join",W/"part.json",D3,W/"seals.json",M,str(W/"joinTp_"),token="JOIN=PASS")
P=json.loads((W/"part.json").read_text()); Pd=json.loads(json.dumps(P)); Pd["batches"][1]["files"].append("t2.txt"); Pd["batches"][1]["sha256"].append(Pd["batches"][0]["sha256"][1]); w("part_dup.json",Pd)
rc,out=run(BATCH,"coverage",W/"part_dup.json",M,D,CD,PK); check("batch neg: a text owned by two batches",rc,out,1,["text t2.txt is owned by batch 1 and batch 2"])
probe("batch probe: deleting the duplicate check turns that negative into PASS",BATCH,"PROBE:C1B_DUPLICATE","coverage",W/"part_dup.json",M,D,CD,PK,token="C1B_BATCH_COVERAGE=PASS")
Pm=json.loads(json.dumps(P)); Pm["batches"][1]["files"].remove("t5.txt"); Pm["batches"][1]["sha256"].pop(); w("part_miss.json",Pm)
rc,out=run(BATCH,"coverage",W/"part_miss.json",M,D,CD,PK); check("batch neg: a manifest text owned by no batch",rc,out,1,["manifest text t5.txt is owned by no batch"])
probe("batch probe: deleting the missing-text check turns that negative into PASS",BATCH,"PROBE:C1B_MISSING","coverage",W/"part_miss.json",M,D,CD,PK,token="C1B_BATCH_COVERAGE=PASS")
CDt=W/"corpus_tampered"; shutil.copytree(CD,CDt); (CDt/"t3.txt").write_text("changed\n")
rc,out=run(BATCH,"coverage",W/"part.json",M,D,CDt,PK); check("batch neg: an owned text's bytes differ from the manifest (codex/kimi: bytes, not names)",rc,out,1,["owned text t3.txt: bytes do not verify against the manifest"])
probe("batch probe: deleting the bytes check turns that negative into PASS",BATCH,"PROBE:C1B_BYTES","coverage",W/"part.json",M,D,CDt,PK,token="C1B_BATCH_COVERAGE=PASS")
D4=W/"seatA_noaccess"; shutil.copytree(D,D4); (D4/"SEAT_REPORT_b2.md").write_text("batch 2 report\n")
rc,out=run(BATCH,"coverage",W/"part.json",M,D4,CD,PK); check("batch neg: a batch report without the packet's ACCESS_SHA",rc,out,1,["batch 2: SEAT_REPORT does not print ACCESS_SHA"])
probe("batch probe: deleting the ACCESS_SHA check turns that negative into PASS",BATCH,"PROBE:C1B_ACCESS","coverage",W/"part.json",M,D4,CD,PK,token="C1B_BATCH_COVERAGE=PASS")
ex=H/"C6_COUNTEREXAMPLE_EXHIBIT.txt"; ex.write_text("C6 counterexample exhibit — emitted by r3c2_staged_tests.py (STAGED, UNADOPTED, repaired after two independent reviews). Each block: the synthetic input in one line, then the tool's full stdout.\n\n"+"\n\n".join(f"=== {t} ===\n{o}" for t,o in EX)); print("exhibit written:",ex)
# ---- MEANINGLESS-ORDER INVARIANCE (Blanc 07:09, widened 07:58): ONE combined property on the delivered tools, and PER-SUBCASE fail-first
#      against pinned predecessor bytes. Every case is judged by the NEGATIVE-CONTROL PREDICATE above: exit code, completion token, exactly
#      the expected row selection, and that subcase's own verdicts/diagnostics/equality results. Rows that pass on predecessor bytes are
#      labelled controls, never counted as fail-first evidence.
LIVE=W/"spi_live"; LIVE.mkdir(); shutil.copy(H/"r3c2_ledger_tools_STAGED.py",LIVE/"r3c2_ledger_tools.py"); shutil.copy(H/"r3c2_lane_tools_STAGED.py",LIVE/"r3c2_lane_tools.py")
def moi_judge(rc,out,spec):
    """returns (ok, why) — `why` names the FIRST reason this is not the exact expected outcome. Setup, exit code and completion
    token are decided by the one evaluator's rules; the row assertions below are this helper's own exact-outcome expectations."""
    why=setup_ok(out)
    if why: return False,why
    if "runs per construction:" not in out: return False,"the exhibition did not reach its completion line"
    if "MERGE_FAIL" in out: return False,"a construction's merge did not run (MERGE_FAIL) — an infrastructure failure, never fail-first evidence"
    if rc!=spec["rc"]: return False,f"exit {rc} != expected {spec['rc']}"
    if spec["token"] not in out: return False,f"completion token {spec['token']!r} absent"
    rows=[l for l in out.splitlines() if l.startswith(("ok  ","BAD "))]
    if not rows: return False,"empty construction selection"
    if len(rows)!=spec["rows"]: return False,f"{len(rows)} construction rows selected, expected exactly {spec['rows']}"
    for key,want_bad,subs in spec["assert"]:
        m=[l for l in rows if key in l]
        if len(m)!=1: return False,f"expected exactly one row containing {key!r}, found {len(m)}"
        l=m[0]
        if want_bad and not l.startswith("BAD "): return False,f"row {key!r} did not FAIL as required"
        if (not want_bad) and not l.startswith("ok  "): return False,f"control row {key!r} did not PASS"
        for sub in subs:
            if sub not in l: return False,f"row {key!r} lacks the required evidence {sub!r}"
    return True,""
def moi(label, tools, only, spec, work, judge_only=False):
    args=[H/"r3c2_spi_exhibition.py",tools,W/work]+(["--only",only] if only else [])
    rc,out=run(*args); ok,why=moi_judge(rc,out,spec)
    if judge_only: return ok,why
    results.append((label,ok)); print(("ok  " if ok else "BAD ")+label+("" if ok else f"\n   {why}\n{out[-700:]}"))
    return ok,why
FF={
 "v35_f1":  dict(rc=1,token="SPI=FAIL",rows=1,assert_=[("codex V35 F1",True,["merged-bytes-equal=True","whole-outcome-equal=True","verdicts=[0]","expected=1","diagnostic-present=False"])]),
 "v35_f2":  dict(rc=1,token="SPI=FAIL",rows=1,assert_=[("codex V35 F2",True,["whole-outcome-equal=False","verdicts=[1]","expected=1","DIFFERING_RUNS=","seed1"])]),
 "v35_md":  dict(rc=1,token="SPI=FAIL",rows=1,assert_=[("missing dependency in the auditor",True,["verdicts=[1]","expected=1","diagnostic-present=False"])]),
 "v35_mo":  dict(rc=1,token="SPI=FAIL",rows=1,assert_=[("multi-diagnostic ordering",True,["verdicts=[1]","expected=1","diagnostic-present=False"])]),
 "v36_dep": dict(rc=1,token="SPI=FAIL",rows=1,assert_=[("dependency-list order",True,["merged-bytes-equal=False","whole-outcome-equal=False","verdicts=[0]","expected=0","reversed-dependency-order"])]),
 "v34_mix": dict(rc=1,token="SPI=FAIL",rows=1,assert_=[("codex V34 F1",True,["verdicts=[1]","expected=0","diagnostic-present=False","compute-ok=False"])]),
 "v33_mem": dict(rc=1,token="SPI=FAIL",rows=1,assert_=[("member order",True,["merged-bytes-equal=False","whole-outcome-equal=False"])]),
 "v32_sea": dict(rc=1,token="SPI=FAIL",rows=1,assert_=[("codex V32 F1",True,["verdicts=[0, 1]","expected=0"])]),
 "c_mem":   dict(rc=0,token="SPI=PASS",rows=1,assert_=[("member order",False,["merged-bytes-equal=True","whole-outcome-equal=True"])]),
 "c_v34":   dict(rc=0,token="SPI=PASS",rows=1,assert_=[("codex V34 F1",False,["merged-bytes-equal=True","whole-outcome-equal=True","compute-ok=True"])]),
 "full":    dict(rc=0,token="SPI=PASS",rows=26,assert_=[("dependency-list order",False,["merged-bytes-equal=True","whole-outcome-equal=True"]),("codex V35 F1",False,["verdicts=[1]","expected=1"]),("codex V35 F2",False,["whole-outcome-equal=True"])]),
}
for _k,_v in FF.items(): _v["assert"]=_v.pop("assert_")
moi("MOI property (delivered tools): 26 constructions, each identical across 2 seat orders x seeds 0,1,2 x reversed arrival x reversed rederivation order x reversed dependency order (both seat orders) x reversed auditor dependency order, every expected verdict met",LIVE,None,FF["full"],"moi_live")
moi("fail-first V35 / F1 (exact): a matched cycle through a CHOSEN record with parents is a FALSE PASS on the V35 bytes — verdict 0 where 1 is required, graph-integrity diagnostic absent",H/"_v35_bytecopy","codex V35 F1",FF["v35_f1"],"ff35_f1")
moi("fail-first V35 / F2 (exact): the all-DERIVED cycle gives UNEQUAL complete outcomes across PYTHONHASHSEED runs on the V35 bytes, the differing runs named",H/"_v35_bytecopy","codex V35 F2",FF["v35_f2"],"ff35_f2")
moi("fail-first V35 / missing dependency (exact): audit FAILs but the graph-integrity diagnostic is absent on the V35 bytes",H/"_v35_bytecopy","missing dependency in the auditor",FF["v35_md"],"ff35_md")
moi("fail-first V35 / multi-diagnostic (exact): audit FAILs, graph-integrity diagnostic absent on the V35 bytes",H/"_v35_bytecopy","multi-diagnostic",FF["v35_mo"],"ff35_mo")
moi("fail-first V36 / dependency-list order (exact): reversing dependency lists changes merged bytes and the whole outcome on the V36 bytes, the differing runs being the dependency-order runs",H/"_v36_bytecopy","dependency-list order",FF["v36_dep"],"ff36_dep")
moi("fail-first V34 / mixed cycle (exact): compute fails and the audit false-mismatches on the V34 bytes",H/"_v34_bytecopy","codex V34 F1",FF["v34_mix"],"ff34")
moi("fail-first V33 / member order (exact): unsorted merge serialisation changes the merged bytes on the V33 bytes",H/"_v33_bytecopy","member order",FF["v33_mem"],"ff33")
moi("fail-first V32 / same-origin searches (exact): the VERDICT ITSELF flips between seat orders on the V32 bytes (verdicts=[0, 1])",H/"_v32_bytecopy","codex V32 F1",FF["v32_sea"],"ff32")
moi("control (not fail-first) on V35 bytes: member order PASSES — closed at V34, retained as a control",H/"_v35_bytecopy","member order",FF["c_mem"],"ctl35_mem")
moi("control (not fail-first) on V35 bytes: the mixed-cycle DISPUTED pair PASSES — closed at V35, retained as a control",H/"_v35_bytecopy","codex V34 F1",FF["c_v34"],"ctl35_v34")
FF["c_v32"]=dict(rc=0,token="SPI=PASS",rows=1); FF["c_v32"]["assert"]=[("codex V32 F1",False,["merged-bytes-equal=True","whole-outcome-equal=True","verdicts=[0]"])]
moi("control (not fail-first) on V35 bytes: the same-origin-search row PASSES — closed at V32, retained as a control (kimi V36 observation (i): §10.31 named three such rows, the kit carried two)",H/"_v35_bytecopy","codex V32 F1",FF["c_v32"],"ctl35_v32")
# meta-controls: the predicate itself must reject evidence it did not ask for
_empty=W/"no_tools"; _empty.mkdir()
_ok,_why=moi("(meta)",_empty,"codex V35 F1",FF["v35_f1"],"meta_launch",judge_only=True)
_old_predicate_would_credit = True   # the retired helper decided got_pass==expect_pass; any failure satisfied a negative case
results.append(("meta-control: an unrelated LAUNCH failure (empty tools directory) is REJECTED as fail-first evidence — the retired polarity predicate would have credited it",(not _ok) and _old_predicate_would_credit and any(s in _why for s in ("setup/launch failure","did not reach its completion line","infrastructure failure","empty output")))); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0]+("" if results[-1][1] else f"\n   judged: ok={_ok} why={_why!r}"))
_ok2,_why2=moi("(meta)",H/"_v35_bytecopy","codex V35 F2",FF["v35_f1"],"meta_wrongrow",judge_only=True)
results.append(("meta-control: a REAL failure of a DIFFERENT subcase is rejected against this subcase's expectations (the predicate is discriminating, not polarity)",(not _ok2) and ("expected exactly one row" in _why2))); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0]+("" if results[-1][1] else f"\n   judged: ok={_ok2} why={_why2!r}"))
_ok3,_why3=moi("(meta)",H/"_v35_bytecopy","codex V35 F1",dict(FF["v35_f1"],assert_=None,**{"assert":[("codex V35 F1",True,["merged-bytes-equal=False"])]}),"meta_wrongevidence",judge_only=True)
results.append(("meta-control: the RIGHT subcase failing for the WRONG stated reason is rejected",(not _ok3) and ("required evidence" in _why3))); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0]+("" if results[-1][1] else f"\n   judged: ok={_ok3} why={_why3!r}"))

# ---- V37 (codex V36 F2): origin-independent graph integrity at the C3 boundaries — seat `validate` and lane `compute`
_gsrc=W/"gsrc"; _gsrc.mkdir(); (_gsrc/"p.txt").write_text("We choose x = 2 using x.\n")
_grec={"claim_id":"p.txt#c","input_id":"p.txt#x","symbol":"x","status":"PRINTED","origin":"CHOSEN","origin_evidence":{"reason_code":"ORIG_CHOICE_STATED","source_file":"p.txt","source_line":1,"verbatim":"We choose x = 2 using x."},"derived_from":["p.txt#x"],"value":"2","source_file":"p.txt","source_line":1}
_gled=w("cyc_chosen_ledger.json",{"records":[_grec]})
_gcand=w("cyc_chosen_cands.json",{"declared_candidate_count":1,"declared_included_count":1,"declared_excluded_count":0,"declared_attempt_count":0,"candidates":[{"candidate_id":"p.txt#c","source_file":"p.txt","source_line":1,"numeral":"2","included":True,"attempts":0,"outcome":"REPRO_NOT_EVALUABLE"}]})
rc,out=run(SEAT,"validate",_gled,_gsrc,_gcand); check("V37 F2 (codex): `validate` rejects a cycle through a NON-DERIVED record — origin-independent graph integrity, exact failure set",rc,out,1,["graph integrity: cycle at p.txt#x"],token="C3_NO_SUBSTITUTION=FAIL")
probe("V37 F2 probe: deleting the validate integrity check lets the CHOSEN self-cycle pass C3",SEAT,"PROBE:VALIDATE_GRAPH_INTEGRITY","validate",_gled,_gsrc,_gcand,token="C3_NO_SUBSTITUTION=PASS",want_rc=0)
rc,out=run(LANE,"compute",_gled,W/"cyc_chosen_compute.json",_gcand); check("V37 F2 (codex): lane `compute` fails BEFORE writing output on a cyclic complete provenance graph, whatever the origin",rc,out,1,["FAIL: provenance graph 0: cycle at p.txt#x"])
probe("V37 F2 probe: deleting the compute integrity check classifies the cyclic graph as USES_CHOSEN",LANE,"PROBE:COMPUTE_GRAPH_INTEGRITY","compute",_gled,W/"cyc_chosen_compute_p.json",_gcand,token="rests_on=USES_CHOSEN",want_rc=0)
if CAPTURE:
    EXACT_PATH.write_text(json.dumps(_CAPTURED,indent=1,sort_keys=True)); print(f"CAPTURED {len(_CAPTURED)} pinned expectations -> {EXACT_PATH.name}")
# ================= META-CONTROLS ON THE JUDGES THEMSELVES =================
def meta(label, cond, detail=""):
    results.append((label,bool(cond))); print(("ok  " if cond else "BAD ")+label+("" if cond else f"\n   {detail}"))
_crash="FAIL: provenance graph 0: cycle at p.txt#x\nTraceback (most recent call last):\n  File \"x\", line 1\nRuntimeError: injected infrastructure failure\n"
_ok,_why=judge("(meta crash)",1,_crash,1,["cycle at p.txt#x"])
meta("meta-control on the exact-result evaluator: a REAL TRACEBACK is rejected even though its exit code and diagnostic row match (this is the case the retired general check credited)",(not _ok) and "traceback failure" in _why,_why)
_ok,_why=judge("(meta notoken)",1,"FAIL: provenance graph 0: cycle at p.txt#x\n",1,["cycle at p.txt#x"])
meta("meta-control: output with no completion token line is rejected — a subcommand that never announces completion cannot serve as control evidence",(not _ok) and "completion token" in _why,_why)
_ok,_why=judge("(meta wrongdiag)",1,"FAIL: something else entirely\nSEAT_VALIDATE=FAIL\n",1,["cycle at p.txt#x"])
meta("meta-control: a control whose subcommand fails for a DIFFERENT stated reason is rejected",(not _ok) and "does not carry the declared expectation" in _why,_why)
_ok,_why=judge("(meta extrarows)",1,"FAIL: a\nFAIL: b\nSEAT_VALIDATE=FAIL\n",1,["a"])
meta("meta-control: an unexpected EXTRA diagnostic row is rejected (the failure set is exact, not a lower bound)",(not _ok) and "expected exactly" in _why,_why)
_inert=W/"inert_tool.py"; _inert.write_text((SEAT.read_text()+"\n# PROBE:INERT_MARKER — a marker on a line that disables nothing\n"))
_ok,_why=probe("(meta inert)",_inert,"PROBE:INERT_MARKER","validate",_gled,_gsrc,_gcand,token="C3_NO_SUBSTITUTION=FAIL",want_rc=1,judge_only=True)
meta("meta-control on deletion probes: a marker RELOCATED to a line that disables nothing is rejected — no diagnostic vanished",(not _ok) and "NO diagnostic vanished" in _why,_why)
n_ok=sum(1 for _,o in results if o); print(f"deletion_probes={NPROBES}"); print(f"controls={len(results)} passed={n_ok} failed={len(results)-n_ok}"); print("STAGED_TESTS="+("PASS" if n_ok==len(results) else "FAIL")); sys.exit(0 if n_ok==len(results) else 1)

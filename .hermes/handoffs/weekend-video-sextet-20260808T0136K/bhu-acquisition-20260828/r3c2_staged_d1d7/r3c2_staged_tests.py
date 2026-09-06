#!/usr/bin/env python3
"""r3c2_staged_tests.py — controls for the STAGED (UNADOPTED) D1/D7/batch tooling. Every negative control asserts the EXACT
failure set (count and text); every load-bearing check has a DELETION PROBE: the tool is copied with that check's line removed
and the negative control must then PASS — proving the control fails because of that check and nothing else.
Run: /usr/bin/python3 -E r3c2_staged_tests.py   (from this directory). Prints STAGED_TESTS=PASS|FAIL."""
import json, subprocess, sys, pathlib, hashlib, shutil, re
H=pathlib.Path(__file__).resolve().parent; PY="/usr/bin/python3"; SEAT=H/"r3c2_ledger_tools_STAGED.py"; BATCH=H/"r3c2_batch_tools_STAGED.py"
W=H/"_ctl"; shutil.rmtree(W,ignore_errors=True); W.mkdir()
def w(p,obj): p=W/p; p.write_text(json.dumps(obj,indent=1,sort_keys=True) if not isinstance(obj,str) else obj); return str(p)
def run(tool,*a): r=subprocess.run([PY,"-E",str(tool),*[str(x) for x in a]],capture_output=True,text=True); return r.returncode, r.stdout+r.stderr
def sha_s(s): return hashlib.sha256(s.encode()).hexdigest()
results=[]
def check(name, rc, out, want_rc, want_fails, token=None):
    fails=[l for l in out.splitlines() if l.startswith("FAIL:")]
    ok = rc==want_rc and len(fails)==len(want_fails) and all(sum(1 for f in fails if s in f)==1 for s in want_fails) and (token is None or token in out)
    results.append((name,ok)); print(("ok  " if ok else "BAD ")+name+("" if ok else f"\n   rc={rc} fails={fails}\n{out[-600:]}"))
    return ok
def probe(name, tool, marker, *args, token):
    src=tool.read_text().splitlines(); hits=[l for l in src if marker in l]; assert len(hits)==1, f"marker {marker} must occur exactly once"
    kept=[(l[:len(l)-len(l.lstrip())]+"pass  # PROBE-DELETED") if marker in l else l for l in src]  # the check is replaced by a no-op of the same indentation
    t=W/(tool.stem+"_minus_"+marker+".py"); t.write_text("\n".join(kept)+"\n"); rc,out=run(t,*args)
    ok=(token in out) and rc==0; results.append((name,ok)); print(("ok  " if ok else "BAD ")+name+("" if ok else f"\n{out[-400:]}"))
# ---------- fixtures: sources
S=W/"src"; S.mkdir()
(S/"paperA.txt").write_text("Title A\nIntro.\nWe adopt a = 2 from paperB (2020).\nThen y = 2a = 4.\n")
(S/"paperB.txt").write_text("Title B\n\n\nSetup.\nFor this calculation we choose a = 2.\n")
(S/"paperC.txt").write_text("Title C\nwe take a = 2 here\n")
(S/"R3C2_CORPUS_MANIFEST.md").write_text("# manifest\n| # | file | sha256 | bytes | non-blank lines |\n|---|---|---|---|---|\n| 1 | `paperA.txt` | `"+sha_s((S/"paperA.txt").read_text())+"` | 1 | 4 |\n| 2 | `paperB.txt` | `"+sha_s((S/"paperB.txt").read_text())+"` | 1 | 3 |\n")
def rec(**k):
    r={"claim_id":"c1","input_id":"i1","symbol":"a","status":"PRINTED","origin":"IMPORTED","origin_evidence":{"reason_code":"ORIG_CITATION","source_file":"paperA.txt","source_line":3,"verbatim":"We adopt a = 2 from paperB (2020)"},"derived_from":[],"value":"2","source_file":"paperB.txt","source_line":5}
    for kk,v in k.items():
        if kk.startswith("ev_"): r["origin_evidence"][kk[3:]]=v
        else: r[kk]=v
    return r
# ---------- D1 controls
rc,out=run(SEAT,"validate",w("d1_pos.json",{"records":[rec()]}),S); check("D1 positive: import whose source line says 'we choose' validates (IMPORTED/ORIG_CITATION)",rc,out,0,[],"C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",w("d1_n_verb.json",{"records":[rec(ev_source_line=2)]}),S); check("D1 neg: verbatim not at the citing sentence",rc,out,1,["verbatim not found at citing sentence paperA.txt:2"])
probe("D1 probe: deleting the citing-sentence check turns that negative into PASS",SEAT,"PROBE:D1_VERBATIM_SITE","validate",W/"d1_n_verb.json",S,token="C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",w("d1_n_val.json",{"records":[rec(source_line=4)]}),S); check("D1 neg: value not at the external value line",rc,out,1,["value 2 not at external value line paperB.txt:4"])
probe("D1 probe: deleting the external-value check turns that negative into PASS",SEAT,"PROBE:D1_VALUE_SITE","validate",W/"d1_n_val.json",S,token="C3_NO_SUBSTITUTION=PASS")
rc,out=run(SEAT,"validate",w("d1_n_enum.json",{"records":[rec(source_file="paperC.txt",source_line=2)]}),S); check("D1 neg: external source not an enumerable text of the manifest",rc,out,1,["external source paperC.txt is not an enumerable text"])
rc,out=run(SEAT,"validate",w("d1_n_self.json",{"records":[rec(ev_source_file="paperB.txt",ev_source_line=5,ev_verbatim="we choose a = 2")]}),S); check("D1 neg: record names its own file as the external source",rc,out,1,["names its own file as the external source"])
rc,out=run(SEAT,"validate",w("d1_old_style.json",{"records":[rec(origin="CHOSEN",ev_reason_code="ORIG_CHOICE_STATED",ev_source_file="paperB.txt",ev_source_line=5,ev_verbatim="we choose a = 2")]}),S); check("D1 unchanged path: a non-import PRINTED record still validates at one line",rc,out,0,[],"C3_NO_SUBSTITUTION=PASS")
# ---------- D7 fixtures
def cand(cid,f,ln,num,inc,outc=None,att=1,pv=None,rv=None):
    c={"candidate_id":cid,"source_file":f,"source_line":ln,"numeral":num,"included":inc}
    if inc: c.update({"attempts":att,"outcome":outc}); 
    if pv is not None: c.update({"printed_value":pv,"reproduced_value":rv})
    return c
SC=[cand("c1","paperA.txt",4,"4",True,"REPRO_WITHIN_STATED_PRECISION",1,"4","4"),cand("c2","paperA.txt",9,"7",True,"REPRO_NOT_EVALUABLE",0),cand("c3","paperB.txt",7,"3.1",True,"REPRO_NO_DERIVATION_STATED",0),cand("c4","paperB.txt",1,"2020",False)]
sc=w("sealed_c.json",{"declared_candidate_count":4,"declared_included_count":3,"declared_excluded_count":1,"declared_attempt_count":1,"candidates":SC})
sx=w("sealed_x.json",{"declared_exclusion_count":1,"exclusions":[{"candidate_id":"c4","kind":"DATE","source_file":"paperB.txt","source_line":1,"numeral":"2020"}]})
sl=w("sealed_l.json",{"records":[rec()]})
AC=[dict(c,candidate_id="a"+c["candidate_id"][1:]) for c in SC]
ac=w("aud_c.json",{"declared_candidate_count":4,"declared_included_count":3,"declared_excluded_count":1,"declared_attempt_count":1,"candidates":AC})
ax=w("aud_x.json",{"declared_exclusion_count":1,"exclusions":[{"candidate_id":"a4","kind":"DATE","source_file":"paperB.txt","source_line":1,"numeral":"2020"}]})
seed="0123456789abcdef"*4
rc,out=run(SEAT,"audit","seal-enumeration",ac,ax,W/"stage1.txt"); check("D7 stage 1: auditor enumeration sealed",rc,out,0,[],"AUDITOR_CANDIDATES_SHA256=")
rc,out=run(SEAT,"audit","select",sc,seed,W/"sel.json"); check("D7 stage 2: selection (N=3, arithmetic c1 + k=1 of {c2,c3})",rc,out,0,[],"N=3 R=2 k=1 audited=2")
sel=json.loads((W/"sel.json").read_text()); samp=sel["sampled_ids"][0]
RD={"c1":{"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":"IMPORTED"}}, samp:{"outcome":SC[1]["outcome"] if samp=="c2" else SC[2]["outcome"],"inputs":{}}}
rd=w("rederiv.json",RD)
rc,out=run(SEAT,"audit","compare",W/"stage1.txt",ac,ax,sc,sx,sl,W/"sel.json",rd,W/"C6_AUDIT.json"); check("D7 positive: stage-ordered audit, complete enumeration, all MATCH",rc,out,0,[],"C6_AUDIT_SAMPLE=PASS")
rc,out=run(SEAT,"audit","select",sc,"XYZ",W/"sel_bad.json"); check("D7 neg: seed not 64 lowercase hex",rc,out,1,["seed must be 64 lowercase hexadecimal"])
ac2=w("aud_c_after.json",{"declared_candidate_count":4,"declared_included_count":3,"declared_excluded_count":1,"declared_attempt_count":1,"candidates":AC+[]}); (W/"aud_c_after.json").write_text((W/"aud_c_after.json").read_text()+"\n")
rc,out=run(SEAT,"audit","compare",W/"stage1.txt",ac2,ax,sc,sx,sl,W/"sel.json",rd,W/"C6_AUDIT_n1.json"); check("D7 neg: auditor enumeration changed after the stage-1 seal",rc,out,1,["C6_STAGE_ORDER"])
probe("D7 probe: deleting the stage-order check turns that negative into PASS",SEAT,"PROBE:C6_STAGE_ORDER","audit","compare",W/"stage1.txt",ac2,ax,sc,sx,sl,W/"sel.json",rd,W/"C6_AUDIT_p.json",token="C6_AUDIT_SAMPLE=PASS")
acm=w("aud_c_missing.json",{"declared_candidate_count":3,"declared_included_count":2,"declared_excluded_count":1,"declared_attempt_count":1,"candidates":[c for c in AC if c["candidate_id"]!="a3"]}); run(SEAT,"audit","seal-enumeration",acm,ax,W/"stage1m.txt")
rc,out=run(SEAT,"audit","compare",W/"stage1m.txt",acm,ax,sc,sx,sl,W/"sel.json",rd,W/"C6_AUDIT_n2.json"); check("D7 neg: a sealed included passage absent from the auditor's own enumeration",rc,out,1,["sealed_included_absent_from_audit_enumeration: ['paperB.txt', 7, '3.1']"])
acx=w("aud_c_extra.json",{"declared_candidate_count":5,"declared_included_count":4,"declared_excluded_count":1,"declared_attempt_count":1,"candidates":AC+[cand("a5","paperA.txt",2,"11",True,"REPRO_NOT_EVALUABLE",0)]}); run(SEAT,"audit","seal-enumeration",acx,ax,W/"stage1x.txt")
rc,out=run(SEAT,"audit","compare",W/"stage1x.txt",acx,ax,sc,sx,sl,W/"sel.json",rd,W/"C6_AUDIT_n3.json"); check("D7 neg: the auditor found a passage both seats missed",rc,out,1,["audit_included_absent_from_sealed: ['paperA.txt', 2, '11']"])
RD2=dict(RD); RD2["c1"]=dict(RD["c1"],outcome="REPRO_FAILED",reproduced_value="5"); rd2=w("rederiv_bad.json",RD2)
rc,out=run(SEAT,"audit","compare",W/"stage1.txt",ac,ax,sc,sx,sl,W/"sel.json",rd2,W/"C6_AUDIT_n4.json"); check("D7 neg: re-derived outcome differs from the sealed record",rc,out,1,["AUDIT c1: MISMATCH (outcome REPRO_FAILED vs sealed REPRO_WITHIN_STATED_PRECISION; printed/reproduced values differ)"])
RD3=dict(RD); RD3["c1"]=dict(RD["c1"],inputs={"i1":"CHOSEN"}); rd3=w("rederiv_orig.json",RD3)
rc,out=run(SEAT,"audit","compare",W/"stage1.txt",ac,ax,sc,sx,sl,W/"sel.json",rd3,W/"C6_AUDIT_n5.json"); check("D7 neg: re-classified origin differs from the sealed ledger",rc,out,1,["AUDIT c1: MISMATCH (origin i1: CHOSEN vs sealed IMPORTED)"])
RD4={k:v for k,v in RD.items() if k!="c1"}; rd4=w("rederiv_missing.json",RD4)
rc,out=run(SEAT,"audit","compare",W/"stage1.txt",ac,ax,sc,sx,sl,W/"sel.json",rd4,W/"C6_AUDIT_n6.json"); check("D7 neg: an audited claim has no re-derivation",rc,out,1,["AUDIT c1: MISMATCH (missing)"])
# ---------- batch fixtures
M=W/"manifest5.md"; T=["t1.txt","t2.txt","t3.txt","t4.txt","t5.txt"]
M.write_text("# m\n| # | file | sha256 | b | n |\n|---|---|---|---|---|\n"+"".join(f"| {i+1} | `{f}` | `{sha_s(f)}` | 1 | 1 |\n" for i,f in enumerate(T)))
rc,out=run(BATCH,"partition",M,2,W/"part.json"); check("batch: partition 5 texts into 2 batches (3+2), manifest order",rc,out,0,[],"batch 2: rows 4-5 (2 texts)")
D=W/"seatA"; D.mkdir(); PK="ab"*32
def batch_files(k,cands,excls,recs,access=True):
    inc=sum(1 for c in cands if c["included"]); att=sum(c.get("attempts",0) for c in cands if c["included"])
    (D/f"candidates_b{k}.json").write_text(json.dumps({"declared_candidate_count":len(cands),"declared_included_count":inc,"declared_excluded_count":len(cands)-inc,"declared_attempt_count":att,"candidates":cands},indent=1,sort_keys=True))
    (D/f"exclusions_b{k}.json").write_text(json.dumps({"declared_exclusion_count":len(excls),"exclusions":excls},indent=1,sort_keys=True))
    (D/f"ledger_b{k}.json").write_text(json.dumps({"records":recs},indent=1,sort_keys=True))
    (D/f"SEAT_REPORT_b{k}.md").write_text((f"ACCESS_SHA={PK}\n" if access else "")+f"batch {k} report\n")
r1=rec(source_file="t2.txt",claim_id="c1",input_id="i1"); 
batch_files(1,[cand("c1","t1.txt",4,"4",True,"REPRO_WITHIN_STATED_PRECISION",1,"4","4"),cand("c2","t2.txt",1,"2020",False)],[{"candidate_id":"c2","kind":"DATE","source_file":"t2.txt","source_line":1,"numeral":"2020"}],[r1])
batch_files(2,[cand("c1","t4.txt",9,"7",True,"REPRO_NOT_EVALUABLE",0)],[],[])
rc,out=run(BATCH,"seal",W/"part.json",1,D,W/"seals.json"); check("batch: seal batch 1",rc,out,0,[],"sealed batch 1")
rc,out=run(BATCH,"seal",W/"part.json",2,D,W/"seals.json"); check("batch: seal batch 2",rc,out,0,[],"sealed batch 2")
rc,out=run(BATCH,"seal",W/"part.json",1,D,W/"seals.json"); check("batch neg: re-sealing a batch is refused",rc,out,1,["batch 1 already sealed"])
rc,out=run(BATCH,"join",W/"part.json",D,W/"seals.json",str(W/"joinA_")); check("batch: join verifies seals and scope, renumbers, recomputes",rc,out,0,[],"joined: batches=2 candidates=3 included=2 excluded=1 exclusions=1 records=1")
j1=(W/"joinA_candidates.json").read_bytes(); run(BATCH,"join",W/"part.json",D,W/"seals.json",str(W/"joinB_")); results.append(("batch: join is deterministic (same bytes twice)",j1==(W/"joinB_candidates.json").read_bytes())); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0])
rc,out=run(SEAT,"census",W/"joinA_candidates.json",W/"joinA_exclusions.json","final"); check("batch: census PASSES over the joined files (one denominator)",rc,out,0,[],"C1_DENOMINATOR_PRINTED=PASS")
rc,out=run(BATCH,"coverage",W/"part.json",M,D,PK); check("batch: C1B_BATCH_COVERAGE positive",rc,out,0,[],"C1B_BATCH_COVERAGE=PASS")
# negatives
c2=json.loads((D/"candidates_b2.json").read_text()); c2["candidates"][0]["source_file"]="t1.txt"; D2=W/"seatA_scope"; shutil.copytree(D,D2); (D2/"candidates_b2.json").write_text(json.dumps(c2,indent=1,sort_keys=True))
sealsc=W/"seals_scope.json"; run(BATCH,"seal",W/"part.json",1,D2,sealsc); run(BATCH,"seal",W/"part.json",2,D2,sealsc)
rc,out=run(BATCH,"join",W/"part.json",D2,sealsc,str(W/"joinS_")); check("batch neg: a batch-2 candidate cites a batch-1 text",rc,out,1,["batch 2: candidate c1 cites t1.txt, not a text of this batch"])
probe("batch probe: deleting the scope check turns that negative into PASS",BATCH,"PROBE:BATCH_SCOPE","join",W/"part.json",D2,sealsc,str(W/"joinSp_"),token="JOIN=PASS")
D3=W/"seatA_tamper"; shutil.copytree(D,D3); (D3/"candidates_b1.json").write_text((D3/"candidates_b1.json").read_text()+"\n")
rc,out=run(BATCH,"join",W/"part.json",D3,W/"seals.json",str(W/"joinT_")); check("batch neg: a sealed artefact changed after its seal",rc,out,1,["batch 1: candidates_b1.json differs from its seal"])
probe("batch probe: deleting the seal check turns that negative into PASS",BATCH,"PROBE:SEAL_MISMATCH","join",W/"part.json",D3,W/"seals.json",str(W/"joinTp_"),token="JOIN=PASS")
P=json.loads((W/"part.json").read_text()); Pd=json.loads(json.dumps(P)); Pd["batches"][1]["files"].append("t2.txt"); w("part_dup.json",Pd)
rc,out=run(BATCH,"coverage",W/"part_dup.json",M,D,PK); check("batch neg: a text in two batches",rc,out,1,["text t2.txt appears in batch 1 and batch 2"])
probe("batch probe: deleting the duplicate check turns that negative into PASS",BATCH,"PROBE:C1B_DUPLICATE","coverage",W/"part_dup.json",M,D,PK,token="C1B_BATCH_COVERAGE=PASS")
Pm=json.loads(json.dumps(P)); Pm["batches"][1]["files"].remove("t5.txt"); w("part_miss.json",Pm)
rc,out=run(BATCH,"coverage",W/"part_miss.json",M,D,PK); check("batch neg: a manifest text in no batch",rc,out,1,["manifest text t5.txt is in no batch"])
probe("batch probe: deleting the missing-text check turns that negative into PASS",BATCH,"PROBE:C1B_MISSING","coverage",W/"part_miss.json",M,D,PK,token="C1B_BATCH_COVERAGE=PASS")
D4=W/"seatA_noaccess"; shutil.copytree(D,D4); (D4/"SEAT_REPORT_b2.md").write_text("batch 2 report\n")
rc,out=run(BATCH,"coverage",W/"part.json",M,D4,PK); check("batch neg: a batch report without the packet's ACCESS_SHA",rc,out,1,["batch 2: SEAT_REPORT does not print ACCESS_SHA"])
probe("batch probe: deleting the ACCESS_SHA check turns that negative into PASS",BATCH,"PROBE:C1B_ACCESS","coverage",W/"part.json",M,D4,PK,token="C1B_BATCH_COVERAGE=PASS")
# ---------- Codex probe (BLANC_ORDER_C6_PROBE, 20:01 KST): the exact counterexample, from TWO seat ledgers, with an exhibit
EX=[]
seatA=[cand("c1","paperA.txt",4,"4",True,"REPRO_WITHIN_STATED_PRECISION",1,"4","4"),cand("c2","paperA.txt",9,"7",True,"REPRO_NOT_EVALUABLE",0),cand("c4","paperB.txt",1,"2020",False)]
seatB=[dict(c) for c in seatA]   # both seats OMIT the required passage paperB.txt:7 numeral 3.1 ("we find M = 3.1")
REQ=("paperB.txt",7,"3.1"); assert not any((c["source_file"],c["source_line"],c["numeral"])==REQ for c in seatA+seatB)
def cfile(name,cs): inc=sum(1 for c in cs if c["included"]); return w(name,{"declared_candidate_count":len(cs),"declared_included_count":inc,"declared_excluded_count":len(cs)-inc,"declared_attempt_count":sum(c.get("attempts",0) for c in cs if c["included"]),"candidates":cs})
sA=cfile("probe_seatA_c.json",seatA); sB=cfile("probe_seatB_c.json",seatB)
agreed=[a for a,b in zip(seatA,seatB) if a==b]; assert len(agreed)==3
sc2=cfile("probe_sealed_c.json",agreed); sx2=w("probe_sealed_x.json",{"declared_exclusion_count":1,"exclusions":[{"candidate_id":"c4","kind":"DATE","source_file":"paperB.txt","source_line":1,"numeral":"2020"}]})
audC=[dict(c,candidate_id="a"+c["candidate_id"][1:]) for c in agreed]+[cand("a3",*REQ,True,"REPRO_NO_DERIVATION_STATED",0)]
ac2=cfile("probe_aud_c.json",audC); ax2=w("probe_aud_x.json",{"declared_exclusion_count":1,"exclusions":[{"candidate_id":"a4","kind":"DATE","source_file":"paperB.txt","source_line":1,"numeral":"2020"}]})
run(SEAT,"audit","seal-enumeration",ac2,ax2,W/"probe_stage1.txt"); run(SEAT,"audit","select",sc2,seed,W/"probe_sel.json")
psel=json.loads((W/"probe_sel.json").read_text()); prd={cid:({"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":"IMPORTED"}} if cid=="c1" else {"outcome":"REPRO_NOT_EVALUABLE","inputs":{}}) for cid in psel["audited_ids"]}
rc,out=run(SEAT,"audit","compare",W/"probe_stage1.txt",ac2,ax2,sc2,sx2,sl,W/"probe_sel.json",w("probe_rd.json",prd),W/"probe_C6_AUDIT.json")
check("PROBE 1 (Codex): a required passage omitted by BOTH seats, retained in the auditor's enumeration → FAIL, listed",rc,out,1,["COMPLETENESS audit_included_absent_from_sealed: ['paperB.txt', 7, '3.1']"],"C6_AUDIT_SAMPLE=FAIL")
EX.append(("PROBE 1 — both seats omit paperB.txt:7 '3.1'; auditor includes it", out))
probe("PROBE 1 deletion probe: removing the both-seats-missed check turns it into PASS (so the check is what fails it)",SEAT,"PROBE:C6_BOTH_SEATS_MISSED","audit","compare",W/"probe_stage1.txt",ac2,ax2,sc2,sx2,sl,W/"probe_sel.json",W/"probe_rd.json",W/"probe_C6_AUDIT_p.json",token="C6_AUDIT_SAMPLE=PASS")
# reverse omission: sealed includes REQ, auditor's enumeration lacks it
sc3=cfile("probe_sealed_c3.json",agreed+[cand("c3",*REQ,True,"REPRO_NO_DERIVATION_STATED",0)]); ac3=cfile("probe_aud_c3.json",[dict(c,candidate_id="a"+c["candidate_id"][1:]) for c in agreed])
run(SEAT,"audit","seal-enumeration",ac3,ax2,W/"probe_stage1_3.txt"); run(SEAT,"audit","select",sc3,seed,W/"probe_sel3.json"); psel3=json.loads((W/"probe_sel3.json").read_text())
prd3={cid:({"outcome":"REPRO_WITHIN_STATED_PRECISION","printed_value":"4","reproduced_value":"4","inputs":{"i1":"IMPORTED"}} if cid=="c1" else {"outcome":"REPRO_NOT_EVALUABLE" if cid=="c2" else "REPRO_NO_DERIVATION_STATED","inputs":{}}) for cid in psel3["audited_ids"]}
rc,out=run(SEAT,"audit","compare",W/"probe_stage1_3.txt",ac3,ax2,sc3,sx2,sl,W/"probe_sel3.json",w("probe_rd3.json",prd3),W/"probe_C6_AUDIT_3.json")
check("PROBE 2 (reverse): a sealed included passage absent from the auditor's enumeration → FAIL, listed",rc,out,1,["COMPLETENESS sealed_included_absent_from_audit_enumeration: ['paperB.txt', 7, '3.1']"],"C6_AUDIT_SAMPLE=FAIL")
EX.append(("PROBE 2 — sealed includes paperB.txt:7 '3.1'; auditor's enumeration lacks it", out))
probe("PROBE 2 deletion probe: removing the sealed-missing check turns it into PASS",SEAT,"PROBE:C6_SEALED_MISSING","audit","compare",W/"probe_stage1_3.txt",ac3,ax2,sc3,sx2,sl,W/"probe_sel3.json",W/"probe_rd3.json",W/"probe_C6_AUDIT_3p.json",token="C6_AUDIT_SAMPLE=PASS")
# inclusion disagreement on a passage BOTH sides list: below 10% listed + PASS; above 10% FAIL
big=[cand(f"c{i}","paperA.txt",100+i,str(i),True,"REPRO_NOT_EVALUABLE",0) for i in range(1,21)]   # N=20, arithmetic group empty
scb=cfile("probe_big_sealed.json",big); sxb=w("probe_big_x.json",{"declared_exclusion_count":0,"exclusions":[]})
def aud_big(nflip,name):
    cs=[]; xs=[]
    for i,c in enumerate(big,1):
        c=dict(c,candidate_id=f"a{i}")
        if i<=nflip: c={"candidate_id":f"a{i}","source_file":c["source_file"],"source_line":c["source_line"],"numeral":c["numeral"],"included":False}; xs.append({"candidate_id":f"a{i}","kind":"AUTHOR_SPECIFIED_INPUT","source_file":c["source_file"],"source_line":c["source_line"],"numeral":c["numeral"]})
        cs.append(c)
    return cfile(name+"_c.json",cs), w(name+"_x.json",{"declared_exclusion_count":len(xs),"exclusions":xs})
for nflip,want_rc,label in ((2,0,"PROBE 3: inclusion disputed on 2 of 20 (10%) → listed, counted, PASS"),(3,1,"PROBE 4: inclusion disputed on 3 of 20 (15%) → FAIL under the 10% rule")):
    acb,axb=aud_big(nflip,f"probe_big_aud{nflip}"); run(SEAT,"audit","seal-enumeration",acb,axb,W/f"probe_big_stage{nflip}.txt"); run(SEAT,"audit","select",scb,seed,W/f"probe_big_sel{nflip}.json")
    selb=json.loads((W/f"probe_big_sel{nflip}.json").read_text()); rdb=w(f"probe_big_rd{nflip}.json",{cid:{"outcome":"REPRO_NOT_EVALUABLE","inputs":{}} for cid in selb["audited_ids"]})
    rc,out=run(SEAT,"audit","compare",W/f"probe_big_stage{nflip}.txt",acb,axb,scb,sxb,w("probe_big_l.json",{"records":[rec()]}),W/f"probe_big_sel{nflip}.json",rdb,W/f"probe_big_C6_{nflip}.json")
    if want_rc==0: check(label,rc,out,0,[],'"inclusion_disputed_count": 2')
    else: check(label,rc,out,1,["AUDIT_INCLUSION_DISPUTED above 10% of the sealed denominator: 3/20"],"C6_AUDIT_SAMPLE=FAIL")
    EX.append((label,out))
probe("PROBE 4 deletion probe: removing the 10% rule turns it into PASS",SEAT,"PROBE:C6_DISPUTE_RATE","audit","compare",W/"probe_big_stage3.txt",W/"probe_big_aud3_c.json",W/"probe_big_aud3_x.json",scb,sxb,W/"probe_big_l.json",W/"probe_big_sel3.json",W/"probe_big_rd3.json",W/"probe_big_C6_3p.json",token="C6_AUDIT_SAMPLE=PASS")
ex=H/"C6_COUNTEREXAMPLE_EXHIBIT.txt"; ex.write_text("C6 counterexample exhibit — emitted by r3c2_staged_tests.py (STAGED, UNADOPTED). Each block: the synthetic input in one line, then the tool's full stdout.\n\n"+"\n\n".join(f"=== {t} ===\n{o}" for t,o in EX)); print("exhibit written:",ex)
n_ok=sum(1 for _,o in results if o); print(f"controls={len(results)} passed={n_ok} failed={len(results)-n_ok}"); print("STAGED_TESTS="+("PASS" if n_ok==len(results) else "FAIL")); sys.exit(0 if n_ok==len(results) else 1)

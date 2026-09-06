import io
T="r3c2_staged_d1d7/r3c2_staged_tests.py"; t=io.open(T,encoding="utf-8").read()
def rep(a,b):
    global t; assert t.count(a)==1,a[:80]; t=t.replace(a,b)

# ---- (1) the predicate, stated ONCE, and the setup guard added to the deletion-probe judge
rep('def probe(name, tool, marker, *args, token, want_rc=0):','''# ================= NEGATIVE-CONTROL PREDICATE (Blanc 2026-09-07 07:58; codex V36 F3) =================
# A NEGATIVE CONTROL MUST ASSERT THE EXACT EXPECTED FAILURE, NEVER THE BARE POLARITY.
# Wherever a control in this kit judges an outcome it requires ALL of:
#   (1) successful setup — no traceback, no import/launch error, no usage banner, and non-empty output;
#   (2) the expected completion token AND the expected exit code;
#   (3) a non-empty selection of EXACTLY the expected rows;
#   (4) that subcase's specific verdicts, diagnostic text and equality results.
# A missing fixture, a traceback, an empty selection, or a failure for an unrelated reason FAILS the kit test; it never satisfies it.
SETUP_ERRORS=("Traceback (most recent call last)","ModuleNotFoundError","ImportError:","No such file or directory","command not found","Permission denied","can\\'t open file","usage: ")
def setup_ok(out):
    if not (out or "").strip(): return "empty output — no evidence the case ran"
    for e in SETUP_ERRORS:
        if e in out: return f"setup/launch failure in output: {e!r}"
    return ""

def probe(name, tool, marker, *args, token, want_rc=0):''')
rep('    ok=(token in out) and rc==want_rc; results.append((name,ok)); print(("ok  " if ok else "BAD ")+name+("" if ok else f"\\n   rc={rc}\\n{out[-500:]}"))',
    '    why=setup_ok(out) or ("" if token in out else f"expected token {token!r} absent") or ("" if rc==want_rc else f"exit {rc} != expected {want_rc}")\n    ok=not why; results.append((name,ok)); print(("ok  " if ok else "BAD ")+name+("" if ok else f"\\n   {why}\\n   rc={rc}\\n{out[-500:]}"))')

# ---- (2) the MOI cases: spec-driven exact-failure assertions, replacing the polarity helper
i=t.index("# ---- MEANINGLESS-ORDER INVARIANCE (Blanc 07:09"); j=t.index("n_ok=sum(1 for _,o in results if o)")
new = '''# ---- MEANINGLESS-ORDER INVARIANCE (Blanc 07:09, widened 07:58): ONE combined property on the delivered tools, and PER-SUBCASE fail-first
#      against pinned predecessor bytes. Every case is judged by the NEGATIVE-CONTROL PREDICATE above: exit code, completion token, exactly
#      the expected row selection, and that subcase's own verdicts/diagnostics/equality results. Rows that pass on predecessor bytes are
#      labelled controls, never counted as fail-first evidence.
LIVE=W/"spi_live"; LIVE.mkdir(); shutil.copy(H/"r3c2_ledger_tools_STAGED.py",LIVE/"r3c2_ledger_tools.py"); shutil.copy(H/"r3c2_lane_tools_STAGED.py",LIVE/"r3c2_lane_tools.py")
def moi_judge(rc,out,spec):
    """returns (ok, why) — `why` names the FIRST reason this is not the exact expected outcome"""
    why=setup_ok(out)
    if why: return False,why
    if "runs per construction:" not in out: return False,"the exhibition did not reach its completion line"
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
    results.append((label,ok)); print(("ok  " if ok else "BAD ")+label+("" if ok else f"\\n   {why}\\n{out[-700:]}"))
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
 "full":    dict(rc=0,token="SPI=PASS",rows=20,assert_=[("dependency-list order",False,["merged-bytes-equal=True","whole-outcome-equal=True"]),("codex V35 F1",False,["verdicts=[1]","expected=1"]),("codex V35 F2",False,["whole-outcome-equal=True"])]),
}
for _k,_v in FF.items(): _v["assert"]=_v.pop("assert_")
moi("MOI property (delivered tools): 20 constructions, each identical across 2 seat orders x seeds 0,1,2 x reversed arrival x reversed rederivation order x reversed dependency order (both seat orders) x reversed auditor dependency order, every expected verdict met",LIVE,None,FF["full"],"moi_live")
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
# meta-controls: the predicate itself must reject evidence it did not ask for
_empty=W/"no_tools"; _empty.mkdir()
_ok,_why=moi("(meta)",_empty,"codex V35 F1",FF["v35_f1"],"meta_launch",judge_only=True)
results.append(("meta-control: an unrelated LAUNCH failure (empty tools directory) is REJECTED as fail-first evidence, not credited",(not _ok) and ("setup/launch failure" in _why or "did not reach its completion line" in _why))); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0]+("" if results[-1][1] else f"\\n   judged: ok={_ok} why={_why!r}"))
_ok2,_why2=moi("(meta)",H/"_v35_bytecopy","codex V35 F2",FF["v35_f1"],"meta_wrongrow",judge_only=True)
results.append(("meta-control: a REAL failure of a DIFFERENT subcase is rejected against this subcase's expectations (the predicate is discriminating, not polarity)",(not _ok2) and ("expected exactly one row" in _why2))); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0]+("" if results[-1][1] else f"\\n   judged: ok={_ok2} why={_why2!r}"))
_ok3,_why3=moi("(meta)",H/"_v35_bytecopy","codex V35 F1",dict(FF["v35_f1"],assert_=None,**{"assert":[("codex V35 F1",True,["merged-bytes-equal=False"])]}),"meta_wrongevidence",judge_only=True)
results.append(("meta-control: the RIGHT subcase failing for the WRONG stated reason is rejected",(not _ok3) and ("required evidence" in _why3))); print(("ok  " if results[-1][1] else "BAD ")+results[-1][0]+("" if results[-1][1] else f"\\n   judged: ok={_ok3} why={_why3!r}"))

# ---- V37 (codex V36 F2): origin-independent graph integrity at the C3 boundaries — seat `validate` and lane `compute`
_gsrc=W/"gsrc"; _gsrc.mkdir(); (_gsrc/"p.txt").write_text("We choose x = 2 using x.\\n")
_grec={"claim_id":"p.txt#c","input_id":"p.txt#x","symbol":"x","status":"PRINTED","origin":"CHOSEN","origin_evidence":{"reason_code":"ORIG_CHOICE_STATED","source_file":"p.txt","source_line":1,"verbatim":"We choose x = 2 using x."},"derived_from":["p.txt#x"],"value":"2","source_file":"p.txt","source_line":1}
_gled=w("cyc_chosen_ledger.json",{"records":[_grec]})
_gcand=w("cyc_chosen_cands.json",{"declared_candidate_count":1,"declared_included_count":1,"declared_excluded_count":0,"declared_attempt_count":0,"candidates":[{"candidate_id":"p.txt#c","source_file":"p.txt","source_line":1,"numeral":"2","included":True,"attempts":0,"outcome":"REPRO_NOT_EVALUABLE"}]})
rc,out=run(SEAT,"validate",_gled,_gsrc,_gcand); check("V37 F2 (codex): `validate` rejects a cycle through a NON-DERIVED record — origin-independent graph integrity, exact failure set",rc,out,1,["graph integrity: cycle at p.txt#x","C3_NO_SUBSTITUTION=FAIL"])
probe("V37 F2 probe: deleting the validate integrity check lets the CHOSEN self-cycle pass C3",SEAT,"PROBE:VALIDATE_GRAPH_INTEGRITY","validate",_gled,_gsrc,_gcand,token="C3_NO_SUBSTITUTION=PASS",want_rc=0)
rc,out=run(LANE,"compute",_gled,W/"cyc_chosen_compute.json",_gcand); check("V37 F2 (codex): lane `compute` fails BEFORE writing output on a cyclic complete provenance graph, whatever the origin",rc,out,1,["FAIL: provenance graph 0: cycle at p.txt#x"])
probe("V37 F2 probe: deleting the compute integrity check classifies the cyclic graph as USES_CHOSEN",LANE,"PROBE:COMPUTE_GRAPH_INTEGRITY","compute",_gled,W/"cyc_chosen_compute_p.json",_gcand,token="rests_on=USES_CHOSEN",want_rc=0)
'''
t=t[:i]+new+t[j:]
io.open(T,"w",encoding="utf-8").write(t); print("kit v37 installed: exact-failure predicate, spec-driven subcases, 3 meta-controls, F2 boundary controls + probes")

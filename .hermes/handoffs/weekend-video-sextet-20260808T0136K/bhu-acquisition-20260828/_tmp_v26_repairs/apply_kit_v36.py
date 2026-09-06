import io
T="r3c2_staged_d1d7/r3c2_staged_tests.py"; t=io.open(T,encoding="utf-8").read()
i=t.index("# ---- SEAT-PERMUTATION INVARIANCE (Blanc 04:37)"); j=t.index("n_ok=sum(1 for _,o in results if o)")
new='''# ---- MEANINGLESS-ORDER INVARIANCE (Blanc 07:09; formerly SPI, Blanc 04:37): ONE combined property (seat orders x seeds 0,1,2 x reversed arrival x
#      reversed rederivation order, whole-outcome equality) on the delivered tools, and PER-SUBCASE fail-first — each subcase its own test — against
#      pinned byte copies of the tools in which that defect lived. A subcase that PASSES on older bytes is a control and is labelled as such.
LIVE=W/"spi_live"; LIVE.mkdir(); shutil.copy(H/"r3c2_ledger_tools_STAGED.py",LIVE/"r3c2_ledger_tools.py"); shutil.copy(H/"r3c2_lane_tools_STAGED.py",LIVE/"r3c2_lane_tools.py")
def moi(label, tools, only, expect_pass, work):
    args=[H/"r3c2_spi_exhibition.py",tools,W/work]+([ "--only",only] if only else [])
    rc,out=run(*args); got_pass=(rc==0 and "SPI=PASS" in out); ok=(got_pass==expect_pass)
    results.append((label,ok)); print(("ok  " if ok else "BAD ")+label+("" if ok else "\\n"+out[-900:]))
moi("MOI property: whole outcome identical under seat orders x seeds {0,1,2} x reversed arrival x reversed rederivation order, every construction, expected verdicts (delivered tools)",LIVE,None,True,"moi_live")
moi("fail-first V35 / F1: a matched cycle through a CHOSEN record with parents is a FALSE PASS on the V35 bytes",H/"_v35_bytecopy","codex V35 F1",False,"ff35_f1")
moi("fail-first V35 / F2: the all-DERIVED cycle diagnostic differs across PYTHONHASHSEED 0,1,2 on the V35 bytes",H/"_v35_bytecopy","codex V35 F2",False,"ff35_f2")
moi("fail-first V35 / missing dependency: no graph-integrity diagnostic on the V35 bytes",H/"_v35_bytecopy","missing dependency in the auditor",False,"ff35_md")
moi("fail-first V35 / multi-diagnostic ordering: no graph-integrity diagnostic on the V35 bytes",H/"_v35_bytecopy","multi-diagnostic",False,"ff35_mo")
moi("control on V35 bytes / member order (closed at V34): PASSES, retained as a control",H/"_v35_bytecopy","member order",True,"ff35_mo2")
moi("control on V35 bytes / mixed-cycle DISPUTED pair (closed at V35): PASSES, retained as a control",H/"_v35_bytecopy","codex V34 F1",True,"ff35_v34")
moi("fail-first V34 / mixed-cycle: compute fails and the audit false-mismatches on the V34 bytes",H/"_v34_bytecopy","codex V34 F1",False,"ff34")
moi("fail-first V33 / member order: unsorted merge bytes on the V33 bytes",H/"_v33_bytecopy","member order",False,"ff33")
moi("fail-first V32 / same-origin different searches: seat order flips the verdict on the V32 bytes",H/"_v32_bytecopy","codex V32 F1",False,"ff32")
'''
t=t[:i]+new+t[j:]; io.open(T,"w",encoding="utf-8").write(t); print("kit: per-subcase MOI methods installed")

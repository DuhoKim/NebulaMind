import io,sys,re
T,LANE,NC,NP=sys.argv[1:]
M="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; m=io.open(M,encoding="utf-8").read()
def rep(a,b,count=1):
    global m; pat=r"\s+(?:>\s*)?".join(re.escape(t) for t in a.split()); hits=re.findall(pat,m); assert len(hits)==count,(a[:60],len(hits)); m=re.sub(pat,lambda _: b,m,count=count)
def repx(pat,b):
    global m; assert re.search(pat,m),pat[:60]; m=re.sub(pat,b,m,count=1)
rep("Version 33 — LIVING DRAFT: V32 + SEAT-PERMUTATION INVARIANCE, the pattern repair of the two-seat gate on V32 (§10.28);","Version 34 — LIVING DRAFT: V33 + the two-seat gate on V33 closed inside the SPI pattern (§10.29); V33 = V32 + SEAT-PERMUTATION INVARIANCE, the pattern repair of the two-seat gate on V32 (§10.28);")
repx(r"the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document,\s+sha256\s+`[0-9a-f]{64}`","the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document, sha256 `"+LANE+"`")
repx(r"the lane owner runs `r3c2_lane_tools.py`\s+\(sha256\s+`[0-9a-f]{64}`;","the lane owner runs `r3c2_lane_tools.py` (sha256 `"+LANE+"`;")
rep("SPI is exhibited by `r3c2_spi_exhibition.py` in the kit: every reviewer construction is merged in both seat orders and the merged bytes and the entire audit outcome must be equal; the same exhibition FAILS against pinned byte copies of the V32 tools.",
    "SPI is exhibited by `r3c2_spi_exhibition.py` in the kit over each reviewer construction and over structurally equal records serialised with different top-level and nested member orders. `merge` serialises its output recursively with sorted object keys, so equality of canonical record keys cannot expose the first seat's original member order. Each construction uses one fixed auditor reconstruction in both seat orders and asserts equal merged bytes, equal exit codes, equal ordered failure lines and equal complete audit artefacts, including `sealed_ledger_sha256`, and asserts its own expected PASS or FAIL: the suite includes both unsupported hybrid directions, a complete parent-only alternative, both complete provenance alternatives, and structurally equal records with different JSON member orders. The exhibition FAILS against pinned byte copies of the V32 tools and of the V33 tools.")
m=m.rstrip("\n")+f"""

## 10.29 V34 — the two-seat gate on V33 closed inside the SPI pattern ({T})

C0 on V33: codex PASS, kimi PASS. Gate on V33: codex `PREREG_UNSOUND` with two findings, **kimi `PREREG_SOUND`** with none; both
PRIOR_FINDINGS_CLOSED=YES (the V32 seat-order finding closed), blind intact, C5 YES, no masked stage. Reconciled BY TOPIC
(`R3C2_V33_GATE_RECONCILIATION_20260907.md`, sweep none missing).

**codex F1 (non-cosmetic, no verdict change):** `merge` wrote its output without sorted keys, so two structurally EQUAL seat records
supplied in different JSON member order (equal canonical keys, tie broken by supply order) merged to different bytes and a different
`sealed_ledger_sha256` with the same verdict. Repaired at the ONE enforcement point: `merge` now serialises recursively with sorted
object keys (no second predicate added anywhere); the §3 sentence is replaced by codex's exact text. **codex F2 (non-cosmetic, the
exhibition):** the row labelled "hybrid direction 1" was a complete parent-only alternative (identical origin and evidence), so no true
hybrid in that direction had been constructed — a fixture defect of the lane's exhibition, disclosed as such. Repaired: that row is
relabelled and kept as the legitimate positive case; the true hybrid (A's DERIVED origin and equation evidence with B's parents, B being
CHOSEN with choice evidence) and its reciprocal are added, both required to FAIL in both orders with the unconditional "record matches
neither complete declared branch" diagnostic; every construction now asserts its expected PASS or FAIL as well as permutation equality;
the fixture writer no longer normalises member order; the complete artefact is compared with `sealed_ledger_sha256` retained and
failure lines in emitted order. Fail-first: the amended exhibition FAILS against pinned byte copies of the V33 tools on the member-order
row only and against the V32 copies as before; PASSES against the delivered tools. Kit: {NC} controls, {NP} deletion probes, PASS;
no pre-existing assertion conflicted. The gate brief for V33 carried one lane slip (its Q7 first line said "gate on V33" for "gate on
V32"; the next sentences named V32 correctly) — disclosed in the run log, not edited while seats ran. **Next:** C0 and the gate on V34.
"""
io.open(M,"w",encoding="utf-8").write(m); print("V34 master written")

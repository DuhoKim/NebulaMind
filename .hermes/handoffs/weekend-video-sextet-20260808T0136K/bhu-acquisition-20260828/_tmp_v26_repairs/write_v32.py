import io,sys,re
T,SEAT,LANE,NC,NP=sys.argv[1:]
M="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; m=io.open(M,encoding="utf-8").read()
def rep(a,b,count=1):
    global m; pat=r"\s+(?:>\s*)?".join(re.escape(t) for t in a.split()); hits=re.findall(pat,m); assert len(hits)==count,(a[:60],len(hits)); m=re.sub(pat,lambda _: b,m,count=count)
def repx(pat,b):
    global m; assert re.search(pat,m),pat[:60]; m=re.sub(pat,b,m,count=1)
rep("Version 31 — LIVING DRAFT: V30 + the repairs from the two-seat gate on V30 (§10.26);","Version 32 — LIVING DRAFT: V31 + the repairs from the two-seat gate on V31 (§10.27); V31 = V30 + the repairs from the two-seat gate on V30 (§10.26);")
repx(r"The seat's tool is `r3c2_ledger_tools.py`,\s+sha256\s+`[0-9a-f]{64}`","The seat's tool is `r3c2_ledger_tools.py`, sha256 `"+SEAT+"`")
repx(r"the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document,\s+sha256\s+`[0-9a-f]{64}`","the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document, sha256 `"+LANE+"`")
repx(r"the lane owner runs `r3c2_lane_tools.py`\s+\(sha256\s+`[0-9a-f]{64}`;","the lane owner runs `r3c2_lane_tools.py` (sha256 `"+LANE+"`;")
rep("An input matches only if its origin, origin evidence and parent list jointly equal the complete primary branch or the complete alternative branch, every declared alternative field applied together and undeclared fields left primary.",
    "An input matches only when its origin, origin evidence, parent list and any required `origin_search` jointly match one complete declared branch: `merge` preserves the primary branch's `origin_search` and the alternative branch's `origin_search_alt` whenever that branch uses `ORIG_SILENT`; `audit compare` checks the search belonging to the matched branch, as JSON structure (member equality, not key order); undeclared alternative fields keep their primary values, except that `origin_search` is required only for a branch using `ORIG_SILENT`; the verdict does not depend on which seat is A and which is B.")
rep("*(Lane side: `r3c2_lane_tools.py merge` adds `origin_alt` and `origin_evidence_alt`; `compute` adds `root_origins` and per-claim `rests_on`.)*",
    "*(Lane side: `r3c2_lane_tools.py merge` preserves branch-specific provenance evidence, adding `origin_alt`, `origin_evidence_alt` and, when the alternative uses `ORIG_SILENT`, `origin_search_alt`; it also preserves disputed parent lists. `compute` adds `root_origins` and per-claim `rests_on`.)*")
m=m.rstrip("\n")+f"""

## 10.27 V32 — the two-seat gate on V31, reconciled and repaired here ({T})

C0 on V31: codex PASS, kimi PASS. Gate on V31: codex `PREREG_UNSOUND` (two new findings, one cosmetic; PRIOR_FINDINGS_CLOSED=YES —
every V30 item closed), **kimi `PREREG_SOUND`** (no findings; PRIOR_FINDINGS_CLOSED=YES); both blind intact, C5_EXECUTABLE_UNDER_SCOPE=YES,
NO_MASKED_STAGE=YES. Reconciled BY TOPIC (`R3C2_V31_GATE_RECONCILIATION_20260907.md`, every label swept programmatically); all routine,
all repaired here and in the tools (kit: {NC} controls, {NP} deletion probes, PASS): `merge` preserves the alternative branch's
`origin_search` as `origin_search_alt` when that branch uses `ORIG_SILENT`, and `audit compare` checks the search belonging to the
matched branch, so a supported `ORIG_SILENT` alternative no longer fails and the verdict is independent of seat order (codex F1); the
search is compared as JSON structure, so key order cannot change a verdict (codex F2); the kit README states the probe contract as it
is — a probe kills its negative, or, where an authoritative guard overlaps the neutralised diagnostic, shows the diagnostic absent
while the guard still fails it (codex C1). **Next:** C0 and the gate on V32; then the completed plan and digest to Blanc for the
final-adoption checkpoint; the run only on Duho's fresh word.
"""
io.open(M,"w",encoding="utf-8").write(m); print("V32 master written")

import io,sys,re
T,SEAT,LANE,NC,NP=sys.argv[1:]
M="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; m=io.open(M,encoding="utf-8").read()
def rep(a,b,count=1):
    global m; pat=r"\s+(?:>\s*)?".join(re.escape(t) for t in a.split()); hits=re.findall(pat,m); assert len(hits)==count,(a[:60],len(hits)); m=re.sub(pat,lambda _: b,m,count=count)
def repx(pat,b):
    global m; assert re.search(pat,m),pat[:60]; m=re.sub(pat,b,m,count=1)
rep("Version 32 — LIVING DRAFT: V31 + the repairs from the two-seat gate on V31 (§10.27);","Version 33 — LIVING DRAFT: V32 + SEAT-PERMUTATION INVARIANCE, the pattern repair of the two-seat gate on V32 (§10.28); V32 = V31 + the repairs from the two-seat gate on V31 (§10.27);")
repx(r"The seat's tool is `r3c2_ledger_tools.py`,\s+sha256\s+`[0-9a-f]{64}`","The seat's tool is `r3c2_ledger_tools.py`, sha256 `"+SEAT+"`")
repx(r"the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document,\s+sha256\s+`[0-9a-f]{64}`","the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document, sha256 `"+LANE+"`")
repx(r"the lane owner runs `r3c2_lane_tools.py`\s+\(sha256\s+`[0-9a-f]{64}`;","the lane owner runs `r3c2_lane_tools.py` (sha256 `"+LANE+"`;")
# the invariant, stated ONCE, named; the merge sentence replaced per codex F1 and routed through the invariant
rep("An input matches only when its origin, origin evidence, parent list and any required `origin_search` jointly match one complete declared branch: `merge` preserves the primary branch's `origin_search` and the alternative branch's `origin_search_alt` whenever that branch uses `ORIG_SILENT`; `audit compare` checks the search belonging to the matched branch, as JSON structure (member equality, not key order); undeclared alternative fields keep their primary values, except that `origin_search` is required only for a branch using `ORIG_SILENT`; the verdict does not depend on which seat is A and which is B.",
    "**SEAT-PERMUTATION INVARIANCE (\"SPI\"): the audit verdict, and the whole audit outcome, are invariant under permutation of the census seats.** SPI is enforced at ONE place, `merge`: for every input it orders the two seats' records by a seat-blind canonical key (the smaller sha256 of each record's canonical JSON is the PRIMARY branch) and preserves the other seat's complete provenance branch — `origin_alt`, `origin_evidence_alt`, `origin_search_alt` when that branch uses `ORIG_SILENT`, and `derived_from_alt` — whenever origin, origin evidence, a required search or the parent set differs, equal origin labels included; the merged ledger is thereby a function of the SET of the two seat records, and no later step (branch matching, the search compared, root recomputation, ordering of records or results) can observe which seat came first. Evidence-only or search-only alternatives are not origin-classification disagreements and do not count toward the 10% rule. An input matches only when its origin, origin evidence, parent list and any required `origin_search` jointly match one complete preserved branch; searches are compared as JSON structure; hybrids and matches to neither branch are `MISMATCH`. SPI is exhibited by `r3c2_spi_exhibition.py` in the kit: every reviewer construction is merged in both seat orders and the merged bytes and the entire audit outcome must be equal; the same exhibition FAILS against pinned byte copies of the V32 tools.")
m=m.rstrip("\n")+f"""

## 10.28 V33 — SEAT-PERMUTATION INVARIANCE: the two-seat gate on V32 repaired as ONE PATTERN ({T})

C0 on V32: codex PASS, kimi PASS. Gate on V32: codex `PREREG_UNSOUND` (one finding, F1: with EQUAL origin labels and different complete
`origin_search` objects, `merge` kept only seat A's search, so the identical auditor record failed in A/B order and passed in B/A order;
PRIOR_FINDINGS_CLOSED=YES), **kimi `PREREG_SOUND`** (no findings; PRIOR_FINDINGS_CLOSED=YES); both blind intact, C5_EXECUTABLE_UNDER_SCOPE=YES,
NO_MASKED_STAGE=YES. Reconciled BY TOPIC (`R3C2_V32_GATE_RECONCILIATION_20260907.md`, sweep none missing).

**Second instance of one class** (Blanc's order of 04:37): V31's codex F1 was seat-order dependence too (an `ORIG_SILENT` alternative's
search dropped). The V32 repair was a point fix with "controls in both seat orders"; the class survived it. Under the third-failure rule
this version repairs the CLASS: (1) the invariant is stated once and named in §3 — SEAT-PERMUTATION INVARIANCE, "SPI"; (2) ONE place
enforces it — `merge` chooses the primary branch by a seat-blind canonical key and preserves the other seat's complete branch whenever
anything provenance-bearing differs, so the merged ledger is a function of the set of seat records and nothing downstream can observe
seat order; (3) the property, not the fixture, is exhibited — `r3c2_spi_exhibition.py` (kit) runs every reviewer construction (both
hybrid directions, the complete alternative branch, the wrong-owner dependency, transitive propagation through another claim's
alternative, agreeing root sets with a fabricated quotation, the `ORIG_SILENT` alternative, and same-origin different searches) under
both seat orders and asserts the merged bytes and the ENTIRE audit outcome (exit code, every failure line, the whole artefact) are
equal; (4) fail-first — the same exhibition FAILS against pinned byte copies of the V32 tools (`r3c2_staged_d1d7/_v32_bytecopy/`), with
the verdict flipping on the codex construction exactly, and PASSES against the delivered tools; the whole kit re-run ({NC} controls,
{NP} deletion probes, PASS) with NO pre-existing assertion in conflict; (5) no path resisted single-point enforcement.

**Blanc's question, answered:** YES — V31's "both seat orders" controls PASSED while V32's F1 was live (the V32 kit passed 182/182 with
them). They were blind because they asserted PASS for ONE fixture in both orders, a fixture whose two seats carried DIFFERENT origin
labels (`CHOSEN` vs `UNDECLARED`), so `merge`'s `origin != origin` condition always created the alternative; they asserted the verdict,
not equality of the whole outcome, and contained no fixture with equal labels and different searches — the exact condition that the
merge predicate excluded. The exhibition now asserts whole-outcome equality across permutations for every construction.
**Next:** C0 and the gate on V33; then the completed plan and digest to Blanc for the final-adoption checkpoint; the run only on Duho's
fresh word.
"""
io.open(M,"w",encoding="utf-8").write(m); print("V33 master written")

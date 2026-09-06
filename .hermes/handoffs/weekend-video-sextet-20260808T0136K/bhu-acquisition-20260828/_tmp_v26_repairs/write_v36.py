import io,sys,re
T,SEAT,LANE,NC,NP,KIMI=sys.argv[1:]
M="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; m=io.open(M,encoding="utf-8").read()
def rep(a,b,count=1):
    global m; pat=r"\s+(?:>\s*)?".join(re.escape(t) for t in a.split()); hits=re.findall(pat,m); assert len(hits)==count,(a[:60],len(hits)); m=re.sub(pat,lambda _: b,m,count=count)
def repx(pat,b):
    global m; assert re.search(pat,m),pat[:60]; m=re.sub(pat,b,m,count=1)
rep("Version 35 — LIVING DRAFT: V34 + complete provenance graphs preserved at merge, the two-seat gate on V34 (§10.30);","Version 36 — LIVING DRAFT: V35 + MEANINGLESS-ORDER INVARIANCE (the widened principle, Blanc 07:09) and the two-seat gate on V35 (§10.31); V35 = V34 + complete provenance graphs preserved at merge (§10.30);")
repx(r"The seat's tool is `r3c2_ledger_tools.py`,\s+sha256\s+`[0-9a-f]{64}`","The seat's tool is `r3c2_ledger_tools.py`, sha256 `"+SEAT+"`")
repx(r"the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document,\s+sha256\s+`[0-9a-f]{64}`","the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document, sha256 `"+LANE+"`")
repx(r"the lane owner runs `r3c2_lane_tools.py`\s+\(sha256\s+`[0-9a-f]{64}`;","the lane owner runs `r3c2_lane_tools.py` (sha256 `"+LANE+"`;")
i=m.index('**SEAT-PERMUTATION INVARIANCE ("SPI"): the audit verdict'); j=m.index("of the V32 tools and of the V33 tools.",i)+len("of the V32 tools and of the V33 tools.")
MOI=("**MEANINGLESS-ORDER INVARIANCE (\"MOI\", formerly SPI): the audit verdict and the whole audit outcome — verdict, the full ordered finding set with each finding's code and reason, the merged ledger bytes and the ledger digest — are invariant under every ordering that carries no meaning.** "
"The KNOWN sources of such ordering, each named: (a) which seat is primary (seat permutation — the former SPI, now one source among several); (b) the order in which records arrive or are merged; (c) the iteration order of unordered containers — sets, dicts built from sets, set differences, anything whose traversal depends on PYTHONHASHSEED; (d) JSON member order (closed by sorted-key serialisation — an instance of this principle, not a separate rule); (e) filesystem listing order — no delivered tool walks a directory, so this source has no instance today. The list is of KNOWN sources; the invariant governs any other that is found. "
"ENFORCEMENT is structural, at the boundary where each ordering is produced, so that no downstream step can observe it: `merge` orders the two seats by a seat-blind canonical key and the preserved complete graphs by their canonical digest, iterates inputs sorted, and serialises with sorted keys; `compute` classifies from the preserved graphs, iterates claims sorted and serialises with sorted keys; `audit compare` traverses every closure, root and graph-integrity walk in sorted order, reads the auditor's rederivation file, the candidate rows and the exclusion rows in sorted key order, and writes its artefact with sorted keys. Traversals and diagnostic selection are deterministic: starting input IDs and dependency IDs are visited in sorted order, and no reported error or output order depends on set iteration or process hash randomization; canonical branch selection remains solely at `merge`. "
"EXHIBITION, one combined property in `r3c2_spi_exhibition.py` (the file and its PASS token keep the historical name): every construction is run under both seat orders and PYTHONHASHSEED 0, 1 and 2 (0 and 1 reproduce the V35 diagnostic variation on the V35 bytes), plus one run with both seats' record lists reversed and one with the auditor's rederivation file in reversed member order, and the whole outcome must be identical across all of them — the only field allowed to differ in the reversed-rederivation run is the seal of the rederivation bytes, which is the digest of what was delivered, an identity and not an ordering; every construction also asserts its expected verdict and diagnostic. Constructions are derived from the enumerated sources, not only from reviewer counterexamples. Fail-first is PER SUBCASE, each its own kit test method, against pinned byte copies of the V35 tools (and of the V32–V34 tools for the earlier subcases).")
m=m[:i]+MOI+m[j:]
rep("A cycle or missing dependency in that matched graph fails the audit.",
    "Before root-origin classification, `audit compare` checks every `derived_from` edge in each selected claim's auditor-reconstructed dependency closure and its matched sealed closure for missing records and cycles, independently of `origin`. A missing dependency or cycle makes that claim `MISMATCH` and fails the audit, including when the cycle passes through a CHOSEN, FITTED, IMPORTED, MEASURED, STANDARD or UNDECLARED record. Root-origin traversal retains its stated origin rule; stopping at a non-DERIVED origin never substitutes for graph-integrity validation. Unmatched diagnostic views do not participate in this decision.")
m=m.rstrip("\n")+f"""

## 10.31 V36 — MEANINGLESS-ORDER INVARIANCE: the principle widened (Blanc 07:09) and the two-seat gate on V35 ({T})

C0 on V35: codex PASS, kimi PASS. Gate on V35: codex `PREREG_UNSOUND` (F1, F2), kimi `{KIMI}`; both PRIOR_FINDINGS_CLOSED=YES (the V34
findings closed), blind intact, C5 YES, no masked stage. Reconciled BY TOPIC (`R3C2_V35_GATE_RECONCILIATION_20260907.md`, sweep none missing).

**Third instance of one principle (Blanc 07:09).** V31 F1 and V32 F1: seat order changed the verdict. V35 F2: randomized set traversal
changed the complete audit outcome. SPI, defined as invariance under permutation of the census seats, closed the first two and had nothing
to say about the third. The invariant is therefore RESTATED once in §3 as MEANINGLESS-ORDER INVARIANCE: the verdict and the whole outcome
are invariant under any ordering that carries no meaning; the known sources are enumerated (a)–(e) with seat permutation as one source
among several; enforcement is structural at each production boundary (sorted traversal of every set, dict-from-set and file-ordered
mapping in the audit; sorted keys on every JSON write; canonical primary and graph order at merge) rather than asserted per site; the
exhibition is ONE combined property over seat orders × PYTHONHASHSEED {{0,1,2}} × reversed record arrival × reversed rederivation member
order with whole-outcome equality, its constructions derived from the enumerated sources and not only from the reviewer counterexamples.

**codex F1 (non-cosmetic, a FALSE PASS in the direction that matters):** a matched graph cycle passing through a CHOSEN record with
parents escaped detection, because root traversal stops at any non-DERIVED origin and the closure walker suppressed revisits without
diagnosing them. Repaired with codex's exact sentence: an origin-independent graph-integrity check over every dependency edge of the
auditor's closure and of the matched sealed closure runs BEFORE root classification; its own fail-first subcase. **codex F2 (non-cosmetic):**
the cycle diagnostic varied between processes (`cycle at x` / `cycle at y`) because root recomputation iterated a set — closed by the
structural enforcement above; its own fail-first subcase (seeds 0 and 1 reproduce it on the V35 bytes). Additional subcases from the
enumerated sources: a missing dependency in the auditor's closure; several diagnostics at once (two missing dependencies and two value
mismatches) whose emitted order must be identical under every seed and order; record arrival order; rederivation member order; JSON
member order.

**Per-subcase fail-first evidence against pinned V35 byte copies** (`r3c2_staged_d1d7/_v35_bytecopy/`): F1 FAILS (verdict 0 where 1 is
required, no graph-integrity diagnostic); F2 FAILS (outcomes differ across seeds); missing-dependency FAILS (no graph-integrity
diagnostic); multi-diagnostic FAILS (no graph-integrity diagnostic); the member-order, V34 mixed-cycle and V32 same-origin-search
subcases PASS on the V35 bytes — those defects were closed earlier, and the rows are retained as controls, stated as such. The full
property PASSES on the delivered tools. Kit: {NC} controls, {NP} deletion probes, PASS. **Next:** C0 and the gate on V36.
"""
io.open(M,"w",encoding="utf-8").write(m); print("V36 master written")

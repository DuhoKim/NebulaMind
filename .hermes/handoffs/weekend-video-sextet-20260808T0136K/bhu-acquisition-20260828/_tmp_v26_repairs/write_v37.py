import io,sys,re
T,SEAT,LANE,NC,NP=sys.argv[1:]
M="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; m=io.open(M,encoding="utf-8").read()
def rep(a,b,count=1):
    global m; pat=r"\s+(?:>\s*)?".join(re.escape(t) for t in a.split()); hits=re.findall(pat,m); assert len(hits)==count,(a[:60],len(hits)); m=re.sub(pat,lambda _: b,m,count=count)
def repx(pat,b):
    global m; assert re.search(pat,m),pat[:60]; m=re.sub(pat,b,m,count=1)
rep("Version 36 — LIVING DRAFT: V35 + MEANINGLESS-ORDER INVARIANCE (the widened principle, Blanc 07:09) and the two-seat gate on V35 (§10.31);","Version 37 — LIVING DRAFT: V36 + dependency-list order as a MOI source, origin-independent graph integrity at both C3 boundaries, and the exact-failure predicate for every negative control (§10.32); V36 = V35 + MEANINGLESS-ORDER INVARIANCE (§10.31);")
repx(r"The seat's tool is `r3c2_ledger_tools.py`,\s+sha256\s+`[0-9a-f]{64}`","The seat's tool is `r3c2_ledger_tools.py`, sha256 `"+SEAT+"`")
repx(r"the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document,\s+sha256\s+`[0-9a-f]{64}`","the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document, sha256 `"+LANE+"`")
repx(r"the lane owner runs `r3c2_lane_tools.py`\s+\(sha256\s+`[0-9a-f]{64}`;","the lane owner runs `r3c2_lane_tools.py` (sha256 `"+LANE+"`;")
# --- codex V36 F1: the invariant sentence (his exact replacement)
rep('MEANINGLESS-ORDER INVARIANCE ("MOI", formerly SPI): the audit verdict and the whole audit outcome — verdict, the full ordered finding set with each finding\'s code and reason, the merged ledger bytes and the ledger digest — are invariant under every ordering that carries no meaning.**',
 'MEANINGLESS-ORDER INVARIANCE ("MOI", formerly SPI): the audit verdict and the whole audit outcome — verdict, the full ordered finding set with each finding\'s code and reason, the merged ledger bytes and the ledger digest — are invariant under every ordering that carries no meaning, including dependency-list order. Before computing canonical record keys or graph digests, selecting branches, deduplicating graphs or serialising merged output, `merge` normalises every `derived_from` list into sorted input-id order in both complete seat graphs and every retained primary or alternative record. This does not reorder a paper\'s computational operations: `derived_from` records dependency edges, not an execution sequence.**')
# --- Blanc 07:58: dependency order becomes an ENUMERATED source; codex C1 + kimi's cosmetic: source (e) corrected
rep("(e) filesystem listing order — no delivered tool walks a directory, so this source has no instance today. The list is of KNOWN sources; the invariant governs any other that is found.",
 "(e) filesystem listing order — `r3c2_manifest.py` walks a directory and sorts subdirectory names, filenames and final digest rows; this source has a delivered instance whose ordering is already normalised; (f) dependency-list order — the order of ids inside a `derived_from` list, normalised at `merge` as stated above and exercised in the combined property. The list is of KNOWN sources; the invariant governs any other that is found.")
# --- codex V36 F3: the fail-first sentence (his exact replacement) + the predicate stated in the operative text
rep("Fail-first is PER SUBCASE, each its own kit test method, against pinned byte copies of the V35 tools (and of the V32–V34 tools for the earlier subcases).",
 "**A NEGATIVE CONTROL MUST ASSERT THE EXACT EXPECTED FAILURE, NEVER THE BARE POLARITY.** Fail-first is tested independently for every subcase against pinned predecessor bytes. Each test requires successful fixture setup, the exact expected exhibition exit code and completion token, exactly the selected construction rows, and that subcase's expected verdicts, ordered diagnostics and equality results. F1 requires a false audit PASS with the graph-integrity diagnostic absent; F2 requires audit FAIL with unequal complete outcomes across seeds 0 and 1; the missing-dependency and multi-diagnostic subcases require audit FAIL with the specified graph-integrity diagnostics absent; the dependency-order subcase requires unequal merged bytes whose differing runs are the dependency-order runs. A launch error, traceback, missing artefact, empty construction selection, a construction whose merge did not run, or an unrelated failure fails the kit test. Rows expected to pass on predecessor bytes remain explicitly labelled controls. The same rule governs every other control in the kit that judges an outcome, the deletion probes included: each asserts its own diagnostic and exit code, and no traceback or launch failure can satisfy one.")
# --- codex V36 F2: the C3 boundary sentence (his exact replacement)
rep("Every `DERIVED` record lists its `derived_from` ids; `validate` fails a `derived_from` id that names no record, a cycle, and a `DERIVED` record with no `derived_from`.",
 "Every `DERIVED` record lists its `derived_from` ids. Before root classification, `validate` checks every dependency edge of the complete input graph independently of origin and returns FAIL for any missing dependency or cycle; it also rejects a `DERIVED` record with no parents. Lane-side `compute` applies the same origin-independent integrity check to every complete provenance graph it classifies and fails before writing output if any graph is invalid. Stopping root traversal at a non-DERIVED origin never substitutes for either integrity check.")
m=m.rstrip("\n")+f"""

## 10.32 V37 — dependency-list order, the C3 integrity boundaries, and the exact-failure predicate ({T})

C0 on V36: codex PASS, kimi PASS. Gate on V36: codex `PREREG_UNSOUND` (F1, F2, F3 non-cosmetic; C1 cosmetic), kimi
`PREREG_SOUND_WITH_REPAIRS` (no numbered findings; one cosmetic — the same false filesystem sentence — and two observations); both
PRIOR_FINDINGS_CLOSED=YES, blind intact, C5 YES, no masked stage. Reconciled BY TOPIC (`R3C2_V36_GATE_RECONCILIATION_20260907.md`,
sweep none missing). Blanc's order of 07:58 governs this version.

**F3 — the fourth instance of one disease, and the priority.** The kit's MOI helper decided a fail-first case by `got_pass ==
expect_pass`, so ANY failure counted as the expected negative: an unrelated launch failure exiting 2 was credited as fail-first
evidence. The rule is now stated ONCE in the operative text and once at the head of the kit, and applied wherever a control judges an
outcome: **a negative control must assert the exact expected failure, never the bare polarity** — successful setup (no traceback, no
import or launch error, no usage banner, non-empty output), the expected completion token and exit code, a non-empty selection of
exactly the expected rows, and that subcase's own verdicts, diagnostic text and equality results; a construction whose merge did not
run is an infrastructure failure and never evidence. The deletion-probe judge carries the same setup guard. Three meta-controls hold the
predicate itself: an unrelated launch failure is rejected; a REAL failure of a DIFFERENT subcase is rejected against this subcase's
expectations; and the right subcase failing for the wrong stated reason is rejected.

**What the old predicate was propping up, measured:** on the twelve real cases the two predicates agree — **0 cases** were passing only
because of the polarity test, and the historical fail-first evidence is genuine (codex's independent runs reproduced all four V35
failures). The difference is what each ACCEPTS: pointed at an emptied tools directory, the retired predicate credits **8 of 8** negative
cases as fail-first evidence; the exact-failure predicate credits **0 of 8**. The measurement script and its output are in the run log.

**F1 — dependency-list order, a MOI source the implementation missed.** Reversing a `derived_from` list changed merged bytes, the ledger
digest, compute output and the audit artefact while all verdicts still PASSED — not a verdict flip, and recorded as what it is: exactly
the case §3's own clause anticipated when it said the enumerated list is of KNOWN sources and the invariant governs any other found. The
sentence stood; the implementation did not. Canonicalisation happens at ONE place, the head of `merge`: every `derived_from` and
`derived_from_alt` list of both seat ledgers is sorted BEFORE canonical record keys, graph digests, branch selection, graph
deduplication and serialisation, so both preserved complete graphs and every retained primary or alternative record carry sorted edges
and no later step can observe the original order. Dependency order is now enumerated source (f), and the combined property gained three
runs per construction: reversed dependency lists in both seat ledgers under both seat orders, and reversed dependency lists in the
auditor's reconstruction — 20 constructions × 9 runs each.

**F2 — origin-independent graph integrity at both C3 boundaries.** A CHOSEN record whose `derived_from` named itself passed `validate`
(C3_NO_SUBSTITUTION=PASS) and was classified USES_CHOSEN by `compute`, because both relied on root traversal, which stops at a
non-DERIVED origin. Repaired with codex's exact sentence at both boundaries: `validate` now walks every dependency edge independently of
origin before root classification, and `compute` checks every complete provenance graph before writing any output. C6's independent
verification is unchanged; this was a false pass of the C3 boundary, not an end-to-end census escape, and it does not reopen the V35 C6
finding. Both new guards carry deletion probes.

**C1 (codex) and kimi's cosmetic — the same sentence:** source (e) claimed no delivered tool walks the filesystem; `r3c2_manifest.py`
does, and already sorts directory names, filenames and digest rows. Corrected with codex's exact replacement; the behaviour, which is
right, is untouched. **kimi's observation (i):** §10.31 said three subcases pass on the V35 bytes and are retained as controls, but the
kit carried two — the third (same-origin searches) is now a kit control row, and this correction is recorded here rather than by
rewriting §10.31, which is history. **kimi's observation (ii):** the lane tool's `roots_alt` helper had been dead since V35 and is
removed; it reached no output.

Kit: {NC} controls, {NP} deletion probes, PASS. **Next:** C0 and the gate on V37.
"""
io.open(M,"w",encoding="utf-8").write(m); print("V37 master written")

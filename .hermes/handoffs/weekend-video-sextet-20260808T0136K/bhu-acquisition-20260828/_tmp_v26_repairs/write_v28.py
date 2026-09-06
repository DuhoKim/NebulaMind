import io,sys,re
T,SEAT,LANE,BAT,NC,NP=sys.argv[1:]
M="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; m=io.open(M,encoding="utf-8").read()
def rep(a,b,count=1):
    global m; pat=r"\s+(?:>\s*)?".join(re.escape(t) for t in a.split()); hits=re.findall(pat,m); assert len(hits)==count,(a[:60],len(hits)); m=re.sub(pat,lambda _: b,m,count=count)
def repx(pat,b):
    global m; assert re.search(pat,m),pat[:60]; m=re.sub(pat,b,m,count=1)
rep("Version 27 — LIVING DRAFT: V26 + the repairs from the two-seat gate on V26 and the routine `rests_on` label (§10.22);","Version 28 — LIVING DRAFT: V27 + the repairs from the two-seat gate on V27 (§10.23); V27 = V26 + the repairs from the two-seat gate on V26 and the routine `rests_on` label (§10.22);")
repx(r"The seat's tool is `r3c2_ledger_tools.py`,\s+sha256\s+`[0-9a-f]{64}`","The seat's tool is `r3c2_ledger_tools.py`, sha256 `"+SEAT+"`")
repx(r"the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document,\s+sha256\s+`[0-9a-f]{64}`","the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document, sha256 `"+LANE+"`")
repx(r"the lane owner runs `r3c2_lane_tools.py`\s+\(sha256\s+`[0-9a-f]{64}`;","the lane owner runs `r3c2_lane_tools.py` (sha256 `"+LANE+"`;")
repx(r"`r3c2_batch_tools.py`,\s+sha256\s+`[0-9a-f]{64}`","`r3c2_batch_tools.py`, sha256 `"+BAT+"`")
# codex C1 / kimi F1: the parenthesis
rep("`DERIVED_STANDARD_OR_MEASURED_ONLY` (the token `DERIVED_STANDARD_OR_MEASURED_ONLY` of V10–V26, identical membership)","`DERIVED_STANDARD_OR_MEASURED_ONLY` (formerly `DERIVED_ONLY`, with identical membership)")
# codex F2: disputed root sentence
rep("A claim with a disputed root carries the pair computed under both classifications and is marked `DISPUTED`.",
    "A claim with a disputed input or parent list carries both script-computed classifications and is marked `DISPUTED`. During the C6 comparison an auditor classification is bound to the matching declared sealed origin, evidence and parent-list branch; roots are recomputed under that branch and compared like with like; both sealed branches and the auditor's matching branch are reported. Matching an explicitly declared alternative is not `MISMATCH`; an unsupported classification or graph difference remains `MISMATCH`.")
# codex F3: STANDARD / BLOCKED requirement
rep("`STANDARD` additionally requires the value as a numeric token at the record's own cited line and closed-list membership; `BLOCKED` additionally requires an empty value and naming evidence in the claiming file.",
    "every `STANDARD` record, including one with `ORIG_SILENT`, requires a non-empty `source_file`, a positive one-based `source_line`, closed-list membership and the value as a numeric token at that line — absence of origin evidence never waives value evidence; every `BLOCKED` record requires an empty value, `IMPORTED`/`ORIG_CITATION`, and a candidate-file binding proving that its naming-evidence file is the claiming file; missing coordinates or a missing candidate binding fails `validate`.")
# codex F4: the "script asserts" sentence
rep("that **each `PRINTED` value machine-matches the text at its cited source line and each verbatim quotation is a substring of that line**, and that **each `STANDARD` value is one of a closed list PRINTED LITERALLY BELOW**",
    "that **each `PRINTED` value machine-matches its `source_file`/`source_line` as a numeric token and each non-`ORIG_SILENT` quotation occurs at its own `origin_evidence.source_file`/`source_line` — the evidence line may differ from the value line, and no second quotation check is applied to the value line**, and that **each `STANDARD` value is one of a closed list PRINTED LITERALLY BELOW and satisfies its own value-line check**")
# codex F1: the audit compare clause
rep("`audit compare` compares those reconstructed fields and dependency edges against the sealed ledger, carrying a declared origin alternative explicitly, and a missing input, a differing dependency edge or an unsupported record is `MISMATCH`; it recomputes each input's chain of origins to its roots from both reconstructions and prints the comparison.",
    "before sealing, `audit seal-rederivation` validates the reconstruction schema — every input carries symbol, status, value, source coordinates, origin, origin evidence and `derived_from` (and `origin_search` when silent) — and refuses an incomplete one; `audit compare` requires every one of those fields, compares every field, every evidence coordinate and quotation, and every dependency edge against the sealed ledger, binds an auditor classification that matches a declared sealed alternative to that branch (§3), and reports a missing field, a missing input, a dependency the auditor did not itself reconstruct, or any unsupported difference as `MISMATCH`; it recomputes each input's chain of origins to its roots from the auditor's own graph and from the sealed ledger under the matching branch and prints the comparison.")
m=m.rstrip("\n")+f"""

## 10.23 V28 — the two-seat gate on V27, reconciled and repaired here ({T})

C0 on V27 (the restored master `12daf4f5…`): codex PASS, kimi PASS. Gate on V27: codex `PREREG_UNSOUND` (four findings, two cosmetics;
LEAK=NONE), kimi `PREREG_SOUND_WITH_REPAIRS` (two cosmetics; 19 of 20 prior items closed); both C5_EXECUTABLE_UNDER_SCOPE=YES,
NO_MASKED_STAGE=YES; prior findings: every V26 item closed by both except the audit's completeness (codex) and the tool docstrings
(kimi). Reconciled BY TOPIC (`R3C2_V27_GATE_RECONCILIATION_20260907.md`); all routine, all repaired here and in the tools (kit: {NC}
controls, {NP} deletion probes, PASS): the audit accepts only complete reconstructions (schema validated at the re-derivation seal),
compares every field, evidence coordinate and quotation, and never borrows a dependency from the sealed side (codex F1); a declared
sealed alternative is compared like with like under its branch (codex F2); `STANDARD` coordinates are required unconditionally and
`BLOCKED` naming evidence is bound to the claiming file (codex F3); an ordinary `PRINTED` record may cite its evidence on a line other
than its value line, the value being checked at its own line only (codex F4); the historical parenthesis (codex C1 / kimi F1); the
delivered lane and batch tool docstrings (codex C2 / kimi F2, kimi's V26 N1). **Next:** C0 and the gate on V28; then the completed plan
and digest to Blanc for the final-adoption checkpoint; the run only on Duho's fresh word.
"""
io.open(M,"w",encoding="utf-8").write(m); print("V28 master written")

import io,sys,re
T,SEAT,LANE,BAT,MANI,BLD,CM,PART,NC,NP=sys.argv[1:]
M="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; m=io.open(M,encoding="utf-8").read()
def rep(a,b,count=1):
    global m; pat=r"\s+(?:>\s*)?".join(re.escape(t) for t in a.split()); hits=re.findall(pat,m); assert len(hits)==count,(a[:60],len(hits)); m=re.sub(pat,lambda _: b,m,count=count)
def repx(pat,b):
    global m; assert re.search(pat,m),pat[:60]; m=re.sub(pat,b,m,count=1)
rep("Version 28 — LIVING DRAFT: V27 + the repairs from the two-seat gate on V27 (§10.23);","Version 29 — LIVING DRAFT: V28 + the repairs from the two-seat gate on V28 (§10.24); V28 = V27 + the repairs from the two-seat gate on V27 (§10.23);")
repx(r"The seat's tool is `r3c2_ledger_tools.py`,\s+sha256\s+`[0-9a-f]{64}`","The seat's tool is `r3c2_ledger_tools.py`, sha256 `"+SEAT+"`")
repx(r"the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document,\s+sha256\s+`[0-9a-f]{64}`","the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document, sha256 `"+LANE+"`")
repx(r"the lane owner runs `r3c2_lane_tools.py`\s+\(sha256\s+`[0-9a-f]{64}`;","the lane owner runs `r3c2_lane_tools.py` (sha256 `"+LANE+"`;")
repx(r"`r3c2_batch_tools.py`,\s+sha256\s+`[0-9a-f]{64}`;\s+partition\s+`[0-9a-f]{16}…`","`r3c2_batch_tools.py`, sha256 `"+BAT+"`; partition `"+PART[:16]+"…`")
repx(r"`r3c2_manifest.py` is committed beside this document,\s+sha256\s+`[0-9a-f]{64}`","`r3c2_manifest.py` is committed beside this document, sha256 `"+MANI+"`")
repx(r"this document,\s+sha256\s+`[0-9a-f]{64}`\s+\(it accepts explicit `--master`","this document, sha256 `"+BLD+"` (it accepts explicit `--master`")
repx(r"\*\*The corpus is pinned: `R3C2_CORPUS_MANIFEST.md` \(sha256\s+`[0-9a-f]{64}`","**The corpus is pinned: `R3C2_CORPUS_MANIFEST.md` (sha256 `"+CM+"`")
# codex F1 (§3 sentence)
rep("During the C6 comparison an auditor classification is bound to the matching declared sealed origin, evidence and parent-list branch; roots are recomputed under that branch and compared like with like; both sealed branches and the auditor's matching branch are reported.",
    "During the C6 comparison, first every reconstructed input in the complete dependency closure of each selected claim — including records assigned to claims outside `audited_ids` — is validated and compared: each record is bound to its sealed `input_id` and claim, every required field, evidence coordinate, quotation and dependency edge is compared, and any unsupported difference is `MISMATCH` on every selected claim that depends on it; branch matching is performed over this full closure before roots are recomputed; both sealed branches and the auditor's matching branch are reported.")
# codex F2
rep("Matching an explicitly declared alternative is not `MISMATCH`; an unsupported classification or graph difference remains `MISMATCH`.",
    "Matching an explicitly declared alternative is not `MISMATCH`: the auditor's origin, origin evidence and parent list are matched against the complete declared primary or alternative record, including an alternative parent list when the origin is unchanged; one consistent matched-branch graph is constructed over the selected claims and their complete dependency closure and used for every dependent claim's sealed-root comparison; an unsupported record, evidence, parent list or inconsistent branch remains `MISMATCH`; both sealed branches and the matching branch are reported without reconciling the original dispute.")
# codex F3 (§2 STANDARD sentence)
rep("**`STANDARD` applies only when the value appears in the claiming paper (or in a pinned enumerable text under the `IMPORTED` rule below): a value the paper does not print is classified by the named-source rule alone and is never `STANDARD`.",
    "**`STANDARD` applies to a closed-list value printed in the claiming paper: for every `STANDARD` record `validate` binds `claim_id` to the claiming file through the candidate file and checks its own positive value coordinates and numeric token; a value outside the claiming file follows the named-source rule and is recorded `PRINTED`/`IMPORTED` with `ORIG_CITATION`, a verified enumerable source and the first symbol-and-value line, even when the value is on the closed list; a missing candidate binding or a `STANDARD` value line outside the claiming file fails `validate`.")
# kimi N5 (merge sentence)
rep("where the two `derived_from` lists differ the merged record carries both parent lists marked `PARENTS_DISPUTED`, and `compute` derives `root_origins` under both, printed as a pair, as for a disputed origin.",
    "where the two `derived_from` lists differ the merged record carries both parent lists marked `PARENTS_DISPUTED`, and `compute` derives `root_origins` under both, printed as a pair, as for a disputed origin; where the two seats' value, status, symbol or source coordinates differ on the same input id, `merge` prints every such disagreement, reports `FIELD_DISAGREEMENTS`, exits 1 and writes no merged file — the lane resolves it in the open before the tally.")
m=m.rstrip("\n")+f"""

## 10.24 V29 — the two-seat gate on V28, reconciled and repaired here ({T})

C0 on V28: codex PASS, kimi PASS. Gate on V28: codex `PREREG_UNSOUND` (three findings; LEAK content-level only), kimi
`PREREG_SOUND_WITH_REPAIRS` (five cosmetics, no executable defect); both C5_EXECUTABLE_UNDER_SCOPE=YES, NO_MASKED_STAGE=YES; prior V27
findings closed by both except the audit's closure comparison and the declared-alternative rule (codex, PARTLY) and the docstring
remnants (both). Reconciled BY TOPIC (`R3C2_V28_GATE_RECONCILIATION_20260907.md`); all routine, all repaired here and in the tools (kit:
{NC} controls, {NP} deletion probes, PASS): every reconstructed record in a selected claim's complete dependency closure is compared,
off-sample claims' records included (codex F1); a declared alternative — origin and/or parent list — is matched over the whole closure
once and the sealed roots are recomputed under that graph, so parent-only and inherited alternatives pass (codex F2); a `STANDARD`
value line outside the claiming file is an import, not `STANDARD` (codex F3); the builder prints byte counts (kimi N1); the corpus
manifest's informational line column carries its stated convention, the manifest re-pinned (`{CM[:16]}…`) and the partition regenerated
(`{PART[:16]}…`) (kimi N2); the kit README (kimi N3); the manifest tool's docstring, the seat tool's labels and its usage synopsis (kimi
N4 / codex C2); `merge` fails in the open on a value, status, symbol or coordinate disagreement (kimi N5). **Next:** C0 and the gate on
V29; then the completed plan and digest to Blanc for the final-adoption checkpoint; the run only on Duho's fresh word.
"""
io.open(M,"w",encoding="utf-8").write(m); print("V29 master written")

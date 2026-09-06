import io,sys,re
T,SEAT,CM,PART,BAT,NC,NP=sys.argv[1:]
M="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; m=io.open(M,encoding="utf-8").read()
def rep(a,b,count=1):
    global m; pat=r"\s+(?:>\s*)?".join(re.escape(t) for t in a.split()); hits=re.findall(pat,m); assert len(hits)==count,(a[:60],len(hits)); m=re.sub(pat,lambda _: b,m,count=count)
def repx(pat,b):
    global m; assert re.search(pat,m),pat[:60]; m=re.sub(pat,b,m,count=1)
rep("Version 29 — LIVING DRAFT: V28 + the repairs from the two-seat gate on V28 (§10.24);","Version 30 — LIVING DRAFT: V29 + the repairs from the two-seat gate on V29 (§10.25); V29 = V28 + the repairs from the two-seat gate on V28 (§10.24);")
repx(r"The seat's tool is `r3c2_ledger_tools.py`,\s+sha256\s+`[0-9a-f]{64}`","The seat's tool is `r3c2_ledger_tools.py`, sha256 `"+SEAT+"`")
repx(r"`r3c2_batch_tools.py`,\s+sha256\s+`[0-9a-f]{64}`;\s+partition\s+`[0-9a-f]{16}…`","`r3c2_batch_tools.py`, sha256 `"+BAT+"`; partition `"+PART[:16]+"…`")
repx(r"\*\*The corpus is pinned: `R3C2_CORPUS_MANIFEST.md` \(sha256\s+`[0-9a-f]{64}`","**The corpus is pinned: `R3C2_CORPUS_MANIFEST.md` (sha256 `"+CM+"`")
rep("During the C6 comparison, first every reconstructed input in the complete dependency closure of each selected claim — including records assigned to claims outside `audited_ids` — is validated and compared: each record is bound to its sealed `input_id` and claim, every required field, evidence coordinate, quotation and dependency edge is compared, and any unsupported difference is `MISMATCH` on every selected claim that depends on it; branch matching is performed over this full closure before roots are recomputed; both sealed branches and the auditor's matching branch are reported.",
    "Before sealing or comparing a reconstruction, every `input_id` must occur exactly once across the entire reconstruction, and an explicit `claim_id` or `input_id` field must agree with its enclosing keys; at comparison each reconstructed record is bound to its sealed identity — its enclosing claim key must be the sealed record's claim — and a duplicate, an identity conflict, a missing record or an unsupported field, evidence or edge difference is `MISMATCH` on every selected claim that depends on it; every record in each selected claim's complete dependency closure is validated and compared, records assigned to unselected claims included; complete branch matching is performed over this closure before roots are recomputed, and the sealed and matched branches are reported.")
rep("Matching an explicitly declared alternative is not `MISMATCH`: the auditor's origin, origin evidence and parent list are matched against the complete declared primary or alternative record, including an alternative parent list when the origin is unchanged; one consistent matched-branch graph is constructed over the selected claims and their complete dependency closure and used for every dependent claim's sealed-root comparison; an unsupported record, evidence, parent list or inconsistent branch remains `MISMATCH`; both sealed branches and the matching branch are reported without reconciling the original dispute.",
    "Matching a declared alternative is not `MISMATCH` only when the auditor's origin, origin evidence and parent list jointly equal one COMPLETE declared branch: the primary branch is the primary fields, the alternative branch is every declared alternative field applied together with the undeclared fields staying primary; an unchanged-origin parent alternative is accepted only when the alternative branch's origin and evidence are also unchanged; a record matching neither complete branch is `MISMATCH` even when the root-origin sets agree; one consistent graph is constructed from the matched complete records over all selected claims and their dependency closures and used for every dependent claim's sealed-root comparison; the original disputes and the matched branches are reported without reconciling the dispute.")
m=m.rstrip("\n")+f"""

## 10.25 V30 — the two-seat gate on V29, reconciled and repaired here ({T})

C0 on V29: codex PASS, kimi PASS. Gate on V29: codex `PREREG_UNSOUND` (two findings; blind intact), kimi `PREREG_SOUND_WITH_REPAIRS` (two
cosmetics, no executable defect); both C5_EXECUTABLE_UNDER_SCOPE=YES, NO_MASKED_STAGE=YES; prior V28 findings closed by both except the
two codex corners (PARTLY) and the manifest column (kimi, PARTLY). Reconciled BY TOPIC (`R3C2_V29_GATE_RECONCILIATION_20260907.md`); all
routine, all repaired here and in the tools (kit: {NC} controls, {NP} deletion probes, PASS): a reconstruction's `input_id`s are unique
across the whole reconstruction, explicit identity fields must agree with their keys, and at comparison each record is bound to its
sealed claim — a duplicate can no longer shadow a fabricated copy and a mis-keyed record is `MISMATCH` (codex F1); a declared alternative
matches only as a COMPLETE branch — a hybrid of primary and alternative fields is `MISMATCH` even when the roots agree (codex F2); the
corpus manifest's informational line column now states its convention at the character level (newline-delimited; space, tab and
carriage return are the only blank characters) and is recomputed to it, the manifest re-pinned (`{CM[:16]}…`) and the partition
regenerated (`{PART[:16]}…`) (kimi N1); a duplicated comment line removed from the seat tool (kimi N2). **Next:** C0 and the gate on V30;
then the completed plan and digest to Blanc for the final-adoption checkpoint; the run only on Duho's fresh word.
"""
io.open(M,"w",encoding="utf-8").write(m); print("V30 master written")

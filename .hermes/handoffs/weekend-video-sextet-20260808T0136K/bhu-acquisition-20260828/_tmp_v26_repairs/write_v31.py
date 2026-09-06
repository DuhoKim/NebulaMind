import io,sys,re
T,SEAT,CM,PART,BAT,NC,NP=sys.argv[1:]
M="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; m=io.open(M,encoding="utf-8").read()
def rep(a,b,count=1):
    global m; pat=r"\s+(?:>\s*)?".join(re.escape(t) for t in a.split()); hits=re.findall(pat,m); assert len(hits)==count,(a[:60],len(hits)); m=re.sub(pat,lambda _: b,m,count=count)
def repx(pat,b):
    global m; assert re.search(pat,m),pat[:60]; m=re.sub(pat,b,m,count=1)
rep("Version 30 — LIVING DRAFT: V29 + the repairs from the two-seat gate on V29 (§10.25);","Version 31 — LIVING DRAFT: V30 + the repairs from the two-seat gate on V30 (§10.26); V30 = V29 + the repairs from the two-seat gate on V29 (§10.25);")
repx(r"The seat's tool is `r3c2_ledger_tools.py`,\s+sha256\s+`[0-9a-f]{64}`","The seat's tool is `r3c2_ledger_tools.py`, sha256 `"+SEAT+"`")
repx(r"`r3c2_batch_tools.py`,\s+sha256\s+`[0-9a-f]{64}`;\s+partition\s+`[0-9a-f]{16}…`","`r3c2_batch_tools.py`, sha256 `"+BAT+"`; partition `"+PART[:16]+"…`")
repx(r"\*\*The corpus is pinned: `R3C2_CORPUS_MANIFEST.md` \(sha256\s+`[0-9a-f]{64}`","**The corpus is pinned: `R3C2_CORPUS_MANIFEST.md` (sha256 `"+CM+"`")
rep("Before sealing or comparing a reconstruction, every `input_id` must occur exactly once across the entire reconstruction, and an explicit `claim_id` or `input_id` field must agree with its enclosing keys; at comparison each reconstructed record is bound to its sealed identity — its enclosing claim key must be the sealed record's claim — and a duplicate, an identity conflict, a missing record or an unsupported field, evidence or edge difference is `MISMATCH` on every selected claim that depends on it; every record in each selected claim's complete dependency closure is validated and compared, records assigned to unselected claims included; complete branch matching is performed over this closure before roots are recomputed, and the sealed and matched branches are reported.",
    "Before sealing, a reconstruction with a duplicate `input_id` or an explicit identity field inconsistent with its enclosing keys is refused. At comparison, each enclosing-claim versus sealed-claim identity conflict is recorded as a `MISMATCH` of that input, propagated to every selected claim whose dependency closure contains the input, and fails the overall audit; every required field, evidence item and dependency edge is compared throughout each selected claim's complete dependency closure, records assigned to unselected claims included; complete branches are matched before roots are recomputed, and the sealed and matched branches are reported.")
rep("Matching a declared alternative is not `MISMATCH` only when the auditor's origin, origin evidence and parent list jointly equal one COMPLETE declared branch: the primary branch is the primary fields, the alternative branch is every declared alternative field applied together with the undeclared fields staying primary; an unchanged-origin parent alternative is accepted only when the alternative branch's origin and evidence are also unchanged; a record matching neither complete branch is `MISMATCH` even when the root-origin sets agree; one consistent graph is constructed from the matched complete records over all selected claims and their dependency closures and used for every dependent claim's sealed-root comparison; the original disputes and the matched branches are reported without reconciling the dispute.",
    "An input matches only if its origin, origin evidence and parent list jointly equal the complete primary branch or the complete alternative branch, every declared alternative field applied together and undeclared fields left primary. If neither complete branch matches, an unconditional record-level `MISMATCH` is appended before any field-specific diagnostic, propagated to every dependent selected claim, and the audit fails even when the root-origin sets agree — the full-record predicate decides the verdict and the diagnostics only explain it. The comparison graph is constructed only from matched branches; the original disputes and the matched branches are reported without reconciliation.")
m=m.rstrip("\n")+f"""

## 10.26 V31 — the two-seat gate on V30, reconciled and repaired here ({T})

C0 on V30: codex PASS, kimi PASS. Gate on V30: codex `PREREG_UNSOUND` (two findings, one cosmetic; blind intact), kimi
`PREREG_SOUND_WITH_REPAIRS` (only the carried, declared-deferred manifest header); both C5_EXECUTABLE_UNDER_SCOPE=YES,
NO_MASKED_STAGE=YES. Reconciled BY TOPIC (`R3C2_V30_GATE_RECONCILIATION_20260907.md`, every label swept programmatically); all routine,
all repaired here and in the tools (kit: {NC} controls, {NP} deletion probes, PASS): the full-record branch predicate is authoritative —
a record matching neither complete declared branch is an unconditional `MISMATCH` before any diagnostic, so the REVERSE hybrid
(alternative origin and evidence with the primary parents) fails (codex F2); an identity conflict is a `MISMATCH` of the record itself,
carried into every dependent selected claim's rows (codex F1); the manifest header now says the line column is summed and reported by
the partition tool and used as no integrity predicate, the manifest re-pinned (`{CM[:16]}…`) and the partition regenerated
(`{PART[:16]}…`) (codex C1 / kimi C1, deferred from V29). **Discipline recorded (Blanc's order of 03:03):** the authoritative guard had
been REMOVED by the lane at 02:31 so that three deletion probes could register kills — the reverse hybrid was the consequence; the guard
is restored and never again weakened for a probe: the affected probes now assert that the specific diagnostic disappears while the
verdict still fails on the guard. **Next:** C0 and the gate on V31; then the completed plan and digest to Blanc for the final-adoption
checkpoint; the run only on Duho's fresh word.
"""
io.open(M,"w",encoding="utf-8").write(m); print("V31 master written")

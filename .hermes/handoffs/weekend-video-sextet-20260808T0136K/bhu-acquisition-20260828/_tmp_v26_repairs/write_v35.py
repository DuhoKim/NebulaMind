import io,sys,re
T,SEAT,LANE,NC,NP=sys.argv[1:]
M="R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md"; m=io.open(M,encoding="utf-8").read()
def rep(a,b,count=1):
    global m; pat=r"\s+(?:>\s*)?".join(re.escape(t) for t in a.split()); hits=re.findall(pat,m); assert len(hits)==count,(a[:60],len(hits)); m=re.sub(pat,lambda _: b,m,count=count)
def repx(pat,b):
    global m; assert re.search(pat,m),pat[:60]; m=re.sub(pat,b,m,count=1)
rep("Version 34 — LIVING DRAFT: V33 + the two-seat gate on V33 closed inside the SPI pattern (§10.29);","Version 35 — LIVING DRAFT: V34 + complete provenance graphs preserved at merge, the two-seat gate on V34 (§10.30); V34 = V33 + the two-seat gate on V33 closed inside the SPI pattern (§10.29);")
repx(r"The seat's tool is `r3c2_ledger_tools.py`,\s+sha256\s+`[0-9a-f]{64}`","The seat's tool is `r3c2_ledger_tools.py`, sha256 `"+SEAT+"`")
repx(r"the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document,\s+sha256\s+`[0-9a-f]{64}`","the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document, sha256 `"+LANE+"`")
repx(r"the lane owner runs `r3c2_lane_tools.py`\s+\(sha256\s+`[0-9a-f]{64}`;","the lane owner runs `r3c2_lane_tools.py` (sha256 `"+LANE+"`;")
rep("A claim with a disputed input or parent list carries both script-computed classifications and is marked `DISPUTED`.",
    "A claim with a disputed input or parent list is marked `DISPUTED`. In addition to its canonical per-input alternatives, `merge` preserves the two complete validated provenance graphs in `provenance_graphs`, ordered by the SHA256 of canonical JSON over their records sorted by `input_id`; equal graphs are retained once. `compute` obtains the claim's reported classification pair from those complete graphs, retaining equal classifications as a pair when the claim is disputed. It never treats an independently mixed PRIMARY or ALT graph as a graph supplied by a seat. The merged output, including these graphs, is serialised recursively with sorted object keys.")
rep("The comparison graph is constructed only from matched branches; the original disputes and the matched branches are reported without reconciliation.",
    "The comparison graph used to decide the audit is constructed only from complete matched input branches. A cycle or missing dependency in that matched graph fails the audit. Unmatched PRIMARY or ALT graphs are diagnostic views only: if their roots cannot be computed, the report records that fact without adding a mismatch or changing the audit verdict. The original disputes and the matched branches are reported without reconciliation.")
m=m.rstrip("\n")+f"""

## 10.30 V35 — complete provenance graphs preserved at merge: the two-seat gate on V34 ({T})

C0 on V34: codex PASS, kimi PASS. Gate on V34: codex `PREREG_UNSOUND` (one non-cosmetic finding F1, one cosmetic C1), kimi
`{{KIMI}}`; both PRIOR_FINDINGS_CLOSED=YES (the V33 findings closed), blind intact, C5 YES, no masked stage. Reconciled BY TOPIC
(`R3C2_V34_GATE_RECONCILIATION_20260907.md`, sweep none missing). Seat-permutation equality HELD on every construction codex built.

**codex F1 (non-cosmetic; a new class, not seat order):** the per-input canonical choice can COMPOSE a primary graph no seat supplied —
two acyclic seat graphs (A: x→y→r, B: y→x→r, measured root only, zero origin-label disagreements) merged to a primary view x↔y; `compute`
exited 1 instead of reporting the promised DISPUTED pair, and `audit compare`'s diagnostic root computation over that mixed view added
a mismatch even when the auditor's reconstruction equalled complete A or complete B. Repaired with codex's exact sentences (§3): `merge`
now also preserves the two COMPLETE validated seat graphs in `provenance_graphs` in seat-blind order (equal graphs once); `compute`
takes every claim's classification pair from those complete graphs and never from the mixed view — a ledger carrying alternative
branches but no graphs is REFUSED, a ledger without alternatives is itself one complete graph; the audit's unmatched-view root
computation is diagnostic only (recorded, never a mismatch), while a cycle or missing dependency in the MATCHED graph still fails.
Seat-blind ordering stays at `merge`; no downstream seat-order selection was added. Exhibition: codex's construction is built
deterministically (the fixture searches a small evidence tag until the canonical keys mix the seats, and prints the tag) and, with the
auditor equal to complete A and to complete B, must give audit PASS, `compute` exit 0 and a DISPUTED pair in both orders; `compute`'s
exit code and output now join every construction's compared outcome. Fail-first: against pinned byte copies of the V34 tools the
exhibition FAILS on the two cycle rows only, with audit [1,1] and compute [1,1] exactly as codex observed; PASSES on the delivered
tools. **codex C1 (cosmetic):** the exhibition docstring replaced by codex's exact text. Kit: {NC} controls, {NP} deletion probes,
PASS; pre-existing assertions in conflict: {{CONFLICTS}}. **Next:** C0 and the gate on V35.
"""
io.open(M,"w",encoding="utf-8").write(m); print("V35 master written (placeholders KIMI/CONFLICTS to fill)")

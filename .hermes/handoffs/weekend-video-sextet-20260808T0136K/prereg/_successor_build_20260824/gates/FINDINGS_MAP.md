# FINDINGS MAP — which referee finding each transition answers

Human-written. `tools/prereg_trace.py` reads this and **fails** when a transition changed a normative
section while citing nothing here. The tool computes the bytes; it refuses to decide which finding a
change answers, because that is a judgement.

Format: `V<from>→V<to>: <finding ids, comma separated>`

V15→V16: FOLD — §6 replaced from SECTION6_DRAFT_AGY_R15 (d2c388a4) on principal's instruction 21:48
V16→V17: GPT56-V16-1, GPT56-V16-2, GPT56-V16-3, GPT56-V16-4, CODEX-V16-1, CODEX-V16-2, CODEX-V16-3
V17→V18: GPT56-V17-1, GPT56-V17-2, GPT56-V17-3, CODEX-V17-1, CODEX-V17-2, CODEX-V17-3, CODEX-V17-4
V18→V19: GPT56-V18-1, CODEX-V18-1, CODEX-V18-2
V19→V20: GPT56-V19-1, CODEX-V19-1
V20→V21: GPT56-V20-1, GPT56-V20-2, GPT56-V20-3, CODEX-V20-1, CODEX-V20-2
V21→V22: GPT56-V21-1, GPT56-V21-2, GPT56-V21-3, CODEX-V21-1, CODEX-V21-2, CODEX-V21-3, CODEX-V21-4
V22→V23: CODEX-V22-1 (class-E count 8 not 7), CODEX-V22-2, CODEX-V22-3, CODEX-V22-4, GPT56-V22-1, GPT56-V22-2, GPT56-V22-3
V23→V24: CODEX-V23-1, CODEX-V23-2, CODEX-V23-3, GPT56-V23-1, GPT56-V23-2, GPT56-V23-3, plus BLANC-20260828 (compute the counts and the trace)
V24→V25: BS2A-ADOPTION-20260828 (quality-cut exclusion predicate; principal's instruction), GPT56-V24-1, GPT56-V24-2, CODEX-V24-4, CODEX-V24-5, CODEX-V24-6
V25→V26: GPT56-V25-1, GPT56-V25-2, CODEX-V25-1, CODEX-V25-2, CODEX-V25-3, CODEX-V25-4
V26→V27: GPT56-V26-1, GPT56-V26-2, GPT56-V26-3, CODEX-V26-1, CODEX-V26-2, CODEX-V26-4
V27→V28: GPT56-V27-1, GPT56-V27-2, GPT56-V27-3, CODEX-V27-1
V28→V29: CODEX-V28-1 (current-transition scope rule)
V29→V30: PRINCIPAL-20260828-LAND-NULL (human direction: "add the land 2008 null to the prereg motivation"; no referee finding — the change answers an instruction, and inventing a finding ID for it would be a lie)
V30→V31: GPT56-V30-1, GPT56-V30-2, GPT56-V30-3, CODEX-V30-1, CODEX-V30-2
V31→V32: GPT56-V31-1, CODEX-V31-1, plus PRINCIPAL-20260828-COUPLING (human direction: "the cut raised the coupling — flag it in §2.7"; measured figures, not a referee finding)
V32→V33: GPT56-V32-6, CODEX-V32-5 (§2.7 conditional-independence overreach). The five gain-control findings — GPT56-V32-1..5, CODEX-V32-1..4 — were repaired in gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md, which is a sidecar and not part of this document's bytes.
V33→V34: BS2A-R6-CLEAR-20260828 (the quality-predicate component cleared its code gate at round 6 from both seats and is pinned by digest in the BS-2a row, with its recorded robustness limit; the slot remains DESIGN, UNFILLED and no class count moves)
V34→V35: GPT56-V34-2, CODEX-V34-3 (the antisymmetry identity does not forbid a biased w creating a signal), CODEX-V34-1 (an unlogged archive read need not break the chain), CODEX-V34-4 (the BS-2a pin overstated the pairwise probe evidence)
V35→V36: GPT56-V35-1 (the repaired BS-2a row duplicated the 26-probe class, reading as 52), CODEX-V35-1 (the crash clause omitted the exit-status boundary; a post-verification emit failure prints MATCH then exits 1)
V36→V37: PRINCIPAL-20260829-VOID-OPTION-A and PRINCIPAL-20260829-BS6-OPTION-A (human decisions relayed by Blanc 09:20 KST, on GPT56-V34-1 and the three §7.1 coverage gaps GPT56 named in the VOID gate round). Closes the degenerate and digest gaps as separate antecedents, extends the §2.7 ID to cover a threshold *chosen* as well as *moved*, and adds class-P slot BS-3g blocking BS-6 — the first row-count change since V4 (15/8 → 16/8). **The §2.7 phase reconciliation was explicitly NOT authorised and remains open.**
V37→V38: PRINCIPAL-20260829-2.7-REFUSED-AS-PUT (the principal declined the §2.7 phase question as not his to answer — the clause was authored by this lane at V11, commit 4d99d1d93; the instant was recovered from that commit's own §2.7 preamble and the cell left unchanged) and PRINCIPAL-20260829-AUTH-DEPRIORITISED (record CODEX-V34-2 accurately in §5; do not build the typed authorisation record; do not touch frozen v9).
V38→V39: GPT56-V38-1 and CODEX-V38-1 (agreed: the DESIGN-slot inventory omitted BS-3g), CODEX-V38-3 (DECISIONS_FOR_DUHO.md cited as the record of a ruling it does not record), CODEX-V38-4 (§6.1/§6.2 mis-cited for the χ-ordering evidence, and commit metadata does not prove lane authorship). CODEX-V38-2 is NOT repaired here — it changes what voids a run and is referred to the principal.
V39→V40: PRINCIPAL-20260829-VOID5-OPTION-C (ruling on CODEX-V38-2: a pre-unblinding numerical failure does not void the run; qualify §5's numerical trigger to post-unblinding and route pre-unblinding permutation/statistic failures to INCONCLUSIVE-BY-COMPUTATION with a binding rerun procedure. Misconduct conditions deliberately unmoved at Any).

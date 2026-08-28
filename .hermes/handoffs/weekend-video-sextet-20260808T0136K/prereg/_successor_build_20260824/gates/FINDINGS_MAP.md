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

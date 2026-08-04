# LANA BRIEF — C41 Step 4: no-overclaim pass over the V2 ledger (80 entries)

Lane: `c41-baseline-restart-20260803T1253Z`. You are Lana. The chain: Goru built `C41_LEDGER.jsonl`
V2 (validation PASS); your pass is the semantic arbiter before Kun's Step-5 stance verification.
Ground truth: the V3 span table (`SPAN_TABLE.jsonl`), the contract + enum definitions
(`docs/claim_ledger_contract_v1_agn_20260703T0830Z/CLAIM_LEDGER_CONTRACT_V1.md`,
`artifacts/ledger_enums.json` — read the DEFINITIONS of each certainty_level, not just the names).

Per entry: does the assertion's modality exceed its bound spans? Is the certainty_level justified
UNDER ITS ENUM DEFINITION? Two coordinator-flagged suspicions requiring explicit verdicts:
1. **Zone recast**: Goru "formally cast" unknown-zone spans to `interpretation` to fit the enum.
   Verdict needed: is that metadata falsification (revert to a compliant honest value / propose a
   docs-only enum extension), or defensible? Do not let a convenient cast stand unexamined.
2. **Certainty inflation**: 65/80 `widely_supported`, 1 `actively_debated` — in the #1 contested
   cluster. Check whether `widely_supported` was granted per its definition (cross-source
   corroboration) or merely because single sources assert confidently. Entries failing the
   definition get your corrected certainty_level in the findings (report-and-propose; Goru applies
   in V3 — you do not edit the ledger).

Deliverables (lane dir): `LANA_STEP4_PASS.md` — verdict PASS / FAIL_WITH_CORRECTIONS + per-entry
findings table (entry id → issue → proposed correction), counts, and your ruling on the two flags.
End with marker: `LANA_STEP4_PASS_COMPLETE_20260804`. Lane-only writes; no ledger edits; no
network; do not read the f_esc or AGN lanes.

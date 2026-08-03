# Lana P1a brief — contract-r3 draft

P0 is OPEN: Lana/Goru/Tori ACKs exist and `receipts/KUN_INPUT_CUSTODY_RECEIPT.md` is GREEN.

Read `HWAO_PLAN.md` §§0–4, the sealed contract `../gemini-dr-revised-canary-20260712T045317Z/prompt/C1r.md`, and the repaired packet's Hwao/Lana T14 adjudication, final synthesis, residue report, validator spec/result, and design review.

Produce only `design/CONTRACT_R3_DRAFT.md` now. Do not start P2 classification.

Requirements:

1. Include a complete proposed r3 contract text suitable for later review, but do not overwrite or edit C1r.
2. Include decisions D1–D6 exactly as Hwao defines them.
3. For every D-item include all seven fields: current rule with sealed `C1r.md:<line-range>`, observed pressure, exact proposed wording, rationale, positive example, negative example, validator implication.
4. Make a concrete choice, not a menu, for D1–D5. D6 is a design matrix only: rule → check → fixture need → expected RED. No code.
5. Any gate relaxation must say `FAIL_CLOSED_IMPACT: YES` and explain the preserved guard/replacement. Otherwise say `FAIL_CLOSED_IMPACT: NO`.
6. Explicitly resolve:
   - calibration-target descriptions versus agreement/tension comparisons in S1;
   - the SIMBA ∼10% tuned-parameter case;
   - Section-2 Result-versus-Citation-cell authority;
   - exact ledger URL normalization, duplicate, near-duplicate, non-empty-name, and bidirectionality rules;
   - one GAP per paragraph/logical unit.
7. Keep source IDs quarantined and scientific/source-fidelity decisions manual.
8. End with `LANA_CONTRACT_R3_DRAFT_DONE_20260713T024458Z`.

Write boundary: `design/CONTRACT_R3_DRAFT.md` only. No network/source retrieval/browser/git/DB/dashboard/deploy/cron/account action. No validator implementation and no live canary.

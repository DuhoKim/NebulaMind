# KUN BRIEF — KUN-WAVE-B1-ENTAILMENT-STANCE-20260703

Role: Kun = Codex implementation/artifact-production lane, model `gpt-5.5`.
Captain/final verifier: Tori/Hermes.

## Context

The Quartet Step 7a tool policy says Step 8 prose remains locked until Wave B1 tests an entailment/stance checker against the existing human stance matrix.

Relevant files:
- Policy report: `/Users/duhokim/NebulaMind/NebulaMind/docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/reports/QUARTET_TOOL_ADOPTION_POLICY.md`
- Policy JSON: `/Users/duhokim/NebulaMind/NebulaMind/docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/artifacts/tool_adoption_policy.json`
- Gold set: `/Users/duhokim/NebulaMind/NebulaMind/docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/artifacts/gold_agn_26.json`
- Claim Ledger Contract v1 dir: `/Users/duhokim/NebulaMind/NebulaMind/docs/claim_ledger_contract_v1_agn_20260703T0830Z/`
- Stance matrix likely at: `/Users/duhokim/NebulaMind/NebulaMind/docs/claim_ledger_contract_v1_agn_20260703T0830Z/artifacts/claim_source_stance_matrix.jsonl`

## Scope

Allowed read roots:
- `/Users/duhokim/NebulaMind/NebulaMind/docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/`
- `/Users/duhokim/NebulaMind/NebulaMind/docs/claim_ledger_contract_v1_agn_20260703T0830Z/`
- repo-local files needed only to understand existing artifact conventions

Allowed writes only:
- `/Users/duhokim/NebulaMind/NebulaMind/docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/scripts/wave_b1_entailment_stance_benchmark.py`
- `/Users/duhokim/NebulaMind/NebulaMind/docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/artifacts/wave_b1_entailment_stance_results.json`
- `/Users/duhokim/NebulaMind/NebulaMind/docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/reports/KUN_WAVE_B1_ENTAILMENT_STANCE_REPORT.md`
- `/Users/duhokim/NebulaMind/NebulaMind/docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/validation/wave_b1_entailment_stance_validation.json`

Out of scope:
- no DB/SQL/migrations
- no deploy/restart
- no git commit/push/merge
- no product/wiki/public publish
- no Step 8 prose preview
- no secrets or token inspection/printing
- no package installs
- no network/model downloads unless you stop and ask the user first
- no mutation outside the allowed writes

## Task

1. Read the Step 7a policy and the Claim Ledger Contract stance artifacts.
2. Build a Wave B1 benchmark harness that loads the human stance rows, especially support/qualify/contradict/no-info cases.
3. First inspect local environment/package availability only. Do not install. If a local NLI/SciFact/MultiVerS-style model is already available, you may use it. If not, implement a clearly labeled deterministic baseline/heuristic probe and mark it as `NOT_A_VALIDATED_NLI_MODEL`.
4. Run the harness on the available stance rows.
5. Report metrics by stance class: counts, confusion matrix if applicable, support precision, qualifier/contradict recall, and known failure cases.
6. Decide whether B1 is actually satisfied. If only a heuristic baseline was possible, say B1 is not fully satisfied and list the exact next approval needed to test a real local/downloaded NLI model.
7. Write the allowed script, result JSON, validation JSON, and report.

## Verification requirements

- Report exact commands run and exit codes.
- Validation JSON must contain:
  - `status`: `PASS`, `PASS_WITH_CAVEAT`, or `BLOCKED`
  - `rows_loaded`
  - `model_or_method_used`
  - `network_used`: false unless explicitly approved
  - `packages_installed`: false
  - `step8_unlocked`: false
  - `done_marker`
- The report must include a Safety ledger with zero DB/SQL/deploy/git/product/prose/secrets.

## Done marker

Put this exact standalone line at the end of the report and mention it in your final terminal response:

KUN_WAVE_B1_ENTAILMENT_STANCE_DONE_20260703

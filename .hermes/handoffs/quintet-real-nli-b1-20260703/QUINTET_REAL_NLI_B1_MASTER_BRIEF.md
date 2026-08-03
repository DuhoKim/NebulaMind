# QUINTET REAL-NLI B1 MASTER BRIEF — 20260703

Marker: `QUINTET_REAL_NLI_B1_MASTER_BRIEF_20260703`

Context: The operator asked why the approved real-NLI B1 gate was not being handled by the Quintet. Tori agrees and is converting the gate to Quintet review before any Step 8 prose.

Quintet roles:
- Tori/Hermes: run, verify, consolidate, update cockpit.
- Kun/Codex: implementation/reproducibility review of script and artifacts.
- Goru/agy: mechanical row/count/schema/file verification.
- Lana/Claude: methods/gate review; decide what B1 does and does not authorize.
- Hwao/Fable: adversarial/doctrine review; prevent NLI/tool overclaiming and Step 8 leakage.

Common evidence packet:
- Comparison JSON: `/Users/duhokim/NebulaMind/NebulaMind/docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/artifacts/wave_b1_real_nli_model_comparison.json`
- Comparison report: `/Users/duhokim/NebulaMind/NebulaMind/docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/reports/QUINTET_REAL_NLI_B1_COMPARISON_PACKET.md`
- Script: `/Users/duhokim/NebulaMind/NebulaMind/docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/scripts/wave_b1_real_nli_benchmark.py`
- Gold stance matrix: `/Users/duhokim/NebulaMind/NebulaMind/docs/claim_ledger_contract_v1_agn_20260703T0830Z/artifacts/claim_source_stance_matrix.jsonl`
- Claim ledger: `/Users/duhokim/NebulaMind/NebulaMind/docs/claim_ledger_contract_v1_agn_20260703T0830Z/artifacts/claim_status_ledger.jsonl`

Current measured summary:
- MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli: accuracy 0.311, support_precision 0.7142857142857143, qualifier_recall 0.9, contradict_recall 0.0, auto_authority=False
- ynie/roberta-large-snli_mnli_fever_anli_R1_R2_R3-nli: accuracy 0.378, support_precision 0.875, qualifier_recall 1.0, contradict_recall 0.0, auto_authority=False
- typeform/distilbert-base-uncased-mnli: accuracy 0.222, support_precision 0.4, qualifier_recall 0.7, contradict_recall 0.3333333333333333, auto_authority=False

Non-negotiable safety:
- No DB writes, SQL mutations, migrations, deploy/restart, git commit/push/merge.
- No Step 8 prose drafting or preview.
- No treating NLI predictions as truth.
- Reports may be written only under `.hermes/handoffs/quintet-real-nli-b1-20260703/` or the existing Step 7a `reports/validation/artifacts` dirs.

Final gate question for the Quintet:
1. Was real-NLI B1 executed reproducibly on all 45 rows?
2. Is the script/mapping sane enough for a tool-evaluation artifact?
3. Do results justify only assistive triage, or stronger adoption?
4. Does this unlock Step 8 automatically? Expected safe answer: no, not automatically; operator approval still required.

QUINTET_REAL_NLI_B1_MASTER_BRIEF_20260703

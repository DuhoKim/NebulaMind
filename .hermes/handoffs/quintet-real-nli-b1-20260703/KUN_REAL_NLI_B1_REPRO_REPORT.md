# Kun Real-NLI B1 Implementation/Repro Review

Marker: `KUN_REAL_NLI_B1_REPRO_DONE_20260703`

Verdict: `PASS_WITH_PATCHES`

## Scope Performed

Reviewed:
- `docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/scripts/wave_b1_real_nli_benchmark.py`
- `docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/artifacts/wave_b1_real_nli_model_comparison.json`
- `docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/reports/QUINTET_REAL_NLI_B1_COMPARISON_PACKET.md`
- Model-specific result, report, and validation files for all three listed models.
- Gold stance matrix and claim ledger joins.

No benchmark script rerun was performed. No model download was performed.

## Findings

1. Artifact packet is internally consistent.

   The comparison JSON lists three models, and each listed model-specific validation/result/report path exists. The packet report exactly matches the JSON summary for model id, row count, accuracy, support precision, qualifier recall, contradiction recall, auto-authority flag, Step 8 flag, and artifact paths.

   Recomputed example-level counts from each model-specific result file match its validation metrics:

   | Model | Rows | Correct | Accuracy | Support precision | Qualifier recall | Contradict recall |
   |---|---:|---:|---:|---:|---:|---:|
   | `MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli` | 45 | 14 | 0.3111111111111111 | 0.7142857142857143 | 0.9 | 0.0 |
   | `ynie/roberta-large-snli_mnli_fever_anli_R1_R2_R3-nli` | 45 | 17 | 0.37777777777777777 | 0.875 | 1.0 | 0.0 |
   | `typeform/distilbert-base-uncased-mnli` | 45 | 10 | 0.2222222222222222 | 0.4 | 0.7 | 0.3333333333333333 |

2. Data joins are clean for the current artifact set.

   The stance matrix has 45 rows and joins to 16 ledger entries. There are no missing ledger entries, no missing evidence spans, no duplicate `(entry_id, span_id)` stance rows, and no empty joined assertion/quote pairs. Gold stance counts are:

   ```json
   {"contradicts": 3, "qualifies": 10, "supports": 32}
   ```

3. Label mapping is sane for the tested artifacts.

   The script uses model `id2label`, normalizes labels by substring to `entailment`, `neutral`, and `contradiction`, and maps NLI labels to stance labels as expected: entailment -> supports, contradiction -> contradicts, neutral/low-confidence -> qualifies. All stored examples contain the three expected probability labels, and rounded probabilities sum to approximately 1.0.

4. Generic artifacts are exact MoritzLaurer copies, not a three-model aggregate.

   `wave_b1_real_nli_results.json` and `wave_b1_real_nli_validation.json` are exact copies of the MoritzLaurer suffixed artifacts. This is internally consistent, but consumers must use `wave_b1_real_nli_model_comparison.json` or the suffixed files for the three-model comparison.

5. Script has preservation/repro hardening gaps before future reruns.

   The script writes only fixed generic paths:

   - `artifacts/wave_b1_real_nli_results.json`
   - `reports/REAL_NLI_B1_REPORT.md`
   - `validation/wave_b1_real_nli_validation.json`

   A rerun with `B1_NLI_MODEL` overwrites those generic files. The current suffixed artifacts appear preserved outside this script, so the packet is usable, but the script itself does not guarantee model-specific preservation.

   The script also calls `AutoTokenizer.from_pretrained(MODEL_ID)` and `AutoModelForSequenceClassification.from_pretrained(MODEL_ID)` without `local_files_only=True`. Under current "do not download more models" constraints, a future rerun should be explicitly offline/cache-only or should fail rather than downloading.

   `build_rows()` silently falls back to `{}` for missing ledger entries or spans. Current data passes the join checks, but the script should fail fast on missing joins to avoid benchmarking synthetic empty-text rows as neutral/qualifies.

## Recommended Patches Before Future Rerun

- Add a stable model key and write suffixed result/report/validation paths from the script itself.
- Add a comparison/manifest writer only after all intended model-specific files exist and validate.
- Add `local_files_only=True` or an explicit offline mode for this gate unless the operator separately approves additional downloads.
- Fail fast if any stance row lacks a ledger entry, evidence span, assertion, or quote.
- Record runtime provenance accurately instead of hardcoding `network_used: true` and `packages_installed: true`.

## Gate Read

Real-NLI B1 was executed reproducibly enough for the current tool-evaluation artifact packet: all three candidate model artifacts cover all 45 human stance rows, metrics recompute, and comparison files agree.

The results do not justify automatic stance authority. They support only assistive warning/triage use. Step 8 is not automatically unlocked.

KUN_REAL_NLI_B1_REPRO_DONE_20260703

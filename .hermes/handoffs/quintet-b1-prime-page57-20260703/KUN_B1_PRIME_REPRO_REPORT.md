# KUN B1-prime implementation/reproducibility report

Marker: `KUN_B1_PRIME_REPRO_DONE_20260703`

Verdict: `PASS_WITH_PATCHES`

Scope followed:
- Reviewed the saved KUN brief and master brief.
- Inspected the gold draft JSONL, summary, verifier script, verifier results, verifier validation, verifier report, source matrix, source rows, and source snippets.
- Ran read-only JSON/count/metric/source-trace checks only.
- Did not run generic NLI.
- Did not download models.
- Did not rerun the local Ollama verifier.
- Did not run DB, deploy, git write, or Step 8 prose work.

## Bottom line

The packet is usable as a contradiction-rich held-out gold draft and verifier smoke/evaluation artifact, but it should not be promoted as reviewed gold or as a Step 8 safety net without patches. JSON validity, row counts, label counts, metric recomputation, source-row traceability, and safety ledger fields are internally consistent. The main problems are:

1. artifact overwrite risk in the verifier script;
2. several draft labels/rationales depend on source context beyond the exact evidence snippet given to the verifier;
3. no durable run manifest/checksum/provenance capture for the exact Ollama model/runtime;
4. the current verifier score is too weak for any adoption authority.

## Checks performed

Gold draft:
- JSONL rows: 15.
- Unique `b1_prime_id`: yes.
- Unique `(claim_id, evidence_id)`: yes.
- Label counts recomputed: `{'refutes': 5, 'supports': 5, 'qualifies': 3, 'noinfo': 2}`.
- Every row has `gold_label_status = TORI_DRAFT_PENDING_QUINTET_REVIEW`.
- Page scope: all checked rows carry `page_id = 57`, `page_slug = galaxy-evolution`, and source set `galaxy_page57_stance_audit_20260702T124152Z`.

Source trace:
- Source matrix says rows extracted: 15; snippets mined: 103; source text ok: 15/15.
- Draft evidence IDs all exist in `page57_stance_audit_rows.jsonl`.
- Draft evidence IDs all exist in `page57_stance_audit_snippets.jsonl`.
- Key source-row metadata matches for checked fields: `claim_id`, `claim_text`, `arxiv_id`, votes, `preliminary_nonbinding_classification`, `audit_class`, title, page ID, and page slug.
- The draft `evidence_snippet` values are not identical to the separate snippet-file top entry for all 15 rows, but they do trace to source-row text fields and/or source-matrix top snippets. This is acceptable if documented as "source text / source-matrix snippet", not as a byte-for-byte copy of the snippet JSONL row.

Verifier results:
- Rows: 15.
- Correct: 8.
- Accuracy recomputed: `0.5333333333333333`.
- Majority baseline recomputed: `refutes`, 5/15 = `0.3333333333333333`.
- Prediction counts recomputed: `{'refutes': 3, 'qualifies': 3, 'noinfo': 6, 'supports': 3}`.
- Refutes recall recomputed: 3/5 = `0.6`.
- Supports recall recomputed: 2/5 = `0.4`.
- Confusion matrix in validation/results matches recomputation.

Validation/safety:
- `status = PASS_WITH_PATCHES`.
- `auto_stance_authority_threshold_met = false`.
- `b1_prime_as_step8_safety_net_satisfied = false`.
- `step8_unlocked = false`.
- Summary and results safety ledgers have all reviewed counters at 0.
- Validation has `generic_nli_runs = 0` and `new_model_downloads = 0`.
- These safety-ledger claims are truthful with respect to this review session; I did not execute any prohibited run.

## Findings

### 1. Artifact overwrite risk in verifier script

Severity: medium.

The verifier writes fixed paths unconditionally:
- `artifacts/b1_prime_scope_attribution_verifier_results.json`
- `validation/b1_prime_scope_attribution_verifier_validation.json`
- `reports/B1_PRIME_SCOPE_ATTRIBUTION_VERIFIER_REPORT.md`

The writes happen with `write_text(...)` and no existence check, run ID, temporary file, lock, or archive. Any rerun replaces the prior verifier output while keeping the same path and done marker. This is an avoidable reproducibility risk, especially because the model call is stochastic enough in practice to warrant preserving each run even at temperature 0.

Patch recommended:
- Write to a timestamped run subdirectory or timestamped result filenames.
- Preserve/update a stable `latest` pointer only after successful completion.
- Include a manifest with script hash, gold JSONL hash, Ollama model name, and Ollama model digest if available.

### 2. Exact evidence passed to verifier is sometimes narrower than draft rationale

Severity: medium.

Several gold draft rationales cite information that is present in lower-ranked source-matrix snippets or broader source text, but not in the exact `evidence_snippet` stored in the gold JSONL and sent to the verifier. This creates apparent "model miss" cases where the verifier may be correctly judging the supplied snippet rather than the broader source context.

Rows needing label/evidence patch review:
- `B1P57-26687`: draft label `refutes`; exact snippet partly supports significant radiation pressure in massive/dense clouds. The refuting sentence about reprocessed IR radiation being unlikely unless conditions are enhanced is in another source-matrix snippet and should be included if `refutes` remains.
- `B1P57-29777`: draft label `refutes`; exact snippet mainly says isolated dwarf spheroidal simulation. The stronger "may not necessarily need clusters/groups" sentence is in another source-matrix snippet and should be included if `refutes` remains.
- `B1P57-25806`: draft label `supports`; exact snippet says Lumina follows galaxies and AGN through HeII reionization to z=3, but the stronger "HeII reionization is driven by AGN and nearly complete by z=3" sentence is not in the stored snippet.
- `B1P57-25834`: draft label `supports`; exact snippet supports environmental-origin testing but does not mention gas starvation, ram pressure, or gas depletion. Patch evidence or weaken label.
- `B1P57-28967`: draft label `supports`; exact snippet says the mechanism is debated and a popular possibility. The stronger jet-energy support is in another snippet. Patch evidence or set to `qualifies`.
- `B1P57-25835`: draft label `qualifies`; exact snippet defines green valley/transition region but does not establish underpopulation at fixed stellar mass. `noinfo` is defensible unless broader source context is added.
- `B1P57-26691`: draft label `qualifies`; exact snippet only establishes that morphology-host-halo relation is investigated. The "weakly with host halo / more strongly with internal properties" sentence is in another snippet and should be included if `qualifies` remains.

Patch recommended:
- For each row, make `evidence_snippet` contain the exact sentence(s) that justify the draft label, or change the draft label to match the exact snippet.
- Add a field such as `evidence_source_field` or `source_matrix_snippet_rank` to distinguish source-row text, matrix top snippets, and snippet JSONL lines.

### 3. Metric implementation is correct but lacks empty-input guard

Severity: low.

Metric recomputation matches the reported results. However, `compute_metrics()` calls `max(Counter(...).items())` even when `rows` is empty. That would fail before returning the otherwise guarded `None` metrics. This is not affecting the current 15-row run, but it is a small implementation defect.

Patch recommended:
- Return an explicit empty metrics object or raise a clear validation error when no rows are loaded.

### 4. Unused imports and unused argument

Severity: low.

The verifier imports `defaultdict`, `sys`, and `urllib.error` without using them, and `call_ollama(..., row_id)` does not use `row_id`. This is not behaviorally harmful, but it weakens script cleanliness.

Patch recommended:
- Remove unused imports and either remove `row_id` or include it in error context.

### 5. Model provenance is incomplete

Severity: low to medium.

The artifacts record `model = qwen3.6:35b-a3b-nvfp4` and method ID, but not the local Ollama model digest, Ollama version, script hash, gold-input hash, or prompt hash. For a held-out safety-net benchmark, the existing metadata is not enough to reproduce or audit an exact run later.

Patch recommended:
- Add hashes for the gold JSONL and verifier script.
- Capture Ollama model digest/version if available without downloading anything.
- Capture environment variables that affect behavior: `B1_PRIME_VERIFIER_MODEL`, `OLLAMA_URL`.

## Label/path mismatch assessment

No hard path mismatch found:
- Gold path in results points to the expected draft JSONL under the run directory.
- Results and validation both use marker `B1_PRIME_SCOPE_ATTRIBUTION_VERIFIER_DONE_20260703`.
- Validation status and report status agree.
- Source rows and source snippets are from the Page57 Galaxy Evolution stance-audit artifact set.

Soft mismatch:
- The report says "Source: Page57 stance-audit source matrix and snippets", while the draft JSONL evidence is sometimes from source-row text fields and sometimes from top source-matrix snippets. This should be stated more precisely in future reports.

## Safety/adoption assessment

The local scope/attribution verifier is a better direction than generic NLI for this project because its prompt encodes scientific claim verification, scope narrowing, attribution, alternative mechanisms, and keyword-collision handling. It should remain classified as a local scope/attribution verifier, not generic NLI.

It does not clear a safety-net threshold:
- Accuracy is 8/15 = 0.533.
- Refutes recall is 0.6.
- Supports recall is 0.4.
- Seven misses remain, many tied to exact-evidence scope.
- Validation correctly keeps `auto_stance_authority_threshold_met = false`, `b1_prime_as_step8_safety_net_satisfied = false`, and `step8_unlocked = false`.

Safe adoption language:
- "Use this packet as a Quintet-review draft and verifier smoke/evaluation artifact only."
- "Do not treat draft labels as final gold."
- "Do not use the current verifier result as Step 8 adoption authority."

## Required patches before promotion

1. Patch the seven evidence/label rows listed above so each label is justified by the exact stored `evidence_snippet`.
2. Change verifier output writing to preserve prior runs rather than overwrite fixed artifacts.
3. Add run provenance: input hash, script hash, prompt hash, model digest/version when locally available.
4. Add an empty-input guard in `compute_metrics()`.
5. Clarify evidence provenance in the draft summary/report.

KUN_B1_PRIME_REPRO_DONE_20260703

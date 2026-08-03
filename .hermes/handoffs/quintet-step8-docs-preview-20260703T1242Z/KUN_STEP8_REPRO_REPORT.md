# KUN Step 8 Reproducibility Report

Marker: `KUN_STEP8_DOCS_PREVIEW_REPRO_DONE_20260703T1242Z`

Scope: docs-only reproducibility review for the Step 8 Galaxy Evolution / AGN-feedback prose preview. No generic NLI was run. No models were downloaded. No DB, product, or git operations were performed.

## Recomputed Counts

Independent recomputation from `step8_sentence_bindings.jsonl`, `GALAXY_EVOLUTION_STEP8_PROSE_PREVIEW_DRAFT.md`, and `step8_b1_prime_attention_audit.json`:

| Check | Recomputed value | Saved validation value | Result |
|---|---:|---:|---|
| Sentence count | 16 | 16 | MATCH |
| Paragraph count | 6 | 6 | MATCH |
| Bound-sentence count | 16 | 16 | MATCH |
| Orphan count | 0 | 0 | MATCH |
| Modality overflow count | 0 | 0 | MATCH |
| Forbidden wording error count | 0 | 0 | MATCH |
| B1-prime attention flag count | 11 | 11 | MATCH |

No recomputed validation errors were found.

## Validator Script Inspection

Inspected `scripts/validate_step8_prose_preview.py`.

- Uses local deterministic file checks only: `pathlib`, `json`, and `re`.
- Reads the draft markdown, sentence bindings JSONL, and B1-prime attention audit JSON under the Step 8 run directory.
- Checks sentence ID presence, exact sentence text presence, binding/citation non-orphan status, modality tier rank, hard forbidden phrases, universal/dominance/reservoir guards, and B1-prime attention flag count.
- Does not import network, database, model, NLI, product, or git libraries.
- Does write the validation JSON when executed, so I did not invoke it; I recomputed the requested counts separately without modifying validation output.

Determinism finding: PASS.

## Hard Stops

Verified hard-stop statements in the draft, approval intake, source inventory, and validation safety ledger.

- Draft boundary says offline docs-only preview, not product copy, not exact diff, and no DB/SQL/migration/deploy/restart/product/git write.
- Approval intake hard stops are zero for DB writes, SQL mutations, migrations, deploy/restart, product publish, git commit/push/merge, exact-diff apply, and secrets.
- Source inventory hard stops are zero for DB writes, SQL mutations, migrations, deploy/restart, product publish, git commit/push/merge, and exact-diff apply.
- Validation safety ledger is zero for DB writes, SQL mutations, migrations, deploy/restart, product publish, git commit/push/merge, exact-diff apply, generic NLI runs, new model downloads, and secrets.
- `product_gate_locked` is true in validation; approval intake product gate is `locked`.

Hard-stop verification: PASS.

## B1-prime Use

The B1-prime audit declares `authority: attention_additive_only`, `auto_stance_assignments: 0`, and `gate_authority: false`. The 11 flags are review-attention flags only and do not assign stance or clear gates.

B1-prime scope verification: PASS.

## Prose Scope Check

The draft explicitly says it covers the currently verified AGN feedback / quenching slice for the Galaxy Evolution page and is not the final full Galaxy Evolution wiki page. The prose keeps prevalence, reservoir response, maintenance/heating, simulation, and dominance claims guarded by sample, tracer, model, and competing-channel qualifiers.

Scope verification: PASS.

## Final Stance

PASS

The Step 8 docs-only prose preview is reproducible against the saved validation facts and can be marked Step 8 docs-only PASS for this lane.

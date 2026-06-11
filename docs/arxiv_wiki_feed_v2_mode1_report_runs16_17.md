# arXiv Wiki Feed v2 Mode 1 Report: Runs 16-17

**Date:** 2026-06-11  
**Mode:** Mode 1, auto-validate/manual-promote  
**Scope:** Resolve the runs 16-17 backlog through the coverage stage and produce a validator report.  
**Promotion:** Not attempted.

## DB Run Check

| db_run_id | run_key | status | retrieval_filter_element_rows | arxiv_wiki_evidence_candidates | atom_coverage_rows |
|---:|---|---|---:|---:|---:|
| 16 | `arxiv_wiki_feed_v2_run_20260602T041255Z` | `candidates_built` | 0 | 1847 | 0 |
| 17 | `arxiv_wiki_feed_v2_run_20260602T042742Z` | `candidates_built` | 0 | 1847 | 0 |

Runs 16 and 17 are present in `arxiv_wiki_feed_runs`, but they did not create element-level
`retrieval_filter_element_rows` or atom coverage rows. They are claim-level candidate runs only.
Because the new coverage materializer consumes element-level rows, the replay used the held-back
BRK-trim element artifact lineage rather than mutating either DB run.

`db_run_id=3` was not read for writes and was not mutated.

## Artifact Lineage

| Stage | Artifact |
|---|---|
| BRK trim source | `/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/retrieval_filter_v2_brk_trim_20260527T065637Z/trimmed_routed_rows.jsonl` |
| Raw coverage materialization | `/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/coverage_materialization_runs16_17_backlog_20260611T070722Z` |
| Hydrated backlog rows | `/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/runs16_17_backlog_hydrated_20260611T070820Z` |
| Hydrated coverage materialization | `/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/coverage_materialization_runs16_17_backlog_hydrated_20260611T070829Z` |
| Atom backfill | `/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/candidate_grounded_atom_backfill_runs16_17_full_20260611T071028Z` |
| Mode 1 validator | `/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/mode1_validator_runs16_17_20260611T072048Z` |

## Coverage Materialization Counts

Initial materialization against the decision-only BRK-trim artifact produced terminal rows because
the artifact lacked claim, element, paper abstract, and `required` hydration fields.

| Input | rows | coverage_ready | coverage_pending | blocked_retryable | blocked_terminal |
|---|---:|---:|---:|---:|---:|
| raw BRK-trim rows | 863 | 0 | 0 | 0 | 863 |
| hydrated BRK-trim rows | 564 | 0 | 496 | 0 | 68 |

Hydration recovered 564 of 863 rows from prior full-text routing artifacts. The remaining 299 rows
remain backlog because no matching hydrated full-text row was found in the available artifact lineage.

## Atom Backfill

The candidate-grounded atom backfill ran artifact-only with Pico
`vanta-research/atom-astronomy-7b:latest`. No DB writes and no promoter calls were made.

| status | rows |
|---|---:|
| ready | 21 |
| missing | 262 |
| error_retryable | 4 |

Pre-model exclusions:

| reason | rows |
|---|---:|
| off_domain | 115 |
| semantic_unsupported | 162 |

Per-section atom readiness:

| section | rows | ready | missing | retryable | ready_rate |
|---|---:|---:|---:|---:|---:|
| env_quenching | 54 | 9 | 45 | 0 | 0.1667 |
| feedback_outflows | 106 | 7 | 97 | 2 | 0.0660 |
| high_z_sf | 127 | 5 | 120 | 2 | 0.0394 |

Coverage-gate summary from the atom backfill:

- Terminal-or-ready coverage: `0.9861`
- Retryable error rate: `0.0139`
- Non-off-domain ready rate: `0.0732`
- The `>=80%` non-off-domain ready gate did not pass, so this is not a promotion batch.

## Mode 1 Validator Result

Validator input was restricted to the 21 `coverage_ready` rows from the atom backfill manifest.
The validator ran in targeted coverage mode, artifact-only, with no DB reads for hydration.

| metric | count |
|---|---:|
| coverage_ready input rows | 21 |
| candidate element pairs | 21 |
| Atom votes | 21 |
| AstroSage votes | 18 |
| claim-candidate aggregate rows | 21 |
| validated_ready rows | 21 |
| distinct validated claims | 14 |

Model label distribution:

| model | supported | partial | missing | needs_human | contradicted |
|---|---:|---:|---:|---:|---:|
| Atom | 5 | 13 | 0 | 2 | 1 |
| AstroSage | 8 | 5 | 5 | 0 | 0 |

The validator artifact is:

`/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2/mode1_validator_runs16_17_20260611T072048Z/phase2_validator_report.md`

## Promotion Gate Status

Promotion was not attempted.

The Mode 1 validated set has 21 rows and 14 distinct claims, below the first-batch gate of
at least 30 deduped claim-paper rows and at least 15 distinct claims. The non-off-domain ready
rate also remains far below the 80% coverage bar. The correct next action is to expand coverage
before any manual promotion review.

## Conclusion

Step 2 is complete as an artifact-first Mode 1 replay:

- Runs 16 and 17 were identified in the DB.
- Their direct DB state was confirmed to be claim-candidate only, with no element coverage rows.
- The held-back element backlog was reprocessed through the new coverage stage using artifact lineage.
- A Mode 1 validator report was produced from coverage-ready rows.
- No Evidence promotion was performed.

# KUN Step 9E Reproducibility Report

Packet: `baseline_step9e_claim_id_guarded_sql_packet_20260703T1532Z`
Role: Kun/Codex reproducibility reviewer

Verdict: PASS

## Scope Control

- Did not execute SQL.
- Did not perform DB writes.
- Did not mutate SQL artifacts.
- Did not perform API mutations, migrations, deploys/restarts, product publish, git commit, git push, or git merge.
- Review used local artifacts and static checks only.

## Static Validator

Command run:

```bash
python3 docs/baseline_step9e_claim_id_guarded_sql_packet_20260703T1532Z/scripts/validate_step9e_guarded_sql_packet.py
```

Result:

- `status`: `PASS`
- `errors`: `[]`
- `hard_stops_zero`: `true`
- `apply_sql_sha256`: `dce5bf411ffb7923de9d3184d8d14248e6499c1b7de786bb12dacb0b1955e746`
- `rollback_sql_sha256`: `aecde9715b084fea52b60f0da4aebb1c2e933c64d22376e13d547d9d028a6c30`

Validator counts:

- `claim_resolution_rows`: 12
- `new_claims`: 5
- `evidence_rows`: 35
- `page_citation_links`: 35
- `rich_ledger_rows`: 31
- `rich_span_rows`: 31

## Independent JSONL Counts

Independent `wc -l` counts:

- `proposed/step9e_claim_id_resolution_decisions.jsonl`: 12
- `proposed/step9e_new_claim_rows_5.jsonl`: 5
- `proposed/step9e_evidence_insert_rows_35.jsonl`: 35
- `proposed/step9e_page_citation_link_insert_rows_35.jsonl`: 35

These match `summary.json` planned counts and `validation/step9e_packet_validation.json` validator counts.

## SQL Artifact Guard Check

Both SQL files exist:

- `sql/apply_guarded_step9e_claim_evidence_citation_packet.sql`
- `sql/rollback_step9e_claim_evidence_citation_packet.sql`

Apply SQL static guard indicators:

- Contains `NOT been executed` marker.
- Contains guarded transaction structure.
- Contains 9 `RAISE EXCEPTION` checks.
- Contains 6 `DRIFT_GUARD` references.
- Contains 3 `POST_GUARD` references.

Rollback SQL static guard indicators:

- Contains `NOT_EXECUTED` marker.
- Contains guarded transaction structure.
- Contains 4 `RAISE EXCEPTION` checks.
- Contains 3 `ROLLBACK_GUARD` references.
- Contains 1 `ROLLBACK_POST_GUARD` reference.

No SQL was executed.

## Execution-Result Artifact Check

Reviewed packet metadata and local artifacts for write/execution claims.

Observed not-executed/read-only indicators:

- `summary.json`: `status = AWAITING_EXPLICIT_EXECUTION_APPROVAL_NOT_EXECUTED`
- `summary.json`: `db_write_performed = false`
- `summary.json`: `sql_mutation_performed = false`
- `summary.json`: `api_mutation_performed = false`
- `summary.json`: `migration_performed = false`
- `summary.json`: `deploy_or_restart_performed = false`
- `summary.json`: `product_publish_performed = false`
- `summary.json`: `git_commit_push_merge_performed = false`
- `diff/step9e_exact_diff.json`: `status = AWAITING_EXPLICIT_EXECUTION_APPROVAL_NOT_EXECUTED`
- `diff/step9e_exact_diff.json`: `db_write_performed = false`
- `diff/step9e_exact_diff.json`: `sql_mutation_performed = false`
- `current_snapshots/step9e_readonly_db_schema_snapshot_summary.json`: `db_write_performed = false`
- `current_snapshots/step9e_readonly_db_schema_snapshot_summary.json`: `sql_mutation_performed = false`
- `APPROVAL_PACKET.md`: states DB writes executed 0, SQL mutations executed 0, API mutations 0, and requires a future explicit execution phrase.

No execution-result artifact was found that claims a DB write happened.

## Patch Requests

None.

KUN_STEP9E_REPRO_DONE

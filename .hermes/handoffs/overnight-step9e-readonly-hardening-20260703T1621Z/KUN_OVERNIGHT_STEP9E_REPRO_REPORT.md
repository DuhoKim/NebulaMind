# Kun overnight Step 9E reproducibility report

Input packet: `baseline_step9e_claim_id_guarded_sql_packet_20260703T1532Z`

Review scope followed: read-only local artifact review plus static validator attempts. No SQL apply, SQL rollback, API mutation, migration, deploy/restart, product/wiki publish, git commit, push, or merge was performed.

## Verdict

BLOCKED

Full reproducibility is blocked because the requested schema/SQL contract audit command attempted to connect to localhost Postgres and failed under the current sandbox/network policy before completing. The saved audit artifact is PASS, and the independent file-level checks below pass, but I cannot honestly mark the rerun itself as reproduced.

## Validator reruns

1. Packet validator command:

`python3 docs/baseline_step9e_claim_id_guarded_sql_packet_20260703T1532Z/scripts/validate_step9e_guarded_sql_packet.py`

Result: PASS.

Observed output summary:

- `status`: `PASS`
- `hard_stops_zero`: `true`
- `errors`: `[]`
- counts: 5 new claims, 35 evidence rows, 35 page citation links, 12 claim resolution rows, 31 rich ledger rows, 31 rich span rows
- apply SQL sha256: `bf6e60b21ad3b07f55aaacd867dc2278a4064def7e63570366d32e4487caf6d1`
- rollback SQL sha256: `11624d35242074545ad66b0ed5c0f300a9f43653dea3ff2bf43624556d191a9e`

2. Schema/SQL contract audit command:

`PYTHONPATH=/Users/duhokim/NebulaMind/NebulaMind/backend /Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python docs/overnight_step9e_readonly_hardening_20260703T1621Z/scripts/overnight_step9e_schema_sql_contract_audit.py`

Result: blocked by environment.

Failure: `psycopg2.OperationalError`, connection to `localhost:5432` failed with `Operation not permitted`. No DB write or SQL mutation was attempted by me.

Saved artifact check:

- `docs/overnight_step9e_readonly_hardening_20260703T1621Z/artifacts/overnight_step9e_schema_sql_contract_audit.json` has `status: PASS`
- `db_write_performed: false`
- `sql_mutation_performed: false`
- `transaction_read_only: on`
- `validator_status: PASS`
- `static_sql_checks.rollback_has_all_zero_or_all_full_state_guard: true`
- `static_sql_checks.rollback_claim_scope_includes_order_idx_732_736: true`

## Independent hardening checks

### Claim stance length and long basis

Checked `proposed/step9e_new_claim_rows_5.jsonl`.

- 5 claim rows present.
- `debate_stance` lengths are 13, 15, 13, 13, and 13 characters.
- All are <=20 characters.
- Every row preserves `debate_stance_basis_long`.
- Long basis lengths are 43, 36, 13, 13, and 49 characters.

### Citation link match method length

Checked `proposed/step9e_page_citation_link_insert_rows_35.jsonl`.

- 35 page citation link rows present.
- All `match_method` values are exactly `step9e_source_registry_key`.
- Max `match_method` length is 26 characters, within the <=32 character limit.

### Rollback guard text

Checked `sql/rollback_step9e_claim_evidence_citation_packet.sql`.

- Header states `ROLLBACK_ARTIFACT_ONLY_NOT_EXECUTED`.
- Guard permits only all-zero state `(0 evidence, 0 links, 0 claims)` or all-full state `(35 evidence, 35 links, 5 claims)`.
- Packet link count is scoped to `pcl.page_id=57`.
- Packet claim count is scoped to `page_id=57`, `order_idx BETWEEN 732 AND 736`, and exact text array.
- Claim delete is scoped to `page_id=57`, `order_idx BETWEEN 732 AND 736`, and exact text array.
- Post-rollback remaining-row check uses the same claim scope.

### Runbook execution gates

Checked the four Step 9E runbooks.

- Pre-execution checklist names the exact execution phrase: `APPROVE EXECUTE baseline_step9e_claim_id_guarded_sql_packet_20260703T1532Z`.
- Execution runbook says it is non-executing documentation and must not run unless the latest user message is exactly that execution phrase.
- Rollback runbook names the exact rollback phrase: `APPROVE ROLLBACK baseline_step9e_claim_id_guarded_sql_packet_20260703T1532Z`.
- Rollback runbook says not to run rollback now and notes current packet rows in DB are zero.
- Post-execution verification forbids wiki publish and silent broadening into worker/vote/jury containment.

## No execution evidence

Checked summary and validation artifacts:

- `summary.json`: `status` is `AWAITING_EXPLICIT_EXECUTION_APPROVAL_NOT_EXECUTED`.
- `summary.json`: `db_write_performed`, `api_mutation_performed`, `migration_performed`, `deploy_or_restart_performed`, and `git_commit_push_merge_performed` are all `false`.
- `validation/step9e_packet_validation.json`: `status` is `PASS`, `hard_stops_zero` is `true`.
- `validation/overnight_step9e_runbooks_validation.json`: `apply_executed: false`, `rollback_executed: false`, `db_write_performed: false`, `sql_mutation_performed: false`, `status: PASS`.
- Saved schema/SQL contract audit artifact: `db_write_performed: false`, `sql_mutation_performed: false`, `status: PASS`.

KUN_OVERNIGHT_STEP9E_REPRO_DONE

# Kun / Codex Step 9C Reproducibility Review

Verdict: PASS

Marker: KUN_STEP9C_REPRO_REPORT_DONE

## Scope Observed

Reviewed only the Step 9C read-only DB evidence match packet at:

`docs/baseline_step9c_readonly_db_evidence_match_20260703T1354Z`

No DB writes, SQL mutations, API mutations, migrations, deploy/restart, product publish, git commit/push/merge, apply, rollback, or executable mutation scripts were run.

I did not run `scripts/validate_step9c_packet.py` because inspection showed it rewrites `validation/step9c_packet_validation.json`, while this handoff allows writing exactly this report path. Instead, I reproduced the packet checks with read-only artifact inspection.

## Evidence Checked

- `APPROVAL_PACKET.md`
- `summary.json`
- `manifest.json`
- `validation/step9c_packet_validation.json`
- `db_readonly/db_evidence_match_summary.json`
- `artifacts/step9c_db_evidence_match.jsonl`
- `artifacts/step9c_insert_candidate_decision.jsonl`
- `artifacts/step9c_existing_evidence_decision.jsonl`
- `artifacts/step9c_claim_evidence_continuity_update.jsonl`
- `artifacts/evidence_2015_peng_db_duplicate_summary.json`
- `artifacts/ads_identifier_enrichment.json`
- `go_no_go_checklist.jsonl`
- `safety_ledger.json`
- `scripts/validate_step9c_packet.py`

## Reproducibility Findings

- Packet status is `PASS_PACKET_ONLY_NOT_EXECUTED`.
- Saved validation status is `PASS` with no errors.
- DB summary status is `PASS`.
- `transaction_read_only` is recorded as `on`.
- Read-only transaction rollback is recorded as `true`.
- Evidence rows scanned: `11817`.
- Step 9 source count: `26`.
- Match JSONL row count: `26`.
- Existing decision count: `1`.
- Existing matched source: source `14` / `2015Natur.521..192P`.
- Accepted existing product evidence IDs are exactly `6640` through `6655`.
- Evidence ID `6651` is isolated as the Galaxy Evolution page-citation-linked row.
- Evidence ID `6651` remains `PREFERRED_FROM_PUBLIC_PAGE_CITATION_LINK_BUT_NOT_EXECUTION_APPROVED`.
- Insert-candidate count: `25`.
- Insert-candidate sources are exactly `1-13` and `15-26`.
- Insert-heavy status remains `CONFIRMED_INSERT_HEAVY_25_OF_26_SOURCES_AFTER_DB_READONLY_MATCH`.
- ADS enrichment status is `FAIL`; recorded error is HTTP 401; `token_printed` is `false`.
- Local full-text source identifiers are recorded as coming from `claim_ledger_contract_v1_agn_20260703T0830Z/artifacts/source_fulltext_scope_checks_26.jsonl`.
- Continuity update row count is `6`.
- Step 9B gates remain locked by `NO_GO` checklist entries for canonical evidence-row selection, insert-heavy execution, claim workflow approval, rollback backup, and apply permission.

## Safety Findings

- `safety_ledger.json` records zero for `db_writes`, `sql_mutations`, `api_mutations`, `migrations`, `deploy_restart`, `product_publish`, `exact_diff_apply`, and `git_commit_push_merge`.
- `manifest.json` records `execution_authorized: false`.
- Search for apply/rollback/migration/SQL-named files inside the packet found no executable apply SQL/script artifacts.
- Text search found only hard-stop language, checklist NO-GO statements, packet narrative, and the read-only validation script; no authorized mutation path was found.

## Conclusion

The packet is reproducible from artifacts and internally consistent with the requested facts. It remains a read-only packet only. No executable apply SQL/script was created or authorized. Step 9B claim gates remain locked, and Step 9C does not authorize execution.

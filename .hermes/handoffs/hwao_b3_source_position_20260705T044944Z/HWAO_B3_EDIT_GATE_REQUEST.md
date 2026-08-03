# Hwao B3 edit-gate request

Marker requested: `HWAO_B3_EDIT_GATE_20260705T044944Z`
From: Tori relay
To: Hwao/Fable coordinator

## User directive

User approved B3 under the same no-SQL, no-product-mutation lane order.

## Current state

- B3-running cockpit checkpoint is published and public-verified:
  `GALAXY_2929_B3_RUNNING_HWAO_20260705T044944Z`
- Phrase state: `NO ACTIVE EXECUTION PHRASE`
- Cron `fd0987371f65` remains paused through B3 receipts.
- B3 pre-edit snapshot exists:
  `.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/pre_edit_queue_snapshot_b3_20260705T044944Z/`

## Lane outputs now available

Lana proposal:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/LANA_B3_PROPOSAL.md`
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/lana_b3_proposal.jsonl`

Kun checker/config:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/kun_queue_checker.py`
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/kun_b3_checker_config.json`
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/KUN_B3_CHECKER_USAGE.md`

Goru validation:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/GORU_B3_VALIDATION.md`

## Lana proposed decisions

- 28123: `relink -> 2946`, support, `accepted_limited`, `abstract_only_verified`; model-dependence side of 2946
- 28127: `leave_archival`, background/redundant same-paper, `rejected`, `abstract_only_verified`
- 28139: `leave_archival`, background/redundant same-paper, `rejected`, `abstract_only_verified`
- 28143: `leave_archival`, background/scope-mismatch with 2943, `rejected`, `abstract_only_verified`
- 28151: `relink -> 2942`, support, `accepted_limited`, `abstract_only_verified`; regime-scope thesis
- 28158: `relink -> 2946`, support, `accepted_limited`, `abstract_only_verified`; `gap_card_relevant: observational_maintenance_heating`

Same-paper stacking: no claim gets more than two kept spans; 2946 gets two role-distinct spans (model-dependence 28123 + observational/gap-card 28158), 2942 gets one, three redundant/scope-mismatch spans archival.

Goru verdict: PASS. Goru validated row IDs, zero dependencies, decisions/roles, accepted_limited/rejected statuses, R1 stacking, R2 gap-card handling, Kun config readiness, and no-write/no-SQL boundary.

## Request

Please write:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/HWAO_B3_EDIT_GATE.md`

Include:
- PASS or BLOCKED;
- whether to accept Lana's exact six decisions as-is or alter any row, especially the three `leave_archival`/`rejected` rows and 28158 gap-card handling;
- exact rows Tori may edit;
- validation Tori must run after apply, including Kun checker;
- exact cockpit progress line/marker Tori may publish after apply.

No queue edit will happen until your PASS gate exists.

Hard locks remain: no SQL, no DB queries/connections, no apply/rollback files, no trust recompute, no prose/wiki publish, no runtime deploy/restart, no git write/push/merge. SQL remains locked until 36/36 and a new operator-approved packet.

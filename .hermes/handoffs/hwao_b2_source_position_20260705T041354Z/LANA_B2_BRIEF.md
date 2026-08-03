# LANA BRIEF — B2 source-position proposal

Marker required in both outputs: `LANA_B2_SOURCE_POSITION_PROPOSAL_20260705T041354Z`
Coordinator: Hwao/Fable
Relay: Tori/Hermes

## User/Hwao directive

The user approved Hwao's recommended next batch B2 and asked that the plan/progress be visible through the cockpit. Hwao issued the B2 plan/cockpit directive at:
`.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/HWAO_B2_PLAN_AND_COCKPIT_DIRECTIVE.md`

Public cockpit marker now visible:
`GALAXY_2929_B2_RUNNING_HWAO_20260705T041354Z`

## Your task

Propose source-position + adjudication values for exactly four B2 rows:

- `28087` — arXiv:2009.11175, candidate 2942
- `28108` — arXiv:2009.11175, kinetic/radio check; candidates 2942/2946, option 2947
- `28133` — arXiv:2009.11175, candidate 2943
- `28074` — arXiv:2604.15438 SWAN, candidate 2942

Use the queue's own `required_source_position_fields` template and the same four blocks as batch 1:

1. source-position block;
2. adjudication block;
3. decision block;
4. checks / duplicate / caveat block.

## Inputs

Queue files:
`docs/galaxy_2929_source_position_queue_20260705T013911Z/queue/`

B2 pre-edit snapshot:
`.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/pre_edit_queue_snapshot_b2_20260705T041354Z/`

Batch-1 proposal to reuse established paper context:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/LANA_SOURCE_POSITION_PROPOSAL.md`
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/lana_source_position_proposal.jsonl`

Hwao remaining-30 plan:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/HWAO_REMAINING_30_BATCH_PLAN.md`

## Binding rules

- Read-only. Do not edit queue files.
- No SQL, DB, apply/rollback, prose/wiki publish, runtime deploy/restart, git write/push/merge.
- Output only the two files listed below in this handoff directory.
- Zone honesty: if using introduction/background spans, label that clearly and cap at `accepted_limited` unless full-text pinning justifies full `accepted`.
- Full `accepted` for a visible-successor relink requires full-text span pinning. Without that, cap at `accepted_limited` or park.
- Abstract-only decisions are acceptable for archival/route/limited outcomes if labeled `abstract_only_verified` and caveated.
- Candidate targets are hints, not orders; propose differently only with a reason.
- Expected dependency counts are zero. If any B2 row has non-zero votes/comments/element links, stop that row and report it as parked for dependency handling.
- If a decision would require creating a new claim, do not improvise; write it as backlog and park that row.

## Special 28108 stacking judgment

If `28108` routes to 2947, assess duplicate/redundancy against:

- 2947 live evidence `26681–26685`; and
- batch-1 docs-only rows already routed to 2947: `28095`, `28111`.

Three rows from the same paper landing on the same successor claim may overweight one source. Judge whether `28108` adds a genuinely distinct span/role or should be `leave_archival` / limited / parked to avoid same-paper stacking.

## Outputs

Write exactly these two files:

1. `.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/LANA_B2_PROPOSAL.md`
   - method;
   - per-row reasoning;
   - the 28108 stacking judgment;
   - source access level per row;
   - any parked/blocker row and why.

2. `.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/lana_b2_proposal.jsonl`
   - exactly four JSONL objects, one per row;
   - include all queue fields needed for Tori to apply only after Hwao gate;
   - include `evidence_id`, `queue_id`, `human_decision_enum`, `accepted_for_docs_source_position`, source locator/quote/context, selected role/stance, accepted target if any, duplicate/dedup status, source-position note, dependency handling action, product gate, and verification status.

Done marker: standalone line `LANA_B2_SOURCE_POSITION_PROPOSAL_20260705T041354Z` in both outputs.

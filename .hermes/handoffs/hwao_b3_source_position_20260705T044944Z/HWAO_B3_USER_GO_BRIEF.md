# Hwao brief — user says go ahead with B3 under same no-SQL lane order

Marker: `HWAO_B3_USER_GO_20260705T044944Z`
From: User via Tori relay
To: Hwao/Fable coordinator

## User directive

"B2 is complete docs-only. Hwao recommends B3 next under the same no-SQL, no-product-mutation lane order."

Interpretation: proceed with B3 as Hwao's next recommended batch under the established Hwao-led no-SQL/no-product-mutation source-position pipeline. Tori is relay/executor only.

## Current verified state

- Queue: `docs/galaxy_2929_source_position_queue_20260705T013911Z/queue/source_position_human_adjudication_queue.{json,jsonl,csv,md}`
- Total rows: 36
- Current completed docs-only rows: 10/36
- Current completed row IDs: `28060, 28074, 28087, 28091, 28095, 28108, 28111, 28133, 28141, 28155`
- Remaining pending: 26
- SQL lock: until 36/36 completed human/source decisions plus a new operator-approved packet
- Active phrase: `NO ACTIVE EXECUTION PHRASE`
- Cron `fd0987371f65` is paused before B3 to avoid queue-file race.

B2 receipts:
`.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/TORI_B2_EDIT_RECEIPTS.md`

B2 public marker:
`GALAXY_2929_B2_APPLIED_10_OF_36_20260705T041354Z`

## B3 from your standing plan

Paper: arXiv `2403.17145` — galaxy groups as AGN-feedback probe

Rows:

| evidence_id | queue_id | current claim | target options | dependency counts |
|---:|---|---:|---|---|
| 28123 | SPQ-2929-28123 | 2929 | 2946, 2942 | comments 0, element_links 0, evidence_votes 0, jury_scorecards 0 |
| 28127 | SPQ-2929-28127 | 2929 | 2946, 2945, 2947 | comments 0, element_links 0, evidence_votes 0, jury_scorecards 0 |
| 28139 | SPQ-2929-28139 | 2929 | 2946, 2947 | comments 0, element_links 0, evidence_votes 0, jury_scorecards 0 |
| 28143 | SPQ-2929-28143 | 2929 | 2946, 2943 | comments 0, element_links 0, evidence_votes 0, jury_scorecards 0 |
| 28151 | SPQ-2929-28151 | 2929 | 2946 | comments 0, element_links 0, evidence_votes 0, jury_scorecards 0 |
| 28158 | SPQ-2929-28158 | 2929 | 2946, 2947 | comments 0, element_links 0, evidence_votes 0, jury_scorecards 0 |

Your prior characterization: "one read amortized over six rows; alternative/qualifier-heavy → likely 2944/2945 or archival."

## Requested Hwao output

Write exactly:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/HWAO_B3_PLAN_AND_COCKPIT_DIRECTIVE.md`

Include:

1. B3 plan/lane order under same pattern:
   - cockpit checkpoint first if you want progress visible;
   - Lana proposal report + JSONL only;
   - Kun checker update/reuse plan;
   - Goru validation;
   - Hwao PASS/BLOCKED gate;
   - Tori bounded docs-only apply + validation + receipts;
   - no SQL/product mutation.
2. Exact B3-running cockpit card/status text and marker for Tori to publish before dispatching lanes, or say explicitly `no cockpit start update` if you do not want one.
3. Exact Lana brief outline: what source material to read for arXiv 2403.17145; how to handle candidate targets 2942/2943/2945/2946/2947; full-text vs abstract-only rule; park/archival conditions.
4. Exact Kun checker requirement: reuse B2 checker if sufficient or request a B3-specific checker copy/config update.
5. Stop conditions and hard locks.

## Hard locks

No DB queries/connections, no SQL files, no apply/rollback files, no DB writes, no trust recompute, no prose/wiki publish, no runtime deploy/restart, no git write/push/merge. Public cockpit mutation only if Hwao explicitly directs it and only as a rich-static checkpoint with `NO ACTIVE EXECUTION PHRASE` preserved.

HWAO_B3_USER_GO_20260705T044944Z

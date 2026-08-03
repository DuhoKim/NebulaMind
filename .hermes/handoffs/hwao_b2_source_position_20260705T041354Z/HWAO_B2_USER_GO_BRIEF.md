# Hwao brief — user says go ahead with B2 and show plan/progress through cockpit

Marker: `HWAO_B2_USER_GO_20260705T041354Z`
From: User via Tori relay
To: Hwao/Fable coordinator

## User directive

"okay go ahead with Hwao's recommended next bach, and let her guide Lana to incldue plan and all through cockpit so that I can check too."

Interpreted plainly:

- Start Hwao's recommended next batch B2.
- Hwao remains coordinator/planner.
- Hwao guides Lana and any other lanes.
- The B2 plan/progress should be visible through the public cockpit so the user can check it.
- Tori remains relay/recorder/verifier/bounded executor.

## Current queue state

Queue dir:
`docs/galaxy_2929_source_position_queue_20260705T013911Z`

Current standing before B2:

- 36 queue rows total.
- 6/36 completed docs-only from the vote-dependent batch.
- 30 remain pending.
- SQL locked until 36/36 human/source decisions plus a new operator-approved packet.

Completed rows already validated PASS:
`28060, 28091, 28095, 28111, 28141, 28155`

B2 rows from your plan:

| Evidence | Source | Candidate/target hints | Current state |
|---:|---|---|---|
| 28087 | arXiv:2009.11175 | candidate 2942 | pending |
| 28108 | arXiv:2009.11175 | kinetic/radio check; candidates 2942,2946, option 2947 | pending |
| 28133 | arXiv:2009.11175 | candidate 2943 | pending |
| 28074 | arXiv:2604.15438 SWAN | candidate 2942 | pending |

## User-authorized cockpit visibility

The user explicitly wants the plan and progress through the cockpit so they can check.

Please direct what Tori should publish to cockpit before/while B2 runs. Requirements:

- Preserve the rich existing cockpit and protected markers.
- Patch only content/status/cards/JSON; no redesign.
- Show B2 is running under Hwao coordination.
- Show lane order: Hwao → Lana proposal → optional Kun checker → Goru validation → Hwao gate → Tori docs-only apply.
- Show row set: 28087, 28108, 28133, 28074.
- Show no active execution phrase and hard no-SQL lock.
- Phrase state remains `NO ACTIVE EXECUTION PHRASE`.
- No public cockpit rewrite beyond Hwao-directed safe status/count/plan update.

## Requested Hwao outputs

Please write:

1. `HWAO_B2_PLAN_AND_COCKPIT_DIRECTIVE.md`
   - exact B2 plan and lane assignments;
   - exact cockpit text/marker Tori should publish now;
   - whether Kun should build the checker before B2 edit step;
   - exact Lana brief requirements;
   - stop conditions.

2. If you want Tori to dispatch Lana immediately, include the exact Lana brief outline and output file requirements.

## Hard locks

No SQL, no DB queries/connections, no SQL/apply/rollback files, no trust recompute, no prose/wiki publish, no runtime deploy/restart, no git write/push/merge.

Queue edits are allowed only after: Lana proposal → Goru validation → Hwao PASS edit gate → Tori bounded apply → validation.

Cockpit static update is authorized by user and must be Hwao-directed; preserve rich layout and verify public URLs.

## Tori current action

Tori paused local cron `fd0987371f65` to avoid a queue race while B2 runs.

HWAO_B2_USER_GO_20260705T041354Z

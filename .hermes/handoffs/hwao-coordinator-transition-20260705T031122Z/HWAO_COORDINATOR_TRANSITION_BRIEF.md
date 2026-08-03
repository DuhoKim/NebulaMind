# HWAO COORDINATOR TRANSITION BRIEF

Marker: `HWAO_COORDINATOR_TRANSITION_20260705T031122Z`
From: User via Tori relay
To: Hwao / Fable

## User directive, verbatim in substance

Use Hwao as coordinator/planner, and Tori just as relay. From now on Tori should relay the user's direction directly to Hwao and let Hwao divide the work, coordinate other members, assemble results, plan the next move, and report to the cockpit.

## New operating model

- Hwao/Fable is coordinator and planner.
- Tori/Hermes is relay, recorder, tool executor only when instructed, receipt verifier, and durable-state updater.
- Hwao decides how to divide work among Lana, Goru, Kun, and any other lanes.
- Hwao assembles results and plans the next move.
- Hwao directs what should be reported to the cockpit.
- Tori should not independently become cockpit captain/planner unless Hwao is unavailable or the user explicitly asks Tori to act.

## Current context to preserve

- Active public cockpit marker: `GALAXY_2929_SOURCE_QUEUE_HELPER_QA_PATCHED_20260705T020200Z`
- Current phrase: `NO ACTIVE EXECUTION PHRASE`
- Current public cockpit is rich Baseline cockpit and must preserve:
  - `RICH_BASELINE_STABLE_COCKPIT_V1`
  - `id="baseline"`
  - `id="baseline-steps"`
  - `id="lane-board"`
  - `id="safety-ledger"`
- HermesOps stale/minimal cockpit source was restored from rich public root at `20260705T030736Z`; do not use stale/minimal copies as templates.

## Hard locks unless user separately approves

- no DB writes
- no SQL/apply files
- no prose/wiki publish
- no NebulaMind runtime deploy/restart
- no git commit/push/merge
- no public cockpit redesign/rewrite
- no use of old approval phrases

## Request to Hwao

Please write a short acknowledgment/coordination contract at:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/hwao-coordinator-transition-20260705T031122Z/HWAO_COORDINATOR_ACK.md`

Include:
1. acknowledgement that Hwao is coordinator/planner and Tori is relay;
2. how future user directions should flow through Hwao;
3. how Hwao will divide work to Lana/Goru/Kun;
4. what Tori may do without asking Hwao first;
5. what Tori must not do without Hwao/user direction;
6. whether the current public cockpit should be updated now or left unchanged.

No DB/prose/runtime/git/public-cockpit mutation is requested by this brief.

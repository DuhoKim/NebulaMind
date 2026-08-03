# Hwao coordinator transition — Tori relay receipt

Status: `HWAO_COORDINATOR_TRANSITION_RELAYED_AND_ACCEPTED`
Timestamp UTC: `20260705T031122Z`

## User directive

From now on Hwao/Fable is coordinator and planner. Tori/Hermes is relay.

## Relay status

- Tori wrote the transition brief.
- Tori sent the brief to the `lana-fable` Hwao lane.
- Hwao wrote the acknowledgment file.
- Hwao says the public cockpit should be left unchanged now; one coordination line can ride the next regular update.

## Hwao-accepted flow

1. User gives direction.
2. Tori relays it to Hwao with a short current-state note.
3. Hwao returns the plan-brief: objective, lane split, gates, what Tori may execute, and what cockpit line to publish.
4. Lana/Goru/Kun report to Hwao's plan.
5. Hwao assembles results and gives Tori bounded recording/rendering/execution instructions.
6. Tori verifies receipts/files/markers and reports plainly.

## Tori may do without asking Hwao first

- relay user direction;
- record durable briefs/receipts;
- read-only verification and snapshots;
- durable-state recording of decisions already made;
- halt unsafe or conflicting actions.

## Tori must not do without Hwao/user direction

- choose next moves;
- mint/rotate/execute approval phrases;
- perform DB/prose/runtime/git mutation;
- redesign/rewrite the public cockpit;
- silently assume coordinator role.

## No-write ledger

- DB writes: `0`
- SQL/apply files: `0`
- prose/wiki publish: `0`
- NebulaMind runtime deploy/restart: `false`
- git commit/push/merge: `false`
- public cockpit redesign/rewrite: `false`

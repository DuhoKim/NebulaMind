# USER_DIRECTION — Flow + Deep Research parallel-run viability test

Timestamp: 2026-07-14T03:47:20Z
Coordinator: Hwao/Fable
Correspondents: Tori/Hermes for Deep Research; Yui for Flow
Helpers: agy agents Goru, Garu, WonE in Hwao-scoped lanes
Mechanical controller: deterministic browser broker

## User direction

The user directed Hwao to test whether the Flow + Deep Research parallel run is viable.

## Start-now interpretation

Hwao is authorized to begin the viability ladder now, not merely save a plan:

1. create this dedicated local test packet and append-only run ledger;
2. collect role/protocol ACKs from Yui, Goru, Garu, and WonE before they participate;
3. prepare/implement the local broker, target leases, account-submission lease, exclusive desktop-control lease, fail-closed fencing, and audit receipts in a dedicated sandbox;
4. create dedicated non-default local test browser profiles and isolated download directories without copying credentials or secrets;
5. run the non-destructive C0–C3 canaries sequentially, three comparable passes per rung, stopping on the first invariant breach;
6. prepare C4 but stop before any account sign-in, security prompt, permission prompt, CAPTCHA/challenge, submit-like action, or quota-bearing action that needs a separate gate.

## Required execution rule

- True parallel browser writes may use browser-native DOM/CDP only, in separate browser processes/profiles and exact target IDs.
- Every cua/AX/pointer/keyboard/desktop write is serialized under one machine-wide desktop-control lease.
- Correspondents relay, record, verify receipts, and report status. They are not automatic browser writers.
- One broker-epoch-ordered append-only ledger is the source of truth. Disagreement is STOP-class and goes to Hwao.
- Anyone may call STOP. The broker freezes both sides immediately; no final action. Only the user may authorize resume after a STOP.

## Still held behind separate explicit user gates

- copying or exposing browser credentials, cookies, tokens, or secrets;
- Google sign-in/account changes or handling permission/security prompts;
- C4 authenticated-surface execution if fresh authentication is needed;
- any Flow or Deep Research submission;
- any AI-credit/quota spend;
- the Phase IV live overlap canary;
- DB writes, deploy/restart, git commit/push/merge, public publication, billing, cron, or unrelated browser actions.

## Viability semantics

- Passing C0–C3 can establish local mechanical viability for parallel DOM/CDP browser operation plus serialized desktop control.
- It cannot prove same-account Flow + Deep Research active-job overlap.
- A full cross-product viability verdict requires the separately gated Phase IV minimal live overlap canary.

No held action is implied by this direction.

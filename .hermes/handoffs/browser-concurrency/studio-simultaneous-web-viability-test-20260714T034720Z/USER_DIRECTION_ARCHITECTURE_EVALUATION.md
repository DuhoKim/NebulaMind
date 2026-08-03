# USER_DIRECTION_ARCHITECTURE_EVALUATION — compare one-Mac and two-Mac designs

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
User direction received: 2026-07-14T04:25:54Z
Coordinator: Hwao/Fable

## Direction

The user authorizes Hwao to evaluate both architectures and run bounded tests when needed:

- Architecture A: Flow + Deep Research isolated on the Mac Studio.
- Architecture B: Flow on Mac Studio and Deep Research on Mac Pro.

The prior HOLD is lifted only for this non-destructive architecture evaluation. Hwao should execute the smallest sufficient test matrix, compare receipts, and recommend one architecture.

## Authorized evaluation actions

Hwao may:

1. append the existing run ledger and amend the execution plan for an A/B architecture evaluation;
2. run the existing local broker unit tests and the necessary single-machine C0–C3 sandbox canaries;
3. run the two-machine RT0–RT3 sandbox readiness ladder, stopping when enough evidence exists for a decision;
4. create task-scoped files and empty non-default browser profiles/download directories inside the dedicated test packet on each host;
5. activate task-scoped local/SSH/tmux test processes on Mac Pro and Mac Studio;
6. implement and test an authenticated, fail-closed SSH-wrapped broker transport without opening an unauthenticated listener;
7. launch only dedicated sandbox Chrome instances against `about:blank` or local inert test pages, with distinct non-default user-data directories and exact CDP targets;
8. run browser-native DOM/CDP actions only for simultaneous browser writes;
9. run cua/AX/pointer/keyboard actions only on explicitly designated sandbox surfaces and only under the exclusive per-machine desktop-control lease;
10. simulate network loss, lease expiry, broker freeze, and recovery without disrupting user applications or network configuration;
11. use Yui, Tori, Goru, Garu, and WonE only within their acknowledged Hwao-scoped roles.

## Required comparison

For both architectures, report:

- mechanical parallelism;
- default-Chrome/Flow non-interference;
- lease and fail-closed behavior;
- split-brain and bridge-loss behavior;
- setup and operating complexity;
- recovery behavior;
- resource contention;
- evidence quality and reproducibility;
- current readiness and blockers;
- what remains unproven without a live account-bearing test.

Prefer the simpler architecture only if its safety and reproducibility are not materially worse.

## Gates that remain held

This direction does NOT authorize:

- reading, copying, exposing, or transferring credentials, cookies, tokens, profile contents, or secrets;
- Google sign-in, account changes, or handling security/permission/2FA prompts;
- CAPTCHA/challenge interaction;
- touching the user's active Flow window or default Chrome profile on either host;
- any Flow or Deep Research submission;
- any AI-credit/quota spend;
- C4 authenticated execution or the Phase IV live overlap canary;
- DB writes, deploy/restart, git commit/push/merge, publication, billing, cron, or unrelated browser actions;
- installing cua-driver on Mac Pro unless the user later explicitly asks (the DR design should remain DOM/CDP-only).

## Stop and decision rules

- Any prompt, challenge, default-profile/Flow anomaly, unleased desktop write, target ambiguity, bridge loss, partition safety failure, or receipt disagreement is STOP-class.
- The broker freezes affected lanes immediately; no final action.
- Only the user may authorize resume after a STOP.
- Hwao may end testing early when receipts establish a clear architecture winner; she must explain why further tests would not change the decision.

No live account-bearing viability claim may be made from these sandbox tests alone.

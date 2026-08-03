# TORI_PASS1R1_PRERUN_APPROVAL — repaired XM-1 over Thunderbolt

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
Approval UTC: 2026-07-14T07:01:02Z
Authority: Duho explicitly authorized the stdin-fed SSH repair and one XM-1 pass-1 retry. Passes 2–3 remain held.

## State recovered after the accidental interrupt

- Hwao pane alive; no command was half-completed.
- Local task processes: 0.
- Mac Pro task processes: 0.
- `/tmp` broker socket directories: 0.
- Forward port 5592: free.
- Local `pass1r1`: absent.
- Remote `pass1r1`: absent.
- Main run ledger: `VERIFY_OK` before this approval.

## Independent validation

- Python AST parse: PASS for all broker/canary Python files.
- Broker, transport, stdin-repair, and Thunderbolt argv tests: PASS, 42/42.
- Node syntax and WebSocket-forward rewrite checks: PASS, 4/4 rewrite assertions.
- Real stdin-fed execution over direct Thunderbolt: PASS both directions.
  - Studio → Pro reached `x86_64` Mac Pro.
  - Studio → Pro → Studio reached `arm64` Mac Studio.
  - Receipt SHA-256: `94957e1956c9a605b4a724f265fdd37c5559a35e2d33379dc6cb3e2c16195089`.
- Fresh Thunderbolt broker probe `thunderbolt-pass1r1`: PASS.
  - Ping/acquire/check/release passed.
  - Live partition failed closed.
  - Authority confirmed the disconnected lease non-live.
  - Per-probe ledger: `VERIFY_OK` (4 entries).
  - Receipt SHA-256: `fa47e6cc59136948b55c4f84ec4eafd71dd0735ebba21a643a3992ff05f84c60`.

## Approved execution

One invocation only:

`xm1_cross_host.py --armed <packet-token> <packet-root> thunderbolt-pass1r1 duhokim@169.254.100.1 100.122.78.110 /Users/duhokim/.hermes/handoffs/browser-concurrency/studio-simultaneous-web-viability-test-20260714T034720Z 5592 1r1`

The harness must use:

- direct Thunderbolt only (`169.254.100.1` Mac Pro; `169.254.100.2` Mac Studio);
- `StrictHostKeyChecking=yes` with the existing Tailscale addresses used only as `HostKeyAlias` values;
- no automatic Tailscale transport fallback;
- fresh task-specific profiles and receipts;
- inert `about:blank` targets;
- exact leased CDP target identity before every action;
- process-group-scoped teardown.

Stop immediately on any failed assertion, target mismatch, prompt/challenge, endpoint mismatch, lost Thunderbolt bridge, teardown disagreement, default-profile/Flow anomaly, or receipt disagreement. Do not patch or retry after a STOP without renewed user authorization.

## Still prohibited

- XM-1 passes 2–3;
- default Chrome or the active Flow window;
- account sign-in, account/profile contents, credentials, cookies, or tokens;
- Flow or Deep Research submissions;
- AI quota/credit use;
- C4 or any Phase-IV/live-account overlap;
- cua-driver installation on Mac Pro;
- DB, deploy/restart, git write, publication, billing, cron, or unrelated browser action.

## Reviewed code hashes

- `net.py`: `43dd19aa768ec9f39ce86c3319527db6d21c26a2d65eac4756274dc5f17b2960`
- `remote_exec.py`: `0b73a47c45d57636a3d5eb6c2ce67ea15095b9ffc7c01076f4fe8ada46e007f5`
- `test_remote_exec.py`: `f81721bca0bdef9328450164d56cfddd3dd4a3a4c2e918a64f6e2b791f84655e`
- `test_net.py`: `4684670f534492cd91cc6ed01dca1900ab8ab7c15333054c816b8ff96799d7d9`
- `thunderbolt_stdin_check.py`: `4a26848d5bf40a5e192e81a68ce142077a4b59015558c95e6bb5c4d10614ce4c`
- `xm1_broker_probe.py`: `b554738d3b89f3dfac42e8695fe60185ee23f1a9341db04426ffe3b7347fcc2c`
- `xm1_cross_host.py`: `c47c81cb42d52413092aea509881873d90dcf0a71988f735db1158a4fbd836e9`
- `remote_chrome_controller.py`: `8dd1188c15deeac5526fc8ad7640cdd6f3f5ba5692dddc14af3eaa5f73673eec`
- `sm1_cdp_parallel.mjs`: `29a9c0830e1a5e86f59f8bf43a06f3aa23eeddbf9951f88e46cb07e21bdc60f0`
- arming token: `8a11f73eab5875ffbf6414978b28522f7a24166efa8c5201566dbf4e4e4a301b`

Any functional change to these reviewed files invalidates this approval.

TORI_XM1_PASS1R1_APPROVED_20260714T070102Z

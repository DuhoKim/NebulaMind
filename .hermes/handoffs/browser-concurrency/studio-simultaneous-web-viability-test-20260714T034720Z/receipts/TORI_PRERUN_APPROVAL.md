# TORI_PRERUN_APPROVAL — bounded A/B sandbox architecture evaluation

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
Approval UTC: 2026-07-14T06:20:17Z
Authority: standing `USER_DIRECTION_ARCHITECTURE_EVALUATION.md`; this receipt is Tori's renewed pre-run safety approval.

## Validation received

- Python AST parse: PASS for all broker and canary Python files.
- Node syntax: PASS.
- WebSocket-forward rewrite unit test: PASS, 4 assertions.
- Broker/transport suite: PASS, 28/28.
- Mac Pro reverse authenticated SSH to Studio: `REVERSE_SSH_OK` previously verified.
- Mac Pro `setsid` is absent; the reviewed remote controller uses Python `start_new_session=True` and exact `killpg` teardown instead.

## Approved execution, in this order

1. Journal the final plan/code/arming token with `broker/journal.py` and verify the chain.
2. Run `xm1_broker_probe.py` once: no browser, real Mac Pro → Studio authenticated broker path, live-lease partition expiry drill.
3. Run SM-1 passes 1, 2, and 3 with fresh per-pass state, ledger, profiles, and receipts.
4. If all preceding steps pass, run XM-1 passes 1, 2, and 3 with fresh local and remote per-pass directories and currently free loopback forwarding ports.
5. Stop immediately on the first failed assertion, prompt/challenge, target mismatch, default-profile/Flow anomaly, bridge/channel ambiguity, teardown failure, or receipt disagreement.
6. If all passes succeed, collect Yui's read-only Studio non-interference countersign and write the comparison/verdict for Tori verification.

## Exact boundaries

Approved:

- dedicated non-default sandbox Chrome only;
- inert `about:blank` targets only;
- browser-native DOM/CDP writes under exact host/profile/target leases;
- one Studio broker authority on a 0600 UDS in a short 0700 `/tmp` directory;
- authenticated SSH/SCP only, with strict host-key checking;
- task-scoped Mac Pro files under `/Users/duhokim/.hermes/handoffs/browser-concurrency/studio-simultaneous-web-viability-test-20260714T034720Z`;
- exact process-group teardown and preserved receipts.

Still prohibited:

- default Chrome or the active Flow window;
- Google sign-in, account/profile contents, credentials, cookies, tokens, challenges, CAPTCHA, or permission prompts;
- Flow or Deep Research submissions and any AI-credit/quota spend;
- C4 or Phase IV live/account overlap;
- cua-driver installation on Mac Pro;
- DB, deployment, git write, publication, billing, cron, or unrelated browser actions.

## Reviewed hashes

- arming token: `8a11f73eab5875ffbf6414978b28522f7a24166efa8c5201566dbf4e4e4a301b`
- `run_sm1.py`: `f26340f45cc9ae585da1c1d920d4edc38abb7d3db74823bd6c0c509ec5efb0c1`
- `sm1_cdp_parallel.mjs`: `29a9c0830e1a5e86f59f8bf43a06f3aa23eeddbf9951f88e46cb07e21bdc60f0`
- `ws_rewrite.mjs`: `c4ece6f3f59ca466b247f1512a3cb81c8c41518441a5d4abcf1cb7c1fdbb5c37`
- `xm1_broker_probe.py`: `f81077e985d5d42f7328b079e9bce6882270a0a33c68ac5616da8120878bcc12`
- `xm1_cross_host.py`: `bdc79af4328473e4c64eaa6064e894851622cb2989daed681db44d226c5d3442`
- `remote_chrome_controller.py`: `8dd1188c15deeac5526fc8ad7640cdd6f3f5ba5692dddc14af3eaa5f73673eec`
- `broker.py`: `93221b10f4d4e300342106c5cb01b8bfda024836831b0fc84234aa4ab5190554`
- `broker_daemon.py`: `9b6177ce70049ffd566274c6be2fe69e4c1ca13b3f3e12d8870252f41819b44e`
- `transport.py`: `0aa280b884959b2cc74183a8f30a20142e9b25baf89c8c8d6be9f17cb817ba30`
- `ARCHITECTURE_EVALUATION_PLAN.md`: `6b94c75e97a051f233aac837cbc439f828cee4f9af9258f5e40f3bf3542a6b72`

These hashes were rechecked after the final rung/host/pass metadata and stricter probe assertions were applied. Hwao must journal the same current hashes before execution; any later functional code change invalidates this approval and requires renewed review.

TORI_ARCHEVAL_PRERUN_APPROVED_20260714T062017Z

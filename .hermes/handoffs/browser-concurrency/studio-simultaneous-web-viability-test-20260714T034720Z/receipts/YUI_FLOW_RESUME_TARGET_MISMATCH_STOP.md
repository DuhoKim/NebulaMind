# YUI Flow resume + target-mismatch STOP receipt

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
Actor: Yui, Flow operator on Mac Studio
Authorization: `receipts/DUHO_RESUME_AUTHORIZATION.md`
Authorization SHA-256: `9f6654c61b91940420793e5e2d06d114b797a97ad27d7932c0b11f4b8246d0b5`
Authorization marker: `DUHO_RESUME_AUTHORIZATION_20260714`

## Authorized reset

The Duho-authorized broker reset completed and was broker-journaled:

- reset ledger epoch: `22`
- reset entry SHA-256: `3ee6ff45d8db6ee45cb2c947a6d37f7a5ec4860f92881163eb1d4c15074310c2`
- reset type: `frozen_reset`
- restarted broker PID: `77150`
- post-reset broker state: `frozen=false`, zero live leases
- ledger: `VERIFY_OK`

The first direct reset invocation changed state but failed to journal because Python resolved the wrong `ledger` module. Yui immediately fail-closed and re-froze at epoch 21, then repeated the authorized reset with the packet broker directory pinned in `sys.path`; epoch 22 is the successful broker-authored reset receipt.

## Binding page-scoped challenge fix

Implemented:

- `canaries/_tmp_yui_flow_page_probe.py`
- `canaries/_tmp_yui_flow_page_probe_test.py`

The detector reads only the exact Flow page URL, Flow DOM, and visible on-page dialogs. It treats `accounts.google.com` redirects, on-page CAPTCHA text, and visible sign-in/verification surfaces as STOP signals. Browser toolbar/profile chrome is not an input and `AXPopUpButton '조치 필요'` alone does not trigger STOP.

Verification: `5 passed`; live Flow page probe returned `challenge=false`, zero signals, zero visible dialogs.

## One bounded job attempt

No accepted Flow job receipt was produced and no batch scaling occurred.

Initial exact leased Flow target:

- project id prefix: `94b7dd5c`
- target lease: `L00015`, epoch `15`

Before the established Flow-driver paste, the page-scoped probe reported a different current Flow target:

- project id prefix: `3b2a3843`
- title timestamp changed from `12:57` to `05:47`
- page challenge result remained clean: `challenge=false`

The non-secret 151-character bounded canary prompt was pasted into the current composer, but no Return/Create submit was performed on that new target. On detecting that the exact page no longer matched the leased target, Yui invoked the broker with `target_verified=false` and stopped rather than falling back to the newly active project.

## Fail-closed receipt

- bridge-loss ledger epoch: `90`
- bridge-loss entry SHA-256: `9a9707c834840e31f8cbf6fe7e0c1a4b822305b53ac913fbd1f1e1bc827b6ac2`
- emergency-freeze ledger epoch: `91`
- emergency-freeze entry SHA-256: `4833287ada358115eb7b1f4350c08a5d01bb91fd66772a59d788273265cd7645`
- broker state after freeze: `frozen=true`, zero live leases
- ledger: `VERIFY_OK`

No credentials, cookies, tokens, profile contents, or secrets were read. No Flow-page sign-in, CAPTCHA, challenge, or `accounts.google.com` redirect was observed. The stop reason is exact-target loss, not the benign Chrome toolbar sync badge.

## Required next action

Hwao/Duho must reconcile which Flow project is the intended one-job target and issue the next Duho-only broker-resume authorization. On resume, Yui must acquire a target lease for the currently verified project id and assert that id immediately before every mutating action. No scaling is permitted.

YUI_FLOW_RESUME_TARGET_MISMATCH_STOP_20260714T085214Z

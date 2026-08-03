# GORU brief — DR authenticated-CDP Chrome launch on Mac Pro (Duho-gated)

Gate of record: `receipts/DUHO_GATE_PRO_CDP_CHROME.md` (sha256 `1f1700e5…c1ac8`). Executor: **Goru** (DR/Pro driver); **Tori** independently verifies the receipt. Coordinator: Hwao (does not drive). Broker authority on the Studio; coordination is ledger-mediated. All standing rails bind. **No agent handles credentials or 2FA at any point.**

## Preconditions (from Pro preflight — re-confirm immediately before acting)
- Console user `duhokim` + WindowServer active on the Pro (a visible window is possible).
- Chrome app present; exactly **1 default Chrome root, unchanged**; **no dedicated DR root**; **port 9223 free**.
- Packet mirror absent on the Pro → create **only** the authorized minimal packet sandbox path, **mode 0700**, fresh non-default profile dir **`dr-live-cdp-20260714`**. Nothing else; no copying of any default profile/credentials.

## Launch (exactly once, VISIBLE — no headless)
1. Create the minimal 0700 sandbox path + fresh `dr-live-cdp-20260714` profile (non-default `--user-data-dir`).
2. Launch **one visible new Chrome** via `open -na "Google Chrome" --args --user-data-dir=<sandbox>/dr-live-cdp-20260714 --remote-debugging-address=127.0.0.1 --remote-debugging-port=9223 https://accounts.google.com`. **Do NOT** `activate`, focus-steal, close, or otherwise touch the default Chrome, any existing window, or the user Flow context.
3. **Verify (ALL must hold; any failure ⇒ STOP):**
   - a **dedicated Chrome PID** whose args carry the exact non-default `user-data-dir` + `--remote-debugging-port=9223` (distinct from the default root, which stays unchanged);
   - the CDP listener is bound **loopback-only** (`127.0.0.1:9223`), never an external interface;
   - a CDP **page target at accounts.google.com** exists (read-only `GET /json/list` on 127.0.0.1:9223);
   - a **PID-specific visible window** is present for that dedicated PID, without activating the default Chrome.
   - **If visible-window verification fails → STOP** (capture, receipt, escalate; no blind retry).
4. After a verified launch, create the authorized **loopback-only forward**: Studio `127.0.0.1:19223` → Pro `127.0.0.1:9223` over the Thunderbolt endpoint (HostKeyAlias-pinned, `StrictHostKeyChecking=yes`, `ExitOnForwardFailure=yes`). No other forward; no existing `ssh -L` was found, so this is a fresh single forward.

## Receipt, then PAUSE for Duho sign-in
- Write a Goru receipt (Tori verifies) recording: dedicated PID, exact args, user-data-dir, **loopback-only listener proof**, CDP target URL, **visible-window proof**, forward status, and an attestation that the **default Chrome/profile and the user Flow window were not touched and no credentials/2FA were handled**.
- Then **PAUSE**. **Duho signs in manually at accounts.google.com** — no agent types, reads, or handles credentials or 2FA. Do **not** drive, navigate, submit, or acquire any DR job lease. **Deep Research job execution is a SEPARATE held gate.**

## Hard stops (→ STOP + receipt + escalate to Hwao; resume Duho-gated)
Visible-window verification failure · any touch of default Chrome/Flow · any non-loopback listener · port 9223 not free · more than one dedicated root · any credential/2FA handling · any account-submit or DR-job action.

GORU_DR_CDP_LAUNCH_BRIEF_20260714T034720Z

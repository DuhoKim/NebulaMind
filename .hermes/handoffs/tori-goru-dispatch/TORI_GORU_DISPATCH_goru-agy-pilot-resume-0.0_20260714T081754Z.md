# Tori -> Goru dispatch

Target: goru-agy-pilot-resume:0.0
Timestamp: 20260714T081754Z

## Payload

```text
GORU / ANTIGRAVITY BRIEF — Tori-dispatched — 20260714T081754Z

Use Gemini/Antigravity quota for this scoped Tori helper task.

Safety boundary:
- Stay inside the explicit scope in the brief below.
- Prefer read-only mechanical checks, counts, inventories, source maps, repro checks, and draft reviews.
- Do not do DB writes, deploy/restart, git commit/push/merge, cloud/GCP/Gemini API config changes, secrets inspection, or live publication unless the user gives a separate explicit gate.
- If command permission is needed, ask for the smallest exact command; Tori will approve only scope-matching safe commands.
- Write/report exact files, counts, commands, and blockers. Do not self-certify unverified external facts.

Assigned brief:

# GORU DR RESUME — ledger epoch 22

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
Authority: `receipts/DUHO_RESUME_AUTHORIZATION.md` and broker-authored ledger reset.

Resume marker verified by Tori:

- Ledger epoch: 22
- Type: `frozen_reset`
- Entry SHA-256: `3ee6ff45d8db6ee45cb2c947a6d37f7a5ec4860f92881163eb1d4c15074310c2`
- User gate: `DUHO_RESUME_AUTHORIZATION_20260714`
- Ledger: `VERIFY_OK` with 23 entries at verification
- Broker state: `frozen=false`, zero leases

You may now execute exactly ONE bounded live Deep Research run on the Mac Pro, paired with Tori as receipt verifier.

Bounded canary prompt:

> Using official Apple and Google Chrome documentation, explain in no more than eight bullets how a direct Thunderbolt Bridge between two Macs can support isolated browser automation. Include two limitations and source links.

Binding execution:

1. Mac Pro only; DOM/CDP only; exact authenticated Deep Research target identity. No CUA, pointer, global keyboard, clipboard, or frontmost fallback.
2. Perform a page-scoped preflight. A real Gemini/Flow page challenge, CAPTCHA, sign-in wall, 2FA, permission prompt, redirect to an account login, or unknown page state is immediate STOP + broker freeze. Chrome toolbar/profile badges alone are out of scope.
3. Acquire and check an exact target lease before browser writes.
4. Immediately before the one submit action, acquire the broker `account-submission` lease from the Studio authority. If held/denied, do not submit; report and wait for Tori/Hwao direction. Release after the submit result is confirmed.
5. No credentials, cookies, tokens, profile-content inspection, or secret access.
6. One bounded run only. Capture: target fingerprint (non-secret), lease IDs/epochs, submit timing, page-scoped preflight result, run-start confirmation/result, quota observation if shown without extra navigation, teardown, and hashes. Append a Goru receipt to the ledger, then stop and report to Tori before scaling.

If the exact authenticated DR target or a broker-aware submit path is unavailable, do not improvise or copy profile data. Stop and report the blocker.

GORU_DR_RESUME_EPOCH22_20260714

Done marker: TORI_GORU_DISPATCH_DONE_20260714T081754Z

```

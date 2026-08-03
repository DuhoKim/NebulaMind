# TORI PRO CDP CHROME — ready for Duho sign-in

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
UTC verified: 2026-07-14T09:29:09Z
Gate: `receipts/DUHO_GATE_PRO_CDP_CHROME.md`
Gate SHA-256: `1f1700e5742ea65478b686d540c47d99c597ccea2cf5cf8ee457e85ea1c81ac8`

## Launch result

Goru launched exactly one dedicated Google Chrome instance on the Mac Pro under the Duho gate. Tori independently verified:

- Dedicated root PID: 65195
- Dedicated Chrome version: 150.0.7871.115
- Fresh non-default profile: packet sandbox `dr-live-cdp-20260714`
- Profile mode: 0700; owner: `duhokim`
- Dedicated remote-debugging flags: exact profile, address `127.0.0.1`, port 9223
- Headless flag: absent
- Pro listener: only `127.0.0.1:9223`
- Chrome roots after launch: 2 total = 1 dedicated + the original/default root unchanged
- Initial sanitized page target: Google Accounts sign-in

No default profile, cookies, credentials, or profile content was copied or read. No command targeted the existing/default Chrome process or windows.

## Visible GUI verification

Goru's first PID-specific System Events check transiently returned zero visible windows and correctly held. Tori immediately rechecked independently:

- Dedicated process visible: true
- Dedicated window count: 2

The dedicated GUI Chrome is therefore surfaced on the Mac Pro. Subsequent sanitized CDP metadata changed while apparent human-side activity was occurring; agents stopped inspecting and make no inference that sign-in is complete.

## Studio-only CDP transport

Tori created the authorized authenticated loopback-only SSH forward over the direct Thunderbolt link:

- Studio: `127.0.0.1:19223`
- Pro destination: `127.0.0.1:9223`
- Forward PID: 92170
- Tracked Hermes process: `proc_378911a01590`
- `ExitOnForwardFailure=yes`; strict host-key checking; pinned Mac Pro host identity
- Local `/json/version` and sanitized `/json/list` probe: PASS

Neither CDP endpoint is exposed on a non-loopback interface.

## Current gate state

Hwao was notified immediately that the visible dedicated browser is ready. Goru acknowledged `briefs/GORU_PRO_CDP_READY_HOLD_FOR_DUHO.md` and is paused completely unarmed.

Actions not taken:

- No credentials or 2FA handled by agents
- No clicks, typing, or sign-in actions by agents
- No DR target or account-submission lease
- No Deep Research navigation, submission, run, or quota spend

Required next marker: Duho explicitly confirms the dedicated Pro Chrome is signed in. Only then may Tori and Goru attach through the loopback SSH forward, perform the page-scoped preflight, acquire the exact target and serialized account-submission leases, and run one bounded DR canary.

TORI_PRO_CDP_READY_FOR_DUHO_SIGNIN_20260714T092909Z

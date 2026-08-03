# GORU — launch one dedicated visible CDP Chrome on Mac Pro, then PAUSE

Gate: `receipts/DUHO_GATE_PRO_CDP_CHROME.md`
Gate SHA-256: `1f1700e5742ea65478b686d540c47d99c597ccea2cf5cf8ee457e85ea1c81ac8`

Duho authorizes exactly one fresh dedicated Chrome for DR sign-in. Do not touch the existing/default Chrome process or windows.

Canonical host and launch parameters:

- SSH: `duhokim@169.254.100.1`, with `HostKeyAlias=100.122.78.110`, strict host-key checking, and batch mode.
- Remote packet root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/browser-concurrency/studio-simultaneous-web-viability-test-20260714T034720Z`
- Fresh user-data-dir: `<packet>/sandbox/profiles/dr-live-cdp-20260714`
- Remote CDP: `127.0.0.1:9223`
- Initial URL: `https://accounts.google.com/`

Verified preflight: console user `duhokim`; WindowServer active; Chrome app present; exactly one existing default Chrome root; no dedicated root; remote port 9223 free; the packet mirror does not yet exist on Pro.

Execution:

1. Re-check that port 9223 is free and no process uses `dr-live-cdp-20260714`. If not fresh/free, STOP.
2. With `umask 077`, create only the authorized minimal packet path and fresh profile directory. Directory mode must be 0700. Do not copy any profile, cookies, credentials, or files from default Chrome.
3. Launch exactly one new visible Chrome through LaunchServices:
   - `open -na "Google Chrome" --args`
   - `--user-data-dir=<fresh profile>`
   - `--remote-debugging-address=127.0.0.1`
   - `--remote-debugging-port=9223`
   - `--no-first-run --no-default-browser-check --new-window`
   - `https://accounts.google.com/`
   - no headless flag.
4. Do not use `killall`, `pkill`, or any command affecting default Chrome.
5. Verify read-only:
   - one root process whose command contains the exact fresh profile and CDP flags;
   - the original default root remains present and has no fresh-profile flag;
   - the CDP listener is bound only to `127.0.0.1:9223`, never `0.0.0.0` or a non-loopback address;
   - `/json/version` responds and `/json/list` shows a page target at Google sign-in/accounts without reading page content;
   - the dedicated root PID has at least one visible GUI window. Use PID-specific read-only System Events/CGWindow metadata; do not activate, focus, inspect, or report the default Chrome window.
6. If the visible-window check cannot be established, STOP and report. Do not click or type.
7. If all checks pass, report the dedicated root PID, loopback listener, sanitized CDP target metadata, profile mode, and visible-window boolean to Tori. Then PAUSE for Duho sign-in. Agents never type credentials, handle 2FA, or solve challenges.

Do not acquire a browser target or account-submission lease yet; those begin only after Duho confirms sign-in.

GORU_PRO_CDP_CHROME_LAUNCH_20260714

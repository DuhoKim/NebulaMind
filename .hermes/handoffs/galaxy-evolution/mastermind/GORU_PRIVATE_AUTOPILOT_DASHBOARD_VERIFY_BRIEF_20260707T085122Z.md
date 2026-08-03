# Goru private autopilot dashboard verification brief

Marker: `GORU_PRIVATE_AUTOPILOT_DASHBOARD_VERIFY_BRIEF_20260707T085122Z`
User request: "build sophisticately with Hwao and Goru"
Scope: private HermesOps/Tailscale dashboard verification.

## Task

After Tori builds the private dashboard renderer, verify it mechanically from disk and HTTP.

Expected files:

- Renderer script: `/Users/duhokim/NebulaMind/NebulaMind/tools/render_ge_autopilot_dashboard.py`
- Wrapper: `/Users/duhokim/.local/bin/ge-auto-dashboard`
- HTML: `/Users/duhokim/HermesOps/cockpit/ge-autopilot.html`
- JSON: `/Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json`
- URL text: `/Users/duhokim/HermesOps/cockpit/latest-ge-autopilot-url.txt`

Expected private URL:
`https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html`

## Required verification output

Write a verification receipt to:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/GORU_PRIVATE_AUTOPILOT_DASHBOARD_VERIFY_20260707T085122Z.md`

Check:

1. HTML contains `GE_AUTOPILOT_PRIVATE_DASHBOARD_V1`.
2. JSON contains `GE_AUTOPILOT_PRIVATE_DASHBOARD_V1`.
3. HTML contains Directors, Method 1, Method 2, Method 3.
4. HTML contains the intended MacBook/private Tailscale URL or copyable link.
5. HTML states tailnet-only/private and no browser execution.
6. Local localhost route via `127.0.0.1:8093/cockpit/ge-autopilot.html` returns body marker.
7. Tailnet route returns HTTP 200 and body marker, if reachable from this Studio host.
8. No public NebulaMind cockpit/Baseline files changed.
9. No DB/API/live publish/deploy/git/cloud/secrets/cron/browser automation occurred.

Stop after writing the verification receipt.

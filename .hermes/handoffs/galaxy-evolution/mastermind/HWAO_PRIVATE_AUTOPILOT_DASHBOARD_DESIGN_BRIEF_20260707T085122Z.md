# Hwao private autopilot dashboard design brief

Marker: `HWAO_PRIVATE_AUTOPILOT_DASHBOARD_DESIGN_BRIEF_20260707T085122Z`
User request: "build sophisticately with Hwao and Goru"
Scope: private HermesOps/Tailscale dashboard for MacBook home viewing.

## Task

Design the operator-facing HTML dashboard for the Phase 1 Galaxy Evolution autopilot monitor.

The implementation target is private tailnet-only, not the public NebulaMind cockpit:

- Web root: `/Users/duhokim/HermesOps/cockpit`
- Intended URL: `https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html`
- Data source: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot-status.json`

## Required design output

Write a concise design receipt to:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/HWAO_PRIVATE_AUTOPILOT_DASHBOARD_DESIGN_20260707T085122Z.md`

Include:

1. Recommended layout sections.
2. Plain-English status model.
3. What the user should see first from MacBook.
4. Safety language.
5. Visual hierarchy for Directors, Method 1, Method 2, Method 3.
6. What Goru should verify mechanically.

## Hard boundaries

No DB/API writes, no live wiki publish, no deploy/restart, no git operation, no public NebulaMind cockpit replacement, no baseline cockpit edit, no cloud/API/billing/OAuth/secrets, no cron. This is a private static HTML/JSON artifact only.

Stop after writing the design receipt.

# Goru private autopilot dashboard V2 verification brief

Marker: `GORU_PRIVATE_AUTOPILOT_DASHBOARD_V2_VERIFY_BRIEF_20260707T093119Z`
User request: "can you upgrade the dashboard?"
Scope: private tailnet-only `/Users/duhokim/HermesOps/cockpit/ge-autopilot.html` and `/Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json`; no public NebulaMind cockpit/Baseline.

## Mechanical checks

Verify read-only:
1. HTML body contains `GE_AUTOPILOT_PRIVATE_DASHBOARD_V2`.
2. JSON contains `GE_AUTOPILOT_PRIVATE_DASHBOARD_V2`.
3. HTML contains these V2 sections: `Room-glance answer`, `Latest autopilot events`, `Safety policy legend`, `Directors`, `Method 1`, `Method 2`, `Method 3`.
4. Local route `http://127.0.0.1:8093/cockpit/ge-autopilot.html` returns HTTP 200 and body marker.
5. Tailnet route `https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html` returns HTTP 200 and body marker.
6. No action surface in source HTML: no `<button`, no `<form`, no `POST`, no external CDN/font/analytics dependencies.
7. Dashboard watcher `ge-auto-dashboard` is alive.
8. Public NebulaMind cockpit/Baseline files are not part of this check.

Use one read-only command at a time if Antigravity prompts. Do not mutate anything.

## Receipt

Write:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/GORU_PRIVATE_AUTOPILOT_DASHBOARD_V2_VERIFY_20260707T093119Z.md`

Include PASS/FAIL and the exact checks above. Stop after writing.

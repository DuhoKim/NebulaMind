# Frontier live build-swap/restart handoff

Status: `LIVE_BUILD_SWAP_RESTART_PUBLICLY_VERIFIED`

Live restart receipt SHA-256: `d16cd8c33d2a0af690aa902165266b103d6065603dd3a1a7334d811942d77cc1`
Live restart manifest SHA-256: `2ba25f70eba0893806e78746cc556b8699c0f8053034d83e84bffaad6614fc9b`
Gate C receipt SHA-256: `bfd9218df587c2ef7aaa92208c3925ad60c058dbbbd6a9c0a36f24adc66b3b88`

## Result

- Active build: `lFt_UDNPmeNh2DCabbYZX` (prior: `t-iRxR98ZKuZzWRYYpD8z`).
- Existing LaunchAgent `com.nebulamind.frontend` restarted once; shell PID 2538 → 43644; node listener PID 43646 on port 3000.
- Local and external Ranking routes verified; externally served chunk contains `1316 papers` and `674 papers`, with `1306 papers` and `661 papers` absent.
- Full-page visual capture shows the Ranking view, updated first two rows, contested-frontier and paper-merit sections, and no obvious rendering failure.
- Runtime old build is preserved byte-for-byte (cache excluded from digest) in `rollback-live-next`.

## Explicit scope note

Gate C preserved `LabStages.tsx` byte-identical. The deployed `FRONTIER_RANK_MOVEMENT` metadata is therefore not rendered as up/down indicators. That is not a restart failure; displaying it requires a separate explicit protected-UI gate.

## Runtime rollback — do not execute without fresh approval

Approval phrase:

`APPROVE FRONTIER LIVE RUNTIME ROLLBACK overnight-arxiv-frontier-preview-20260731T133649Z d16cd8c33d2a0af690aa902165266b103d6065603dd3a1a7334d811942d77cc1`

Then the guarded command is:

`/Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python -B /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/overnight-arxiv-frontier-preview-20260731T133649Z/product-gate/live-restart/rollback_live_restart.py --execute --live-receipt-sha d16cd8c33d2a0af690aa902165266b103d6065603dd3a1a7334d811942d77cc1`

This rolls back only the active runtime build and restarts the existing frontend LaunchAgent. Reverting the four Gate C source/canonical targets remains a separate fresh approval.

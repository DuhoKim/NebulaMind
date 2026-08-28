# Tori receipt — spin-parity private cockpit link corrected

- Marker: `TORI_SPIN_PRIVATE_COCKPIT_CORRECTION_RECEIPT_20260809T1916K`
- Authority: `DUHO_PRIVATE_COCKPIT_SPIN_LINK_CORRECTION_20260809T1913K`
- Hwao order: `HWAO_SPIN_PRIVATE_COCKPIT_CORRECTION_20260809T1915K`
- Executed: 2026-08-09 19:15 KST

## Result

The private cockpit now selects the accepted spin overhaul rather than the stale 2026-08-08 cut.

- Source: `spin-method-overhaul-canary-20260808T1959K.mp4`
- Private served copy: `spin-parity-census-narrated-20260809T1915.mp4`
- SHA-256: `c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240`
- Bytes: `16,065,978`
- Tailnet URL: <https://duho-macstudio.taila27502.ts.net/cockpit/videos/spin-parity-census-narrated-20260809T1915.mp4>

## Verification

- Source and destination at-rest hashes match exactly.
- Tailnet response: HTTP 200, `video/mp4`, 16,065,978 bytes.
- Served bytes were streamed and independently SHA-256 hashed; exact match to `c5e7deed…`.
- Live `ge-autopilot-status.json` selects `videos/spin-parity-census-narrated-20260809T1915.mp4`.
- Dashboard HTML watcher advanced automatically to 19:16:00 KST; no restart or manual render.
- The four sibling review links remain selected and unchanged.
- `published.json` remains SHA-256 `4abe62fbf2b9bf7a6e9f694a3fcbbe8313747a00184075fba8c5c49a190548e0`.
- The YouTube registry still truthfully points at the older `spin-parity-census-narrated-20260807T1903.mp4` unlisted upload; no upload/replacement occurred.
- Git HEAD remains `ebe9c7f587bfbdad30ea8cb62d42e51294e1599e`; cached diff remains empty.

## Safety ledger

Exactly one new private versioned MP4 copy. No overwrite; no stable-alias edit; no YouTube upload/replacement; no registry change; no renderer restart; no `frontend/public/videos`; no public Baseline; no product/DB/wiki/deploy/Git/browser/account/billing/config/secret action. Spin's existing Duho acceptance is unchanged, not newly asserted.

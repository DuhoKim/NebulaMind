# Duho correction — include current accepted spin-parity overhaul in private cockpit

- Marker: `DUHO_PRIVATE_COCKPIT_SPIN_LINK_CORRECTION_20260809T1913K`
- Recorded: 2026-08-09 19:13 KST
- User correction: `why spin parity video not updated?`

## Verified omission

The prior four-sibling publish order explicitly said `spin-parity is untouched`. That narrowed Duho's review publication too far. The dashboard still selects `spin-parity-census-narrated-20260808T0149.mp4` and its YouTube registry points to the older `20260807T1903` cut, while the current accepted overhaul exists at:

- Candidate: `integrator/canaries/spin-method-overhaul-canary-20260808T1959K/spin-method-overhaul-canary-20260808T1959K.mp4`
- SHA-256: `c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240`
- Bytes: `16,065,978`
- Duration: `187.695 s`
- Durable verdict: `HWAO_FINAL_VERDICT_c5e7deed.md` — ACCEPTED by Duho on 2026-08-09 (`accept it`).

## Corrected private-publish scope

Publish this exact accepted spin candidate as a new versioned private Tailnet cockpit copy using the established `spin-parity-census-narrated-<date-at-copy-time>.mp4` mechanism. Re-hash source and destination; let the existing watch-mode renderer select it automatically; verify the Tailnet served bytes and dashboard href.

Do not overwrite the stable alias, change `published.json`, replace or upload the YouTube video, restart/re-render, touch `frontend/public/videos`, alter the public Baseline, or perform product/DB/deploy/Git/browser/account/billing/config/secret actions.

The older YouTube link may remain visible and should truthfully appear as an older published cut; this correction is the private cockpit review link only.

Hwao issues the bounded correction order. Parent Tori executes and verifies; do not dispatch a duplicate writer.

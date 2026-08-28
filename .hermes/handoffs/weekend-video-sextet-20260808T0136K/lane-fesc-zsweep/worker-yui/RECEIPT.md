# Worker-Yui FESC lane receipt

## Outcome

`PASS_WITH_MINOR_INTEGRATION_REQUEST` for the v4 evidence/storyboard proposal.

`BLOCKED_AS_IS` for an official render from the current storyboard/current dark plot.

No official candidate, MP4, audio, TTS artifact, shared-tool edit, public mutation, or Git write was produced.

## Authority and write scope

Hwao's order and coordination update were read before post-order work. Pre-order artifacts under `../../lanes/fesc/` remain preserved. Every post-order write is under this official worker directory.

Hwao remains the sole integrator and candidate/shared-tool/TTS writer.

## Exact source decision

The frozen paper packet supports a local graphics proposal, but `video_reportable_now=false` for the current storyboard/plot because:

1. `z_c=8.045` is the closure-envelope crossing where the 16th-percentile Delta edge reaches zero, not the median required/inferred crossing. The median Delta crossing is `z_m=6.328`.
2. `z_c=7.615` belongs to a separate no-SFRD-tail run with one prior family removed and unpaired Monte Carlo draws. It is not an all-assumptions corner or paired one-variable counterfactual.

The current public MP4 remains unchanged at SHA-256 `840ced2b52c2007bc5387fc69b49527c548daca6f6d81b3f14bc9a43b7e9b5af` and fails because it is a stale, video-only, ten-card artifact with no inspectable evidence plot.

## Recommended worker packet

- `STORYBOARD_PROPOSAL.json` — SHA-256 `49db67e9c565eef6c8ec0f53bf348e8ecf1f581168507ce6eb2fa24c4a44c182`; eight continuous scenes, 98 seconds, 200 proposed narration words, approximately 122 WPM.
- `visual_proposal_v4/manifest.json` — SHA-256 `683460640960402716741303b38d833e1edece2a95806f912ba4c640f5f38622`.
- `visual_proposal_v4/static_states_contact_sheet.jpg` — SHA-256 `d3913812de4bf8a01c8ab9b875e1d5c2f2f4158d9200491402d4617c7d1d6fb7`.
- `REQUEST_TO_INTEGRATOR.md` — exact semantic and shared-renderer request.
- `PROVENANCE.md`, `SCIENTIFIC_CLAIM_MATRIX.md`, and `REPRESENTATION_BOUNDARY_AUDIT.md` — source and role boundaries.

v1–v3 remain preserved. v4 adds the escape-fraction definition, finite-Monte-Carlo 16–84% resampling labels, separate/unpaired no-tail-run disclosure, and a non-exhaustive model-boundary rail without changing source geometry.

## QA receipts

- Machine validation: `21/21 PASS`; SHA-256 `47302d860f3ac5d5087a9773feeec5900c0049fd8d55da9d303019eb603ae1f7`.
- Full-resolution visual review: PASS on the contact sheet and S01/S04/S05/S06/S07/S08 critical states; no clipping, collisions, internal audience paths, or source-role mismatch found.
- Adjacent-state difference: all seven pairs exceed the 0.5% changed-pixel floor; observed changed fractions are 2.271%–13.128%.
- Tesseract support check: PASS on v4 S01 and S04–S08 critical terms and values.
- Independent paper-naive review: PASS with terminology confusion; recovered the scientific question, crossing meaning, keyed percentages, separate no-tail change, model status, dominant limitation, and next test, but concrete proxies and “proxy transport” remain unspecified.
- Independent source-backed adversarial review: PASS; replayed the pipeline to `4.44e-16`, distinguished `z_c`/`z_m`, verified keyed fractions, confirmed separate/unpaired scenario status, finite-Monte-Carlo labels, model/no-measurement/non-exhaustive boundary, and proposal-only custody.
- Late v3 paper-naive review: MINOR. Most terminology findings were resolved by v4, but the S05 percentage markers remain positioned at median-Delta y-values and can imply that the curve itself encodes probability. See `LATE_V3_REVIEW_RECONCILIATION.md`.
- Late pre-v4 scientific review: MINOR after reproducing every core number. v4 resolved its finite-Monte-Carlo, non-exhaustive-boundary, and unpaired-run findings; surviving requests are exact root-to-displayed-curve geometry and a visible physical `f_esc=1` boundary.
- Late pre-v4 paper-naive review: MINOR for specialist shorthand; use compact first-use expansions or plain-language replacements in the integrated canary.
- Late compact v3 batch: paper-naive PASS; scientific BLOCK on preserved v3 because S07 looked exhaustive and S04/S06/S08 retained generic `bootstrap`/`ONE CHANGE` wording. Those blocking findings are resolved in v4 and introduce no new v4 blocker.
- Zero `.mp4`, `.wav`, or `.mp3` files exist in the official worker directory.

Detailed evidence is in `QA.md` and `qa/proposal/`.

## Gates deliberately left closed

- Storyboard-of-record modification.
- Shared plot/renderer modification.
- Official silent-canary render.
- TTS or audio generation.
- Narrated candidate render.
- Public MP4 replacement, upload, or publication.
- Website/cockpit, database, deployment, restart, or Git writes.

## Exact next action for Hwao

Accept or reject the two semantic corrections and four representation/disclosure requests in `REQUEST_TO_INTEGRATOR.md`. If accepted, integrate the v4 representation into Hwao-owned shared tooling: separate 66/83/93% from median-Delta coordinates, make fine roots exact on the displayed curves, show and explain the physical `f_esc=1` boundary, and expand specialist shorthand at first use. Then render a silent encoded canary. Before TTS, inspect encoded contact sheets and full-resolution S02/S04–S08-equivalent frames. Invoke Alloy at speed 1.18 only after that silent-canary pass and a fresh review of any changed narration.

This receipt does not authorize integration, TTS, publication, upload, or public replacement.

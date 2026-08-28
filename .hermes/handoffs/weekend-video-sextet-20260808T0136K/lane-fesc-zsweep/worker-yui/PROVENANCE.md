# Provenance — worker-Yui FESC review packet

## Scientific source of record

The proposal's quantitative geometry comes only from the frozen z-sweep model-output packet:

- `TREND_RESULTS.json` — SHA-256 `8df9f25b5f8acaf22825d6ece958867562c7e37a73fe69aa8e8175fe0b7aa242`
- `TREND_DATA.json` — SHA-256 `879b1e63de21caccddc952fe15113207f8785c6ca2932c8bb0844b992238dcb3`
- `MERGED_FESC_ZSWEEP.tex` — SHA-256 `22f5950b8bc35f70700df86a130ba7634bd74a88693e88496ae342caff9fbc5c`
- `fesc_zsweep_trend.png` — SHA-256 `10269f5f89b3d9a11365d5cb11f09f3dc62152d71fd26418affcb8c1db4f6b3c`

The exact freeze, review state, code/renderer hashes, and current-MP4 lineage are recorded in `SOURCE_FREEZE.json`.

## Visual proposal lineage

`visual_proposal_v4/` is the recommended deterministic static redraw from the frozen arrays. The worker script verifies the numeric-source hash before rendering and records an output hash for every 1920×1080 PNG in `visual_proposal_v4/manifest.json`.

Earlier v1–v3 proposals are preserved. v4 adds explicit finite-Monte-Carlo interval labeling, separate/unpaired no-tail-run status, a non-exhaustive model-boundary rail, and a plain-language escape-fraction definition without changing source geometry.

The redraw uses only source-recoverable elements:

- required and proxy-inferred 16th/50th/84th percentiles at each frozen grid redshift;
- Delta 16th/50th/84th percentiles;
- exact stored median and closure crossing values;
- exact stored bootstrap bounds;
- exact stored shortfall fractions, rounded to displayed percentages;
- exact no-SFRD-tail lower-edge curve and crossing.

No point, curve, band, uncertainty, or crossing value was generated, guessed, smoothed, or fetched from the web.

Late-review geometry note: the plotted curves connect frozen z=0.5 grid arrays, while crossing markers use separately stored fine-root values. Both are source-backed, but the marker and displayed coarse polyline are not mathematically identical at the zero crossing. Hwao must insert the fine roots into the plotted geometry or use one continuous/interpolated representation for both drawing and root finding.

## Audience-facing provenance

The proposed display line is:

“NebulaMind z-sweep model output (2026-08-04) · 40,000 draws per redshift · conditional on frozen low-z proxy anchors”

A persistent chip states:

“MODEL OUTPUT · NO NEW MEASUREMENT”

Repository paths, internal review filenames, and manuscript paths are intentionally absent from audience frames. Internal verification paths remain in `STORYBOARD_PROPOSAL.json` and this receipt only.

## Excluded assets

### Current dark video plot

`/Users/duhokim/HermesOps/cockpit/videos/plots/fesc-zsweep-photon-budget_trend.png` was inspected but excluded. It places `z=8.045` on a median required/inferred panel under “Where the two curves cross is the result,” although the median crossing is `z_m=6.328` and `z_c=8.045` is the 16th-percentile Delta-envelope crossing. It also omits the Delta panel, no-tail curve, and keyed shortfall values.

### Literature-context scatter

`/Users/duhokim/HermesOps/cockpit/videos/plots/lit_fesc.png` was inspected but excluded from the canary proposal. It is useful as heterogeneous literature context but does not establish a coherent measured redshift trend; introducing it would add provenance and interpretation work without helping the central closure-envelope argument.

### Manuscript cover/pages

The manuscript PDF and cover were excluded as presentation surfaces. They remain verification sources only.

## Rights and transformation status

The proposal contains a local deterministic redraw of NebulaMind's archived model output, not a third-party figure reproduction. No external photograph, generated scientific illustration, presenter image, manuscript screenshot, or face asset is used.

## Audio and candidate status

- Audio: none produced.
- TTS: not invoked.
- Narration: proposed text only in `STORYBOARD_PROPOSAL.json`.
- MP4: none produced by this official worker lane.
- Official candidate: none produced.
- Publication/upload: not authorized.

Hwao is the sole integrator and candidate/shared-tool/TTS writer under the coordination order.

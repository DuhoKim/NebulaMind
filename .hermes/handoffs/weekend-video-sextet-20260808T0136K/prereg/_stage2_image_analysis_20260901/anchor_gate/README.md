# Anchor gate V2

Status: **DRAFT ONLY, UNPINNED, SYNTHETIC FIXTURES ONLY.** Nothing here authorizes real-pixel access.

## Clause map

- `instrument_identity.py`: §§2.13, 7.10, 9.1–9.3, and 16.3. It recomputes the frozen instrument SHA-256, creates and closed-field-validates the environment record, and forms a canonical chained seal event by importing `canonical_bytes`, `_seal_predecessor`, and digest helpers from `seal_gate/seal_gate.py`.
- `bs4_anchor.py`: §§2.11–2.13, 8, and 10.1–10.3. Step (b) imports `render_cutout` from `study_renderer.renderer` and sends labelled N/E fiducials plus synthetic image, maskbits, and inverse-variance planes through the real rendering chain.
- `blind_guard.py`: §§2.5–2.6 and 15.3–15.5. Both protected catalogues are digest- and count-verified before comparisons. Identity and binary64 great-circle comparisons use the inclusive 1.0-arcsec boundary. The returned/printed receipt is formed before any downstream image path can be supplied; request path fields are forbidden.
- `test_anchor_gate.py`: synthetic refusal, boundary, literal-token, and real-format temporary journal-chain fixtures.

## Renderer integration

The synthetic anchor now executes `study_renderer.renderer.render_cutout`; no placeholder reprojection remains. Its receipt identifies that callable and incorporates the rendered synthetic raster digest.

## Not done

- No real image, FITS file, survey pixel, or image path was resolved or opened.
- No live journal is written unless a future operator explicitly passes `--append`; tests use a temporary byte-copy of the live seal journal.
- No preregistration, pin, acquisition artifact/journal, seal/completeness tooling, brick tree, or referee report is modified.
- This directory remains unpinned draft tooling.

The exact synthetic BS-4 command was run once during drafting and passed; its complete captured stdout is pasted in the drafting handoff.

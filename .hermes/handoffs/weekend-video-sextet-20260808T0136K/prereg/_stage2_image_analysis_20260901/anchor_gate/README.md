# Anchor gate draft V1

Status: **DRAFT ONLY, UNPINNED, SYNTHETIC FIXTURES ONLY.** Nothing here authorizes real-pixel access.

## Clause map

- `instrument_identity.py`: §§2.13, 7.10, 9.1–9.3, and 16.3. It recomputes the frozen instrument SHA-256, creates and closed-field-validates the environment record, and forms a canonical chained seal event by importing `canonical_bytes`, `_seal_predecessor`, and digest helpers from `seal_gate/seal_gate.py`.
- `bs4_anchor.py`: §§2.11–2.13, 8, and 10.1–10.3. Ordered execution is instrument identity, synthetic geometry, the exact frozen fixture subprocess command, then a BS-4 chained event. Every failure is `ABSOLUTE-ANCHOR-FAIL`.
- `blind_guard.py`: §§2.5–2.6 and 15.3–15.5. Both protected catalogues are digest- and count-verified before comparisons. Identity and binary64 great-circle comparisons use the inclusive 1.0-arcsec boundary. The returned/printed receipt is formed before any downstream image path can be supplied; request path fields are forbidden.
- `test_anchor_gate.py`: synthetic refusal, boundary, literal-token, and real-format temporary journal-chain fixtures.

## Renderer search report

The required search covered every file below `../_successor_build_20260824/gates/`, `ref/`, and `run/`, using both renderer/cutout/reprojection/planner filenames and code definitions/references for rendering, reprojection, `CRPIX`, stitching, bilinear interpolation, parity refusal, cutouts, and `plan_candidate_bricks`.

Result: **ABSENT.** There is no renderer or cutout planner implementation in those three trees, so there is no conforming pinned study-renderer path or SHA-256 to report. The search found prose references and the frozen verdict instrument, but no callable renderer/planner definition. Accordingly, `bs4_anchor.py` implements only `synthetic_wcs_reproject`, a minimal asymmetric labelled-N/E synthetic-WCS fiducial test. It is explicitly **NOT the study renderer** and must never be substituted for one.

## Not done

- No study renderer was found, implemented, claimed, or pinned.
- No real image, FITS file, survey pixel, or image path was resolved or opened.
- No live journal is written unless a future operator explicitly passes `--append`; tests use a temporary byte-copy of the live seal journal.
- No preregistration, pin, acquisition artifact/journal, seal/completeness tooling, brick tree, or referee report is modified.
- This directory remains unpinned draft tooling.

The exact synthetic BS-4 command was run once during drafting and passed; its complete captured stdout is pasted in the drafting handoff.

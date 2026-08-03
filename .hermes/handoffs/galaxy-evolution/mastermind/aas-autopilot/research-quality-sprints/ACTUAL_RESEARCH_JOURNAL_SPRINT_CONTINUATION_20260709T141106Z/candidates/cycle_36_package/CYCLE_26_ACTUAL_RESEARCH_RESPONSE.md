# Cycle 26 Actual Research Response

Changed in the candidate-copy TeX files only.

## What I changed
- Fixed the flagship abstract so the robustness variants are reported separately: `S/N >= 10` now maps to `-0.744 dex`, and the Seyfert-like subset remains `-0.763 dex`.
- Updated the flagship interpretation and conclusion text to keep those two robustness rows distinct.
- Added a literature citation for the aperture/morphology caveat with the review-supplied metadata: `\citep{bundy2015}` plus the matching bibliography entry.
- Rewrote the supplementary stellar-mass diagnostic so the mass range is expressed in standard log-mass notation, not as a shorthand `dex` label.

## What I refused
- I did not change any sample counts, offsets, confidence bounds, or the `60,000` cache cap.
- I did not add any new measured quantities, mock values, placeholder data, or invented citations.
- I did not alter the association-only scope boundary or the supplement’s role as a denominator/proxy atlas.

## Why
- The abstract had conflated two different robustness rows; that needed a direct correction to preserve traceability to Table 2.
- The mass-bin note needed standard astrophysical notation for clarity and compile-safe prose.
- The aperture/morphology caveat was strengthened using a review-verified public source, without changing the manuscript’s real-data-only constraints.

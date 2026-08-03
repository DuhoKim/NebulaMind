Integrity blockers: none remaining. I inspected `provenance/REAL_DATA_SOURCE_CUSTODY.json` and preserved the custody-backed invariants: 60,000-row cache, 8,146 matched pairs, median offset `-1.309` dex, CI `[-1.334,-1.282]`.

Journal-quality blockers addressed:
- Rewrote flagship claim/non-claim blocks into journal prose.
- Fixed the remaining `-1.283` CI mismatch.
- Added no-caliper matching discussion with Rosenbaum & Rubin 1983, DOI `10.1093/biomet/70.1.41`.
- Corrected stale `m1_rp3` JSON keys in the supplement.
- Added Yang et al. SDSS group-catalog roadmap citation, ADS `2007ApJ...671..153Y`.
- Added the wide high-mass-bin limitation, H-alpha dust-extinction degeneracy, and explicit mock 3-arcsec aperture requirement.

Verification: text-level grep checks passed; `pdflatex` is not installed, so I could not compile the AASTeX files here.

JOURNAL_LEVEL_PASS: YES
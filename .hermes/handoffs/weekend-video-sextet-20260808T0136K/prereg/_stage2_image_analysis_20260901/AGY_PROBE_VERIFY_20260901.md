# R-C Probe Verification Audit

## 1. Scope Compliance
Exactly one FITS file (`legacysurvey-0489m442-image-r.fits.fz`) was downloaded and is present in the `probe/` directory. The transcript confirms only metadata/catalog TAP queries were made over the network (to resolve the brick ID to a brick name, and to fetch NERSC directory listings and checksums), followed by a single `curl` command to download the specified `.fits.fz` file. No second image file or second brick was downloaded. The probe stayed strictly within the one-brick boundary.

## 2. No Science Pixels
The transcript shows only metadata and structural queries using `astropy.io.fits`, specifically `fits.open` with `mode='readonly'` and `disable_image_compression=True`. The code iterated over HDUs and read headers and `shape` properties but never accessed `.data` or performed any computations. A search for pixel statistics (min, max, mean, std, median, histogram, percentile, sum), plotting, or numpy arrays yielded zero results on pixel values. No science pixels were interpreted. The boundary held.

## 3. Integrity
The published SHA-256 in `legacysurvey_dr10_south_coadd_048_0489m442.sha256sum` is `7c461a5f4d63547d16b552085584661fe452da50ed6013ac30bed63d6dca3486`. Recomputing the SHA-256 of the downloaded file `probe/legacysurvey-0489m442-image-r.fits.fz` yields exactly `7c461a5f4d63547d16b552085584661fe452da50ed6013ac30bed63d6dca3486`. The receipt honestly and correctly reports a MATCH.

## 4. Blindness
The content-blind rule was stated prior to downloading: "bytewise-lexicographically sort the newline-delimited IDs in the frozen `../_successor_build_20260824/acquire/selected_brickids_cut.txt`; select the first ID; resolve that ID to `brickname` using catalogue naming metadata only". This rule is purely structural and objective. Verifying this against the frozen list (`sort selected_brickids_cut.txt | head -n 1`) yields `100048`, which corresponds via TAP metadata to `0489m442`. The rule is valid, content-blind, and correctly executed.

## 5. Receipt Completeness
The receipt (`R_C_PROBE_RECEIPT_20260901.md`) is complete. It delivers the precise format contract (HDU inventory, verbatim WCS and compression header cards, BUNIT, dtype, and shape dimensions). It includes an explicit and detailed "Read / not-read declaration" affirming what was intentionally ignored (including statistics, plots, and companion files). It also details a robust list of "Questions still open", maintaining the boundary that a single probe cannot establish population invariance or valid-pixel coverage.

## 6. Usefulness
The pinned contract successfully specifies BS-9's required input function behaviors: expecting a 2-D `(3600, 3600)` float32 array in NumPy `(y, x)` order from `CompImageHDU` (HDU 1), recognizing the `RA---TAN`/`DEC--TAN` WCS via CD matrix, and verifying the `nanomaggy` units.
It also firmly grounds R-B's geometry proposal by extracting the exact pixel scale (`0.262 arcsec/pixel`), diagnosing the half-pixel WCS reference alignment (`1800.5, 1800.5`), and observing the north-up axis-alignment.

**Still Missing:**
While the probe provided structural geometry, it notes that actual data coverage, artifact locations, or invalid edges within the `3600 x 3600` grid cannot be determined without reading the mask/inverse-variance companion files (which was forbidden here). BS-9 also still requires a defined edge-padding behavior, and R-B must still choose the exact cutout sizes, interpolation kernel, and half-pixel rounding rules. Population invariance across other bricks is also unproven by a single sample.

SEAT: AGY
VERSION: PROBE-VERIFY-V1
VERDICT: SOUND
COUNT: 0
F-lines: NONE

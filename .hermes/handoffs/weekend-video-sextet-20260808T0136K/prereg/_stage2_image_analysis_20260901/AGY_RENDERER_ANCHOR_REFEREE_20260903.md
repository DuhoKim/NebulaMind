# RENDERER FINDINGS

**R1** (Severity: High, file: study_renderer/renderer.py:89, clause: §8.13)
The renderer hard-codes `PINNED_GEOMETRY` and never reads the pinned `miniprereg_pins/render_config.json` file. The specification strictly requires that the prose constants agree exactly with the pinned configuration file, and that any disagreement refuses the run before pixel access.
**Repair**: Load `miniprereg_pins/render_config.json` directly during initialization and compare its contents against the required geometry, refusing on any mismatch.

**R2** (Severity: High, file: study_renderer/renderer.py:138, clause: §8.7)
The effective source-to-output Jacobian is computed numerically at only the exact center of the tile `(w - 1) / 2, (h - 1) / 2`. A malicious or heavily distorted WCS could flip parity at the raster edges while maintaining correct parity at the center, escaping this refusal.
**Repair**: Compute and assert the Jacobian parity at all four corners of the tile in addition to the center.

**R3** (Severity: Critical, file: study_renderer/renderer.py:198, clause: §8.12)
The renderer currently only processes a single `np.ndarray` for the image and does not handle `maskbits` or `inverse-variance` arrays at all. The specification mandates that every output pixel requires valid image, maskbits, and inverse-variance coverage, and any missing/non-finite value must yield `DATA-INTEGRITY-FAIL`.
**Repair**: Modify `render_cutout` and its signature to accept, stitch, and validate `maskbits` and `inverse-variance` arrays alongside the primary image array.

**R4** (Severity: Medium, file: study_renderer/test_study_renderer.py:38, clause: Tests)
Missing test cases: edge-of-raster parity flip, RA wrap at 0/360, Dec near ±90, empty tile list, NaN in a tile, and tiles with inconsistent pixel scales.
**Repair**: Add the missing test cases to `StudyRendererTests` to ensure these edge cases are explicitly handled and tested.

# ANCHOR GATE FINDINGS

**A1** (Severity: Critical, file: anchor_gate/bs4_anchor.py:28, clause: §10.1)
The BS-4 anchor uses a placeholder `synthetic_wcs_reproject` that explicitly returns `"renderer": "ABSENT; synthetic-WCS reference only"`. It is not wired to run through the pinned rendering chain as mandated by the absolute-sign anchor spec.
**Repair**: Import `render_cutout` from `study_renderer.renderer` and execute the actual renderer within the anchor instead of relying on the placeholder.

**A2** (Severity: Low, file: anchor_gate/blind_guard.py:23, clause: §15.4)
The `separation_arcsec` function is duplicated from `completeness_gate.py` and is not byte-identical (type annotations and the unused `cd` calculation were removed).
**Repair**: Remove the duplicated `separation_arcsec` definition from `blind_guard.py` and import it directly from `completeness_gate.completeness_gate`.

**A3** (Severity: Medium, file: anchor_gate/test_anchor_gate.py:51, clause: Tests)
The blind guard test suite tests an object exactly 1.0 arcsec away and one binary64 step outside, but misses the critical test case for a coordinate exactly one binary64 step INSIDE 1.0 arcsec.
**Repair**: Add a test case using `math.nextafter(1.0 / 3600.0, -math.inf)` to verify the guard strictly refuses an object exactly one step inside the 1.0 arcsec boundary.

SEAT: AGY
VERSION: RENDERER-ANCHOR-REFEREE-V1
RENDERER_VERDICT: PINNABLE-AFTER-REPAIRS
ANCHOR_GATE_VERDICT: PINNABLE-AFTER-REPAIRS
BS4_FIXTURES: PASS
COUNT: 7

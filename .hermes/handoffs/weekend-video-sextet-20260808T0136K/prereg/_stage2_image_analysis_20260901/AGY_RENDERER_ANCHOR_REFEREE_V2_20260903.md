# RENDERER FINDINGS

**TASK A — CLOSURE**
* **R1**: CLOSED. The renderer reads `miniprereg_pins/render_config.json` directly at initialization (`_loaded_geometry = json.loads(_CONFIG.read_text...)`), compares its contents field-for-field against the required `_SECTION8_GEOMETRY`, and refuses on mismatch with the token `CONFIG_GEOMETRY_MISMATCH = "PINNED-CONFIG-MISMATCH"`.
* **R2**: CLOSED. The Jacobian parity is asserted at the center, the four corners, and the four edge centers (9 points total). Any disagreement (non-positive determinant or inconsistent sign) raises a `ValueError` with `WRONG_PARITY_REFUSAL`.
* **R3**: CLOSED. The `render_cutout` signature accepts `Sequence[tuple[np.ndarray, np.ndarray, np.ndarray, WCS]]` and stitches the image, maskbits, and inverse-variance arrays identically. Any missing or non-finite values across the three planes correctly raise a `ValueError` with `DATA_INTEGRITY_FAIL`.
* **R4**: CLOSED. The test suite includes 7 added tests asserting exact refusal strings for: edge-of-raster parity flip, RA wrap at 0/360, Dec near ±90, empty tile list, NaN in a tile, inconsistent pixel scales, and missing maskbits/invvar.

**TASK B — REGRESSION SWEEP**
No regressions found. The renderer remains in-memory, deterministic, and free of real FITS files or disk I/O outside of the config load. Clauses §8.1-8.13, §9, §10, §15, §16.3 are respected.

---

# ANCHOR GATE FINDINGS

**TASK A — CLOSURE**
* **A1**: CLOSED. `anchor_gate/bs4_anchor.py` imports `render_cutout` and runs it with synthetic three-plane tiles, actively checking the renderer's orientation logic rather than relying on a placeholder.
* **A2**: CLOSED. The duplicate `separation_arcsec` function is removed from `blind_guard.py`, and it is now imported directly from `completeness_gate.completeness_gate`.
* **A3**: CLOSED. `test_anchor_gate.py` includes a test case `test_blind_guard_one_step_inside_refuses` using `math.nextafter(1./3600., -math.inf)`, which correctly ensures the guard strictly refuses objects exactly one binary64 step inside the boundary.

**TASK B — REGRESSION SWEEP**
No regressions found. Blind guard strictly enforces the exact boundary, instrument identity validates identically, and BS-4 runs as specified.

---

SEAT: AGY
VERSION: RENDERER-ANCHOR-REFEREE-V2
RENDERER_VERDICT: PINNABLE
ANCHOR_GATE_VERDICT: PINNABLE
BS4_FIXTURES: PASS
COUNT: 0

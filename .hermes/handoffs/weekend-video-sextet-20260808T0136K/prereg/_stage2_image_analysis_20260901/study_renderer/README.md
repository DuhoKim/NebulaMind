# Study renderer draft V1

Status: **DRAFT ONLY, UNPINNED, SYNTHETIC TESTS ONLY.** This directory does not authorize real-pixel access.

## Implemented clause map (quoted)

- V10 §8.1: “Each scientific raster is exactly 128 by 128 pixels … at 0.262 arcsecond per pixel.”
- §§8.2–8.4: “The output is a TAN WCS centered on the exact catalogue `(RA, Dec)` parsed as binary64”; `CRPIX1=CRPIX2=64.5`; and “`CD1_1=-0.262/3600`, `CD1_2=0`, `CD2_1=0`, `CD2_2=+0.262/3600`.”
- §§8.5–8.7: “north-up and east-left”; “Parity is strictly preserved”; wrong effective source-to-output parity yields literal `WRONG-PARITY-REFUSAL` and is never corrected.
- §§8.8–8.9: “All required neighbouring bricks are stitched before reprojection” and “Exactly one deterministic bilinear reprojection maps the stitched inputs to the output WCS.”
- V10 §8.10 (the prompt called this §8.12): “Resizing, further interpolation, rotation, transpose, PSF homogenization, padding, wrapping, reflection, intensity-conditioned source choice, and chirality-conditioned processing are prohibited.” None is implemented.
- §8.12: every output pixel requires valid coverage; missing/non-finite supplied image coverage produces `DATA-INTEGRITY-FAIL`. Maskbits and inverse variance are outside this image-only function's input contract and remain a caller/seal-gate responsibility.
- §8.13: prose and pinned configuration must agree. The draft exposes the frozen request fields, and any requested deviation yields `WRONG-GEOMETRY-REFUSAL` (the prompt-specified draft token; V10 does not name a geometry token).
- §9.4 defines `chi(x) = (w(x) - w(mirror(x)))/2`; this renderer returns the one unmirrored raster from which the instrument must make its exact mirror. §9.7 requires identical reruns to reproduce binary64 `chi` bytes; the renderer itself is tested for byte-identical canonical binary64 raster output.
- §§15.3–15.4 require the exclusion receipt and inclusive 1.0-arcsec protected guard before a pixel path is resolved or opened. This renderer cannot resolve or open paths and must only be called after that gate.
- §16.3 requires every render to be entered in the chained seal journal. Journaling is deliberately a caller responsibility because this function is pure.
- Parent V134 §2.6: “Each galaxy's cutout can require neighbouring bricks outside the selection”; and “assuming the manifest equals the selection is the exact defect BS-2m exists to catch.” The API therefore consumes every tile supplied by the caller and records all tile identifiers.

## Interface and limits

`render_cutout(sources, target) -> Raster` accepts `(image array, astropy.wcs.WCS)` pairs and `(ra, dec)`. It never imports FITS support, touches disk, resolves a neighbour, handles a path, chooses a brick manifest, opens maskbits/inverse-variance products, mirrors an instrument input, invokes the instrument, or writes a journal. The caller owns all of those gates and records. Canonical raster bytes are little-endian float64 in C order; the returned digest is their SHA-256. Metadata contains every frozen constant, tile IDs, Jacobian sign, digest, and Astropy version.

V10 §8.9 also says binary64 accumulation is “materialized once as float32,” whereas the drafting request explicitly requires canonical raster bytes to be float64. This unpinned draft follows the explicit requested float64 output and records that fact for referee resolution before pinning.

## Future BS-4 step (b) integration

After referee approval and pinning, `anchor_gate/bs4_anchor.py` step (b) can import `study_renderer.renderer.render_cutout`, pass its already-created asymmetric in-memory synthetic tile/WCS and target coordinate, assert the returned N/E fiducials and `source_to_output_jacobian_sign`, then feed `Raster.array` to the frozen instrument. A deliberately wrong-parity synthetic WCS must raise exactly `ValueError("WRONG-PARITY-REFUSAL")`. The gate must additionally seal this module's digest, its environment record (including Astropy), synthetic input/output digests, and PASS before any real image is opened.

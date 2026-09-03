# Study renderer V2

Status: **DRAFT ONLY, UNPINNED, SYNTHETIC TESTS ONLY.** This directory does not authorize real-pixel access.

## Implemented clause map (quoted)

- V10 §8.1: “Each scientific raster is exactly 128 by 128 pixels … at 0.262 arcsecond per pixel.”
- §§8.2–8.4: “The output is a TAN WCS centered on the exact catalogue `(RA, Dec)` parsed as binary64”; `CRPIX1=CRPIX2=64.5`; and “`CD1_1=-0.262/3600`, `CD1_2=0`, `CD2_1=0`, `CD2_2=+0.262/3600`.”
- §§8.5–8.7: “north-up and east-left”; “Parity is strictly preserved”; wrong effective source-to-output parity yields literal `WRONG-PARITY-REFUSAL` and is never corrected.
- §§8.8–8.9: “All required neighbouring bricks are stitched before reprojection” and “Exactly one deterministic bilinear reprojection maps the stitched inputs to the output WCS.”
- V10 §8.10 (the prompt called this §8.12): “Resizing, further interpolation, rotation, transpose, PSF homogenization, padding, wrapping, reflection, intensity-conditioned source choice, and chirality-conditioned processing are prohibited.” None is implemented.
- §8.12: image, maskbits, and inverse-variance planes are stitched identically. Every output pixel requires finite coverage in all three; a missing plane or missing/non-finite value refuses the whole study with `DATA-INTEGRITY-FAIL`.
- §8.13: initialization reads `miniprereg_pins/render_config.json` and compares every field with the §8 constants before geometry is used. Missing, malformed, extra, or disagreeing configuration refuses with literal `PINNED-CONFIG-MISMATCH`. A target-request deviation yields `WRONG-GEOMETRY-REFUSAL`.
- §9.4 defines `chi(x) = (w(x) - w(mirror(x)))/2`; this renderer returns the one unmirrored raster from which the instrument must make its exact mirror. §9.7 requires identical reruns to reproduce binary64 `chi` bytes; the renderer itself is tested for byte-identical canonical binary64 raster output.
- §§15.3–15.4 require the exclusion receipt and inclusive 1.0-arcsec protected guard before a pixel path is resolved or opened. This renderer cannot resolve or open paths and must only be called after that gate.
- §16.3 requires every render to be entered in the chained seal journal. Journaling is deliberately a caller responsibility because this function is pure.
- Parent V134 §2.6: “Each galaxy's cutout can require neighbouring bricks outside the selection”; and “assuming the manifest equals the selection is the exact defect BS-2m exists to catch.” The API therefore consumes every tile supplied by the caller and records all tile identifiers.

## Interface and limits

`render_cutout(sources, target) -> Raster` accepts `(image, maskbits, inverse_variance, astropy.wcs.WCS)` tuples and `(ra, dec)`. It never imports FITS support or touches acquisition files. Canonical image raster bytes are little-endian float64 in C order; the result also exposes the stitched maskbits and inverse-variance rasters.

The current Tier-C acquisition holds **only 17,947 image-r files**. Required maskbits and inverse-variance companions are a separate acquisition (Hwao is raising this with the principal). Until all companions are supplied, the renderer refuses; it never invents, substitutes, or infers a plane.

V10 §8.9 also says binary64 accumulation is “materialized once as float32,” whereas the drafting request explicitly requires canonical raster bytes to be float64. This unpinned draft follows the explicit requested float64 output and records that fact for referee resolution before pinning.

BS-4 step (b) imports this renderer and passes asymmetric synthetic N/E fiducials with all three synthetic planes through it. A deliberately wrong-parity WCS must refuse with `WRONG-PARITY-REFUSAL`.

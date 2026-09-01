# CODEX R-band cutout geometry proposal — 2026-09-01

## Status and ground

This is a proposal for Duho to ratify under direction #33, not a freeze. Pixel scale remains **FROZEN at 0.262 arcsec/pixel**.

The real structural ground is the one authorized probe receipt: the R-band coadd is a `(3600, 3600)` logical float32 image, compressed as `RICE_ONE` in `100 × 100` tiles, with a TAN WCS, `CRPIX1 = CRPIX2 = 1800.5`, `CD1_1 = -0.262/3600 deg/pixel`, `CD2_2 = +0.262/3600 deg/pixel`, and separate maskbits and R-band inverse-variance companions. No pixel values or statistics were read. A brick spans 943.2 arcsec = 15.72 arcmin per side.

The decisive frozen constraint is in `successor_ref_v9.py`: `CUTOUT_PIX = 128`, explicitly called the frozen tensor side, `IC6_SHAPE = (1, 128, 128)`. The prohibited predecessor runner was read only to understand prior geometry; none of its science outputs or implementation is adopted merely because it existed.

## 1. Size

**Proposal: 128 × 128 pixels.** This is not a free optimization: the frozen successor instrument requires it. At 0.262 arcsec/pixel the side is **33.536 arcsec** (0.559 arcmin), with a nominal half-width of 16.768 arcsec.

The catalogue cut `shape_r > 1.5 arcsec` means the minimum selected scale is 5.73 pixels. If `shape_r` is interpreted as the fitted radial scale, a minimum-scale object's diameter of twice that value occupies about 11.45 pixels, or 8.9% of the cutout width; its radial scale occupies 4.5%. This leaves substantial sky/context and room for larger galaxies, while the minimum object is not generously sampled for human spiral-arm judgment. That human-visibility limitation is real, but it cannot justify changing the tensor geometry after the instrument freeze. A human display may magnify pixels without changing or interpolating the scientific raster.

Using the frozen 128-pixel footprint planner and the frozen retained position table, **7,226/49,211 = 14.684%** of retained objects need more than one candidate brick: 6,679 need two, 467 need three, and 80 need four. The remaining 41,985 need one. This is the operational seam exposure; it is more relevant than a uniform-area approximation because it is evaluated on the actual retained catalogue positions and official catalogue brick geometry, without image pixels.

One raw float32 tensor is 65,536 bytes. For 49,211 objects the science tensors alone are **3,225,092,096 bytes = 3.00 GiB** before FITS headers, checksums, receipts, coverage, maskbits, inverse variance, temporary arrays, or compression. Doubling the side would quadruple this volume and violate the frozen model input.

Tradeoff: 128 is relatively context-rich but makes the smallest allowed galaxies only about 11 pixels across under the twice-`shape_r` illustration. The remedy is eligibility/hand-check calibration, not a post-freeze resize.

## 2. Centering

**Proposal: exact celestial centering on the catalogue `(ra, dec)` using an even-sized output TAN WCS.** Define the output FITS WCS by

- `NAXIS1 = NAXIS2 = 128`;
- `CRVAL1 = ra`, `CRVAL2 = dec`, using the catalogue float values as parsed to IEEE-754 binary64;
- `CRPIX1 = CRPIX2 = 64.5` in the FITS one-based, pixel-center convention;
- `CD1_1 = -0.262/3600`, `CD1_2 = 0`, `CD2_1 = 0`, `CD2_2 = +0.262/3600` degrees/pixel.

Thus the object lies at the geometric center, the corner shared by the four central pixels—not at an integer pixel center. Output pixel centers are evaluated at FITS coordinates `(x, y) = (1..128, 1..128)`. There is **no rounding of the object position to a source pixel**. Each output pixel center is transformed output-pixel → sky → source-pixel in binary64 through the stated TAN WCS. This convention removes the otherwise unavoidable one-half-pixel asymmetry of putting an object on one central pixel in an even array and is precise enough for two conforming implementations to address the same samples.

Tradeoff: exact centering requires resampling because catalogue positions are generally subpixel and neighboring TAN planes are not one common integer lattice. The alternative integer-only rule would have to round the source coordinate and choose an asymmetric half-open window; it would move each object by up to roughly 0.185 arcsec radially and would not provide exact common-grid stitching.

## 3. Rotation and parity

**Proposal: no object-dependent rotation.** Preserve **north up, east left** with the CD matrix above. Do not rotate to a galaxy position angle, brick angle, or local morphology.

A proper rotation has determinant `+1` and does not flip chirality; a reflection has determinant `-1` and does. For a handedness measurement, every WCS transform, array-axis conversion, display, and model input must preserve the declared parity. East-left is achieved by the negative RA-axis CD term, not by an undocumented array reflection. The instrument's explicit left-right mirror remains the only chirality-changing transform. Any implementation whose effective source-to-output Jacobian has the opposite parity must refuse the cutout rather than silently flip it.

Tradeoff: no rotation leaves galaxies at arbitrary position angles, but avoids morphology-conditioned preprocessing and interpolation variation.

## 4. Resampling

**Proposal: prohibit all resizing, rotation, PSF homogenization, and discretionary interpolation, but permit exactly one geometry-mandated deterministic bilinear reprojection onto the output WCS defined above.** This is the narrow exception forced by exact celestial centering and seamless use of neighboring TAN bricks.

For reproducibility, use source FITS pixel-center coordinates; for a mapped source coordinate `(sx, sy)`, set zero-based `fx = sx - 1`, `fy = sy - 1`, `x0 = floor(fx)`, `y0 = floor(fy)`, `x1 = min(x0 + 1, 3599)`, `y1 = min(y0 + 1, 3599)`, and the ordinary four bilinear weights from the fractional parts. Accumulate in binary64 and materialize the delivered raster once as float32. A source contributes only when the output pixel center maps inside its pixel-center support `[1, 3600] × [1, 3600]`. Where multiple valid bricks cover an output pixel, combine them by the separately ratified companion-aware rule; do not choose a brick based on image intensity or inferred handedness.

Interpolation is not scientifically neutral: bilinear sampling is a low-pass, phase-dependent operation that attenuates high-spatial-frequency arm contrast and can alter a weak chirality score. It should not create a reflection by itself, but position-dependent sampling or parity mistakes could couple to handedness. Therefore the identical reprojection must be applied before both `x` and the instrument's exact mirror of `x`; never reproject the mirrored branch separately.

Alternative for Duho's consideration: nearest-integer, no-interpolation home-brick cuts. Cost: loss of exact centering, a fixed half-pixel asymmetry for an even side, no principled seam mosaic across different TAN WCSs, and likely exclusion of the 7,226 seam-exposed objects. I do **not** recommend it.

## 5. Edge and coverage policy

**Proposal: stitch all planned neighboring bricks first; exclude only if the complete 128 × 128 raster still cannot be formed with valid required coverage and companions.** The frozen preregistration is explicit that the parent's cutout geometry defines a required brick set **including neighbor bricks at footprint edges**, and its measured closure is frozen. Consequently, a home-brick boundary is not reason (b). Treating every seam crossing as “incomplete” would contradict that closure and discard up to the 7,226 seam-exposed retained objects before testing actual coverage.

For every output pixel, consult every brick selected by the frozen planner. A cutout is complete only when every one of its 16,384 output pixels has the required R image, maskbits, and inverse-variance evidence under the eventual companion-validity contract. Overlap handling must be deterministic and companion-aware, with no intensity- or chirality-conditioned choice. If a required neighbor is missing, fails byte integrity, has rejected WCS/parity, or the union of valid inputs leaves any required output pixel uncovered, retry under the frozen acquisition rule; after terminal failure record the applicable frozen reason: (a) missing/integrity failure, or (b) incomplete at `(1,128,128)`. Do not pad, reflect, wrap, shrink, or substitute zeros to manufacture geometric completeness. Any later invalid-pixel allowance belongs to the separately frozen input contract and must not be used to relabel absent sky coverage as complete.

Tradeoff: stitching costs more I/O and requires companion-aware overlap semantics, but preserves the frozen population and is exactly why closure includes neighbors.

## Recommended set for ratification

1. **Size:** 128 × 128 pixels = 33.536 × 33.536 arcsec.
2. **Centering:** exact catalogue sky position at output `CRPIX=(64.5,64.5)` in the FITS one-based pixel-center convention; no coordinate rounding.
3. **Rotation:** none; fixed north-up/east-left TAN WCS and parity-preserving transforms only.
4. **Resampling:** one deterministic bilinear WCS reprojection only; all other resampling prohibited.
5. **Edges/coverage:** stitch frozen-planner neighbors; exclude only after the full tensor and required companion coverage cannot be completed under frozen retry/integrity rules.

## Still open; requires later authorization or a separate ratification

- The real distribution of `shape_r`, visual arm visibility, backgrounds, masks, inverse variance, and interpolation effects cannot be assessed without reading additional catalogue fields or pixel values. No such read was performed here.
- Exact companion-validity predicates and the deterministic rule for combining genuinely overlapping valid bricks must be frozen before production. The structural receipt proves the companions exist separately but contains no companion bytes or schemas.
- Bit-for-bit numerical equality also requires pinning the TAN transform implementation/library and floating-point execution environment; the coordinate convention above fixes geometry but does not by itself standardize transcendental rounding across libraries.
- Whether bilinear reprojection measurably attenuates the frozen instrument's chirality response needs authorized, handedness-blind validation data. No real-image statistic is inferred from structure alone.

SEAT: CODEX
VERSION: GEOM-V1
VERDICT: PROPOSED
COUNT: 5

# YUI synthetic boundary fixtures — 2026-08-15

Status: **BUILT AND SELF-TESTED; ADAPTER NOT TESTED; ROUTE STILL CLOSED**

## Purpose

These fixtures make Tori's written §6 boundary rule executable as an adapter-independent synthetic contract. They are intentionally not derived from her parallel implementation. A later adapter comparison should consume `generated/fixture_manifest.json`, `generated/objects.json`, the synthetic FITS bricks, and the exact expected arrays. A disagreement is a gate failure to investigate, not a reason to rewrite the fixtures around the adapter.

The defect under test is a shape-correct but incomplete cutout. Every expected pixel is therefore value-coded. A `128 × 128` result passes only if all 16,384 float32 values agree with the analytic sky-plane expectation within absolute tolerance `5e-6`, source-set custody closes, and coverage contains no zero.

## Fixture geometry

The corpus is a 3 × 3 synthetic brick grid:

- source image size: exactly `3600 × 3600`;
- output size: exactly `128 × 128`;
- pixel scale: exactly `0.262 arcsec/pixel`;
- source-grid stride: 3472 pixels;
- source overlap: 128 pixels;
- projection: shared, non-rotated TAN with North up and East left;
- image plane: float32, HDU 1, synthetic nanomaggy-labelled values;
- compression: lossless GZIP_2 FITS tile compression with no float quantization.

The sources share one TAN plane, while every object uses the exact object-centred output TAN WCS written by Tori §7.2. Output pixel centres and the nine boundary points are independently projected back into the common source plane. Pixels at the same projected global coordinate have the same analytic value in every overlapping brick. Thus source-order changes cannot alter the expected image, while a shifted read, wrong local crop, missing strip, or zero pad does alter it.

The value function is recorded in the manifest and is strictly positive: `float32(20 + global_y*0.002 + global_x*0.0001)`. Independent x/y slopes make both shift directions visible while remaining exactly replayable by linear interpolation to float precision. Expected arrays are sealed by SHA-256, and every object row contains five exact float32 bit probes.

## Source-selection oracle

Each source and output has a nine-point pixel-edge polygon: four corners, four edge midpoints, and the repeated starting corner required by Tori §6. Source rectangles and the object-centred output polygon are projected into the common TAN plane, and the independent oracle applies a convex positive-area intersection test. This is geometric fixture code, not Tori's adapter.

The overlap rule does not pick one preferred brick. It deterministically includes **all** intersecting source bricks and records the sorted set plus its SHA-256 signature. The fixture stitcher accepts reversed input order and proves identical output bytes. This is consistent with the written distinction between candidate, planned-intersecting, opened, contributing, and zero-pixel-touch sets.

A catalogue-style primary brick is never treated as a sufficient source set.

## Covered matrix

There are 29 object rows:

- 1 centre control;
- 20 edge rows: north, south, east, west × no-neighbour, overlap-only, within 63 pixels, exact unique edge, and one pixel beyond;
- 4 exact unique-area corners;
- 4 one-pixel-beyond corner stress rows.

The overlap-only rows are the key scalar-margin counterexample: their output footprints do not cross the unique-area edge, yet they intersect an adjacent source image and therefore require that source in the planned set.

The eight beyond-edge/corner stress rows deliberately run a broken primary-only crop with silent zero padding. Each broken array has the requested shape and each fails the full value comparison. Corner stress cases detect loss on both axes, not merely one truncated strip.

Missing required neighbour and required-source digest mutation are terminal before output creation. Successful outputs report coverage minimum at least one and zero uncovered pixels.

## Adapter handoff contract

A later adapter check should, per object:

1. read RA/Dec and the exact output-WCS fields from `objects.json`;
2. independently compute candidate and intersecting source sets from the synthetic FITS WCSs;
3. require equality with `expected_bricks` and `source_set_signature_sha256`;
4. render without normalization, clipping, resize, rotation, or padding;
5. compare shape and dtype;
6. compare the complete float32 array with `expected/<object_id>.npy` at absolute tolerance `5e-6` and zero relative tolerance, reporting maximum absolute error, first out-of-tolerance pixel, and total mismatch count;
7. compare planned/opened/contributing/zero-touch sets and coverage hash;
8. run again with source order reversed;
9. remove one required edge and one required diagonal file, independently, and require terminal failure with no accepted output.

These instructions describe the fixture contract only. They do not import, patch, or bless Tori's implementation.

## What this proves

- The synthetic source-set oracle distinguishes centre, no-neighbour, overlap-only, edge, exact-boundary, and four-way corner geometry.
- A complete output can be checked pixel-for-pixel against known nonzero values.
- A correctly shaped truncated or zero-padded output is detectable.
- Source ordering does not change the oracle output.
- Missing and digest-mismatched planned neighbours fail before output acceptance.
- The fixture files and expectations are reproducible offline from one script.

## What this does not prove

- It does **not** test Tori's adapter; that code was not read, imported, or executed.
- It does not prove the pinned Imagine `bricks_touching_aa_wcs`, `polygons_intersect`, resampler, interpolation, weight accumulation, or multiprocessing implementation.
- The synthetic sources use one shared tangent plane; the outputs are correctly object-centred TAN projections. This still does not reproduce distinct real per-brick tangent points, the irregular South brick grid, or all real edge-touch semantics.
- The 128-pixel synthetic overlap is a controlled approximation to the brief's approximately 130-pixel overlap, not a claim about any particular DR10 brick pair.
- It does not cover the separate §8.3 RA-wrap, selected-footprint declination-extreme, legitimate three-source T-junction, or multiprocessing-scheduling fixtures. Those remain adapter/geometry-suite obligations.
- It does not cover PC-4's complete distorted/malformed WCS-header rejection matrix; only required-file absence and byte-digest mismatch are exercised here.
- It does not prove production FITS compression, astrometry.net, legacypipe, fitsio, dependency/container determinism, real source hashes, or real output parity.
- Synthetic global-pattern agreement across overlaps deliberately removes inter-source photometric disagreement; it tests completeness and order invariance, not production overlap weighting differences.
- It uses no real brick, real object, real cutout, catalogue row, network, Globus endpoint, transfer, or empirical estimator.
- A PASS does not authorize a source manifest, transfer, production canary, acceptance, publication, commit, or push. Duho owns acceptance and Kun owns the reproducibility gate.

## Result

`7/7` tests passed. The generated corpus contains 9 bricks, 29 object rows, 29 expected arrays, 40 files, and 42,462,304 bytes. Exact commands, logs, authority hashes, source/test hashes, and generated-manifest hashes are in `SELFTEST.md`.

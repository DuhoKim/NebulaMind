# KUN ROUTE BINDING GATE -- 2026-08-15

## Verdict

**PASS_ROUTE_BINDING_CONTENT; NOT EXECUTABLE.**

I re-read the repinned brief and the settled Tori route binding. The target hash
now matches disk:

- `prereg/_tmp_KUN_ROUTE_BINDING_GATE_BRIEF.md`
  - SHA-256 `65583938dad5f934a60206bfb4e00b0911b7aefa010b9b32bfcf0655be853823`
- `prereg/TORI_ROUTE_BINDING_20260815.md`
  - SHA-256 `c7ed11c12ad7c26db8ce784b4d4d76c86694231d4eaab42b3ddca720a265d4cb`
  - size `24,307` bytes
  - mode `0644`
- `prereg/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
  - SHA-256 `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
  - size `42,883` bytes
  - mode `0444`

This pass gates the route-binding content only. It does not authorize a Globus
task, a source manifest, a real image fetch, a cutout run, a sky statistic, a
publication action, or acceptance. Duho owns acceptance.

## Route Variant

Tori's disclosure is adequate. The selected sequence is a **documented variant**,
not the thread's first recommendation. The first recommendation was to generate
cutouts at NERSC and transfer cutouts out. The selected route instead transfers
DR10.1 South r-band brick images by Globus and cuts locally.

That variant is defensible because it combines documented components: Legacy
Survey brick products, the thread's local Imagine/brick-cache path, and NERSC's
documented Globus/DTN bulk-transfer route. It must not be described as the
survey-thread default or as the minimal-transfer path.

The tradeoff is real: the default NERSC-compute route moves far less data
(about `54.6 GB` of cutouts versus about `2.93 TB` of bricks, per the brief).
If NERSC compute and allocation become available, that route remains operationally
leaner. But given Duho's choice and the documented Globus path, the brick-transfer
variant is acceptable as a successor route binding.

## PC-3

PC-3 as amended is sufficient as a future receipt standard. It is not merely a
restatement of the obligation.

The binding correctly says our code creates the output WCS and must prove it.
The required proof is concrete: exact WCS constants, determinant sign, centre
mapping, RA/Dec perturbation direction, round-trip residuals, source/opened/
contributing set accounting, per-pixel coverage, output hashes, code-manifest
hashes, and a production-derived parity receipt.

The existing `validate_wcs_parity.py` is appropriate only as a predicate/helper.
It explicitly describes itself as position-free and synthetic, and it states that
it does not substitute for future per-object PC-3. Tori's route binding preserves
that boundary by requiring production-derived FITS values and receipts.

## PC-4

PC-4 is correctly applied twice: first to every source header before the local
WCS parser, and again to every synthesized output header.

This is necessary because the pinned Imagine layer includes a fallback path that
can default missing CD terms to zero. The successor route correctly requires a
pre-parse fail-closed gate for source headers and a second gate for outputs. I
found no missed synthesized-header path in the route text.

The existing `fail_closed_wcs.py` is appropriate as a policy core. It rejects
distortion families, non-celestial axes, incomplete linear WCS, and singular
determinants. It is not enough by itself; the production adapter still has to
make it atomic with source validation, rendering, output validation, quarantine,
and receipt writing.

## Brick-Corner Margin Geometry

The margin rule passes at route-binding level.

The dangerous failure would be using the human-readable `16.768"` scalar as the
source-file selection rule. That would risk truncating edge or corner objects,
creating a position-correlated defect in the dipole test. Tori does not do that.

The scalar is correctly limited to explaining the 128-pixel cutout footprint:

- `128 / 2 * 0.262" = 16.768"` from centre to each output pixel-edge side.

The nominal `38.368"` neighbour-intersection figure is also correctly marked as
explanatory only. The executable rule is stronger: construct the exact output
TAN WCS, construct candidate source WCS polygons, use the pinned
`bricks_touching_aa_wcs` / `polygons_intersect` logic on pixel-edge boundary
polygons, and require every planned intersecting brick to be present, digest
matched, header-valid, and readable.

That rule handles primary, side-neighbour, and corner-neighbour cases in the
right geometry class. It still needs the synthetic fixture matrix Tori specifies:
edge cases, exact-boundary cases, all four corners, overlap without unique-area
crossing, RA wrap, declination extremes, source ordering, and multi-source
contribution. Until those fixtures pass, the route remains non-executable.

## Frozen Boundary Check

The route binding does not weaken F-10, BS-11, the STOP rule, or the frozen input
contract.

It preserves:

- one input band: `r`;
- shape: exactly `128 x 128`;
- estimator dtype: `float32`;
- native scale: `0.262 arcsec/pixel`;
- no route-induced resize, crop, rotation, clipping, normalization, or band
  combination;
- no route-specific invalid-pixel policy;
- no real-image transfer or cutout before later gates.

The frozen V3 preregistration file remains mode `0444` and hash-matched.

## What Still Blocks Execution

This content pass does not open execution. The blockers are:

1. Duho accepts the successor route wording.
2. A guarded production adapter is built offline.
3. Dependency/container lock is frozen, including astrometry.net, legacypipe,
   fitsio, numpy, scipy, and resampler behavior.
4. Synthetic boundary fixtures pass, especially edge/corner truncation cases.
5. PC-3 production-derived WCS parity receipts are implemented and gated.
6. PC-4 source and output fail-closed WCS rejection fixtures are implemented and
   gated.
7. Atomic failure behavior is proven: no missing source, zero-coverage pixel,
   digest mismatch, or header failure can produce an accepted output.
8. A manifest-only gate computes and seals the exact brick working set without
   transferring anything.
9. Duho explicitly approves the manifest hash, destination, and byte total.
10. Globus transfer uses explicit batch transfer, checksum verification, checksum
    restart semantics, zero skipped files, and terminal `SUCCEEDED`.
11. Destination acceptance verifies local byte size and SHA-256 equality for
    every file before any FITS open.
12. An edge/corner-stratified local-cut canary passes before production shards.

## Final Ruling

**Pass the successor route binding as a documented route choice and design
constraint. Do not execute it yet.**

The route is honest about being a documented variant rather than the forum's
first recommendation. The PC-3 and PC-4 standards are concrete enough to gate a
future guarded adapter. The brick-corner risk is handled by polygon-intersection
geometry rather than a scalar margin. The remaining work is implementation and
fixture proof, not another route-selection blocker.

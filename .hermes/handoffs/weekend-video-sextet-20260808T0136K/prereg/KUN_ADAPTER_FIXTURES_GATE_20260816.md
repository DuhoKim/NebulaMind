# KUN ADAPTER + BOUNDARY FIXTURES GATE -- 2026-08-16

## Verdict

**HOLD_ADAPTER_FIXTURES_CROSS_FAILS_CORNER_BOUNDARY_CASES.**

The two self-tests pass independently, and the adapter's no-fetch boundary
checks out from source. But the cross-check the brief requested -- Yui's
boundary fixtures against Tori's adapter -- does **not** pass. The adapter fails
all eight corner stress cases at planning time before it reaches rendering:
exact-corner and one-pixel-beyond-corner objects produce `expected exactly one
primary brick, found 0`.

That is a route blocker before any transfer or source manifest. A truncated or
dropped corner object is position-correlated by construction, which is the
defect class this gate exists to prevent.

## Exact Artifacts Checked

- `prereg/adapter/nm_brick_cutout_adapter.py`
  - SHA-256 `3422f2491d44f537948af59744fb11338bcf63099f38c77ffe7767f071ec4913`
- `prereg/boundary_fixtures/make_boundary_fixtures.py`
  - SHA-256 `24f55943bffabb855c2c6396d792e19ed4350449809bd22a63f59d3b6fa3404d`
- `prereg/TORI_ROUTE_BINDING_20260815.md`
  - SHA-256 `c7ed11c12ad7c26db8ce784b4d4d76c86694231d4eaab42b3ddca720a265d4cb`
- `prereg/PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
  - SHA-256 `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- `prereg/yui_bs5_sign_anchor_20260814/validate_wcs_parity.py`
  - SHA-256 `7bf0201917e7722ee9545c9c11b6cc1cbdec345504e3f29fa1aeb01e58edaa55`
- `prereg/_tori_bs7_distortion_evidence/fail_closed_wcs.py`
  - SHA-256 `cae1b1b7ef4e25000ad5d8c906647216b1425638ac737b4ea7363ca948760569`

Scratch cross-run script:

- `prereg/_tmp_kun_cross_adapter_fixtures_20260816.py`
  - SHA-256 `69115bc3133b50c195db77e6ae6ea070f4ee1b989675b8da1bf4fb850157ae7a`

## Self-Test Results

Tori adapter suite:

- command: `python3 -m unittest prereg.adapter.test_nm_brick_cutout_adapter`
- result: `27/27` passed

Yui boundary fixture suite:

- command: `python3 -m unittest test_boundary_fixtures`
- working directory: `prereg/boundary_fixtures`
- result: `7/7` passed

The first attempt to run Yui's suite from the repository root failed because the
test imports `make_boundary_fixtures` as a directory-local module. Re-running
from the fixture directory resolved that; I do not count the import-path miss as
a fixture failure.

## No-Fetch Boundary

The adapter passes the no-fetch source review.

The module imports only:

`__future__`, `argparse`, `datetime`, `hashlib`, `importlib.util`, `json`,
`math`, `pathlib`, `re`, `struct`, `sys`, and `typing`.

I found no imports of `socket`, `ssl`, `http`, `urllib`, `requests`, `httpx`,
`aiohttp`, `globus`, `subprocess`, `asyncio`, `ctypes`, or `os`. I also found
no shell-out or transport call path. The only `compile` calls reported by a
simple AST name scan are `re.compile`, not dynamic code compilation.

`importlib.util` is used only for hash-pinned local validator imports. That is
acceptable because the path and expected SHA-256 are fixed before import, and a
tampered validator is rejected by the self-test.

## Yui Fixture Claim

Yui's central fixture claim is real, not tautological.

The fixture generator builds a 3x3 synthetic brick grid, 29 object rows, and
expected value arrays from an independent Astropy WCS oracle. The tests verify:

- center, edge, overlap-only, exact-edge, beyond-edge, exact-corner, and
  beyond-corner source sets;
- every expected value against the analytic object-centered WCS;
- reversed source order invariance;
- terminal missing-neighbour and digest-mismatch failures;
- shape-correct primary-only zero-padding failures for all four beyond-edge and
  all four beyond-corner stress classes.

That directly tests the defect class I refused to accept by reasoning alone:
the output can be `128 x 128` and still be wrong because edge or corner pixels
were silently padded or shifted.

## Cross-Check

I ran a separate cross-check that imports Yui's fixture cases and Tori's adapter
API without modifying either artifact. The cross-check maps Yui's 3x3 synthetic
grid into Tori's `SyntheticBrickGeometry`, stages Tori-accepted synthetic FITS
sources, and then for each Yui object requires:

- Tori `plan_object` source set equals Yui `expected_bricks`;
- Tori `run_local_cut` completes;
- PC-3 receipt planned/opened source sets equal Yui `expected_bricks`;
- coverage minimum is at least `1`;
- zero coverage count is `0`.

I intentionally did **not** require pixel-value equality in this cross-run.
Yui's oracle uses Astropy WCS plus bilinear sampling; Tori declares a
nearest-neighbour renderer stand-in. A value mismatch under those conditions
would not isolate the boundary rule.

Result:

- total cases: `29`
- passed: `21`
- failed: `8`

Passed: center and all edge cases, including overlap-only, exact-edge, and
one-pixel-beyond-edge cases.

Failed: all corner cases:

- `corner_north_east_exact`
- `corner_north_east_beyond`
- `corner_north_west_exact`
- `corner_north_west_beyond`
- `corner_south_east_exact`
- `corner_south_east_beyond`
- `corner_south_west_exact`
- `corner_south_west_beyond`

Each fails in `plan_object` before rendering, with zero primary bricks found.
This comes from the adapter requiring exactly one rectangular unique-area
primary before the polygon-intersection working set is allowed to proceed.

That requirement is too brittle for the corner fixture class. The written route
says the object catalogue `BRICKID/BRICKNAME` is only a cache-grouping hint, not
a sufficient source set. That is correct. But the current adapter has made a
computed rectangular primary a hard precondition. At exact or near-corner
geometry, this can fail before the stronger polygon source-set rule runs.

## PC-3 On Synthesized Headers

The reuse of `validate_wcs_parity.py` is acceptable only with the adapter's
additional checks.

The validator itself is position-free and synthetic; it cannot validate a
production output header by itself. Tori's adapter handles that correctly by
using it only for the row-order convention, 2x2 determinant algebra, and
predicate set, while the adapter's `pc3_output_receipt` checks the staged output
bytes for exact WCS constants, CRVAL center mapping, perturbation directions,
round-trip residuals, coverage, and source-set accounting.

No extra PC-3 concept is needed beyond those checks, but the corner-planning
repair must pass before PC-3 can be trusted for corner objects.

## PC-4 Twice

PC-4 is correctly wired twice in the adapter source:

- `SyntheticBrickSource.__init__` parses raw source FITS cards and runs
  `fail_closed_header_gate` before constructing a `TanWcs`;
- `pc3_output_receipt` parses the staged output header and runs
  `fail_closed_header_gate` again before accepting the output.

The output tamper test proves the synthesized-header path is not skipped:
flipping the output CD sign sends the staged file to quarantine and produces no
accepted cutout.

## Yui's Declared Gaps

Before transfer or any source manifest, the following must be closed:

- the cross-failed exact and beyond-corner source-set cases;
- RA-wrap source planning against the same fixture framework or a successor
  real-geometry fixture;
- selected-footprint declination-extreme planning;
- distinct per-brick tangent-point geometry, not only Yui's shared tangent-plane
  approximation;
- the overlap scalar updated from the synthetic `128` pixels to the documented
  DR10 approximately `130` pixels or, better, replaced by real WCS polygon
  tests from the geometry sidecar.

Before production cutting, but not necessarily before the transfer manifest:

- multiprocessing scheduling determinism;
- production `.fits.fz` image-HDU-1 read path;
- pinned Imagine/astrometry.net resampler value comparison;
- legitimate three-source T-junction if it occurs in the real DR10 South
  geometry;
- full dependency/container lock.

If the manifest planner and production cutter are the same artifact, close all
of these before manifest approval.

## Required Repair

A passing repair must do all of the following:

1. Remove the hard dependency on exactly one computed rectangular primary before
   polygon source-set planning. Either accept a frozen catalogue primary as
   metadata while still deriving the source set by polygon intersection, or make
   ambiguous/no-primary boundary cases fail only after a documented replacement
   rule has proven the complete intersecting source set.
2. Re-run the cross-check against all 29 Yui fixture objects and pass the exact
   and beyond-corner cases.
3. Preserve terminal failure for genuinely missing planned sources, digest
   mismatch, invalid headers, and zero coverage.
4. Keep PC-3 and PC-4 atomic to output acceptance.
5. Record the cross-check as an adapter receipt, not just separate self-tests.

## Final Ruling

**Hold.**

Tori's adapter is a strong build artifact in isolation, and Yui's fixtures are a
strong independent oracle. The thing neither author ran is precisely what fails:
their boundary contracts cross at corners. That must be repaired before any
source manifest, transfer, local-cut canary, production shard, publication, or
acceptance.

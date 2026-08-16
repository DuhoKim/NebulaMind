HOLD_RECEIPT_HASH_MISMATCH

# KUN ROUND-2 BOUNDARY COVERAGE REGATE -- 2026-08-16

## Verdict

**HOLD_RECEIPT_HASH_MISMATCH.**

The brief required pinned hashes to be verified first and said to abort on
mismatch. The cross-runner, adapter, and fixture generator hashes match the
brief prefixes, but the pinned receipt does not.

The brief pins:

- `prereg/adapter/CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json`
  - expected prefix `4ff79c6ac52cc239`

Measured before re-running:

- `prereg/adapter/CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json`
  - SHA-256 `14d137c8d533540dad715c50cfe98bba5765a8ac4e816c0e37dc925b7ced54ee`

After I re-ran the formal cross-check, the receipt changed again:

- SHA-256 `c4c167138d89cbfac088cbcd6d26444db77c99cc2c0cdf4a0ff0cf338ec07967`

That makes this receipt unsuitable as a pinned input in its current form. The
likely reason is that the cross-runner rewrites the receipt and includes a
fresh `recorded_utc`. If a receipt is an input to the gate, it must be stable;
if it is an output of the gate, the brief should pin the runner and expected
semantic counts, not the pre-run receipt hash.

## Hashes Measured

- brief `prereg/_tmp_kun_round2_regate_brief_20260816.md`
  - SHA-256 `916869181417ab2a1f20230f7f3cdf4d7a925b7145174445938ce26d332c97f9`
- cross-runner `prereg/adapter/cross_check_yui_boundary.py`
  - SHA-256 `dea3b87be22ff91632541b6714b7fa11f7108fe2cb239855bf7235e25028cbc8`
- receipt before formal rerun `prereg/adapter/CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json`
  - SHA-256 `14d137c8d533540dad715c50cfe98bba5765a8ac4e816c0e37dc925b7ced54ee`
- receipt after formal rerun
  - SHA-256 `c4c167138d89cbfac088cbcd6d26444db77c99cc2c0cdf4a0ff0cf338ec07967`
- adapter `prereg/adapter/nm_brick_cutout_adapter.py`
  - SHA-256 `f3c71021f9e01051363dad5a0bd5128b5f398234b5f37c552d267fade7fb658a`
- round-1 fixture generator `prereg/boundary_fixtures/make_boundary_fixtures.py`
  - SHA-256 `24f55943bffabb855c2c6396d792e19ed4350449809bd22a63f59d3b6fa3404d`
- round-2 fixture generator `prereg/boundary_fixtures/make_boundary_fixtures_round2.py`
  - SHA-256 `60e3d662d72fbc87e0c82889b4f9174c033882b8f9a2019011c5104bb4aa15bc`

## Counts Observed

I continued far enough to identify whether this was only a custody defect or
also a content defect.

Formal cross-run command:

- `python3 prereg/adapter/cross_check_yui_boundary.py`

Observed output:

- overall `PASS`
- round 1: `29/29`, `0` failed
- round 2: `4/4`, `0` failed

The receipt reports round-1 and round-2 counts separately. I found no top-level
summed case count in the receipt after the rerun. The runner also states the
counts contract as: round-1 and round-2 are reported separately and never
merged.

Fixture suites:

- command from `prereg/boundary_fixtures`:
  `python3 -m unittest test_boundary_fixtures test_boundary_fixtures_round2`
- result: `12/12` passed

Adapter suite:

- command: `python3 -m unittest prereg.adapter.test_nm_brick_cutout_adapter`
- result: `30/30` passed

Round-2 generated tree integrity:

- `objects.json` manifest SHA matched disk:
  `e4333443cedb511256ebc1ec487f93b293c8d1bafed3ddbb41ced242ad59df2b`
- `geometry_sidecar.json` manifest SHA matched disk:
  `9f0dc0f5125961c00aaef3d540bc9de95fabe0ae6b5d3e762b67760d2f9df635`
- object count `4`, brick count `8`

## Item 2 -- Adapter Unmodified For Round 2

The adapter hash is unchanged from the corner-repair gate:
`f3c71021f9e01051363dad5a0bd5128b5f398234b5f37c552d267fade7fb658a`.

The round-2 PASS is therefore not evidence that the adapter was bent to the new
oracle. It is evidence that the polygon-only planner already handles these
coarse round-2 classes: RA wrap, selected declination extremes, distinct
per-brick tangent points, and overlap-without-unique-crossing.

That said, the round-2 cases are not a complete stress test. They are coverage
fixtures, not a proof of equivalence between the adapter's source-polygon-into-
object-frame approach and Yui's output-polygon-into-source-frame clipping under
all boundary conditions.

## Item 3 -- Adequacy Of Four Round-2 Cases

One case per round-2 class is sufficient for this specific regate only:
confirming that the formal cross-runner now includes round-2 coverage and that
the adapter does not fail the obvious RA-wrap, selected-footprint declination,
distinct tangent point, and overlap-only cases.

It is not sufficient as final pre-transfer boundary coverage for the hardest
geometry. At minimum, the declination-extreme classes need additional near-edge
variants before relying on them for a real manifest/canary gate: exact boundary,
one-pixel-beyond, one-pixel-inside, and sub-pixel knife-edge cases at both the
selected high and low declination extremes.

## Item 4a -- Round-2 Primary Field Not Compared

Leaving Yui's `primary_brick` unchecked is acceptable for this gate.

The field uses a west-side convention, while the adapter primary is explicitly
grouping metadata selected by nearest planned source centre. Source-set equality
and coverage are the safety properties here. Comparing two intentionally
different primary conventions would not test the route's source-completeness
contract and could reintroduce the over-strict primary gate that caused the
corner failure.

The field should remain recorded so a later real-geometry gate can inspect
primary metadata, but it is not a blocker for this round-2 source-set coverage
gate.

## Item 4b -- Extreme-Declination Knife Edge

This is the substantive residual gap. Round-2 is useful, but it does not close
sub-pixel knife-edge inclusion at extreme declination. The declared margins are
at least about ten source pixels, while the hardest case is exactly where the
projection geometry is most distorted.

This gap does not block the current narrow question if the custody hash issue is
repaired. It does block using this as the last boundary fixture before transfer
or real source-manifest approval. A later pre-transfer gate needs explicit
high/low-declination knife-edge fixtures near the polygon inclusion threshold.

## Pixel-Equality Exclusion

The pixel-equality exclusion is still correctly scoped to the later resampler
gate.

The current cross-run compares source-set planning, PC-3 planned/opened sets,
and coverage. It deliberately excludes pixel equality because Yui's oracle uses
Astropy bilinear sampling while the adapter uses a declared nearest-neighbour
stand-in. Pixel equality should be required only after the pinned
Imagine/astrometry.net resampler and environment lock are in place.

## Required Repair To Clear This HOLD

Re-issue the brief or receipt so the exact-hash gate is coherent:

1. If `CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json` is an input, make it deterministic
   and pin its exact settled hash. Do not include a changing timestamp in the
   hashed body.
2. If it is an output, do not pin the pre-run receipt hash. Pin
   `cross_check_yui_boundary.py`, the fixture generators, and the expected
   semantic result: round 1 `29/29`, round 2 `4/4`, separate counts, no merged
   total.

After that repair, I can tight-confirm the content as passing this round-2
coverage gate, with the declared extreme-declination knife-edge gap carried
forward to the pre-transfer fixture gate.

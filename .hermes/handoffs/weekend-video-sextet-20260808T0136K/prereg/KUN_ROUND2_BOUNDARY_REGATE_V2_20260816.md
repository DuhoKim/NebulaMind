PASS_ROUND2_BOUNDARY_COVERAGE

# KUN ROUND-2 BOUNDARY COVERAGE REGATE V2 -- 2026-08-16

## Verdict

**PASS_ROUND2_BOUNDARY_COVERAGE.**

The receipt identity repair is valid. The stable identity is the receipt's
internal `content_sha256`, not the receipt file SHA-256. I regenerated the
receipt twice: `recorded_utc` changed, while `content_sha256` remained fixed at
the pinned value.

This pass remains build-only and synthetic-only. It authorizes no network, no
real survey data, no source manifest, no sky statistic, no real rows, no real
positions, no real images, no chirality, no publication, no accepted status, no
commit, and no push.

## Hashes Measured

- brief `prereg/_tmp_kun_round2_regate_v2_brief_20260816.md`
  - SHA-256 `b97045d07e7f68c2de5f9fccbe667de725af9dab05c2f31711303a8d61b23b84`
- cross-runner `prereg/adapter/cross_check_yui_boundary.py`
  - SHA-256 `0ebc1eeba1f15ae3171e5abc8b03243e665d900bcb51c93d2f348af417a61db1`
- adapter `prereg/adapter/nm_brick_cutout_adapter.py`
  - SHA-256 `f3c71021f9e01051363dad5a0bd5128b5f398234b5f37c552d267fade7fb658a`
- round-1 fixture generator `prereg/boundary_fixtures/make_boundary_fixtures.py`
  - SHA-256 `24f55943bffabb855c2c6396d792e19ed4350449809bd22a63f59d3b6fa3404d`
- round-2 fixture generator `prereg/boundary_fixtures/make_boundary_fixtures_round2.py`
  - SHA-256 `60e3d662d72fbc87e0c82889b4f9174c033882b8f9a2019011c5104bb4aa15bc`

Receipt after my final rerun:

- file SHA-256 `69c0ec6623676c42464df07b5c932284831d4be9c37c4ef1c8193ee68383cada`
- internal `content_sha256`
  `6a0a4e40653f79128af9359c25614f432ee1d00702e554047d07721bf4e08744`

Round-2 generated tree:

- `fixture_manifest.json`
  `906d0bebb66c421dfb441c30813693e7d14525efa266d8c45b17f89d61781962`
- `objects.json`
  `e4333443cedb511256ebc1ec487f93b293c8d1bafed3ddbb41ced242ad59df2b`
- `geometry_sidecar.json`
  `9f0dc0f5125961c00aaef3d540bc9de95fabe0ae6b5d3e762b67760d2f9df635`

## Receipt Identity

The identity fix is honest.

The receipt's `content_hash_excludes` field is exactly:

`["content_sha256", "recorded_utc"]`

Nothing else is excluded. The exclusion list is itself included in the hashed
body, because the runner builds the hash body by excluding only those two top
level fields after `content_hash_excludes` has been set.

Two formal cross-run executions:

- run 1:
  - `content_sha256`
    `6a0a4e40653f79128af9359c25614f432ee1d00702e554047d07721bf4e08744`
  - `recorded_utc` `2026-08-15T16:41:45Z`
  - round 1 `29/29`, round 2 `4/4`
- run 2:
  - `content_sha256`
    `6a0a4e40653f79128af9359c25614f432ee1d00702e554047d07721bf4e08744`
  - `recorded_utc` `2026-08-15T16:42:20Z`
  - round 1 `29/29`, round 2 `4/4`

The receipt file SHA changes, as expected. The content identity does not.

## Counts And Separation

Formal cross-run:

- command: `python3 prereg/adapter/cross_check_yui_boundary.py`
- overall status `PASS`
- round 1: `29` total, `29` passed, `0` failed
- round 2: `4` total, `4` passed, `0` failed

The receipt reports round-1 and round-2 in separate objects. I found no top-level
merged count, and no downstream field that sums them into `33`. The runner's
comparison contract explicitly says: round-1 and round-2 are reported separately
and never merged.

Supporting suites:

- adapter suite: `python3 -m unittest prereg.adapter.test_nm_brick_cutout_adapter`
  - `30/30` passed
- fixture suites from `prereg/boundary_fixtures`:
  `python3 -m unittest test_boundary_fixtures test_boundary_fixtures_round2`
  - `12/12` passed

## Item 3 -- Unmodified Adapter

The adapter was not modified for this round-2 coverage extension. Its hash is
the same `f3c71021...` hash I already gated in the corner repair.

That means the polygon-only planner genuinely already handles the coarse
round-2 classes tested here:

- RA-wrap seam crossing at Dec `-10`;
- selected-footprint high declination;
- selected-footprint low declination;
- distinct per-brick tangent points;
- overlap-without-unique-boundary crossing.

It does **not** mean the planner is proven for every real boundary geometry.
The round-2 cases are useful coverage, but they are not a proof of equivalence
between every possible output/source polygon inclusion convention near the
hardest projection edges.

## Item 4 -- Adequacy Of Four Cases

One case per class is adequate for this gate: verifying that the formal
cross-runner is no longer round-1-only and that the adapter can pass the named
round-2 coverage classes.

It is not adequate as final pre-transfer boundary coverage. Before any real
manifest or transfer, high and low declination need additional stress cases:
inside, exact-boundary, one-pixel-beyond, and sub-pixel knife-edge inclusion at
both extremes. The current pass should be read as a coverage regate, not the
last geometry gate before real data movement.

## Item 5a -- Unchecked `primary_brick`

Leaving Yui's round-2 `primary_brick` field unchecked is acceptable here.

Yui records a west-side convention. The adapter records a nearest-planned-centre
grouping primary. Source completeness does not depend on either field. The
safety properties are planned source-set equality, PC-3 planned/opened equality,
contributing source coverage, and zero uncovered pixels.

Forcing the two primary conventions to match would re-elevate grouping metadata
into a gate, which is the failure mode the corner repair removed. The field
should remain recorded, but reconciliation is not required for this gate.

## Item 5b -- Extreme-Declination Knife Edge

The declared knife-edge gap is real but does not block this round-2 coverage
gate.

Round-2 covers selected-footprint extremes and distinct tangent points, but it
does not stress sub-pixel inclusion at those extremes. The margins are at least
about ten source pixels. Round-1 has exact-edge and one-pixel-beyond cases, but
only at Dec `-30`.

This combination is not sufficient for a pre-transfer fixture gate. It is
sufficient for the current claim that round-2 coverage has been added and passes
as a separate class. The knife-edge stress belongs to the next geometry tier
before a source manifest or real transfer.

## Pixel-Equality Exclusion

The pixel-equality exclusion remains correctly scoped to the later resampler
gate.

Yui's oracles use Astropy bilinear sampling. The adapter still uses a declared
nearest-neighbour renderer stand-in. For this gate, the relevant checks are
source-set equality, PC-3 planned/opened equality, coverage minimum, and zero
uncovered pixels. Pixel equality should become mandatory only after the pinned
Imagine/astrometry.net resampler and environment lock replace the stand-in.

## Final Ruling

**Pass this round-2 boundary coverage regate.**

Carry forward the limitation explicitly: this is not the last geometry gate
before transfer. Extreme-declination sub-pixel knife-edge fixtures remain
required before any source manifest, Globus transfer, real-image read, or
production cutout can be authorized.

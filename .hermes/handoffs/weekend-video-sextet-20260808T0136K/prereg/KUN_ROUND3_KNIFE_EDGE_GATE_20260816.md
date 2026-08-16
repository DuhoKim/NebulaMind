PASS_ROUND3_KNIFE_EDGE

# KUN ROUND-3 EXTREME-DECLINATION KNIFE-EDGE GATE -- 2026-08-16

## Verdict

**PASS_ROUND3_KNIFE_EDGE.**

The moved adapter is hash-pinned and passes the round-1, round-2, and round-3
cross-checks. The receipt identity is stable across reruns. The contribution
window change does not invalidate the earlier corner-repair or round-2 passes
for the planning/source-set/coverage semantics those gates covered.

This remains build-only and synthetic-only. It authorizes no network, no real
survey data, no source manifest against the real parent set, no sky statistic,
no real rows, no real positions, no real images, no chirality, no publication,
no accepted status, no commit, and no push.

## Hashes Measured First

- brief `prereg/_tmp_kun_round3_gate_brief_20260816.md`
  - SHA-256 `b886920e954a3c43948f407bdc9556d026bad76731b90ba37b6597803ca821c7`
- adapter `prereg/adapter/nm_brick_cutout_adapter.py`
  - SHA-256 `cd18ead45f4b77f2c1aaa505d5bce9c401f02eda4bd2e5cdfdb8c2bbe8f58128`
- cross-runner `prereg/adapter/cross_check_yui_boundary.py`
  - SHA-256 `74ad048178df66a5025d5516514d233d6d3eeedabe916b80088e5cd2315a80ad`
- round-1 fixture generator `prereg/boundary_fixtures/make_boundary_fixtures.py`
  - SHA-256 `24f55943bffabb855c2c6396d792e19ed4350449809bd22a63f59d3b6fa3404d`
- round-2 fixture generator `prereg/boundary_fixtures/make_boundary_fixtures_round2.py`
  - SHA-256 `60e3d662d72fbc87e0c82889b4f9174c033882b8f9a2019011c5104bb4aa15bc`
- round-3 fixture generator `prereg/boundary_fixtures/make_boundary_fixtures_round3.py`
  - SHA-256 `6b410fb40def2869d4f3431f029654d8fa7cacd20741dca5a84b12409d5e5e62`

Receipt after final rerun:

- file SHA-256 `8a26bfa1c3fd94ef33b8e89d609f3d7757f9e63792250224d413ca109adc4559`
- internal `content_sha256`
  `1eba47d8cef18d84941e6a85ffca010717825b7134cf8be72656b53f6a7561c7`

Round-3 generated tree:

- `fixture_manifest.json`
  `6ef41ca6ae48d34ab3b8dda56e165dffbc964566c08231a7553ee11a802315e4`
- `objects.json`
  `cff97437049634336fcd8893dd36830b9c146f4cb3d192102c545b10fc6fe996`
- `geometry_sidecar.json`
  `2b70048a463ee51c4834510bad41475153e33bbe13c98bbf6adad6fe414e6098`

## Counts Run

Cross-runner, run 1:

- command: `python3 prereg/adapter/cross_check_yui_boundary.py`
- `content_sha256`
  `1eba47d8cef18d84941e6a85ffca010717825b7134cf8be72656b53f6a7561c7`
- `recorded_utc` `2026-08-16T03:00:43Z`
- round 1: `29/29`, `0` failed
- round 2: `4/4`, `0` failed
- round 3: `10/10`, `0` failed

Cross-runner, run 2:

- `content_sha256`
  `1eba47d8cef18d84941e6a85ffca010717825b7134cf8be72656b53f6a7561c7`
- `recorded_utc` `2026-08-16T03:01:18Z`
- round 1: `29/29`, `0` failed
- round 2: `4/4`, `0` failed
- round 3: `10/10`, `0` failed

The stable identity holds while `recorded_utc` moves.

Self-tests:

- adapter suite: `python3 -m unittest prereg.adapter.test_nm_brick_cutout_adapter`
  - `30/30` passed
- fixture suites from `prereg/boundary_fixtures`:
  `python3 -m unittest test_boundary_fixtures test_boundary_fixtures_round2 test_boundary_fixtures_round3`
  - `17/17` passed

The cross receipt reports round 1, round 2, and round 3 separately. There is no
standalone merged `43` count in the cross-runner or receipt; any `43` occurrence
remaining is inside hashes or numeric geometry values, not a total-case field.

## Item 2 -- Contribution-Window Change

The adapter moved because the contribution window now requires an output pixel
centre to lie within the source's interior pixel-centre window `[1, N]`. This
matches the fixture oracle's bilinear-support rule for the synthetic gates.

I do not find evidence that this change invalidates round 1 or round 2:

- round 1 still passes `29/29`;
- round 2 still passes `4/4`;
- for all round-1 and round-2 receipt cases, `contributing_sources` equals
  `expected_bricks`;
- coverage minimum remains at least `1` and zero coverage remains `0`;
- an additional scratch coverage comparison passed:
  `prereg/_tmp_kun_round3_coverage_compare_20260816.py`
  SHA-256 `ff2f78498eeb58c4956d1e2174f5c99881f73a14a7193fd44505d5d5d5ae08a1`.

The scratch comparison matched current adapter coverage against Yui's analytic
round-2 coverage arrays exactly, and found no round-1 coverage minimum/zero
coverage drift against the round-1 oracle. The earlier corner-repair and
round-2 passes therefore still stand against the moved adapter for the
planning/source-set/coverage semantics they covered.

Pixel-value equality remains outside this gate because the renderer is still a
nearest-neighbour stand-in.

## Item 3 -- Planned Versus Contributing Split

The planned/contributing split at positive knife-edge offsets is handled
correctly.

Round 3 contains ten cases: five offsets at the selected high-declination edge
and five at the selected low-declination edge:

- `inside`: `-10` source pixels;
- `subpixel_just_inside`: `-0.25`;
- `exact_boundary`: `0`;
- `subpixel_just_outside`: `+0.25`;
- `one_pixel_beyond`: `+1`.

For the `+0.25` and `+1` cases at both declination extremes:

- the candidate source is present in `planned_bricknames`;
- the candidate source is opened;
- the candidate source is **not** in `contributing_sources`;
- the candidate source is recorded in `zero_pixel_touch_sources`;
- the cut completes with `coverage_min = 1` and `coverage_zero_count = 0`.

This is the right semantics. Positive polygon intersection means the source
must be planned/fetched. No output pixel centre inside that source means it must
not be credited for coverage.

## Item 4 -- Are Ten Cases Enough?

Ten cases are adequate for the round-3 knife-edge gate.

They cover the ladder at both selected declination extremes and include the
exact classes the prior gap named: inside, exact boundary, one-pixel beyond,
subpixel just inside, and subpixel just outside. The achieved offsets in the
round-3 manifest are within the stated solve tolerance, including:

- `dec_max_subpixel_just_inside`: `-0.2500000002687557`;
- `dec_max_subpixel_just_outside`: `0.25000000020418156`;
- `dec_min_subpixel_just_inside`: `-0.24999999991246113`;
- `dec_min_subpixel_just_outside`: `0.24999999995316102`;
- exact-boundary cases within about `5.1e-10` and `6.9e-13` pixels.

I do not require widening this ladder before a source manifest is discussable.
The later real-geometry manifest/canary gate still has to bind actual DR10
geometry sidecar rows and production resampler semantics, but this synthetic
knife-edge gap is closed.

## Item 5 -- Overlap Scalar / Polygon Replacement

Gap 5 is closed for the adapter and synthetic fixture gates.

The old scalar concern was that the source-selection rule could depend on a
synthetic overlap width such as `128` pixels rather than real WCS geometry or
the documented DR10 overlap. The current adapter does not use that scalar for
selection. Selection is:

- candidate prefilter by a broad angular radius with slack;
- exact output nine-point boundary projected into each candidate source TAN
  pixel plane;
- clipped polygon area inside the source pixel box;
- source planned iff area is greater than
  `INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2 = 1e-8`.

The `128` values that remain are the frozen cutout size and pixel-edge probe
coordinates such as `128.5`, not an overlap-width selection scalar. I found no
surviving `130` or synthetic-overlap scalar in the adapter selection path.

The real DR10 source manifest still must be generated from the real geometry
sidecar and the same polygon rule; that is a later manifest gate, not an open
synthetic-fixture gap.

## Final Ruling

**PASS_ROUND3_KNIFE_EDGE.**

The moved adapter keeps the earlier corner-repair and round-2 gates standing
for their scoped semantics, closes the extreme-declination subpixel knife-edge
fixture gap, and closes the synthetic overlap-scalar gap by replacing scalar
selection with polygon-area source selection.

Still not authorized: real source manifest, Globus transfer, real image read,
production cutout, sky statistic, publication, commit, push, or accepted status.

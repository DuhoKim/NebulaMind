PASS_PIXEL_VALUE_EQUALITY

# KUN RESAMPLER / PIXEL-VALUE EQUALITY GATE -- 2026-08-16

## Verdict

**PASS_PIXEL_VALUE_EQUALITY.**

The moved adapter is hash-pinned at `267b2a93d2a6...` and passes round-1,
round-2, and round-3 planning/source-set/coverage semantics plus the new
pixel-value comparison where that comparison is meaningful. This closes the
previously deferred synthetic adapter-vs-oracle pixel-value equality gate.

This does not assert equivalence with the production Imagine/astrometry.net
kernel. The lock supports the measured offline environment and the adapter
stdlib-only invariant; production-kernel identity remains a later gate.

No network, no real survey data, no source manifest against the real parent
set, no sky statistic, no rows/positions/images/chirality, no publication, no
accepted status, no commit, and no push are authorized.

## Hashes Measured First

- brief `prereg/_tmp_kun_resampler_gate_brief_20260816.md`
  - SHA-256 `fbd3b451092e8bb098f6bf875006650258f86fab2cf329318879a98edb714664`
- adapter `prereg/adapter/nm_brick_cutout_adapter.py`
  - SHA-256 `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`
- cross-runner `prereg/adapter/cross_check_yui_boundary.py`
  - SHA-256 `e4168e331148feb9d348e30dcd10427f572492dfbedab141b745b8e3c34c691d`
- round-1 fixture generator `prereg/boundary_fixtures/make_boundary_fixtures.py`
  - SHA-256 `24f55943bffabb855c2c6396d792e19ed4350449809bd22a63f59d3b6fa3404d`
- round-2 fixture generator `prereg/boundary_fixtures/make_boundary_fixtures_round2.py`
  - SHA-256 `60e3d662d72fbc87e0c82889b4f9174c033882b8f9a2019011c5104bb4aa15bc`
- round-3 fixture generator `prereg/boundary_fixtures/make_boundary_fixtures_round3.py`
  - SHA-256 `6b410fb40def2869d4f3431f029654d8fa7cacd20741dca5a84b12409d5e5e62`
- dependency lock `prereg/YUI_DEPENDENCY_ENVIRONMENT_LOCK_20260816.json`
  - SHA-256 `6e0c9ae2c414f0659c1dda5fba4f42bb417924fb64bb0bb08fb60d6d0f6e24ab`

Final receipt:

- receipt path `prereg/adapter/CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json`
- file SHA-256 `786db8e27582fed8168bf782955465f6b10eb7df5c6bd5c5bff39dadd87e5651`
- internal `content_sha256`
  `a8a5e998549c6b66732591b5ca0c3b5fbf37b076ac29080c33bea99a16cde586`
- `content_hash_excludes`: `["content_sha256", "recorded_utc"]`

## Runs Performed

Cross-runner run 1:

- command: `python3 prereg/adapter/cross_check_yui_boundary.py`
- status: `PASS`
- `content_sha256`
  `a8a5e998549c6b66732591b5ca0c3b5fbf37b076ac29080c33bea99a16cde586`
- `recorded_utc` `2026-08-16T04:16:30Z`
- round 1: `29/29`, `0` failed
- round 2: `4/4`, `0` failed
- round 3: `10/10`, `0` failed

Cross-runner run 2:

- status: `PASS`
- `content_sha256`
  `a8a5e998549c6b66732591b5ca0c3b5fbf37b076ac29080c33bea99a16cde586`
- `recorded_utc` `2026-08-16T04:16:55Z`
- round 1: `29/29`, `0` failed
- round 2: `4/4`, `0` failed
- round 3: `10/10`, `0` failed

Adapter and fixture tests:

- `python3 -m unittest prereg.adapter.test_nm_brick_cutout_adapter`
  - `30/30` passed
- from `prereg/boundary_fixtures`:
  `python3 -m unittest test_boundary_fixtures test_boundary_fixtures_round2 test_boundary_fixtures_round3`
  - `17/17` passed
- Kun coverage comparator:
  `python3 prereg/_tmp_kun_round3_coverage_compare_20260816.py`
  - `PASS`, no failures

## Pixel Agreement

Round 1:

- `cases_compared`: `5`
- `cases_skipped`: `24`
- `max_abs_error_over_compared`: `1.9073486328125e-06`
- tolerance: `5e-06`
- compared cases: centre plus the four no-neighbour edge controls
- skipped cases: all neighbour-involving edge/corner cases
- skip reason: round-1 uses one shared tangent plane, while the adapter's
  production-shaped model uses per-brick TAN source frames; neighbour value
  comparison there would measure that fixture approximation, not the resampler.

Round 2:

- `cases_compared`: `4`
- `cases_skipped`: `0`
- `max_abs_error_over_compared`: `7.62939453125e-06`
- tolerance: `1e-05`
- all cases compared, including RA wrap, selected declination max/min, and
  overlap-without-unique-crossing.

Round 3:

- `cases_compared`: `10`
- `cases_skipped`: `0`
- `max_abs_error_over_compared`: `7.62939453125e-06`
- tolerance: `1e-05`
- all ten extreme-declination knife-edge cases compared, including exact,
  subpixel-inside, subpixel-outside, and one-pixel-beyond cases at both
  selected declination extremes.

The tolerances are not fitted to the adapter output: round 1's `5e-6` is in
the pinned round-1 fixture file, and rounds 2/3 use `VALUE_TOLERANCE = 1e-5`
from the pinned round-2 fixture file, imported by round 3. The observed maxima
are consistent with float32 quantization: `1.9073486328125e-06` for round 1
and one float32 ulp at values near 100, `7.62939453125e-06`, for rounds 2/3.

## Rulings

1. **Round-1 skip:** acceptable for this gate. It is not hidden: the receipt
   reports `5` compared and `24` skipped with one explicit geometric reason.
   Round 1's neighbour-involving value comparison is invalid because its source
   model is a shared-tangent approximation. Rounds 2 and 3 are the relevant
   neighbour-sampling value tests because they use distinct per-brick tangent
   points and compare every case with zero skips. I do not see a pixel
   behaviour exercised only by round-1 neighbour cases that rounds 2/3 miss
   for the synthetic resampler gate.

2. **Rounds 2 and 3 full comparison:** confirmed. The source shows no filter
   other than round-1's `primary_only` condition. `_run_pinned_tree` passes an
   expected array for every round-2 and round-3 case, and the receipt reports
   `cases_skipped: 0` for both.

3. **Acceptance bar:** one float32 ulp is the right bar here; exact bit equality
   is not a valid requirement for this oracle/adapter comparison. The oracle
   expected arrays are float32 products of an analytic construction, while the
   adapter samples staged float32 raster values and accumulates in float64.
   The residuals are below the predeclared tolerances and match the expected
   float32 quantization scale. Demanding bit equality would conflate numeric
   representation with semantic resampling equality.

4. **Dependency lock and imports:** the adapter remains stdlib-only. Its direct
   imports are `argparse`, `datetime`, `hashlib`, `importlib.util`, `json`,
   `math`, `pathlib`, `re`, `struct`, `sys`, and `typing`. The dependency lock
   records that adapter tests loaded no third-party distributions beyond the
   startup baseline. The cross-runner and oracle fixtures correctly require
   `numpy` and `astropy`; that is test/oracle scope, not adapter runtime scope.
   The lock is adequate as an environment measurement for this synthetic gate,
   but it openly does not provide an exact offline rebuild or production-kernel
   equivalence, so those claims remain out of scope.

## Prior Passes

The earlier corner-repair, round-2, and round-3 passes still stand against the
moved adapter for planning/source-set/coverage semantics. The current adapter
also closes the previously deferred synthetic pixel-value equality piece for
round-1 centre-only cases and all round-2/round-3 cases.

The next step must remain build-only unless separately gated. If it touches
real galaxies, source manifests, real image reads, rows, positions, sky
statistics, or chirality, this pass does not authorize it.

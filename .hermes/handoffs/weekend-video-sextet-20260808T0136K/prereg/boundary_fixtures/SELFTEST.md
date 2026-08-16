# Synthetic boundary-fixture self-test

Verdict: **PASS_SYNTHETIC_BOUNDARY_FIXTURES_ROUND1_ROUND2_AND_ROUND3**

Scope: offline synthetic fixtures only. This is not a verdict on Tori's parallel adapter, production Imagine/legacypipe behavior, a real DR10 brick, a real cutout, or transfer readiness.

## Authority read

The fixtures were built from the written boundary contract, without reading or importing `prereg/adapter/`:

- `_tmp_YUI_BOUNDARY_FIXTURES_BRIEF.md` — SHA-256 `0f065b8ecd2ef3145e716a15e1379366dc81474ecca6fe48d5156e1c54c48059`
- `TORI_ROUTE_BINDING_20260815.md` — SHA-256 `c7ed11c12ad7c26db8ce784b4d4d76c86694231d4eaab42b3ddca720a265d4cb`
- `KUN_ROUTE_BINDING_GATE_20260815.md` — SHA-256 `1cf1231126bcb3f6ec69487abe6909280bff662e73677acc6c831dcb4a4467aa`

## Commands run

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile make_boundary_fixtures.py test_boundary_fixtures.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_boundary_fixtures
PYTHONDONTWRITEBYTECODE=1 python3 make_boundary_fixtures.py --output generated
```

Final unit result: **7/7 PASS**, 43.347 seconds. The standard `unittest` stream is preserved in `boundary_fixture_selftest_stderr.log`; stdout is empty because `unittest` writes its verbose stream to stderr.

## Generated corpus

- 9 losslessly compressed synthetic FITS bricks, each exactly `3600 × 3600`, image HDU 1, float32, one r-like plane, `0.262 arcsec/pixel` TAN headers.
- 128-pixel overlap in the synthetic rectilinear brick grid, deliberately close to the approximately 130-pixel overlap stated in the brief.
- 29 object rows and 29 exact expected `128 × 128` float32 arrays.
- 40 generated files, 42,462,304 bytes in total.
- Expected source-set sizes: five one-brick cases, sixteen two-brick cases, and eight four-brick cases.
- Final generated-tree replay: 29/29 cases, zero uncovered pixels, coverage minimum 1, maximum bilinear-versus-analytic absolute error `1.9073486328125e-06` against the `5e-6` gate.

## Assertions exercised

1. Centre control uses one source.
2. North, south, east, and west each have:
   - a no-neighbour case;
   - an overlap-only neighbour case whose output does not cross the unique boundary;
   - a centre within 63 pixels of the unique boundary;
   - a centre exactly on the unique boundary;
   - a centre one pixel beyond it.
3. Northeast, northwest, southeast, and southwest each have exact-corner and one-pixel-beyond-corner cases; every case plans the primary, both side neighbours, and the diagonal neighbour.
4. Every source and output row records the written nine-point pixel-edge polygon shape: four corners, four edge midpoints, and the repeated starting corner.
5. Every output polygon and expected value is derived from the exact object-centred `CRVAL`, `CRPIX=64.5`, non-rotated TAN output WCS, then independently mapped into the synthetic source plane.
6. Every one of all `29 × 128 × 128 = 475,136` expected pixels is compared by value, not only by array shape; bilinear source replay must agree with the analytic float32 sky-plane value to absolute tolerance `5e-6`.
7. The generated linear pattern is strictly positive and fingerprints both global x and global y. Five explicit uint32 float-bit probes are recorded per object in addition to each full-array SHA-256.
8. Reversing source order produces the same complete output and output-array hash.
9. Shape-correct, primary-only zero-padded crops are deliberately constructed for all four beyond-edge and all four beyond-corner stress cases. All eight are detected by value and contain forbidden zeros.
10. Removing a required diagonal neighbour raises `MissingNeighbourError` before any output is written.
11. Mutating one required neighbour byte raises `FixtureSourceError` on manifest digest mismatch before any output is written.
12. Every accepted oracle output has zero uncovered pixels and coverage minimum at least one.

## Sealed hashes

- `make_boundary_fixtures.py`: `24f55943bffabb855c2c6396d792e19ed4350449809bd22a63f59d3b6fa3404d`
- `test_boundary_fixtures.py`: `295e9a1a72f56a2ca66caa3910b2c92f8c67700e9302e133a202593ba76b3da0`
- `generated/fixture_manifest.json`: `21cecd7a342a57098c6c4eb03dba801799d9c5fc7b1e713d3080e97514a43237`
- `generated/objects.json`: `37f91e8c0ef6220f85c5350b233333c17fae595c929ff0bdebe36e43ba2b972e`
- `boundary_fixture_selftest_stdout.log`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `boundary_fixture_selftest_stderr.log`: `f997d82566543800d274d82ce498976be8ef8e11250985f2158833027c4818a5`

The fixture manifest additionally binds each FITS file and each source data array; each object row binds its expected `.npy` file and five exact float32 bit probes.

---

## Round 2 — per-brick geometry closure

Round 2 extends rather than replaces the 7/7 round-1 suite and generated corpus above. It was built from `_tmp_YUI_FIXTURES_ROUND2_BRIEF.md` (SHA-256 `cb481cfaf52afa6f8de07ffdc93455e23599117bee65e8b696abe21b8ca0bb2a`), the same written Tori route contract, and `KUN_ADAPTER_FIXTURES_GATE_20260816.md` (SHA-256 `8ff4d49866013368887bc8a3299e7bd3664d10b6a25df72646d1228a87789fcb`). No file under `prereg/adapter/` was read, imported, or executed.

### Round-2 commands

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile make_boundary_fixtures.py make_boundary_fixtures_round2.py test_boundary_fixtures.py test_boundary_fixtures_round2.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_boundary_fixtures test_boundary_fixtures_round2
PYTHONDONTWRITEBYTECODE=1 python3 make_boundary_fixtures_round2.py --output generated_round2
```

Combined result: **12/12 PASS**, 61.427 seconds. The combined verbose stream is `boundary_fixture_round2_selftest_stderr.log`; stdout is empty.

### Round-2 generated corpus

- Eight GZIP_2 synthetic `3600 × 3600` float32 FITS bricks with eight distinct TAN tangent points.
- One synthetic geometry sidecar. Every source row records its exact WCS, unique-area metadata, nine-point sky polygon, file hash, data hash, and value offset.
- Four new expected `128 × 128` arrays: RA wrap, selected South-domain maximum declination row, selected South-domain minimum declination row, and geometry-derived overlap-only.
- No `source_overlap_pixels`, `stride_pixels`, or executable scalar overlap threshold in the round-2 manifest.
- Fifteen files and 34,599,795 bytes under `generated_round2/`.
- Round 1 remains byte-identical. Both trees contain 17 source bricks, 33 object cases, 55 generated files, and 77,062,099 bytes.

### Round-2 assertions

1. RA-wrap candidates have tangent-point RAs on opposite numeric sides of 0/360; their plain numeric difference exceeds 358 degrees while their great-circle separation is below 0.3 degrees. The object at RA 0 plans both by WCS polygon intersection.
2. The South-domain extreme fixture centres are `32.25°` and `−89.875°`, inside the written northern seam `32.375°` and the closed celestial lower limit `−90°`. Their synthetic per-row RA spacings are `0.2955665024630605°` and `120°`; a fixed rectangular RA grid cannot satisfy both.
3. Every source uses its own `CRVAL1/CRVAL2`; opening generated FITS reproduces the sidecar tangent point and emits no Astropy warning.
4. The overlap-only object is discovered by exact WCS polygon tests. Its output does not cross the unique-area boundary but does intersect and receive values from the neighbouring source. The admissible inward-offset range was 65–146 pixels and the deterministic selected midpoint was 106. None of these is used as a reusable threshold.
5. The expected oracle is a smooth spherical sky function plus a declared per-brick fingerprint offset, analytically evaluated at every output sky coordinate and averaged over every valid contributor.
6. All `4 × 128 × 128 = 65,536` new expected pixels are compared by value. Round 1 plus round 2 compare 540,672 expected pixels.
7. Reversed source order reproduces each exact expected array and array hash.
8. Primary-only shape-correct omissions differ at 16,384 pixels for each wrap/declination case and 7,573 pixels for the overlap-only case. The overlap-only failure is detectable even though the primary alone fills the requested shape without zero padding.
9. Final generated-tree replay is 4/4 PASS, zero uncovered pixels, coverage minimum at least one, and maximum bilinear-versus-analytic error `7.62939453125e-06` against the `1e-5` gate.

### Round-2 sealed hashes

- `make_boundary_fixtures_round2.py`: `60e3d662d72fbc87e0c82889b4f9174c033882b8f9a2019011c5104bb4aa15bc`
- `test_boundary_fixtures_round2.py`: `f369b659f54f2aed677d92019428ffed82fd965bfe264b6e6efa9205c9dfa951`
- `generated_round2/fixture_manifest.json`: `906d0bebb66c421dfb441c30813693e7d14525efa266d8c45b17f89d61781962`
- `generated_round2/geometry_sidecar.json`: `9f0dc0f5125961c00aaef3d540bc9de95fabe0ae6b5d3e762b67760d2f9df635`
- `generated_round2/objects.json`: `e4333443cedb511256ebc1ec487f93b293c8d1bafed3ddbb41ced242ad59df2b`
- `generated_round2_replay.json`: `105f5b96e58923f7a0cc1be161c3cdaf75a6ee5a5d48ca94d96afec9d960a9f2`
- `boundary_fixture_round2_selftest_stdout.log`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `boundary_fixture_round2_selftest_stderr.log`: `fccff6ad403797b3d4c5215921fb2585bdbff06fd3e9ecadff869a2802312566`
- `_tmp_YUI_BOUNDARY_FIXTURES_ROUND2_20260816.md`: `17e69a2096a9826469ce33b72446d61c109f930a7a829c585705b08dc78a6ce6`

### Round-2 limits

The sidecar and all bricks are synthetic, as required. This proves the source-planning rule under RA wrap, severe declination-dependent RA convergence, separate tangent points, and polygon-derived overlap. It does not claim that the synthetic sidecar rows are real DR10 rows or that a fixture row is an observed selected-parent object. Exact realized-parent extrema, production sidecar bytes, pinned Imagine/astrometry.net polygon behavior, production Lanczos-3 values, three-source junctions, multiprocessing, and dependency/container locking still require their separately gated production stages. Kun must cross-run these fixtures against Tori's repaired adapter; this self-test is not that acceptance result.

---

## Round 3 — extreme-declination sub-pixel knife edge

Round 3 is additive and leaves the pinned round-1 and round-2 generators byte-identical. It was built from `_tmp_yui_fixtures_round3_knifeedge_brief_20260816.md` (SHA-256 `4127deec7fb1b81f52040e31d733fa749ac2d5b9173732a8d75d6e01357b7fc8`). No adapter or cross-runner implementation was read, imported, or executed to construct the oracle.

### Round-3 generated corpus

- Four distinct-TAN GZIP_2 synthetic `3600 × 3600` float32 FITS sources.
- Ten separately counted cases: inside, exact boundary, one pixel beyond, subpixel just inside, and subpixel just outside at both `+32.25°` and `−89.875°`.
- Ten expected `128 × 128` float32 arrays, full SHA-256 custody, coverage hashes, and five exact bit probes per case.
- Seventeen files and 17,328,549 bytes under `generated_round3/`.
- Object rows preserve the round-2 schema and add requested/achieved candidate-source pixel offsets.

### Round-3 placement and result

Object declination remains fixed while bisection moves the centre along the primary-to-candidate RA arc. Every objective evaluation projects the exact nine-point output pixel-edge polygon into the candidate source's own TAN pixel plane. Positive offset means positive-area candidate intersection; negative means the polygon remains outside it.

The high-declination boundary resolves along source `x`; the near-pole boundary resolves along source `y`. The requested ladder `−10, 0, +1, −0.25, +0.25` pixels was achieved with maximum error `5.056790541857481e-10` pixel against the `1e-8` gate. Both subpixel directions achieve approximately one quarter pixel at both extremes. Exact achieved values are pinned in `generated_round3/fixture_manifest.json`, `generated_round3/objects.json`, and `_tmp_YUI_BOUNDARY_FIXTURES_ROUND3_20260816.md`.

At each declination, inside, exact, and subpixel-just-inside plan only the primary. One-pixel-beyond and subpixel-just-outside plan the primary plus candidate. Their positive-area candidate slivers contain no output pixel centres at these curved projection edges; the candidate remains a required planned/opened source and is explicitly recorded as a zero-pixel-touch source. Coverage remains one at every output centre, with zero uncovered pixels.

Generated-tree replay: **10/10 PASS**. Maximum bilinear-versus-analytic error `7.62939453125e-06` against `1e-5`. Forward and reversed source order reproduce every value and coverage hash.

Combined fixture suites: **17/17 PASS**, 72.391 seconds.

### Round-3 sealed hashes

- `make_boundary_fixtures_round3.py`: `6b410fb40def2869d4f3431f029654d8fa7cacd20741dca5a84b12409d5e5e62`
- `test_boundary_fixtures_round3.py`: `36f9438d3359cbca6c27432b22ecf73570a581e15c64ca062a0a921e319b668f`
- `generated_round3/fixture_manifest.json`: `6ef41ca6ae48d34ab3b8dda56e165dffbc964566c08231a7553ee11a802315e4`
- `generated_round3/geometry_sidecar.json`: `2b70048a463ee51c4834510bad41475153e33bbe13c98bbf6adad6fe414e6098`
- `generated_round3/objects.json`: `cff97437049634336fcd8893dd36830b9c146f4cb3d192102c545b10fc6fe996`
- `generated_round3_replay.json`: `dee8b6c5748b06b76e21a94383fb01a6ee068dc6720caede29c781ff3e0fe6b8`
- `boundary_fixture_round3_selftest_stdout.log`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `boundary_fixture_round3_selftest_stderr.log`: `843d797e4f5efe2a6da4d43490273a356dfb5cdb27f805520e370dfb2cc8b1cc`
- `_tmp_YUI_BOUNDARY_FIXTURES_ROUND3_20260816.md`: `d22b0cf51de23d2b6a5e82259ac50fb148b334991a0341bc6e4d6777689190b6`

### Round-3 limit and stop

This self-test is not Tori's cross-run result and does not authorize a source manifest, Globus transfer, network access, real survey data, a real-image read, a production cutout, publication, commit, or push. Tori/Kun must load round 3 as a third separately counted block. If the next action would touch real galaxies, this lane stops successfully here.

PASS_ROUND5_TJUNCTION

# KUN ROUND-5 THREE-SOURCE T-JUNCTION GATE -- 2026-08-17

## Verdict

**PASS_ROUND5_TJUNCTION.**

Round-5 asks the unchanged adapter something new: a legitimate three-source
T-junction in which the adapter grouping primary differs from Yui's west-side
oracle convention, while planned/opened/contributing sources must still be the
same three bricks. The adapter passes that test on all nine synthetic cases.

This remains build-only and synthetic-only. It authorizes no network, no real
survey image data, no source manifest against the real parent set, no sky
statistic, no rows/positions/images/chirality, no publication, no accepted
status, no commit, and no push.

## Items 1 and 3 -- Why This Pass Means Something

1. **The adapter was not modified, but round-5 is not a no-op.**

   The adapter remains byte-identical at
   `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`.
   Round-5 introduces a geometry class earlier rounds did not cover: five
   local candidates, exactly three legitimate planned sources, and two guard
   bricks that must be excluded.

   The pass therefore means the existing polygon planner handles this
   synthetic three-source T-junction pattern. It does not mean the real working
   set has been enumerated for how often parent objects touch such junctions.

3. **Primary selection remains metadata at a T-junction.**

   In every round-5 case, the adapter grouping primary is `tj-upper-span` while
   Yui's oracle records `tj-lower-west` as its west-side convention. Despite
   that disagreement:

   - planned sources are always
     `["tj-lower-east", "tj-lower-west", "tj-upper-span"]`
   - contributing sources are always the same three bricks
   - zero-pixel-touch sources are always `[]`
   - status is `PASS`

   This is exactly the corner-repair separation being retested under a harder
   topology: "which brick is primary" does not decide "which pixels are
   available."

## Hashes Measured

- brief `prereg/_tmp_kun_round5_tjunction_gate_brief_20260817.md`
  - SHA-256 `332f0224ed7b07c9074829a658f213d098f2d8630ed28fd82a56b59b276a8c96`
- adapter `prereg/adapter/nm_brick_cutout_adapter.py`
  - SHA-256 `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`
- cross-runner `prereg/adapter/cross_check_yui_boundary.py`
  - SHA-256 `e6ac5b11008e0614b0574bba48796d41a68873d5769c255ff044597b80edb085`
- readstage `prereg/readstage/nm_brick_read_stage.py`
  - SHA-256 `6662c8c74d71b81216149596d65deeaa39c07a19a57e50ba9bbe4ac22d478b0a`
- production-read lock
  `prereg/YUI_PRODUCTION_READ_ENVIRONMENT_LOCK_20260816.json`
  - SHA-256 `01398e324446b4ce0681d3f6a3fa2b7b494f2f024ac2c556e40de09da169166a`
- round-1 fixture generator
  - SHA-256 `24f55943bffabb855c2c6396d792e19ed4350449809bd22a63f59d3b6fa3404d`
- round-2 fixture generator
  - SHA-256 `60e3d662d72fbc87e0c82889b4f9174c033882b8f9a2019011c5104bb4aa15bc`
- round-3 fixture generator
  - SHA-256 `6b410fb40def2869d4f3431f029654d8fa7cacd20741dca5a84b12409d5e5e62`
- round-4 fixture generator
  - SHA-256 `d6c193841ff8ff52f1188ae1d48bbe5ea8c89bf553c542ad176f70189b7b7533`
- round-5 fixture generator
  - SHA-256 `498659bf1798c228aac8146fbfd53ea43c6723f319aae1d7ddec41f9d93ddf6c`
- round-5 fixture tests
  - SHA-256 `97485b17708515de8f17eb9e0c4f9c8be1bb50519502722747ff8c0a5119e93a`
- generated round-5 manifest
  - SHA-256 `6ea163b4f372879f6b960bcb25754ab9c4e120ef45fb104ff2afa9576e36c4e8`
- generated round-5 objects
  - SHA-256 `d40b74d3a90a4366135c0f3d336ce05695fa5d8d8e394e9f394a2327d2a21031`
- generated round-5 geometry sidecar
  - SHA-256 `469671589abf31b4674878dc6befb4adcfd3872d318d8669165512d105b934dc`

## Runs Performed

Cross-runner run 1:

- command: `python3 prereg/adapter/cross_check_yui_boundary.py`
- status: `PASS`
- `content_sha256`
  `38585df8e4e752062e143bd18788c4bd48749d8925c33a1644dbe4626ae87b55`
- `recorded_utc` `2026-08-16T17:29:22Z`
- round 1: `29/29`, `0` failed
- round 2: `4/4`, `0` failed
- round 3: `10/10`, `0` failed
- round 4: `3/3`, `0` failed
- round 5: `9/9`, `0` failed

Cross-runner run 2:

- status: `PASS`
- `content_sha256`
  `38585df8e4e752062e143bd18788c4bd48749d8925c33a1644dbe4626ae87b55`
- `recorded_utc` `2026-08-16T17:29:54Z`
- same block counts: `29 / 4 / 10 / 3 / 9`

Final receipt:

- path `prereg/adapter/CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json`
- file SHA-256 `43a686f6249c375e0b95295cc0bb1dacb34be49db1a2bcdfc6c3395f5b931fc9`
- internal `content_sha256`
  `38585df8e4e752062e143bd18788c4bd48749d8925c33a1644dbe4626ae87b55`
- `content_hash_excludes`: `["content_sha256", "recorded_utc"]`

Tests:

- adapter suite: `python3 -m unittest prereg.adapter.test_nm_brick_cutout_adapter`
  - `30/30` passed
- full fixture suite from `prereg/boundary_fixtures`:
  `python3 -m unittest test_boundary_fixtures test_boundary_fixtures_round2 test_boundary_fixtures_round3 test_boundary_fixtures_round4 test_boundary_fixtures_round5`
  - `29/29` passed

## Geometry Ruling

Yui's T-junction premise is supported by the frozen local geometry metadata:

- local geometry source SHA-256
  `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a`
- rows read: `366912`, geometry/provenance columns only
- unique declination rows: `503`
- adjacent row pairs: `502`
- adjacent row count changes: `426`
- matched lower row RA count: `1018`
- matched upper row RA count: `1022`

For the matched junction:

- lower-west `ra2` equals lower-east `ra1`:
  `175.40275049115917`
- lower-west `dec2` equals upper-span `dec1`: `-45.125`
- upper-span `ra1 < lower boundary < upper-span ra2`:
  `175.06849315068496 < 175.40275049115917 < 175.42074363992174`

That is a true three-cell T-junction pattern in the brick geometry, not an
assumed geometry drawn from memory.

## Item 2 -- Guard Exclusion

The fixture asks five candidates and expects exactly three planned sources in
all nine cases:

- meeting sources: `tj-lower-east`, `tj-lower-west`, `tj-upper-span`
- guard sources: `tj-upper-east-guard`, `tj-upper-west-guard`

The generated manifest reports coverage `3..3` for every object, and every
adapter receipt reports the same three contributing sources with zero
zero-touch sources. The two guards are excluded as non-intersecting polygons
under the positive-area intersection rule, not credited as planned and then
silently unused.

The source threshold remains
`INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2 = 1e-8`; round-5's exact and subpixel
ladder cases are not perched on a guard-threshold accident. They deliberately
exercise both T-branches and the exact junction.

## Item 4 -- Pixel Comparison

Round-5 pixel comparison ran on all nine cases:

- `cases_compared`: `9`
- `cases_skipped`: `0`
- `max_abs_error_over_compared`: `7.62939453125e-06`
- tolerance: `1e-05`

Round-5 uses the pre-existing pinned round-2/3 value tolerance declared in
`make_boundary_fixtures_round2.py`, not a newly tuned round-5 tolerance. That
is the same one-ulp floor already judged acceptable for synthetic
adapter-vs-oracle comparison. This is not a codec gate; round-5 sources are
ordinary fixture rasters loaded through the pinned-tree path, so the relevant
question is resampling/planning at the T-junction, not compressed-container
byte identity.

## Item 5 -- Prior Passes

The six prior passes still stand against the unchanged adapter:

- corner repair
- round-2 boundary
- round-3 knife edge
- resampler pixel-value equality
- readstage/round-4
- production-read lock

Round-5 adds a synthetic three-source T-junction fixture gate. It does not
change the adapter and does not reopen the earlier gates.

## Still Open

Whether real parent-set objects touch T-junctions, and how many, is a manifest
gate/data question. This round proves:

- the T-junction pattern exists in the DR10 South brick table;
- one synthetic instance derived from that pattern is correctly handled by the
  unchanged adapter.

It does not enumerate the real working set and does not authorize real-image
or real-source-manifest work.

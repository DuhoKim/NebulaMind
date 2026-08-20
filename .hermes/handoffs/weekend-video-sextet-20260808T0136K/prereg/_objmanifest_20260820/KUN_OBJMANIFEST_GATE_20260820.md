PASS_OBJECT_MANIFEST

# KUN Object-Brick Manifest Gate — 2026-08-20

Gate seat: kimi (Nous route), fresh one-shot. Target: `_objmanifest_20260820/` object-brick manifest builder.
Method: local files, grep, python3. No network. Findings-only.
Working dir: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg`

## Verdict

PASS_OBJECT_MANIFEST. All six gate checks independently recomputed and passed. The only deltas vs the
shipped 14:52 build are transfer-progress drift (the campaign was RUNNING during the gate), not defects.

## (1) Planner REUSE — verified, not reimplemented

The builder imports the hash-pinned cutout runner and calls through to the gated adapter's polygon
source-set planner. Exact reuse chain in `build_object_manifest.py`:

- Line 23: `RUNNER_PATH = PREREG / "_cutout_runner_20260820" / "cutout_runner.py"`
- Line 24: `PINNED_ADAPTER_SHA256 = "267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f"`
- Lines 100-116: `_load_runner()` loads the runner by file-location import and asserts
  `module.ADAPTER_SHA256 != PINNED_ADAPTER_SHA256 -> ManifestBuildError`; `_adapter()` returns
  `_load_runner()._adapter()`.
- Lines 245-251 (the planner call — quoted verbatim):
    def plan_candidate_bricks(geometry: GeometryIndex, ls_id: str, ra: float, dec: float) -> list[str]:
        adapter = _adapter()
        candidate_rows = geometry.declination_candidates(dec, adapter.CANDIDATE_PREFILTER_DEG)
        safe_key = "SYNTH-OBJ-" + hashlib.sha256(ls_id.encode("utf-8")).hexdigest()[:24].upper()
        target = adapter.SyntheticCutTarget(safe_key, ra, dec)
        plan = adapter.plan_object(target, _GeometryView(candidate_rows))
        return list(plan["planned_bricknames"])

The polygon-intersection decision lives entirely inside the gated adapter
(`adapter/nm_brick_cutout_adapter.py:712 plan_object`, using `output_overlap_area_in_source_pixels` and
`INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2`). I verified the adapter file's real sha256 is exactly the pin
(`shasum -a 256` -> `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`).

No reimplemented geometry: the builder's only geometry-side work is `GeometryIndex.declination_candidates`
(bisect on `dec`, line 81-84), a narrowing pre-filter. It passes a SUPERSET to `plan_object`: any brick
within the adapter's angular-separation prefilter (`separation > CANDIDATE_PREFILTER_DEG -> continue`,
adapter line 741) necessarily satisfies |Δdec| ≤ CANDIDATE_PREFILTER_DEG, so the dec-only prefilter can
never exclude a brick the planner would select. The authoritative polygon inclusion still happens inside
the reused `plan_object`. No `TanWcs` / `overlap` / `intersect` / polygon math exists in the builder
(grep-confirmed). NOT a reimplementation.

## (2) Test suite — run by me, all pass

`python3 -m unittest test_build_object_manifest -v` from `_objmanifest_20260820/`:
5 tests, OK in 12.3s.
- `test_reuses_certified_planner_for_edge_corner_and_tjunction` ... ok
- `test_every_candidate_must_be_accepted_and_manifest_matches_runner_schema` ... ok
- `test_only_bricks_requires_candidate_set_to_be_within_subset` ... ok
- `test_receipts_are_hashed_from_the_same_snapshot_used_for_the_join` ... ok
- `test_same_inputs_produce_byte_identical_output` ... ok

The fixture exercises edge/corner/T-junction through the REUSED planner: the test calls
`builder.plan_candidate_bricks` (which calls `adapter.plan_object`) on round1 `edge_north_exact` and
`corner_north_east_exact`, and round5 `tjunction_exact` (the round5 fixture_manifest verifies a real DR10
row-offset T-junction at ra=175.40275, dec=-45.125, expected bricks tj-lower-east/tj-lower-west/tj-upper-span).
It also asserts `builder.planner_module_sha256() == builder.PINNED_ADAPTER_SHA256`. The fixture sidecars are
digest-verified via companion `.sha256` / `fixture_manifest.json` before planning. No stub planner.

## (3) Readiness semantics — verified in code and spot-checked

Code (build_object_manifest.py):
- Receipt filter (line 266): `if receipt.get("outcome") != "ACCEPTED" or receipt.get("digest_verified") is not True: continue`
  — only ACCEPTED + digest_verified receipts enter `accepted`. Conflicting accepted receipts for the same
  brick raise (line 278-279).
- Emission gate (lines 320-323): `missing = [b for b in bricknames if b not in accepted]; if missing:
  waiting += 1; ... continue` — an object is emitted ONLY when `missing` is empty, i.e. every candidate
  brick is ACCEPTED+digest_verified. Correct.

Spot-check vs CURRENT receipts snapshot (`/tmp/_tmp_kun_receipts_snapshot.jsonl`, 4739 ACCEPTED+digest_verified,
sha a9f11169..., taken 05:57:32Z):
- 5 READY objects (10995116290343288, ...344162, ...121193, ...121664, ...121668): every emitted brick is in
  receipts with matching sha256 and path under root — all True. (See note on `exists` below.)
- 5 WAITING objects (10995116291391783, ...391923, ...490086, ...492031, ...492081): each recomputed through
  `builder.plan_candidate_bricks` has ≥1 candidate brick absent from receipts — all True.

## (4) Schema conformance — load_brick_manifest parses; paths + sha verified

Imported `cutout_runner.load_brick_manifest` via importlib and called it on the freshly built manifest:
parsed OK, `objects = 15384`, no ContractError. The builder emits `schema_version: 1` and entries with exactly
`{brickname, path, row:{ra,dec}, sha256}`, matching the runner's BrickSpec constructor.

For the 5 spot-checked ready objects (and extended to ALL emitted objects):
- all emitted paths under `/Users/duhokim/NebulaMindData/dr10_south_image_r` : True
- all emitted sha256 == receipts' local_sha256 : True (all 15384 objects, every brick)
- Hash chain closed to real bytes for brick 0112m895: staged file bytes sha256 = receipt local_sha256 =
  manifest sha256 = `9bc20aff3f2e7b48d25384b67876e2d96f9e44a14294ca6bcd56953dfd825611`.

NON-BLOCKING OBSERVATION (path existence, not part of the gate's pass criteria): manifest `path` values are
`DEST/coadd/<...>` (the post-promotion layout), but the transfer is still RUNNING and bricks currently live
under `DEST/staging/coadd/<...>`. `load_brick_manifest` parses paths without requiring existence, so schema
conformance holds; the files resolve at the destination root only after the campaign promotes staging out.
The builder faithfully records each receipt's `destination_relative_path`; promotion is a downstream step,
not a builder defect.

## (5) Determinism — byte-identical across two runs

Ran the builder twice against the same frozen inputs (snapshot receipts a9f11169, official sidecar,
positions_runner_view.csv), outputs to two separate files:
- run1 manifest sha256 = a2bb4eb0e6888b6af1c3de2392206189598c839851df02bbfc014cda29ca7495
- run2 manifest sha256 = a2bb4eb0e6888b6af1c3de2392206189598c839851df02bbfc014cda29ca7495  (BYTE-IDENTICAL)
- run1/run2 summary JSON: identical.
(The shipped `manifest.json` from 14:52 has sha 5ba0afce...; it differs because it was built from the earlier
4683-accepted receipts snapshot — expected drift, not nondeterminism.)

## (6) Counts — recomputed from CURRENT receipts; drift is transfer progress

I rebuilt from the current snapshot myself (not the shipped summary). Fresh counts:
- objects_considered = 208407 (objects_total 208407, excluded_by_only_bricks 0)
- objects_ready   = 15384
- objects_waiting = 193023
- 15384 + 193023 = 208407 (consistent)
- accepted_bricks = 4739 ; receipts_sha256 = a9f11169628be7b1ce76c6b7b94ed26a78c79789e2954b1549371a87b162d228
  (equals my snapshot's sha — the summary hashed the same snapshot used for the join, as the
  `test_receipts_are_hashed_from_the_same_snapshot...` test enforces)

Drift vs shipped 14:52 summary (ready=15203, waiting=193204, accepted=4683): the transfer advanced
4683 -> 4739 between build and gate (heartbeat state RUNNING, last_brick advanced). Ready rose 15203->15384
(+181) and waiting fell 193204->193023 (-181): a symmetric ±181, exactly what newly accepted bricks completing
objects should produce. The missing-bricks top-10 histogram is identical across both builds (same bricknames,
same counts) — strong internal-consistency signal. The CODE logic (emit iff every candidate ACCEPTED+digest_verified)
is verified correct independent of the drift.

Pinned-input digests verified by me:
- adapter  nm_brick_cutout_adapter.py = 267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f (== pin)
- sidecar  survey-bricks-dr10-south.fits.gz = 863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a (== OFFICIAL_SIDECAR_SHA256)
- positions positions_runner_view.csv = 0edfdef08361f1606f714e59c0dd1472d4d13e357a75df2173824da1ca8ff8ab (== OFFICIAL_POSITIONS_SHA256)

## What I ran (evidence ledger)

- `shasum -a 256` on adapter, sidecar, positions, both receipts candidates, live receipts, snapshot, both
  run manifests, staged brick 0112m895.
- `python3 -m unittest test_build_object_manifest -v` (in-lane) -> 5/5 OK.
- Two full builder runs against `/tmp/_tmp_kun_receipts_snapshot.jsonl` -> exit 0/0, byte-identical output.
- `python3 /tmp/_tmp_kun_verify.py` -> schema OK; 5 ready + 5 waiting spot-checks; all-sha + all-under-root True.
- Reads: build_object_manifest.py, test_build_object_manifest.py, cutout_runner.py,
  adapter/nm_brick_cutout_adapter.py (plan_object/SyntheticCutTarget/SyntheticBrickGeometry regions),
  boundary_fixtures round5 fixture_manifest/objects.json, cross_check_yui_boundary.py (grep), campaign
  binding/heartbeat (NebulaMindData, read-only).

## Uncertainties / not inspected

- The transfer was RUNNING during the gate; the live receipts file advanced between my snapshot (a9f11169,
  4739) and now. Counts above are exact for the snapshot; re-run against a later snapshot will shift
  ready/waiting monotonically as more bricks land. Code logic is invariant to this.
- I did not open every emitted object (15384); I spot-checked 5 ready + 5 waiting per the brief, plus a
  whole-manifest all-sha/all-under-root sweep.
- Latent edge (did not trigger): if a position has zero intersecting bricks, `plan_object` raises
  `ObjectTerminalError` and the build aborts rather than counting that object as waiting. It did not occur on
  the real 208407-position run (15203+193204=208407, and my 15384+193023=208407). Worth knowing if positions
  are ever extended outside brick coverage; not a defect for the current input.

Findings-only: no files modified in the lane or repo. My only writes are this report and `/tmp/_tmp_kun_*` temps.

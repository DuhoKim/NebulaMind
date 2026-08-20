PASS_OBJECT_MANIFEST_REPAIRS

# KUN Object-Manifest Repair Re-gate — 2026-08-20

Gate seat: kimi (Nous route), fresh one-shot. Scope: ONLY the two repairs (R1 path rule +
fail-closed file-presence gate; R2 zero-intersecting-bricks waiting rule) to
`_objmanifest_20260820/build_object_manifest.py`. Prior gate: PASS_OBJECT_MANIFEST with 2 findings.
Repair receipt: `GPT2_OBJM_REPAIR_DONE.md`. Method: local files, grep, python3. No network.
Findings-only. Working dir: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg`

## Verdict

PASS_OBJECT_MANIFEST_REPAIRS. Both repairs verified in code and by execution. Quick confirmations:
planner reuse pin unchanged (adapter sha256 = 267b2a93...6006f == PINNED_ADAPTER_SHA256, re-hashed
by me), determinism preserved (two fresh full builds byte-identical), schema still conforms
(`load_brick_manifest` parses the emitted manifest, no ContractError).

## Repair 1a — R1 path rule (active_root matches the transfer's own rule) — PASS

Side-by-side code sites:

Builder `build_object_manifest.py:311`:
    active_root = destination_root / "accepted" if (destination_root / "accepted").exists() else destination_root / "staging"

Transfer `../_tori_transfer_20260819/nm_image_transfer.py:698` (receipt verification):
    path = self.accepted_root / relative if self.accepted_root.exists() else self.staging / relative
and `nm_image_transfer.py:709` (active-root sweep):
    active_root = self.accepted_root if self.accepted_root.exists() else self.staging
(with `self.staging = self.root / "staging"` / `self.accepted_root = self.root / "accepted"` at
lines 629-630, and finalization `os.replace(self.staging, self.accepted_root)` at line 997).

The builder mirrors the transfer's rule exactly: prefer `DEST/accepted` when it exists, else
`DEST/staging`. Emitted paths resolve under it: `receipt_paths = {brickname: active_root /
receipt.destination_relative_path ...}` (line 312-315), and entries emit
`"path": str(receipt_paths[brickname])` (line 358). Live root state right now:
`/Users/duhokim/NebulaMindData/dr10_south_image_r/` has `staging/` and NO `accepted/`, so
active_root = `.../staging` — matching the build receipt (`real_build_summary.json`).

Spot-check of 5 emitted objects (first/quarter/half/three-quarter/last of the 17173) — every
brick path resolves under active_root AND exists as a regular file on disk right now AND its
manifest sha256 equals the receipt's local_sha256:

- 10995116290343288 / 0112m895: under_root=True is_file=True sha==receipt=True
- 10995150754946243 / 0117m642: under_root=True is_file=True sha==receipt=True
- 10995183438010320 / 0174m537: under_root=True is_file=True sha==receipt=True
- 10995212540192429 / 0055m462, 0059m462: both under_root=True is_file=True sha==receipt=True
- 10997316775322957 / 0119m847, 0145m847: both under_root=True is_file=True sha==receipt=True

Extended to a whole-manifest sweep (all 17173 objects, 17173 brick entries): paths NOT under
active_root = 0; sha256 mismatches vs receipts = 0. Hash chain closed to real bytes: staged file
`staging/coadd/011/0112m895/legacysurvey-0112m895-image-r.fits.fz` hashes to
9bc20aff3f2e7b48d25384b67876e2d96f9e44a14294ca6bcd56953dfd825611 == manifest sha256 == receipt
local_sha256.

## Repair 1b — R1 fail-closed rule (receipt without file => waiting, never emitted) — PASS

Code: lines 316-318 compute `receipts_without_file = {brickname for brickname, path in
receipt_paths.items() if not path.is_file()}` over ALL accepted receipts before the object loop.
Lines 343-351: `missing_files = [brickname for brickname in bricknames if brickname in
receipts_without_file]`; when non-empty the object is counted waiting with reason
`RECEIPTED_FILE_MISSING` and `continue` — it can never reach the emission block (lines 352-362),
which only runs when both `missing` and `missing_files` are empty. The code comment at lines
344-347 states the rule verbatim, and the summary records `receipts_without_file` plus a
deterministic `waiting_reason_histogram`.

Temp fixture constructed by me (independent of the shipped tests): one position at the round1
centre brick, one ACCEPTED + digest_verified receipt for that brick, NO file written. Result:
emitted objects = [] (empty), objects_ready = 0, objects_waiting = 1, receipts_without_file = 1,
waiting_reason_histogram = {"RECEIPTED_FILE_MISSING": 1}. A receipt pointing at a nonexistent file
yields waiting, never emitted. The shipped test
`test_active_root_prefers_accepted_and_missing_receipted_file_waits` additionally proves the
accepted-preferred branch (staging-phase emit with paths under `DEST/staging`, then with
`DEST/accepted` present and one omitted file: objects = {}, histogram {"RECEIPTED_FILE_MISSING": 1}).

## Repair 2 — R2 zero-intersecting-brick position waits, never aborts — PASS

Code (lines 326-333): `plan_candidate_bricks` is called inside `try`; only
`adapter.ObjectTerminalError` with `exc.code == "FAILED_PLAN_NO_SOURCES"` is translated to
waiting + `waiting_reason_histogram["ZERO_INTERSECTING_BRICKS"] += 1` + `continue`. Any other
planner terminal error re-raises (line 329-330 `if exc.code != "FAILED_PLAN_NO_SOURCES": raise`)
— fail-closed preserved for non-R2 errors.

Ran the added test: `python3 -m unittest test_build_object_manifest -v` from
`_objmanifest_20260820/` => 7/7 OK in 16.6s, including
`test_zero_intersecting_bricks_waits_without_aborting_build ... ok`. That test places a
zero-intersection position (ra=10.0, dec=0.0, outside the fixture's brick coverage) before a
valid position; the build completes, emits only the valid object, and records
{"ZERO_INTERSECTING_BRICKS": 1}. Production impact: the fresh production histogram is
{"MISSING_ACCEPTED_BRICKS": 191234} — no zero-intersection objects in the current 208407
positions, consistent with the prior gate's observation that the abort never triggered on real
input.

## Quick confirmations (previously passed items, not re-litigated)

- (4) Determinism: ran the builder twice myself against the frozen inputs
  (positions_runner_view.csv sha 0edfdef0..., repair_receipts_snapshot.jsonl sha 4c9d1bff...,
  sidecar sha 863e5ded...). Both full runs: manifest sha256 =
  bbc5b3a7a39c1c172ceb15661f0054c73c661abd265ff16f38372b6210ce3d78 (byte-identical, cmp clean);
  summary sha256 = 5e25d93b62a191cbd2afc7916cfc2485ca0b50fe4e25f8bca73c3ddd825acee2
  (byte-identical). My rebuild is also byte-identical to the shipped `manifest.json` and
  `real_build_summary.json` — reproduces the repair receipt's recorded digests exactly.
- (5) Schema: imported `cutout_runner.load_brick_manifest` (via importlib, from
  `_cutout_runner_20260820/cutout_runner.py`) and parsed the shipped manifest.json: OK,
  objects = 17173, entries are BrickSpec instances, NO ContractError.
- Planner reuse: adapter file re-hashed by me = 267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f
  == PINNED_ADAPTER_SHA256 (build_object_manifest.py:24) and == summary planner_module_sha256.
  The planner call site (lines 245-251) is unchanged from the gated version.
- Fresh counts reproduced from my own runs: objects_total/considered = 208407/208407,
  ready = 17173, waiting = 191234 (17173+191234=208407), accepted_bricks = 5307,
  receipts_without_file = 0 — all equal to the repair receipt.

## What I ran (evidence ledger)

- `shasum -a 256` on adapter, sidecar, positions, receipts snapshot, staged brick 0112m895,
  both fresh manifests/summaries, shipped manifest/summary pairs.
- `python3 -m unittest test_build_object_manifest -v` (in-lane) -> 7/7 OK.
- Two full builder runs -> /tmp/_kun_regate_run{1,2}.json + summaries; cmp byte-identical;
  cmp vs shipped manifest.json / real_build_summary.json identical.
- Whole-manifest sweep script: 17173 objects; 0 paths outside active_root; 0 sha mismatches;
  5-object is_file/under-root/sha spot-check all True.
- Temp fail-closed fixture (receipt without file) -> waiting, RECEIPTED_FILE_MISSING, never emitted.
- `load_brick_manifest(manifest.json)` -> 17173 objects, no ContractError.
- Reads: build_object_manifest.py, test_build_object_manifest.py,
  _tori_transfer_20260819/nm_image_transfer.py (lines 625-633, 690-720, 995-1005),
  KUN_OBJMANIFEST_GATE_20260820.md, GPT2_OBJM_REPAIR_DONE.md, real_build_summary.json.

## Uncertainties / not inspected

- The transfer campaign is still RUNNING; a rebuild against a newer receipts snapshot will shift
  ready/waiting monotonically (repair snapshot: 5307 accepted). Code logic is invariant to this.
  If `DEST/accepted` appears at finalization, the active_root rule flips emitted paths to
  `accepted/` on the next build — the intended mirror of the transfer's behavior, not a defect.
- I did not re-run the full planner-level edge/corner/T-junction geometry verification from the
  prior gate beyond the shipped test suite (which exercises it and passed 7/7); the planner file
  is byte-identical to the gated pin.

Findings-only: no files modified in the lane or repo. My only writes are this report and
/tmp/_kun_regate_* temps.

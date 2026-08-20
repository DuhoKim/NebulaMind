GPT2_OBJM_REPAIR_COMPLETE ready=17173 waiting=191234 receipts_without_file=0

# GPT2 object-manifest repair receipt

Both recorded findings are repaired.

## R1 — transfer-aligned paths and file-presence gate

- The builder now uses the transfer's exact active-root rule: `DEST/accepted` when it exists, otherwise `DEST/staging`.
- Emitted paths resolve under that active root.
- Emission is fail-closed: every planned brick must have an ACCEPTED, digest-verified receipt and an existing regular file under the active root at build time.
- A receipt without its file makes the object wait with reason `RECEIPTED_FILE_MISSING`; it is never emitted from receipt evidence alone.
- The build receipt records `active_root`, `emission_rule`, `receipts_without_file`, and a deterministic `waiting_reason_histogram`.
- Fresh frozen-snapshot result: `receipts_without_file=0`; every emitted manifest path was independently checked with `Path.is_file()` and all passed.

## R2 — zero-intersection positions wait instead of aborting

- Only planner `ObjectTerminalError(code="FAILED_PLAN_NO_SOURCES")` is translated to waiting reason `ZERO_INTERSECTING_BRICKS`.
- Other planner terminal errors still propagate fail-closed.
- The new fixture includes one zero-intersection position followed by a valid position; the build completes, excludes the zero-intersection object, emits the valid object, and records `{"ZERO_INTERSECTING_BRICKS":1}`.
- The current production positions contain no zero-intersection objects, so the fresh production histogram is `{"MISSING_ACCEPTED_BRICKS":191234}`.

## Fresh build receipt

- objects total/considered: 208407 / 208407
- objects ready: 17173
- objects waiting: 191234
- accepted bricks: 5307
- receipts without file: 0
- active root: `/Users/duhokim/NebulaMindData/dr10_south_image_r/staging`
- receipts snapshot SHA-256: `4c9d1bff1f8abd40375b405ae227e6208fc7475535840cb69bc047f4fd56c4a0`
- manifest SHA-256: `bbc5b3a7a39c1c172ceb15661f0054c73c661abd265ff16f38372b6210ce3d78`
- pinned reused planner SHA-256: `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`
- build wall time: 210.35 seconds

## Verification

- `python3 -m unittest -v test_build_object_manifest.py`: 7/7 PASS.
- Frozen-input full builds: `manifest.json` and `manifest.repeat.json` are byte-identical.
- Frozen-input build receipts: `real_build_summary.json` and `real_build_summary.repeat.json` are byte-identical.
- Pinned planner hash is unchanged and still matches the gate pin.
- `cutout_runner.load_brick_manifest` loaded all 17173 emitted objects.
- Emitted non-file paths: 0.
- No network was used.

Artifacts remain in `_objmanifest_20260820/`; the re-emitted current manifest is `_objmanifest_20260820/manifest.json`.

# Manifest-closure check — CODEX referee report

## Executive result

The honest-path repair works on the pinned real geometry: the two historical objects require five distinct bricks; the complete five-brick manifest passes; omitting `3471m885` or `2857m870` is refused by `ManifestClosureError`, naming the omitted brick. The closure is nevertheless not safe as a download gate because its two supposed external witnesses remain caller-authored, and the reported planner digest does not bind all executable code that determines the answer.

## Numbered findings

### 1. BLOCKER — a shortened parent with a regenerated digest still passes, while the canonical BS-2s receipt cannot be consumed

**Symbol / quoted line.** `close_manifest()` accepts both `expected_parent_digest` and `selection_receipt` (`successor_ref_v4.py:261-263`), then accepts any dictionary whose `slot` is `BS-2s` and whose top-level `parent_digest` equals the supplied digest (`284-291`). But `SLOT_SCHEMA["BS-2s"]` does not contain `parent_digest` (`138-143`), and `receipt()` returns only envelope metadata and hashes, not the body fields (`161-177`).

**Executed failure.** I removed one of the two historical parents, regenerated `parent_digest()` on that one-row table, supplied `{'slot':'BS-2s','parent_digest': <regenerated>}`, and supplied its exact two-brick closure. `close_manifest()` passed with `objects=1`, `required_count=2`, `manifest_count=2`, parent digest `7c3f5890…`. Conversely, a canonical `receipt('BS-2s', ...)` had keys only `body_sha256`, `envelope_sha256`, `environment`, `schema`, and `slot`, and `close_manifest()` refused it because it had no `parent_digest`.

**Why it fails.** The comparison proves only consistency among three values authored in the same call. It does not prove that the parent table is the complete catalogue export for the selected bricks. The exact shortened-parent route named in question 3 therefore remains open, and the only receipt producer in the reviewed reference cannot drive the production closure at all.

**Smallest sufficient repair.** Introduce a canonical, parseable parent-export custody receipt that binds at least the selected-brick digest, catalogue query/export bytes digest, row count, and `parent_digest`. Retain and validate its typed body and recompute its body/envelope digests on consumption. Remove `expected_parent_digest` from the public call and obtain it only from that validated receipt; reject bare dictionaries. If this is folded into BS-2s instead, amend the BS-2s schema and chronology so the selected-brick receipt is completed only after the catalogue export is sealed.

### 2. BLOCKER — the geometry used to compute closure is not bound to the pinned sidecar

**Symbol / quoted line.** `close_manifest()` compares the caller's `universe_sha256` string to the constant and checks only `len(geometry.by_name)` (`successor_ref_v4.py:273-283`). It never checks `geometry.sidecar_sha256`, never loads the sidecar itself, and accepts any object exposing `by_name` and `declination_candidates()`.

**Executed failure.** I passed a geometry facade whose `by_name` was the real 366,912-entry mapping but whose `declination_candidates()` filtered out `3471m885` and `2857m870`; its declared `sidecar_sha256` was deliberately `not-the-pinned-sidecar`. I still supplied the pinned digest string. The frozen planner then returned only `['3385m885']` and `['2894m872','2902m870']`, and `close_manifest()` passed that genuinely short three-brick manifest with zero missing and zero extra.

**Why it fails.** The value checked as the universe digest is not a digest of the geometry object that actually answers planner queries. Cardinality does not establish byte identity or query integrity. This directly reopens the substituted/shortened-universe route in question 3 and reproduces both historical omissions under a passing closure.

**Smallest sufficient repair.** Make `close_manifest()` accept the sidecar path or bytes, call the frozen module's `load_geometry_sidecar()` internally, and require the resulting `sidecar_sha256` to equal `PINNED_UNIVERSE_SHA256`. Remove the separately supplied digest/count assertions. Also require every planned brickname to exist in the loaded `GeometryIndex.by_name` before comparing the manifest.

### 3. BLOCKER — `frozen_planner_digest()` is not a digest of all code that runs, and altered planner configuration can retain the same digest

**Symbol / quoted line.** `_frozen_planner()` imports `build_object_manifest.py` (`successor_ref_v4.py:219-230`). `frozen_planner_digest()` hashes that module plus the text of `PINNED_ADAPTER_SHA256` (`239-243`), but `plan_candidate_bricks()` calls `_adapter()`, which first loads `_cutout_runner_20260820/cutout_runner.py` (`build_object_manifest.py:100-121,245-251`). The runner bytes are neither pinned by the builder nor included in `frozen_planner_digest()`. Worse, `_load_runner()` returns a pre-existing `sys.modules['nm_objmanifest_pinned_runner']` before checking even its declared adapter pin (`build_object_manifest.py:100-103`).

**Executed failure.** In a fresh process I measured the honest planner digest as `36bbbf2502159474e0a56ec904e924e2ee80645b485c2ee20208ef25a514f610`. I then preloaded that module name with a runner whose adapter returned `['forged-only']` for every object. With the real sidecar and both historical parents, `close_manifest()` passed the one-brick manifest `['forged-only']`. `frozen_planner_digest()` remained byte-for-byte the same `36bbbf250215…` before and during the substituted execution.

**Why it fails.** The adapter itself is the right semantic authority on the honest path: its measured SHA-256 is the pinned `267b2a93…`, and it applies the polygon-intersection planner. But the binding is incomplete. The reported digest omits the runner/import path that selects that adapter and can therefore attest to code different from what produced the plan. This answers question 4 negatively.

**Smallest sufficient repair.** Pin and verify the runner file's SHA-256 before import; do not accept an unverified cached module. Define one sealed planner bundle whose digest includes the exact bytes of `build_object_manifest.py`, `cutout_runner.py`, `nm_brick_cutout_adapter.py`, and all configuration constants that affect planning. Make both planning and digest reporting use that same already-verified bundle. Add a negative test that preloads each module name and proves substitution is refused.

### 4. MAJOR — the relevant historical-omission fixture does not call the production closure

**Symbol / quoted line.** `run_fixtures()` labels `CLOSURE-CATCHES-HISTORICAL` as a closure catch, but it only computes `missing_named = sorted(set(req) - set(short))` and compares that list to the expected names (`successor_ref_v4.py:1268-1274`). It never invokes `close_manifest()` for the complete or shortened candidates.

**Why it fails.** This fixture cannot detect a recurrence in the manifest-comparison path, receipt checks, geometry binding, or exception result. It repeats the exact test/production separation highlighted in the brief. My independent end-to-end calls establish that the present honest path does refuse each omission, but the pinned fixture does not protect that fact.

**Smallest sufficient repair.** Replace the set-difference assertion with three actual `close_manifest()` calls over the loaded real geometry: complete manifest must pass, and each one-brick omission must raise `ManifestClosureError` with that exact name in both the message and `result['missing_from_manifest']`. Use the repaired canonical parent receipt, not a bare dictionary.

### 5. MAJOR — malformed or uncovered inputs escape as unrelated exception types rather than one clean closure refusal

**Symbol / quoted line.** Conversion and planning occur without an input-schema boundary or exception normalization (`successor_ref_v4.py:273-317`). The `if not bs` guard at `308-309` cannot normalize the frozen adapter's no-source case because the adapter raises before returning an empty list.

**Executed failures.** `universe_bricks='not-an-int'` raised raw `ValueError`; scalar parent arrays raised raw `TypeError: len() of unsized object`; `manifest_bricknames=None` raised raw `TypeError`; Dec `91` raised adapter-construction `ValueError`; and a valid-shaped northern coordinate with no DR10 South source raised the adapter's `ObjectTerminalError`. Duplicate manifest entries did cleanly raise `ManifestClosureError`.

**Why it fails.** A production caller cannot handle all refusals through the advertised `ManifestClosureError` result contract, and an uncovered or malformed catalogue row can abort a batch without a structured object/name receipt. This is fail-closed but operationally unusable for the affected input and answers question 5 affirmatively.

**Smallest sufficient repair.** Validate array rank, equal nonzero lengths, integral unique IDs, finite RA in `[0,360)`, finite Dec in `[-90,90]`, manifest type/content, and integer universe metadata before planning. Catch the planner's declared terminal/no-source exception per object and raise `ManifestClosureError` with the object ID and structured result. Normalize caller-data conversion failures likewise while allowing genuine system faults to propagate.

## Positive checks and exact execution results

1. Pinned hashes matched:
   - `successor_ref_v4.py`: `0b312c96db0b4551bcafd554b4bdd7124d3104cef4cc7f405eea3f849e08e21c`
   - `FIXTURES_V4_20260825.out`: `6b14d8a69b606cbf5ddb6d0e82f856a08d6a5928227c3cba4956a1c02636e436`
2. The real sidecar loaded through the frozen loader with SHA-256 `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a` and 366,912 rows.
3. Honest planner output:
   - `10997315463551936` -> `['3385m885','3471m885']`
   - `10995116744378804` -> `['2857m870','2894m872','2902m870']`
4. Complete five-brick manifest passed with `objects=2`, `required_count=5`, `manifest_count=5`, zero missing/extra.
5. Omitting `3471m885` raised `ManifestClosureError` saying `missing 1 ['3471m885']`; omitting `2857m870` likewise named `['2857m870']`.
6. Duplicate entries were refused by `ManifestClosureError`.
7. The retired `plan_object_bricks()` is not called by `close_manifest()` and raises if invoked.

## Testimony

Not independently established and not used to support the verdict: the brief's historical 60,308/60,310 account, the projected 77 GB transfer size, and the historical claim that this exact builder file is byte-identical to what the predecessor executed. The scoped code does establish that the honest current chain reaches the SHA-pinned adapter's polygon planner; it does not establish historical execution provenance.

I did not read `/Users/duhokim/NebulaMindData/`. All real-geometry reads used the already-acquired sidecar under `_tori_parent_row_count_evidence/.../static/`.

The blocking findings are 1 (parent custody bypass), 2 (unbound geometry), and 3 (planner digest/runtime substitution).

**NOT CLEAR**
# Manifest-closure check — GPT56 referee report

Verdict: NOT CLEAR. The clean, unmodified path now derives the correct five-brick closure for the two historical objects and refuses either historical omission by name. The mechanism is nevertheless bypassable through caller-authored custody and geometry inputs, and its reported planner digest can remain unchanged while different planner code runs.

## Numbered findings

### 1. BLOCKER — the selected parent is not held by a verified receipt; a shortened parent with regenerated values passes

**Symbol / quoted lines.** `close_manifest()` accepts `expected_parent_digest` and `selection_receipt` from the caller, then checks only `selection_receipt.get("slot") == "BS-2s"` and `selection_receipt.get("parent_digest") == expected_parent_digest` (`successor_ref_v4.py:261-304`). `SLOT_SCHEMA["BS-2s"]` does not contain `parent_digest`, and `receipt()` returns only receipt metadata and hashes, not the supplied fields (`successor_ref_v4.py:138-177`).

**Why it fails.** On the real 366,912-row sidecar, I removed the second historical object, regenerated `parent_digest`, supplied `{"slot":"BS-2s","parent_digest":<regenerated>}`, and supplied the two bricks required by the remaining object. `close_manifest()` passed with `objects=1`, `required_count=2`, and `manifest_count=2`; all three bricks needed only by the omitted parent disappeared without a refusal. The canonical BS-2s receipt cannot repair this: its emitted keys were only `body_sha256`, `envelope_sha256`, `environment`, `schema`, and `slot`, so it was refused for lacking the top-level parent digest; attempting to add `parent_digest` to its canonical field set was itself refused as an extra field. Thus the passing input is a receipt-shaped caller assertion, not custody of the selected parent.

**Smallest sufficient repair.** Add the selected-parent artifact digest, object count, and `parent_digest` to a canonical BS-2s payload that is retained/decoded and whose body and envelope hashes are recomputed by the consumer. Accept only that validated receipt and load the parent artifact it identifies; do not accept a separately supplied digest or bare dictionary. Add a negative test that removes one selected object, regenerates every downstream value, and must refuse.

### 2. BLOCKER — the geometry object that determines the answer is not bound to the pinned sidecar

**Symbol / quoted lines.** `close_manifest()` compares the caller's `universe_sha256` string with `PINNED_UNIVERSE_SHA256` and checks only `len(geometry.by_name)` against 366,912 (`successor_ref_v4.py:273-283`). It never reads or compares `geometry.sidecar_sha256`, never hashes the geometry it actually traverses, and passes that caller-supplied object directly to `frozen_plan_object()` (`successor_ref_v4.py:307`).

**Why it fails.** I supplied a geometry object whose `sidecar_sha256` was literally `NOT_THE_PINNED_SIDECAR`, whose `by_name` mapping was padded to 366,912 keys, and whose candidate method exposed only the home row `3385m885` for historical object 10997315463551936. Supplying the pinned digest string separately allowed a one-brick manifest to pass with `required_count=1`; required neighbour `3471m885` was absent. Cardinality plus a caller-authored digest label does not bind the rows used by the planner.

**Smallest sufficient repair.** Make the production closure entry point accept the sidecar path/artifact, load it internally with the frozen loader, and verify the bytes against `PINNED_UNIVERSE_SHA256` before constructing a non-substitutable geometry index. At minimum require the expected concrete geometry type, verify its source digest, prevent post-load mutation, and bind the exact artifact digest into the result. Add a padded-substitute geometry negative test.

### 3. BLOCKER — `frozen_planner_digest()` is not a digest of all code that runs, and no expected planner digest is enforced

**Symbol / quoted lines.** `_frozen_planner()` dynamically executes `build_object_manifest.py` (`successor_ref_v4.py:219-230`). `frozen_planner_digest()` hashes that file plus the text of `PINNED_ADAPTER_SHA256` (`successor_ref_v4.py:239-243`), but `plan_candidate_bricks()` executes through `_load_runner()._adapter()` (`build_object_manifest.py:100-121,245-251`). The intervening `cutout_runner.py` bytes are omitted, and `_load_runner()` returns an existing `sys.modules["nm_objmanifest_pinned_runner"]` before validating it. `close_manifest()` reports the resulting digest but never compares it to an approved constant.

**Why it fails.** With no file edits, I replaced that module-cache entry with an adapter returning `['ATTACK-BRICK']`. `frozen_plan_object()` then returned `['ATTACK-BRICK']`, while `frozen_planner_digest()` remained exactly `36bbbf2502159474e0a56ec904e924e2ee80645b485c2ee20208ef25a514f610` before and after. Measured component hashes were `c63030e2878bbea126ef32de1e3687bdf550457aa0cbf31c02fc1743e5e369ed` for `build_object_manifest.py`, `ccb9b8fed457333669e54fa9f0a3dac645dc866a56c6cd8dc665ffd4d93b1bcc` for `cutout_runner.py`, and `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f` for the adapter. The clean planner is the correct operational authority, but the current binding does not prove that authority was what ran.

**Smallest sufficient repair.** Pin and verify before execution the exact hashes of `build_object_manifest.py`, `cutout_runner.py`, the adapter, and all effective planner configuration; include those verified bytes/digests in one transitive planner digest and compare it to a frozen expected value. Do not trust pre-existing module-cache objects; load into an isolated namespace or verify the cached module's file and callable identity before reuse. Add a changed-runner/cache-substitution negative test requiring refusal before planning.

### 4. HIGH — several invalid or zero-coverage inputs escape as unstructured exceptions rather than clean closure refusals

**Symbol / quoted lines.** The function raises plain `RuntimeError` for malformed/duplicate parents and expects `if not bs` to catch zero plans (`successor_ref_v4.py:292-309`), but the frozen adapter raises `ObjectTerminalError(code="FAILED_PLAN_NO_SOURCES")` before returning an empty list. Other conversions and iterations are not normalized.

**Why it fails.** Executed probes produced unstructured `RuntimeError` for unequal lengths and duplicate parent IDs, `TypeError: len() of unsized object` for scalar parents, `ValueError` for a nonnumeric universe count, and `TypeError: 'NoneType' object is not iterable` for a null manifest. A valid coordinate outside the south-sidecar coverage raised uncaught `ObjectTerminalError` with `FAILED_PLAN_NO_SOURCES`, so the intended zero-brick refusal branch is unreachable for the frozen planner. Duplicate manifest entries did correctly return `ManifestClosureError` with counts.

**Smallest sufficient repair.** Validate input container rank, equal nonzero lengths, finite/ranged coordinates, integral IDs/counts, and manifest iterability before planning. Catch the planner's expected terminal no-source error and convert every refusal into `ManifestClosureError` with a stable code and structured result; reserve unexpected exceptions for genuine internal faults. Add one test per malformed class and a real-sidecar zero-coverage object.

## Positive executed evidence

- `successor_ref_v4.py` SHA-256 is the required `0b312c96db0b4551bcafd554b4bdd7124d3104cef4cc7f405eea3f849e08e21c`.
- `FIXTURES_V4_20260825.out` SHA-256 is the required `6b14d8a69b606cbf5ddb6d0e82f856a08d6a5928227c3cba4956a1c02636e436`.
- The real sidecar SHA-256 is `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a`, and its loaded index contains 366,912 distinct names.
- Clean execution planned `['3385m885','3471m885']` for 10997315463551936 and `['2857m870','2894m872','2902m870']` for 10995116744378804. Their complete five-brick manifest passed. Removing `3471m885` produced a `ManifestClosureError` naming `['3471m885']`; removing `2857m870` likewise named `['2857m870']`.
- The retired `plan_object_bricks()` is no longer called by `close_manifest()` and now refuses if invoked.

## Testimony

The two relevant fixture statements are weaker than their wording suggests. `CLOSURE-PRODUCTION-USES-FROZEN` is an `inspect.getsource()` substring check, not production-path execution. `CLOSURE-CATCHES-HISTORICAL` computes a Python set difference over planner outputs but never calls `close_manifest()` with the complete or shortened manifests (`successor_ref_v4.py:1254-1274`). The positive end-to-end result above was independently executed, but the shipped fixture output itself does not support those production-path claims and contains no negative coverage for Findings 1-4.

Blocking findings: 1 (parent custody bypass), 2 (substituted geometry bypass), and 3 (planner execution/digest substitution).

**NOT CLEAR**
# CLOSURE RECEIPT — GPT56

## Verdict

The closure check is **not safe to authorize the queued download**. Blocking findings are F1 (the caller supplies the purportedly independent count oracle), F2 (the caller supplies the selection that defines which oracle rows matter), F3 (the caller supplies unauthenticated parent identities and coordinates), and F4 (the digest can clear while different live planner code executes). C01–C04 are real failures, not fixture artefacts. The C04 contract dispute is rejected for this gate because no independently bound upstream parent artifact is named or enforced.

## Scope and custody

I based the ruling only on the current brief and the artifacts it names. A repository search for the named symbols exposed filenames and short snippets from nonbinding sibling/temporary artifacts; I did not open them and excluded those snippets from the ruling. I did not read `/Users/duhokim/NebulaMindData/`. Independently computed SHA-256 values include:

- `closure_probe_suite.py`: `2dd141b48e74115f4fc6be4ba5cd8bd74a3c4e208565995d60af98a880b11e69`
- `../ref/successor_ref_v4.py`: `8191c42be1e8153e80480c0d110eb03c8f9c92f91895692e333af3fcbef50a21` — matches the brief
- `../../_objmanifest_20260820/build_object_manifest.py`: `c63030e2878bbea126ef32de1e3687bdf550457aa0cbf31c02fc1743e5e369ed`
- `../acquire/DOWNLOAD_QUEUE_PLAN_20260825.md`: `ddc0794aacde2cb8048ef948663702ef8459e6f910a93a74bd93dc14910b8fef`

## Reproduction

1. Two independent `--fast-geometry` runs each produced 18/22 conforming, exactly C01–C04 non-conforming, no error-typed probes, and the same stable hash:

   `1f03ada3e55990f6581ae036087b34dadec2c03ab56ebcd3c9e36720fec40b94`

2. That does **not** match the brief's stated fast-mode hash `3abf01ae...`. I independently transformed the shipped production stable block by changing only `geometry_mode` and appending the suite's exact `FAST_MODE_CAVEAT`; the resulting canonical hash is `1f03ada3...`, exactly my two runs. Thus the fast run is reproducible against the current suite and shipped stable block; the fast hash quoted in the brief is stale or was produced from a different stable block.

3. I independently canonicalized the shipped production receipt's `stable` object. Its recomputed hash is `43f2a1226728b868bb29ed59914337efc6cbd7c88888bdd2ab844b1d8d37910f`, exactly its stored value.

4. A default, uncached `--only P01` run cleared cleanly. Two attempts at the full uncached run were terminated by this executor's 180-second background-process ceiling before a receipt was emitted; this is a limitation of my execution lane, not an observed exception from `close_manifest()`. I therefore do not claim an independent full-production-run reproduction.

## Numbered findings

### F1 — CRITICAL — the count oracle is caller-controlled, so I1 fails (C01 and C03)

**Symbol/line:** `close_manifest(parent_csv, selection_npz, oracle_npz, manifest_bricknames)`, especially `ora_p = _P(oracle_npz)` and `ora = np.load(ora_p)` (`successor_ref_v4.py:317,342,355`).

**Why it fails:** `PINNED_COUNTS_SHA256` exists, but `close_manifest()` never hashes `oracle_npz` against it. It checks only `sum(n_eligible) == PINNED_COUNT_TOTAL`. C01 removes a parent row, changes that selected brick's count from 1 to 0, and moves the unit to the filler row. The total remains 832,393 and every checked per-selected-brick count balances. C03 proves that reaching the same caller-controlled bytes through symlinks changes nothing. Both accept a shortened manifest whose completeness rests on an oracle nominated and edited by the caller. This is the exact I1 defect, not a probe artefact.

**Smallest sufficient repair:** add `load_pinned_counts()` analogous to `load_pinned_geometry()`: use a fixed relative path, recompute and enforce `PINNED_COUNTS_SHA256`, validate its schema, and remove `oracle_npz` from `close_manifest()`'s public parameters. A digest supplied by the caller is not sufficient.

### F2 — CRITICAL — the selection is caller-controlled, so C02 independently defeats I1

**Symbol/line:** `sel_p = _P(selection_npz)` and `sel = np.load(sel_p)` (`successor_ref_v4.py:342,348`).

**Why it fails:** C02 removes the second parent row, reduces the selection to the remaining brick, and supplies a matching oracle. All artifacts agree only because the same caller chose all of them. Pinning the full oracle alone would block this exact fixture if the full oracle has the omitted brick's count, but the mechanism still needs an independent statement of the authorized 6,445-brick selection; otherwise the caller chooses which oracle rows enter the proof.

**Smallest sufficient repair:** remove arbitrary `selection_npz` custody. Load a fixed, digest-pinned authorized selection artifact, or derive the selection inside the check from the independently pinned selection-stage record. The expected digest/path must be fixed outside this call, not supplied alongside the candidate.

### F3 — CRITICAL — parent row contents are unauthenticated, so C04 is in contract and real

**Symbol/line:** `par_p = _P(parent_csv)` followed by CSV parsing into `(ls_id, ra, dec)` (`successor_ref_v4.py:342,368-383`).

**Why it fails:** the count oracle authenticates only a count per brick. It does not authenticate which release objects occupy those rows or their coordinates. C04 preserves the per-brick count while replacing the second release object with an unused `ls_id` and the first object's coordinates. `close_manifest()` plans from those supplied rows and accepts the understated candidate manifest.

The dispute note does not move this outside the present gate. The brief defines the mechanism as computing the complete image list “from the galaxies themselves,” I1 says a path handed in by the caller is not independent, and no named upstream artifact binds the parent contents. Moving responsibility upstream without naming and enforcing that binding leaves the download with the same hole.

**Smallest sufficient repair:** load/derive the parent from an independently frozen catalogue extraction at a fixed path and verified digest, or verify every `(ls_id, brickid, ra, dec)` against an independently pinned release-catalogue artifact. Remove arbitrary `parent_csv` custody. A caller-supplied parent digest would recreate the earlier seam.

### F4 — CRITICAL — the pinned digest does not bind the live planner callable, so I2 fails

**Symbol/line:** `frozen_planner_digest()` hashes source-file bytes and `repr(ad.CANDIDATE_PREFILTER_DEG)` (`successor_ref_v4.py:246-261`), while `frozen_plan_object()` later executes the adapter obtained through the cached runner (`successor_ref_v4.py:240-243`; `build_object_manifest.py:100-116,245-251`).

**Why it fails:** R10 mutates only `CANDIDATE_PREFILTER_DEG`, the one live value explicitly included in the digest. It does not test mutation of the live callable. I replaced the already loaded adapter's `plan_object` in memory with a function returning `['0001p000']`. `require_pinned_planner()` still returned the pinned digest `82971b80...`, and `frozen_plan_object()` then executed the replacement and returned `['0001p000']`. Different answer-producing code therefore executes under an accepted digest.

**Smallest sufficient repair:** execute the planner in a fresh isolated process/module graph loaded only after file verification, or bind and verify the actual live callable (code object, defaults, closures and answer-affecting globals) and retain that verified callable reference for the entire plan. Re-importing from shared cached modules after checking disk bytes is insufficient. Add a negative probe that replaces `adapter.plan_object`, not just its prefilter constant.

### F5 — MAJOR — I4 is stronger than what the E-probes establish

**Symbol/quoted line:** trailing handler returns `ManifestClosureError(..., {"error": type(exc).__name__})` (`successor_ref_v4.py:437-441`); suite conformance checks only `actual == "REFUSE"` unless a message substring is declared (`closure_probe_suite.py:492-500`).

**Why it fails:** E02–E05 prove one refusal type, but they do not prove that the refusal carries “the numbers a receipt needs.” For those paths the structured result contains only an error-type string. The suite also drops every probe's `result`, so its receipt cannot inspect structured refusal payloads at all.

**Smallest sufficient repair:** define the minimum structured refusal schema by phase (error code, phase, verified input hashes and every count known at failure), enforce it in `ManifestClosureError`, retain `result` in the probe receipt, and assert the required keys. If no numeric values exist before parsing, narrow I4's wording rather than claiming the present E-probes prove it.

### F6 — MODERATE — probe metadata/code fidelity discrepancies

I read all 22 decorated bodies. The following discrepancies must be named; none explains away C01–C04:

- **R09:** metadata declares only a parent-row omission with oracle and selection untouched, but code also changes the candidate manifest from `all_required` to `first_required`.
- **R10:** its own label accurately describes a planner-digest control, but it calls `require_pinned_planner()` directly rather than the production `close_manifest()` entry point, contrary to the suite-level claim that every probe calls that entry point.
- **R11:** metadata declares only a duplicate selection entry, but code also passes `first_required` instead of the baseline manifest. The duplicate check occurs first, so the conforming refusal remains meaningful.
- **G01:** metadata says the actual planner digest is recorded for reviewer comparison. The body returns it, but `classify()`'s `result` is discarded when rows are built. The stable receipt records the pinned constant, not G01's returned value. PASS still shows that `require_pinned_planner()` did not refuse, but the claimed recording does not occur.
- **C01:** code also reduces the candidate manifest to `first_required`; that necessary variation is omitted from metadata.
- **C02:** code also reduces the candidate manifest; metadata says “all three inputs” even though the public entry point has four inputs and the fourth changed.
- **C03:** inherits C01's undeclared reduced manifest in addition to changing path form.
- **C04:** code also reduces the candidate manifest to the understated `first_required`; metadata describes the understated derived set but does not declare the candidate-manifest change.
- **E02:** `b"not an npz file"` is 15 bytes, not the declared 16.
- **E04:** code replaces the two fields with text **and** drops the second honest parent row. Numeric parsing fails first, so the intended malformed-field behavior is still exercised.

P01, R01–R08, E01, E03 and E05 have metadata faithful to their bodies. R09's, R11's and E04's extra changes are downstream or unreachable before the intended refusal and do not invalidate those particular conforming outcomes. The undeclared candidate-manifest reductions in C01–C04 should be repaired in metadata because they are essential to demonstrating acceptance of a coherent but shortened package.

### F7 — MODERATE — the brief's fast-mode reproduction hash is not for the current stable block

**Quoted line:** brief lines 77–79 state `3abf01ae66a6e7ed2a165099353c0762b1676e6eed4c8c138a607e81690d40c0` for fast mode.

**Why it fails:** two current runs and an independent canonical derivation from the shipped stable block all give `1f03ada3e55990f6581ae036087b34dadec2c03ab56ebcd3c9e36720fec40b94`.

**Smallest sufficient repair:** replace the quoted fast hash after preserving the old value with its exact originating suite/subject hashes, or regenerate and ship a named fast receipt so mode-matched reproduction has an artifact rather than prose testimony.

## Invariant ruling

- **I1 is necessary but currently phrased too weakly.** Pinning only the oracle's grand total does not make its per-brick contents independent. I1 must require verified custody of the full oracle bytes/schema, the authorized selection, and the parent identities/coordinates.
- **I2 is necessary but incomplete.** It must bind the code that actually executes, including live callables and answer-affecting state, not only source bytes on disk. It also needs an atomicity rule preventing planner mutation between verification and use.
- **I3 is right.** R01/R02 show the historical omitted bricks are refused by name. For many omissions the exception message shows only four examples, while `ManifestClosureError.result["missing_from_manifest"]` carries the full set. The invariant should explicitly say whether the structured result satisfies “name the brick”; add a probe with more than four omissions and inspect `result`.
- **I4's single refusal type is right; its receipt-payload requirement is unspecified and not tested.** F5 gives the required clarification.

An additional invariant is needed: **I5 — custody/atomicity.** Every answer-determining artifact and live callable must be independently fixed before the candidate is presented, and the verified bytes/code must be the bytes/code actually consumed.

## Coverage gaps beyond the suite author's `not_covered` list

1. Live monkeypatch/replacement of `adapter.plan_object` or other planner callables while source files and the prefilter remain unchanged (demonstrated in F4).
2. Planner source or live-state modification after `require_pinned_planner()` but before/during the 65,060-object loop; the existing list mentions substitution but not this verification-to-use race.
3. Oracle schema attacks: duplicate `brickid`, unequal array lengths (silently truncated by `zip`), multidimensional arrays, negative counts, and non-integral values silently coerced to `int64`.
4. Selection IDs absent from the pinned geometry/universe, zero-count selected bricks, and non-integral values silently coerced to `int64`.
5. Parent authenticity and geometry: unknown but unique `ls_id`, non-finite/out-of-range RA/Dec, and disagreement between a row's `brickid` and coordinates.
6. Structured refusal-payload completeness for every failure phase; the suite currently discards `result`.
7. Multiple missing bricks, including a required name beyond the message's first-four truncation, and verification that the full structured result remains available.
8. Path custody beyond symlink equivalence: fixed-root enforcement, regular-file requirements, and replacement between digest and parse.
9. Manifest argument generators/iterables that fail during iteration. Ordinary `Exception` subclasses are wrapped; a pathological iterable raising a `BaseException` would escape, though that is not a normal list input.

## Production usability

- I found no ordinary malformed file/list input in the reviewed paths that escapes as an unrelated `Exception`; the trailing `except Exception` wraps normal parser, NumPy, CSV and type failures. The suite's five E-probes also produced no error-typed result.
- The uncached P01 production path completed cleanly. My inability to complete the full uncached suite was the executor's 180-second job ceiling, not a `close_manifest()` exception.
- One real closure call verifies the sidecar once, so the stated ~47 seconds is not by itself unusable. Memory for 65,060 rows and their short per-object brick lists appears bounded by those inputs, but the production-scale run remains unmeasured.
- `frozen_plan_object()` reloads the object-manifest module for every object. That is avoidable per-object overhead and widens F4's verification/use surface. Load and verify the planner once, retain its verified callable, and benchmark the actual 65,060-object closure before release. I found no evidence proving scale is unusable, but there is also no production-scale evidence proving it usable.

## Failed attacks / positive evidence

- Honest baseline passed on both fast runs and one uncached production probe.
- Removing either historical neighbour brick was refused and named correctly.
- Extra and duplicate manifest entries, parent rows outside selection, duplicate `ls_id`, wrong oracle total, uncovered selected brick, honest-oracle parent shortening, duplicate selection, and the tested malformed inputs all refused.
- The pinned subject SHA-256 and the shipped production stable-block SHA-256 recomputed exactly.
- C01–C04 outcomes were identical in both fast runs; path form did not change C01/C03 behavior.

## Testimony

The shipped receipt states that its historical uncached run took 996.2 seconds and produced the recorded per-probe timings. I verified the receipt's current bytes and canonical stable hash, but I did not independently complete that full uncached run.

The download plan states that the transfer is queued and blocked on a clean independent closure verdict. I did not inspect or mutate any live downloader process or data directory; this report authorizes no download.

**NOT CLEAR**

# CLOSURE V5 REFEREE — CODEX

## Verdict

**NOT CLEAR.** The repaired mechanism reproduces its shipped production receipt exactly, derives 12,117 required bricks independently of the candidate manifest, and closes the v4 CSV/selection/parent argument seams on an ordinary unmodified import. Those positive results are not sufficient for I1–I5. Blocking findings are F1 (ordinary mutable module pins still let the in-process caller nominate a judging artifact), F2 (the planner digest ignores answer-determining live globals and does not retain the verified callable graph), F3 (every file loader hashes bytes and then reopens the path, contrary to I5), and F4 (a manifest that both duplicates one required brick and omits another is refused without naming the omission, contrary to I3).

This verdict does not dispute the measured 12,117-brick closure. I independently enumerated the pinned 65,060-row parent through the planner without calling `close_manifest`; it also produced 12,117 distinct bricks.

## Reproduction

- Independently measured subject SHA-256: `02237163b27be3a531676275e10dfd08c2ae6198bf383b2ffd0f63e9437c1171`.
- Independently measured fixture-output SHA-256: `dfa8d92784ea98a4c72bba18bf160cdcd94e7fc0f20d215b9def539a7d6cc3af`.
- Independently measured probe-suite SHA-256: `e5a24df405c58e05f9934c71412e100968669a53a3bfb7577e3f51fb53a6d543`.
- Full `production-uncached` run completed in 1,762.6 s: 23/23 conforming, no non-conforming probes, and no unexpected error type.
- My run's `stable_sha256`: `6213e2a054ef3dacc87f93f8ca6ab4ff681cd39e485f30b1456b0b3bc1ada566`.
- Shipped receipt's `stable_sha256`: `6213e2a054ef3dacc87f93f8ca6ab4ff681cd39e485f30b1456b0b3bc1ada566`.
- I independently canonicalized my run's `stable` object and obtained the same hash. My `stable` object is dictionary-equal to the shipped receipt's `stable` object.
- Five fresh processes each produced planner digest `10cea7a6a16458b9f0bcb3534f7afaeb1173ba98a89ac4c7cd709db98e4bb8d1`. Its cross-process stability reproduces.

The production-path suite therefore reproduces. Its conformance rule, however, is only expected PASS/REFUSE plus an optional message substring (`closure_probe_suite_v5.py:534-547`). It does not establish the stronger invariants that several probe `basis` fields say they establish.

## Numbered findings

### F1 — BLOCKER — I1 is enforced only at the function signature; mutable module pins let the caller nominate the judge

**Symbol / quoted line.** `close_manifest(manifest_bricknames)` has one explicit argument (`successor_ref_v5.py:520`), but every path, expected digest, expected count, and receipt path it consumes is an ordinary mutable module global (`PINNED_*`, lines 104-146). The probe harness itself changes these values through `Ctx.redirect()` (`closure_probe_suite_v5.py:132-137`).

**Why it fails.** Removing path arguments closes ordinary argument substitution, but it does not close nomination by an in-process Python caller. I reproduced the bypass using D01's moved-count table. Before calling `load_pinned_counts`, I set `PINNED_COUNTS_REL` to that table and set `PINNED_COUNTS_SHA256` to its digest. The loader accepted the altered judging artifact:

- accepted digest: `e9064985934b0e9698fc1aa3c451fd085f9aca9266842f15f41f44d952fcb46d`
- rows: 270,577
- total: 832,393

This is the same balanced-count edit D01 correctly refuses when only the path is redirected. Updating the ordinary digest global makes it pass. Selection, parent, parent-receipt, and geometry paths/pins are mutable in the same way. U02 already demonstrates that the parent path, parent digest, and producer-receipt path can all be redirected in one process; its coherence validator, not independent pin custody, is what then refuses that particular fixture.

The previous round accepted in-memory planner mutation as in scope. Under that same threat model, artifact-pin mutation cannot be excluded merely because the names begin with `PINNED_`.

**Smallest sufficient repair.** Put closure behind a fresh isolated executable/process whose startup verifies the subject and an immutable configuration/manifest identity supplied by a gate outside the manifest presenter. Load pins into private immutable state, expose only the candidate manifest over a serialization boundary, and reject any preloaded/shared module graph. A one-argument Python function in the caller's interpreter is not a custody boundary.

### F2 — BLOCKER — the planner digest is stable because it ignores answer-determining live state

**Symbol / quoted line.** `_code_fingerprint()` records `co_code`, names, varnames, constants, and nested code (`successor_ref_v5.py:290-306`). `frozen_planner_digest()` applies it only to `m.plan_candidate_bricks` and `ad.plan_object`, plus `__defaults__` (`:309-337`). Actual closure resolves the mutable global `frozen_plan_object` for every row (`:628-635`); that wrapper reloads `_frozen_planner()` and resolves the shared adapter graph (`:258-275`).

`adapter.plan_object` uses answer-determining globals including `build_output_wcs`, `angular_separation_deg`, `output_overlap_area_in_source_pixels`, `_source_wcs_for_row`, `INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2`, `ObjectTerminalError`, and other helpers (`adapter/nm_brick_cutout_adapter.py:712-802`). The fingerprint stores those names, not the live values or callable implementations to which they resolve.

**Why it fails.** I changed `adapter.INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2` to `10**30` before verification. `require_pinned_planner()` still returned the pinned digest `10cea7a6...8d1`; a centered one-brick plan then executed under that accepted digest and failed `FAILED_PLAN_NO_SOURCES`. Thus the digest's process stability comes partly from ignoring state that changes the answer.

I separately verified the verification/use race: after `require_pinned_planner()` returned the pinned digest, I rebound the cached adapter's `plan_object`; `frozen_plan_object()` then executed the replacement and returned `['0001p000']`. N01 catches rebinding only when it occurs before the direct `require_pinned_planner()` call. It does not retain the checked callable or test mutation after verification or during the 65,060-object loop.

The wrapper `frozen_plan_object` itself, `plan_candidate_bricks`' global `_adapter`, transitive helper callables, closures, `__kwdefaults__`, and answer-affecting scalar/class state are not comprehensively bound.

**Smallest sufficient repair.** Load the complete planner module graph once in a fresh isolated process after exact source-byte verification; retain the verified module/callable references for the entire plan; forbid shared `sys.modules` reuse; and return the result before that process exits. If a fingerprint remains, make it a recursive binding over every actually resolved callable/default/closure and answer-affecting global, including the closure wrapper. Re-verify at completion or make mutation structurally impossible. Add probes for helper/global mutation before verification, wrapper rebinding, same-code/different-globals functions, and mutation after verification/during iteration.

### F3 — BLOCKER — I5's verified-bytes-equal-consumed-bytes requirement is not met

**Symbol / quoted line.** The loaders perform separate hash and parse opens:

- geometry: `sha256_file(sidecar)` then `load_geometry_sidecar(sidecar)` (`successor_ref_v5.py:365-370`);
- counts: `sha256_file(table)` then `table.open()` (`:395-403`);
- selection: `sha256_file(path)` then `np.load(path)` (`:439-445`);
- parent: `sha256_file(path)` then `path.open()` (`:473-497`);
- parent receipt: a mutable path is read independently (`:469-478`).

**Why it fails.** A path can be replaced between the verified read and the consuming read. The repair record and suite `not_covered` list acknowledge this window, but I5 is an invariant, not an optional coverage item: “the verified bytes and code must be the bytes and code actually consumed.” The implementation presently provides no same-file-descriptor/same-byte-snapshot guarantee. The planner has an analogous verification/use gap under F2.

**Smallest sufficient repair.** Open each artifact once, hash the exact byte snapshot read from that descriptor, and parse that same snapshot (for example, verified bytes/`BytesIO` for CSV/JSON/NPZ and a retained descriptor or immutable copied snapshot for the large FITS sidecar). Bind file identity with `fstat`, reject symlinks/non-regular files where applicable, and do not resolve/reopen the mutable path after verification.

### F4 — BLOCKER — I3 fails for a candidate that combines a duplicate with an omission

**Symbol / quoted line.** Duplicate detection precedes planning and the set difference (`successor_ref_v5.py:622-626` versus `:628-653`). The duplicate refusal carries only `manifest_count` and `distinct`.

**Why it fails.** I constructed a 12,117-entry candidate from the independently enumerated required set by omitting required brick `0001m250` and duplicating required brick `0001m252`. The actual refusal was:

`manifest contains duplicate bricknames`

with structured result:

`{'manifest_count': 12117, 'distinct': 12116}`

The candidate omits a required brick, but neither the message nor structured result identifies it. I3 says a manifest omitting a required brick must be refused and the refusal must identify the bricks. R04 tests a duplicate without an omission; R01/R02 test omissions without a duplicate. The combined condition is untested.

**Smallest sufficient repair.** Derive the required set before final manifest adjudication and return one structured closure result containing duplicates, missing names, and extra names together. A duplicate may remain a refusal, but it must not suppress the required-brick difference.

### F5 — MAJOR — I4's receipt payload requirement remains undefined and is demonstrably unmet

**Symbol / quoted line.** The generic handler returns only `{"error": type(exc).__name__}` (`successor_ref_v5.py:655-661`). R06's shipped and reproduced result is only `{"error": "TypeError"}`. Probe conformance checks REFUSE and no result schema (`closure_probe_suite_v5.py:537-547`).

**Why it fails.** R06 reaches manifest conversion only after geometry, planner, counts, selection, and parent have been loaded and validated (`successor_ref_v5.py:554-622`). Objects, selected-brick count, and verified digests are therefore known, yet the refusal discards all of them. Other early refusals similarly return inconsistent ad-hoc subsets. The coherence loop also stops after collecting five examples (`:589-595`) and reports that capped length as `incoherent_rows`, so its purported count is not a total when more than five rows are bad.

A single `ManifestClosureError` type is fail-closed in the narrow exception-class sense. It does not satisfy “carrying the numbers a receipt needs.”

**Smallest sufficient repair.** Freeze an exact phase-aware refusal schema: error code and phase, candidate count when obtainable, every verified artifact digest, every parsed object/selection/count known at that phase, full/correct discrepancy counts, and bounded examples separately from totals. Make the suite assert required keys and values for every refusal phase.

### F6 — MAJOR — the parent has two copies of one digest, not two fully enforced witnesses; selection provenance is absent

**Symbol / quoted line.** `load_pinned_parent()` compares the parent bytes to `PINNED_PARENT_SHA256`, then reads `positions_receipts.json` and compares only `rec["output_sha256"]` to the same digest plus `total_rows` to the sum of chunk row counts (`successor_ref_v5.py:456-501`). `fetch_positions.py:150-158` shows how the receipt was written after assembling the output. `load_pinned_selection()` checks only path, code digest, uniqueness, and count (`successor_ref_v5.py:428-453`).

**Why it fails.** The parent code pin and the producer receipt are chronologically distinct records, and I verified that current bytes agree: parent `425a42c3...f70831`, receipt has 13 chunks, 65,060 summed rows, and 6,445 summed bricks. That is positive provenance evidence.

It is not a second immutable witness as enforced by this mechanism. The receipt's own SHA-256 (`41716d47...5701`) is not pinned; its schema, chunk sequence/uniqueness, endpoint/jobs, query hashes, result hashes, byte counts, brick total, and relation between chunk payload digests and the assembled parent are not verified by `load_pinned_parent()`. D05 proves only that changing the code parent pin while leaving the receipt's top-level copy unchanged refuses. U02 demonstrates that redirecting the receipt's top-level copy along with the code pin defeats both digest comparisons.

A code pin is sufficient to identify exact current selection bytes only if the subject/configuration has an externally trusted immutable process boundary. It is not sufficient to establish that those bytes are the authorized BS-2s producer output, and F1 shows that the current in-process boundary does not even make the code pin immutable to the caller.

**Smallest sufficient repair.** Seal and pin the parent receipt envelope itself and verify its canonical schema plus chunk-to-output assembly. For selection, produce a canonical BS-2s receipt containing the exact selection digest, canonical selected IDs/count, producer code and frozen-input/contract hashes, and pass metrics; pin the receipt identity and require receipt → code pin → consumed bytes equality.

### F7 — MODERATE — probe metadata and conformance overstate what the 23 probes establish

I read all 23 decorated bodies.

- Faithful body/mutation descriptions: `P01, R01, R03, R04, R05, R06, R07, D01, D03, D04, S01, S02, S03, S04, S05, U01, U02, N01, N02, G01`, subject to the assertion limitations below.
- `R02`: the body really removes 100 bricks, but its basis says the probe checks that the structured result carries the full set. Conformance checks only REFUSE plus message substring `missing 100`; `jsonable()` truncates the retained list after eight values (`closure_probe_suite_v5.py:474-486`). No assertion compares the runtime list length/content to the 100 omitted names.
- `D02`: metadata says the symlink targets D01's file, but the body creates a different `counts_moved2.csv` with a different mutation and links to that (`:251-262`). The symlink/digest-gate purpose still holds.
- `D05`: “that copy” implies D04's copy, but the body creates a different `parent_swapped2.csv` and changes a different field (`:289-299`). Its remaining-receipt-witness purpose still holds.
- `S01`–`S05` and `U01`: `varies` names the altered copy and digest override but does not explicitly enumerate the corresponding `PINNED_*_REL` reassignment performed by `Ctx.redirect`. `U02` changes both parent and receipt path constants; its prose describes the receipt as redirected but does not name that second path-global change explicitly.
- `N01` and `N02` honestly declare direct calls. They test the binding helper at one instant, not production wiring or whole-plan lifetime.
- `G01` now retains the observed digests in the receipt. Its PASS still does not prove those same loaded objects/callables are retained and consumed later.

The 23/23 suite verdict is accurate under the runner's narrow conformance function. It is not proof that I1–I5 hold.

## Answers to the eight referee questions

1. **Reproduction:** yes. My production-uncached stable hash and the shipped same-mode hash are both `6213e2a054ef3dacc87f93f8ca6ab4ff681cd39e485f30b1456b0b3bc1ada566`.
2. **I1:** no at the actual in-process caller boundary (F1). It holds only at the signature level under an extra, unenforced assumption that the caller cannot mutate module state.
3. **Planner binding / I5:** no (F2). The value is stable across processes, but ignores answer-affecting globals/helpers and does not retain the verified graph for the plan's duration.
4. **Two-witness parent:** two historical records, but only one digest assertion duplicated as enforced by this code (F6). The producer receipt is useful evidence, not a sealed second witness.
5. **Selection code pin:** enough to name exact bytes only under an externally trusted immutable subject/configuration; not enough for current I1/I5 or producer authorization. A pinned canonical BS-2s receipt with selection digest, IDs/count, producer/tool/input/contract hashes, and recomputable envelope is the sufficient witness.
6. **Probe fidelity:** detailed in F7. Hard metadata mismatches are D02 and D05; R02 does not assert its stated structured-result property; direct N01/N02 do not exercise production lifetime.
7. **Additional uncovered conditions:** mutable path/digest/count globals changed together; answer-affecting planner helpers/scalars and wrapper mutation before verification; mutation after verification/during iteration; duplicate-plus-omission I3 behavior; exact phase-aware refusal schemas; parent receipt schema/chunk-to-output reconstruction; selection producer authorization; selection/count dtype/shape coercion paths after a digest override; geometry duplicate brick IDs; and capped-vs-total incoherent-row accounting.
8. **Production usability / 12,117:** yes, the number is consistent. A separate direct enumeration imported the pinned object-manifest planner, parsed the pinned parent, and did not call `close_manifest`: 65,060 objects, 12,117 distinct required bricks. Per-object planned-brick histogram was `{1: 55566, 2: 8801, 3: 591, 4: 102}`. Runtime was 144.117 s. The ratio is `12117/6445 = 1.880062...`; at 12.2 MB/brick, the arithmetic is 147.8274 decimal GB (about 148 GB). This validates the measured count/ceiling arithmetic, not the unsafe custody/atomicity boundary.

## Failed attacks / positive evidence

- All named subject/suite/fixture hashes reproduce.
- The current sidecar, count CSV, selection, and parent hashes reproduce their code pins.
- The count CSV independently has 270,577 unique brick IDs totaling 832,393.
- The selection independently has shape `(6445,)`, dtype `int64`, and 6,445 unique values.
- The parent receipt currently has 13 unique chunk entries; chunk rows sum to 65,060 and chunk bricks sum to 6,445.
- The full production-uncached suite reproduces byte-for-byte at the stable-object level.
- P01 accepts the exact set the mechanism derives; simple missing, extra, and duplicate controls refuse.
- R01/R02 carry complete missing sets in the runtime `ManifestClosureError.result` for their simple non-duplicate cases; the receipt serialization/runner assertion is the weakness, not those runtime lists.
- D01–D05 refuse when only the mutations stated by their intended front-gate attacks are made.
- Count schema validators refuse the tested duplicate, negative, total, row-count, and column-name faults.
- Selection-universe and parent-coordinate coherence validators refuse their tested faults.
- N01/N02 refuse the two exact pre-verification mutations they exercise.
- I2 holds in the narrow derivation sense: no required-set argument exists, and the candidate manifest is compared only after planning.
- A separate planner enumeration reproduces 12,117 required bricks.

## Evidence ledger

Content-read artifacts:

- `BRIEF_CLOSURE_V5_REFEREE.md`
- `CLOSURE_REPAIR_20260826.md`
- `CLOSURE_RECEIPT_CODEX.md`
- `CLOSURE_RECEIPT_GPT56.md`
- `CLOSURE_PROBE_V5_RECEIPT_20260826.json`
- `closure_probe_suite_v5.py`
- `../ref/successor_ref_v5.py` (closure/planner regions and constants; unrelated statistical regions were not adjudicated)
- `../../_objmanifest_20260820/build_object_manifest.py`
- `../../_cutout_runner_20260820/cutout_runner.py`
- `../../adapter/nm_brick_cutout_adapter.py` (planner and transitive loading regions)
- `../acquire/positions_receipts.json`
- `../acquire/fetch_positions.py`
- `../acquire/DOWNLOAD_QUEUE_PLAN_20260825.md`

Principal commands/probes:

- `shasum -a 256` over subject, fixture output, suite, shipped receipt, sidecar, count CSV, selection, parent, and parent receipt.
- `python3 closure_probe_suite_v5.py --list`.
- `python3 closure_probe_suite_v5.py --json _tmp_CODEX_v5_receipt.json --run-dir _tmp_CODEX_v5_run`.
- Canonical JSON rehash and exact stable-object comparison between my receipt and the shipped receipt.
- Five fresh-process calls to `frozen_planner_digest()`.
- Direct count-table, selection, and parent-receipt recount/schema checks.
- Independent direct planner enumeration over 65,060 parent rows.
- Pre-verification planner-threshold mutation and post-verification live-callable mutation probes.
- Mutable count-path plus mutable count-digest acceptance probe.
- Combined duplicate-plus-omission production call.

## Constraints and uncertainties

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not launch, authorize, inspect, or mutate any downloader or transfer process.
- No image bytes were read.
- Apart from the required report, writes were confined to suite-created `_tmp_CODEX_v5_*` artifacts in this gate directory.
- This pass is intentionally limited to the closure mechanism. It does not re-referee the wider preregistration, selection science, transfer implementation, or image products.

## Testimony

`DOWNLOAD_QUEUE_PLAN_20260825.md` states that no image byte has been fetched and that a clean closure referee verdict gates transfer. I read that record but did not inspect live transfer state, so I do not independently assert the current live downloader state.

The receipt's UTC fields and `fetch_positions.py` support the claim that the parent receipt was produced by the fetch before the v5 closure repair. I did not re-query the 13 remote TAP job URLs or reconstruct the parent from their archived result payloads, so remote-job provenance beyond the on-disk receipt remains testimony.

**NOT CLEAR**
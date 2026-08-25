# CLOSURE RECEIPT — CODEX

## Verdict

**NOT CLEAR.** I1 does not hold. The blocking findings are F1 (caller-controlled count oracle), F2 (caller-controlled selection), and F3 (unbound parent contents). C01–C04 are real independence failures, not probe artefacts. A transfer manifest built on this mechanism is not safe to download against yet.

## Reproduction and custody

- Independently computed `../ref/successor_ref_v4.py` SHA-256: `8191c42be1e8153e80480c0d110eb03c8f9c92f91895692e333af3fcbef50a21` — matches the brief and shipped receipt.
- Independently computed suite SHA-256: `2dd141b48e74115f4fc6be4ba5cd8bd74a3c4e208565995d60af98a880b11e69`.
- Full production-uncached run completed in 1047.7 s. It reproduced `18/22` conforming, non-conforming `C01,C02,C03,C04`, no unexpected exception type, and `stable_sha256 = 43f2a1226728b868bb29ed59914337efc6cbd7c88888bdd2ab844b1d8d37910f`. This exactly matches `CLOSURE_PROBE_RECEIPT_20260825.json` for the same mode. I also independently re-hashed the emitted canonical `stable` block and obtained the same value.
- Two independent memoised-after-one-verification runs agreed with each other at `1f03ada3e55990f6581ae036087b34dadec2c03ab56ebcd3c9e36720fec40b94`, not the brief's stated prior fast-mode value `3abf01ae66a6e7ed2a165099353c0762b1676e6eed4c8c138a607e81690d40c0`. F6 records this receipt-document inconsistency; it does not displace the exact production-mode reproduction.

## Findings

### F1 — BLOCKER — the count oracle is caller-controlled; C01 and C03 are real I1 failures

**Symbol / quoted line.** `close_manifest()` at `successor_ref_v4.py:342-346` assigns `ora_p = Path(oracle_npz)` and computes `ora_sha`, but lines 355-366 trust the arrays read from that caller-selected file. The declared `PINNED_COUNTS_SHA256` at line 105 is never compared to `ora_sha`. The docstring's claim at lines 329-332 that a shortened parent “cannot also shorten the oracle” is therefore false.

**Why it fails.** C01 deletes one parent row and edits the selected-brick count to zero while moving one count to the filler row. The total remains 832,393 and every checked per-selected-brick count balances, so the mechanism accepts. C03 proves that spelling those same caller-controlled bytes through symlinks changes nothing. Computing a digest for a path supplied by the same caller is custody metadata, not an independent witness. C03 is not a distinct symlink vulnerability; it is the same unpinned-oracle defect reached through another path form.

**Smallest sufficient repair.** Add a fixed `PINNED_COUNTS_REL`, load the already-pinned `combined_per_brick_counts.csv` from that path inside `close_manifest()`, and compare its bytes to `PINNED_COUNTS_SHA256` before parsing. Remove `oracle_npz` from the production signature. If a canonical NPZ is preferred, first freeze a separate NPZ digest; the existing constant is the CSV digest and must not be compared to a newly serialized NPZ. Reject duplicate keys, length/shape disagreement, non-integral or negative counts, and total disagreement while parsing.

### F2 — BLOCKER — the selected-brick set is caller-controlled; C02 is a real independence failure

**Symbol / quoted line.** `close_manifest()` lines 342 and 348-353 read `selection_npz` from the caller and accept any non-empty unique `selected_brickid` array. `sel_sha` is reported but compared to no independently fixed value.

**Why it fails.** C02 removes the second parent row, reduces the selection to the first brick, and supplies matching counts. All three caller-selected artifacts agree, so closure accepts a smaller study. Even a properly pinned full count table would not fix this: lines 362-366 deliberately project the oracle onto whatever `selset` the caller supplied.

**Smallest sufficient repair.** Bind the production selection to the independently sealed BS-2s output: load it from a fixed authorized path and verify a digest stored in a frozen authorization/registry outside this call. Remove `selection_npz` as an unconstrained production argument, or compare it to that independently installed digest before using it. Also require every selected brick ID to resolve uniquely in the pinned geometry universe.

### F3 — BLOCKER — parent identity and coordinates have no independent binding; C04 is real

**Symbol / quoted line.** `close_manifest()` lines 342-346 hash the caller-selected `parent_csv`, then lines 368-400 validate only columns, selected-brick membership, per-brick row counts, non-emptiness, and duplicate `ls_id`. `par_sha` is never compared with an independent value. Lines 408-415 then treat the caller's `ls_id,ra,dec` as the galaxies from which closure is derived.

**Why it fails.** C04 preserves both selected-brick counts but replaces the second galaxy with an unused ID and the first galaxy's coordinates. The resulting understated one-object-equivalent plan and matching manifest pass. This is not outside the reviewed mechanism's contract: the brief says the image set is computed “from the galaxies themselves,” and no reviewed upstream artifact binds those row contents. A count oracle proves cardinality by brick, not object identity or sky position. The finding would move upstream only if a named, independently verified parent artifact existed; none is consumed here.

**Smallest sufficient repair.** Before planning, require `par_sha` to match a parent-artifact digest installed by the authorized catalogue/selection producer in an independently frozen registry or receipt, not a digest argument supplied with this call. Prefer a fixed production parent path and remove the arbitrary `parent_csv` path. Freeze the exact canonical row schema and ordering (or canonicalize before hashing), including `ls_id`, `brickid`, `ra`, and `dec`.

### F4 — MAJOR — I1–I4 are necessary but incomplete and I4 is underspecified

**Symbol / quoted line.** I1 speaks only of the count oracle; I2 says derivation occurs from parent objects; I4 asks for “numbers a receipt needs.” In code, the generic handler at `successor_ref_v4.py:437-441` returns only `{"error": <type>}` for E02–E05.

**Why it fails.** The four invariants do not explicitly require independent custody of (a) the selection and (b) the parent row identities/coordinates, which are exactly the C02 and C04 seams. I4 has no exact result schema, so the suite can call a refusal conforming even when its payload contains only an exception class and no input role, digest, stage, or parsed counts. I2 does hold in the narrow computational sense: the required set is derived inside the check by `frozen_plan_object()` and the candidate manifest is only compared afterward. That does not authenticate the parent supplied to the derivation.

**Smallest sufficient repair.** Add explicit invariants for selection custody and parent-content custody. Define one exact success/refusal result schema with required fields by failure stage (input role/path identifier, verified digests available at that stage, parsed object/selection/oracle/manifest counts when available, and the closure difference when planning completes). Extend E-probes to inspect that payload, not only the exception class.

### F5 — MAJOR — six probe `varies` records omit additional input changes; two controls bypass the advertised entry point

**Symbol / quoted line.** The decorator contract at `closure_probe_suite.py:116-126` says `varies` records what changes relative to the honest baseline. The suite introduction at lines 22-24 says “Every probe calls the real `close_manifest(...)`.”

**Why it fails.** The following metadata/code disagreements are present:

1. `R09` removes a parent row **and** changes the manifest from `all_required` to `first_required` (`:269-274`), although `varies` names only the row removal and says oracle/selection are untouched.
2. `R11` changes the selection **and** changes the manifest to `first_required` (`:291-298`), although `varies` names only the duplicate selection entry.
3. `C01` changes the parent and oracle **and** reduces the manifest to `first_required` (`:309-316`); the manifest change is omitted.
4. `C02` changes parent, selection, oracle, **and** manifest (`:319-330`); its “all three inputs” wording omits the fourth production argument.
5. `C04` changes the second parent row **and** reduces the manifest (`:350-364`); the manifest change is omitted.
6. `E04` replaces two fields with text **and** drops the second baseline parent row (`:389-394`); the row-count change is omitted.

These hidden manifest reductions do not create the C01/C02/C04 acceptances: they make the candidate manifest complete for the shortened/altered parent so the intended custody seam is isolated. Likewise, R09/R11/E04 refuse before the extra change can decide the outcome. The lines are still not faithful records of what varied.

`R10` and `G01` are faithful to their own labels, but they call `require_pinned_planner()` directly (`:281-288`, `:301-305`) rather than the advertised production entry point. Therefore the suite-wide “Every probe” claim is false and those two probes do not exercise production wiring.

**Smallest sufficient repair.** Amend each listed `varies` value to enumerate every changed argument. Amend the suite introduction to exempt direct binding controls, or route R10/G01 through a narrowly selected production call while preserving their purpose.

### F6 — MINOR — the brief's fast-mode reproducibility claim does not reproduce

**Symbol / quoted line.** `BRIEF_CLOSURE_RECEIPT_V5.md:77-79` states that two fast runs produced `3abf01ae...d40c0`.

**Why it fails.** Two current fast runs of the pinned suite and subject both produced and self-rehashed to `1f03ada3...0b94`. The production-mode hash exactly reproduces the shipped production receipt, so this does not affect F1–F3 or the primary reproduction answer; it does mean the fast-mode testimony is stale or incorrectly recorded.

**Smallest sufficient repair.** Replace the stated fast hash only after preserving and diffing the two canonical `stable` blocks that produced the old and current values; alternatively ship a fast-mode receipt beside the production receipt so the claim is machine-comparable.

### F7 — MAJOR — uncovered conditions bearing on I1–I4 extend beyond `not_covered`

**Symbol / quoted line.** `closure_probe_suite.py:80-92` lists four known gaps. Additional untested conditions are:

1. Oracle schema attacks: unequal array lengths (silently truncated by `zip`), duplicate `brickid` keys (silently overwritten by the dict comprehension), negative counts, non-integral values coerced to `int64`, and non-1-D arrays.
2. A unique selected brick ID absent from the pinned geometry universe; selection membership is never checked against geometry by brick ID.
3. Finite/range validation for parent RA/Dec and consistency between a row's declared `brickid` and its coordinates/home brick.
4. In-memory planner mutation: `frozen_planner_digest()` hashes source-file bytes, but planning uses imported module objects. A monkeypatch to an adapter function can leave the file digest and prefilter value unchanged while changing executed code. Concurrent planner/source change after `require_pinned_planner()` and before or between per-object calls is likewise not the input-file race already listed.
5. Exact refusal-payload conformance for corrupt oracle files, missing oracle keys, missing parent columns, empty parent, non-finite coordinates, planner exceptions, and zero-brick plans.
6. Candidate manifest edge cases: empty iterables, non-string values converted by `str`, and very large iterables.

**Smallest sufficient repair.** Add one focused probe for each schema/control-flow class, make oracle/selection/parent validators explicit and fail-closed before planning, hash or otherwise attest the actually loaded planner implementation, and assert the exact refusal result schema.

## Per-probe fidelity accounting

Faithful to their own decorator metadata: `P01, R01, R02, R03, R04, R05, R06, R07, R08, R10, G01, C03, E01, E02, E03, E05`.

Metadata/code disagreements: `R09, R11, C01, C02, C04, E04`, as enumerated in F5. `R10` and `G01` additionally contradict the suite-wide production-entry-point claim but not their own labels.

## Ruling on I1–I4 and the four non-conforming probes

- **I1: does not hold.** C01 and C03 directly demonstrate that the count oracle is not independent. C02 demonstrates that caller custody of the selection can shrink the domain against which the oracle is projected. C04 demonstrates the remaining parent-content custody seam. All four are real; none is an artefact of fixture construction.
- **I2: holds only narrowly.** The code derives the required set inside the check with the pinned planner and exposes no direct required-set argument. It does not establish that the parent objects are the authorized galaxies; F3/F4 must be added to the contract.
- **I3: holds for the exercised cases.** R01 and R02 refuse and name `3471m885` and `2857m870`, respectively.
- **I4: ordinary exception normalization holds for E01–E05, but the invariant is not fully testable as written because the required receipt payload is unspecified.** No exercised malformed input escaped as an unrelated exception type.

## Production usability

The production run measured 51.644 s to load/verify 366,912 geometry bricks and 1047.7 s for 22 uncached calls. In the fast run, after the one geometry verification, the median two-object probe call was 0.0015 s and the maximum was 0.004 s. The real operation is one call, not 22, and 65,060 rows plus a five-digit brick set are modest in-memory sizes. I found no demonstrated reason it is unusable at that scale rather than wrong, and E01–E05 produced clean `ManifestClosureError` refusals. However, no 65,060-object run has occurred, so runtime/memory at scale remains unverified as the suite itself states. The per-object `frozen_plan_object()` reload path is a scale-risk worth timing, not presently evidence of unusability.

## Failed attacks / positive evidence

- The honest five-brick baseline clears.
- Omitting either historical neighbour is refused by name.
- Extra and duplicate manifest entries are refused.
- A parent row outside the selection, duplicate parent IDs, a wrong oracle total, incomplete oracle coverage, an honestly shortened parent, a duplicate selection, and the tested planner-prefilter mutation are refused.
- The pinned geometry path/digest/cardinality and full-transitive planner digest reproduce on the tested path.
- The retired `plan_object_bricks()` is not used by `close_manifest()`; derivation calls `frozen_plan_object()`.
- E01–E05 all leave as `ManifestClosureError`, with no unexpected exception type in the receipt.

## Testimony

The brief states that the real production call will contain 65,060 objects and 6,445 selected bricks and that the queued transfer is approximately 77 GB. I did not independently produce that parent, selection, manifest, or byte total. I did not read `/Users/duhokim/NebulaMindData/` and did not launch or authorize any download.

**NOT CLEAR**
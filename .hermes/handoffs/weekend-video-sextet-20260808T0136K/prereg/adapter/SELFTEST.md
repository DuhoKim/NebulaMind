# Guarded brick-route local-cut adapter — synthetic self-test

Recorded: 2026-08-16T09:59:42Z (2026-08-16T18:59:42+09:00)
Supersedes the 2026-08-16T03:24:43Z record after the read/decompression-stage
gate and round-4 cross (TORI_ADAPTER_20260815.md §0.5; earlier supersessions:
resampler gate 03:24:43Z, round-3 knife-edge 2026-08-15T17:47:26Z,
content-hash identity 16:37:44Z, round-2 extension 16:23:04Z, corner repair
16:03:08Z).

Verdict: **PASS — BUILD ONLY; ZERO TRANSFER; ZERO REAL ACQUISITION;
YUI CROSS-CHECK ROUND-1 29/29, ROUND-2 4/4, ROUND-3 10/10 (separate, never
merged); PIXEL VALUES COMPARED per round on Yui's hash-verified brick data at
her pre-declared tolerances — r1 max 1.907e-06 vs 5e-6 (5 compared / 24
skipped with recorded geometric reason), r2 max 7.629e-06 vs 1e-5 (4/4), r3
max 7.629e-06 vs 1e-5 (10/10); residuals sit at the float32 quantization
floor (one ulp of the fixture values)**

## Boundary counters

- Globus endpoints activated: **0**
- Globus tasks submitted: **0** (no submission code path exists in the module)
- transfer manifests executed: **0** (manifests are sealed dry-run artifacts only)
- real survey image files listed, read, or fetched: **0**
- real catalogue rows or positions read: **0**
- real cutouts requested or generated: **0**
- network calls made by this lane: **0**
- chirality or morphology labels computed: **0**
- sky statistics computed: **0**
- publication, acceptance, commit, or push: **0**

Every brick geometry row, FITS header, FITS byte, and object position was
generated synthetically inside `_tmp_selftest_*` directories under
`prereg/adapter/`, which the test harness deleted on teardown. The frozen V3
preregistration was read only to verify its SHA-256 and mode 444.

## Commands actually run

```text
cd prereg/adapter
/usr/bin/python3 -m py_compile nm_brick_cutout_adapter.py test_nm_brick_cutout_adapter.py cross_check_yui_boundary.py
/usr/bin/python3 -m unittest -v
cd prereg && /usr/bin/python3 _tmp_kun_cross_adapter_fixtures_20260816.py   # Kun's own runner, unmodified
```

Result:

```text
Ran 30 tests in 26.639s

OK
```

(The suite runs the cross-check twice to enforce `content_sha256`
reproducibility on every run, which accounts for the added wall time.)

Standalone cross-check run (`/usr/bin/python3 cross_check_yui_boundary.py`):

```text
{"round1": {"cases_failed": 0, "cases_passed": 29, "cases_total": 29, "status": "PASS"},
 "round2": {"cases_failed": 0, "cases_passed": 4, "cases_total": 4, "status": "PASS"},
 "round3": {"cases_failed": 0, "cases_passed": 10, "cases_total": 10, "status": "PASS"},
 "status": "PASS",
 "content_sha256": "1eba47d8cef18d84941e6a85ffca010717825b7134cf8be72656b53f6a7561c7"}
```

Round-3 loads Yui's pinned pre-generated knife-edge tree
(`boundary_fixtures/generated_round3/`, generator `6b410fb4…5e5e62`,
objects/sidecar hash-verified against its own manifest). It surfaced one real
planning defect (`dec_min_exact_boundary`: candidate over-planned at
zero-area tangency, dec −89.875) which was repaired in the adapter — the
inclusion rule now clips the output nine-point polygon in each candidate
source's pixel plane with a positive-area threshold, and the renderer
contribution window matches the oracle's bilinear-support rule. The
planned-vs-contributing split cases (+1 / +0.25 offsets) pass all three
failure-mode checks: candidate kept in planned, not credited as contributing,
recorded zero-pixel-touch with the cut completing on primary-only coverage.

Round-2 loads Yui's pinned pre-generated tree
(`boundary_fixtures/generated_round2/`, objects `e4333443…59df2b`, sidecar
`9f0dc0f5…9df635`, verified against its own manifest before use) and covers
the boundary classes the round-1-only receipt did not: RA-wrap seam crossing
at dec −10, selected-footprint declination extremes at +32.25 and −89.875,
distinct per-brick tangent points, and a derived
overlap-without-unique-crossing case. All four complete the full cut pipeline
(PC-3 round trips ≤1e-6 px hold at 0.125° from the pole). Neither fixture
generator was modified: `make_boundary_fixtures.py` `24f55943…3404d`,
`make_boundary_fixtures_round2.py` `60e3d662…aa15bc`.

Kun's unmodified scratch cross-runner (`69115bc3…157ae7a`): `"status": "PASS"`,
`cases_passed: 29 / 29`, all eight corner cases included.

Compilation result: **PASS** (Python 3.9.6). The cross-check path additionally
uses numpy 1.26.4 + astropy 6.0.1 — required by Yui's fixture oracle, imported
only by `cross_check_yui_boundary.py`, never by the adapter module.

## Deliverable hashes at test time

| File | SHA-256 |
|---|---|
| `nm_brick_cutout_adapter.py` | `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f` (UNCHANGED by the read-stage gate — byte-identical to Kun's resampler-gate pin; AST audit: zero third-party imports) |
| `test_nm_brick_cutout_adapter.py` | `7fc77ee74bdff2facbba6bc5de1f45d78875193841dc67df9b76e67565b3f99c` |
| `cross_check_yui_boundary.py` | `3bb84cefe44eea4a49b8d8ef7bad6a64a92137d67731606e4bccbe33703f9436` |
| `../readstage/nm_brick_read_stage.py` | `6662c8c74d71b81216149596d65deeaa39c07a19a57e50ba9bbe4ac22d478b0a` (new pinned read/decompression stage; astropy-backed, outside the adapter) |
| `../readstage/test_nm_brick_read_stage.py` | `dd669e434de0319d237f53a16792c3a9c0a2b61457b84ea81a01d9d71c325790` (9/9: positive chain + fail-closed negatives) |
| `CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json` | regenerated each suite run; `status: PASS`, round-1 29/29 + round-2 4/4 + round-3 10/10 + round-4 3/3 separately, per-round `pixel_agreement` blocks, round-4 `byte_identity` (read-stage path vs uncompressed path, exact) and embedded timestamp-stripped read-stage receipts, with a written `scope` field, binding the adapter hash above. Pinnable identity: `content_sha256 = c30a7b315a55a24bb3a022bc851f38b7c79e12b8f58903e7dece7b344773a978` (canonical content hash excluding exactly `recorded_utc` + itself, exclusions declared in-artifact; proven identical across two consecutive runs with differing timestamps 09:58:05Z / 09:58:30Z) |

## Guarantee-fires matrix (a guarantee never observed to fire is not a guarantee)

| Guarantee | Test | Observed result |
|---|---|---|
| No transport exists structurally | `test_static_source_has_no_transport` | AST import set is exactly the stdlib allowlist; no socket/http/urllib/requests/globus/subprocess/os import; no eval/exec/`__import__` |
| No fetch/submit callable exists | `test_module_has_no_fetch_or_submit_capability` | no module attribute or class method named fetch/submit/download/upload |
| Authority docs hash-bound | `test_authority_hashes_match_disk` | route binding + frozen V3 hashes match; V3 mode 0444 |
| Validators hash-pinned | `test_pinned_validator_hashes` | both pins match disk; a tampered copy refuses to load |
| Exact frozen output WCS constants | `test_output_wcs_exact_constants` | CD terms repr-exact; determinant negative, bound to CD product |
| SIP-bearing source header rejected | `test_sip_source_rejected_and_skip_is_counted` | `REJECTED_DISTORTION`, no output file written |
| Skipped object is logged and counted | same test, resume pass | `skipped=1`, `RESUME_TERMINAL_NOT_RECUT` in hash-chained log |
| Parity-flipped source header rejected | `test_parity_flipped_source_rejected` | `REJECTED_PARITY` |
| Output header failing PC-4 rejected | `test_output_header_tamper_rejected_and_quarantined` | post-generation CD sign tamper → `REJECTED_PARITY`, staged file quarantined, no cutout |
| PC-4 rejection matrix (§9.3) | `test_rejection_matrix`, `test_duplicate_keyword_rejected`, `test_clean_canonical_tan_passes` | SIP, CTYPE-SIP, PV, TPV, CPDIS, D2IM, DP lookup, partial CD, partial PC/CDELT, mixed CD+PC, singular, NaN, Inf, missing CRPIX/CRVAL/CTYPE, non-celestial, swapped axes, alternate suffix, duplicate keyword all rejected with distinct codes; clean canonical TAN passes |
| Corner object requests three extra bricks | `test_corner_object_requests_three_extra_bricks` | primary + 2 edge neighbours + 1 corner neighbour, classified |
| Margin scalar is not the selection rule | `test_margin_scalar_is_not_the_selection_rule` | at exactly 16.768" the neighbour is included; at 30" (no unique crossing) the overlapping neighbour is still included with `crosses=False` |
| RA wrap at 0/360 | `test_ra_wrap_plan` | primary+neighbour planned across the wrap, edge-classified |
| Truncated cutout rejected, never padded | `test_truncated_cutout_rejected_not_padded` | `FAILED_ZERO_COVERAGE`, zero cutouts on disk |
| Truncated source FITS rejected | `test_truncated_source_rejected` | `FAILED_FITS_INTEGRITY` |
| Digest custody enforced before FITS open | `test_source_digest_mismatch_rejected` | `FAILED_SOURCE_DIGEST` / `FAILED_SOURCE_MISSING` |
| Missing manifest-required file terminal | `test_missing_required_file_is_terminal_not_skippable` | `ManifestError`, batch refuses to seal |
| Invalid-pixel cap (binding slot) enforced | `test_invalid_pixel_cap_enforced` | all-NaN source → `FAILED_INVALID_PIXEL_CAP` |
| PC-3 receipt on accepted output | `test_corner_cut_completes_with_pc3_pc4_receipts` | constants exact, centre residual ≤1e-6 px, +RA→x decreases, +Dec→y increases, round-trip ≤1e-6 px, coverage min ≥1, planned=opened=contributing, per-source gate receipts PASS |
| Resume after interrupt loses nothing | `test_resume_after_interrupt_loses_nothing` | completed object validated and not recut; remaining objects completed; outputs byte-identical to an uninterrupted run; log chain verifies |
| Input order cannot change outputs | `test_reversed_input_order_is_deterministic` | identical manifest hash and per-object output hashes both directions (work sorted by brick id) |
| Corner objects plan without failure (repair) | `test_exact_and_beyond_corner_objects_plan_without_failure` | exact- and one-pixel-beyond-corner objects plan all 4 bricks; rectangular containment recorded as metadata only |
| Empty intersecting set is the only plan-terminal | `test_empty_intersection_is_terminal_plan_failure` | `FAILED_PLAN_NO_SOURCES` receipt, logged and counted |
| Yui boundary fixtures cross-check, both rounds | `test_cross_check_receipt_passes_both_rounds_separately` | round-1 29/29 (incl. all 8 corner cases) and round-2 4/4 (RA-wrap, dec ±extremes, distinct tangent points, overlap-only) reported separately; source sets equal Yui's oracles; receipt carries a written scope statement and artifact hashes |
| Manifest sealed, sorted, and tamper-evident | `test_dry_run_manifest_sealed_not_submitted` | sorted records, per-file SHA-256, reason classes, geometry sidecar bound, `verify_checksum=true`, `sync_level=checksum`, `skip_source_errors=false`, `submitted=false`, hash breaks if a record is added |
| CLI cannot execute anything real | `test_cli_refuses_everything_but_dry_run`, `test_cli_dry_run_manifest_only` | non-dry-run invocation exits 2 with `BUILD_ONLY_STOP`; dry run seals a manifest and submits nothing |

## Known stand-ins (not tested because out of build-gate scope)

- Synthetic staged bricks are uncompressed primary-HDU FITS; production reads
  fpack-compressed image HDU 1 via the pinned fitsio/Imagine layer.
- The renderer is a deterministic nearest-neighbour stand-in for the
  hash-pinned Imagine/astrometry.net resampler.

Both are declared in every COMPLETED receipt and in
`TORI_ADAPTER_20260815.md`; they are environment-lock-gate obligations.

# AGY Completeness Gate Referee Report
**DATE:** 2026-09-03
**VERSION:** COMPLETENESS-GATE-DRAFT-V3 (UNPINNED)

## TASK A — CLAUSE-BY-CLAUSE CONFORMANCE

- **§3.2 (Dec sign rule):** CONFORMS. `parse_dec(text)` correctly applies `sign = -1.0 if raw[0] == "-" else 1.0` and multiplies by the total parsed sexagesimal quantity `sign * (d + m / 60.0 + s / 3600.0)`.
- **§3.5 (binary64 great-circle):** CONFORMS. `separation_arcsec` correctly implements the Haversine formula (numerically safe for small angles) in binary64.
- **§3.6 (inclusive 1.0 arcsec):** CONFORMS. `separation_arcsec(...) <= 1.0` logic applies inclusive matching correctly.
- **§3.7 (ALL candidates enumerated):** CONFORMS. ADQL `q3c_radial_query` is used without `LIMIT 1` or `ORDER BY dist ASC`, gathering all targets.
- **§3.8 (Duplicate OBJID refusal):** CONFORMS. Enforced in `run_gate` via `seen` set duplicate checks.
- **§3.9 (Zero-candidate unmatched):** CONFORMS. `dispositions[r.objid] = "NO-DR10-WITHIN-1ARCSEC"` for empty candidate lists.
- **§3.10 (≥2 ambiguous):** CONFORMS. `dispositions[r.objid] = "MULTIPLE-DR10-WITHIN-1ARCSEC"` for multiple candidates.
- **§3.11 (GZ collision -> all excluded):** CONFORMS. `unique_owner` maps back to `collided` sets which sets `DR10-COLLISION-AMBIGUOUS`.
- **§3.12 (Exclusions before labels):** CONFORMS. Handled in two loops; label conditions are strictly separated and evaluated only after spatial and identity exclusions.
- **§4.1-4.6 (Tier priority A>B>C, protected-parent):** CONFORMS. Evaluated against `tier_a` then `parent` arrays with `_within` before any labels or pixel paths are checked. Never touches image paths.
- **§4.7-4.11 (0.8 inclusive thresholds):** CONFORMS. `record.p_cw >= LABEL_THRESHOLD` and `record.p_acw >= LABEL_THRESHOLD` enforce inclusive 0.8 boundaries and fails for contradictory labels.
- **§4.12 (NO magnitude cut):** CONFORMS. The ADQL query `make_sync_adql` restricts matches only via `q3c_radial_query` geometry.
- **§4.13-4.14 (canonical sort):** CONFORMS. `pairs.sort(key=lambda p: (int(p.gz1_objid), int(p.dr10_brickid), int(p.dr10_objid)))`.
- **§5.1 (COMPLETE relation):** CONFORMS. Explicitly targets `ls_dr10.tractor_s`.
- **§5.2 (13,725 prior-unresolved terminal disposition):** MISSING. The code defines `prior_unresolved_objids` as an argument to `run_pinned_files()`, but no script or routine actually loads the pinned file containing the 13,725 positions or calls `run_pinned_files` to execute the whole gate.
- **§5.3 (Nothing inferred):** CONFORMS. Exact queries run via q3c without rectangle heuristics.
- **§5.4 (Receipt bindings):** CONFORMS. Done exactly inside `run_gate`.
- **§5.5 (exactly once):** CONFORMS. Verifies `sorted(indices) == list(range(expected_rows))` guaranteeing index sets.
- **§5.6 (Enumeration complete inside 1.0):** CONFORMS. Checks are made server-side (ADQL) and exactly capped inside the client via `_admit_rows` bounding loop.
- **§5.7 (refusal on any gap):** DEVIATES. Because there is no final loop or runner script to finalize the chunks, global gap refusal isn't fully orchestrated.

## TASK B — ROUTE C EVIDENCE

- **URL derived from capabilities?** DEVIATES. `probe()` retrieves `advertised_sync` via `discover_interfaces()` but then overrides it: `sync_url = requested + "/sync"`.
- **q3c_radial_query radius:** CONFORMS. Radius is set to one bit above via `math.nextafter(1.0 / 3600.0, math.inf)`. Client recomputes exact `<= 1.0` arcsec filter on all returned elements in `_admit_rows`.
- **Provenance exact and collision-free?** CONFORMS. The ADQL `CASE` only emits one `input_index` for overlapping cones, but the client safely expands provenance by checking: `matches = [r.input_index for r in records if separation_arcsec(...) <= 1.0]` and attributes the row to all correct GZ1 geometries in the chunk.
- **OR-ed query length bounded?** CONFORMS. At `CHUNK_SIZE=100`, the query string length is roughly ~5000 characters, easily bypassing standard HTTP ADQL length limits. 
- **Overflow terminal signal:** CONFORMS. Evaluated precisely from XML `INFO` tags at EOF checking for `OVERFLOW` strings. 

## TASK C — RESUME/CUSTODY

- **Chunk manifest partitions exactly once:** CONFORMS.
- **Append-only checkpoint hashes raw bytes:** CONFORMS.
- **Resume re-verifies:** CONFORMS.
- **One successful attempt per chunk:** CONFORMS.
- **Partial chunk admitted?** CONFORMS locally (requires exactly chunk-size contiguous indices), but MISSING globally because finalisation logic does not exist to stitch chunks to complete the gate.

## TASK D — TESTS

Output of `test_completeness_gate.py`:
```
test_backend_duplicate_candidate_refused (__main__.MatchTests) ... ok
test_equality_at_one_arcsecond_is_inclusive (__main__.MatchTests) ... ok
test_gz_collision_excludes_all_owners (__main__.MatchTests) ... ok
test_ra_wrap_great_circle (__main__.MatchTests) ... ok
test_zero_one_two_candidates (__main__.MatchTests) ... ok
test_csv_duplicate_is_checked_by_gate (__main__.ParserTests) ... ok
test_declination_sign_applies_to_whole_quantity (__main__.ParserTests) ... ok
test_official_gzip_csv_is_parsed (__main__.ParserTests) ... ok
test_parser_requires_printed_dec_sign (__main__.ParserTests) ... ok
test_ra_wrap_and_invalid_24_hours (__main__.ParserTests) ... ok
test_missing_prior_unresolved_position_refused_exactly (__main__.ReceiptTests) ... ok
test_required_receipt_fields_present (__main__.ReceiptTests) ... ok
test_row_once_gap_refused_exactly (__main__.ReceiptTests) ... ok
test_canonical_pair_sort_uses_integer_keys (__main__.TierAndLabelTests) ... ok
test_contradictory_labels_refused_exactly (__main__.TierAndLabelTests) ... ok
test_equality_at_point_eight_is_inclusive (__main__.TierAndLabelTests) ... ok
test_tier_priority_a_then_b_then_c (__main__.TierAndLabelTests) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.026s

OK
```
Output of `test_tap_source.py`:
```
test_429_honors_retry_after_and_retries (__main__.FakeServerTest) ... ok
test_clean_checkpoint_and_http_capture (__main__.FakeServerTest) ... ok
test_missing_cap_signal_refuses (__main__.FakeServerTest) ... ok
test_overflow_refuses_without_checkpoint (__main__.FakeServerTest) ... ok
test_provenance_expands_overlapping_cones_exactly (__main__.FakeServerTest) ... ok
test_query_is_all_candidate_q3c_case_and_no_upload (__main__.FakeServerTest) ... ok
test_resume_verifies_hash_restores_rows_and_does_not_recreate (__main__.FakeServerTest) ... ok
test_exact_893212_partition_has_no_gap_or_overlap (__main__.ManifestTest) ... ok
test_noncanonical_input_index_set_refuses (__main__.ManifestTest) ... ok

----------------------------------------------------------------------
Ran 9 tests in 3.561s

OK
```
- Exact refusal strings? Yes.
- Equality at 1.0 arcsec? Yes.
- Equality at 0.8? Yes.
- Dec sign? Yes.
- DR10 row near two positions? Yes.
- Overflow refusal? Yes.
- Missing QUERY_STATUS refusal? Yes.
- Manifest gap refusal? Yes.
- Resume hash mismatch? Yes.
- Missing cases? None.

## TASK E — BOUNDARIES

- No pixel/FITS access anywhere: CONFORMS.
- Network only in tap_source: CONFORMS.
- No writes outside completeness_gate/artifacts: CONFORMS.
- Live acquisition untouched: CONFORMS.

## VERDICT AND FINDINGS

**C1: Missing Executable Finalization Script**
- **Severity:** HIGH
- **File/Line:** `completeness_gate.py` and `tap_source.py`
- **Clause:** §5.2, §5.7
- **Repair:** Create an executable Python script (`run_gate_final.py` or similar) that loops over all chunks in `tap_source.py`, collects all results, loads the 13,725 prior unresolved OBJIDs from their pinned file, concatenates them, and calls `run_pinned_files()`.

**C2: Hardcoded TAP Sync URL**
- **Severity:** MEDIUM
- **File/Line:** `tap_source.py:303`
- **Clause:** §5.4 (implicit in Route C Evidence)
- **Repair:** Change `sync_url = requested + "/sync"` inside `probe()` to `sync_url = advertised_sync` to properly use the dynamically queried standard standard TAP interface endpoint.

SEAT: AGY
VERSION: COMPLETENESS-GATE-REFEREE-V1
VERDICT: PINNABLE-AFTER-REPAIRS
COUNT: 2


SEAT: AGY
VERSION: COMPLETENESS-GATE-REFEREE-V2
VERDICT: PINNABLE-AFTER-REPAIRS
COUNT: C3, C4
C1: CLOSED
C2: CLOSED
PRIOR_UNRESOLVED_REDERIVED: 13725
ESTIMATE: 28

### Task A — Closure of C1 and C2
- **C1 (CLOSED):**
  - **(a)** `run_full.py` explicitly matches all core input files against `PINNED_DIGESTS` before use.
  - **(b)** The `prior_unresolved_13725.json` file is correctly formatted, checks the 13,725 count, and guards against duplicates. I ran an independent script evaluating the exact rule against `gz1_parsed.csv.gz`, `survey-bricks-dr10-south.fits.gz`, and `gz_dr10_matches.csv.gz` which re-derived exactly 13,725 unresolved objects.
  - **(c)** `TAPCandidateSource.run_chunk()` processes manifest items with exactly a single worker and a forced `CREATE_INTERVAL_SECONDS = 2.0` pace.
  - **(d)** `chunk_manifest.json` exactly partitions rows 0 through 893,211. `execute()` properly blocks `run_pinned_files()` and the §5 receipt until all 893,212 indices are identically represented.
  - **(e)** A dry run using `--dry-finalise` successfully triggers the gap refusal exactly as requested (reporting 300 covered input indices, exactly 3 admitted chunks, and correctly failing with `COMPLETENESS-FAIL: dry-finalise gap`).

- **C2 (CLOSED):**
  - The sync URL is explicitly parsed from the TAP capability endpoint using `discover_interfaces()`. It is strictly verified before proceeding (`if not sync: fail("capabilities/probe receipt lacks advertised TAP sync endpoint")`).

### Task B — Regression Audit
- A DR10 row within 1 arcsec of overlapping GZ1 source positions is now properly attributed to BOTH, as the client loops over all matched GZ1 inputs and evaluates `separation_arcsec`.
- No magnitude, flux, or quality predicates remain in the sync ADQL (`make_sync_adql()`).
- `MAXREC`/`QUERY_STATUS` cap detection is enforced by `require_uncapped()` and terminal on failure.
- Manifest partition chunks correctly divide exactly once into 8,933 chunks of size 100.

### Task C — Tests
All 30 unit/integration tests run and pass without failure. 
- The fake-server chunk run and resume is explicitly checked in `test_five_chunks_resume_after_uncheckpointed_killed_attempt` and `test_resume_verifies_hash_restores_rows_and_does_not_recreate`.
- The dry-finalise gap refusal is tested in `test_dry_finalise_gap_refuses_without_receipt` and `test_row_once_gap_refused_exactly`.
- The prior count refusal is tested in `test_prior_count_refusal`.
- Two-position overlap matching is validated in `test_one_dr10_row_is_attributed_to_both_positions`.
No missing test cases were identified.

### Task D — Live-Run Readiness & Findings
My estimate is ~28 hours (8933 chunks * 11.3s/chunk = 100,942s = ~28h). 

During analysis for the 28-hour unattended run, the following issues were identified:
- **C3 (Checkpoint corruption on kill):** `checkpoint.jsonl` is written in standard append mode without atomicity or temporary files (`f.write()`). If the process receives a termination signal midway through the write, a partial JSON line will remain. On startup, `_checkpoint_map()` attempts to `json.loads` every line, triggering a `JSONDecodeError` that crashes the runner until a human operator intervenes to manually strip the broken record.
- **C4 (No automatic resume on network drop):** The HTTP client employs a 6-attempt exponential backoff. If a network outage extends beyond this duration (approx. 63 seconds total), the client throws a terminal exception, breaking the process. There is no outer loop that traps this to infinitely resume the remaining chunks, requiring an operator to manually monitor and re-invoke the script with `--resume`.
- All outputs (chunks, manifest, checkpoint, pairs, receipts) are strictly confined to the designated `artifacts` directory, which defaults to `completeness_gate/artifacts_full/`.

### Pytest Output
```
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
cachedir: .pytest_cache
rootdir: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/completeness_gate
plugins: anyio-4.12.1, langsmith-0.4.37, cov-7.0.0
collecting ... collected 30 items

test_completeness_gate.py::ParserTests::test_csv_duplicate_is_checked_by_gate PASSED [  3%]
test_completeness_gate.py::ParserTests::test_declination_sign_applies_to_whole_quantity PASSED [  6%]
test_completeness_gate.py::ParserTests::test_official_gzip_csv_is_parsed PASSED [ 10%]
test_completeness_gate.py::ParserTests::test_parser_requires_printed_dec_sign PASSED [ 13%]
test_completeness_gate.py::ParserTests::test_ra_wrap_and_invalid_24_hours PASSED [ 16%]
test_completeness_gate.py::MatchTests::test_backend_duplicate_candidate_refused PASSED [ 20%]
test_completeness_gate.py::MatchTests::test_equality_at_one_arcsecond_is_inclusive PASSED [ 23%]
test_completeness_gate.py::MatchTests::test_gz_collision_excludes_all_owners PASSED [ 26%]
test_completeness_gate.py::MatchTests::test_ra_wrap_great_circle PASSED  [ 30%]
test_completeness_gate.py::MatchTests::test_zero_one_two_candidates PASSED [ 33%]
test_completeness_gate.py::TierAndLabelTests::test_canonical_pair_sort_uses_integer_keys PASSED [ 36%]
test_completeness_gate.py::TierAndLabelTests::test_contradictory_labels_refused_exactly PASSED [ 40%]
test_completeness_gate.py::TierAndLabelTests::test_equality_at_point_eight_is_inclusive PASSED [ 43%]
test_completeness_gate.py::TierAndLabelTests::test_tier_priority_a_then_b_then_c PASSED [ 46%]
test_completeness_gate.py::ReceiptTests::test_missing_prior_unresolved_position_refused_exactly PASSED [ 50%]
test_completeness_gate.py::ReceiptTests::test_required_receipt_fields_present PASSED [ 53%]
test_completeness_gate.py::ReceiptTests::test_row_once_gap_refused_exactly PASSED [ 56%]
test_tap_source.py::FakeServerTest::test_429_honors_retry_after_and_retries PASSED [ 60%]
test_tap_source.py::FakeServerTest::test_clean_checkpoint_and_http_capture PASSED [ 63%]
test_tap_source.py::FakeServerTest::test_missing_cap_signal_refuses PASSED [ 66%]
test_tap_source.py::FakeServerTest::test_overflow_refuses_without_checkpoint PASSED [ 70%]
test_tap_source.py::FakeServerTest::test_provenance_expands_overlapping_cones_exactly PASSED [ 73%]
test_tap_source.py::FakeServerTest::test_query_is_all_candidate_q3c_case_and_no_upload PASSED [ 76%]
test_tap_source.py::FakeServerTest::test_resume_verifies_hash_restores_rows_and_does_not_recreate PASSED [ 80%]
test_tap_source.py::ManifestTest::test_exact_893212_partition_has_no_gap_or_overlap PASSED [ 83%]
test_tap_source.py::ManifestTest::test_noncanonical_input_index_set_refuses PASSED [ 86%]
test_run_full.py::RunFullE2E::test_dry_finalise_gap_refuses_without_receipt PASSED [ 90%]
test_run_full.py::RunFullE2E::test_five_chunks_resume_after_uncheckpointed_killed_attempt PASSED [ 93%]
test_run_full.py::RunFullE2E::test_one_dr10_row_is_attributed_to_both_positions PASSED [ 96%]
test_run_full.py::RunFullE2E::test_prior_count_refusal PASSED            [100%]

============================= 30 passed in 11.68s ==============================
```

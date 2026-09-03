ACCESS_SHA=bc361a124e964dbd44d464f09c841c69ff310226a8a022cf1f837b7795f06e40

# Completeness Gate 2-Worker Review

## Task A: Guarantees Under 2 Workers

1. **Exactly ONE writer appends the checkpoint:**
   The `fetcher` threads don't write to the checkpoint file directly. They place their results in a thread-safe `completed` queue (`completed.put(("ok", metadata))`). The main thread acts as the single writer, popping from this queue and writing sequentially:
   ```python
   while written < len(todo):
       kind, value = completed.get()
       if kind == "error": raise value
       append_jsonl(artifacts / "checkpoint.jsonl", value)
       written += 1
   ```
2. **Two fetchers never take the same chunk id nor an already admitted one:**
   Unadmitted chunks are filtered prior to fetching (`todo = [c for c in manifest["chunks"] if c["chunk_id"] not in admitted]`). Fetchers acquire chunk IDs atomically under `pending_lock` by advancing `state["next"]`.
3. **Per-chunk artifacts and receipts unchanged; MAXREC + terminal QUERY_STATUS checks unchanged:**
   `MAXREC` is hardcoded to `"10000"` in `fetch_chunk`. The `cap_signal = require_uncapped(status, chunk_id)` check is preserved unmodified in `fetch_chunk`.
4. **Admission order interleaves (checkpoint treated as a SET):**
   `run_full.py`'s `_checkpoint_map` loads entries and just ensures set membership and absence of duplicates. `tap_source.py` was explicitly modified to sort the checkpoint entries by `chunk_id` when calculating provenance to prevent non-deterministic hashes due to interleaving:
   ```python
   # Checkpoint admission order may interleave; provenance is manifest order.
   entries = sorted(self._checkpoint_entries(), key=lambda entry: entry["chunk_id"])
   ```
5. **Kill of both fetchers mid-chunk / torn-tail handling:**
   The single writer (main thread) ensures that only the very end of `checkpoint.jsonl` could be torn if interrupted mid-append. `read_checkpoint(..., repair_tail=True)` truncates the final malformed line, leaving all cleanly appended chunks valid. The orphaned attempt directories remain but are ignored since their chunks are re-queued.
6. **429/5xx/timeout on either fetcher drops to 1 worker:**
   `HttpClient` invokes the `on_retryable` callback, which delegates to `downgrade()` in `run_full.py`:
   ```python
   def downgrade(detail: Mapping[str, object]) -> None:
       with pending_lock:
           if state["active_workers"] == 1: return
           state["active_workers"] = 1
   ```
   Fetchers stop taking new tasks if `worker_id >= state["active_workers"]`, leaving only worker 0 active.
7. **Completeness receipt bytes IDENTICAL between 1 and 2 workers:**
   Confirmed. Tests (`test_worker_count_does_not_enter_analytical_receipt`) successfully assert digest equality regardless of the thread count, enabled by the provenance sort fix mentioned in (4).

## Task B: Diff Discipline
Zero findings. All changes tightly scoped to the queue/thread pool plumbing, the pacing lock, the down-scaling callback, and the tests.

## Task C: Tests
```
$ python3 test_run_full.py
test_cli_outage_budget_exhaustion_exits_75_with_status (__main__.RunFullE2E) ... ok
test_dry_finalise_gap_refuses_without_receipt (__main__.RunFullE2E) ... ok
test_one_dr10_row_is_attributed_to_both_positions (__main__.RunFullE2E) ... ok
test_prior_count_refusal (__main__.RunFullE2E) ... ok
test_retryable_response_drops_to_one_worker (__main__.RunFullE2E) ... ok
test_two_workers_admit_interleaved_exactly_once (__main__.RunFullE2E) ... ok
test_two_workers_resume_after_both_uncheckpointed_killed_attempts (__main__.RunFullE2E) ... ok
test_worker_count_does_not_enter_analytical_receipt (__main__.RunFullE2E) ... ok
----------------------------------------------------------------------
Ran 8 tests in 5.518s
OK

$ python3 test_tap_source.py
test_429_honors_retry_after_and_retries (__main__.FakeServerTest) ... ok
test_clean_checkpoint_and_http_capture (__main__.FakeServerTest) ... ok
test_corrupt_middle_checkpoint_line_refuses (__main__.FakeServerTest) ... ok
test_missing_cap_signal_refuses (__main__.FakeServerTest) ... ok
test_outage_budget_exhaustion_leaves_checkpoint_unchanged (__main__.FakeServerTest) ... ok
test_outage_failures_then_recovery_retries_same_chunk (__main__.FakeServerTest) ... ok
test_overflow_refuses_without_checkpoint (__main__.FakeServerTest) ... ok
test_provenance_expands_overlapping_cones_exactly (__main__.FakeServerTest) ... ok
test_query_is_all_candidate_q3c_case_and_no_upload (__main__.FakeServerTest) ... ok
test_resume_verifies_hash_restores_rows_and_does_not_recreate (__main__.FakeServerTest) ... ok
test_torn_checkpoint_tail_is_discarded_and_exactly_one_chunk_reruns (__main__.FakeServerTest) ... ok
test_exact_893212_partition_has_no_gap_or_overlap (__main__.ManifestTest) ... ok
test_noncanonical_input_index_set_refuses (__main__.ManifestTest) ... ok
----------------------------------------------------------------------
Ran 13 tests in 5.622s
OK
```

SEAT: AGY
VERSION: COMPLETENESS-2WORKERS-REFEREE-V1
VERDICT: PINNABLE
RECEIPT_IDENTICAL_1v2: confirmed
COUNT: 0

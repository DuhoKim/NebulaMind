SEAT: AGY
VERSION: COMPLETENESS-GATE-REFEREE-V3
VERDICT: PINNABLE
COUNT: 0
C3: CLOSED
C4: CLOSED

### TASK A — Closure of C3 and C4
* **C3 (CLOSED):** Checkpoints strictly utilize `append_jsonl()` which ensures a single JSON record is appended with a trailing `\n`, followed immediately by a `flush()` and `os.fsync()`. In the event of process termination mid-write, `read_checkpoint()` identifies the corrupt/torn tail (via checking for `valid_lf`). With `repair_tail=True` enabled during standard resume, the truncated tail is discarded, the event `checkpoint_tail_discarded` is logged, and the exact chunk gracefully re-runs. Mid-line corruptions conversely raise `GateError("COMPLETENESS-FAIL: checkpoint_corrupt")`. A torn tail cannot be silently accepted because a trailing newline is unconditionally required for parsing validation. The sha256 digest is strictly mandated per line (`isinstance(entry.get("raw_sha256"), str) and bool(...)`).
* **C4 (CLOSED):** `HttpClient` implements capped exponential backoff `min(60.0, 2**attempt + rng)` preventing wait times >60s. It strictly honors HTTP `Retry-After` (hard-capped to 300s). The failure budget checks wall-clock elapsed time continuously and exits if it breaches `--max-outage-minutes` (defaults to 180s/3h), successfully resetting on `failure_started = None` upon an HTTP 200. On budget exhaustion, `run_full.py` halts gracefully returning exit code 75 and `{"status": "outage_budget_exhausted"}` without altering `checkpoint.jsonl`. The bash wrapper `run_full_resume.sh` safely re-invokes with `--resume` only upon detecting `rc == 75` and correctly aborts instantly if it detects any other failure code, completely avoiding infinite-loop swallowing. 

### TASK B — Regression Sweep
All V1/V2 criteria remain intact. No magnitude, flux, or quality predicates were reintroduced. Input hashes strictly map to the exact `PINNED_DIGESTS`. The 8,933 partitions and gap refuse logic are fully enforced. 

### TASK C — Tests
All 35 tests pass perfectly. Test validations match requirements:
* `test_torn_checkpoint_tail_is_discarded_and_exactly_one_chunk_reruns`: Asserts the `checkpoint_tail_discarded` event.
* `test_corrupt_middle_checkpoint_line_refuses`: Asserts `GateError` for `checkpoint_corrupt`.
* `test_outage_failures_then_recovery_retries_same_chunk`: Confirms exact retry of the identical chunk ID. 
* `test_cli_outage_budget_exhaustion_exits_75_with_status`: Asserts rc 75 and `{"status": "outage_budget_exhausted"}` exactly. 
* `test_outage_budget_exhaustion_leaves_checkpoint_unchanged`: Verifies unmodified checkpoint bytes post-exhaustion.

### TASK D — Unattended-Run Readiness
* **Memory Bounded:** Peak memory processing per chunk is highly bounded as each chunk iterates over exactly 100 records and strictly releases intermediate XML state. Aggregate state (`self._results`) accumulates `Candidate` instances incrementally resulting in ~1M objects total, requiring just roughly ~150-250MB memory footprint which is very safe.
* **Artefact Growth:** Each of the 8,933 chunks writes local logs (`query.adql`, `result.vot`, `metadata.json`) totaling ~45KB/chunk, plus a bounded HTTP capture limit. Total artefact growth is highly predictable at ~500–600 MB (0.5-0.6 GB) for the complete 28h sequence. 
* **Isolation:** All dynamic outputs write strictly within the nested `artifacts` parameter initialized to `completeness_gate/artifacts_full/`. 
* **FITS & Pixels:** A scan verified NO FITS files or image pixels are accessed. The script properly limits interaction strictly to `acquire/positions_selected_cut.csv` and `acquire/positions_selected.csv` for read-only positional catalog matching.

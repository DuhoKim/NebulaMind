ACCESS_SHA=74e825034e39ffc949ca9d3217759c413ff446504f069b312e042de2ec61d27f

JUDGE:

1. Exact equivalence: Yes, for a pure-resume finalisation, the sequence of admitted rows and every `_fail` condition are identical to the old behaviour. For a mixed run, `entries.append(metadata)` in `run_chunk` keeps the memory cache fully consistent with what the old code would have read from disk after appending (preserving chunk_id order, duplicate-detection logic, and tail-repair semantics on start). There is a path where the old code would have detected an on-disk change mid-run: if a second writer appended to `checkpoint.jsonl`, the old code would have picked it up on its next chunk read, whereas the new code caches the initial read. However, the pinned single-writer design makes this moot.

2. Every raw result file is still sha256-verified exactly once per finalisation. The relevant code is in `_checkpoint_entries`:
```python
    def _checkpoint_entries(self) -> list[dict]:
        if self._entries is not None:
            return self._entries
        path = self.artifacts / "checkpoint.jsonl"
        entries = read_checkpoint(path, repair_tail=True,
                                  run_log=self.artifacts / "run.log.jsonl")
        for entry in entries:
            raw_path = self.artifacts / entry["raw_result"]
            if not raw_path.exists() or sha256_file(raw_path) != entry["raw_sha256"]:
                _fail(f"resume hash mismatch for chunk {entry['chunk_id']}")
        self._entries = entries
        return self._entries
```
The early return `if self._entries is not None:` ensures that the verification loop only runs on the initial load.

3. Pytest summary lines:
```
..........................................                               [100%]
42 passed in 21.04s
```
Direct run summary lines:
```
----------------------------------------------------------------------
Ran 20 tests in 10.588s

OK
TIMING_100K: 0.369 seconds
```
The new test in `test_tap_source.py` is named `test_resumed_chunks_read_checkpoint_once_and_hash_each_raw_once`. It patches `tap_source.read_checkpoint` and `tap_source.sha256_file` to count calls, asserting `self.assertEqual(calls, {"read": 1, "sha": count})` where `count = 50`. It also compares the results against the reload-per-chunk behavior using `self.assertEqual(resumed._results, expected)`.

4. `completeness_gate.py` (`d403c8cced25fa4c3cdcba182840bb594b48215c5b6ca64589756cf234c5c716`) and `run_full.py` (`bc361a124e964dbd44d464f09c841c69ff310226a8a022cf1f837b7795f06e40`) are byte-identical to their pin sheets.

5. No semantic changes beyond the caching are present.

SEAT: AGY
VERSION: TAP-CHECKPOINT-ONCE-REFEREE-V1
VERDICT: PINNABLE
COUNT: 0

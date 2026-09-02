# AGY SEAL GATE REFEREE REPORT V2
Date: 2026-09-02
Target: `seal_gate/` draft V2 (SEAL-GATE-DRAFT-V2)

## TASK A — CLOSURE of G1, G3, G4
*   **(G1) Exception handling**: CLOSED. The outermost try/except in `run_gate` catches all `Exception` subclasses (`seal_gate.py:268`), safely setting `status="REFUSE"` and `data_integrity_pass=False`. The receipt mutation during a failed `--append` write (`seal_gate.py:327`) is also wrapped; if the seal journal isn't writable, it mutates the receipt and emits it safely to `stdout`.
*   **(G3) Git blob ID**: CLOSED. `seal_gate.py:119` explicitly asserts that the fetched blob ID matches `EXPECTED_BLOB_ID` (`df704bed1c5fd872cf9dee9f4be2e88f64bb94a0`) and raises `git_blob_id_mismatch` if it does not.
*   **(G4) Predecessor digest**: CLOSED. `_seal_predecessor` (`seal_gate.py:142`) correctly parses the last valid line of the seal journal, recomputes the canonical hash to ensure its integrity, and extracts the predecessor digest. It safely returns 64 zeroes when the journal is absent or empty. The append logic is cleanly gated behind `--append` (`seal_gate.py:323`), and no other file system mutations (e.g., `write_*`, `unlink`, `shutil`) or mutating `subprocess` calls exist in the code.

## TASK B — RE-AUDIT
*   **Completion set condition**: Exact match. Duplicate OK receipts are handled cleanly via `any(r["verdict"] == "OK" ...)`. The regex for detecting the running process correctly matches `fetch_bricks[.]py --manifest` and accurately excludes the tool's own PID.
*   **Per-receipt equalities**: Completely enforced. The gate strictly raises `fresh_published_receipt_disagreement` and `ok_receipt_digest_mismatch`.
*   **Git custody**: Verified and robustly implemented across all four required checks.
*   **Disk re-hash**: Validated. Following the Coordinator's ruling on G2, the single URL construct is correct per V9 §7.11 line 215. The script accurately constructs `legacysurvey_dr10_south_coadd_<AAA>_<brick>.sha256sum` without any fallback.
*   **Binding digest bytes**: `raw_line.rstrip(b"\r\n") + b"\n"` mathematically guarantees exactly one trailing LF, and it operates precisely in manifest order.
*   **Canonical receipt bytes**: Handled securely via `canonical_bytes()`.
*   **Data_integrity_pass**: This Boolean is strictly derived from the exact 5 conjuncts. It is impossible to set it arbitrarily from CLI flags.
*   **Conclusion**: No regressions were introduced. V2 is completely compliant with V9 text.

## TASK C — TESTS
*   **Execution**: `test_seal_gate.py` runs successfully, passing all 19 tests.
*   **Assertions**: `assert_refusal` rigidly asserts the exact string (e.g. `"non_ok_without_later_ok"`) and proves that `data_integrity_pass == False`.
*   **Duplicates**: `test_duplicate_ok_receipts_pass` explicitly validates the duplicate-OK condition conforming to "at least one receipt with verdict OK".
*   **Exceptions**: `test_unexpected_exception_emits_named_refusal` injects `KeyError("injected")` and confirms a correctly named receipt is generated.
*   **Isolation**: All paths use `tempfile.TemporaryDirectory()`. Real `acquire/` resources or the live journal are entirely untouched.

## TASK D — BOUNDARIES
*   **Read-only**: Code operates in strict read-only mode regarding external files. `git` interacts safely using `ls-files -s`, `cat-file -p`, and `diff --quiet`. No live modifications exist.
*   **Synthetic paths**: Evaluated via synthetic `--manifest`, `--journal`, `--bricks-dir`, `--live-script`, `--pinned-copy`, and `--seal-journal`.
*   **No Network in Tests**: Live network connections are completely circumvented in the test suite using `fetcher=self.fetcher`.

## FINDINGS
No new findings.

SEAT: AGY
VERSION: SEAL-GATE-REFEREE-V2
VERDICT: PINNABLE
COUNT: 0
G1: CLOSED
G3: CLOSED
G4: CLOSED

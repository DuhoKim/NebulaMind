# AGY SEAL GATE REFEREE REPORT
Date: 2026-09-02
Target: `seal_gate/` draft (SEAL-GATE-DRAFT-V1)

## TASK A — CLAUSE-BY-CLAUSE CONFORMANCE

**Completion (17,947 count, OK logic, running process)**
*   *Clause §7.11*: "the set of `brick` values having at least one receipt with `verdict == \"OK\"`... equals the 17,947-element manifest set... no process matching `fetch_bricks[.]py --manifest` is running"
*   *Implementation*: `seal_gate.py:182` checks `ok_bricks != manifest_bricks`. `seal_gate.py:170` checks `len(entries) != expected_manifest_count` (defaults to 17947). `seal_gate.py:98` uses `re.compile(r"fetch_bricks[.]py --manifest(?:\s|$)")` and safely excludes its own PID. Duplicate OK receipts are permitted by `any(r["verdict"] == "OK")`. Non-OK without later OK causes refusal (`seal_gate.py:186`).
*   *Status*: **CONFORMS**. (Note: The regex strictly follows the text and will not match a renamed script, which is exact to the letter of the clause).

**Per-receipt equality and journal recording**
*   *Clause §7.11*: "every OK receipt has `computed_sha256` equal to `published_sha256`... `journal_head_sha256`... and `receipt_count`"
*   *Implementation*: `seal_gate.py:178` raises `ok_receipt_digest_mismatch`. Lines 173-174 bind `journal_head_sha256` and line count.
*   *Status*: **CONFORMS**.

**Git Custody**
*   *Clause §7.11*: "Git custody receipt passed" (incorporating the blob IDs listed).
*   *Implementation*: `_git_custody` (lines 107-132) checks `git ls-files -s`, `git cat-file -p`, and `git diff --quiet`. It enforces that `git_blob_content_sha256`, `live_file_sha256`, and `pinned_copy_sha256` are identical, and that the working tree is clean. However, it only *records* the `git_blob_id` without validating it against the specific hash `df704bed1c5fd872cf9dee9f4be2e88f64bb94a0` mentioned in the prose.
*   *Status*: **DEVIATES**. Binds the content identically, but only records (does not assert) the explicit blob ID.

**Content Re-hash**
*   *Clause §7.11*: "URL convention identical to `published_sha()` in the pinned copy... binding digest = sha256 of fetched checksum lines in MANIFEST ORDER each with exactly one trailing LF"
*   *Implementation*: `seal_gate.py:207-231` verifies disk sha256 against fetched value and receipt values. `raw_line.rstrip(b"\r\n") + b"\n"` mathematically guarantees exactly one trailing LF regardless of original line endings.
*   *Status*: **DEVIATES**. The `checksum_url` function (`seal_gate.py:47`) only builds one URL format (`legacysurvey_dr10_south_coadd_{aaa}_{brick}.sha256sum`). The pinned script's `published_sha()` has a three-URL fallback sequence.

**Seal Receipt**
*   *Clause §7.10/§16.3*: Schema fields, canonical JSON receipt digest excluding itself, predecessor digest.
*   *Implementation*: `canonical_bytes` (`seal_gate.py:43`) sorts keys and removes spaces. The digest is computed over the body before the digest key itself is added (`seal_gate.py:258`). The predecessor digest is not read from the journal; it is "invented" via the CLI argument `--predecessor-digest` (defaults to 64 zeroes, which §7.10 states is correct for the *first* record).
*   *Status*: **CONFORMS** (assuming this gate represents the first seal journal record).

**Data Integrity Pass**
*   *Clause §16.7c*: Derived exactly as the 5 conjuncts.
*   *Implementation*: `seal_gate.py:235` derives it strictly from the Boolean combinations of the verification logic, plus `status == "PASS"`. Never settable by flag.
*   *Status*: **CONFORMS**.

---

## TASK B — FAIL-CLOSED AUDIT

**Failure Paths:**
*   **Fetch error**: Caught by `except Exception`, raises `GateFailure("published_checksum_fetch_failed")` -> REFUSE.
*   **Missing checksum file**: 404 raises exception -> REFUSE.
*   **Malformed line**: Raises `GateFailure("missing_or_malformed_checksum_line")` -> REFUSE.
*   **Disagreement**: Raises `GateFailure("fresh_published_receipt_disagreement")` -> REFUSE.
*   **Missing file**: Raises `GateFailure("missing_brick_file")` -> REFUSE.
*   **Extra file**: Raises `GateFailure("extra_brick_file")` -> REFUSE. (V9 §7.11 notes the Tier-C dest is used to keep the "#52 closure's zero-extra-files invariant checkable", so failing on extra files is intended).
*   **Hash mismatch**: Raises `GateFailure("disk_hash_mismatch")` -> REFUSE.
*   **Unequal count**: Raises `GateFailure("manifest_count_mismatch")` -> REFUSE.
*   **Process running**: Raises `GateFailure("acquisition_process_running")` -> REFUSE.
*   **Git mismatch**: Raises `git_worktree_dirty` or `git_custody_digest_mismatch` -> REFUSE.
*   **Journal parse error**: Raises `GateFailure("malformed_journal")` -> REFUSE.
*   **Omit `--fetch`**: Raises `GateFailure("published_checksum_refetch_not_requested")` -> REFUSE.

**Exceptions swallowed?**
No exception is swallowed into a PASS. However, if a built-in exception like `KeyError` or `AttributeError` occurs (e.g., unexpected JSON structure not fully caught by schema checks), it bypasses `except (GateFailure, OSError, ValueError, TypeError)`. This crashes the gate with exit code 1, but **fails to emit a receipt** naming the cause, violating the receipt requirement.

---

## TASK C — TESTS

*   **Assertions**: `test_seal_gate.py` uses `assert_refusal` which asserts the exact strings `"REFUSE"`, `"DATA-INTEGRITY-FAIL"`, the exact failure reason, and `data_integrity_pass == False`.
*   **Happy-path test**: `test_all_good` successfully asserts all 5 conjuncts and digest calculations.
*   **Fake fetcher realistic?**: Yes, `f"{digest}  {filename}\r\n".encode()` correctly mimics NERSC `.sha256sum` files.
*   **Missing test cases**:
    *   Duplicate OK receipts.
    *   URL fetch network error.
    *   Malformed journal JSON / schema.
    *   `--fetch` omitted.
    *   Git working tree dirty (`git diff` returning non-zero).
    *   Unexpected exceptions (e.g. `KeyError`).

*   **Test Run Output**:
```text
test_all_good (__main__.SealGateTests) ... ok
test_disk_hash_mismatch (__main__.SealGateTests) ... ok
test_extra_file_refuses_under_section_7_8 (__main__.SealGateTests) ... ok
test_fresh_published_disagrees_with_receipt (__main__.SealGateTests) ... ok
test_git_custody_mismatch (__main__.SealGateTests) ... ok
test_incomplete_journal (__main__.SealGateTests) ... ok
test_missing_file (__main__.SealGateTests) ... ok
test_non_ok_without_later_ok (__main__.SealGateTests) ... ok
test_process_running (__main__.SealGateTests) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.019s

OK
```

---

## TASK D — BOUNDARIES

*   **Read-only behaviour**: Confirmed. Directory reading uses `iterdir()`; files are read with `.read_bytes()` and `urllib`; git interactions are purely `ls-files -s`, `cat-file -p`, and `diff --quiet`. No mutating commands exist in the gate.
*   **Synthetic paths**: Confirmed. The tool utilizes `--manifest`, `--journal`, `--bricks-dir`, `--live-script`, and `--pinned-copy` arguments. It can strictly run against mock data without ever touching the live acquisition.

---

## FINDINGS

**G1** (MAJOR) - `seal_gate.py:232`, Clause §16.3
*Defect*: Exception handler `except (GateFailure, OSError, ValueError, TypeError)` misses arbitrary runtime exceptions (like `KeyError` or `AttributeError`). The tool will exit 1 but fail to emit a valid JSON refusal receipt as required.
*Repair*: Change line 232 to `except Exception as exc:`

**G2** (MAJOR) - `seal_gate.py:47-50`, Clause §7.11
*Defect*: URL convention deviates from `published_sha()` in `fetch_bricks_pinned.py`. The gate constructs exactly one URL, missing the 3-item fallback sequence present in the pinned code.
*Repair*: Implement the exact tuple iteration `for name in (f"legacysurvey_dr10_south_coadd_{aaa}_{brick}.sha256sum", f"legacysurvey-{brick}.sha256sum", "checksums.sha256"):` for URL construction.

**G3** (MINOR) - `seal_gate.py:110-132`, Clause §7.11
*Defect*: Git custody only checks that the live and pinned files share the exact same hash as the working tree blob. It records the `git_blob_id` but does not assert it equals `df704bed1c5fd872cf9dee9f4be2e88f64bb94a0` as explicitly called out in the text.
*Repair*: Explicitly assert `blob_id == "df704bed1c5fd872cf9dee9f4be2e88f64bb94a0"`.

**G4** (MINOR) - `seal_gate.py:270`, Clause §7.10
*Defect*: Predecessor digest is an arbitrary argument with a fallback, not directly read from a verifiable chain. This is permissible for the first record but requires external trust of the argument.
*Repair*: N/A if verified by caller wrapper, but strictly it is invented rather than read.

SEAT: AGY
VERSION: SEAL-GATE-REFEREE-V1
VERDICT: NOT-PINNABLE
COUNT: 4

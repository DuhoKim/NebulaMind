# Seal gate draft V3 implementation log

Date: 2026-09-03

Implemented Duho's overnight ruling “Hwao a” over all four verdicts and both
receipt shapes written by `miniprereg_pins/fetch_bricks_pinned.py` lines
136--153. No pixels or network were accessed. Neither `acquire/`, the
acquisition journal, nor `SEAL_GATE_PIN_20260903.md` was modified.

The V9-to-V10 unified diff hunk headers are:

```text
@@ -1,8 +1,8 @@
@@ -162,7 +162,28 @@
@@ -510,12 +531,13 @@
@@ -528,5 +550,5 @@
```

Command:

```text
cd seal_gate && python3 -m unittest -v test_seal_gate.py
```

Real output:

```text
test_all_good (test_seal_gate.SealGateTests) ... ok
test_disk_hash_mismatch (test_seal_gate.SealGateTests) ... ok
test_duplicate_ok_receipts_pass (test_seal_gate.SealGateTests) ... ok
test_extra_file_refuses_under_section_7_8 (test_seal_gate.SealGateTests) ... ok
test_fetch_failed_then_later_ok_passes (test_seal_gate.SealGateTests) ... ok
test_fetch_failed_without_later_ok_refuses (test_seal_gate.SealGateTests) ... ok
test_fetch_network_error (test_seal_gate.SealGateTests) ... ok
test_fetch_omitted (test_seal_gate.SealGateTests) ... ok
test_five_key_ok_is_malformed (test_seal_gate.SealGateTests) ... ok
test_fresh_published_disagrees_with_receipt (test_seal_gate.SealGateTests) ... ok
test_genesis_predecessor_when_seal_journal_absent (test_seal_gate.SealGateTests) ... ok
test_git_blob_id_mismatch (test_seal_gate.SealGateTests) ... ok
test_git_custody_mismatch (test_seal_gate.SealGateTests) ... ok
test_git_worktree_dirty (test_seal_gate.SealGateTests) ... ok
test_incomplete_journal (test_seal_gate.SealGateTests) ... ok
test_malformed_journal_json (test_seal_gate.SealGateTests) ... ok
test_missing_file (test_seal_gate.SealGateTests) ... ok
test_ok_no_published_sha_without_later_ok_refuses_as_non_ok (test_seal_gate.SealGateTests) ... ok
test_ok_with_published_null_is_malformed (test_seal_gate.SealGateTests) ... ok
test_predecessor_from_two_record_seal_journal (test_seal_gate.SealGateTests) ... ok
test_process_running (test_seal_gate.SealGateTests) ... ok
test_seal_journal_chain_broken (test_seal_gate.SealGateTests) ... ok
test_sha_mismatch_quarantined_then_later_ok_passes (test_seal_gate.SealGateTests) ... ok
test_unexpected_exception_emits_named_refusal (test_seal_gate.SealGateTests) ... ok
test_unknown_verdict_is_malformed (test_seal_gate.SealGateTests) ... ok

----------------------------------------------------------------------
Ran 25 tests in 0.045s

OK
```

SEAT: CODEX
VERSION: MINI-PREREG-DRAFT-V10 + SEAL-GATE-DRAFT-V3
TESTS: 25/25
COUNT: 179

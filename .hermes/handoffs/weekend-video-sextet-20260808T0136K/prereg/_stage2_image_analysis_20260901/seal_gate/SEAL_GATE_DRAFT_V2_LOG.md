# Seal gate draft V2 implementation log

Date: 2026-09-02

Implemented accepted findings G1, G3, and G4 from
`AGY_SEAL_GATE_REFEREE_20260902.md`. Preserved the single ruled checksum URL
under the coordinator's G2 rejection and documented the §7.11 line 215 ruling
in code and README. No network was used.

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
test_fetch_network_error (test_seal_gate.SealGateTests) ... ok
test_fetch_omitted (test_seal_gate.SealGateTests) ... ok
test_fresh_published_disagrees_with_receipt (test_seal_gate.SealGateTests) ... ok
test_genesis_predecessor_when_seal_journal_absent (test_seal_gate.SealGateTests) ... ok
test_git_blob_id_mismatch (test_seal_gate.SealGateTests) ... ok
test_git_custody_mismatch (test_seal_gate.SealGateTests) ... ok
test_git_worktree_dirty (test_seal_gate.SealGateTests) ... ok
test_incomplete_journal (test_seal_gate.SealGateTests) ... ok
test_malformed_journal_json (test_seal_gate.SealGateTests) ... ok
test_missing_file (test_seal_gate.SealGateTests) ... ok
test_non_ok_without_later_ok (test_seal_gate.SealGateTests) ... ok
test_predecessor_from_two_record_seal_journal (test_seal_gate.SealGateTests) ... ok
test_process_running (test_seal_gate.SealGateTests) ... ok
test_seal_journal_chain_broken (test_seal_gate.SealGateTests) ... ok
test_unexpected_exception_emits_named_refusal (test_seal_gate.SealGateTests) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.033s

OK
```

SEAT: CODEX
VERSION: SEAL-GATE-DRAFT-V2
TESTS: 19/19

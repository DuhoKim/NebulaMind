# r3c2_staged_d1d7 — STAGED, UNADOPTED tooling for the D1 / D7 / batch candidates (2026-09-06 20:01 KST)

Nothing here is installed. The pinned seat tool remains `r3c2_ledger_tools.py` (sha256 230359eb…); the seat packet, brief and
pin sheet are untouched; V23 is the signed design of record. Adopting any of this means: Duho's ruling → a version carrying it →
re-pin in `R3C2_SEAT_PACKET.sha256` → packet rebuild → C0 by two seats → two-seat gate → approval by the 11:11 procedure.

- `r3c2_ledger_tools_STAGED.py` — the seat tool plus (D1) the import evidence rule in `validate` and (D7) `audit seal-enumeration | select | compare`.
- `r3c2_batch_tools_STAGED.py` — lane-side `partition | seal | join | coverage` for the batch-reading candidate (`C1B_BATCH_COVERAGE`).
- `r3c2_staged_tests.py` — 44 controls: positives, negatives asserting the EXACT failure set, and 13 deletion probes (each load-bearing check is
  removed in a copy and the negative control must then PASS). Run from this directory: `/usr/bin/python3 -E r3c2_staged_tests.py` → `STAGED_TESTS=PASS`.
- `partition_12_of_89.{json,txt}` — the candidate partition of the real manifest (sha256 300d4da144d96ae9f1390c9018e919ae1ba6cf00be9f45ad36fdccfdcfbf9b24) into 12 batches, printed.
- `C6_COUNTEREXAMPLE_EXHIBIT.txt` — the emitted completeness results for the Codex counterexample (both seats omit a required passage), its reverse, and the 10% dispute rule.
- `R3C2_STAGED_D1D7.sha256` — pins of the three scripts, this README and the partition.

# Kun final GREEN and fixture-countersign brief

Packet: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-dr-c1r-chip-validator-repair-20260713T010203Z`
Role: independent custody/reproducibility gate. Do not trust Tori's self-reported success.

Read:
- `HWAO_IMPLEMENTATION_DIRECTION.md`
- `HWAO_GORU_FIXTURE_ADJUDICATION.md`
- `HWAO_T14_DEVIATION_ADJUDICATION.md`
- `design/LANA_T14_COUNTERSIGN.md`
- `fixtures/TORI_FIXTURE_SUPERSEDE_RECEIPT.md`
- `receipts/RED.md`
- `readjudication/READJUDICATION_SUMMARY.json`
- `readjudication/RESIDUE_REPORT.md`

Allowed writes only:
- `tests/run_all.sh`
- new files under `receipts/`
Do not edit capture, validator, fixtures, design, re-adjudication outputs, sealed packet, product code, git, dashboard, or any other path.

Tasks:

1. Fix `tests/run_all.sh` only as needed so it runs:
   - `/Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python -m pytest -q tests`
   - every `tests/test_*.js` and `tests/test_*.mjs` with Node
   - syntax/import checks for `capture/structured_capture_v2.js`, `capture/run_capture_v2.mjs`, `validator/validator_v2.py`, and `validator/run_validator_v2.py`.
2. Re-run the fixture generator twice. Do not leave generated temp files outside the packet. Verify the three generated output hashes remain exactly:
   - facts `1b812817fe0f02b576106fcb701a98ea0de7ea3e3c681e9d6fdea90b047a21a1`
   - corrupted HTML `05833834be7b2e54cc3a1aeafd33890e974e40f9e1ae080c95d6f2ebb84665d0`
   - corrupted manifest `76d7fb5f38064a5627381a7f8f97ed13b65172f86b380d363dee0a0afe365b55`
   Verify published facts: 108; 40/8/3/9/2/46; 46/37/0; S2 chips 27,28,10,11,15,20,30,30; four GAP units chip/token/chip/token; 12 orphan indices; 9 duplicate rows; 46 blank names; corrupted index 10 conflict.
3. Run the full test harness. Require every test GREEN. Confirm T14's countersigned amended residue: 17 FAIL findings = C2 sentinel 1 + C4 uncited result 8 + C6 unlabeled comparison 6 + C6 missing qualifier 1 + C7 integrity 1. Confirm artifact regressions absent.
4. Independently run capture and validator twice and require byte-identical outputs matching `readjudication/READJUDICATION_SUMMARY.json` hashes:
   - capture `e26819dbc90a040ecc228639fbee3e2a68f8942fa9d26b9458aee71bbc65e3e9`
   - validator `ad4d035b291f6d64ad47f510811cc05826d822f449cf3d181974be2ce2473d52`
5. Re-hash every sealed file listed in `receipts/KUN_PREFLIGHT.json` and require all hashes unchanged. Audit that task writes are confined to this repair packet. Do not interpret unrelated pre-existing repo changes as task writes.
6. Verify `RESIDUE_REPORT.md` says mechanical-only, no science/source-fidelity certification, no retro-acceptance, and FAIL_CLOSED preserved.

If any check fails, write one `receipts/KUN_GREEN_GATE_BLOCKED.md` with exact evidence and stop. Do not weaken tests or pins.

If all checks pass, write exactly:
- `receipts/KUN_FIXTURE_COUNTERSIGN.md`, ending `KUN_C1R_FIXTURE_COUNTERSIGN_GREEN_20260713T010203Z`
- `receipts/KUN_WRITE_SCOPE_AUDIT.md`, ending `KUN_C1R_WRITE_SCOPE_GREEN_20260713T010203Z`
- `receipts/KUN_GREEN_GATE.md`, ending `KUN_C1R_REPAIR_GREEN_GATE_20260713T010203Z`

Receipts must include commands, exit codes, hashes, test counts, and the 17-finding residue. No approval phrase, no live action.

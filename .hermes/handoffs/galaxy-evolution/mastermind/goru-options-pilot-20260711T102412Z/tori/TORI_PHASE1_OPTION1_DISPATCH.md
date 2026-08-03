# Tori Phase 1 dispatch — OPTION-1 only

Packet: `goru-options-pilot-20260711T102412Z`
Official class: `MOCK_ONLY`
Official verdict marker: `ADMISSIBILITY_VERDICT_20260711T104119Z`

Read and obey `DIRECTION.md`, `TEST_DESIGN.md`, `MANIFEST.json`, and the official admissibility ledger row.

## Authorized work

Implement and run OPTION-1 only:

- Create `goru/option1_shim.py` and any OPTION-1-only helper/test runner under `goru/`.
- Use Python 3.9 stdlib plus already-installed `requests` only. No install.
- The mock transport may listen only on `127.0.0.1` with an OS-assigned or explicitly local port.
- The shim must require an explicit base URL and reject/fail closed for every host other than literal loopback `127.0.0.1`.
- Only inert synthetic auth literal `DUMMY_1PSID_DO_NOT_USE` may appear. Do not read environment auth values, cookies, profiles, keychains, browser state, or credential files.
- No Google hostname, endpoint, RPC, wrapper import, browser, Playwright, Chrome, System Events, Accessibility, display action, external network, or subagent.
- Run T1 through T5 exactly as defined in `TEST_DESIGN.md`, sequentially, writing immutable results only under `tests/results/OPTION-1/T1/` through `T5/`.
- Do not modify `tests/gen_fixtures.py`, `tests/fixtures/`, `EXPECTED_VERDICTS.json`, or `targets.json`. Hash-check all pinned ground truth before and after.
- Each test-run must remain under five minutes; all OPTION-1 output must remain under 20 MB.
- Log mock bind address/port and record `127.0.0.1 loopback only; zero external network` in the receipt.
- Write `tests/results/OPTION-1/RECEIPT.md` with byte counts and SHA-256 for every output and implementation file used.
- Append one ledger row per T1–T5 plus the receipt row. Do not edit old rows.
- Reply with T1–T5 verdicts, receipt SHA-256, total bytes, and a standalone text marker `GORU_OPTION1_PHASE1_DONE_<UTC>Z`.

Do not begin OPTION-2 or OPTION-3. If any banned action, fixture mismatch, non-loopback URL, or ambiguity occurs, stop and report it without running further tests.

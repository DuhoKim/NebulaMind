# Tori final comparison handoff to Hwao

Packet: `goru-options-pilot-20260711T102412Z`
Status: all three sequential lanes adjudicated; ready for Hwao comparison/closure

## Required Hwao actions

1. Read `DIRECTION.md`, `DECISION_MATRIX.md`, `WAVE_LEDGER.md`, and the artifacts listed below.
2. Compile/update `DECISION_MATRIX.md` and create `COMPARISON.md` under this packet root.
3. Use the binding closed verdicts below; do not reinterpret FAIL as PASS.
4. Include the exact NON-EQUIVALENCE block from `DIRECTION.md` §6 verbatim in both outputs.
5. Append the final comparison/decision rows to `WAVE_LEDGER.md` with artifact hashes.
6. If packet integrity is intact, create exactly one zero-byte `PILOT_TESTS_COMPLETE_<UTC>Z` marker. Do not create an eligibility/live marker.
7. Duho asked Goru whether the dashboard was updated. The WAVE_LEDGER is not the public cockpit. Decide and report whether a separate cockpit/status update is appropriate; do not redesign or publish from this handoff without the applicable gate.

## Option 1

- Surrogate class: `MOCK_ONLY`
- Live class: `INADMISSIBLE-LIVE`
- T1/T2/T3/T5: PASS
- T4: FAIL
- Receipt: `tests/results/OPTION-1/RECEIPT.md`
- Receipt SHA-256: `ff665b7ed50820dd67032307c822787aa918a6b937163b85dc944a78621a9370`
- Tori recheck: `tori/RECEIPT_RECHECK_OPTION-1.md`
- Tori recheck SHA-256: `a960395407c30a24a067c1924f51f2e983bc714ec137343d52a76a2fe35ec693`
- Final verdict: `REJECT_LIVE__SURROGATE_FAIL`
- Attempt note: first run was a logged harness defect; its partial tree remains preserved. Exactly one corrected rerun was used.

## Option 2

- Surrogate class: `PAPER_ONLY_NOW`
- Live class: `INADMISSIBLE-LIVE`
- T1–T5: NOT_RUN
- Analysis: `tori/PAPER_ANALYSIS_OPTION-2.md`
- Analysis SHA-256: `9174d32c6a237aec8ee1463f22aca797f2636827d5a590fca27a44ba2d30080c`
- Dispatch: `tori/TORI_PHASE1_OPTION2_DISPATCH.md`
- Dispatch SHA-256: `514aaa67f68aab679676eaeff59ddfa6f22973886a98775a46236597e6d94533`
- Final verdict: `REJECT_LIVE__SURROGATE_NOT_RUN`
- No Option-2 shim, runner, result directory, browser, profile, or network action exists.

## Option 3

- Surrogate class: `SURROGATE_TESTABLE`
- Live class: `SEPARATELY-GATED-LIVE`
- T1/T2/T3/T5: PASS
- T4: FAIL
- Receipt: `tests/results/OPTION-3/RECEIPT.md`
- Receipt SHA-256: `2923f8ac36120eda8311b32e3058b7c863e09693ccb16a447e080e1fe12185ee`
- Tori recheck: `tori/RECEIPT_RECHECK_OPTION-3.md`
- Tori recheck SHA-256: `af9d1162a183a34cba13bccc280dfd99c7c8a556720a572fc4173fb957fa3df4`
- Discovery: `goru/OPTION-3_DISCOVERY.md`
- Discovery SHA-256: `aac84ca74d97ecf46ba545d737ca0742163484ee74830807a55766839ff857bd`
- Final verdict: `NEEDS_REWORK`
- It is **not** eligible for a separately gated next step because the binding rule requires every executed test to pass.

## Shared T4 contradiction

Both executed options deterministically extracted the pinned `fx_complete_marker_dup.html` body as:

1. marker
2. `Section 2.`
3. marker

Thus marker count is 2 and the final nonblank line is the marker (`true`). The pinned `EXPECTED_VERDICTS.json` requires marker count 2 but `marker_is_final_nonblank_line=false`. This exact pinned fixture/expectation contradiction caused T4 FAIL for both Options 1 and 3. Neither pinned file was edited; no further rerun is authorized. Repair requires a new explicitly approved packet revision, not retrospective result mutation.

## Safety and publication status

- No Option 3 browser, network, Google/Gemini, System Events, Accessibility, display, install, or kext mechanism was invoked.
- No option authorizes live use.
- No Option 3 separately gated next step is authorized by this packet.
- No database, deploy/restart, git commit/push, public cockpit, or publication action is included in this handoff.

# Tori receipt recheck — OPTION-3

Packet: `goru-options-pilot-20260711T102412Z`
UTC: `2026-07-11T11:46:22Z`
Reviewer: Tori
Class: `SURROGATE_TESTABLE`
Live status: `SEPARATELY-GATED-LIVE`

## Receipt integrity

- Receipt: `tests/results/OPTION-3/RECEIPT.md`
- Receipt SHA-256: `2923f8ac36120eda8311b32e3058b7c863e09693ccb16a447e080e1fe12185ee`
- Receipt bytes: 12,544
- Listed entries: 51
- Missing, byte-mismatched, or hash-mismatched entries: 0
- Receipt claimed total: 24,320 bytes
- Independent sum of listed file sizes: 24,320 bytes
- `T5/summary.json` total: 24,320 bytes
- Bound: PASS, below 20 MB

## Independent T1–T5 recomputation

| Test | Verdict | Independent result |
|---|---|---|
| T1 | PASS | All 12 fixture states match; planned actions satisfy allowed/required sets. |
| T2 | PASS | Exact requested target echoed in 9/9 invocations. |
| T3 | PASS | Verification, billing, and login walls each produce the exact wall state and `["HARD_STOP"]`. |
| T4 | FAIL | Determinism and pairwise-distinct hashes pass, but the pinned duplicate-marker fixture ends with the marker while pinned expected data says it does not. |
| T5 | PASS | First start intent present; second start refused with `UNKNOWN` + `["HARD_STOP"]`; 15-second subprocess timeout; all test durations below 300 seconds; output bound passes. |

### Exact T4 mismatch

`fx_complete_marker_dup.html` contains two exact marker lines and its final nonblank line is the marker. Both independent runs produced SHA-256 `274cde84d3e2752b1226edcacdd34e88c42ccf0682c9d946ec610cda202ca7a7`, marker count `2`, and `final_line_is_marker=true`. Pinned `EXPECTED_VERDICTS.json` requires marker count `2` but `marker_is_final_nonblank_line=false`.

The failure is preserved. Neither pinned file was edited, and no rerun is authorized. This same pinned contradiction also caused Option 1's T4 failure.

## Code and custody checks

- All `MANIFEST.json` read-only fixture/generator pins still match.
- Approved Goru files are unchanged after execution:
  - `goru/option3_shim.py`: `a6cb3974aca64e9ff46e636bef486fbfa7e5c38bc53e3591820e55473b098027`
  - `goru/test_runner_option3.py`: `d4e642ad5afdf76f20c1494f90ea387de7f73022a177707c9d456343d07e01cb`
  - `goru/OPTION-3_DISCOVERY.md`: `aac84ca74d97ecf46ba545d737ca0742163484ee74830807a55766839ff857bd`
- Static review found no requests, socket, URL fetch, Playwright, Selenium, WebDriver, browser, AppleScript, System Events, or GUI/display execution path.
- Post-run process check found no Option-3 runner/shim, Playwright, Chrome for Testing, headless/remote-debug Chromium, AppleScript, or System Events process.
- Discovery mechanics remain documentation-only and explicitly `NOT_INVOKED`.

## Adjudication

Receipt status: `VALID`.

Option-3 executed result: `T1 PASS / T2 PASS / T3 PASS / T4 FAIL / T5 PASS`.

Because the binding closed verdict requires every executed test to pass before Option 3 can become eligible for a separately gated next step, this run does **not** authorize that next step. Recommended matrix status: `NEEDS_REWORK — pinned T4 fixture/expectation contradiction requires a new, explicitly approved packet revision; no live authorization`.

A local result tests only transport-free decision logic against synthetic fixtures. It is not a Gemini result, not evidence of GUI/display/Accessibility reliability, and not permission for any live use.

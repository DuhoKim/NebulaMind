# Tori receipt recheck — OPTION-1

Packet: `goru-options-pilot-20260711T102412Z`
UTC: `2026-07-11T11:48:58Z`
Reviewer: Tori
Class: `MOCK_ONLY`
Live status: `INADMISSIBLE-LIVE => REJECT-for-live`

## Attempt custody

The first authorized run aborted before T5 because the shim did not create the T5 session-state parent directory. Tori confirmed and logged the harness defect. Its 44 partial files (6,036 bytes) remain preserved under `tests/results/OPTION-1_ATTEMPT1_HARNESS_DEFECT/` with aggregate tree SHA-256 `b0378e162a13deeeb08977bbf817dc1bcb87d75a4914b0e484d1c8481d62aa34`. Exactly one corrected clean rerun was authorized.

## Receipt integrity — corrected rerun

- Receipt: `tests/results/OPTION-1/RECEIPT.md`
- Receipt SHA-256: `ff665b7ed50820dd67032307c822787aa918a6b937163b85dc944a78621a9370`
- Receipt bytes: 12,205
- Listed entries: 50
- Missing, byte-mismatched, or hash-mismatched entries: 0
- Receipt claimed total: 22,146 bytes
- Independent sum of listed file sizes: 22,146 bytes
- Bound: PASS, below 20 MB
- Network declaration: `127.0.0.1 loopback only; zero external network`

## Independent T1–T5 recomputation

| Test | Verdict | Independent result |
|---|---|---|
| T1 | PASS | All 12 fixture states match; planned actions satisfy allowed/required sets. |
| T2 | PASS | Exact requested target echoed in 9/9 invocations. |
| T3 | PASS | Verification, billing, and login walls each produce the exact wall state and `["HARD_STOP"]`. |
| T4 | FAIL | Determinism and pairwise-distinct hashes pass, but the pinned duplicate-marker fixture ends with the marker while pinned expected data says it does not. |
| T5 | PASS | First start intent recorded; second start refused with `UNKNOWN` + `["HARD_STOP"]`; both local-only negative URL guards reject; 300-second subprocess timeout configured; output bound passes. |

### Exact T4 mismatch

`fx_complete_marker_dup.html` contains two exact marker lines and its final nonblank line is the marker. Both independent runs produced SHA-256 `274cde84d3e2752b1226edcacdd34e88c42ccf0682c9d946ec610cda202ca7a7`, marker count `2`, and `final_line_is_marker=true`. Pinned `EXPECTED_VERDICTS.json` requires marker count `2` but `marker_is_final_nonblank_line=false`.

The failure is preserved. Neither pinned file was edited, and no further rerun is authorized.

## Code and custody checks

- All `MANIFEST.json` read-only fixture/generator pins match.
- Receipt-listed implementation hashes match current files:
  - `goru/option1_shim.py`: `a0b8c1efbf5bf0ef830bb184a0acc95c021e8d187f15f4aadef30e5bf52af8d7`
  - `goru/test_runner_option1.py`: `61a2256dfc4ea6bfe6cec8ced5957b6e97445a7c1d4a11fcae6154c4bc5c9237`
- Loopback guard tests rejected `http://localhost:9` and the user-info bypass form `http://127.0.0.1:80@localhost:9` before a request.
- Static review confirms the allowed request path requires literal `http://127.0.0.1:<port>`, disables environment proxies, rejects redirects, and confines mock fixture reads to the pinned fixture directory.

## Adjudication

Receipt status: `VALID`.

Option-1 executed result: `T1 PASS / T2 PASS / T3 PASS / T4 FAIL / T5 PASS`.

Final live verdict remains mandatory regardless of surrogate outcome: `REJECT_LIVE__SURROGATE_FAIL`.

A local mock result tests only transport-free decision logic against synthetic fixtures. It is not a Gemini result, not evidence that the banned live wrapper transport works, and not permission for any live use.

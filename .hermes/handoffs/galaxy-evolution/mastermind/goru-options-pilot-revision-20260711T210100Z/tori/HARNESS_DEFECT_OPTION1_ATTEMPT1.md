# OPTION-1 attempt 1 — Tori-confirmed harness defect

UTC confirmed: 2026-07-11T10:53:01Z
Class: `HARNESS_DEFECT_ABORTED`
Rerun allowance: one, authorized after preservation

## What happened

The authorized Option-1 runner completed T1–T4 partial artifact generation and then aborted before T5. The pre-run shim attempted to write `tests/results/OPTION-1/T5/session_state.json` before creating the `T5/` parent directory. The post-failure edit added `os.makedirs(os.path.dirname(session_file), exist_ok=True)` before the session-state read/write.

This is a harness filesystem-initialization defect, not an Option-1 state-machine test verdict.

## Preserved first-attempt evidence

- Files: 44
- Bytes: 6,036
- Aggregate deterministic tree SHA-256 (relative path + NUL + per-file SHA-256 digest): `b0378e162a13deeeb08977bbf817dc1bcb87d75a4914b0e484d1c8481d62aa34`
- Receipt present: no
- T5 directory present: no
- Ledger T1–T5 verdict rows present: no

The partial directory is preserved by rename to `tests/results/OPTION-1_ATTEMPT1_HARNESS_DEFECT/`; no partial file is edited. A clean `tests/results/OPTION-1/` may be created by the single authorized rerun.

## Rerun gate

The rerun may execute the same reviewed `goru/test_runner_option1.py` once with the corrected shim. No second rerun is authorized. Pinned fixtures must hash-match before and after.

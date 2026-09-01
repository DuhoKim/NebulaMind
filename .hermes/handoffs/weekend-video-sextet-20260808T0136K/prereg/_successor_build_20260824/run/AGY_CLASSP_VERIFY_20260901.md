# AGY Class-P Verification

## 1. SLOT_SCHEMA and Receipt Verification
Both `BS-4.json` and `BS-7p.json` carry exactly their `v9` `SLOT_SCHEMA` field sets.
However, if the parsed JSON dictionaries are passed directly to `v9.receipt()`, it results in a `TypeError: can't concat str to bytes` refusal because `v9.receipt()` strictly requires `bytes` values and does not internally encode strings. The check passes only if the values are manually encoded to `bytes` prior to the call.

## 2. BS-4 Verification
- `python3 ref/successor_ref_v9.py --fixtures` was run twice. The output is byte-deterministic across runs.
- **`anchor_digest`**: The `sha256` of the fresh output is exactly `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`, matching the candidate's `anchor_digest`.
- **BATTERY lines & verdicts**: The output contains:
  `BATTERY-SIGN: PASS A=-0.0408 -> INCONCLUSIVE (A_L=-0.04272)`
  `BATTERY-POS: PASS A=+0.0408 at powered N -> REPRODUCED-LONGO (A_L=0.04243, p=2.23e-21, floor=0.01431)`
  The candidate's `verdict` field is `"PASS"`. This does not match the actual verdicts (`INCONCLUSIVE` and `REPRODUCED-LONGO`) printed in those lines. Instead, `"PASS"` is a paraphrase or conflation of the test runner's test status prefix (`PASS`) or the final `ALL FIXTURES PASS` summary.
- **`sign_convention`**: The candidate's `sign_convention` is `"EAST-OF-NORTH:+0.0408"`. This is a paraphrase synthesizing the script's comment: `our East-of-North winding maps it to +0.0408`.

## 3. BS-7p Verification
- **`ref_code_sha256`**: Matches the on-disk `ref/successor_ref_v9.py` sha256 (`6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`).
- **`environment`**: Exactly matches the live, serialized output of `v9.environment_record()`.
- **`n_perm`**: The candidate value is `"100000"`, which correctly equals the frozen `N_PERM = 100_000` constant in `v9`.
- **`fixtures_sha256`**: Matches the byte-deterministic fresh fixtures output (`fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`).

## Findings Summary
1. `BS-4.json` `verdict`: `"PASS"` is a paraphrase/conflation of the test-runner prefix or summary, rather than quoting the actual experimental verdicts (`INCONCLUSIVE` / `REPRODUCED-LONGO`) present in the BATTERY lines.
2. `BS-4.json` `sign_convention`: `"EAST-OF-NORTH:+0.0408"` is a synthesized paraphrase of the source comment (`our East-of-North winding maps it to +0.0408`).
3. `TypeError` on `receipt()`: The candidate payloads are JSON strings, which cause a crash/refusal in `v9.receipt()` unless the caller manually encodes them to bytes, as `receipt()` strictly assumes byte values.

SEAT: AGY
VERSION: CLASSP-VERIFY-V1
VERDICT: DEFECTIVE
COUNT: 3
F-lines: 23, 24, 25

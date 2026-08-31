# Gain Mapping Flip Verification

## 1. Digest and Verified State
- Verified the SHA256 digest of `../ref/gain_mapping_a.py` exactly matches the literal `8bc693ffae7009e0967a0b433b9bc7787494da8742457ad381443d4b210b4aa1` added to the `MANIFEST`.
- Verified via Git history and `AGY_MAPPING_REVERIFY_20260831.md` that the file content corresponds precisely to the AGY-MAPA-V2-verified bytes. The file has not changed since the `SOUND` verdict and principal confirmation (`MAPPING_CONFIRMATION_RULING_20260831.md`).

## 2. Fixture Runs and R7 Logic
- Executed `replay_harness.py` and successfully passed all fixtures (7/7 green).
- The `replay_machinery_proof` cleanly survives the flip: the audit-hook census evaluates the third manifest name flawlessly, and the root re-verification loop successfully verifies all three loaded buffers.
- Verified the `R7` control does real work: it validates that the `ACTIVE` entry is read and hashed by `_read_and_verify`, correctly checks the digest against `MANIFEST[2][2]`, and effectively simulates a flipped-byte attack that is correctly caught with a `ReplayRefusal`. 

## 3. Replay Sweep Execution Path
- Verified `replay_sweep()` remains cleanly blocked. It refuses outright on the stated "run-time calibration artifacts" ground, opening no execution path to a real sweep without providing the required calibration data.

## 4. Diff Inspection
- Conducted a focused review of the flip diff (docstring updates, `MANIFEST` state and digest change, `replay_sweep` exception adjustment, and `R7` addition). No defects were introduced. The diff executes the precise observable re-pin exactly as designed.

SEAT: AGY
VERSION: RPH-FLIP-V1
VERDICT: SOUND
COUNT: 0
F-lines: NONE

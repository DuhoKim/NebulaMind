# STAGE-V2 VERIFY (AGY) — 2026-08-31

**Independent Adversarial Pass on codex's `bs2k_stage_v2.py`**

The script correctly implements the 2-way XOR key splitting, OS boundary modes (0700), and the exact rejection on drift or corrupted shares. However, it circumvents three critical frozen requirements through mocks and hardcoded constants.

### Findings

1. **Boundary Honesty Mocked (F1)**
   `bs2k_stage_v2.py` implements `direct_store_read` as a pure mock that unconditionally raises `Refusal(REFUSAL_DIRECT)` (line 185). It never attempts an actual raw POSIX filesystem read (`read_bytes()`). Consequently, `boundary_test.py` passes the raw read denial test for the wrong reason—it verifies the mock's behavior rather than proving the OS boundary actually blocks the read.
2. **Archive Identity Hand-Answered (F1)**
   The script hardcodes the predecessor archive identity as string constants (`PARENT_RECEIPT_SHA256`, `PARENT_PAYLOAD_SHA256`) at lines 45-46. It does not dynamically derive them from the frozen parent bytes or pins, directly violating the "never a hand answer" clause. The derivation logic only hashes a local file to compare against these hand-answered constants.
3. **X2 Tokens Hardcoded (F7)**
   The X2 token set (`X2_TOKENS`) is hardcoded as a python tuple in the script (line 47). The script hashes this internal constant rather than dynamically parsing and extracting the tokens from `run/OPERATION_SET_COMMIT_20260831.md` as required by the "X2 digest recomputes from run/..." clause.

SEAT: AGY
VERSION: STAGEV2-VERIFY-V1
VERDICT: DEFECTIVE
COUNT: 3
F-lines: F1, F7

ACCESS_SHA=a8277a193caffa826ac3a1c2884545f0112b64e7cd3f6a6556dcc996041e49ba
# AGY BS-3g Referee Report

## TASK A — CONFORMANCE
1. **Ruled parameters**: All derived parameters strictly parse the authoritative texts using `re.findall`. Specifically:
   - `n_draws = 99`, `seed = 20260830`, `generator = numpy-1.26.4-PCG64-default_rng` from `DRAW_MECHANICS_COMMIT_20260830.md`.
   - `n_steps = 50`, `j0 = 25`, `n_perm = 100,000` from V136 and mechanical rulings.
   - `Γ = 0.25` from `GAMMA_RATIFICATION_20260830.md`, deriving `Δγ = 0.01` and 51 points.
   - Conventions (`a₀ = cal["a_hat"]`, `c` mean, `[0.5 + 1e-9, 1.0]`) from `MAPPING_CONFIRMATION_RULING_20260831.md`.
2. **Twenty fields & digest**: `compute_fields()` executes the 20-field subset and explicitly checks `schema_entry_digest("BS-3g") != "eb8589f5f70656b16dc8ba16e7d78677a0ab0da7b92cb54eddd22fef14e20102"`. It uses `receipt_strict()`.
3. **Reading (i) implemented EXACTLY**: `_path_outcome` properly isolates and converts `P07` exceptions wrapping `v9.InconclusiveByCalibration` and `v9.InconclusiveByPower` into `"INCONCLUSIVE-BY-CALIBRATION"` and `"INCONCLUSIVE-BY-POWER"` cell tokens. Every other refusal code (P01, P02, P03, P04, P05, P06, P08, P09, and other P07s) correctly raises an exception and aborts receipt generation.
4. **Reduction**: `HELD` strictly requires every cell to equal its own draw's `j0 = 25` baseline cell. The `j0` column produces conclusive verdicts (never breaching the 0.85 floor). Only columns at `γ ∈ {-0.01, 0, 0.01}` hold; all other 48 columns trigger the calibration halt.
5. **Replay harness obligations**: The producer verifies `sys.flags.optimize != 0`, strictly enforces `v9.FixtureMask` type, runs `harness._census()` to validate no unauthorized objects are present, and checks object hashes post-execution.
6. **Determinism**: Execution is fully deterministic. Reruns produce identically matching hashes.

## TASK B — INDEPENDENCE
The independent verifier (`gates/verify_bs3g_receipt.py`) reconstructs the grid natively without importing producer code. It correctly refuses:
- Tampered token: It enforces strict evaluation of known numeric and inconclusive outcome tokens.
- Wrong `j0` column: Fails via `if ns % 2 or decstr(grid[j0]) != "0": raise VerificationRefusal("non-canonical baseline")`.
- Draw count 98: Evaluates `nd` statically via regex (`n_draws = 99`).
- Missing harness digest: Checks `replay_harness_sha256` explicitly against expected.

## TASK C — THE EVIDENCE ITSELF
The "48 of 51 columns inconclusive" outcome is an intrinsic mathematical property of the fixture's `a_hat` mapping under option A `a(c) = a₀ + γ(c - c̄)`, not a bug.
- Fixture `a_hat` = `0.88`
- Hand computation of `a_lb_b` given the fixture spread:
  - `γ = -0.01` -> `a_lb_b = 0.85339` (holds, > 0.85)
  - `γ = +0.01` -> `a_lb_b = 0.85348` (holds, > 0.85)
  - `γ = -0.02` -> `a_lb_b = 0.84679` (fails, < 0.85)
  - `γ = +0.02` -> `a_lb_b = 0.84696` (fails, < 0.85)
This matches the matrix exactly (first breaches at `j=23` (γ=-0.02) and `j=27` (γ=+0.02)). The 0.85 calibration floor is fundamentally incompatible with the ±0.25 sweep range.

## TASK D — TESTS
All claimed 55/55 checks legitimately pass.

## TASK E — BOUNDARIES
Zero pixels or real data were used. The `P0_PACKAGE_MANIFEST_20260831.txt` validates with exactly 30 entries, and `ref/gain_counterfactual_path.py` retains the exact digest `92cbbdf89bd2a494c9cfb9f19fb12a46cf59a16731246cea2e74c56d2454a9b7`.

SEAT: AGY
VERSION: BS3G-BUILD-REFEREE-V1
TOOLING_VERDICT: PINNABLE
RECEIPT_VERDICT: VALID-FAILED-RECORD
HELD_COLUMNS: -0.01, 0, 0.01
COUNT: 55/55

# BS-3g fixture build record — 2026-09-03

## Outcome

Steps A and B were built, but step C is **STOPPED AND BLOCKED**.  The first full producer
execution reached the first endpoint (`gamma = -0.25`) and the frozen counterfactual path refused
the confirmed per-bin calibration transform:

```text
gain_counterfactual_path.PathRefusal: [P07] the calibration the mapping returned is missing a key production reads: adjudicate_path refused: InconclusiveByCalibration: a_lb_b min 0.694958 < 0.85
```

V136 §11 requires every cell to carry one of the three numeric production-verdict tokens and says
that any refusal emits no receipt.  Consequently no `run/classp_candidates/BS-3g.json` was emitted,
the independent receipt verifier could not be run on a candidate, and two receipt digests do not
exist.  Treating P07 as `FAILED`, shrinking the grid, changing the fixture, or weakening the
calibration transform would alter frozen semantics and was not done.

## Built bytes and pins

| artifact | sha256 |
|---|---|
| `gates/bs3g_producer.py` | `73b088b594e8c1645df34731185c6c2ba8c3307619997ccbd1700cd30e401088` |
| `gates/verify_bs3g_receipt.py` | `6b63a98a0f0dd166337d03547d9cf52d0ee89a6345e2aeaf480901974fd9d94c` |
| `gates/replay_harness.py` | `b6a0592bf881ca9b8b65d1fd6e716e2e845dd47c0f5c763799a40dec9966e4ac` |
| `ref/gain_gradient_estimator.py` | `e227029713396a920f76d33eed2383339dd0e566e1cdbb6818092ec4403727fd` |
| `gates/verify_mu_gamma.py` | `e33d9275d80787437429af7aa5989f3b886a8d1a477eddd55459e2270e046d04` |
| `ref/gain_gradient_kernel.py` | `10dd6f62074f30a3d98ff3838c98463eb2574e99012b6db00d8454b1f25978ab` |
| `ref/gain_counterfactual_path.py` | `92cbbdf89bd2a494c9cfb9f19fb12a46cf59a16731246cea2e74c56d2454a9b7` |
| `ref/gain_mapping_a.py` | `8bc693ffae7009e0967a0b433b9bc7787494da8742457ad381443d4b210b4aa1` |
| `ref/DRAW_MECHANICS_COMMIT_20260830.md` | `32673bd05f988b757a51eb445ae10d5e6a0dbe3d3a7593459db295917192790f` |
| `ref/MAPPING_CONVENTION_COMMIT_20260831.md` | `ff7b2cdb0441702ae471530b794ec43b62d0f9c07e776e308a26a76984fe0ebc` |
| `GAMMA_RATIFICATION_20260830.md` | `bf367191eda9d2762e2d78eac5257c390e61c3642776ba733f4f84eaa7f263a4` |
| `run/receipt_strict.py` | `c3cea71615c33ea57780872e47619b6763dad4b6aa2fb6787203dda9ec6d074c` |
| `SLOT_SCHEMA_SUCCESSOR['BS-3g']` entry | `eb8589f5f70656b16dc8ba16e7d78677a0ab0da7b92cb54eddd22fef14e20102` |

The producer owns the matrix and reduction; Mapping A remains one-draw-only.  Both new programs
derive the ruling values independently, compile the pinned v9/path/mapping buffers with optimize
zero and pre-binding, require a type-exact fixture mask, journal the computation load census,
re-read roots after computation, call the pinned estimator and kernel, and bind the strict
twenty-field schema.  The verifier imports no producer code.

## Ruled values and source quotations

- `ref/DRAW_MECHANICS_COMMIT_20260830.md`: “`n_draws` | **99**”; “`draw_master_seed` |
  **20260830**”; “`draw_generator_id` | **`numpy-1.26.4-PCG64-default_rng`**”; “draw variates |
  **COMMON RANDOM**”.
- The same file, Amendment 1: “The rule is corrected to ZERO-BASED”.
- The same file, Amendment 2: “`n_steps` | **50** (EVEN)”; “`delta_gamma` (Δγ) |
  **DERIVED: 2Γ / n_steps**”; “`n_perturbations` | **n_steps + 1 = 51**”; “baseline index |
  **j₀ = n_steps/2 = 25**, with **γ_{j₀} = 0 exactly**”; and HELD iff every cell equals its own
  draw's baseline cell.
- `GAMMA_RATIFICATION_20260830.md`: “γ range approved as proposed, ±0.25 in 50 steps” and “That
  number is now ratified: **Γ = 0.25**.”
- `OPEN_QUESTION_T_COMPLETENESS.md`: “STATUS: RULED — option (b), ‘real gate’”.
- `OPEN_QUESTION_GAIN_SIGN_MAPPING.md`: “STATUS: RULED — option A ... with WORST CASE OVER DRAWS”.
- `MAPPING_CONFIRMATION_RULING_20260831.md`: “Confirmed as committed (Recommended)”, confirming
  `a₀ = cal["a_hat"]`, the mean of `mask.c`, clamp `[0.5 + 1e-9, 1.0]`, and the per-bin-means
  calibration transform with preserved margins.
- V136 §11: “PRODUCTION permutation contract — `n_perm = 100,000`”; row-major verdict tokens are
  newline-separated UTF-8 with no trailing separator; a refusal emits no receipt.

## Outputs

Derivation/compile check:

```text
producer: n_draws=99 seed=20260830 generator=numpy-1.26.4-PCG64-default_rng n_steps=50 Gamma=0.25 delta=0.01 points=51 j0=25 n_perm=100000
verifier: n_draws=99 seed=20260830 generator=numpy-1.26.4-PCG64-default_rng n_steps=50 Gamma=0.25 delta=0.01 points=51 j0=25 n_perm=100000
python compile: PASS
```

First full producer execution:

```text
Traceback (most recent call last):
  ...
successor_ref_v9.InconclusiveByCalibration: a_lb_b min 0.694958 < 0.85
  ...
gain_counterfactual_path.PathRefusal: [P07] the calibration the mapping returned is missing a key production reads: adjudicate_path refused: InconclusiveByCalibration: a_lb_b min 0.694958 < 0.85
exit: 1
candidate absent: PASS
```

Required supporting fixtures:

```text
replay harness fixtures: 7/7 green
HARNESS_EXIT=0
receipt_strict fixtures: 10/10 PASS
RECEIPT_STRICT_EXIT=0
gain-gradient estimator self-test
  OK   9 of 9 codes exercised by a control; [] declared unreachable by construction, not counted as covered
  self-test: 0 failure(s)
ESTIMATOR_EXIT=0
gain_mapping_a self-test: 9/9 green — MAPPING-A-CRN-PCG64-20260830-v1 (identity 450c6a6ed43fc090…)
MAPPING_EXIT=0
NO_CANDIDATE_EXIT=0
```

`receipt_strict`'s 10/10 includes `assert_entries_preserved()` and the V136-recorded successor
entries.  Producer run 2 and verifier execution were not attempted because repeating a deterministic
protocol refusal cannot lawfully create the missing candidate.

## What V137 must change after the block is ruled

No V137 text was written.  A future ruling must first decide how a frozen-fixture grid cell whose
confirmed calibration transform triggers the pre-Stage-C calibration halt is represented.  Only
after that ruling can V137 update §7's BS-3g status, §11's cell vocabulary/refusal interaction,
producer/verifier/candidate pins, generated counts, registry provenance, findings map, and the
fill/amendment/signing records.  V134/V135/V136 and all pinned files remain unchanged.

SEAT: CODEX
VERSION: BS3G-BUILD-V1
TESTS: 7/7
RECEIPT: NONE DETERMINISTIC: no
VERDICT_FIELD: UNAVAILABLE (P07; NO RECEIPT)

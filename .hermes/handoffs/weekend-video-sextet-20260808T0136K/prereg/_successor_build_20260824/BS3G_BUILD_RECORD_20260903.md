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

## Round 2 — adjudicated P07 cell handling

AGY's committed adjudication `84ed219bf` selects reading (i): a typed pre-statistic
inconclusive halt is one recordable matrix-cell outcome.  The implementation change is confined
to the unpinned producer and independent verifier.  Neither
`ref/gain_counterfactual_path.py` nor any other P0-signed byte was edited; the path remains
`92cbbdf89bd2a494c9cfb9f19fb12a46cf59a16731246cea2e74c56d2454a9b7`, exactly the digest in
`P0_PACKAGE_MANIFEST_20260831.txt`.

The producer and verifier now inspect the preserved exception context of a P07 `PathRefusal`.
P07 wrapping the type-exact `successor_ref_v9.InconclusiveByCalibration` records the exact token
`INCONCLUSIVE-BY-CALIBRATION` and continues.  The analogous type-exact P07 branch for
`InconclusiveByPower` records `INCONCLUSIVE-BY-POWER`; the present pinned `adjudicate_path()` can
raise calibration, not power, so that counterpart was not exercised.  Returned numeric-helper
tokens retain their three-token validation, but matrix cells are no longer restricted to those
three tokens.

The refusal codes actually present in `ref/gain_counterfactual_path.py` are P01 (no mapping), P02
(wrong sign-vector length), P03 (non-binary signs), P04 (non-finite signs), P05 (degenerate signs),
P06 (invalid gain grid), P07 (invalid/refused calibration), P08 (permutation record raised), and
P09 (decision helper raised).  Only the two type-exact P07 subcases above are cell outcomes.  Every
other P07 cause and every P01–P06/P08–P09 code remains a refusal and emits no receipt.  This follows
§5's partition: “A pinned, sealed or already-verified object ... is `VOID`”; “A quantity the run
computed from admissible inputs ... is `INCONCLUSIVE-BY-NUMERICAL-FAILURE` — or the more specific
inconclusive code that names it.”  Here the mapping-computed calibration reaches the more-specific
calibration code; malformed caller/path inputs remain outside that outcome conversion.

The strict BS3G-V1 schema has no fields for an inconclusive-cell count or first coordinate.  No
fields were added: its entry digest remains
`eb8589f5f70656b16dc8ba16e7d78677a0ab0da7b92cb54eddd22fef14e20102`.  Those diagnostics are
therefore recorded only here.

### Matrix result and design evidence

- Shape: 99 draws × 51 perturbations = 5,049 cells, row-major.
- `INCONCLUSIVE-BY-CALIBRATION`: 4,752/5,049 cells (99 cells in each of 48 columns).
- Admissible columns: j=24, 25, 26, respectively γ=−0.01, 0, +0.01.  Every other γ column is
  calibration-inconclusive; there are no power-inconclusive cells.
- First row-major inconclusive coordinate: (i, j) = (0, 0), γ=−0.25.
- Moving outward from baseline j0=25, the first breaches are j=23 at γ=−0.02 and j=27 at γ=+0.02.
- Minimum `a_lb_b`: `0.6949581589958159`, first attained at (i, j)=(0, 0), γ=−0.25.
- Baseline token: `INCONCLUSIVE`.  Because the extreme cells differ from their draw's j0 cell,
  the §11 all-cells-equal reduction is `invariance_outcome = FAILED`.

This is the design contradiction for the principal: the ratified ±0.25 range leaves only three
central grid columns above the fixed 0.85 calibration floor on the frozen fixture.

### Final bytes and receipts

| artifact | sha256 |
|---|---|
| `gates/bs3g_producer.py` | `618767cd41e5283bdf736e30249ce2f0bdb180b4f0257e58e690bea58d3a18e6` |
| `gates/verify_bs3g_receipt.py` | `09b0acaadca1d95c756ad974ed48de28a4a1bbbf5f5fb765e7d7f042ea87dd64` |
| `gates/replay_harness.py` | `b6a0592bf881ca9b8b65d1fd6e716e2e845dd47c0f5c763799a40dec9966e4ac` |
| `ref/gain_counterfactual_path.py` (P0-signed, untouched) | `92cbbdf89bd2a494c9cfb9f19fb12a46cf59a16731246cea2e74c56d2454a9b7` |
| `ref/gain_mapping_a.py` | `8bc693ffae7009e0967a0b433b9bc7787494da8742457ad381443d4b210b4aa1` |
| `ref/gain_gradient_estimator.py` | `e227029713396a920f76d33eed2383339dd0e566e1cdbb6818092ec4403727fd` |
| `ref/gain_gradient_kernel.py` | `10dd6f62074f30a3d98ff3838c98463eb2574e99012b6db00d8454b1f25978ab` |
| `gates/verify_mu_gamma.py` | `e33d9275d80787437429af7aa5989f3b886a8d1a477eddd55459e2270e046d04` |
| `run/receipt_strict.py` | `c3cea71615c33ea57780872e47619b6763dad4b6aa2fb6787203dda9ec6d074c` |
| `run/classp_candidates/BS-3g.json` | `a8277a193caffa826ac3a1c2884545f0112b64e7cd3f6a6556dcc996041e49ba` |

Fresh final-byte producer run 1:
`a8277a193caffa826ac3a1c2884545f0112b64e7cd3f6a6556dcc996041e49ba`.
Fresh final-byte producer run 2:
`a8277a193caffa826ac3a1c2884545f0112b64e7cd3f6a6556dcc996041e49ba`.
`cmp` passed, so the receipts are byte-identical.  The strict receipt carries body digest
`067a2fe56978f44478ecfc34ddca64b99682dc357e807800b6247c438355d52a` and envelope digest
`8c78236ba698c454004354c7df4c643b1031ff336135a4814ed167619e3bc0c3`.

Final validation output:

```text
BS-3g receipt verifier: 20/20 fields PASS; outcome FAILED
receipt_strict fixtures: 10/10 PASS
replay harness fixtures: 7/7 green
gain-gradient estimator self-test: 0 failure(s); 9 of 9 codes exercised
gain_mapping_a self-test: 9/9 green
```

The receipt-strict fixture run includes `assert_entries_preserved()` and confirms the unchanged
BS3G-V1 entry digest.  Aggregate reported checks are 55/55 (20 receipt fields, 10 strict fixtures,
7 harness fixtures, 9 estimator refusal codes, and 9 mapping fixtures).

### V137 carry-forward

V137 must carry reading (i) into §5/§11 explicitly: typed pre-statistic inconclusive tokens are
valid sweep-cell tokens; one token is digested per cell; HELD still requires equality with each
draw's own j0 cell; and all non-outcome `PathRefusal` branches still emit no receipt.  It must carry
the emitted FAILED candidate and its digest, the two unpinned gate hashes, the unchanged
counterfactual-path/P0 pin, the 4,752/5,049 diagnostic and first-breach coordinates, and route the
±0.25-versus-0.85 contradiction to the principal.  It must also update the BS-3g status, relevant
candidate/pin tables, generated counts, registry provenance, findings map, and fill/amendment/
signing records without changing the twenty-field BS3G-V1 schema.

SEAT: CODEX
VERSION: BS3G-BUILD-V2
TESTS: 55/55
RECEIPT: a8277a193caffa826 DETERMINISTIC: yes
INVARIANCE_OUTCOME: FAILED INCONCLUSIVE_CELLS: 4752/5049 MIN_A_LB: 0.6949581589958159

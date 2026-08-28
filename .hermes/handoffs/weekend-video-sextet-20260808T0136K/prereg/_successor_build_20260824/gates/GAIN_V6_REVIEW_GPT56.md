# GAIN CONTROL V6 SCOPED RE-REVIEW — GPT56

## Verdict

**CLEAR for the scoped repairs.** I did not re-derive or re-litigate the accepted v5 finding that production `p` is not a function of `|A|`; that issue remains parked on the human decision in `OPEN_QUESTION_T_COMPLETENESS.md`. The four other repairs named in the brief hold on the pinned bytes: all `numpy.linalg` calls are now caught under the result-or-refusal contract, `recipe_gamma()` now refuses the three exact attacks before bin averaging, the design now records nine codes/no exemptions/G09 and marks the p-gated half REFUTED and OPEN, and the transcription check now compares against the actual production decision helper rather than a second local restatement. All three required self-tests independently exited 0 with the requested totals.

## Exact subjects and digest comparisons

1. `../ref/gain_gradient_estimator.py`
   - supplied SHA-256: `e227029713396a920f76d33eed2383339dd0e566e1cdbb6818092ec4403727fd`
   - recomputed SHA-256: `e227029713396a920f76d33eed2383339dd0e566e1cdbb6818092ec4403727fd`
   - comparison: **MATCH**, exact 64-hex equality.

2. `verify_mu_gamma.py`
   - supplied SHA-256: `e33d9275d80787437429af7aa5989f3b886a8d1a477eddd55459e2270e046d04`
   - recomputed SHA-256: `e33d9275d80787437429af7aa5989f3b886a8d1a477eddd55459e2270e046d04`
   - comparison: **MATCH**, exact 64-hex equality.

3. `../ref/verdict_breakpoints.py`
   - supplied SHA-256: `712b535d43890f327a1da3c7de183cf1ef839ed3b17f86ba6c06b3411d67e707`
   - recomputed SHA-256: `712b535d43890f327a1da3c7de183cf1ef839ed3b17f86ba6c06b3411d67e707`
   - comparison: **MATCH**, exact 64-hex equality.

4. `GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`
   - supplied SHA-256: `1c3ced94086be0f1995a71435ee59dff8a0d84633c44593adcc73d6c434b1f20`
   - recomputed SHA-256: `1c3ced94086be0f1995a71435ee59dff8a0d84633c44593adcc73d6c434b1f20`
   - comparison: **MATCH**, exact 64-hex equality.

## Scoped repair findings

### 1. All `numpy.linalg` calls are now inside refusal handling — HELD

The two v5 escapes are closed: `eigvalsh(S)` is wrapped at estimator lines 113–117 and `matrix_rank(X)` at lines 130–134. The remaining calls (`cholesky`, two whitening `solve` calls, `eigvalsh(XtX)`, and two final `solve` calls) remain inside the existing lines 143–158 wrapper.

I injected `numpy.linalg.LinAlgError` independently at the first `eigvalsh`, `matrix_rank`, `cholesky`, `solve`, and the second `eigvalsh`. Every attack returned `result is None` with exact code set `{'G08'}`; no exception escaped. The shipped refusal controls retained their distinct expected codes, including G01 overflow, G03 rank failure, G04 conditioning, G05 near-coincident centres, G08 denormal covariance, and G09 physical-range refusal. Thus wrapping did not collapse the ordinary precondition refusals into G08.

### 2. `recipe_gamma()` now carries the applicable `simulate()` guards — HELD

`recipe_gamma()` checks finite `gamma_true`/`gbar`, constructs the full per-object accuracy field before binning, and refuses unless every value is in `(0.5, 1.0]`. This is the same applicable parameter-finiteness then full-field-domain order used by `simulate()`; the latter's `mu`/latent-probability guard has no analogue because `recipe_gamma()` has no `mu` input.

I reran all three exact attacks on the real retained `cos(theta)` fixture:

- `gamma=0.251, gbar=0.8` → refused, per-object accuracy `[0.799600, 1.000396]`;
- `gamma=0.30, gbar=0.8` → refused, per-object accuracy `[0.780000, 1.019995]`;
- `gamma=nan, gbar=0.8` → refused as `non-finite parameter`.

For each, `simulate()` also refused. The guard is duplicated rather than factored into a shared helper, so future drift remains mechanically possible, but the pinned implementations are semantically aligned and the v5 defect is closed.

### 3. The design's scoped stale-contract defects are repaired — HELD

The design now lists G01–G09, explicitly withdraws the G08 unreachability exemption, says 9 of 9 codes are exercised with nothing exempt, documents G09, and says every `numpy.linalg` call is inside refusal handling. These statements match the estimator and its executed controls.

Section 4 now explicitly says the p-gated half is **REFUTED and OPEN**, that `verdict_breakpoints.py` does not close T-completeness, and that the accepted p-to-|A| reduction is false. It therefore no longer presents the parked mechanism as freeze closure. The surviving amplitude-side discussion remains subordinate to that explicit open blocker. I found no scoped regression caused by these edits.

### 4. The transcription check is now real, not differently circular — HELD

The prior check compared `verdict_at()` with a second local `if/elif`. The repaired check instead calls `successor_ref_v9._decide_from()`, then feeds `rec['A_L']`, `rec['sigma_comb']`, `rec['sigma_ours_band']`, and `rec['evaluated_floor']` into the local transcription and compares against `rec['verdict']`.

This reaches the actual helper called by `run_production_verdict()` after the production permutation record (`successor_ref_v9.py:1618–1622`). The fixture selects `SCALAR`, but that does not make the branch comparison vacuous: scalar/profile only derive `A`, `sig_band`, and `floor` differently; both paths converge on the same production decision branch at lines 1579–1584, and the test takes those derived values back out of the production record rather than synthesising them locally. The stub mask supplies only receipt fields on the selected scalar path.

The shipped 48-point check passed. As an additional attack, I compared the two functions over 10,000 deterministic random `(A,p)` points through `_decide_from()` and observed zero mismatches while exercising all three verdicts: 645 `REPRODUCED-LONGO`, 409 `REJECTED-AT-LONGO-AMPLITUDE`, and 8,946 `INCONCLUSIVE`. This confirms the repair is genuinely production-anchored. It does not validate the parked p-to-|A| model, and I do not credit it as doing so.

## Required self-tests run independently

1. `python3 ../ref/gain_gradient_estimator.py --self-test`
   - exit 0;
   - five noiseless recovery fixtures passed;
   - old-normalisation regression controls passed;
   - exact refusal controls passed;
   - `9 of 9 codes exercised`;
   - `0 failure(s)`.
   - Expected NumPy overflow warnings appeared only in deliberate numerical controls.

2. `python3 verify_mu_gamma.py`
   - exit 0;
   - `N = 49,211`;
   - ten in-domain cases passed;
   - five domain controls refused as required;
   - three end-to-end recipe fixtures passed;
   - `0 failure(s)`.

3. `python3 ../ref/verdict_breakpoints.py --self-test`
   - exit 0;
   - 48 production-helper transcription points passed;
   - breakpoint/invariance examples and T01/T02 controls passed;
   - `0 failure(s)`.

## Failed attacks and scope

- Injected failures into each distinct linalg stage; all became G08 refusals.
- Rechecked ordinary refusal controls for code drift; exact code sets held.
- Replayed the three named `recipe_gamma()` attacks; all refused before averaging.
- Compared `recipe_gamma()` and `simulate()` refusal outcomes for those attacks; aligned.
- Attacked transcription beyond the shipped grid with 10,000 points; zero mismatches and all verdict classes exercised.
- Checked that `_decide_from()` is the helper reached by the production runner, not an unused local analogue.
- Checked the design against the estimator's nine-code/no-exemption contract and the explicit REFUTED/OPEN status.

I deliberately did not read `/Users/duhokim/NebulaMindData/`, fill `gamma_hat`, fetch an image, revisit the accepted p-to-|A| refutation, decide the parked fork, or infer that the control is freezeable. **CLEAR here means only that the scoped repairs hold.** BS-6 and the first image byte remain blocked as stated in the brief.

**CLEAR**
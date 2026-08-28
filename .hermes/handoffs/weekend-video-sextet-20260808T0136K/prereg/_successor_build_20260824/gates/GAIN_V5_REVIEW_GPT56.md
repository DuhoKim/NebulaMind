# GAIN CONTROL V5 RE-REVIEW — GPT56

## Verdict

**NOT CLEAR. Remaining defects block FREEZING, not merely FILLING.** The v4 estimator and verifier failures named in the brief are substantially repaired and their shipped tests pass, but the new `verdict_breakpoints.py` does not close T-completeness. Its central reduction of production `p` to a function of `|A|` is false for the actual permutation statistic, and the module takes an externally supplied `p_of_A` rather than deriving one from production. Even its stated monotonicity assumption is only sampled, allowing an omitted interior p-gate crossing and a false invariance result. Separately, the digest-bound design subject is still the old text: it still declares G08 unreachable, lists only eight codes, and leaves `T` to a future receipt. `gamma_hat` remaining unmeasured would block only FILLING after these freeze defects are repaired.

## Exact subjects and digest comparisons

1. `../ref/gain_gradient_estimator.py`
   - supplied SHA-256: `af67230a310d3026378984f234c844dabed9fd38e9f950437572f091d6a15f1f`
   - recomputed SHA-256: `af67230a310d3026378984f234c844dabed9fd38e9f950437572f091d6a15f1f`
   - comparison: **MATCH**, exact 64-hex equality.

2. `verify_mu_gamma.py`
   - supplied SHA-256: `d91fb2b2a894a8651c16a0380eeaeb8e56ba9efa62949255b9a2981da7917cbb`
   - recomputed SHA-256: `d91fb2b2a894a8651c16a0380eeaeb8e56ba9efa62949255b9a2981da7917cbb`
   - comparison: **MATCH**, exact 64-hex equality.

3. `../ref/verdict_breakpoints.py` (NEW)
   - supplied SHA-256: `8f81eef77ea195f9404530f2b798e15a935b9af64ad58c17da8a07da290e676e`
   - recomputed SHA-256: `8f81eef77ea195f9404530f2b798e15a935b9af64ad58c17da8a07da290e676e`
   - comparison: **MATCH**, exact 64-hex equality.

4. `GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`
   - supplied SHA-256: `47b4ce87bc89d919200081ec0c3d9148cc09000aba8464946dccea394ecc45f6`
   - recomputed SHA-256: `47b4ce87bc89d919200081ec0c3d9148cc09000aba8464946dccea394ecc45f6`
   - comparison: **MATCH**, exact 64-hex equality.

## Numbered findings

### 1. HIGH / BLOCKING FREEZE — `verdict_breakpoints.py:19-28,38-40,95-154` — production `p` is not a single-valued function of `A`

The argument to attack was that `p` is a monotone function of the same statistic against a null that the gain gradient does not move. The production bytes contradict both premises.

Production computes `A = beta / w` (`successor_ref_v9.py:1566-1575`) but computes `p` by permuting the accepted-sign vector (`1138-1155`). The permutation null is not geometry-only: `perm_sigma_exact()` explicitly uses the variance of `s` (`1127-1135`), and the exact permutation distribution likewise depends on the accepted-sign multiset. A gain gradient acts on accepted signs, so it can move that multiset and its null. Further, `w` comes from calibration; the map from raw `beta` to corrected `A` is not the p-value map.

I independently constructed a physical-range geometry `c=[-1,-0.5,0,0.5,1]` and exhaustively enumerated the exact permutation distributions for two accepted-sign vectors. Both have the same raw slope `beta=-0.8`, hence the same `A` for any fixed `w`, but:

- `s=[1,-1,-1,-1,-1]`: mean sign `-0.6`, exact one-sided permutation p `1.0`, `perm_sigma_exact=0.5656854249`;
- `s=[1,-1,1,-1,-1]`: mean sign `-0.2`, exact one-sided permutation p `0.9`, `perm_sigma_exact=0.6928203230`.

Thus `p(A)` is not single-valued even at fixed geometry and fixed calibration. Threshold values are irrelevant to this counterexample: it kills the claimed functional reduction itself. If the systematic interval is intended to vary corrected `A` while holding the observed production p fixed, then p contributes no A-breakpoints; if it is intended to recompute counterfactual p, a frozen joint counterfactual model for the sign vector, calibration, statistic, and permutation null is required. The new module supplies neither interpretation.

The implementation confirms the missing derivation: `breakpoints()` accepts an arbitrary external `p_of_A` callable. Nothing in the module constructs it from the sealed production sign vector or `perm_record()`. Its self-test uses synthetic exponentials. The “transcription” test compares `verdict_at()` to another local restatement of the same `if/elif`; it does not call the production decision helper. Therefore this is still a future-input seam, not a derivation of the complete production breakpoint set.

**Smallest sufficient repair:** freeze one explicit sensitivity semantics. Either (a) hold the observed production p fixed and derive completeness with p gates treated as fixed booleans, or (b) freeze an executable joint counterfactual path that maps each allowed gain perturbation through accepted signs/calibration and the production permutation record. Do not insert an assumed scalar `p_of_A` between production and the verdict.

### 2. HIGH / BLOCKING FREEZE — `verdict_breakpoints.py:116-133,136-154` — sampled monotonicity can miss exactly the interior p-boundary the rule is meant to catch

Even granting an externally supplied `p_of_A`, the claimed enforcement is not exact. `breakpoints()` checks only 401 samples, while `_p_gate_crossings()` assumes global monotonicity and returns at most one crossing per gate. A narrow non-monotone region between samples is accepted.

I supplied a callable equal to `p=0.01` except for a narrow dip to `0.0005` around `A=0.0400025`. On interval `[0.039,0.041]`, with `sigma_comb=0.004`, `sig_band=0.003`, and `floor=0.010`, the code returned:

`reported True; T=[]; verdicts=['INCONCLUSIVE']; n_probes=2`

But direct evaluation gave:

- `A=0.039`, `p=0.01` -> `INCONCLUSIVE`;
- `A=0.0400025`, `p=0.0005` -> `REPRODUCED-LONGO`;
- `A=0.041`, `p=0.01` -> `INCONCLUSIVE`.

This is the original endpoint-equality defect reproduced inside the proposed repair: the verifier reports invariance while the interior verdict differs. I also supplied a narrower upward bump between the 401 samples; T01 did not fire. A finite grid cannot prove a callable monotone or its crossing set complete.

**Smallest sufficient repair:** remove sampled proof of an arbitrary callable. Completeness must follow structurally from the frozen executable decision path and a p relation with a proved representation, or the rule must conservatively refuse whenever such a proof is unavailable.

### 3. HIGH / BLOCKING FREEZE — digest-bound design lines 72-94 and 145-157 — the normative design still states the v4-defective contract

The design subject is byte-identical to v4. It still:

- lists only G01-G08;
- says G08 is “declared unreachable” and exempt from coverage (line 89);
- says the self-test fires every *reachable* refusal (lines 91-94);
- says `T` “must be enumerated in the receipt” and only requires a control with one threshold inside the interval (lines 145-157).

Those statements directly contradict the repaired estimator (G09 exists, G08 is reachable, 9/9 are controlled) and the new claim that breakpoints are derived. A freeze cannot bind mutually inconsistent code and design while leaving an operator to decide which is authoritative. The exact design digest requested here proves the stale text is part of the reviewed artifact, not a historical quote.

**Smallest sufficient repair:** update and digest-bind the design so it names the nine-code contract, withdraws the G08 exemption, and specifies the final, valid T-completeness semantics and executable trust root. Then re-review the resulting exact bytes.

### 4. MEDIUM / CONTRACT MISMATCH — `gain_gradient_estimator.py:113,126-127,134-149` — not every `numpy.linalg` call is wrapped

The repaired solver path catches `LinAlgError`, and the v4 near-coincident attack now refuses G05. However, the statement that every `numpy.linalg` call is wrapped is literally false: `np.linalg.eigvalsh(S)` at line 113 and both calls to `np.linalg.matrix_rank(X)` at lines 126-127 are outside the `try` beginning at line 134. I did not produce a deterministic failure for these finite 3x3/3x2 inputs, so this is not credited as a reproduced crash. It remains a contract mismatch in an API promising result-or-refusal totality and should be closed by moving all linalg calls under the refusal wrapper.

## Repairs that held / failed attacks

1. **Near-coincident bin-centre crash — repaired.** The shipped control refuses G05 rather than raising.
2. **G08 unreachability exemption — repaired in code.** The denormal covariance control reaches G08; computed coverage reports 9 of 9, with an empty exemption set.
3. **Post-scaling covariance finiteness — repaired.** The overflow control returns G01.
4. **Out-of-range `c_bar` — repaired.** It returns G09.
5. **Verifier NaN saturation — repaired for the dispatched scalar controls.** NaN `mu` and NaN `gamma` refuse before simulation.
6. **Normalization regression — held.** Five noiseless recovery fixtures and three old-normalization controls pass.
7. **End-to-end estimator recipe — held.** All three `gamma_true` fixtures pass.
8. **Shipped breakpoint examples — passed but did not survive adversarial callable tests.** The synthetic exponential examples exercise only the assumed one-dimensional monotone model.

## Executions

- `python3 ../ref/gain_gradient_estimator.py --self-test`: exit 0; five recovery fixtures OK; old-normalization controls OK; all refusal controls OK; `9 of 9 codes exercised`; `0 failure(s)`. Expected NumPy overflow warnings appeared in the deliberate denormal/overflow controls.
- `python3 verify_mu_gamma.py`: exit 0; `N=49,211`; ten in-domain cases OK; five domain controls refused; three recipe fixtures OK; `0 failure(s)`.
- `python3 ../ref/verdict_breakpoints.py --self-test`: exit 0; 48 local transcription points, shipped breakpoint/invariance examples, T01/T02 controls all reported OK; `0 failure(s)`.
- Independent exact-permutation enumeration produced the same-beta/different-p counterexample in Finding 1.
- Independent hidden-dip attack produced the false invariance result in Finding 2.

## Freeze versus fill ruling

Plain answer: **the remaining defects block FREEZING**. Findings 1 and 2 leave the p-gated verdict sensitivity incomplete and capable of a wrong invariance answer. Finding 3 independently leaves the digest-bound design contradictory and stale. The absence of a measured `gamma_hat` is separate: once the freeze defects are repaired, that absence blocks only **FILLING**. Nothing in this review fills `gamma_hat` or authorizes downstream image work.

## Scope and evidence ledger

I read the exact four subjects, my v4 report, and the relevant production implementations of the permutation statistic, p-value, calibrated amplitude, and verdict. I recomputed all four subject digests, ran all three shipped programs, and ran targeted independent permutation and breakpoint attacks. I did not read NebulaMindData, fetch images, fill any result, or modify any subject. The only intended write is this report.

**NOT CLEAR**
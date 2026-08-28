# GAIN v6 SCOPED REVIEW — CODEX

## Scoped verdict

**CLEAR for the repairs in scope.** All four supplied subject digests match. The two formerly unwrapped `numpy.linalg` calls now refuse as `G08`; all three exact `recipe_gamma()` attacks now return named refusals rather than a value or an escaped NumPy exception; the design now documents nine codes with no exemption and marks the p-gated reduction REFUTED/OPEN; and the transcription control now compares against the exact `_decide_from()` helper called by the production runner. All three mandated executions exited 0 with their stated counts.

This is deliberately **not** a finding on, or a clearance of, T-completeness. CODEX v5 finding 1 is accepted and parked in `OPEN_QUESTION_T_COMPLETENESS.md`; I did not re-derive it. Therefore CLEAR here means only that the other v5 repairs hold. The control remains DESIGN, defined, UNFILLED and is not freezeable unless the parked fork is resolved.

## 1. Digest comparisons

Recomputed from the gate directory with `shasum -a 256`:

1. `../ref/gain_gradient_estimator.py`
   - supplied: `e227029713396a920f76d33eed2383339dd0e566e1cdbb6818092ec4403727fd`
   - recomputed: `e227029713396a920f76d33eed2383339dd0e566e1cdbb6818092ec4403727fd`
   - comparison: **MATCH**
2. `verify_mu_gamma.py`
   - supplied: `e33d9275d80787437429af7aa5989f3b886a8d1a477eddd55459e2270e046d04`
   - recomputed: `e33d9275d80787437429af7aa5989f3b886a8d1a477eddd55459e2270e046d04`
   - comparison: **MATCH**
3. `../ref/verdict_breakpoints.py`
   - supplied: `712b535d43890f327a1da3c7de183cf1ef839ed3b17f86ba6c06b3411d67e707`
   - recomputed: `712b535d43890f327a1da3c7de183cf1ef839ed3b17f86ba6c06b3411d67e707`
   - comparison: **MATCH**
4. `GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`
   - supplied: `1c3ced94086be0f1995a71435ee59dff8a0d84633c44593adcc73d6c434b1f20`
   - recomputed: `1c3ced94086be0f1995a71435ee59dff8a0d84633c44593adcc73d6c434b1f20`
   - comparison: **MATCH**

For reproducibility of the transcription attack, the dynamically imported production source in this execution was `../ref/successor_ref_v9.py`, SHA-256 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` (recorded, not compared to a supplied v6 pin).

## 2. Repairs to the other v5 findings

### 2.1 Every `numpy.linalg` call is now refusal-wrapped — HOLDS

AST enumeration found eight calls in `gain_gradient_estimator.py`: `eigvalsh` at lines 114 and 148, `matrix_rank` at line 131, `cholesky` at line 144, and four `solve` calls at lines 145, 146, 154 and 155. The formerly exposed calls are now inside dedicated `try/except np.linalg.LinAlgError` blocks:

- forced `eigvalsh(S)` failure returned `result=None`, code set `{'G08'}`, reason `numerical linear algebra failed in eigvalsh: forced-eig`;
- forced `matrix_rank(X)` failure returned `result=None`, code set `{'G08'}`, reason `numerical linear algebra failed in matrix_rank: forced-rank`.

The official controls retained their exact refusal sets: G01 non-finite/overflow; G02 asymmetry; G03 non-positive-definite covariance; G04 covariance condition ceiling; G05 degenerate or numerically singular design; G06 unresolved intercept; G07 accuracy domain; G08 caught linalg failure; G09 physical centre range. Wrapping the two calls changes only an escaping `LinAlgError` into G08; I found no distinct pre-existing refusal path masked by the new handlers.

### 2.2 `recipe_gamma()` exact attacks — HOLDS

I ran the three CODEX v5 attacks against the real retained `c` loaded through the verifier's existing `load_cos_theta()` path:

- `gamma_true=0.251, gbar=0.8` returned `(None, 'REFUSED: per-object accuracy [0.799600, 1.000396] outside (0.5, 1.0]')`;
- `gamma_true=0.30, gbar=0.8` returned `(None, 'REFUSED: per-object accuracy [0.780000, 1.019995] outside (0.5, 1.0]')`;
- `gamma_true=nan, gbar=0.8` returned `(None, 'REFUSED: non-finite parameter')`.

No value and no raw `ValueError` escaped. The guard is in the correct function, before binning or averaging.

Advisory, not a scoped failure: `simulate()` and `recipe_gamma()` currently implement equivalent finiteness/per-object-accuracy rules as duplicated code rather than calling one shared helper. The present behavior agrees and the exact attacks hold, but a shared predicate would reduce future drift risk.

### 2.3 Design/code reconciliation — HOLDS

The design now:

- enumerates G01 through G09;
- says the G08 exemption is withdrawn;
- states 9 of 9 codes are controlled and nothing is exempt;
- states every `numpy.linalg` call is refusal-wrapped;
- marks §4's p-gated half explicitly **REFUTED and OPEN**;
- says `verdict_breakpoints.py` does not close T-completeness and limits the surviving claim to the amplitude-side breakpoints plus the production transcription check.

Those statements match the reviewed code. I found no surviving v4 text claiming G08 unreachable, only eight codes, or T-completeness closed.

### 2.4 Transcription check against `_decide_from()` — HOLDS

This is now a real cross-implementation check, not the v5 local-copy comparison:

- `verdict_breakpoints.verdict_at()` remains the independently written three-way predicate.
- The control calls `V9._decide_from(...)` and compares `mine` with `rec['verdict']`.
- It consumes `rec['A_L']`, `rec['sigma_comb']`, `rec['sigma_ours_band']`, and `rec['evaluated_floor']`; it does not locally reconstruct those production decision inputs.
- `successor_ref_v9.run_production_verdict()` calls that exact same `_decide_from()` helper at line 1621 after obtaining the production permutation record. Thus the reference side is the actual production decision branch, not a second restatement.

The built-in fixture selects the production-defined `SCALAR` calibration path and checks 48 `(A,p)` points. Independent recount of those 48 calls exercised all three verdicts: 38 `INCONCLUSIVE`, 8 `REJECTED-AT-LONGO-AMPLITUDE`, and 2 `REPRODUCED-LONGO`, with zero transcription mismatches. Its p grid includes values below, exactly at, and above both strict p thresholds (`0.001` and `0.05`).

The built-in stub mask is sufficient for the scalar branch because `_decide_from()` reads only `n` and `digest` from the mask on that path. It does not establish which calibration path future data will select. To attack that limitation, I separately constructed an admissible `V9.FixtureMask` and a calibration fixture that forces `PROFILE`, then ran the same 48-point comparison. It again exercised all three verdicts with counts 38/8/2 and zero mismatches. This confirms the local transcription also agrees after the other production-selectable transformation path. Since the final predicate is common below the SCALAR/PROFILE split and the comparison consumes the values returned by production, the original scalar fixture is not circular with respect to the branch it is meant to transcribe.

The check intentionally does not prove the parked p-to-A reduction, the completeness of T, upstream production authorization, or permutation construction. None is credited here.

## 3. Required executions

All commands were run unmodified except `PYTHONDONTWRITEBYTECODE=1` to keep the audit read-only outside this report.

1. `python3 ../ref/gain_gradient_estimator.py --self-test`
   - exit 0;
   - five recovery fixtures and three old-normalisation regression controls passed;
   - exact refusal controls passed;
   - **9 of 9 codes exercised**, `[]` unreachable;
   - **0 failures**.
   - Expected overflow warnings appeared in the denormal/overflow attack controls; no exception escaped.
2. `python3 verify_mu_gamma.py`
   - exit 0;
   - **10 in-domain cases**;
   - **5 domain controls**;
   - three end-to-end recipe cases passed;
   - **0 failures**.
3. `python3 ../ref/verdict_breakpoints.py --self-test`
   - exit 0;
   - production transcription matched on **48** points;
   - breakpoint/invariance/refusal controls passed;
   - **0 failures**.

## 4. Failed attacks / limits

Failed attacks that held:

- all four supplied pins matched;
- injected failures at each formerly exposed linalg site returned G08;
- all three exact `recipe_gamma()` attacks refused before averaging;
- scalar transcription covered all three verdicts and both exact p thresholds;
- forcing the alternate PROFILE path produced zero mismatches on the same 48-point grid;
- the design's code table and status language now agree with the reviewed implementation;
- all three official executions returned the required counts with zero failures.

Limits and deliberate exclusions:

- I did not re-derive or adjudicate the accepted/parked p-versus-`|A|` finding.
- I did not read `/Users/duhokim/NebulaMindData/`, fetch an image, form a science result, or fill `gamma_hat`.
- I did not claim that passing these scoped repairs freezes the control.
- I did not modify any reviewed subject. The only intended durable write is this report.

**CLEAR**

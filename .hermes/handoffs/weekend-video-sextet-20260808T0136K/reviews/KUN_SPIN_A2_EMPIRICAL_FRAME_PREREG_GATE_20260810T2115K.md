# KUN — Spin A2 Empirical Frame Pre-registration Gate

Filed: 2026-08-10 21:48 KST  
Lane: `spin`  
Scope: pre-computation gate only; no empirical frame correlation computed.

## Bytes Read

- Grant: `lanes/spin/SOURCE_FREEZE_AMENDMENT_A2_EMPIRICAL_FRAME_GRANTED_20260810T2115K.md`
  - SHA-256: `ebd0ef76484429294b61b92576ba64c89fb1d6859c8758bafe389ff75f333c04`
- Operative draft detail: `lanes/spin/SOURCE_FREEZE_AMENDMENT_EMPIRICAL_FRAME_DRAFT_20260810T2040K.md`
  - SHA-256: `754be165324ed6f5ad54d89d3bdee779b2a3b7f9b29df968e1449225d5476fbb`
- Existing mirror-bias output inspected for blind contamination only:
  - `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/spin-parity-census-20260805T1922K/T2_MIRROR_BIAS.json`
  - SHA-256: `113f4372507eb3c17c98b2c798d343b78fd4099a9861b52d8c24c71369690d1b`
- Existing mirror-bias script inspected for statistic identity only:
  - `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/spin-parity-census-20260805T1922K/t2_mirror_bias.py`
  - SHA-256: `625a242df93a6649921a9b1ac34da2cf898d677c7d4fae758a9683b06871f37b`

## Verdict

BLOCK. Do not run the empirical frame computation from this pre-registration.

This is not a rejection of A2. It is a gate failure on the current operative pre-registration. A2 explicitly allows a deliberately lowered evidence bar only if the pre-registration is frozen and independently gated before any number is seen. The current draft is not yet a frozen, executable contract.

## Blocking Defects

1. Numeric thresholds are not frozen.

The draft says: `Pre-registered rules (exact numbers to be frozen at gate; structure fixed here)`. That leaves the decisive values unavailable at the time I am asked to gate:

- minimum vote count in either leg
- matched-object floor after exclusions
- `ρ_min`
- `α`
- frozen fraction for the bias-confound same-sign magnitude test
- representativeness thresholds and covariates

A gate cannot supply or infer those numbers without becoming part of the design. If a later file freezes them, that later file must be separately hashed and gated before any computation. As written, this draft is loose enough for different later thresholds to make the same correlation pass or fail.

2. The bias-confound control is not specified.

The draft requires a bias-only control but gives alternatives: `e.g. the same per-object correlation computed where the frame prediction is null... or a permutation preserving the bias structure and scrambling the frame relation`. Those are materially different analyses. The exact null construction, randomization unit, seed policy, number of permutations if any, preserved margins, statistic, p-value definition, and same-sign comparison rule are not frozen.

This is the central confound. If it remains selectable after this gate, the result can be manufactured by choosing the control that does not reproduce the main sign.

3. The representativeness stop is qualitative.

The draft says the matched/full selection comparison must fail inconclusive if the missing subset is `non-random in a way that could flip the sign`. That is correct as a principle but not a gateable rule. It does not freeze:

- the exact handedness-relevant covariates
- the test statistics for each covariate
- adjustment for multiple comparisons, if any
- what effect size or p-value triggers INCONCLUSIVE
- how to decide whether a difference `could flip the sign`

This wording can be read either strictly or permissively after seeing a result, which is exactly the failure mode A2 is trying to prevent.

4. "Computed once" is not yet operationally enforced.

The draft says the correlation is computed once as a fresh, separately receipted run. It does not yet bind an execution receipt shape that prevents silent retries or alternate parameter files. A gateable contract needs at least the exact script path/hash to be run, immutable input list/hashes, output path policy, timestamp/receipt fields, and a rule that any failed/partial run is preserved and does not permit parameter revision.

## Blind Check

The existing `T2_MIRROR_BIAS.json` does not compute the proposed per-object correlation between `pcS1` and the normal-leg clockwise fraction. It reports aggregate dominance-ladder counts for normal, monochrome, and mirrored conditions, and it explicitly says it carries counts only and applies no reading.

However, it does reveal related aggregate signs on the same matched population:

- normal 0.80 rung: `N_CW=3481`, `N_ACW=3988`
- mirrored_1 0.80 rung: `N_CW=3659`, `N_ACW=3351`
- mirrored_2 0.80 rung: `N_CW=3603`, `N_ACW=3329`
- normal 0.60 rung: `N_CW=3997`, `N_ACW=4518`
- mirrored_1 0.60 rung: `N_CW=4273`, `N_ACW=3898`
- mirrored_2 0.60 rung: `N_CW=4283`, `N_ACW=3904`

That does not mathematically reveal the sign of the new per-object frame-discriminant correlation, so I do not mark the proposed test void on blind grounds alone. But the operator is not blind in the strong sense: the old output already shows aggregate mirrored-condition behavior and could shape expectations. This makes the frozen pre-registration more important, not less. With the current loose thresholds/control language, the contamination is unacceptable.

## Required Before Re-gate

A re-gate needs a single frozen pre-registration artifact, not prose saying values will be frozen later. It must include:

- exact threshold values for every stopping rule
- exact bias-confound control construction, including seed/repetition policy if randomized
- exact representativeness covariates and pass/fail criteria
- exact one-run execution receipt schema and immutable output policy
- exact script path/hash and input path/hash list, or a rule that the script is gated before run
- explicit decision table preserving `INCONCLUSIVE → FRAME_UNSTATED / Path C`
- explicit machine label requirement `frame_basis: "empirical_inference"` for any conclusive result
- explicit ban on `ESTABLISHMENT`, Land comparison, sky/dipole/parity/cosmological interpretation, and video/reportable unlock

Until then, uncertainty defaults to BLOCK and no empirical frame number should be computed.

BLOCK_PREREGISTRATION_GATE

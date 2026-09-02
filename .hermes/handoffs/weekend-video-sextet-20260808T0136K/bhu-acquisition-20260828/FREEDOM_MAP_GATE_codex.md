WRITEUP_REFUTED

# Hostile document gate: `PROGRAM_A_FREEDOM_MAP_20260902.md`

## 1. Fatal: the theorem-shaped quantitative bound is not licensed, and one of its numbers is false

Section 6 says that “every natural refinement tried” suppresses `S₁/₂` by **2.5–5×** and that no choice in the map reaches below about 6,100. The table itself contains `S₁/₂ = 6,113`, for which

`34,924 / 6,113 = 5.713`,

not at most 5. The stated range must be approximately **2.49–5.71×** if all rows in the table are included. The same mismatch infects the three-sentence headline (“between ~6,900 and ~14,000”, “2.5–5×”), because §4 and §6 themselves include 6,113.

More importantly, the 6,100 floor is only the minimum of a tiny enumerated test set, not a bound on the stated class of “natural completions.” `PROGRAM_A_PVALUE_RESULT_20260901.md` expressly retracts the earlier upper-bound/most-favourable claim: only three smoothing widths were tested, “nothing establishes an upper bound,” and “a different admissible spectrum could plausibly reach a higher p-value.” `CGATE_PROGRAM_A_PVALUE_codex.md` is even more direct: the smooth windows “do not span legitimate causal kernels or spectra engineered from a real-space boundary condition.” `AGATE_PROGRAM_A_STEP2_physics.md` exhibits the broader underconstrained class reaching toy `S_min` values far below 6,100 (down to about 4), although those values are not predictions of the paper either. Thus “no choice within this map” is a tautology about the displayed samples, not a theorem or a quantitative calibration no-go. The prose immediately strengthens it into “the amplitude is confined to a narrow band by any natural completion,” which the receipts explicitly deny.

Required repair: demote §6 to a report on the **specific finite implementations computed**, give the actual 2.49–5.71× numerical span, and delete all language implying completeness, a lower bound, or confinement of all natural completions. Without that repair, the central advertised result is refuted.

## 2. Fatal: a refuted observed-sky comparison survives both explicitly and implicitly

The headline says the computed band is “nowhere near the ~30× the observed sky shows.” Section 6 says the band “sits far above the observed value” and calls this “the only (full-sky) comparison this program is currently entitled to.” But §7 correctly says the opposite: the model numbers are full-sky spectrum statistics while ~1,150 is cut-sky and estimator-specific, so they are **not comparable** until the same mask and pseudo-`C_l` estimator are applied.

This is precisely refuted C2. `CGATE_PROGRAM_A_PVALUE_codex.md` says the mismatch is fatal and could overturn the claimed factor-six discrepancy. `PROGRAM_A_PVALUE_RESULT_20260901.md` records `C2_REFUTED` and says every constructive claim in that round fell. Calling the arithmetic “~30×” does not cure the estimator mismatch. Section 7’s not-claimed disclaimer is contradicted by the headline and §6; the document implicitly makes exactly the failure/overshoot claim it says it does not make.

Required repair: remove “nowhere near,” “far above,” “~30× the observed sky shows,” and any suggestion of an entitled observed comparison. The observed 1,150 may appear only as a clearly non-comparable orientation number pending phase (b).

## 3. Major: “admissibility ... is now a theorem” overstates what the displayed theorem proves

Section 5 cites

`P_B''(0) = -(4π/3) Cov_mu(r²,xi) > 0`

as establishing admissibility. That inequality proves only that the spectrum leaves zero upward locally. It does not by itself prove `P_B(k) >= 0` for every `k`. `POSITIVITY_third_VERDICT.md` does conclude positivity for the particular construction, but its scope statement is narrow: fixed support 14,015 Mpc, the stated overlap window and subtraction, a pure power-law `Delta²`, and regulator removed. Its global sign conclusion also rests on analytic/numerical transform work beyond the local second-derivative identity. `MONOPOLE_FIXED_codex_RESULT.md` supplies only a numerical grid minimum, not a general theorem.

The write-up further phrases the covariance result as holding “for any decreasing xi and any chi,” then leaps to global admissibility. That universal global conclusion is not supplied by the cited receipt. Required repair: say that the ruled seat established positivity for the **specific Reading-B construction and stated spectrum**, using the full adjudication; describe the covariance identity only as the small-`k` check.

## 4. Major: the smoothed spectra are mislabeled “A/B-compatible”

Sections 4 and 6 call the three smoothed Fourier cuts a “Reading-B-compatible family.” Paley–Wiener gives a necessary analytic property of the transform of a compactly supported correlation; merely smoothing an IR cut does not establish that its inverse transform has compact support at `chi_§`, nor that it realizes Reading B. The controlling receipt retracts the broad inference: `PROGRAM_A_PVALUE_RESULT_20260901.md` calls this only a family test and says a Reading-B spectrum need not be a smoothed ΛCDM spectrum at all; `CGATE_PROGRAM_A_PVALUE_codex.md` says the family does not span legitimate real-space causal kernels. Required repair: label these simply “three tested smooth Fourier windows,” with no A/B-compatibility claim absent an inverse-transform support proof.

## 5. Major: the Reading-B 8,777–10,132 “normalization freedom” is an externally imposed modeling spread, not a paper-defined residual choice

The numbers themselves match `MONOPOLE_FIXED_codex_RESULT.md` (8,776.675) and `MONOPOLE_NORM_RESIDUAL_codex.md` (10,132.383; +15.447%). But the source paper licenses neither Reading B nor the overlap window, monopole subtraction, homogeneous/isotropic scalar spectrum, standard ΛCDM transfer functions, nor the splice at `k=0.006/Mpc`. `AGATE_PROGRAM_A_STEP2_codex.md` lists these missing assumptions explicitly. Calling the splice “the program’s held-out constraint” and the difference a “freedom the paper does not fix” risks implying that the paper defines the construction except for normalization. It does not. Both endpoints are outputs of a stack of external choices.

Required repair: enumerate those assumptions beside the Reading-B result and describe 8,777–10,132 as sensitivity within one invented construction, not as the theory’s normalization band.

## 6. Moderate: “READING_C ... was returned ... by four seats” is literally inaccurate

The cited first tokens are not unanimous: `CGATE_PROGRAM_A_STEP2_textual.md`, `AGATE_PROGRAM_A_STEP2_codex.md`, and `KGATE_PROGRAM_A_STEP2_kimi.md` return `READING_C`, while `AGATE_PROGRAM_A_STEP2_physics.md` returns `CLASS_REFUTED`. The physics verdict is compatible with the broader conclusion that the class is unlicensed, but it did not return Reading C. Required repair: say that three seats returned Reading C and the physics seat independently refuted the proposed class.

## 7. Moderate: “two natural formalizations” and “freedom fully mapped” omit receipt-mandated alternatives and assumptions

`AGATE_PROGRAM_A_STEP2_codex.md` requires choices about stochastic state/covariance, homogeneity and isotropy, observer position, patch geometry and boundary/matching conditions, realizability/regularity, transfer functions, late-time parameters, and uncertainty in `chi_§`. The map varies only a cutoff convention, three arbitrary smoothing widths, one special overlap window, and one splice. It therefore cannot be described as fully mapping the freedom. Reading A and this one Reading-B construction are examples, not an exhaustive partition of causal completions.

## 8. Moderate: the high-ell and transfer-function caveat is missing from the advertised result

All quoted `S₁/₂` values use standard infinite-volume ΛCDM transfer physics with a modified primordial spectrum. `CGATE_PROGRAM_A_PVALUE_codex.md` warns that this tests “ΛCDM transfer physics plus an infrared spectral window,” not necessarily the paper’s causal-boundary model; a genuine boundary could alter modes, projection, or evolution. Section 7 disclaims ISW/lensing separation but does not disclose this larger structural assumption. This caveat belongs in the headline result and theorem discussion, not only in a receipt.

## 9. Minor numerical/wording issues

- Section 5 says the naive 252,066→900,646 sequence occurred “over three decades.” `READINGB_RECONCILIATION_20260902.md` labels the regulator range `10^-3 -> 10^-6 × k_§`, which is defensible as three orders of magnitude, but there are four regulator endpoints; wording should be “across a factor 1,000 in the regulator” to avoid ambiguity.
- Section 5’s “both seats independently” is too strong for the repaired construction. The 10,063 second-seat value was explicitly “not confirmed” by `MONOPOLE_FIXED_codex_RESULT.md`; agreement to 0.7% emerges only with the later no-splice 10,132 branch and does not independently validate the spliced 8,777 branch.
- Section 8 says the “surviving numbers passed blind double computation.” That is not true uniformly: 8,777 was a corrected single production result; the independent 10,063 initially disagreed by 12.8%, and only later matched a different no-splice treatment. State exactly which branch was independently corroborated.

## Bottom line

Many individual computations are accurately transcribed: 6,897; 14,000; 6,113–10,095 for the three tested smooth windows; 8,776.675; 10,132.383; the +15.447% splice sensitivity; and the corrected-window/convergence history. The source-level negative conclusion—that the paper supplies no sharp perturbation prescription—is also well supported. But the document turns a finite sensitivity study into an exhaustive narrow-band theorem, states a numerically wrong 5× ceiling, and revives the refuted observed-sky comparison. Those are load-bearing, not cosmetic, failures.

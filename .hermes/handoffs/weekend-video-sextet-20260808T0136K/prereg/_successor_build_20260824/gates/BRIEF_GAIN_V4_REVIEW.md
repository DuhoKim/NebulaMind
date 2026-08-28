# GAIN CONTROL v4 — the normalisation is fixed and the GLS contract is now code, not prose.

Subjects:

- **`GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`**, sha256 `47b4ce87bc89d919200081ec0c3d9148cc09000aba8464946dccea394ecc45f6`
- **`../ref/gain_gradient_estimator.py`** (NEW), sha256 `287ffe841400fff8462708bc6d423dbdf0ef62fc998f9a52cceaeb8ad488556e`
- **`verify_mu_gamma.py`**, sha256 `43243fe73769deee371ee7896e1f917fdb680dd92f0e9f7772047387f8d2efc5`

**Verify all three and state the comparisons.** The draft `../PREREG_SUCCESSOR_DRAFT_V33_20260828.md`
(`b247f402…`) is **unchanged and not the subject** — you both cleared it. Confirm it is
byte-identical and that nothing here is credited to it. **Write to `GAIN_V4_REVIEW_<YOURSEAT>.md`.**

## Your two findings were one seam, and one fix answers both

**GPT56-GAINV3-1:** the bias equation is derived for `g(c) = g₀(1 + γc)`, in which the regression
**intercept** is `g₀` and the slope is `g₀γ`. v3 divided the slope by the count-weighted sample
mean, which is `g₀(1 + γ·mean(c))` — so the statistic actually defined was `γ/(1 + γ·mean(c))`.
Your worked numbers reproduce here: `mean(c) = −0.158387518` to nine decimals, true `γ = +0.2`
reading as `+0.2065`.

**CODEX-GAINV3-1:** `n_b` was undefined between three live readings — population tertile counts, the
hand-check allocation (deliberately *not* proportional, v9:1378–1443), and the GLS's own implied
pivot.

**Fix: `γ̂ = θ₁/θ₀`, slope over the fitted INTERCEPT, both from the same GLS fit.** That is the
model's own parameter, so it matches the bias equation exactly — **and it removes `n_b` from the
statistic entirely**, so the weighting ambiguity dissolves rather than needing a fourth convention
pinned. **Check that claim: is there any residual dependence on a weighting choice?**

## The contract is code now

`gain_gradient_estimator.py` pins the design matrix including the intercept, a Cholesky solve rather
than an explicit inverse, eigenvalue rank and conditioning checks **before** any inverse, the
delta-method Jacobian `[−θ₁/θ₀², 1/θ₀]` written out, exact receipt fields, and eight refusal codes
under an exact-code-set battery.

- **A rank-deficient covariance is REFUSED (`G03`), not pseudo-inverted** — choosing a generalised
  inverse would itself be the unpinned freedom you objected to. **Is refusal the right call, or does
  it make the control unrunnable on a legitimate input?** Your own `agree=[100,100,100]`,
  `n=[100,100,100]`, `eps=0`, `sigma_eps=0` case is exactly what now refuses.
- **`G08` is declared unreachable and exempted from coverage BY NAME**, not quietly counted.
  **Verify it really is unreachable** after G01/G03/G05/G06.
- **A regression control** asserts the old sample-mean normalisation yields a different, *predicted*
  number, so the defect cannot return silently.

## The guard that could not fail — closed

GPT56: `verify_mu_gamma.py` "does not construct `γ̂` by §3's three-bin recipe." Correct, and that is
the shape this lane has caught repeatedly. **It now bins simulated data with v9's own
`calibration_bins()` and calls the same estimator production would**, end to end:

    gamma_true=+0.00 -> gamma_hat=+0.0447 +/- 0.0262
    gamma_true=+0.20 -> gamma_hat=+0.2326 +/- 0.0245
    gamma_true=-0.20 -> gamma_hat=-0.2287 +/- 0.0335

**GPT56-GAINV3-4 is also fixed**: the latent probability `(1 + μ + A·c)/2` could leave `[0,1]`. I had
guarded the accuracy domain and missed the neighbouring line. A third domain control now asserts the
refusal. **Try to make either script clamp rather than refuse.**

## Still open, and stated rather than hidden

`T`'s completeness (GPT56-GAINV3-3, CODEX-GAINV3-3) is **not** fixed in this round: the receipt
records `T` and its digest, but the completeness check is not yet code and the **p-gated boundaries
are unaddressed**. Judge whether that alone blocks freezing.

## Say plainly

**Does any remaining defect block FREEZING, or only FILLING?** `γ̂` is unmeasured; the control is
**DESIGN, defined, UNFILLED** and nothing may be filled against it. Run `--self-test` on the
estimator (expect 0 failures, 7 of 8 codes controlled, G08 exempted) and `verify_mu_gamma.py`
(expect 10 in-domain, 3 domain controls, 0 failures). **Do not take those from me.**

**BS-6 and the first image byte remain blocked.** §3 needs no images at all. Do not read
`/Users/duhokim/NebulaMindData/`. No deadline. Budget iterations so the report file is written.

## Verdict

Numbered findings with severity, file and line, why it fails, smallest sufficient repair. Anything
asserted but not executed under `Testimony`. Final line exactly `**CLEAR**` or `**NOT CLEAR**`.

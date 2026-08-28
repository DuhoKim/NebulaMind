# The sensitivity-gradient control — design v2, repaired against the round-1 referee findings

**Status: DESIGN, defined, UNFILLED.** `β` is unmeasured. Nothing here has produced a bound, and
nothing may be filled against it until it has.

**Principal's authorisation, 2026-08-28:** *"unrelated cutouts are fine, build the gain control."*
This authorises instrument characterisation on **non-sample** DR10 cutouts. **BS-6 and the first
image byte of this study's footprint remain blocked.**

**v1 was refereed by GPT56 and CODEX on 2026-08-28 and returned NOT CLEAR from both, with five
converged blocking findings.** This version answers each. What survived review unchanged: the
non-constructibility argument below, and the propagation-kernel arithmetic.

---

## 1. Why this is not the antisymmetry receipt — survived review, unchanged

From `paper/PAPER_DRAFT_SPIN_INSTRUMENT_20260812.md` §2.1: `mirror(·)` is pure index reversal
(`np.fliplr`, no resampling), `χ(x) = (w(x) − w(mirror(x)))/2`, so `χ(mirror(x)) = −χ(x)`
**algebraically, for any weights and any raster**. §2 receipts `max|χ(mirror(x)) + χ(x)| = 0.0`
exactly, 1000/1000 spirals.

So `d(g) = χ(g) + χ(Mg) ≡ 0`. **Stratifying it in `cos θ` returns 0.0 in every bin, forever.** It is
an identity, not a measurement.

CODEX verified this against the extant implementation, not only the paper: `chi_tensor` uses
`torch.flip(..., dims=[3])`, the cutout runner's mirror is `np.fliplr` — the interpolating mirror
that would break the identity by 0.058–0.944 is **not reachable inside the inspected χ path**. It
also noted the successor still requires BS-9 input-path rebinding, so this verifies the architecture
and the extant implementation, **not** a future production path.

**This corrects `MIRROR_TEST_DESIGN_20260828.md` Q2**, which proposed stratifying `⟨d⟩` in 8 bins.

## 2. What this control does and does not bound *(repairs GPT56-V32-3)*

§2.3 of the instrument description names three surviving routes:

| route | bounded here? |
|---|---|
| (a) chirality introduced upstream of the analysis raster | **no** |
| (b) global offset × sky gradient in sensitivity | **only the first-order linear part, see below** |
| (c) sample selection by a non-equivariant process | **no** |

v1 marked route (b) simply "yes". That exceeded the statistic and is withdrawn. **What is bounded is
the first-order linear response of recovered gain to the three authenticated quality variables**,
propagated through their measured coupling to the tested axis. **Explicitly NOT bounded:**
nonlinearity in that response, interactions between quality variables, dependence on any
position-coupled property outside the three, and any component reachable only through routes (a)
or (c).

## 3. The propagation kernel — vector, not scalar

v1 fitted one slope on `psfsize_r` and accepted with one kernel while injecting across two variables.
The three quality variables are correlated, so a univariate slope cannot stand in for them:

    correlation, retained sample      flux_ivar_r   psfsize_r     nobs_r
      flux_ivar_r                        +1.0000     -0.1257     +0.7176
      psfsize_r                          -0.1257     +1.0000     -0.1085
      nobs_r                             +0.7176     -0.1085     +1.0000

With `s_j` each quality variable normalised to zero mean and unit variance on the retained sample,
and a **vector** gain model `g/ḡ − 1 = Σ_j β_j s_j`:

    γ = βᵀK,     K_j ≡ Cov(s_j, cos θ) / Var(cos θ)

Computed with the frozen `AXIS` (`successor_ref_v9.py:100`) and v9's own `cos_theta()`, on the
49,211 retained objects — **no images required, so a referee can recompute all of it**:

    K[flux_ivar_r] = −0.270181
    K[psfsize_r  ] = +0.483014
    K[nobs_r     ] = −0.317419
    Var(cos θ)     =  0.751761

`Var(K̂)` is propagated from the WLS covariance of `β̂` as `Kᵀ Cov(β̂) K`.

## 4. The acceptance statistic — one path only *(repairs GPT56-V32-1, CODEX-V32-1/2)*

v1 named two incompatible observables: an inequality on a continuous slope, and a "decision reads the
two-hemisphere contrast" claim with no estimator, no uncertainty and no conversion between them.
**One is now the decision and the other is deleted from the decision path.**

**The acceptance statistic is `γ̂ = β̂ᵀK` and nothing else. The two-hemisphere contrast and the
8-bin profile are DIAGNOSTIC DISPLAYS ONLY** and enter no threshold.

Because "frozen bin labels" do not freeze the answer-determining freedoms, the sampling contract is
frozen here in full. All of it is fixed before any cutout is fetched:

1. **Backgrounds** — a pre-fetch manifest of non-sample DR10 cutouts (§6), frozen by digest **before
   any recovery is computed**, allocated to a fixed stratified grid over the three quality variables
   spanning the retained sample's support. Allocation counts per cell are in the manifest.
2. **Injections** — synthetic spirals on a frozen amplitude × morphology × orientation grid, both
   handedness signs at every grid point.
3. **Recovery, paired** — for each background *b* and injection *i*:
   `r(b,i) = χ(b ⊕ i) − χ(b)`. **The uninjected background is subtracted**, which cancels any
   background chirality; this is what licenses the blindness claim in §7 rather than an assertion
   about the sky being absent.
4. **Response** — `ĝ(b,i) = r(b,i) / A_inj`, and the fitted quantity is `ĝ/ḡ − 1`.
5. **Design matrix** — WLS of `ĝ/ḡ − 1` on `[1, s_flux, s_psf, s_nobs]`. **The intercept is fitted
   and discarded**; only the three slopes enter `γ̂`.
6. **Weights** — inverse recovery variance per cell, estimated from the within-cell replicate spread.
7. **Dependence unit** — the **background** is the clustering unit. `Cov(β̂)` is a
   cluster-robust (CR2) estimator over backgrounds, not the naive WLS covariance, because
   injections sharing a background are not independent.
8. **Support** — extrapolation is refused: if any retained-sample quality cell has no manifest
   coverage, the run emits `INCONCLUSIVE-BY-SUPPORT` rather than extrapolating.
9. **Receipt fields**, exactly: `manifest_sha256`, `n_backgrounds`, `n_injections`, per-cell counts,
   `beta_hat[3]`, `cov_beta[3][3]`, `K[3]`, `gamma_hat`, `sigma_gamma`, `mu_ceiling`, `mu_obs`,
   `bound`, `verdict`, and the diagnostic hemisphere and 8-bin arrays.

## 5. The decision rule *(repairs GPT56-V32-2, GPT56-V32-4, CODEX-V32-3)*

**The v1 claim that a systematic below `0.011` "cannot flip the verdict" is withdrawn. It was
false.** Any nonzero nuisance shift can change an outcome arbitrarily close to a decision boundary,
and `0.011` is about 27% of the tested `0.0408`. An external anchor is a policy tolerance, not an
invariance proof.

**Replaced by a rule that does not need that claim.** Define the signed systematic interval

    Γ = |μ_ceiling| · (|γ̂| + 1.96·σ_γ)          [absolute values throughout; K may be negative]

**The verdict must be invariant across the whole interval.** The preregistered decision function is
evaluated at every signed shift `δ ∈ {−Γ, +Γ}` applied to the estimated amplitude. If the study's
verdict — detection, rejection, sign, and band — is not identical at both endpoints, the run emits

    INCONCLUSIVE-BY-SENSITIVITY-GRADIENT

and **no dipole detection is reported.** No retry, no rebinning, no recalibration. This is a
terminated branch under §6.3 clause 10, and it makes the systematic's *consequence* the criterion
rather than its size against a borrowed number.

**`μ` is defined operationally**, which v1 did not do: `μ_obs` is the mean of the accepted-sign
`χ` output over exactly the accepted population the dipole estimator uses — same rows, same
acceptance, same phase. It is produced by an automated post-unblinding producer that writes an
authenticated receipt **before any result is displayed to any operator**, so no human chooses how to
recompute after seeing an outcome.

    μ_ceiling = max(0.10, |μ_obs|)

**`0.10` is an assumed pre-unblinding working ceiling, not an empirically generous one.** v1 called
it generous on the strength of two point comparisons; both reproduce — Land's superclean
`(Z,S)=(6106,7034)` gives `(S−Z)/(S+Z) = 0.070624`, and this lane's GZ1 paired-flip record gives
`0.094962 ± 0.024` — but `0.10` exceeds the latter by only 5.3%, its ~95% upper value is `0.142`,
and **both are human-label GZ1 statistics, one of them `FRAME_UNSTATED` and uncitable as a sky
quantity.** They do not bound this automated instrument's output monopole on this population. The
`max(...)` construction is what makes the rule safe, not the constant.

## 6. Provenance — non-sample means non-parent *(repairs CODEX-V32-4)*

v1 required exclusion from the **49,211 retained mask**. That was wrong: it permits any of the
15,849 catalogue-quality exclusions, which are study-parent objects.

**"Non-sample" is defined against the complete 65,060-object parent and the forbidden footprint.**
Every background must be proven outside both, by exact `(brickid, objid)` key comparison against the
frozen parent key set (`PARENT_KEYSET_SHA256 = 550e50a8…`) **and** by a spatial check against the
footprint. The manifest is frozen by digest **before any recovery is computed**, so backgrounds
cannot be chosen after inspecting recoveries.

## 7. Blindness, stated narrowly *(repairs GPT56-V32-5, CODEX-V32-4)*

**The v1 claim that "the real sky is simply absent" is withdrawn. It was false** — the inputs are
real DR10 backgrounds, with real structure, real observing conditions and real positions.

What is true, and sufficient:

- **No study-parent image and no study `χ` enters the statistic** (§6).
- **The injected amplitude and handedness are known**, so the signal being measured is synthetic.
- **The paired construction `χ(b ⊕ i) − χ(b)` cancels the background's own chirality**, so a real
  background galaxy cannot contribute to the recovered amplitude at first order.
- **The kernel is catalogue-only** — `K` uses metadata and the frozen axis, never an image.

That is outcome-blindness with respect to this study. It is not "no real sky", and this document no
longer claims a blindness property stronger than the mirror test's.

## 8. What remains open

- `β` is unmeasured. **DESIGN, defined, UNFILLED.**
- Routes (a) and (c) are unbounded by this control.
- Nonlinearity, interactions, and position-coupled properties outside the three quality variables
  are unbounded.
- **This does not close conditional independence.** It bounds one first-order route by which a
  violation could reach the estimator.
- `SLOT_SCHEMA` is frozen. Whether this receipt lives inside BS-3's `antisymmetry_receipt` or as a
  new field is a **gate matter, not an edit**; `successor_ref_v9.py` is not to be modified.

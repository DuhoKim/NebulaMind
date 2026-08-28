# Methods note — the Mittal–Singal Quaia-dipole disagreement is not attributable from the published record

**Assembled by Lana (science / claim-boundary seat), 2026-08-11 13:13 KST.** Per Duho: *"have lana assemble
it as a methods note."* Draft methods note; **not published, uploaded, or accepted — Duho decides after
reading.** Every factual claim is traced to a seat receipt (§Provenance). Kun gates this for overclaim; Tori
binds the sources. **We did not re-run either analysis and do not claim to.**

## Summary (the finding)
Two peer-reviewed analyses — **Mittal et al. 2024** (MNRAS **527**, 8497) and **Singal 2024** (MNRAS **532**,
L1) — measure the cosmic number-count dipole in **what is strongly supported to be the same Quaia v0.1.0
release** and reach conclusions that differ by a **factor of three to four** in amplitude (the direction is
undisputed in both). We find that this disagreement **cannot be attributed to any single analysis choice from
the published record.** The inputs are **strongly supported to be the same Quaia v0.1.0 release, but Mittal
does not self-bind exact input bytes, so a release mismatch is not *supported* as the explanation** (see §1 —
it is not byte-verified identical on Mittal's side); the principal method fork is openly stated; **but the
analyses couple their choices, leave order-unity corrections unstated, and estimate different quantities**, so
no one changed choice can be
isolated as *the* cause without re-deriving both pipelines under a single controlled convention — which is
**not available from the published record as-is** (§5). **This note reports only what can and cannot
be established from the published record; it adjudicates nothing and makes no cosmological claim.**

## 1. The inputs are strongly supported to be the same release — but not byte-verified on Mittal's side (Tori custody record)
What Tori's custody record actually established, stated exactly:
- **Singal 2024** self-binds the catalogue: **Quaia v0.1.0, DOI `10.5281/zenodo.8060755`**, and **states this
  is the release Mittal et al. used**.
- **Mittal 2024 self-binds no record** but **predates the public v1.0.0 release**.
- **Tori downloaded the v0.1.0 catalogues and selection maps; they match the published MD5 checksums and byte
  counts** — i.e. the v0.1.0 *products* are verified, and Singal's binding to them is verified.
- **What is NOT verified:** Mittal's *exact input bytes*. Mittal does not self-bind a record, so the identity
  of his inputs rests on Singal's statement and on Mittal predating v1.0.0, **not** on byte-level verification
  of Mittal's own data.
- **Therefore, precisely:** the two analyses are **strongly supported as the same Quaia v0.1.0 release, but
  Mittal does not self-bind exact input bytes; a release mismatch is not *supported* as the explanation** — it
  is neither byte-verified identical nor is a mismatch evidenced. This is a *strongly-supported*, not a
  *verified-identical*, claim, and the distinction is deliberate.
> *Factual base: Tori custody record. This note does not re-derive the checksums; it reports her result at her
> stated strength — supported, not byte-verified on Mittal's side.*

## 2. The principal method fork is openly stated, not hidden (Lana finding, primary sources verbatim)
The papers differ, first and explicitly, on **whether the Quaia selection function is applied**:
- **Mittal** writes the selection function into the likelihood — multiplicatively in the Poisson rate
  (`λᵢ·sᵢ`) and as a `1/sᵢ` scaling of pixel counts in the point-by-point construction.
- **Singal**, verbatim: *"We did not incorporate the selection function provided by [Storey-Fisher et al.].
  The reason being that their procedure seems to obliterate any dipole asymmetries across the sky,"* and
  *"the dipoles will get suppressed in this procedure and that might be the reason why results of Mittal et
  al. (2024) differ from ours."*
This fork is real and acknowledged by both sides. **It is the obvious candidate — but candidate is not cause
(§3).**

## 3. Why the factor of three cannot be attributed from the record (Kun result; Tori custody support)
The published record does not permit isolating the cause, for three compounding reasons:
1. **Coupled choices, never varied one-at-a-time.** Mittal's Galactic-plane masking (`|b|<40°` plus a `30∗`
   composite capping the central 4 sr) and selection-function scaling act **together**; the paper does not
   report the dipole with one changed and the other held fixed, so their individual contributions are not
   separable from the text.
2. **An unstated order-unity correction on the other side.** Singal's amplitude comes from a **direct count
   dipole** (vector sum + hemisphere `2(N₁−N₂)/(N₁+N₂)`) on a **cut sky**, which requires a **mask correction
   of order unity whose implementation is not stated** — so even his own number is not fully reconstructable
   from the paper.
3. **Different estimands.** Mittal reports a **Bayesian model comparison** (nested sampling, Bayes factors)
   over **masked, selection-treated HEALPix `Nside=64` pixel counts**; Singal reports a **direct count-dipole
   amplitude** on masked counts **without** selection treatment. These are **not the same quantity**, so a
   numerical ratio between them does not measure the effect of any one choice.
Some simple single-factor explanations are **not sufficient by themselves to explain the disagreement from the
published tables** — but this rules nothing out and promotes no factor: Singal reports `D≈3.3×10⁻²` under
Mittal's own `|b|<40°` mask and across magnitude cuts (`mG<20.5`, `mG<20.0`, `20<mG<20.5`) and latitudes
(`|b|>30°, 35°, 40°`), which *weakens* a pure magnitude- or latitude-cut explanation without excluding
estimator or masking effects, whose implementations differ and are not varied one-at-a-time.

**The kinematic-null constructions also differ (correction — Rev 1 was wrong here).** The two do **not** adopt
the same null:
- **Singal** uses the closed-form Ellis–Baldwin prediction `D=[2+x(1+α)]·β` with `x=1.3`, `α≈2.4` → prefactor
  ≈6.4, `v≈370 km s⁻¹`.
- **Mittal** does **not** use that closed form: he **forward-models Doppler boosting of the actual source
  counts** (`Sⱼ → Sⱼ·δ^{1+α}`) with a **per-source spectral index `αᵢ`** from Gaia colours, Monte-Carlo over
  the observed `α` distribution, at `v=369.82 km s⁻¹`. **With the published spectral-index correction in
  Mittal's current paper, the expected amplitudes are `D̄≈0.0048` (Quaia low) / `0.0043` (high)** (Tori
  custody receipt: the correction also increases prior sensitivity and makes amplitude consistency less
  decisive; **Singal uses the uncorrected input**). The original-analysis values `0.0080/0.0068` are
  **superseded by that published correction** and are quoted here only so the historical numbers carry their
  superseded label rather than circulating unlabelled.
The two null constructions are different, **and this note draws no inference — of attribution or exclusion —
from any numerical relation between their expected amplitudes**; doing so would repeat the error Rev 1 was
blocked for. The differing null constructions are one more reason the two numbers are not the same
estimand.

## 4. Corrections carried openly (not quietly fixed)
- **Lana (mine).** In my recoverability packet I identified the selection-function fork correctly but
  **overstated it as the entire, quantified cause** ("entirely the selection function," "decisively
  recoverable"). **Tori's custody assessment is right that this overstates the record:** the fork is the
  stated difference, but §3 shows the *magnitude* of its effect is not attributable from the papers, because
  Singal's side carries its own unstated O(1) correction and the estimands differ. The corrected finding is
  **non-attributability**, not "selection function explains the factor of three."
- **Hwao (coordinator).** The assessment artifact `HWAO_LOOSENED_BAR_MITTAL_SINGAL_ASSESSMENT_20260811T1110K.md`
  is **non-authoritative** and contains three errors that are **not** inherited here: it describes Mittal as
  using a Bayesian **spherical-harmonic** estimator (Mittal uses Bayesian model comparison over pixel counts,
  not spherical harmonics), states Singal's **magnitude cuts are unstated** (they are stated — see §3), and
  **omits Singal's 35° and 40° latitude cuts** (both included above). The factual base for this note is
  **Tori's custody record and Lana's primary read of the papers**, not that artifact.

## 5. What would settle it — and what that would require
The disagreement would be resolved only by **re-deriving both pipelines under one frozen convention** — a
single mask, one selection treatment, one estimator, one kinematic null — so that exactly one choice varies at
a time. That controlled re-derivation is **not available from the published record as-is**: neither paper
releases analysis code or exact mask memberships, and Singal's O(1) mask correction is not published to
reconstruct (Tori custody record). **A separate reconstruction scope would first need Tori to verify exact
recoverable artifacts, or record each missing implementation choice as an explicit replacement convention.**
This note does not attempt it.

## 6. Limitation and claim boundary (binding, unchanged)
- **We did not re-run either analysis.** No statistic here is ours; all measured values are quoted from the
  papers (Lana primary read) or from Tori's custody record of the public products.
- This note **does not adjudicate** the dispute, **does not endorse** either amplitude, and **states nothing**
  about whether the universe is anisotropic or isotropic, or whether the cosmological principle holds. **Neither
  paper's conclusion becomes ours to assert.** The permitted claim is exactly and only: *from the published
  record, the factor-of-three disagreement between two analyses of what is strongly supported to be the same
  Quaia v0.1.0 release (Mittal not byte-self-binding) cannot be attributed to any single isolated analysis
  choice, because the choices are coupled, an order-unity correction is unstated, and the two estimate
  different quantities.* That is the whole scope, and it is a genuine contribution to a contested literature.

## Provenance (every factual claim → seat receipt)
| Claim | Source / receipt |
|---|---|
| Singal self-binds Quaia v0.1.0 (DOI 10.5281/zenodo.8060755) and states it is Mittal's release; Mittal self-binds no record and predates public v1.0.0; the v0.1.0 products match published MD5 + byte counts; **Mittal's exact input bytes are NOT byte-verified** — "strongly supported same release," not "verified identical" | **Tori custody record** (reported at her stated strength) |
| Selection-function fork; Mittal `λᵢ·sᵢ`, `1/sᵢ`; Singal verbatim omission quotes | **Lana** read of Mittal 2024 / Singal 2024 (primary, verbatim) |
| Coupled masking+selection; unstated O(1) mask correction; different estimands (Bayesian model comparison vs direct count dipole) | **Kun** assessment, **Tori** custody support |
| Singal cuts (`mG<20.5/20.0/20<mG<20.5`; `|b|>30/35/40`); Mittal `Nside=64`, `|b|<40°`+`30∗` | **Tori** custody record + **Lana** primary read |
| Kinematic-null constructions **differ**: Singal closed-form `[2+x(1+α)]`, `x=1.3, α≈2.4`→≈6.4, `v≈370`; Mittal forward Doppler-boost of actual counts, per-source `αᵢ`, `v=369.82` | **Lana** primary read of Mittal 2024 / Singal 2024 |
| Corrected Mittal expected amplitudes `D̄≈0.0048/0.0043` (published spectral-index correction; original `0.0080/0.0068` superseded; Singal uses the uncorrected input) | **Tori** custody receipt `TORI_TO_HWAO_MITTAL_SINGAL_CUSTODY_ASSESSMENT_RECEIPT_20260811T1125K.md` (spectral-index-correction bullet) |
| Controlled re-derivation **not available from the published record as-is**; a reconstruction scope needs Tori-verified recoverable artifacts or recorded replacement conventions | **Kun** re-gate formulation + **Tori** custody record (code / mask memberships / O(1) correction omissions) |
| Hwao *assessment artifact* is non-authoritative + its three named errors — cited only to exclude it; **no factual claim in this note rests on it** | **Hwao** order `…LOOSENED_BAR…ORDER_20260811T1110K` (the order, not the artifact) |

# Design brief V2 — preregistered test of LONGO'S AMPLITUDE at Longo's axis
## narrowed per Duho: "narrow it to Longo's amplitude"

**Lana (science / claim-boundary seat), 2026-08-12.** Supersedes
`LANA_SPIN_DESIGN_BRIEF_20260812.md` (V1, preserved unchanged) for all design purposes. The narrowing
chain, closed end to end: Goru's exact power simulation
(`spike/GORU_STATS_RECOVERY_TEST_20260812.md`) showed V1's indicative N ≥ 30,000 gate delivers only
**8.0% power at A = 0.02 under p < 0.001**; Kun adopted **N ≥ 200,000 accepted** as the freeze condition
for the class-floor design (`spike/KUN_SPIKE_RECEIPTS_GATE_20260812.md`); Goru's feasibility chain
(`spike/GORU_SAMPLE_FEASIBILITY_20260812.md`) then established that **no currently public survey can
supply 200,000 accepted spirals** (DESI Legacy best case ~175k; Pan-STARRS clears 262k on paper but
Shamir's real run recovered ~33k). Duho resolved the impasse by narrowing rather than waiting for
Euclid DR1 / Rubin. Kun re-gates this brief. **Nothing is published, accepted, or run; Duho decides.**

---

## 0. THIS IS A DIFFERENT QUESTION — read this before assuming continuity with V1

V1 asked whether the **class** of published spin-anisotropy claims (amplitude floor A ≈ 0.02) survives a
bias-immune instrument. **V2 does not ask that question.** V2 tests **one specific published claim**:

> **Longo 2011 (Phys. Lett. B 699, 224): dipole asymmetry of |A| ≈ 0.0408 ± 0.011 at the axis
> (l, b) = (52°, 68.5°).**

Three consequences, stated in this brief's own voice so no reader has to infer them:

1. **The study tests Longo's claim, not the spin-anisotropy class.** A verdict here — either way — is a
   statement about the amplitude and axis Longo published, measured with an instrument designed not to
   create it. It is not a general isotropy test.
2. **A null at A ≈ 0.04 does not exclude A = 0.02.** With the narrowed sample gate (N = 100,000
   accepted; §7), a true-null measurement is expected to leave a 3σ upper limit of roughly
   **0.021 after attenuation correction** (indicative, a = 0.9; frozen number computed at prereg). So a
   REJECTED outcome here **rules out Longo's published amplitude at his axis; it leaves the smaller
   claimed amplitudes in this literature — including anything at or below ~0.02 — untested.** Anyone
   reading a null here as "the sky is isotropic" is over-reading it. The canonical boundary sentence,
   supplied by Kun's V2 gate and carried **verbatim** here and in §6, byte-identical on its own line:
> **"A null here does not establish that the sky is isotropic; it rejects only Longo's published amplitude at Longo's published axis if the preregistered rejection rule is met."**
   *(Correction carried openly, per `KUN_SPIN_V2_REGATE_20260812.md` §1: this clause originally claimed
   a verbatim repetition in §6 that was in fact equivalent wording — a custody error in exactly the
   boundary language that gets copied. Repaired by installing Kun's exact sentence in both places.)*
3. **The decision regions are re-derived for the narrowed target (§2), not carried over.** V1's
   REPRODUCED band [0.02, 0.08] was built for the class-floor question and is void here.

Shamir 2012's claim (P < 5.8×10⁻⁶, axis RA = 132°, Dec = 32°) is **demoted to a reported, non-decision
secondary** (§2): Duho narrowed to Longo's amplitude, and Shamir's implied amplitude class is not yet
custody-pinned **[VERIFY from Shamir 2012 full text before freeze — if it is materially below 0.04, this
design is underpowered for it and must say so rather than pretend to test it]**.

## 1. What carries over from V1 unchanged

- **The antisymmetry first principle** (V1 §0): χ(x) = (w(x) − w(mirror(x)))/2 obeys
  χ(mirror(x)) = −χ(x) for any w and any training; the sorter cannot manufacture a net asymmetry; the
  paired-flip statistic is zero by architecture; acceptance |χ| is mirror-invariant so confidence
  selection is bias-immune; biased calibration costs sensitivity, never validity — with the attenuation
  estimated from a hand-checked subsample (§7). Kun's leakage channels remain absorbed as **gain and
  selection modulation**, with the **monopole × sensitivity-gradient coupling** named and controlled
  (§5-C5).
- **The negative-control battery** (V1 §5, C1–C6), upgraded in §5 with the executable covariate battery.
- **The boundary**: a positive result would NOT identify BHU (V1 §6; Kun verbatim: a positive would be
  "a spin-anisotropy/statistical-isotropy result only"). Carried whole into §6.
- **The prior-art boundary** (Kun item 7): Shamir 2024 and Jia, Zhu & Pen 2023 own the components; our
  contribution is the combination plus preregistration and custody.

## 2. Preregistered hypothesis, statistic, and decision regions — re-derived for Longo's amplitude

**Freeze discipline unchanged:** everything here is sha-pinned before any sky statistic; one run; any
post-statistic parameter change voids the run.

- **Sign dictionary first:** Longo's sign convention at his axis re-derived from his methods at freeze —
  his −0.0408 is signed relative to his axis orientation, so REPRODUCED requires *his* sign at *his*
  orientation, worked from the paper, not from memory **[VERIFY at freeze]**.
- **Estimand:** D̂(n̂_L) = mean(sign(χᵢ)·cos θᵢ) at n̂_L = (l, b) = (52°, 68.5°); reconstructed amplitude
  Â = 3·D̂ (Goru: unbiased, recovered 0.0402 on injected 0.0400); attenuation-corrected
  Â_c = Â/(2a−1) with a from §7. **Monopole M̂ reported first**, always.
- **Null:** ≥ 10⁵ label permutations preserving positions and the accepted-sample footprint (Goru:
  correctly sized; KS uniformity p = 0.5003).
- **Primary decision regions (indicative numbers; each frozen numerically at prereg from final N and a):**
  - **REPRODUCED-LONGO:** permutation p < 0.001 at n̂_L, sign matches Longo's, and Â_c within
    **±3σ_comb of 0.0408**, where σ_comb = √(σ_pub² + σ_ours²), σ_pub = 0.011,
    σ_ours ≈ 3·√(1/3N)/(2a−1) (≈ 0.0069 at N = 10⁵, a = 0.9 → σ_comb ≈ 0.013, band ≈ [0.002, 0.080] —
    note the band's lower edge is dominated by *Longo's own* uncertainty; the p < 0.001 detection
    requirement is what does the excluding work at the low end).
  - **REJECTED-AT-LONGO-AMPLITUDE:** p > 0.05 (null-consistent) **and** corrected 3σ upper limit on
    |Â_c| **below 0.0408** (comfortably achievable at N = 10⁵: expected null UL ≈ 0.021). This verdict
    excludes *Longo's amplitude at Longo's axis* — nothing more (§0.2).
  - **INCONCLUSIVE:** anything else, reported as such; no rescue.
  - **INCONCLUSIVE-BY-POWER:** declared before unblinding if the §7 gate fails.
- **Secondary, non-decision:** (i) D̂ at Shamir's axis (RA 132°, Dec 32°), reported with interval, no
  decision region (see §0); (ii) one axis-marginalised free-axis scan, permutation-calibrated,
  multiplicity-corrected, reported after the primary and never able to rescue it (Kun item 6; his §2:
  drifting back to a free-axis hunt makes the design "weak immediately").

## 3. Instrument — updated for the yield arithmetic

The spike created a real tension V1 did not face: **Kun's item 1** (primary must not be human-label-
trained) meets **Goru's acceptance rates** — Ganalyzer-class deterministic acceptance ~14% yields only
**~49k accepted on DESI Legacy**, below the narrowed N = 100k gate; Yui's crude spike estimator abstained
~92%. Kun's rule itself provides the resolution: he permits *"a classifier trained without GZ1-style
human chirality labels."*

- **Primary instrument:** an equivariant (CE-ResNet-pattern) classifier **trained exclusively on
  synthetic spirals** — no human chirality label anywhere in training, so Kun's channels (1) and (3)
  have no human source to leak — wrapped in the enforced identity (which holds for any weights;
  §1). Target acceptance ~50% of face-on spirals (Goru's CE-ResNet figure) **[VERIFY in production —
  the §7 gate binds to the real rate]**. Synthetic training set generation (arm pitch, S/N, inclination,
  PSF ranges matched to the chosen survey) is frozen as part of the prereg.
- **Secondary instrument:** deterministic Ganalyzer-class geometric estimator, antisymmetrization-
  wrapped, run on the full sample; its accepted subset (~49k-scale) provides the training-free
  cross-check on the same objects. Disagreement rates published per object class.
- **Receipts (Kun item 3, and now his no-prose rule):** paired original/mirror outputs, mismatch rate,
  flip-balance, confidence and abstention deltas — published artifacts, not statements.
- **Sample selection:** unchanged from V1 — survey photometric cuts only, spirality gated by the
  mirror-invariant score s(x) = (u(x) + u(mirror(x)))/2, no human morphology flags, all cuts frozen.

## 4. Pixel-path custody — now carrying the spike's two hard rules verbatim

All of V1 §4 stands (single source/route/versions; raw-pixel measurement path; per-object WCS parity;
injected chiral test images; scrambled-WCS null). Added, as **frozen preregistration text**, Kun's two
hard rules from the spike:

1. **NO-RESAMPLING MIRROR (hard rule).** *"The mirror operation inside χ is pure pixel-index reversal on
   the final analysis raster. It is never an affine, WCS, interpolation, rotation, reprojection, or
   subpixel reflection transform. mirror(mirror(x)) == x must be byte-exact on the exact dtype passed
   to w."* Yui demonstrated an interpolating mirror violates the identity by **0.058–0.944** — against
   A ≈ 0.04 that is the size of the entire signal or larger. Corollaries frozen with it: no
   discretionary reprojection/rotation/resampling after the archive pixel product is selected; mirrored
   inputs are never created in sky coordinates by interpolation — index reversal on the analysis raster,
   sky parity accounted separately.
2. **SIGNED-ZERO RULE (hard rule).** *"All chirality decisions use value comparisons with |χ| > τ and
   ordered numeric comparisons. No code may branch on signbit, copysign, raw IEEE-754 bit patterns, or
   the sign of zero. Exact zero and sub-threshold values abstain."* Plus Kun's required unit test that
   fails if any classification function uses sign-bit semantics.
3. **Resampled-upstream policy (Kun's ruling, adopted):** a cutout service that has already resampled is
   **not automatically fatal** — but the delivered pixels plus WCS become the measurement input and must
   pass the parity/injection battery on their own terms. This is live: **DESI Legacy delivers generated
   TAN cutouts (Tori's audit)** — if Legacy is chosen, its TAN product is the measurement input, the
   injection tests run through the same service path, and no further resampling of any kind follows.
4. **Distortion policy (Kun item 7 of the spike gate):** fail closed on distortion keywords
   (SIP/PV/CPDIS/DET2IM) **or** implement a tested local Jacobian-sign calculation with injected-source
   receipts. **No silent fallback to a linear determinant on distorted WCS.** The choice between the two
   is made at survey binding and frozen.

## 5. The covariate battery — executable, per Kun's still-open blocker

Kun: *"The preregistration still needs executable definitions: covariate sources, maps, binning or model
form, matching/regression/adversarial test, leakage thresholds, multiple-testing handling, and exact
INCONCLUSIVE triggers."* This section is that specification. Where a covariate cannot be specified
executably from public data, it is dropped here with a statement — an unspecifiable covariate in a
frozen prereg is worse than an acknowledged gap.

**The covariate vector (per accepted object), sources named:**

| # | Covariate | Executable source | Form |
|---|---|---|---|
| 1 | Imaging depth | survey depth maps (Legacy DR10 `psfdepth_r` per brick / SDSS field limits) **[VERIFY exact product at survey binding]** | HEALPix Nside = 128 lookup |
| 2 | Seeing / PSF FWHM | survey per-brick/field PSF size (`psfsize_r` or equivalent) | same |
| 3 | Galactic extinction | SFD98 E(B−V) (public, definitive) | same |
| 4 | Stellar density | Gaia DR3 source-count map, mag < 19 | same |
| 5 | Crowding proxy | neighbour count within 30″ from the survey's own catalogue | per-object integer |
| 6 | Angular size | half-light radius from survey shape fits | per-object |
| 7 | Inclination proxy | axis ratio b/a from survey shape fits | per-object |
| 8 | Colour | g − r survey photometry | per-object |
| 9 | Magnitude | r-band | per-object |
| 10 | Arm-contrast | our mirror-invariant spirality score s(x) | per-object |
| — | Redshift | **dropped unless the bound survey ships public photo-z for the parent sample** (Legacy DR10 photo-z **[VERIFY]**); if absent, stated as a gap, not fudged | — |
| — | Deblend quality | survey deblend flags differ per survey; specified at binding from the named flag set, else **dropped with statement** | — |

**Layer A — stratified-permutation leakage test (per covariate, and jointly):**
For covariate C, bin accepted objects into deciles of C; generate the permutation null **within bins**
(signs shuffled only among objects in the same decile); recompute D̂(n̂_L). Leakage statistic
L_C = |D̂_raw-null-mean − D̂_C-stratified-null-mean| and the shift in p-value. **Frozen thresholds:**
L_C < 0.25·σ_D → pass; 0.25·σ_D ≤ L_C < 0.5·σ_D → flagged, enters the joint bound; **L_C ≥ 0.5·σ_D for
any covariate → the axis result is INCONCLUSIVE** (exact trigger, no discretion). Joint version: single
stratification on the first three principal components of the standardised covariate vector (deciles³
capped at occupancy ≥ 50, else coarsened by a frozen rule).

**Layer B — adversarial predictability test (object-level):**
(i) logistic regression of sign(χ) on the full covariate vector + squares; likelihood-ratio test vs
null. (ii) gradient-boosted trees (fixed hyperparameters, frozen seed, 5-fold CV) predicting sign(χ)
from covariates only; metric = out-of-fold AUC. **Frozen thresholds: AUC < 0.520 → pass;
0.520 ≤ AUC < 0.550 → flagged; AUC ≥ 0.550 → INCONCLUSIVE.** (Under the identity, covariates are
mirror-invariant and should carry zero information about sign; any predictability is leakage by
definition.)

**Layer C — abstention structure (feeds C5, not a veto by itself):**
The same Layer-B machinery predicting *abstention* instead of sign — this WILL show structure
(depth/seeing predict abstention; benign). Its output is the sensitivity map for the
**monopole-coupling bound**: coupling bound B = |M̂| · Dip(sensitivity map) + |M̂| · Dip(abstention map);
**frozen trigger: the axis result stands only if |D̂(n̂_L)| > 5·B; if B ≥ |D̂|/5 → INCONCLUSIVE at that
axis.**

**Multiple testing:** Layer A per-covariate tests corrected Holm–Bonferroni within the frozen family
(10 covariates + joint); Layer B is two tests, Holm-corrected. Flags do not accumulate into a veto —
only the exact triggers above do — but all flags are published.

**Mirror-pair accounting (Kun item 4's premise):** every Layer A/B statistic is computed on the
symmetrised accepted sample (object + mirror processed identically); any covariate correlation that
survives symmetrisation is by construction not a sorter artefact, which is what makes these tests
diagnostic of *selection and sky structure* rather than instrument chirality.

## 6. Boundary — what results mean, in plain words

- **A REPRODUCED-LONGO outcome would NOT identify BHU.** The BHU closing record stands; Kun's ruling is
  adopted verbatim: *"Any positive spin result … would be a spin-anisotropy/statistical-isotropy result
  only."* A positive first triggers an adversarial systematics re-audit inside the lane, before any
  claim, video, or upload exists.
- **A REJECTED-AT-LONGO-AMPLITUDE outcome rules out Longo's published amplitude at Longo's published
  axis, as measured by an instrument that cannot itself produce the sign.** It does **not** exclude
  A = 0.02; it does not adjudicate Shamir's claim; it does not establish that the sky is isotropic. The
  expected reach of a null here leaves everything below roughly **Â_c ≈ 0.021** (indicative, N = 10⁵,
  a = 0.9) alive. Canonical boundary sentence (byte-identical to §0):
> **"A null here does not establish that the sky is isotropic; it rejects only Longo's published amplitude at Longo's published axis if the preregistered rejection rule is met."**
  **The narrower question was chosen deliberately — power against one real published
  number, instead of impotence against a class** — and this boundary travels into any derived
  artifact, including any video.
- **INCONCLUSIVE outcomes are published as INCONCLUSIVE.** The battery's triggers (§5) are exact so that
  this word cannot be negotiated after the fact.

## 7. Attenuation and the power gate — narrowed numbers

- Hand-check protocol as V1 §7 (N ≈ 500, stratified, two checkers, randomised parity presentation,
  sealed key), now with Kun's freeze demand: exact strata, adjudication rule, uncertainty propagation
  into σ_ours and the §2 bands, all frozen numerically at prereg.
- **Power gate (frozen):** minimum **N ≥ 100,000 accepted** spirals after all cuts, abstentions, and
  mirror-pair exclusions. Goru's exact simulation: 100% power at A = 0.04, p < 0.001, N = 10⁵ (76% at
  N = 3×10⁴ — below requirement). **Caveat carried openly:** Goru's table is computed at label accuracy
  a = 1; the effective observed amplitude is (2a−1)·0.0408 ≈ 0.033 at a = 0.9, where interpolation of
  his table suggests power remains ≳ 99% at N = 10⁵ but **must be recomputed exactly with the measured
  a before freeze [VERIFY — one rerun of Goru's harness at A_eff]**. If the bound survey cannot deliver
  100k accepted with the production estimator's real acceptance rate, INCONCLUSIVE-BY-POWER is declared
  and the run does not start (kill switch).

## 8. Data — narrowed feasibility, choice still not frozen

Goru's chain, with CE-ResNet-class acceptance (~50%): **DESI Legacy ~175k accepted (headroom 1.75×);
SDSS ~130k-scale; HSC-SSP ~105k** — all three clear the narrowed 100k gate; **Pan-STARRS excluded**
(paper yield 262k, real-world precedent ~33k — seeing/noise destroys arm gradients); **Euclid Q1
excluded** (~11k). With the deterministic instrument as primary, *no survey clears the gate* — which is
why §3 assigns it the secondary role. Survey binding happens at prereg with Tori's custody file on the
chosen route (for Legacy: the TAN-cutout service becomes the measurement input per §4.3). V1 §8's six
minimum properties still score the choice; property 2 (footprint covering the Longo axis projection
range) now binds to n̂_L specifically.

## 9. Kill switches — V1's ten, plus the spike's

K-1…K-10 carry from V1 unchanged (with K-6's power gate now **N ≥ 100,000 accepted for the Longo
target**). Added:

- **K-11 (spike):** any mirror implementation that is not pure index reversal, or any
  mirror(mirror(x)) byte-inequality on the analysis dtype → halt. (Yui's 0.058–0.944 injection is the
  standing demonstration of why.)
- **K-12 (spike):** any code branching on sign-bit semantics → halt until removed; the failing unit
  test is part of the frozen suite.
- **K-13 (spike):** distortion keywords present with neither fail-closed rejection nor a tested local
  Jacobian receipt → halt. No silent linear-determinant fallback.
- **K-14 (V2):** if Shamir's implied amplitude class, once custody-pinned, is at or below ~0.02, no
  decision language about Shamir's claim may appear in any output of this study — reported interval
  only. (Prevents the narrowed design from quietly widening its own verdict.)

## 10. What this study is, in one sentence, for the record

**A preregistered, orientation-custodied, mirror-controlled measurement of whether Longo 2011's
published dipole amplitude at Longo's published axis survives an instrument that cannot have produced
it — with exact, executable leakage triggers, and with its non-verdicts (A ≤ 0.02, Shamir's claim, BHU,
global isotropy) stated in the artifact itself.**

---

**Open [VERIFY] register:** Longo sign convention (freeze-time, from methods); Shamir 2012 implied
amplitude class (decides K-14); production acceptance rates (primary and secondary instruments); Goru
power rerun at A_eff = (2a−1)·0.0408; Legacy DR10 depth/PSF/photo-z product names; deblend-flag sets per
survey; survey binding itself. **Frozen only at prereg, which is a separate sha-pinned artifact after
Kun gates this brief.** Nothing is published, accepted, or run; Duho decides.

— Lana, 2026-08-12. V1 preserved unchanged at `LANA_SPIN_DESIGN_BRIEF_20260812.md`.

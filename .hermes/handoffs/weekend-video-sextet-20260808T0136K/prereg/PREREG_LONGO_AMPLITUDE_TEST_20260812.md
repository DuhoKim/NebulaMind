# PREREGISTRATION (DRAFT FOR GATE) — LONGO-AMPLITUDE TEST
## A preregistered test of Longo 2011's published dipole amplitude at Longo's published axis

**Lana (science / claim-boundary seat), 2026-08-12. Status: DRAFT — goes to Kun's freeze gate; becomes
the preregistration only when sha-pinned after his PASS and every Binding Slot (§B) is filled with a
receipt.** Authorised by Kun's V2 regate (`reviews/KUN_SPIN_V2_REGATE_20260812.md`): *"Preregistration
drafting is authorized under my prior ruling."* **Not authorised, absolute and unchanged: any sky run,
any result, any publication or accepted status. The moment the next step would touch real galaxies,
this lane STOPS and reports that as the successful outcome.**

**Title rule (Kun, binding):** every derived artifact of this study titles itself a
**"Longo-amplitude test"** — never a "spin anisotropy test."

**Canonical boundary sentence** (Kun's exact wording; byte-identical wherever it appears, including in
V2 §0/§6 and in every derived artifact):
> **"A null here does not establish that the sky is isotropic; it rejects only Longo's published amplitude at Longo's published axis if the preregistered rejection rule is met."**

**Headline boundary (Kun's exact wording, carried with the title):**
> This tests Longo's published `A ≈ 0.0408` amplitude at Longo's published axis. It does not test
> `A ≈ 0.02`, Shamir, BHU, or whether the sky is isotropic.

**Provenance note, carried openly:** V2 §0 originally claimed its boundary warning appeared "verbatim"
in V2 §6; Kun's gate found it was equivalent wording, not verbatim — a custody error in exactly the
boundary language that gets copied. Repaired 2026-08-12 before this artifact was drafted: Kun's exact
sentence now appears byte-identically in V2 §0 and §6 (single-line form, verified by unique-line count),
and this prereg carries it as the canonical form. Gate chain: design V1 → Kun gate → feasibility spike
(Yui identity, Goru statistics/power, Tori pixel-path) → Kun spike gate (hard freeze conditions) → Goru
sample feasibility (no public survey clears N ≥ 200k accepted) → Duho: *"narrow it to Longo's
amplitude"* → V2 → Kun V2 regate (PASS FOR PREREGISTRATION DRAFTING) → this draft.

---

## 1. Claim under test (frozen)

**Longo 2011**, *Phys. Lett. B* 699, 224–229 (DOI 10.1016/j.physletb.2011.04.008): dipole asymmetry in
spiral-galaxy handedness of **|A_L| = 0.0408, σ_pub = 0.011**, at the axis
**n̂_L : (l, b) = (52°, 68.5°)** (equivalently (α, δ) = (217°, 32°) as published), from 15,158 SDSS
spirals at z < 0.085. The test asks exactly one question: **does an instrument that cannot produce the
sign reproduce or reject this amplitude at this axis?**

## 2. Frozen statistical protocol

All values in this section are **frozen**. Formulas are exact; the only quantities entering them at run
time are the bound N_accepted and measured a, via the rules stated here and the slots in §B.

- **F-1 Estimand.** D̂(n̂_L) = (1/N)·Σᵢ sign(χᵢ)·cos θᵢ over accepted galaxies; reconstructed amplitude
  Â = 3·D̂ (unbiasedness receipt: spike, injected 0.0400 → recovered 0.0402); attenuation-corrected
  Â_c = Â/(2a−1), a from §5.
- **F-2 Order of reporting.** Monopole M̂ = (1/N)·Σ sign(χᵢ) first, always; then D̂(n̂_L); then
  secondaries. No free-axis quantity is computed before the fixed-axis quantities are locked to disk.
- **F-3 Null.** Label-permutation: **N_perm = 100,000** permutations of {sign(χᵢ)} over fixed positions
  and footprint. One-sided p at Longo's sign.
- **F-4 σ definitions.** σ_D ≡ √(1/(3·N_accepted)); σ_ours ≡ 3·σ_D/(2a−1);
  σ_comb ≡ √(σ_pub² + σ_ours²) with σ_pub = 0.011.
- **F-5 Sign.** REPRODUCED requires **Longo's sign at Longo's oriented axis** — the sign convention is
  Binding Slot **BS-5** (filled by quotation from Longo's methods, never from memory).
- **F-6 Decision regions (exhaustive, mutually exclusive):**
  - **REPRODUCED-LONGO:** permutation p < **0.001** AND sign per F-5 AND |Â_c − 0.0408| ≤ 3·σ_comb.
  - **REJECTED-AT-LONGO-AMPLITUDE:** permutation p > **0.05** AND the 3σ upper limit on |Â_c|
    (|Â_c| + 3·σ_ours) < **0.0408**.
  - **INCONCLUSIVE:** any other numeric outcome, or any triggered INCONCLUSIVE rule in §4/§6.
  - **INCONCLUSIVE-BY-POWER:** declared before unblinding if the §5 power gate fails; the run does not
    start.
- **F-7 Effective detection floor (Kun's §2 requirement, stated so a tiny positive cannot masquerade as
  reproduction inside the broad band):** the p < 0.001 requirement implies a one-sided detection floor
  of **3.09·σ_ours** on Â_c. Evaluated at the frozen minima (N = 100,000, a = a_floor = 0.85):
  floor = 3.09 × 3·√(1/3×10⁵)/0.70 = **0.0242**; at a = 0.90: **0.0212**. The REPRODUCED band's low
  edge is therefore inoperative below the floor — **no Â_c below the evaluated floor can be called
  REPRODUCED regardless of the band**, and the evaluated floor is printed in the results table.
- **F-8 Secondaries (non-decision, reported after primary lock):** (i) D̂ at Shamir's axis
  (RA = 132°, Dec = 32°) with interval only — **no decision language about Shamir in any output**
  (kill switch K-14; his amplitude class is unpinned, BS-10); (ii) one free-axis scan on a HEALPix
  **Nside = 16** direction grid (3,072 directions), permutation-calibrated with the global maximum as
  the look-elsewhere statistic; multiplicity handled by the permutation distribution of the global
  maximum; **cannot modify or rescue the primary outcome**.
- **F-9 One run.** Any parameter change after any real-sky statistic voids the run (K-8); re-entry only
  via a new preregistration.

## 3. Instrument (frozen structure; production details = Binding Slots)

- **I-1 Primary:** equivariant classifier in the CE-ResNet pattern (Z-score from image, S-score from the
  same trunk on the index-reversed image), **trained exclusively on synthetic spirals — no human
  chirality label anywhere in training.** Full production spec (generator, architecture, weights-freeze
  policy, acceptance threshold τ, mirror receipts) is **Appendix A = Binding Slot BS-3 (Yui, drafting in
  parallel)**; this prereg is not freezable until BS-3 is filled and its receipts pass.
- **I-2 Secondary:** deterministic Ganalyzer-class geometric estimator, antisymmetrization-wrapped
  (χ = (w(x) − w(mirror(x)))/2), spec = **BS-4**; runs on the full sample; its accepted subset is the
  training-free cross-check. Disagreement rates on jointly-accepted objects are published.
- **I-3 Hard rules (frozen verbatim from the spike gate):**
  - **No-resampling mirror:** *"The mirror operation inside χ is pure pixel-index reversal on the final
    analysis raster. It is never an affine, WCS, interpolation, rotation, reprojection, or subpixel
    reflection transform. mirror(mirror(x)) == x must be byte-exact on the exact dtype passed to w."*
    (Receipt at freeze: unit test on the exact analysis raster and dtype. Yui's spike measured
    0.058–0.944 identity violation from an interpolating mirror — signal-sized against 0.04.)
  - **Signed-zero rule:** *"All chirality decisions use value comparisons with |χ| > τ and ordered
    numeric comparisons. No code may branch on signbit, copysign, raw IEEE-754 bit patterns, or the sign
    of zero. Exact zero and sub-threshold values abstain."* (Receipt: the unit test that fails on any
    sign-bit branch.)
- **I-4 Identity receipts required before any real image:** 1,000/1,000 bit-exact
  χ(mirror(x)) = −χ(x) on synthetic spirals for BOTH instruments on the production rasters (spike
  standard), plus paired original/mirror outputs, flip-balance, confidence/abstention deltas as
  published artifacts.
- **I-5 Sample selection:** survey photometric cuts only (constants at BS-6); **b/a > 0.4** (frozen);
  spirality gate via the mirror-invariant score s(x) = (u(x) + u(mirror(x)))/2 with threshold frozen in
  BS-3; **no human morphology flags, no Galaxy Zoo membership, anywhere in the chain.**

## 4. Covariate battery (structure and triggers frozen; products = BS-2)

Kun's ten fill-ins from the V2 regate are resolved here where survey-independent; survey-dependent items
are BS-2 with exact fill rules.

- **CB-1 Covariates (10):** imaging depth; seeing/PSF; Galactic extinction (SFD98 E(B−V)); stellar
  density (Gaia DR3 counts, G < 19); crowding (neighbour count within 30″ from the bound survey
  catalogue); angular size (half-light radius); axis ratio b/a; colour g−r; magnitude r; arm-contrast
  (our mirror-invariant s(x)). **Redshift: included only if the bound survey ships public photo-z for
  the parent sample (BS-2 decides), else dropped and the drop published. Deblend quality: bound to the
  survey's named flag set at BS-2, else dropped and published.**
- **CB-2 Sky-map form (frozen):** all map covariates on HEALPix **Nside = 128, RING, ICRS**; per-object
  value = value of the pixel containing the object (**no interpolation**); object in a missing/masked
  pixel → object missing that covariate. Sensitivity/abstention maps (CB-7): **Nside = 32, RING, ICRS**;
  pixels with < **50** processed objects masked.
- **CB-3 Standardisation and missing data (frozen):** per-object covariates z-scored on the accepted
  sample (mean/SD); objects missing any covariate are excluded from Layer A/B but retained in the
  primary statistic; any covariate missing for > **5%** of accepted objects is dropped from the battery
  and the drop published before unblinding.
- **CB-4 Layer A — stratified permutation (frozen):** deciles by rank, ties broken by ascending
  catalogue ID; if any decile occupancy < **200**, coarsen to quintiles; if still < 200, drop the
  covariate from Layer A (retain in Layer B) and publish. Leakage statistic
  L_C = |mean(D̂)_raw-null − mean(D̂)_C-stratified-null| at n̂_L. **Triggers (raw thresholds, applied
  first, no correction): L_C < 0.25·σ_D pass; 0.25·σ_D ≤ L_C < 0.5·σ_D flagged; L_C ≥ 0.5·σ_D →
  INCONCLUSIVE at n̂_L.** Joint version: correlation-matrix PCA on complete cases; PC1–3; 5×5×5
  rank-quantile cells (125); cells < **50** merged into the neighbouring cell with the next-lower PC1
  bin index (deterministic; then PC2, then PC3 order) until all cells ≥ 50.
- **CB-5 Layer B — predictability (frozen):** (i) logistic regression, scikit-learn
  `LogisticRegression(penalty=None, solver="lbfgs", tol=1e-8, max_iter=1000, class_weight=None)`, on
  z-scored covariates plus their squares (squares z-scored after squaring); likelihood-ratio test vs
  intercept-only; **reported, Holm-corrected with (ii); flag if Holm-p < 0.01; never a sole veto.**
  (ii) gradient-boosted trees, scikit-learn
  `GradientBoostingClassifier(n_estimators=200, max_depth=3, learning_rate=0.1, subsample=0.8,
  random_state=20260812)`, 5-fold stratified CV (`shuffle=True, random_state=20260812`), metric = mean
  out-of-fold AUC predicting sign(χ) from covariates only. **Triggers: AUC < 0.520 pass;
  0.520–0.550 flagged; AUC ≥ 0.550 → INCONCLUSIVE.**
- **CB-6 Order of operations (Kun item 10, frozen):** hard absolute thresholds (CB-4 L_C, CB-5 AUC)
  are evaluated first and are decision-bearing without any multiplicity correction (conservative);
  Holm–Bonferroni applies only to the significance flags published alongside (Layer A per-covariate
  shift p-values as one family of ≤ 11; Layer B's two tests as a second family).
- **CB-7 Layer C — monopole-coupling bound (frozen):** abstention map = abstained/processed per pixel;
  sensitivity map = (2a_s − 1) per pixel via §5 strata composition; Dip(·) = ℓ = 1 amplitude of a
  masked least-squares monopole+dipole fit. Coupling bound B = |M̂|·Dip(sens) + |M̂|·Dip(abst).
  **Trigger: the n̂_L result stands only if |D̂(n̂_L)| > 5·B; else INCONCLUSIVE at n̂_L.**
- **CB-8 Mirror-pair accounting (frozen):** every Layer A/B/C statistic is computed on the symmetrised
  accepted sample (object and mirror processed identically), so surviving correlations are diagnostic
  of selection/sky, not sorter chirality.

## 5. Hand-check attenuation protocol (frozen)

- **HC-1 Sample:** **N_hc = 500** accepted galaxies; **9 strata** = tertiles of |χ| × tertiles of
  angular size; allocation proportional to stratum population with a floor of **40** per stratum
  (remainder redistributed proportionally).
- **HC-2 Blinding:** each image presented in a **random parity** (mirrored or not, p = 0.5, seeded
  `random_state=20260812`), assignment key sealed (sha-pinned, opened only after all labels are in), so
  human chirality bias enters symmetrically and cancels in the accuracy estimate.
- **HC-3 Checkers and adjudication:** two independent checkers; disagreements go to a third blind
  checker; majority label is final. Checker identities and instructions frozen with this document.
- **HC-4 Estimate:** a = stratum-weighted agreement between instrument sign and final human sign
  (de-mirrored via the key); per-stratum Wilson 68% intervals; σ_a by delta method through the stratum
  weights; propagated as σ(2a−1) = 2σ_a into σ_ours and both decision regions of F-6 (bands evaluated
  at the measured a, printed with their propagated widths).
- **HC-5 Validity floor (frozen):** **a ≥ 0.85** overall, and no stratum with a_s < 0.70. Failure →
  INCONCLUSIVE-BY-POWER (instrument not accurate enough for the narrowed target), run does not start.
- **HC-6 Power gate (frozen rule, receipt = BS-8):** using the sha-pinned spike harness
  (`spike/sim_power.py`), power is recomputed at **A_eff = (2a − 1) × 0.0408** with the bound
  N_accepted. **Requirement: power ≥ 0.95 at p < 0.001.** Reference points from the spike (a = 1):
  100% at A = 0.04, N = 10⁵; 62.2% at A = 0.02, N = 10⁵. Failure → INCONCLUSIVE-BY-POWER, declared, no
  run. **Minimum accepted sample (frozen): N_accepted ≥ 100,000** after all cuts, abstentions, and
  mirror-pair exclusions.

## 6. Pixel-path custody and negative controls (frozen; branch declarations = BS-7)

- **PC-1** Single survey, single cutout route, exact versions (BS-1); checksums and query logs at the
  Mittal–Singal custody standard.
- **PC-2** The delivered pixel product + WCS is the measurement input. If the bound service has already
  resampled (e.g., DESI Legacy generated TAN cutouts — Tori's audit), that is not automatically fatal:
  the injection battery runs **through the same service path**, and **no further resampling of any kind
  follows** (Kun's spike ruling, adopted verbatim in substance).
- **PC-3** Per-object WCS parity: CD/PC·CDELT determinant logged; row-order transform determinant
  logged; combined pixel→sky sign logged; handedness evaluated in sky coordinates (winding
  East-of-North).
- **PC-4** **Distortion policy (branch declared at BS-7):** fail closed on SIP/PV/CPDIS/DET2IM
  keywords, **or** tested local Jacobian-sign receipts across the cutout. **No silent
  linear-determinant fallback** (frozen).
- **PC-5 Injection battery (frozen pass criteria):** ≥ **1,000** synthetic chiral sources, both
  parities, spanning the footprint, pushed through the entire delivered-pixel path: required **100%**
  correct signed recovery and exact count swap under mirroring; the deliberate silent-row-flip and
  scrambled-WCS controls must be **detected** (the harness must fail when it should — spike standard).
- **NC-1…NC-6 (frozen):** C1 full-mirror run of the accepted sample — counts must swap exactly and
  D̂ must negate exactly (tolerance 0; deviations are pipeline faults); C2 permutation nulls (F-3);
  C3 axis controls — D̂(−n̂_L) must negate; two orthogonal axes (frozen at freeze from n̂_L by the
  standard orthonormal construction) must be null-consistent at p > 0.01; C4 = §4 battery;
  C5 = CB-7; C6 splits — D̂ by depth tertile, hemisphere, size tertile, published with heterogeneity
  χ² (flag if p < 0.01; splits are diagnostics, not deciders).

## 7. Outcome handling (frozen)

- All outcomes — REPRODUCED-LONGO, REJECTED-AT-LONGO-AMPLITUDE, INCONCLUSIVE, INCONCLUSIVE-BY-POWER —
  are published with the full receipt set. INCONCLUSIVE triggers are exact (§4/§5/§6); the word cannot
  be negotiated after the fact.
- **A REPRODUCED-LONGO outcome triggers an adversarial systematics re-audit inside the lane before any
  claim, video, or upload exists.** It would NOT identify BHU (Kun, verbatim: *"Any positive spin
  result … would be a spin-anisotropy/statistical-isotropy result only"*), and no BHU interpretation is
  authorised in any artifact of this study.
- Every derived artifact carries: the **title rule**, the **canonical boundary sentence**
  (byte-identical), and the **headline boundary** — all three from the preamble of this document.

## B. BINDING SLOT REGISTER — the only unfrozen items, each with its fill rule and validity range

| ID | What | Fill rule | Validity range (else prereg INVALID, back to gate) | Owner |
|---|---|---|---|---|
| BS-1 | Survey route | Tori custody receipt (products, versions, cutout service, licence) + Goru accepted-yield receipt for the route | forecast N_accepted ≥ 100,000 with the BS-3 instrument's measured acceptance; footprint var(cos θ) about n̂_L ≥ **0.15**; licence permits derived-catalogue publication | Tori + Goru |
| BS-2 | Covariate products | exact named public products/versions per CB-1, each covering ≥ **95%** of the accepted footprint; photo-z and deblend-flag decisions declared | any covariate failing coverage → dropped + published; ≥ **8** of 10 covariates must survive | Tori |
| BS-3 | Primary instrument (Appendix A) | Yui's appendix: synthetic generator spec, architecture, weights-freeze policy, τ, acceptance rate, mirror receipts | identity 1,000/1,000 bit-exact; acceptance × BS-1 parent forecast ≥ 100,000; τ frozen before any real image | Yui |
| BS-4 | Secondary instrument spec | frozen algorithm description + same identity receipts | identity bit-exact; abstention published | Yui/Lana |
| BS-5 | Longo sign dictionary | verbatim quotation of Longo 2011's sign/axis-orientation definition, with page/paragraph, mapped to our East-of-North winding convention | unambiguous mapping; if the paper is ambiguous, the documented convention is chosen so his reported amplitude is positive toward his stated axis, and the ambiguity is published | Lana |
| BS-6 | Photometric cut constants | numeric cuts (mag/size/SB ranges) for the bound survey, set from survey documentation only — never from label distributions | cuts cite survey docs; no cut references any chirality or morphology label | Lana + Tori |
| BS-7 | Distortion branch | declaration: fail-closed OR local-Jacobian, with the corresponding receipt for the bound route | one branch declared; receipts pass | Tori |
| BS-8 | Power receipt | rerun of sha-pinned `spike/sim_power.py` at A_eff = (2a−1)·0.0408, bound N | power ≥ 0.95 at p < 0.001 | Goru |
| BS-9 | Evaluated constants table | σ_D, σ_ours, σ_comb, detection floor (F-7), REPRODUCED band, expected null UL — evaluated at bound N and measured a, printed | σ_ours ≤ **0.008**; detection floor ≤ **0.025** | Lana |
| BS-10 | Shamir amplitude class | custody-pinned from Shamir 2012 full text **[VERIFY]** | informational only; K-14 stands regardless | Tori/Lana |

**Freeze condition:** all ten slots filled with receipts inside their validity ranges → the assembled
document is sha-pinned and returns to Kun for the freeze gate. Any slot outside its range → the prereg
is INVALID as-is and returns to design, not to negotiation.

## Kill switches

K-1…K-14 of V2 carry unchanged and bind this document. Restated for the two that govern conduct from
this point: **K-8** — any parameter change after any real-sky statistic voids the run; **STOP rule
(Hwao, this dispatch)** — if work reaches the point where the next step is touching real galaxies, the
lane stops and reports that as the successful outcome.

---

**Open [VERIFY] register:** BS-5 (Longo sign, from methods), BS-10 (Shamir amplitude class), production
acceptance rates (BS-3/BS-4 receipts), Legacy photo-z product existence (BS-2). Nothing in this draft
authorises a run. **Nothing is published, accepted, or run; Kun gates this draft; Duho decides.**

— Lana, 2026-08-12.

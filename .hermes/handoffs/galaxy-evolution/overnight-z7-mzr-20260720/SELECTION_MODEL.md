# SELECTION_MODEL — Phase-6 JWST emission-line selection forward model (Test 4)

**Run:** overnight-z7-mzr-20260720 (Trikitear) · **Phase 6 (Tori)** · 2026-07-20T08:51:50+0900 KST
**Purpose:** Bound the emission-line **selection bias** Δ_sel(dex) on the recovered z>7
mass–metallicity relation, correct the observed offset (0.45 dex matched, 0.33 dex Te-only),
and decide pre-registered **Test 4 (selection)** — the one test the P2/P4 gate could not close
because the bias was *unbounded*. Real physics, honest brackets, no fabricated results.

---

## What Δ_sel is (and is not)
Δ_sel ≡ ⟨12+log(O/H)⟩_intrinsic(parent) − ⟨12+log(O/H)⟩_detected, at **fixed stellar mass**,
averaged over the overlap window logM∈[8.0, 9.5]. It is a **pure sample-selection shift**: the
O/H *estimator* is taken to be unbiased (Te is calibration-free; strong-line calibration bias is
Test 3, already handled), so a detected galaxy's recovered O/H equals its true O/H, and the only
thing selection does is change *which* galaxies enter each mass bin. Δ_sel>0 means the detected
sample is metal-poor relative to the true population at that mass → selection *inflates* the
apparent deficit. Corrected offset = observed − Δ_sel (exactly the pre-registered correction).

## Forward model (Monte Carlo, N=3–4×10⁵ per run)
1. **Parent population.** Stellar masses drawn from a **Schechter SMF** in log-mass,
   φ(logM)∝(M/M*)^(α+1)e^(−M/M*), logM*=10.0, faint-end slope **α=−1.9** fiducial
   (z≈8 SMF, Song et al. 2016; varied −1.7…−2.1). Redshifts drawn from the **actual
   Nakajima+23 z>7 sample** (z=7.0–8.7) so d_L is grounded, not assumed.
2. **Intrinsic MZR + scatter.** 12+log(O/H)=MZR(logM) with low-mass slope 0.30
   (Sanders et al. 2021) and total scatter σ_OH=0.12 dex fiducial (0.10–0.20 grid).
   Two normalisations run — **local-like** and **modest-evolution** (−0.3 dex) — to test
   normalisation-invariance of the bias.
3. **FMR coupling.** log SFR from a z≈8 main sequence (sSFR~few×10⁻⁹/yr, slope 0.9) with
   scatter σ_MS=0.35 dex; at fixed mass, higher SFR ↔ **lower** O/H via an FMR anti-correlation
   β_FMR=0.20 (0.10–0.30 grid) (Mannucci et al. 2010; Sanders et al. 2021). This is what makes
   *any* flux-limited selection lean metal-poor.
4. **Emission lines.** L(Hβ) from SFR (Kennicutt & Evans 2012, Chabrier: L(Hα)=1.86×10⁴¹·SFR,
   Hβ=Hα/2.86). L([OIII]5007)=L(Hβ)·R3(O/H) and L([OII]3727)=L(Hβ)·R2(O/H) with the
   **Curti et al. (2020)** strong-line calibrations. **Auroral [OIII]4363** from atomic physics:
   I(4363)/I(5007)=0.169·exp(−3.29×10⁴/Te) (Osterbrock & Ferland, low-density limit), with a
   Te–O/H anti-correlation (Te~1.4×10⁴K at O/H=8.0 rising to ~2×10⁴K at O/H=7.3; Nakajima+22 /
   Curti+20 Te behaviour). **4363 rises steeply toward low O/H / high Te — the crux of the
   Te-subset bias.**
5. **Selection.** Fluxes at d_L(z) (Planck18). Probabilistic detection: measured = true + N(0,σ_line),
   S/N>cut. **Strong-line subset** detected if Hβ **and** [OIII]5007 pass (R3 minimum, as most z>7
   objects use); **Te subset** additionally requires [OIII]4363. Fiducial σ_line=1.5×10⁻¹⁹
   erg s⁻¹ cm⁻² (deep NIRSpec-like; ±0.3 dex grid = 0.75–3×10⁻¹⁹, which also folds in the lensing
   magnification spread of the GLASS/ERO fields), S/N cut 5 (3–5 grid). Fiducial flux limits place
   the detection boundary at logM≈8.5–9 — matching the sparsity of the real z>7 sample below logM 8.
6. **Recover** the MZR from the detected mocks in [8.0,9.5], per 0.5-dex bin, and difference against
   the input → Δ_sel(mass), separately for Te and strong-line.

## Sensitivity grid (one-at-a-time + 32 multi-knob corners)
flux limit ±0.3 dex · α∈{−1.7,−1.9,−2.1} · σ_OH∈{0.10,0.15,0.20} · S/N∈{3,5} ·
β_FMR∈{0.10,0.20,0.30} · MZR∈{local-like, modest-evol}. Δ_sel reported as a **range**.

---

## RESULTS — Δ_sel is now BOUNDED (this was the original failure)

| subset | Δ_sel bracket (dex) | fiducial |
|---|---|---|
| **strong-line** (drives the matched N=16 sample) | **0.01 – 0.11** | 0.04 |
| **Te / auroral** (the "calibration-free" subset) | **0.04 – 0.35** | 0.22 |

**Key physical finding (counter-intuitive):** the **auroral/Te subset is the MORE
selection-biased**, not the safer one. Auroral [OIII]4363 detectability itself preferentially
selects low-metallicity/high-Te galaxies, so the "clean" Te subset is where selection bites hardest
(0.04–0.35 dex, and normalisation-dependent — a more metal-poor true population makes 4363 easier to
detect and shrinks the bias). The **strong-line** selection is nearly metallicity-neutral: the
[OIII]5007 requirement favors *higher* O/H (more oxygen → brighter 5007), which largely cancels the
FMR-driven metal-poor lean, leaving only ~0.01–0.11 dex.

### Corrected offsets
- **Matched (headline):** 0.449 − Δ_sel,strong ⇒ **0.41 dex** (central), conservative CI
  **[0.17, 0.61]** (obs bootstrap CI folded with the full Δ_sel range). Excludes 0 across the
  entire grid; worst-case (Δ_sel=0.11) central still 0.34 dex.
- **Te-only:** 0.332 − Δ_sel,Te ⇒ **0.09 dex** (central), CI **[−0.27, 0.49]** — **includes 0**.
  Selection explains ~40–100% of the Te-only offset; the Te-only "detection" is largely a selection
  artifact and cannot stand on its own.

---

## TEST 4 VERDICT: **PASS (for the matched/headline offset)**

Both pre-registered PASS conditions are met for the headline number:
1. **Δ_sel is now bounded** (strong-line 0.01–0.11 dex over the full grid incl. 32 corners) — the
   original failure (unbounded, could-be-anything) is resolved.
2. **The corrected matched offset's plausible range excludes 0** across the entire sensitivity grid
   (CI [0.17, 0.61]; worst-case central 0.34 dex).

Selection therefore **cannot by itself account for** the 0.45 dex matched deficit — it contributes
only ~0.04 dex (≈10%), leaving a **residual physical deficit ≈0.41 dex**. Per the pre-registration
Test-4 criterion ("selection stated AND its direction cannot by itself account for the measured
offset"), Test 4 **passes** for the matched sample.

**Honest caveats (do not overclaim):**
- The **Te-only subset does NOT pass** on its own: its selection bias (0.04–0.35 dex) is comparable
  to its 0.33 dex offset, so the corrected Te CI includes 0. The robust evidence is the strong-line/
  matched offset, *not* the Te subset — the reverse of the earlier intuition that Te was the
  conservative anchor.
- The Δ_sel,Te bracket is genuinely wide and **normalisation-dependent** (auroral detectability
  depends on the true O/H level, which is what we're trying to measure) — it can only be *bracketed*,
  not pinned.
- Δ_sel,strong is near-invariant to intrinsic MZR normalisation (0.041 vs 0.042 across the two MZRs),
  as expected for a differential within-mass effect — which is why the matched correction is trustworthy.

**Bottom line:** with selection now forward-modeled and bounded, the z>7 MZR deficit moves from a
"strong upper bound" to a **selection-corrected measurement of ≈0.41 dex** at fixed mass (CI excludes
0), driven by the near-unbiased strong-line sample; ≈0.04 dex (~10%) of the 0.45 dex is selection,
~0.41 dex is residual physical. The Te-only channel is selection-dominated and should be quoted only
as corroboration, not as the primary result.

## References (all identity-verified in the DR packet or standard atomic physics)
Song et al. (2016) SMF z=8 · Sanders et al. (2021) MZR slope/evolution & FMR · Mannucci et al. (2010)
FMR · Curti et al. (2020, MNRAS 491,944) strong-line R2/R3 calibrations · Nakajima et al. (2022/2023)
Te / high-z diagnostics · Kennicutt & Evans (2012) SFR–L(Hα) · Osterbrock & Ferland (2006) [OIII]
auroral atomic physics · Planck18 cosmology (astropy).

## Files
`selection_forward_model.py` · `selection_results.json` · `fig_selection.png` · `_fig_selection.py`

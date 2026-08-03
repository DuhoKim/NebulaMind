# Cycle 3 — Tori: ready-to-apply manuscript text

Two jobs. All numbers verbatim from Goru's cycle-2 writeup (`cycle2_goru.md`) and Kun's
re-derivation (`cycle2_kun_gate.md`). No repo edits — these are the exact passages to drop in.

===============================================================================
# JOB 1 — Paper #4 (TNG massive-galaxy abundance) revised passages
Target body: `.../research-frontiers/tng-massive-galaxy-abundance-systematics.pdf`
Applies Kun's E1–E7. Each deliverable is labelled with the E-item(s) it satisfies.
===============================================================================

-------------------------------------------------------------------------------
## 1A. REVISED ABSTRACT  [satisfies E1, E2, E4, E5]
-------------------------------------------------------------------------------

The reported over-abundance of massive galaxies at z > 4 relative to ΛCDM hydrodynamical
simulations ("too massive, too early") has been read as possible evidence for new physics. We
test this by confronting IllustrisTNG (TNG100-1) cumulative number densities n(> M⋆, z) against
JWST-era observations on a like-for-like stellar-mass basis, and by benchmarking the observed
abundance against the ΛCDM baryon-conversion ceiling. At z ≃ 5–6 the observed
n(> 10^10.5 M⊙) (Weibel et al. 2024, ≈ 3×10^−5 Mpc^−3) exceeds TNG (1.1×10^−5 Mpc^−3 at z = 5)
by a factor ≈ 2.7 (0.43 dex); given the steep massive-end slope of the simulated stellar mass
function (d log n/d log M⋆ ≈ −1.58), this excess is erased by a downward stellar-mass shift of
only ≈ 0.28 dex. We replace the loosely quoted "~1 dex" budget with an itemized, six-axis
stellar-mass systematic ledger whose realistic (independent-quadrature) value is 0.55 dex —
0.46 dex if the contested top-heavy-IMF term is excluded, and 1.30 dex only in the fully
correlated worst case. The required 0.28 dex shift is ~0.5× the committed budget and is covered
even without invoking a top-heavy IMF; the z ≃ 5–6 consistency is therefore robust and
IMF-independent. Crucially, the *unshifted* observed abundance already implies a
baryon-conversion efficiency ε = M⋆/(f_b·M_halo) ≈ 0.20 at the abundance-matched halo mass
M_halo = 1.0×10^12 M⊙ (f_b = 0.157) — i.e. the fiducial ΛCDM star-formation efficiency, far
below the ε ≤ 1 hard ceiling. The z ≃ 5–6 offset is thus not a ΛCDM stress test at all but a
mismatch against TNG's *specific* feedback/SMF calibration; ΛCDM feasibility would be breached
only if the true masses were ≈ +0.70 dex *higher* than reported (opposite in sign, and 2.5×
larger than any plausible downward budget). The larger apparent excess at z ≃ 7–9 (Labbé et al.
2023 candidates, ≈ 13.6×, 1.13 dex) requires ≈ 0.72 dex at the same slope — which *exceeds* the
committed 0.55 dex budget — and rests on unconfirmed photometric masses; we therefore label it
outside the realistic budget and marginal, not consistent. We flag as a distinct, harder
residual the spectroscopically confirmed quiescent galaxies at z > 6, whose ∼ 2 dex excess is
not dissolved by these systematics. This is a descriptive confrontation of simulation
predictions with observations on a matched stellar-mass basis; it is not a validated
measurement.

-------------------------------------------------------------------------------
## 1B. NEW SUBSECTION — Itemized stellar-mass systematic budget  [satisfies E1; also E4/E5 lead-in]
Insert as §3.1 (or a boxed subsection immediately after the Results paragraph that
currently quotes "~1 dex"). Replaces the sentence "The stellar-mass systematic budget
from independent recent analyses is substantially larger than either: SED-fitting codes
disagree by ∼1 dex …"
-------------------------------------------------------------------------------

**3.1. An itemized stellar-mass systematic budget.**
The claim that the required shift lies "within the budget" is only as good as the budget. We
therefore replace the single "~1 dex" figure — which is the code-to-code SED spread, and already
*contains* the IMF, SPS and SFH drivers it is often added to — with a decomposition into
independent physical axes, each driving a downward revision of M⋆ for z ≈ 4–6 massive JWST
galaxies:

| # | Source of M⋆ systematic | central (dex) | plausible range | grounding |
|---|--------------------------|:---:|:---:|---|
| 1 | IMF choice (Chabrier → top-heavy at high z) | 0.30 | 0.1–1.0 | Lapi+2024; Steinhardt+2023 |
| 2 | SFH prior / outshining (parametric vs nonparametric) | 0.30 | 0.2–0.5 | Harvey+2025 (EPOCHS IV) |
| 3 | SPS model + nebular continuum (BC03 vs BPASS) | 0.20 | 0.1–0.3 | Choe+2026; Cochrane+2025 |
| 4 | Dust–age–metallicity degeneracy | 0.15 | 0.1–0.25 | Choe+2026 |
| 5 | AGN / "Little Red Dot" host contamination (pop.-averaged) | 0.20 | 0.1–1.0* | Zhuang+2026; Kocevski+2025 |
| 6 | Eddington bias (steep MF × mass-error convolution) | 0.15 | 0.1–0.25 | Adams+2023; Grazian+2015 |

*Per-object LRD contamination can reach orders of magnitude, but only a fraction of the massive
sample are LRDs, so the population-averaged budget is ≈ 0.2 dex.

Combining these independently in quadrature gives a **realistic committed budget of 0.55 dex**;
dropping the contested top-heavy-IMF term (#1) gives **0.46 dex**; the fully correlated
worst case (linear sum) is **1.30 dex** — this last is the "~1 dex" figure the earlier literature
quotes, and it is an *upper* bound, not the realistic budget. We caution that terms #2–#4 are
three manifestations of the same SED-fitting degeneracy and #6 is partly derived from the #1–#4
mass scatter, so treating all six as strictly independent mildly inflates the quadrature; a
hostile accounting lands the committed budget in the range **0.46–0.55 dex**. We adopt this
range, not a single clean number.

Against this budget: the z ≃ 5–6 requirement of 0.28 dex is ≈ 0.5–0.6× the committed budget and
is covered even by the IMF-excluded 0.46 dex — so the z ≃ 5–6 consistency does **not** depend on
a top-heavy IMF and is robust. The z ≃ 7–9 requirement of 0.72 dex (Section 3, at s = −1.58)
**exceeds** the committed 0.55 dex quadrature budget and is met only under the fully correlated
worst case; it is therefore marginal and photometric, and we group it with the quiescent excess
as outside the realistic budget rather than with the secure z ≃ 5–6 result. The spectroscopic
quiescent z > 6 excess (≳ 1.4 dex required) exceeds even the 1.30 dex linear worst case and is
genuinely outside budget.

> Note on the z ≃ 7–9 arithmetic (corrects the abstract/Results of the prior draft): erasing the
> z ≃ 7–9 factor of 13.6× (1.134 dex) at the paper's own slope s = −1.58 requires
> Δ = 1.134/1.58 = **0.72 dex**, consistent with Table 1's 0.70 dex at s = −1.6 — **not** the
> 0.44 dex quoted previously, which would follow only from an unstated steeper high-z slope
> (s ≈ −2.6). The correct like-for-like value is 0.72 dex, and it is outside the committed budget.

-------------------------------------------------------------------------------
## 1C. FALSIFICATION-THRESHOLD PARAGRAPH  [satisfies E3, E4; corrects the Tinker sentence]
Insert into §4 Discussion (before the quiescent-residual paragraph), and mirror the two
thresholds as a footnote to Table 1.
-------------------------------------------------------------------------------

The conclusion is falsifiable on two distinct axes that must not be conflated.
**(i) Abundance vs TNG (from Table 1).** The z ≃ 5–6 null reverts to a tension only if the true
mass-systematic budget is < 0.28 dex; the z ≃ 7–9 point reverts below its slope-dependent
threshold of ≈ 0.72 dex (at s = −1.58). The committed 0.46–0.55 dex budget clears the first with
a factor ~2 of margin but falls *short* of the second — hence z ≃ 7–9 is labelled marginal.
**(ii) ΛCDM physical feasibility (the hard bound).** Abundance-matching the observed
n = 3×10^−5 Mpc^−3 at z = 5 to a self-contained Sheth–Tormen halo mass function (Planck
f_b = 0.157) gives M_halo = 1.0×10^12 M⊙ (log = 12.00; HMF sanity n(> 10^12, z = 5) = 3.0×10^−5
Mpc^−3, self-consistent). The unshifted M⋆ = 10^10.50 then implies a baryon-conversion efficiency
ε = M⋆/(f_b·M_halo) = **0.20** — precisely the fiducial ΛCDM value and well under the ε ≤ 1 hard
ceiling (Boylan-Kolchin 2023); after the 0.28 dex shift, ε = **0.105**. The ε = 1 ceiling is
breached only if the true masses are **+0.70 dex HIGHER** than reported — a change opposite in
sign, and 2.5× larger, than any plausible downward systematic. The observed abundance is thus
nowhere near physically impossible in ΛCDM. This benchmark is robust to the HMF prescription:
across Sheth–Tormen, Tinker-2008 and Press–Schechter and across halo mass-definition choices,
the abundance-matched M_halo moves by ≲ 0.12 dex, shifting ε by ≤ ~0.06 (a Tinker-2008 200m mass
function gives log M_halo = 11.90, ε ≈ 0.26) and the +0.70 dex breach threshold by ≤ ~0.11 dex
(to ≈ +0.59 dex). The direction of this HMF sensitivity runs mildly *against* consistency
(higher ε, thinner margin), but ε ≈ 0.2–0.26 is nowhere near unity and the verdict is unchanged
— we therefore quote the HMF sensitivity as ≤ ~0.06 in ε and ≤ ~0.11 dex in the threshold, and
do not claim it is ≲ 0.05 dex.

-------------------------------------------------------------------------------
## 1D. REVISED CONCLUSION  [satisfies E5; keeps "descriptive — not validated"; honest z7-9]
-------------------------------------------------------------------------------

The "too massive, too early" reading of JWST massive-galaxy counts at z ≃ 5–6 is not a ΛCDM
stress test. The *unshifted* observed abundance already sits at a baryon-conversion efficiency
ε ≈ 0.20 — the fiducial ΛCDM star-formation efficiency — so ΛCDM is comfortably satisfied with
no mass revision at all; reaching the ε = 1 physical ceiling would require masses ≈ +0.70 dex
*higher* than reported, not lower. What the z ≃ 5–6 offset actually probes is TNG's *specific*
feedback and SMF calibration: the factor-2.7 excess is erased by a 0.28 dex downward stellar-mass
shift, ≈ half the committed 0.46–0.55 dex systematic budget and covered even without a top-heavy
IMF, so we find no robust tension with TNG at z ≃ 5–6. We do not claim a measurement of
consistency, only that the data at these redshifts neither require a departure from ΛCDM nor a
change to TNG beyond its known stellar-mass systematics. The apparent z ≃ 7–9 excess is a weaker
case: it requires ≈ 0.72 dex, which exceeds the committed budget, and rests on unconfirmed
photometric masses — we label it outside the realistic budget and marginal, alongside the one
genuine ΛCDM-relevant residual, the spectroscopically confirmed quiescent galaxies at z > 6
whose ∼ 2 dex excess is not dissolved by these systematics and is not claimed to be resolved
here. This is a descriptive, automated confrontation; it has not been validated by human review.

-------------------------------------------------------------------------------
## 1E. Flags — E-items NOT fully satisfiable from available material
-------------------------------------------------------------------------------
- **E6 (M4 — TNG stellar-mass aperture):** NOT satisfiable from the materials. Neither Goru's
  writeup nor the current PDF states which TNG100-1 aperture defines M⋆ (total-subhalo vs 2R½ / 30
  kpc). This must be pulled from the TNG catalog metadata and either matched to the SED-mass
  convention or added as a *named* definition-offset line in the §3.1 ledger. Recommended
  placeholder text once the aperture is known: "TNG100-1 M⋆ is the [total-subhalo / within-2R½]
  value; the SED masses are total-galaxy, an offset of [X] dex, which we add to the budget as
  term #0." Cannot be filled in honestly here — FLAG for M4 author.
- **E7 (M5 — in-box object count / single-anchor fragility):** PARTIALLY satisfiable. The TNG100
  box (110 Mpc, V ≈ 1.33×10^6 Mpc^3) at n ≈ 1.1×10^−5–3×10^−5 Mpc^−3 implies only ≈ **15
  (TNG-predicted) to ≈ 40 (observation-implied)** objects above 10^10.5 M⊙ — a small, cosmic-
  variance-limited count resting on a single Weibel data point versus a single TNG value. I have
  folded a one-line version of this into §3.1/§4 where natural, but the *exact* in-box subhalo
  count at the matched z must be read from the catalog (I only have the number-density anchors,
  not the raw N). FLAG the single-anchor fragility explicitly in M5.
- **E7 (M6 — TNG n at the observed bin's median z):** NOT fully satisfiable. Only the z = 5 TNG
  value (1.1×10^−5 Mpc^−3) is in the materials; the z = 6 value needed to bracket the z ≃ 5–6
  median is not provided. FLAG for M6 author to quote n at both z = 5 and z = 6 for an exact
  like-for-like.
- E1–E5 are fully satisfied above.


===============================================================================
# JOB 2 — Paper #1 reframe, finalized (N reconciled)
Target body: `.../studies/z9-10-unlensed-metallicity-deficit.pdf`
Non-blocking fix applied: N≈6 vs N=5. Correct count from the body — the Pollock et al. (2026)
unlensed core sample is **N = 5** direct-Te (z = 9.3–9.9); §4 Discussion *extends* it to z = 10.6
with GN-z11 (Curti et al. 2023), making **6** individual detections. I therefore standardize on
"N = 5 (6 including GN-z11 at z = 10.6)" and remove the stray "≈6", so the reframed abstract's
"N = 5 direct-Te" and the closing sentence are internally consistent with each other and with the
body. No number or claim-strength changed.
===============================================================================

-------------------------------------------------------------------------------
## 2A. FINAL ABSTRACT (ship-ready)
-------------------------------------------------------------------------------

Whether the earliest galaxies are already chemically enriched or remain genuinely metal-poor
relative to the local mass–metallicity relation (MZR) is unsettled. JWST/NIRSpec studies have
variously reported a declining MZR normalization toward z ≈ 8 (Langeroodi et al. 2023; Sarkar et
al. 2025) and rapid early enrichment that keeps massive galaxies near local abundances by z ≈ 5
(Faisst et al. 2026), and the earliest z > 7 anchors that would break the tie are dominated by
gravitationally lensed galaxies — where differential magnification distorts the inferred stellar
masses, and where the (fundamental) metallicity relation has historically been probed (cf. Belli
et al. 2013). We adjudicate this by measuring the offset of z > 7 star-forming galaxies from the
local MZR on a single, Te-consistent abundance scale, separating lensed from genuinely unlensed
field samples. Restricting the Nakajima et al. (2023) compilation to direct electron-temperature
(Te) abundances yields a deficit of −0.47 ± 0.10 dex, but two of its anchors (ERO, GLASS) lie
behind lensing clusters. Using instead the strictly unlensed field sample of Pollock et al.
(2026) (CAPERS/JADES, N = 5 direct-Te, z = 9.3–9.9, log M⋆ = 8.2–8.6), we recover
−0.69 ± 0.03 dex, robust to leave-one-out (spread 0.04 dex). The deficit is also robust to the
choice of local anchor: replacing the Curti et al. (2020) relation — extrapolated below its SDSS
calibration mass range — with the direct-Te stacked MZR of Andrews & Martini (2013), which is
measured at these masses, changes the deficit by only 0.04 dex (to −0.65 dex). An independent,
much larger stacked-Te sample — the ∼ 1500-galaxy JADES analysis of Isobe et al. (2026) — gives a
consistent normalization deficit of −0.5 to −0.6 dex at log M⋆ = 8 (12 + log O/H = 7.62 at
log M⋆ = 8 over z = 4–10) via a different method; the z ≃ 9–10-specific value rests on the
individual detections. Within the unlensed sample the offset shows no significant trend with
stellar mass or redshift — a pure normalization deficit at unchanged slope. The dominant
remaining uncertainty is the absolute Te abundance scale (∼ 0.1–0.2 dex). On an independent,
unlensed, single-scale footing the data therefore land on the metal-poor side of this debate: a
robust deficit relative to the local MZR, present across two high-z samples and two local anchors
— and explicitly not a formal statistical detection, nor a validated measurement. What it settles
is the sign and approximate size of the z ≃ 9–10 offset on lensing-free, single-scale data; what
it cannot yet settle is the precise value, bounded by the ∼ 0.1–0.2 dex Te-scale floor and by the
small unlensed individual-detection sample (N = 5, or 6 including GN-z11 at z = 10.6).

-------------------------------------------------------------------------------
## 2B. FINAL OPENING PARAGRAPH — §1 Introduction (ship-ready)
-------------------------------------------------------------------------------

The gas-phase mass–metallicity relation (MZR) encodes the integrated history of star formation,
accretion, and outflows, and its behavior at z > 7 has become a specific point of contention:
does the MZR normalization decline toward the Epoch of Reionization — leaving the earliest
galaxies genuinely metal-poor at fixed stellar mass — or have these galaxies already enriched
rapidly toward near-local abundances? JWST/NIRSpec measurements have reported an evolving,
declining normalization out to z ≈ 8 (Langeroodi et al. 2023; Sarkar et al. 2025), while others
infer fast early enrichment that keeps massive galaxies close to the local relation by z ≈ 5
(Faisst et al. 2026). The disagreement persists in part because the deciding z > 7 auroral-line
anchors are dominated by gravitationally lensed galaxies — and the universality of the
(fundamental) metallicity relation has historically been probed precisely with such lensed
samples (Belli et al. 2013). Two systematics limit these tests: (i) lensing, since the compact
H ii regions emitting auroral [O iii] λ4363 are spatially offset from the extended stellar
continuum, so a single magnification factor distorts M⋆; and (ii) the local anchor, which at the
low masses of high-z galaxies (log M⋆ ∼ 8) is typically an extrapolation of relations calibrated
on more massive SDSS galaxies. Both systematics act on the normalization of the offset — exactly
the quantity in dispute — so an independent measurement that removes lensing (an unlensed field
sample) and controls the anchor (a directly-measured local Te relation), all on a single
Te-consistent abundance scale, can adjudicate the sign and approximate size of any z ≃ 9–10
deficit even where it cannot yet pin the precise value. We make that measurement here, and
address both systematics directly.

-------------------------------------------------------------------------------
## 2C. Change note (JOB 2)
-------------------------------------------------------------------------------
- ONLY change vs Tori's cycle-2 reframe: the closing clause of the abstract now reads
  "the small unlensed individual-detection sample (N = 5, or 6 including GN-z11 at z = 10.6)"
  in place of "the N ≈ 6 individual-detection sample." This reconciles Kun's flagged
  inconsistency: the abstract's Pollock "N = 5 direct-Te" is the core unlensed sample, and §4's
  GN-z11 (Curti et al. 2023, z = 10.6) extension makes 6 — now stated explicitly rather than
  papered over with "≈6". Verified against the body: PDF §4 reads "Extending the unlensed
  direct-Te sample to z = 10.6 with GN-z11 … leaves the population deficit at −0.64 to −0.68 dex."
- No other number, citation, or claim-strength changed. Intro unchanged from cycle-2 (it carries
  no N count, so it is already consistent). Both "not a validated measurement" and "not a formal
  statistical detection" are retained as closing clauses. SHIP-READY.

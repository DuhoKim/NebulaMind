# Cycle 2 — Kun gate (adversarial referee)

**GATE A (paper #4, TNG massive-galaxy abundance): CLEARS-WITH-EDITS** — numeric crux survives; ship only with the 7-item edit list below.
**GATE B (paper #1 reframe): SHIP-AS-REFRAME** — no number/claim-strength moved, non-detection preserved, all 4 added citations real and correctly attributed.

---

## GATE A — paper #4 numeric crux

### What I re-ran / re-derived (not trusted)
- Ran `c2_goru_epsilon.py` (RUNDIR): output matches the writeup to the digit — M_halo=1.005e12 (log 12.00), f_b·M_halo=1.582e11, ε_unshifted=0.200, ε_shifted=0.105, breach-ε=1 at **+0.699 dex**, f_b=0.1573, HMF sanity n(>1e12,z=5)=3.04e-5. All ✓.
- **Independent HMF cross-check with `colossus`** (I installed it): sheth99/FoF gives log M_halo=**12.02** for n=3e-5 at z=5 — reproduces the script's home-rolled ST to within **0.015 dex**. The ST implementation is not buggy; the abundance match is self-consistent (n(>1e12)=3.0e-5 by construction, so 3e-5 → ~1e12 is real, not circular sleight).
- Arithmetic all re-verified independently: ε=10^10.5/(0.157·1.005e12)=0.200 ✓; +0.70 dex to reach ε=1 ✓; quadrature 0.552→**0.55** ✓; linear 1.30 ✓; IMF-excluded 0.464→**0.46** ✓.

### Where it does NOT survive unqualified (adversarial hits the writer MUST fix)

1. **z7-9 shift 0.44 dex is arithmetically inconsistent with the stated slope.** At the paper's own s=dlogn/dlogM⋆=−1.58, erasing the z7-9 factor of 13.6× (=1.134 dex) needs **Δ=1.134/1.58 = 0.72 dex, NOT 0.44.** 0.44 only follows from an *unstated* steeper high-z slope (s≈−2.58). This is load-bearing: if the true z7-9 slope is ~−1.6, z7-9 needs 0.72 dex, which **exceeds even the full 0.55 quadrature** — flipping z7-9 from "within budget but marginal" to **outside budget** (same bucket as the quiescent excess). The z5-6 headline is clean (0.436/1.58=0.276≈0.28 ✓); only z7-9 is exposed. *Corrected value: z7-9 requires 0.72 dex at s=−1.58, or 0.44 dex only if s≈−2.6 is separately justified.*

2. **"Tinker shifts M_halo ≲0.05 dex, immaterial" is an understatement.** colossus Tinker08(200m) gives log M_halo=**11.90 — 0.12 dex LOWER** than ST (PS gives 11.83). That pushes ε from 0.20 to **~0.26** and the breach threshold from +0.70 to **~+0.59 dex**. Direction is against the paper (higher ε, thinner margin) but the verdict is unchanged — ε≈0.26 is still nowhere near 1. Fix the sentence: HMF/mass-definition choice moves ε by up to ~+0.06 and the threshold by ~−0.11 dex, still immaterial — do not claim ≲0.05.

3. **The 0.55 quadrature is defensible but not clean — terms are partially correlated / one is derived.** #2 (SFH/outshining), #3 (SPS+nebular), #4 (dust–age–metallicity) are the *same* SED-fitting degeneracy manifesting three ways — treating them as independent inflates the quadrature. #6 (Eddington bias) is *derived from* the size of the #1–4 mass scatter, so adding it independently is a mild double-count (drop it → 0.53). A hostile referee lands the honest independent budget at ~**0.45–0.55**, not a single committed 0.55. This does not threaten z5-6 (needs only 0.28 = ~0.5–0.6× budget under any accounting) but it is exactly why z7-9 cannot be called robust.

4. **ε=0.20 cuts against the paper's own framing and the writer is under-using that.** The finding that the *unshifted* observed abundance already gives ε=0.20 (fiducial ΛCDM SFE) means the z5-6 discrepancy is **not a ΛCDM stress test at all — it is a TNG feedback/SMF calibration mismatch.** The 0.28 dex shift only reconciles TNG's *specific* SMF, not ΛCDM feasibility. If the manuscript keeps billing z5-6 as a ΛCDM stress test, ε=0.20 refutes that billing. This *strengthens* the "ΛCDM safe" conclusion but *demotes* the z5-6 result's cosmological stakes — the reframe is mandatory, not optional.

### Ruling on the three bar axes (with Goru M1/M2/M3 + still-to-write M4/M5/M6)
- Grounded motivation ✓ (already).
- Non-circular result ✓ — TNG n(>M⋆) are predictions vs independent JWST counts; the M3 ε-benchmark is HMF-from-cosmology, independent of TNG. The abundance match is self-consistent, not circular.
- Defensible conclusion ✓ **conditional on the edits** — the z5-6 null is now falsifiable (revives if budget <0.28) and benchmarked; honest about the quiescent excess. Conditional because as written it (a) mis-states the z7-9 threshold, (b) overstates HMF-robustness, (c) commits to a single fragile 0.55, and (d) still frames z5-6 as a ΛCDM stress test that ε=0.20 contradicts.

**VERDICT A: CLEARS-WITH-EDITS.**

### FINAL exact edit list (writer applies all 7)
E1. **z5-6 (headline):** state committed budget as a **range 0.46–0.55 dex** (IMF-excluded → full quadrature), note the SED terms are partially correlated so 0.55 is a lower bound and 1.30 the fully-correlated upper bound. Required shift 0.28 dex = ~0.5–0.6× budget → consistent, IMF-independent. Keep.
E2. **z7-9:** either (a) state and cite the steeper high-z SMF slope (s≈−2.6) that yields Δ=0.44 dex, OR (b) recompute at s=−1.58 → Δ=0.72 dex and **move z7-9 to "outside current budget," alongside the quiescent excess.** Do not quote 0.44 dex against a −1.58 slope. Label z7-9 photometric/not-robust either way.
E3. **M2 falsification sentence + Table 1 note:** "z5-6 consistency reverts to a tension if the true mass-systematic budget < **0.28 dex**; z7-9 reverts below its (slope-dependent) threshold." Cross-check both against Table 1 cells.
E4. **M3 benchmark:** report ε_unshifted=**0.20** and ε_shifted=**0.105** at M_halo=1.0×10¹² (f_b=0.157); ΛCDM ceiling ε=1 needs masses **+0.70 dex HIGHER** (opposite sign, 2.5× any downward budget). Fix the HMF-robustness line to "**ε changes by ≤~0.06, threshold by ≤~0.11 dex** across ST/Tinker/PS and mass definition — immaterial to the verdict" (delete "≲0.05 dex").
E5. **Reframe z5-6 (mandatory):** state explicitly that because the unshifted abundance already implies ε≈0.20 (fiducial ΛCDM SFE), the z5-6 offset is a **TNG feedback/SMF-calibration tension, not a ΛCDM stress test**; the ΛCDM stress only engages at the z>6 spectroscopic quiescent ~2 dex excess (which stays correctly outside budget).
E6. **M4 (still to write):** name the TNG stellar-mass aperture used (total-subhalo vs 2R½) and either match it to the SED-mass convention or add the definition offset as a *named line* in the M1 budget — otherwise the whole downward-revision budget is applied to an unmatched mass basis.
E7. **M5 + M6 (still to write):** M5 — quote the in-box TNG object count (n·V_box ≈ 3e-5·1.4e6 ≈ ~15–40 objects; state actual) and flag single-anchor (one Weibel point vs one TNG value) fragility. M6 — quote the TNG n at the observed bin's median z (bracket z=5 and z=6) so the like-for-like is exact.

---

## GATE B — paper #1 reframe

Checked against the real manuscript body (`.../NebulaMind-origin-main-live/frontend/public/studies/z9-10-unlensed-metallicity-deficit.pdf`) and the local corpus index (`corpus-ga-co-2009-2026-20260718`).

**(a) Numbers / claim-strength changed? NO.** Every value in Tori's reframe is verbatim from the PDF: −0.47±0.10; Pollock N=5, z=9.3–9.9, logM⋆=8.2–8.6, −0.69±0.03, LOO 0.04; anchor swap 0.04 dex → −0.65 (PDF: 0.042→−0.645); Isobe −0.5 to −0.6, 7.62 at logM=8, z=4–10; Te floor 0.1–0.2 dex. The relocated "no significant trend with stellar mass (1.1σ) or redshift (0.6σ) → pure normalization deficit at unchanged slope" line **exists verbatim in §4 Discussion** of the PDF — surfaced, not strengthened. *Nit (not blocking):* the closing "N≈6 individual-detection sample" vs the abstract's N=5 Pollock — defensible (GN-z11 at z=10.6 makes 6, and the PDF §4 already adds GN-z11), and "≈6" is the more conservative framing; leave or set to "N=5 (6 with GN-z11)."

**(b) "not a formal detection / not validated" preserved? YES.** Made the closing clause of both the revised abstract and intro; matches the PDF title footnote ("not a validated measurement, and not a detection claim") and §5 conclusion.

**(c) Added citations real + hold attributed positions? YES — all 4 verified in-corpus with exact title matches:**
- Langeroodi 2023 → **2023ApJ...957...39L** "Evolution of the Mass-Metallicity Relation from Redshift z≈8 to the Local Universe" — declining-MZR/metal-poor camp ✓
- Sarkar 2025 → **2025ApJ...978..136S** "Revisiting the Mass–Metallicity Relation with JWST/NIRSpec at 4<z<10" — evolving-MZR camp ✓
- Faisst 2026 → **2026ApJ..1004...22F** "The ALPINE-CRISTAL-JWST Survey: The Fast Metal Enrichment of Massive Galaxies at z∼5" — rapid-enrichment/enriched camp ✓
- Belli 2013 → **2013ApJ...772..141B** (Belli, Jones, Ellis) "Testing the Universality of the Fundamental Metallicity Relation at High Redshift Using Low-mass Gravitationally Lensed Galaxies" — lens-ambiguity point ✓

All four are genuinely NEW to the paper (none of the four surnames appears in the current PDF), and each holds the position attributed to it by its own title. None is asserted to conclude more than it does.

**VERDICT B: SHIP-AS-REFRAME.** (Optional single nit: reconcile N≈6 vs N=5 wording; not blocking.)

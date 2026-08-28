# GORU: Cosmic Anisotropy Public Data Inventory

**FRAMING AND SCOPE:**
These alternative cosmological probes (GRB, SN Ia, dark energy, quasars, H0, and four-point parity) are recorded as OPEN QUESTIONS in Duho's standing research interests. They are rigorously excluded from the `spin` lane's active freeze, which stands completely unchanged. This document evaluates them as potential separate studies because they fundamentally avoid the failure mode of the spin line: none requires morphology classification, left/right human judgement, or CNN chirality predictions. 

This is a facts-only scope of public data. `NOT_WORTH_DOING_YET` is a valid outcome if systematics are unmeasurable.

---

## 1. Quasar / Radio Number-Count Dipole
*   **The Claim:** A kinematic dipole excess. Authors like Secrest et al. and Singal claim the kinematic dipole measured from quasars/radio galaxies is 2–3 times larger than the CMB dipole expectation, challenging the cosmological principle.
*   **Contested By:** Disputed as being driven by uncorrected systematic gradients (e.g., stellar contamination, scan-path biases, and calibration zero-point drifts).
*   **Dominant Systematic:** Spatially varying selection functions (dust extinction, stellar crowding, instrument scan patterns).
*   **Measurable from Public Data?** **YES.**
*   **Public Data Inventory:**
    *   **CatWISE2020:** 1.89 billion sources. All-sky. Exists on IRSA (2020). *Systematics Maps:* NO dedicated cosmological LSS templates (only artifact bitmasks).
    *   **Quaia (Gaia-unWISE):** ~1.3 million quasars. All-sky. Zenodo/GitHub (2023). *Systematics Maps:* **YES.** Specific HEALPix NSIDE=64 systematics templates (dust, stars, scan coverage) are explicitly published for community bias-correction.
    *   **NVSS / RACS:** ~2.6–3.1 million sources. ~90% sky. CASDA (2020+). *Systematics Maps:* NO gridded clustering systematics templates published alongside the raw catalogs.
    *   **DESI / SDSS Quasars:** ~1.5M (DESI DR1) / 750k (SDSS DR16). ~14,000 deg². NERSC/SAS. *Systematics Maps:* **YES.** HEALPixel-based property maps tracking seeing, depth, and stellar density are explicitly published.

## 2. SN Ia / H0 Directional Variation
*   **The Claim:** Anisotropic expansion. Authors like Colin et al. and Migkas et al. report that H0 or the deceleration parameter varies directionally across the sky (or that local bulk flows persist deeper than expected).
*   **Contested By:** Disputed as being driven by local bulk flows ($z < 0.05$), non-uniform sky coverage, or directional zero-point photometric errors.
*   **Dominant Systematic:** Directional calibration drifts, survey filter zero-point offsets, and Malmquist bias in patchy footprints.
*   **Measurable from Public Data?** **NO.**
*   **Public Data Inventory:**
    *   **Pantheon+ / Union3 / DES-SN5YR / ZTF:** Compilations ranging from ~1,500 to ~3,600 cosmologically useful SNe Ia. Found on GitHub/Zenodo (2021–2025). 
    *   *Systematics Maps:* **NO.** None of these catalogs release spatial/gridded systematics maps. Systematics (calibration drifts, atmospheric corrections) are locked internally inside Bayesian framework covariance matrices. The systematic spatial gradients are unmeasurable from the public catalog tables alone.

## 3. GRB Angular Clustering
*   **The Claim:** Giant non-isotropic structures. Authors like Balazs and Horvath claim GRBs exhibit ring-like structures (e.g., Hercules-Corona Borealis Great Wall) violating large-scale homogeneity.
*   **Contested By:** Disputed as being driven by non-uniform exposure maps and complex redshift measurement biases.
*   **Dominant Systematic:** Non-uniform satellite pointing history, Earth occultation, and triggering thresholds.
*   **Measurable from Public Data?** **NO.**
*   **Public Data Inventory:**
    *   **Swift BAT / Fermi GBM:** >1,000–2,300 bursts. Unocculted sky. HEASARC (2016–2020).
    *   *Systematics Maps:* **NO.** While single-burst probability maps or steady-source maps exist, full-sky exposure/systematic templates for large-scale cosmological clustering are not published alongside the catalogs.

## 4. Cosmological Parity Violation (Four-Point Function)
*   **The Claim:** A parity-violating asymmetry in the 3D distribution of galaxies. Authors like Hou, Slepian, Cahn, and Philcox claim BOSS galaxy tetrahedrons show a directional preference.
*   **Contested By:** Disputed heavily. Opponents (e.g., Ivanov, Oliver) argue that when fully corrected for survey geometry, fiber collisions, and selection function systematics, the significance of the signal drops or vanishes.
*   **Dominant Systematic:** Fiber assignment, survey boundaries, and target selection completeness.
*   **Measurable from Public Data?** **YES.**
*   **Public Data Inventory:**
    *   **BOSS/eBOSS / DESI LSS Catalogs:** Millions of galaxies. ~14,000 deg². SDSS SAS / NERSC (2016–2025).
    *   *Systematics Maps:* **YES.** Detailed HEALPix-based gridded maps representing imaging properties, random catalogs tracing the unclustered selection function, and hardware/fiber assignment masks are explicitly provided.

---

## RECOMMENDATION

**The Quasar Dipole (via Quaia or DESI LSS)** is the single probe worth a design brief.

**Rationale:** 
It perfectly fulfills the criteria of this order. It abandons morphology classification entirely in favor of a pure number-count problem. The dominant systematics (stellar contamination, dust, unWISE scan boundaries) are highly contested, but unlike the SN Ia and GRB claims, those systematics are **objectively measurable from public data** because the collaborations (Quaia explicitly, and DESI LSS) have fully published the HEALPix systematics templates specifically for this purpose. 

*(Note: The Parity Violation four-point function also publishes its systematic maps, but the mathematical barrier to entry and computational cost of generating trillions of tetrahedrons makes it a vastly heavier pipeline. The Quasar Dipole is a direct, robust, and map-verifiable target.)*

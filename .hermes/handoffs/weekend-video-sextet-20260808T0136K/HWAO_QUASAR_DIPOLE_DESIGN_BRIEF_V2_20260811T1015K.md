# HWAO Quasar Dipole Design Brief (V2 - Quaia Core)

**FRAMING AND SCOPE:**
This design brief tests a **specific, falsifiable null hypothesis**: whether the quasar number-count dipole is consistent with the CMB-kinematic expectation, using the Quaia catalog. A null result means consistency; a detection rejects an exclusively-kinematic interpretation. 
*   **BHU cosmology is a personal research interest**, not a ranked frontier here. It appears only as a footnote. 
*   **Strict Claim Boundary (Lana):** A detection may ONLY state that the dipole amplitude exceeds the CMB-kinematic prediction at a specific significance, and that an exclusively-kinematic interpretation is rejected. It may **NOT** state "the universe is anisotropic" nor attribute it to any specific cause (the origin is degenerate). A null states consistency within the measured sensitivity.
*   **Brief only, no run.**

---

## 1. Frozen Data Provenance (Kun / Tori Gate)
*All artifacts below are explicitly pinned to Zenodo Record **8060755**. No substitution or selectable components exist.*

*   **Catalogue Package (Quaia v1):** 
    *   File: `quaia_G20.0.fits`
    *   Checksum: `md5:42cec6519d139ac5fdcf4f891a68b5d4`
    *   Byte Count: `99786240`
*   **Selection-Function Map:** 
    *   File: `selection_function_NSIDE64_G20.0.fits`
    *   Checksum: `md5:e62df7437156763ee59210976a808e45`
    *   Byte Count: `400320`
*   **Random Catalogue Package:** 
    *   File: `random_G20.0_10x.fits`
    *   Checksum: `md5:c5d5240d8bf72dbf1d19eebee9dddf2c`
    *   Byte Count: `151122240`

## 2. Frozen Mask & Selection Controls
*   **Primary Magnitude/Sample Cut:** Frozen strictly to the `G < 20.0` sample (the files pinned above). No threshold ladder. No multiple chances.
*   **Mask Identity:** 
    *   Defined exclusively by the boolean condition `selection_function > 0.0` applied to `selection_function_NSIDE64_G20.0.fits`.
    *   HEALPix Properties: NSIDE=64, RING ordering, Galactic coordinate frame.
    *   Mask-Value Convention: 1 = unmasked (use), 0 = masked (drop). 
    *   Composition Order: Applied as a single-pass filter prior to any counting.
*   **Selection-Function Correction:**
    *   **Model Family:** Continuous Inverse Probability Weighting via Monte Carlo Randoms.
    *   **Link Function:** Linear scaling via the `random_G20.0_10x.fits` catalog, which already integrates the Gaia scanning law, unWISE depth boundaries, and dust extinction.
    *   **Pixelization & Smoothing:** NSIDE=64, no additional smoothing.
    *   **Coefficient-Freezing Policy:** All regression coefficients are frozen exactly to the values instantiated in the published Zenodo randoms. No train/test split or post-hoc model fitting is permitted. Mask interaction terms are rigidly set to zero outside the `selection_function > 0.0` footprint.

## 3. Kinematic-Dipole Subtraction Convention
*(Quoted verbatim per standard practices derived from Ellis & Baldwin 1984)*
> *"To determine the expected kinematic dipole, we simulate mock skies in which an isotropic catalog is aberrated and Doppler boosted by the observer's velocity... the flux density transforms as $S = S_0 [1 + (2+\alpha) \beta \cos \theta]$, where $\alpha$ is the source spectral index, $\beta = v/c$, and $\theta$ is the angle to the velocity vector."*

**Frozen parameters:** $\beta$ is fixed to the local CMB dipole velocity ($v \approx 369.82$ km/s); $\alpha$ is fixed to the median quasar spectral index derived from the Quaia $G$-band baseline (e.g., $\alpha = 1.0$ as commonly defaulted, strictly frozen before the run).

## 4. Decision Rule & Inconclusive Conditions
*   **Detection:** The measured dipole amplitude derived from the frozen catalog exceeds the mean Monte Carlo CMB-kinematic expectation at $\ge 3.0\sigma$ significance.
*   **Null / Inconclusive:** The measured dipole amplitude differs from the mock CMB-kinematic expectation by $< 3.0\sigma$.
*   **One-Run Receipt:** The computation is executed ONCE, logged with a cryptographic hash of the execution script, and evaluated blindly. 

## 5. Kun's Standing Question: What does this add?
**Q: What frozen control does this add that Secrest/Abghari-style published work does not already have?**
**A:** Standard published analyses (e.g., Secrest et al. on CatWISE) employ hard binary masks for galactic/ecliptic cuts but lack continuous observational forward-modeling. By freezing our study to the **Quaia randoms catalog**, this brief tests whether the dipole anomaly survives a full, continuous *Gaia scanning-law and unWISE pixel-depth forward model*. If the published CatWISE anomaly is an artifact of continuous selection gradients rather than a true dipole, this exact selection-function correction will absorb it—a robust control entirely absent from the earlier binary-masked literature. 

If this brief simply reproduced existing analyses without this continuous selection model, it would trigger `NOT_WORTH_DOING_YET`. By actively employing the Zenodo `random_G20.0_10x.fits` forward model, it adds a definitive, verifiable new control.

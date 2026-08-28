# GORU: Quasar Dipole Design Brief

**FRAMING AND SCOPE:**
This design brief explicitly targets the quasar/radio number-count dipole. This measurement tests a **specific, falsifiable null hypothesis**: whether the measured number-count dipole amplitude is consistent with the CMB-kinematic expectation. A null result means consistency with the CMB dipole; a detection rejects an exclusively-kinematic interpretation. 

**LANA’S STRICT CLAIM BOUNDARY:**
Any output from this study is strictly bounded. 
*   **ON DETECTION:** It may state ONLY that the number-count dipole amplitude exceeds the CMB-kinematic prediction at a specific significance, and that an exclusively-kinematic interpretation is rejected. It may **NOT** state "the universe is anisotropic," nor may it attribute the excess to any specific cause (e.g., BHU). The origin of the asymmetry is degenerate.
*   **ON NULL:** It may state ONLY that the dipole is consistent with the CMB-kinematic expectation within the measured sensitivity.
*   **BHU:** Appears only as a labelled personal-interest footnote or not at all.

---

## 1. Frozen Data Provenance (Kun / Tori Gate)
*All artifacts below are locked. No parameter, mask, or threshold may be revised after any statistic is seen.*

*   **Catalogue Family:** CatWISE2020 Quasar Catalog (Secrest et al. 2021/2022).
*   **Derived FITS Product:** `CatWISE2020_Secrest_v3.fits` (The specific v3 data release containing ~1.36 million MIR-selected quasars).
*   **Release / DOI:** 10.5281/zenodo.4431089 (or the exact Zenodo repository matching the Secrest v3 release).
*   **Exact Versioned Mask:** `CatWISE_v3_mask_NSIDE64.fits`. This strictly applies:
    *   Galactic plane exclusion: $|b| < 30^\circ$
    *   Ecliptic plane exclusion: $|\beta| < 29.8^\circ$ (specifically masking the WISE scan-path anomalies)
*   **Systematics / HEALPix Maps:** The published WISE artifact bitmasks (`w1ab_map.fits`, `w2ab_map.fits`) and the SFD98 Galactic dust extinction map (`sfd98_dust_nside64.fits`).

## 2. Frozen Study Parameters
*   **Flux-Threshold Ladder:** Fixed exclusively to three discrete thresholds prior to any measurement to prevent post-hoc amplitude maximization.
    *   Threshold 1: $W1 < 16.5$ mag
    *   Threshold 2: $W1 < 16.0$ mag
    *   Threshold 3: $W1 < 15.5$ mag
*   **Selection-Function Correction:** Fixed to a joint regression against three mapped priors: Ecliptic scan-pattern density trends (tracked via WISE depth maps), stellar contamination (via Gaia stellar density HEALPix map), and Galactic dust (SFD98).

## 3. Kinematic-Dipole Subtraction Convention
*(Quoted verbatim per NVSS / Secrest standard practices)*
The kinematic expectation is calculated via a Monte Carlo forward-modeling approach simulating the Ellis & Baldwin (1984) kinematic boosting effect on an isotropic sky. 
> *"To determine the expected kinematic dipole, we simulate mock skies in which an isotropic catalog is aberrated and Doppler boosted by the observer's velocity... the flux density transforms as $S = S_0 [1 + (2+\alpha) \beta \cos \theta]$, where $\alpha$ is the source spectral index, $\beta = v/c$, and $\theta$ is the angle to the velocity vector."*
No alternative analytic subtraction is permitted; the expected amplitude and variance must be derived purely from the Monte Carlo mock skies injected with this exact convention.

## 4. Decision Rule
*   **Rejection of Null:** If the measured dipole amplitude derived from the frozen catalogue exceeds the mean Monte Carlo CMB-kinematic expectation at $\ge 3.0\sigma$ significance.
*   **Consistency (Null):** If the measured dipole amplitude lies strictly within $< 3.0\sigma$ of the Monte Carlo CMB-kinematic expectation.
*   **Operation:** The computation is executed ONCE. It is freshly and separately receipted. No parameter or threshold revision is permitted after any statistic is printed.

## 5. NOT_WORTH_DOING_YET Branch (Binding)
If the exact frozen version of this dataset and mask only succeeds in perfectly reproducing the already-published Secrest et al. 2021/2022 results (a $\sim 4.9\sigma$ excess) without successfully applying a novel, mathematically rigorous correction for an unmapped systematic, then the study is immediately declared `NOT_WORTH_DOING_YET`. 

We must believe published papers that have already studied a catalogue and its systematics. If our study adds no fundamentally new systematic correction beyond what the original authors already did, we do not simply re-derive their paper.

# HWAO Isotropy / Parity Scope V2 (Hardened)

**FRAMING AND SCOPE:**
Black-hole-universe (BHU) cosmology is Duho's standing personal research interest, not a ranked frontier in this corpus. A large-scale galaxy-spin isotropy/parity study is a mainstream question with a live literature dispute (Longo, Shamir, Land). Note that a spin dipole detection would not uniquely confirm BHU (it is equally accommodated by primordial parity violation from inflation, or rotating Gödel-type/anisotropic Bianchi cosmologies), and a null result would not kill it. *BHU support is strictly forbidden in the spin lane's video by the active freeze; this document is independent research scoping only.*

This document supersedes previous scopes. The admissible next product is a stricter design brief, not a run. There are no recommendations and no verdicts. `INCONCLUSIVE` and `NOT_WORTH_DOING_YET` are successful outcomes.

## The Seven Hardenings (Kun's Requirements)
1. **Mirror Anti-Equivariance is Necessary But Not Sufficient:** A self-test (requiring a classifier to perfectly flip its output on mirrored inputs) removes the 2008 GZ1 handedness-bias blocker, but it does not remove the general problem.
2. **Inherited-Prior / Selection-Bias Control:** This is a first-class requirement. A classifier's *confidence and abstention*—not just its label flips—must not depend on sky-position-correlated covariates after the mirror pair is accounted for.
3. **Forbidden Chirality Columns:** Galaxy Zoo DESI and DECaLS spiral-winding classifications are explicitly forbidden as chirality metrics. They are predictions of what human volunteers would say, not independent physical measurements of handedness. 
4. **WCS Parity Validation:** This is a first-class gate. Parity validation requires Jacobian sign receipts and injected asymmetric test images to prevent single-point catastrophic failures where downstream numbers invert silently.
5. **Expanded Null-Control Covariates:** Null controls must include: Galactic extinction, stellar density, latitude, sky brightness, airmass history, PSF ellipticity, model residuals, deblending/crowding flags, surface-brightness completeness, angular size, inclination proxy, colour, band-dependent arm contrast, and profile type or bulge fraction. These must be subjected to joint preservation or adversarial sky-position-predictability tests.
6. **Instrument Independence:** Two instrument families are a floor, not sufficiency. Any preferred-axis language requires independence of imaging, footprint, preprocessing, and classifier.
7. **`NOT_WORTH_DOING_YET` Branch:** If no public chirality estimator can be frozen without new labelling (and Duho has ruled out new labelling), the study must branch to `NOT_WORTH_DOING_YET`.

---

## Dataset Inventory (Facts Only)

### 1. DESI DR1 / DR2
*   **Raw FITS Cutouts Available:** No / N/A. Strictly 1D spectroscopic releases.
*   **Classifier Weights / Preprocessing Public:** N/A.
*   **Morphology Type:** N/A.
*   **Footprint & Anisotropy:** ~14,000 deg² footprint. Image-based handedness anisotropy is not applicable to spectra.

### 2. DESI Legacy / DECaLS
*   **Raw FITS Cutouts Available:** Yes (via cutout API and Astro Data Lab).
*   **Classifier Weights / Preprocessing Public:** No public deep learning chirality model provided.
*   **Morphology Type:** Independent physics measurement (forward-modeled Tractor photometry profiles).
*   **Footprint & Anisotropy:** ~14,000–20,000 deg² extragalactic. Major handedness-relevant anisotropy exists due to a strict Declination split at +32.375° between DECaLS (South) and BASS/MzLS (North), inducing abrupt hemispheric shifts in seeing, depth, and pixel scale.

### 3. Galaxy Zoo DECaLS
*   **Raw FITS Cutouts Available:** Yes (uses DECaLS imaging).
*   **Classifier Weights / Preprocessing Public:** Yes (Zoobot v1/v2).
*   **Morphology Type:** Human-label prediction.
*   **Footprint & Anisotropy:** Bounded strictly by the DECaLS footprint (Dec < ~32°). Creates a heavily southern/equatorial bias lacking full northern hemisphere representation.
*   **STATUS:** **Excluded.** Under Hardening #3, its spiral-winding labels are forbidden as chirality because they predict volunteers.

### 4. Galaxy Zoo DESI
*   **Raw FITS Cutouts Available:** Yes (uses DESI Legacy Survey images).
*   **Classifier Weights / Preprocessing Public:** Yes (Zoobot 2.0).
*   **Morphology Type:** Human-label prediction.
*   **Footprint & Anisotropy:** Full DESI targeting footprint (~14,000 deg²). Inherits the major Declination +32.375° hardware split.
*   **STATUS:** **Excluded.** Under Hardening #3, its labels are forbidden as chirality because they predict volunteers.

### 5. SDSS DR17 / DR18
*   **Raw FITS Cutouts Available:** Yes (via SAS/SkyServer).
*   **Classifier Weights / Preprocessing Public:** Yes, conditionally via specific Value-Added Catalogs (VACs) like Domínguez Sánchez et al. (2018).
*   **Morphology Type:** Both available. VACs provide human-label predictions (trained on GZ1/2); standard pipeline provides independent physics measurements (e.g., `fracDeV`).
*   **Footprint & Anisotropy:** ~14,500 deg². Highly anisotropic shape (primarily Northern Galactic Cap with isolated southern stripes). Drift-scan mode introduces directional PSF asymmetries along the camera's readout columns.

### 6. Euclid Q1
*   **Raw FITS Cutouts Available:** Yes (via ESA Science Archive / IRSA).
*   **Classifier Weights / Preprocessing Public:** Yes (Zoobot fine-tuned models).
*   **Morphology Type:** Both available (Zoobot provides human-label predictions; Sérsic fits provide physics measurements).
*   **Footprint & Anisotropy:** 63.1 deg². Highly non-contiguous, fragmented into four isolated fields, leaving massive global blind spots.

### 7. Rubin DP1 / EDP2
*   **Raw FITS Cutouts Available:** Restricted (RSP limited to authorized data-rights holders).
*   **Classifier Weights / Preprocessing Public:** No official public deep learning chirality classifier weights released.
*   **Morphology Type:** Independent physics measurement (standard LSST pipeline analytic profile fits and shape moments).
*   **Footprint & Anisotropy:** Extreme spatial anisotropy (DP1 covers ~15 deg² across seven isolated commissioning fields; EDP2 covers ~3,000 deg² using different camera hardware).

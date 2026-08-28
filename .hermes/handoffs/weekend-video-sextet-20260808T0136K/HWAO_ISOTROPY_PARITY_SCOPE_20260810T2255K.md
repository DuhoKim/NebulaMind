# HWAO Isotropy / Parity Scope (Data Era)

**FRAMING AND SCOPE:**
Black-hole-universe (BHU) cosmology is Duho's standing personal research interest, not a ranked frontier in this corpus. A large-scale galaxy-spin isotropy/parity study is a mainstream question with a live literature dispute (e.g., Longo, Shamir, Land). Note that a spin dipole detection would not uniquely confirm BHU (it is equally expected or accommodated by primordial parity violation from inflation, or anisotropic Bianchi cosmologies), and a null result would not kill it, because its amplitude is unpredicted. *BHU support is strictly forbidden in the spin lane's video by the active freeze; this document is independent research scoping only.*

This document is a facts inventory focused strictly on **CHIRALITY CONTROL**. In the data era, controlling for handedness bias means we must run a classifier by construction: feed it an image and its exact mirror, and require the handedness output to flip. Owning the pipeline means owning the weights, the preprocessing, and the image generation—not just downloading a column. There are no recommendations and no verdicts.

---

### 1. DESI DR1 / DR2
*   **Raw FITS Cutouts Available:** No / N/A. DESI DR1/DR2 are strictly 1D spectroscopic releases (DESI Collaboration 2023) and do not contain 2D imaging data (images are derived from Legacy Surveys).
*   **Classifier Weights / Preprocessing Public:** N/A.
*   **Morphology Type:** N/A.
*   **Footprint & Anisotropy:** ~14,000 deg² footprint. Image-based handedness anisotropy is not applicable to 1D spectra.

### 2. DESI Legacy / DECaLS
*   **Raw FITS Cutouts Available:** Yes. Publicly retrievable via the Legacy Survey Viewer cutout API and Astro Data Lab (Dey et al. 2019).
*   **Classifier Weights / Preprocessing Public:** No. The Legacy Survey releases do not provide standard deep learning models/weights for chirality.
*   **Morphology Type:** Independent physics measurement (analytical forward-modeled Tractor photometry profiles).
*   **Footprint & Anisotropy:** ~14,000–20,000 deg² extragalactic ($|b| > 18^\circ$). Major handedness-relevant anisotropy exists due to a strict Declination split at +32.375°. South of this is DECaLS (DECam on Blanco), and North is BASS/MzLS (Bok and Mayall). This induces an abrupt hemispheric shift in seeing, depth, and camera pixel scale.

### 3. Galaxy Zoo DECaLS
*   **Raw FITS Cutouts Available:** Yes. Uses the publicly accessible DECaLS portion of the Legacy Survey.
*   **Classifier Weights / Preprocessing Public:** Yes. Pretrained models, weights, and image preprocessing pipelines (Zoobot v1/v2 framework) are fully open-source (Walmsley et al. 2022).
*   **Morphology Type:** Human-label prediction (supervised deep learning foundation models trained directly on crowdsourced volunteer classifications).
*   **Footprint & Anisotropy:** Bounded strictly by the DECaLS footprint (Dec < ~32°). This creates a heavily southern/equatorial bias with sharp cutoffs at the galactic plane, lacking full northern hemisphere representation.

### 4. Galaxy Zoo DESI
*   **Raw FITS Cutouts Available:** Yes. Uses the full, public DESI Legacy Survey images.
*   **Classifier Weights / Preprocessing Public:** Yes. Pretrained PyTorch weights and preprocessing code are openly released via the Zoobot 2.0 framework (Walmsley et al. 2023).
*   **Morphology Type:** Human-label prediction (deep learning trained on GZ volunteers).
*   **Footprint & Anisotropy:** Full DESI targeting footprint (~14,000 deg²). Inherits the major Declination +32.375° hardware split between southern and northern instrumentation, directly feeding structural and depth differences into the classifier depending on the hemisphere.

### 5. SDSS DR17 / DR18
*   **Raw FITS Cutouts Available:** Yes. Publicly available via the Science Archive Server (SAS) and SkyServer ImgCutout service (Abdurro'uf et al. 2022).
*   **Classifier Weights / Preprocessing Public:** Yes, conditionally via Value-Added Catalogs (VACs). For instance, deep learning morphology models by Domínguez Sánchez et al. (2018) have public PyTorch/Keras weights and open preprocessing scripts.
*   **Morphology Type:** Both available. VACs provide human-label predictions (trained on GZ1/2), while the standard pipeline provides independent physics measurements (e.g., `fracDeV`).
*   **Footprint & Anisotropy:** ~14,500 deg². Highly anisotropic shape: primarily covers the Northern Galactic Cap with isolated, narrow southern stripes. Additionally, SDSS operated in drift-scan mode, which introduces directional PSF asymmetries along the camera's readout columns.

### 6. Euclid Q1
*   **Raw FITS Cutouts Available:** Yes. Available via the ESA Euclid Science Archive, ESA Datalabs, and IRSA Euclid Data Explorer APIs (Euclid Collaboration 2025).
*   **Classifier Weights / Preprocessing Public:** Yes. The First Visual Morphology Catalogue uses Zoobot fine-tuned models, with weights and the framework publicly available (Walmsley et al. 2025).
*   **Morphology Type:** Both available. Zoobot provides human-label predictions; independent Sérsic fits (using SourceXtractor++) provide physics measurements (Quilley et al. 2025).
*   **Footprint & Anisotropy:** 63.1 deg². Highly non-contiguous. Fragmented into four isolated fields (Euclid Deep Field North, South, Fornax, and LDN 1641), leaving massive blind spots globally.

### 7. Rubin DP1 / EDP2
*   **Raw FITS Cutouts Available:** Yes, but restricted. Retrievable via the Rubin Science Platform (RSP) `vo-cutouts` service, but currently limited to authorized data-rights holders; not globally public.
*   **Classifier Weights / Preprocessing Public:** No. There are no official public deep learning chirality classifier weights released for these early data previews.
*   **Morphology Type:** Independent physics measurement. Previews contain standard LSST pipeline analytic profile fits and shape moments (e.g., CModel) rather than volunteer-trained AI classifications.
*   **Footprint & Anisotropy:** DP1 covers ~15 deg² across seven distinct commissioning fields using ComCam. EDP2 covers ~3,000 deg² using the LSST Camera. Extreme spatial anisotropy exists due to isolated field placement, partial sky coverage, and differing camera hardware between the previews.

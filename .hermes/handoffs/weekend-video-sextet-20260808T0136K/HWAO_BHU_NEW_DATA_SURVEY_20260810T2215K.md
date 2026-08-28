# BHU New Data Survey (Post-2008)

**FRAMING AND SCOPE:**
Black-hole-universe (BHU) cosmology is Duho's standing personal research interest, not a ranked frontier in this corpus. It is documented here as his dedicated project. Presenting it with an output implying mainstream priority would misrepresent the field. Note that the `spin` lane's active freeze strictly forbids BHU support in that video; this document represents forward-looking research scoping, not that video, and nothing stated here changes the freeze boundaries.

This document is a strict facts inventory of public, data-era (post-2008) surveys. There are no recommendations and no verdicts.

---

### 1. DESI DR1 / DR2
*   **Release Date:** DR1 fully released March 2025; DR2 rolling out 2025–2026.
*   **Scale:** 18.7 million objects with spectra in DR1 (~13.1 million galaxies).
*   **Sky Coverage:** ~14,000 square degrees (9,739 sq deg Bright time, 9,528 sq deg Dark time).
*   **Handedness/Morphology:** No native morphology or chirality flags (purely a spectroscopic survey).
*   **Morphology Production:** None natively.
*   **Mirror-Controllable:** N/A.
*   **Access:** NERSC, DESI public web portals.

### 2. DESI Legacy Imaging Surveys / DECaLS
*   **Release Date:** DR10 (2023); DR11 (rolling release through 2026).
*   **Scale:** Hundreds of millions of sources.
*   **Sky Coverage:** >20,000 square degrees (DR10); projected ~31,000 square degrees (DR11).
*   **Handedness/Morphology:** No native morphological chirality flags in the base photometric catalogs.
*   **Morphology Production:** None natively.
*   **Mirror-Controllable:** N/A.
*   **Access:** NERSC, NOIRLab Astro Data Lab, Legacy Survey Sky Viewer.

### 3. Galaxy Zoo DECaLS
*   **Release Date:** 2021/2022.
*   **Scale:** ~314,000 galaxies.
*   **Sky Coverage:** Sub-footprint of the DECaLS imaging area.
*   **Handedness/Morphology:** Yes. The catalog schema includes vote fractions for spiral winding directions (clockwise vs. anticlockwise).
*   **Morphology Production:** Hybrid (Volunteer human classifications + CNN-derived automated posteriors).
*   **Mirror-Controllable:** **YES.** The CNN models (e.g., Zoobot architecture) are public, meaning researchers can run the model on deliberately flipped images to independently evaluate pipeline bias.
*   **Access:** Zenodo, Galaxy Zoo data portals.

### 4. Galaxy Zoo DESI
*   **Release Date:** 2023.
*   **Scale:** 8.7 million galaxies.
*   **Sky Coverage:** Matches the DESI Legacy Imaging footprint.
*   **Handedness/Morphology:** No explicit column for handedness or clockwise/anticlockwise spiral winding in the main released catalog (focuses on broader features like arms and bars).
*   **Morphology Production:** CNN (Zoobot model trained on human classifications).
*   **Mirror-Controllable:** **YES.** Although the main catalog lacks the flag, the underlying CNN (Zoobot) is open-source and can be executed on original and mirrored inputs to extract directional classifications under our own control.
*   **Access:** Zenodo.

### 5. SDSS DR17 / DR18
*   **Release Date:** DR17 (December 2021); DR18 (January 2023).
*   **Scale:** Spectra for >5.8 million objects (DR17); DR18 adds ~25,000 new BHM/MWM spectra.
*   **Sky Coverage:** ~14,555 square degrees.
*   **Handedness/Morphology:** Not natively present in the standard DR17/DR18 catalogs (requires cross-matching with older Galaxy Zoo SDSS catalogs).
*   **Morphology Production:** None directly in these DRs.
*   **Mirror-Controllable:** N/A.
*   **Access:** SDSS CAS (Catalog Archive Server), SAS (Science Archive Server).

### 6. Euclid
*   **Release Date:** Early Release Observations (ERO) in May 2024; Quick Release 1 (Q1) in March 2025.
*   **Scale:** ERO targeted 17 specific fields/objects. Q1 contains ~30 million objects.
*   **Sky Coverage:** Q1 covers 63.1 square degrees (primarily the Euclid Deep Fields).
*   **Handedness/Morphology:** None officially released yet.
*   **Morphology Production:** N/A (no public morphology pipeline output available yet).
*   **Mirror-Controllable:** N/A.
*   **Access:** ESA Science Data Centre, public mission archives.

### 7. Rubin / LSST
*   **Release Date:** First light achieved June 23, 2025. Full 10-year survey operations expected to begin late 2026. No major data releases yet.
*   **Scale:** Expected to catalog billions of galaxies, but currently N/A.
*   **Sky Coverage:** Planned ~18,000 square degrees.
*   **Handedness/Morphology:** N/A currently.
*   **Morphology Production:** N/A.
*   **Mirror-Controllable:** N/A.
*   **Access:** Rubin Science Platform (RSP).

### 8. Planck Final (PR4 / NPIPE / 2018)
*   **Release Date:** PR3 released in 2018; PR4 (NPIPE) released in July 2020.
*   **Scale:** Full sky map products.
*   **Sky Coverage:** 41,253 square degrees (100% of the sky).
*   **Handedness/Morphology:** N/A (CMB temperature and polarization survey; no galaxy morphology).
*   **Morphology Production:** N/A.
*   **Mirror-Controllable:** N/A.
*   **Access:** Planck Legacy Archive (PLA), IRSA, NERSC.

### 9. ACT DR6
*   **Release Date:** March 2025.
*   **Scale:** High-resolution map products (arcminute resolution) and SZ cluster catalogs.
*   **Sky Coverage:** ~19,000 square degrees.
*   **Handedness/Morphology:** N/A (CMB and cluster survey).
*   **Morphology Production:** N/A.
*   **Mirror-Controllable:** N/A.
*   **Access:** NASA LAMBDA, NERSC.

### 10. SPT-3G
*   **Release Date:** Deep Field (D1) released early 2026; 5-year Galaxy Cluster Catalog released July 2026.
*   **Scale:** >7,000 galaxy clusters; deep CMB polarization maps.
*   **Sky Coverage:** ~1,500 square degrees (main survey).
*   **Handedness/Morphology:** N/A (CMB and cluster survey).
*   **Morphology Production:** N/A.
*   **Mirror-Controllable:** N/A.
*   **Access:** NASA LAMBDA.

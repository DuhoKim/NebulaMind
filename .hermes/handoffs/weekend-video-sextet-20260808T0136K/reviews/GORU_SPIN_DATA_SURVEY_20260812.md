# GORU: Spin Data Survey (Orientation Custody)

**FRAMING AND REQUIREMENT:**
This survey actively searches for a dataset that provides **end-to-end orientation custody**. The specific failure mode in previous handedness studies (like Shamir's undocumented FITS-to-image conversions or Ganalyzer's inability to ingest FITS natively) is the potential for an algorithmic pixel-path chirality flip prior to classification. We require verifiable documentation of pipeline parity and FITS-to-image rendering, or natively published mirrored-image controls.

---

## EXECUTIVE VERDICT ON ORIENTATION CUSTODY
**ALL CANDIDATES FAIL the mirrored-image control requirement.** 
Zero surveys publish their own mirrored-image control runs or explicitly document "pipeline parity checks" natively. Mirrored controls in the literature (e.g., Galaxy Zoo) were strictly UI interventions implemented by the researchers *after* data acquisition, not products of the survey pipelines.

**Regarding WCS Custody:**
All major surveys (HSC, DESI, SDSS, Pan-STARRS, KiDS, DES, Euclid, Rubin) mathematically handle orientation and parity via standard FITS World Coordinate System (WCS) `CDi_j` matrices. The failure of orientation custody historically lies not in the survey FITS, but in the undocumented tools researchers use to render FITS into JPEGs (which often ignore the negative determinant of the CD matrix, silently mirroring the output). Therefore, a survey only offers end-to-end custody if it provides a strictly documented, server-side JPEG cutout service.

---

## 1. Subaru HSC-SSP (Hyper Suprime-Cam)
*   **Raw FITS Access:** STARS/SMOKA archive; Processed FITS via `hsc-release.mtk.nao.ac.jp`.
*   **WCS/Orientation:** WCS handled by the `hscPipe` pipeline.
*   **Sky / Depth / Res:** ~1,400 deg² (Wide). $r \sim 26$ mag. Resolution: 0.168"/pixel (median seeing ~0.6").
*   **Handedness History:** Extensively used by Lior Shamir (2020+) to measure chirality at higher redshifts.
*   **Custody Status: FAILS.** No native mirrored runs. FITS-to-JPEG cutout generation parity is not rigorously documented to prevent client-side flipping errors.

## 2. DESI Legacy Imaging (DECaLS / BASS / MzLS, DR10)
*   **Raw FITS Access:** NOIRLab Astro Data Archive.
*   **WCS/Orientation:** Cutouts use WCS TAN projection. The `legacysurvey.org/viewer` cutout service renders JPEGs using strict North-up/East-left WCS enforcement with no native pipeline flipping commands.
*   **Sky / Depth / Res:** ~14,000–20,000 deg². $r \sim 24.4$ mag. Resolution: 0.262"/pixel.
*   **Handedness History:** Used by Shamir to map multi-pole spin alignments.
*   **Custody Status: FAILS (Strictly).** No native mirrored runs. While LegacyViewer enforces standard WCS on JPEGs, there is no explicit parity-check documentation guaranteeing end-to-end custody without external verification.

## 3. SDSS (Sloan Digital Sky Survey)
*   **Raw FITS Access:** Science Archive Server (SAS).
*   **WCS/Orientation:** SkyServer JPEG cutout service explicitly relies on WCS to correct CCD-level parity, projecting to North-up/East-left. 
*   **Sky / Depth / Res:** ~14,055 deg² (Legacy). Resolution: 0.396"/pixel.
*   **Handedness History:** The foundation of Galaxy Zoo and Shamir's early dipole alignment claims.
*   **Custody Status: FAILS.** No mirrored runs published by SDSS. Furthermore, intense debate exists in the literature regarding whether the SkyServer FITS-to-JPEG conversion itself introduced biases in early chirality studies, compromising its status as a trusted parity custodian.

## 4. Pan-STARRS (DR1 / DR2)
*   **Raw FITS Access:** MAST Archive (`ps1images.stsci.edu`).
*   **WCS/Orientation:** Standard `CD` matrix. Documentation warns that older visualization software (like DS9) might misinterpret equinox epochs without specific `RADESYS` keywords.
*   **Sky / Depth / Res:** ~30,000 deg² (3$\pi$ survey). Resolution: 0.25"/pixel.
*   **Handedness History:** Used by Shamir to cross-validate SDSS handedness claims.
*   **Custody Status: FAILS.** No mirrored runs. Explicit warnings about software misinterpreting headers highlight the exact FITS-to-image pipeline vulnerability we are avoiding.

## 5. KiDS (Kilo-Degree Survey) & 6. DES (Dark Energy Survey DR2)
*   **Raw FITS Access:** ESO Archive (KiDS) / NOIRLab Science Archive (DES).
*   **WCS/Orientation:** Standard Astro-WISE (KiDS) and DESDM (DES) WCS pipelines.
*   **Sky / Depth / Res:** KiDS: 1,347 deg², seeing < 0.7". DES: ~5,000 deg², 0.263"/pixel.
*   **Handedness History:** Both have been included in large-scale quadrupole/dipole spin aggregations.
*   **Custody Status: FAILS.** Neither survey publishes mirrored controls or explicit parity-custody pipeline documentation.

## 7. Euclid (Q1 / ERO)
*   **Addressing the Corpus Question:** The 1,359 mentions of Euclid are *not* just anticipation. The Euclid Q1 release (March 2025) provides genuinely available, public, calibrated FITS data via the ESA Science Archive (ESASAC). 
*   **Sky / Depth / Res:** Q1 covers 63.1 deg². Resolution: 0.16"-0.18" (VIS instrument), completely resolving spiral arms at deep redshifts.
*   **WCS/Orientation:** Extreme precision astrometry with satellite azimuth/beta orientation angles rigorously documented.
*   **Handedness History:** None yet due to recency.
*   **Custody Status: FAILS.** No native mirrored runs.

## 8. Rubin / LSST (Data Previews)
*   **Public Availability:** **FAILS PUBLIC DATA REQUIREMENT.** Data Previews (DP1, DP2) available via the Rubin Science Platform (RSP) are restricted strictly to Rubin data rights holders. They are not public.
*   **WCS/Orientation:** LSST Science Pipelines warn users explicitly *against* manually manipulating FITS WCS headers outside of the `Butler` environment due to orientation mapping errors.
*   **Handedness History:** None.
*   **Custody Status: FAILS.** Not public, no mirrored runs.

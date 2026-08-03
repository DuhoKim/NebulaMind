# gemini-agy-deep-cycle-5
Started UTC: 2026-07-09T02:39:47Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_05

## 1. Executive Summary & Synthesis
This review is conducted in a read-only mode to assess the scientific framing of the flagship paper (RP-1) and its supplementary denominator/proxy atlas. The overarching goal is to prevent any physical interpretation of selection-skewed or aperture-biased catalog parameters and to ensure they are strictly understood as observational denominators.

---

## 2. Issues and Proposed Revisions

### Issue 1: Overclaim / Confounding of Fiber-Center Catalog sSFR with Global Star Formation
* **Severity**: Major
* **Risky Sentence (Flagship, Sec. 2)**: 
  > "Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2–6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global."
* **Critique**: The abstract and subsequent sections repeatedly refer to "catalog specific star-formation rate" and "median $\Delta\log {\rm sSFR}$ of -1.309 dex". A reader might mistake this catalog offset as representing a physical suppression of star formation across the whole galaxy. Because BPT classifications and catalog properties are measured within a fixed 3-arcsec physical aperture that covers different physical scales at different redshifts (1.2 kpc vs 6.5 kpc), there is a strong aperture bias. If the AGN hosts are more centrally concentrated or bulgy, the fiber will sample more bulge light than in star-forming control galaxies of the same mass, artificially depressing the fiber sSFR proxy.
* **Proposed Replacement**:
  > "Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2–6.5 kpc. Consequently, the catalog sSFR offset is dominated by fiber-aperture limitations and represents a central fiber-based proxy offset rather than a global galaxy-wide specific star-formation rate suppression."

---

### Issue 2: Weak Caveat on Sample Non-Randomness and Capping
* **Severity**: Blocker
* **Risky Sentence (Flagship, Abstract & Sec. 2)**: 
  > "The analysis uses a non-random, capped 60,000-row emission-line cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies..."
* **Critique**: Why was the cache capped at 60,000 rows, and how was it ordered? The text notes it is ordered by `specObjID`. Since `specObjID` encodes plate, MJD, and fiber, sorting by it and truncating introduces systematic selection bias based on observation date and sky coverage (e.g., plates observed early in the SDSS survey vs. later runs). This is a blocker for treating the statistics as representative of even the parent SDSS catalog.
* **Proposed Replacement**:
  > "Because the 60,000-row cache is truncated sequentially by \texttt{specObjID}, it is subject to spatial and observational epoch biases from the early stages of the SDSS survey. All statistical intervals and offset measurements are purely illustrative of this sub-sample and must not be treated as unbiased representations of the DR17 parent population."

---

### Issue 3: Citation-Role Ambiguity (Method Support vs. Future Motivation)
* **Severity**: Minor
* **Risky Citation Grouping (Flagship, Sec. 6)**:
  > "...future work needs the kinds of measurements used in radio-mode, X-ray cavity, molecular-gas, outflow, environment, and simulation-mock studies \citep{best2005,dekel2006,fabian2012,heckmanbest2014,lamassa2013,mcnamara2007,veilleux2005,xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,simba2019,tng2019,eagle2015,peng2010,piotrowska2022,wetzel2013}; they are not part of the present SDSS-only denominator."
* **Critique**: The paper cites a massive block of 18 papers at once. Some of these papers contain actual observational methods or catalogs (like `\citep{xcoldgass2017,xgass2018}` for gas masses, `\citep{best2005}` for radio), whereas others are theoretical models or simulations (`\citep{dekel2006,tng2019,eagle2015}`). Grouping them together obscures which references serve as motivation for future multiwavelength data vs. which ones represent theoretical simulation targets.
* **Proposed Replacement**:
  > "In practice, this means future work must incorporate external physical constraints: radio jet power and cavity energetics (e.g., \citealt{best2005,mcnamara2007,heckmanbest2014}), molecular gas reservoirs (e.g., \citealt{xcoldgass2017,xgass2018}), kinematics of multiphase outflows (e.g., \citealt{veilleux2005,cicone2014}), environment and group halo membership (e.g., \citealt{peng2010,wetzel2013}), and mock observations generated from cosmological simulations (e.g., \citealt{tng2019,eagle2015})."

---

### Issue 4: Denominator Misinterpretation in Supplement
* **Severity**: Major
* **Risky Sentence (Supplement, Sec. 3.5)**:
  > "At what stellar-mass scale do the low-sSFR emission-line fraction and optical AGN incidence rise in the same SDSS denominator?"
* **Critique**: A casual reader might interpret this mass scale (e.g. $[11.0, 12.5]$ dex) as a physical quenching transition mass due to AGN feedback. However, in this BPT-selected emission-line sample, the high-mass bins are extremely incomplete due to the exclusion of weak/retired galaxies that do not meet the four-line S/N $\geq 3$ threshold. 
* **Proposed Replacement**:
  > "We identify the stellar-mass bin where the active emission-line fraction is dominated by low-sSFR and optical AGN classifications within our selection cut. This transition reflects selection-induced emission-line survivorship rather than a physical transition mass for individual galaxy quenching."

---

## 3. Required Missing-Data Observables Checklist

The supplementary atlas must explicitly document the following missing observables to avoid presenting proxy values as physical results:

| Section | Topic / Paper | Missing Physical Observables | Risk of Status Quo |
| :--- | :--- | :--- | :--- |
| **3.1** | Environment Quenching | Group catalogs, central/satellite classification, weak-lensing or X-ray group halo masses. | Density proxy is mistaken for physical halo-based environmental quenching. |
| **3.2** | Maintenance Heating | High-resolution radio maps (VLA/LOFAR), X-ray cavity/cooling measurements (Chandra/XMM). | Optical BPT class is mistaken for active mechanical/radio jet feedback. |
| **3.3** | Outflow Escape | Spatially resolved kinematics (IFU), gas phase tracers (neutral/molecular/ionized). | Ionization line ratios are mistaken for physical gas outflows. |
| **3.4** | Radio Jet Environment | Radio morphologies, environmental group membership, cluster-gas density profile. | Host local density proxy is mistaken for radio-mode coupling. |
| **3.5** | Transition Mass | Gas fractions ($f_{\rm gas}$), total baryon census, halo masses. | Survivorship bias in BPT sample is mistaken for a physical feedback mass threshold. |
| **3.6** | Multiphase Census | CO (molecular), H I (neutral), X-ray (hot gas) mass measurements. | Optical emission ratios are mistaken for total cold/warm gas budget. |
| **3.7** | Gas Depletion | Direct CO molecular gas masses, resolved aperture corrections. | Catalog sSFR drop is mistaken for low gas-fraction or altered SFE. |
| **3.8** | Sim Validation | Synthetic mock catalogs processed through the exact SDSS fibers and line selection. | Direct catalog-to-simulation comparison without forward modeling. |

---

## 4. Ranked Integrator Actions

1. **[Priority 1: Blocker] Fix Cache Bias Statement**: Add a clear disclaimer in the flagship paper's introduction and data section explaining how sorting the 60,000-row sample by `specObjID` impacts statistical generality.
2. **[Priority 2: Major] Add Aperture/Fiber Warning**: Include a specific warning about the difference between fiber-based and global specific star-formation rates (sSFR) in Section 2 of the flagship paper.
3. **[Priority 3: Major] Standardize Supplement Section Disclaimers**: Ensure that each of the 8 subsections in the supplement starts with a bolded warning that the figures show selection-skewed denominators, not physical population properties.
4. **[Priority 4: Minor] Unpack Block Citations**: Split the large bibliography group in Section 6 into category-specific citations (e.g. splitting simulations from observations).

---

## 5. Safety Ledger

* **Files Read**: None (Read-only review performed solely using the text provided in the prompt).
* **Files Written**: None.
* **Commands Run**: None.
* **Database/API/Cloud Changes**: None.
* **Git Actions**: None.
* **Status**: 100% Local, Read-Only, Safe Review.


# command_result
exit_code=0
elapsed_s=15.6
timed_out=False
finished_utc=2026-07-09T02:40:03Z

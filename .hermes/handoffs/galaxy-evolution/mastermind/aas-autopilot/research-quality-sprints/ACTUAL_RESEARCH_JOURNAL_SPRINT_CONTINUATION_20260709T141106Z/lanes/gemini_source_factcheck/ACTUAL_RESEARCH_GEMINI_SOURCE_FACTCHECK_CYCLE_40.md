# gemini-source-factcheck-flash-low-cycle-40
Started UTC: 2026-07-09T19:19:10Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.5 Flash (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_GEMINI_SOURCE_FACTCHECK_CYCLE_40

Review of the primary candidate package for overclaims, citation-role errors, and compliance with the real-data-only policy has been completed.

---

### Explicit Policy Declaration
> [!IMPORTANT]
> **No mock, synthetic, fake, placeholder, or toy data are accepted under any circumstances. All analyses are strictly limited to real observational measurements derived from local SDSS/MPA-JHU value-added catalog products, or clearly identified public database queries.**

---

### 1. Blocker, Major, and Minor Issues

* **Blocker Issues:** None. 
  * *Rationale:* The text adheres strictly to safety locks. There are no attempts to write outside the candidate directory, alter active databases, or perform database mutations. The manuscripts explicitly state that all external/multiwavelength and simulation datasets are *missing* and are for *motivation and future target-list design only*.
* **Major Issues:** None.
  * *Rationale:* The text is highly selection-aware and explicitly states that the 60,000-galaxy cache is non-volume-complete and non-random, selected sequentially by `specObjID`. It clearly reports that morphological controls (such as $R_{90}/R_{50}$ or `fracDeV`) were not retained in the cache, and the sSFR offset is thus degenerate with bulge-fraction or morphology.
* **Minor Issues:** 
  1. *Unclassified Objects Handling:* In the flagship paper, it is stated: *"the 67 unclassified objects are retained in denominator counts but excluded from control pairing."* While accurate, it could explicitly detail how these 67 are classified or why they failed matching (e.g., missing flux or invalid line values) to prevent any ambiguity.
  2. *H$\alpha$ Extrapolation Systematics:* In Section 4.7 of the supplement (molecular-gas proxy), the text states: *"Here the H-alpha luminosity proxy is the aperture-corrected galSpecExtra catalog value rather than raw fiber flux; that catalog-level correction extrapolates the fiber measurement..."* A minor note could remind the reader that dust correction systematics (e.g., Balmer decrements) represent an unmodeled catalog uncertainty.

---

### 2. Risky Sentences and Proposed Wording

* **Flagship, Abstract (Line 13):**
  * *Current Text:* "...the reported -1.309 dex sSFR offset is an association-only measurement within this fixed-size, morphology-uncontrolled optical denominator and cannot be disentangled from a morphology or bulge-fraction association."
  * *Risk Assessment:* Low, but can be made even safer by reinforcing that this is catalog-dependent.
  * *Proposed Safer Wording:* "...the reported -1.309 dex sSFR offset is an association-only measurement within this fixed-size, morphology-uncontrolled catalog-dependent optical denominator and cannot be disentangled from host morphology, bulge-fraction, or fiber aperture effects."

* **Supplement, Section 4.1 (Relative neighbor-count baseline, Line 68):**
  * *Current Text:* "The 10th-neighbor index is the rank of the 10th nearest companion in projected sky separation within this redshift-limited sample; it is an internal ordinal rank..."
  * *Risk Assessment:* Medium-low. Without group catalog validation, readers might treat this rank as a physical density.
  * *Proposed Safer Wording:* "The 10th-neighbor index is a relative rank of the 10th nearest companion in projected sky separation within this specific, selection-limited sample; it is an internal ordinal rank that is highly biased by the 55-arcsec fiber collision limit and must not be used as a physical environmental density or halo-mass proxy."

---

### 3. Multiwavelength & Simulation Literature Tracking

All citations to radio, X-ray, CO, HI, outflow, and simulation literature are strictly tracked and verified as motivation/checklist items rather than active measurements:
* **CO/HI Literature:** Catinella et al. (2018) \citep{xgass2018}, Saintonge et al. (2017) \citep{xcoldgass2017}, and Tacconi et al. (2018) \citep{tacconi2018} are correctly framed as baseline motivation for future molecular gas mass follow-ups.
* **X-ray / Radio Heating:** Fabian (2012) \citep{fabian2012}, McNamara & Nulsen (2007) \citep{mcnamara2007}, Heckman & Best (2014) \citep{heckmanbest2014}, and Best et al. (2005) \citep{best2005} are correctly positioned as motivators for future heating-to-cooling duty cycle measurements.
* **Outflows:** Veilleux et al. (2005) \citep{veilleux2005}, Cicone et al. (2014) \citep{cicone2014}, and Harrison et al. (2018) \citep{harrison2018} are correctly identified as resolved kinematics constraints missing from the current fiber-centered study.
* **Simulations:** Davé et al. (2019) \citep{simba2019}, Nelson et al. (2019) \citep{tng2019}, and Schaye et al. (2015) \citep{eagle2015} are correctly labeled as comparison frameworks that require mock-observational pipelines (through the same sequential `specObjID` selection function) before any validation can be attempted.

---

### 4. Claims Requiring Uninventoried Real Data

Any attempt to make the following physical claims would require data not currently in the local real-data inventory (which is restricted to optical SDSS DR17 catalog rows):
1. *Gas-depletion timescales or molecular-gas mass estimates:* Requires CO/dust measurements (e.g., ALMA/IRAM).
2. *Mechanical/Feedback coupling efficiency:* Requires radio flux/morphology and X-ray temperature/pressure profiles.
3. *Outflow gas-mass rates or escape velocities:* Requires high-resolution spatially resolved IFU spectroscopy (e.g., MaNGA/MUSE) to decouple outflow from circular velocity.
4. *Halo or group membership quenching:* Requires complete spectroscopic environmental group catalogs (e.g., Yang et al. group catalogs) and correction for fiber collisions.

---

### 5. Checkable Source/Citation Suggestions

The following identifiers are verified and correct in the TeX bibliography:
* **SDSS DR17 Catalog Backbone:** Abdurro'uf et al. 2022, ApJS, 259, 35 (ADS: [2022ApJS..259...35A](https://ui.adsabs.harvard.edu/abs/2022ApJS..259...35A))
* **BPT Diagnostic Demarcations:** 
  * Kauffmann et al. 2003, MNRAS, 346, 1055 (ADS: [2003MNRAS.346.1055K](https://ui.adsabs.harvard.edu/abs/2003MNRAS.346.1055K))
  * Kewley et al. 2006, MNRAS, 372, 961 (ADS: [2006MNRAS.372..961K](https://ui.adsabs.harvard.edu/abs/2006MNRAS.372..961K))
* **MPA-JHU Catalog Methodology:** Brinchmann et al. 2004, MNRAS, 351, 1151 (ADS: [2004MNRAS.351.1151B](https://ui.adsabs.harvard.edu/abs/2004MNRAS.351.1151B))

---

### 6. Safety Ledger

| Parameter | Constraint | Compliance Status |
| :--- | :--- | :--- |
| **Write Directory** | Under sprint directory or candidate copies only | **COMPLIANT** (Read-only review; zero files modified) |
| **Public Pages / Roots** | No direct edits to static roots or production pages | **COMPLIANT** |
| **Database Operations** | No SQL inserts, page versioning, or mutations | **COMPLIANT** |
| **Deploy / Restart** | No system restarts or builds executed | **COMPLIANT** |
| **Git Actions** | No commits, merges, or history rewrites | **COMPLIANT** |
| **Credentials / API** | No access token or account configuration reads | **COMPLIANT** |
| **External Submission** | No external manuscript submissions | **COMPLIANT** |


# command_result
exit_code=0
elapsed_s=12.2
timed_out=False
finished_utc=2026-07-09T19:19:22Z

# gemini-agy-deep-cycle-7
Started UTC: 2026-07-09T02:50:38Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_07

## 1. Executive Summary & Critical Review

This quality sprint review focuses on identifying overclaims, missing observables, citation-role issues, weak caveats, and potential denominator-vs-physical confusion in the cycle 7 candidate drafts: the **RP-1 Flagship Draft** ([rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_07_package/flagship_rp1/aastex/rp1_flagship_polished.tex)) and the **Supplementary Denominator/Proxy Atlas** ([supplementary_denominator_atlas.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_07_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex)).

---

## 2. Issues & Proposed Wording Revisions

### Issue 1: Spatial/Plate Selection Bias from `specObjID` Ordering (Severity: Blocker)
* **Risky Sentence:** 
  > "The pilot analysis sample is capped at 60,000 rows and ordered by `specObjID`; it is not a random sample." (Flagship, Sec. 2 & Supplement, Sec. 2)
* **Problem:** `specObjID` is directly determined by the SDSS plate, MJD, and fiber ID. Sorting and capping by `specObjID` means the sample consists of the first ~12% of SDSS plates. This introduces severe spatial selection effects (clustering in specific regions of the sky/RA-Dec) and temporal/instrumental calibration biases. If local density proxies (e.g., 10th-neighbor density) are computed *only* within this spatially capped subset, the density estimates are highly distorted.
* **Propose Safer Replacement:** 
  > "The pilot analysis sample is a capped 60,000-row subset selected sequentially by `specObjID`. Because `specObjID` is structured by plate, observing date, and fiber ID, this sequential cap introduces systematic spatial clustering and field bias. All matched-control results, catalog offsets, and density estimates are conditional on this localized sub-sample rather than representing a random or volume-complete SDSS population."

---

### Issue 2: Denominator Confusion in Environment Density Proxy (Severity: Major)
* **Risky Sentence:** 
  > "The nearest-neighbor density proxy adds low-sSFR incidence information beyond stellar mass in the SDSS emission-line sample. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor density proxy. The high-density quartile has a low-sSFR emission-line fraction of 0.230..." (Supplement, Sec. 3.1)
* **Problem:** The 10th-neighbor density is computed inside an emission-line-only sample (where active star-forming galaxies are over-represented and quiescent galaxies are mostly excluded due to the S/N $\geq 3$ BPT line cut). Calculating density on this subset severely underestimates the true environmental density, especially in clusters. Furthermore, the "low-sSFR emission-line fraction" of 0.230 is highly artificial because it completely ignores the dominant population of fully quenched, non-emission-line galaxies in high-density regions.
* **Propose Safer Replacement:** 
  > "The density proxy computed here is internal to the emission-line-selected cache and does not account for the dominant population of quenched, non-emission-line galaxies. Consequently, this density serves as a relative subset-restricted rank rather than a physical group/cluster density, and the low-sSFR emission-line fraction of 0.230 is an artifact of the selection cascade rather than a true environmental quenching fraction."

---

### Issue 3: Denominator Confusion in Stellar-Mass Incidence (Severity: Major)
* **Risky Sentence:** 
  > "The first stellar-mass bin with low-sSFR fraction above 0.5 is $\log(M_\star/M_\odot) \in [11.0,12.5]$." (Supplement, Sec. 3.5)
* **Problem:** In a volume-complete sample, the fraction of low-sSFR galaxies at $M_\star > 11$ is much higher (often $>80\%$). A value of 0.5 is an artifact of requiring $S/N \geq 3$ in all four BPT lines (which preferentially excludes quenched massive galaxies that lack gas). A reader could mistake this for a physical transition mass or a real population fraction.
* **Propose Safer Replacement:** 
  > "The first stellar-mass bin where the low-sSFR fraction *within this emission-line-selected sample* exceeds 0.5 is $\log(M_\star/M_\odot) \in [11.0,12.5]$. This fraction is suppressed relative to the general galaxy population because the strict four-line emission requirement systematically excludes fully quenched massive systems."

---

### Issue 4: Fiber Aperture vs. Global sSFR (Severity: Minor)
* **Risky Sentence:** 
  > "Because the fiber misses more of the outskirts of low-redshift galaxies, this central comparison can over-penalize bulge-dominated systems relative to more extended star-forming disks." (Flagship, Sec. 2)
* **Problem:** The MPA-JHU catalog provides both fiber and total physical parameters (`lgm_tot_p50` vs. `lgm_fib_p50`, and `specsfr_tot_p50` vs. `specsfr_fib_p50`). It is important to clarify whether the fiber-aperture correction applied in the MPA-JHU catalog is sufficient, or if the matched-control setup itself is biased by comparing different aperture fractions.
* **Propose Safer Replacement:** 
  > "Because the SDSS 3-arcsec fiber covers different physical scales (1.2–6.5 kpc) depending on redshift, matched pairs at different redshifts or with differing concentration indices will have different aperture fractions. While we use the aperture-corrected catalog estimates, unresolved spatial profiles remain a key source of systematic uncertainty in the matches."

---

### Issue 5: Citation-Role Ambiguity (Severity: Minor)
* **Risky Citations:** In the Supplement (Sec. 3.1–3.8) and Flagship (Sec. 6), citations like `Wetzel et al. (2013)`, `Peng et al. (2010)`, `Best et al. (2005)`, `Cicone et al. (2014)` are cited at the end of subsections containing the missing-observables list.
* **Problem:** These citations might be misinterpreted as supporting the *methodology* or *data* of the current pilot, when they actually represent the external/future datasets and models that the current pilot *lacks*.
* **Propose Safer Alignment:** Ensure that the text explicitly prefixes these citations to highlight their role as external references for future missing-observable benchmarks:
  > "...as physically demonstrated in resolved/multiphase studies (e.g., \citealt{cicone2014, carniani2017}; which are not measured in this work)."

---

## 3. Checklist of Missing Observables

The following table flags the specific missing-data claims in each supplement note and identifies what physical tracers must be added for a sound physical interpretation:

| Supplement Note | Topic | Missing Observable Tracers / Models Required |
| :--- | :--- | :--- |
| **3.1** | Environment | Group/cluster membership catalogs, halo masses, morphology controls |
| **3.2** | Maintenance Heating | X-ray cavity/cooling-core data, high-sensitivity radio jet power |
| **3.3** | Outflows | Resolved kinematics, outflow velocities, multiphase gas budgets (neutral/ionized/molecular) |
| **3.4** | Environment & Jets | Radio jet morphology, hot-gas density maps, cavity energetics |
| **3.5** | Transition Mass | Total gas mass fraction, baryon deficits, stellar-feedback observables |
| **3.6** | Multi-phase Census | Shared parent denominator, consistent aperture models, neutral/molecular gas maps |
| **3.7** | Gas Depletion | CO/dust-based molecular gas masses, aperture-matched SFR |
| **3.8** | Mock Validation | Simulation mock catalogs passed through observational/instrumental selection filters |

---

## 4. Ranked Concrete Integrator Actions

1. **[Action 1] (Priority: High / Blocker):** Add explicit warnings about the spatial and instrument-calibration bias introduced by selecting the sample based on a sequential `specObjID` cap.
2. **[Action 2] (Priority: High):** Revise the environmental density subsection to clearly state that the 10th-neighbor density proxy is calculated on a highly biased emission-line subset, not a volume-complete catalog.
3. **[Action 3] (Priority: Medium):** Revise all references to "low-sSFR fraction" in specific bins to emphasize that they are fractions *conditional on the emission-line denominator*, not global population fractions.
4. **[Action 4] (Priority: Medium):** Add explicit qualifiers to the citations in the references section to ensure they are not misconstrued as supporting the methodology or dataset used in the current work.

---

## 5. Safety Ledger

* **Live system updates:** None.
* **Git commits/pushes/merges:** None.
* **Database writes:** None.
* **API/External requests:** None.
* **Local file edits:** None (Read-only review).


# command_result
exit_code=0
elapsed_s=17.9
timed_out=False
finished_utc=2026-07-09T02:50:55Z

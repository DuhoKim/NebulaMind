**Review: Phase: Abstract/Title**

I have inspected `provenance/REAL_DATA_SOURCE_CUSTODY.json`, which correctly inventories the 13 analysis files, 60,000-row cache, 8,146-pair matched catalog, and downstream figures/tex files. The provenance is verified, and all numeric invariants (-1.309 dex median $\Delta\log {\rm sSFR}$, bootstrap 95\% interval [-1.334,-1.283], $N=8,146$ pairs) are strictly preserved.

### Integrity Blockers
- **None.** The manuscript adheres perfectly to the association-only, provenance-backed boundaries. The 60,000-row sample and fiber biases are accurately identified, and no causal claims are invented. 

### Journal-Quality Blockers & Section-Level Improvements

**1. Flagship Abstract & Title**
- **Title:** The title is slightly verbose. Consider streamlining to: *Broad Optical BPT Excitation and Catalog Specific Star Formation in SDSS DR17: A Matched-Control Pilot*.
- **Abstract:** The abstract is overly defensive. While it successfully respects safety boundaries, dedicating the final 40% of the abstract to listing what the study *is not* (e.g., "not a causal feedback, physical-quenching, gas-depletion, or population-abundance measurement") undermines the scientific utility of what *is* measured. 
  - *Improvement:* Condense the limitations into a single, punchy sentence. State the actual offset upfront, mention the missing morphology/aperture controls, and direct the reader to the supplement for the specific missing physical requirements (IFU/radio/CO/X-ray).

**2. Supplementary Atlas Abstract & Title**
- **Title:** The title is appropriate. 
- **Abstract:** Similar to the flagship, the abstract reads more like a compliance checklist than a scientific guide. The phrase "Each entry is a missing-observable checklist item first and a literature pointer second" is too meta for a formal journal publication.
  - *Improvement:* Restructure the abstract to first list the eight baselines provided (e.g., environmental rank, stellar-mass bins, outflow incidence) and then state universally that these baselines are optical-only and require specific multi-wavelength (e.g., ALMA CO, VLA radio) or IFU (e.g., MaNGA) integration to yield physical density or causal mechanisms.

**3. Literature Integration & Real Identifiers**
If you choose to add context regarding how other surveys handle these exact fiber-aperture and morphological biases, ensure you cite real, verified literature with exact identifiers. For example, when discussing the necessity of IFU data to break the aperture-morphology degeneracy, you could integrate the MaNGA overview:
- *Bundy et al. (2015)* (ADS bibcode: 2015ApJ...798....7B; already in your bibliography, but ensure it's utilized effectively in the introduction/abstract context).
- *Wake et al. (2017)* for the MaNGA sample design and mass-completeness limits to contrast with this non-volume-complete cache (ADS bibcode: 2017AJ....154...86W; DOI: 10.3847/1538-3881/aa7ecc).

JOURNAL_LEVEL_PASS: NO

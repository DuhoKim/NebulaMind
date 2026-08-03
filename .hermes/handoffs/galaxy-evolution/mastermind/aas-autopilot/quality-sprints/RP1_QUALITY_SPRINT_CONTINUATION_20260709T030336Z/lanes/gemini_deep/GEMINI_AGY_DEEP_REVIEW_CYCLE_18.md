# gemini-agy-deep-cycle-18
Started UTC: 2026-07-09T04:56:31Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_18

# Manuscript Quality Sprint Deep Review (Cycle 18)

This review evaluates the candidate flagship manuscript (`rp1_flagship_polished.tex`) and its accompanying supplement (`supplementary_denominator_atlas.tex`) under a strict read-only safety model. 

---

## 1. Severity-Ranked Issues

### Issue 1: Over-generalized "AGN Fraction" in Low-Resolution Denominators (Major)
* **Location**: Supplement sections 3.2 (Maintenance Heating), 3.4 (Radio-Jet), 3.5 (Stellar-Mass), and 3.7 (Gas Depletion).
* **Risky Wording**: 
  > "The optical BPT AGN fraction is 0.430 in the massive subset..."
  > "...the optical AGN fraction peaks in the 11.0–12.5 bin at 0.520."
* **Physical vs. Proxy Misdirection**: Calling the BPT-demarcated denominator the "optical AGN fraction" without qualification leads readers to mistake this classification proxy for active supermassive black hole accretion. At SDSS spatial resolutions and fiber apertures, this fraction is heavily contaminated by retired stellar populations and low-ionization gas (LINER-like emission) not powered by accretion.
* **Safer Replacement Wording**: 
  > "The fraction of galaxies falling within the BPT-defined AGN/composite classification boundary (which includes both accretion-powered Seyferts and contamination from retired, stellar-heated bulge systems) is 0.430..."

---

### Issue 2: Insufficient Caveating of Aperture-Extrapolated sSFR (Major)
* **Location**: Flagship Abstract and Section 4.
* **Risky Wording**: 
  > "The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex..."
* **Physical vs. Proxy Misdirection**: A reader could interpret this -1.309 dex offset as a physical galaxy-wide quenching result (star-formation suppression). Because the 3-arcsec fiber only covers the central bulge, and the controls are not matched in morphology, this offset is highly likely a spatial-aperture mismatch effect rather than physical feedback.
* **Safer Replacement Wording**: 
  > "The preferred matched comparison yields 8,146 pairs and a median fiber-aperture-convoluted catalog $\Delta\log {\rm sSFR}$ offset of -1.309 dex (reflecting central sSFR differences and potential morphology/bulge-fraction mismatch)..."

---

### Issue 3: Incomplete Environment Definition from 10th-Neighbor Index (Minor)
* **Location**: Supplement Section 3.1 & 3.4.
* **Risky Wording**: 
  > "We establish a relative neighbor-count baseline... 10th-neighbor index for low-sSFR incidence"
* **Physical vs. Proxy Misdirection**: The 10th-neighbor rank within a capped, selection-limited sample is an ordinal proxy rather than a physical volume density or halo-mass proxy, and fiber collisions severely suppress pairs.
* **Safer Replacement Wording**: 
  > "We establish an ordinal 10th-neighbor index ranking internal to this selection-limited sample (which serves as a target baseline and suffers from fiber-collision suppression rather than representing absolute local volume density)..."

---

## 2. Citation-Role Mapping Audits
All citations in the manuscript are correctly partitioned according to their physical roles:
* **Method/Classification Support (Valid)**: \citep{stasinska2008, stasinska2015} are correctly restricted to identifying stellar/LINER contamination in the optical line ratios.
* **Future-Data Motivation (Valid)**: The multiwavelength references—specifically \citep{best2005, heckmanbest2014, fabian2012, mcnamara2007} (radio/X-ray), \citep{xcoldgass2017, xgass2018} (molecular gas), \citep{veilleux2005, cicone2014} (outflows), and \citep{simba2019, tng2019, eagle2015} (simulations)—are correctly confined to outlining the observational follow-up requirements. They are not used to validate or corroborate the current SDSS-only statistical associations.

---

## 3. Required Missing-Data Warnings

The supplement must explicitly flag where physical claims are currently blocked by missing data:

| Section / Topic | Missing Observables Required for Causal Inference |
| :--- | :--- |
| **3.1 Environment Quenching** | Group catalogs, satellite/central classification, halo mass estimates, and fiber-collision angular corrections. |
| **3.2 Maintenance Heating** | X-ray cavity detection, cooling-flow rates, high-resolution radio jet power, and parent halo-selected samples. |
| **3.3 Outflow Kinematics** | High-resolution resolved kinematics, escape velocity potentials, and multiphase (molecular/neutral) gas tracers. |
| **3.4 Radio-Jet Environment** | Jet morphology/ages, hot-gas density maps, and cavity energetics. |
| **3.8 Simulation Mocks** | Simulated galaxies run through the exact SDSS selection function, line S/N caps, and 3-arcsec fiber aperture convolution. |

---

## 4. Concrete Integrator Action Plan

1. **[Priority 1 - Blocker] Update Abstract and Section Titles in Flagship & Supplement**: Apply the safer replacement wording for BPT AGN fractions (clarifying LINER/retired contamination) and catalog sSFR offsets (clarifying aperture-extrapolation and morphology mismatches).
2. **[Priority 2 - Major] Standarize "Proxy" Terminology**: Scan both documents to ensure terms like "star-formation rates" and "AGN fractions" are consistently prepended with "catalog-derived" or "BPT-classified proxy".
3. **[Priority 3 - Minor] Table Captions**: Add explicit notes to Table 1 and Table 2 explaining that counts are conditional on the non-random pilot query cap (`specObjID` sequential ordering).

---

## 5. Safety Ledger

* **Live system edits**: None.
* **Git actions (commit/push)**: None.
* **Database/API mutations**: None.
* **Public publishing / manuscipt submissions**: None.
* **Resource consumption**: Read-only verification of local file paths under user directory `/Users/duhokim/` was strictly maintained.


# command_result
exit_code=0
elapsed_s=16.5
timed_out=False
finished_utc=2026-07-09T04:56:47Z

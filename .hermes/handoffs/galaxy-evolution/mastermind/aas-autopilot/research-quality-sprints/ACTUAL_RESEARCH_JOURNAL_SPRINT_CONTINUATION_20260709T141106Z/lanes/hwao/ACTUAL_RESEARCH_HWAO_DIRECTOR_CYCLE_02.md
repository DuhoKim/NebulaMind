# hwao-agy-low-cycle-2
Started UTC: 2026-07-09T14:17:15Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_02

# Cycle 02 Paper-Quality Triage Plan

## Publication-Readiness Verdict
**RP-1 Flagship:** The manuscript is structurally sound as a formal pilot and successfully maintains its association-only boundary. It correctly documents its limitations: the 60,000-galaxy cache cap, the fiber-aperture bias, and the lack of morphological controls. It is ready for final polish as a methods-and-baselines observational paper, provided it strictly continues to avoid causal "feedback" claims.
**Supplementary Denominator/Proxy Atlas:** The atlas correctly structures the 8 inactive proposals as observational baselines and follow-up target vectors. It is ready to serve as a companion piece outlining future data requirements, preventing the premature publication of incomplete causal claims. 

## Top 12 Concrete Quality Improvements (Ranked by Scientific Value)

### Improvements Using Real Local SDSS Data Already Inventoried
*These can be addressed through text, table, and citation refinement based on the existing `galSpecExtra`, `SpecObj`, and `PhotoObj` joins.*

1. **Quantify the Cap Bias:** Add a concrete table or figure explicitly showing the marginal distributions (mass, redshift, sSFR) of the 60,000-galaxy pilot cap versus the 249,917-galaxy parent to empirically prove the stated "maximum 5 percentage point difference" claim.
2. **Clarify Fiber-Aperture Scales:** Explicitly map the 3-arcsec fiber (1.2–6.5 kpc) to the typical Petrosian or effective radii of the matched pairs (available via `PhotoObj`) to quantify exactly how much of the galaxy is missed by the central aperture. 
3. **Detail the Control Pool Balance:** Explicitly report the post-matching distribution of variance-normalized Euclidean distances between the 8,146 targets and their matched controls to demonstrate the quality of the mass-redshift pairing.
4. **Expand on S/N Bias:** Elaborate on the "preferential loss of passive galaxies" note in Table 1; explicitly state the median sSFR of the rows dropped when moving from S/N$\geq$3 to S/N$\geq$10.
5. **Calibrate the 10th-Neighbor Index:** For the Supplement's relative neighbor-count baseline, report the median projected physical distance (in kpc or Mpc) corresponding to the 10th-neighbor rank within the specific density quartiles to give the ordinal rank physical context.
6. **Clarify LINER/Composite Attrition:** Provide exact counts and median properties for the 12,234 intermediate/composite galaxies that were explicitly excluded from the matched control pairing, clarifying what population is missing from the binary broad-BPT vs. SF comparison.

### Improvements Requiring New Real Data (Must Not Be Written As Results Yet)
*These strictly define the boundaries of what this sprint cannot claim.*

7. **Aperture-Matched Global SFR:** Adding WISE, GALEX, or other global multiwavelength photometry to derive true total SFRs, breaking the central-fiber degeneracy. *(No claims of global quenching allowed).*
8. **Resolved Morphology Controls:** Incorporating structural decompositions (e.g., bulge-to-total ratios) or visual morphologies to match pairs by structure, eliminating the morphology-sSFR confounding variable. *(No claims separating bulge growth from AGN suppression allowed).*
9. **Spatially Resolved Spectroscopy:** Using IFU data (e.g., MaNGA) to separate central gradients from global suppression. *(No claims of spatially resolved feedback allowed).*
10. **Physical Halo and Environment Labels:** Utilizing volume-complete group catalogs with central/satellite labels and estimated halo masses to replace the relative 10th-neighbor index. *(No claims of environmental quenching or jet-coupling efficiency allowed).*
11. **Gas Mass Measurements:** Integrating direct CO, HI, or dust-continuum measurements to distinguish molecular gas depletion from reduced star-formation efficiency. *(No claims of gas depletion or efficiency drops allowed).*
12. **Accretion Luminosity Proxies:** Adding X-ray or radio luminosities to convert BPT excitation classes into physical bolometric AGN luminosities or Eddington ratios. *(No claims of feedback scaling with AGN power allowed).*

## Guidance for the Integrator
- **Safe Wording Changes Only:** You may only edit the TeX files to tighten phrasing around the improvements listed in the "local SDSS data" section (Improvements 1-6). 
- **Preserve Boundaries:** Ensure all references to the 60,000-galaxy sample retain the phrases "computational pilot cap," "non-random," and "arbitrary cache limit."
- **Strictly No Causal Language:** Scan for and remove any accidental use of "quenches," "suppresses," "drives," or "depletes" when referring to the RP-1 matched-control results. Replace them with "is associated with a lower catalog sSFR."
- **Citation Integrity:** Do not insert new citations to support claims you are not measuring. Retain existing citations (e.g., *Stasińska et al. 2008*, *Kewley et al. 2006*) purely as methodological demarcations or theoretical motivations.

## No-Mock-Data Receipt and Safety Ledger
- **Status:** Read-only review completed.
- **Data Used:** Relying strictly on the summarized metrics from the 60,000-galaxy SDSS DR17 cache.
- **Mock Data Generation:** Zero. No synthetic numbers, fake citations, or placeholder values were generated.
- **File Edits:** Zero. No TeX, JSON, or CSV files were modified.
- **System Interactions:** Zero. No git, DB, API, cron, or deploy actions were triggered. No public/live roots were touched. 
- **Integrity Verified:** The RP-1 and Atlas drafts strictly adhere to the association-only, observational-baseline policy.


# command_result
exit_code=0
elapsed_s=33.2
timed_out=False
finished_utc=2026-07-09T14:17:48Z

# hwao-agy-low-cycle-20
Started UTC: 2026-07-09T16:45:42Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_20

Here is the paper-quality triage plan for the cycle 20 integrated manuscripts, adhering strictly to the read-only, real-data-only policy.

### 1. Publication-Readiness Verdict
**Verdict:** **Not Ready for Astrophysical Causal Interpretation; Ready as a Methodological / Baseline Data Release Note.**
*   **RP-1 Flagship:** The manuscript is robust as a transparent, selection-aware matched-control pilot, but it cannot be published as a definitive physical study of AGN feedback. The arbitrary 60,000-galaxy `specObjID`-ordered computational cache limit introduces unquantified sky-coverage and survey-plate biases, making it non-volume-complete. Furthermore, the lack of morphological/structural control leaves the $-1.309$ dex sSFR offset highly degenerate with the well-known mass-morphology relation (i.e., bulges are both older/quenched and more likely to host LINERs/optical AGN). 
*   **Supplementary Atlas:** The atlas correctly identifies itself as an observational baseline and target vector list rather than a physics result. It is ready to serve as an internal project reference or a supplementary data-product release, but its 8 individual sections cannot stand as independent papers until the required multiwavelength cross-matches are physically executed.

### 2. Top 12 Concrete Quality Improvements (Ranked by Scientific Value)
1.  **Resolve Morphological Degeneracy (Structural Matching):** Include a structural proxy (e.g., concentration index $R_{90}/R_{50}$ or `fracDeV`) in the matched-control pairing to separate true excitation-linked sSFR offsets from simple disk-to-bulge transition effects.
2.  **Remove Arbitrary Computational Cap:** Lift the 60,000-galaxy cache limit to utilize the full 249,917 eligible S/N$\geq3$ parent sample, eliminating `specObjID` sequential ordering bias.
3.  **Volume-Completeness Corrections:** Implement $1/V_{\max}$ weighting based on the $0.02 < z < 0.12$ redshift slice and mass limits to allow for population-normalized abundance claims rather than just cache fractions.
4.  **Rigorous Seyfert vs. LINER/Retired Separation:** Apply a formal separation (e.g., the WHAN diagram using EW(H$\alpha$) or the stricter Kewley et al. 2006 cut across *all* analyses) to cleanly remove hot post-AGB powered retired galaxies from the "broad optical BPT-selected" pool.
5.  **Address the SDSS 55-arcsec Fiber Collision Bias:** The 10th-neighbor index is artificially suppressed in dense environments due to fiber collisions. Implement collision-correction weights or replace the proxy with a true group catalog.
6.  **Global vs. Central sSFR Calibration:** The 3-arcsec fiber captures only the central 1.2-6.5 kpc. Compare the fiber `specsfr` to total/global `specsfr` (if available in the MPA-JHU catalog) to measure the extent of aperture bias.
7.  **Dust Attenuation Correction:** Use the observed Balmer decrement (H$\alpha$/H$\beta$) to ensure that the strict S/N cuts are not preferentially dropping dusty, highly star-forming systems.
8.  **Statistical Treatment of Non-Detections:** Instead of dropping all galaxies that fail the strict 4-line S/N$\geq3$ cut (which preferentially removes passive galaxies), incorporate upper limits to retain a representative quenched denominator.
9.  **True Environment / Halo Mass Cross-Matching:** Map the galaxies to an existing SDSS group catalog (e.g., Yang or Tinker) to obtain central/satellite designations and halo masses instead of relying on the projection-vulnerable 10th-neighbor rank.
10. **Multiwavelength Gas Cross-Matching:** Cross-match the specific 6,729-galaxy gas-depletion denominator with xCOLD GASS and xGASS catalogs to evaluate true cold gas depletion vs. efficiency.
11. **Radio and X-ray Cross-Matching:** Cross-match the 5,695 massive low-sSFR hosts with FIRST/NVSS and ROSAT/Chandra archives to substitute the optical baseline with true maintenance-heating proxies.
12. **IFU Kinematic Cross-Matching:** Cross-match the 4,440 high-excitation subset with SDSS-IV MaNGA data to provide the resolved outflow velocities needed to test escape vs. recycling.

### 3. What Can Be Improved NOW Using Real Local SDSS Data Already Inventoried
*   **Structural Control Matching:** The MPA-JHU `PhotoObj` / `galSpecExtra` joins likely already contain basic structural parameters (concentration index, `fracDeV`). The nearest-neighbor Euclidean match can be immediately expanded from $(\log M_\star, z)$ to $(\log M_\star, z, C)$.
*   **Seyfert vs. Retired Classification:** The inventoried `galSpecLine` table contains H$\alpha$ equivalent widths, meaning WHAN classification or stricter EW cuts can be implemented on the existing 60,000-galaxy cache to isolate true AGN.
*   **Dust Corrections:** H$\alpha$ and H$\beta$ fluxes are already in the cached data, allowing immediate calculation of the Balmer decrement to test if dust bias affects the matched controls.
*   **Aperture Checks:** If the inventoried `galSpecExtra` contains both fiber and total SFR estimates, the central-vs-global discrepancy can be quantified immediately.

### 4. What Requires New Real Data (MUST NOT be written as a result yet)
*   **Causal AGN Feedback / Quenching:** Without time-domain models and molecular gas masses, no claim can be made that the AGN is actively depleting gas or shutting down star formation.
*   **Environmental / Halo Claims:** The 10th-neighbor index is projection-biased and collision-limited. True central/satellite dynamics and halo mass dependencies require an external group catalog.
*   **Radio Maintenance Heating:** No claims of jet-mode feedback efficiency can be made without actual radio luminosities (FIRST/NVSS) and X-ray cavity energetics.
*   **Outflow Escape Fractions:** Cannot be estimated without spatially resolved IFU kinematics (MaNGA) and halo potential depths.
*   **Cold Gas Depletion Times:** The $H\alpha$ proxy is insufficient; actual CO/HI masses (xCOLD GASS/xGASS) are required to measure depletion.

### 5. Exact Guidance for the Integrator (Safe wording/citation changes only)
*   **Preserve Boundaries:** Maintain all existing "association-only", "observational baseline", and "selection-aware" terminology. Do not escalate to causal language.
*   **Caveat the 60k Cap:** Ensure the abstract and introduction explicitly state: *"The 60,000-galaxy pilot cap is an arbitrary computational limit sequentially ordered by specObjID, and introduces survey-plate and sky-coverage biases. It is not volume-complete."*
*   **Emphasize Morphological Degeneracy:** In the interpretation of the $-1.309$ dex offset, explicitly state: *"Because the matching algorithm controls only for mass and redshift, this offset remains fully degenerate with the morphological transition from star-forming disks to passive bulges."*
*   **Citation Roles:** Ensure all references to radio, X-ray, CO, HI, IFU, and cosmological simulations (e.g., Best et al., Fabian, xCOLD GASS, SIMBA) are explicitly framed as *missing observables required for future validation*, not as support for the current optical baseline. 

### 6. No-Mock-Data Receipt and Safety Ledger
*   **Read-Only Integrity:** No files were edited, written, or deleted. No Git operations were performed.
*   **No Synthetic Data:** No mock catalogs, placeholder numbers, or toy data were proposed.
*   **No Invented Metrics:** All counts (60,000 cache, 249,917 parent, 8,146 matched pairs, -1.309 dex offset) were strictly sourced from the provided real-data TeX excerpts.
*   **No Fake Citations:** All referenced catalogs and papers (SDSS DR17, MPA-JHU, xCOLD GASS, FIRST, MaNGA, Kewley 2006) are real astrophysical literature/datasets reflecting standard community knowledge.
*   **Boundary Maintained:** The analysis strictly adhered to the instruction that literature-only sources motivate future work and do not become measured NebulaMind results.


# command_result
exit_code=0
elapsed_s=37.1
timed_out=False
finished_utc=2026-07-09T16:46:19Z

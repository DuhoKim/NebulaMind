# hwao-agy-low-cycle-27
Started UTC: 2026-07-09T17:37:02Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_27

### 1. Publication-Readiness Verdict
**RP-1 Flagship:** **Not ready for external publication in a high-impact astrophysics journal (e.g., ApJ, MNRAS) in its current form.** While the honesty regarding the association-only nature and the arbitrary 60,000-galaxy computational cap is excellent, the cap itself (selected sequentially by `specObjID`) introduces unquantified survey-plate biases. Furthermore, the lack of structural/morphological control (despite having joined `PhotoObj`, which contains standard SDSS morphological proxies) leaves the primary result (-1.309 dex sSFR offset) fundamentally degenerate with the mass-morphology relation. It reads more like an internal technical memo or a robust methodology pre-registration than a complete scientific discovery.

**Supplementary Denominator/Proxy Atlas:** **Not ready for standalone publication.** It is a highly valuable internal targeting catalog and follow-up ledger, but since it repeatedly states it is "not a causal-mechanism test," it functions better as a data-release appendix or an online dataset accompanying a future, multi-wavelength physics paper.

### 2. Top 12 Concrete Quality Improvements (Ranked by Scientific Value)

**High Value: Addressing the Primary Degeneracies (Using Existing Data)**
1. **Incorporate Structural Proxies into the Match:** The selection cascade explicitly states `PhotoObj` is joined. Extract the concentration index ($R_{90}/R_{50}$) or `fracDeV` (bulge fraction) from the existing cached `PhotoObj` data and add it as a third dimension to the variance-normalized Euclidean matching. This will explicitly test if the sSFR offset is purely a morphological bulge effect.
2. **Quantify the `specObjID` Bias:** Since the 60,000 cap is sequential by `specObjID`, plot the sky distribution (RA/Dec) or plate distribution of the cached sample against the full 249,917 parent to quantify the exact regional/survey-plate bias introduced, proving whether it skews the environment metrics.
3. **Formalize the S/N Demographics:** The retention table shows a massive drop in passive galaxies at higher line S/N. Add a figure showing the $\log M_\star$ vs. sSFR plane colored by S/N retention to explicitly visualize how the emission-line cut removes the red sequence.
4. **Refine the 10th-Neighbor Index:** The 10th-neighbor index is computed within the $0.02 < z < 0.12$ slice without a narrow line-of-sight velocity window. Use the existing redshift data to restrict the neighbor search to a physical velocity cylinder (e.g., $\pm 1000$ km/s) to reduce severe foreground/background projection effects.

**Medium Value: Strengthening the Statistical Argument**
5. **Plot the Matched Distributions:** Add a figure showing the $\log M_\star$ and redshift distributions of the BPT targets versus the matched controls to visually prove that the variance-normalized Euclidean matching successfully balanced the populations.
6. **Compare Seyfert vs. LINER Offsets:** The text notes the offset drops from -1.309 to -0.763 for the Seyfert-like subset. Explicitly calculate and report the offset for the remaining LINER/retired subset to confirm if the primary -1.309 signal is driven entirely by the low-ionization retired-galaxy tail.
7. **Consolidate Atlas Caveats:** The supplementary atlas repeats the exact same 3-arcsec fiber, S/N $\ge$ 3, and 55-arcsec collision caveats in almost every subsection. Move these to a single, rigorous "Global Sample Limitations" section to improve readability.
8. **Clarify the Mass-Bin Diagnostic:** In Atlas Section 4.5, the peak in broad BPT incidence at $11.0 \le \log(M_\star) \le 12.5$ is flagged as a selection effect. Plot the fractional retention vs. mass explicitly so readers can see the selection function driving this peak.

**Low Value: Formatting and Wording Enhancements**
9. **Soften the Defensive Tone:** The flagship abstract and text heavily repeat what the paper *does not* do (e.g., "not a volume-complete census", "not a causal claim", "arbitrary cache limit"). Condense these into a single precise limitations paragraph rather than diluting the actual findings throughout the text.
10. **Standardize "Broad Optical BPT-Selected":** Ensure this exact phrase is used consistently. In a few places, the text slips into just saying "BPT classification is associated with...".
11. **Highlight the H$\alpha$ Luminosity Proxy Drop:** In Atlas Section 4.7, the 0.66 dex drop in median H$\alpha$ luminosity is buried in the text. This is a strong quantitative baseline and should be added to the Atlas Summary table (Table 3).
12. **Specify the Variance Normalization:** Briefly define the exact variance normalization used for the Euclidean distance (e.g., "normalized by the standard deviation of the denominator sample") so the matching is perfectly reproducible from the text alone.

### 3. What Can Be Improved Now (Using Real Local SDSS Data Already Inventoried)
*   **Morphological Matching:** Using the already joined `PhotoObj` table to extract concentration ($R_{90}/R_{50}$) or `fracDeV`.
*   **Sky/Plate Bias Quantification:** Using RA/Dec/Plate/MJD from `SpecObj` to map the 60,000-galaxy footprint.
*   **Velocity-Cylinder Neighbor Index:** Using the existing spectroscopic redshifts to restrict the 10th-neighbor search to a $\Delta v$ cylinder rather than the full $z=0.02-0.12$ slice.
*   **Seyfert vs. LINER Split:** Using the existing line fluxes to isolate the low-excitation LINER/retired galaxies and report their specific sSFR offset.

### 4. What Requires New Real Data (Must Not Be Written As A Result Yet)
*   **Causal Mechanisms:** Any claim that AGN feedback *causes* the observed sSFR offset.
*   **True Environmental Density:** Halo mass, central/satellite status, or volume-complete local density (requires a proper group catalog or fiber-collision corrections).
*   **Total Gas Mass / Depletion Times:** Requires ALMA/IRAM CO observations or HI 21cm data.
*   **True AGN Bolometric Luminosity / Eddington Ratio:** Requires X-ray or robust IR data, beyond the optical emission lines which are contaminated by retired stellar populations.
*   **Resolved Outflow Kinematics:** Requires IFU data (e.g., MaNGA) to measure outflow escape velocities.

### 5. Exact Guidance for the Integrator (Safe Wording/Citation Changes Only)
*   **Do not run new SQL queries or change the 60,000-galaxy cache limit.** Work entirely within the existing generated CSV/JSON inventory.
*   **Update the matching paragraph in RP-1:** If `PhotoObj` data is available in the local CSVs, write a script to re-run the matching including concentration index. If it is not in the local CSVs, add a sentence explicitly stating: *"Although `PhotoObj` was joined to extract catalog sSFR, structural parameters like $R_{90}/R_{50}$ were not retained in the 60,000-galaxy cache, preventing morphological matching in this cycle."*
*   **Streamline the Abstract:** Remove redundant phrases like "This result is association-only, not causal" if it is already stated that "BPT classification... is an association-only measurement."
*   **Add LINER statistics:** Compute the offset for the non-Seyfert broad-BPT galaxies using the existing cached data and add it to Table 2 (Robustness ladder).
*   **Do not add any new citations** unless they directly point to the SDSS DR17 data access or the MPA-JHU catalog pipeline.

### 6. No-Mock-Data Receipt and Safety Ledger
*   **Mock Data Status:** CLEAN. Zero synthetic, mock, or placeholder data proposed. All recommended metric improvements rely strictly on the 35 CSVs and 167 JSONs currently in the local inventory.
*   **Data Invention:** CLEAN. No invented numeric values, DOIs, sample sizes, or citations were generated.
*   **Association-Only Boundary:** MAINTAINED. All guidance explicitly enforces that no causal claims be made without external X-ray/Radio/IFU data.
*   **Read-Only Constraints:** VERIFIED. No file edits, git commits, API calls, or database mutations were executed during this review. No external network requests were made. No tools were invoked.


# command_result
exit_code=0
elapsed_s=35.8
timed_out=False
finished_utc=2026-07-09T17:37:38Z

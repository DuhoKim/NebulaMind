# Gemini Advisory Fallback: Current RT Professionalization

**Marker:** `GEMINI_AGY_FALLBACK_CURRENT_RT_PROFESSIONALIZATION_20260708T120000Z`

*Note: Automated public web lookup for deep arXiv/ADS verification is unavailable in this fallback environment to prevent hallucination and respect safety boundaries. All source suggestions are labeled `DO_NOT_USE_UNTIL_VERIFIED`.*

## A. Overall Diagnosis
The current Research Topic (RT) pages fail to read like professional astronomy proposals because they conflate the internal mechanics of the NebulaMind agent runs (e.g., "wiki-method results", "source basis", "claim 2946", "ledger") with actual astrophysical science. Many cards (e.g., RP-5, RP-6, P6, p6) are meta-commentary on the literature review process rather than testable hypotheses about galaxy evolution. Professional proposals focus on the physical universe: what is the astrophysical uncertainty, what instrument and sample will measure it, what is the control or denominator, and what is the falsification criterion. 

## B. Cross-Method Redesign Principles
1. **Remove Meta-Narrative:** Eliminate all mentions of internal tooling, "claims", "ledgers", "source basis", and "wiki rebuilds". 
2. **Standardize the Proposal Anatomy:** Every scientific RT must have:
   - A declarative, professional title.
   - A single-sentence falsifiable hypothesis or objective.
   - A synthesized background (prior literature).
   - A specific remaining gap/uncertainty.
   - A rigorous data plan (named instruments, specific surveys, explicit control samples).
   - A concrete decision/falsification criterion.
3. **Segregate Methodology:** Meta-research topics evaluating the literature review itself should be distinctly categorized as "Methodological Programs" or "Appendices" so they do not dilute the astrophysical science proposals.

## C. Revision Blueprint for 18 Current RT Cards

### Method 1 Cards
**1. RP-1: A causal test of whether active galactic nucleus feedback suppresses star formation**
- **Proposed Title:** Observational constraints on the suppression of star formation by AGN feedback
- **Hypothesis:** AGN feedback mechanically and radiatively depletes the molecular gas reservoir, causing a statistically significant drop in star formation relative to mass-matched inactive controls.
- **Prior Sources:** `DO_NOT_USE_UNTIL_VERIFIED` (arXiv:2604.15438, 2512.05584).
- **Literature Establishes:** `UNCITED_NOT_USABLE` (Needs local verification of the exact mechanisms cited).
- **Gap:** Direct causal linking of AGN power to star-formation history over a statistically complete sample.
- **Data Plan:** SDSS-MaNGA/MUSE for spatially resolved SFR; ALMA CO for gas mass; Chandra/XMM for AGN power.
- **Decision Criterion:** Statistically significant reduction in specific SFR in AGN hosts vs. controls.
- **Risks:** Correlation vs. causation; matching controls properly.

**2. RP-2: Locating the regime in which internal and environmental quenching separate**
- **Proposed Title:** Disentangling internal mass quenching from environmental quenching across cosmic time
- **Hypothesis:** Environmental quenching dominates below a critical halo mass, while internal (AGN/stellar) quenching dominates above it, with the transition epoch occurring near cosmic noon.
- **Prior Sources:** `DO_NOT_USE_UNTIL_VERIFIED` (arXiv:2511.02964, 2606.25367).
- **Literature Establishes:** `UNCITED_NOT_USABLE`.
- **Gap:** The exact mass-redshift parameter space where the dominant quenching mechanism swaps.
- **Data Plan:** SDSS/GAMA (low-z), COSMOS/CANDELS/JWST (z~2), DESI/Euclid (large scale structure).
- **Decision Criterion:** A measurable inflection point in quenched fraction models mapping stellar mass to halo mass.
- **Risks:** Misattributing pre-processing in groups to cluster environments.

**3. RP-3: An observed heating-versus-cooling balance for maintenance quenching**
- **Proposed Title:** Empirical constraints on the AGN maintenance heating cycle in massive halos
- **Hypothesis:** Mechanical energy injected by radio-mode AGN balances the radiative cooling of the hot intracluster medium over the AGN duty cycle.
- **Prior Sources:** `DO_NOT_USE_UNTIL_VERIFIED` (arXiv:2112.07672, 2008.00005).
- **Literature Establishes:** `UNCITED_NOT_USABLE`.
- **Gap:** Extrapolating instantaneous X-ray cavity measurements to a time-averaged duty cycle.
- **Data Plan:** Chandra/XMM-Newton/eROSITA (cooling); VLA/LOFAR (radio power).
- **Decision Criterion:** The ratio of time-averaged cavity power to X-ray cooling luminosity equals unity.
- **Risks:** Systematics in estimating cavity buoyancy times and total jet power.

**4. RP-4: A prioritised evidence-gap programme for the narrative-only sections**
- **Demote/Reframe:** This is a meta-process card. Reframed as an appendix on "Future Observational Directions" rather than a standalone astrophysical proposal.

**5. RP-5: Robustness of the synthesis to evidence accounting**
- **Demote/Reframe:** This is a meta-process card. Move to "Methodology Appendix."

**6. RP-6: Pre-registered acceptance criteria for AGN-feedback conclusions**
- **Demote/Reframe:** This is a meta-process card. Merge with RP-5 into "Methodology Appendix."

### Method 2 Cards
**7. P1: Quantifying the permanence of AGN-driven gas removal: an escape-versus-recycling census**
- **Proposed Title:** Escape versus recycling: the ultimate fate of AGN-driven multiphase outflows
- **Hypothesis:** A significant fraction of AGN-driven outflowing gas remains gravitationally bound and recirculates, limiting the permanence of AGN quenching.
- **Prior Sources:** `DO_NOT_USE_UNTIL_VERIFIED` (arXiv:1706.08987, 2512.05584).
- **Literature Establishes:** `UNCITED_NOT_USABLE`.
- **Gap:** The ratio of outflow velocity to halo escape velocity across a representative sample.
- **Data Plan:** MUSE/MaNGA (kinematics), ALMA (cold gas), JWST/NIRSpec (z>2), mass-matched controls.
- **Decision Criterion:** Monotonic escaped-fraction relation exceeding recycling above a critical mass threshold.
- **Risks:** Difficulty in observing the diffuse circumgalactic medium.

**8. P2: An observational bound on AGN maintenance heating: cavity enthalpy versus cooling luminosity**
- **Proposed Title:** (Merge with RP-3 as they address the exact same hypothesis and data plan).

**9. P3: Measuring the coupling efficiency of radio-mode jets to galaxy gas**
- **Proposed Title:** Environmental dependence of radio-jet coupling efficiency in host galaxies
- **Hypothesis:** Radio-mode jets deposit mechanical power into the ISM with an efficiency that depends heavily on the local ambient density and environment.
- **Prior Sources:** `DO_NOT_USE_UNTIL_VERIFIED` (arXiv:2009.11175, 0901.1880).
- **Literature Establishes:** `UNCITED_NOT_USABLE`.
- **Gap:** Quantifying the distribution of coupling efficiencies (energy deposited vs jet power).
- **Data Plan:** VLA/LOFAR/MeerKAT (jets); Chandra (work); MaNGA/MUSE (ISM shock ratios).
- **Decision Criterion:** Measured coupling efficiency distribution matches or refutes hydrodynamical simulation priors.
- **Risks:** High uncertainty in extracting kinetic power from radio luminosities.

**10. P4: Testing the generality of M51-scale kinetic and positive feedback**
- **Proposed Title:** The frequency and impact of positive AGN feedback in the local universe
- **Hypothesis:** Jet-induced gas compression (positive feedback) triggers star formation at a rate significant enough to offset local quenching in a measurable fraction of nearby active galaxies.
- **Prior Sources:** `DO_NOT_USE_UNTIL_VERIFIED` (arXiv:2604.15438).
- **Literature Establishes:** `UNCITED_NOT_USABLE`.
- **Gap:** Whether the positive feedback observed in M51 is a ubiquitous phenomenon or a statistical outlier.
- **Data Plan:** ALMA (PHANGS), MUSE, MaNGA for nearby AGN and matched controls.
- **Decision Criterion:** Frequency of positive feedback signatures exceeds a predetermined population threshold.
- **Risks:** Over-claiming the global impact of locally constrained positive feedback.

**11. P5: Locating the stellar-to-AGN feedback transition mass in quenching**
- **Proposed Title:** Determining the transition mass from stellar to AGN-dominated feedback
- **Hypothesis:** There exists a distinct stellar mass threshold above which stellar feedback momentum budgets fail, necessitating AGN feedback to maintain quiescence.
- **Prior Sources:** `DO_NOT_USE_UNTIL_VERIFIED` (arXiv:2512.05584, 2605.03008).
- **Literature Establishes:** `UNCITED_NOT_USABLE`.
- **Gap:** The exact mass at which the crossover occurs observationally.
- **Data Plan:** DESI/MOSDEF (outflows), JWST (high-z), GAMA/COSMOS.
- **Decision Criterion:** A sharp crossover in the mass-loading vs. halo mass plane coincident with rising AGN incidence.
- **Risks:** Confounding effects from halo mass vs stellar mass mapping.

**12. P6: Strengthening evidence traceability**
- **Demote/Reframe:** This is a meta-process card. Move to "Methodology Appendix."

### Method 3 Cards
**13. p1: Isolating the causal contribution of AGN feedback to central-galaxy quenching**
- **Proposed Title:** (Merge with RP-1).

**14. p2: A tracer-resolved, common-denominator census of AGN-driven outflows**
- **Proposed Title:** A multiphase kinematic census of AGN-driven outflows
- **Hypothesis:** Outflow occurrence and mass-loading are strongly dependent on the observed gas phase (ionized, neutral, molecular).
- **Prior Sources:** `DO_NOT_USE_UNTIL_VERIFIED`.
- **Literature Establishes:** `UNCITED_NOT_USABLE`.
- **Gap:** Harmonizing outflow metrics across different tracers.
- **Data Plan:** Multi-wavelength IFU (MUSE, ALMA).
- **Decision Criterion:** Significant statistical divergence in outflow properties depending on the phase tracer.
- **Risks:** Cross-calibration of mass estimates between different gas phases.

**15. p3: Distinguishing reservoir removal from inefficient star formation**
- **Proposed Title:** Distinguishing gas depletion from suppressed star formation efficiency in quenched galaxies
- **Hypothesis:** Quenching is driven primarily by the removal of the molecular gas reservoir rather than a drop in the star formation efficiency of existing gas.
- **Prior Sources:** `DO_NOT_USE_UNTIL_VERIFIED`.
- **Literature Establishes:** `UNCITED_NOT_USABLE`.
- **Gap:** Deconvolving gas fraction from star formation efficiency (SFE).
- **Data Plan:** ALMA (gas mass), optical/UV (SFR).
- **Decision Criterion:** A measured dominant drop in gas fraction rather than SFE in quenched populations.
- **Risks:** Uncertainties in the CO-to-H2 conversion factor (alpha_CO).

**16. p4: An observational determination of the maintenance-heating duty cycle**
- **Proposed Title:** (Merge with P2 and RP-3).

**17. p5: Forward-modeled validation of simulation feedback predictions**
- **Proposed Title:** Observational validation of cosmological simulation feedback prescriptions
- **Hypothesis:** Forward-modeled synthetic observations of cosmological simulations will diverge from real multi-wavelength data if the subgrid feedback models are fundamentally inaccurate.
- **Prior Sources:** `DO_NOT_USE_UNTIL_VERIFIED`.
- **Literature Establishes:** `UNCITED_NOT_USABLE`.
- **Gap:** Direct, apples-to-apples comparison of simulations to observations using instrumental mock pipelines.
- **Data Plan:** IllustrisTNG/EAGLE synthetic observables vs. SDSS/MUSE.
- **Decision Criterion:** Residuals between synthetic and real observations exceed observational errors.
- **Risks:** Degeneracies in subgrid models yielding similar macroscopic observables.

**18. p6: Rebalancing the multi-channel evidence base**
- **Demote/Reframe:** This is a meta-process card. Move to "Methodology Appendix."

## D. Top 6 Prioritized Proposals
1. **P1 (Escape vs. Recycling):** Directly addresses the physical permanence of feedback, a highly debated and critical topic in galaxy evolution.
2. **P5 (Transition Mass):** Addresses the fundamental boundary between stellar and AGN feedback scaling relations.
3. **RP-1 (AGN Suppression Causal Test):** The core premise of AGN feedback; framed excellently with a complete multi-wavelength data plan.
4. **P3 (Radio-Jet Coupling):** Targets the physics of the maintenance mode with a strong reliance on measurable cavities and shock diagnostics.
5. **p3 (Depletion vs SFE):** A clean, testable hypothesis about the nature of the star-forming reservoir in quenched galaxies. 
6. **RP-2 (Internal vs Environmental):** Connects the internal galactic physics to the larger cosmological web, leveraging premier next-gen datasets (JWST, Euclid, DESI).

## E. DO_NOT_USE_UNTIL_VERIFIED
- All arXiv IDs and external links (e.g., `arXiv:2604.15438`, `arXiv:2512.05584`, `arXiv:2112.07672`, `arXiv:2008.00005`, etc.)
- Specific numerical claim IDs (e.g., `claim 2946`, `claim 2929`)
- Method 1/2/3 local html references (e.g., `../prose-evidence-trust-deepening...`)

`GEMINI_WEB_RT_DEEP_RESEARCH_OUTPUT_DONE`

# gemini-agy-deep-cycle-20
Started UTC: 2026-07-09T05:10:23Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

```markdown
GEMINI_AGY_DEEP_REVIEW_CYCLE_20

# Overview
This quality review evaluates the flagship manuscript draft (`flagship_rp1`) and the companion supplementary atlas (`supplementary_denominator_atlas`). The assessment focuses on identifying overclaims, incorrect citation roles, missing observables, and instances where sample/proxy properties might be misinterpreted as physical results.

---

# 1. Critical Issues & Proposed Wording Edits

## Flagship Paper (`flagship_rp1`)

### Issue 1: Conflation of BPT-selected galaxies with physical AGN hosts
*   **Severity**: Major
*   **Risky Sentence (Section 3)**:
    > "The analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects."
*   **Skeptical Critique**: Using "targets" or "galaxies" interchangeably with BPT classification can cause readers to assume these are all active galactic nuclei. Because retired stellar populations and LINER-like low-ionization lines contaminate these selections, the text must strictly emphasize the proxy nature of the selection.
*   **Propose Wording**:
    > "The analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected galaxy proxies, and 67 unclassified objects."

### Issue 2: Implication of star formation suppression (quenching) from matching
*   **Severity**: Major
*   **Risky Sentence (Section 5)**:
    > "The preferred broad optical BPT comparison gives a large negative catalog-sSFR offset for the broad optical BPT-selected galaxies relative to star-forming controls."
*   **Skeptical Critique**: Labeling this as a "broad optical BPT comparison" without immediately restating that it is a catalog-sSFR offset in an aperture-limited sample can mislead readers into interpreting the offset as galaxy-wide physical quenching.
*   **Propose Wording**:
    > "The preferred comparison yields a large negative catalog-sSFR offset within the 3-arcsec fiber aperture for the broad optical BPT-selected galaxies relative to star-forming controls, which may reflect different spatial profiles of star formation rather than total galaxy quenching."

---

## Supplementary Atlas (`supplementary_denominator_atlas`)

### Issue 3: Interpretative leap on environmental "low-sSFR fraction"
*   **Severity**: Major
*   **Risky Sentence (Section 3.1)**:
    > "The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000)."
*   **Skeptical Critique**: Quoting these fractions without immediate qualification risks readers interpreting them as physical environmental quenching rates. These are strictly population fractions *conditional* on a selection-biased, non-volume-complete emission-line sample.
*   **Propose Wording**:
    > "Within our selection-limited, non-random emission-line denominator, the high-index quartile has a conditional low-sSFR fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000); these values are internal denominator fractions and do not represent absolute quenching rates in a volume-complete population."

### Issue 4: Conflating "AGN/composite fraction" with physical duty cycle
*   **Severity**: Major
*   **Risky Sentence (Section 3.2)**:
    > "This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement."
*   **Skeptical Critique**: The term "duty-cycle denominator" implies that we are tracing the actual accretion lifetime of active black holes. Because BPT lists are contaminated by LINERs and retired stellar populations (which are long-lived states), calling it a "duty cycle" is an overclaim.
*   **Propose Wording**:
    > "This provides an optical emission-line selection denominator for potential future X-ray and radio follow-up, not a physical duty-cycle or heating-to-cooling measurement."

---

# 2. Citation Role Audit

The citations in both drafts must be strictly partitioned. References used to document the methods and datasets in the current analysis must not be mixed with references motivating missing physical observables.

| Citation | Intended Section / Topic | Current Role in Text | Audited Correct Role | Review Status |
| :--- | :--- | :--- | :--- | :--- |
| **Kauffmann et al. (2003bpt)** | Flagship / Supp. Selection | Methodology Support (BPT) | **Methodology Support** (Valid) | **OK** |
| **Catinella et al. (2018) / Saintonge et al. (2017)** | Atlas 3.6 / 3.7 (Gas fractions) | Method / Reference context | **Future-Data Motivation Only** | **OK** (Accurately isolated as missing CO/HI observables) |
| **Dave et al. (2019) / Nelson et al. (2019)** | Atlas 3.8 (Simulations) | Target comparison | **Future-Data Motivation Only** | **OK** (Correctly framed as validation requirements, not comparisons) |
| **Best et al. (2005) / Fabian (2012)** | Atlas 3.2 / 3.4 (Radio/X-ray) | Theoretical context | **Future-Data Motivation Only** | **OK** (Correctly framed as missing multiwavelength measurements) |

---

# 3. Missing Observables & Data Diagnostics

Both manuscripts discuss galaxy evolution trends. However, because they are based purely on a cached, non-volume-complete SDSS spectroscopic sample, the following missing observables must be explicitly labeled as **unobserved requirements** for any physical feedback or environmental model testing:

1.  **Resolved Kinematics & Outflow Velocities**: The current data cannot distinguish between quiescent gas reservoirs and active outflows (requires resolved ionized/molecular kinematics).
2.  **Multiphase Gas Census (CO/HI)**: Total gas depletion times and gas fractions are unconstrained (requires radio/sub-mm follow-up).
3.  **Group Catalogs & Halo Mass Identifiers**: Environmental projections (10th-neighbor index) suffer from fiber collisions and lack halo context (requires satellite/central designations).
4.  **Aperture/Morphology Corrections**: The 3-arcsec fiber creates a mismatch when comparing bulge-dominated hosts to disk-dominated controls (requires resolved spatial profiles or global star-formation tracers).
5.  **Simulation Mocks with Mock Selection**: Comparisons to cosmological simulations are invalid without processing simulation outputs through identical optical S/N and fiber-aperture selection pipelines.

---

# 4. Ranked Integrator Actions

To prepare the manuscript package for a science review, the following actions are ranked by priority:

1.  **[High Priority] Refine BPT Terminology**: Replace terms like "BPT galaxies" and "duty cycle" with "BPT-selected emission-line proxies" to prevent readers from mistaking emission-line classifications for physical accretion states.
2.  **[High Priority] Explicitly Quantify the Selection Bias in Abstract**: Add a sentence to the Abstract of the Flagship draft stating: *"The four-line S/N $\geq 3$ threshold preferentially retains star-forming systems while discarding passive hosts, making the matched offset conditional on this selection."*
3.  **[Medium Priority] Restructure the Environmental Baseline Section**: Revise the discussion of the 10th-neighbor index in Section 3.1 to clarify that it is an internal ordinal ranking within a non-volume-complete subset and cannot be compared to physical galaxy densities.
4.  **[Medium Priority] Standardize the Warning Headers**: Add an explicit, standardized warning callout at the beginning of each Atlas section indicating that the values are baseline diagnostic tables, not physical evolution metrics.

---

# 5. Safety Ledger

*   **Public Pages / Roots**: None accessed or modified.
*   **Database / SQL Operations**: None executed.
*   **Git / Deploys / Configs**: No git changes, no script executions, and no deployment modifications were performed.
*   **Local Files**: Read-only review of `rp1_flagship_polished.tex` and `supplementary_denominator_atlas.tex` performed. No edits were written to the filesystem.
```


# command_result
exit_code=0
elapsed_s=13.5
timed_out=False
finished_utc=2026-07-09T05:10:37Z

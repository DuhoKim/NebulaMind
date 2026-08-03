# gemini-agy-deep-cycle-9
Started UTC: 2026-07-09T03:54:16Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_09

## 1. Executive Summary & Critical Review

This deep quality review evaluates the **Flagship Paper Draft (RP-1)** and the **Supplementary Denominator/Proxy Atlas** for Cycle 9. The separation of the 9-paper integrated run into one flagship analysis of SDSS DR17 matched controls and one supplementary atlas of observational baselines is a major scientific improvement that correctly positions the work as an association study rather than a causal feedback analysis. 

However, several lingering terms, citation mappings, and proxy descriptions carry a minor-to-major risk of misleading readers into assuming physical mechanisms (e.g., causal active galactic nucleus (AGN) quenching) or treating literature references as methodological validation instead of future-data motivation.

---

## 2. Issues and Proposed Text Corrections

### Issue 1: physical vs. observational labelling in classification ("Broad BPT AGN")
*   **Severity**: Major
*   **Location**: `rp1_flagship_polished.tex` (Section 3, Table 2, and throughout)
*   **Risky Sentence / Term**:
    *   *Abstract & Section 3*: "...yields 8,146 pairs of broad optical BPT AGN..."
    *   *Table 2 (Row 1 & 4)*: "Broad BPT AGN, S/N$\geq3$..." and "Broad BPT AGN, S/N$\geq10$..."
*   **Critique**: Despite the caveats stating that retired stellar populations and LINER-like emission contaminate this sample, using the term "Broad BPT AGN" in tables and summary statistics re-introduces the causal/physical label as an active variable. Since BPT selects based on optical emission-line ratios (which can be powered by post-AGB stars in retired bulges rather than supermassive black hole accretion), the target sample should be referred to purely by its observational selection.
*   **Proposed Wording**:
    *   *Abstract/Text*: Replace "broad optical BPT AGN" with "broad optical BPT excitation candidates" or "BPT-selected high-excitation hosts".
    *   *Table 2*: Replace "Broad BPT AGN" with "Broad BPT-selected targets" or "Broad BPT-excitation targets".

---

### Issue 2: Citation Role Ambiguity (Literature Cited as "Needed" Observables)
*   **Severity**: Minor
*   **Location**: `supplementary_denominator_atlas.tex` (Sections 3.1 through 3.8)
*   **Risky Sentence**:
    *   *Section 3.1*: "These are still needed for a future environmental test \citep{peng2010,wetzel2013,dekel2006}."
    *   *Section 3.2*: "These are still needed for a future maintenance-heating test \citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}."
*   **Critique**: The parenthetical citations are positioned immediately after bulleted lists of physical observables (e.g., "X-ray cavity measurements," "group catalogues"). A reader might misinterpret these citations as the source of the methods/data used in this work, or as direct physical validation of the current baseline, whereas they only represent scientific motivation for why those missing datasets are needed in future work.
*   **Proposed Wording**:
    *   *Alternative*: "These physical observables are not present in our SDSS-only data; the scientific motivation for adding them is discussed in prior work (e.g., \citealt{peng2010,wetzel2013,dekel2006} for environmental indicators)."
    *   *Alternative (Section 3.2)*: "These physical parameters are not measured in this study; they represent crucial future multiwavelength inputs motivated by studies of heating-to-cooling balances (e.g., \citealt{best2005,fabian2012})."

---

### Issue 3: Title and residual naming of "Feedback Transition Mass"
*   **Severity**: Minor / Optional
*   **Location**: `supplementary_denominator_atlas.tex` (Section 3.5 & Table 3)
*   **Risky Sentence / Header**:
    *   *Section 3.5 Title*: "Mass-bin diagnostic: low-sSFR and optical AGN incidence"
    *   *Table 3 (Row 5)*: "Mass bin | low-sSFR and AGN by $M_\star$ bin | gas fractions; baryon deficits; halo masses; feedback observables | selection diagnostic"
*   **Critique**: While the text of Section 3.5 is well-caveated (clarifying that the peak in massive hosts is a selection-function artifact where BPT cuts remove passive quiescent galaxies), the original draft title was `m2_p3_feedback_transition_mass`. In the supplementary index (Table 3), the label "Mass bin" is used. To avoid any association with a physical "feedback transition mass" or an evolutionary boundary, the header and summary should explicitly mention selection bias.
*   **Proposed Wording**:
    *   *Section 3.5 Title*: "Mass-bin selection diagnostic: low-sSFR and optical incidence variations"
    *   *Table 3 (Row 5 Role)*: Change "selection diagnostic" to "selection-biased denominator diagnostic".

---

### Issue 4: H-alpha Luminosity as Star-Formation Rate Proxy in Quiescent Denominators
*   **Severity**: Major
*   **Location**: `supplementary_denominator_atlas.tex` (Section 3.7 - Gas Depletion)
*   **Risky Sentence**:
    *   "...and the median H-alpha luminosity proxy is 40.06... The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies."
*   **Critique**: In low-sSFR, BPT-selected galaxies (especially LINERs/retired systems), H-alpha emission can be dominated by old stellar populations (e.g., post-AGB stars) or shocks rather than active star formation. Comparing the raw or catalog-corrected H-alpha luminosities of BPT-selected hosts directly to star-forming galaxies as a linear indicator of SFR depletion is physically risky.
*   **Proposed Wording**:
    *   "The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming control galaxies. However, in these low-sSFR environments, H-alpha emission ceases to be a clean tracer of young star formation and is heavily contaminated by retired stellar populations or shock excitation; this discrepancy underscores the need for CO- or dust-derived gas masses."

---

## 3. Observational and Missing-Data Checklist

Any future expansion of these proxy notes into physical results requires replacing target denominators with active measurements. The following table maps the missing data requirements identified across both documents:

| Topic | Missing Data Type | Recommended Observational Source / Sim Mock |
| :--- | :--- | :--- |
| **Environment** | Group/Halo Catalogues | SDSS group catalogs (e.g., Yang et al.) to identify central/satellite status; fiber-collision corrections |
| **Maintenance Heating** | X-ray / Radio jet energy | X-ray cavity/cooling-flow observations (e.g., Chandra) and radio jet powers (e.g., VLA/JVLA) |
| **Outflows** | Kinematics | Resolved ionized/neutral/molecular outflow kinematics (e.g., MaNGA, ALMA, JWST) |
| **Gas Depletion** | Cold/Neutral Gas | CO (1-0) or dust-continuum measurements (e.g., xCOLD GASS, ALMA) to estimate molecular gas mass |
| **Simulations** | Synthetic Observables | Mocks passed through the exact 3-arcsec fiber aperture and 4-line S/N $\geq 3$ selection cuts (e.g., IllustrisTNG, EAGLE, SIMBA) |

---

## 4. Ranked Integrator Actions

If a subsequent cycle is initiated to refine the text before human/scientific review:

1.  **Refine Terminology (Flagship & Supplement)**: Strip remaining physical labels like "Broad BPT AGN" in tables/legends and replace them with observational terms ("BPT-excitation targets").
2.  **Disambiguate Citations (Supplement)**: Rephrase sentences ending with `\citep{...}` in Section 3 of the supplement to state clearly that these references represent the physical *motivation* for missing data, rather than method support or validation.
3.  **Enhance H-alpha Caveat (Supplement Section 3.7)**: Add a sentence explicitly warning that H-alpha in low-sSFR hosts is contaminated by post-AGB stars and does not translate directly to a star-formation rate or gas depletion efficiency.

---

## 5. Safety Ledger

*   **Public pages modified**: None.
*   **Databases queried / written**: None (local text-only analysis).
*   **Repository commits / pushes**: None.
*   **Deployment status**: Unchanged.
*   **External manuscript submissions**: None.
*   **Scope of changes**: Read-only review of local draft tex files.


# command_result
exit_code=0
elapsed_s=14.7
timed_out=False
finished_utc=2026-07-09T03:54:31Z

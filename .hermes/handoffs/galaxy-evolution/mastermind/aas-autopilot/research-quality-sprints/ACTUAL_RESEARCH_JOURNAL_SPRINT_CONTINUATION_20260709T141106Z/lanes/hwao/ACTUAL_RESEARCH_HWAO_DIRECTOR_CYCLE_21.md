# hwao-agy-low-cycle-21
Started UTC: 2026-07-09T16:53:30Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_21

### Publication-Readiness Verdict

**RP-1 Flagship:** **Ready for submission as a Guarded Pilot.** 
The flagship succeeds by strictly bounding its claims to an association within a selection-biased optical denominator. Its explicit acknowledgement of the 60,000-galaxy computational cap, the S/N$\geq$3 preferential removal of passive galaxies, and the lack of morphology/aperture controls ensures it does not overstate its findings. It is a robust, falsifiable pilot study of the BPT-sSFR association, provided the causal boundaries are maintained.

**Supplementary Denominator/Proxy Atlas:** **Ready as a Follow-up Checklist.**
The supplement is correctly framed as a baseline target list rather than a collection of physical-mechanism papers. By uniting the eight entries under the shared limitations of the optical denominator and explicitly listing the missing observables required for physical inference, it serves as a scientifically valuable roadmap for future multiwavelength campaigns.

---

### Top 12 Concrete Quality Improvements (Ranked by Scientific Value)

1. **Flagship:** Consolidate the discussion of the 55-arcsec fiber collision limit and 3-arcsec aperture bias into a dedicated "Observational Systematics" section to prevent these critical caveats from being diluted.
2. **Flagship:** Expand the discussion on the Seyfert-like proxy sensitivity check. The reduction of the offset from -1.309 dex to -0.763 dex is a major finding; explicitly state how much of the primary offset is driven by the low-ionization LINER/retired branch.
3. **Supplement:** Unify the scattered "missing observables" lists across the 8 entries into a single, cohesive requirements matrix (expanding Table 3) for future multiwavelength campaigns to emphasize it is one integrated atlas.
4. **Flagship:** Enhance Table 1 (Selection cascade) by explicitly quantifying the preferential loss of passive galaxies (e.g., tabulating the retention of the $-12<\log {\rm sSFR}<-11$ bin vs the $-10<\log {\rm sSFR}<-9.5$ bin) alongside the aggregate counts.
5. **Supplement:** Reinforce in the "Relative neighbor-count baseline" section that the 10th-neighbor index is explicitly *not* a proxy for halo mass due to the 55-arcsec fiber collision limit, to preempt misinterpretation.
6. **Flagship:** Move the median absolute separations of the matched control (0.0045 dex in mass, 0.00021 in redshift) from Section 3 to the Abstract to immediately establish the quality of the pairing.
7. **Flagship:** Clarify that structural proxies (e.g., `fracDeV` or concentration index) are entirely absent from the matching criteria, heavily underlining the mass-morphology relation degeneracy.
8. **Supplement:** Enforce the standardized terminology "broad optical BPT-selected galaxies" strictly across all 8 sub-entries to prevent unintended subclass inference where Kewley cuts are not applied.
9. **Flagship:** Ensure the 60,000-galaxy cap is consistently referred to as a "local workflow/computational limit" in all sections, removing any risk of it being perceived as a physically motivated threshold.
10. **Supplement:** Audit all citations in the 8 notes to guarantee they are explicitly framed as "methodological pointers to missing observables" rather than validation of the SDSS optical denominator.
11. **Flagship:** State the physical scale distribution (1.2–6.5 kpc) of the 3-arcsec fiber more prominently when discussing the central-to-global sSFR mismatch.
12. **Both:** Perform a final sweep to ensure all findings are strictly described as "association-only" within the stated optical denominator, purging any residual causal language regarding quenching, feedback, or gas depletion.

---

### What Can Be Improved Now (Using Real Local SDSS Data Already Inventoried)

- **Structural Proxies:** If variables like `fracDeV` or concentration indices (e.g., R90/R50) are already present in the joined `PhotoObj` or `galSpecExtra` tables, their median differences between the targets and controls can be computed and reported to quantify the extent of the mass-morphology degeneracy, *without* adding them to the matching algorithm.
- **Seyfert vs. LINER Counts:** The exact counts of galaxies falling into the Kewley Seyfert-like region versus the LINER/retired region within the 8,146 broad optical BPT-selected targets can be tabulated using the already cached emission-line fluxes.
- **Passive Fraction Loss:** The exact numeric retention rates of the specific sSFR bins (33.6% vs 94.9%) already mentioned can be formalized into a table showing the demographic shift of the denominator before and after the S/N$\geq$3 cut.

---

### What Requires New Real Data (Must NOT Be Written as a Result Yet)

- **Causal Mechanisms:** Any claim that the broad optical BPT classification *causes* the observed -1.309 dex sSFR offset.
- **Multiwavelength Measurements:** Gas fractions (CO/HI), radio jet power/coupling efficiency, X-ray cavity energetics, or outflow escape velocities. These are explicitly missing and must remain categorized as future follow-up targets.
- **Environment and Halo Dynamics:** True halo mass, central/satellite classifications, physical volume density, or corrected group catalogs. The 10th-neighbor index remains an internal ordinal rank only.
- **Global Star Formation:** Galaxy-wide sSFR measurements that account for extended disk star formation outside the 3-arcsec fiber at low redshift.
- **Volume-Complete Extrapolations:** Luminosity functions, mass functions, or absolute volume densities derived from the 60,000-galaxy capped sample.

---

### Exact Guidance for the Integrator: Safe Wording/Citation Changes Only

- **No New Data:** Do not fetch, invent, or inject new sample sizes, values, or metrics. Limit adjustments to formatting, clarity, and the structural improvements listed above.
- **Strict Terminology:** Globally find-and-replace any loose usage of "AGN" with "broad optical BPT-selected galaxies" or "Seyfert-like" depending on the explicit cut applied, ensuring the optical excitation classification is never conflated with bolometric AGN luminosity.
- **Citation Guardrails:** Ensure that all references to radio, X-ray, CO, HI, and simulations (e.g., `best2005`, `xcoldgass2017`, `simba2019`) are strictly fenced within sentences describing *missing* future follow-up requirements. They must not be used to validate the current SDSS optical findings.
- **Caveat Frontloading:** Ensure the fiber collision, fixed-aperture bias, and cache-cap limitations are stated as fundamental denominator properties, not as secondary footnotes.

---

### No-Mock-Data Receipt and Safety Ledger

- **Mock Data:** 0 mock, synthetic, fake, or placeholder data points used or proposed.
- **Invented Values:** 0 invented numbers, sample sizes, citations, URLs, DOIs, arXiv IDs, or ADS bibcodes introduced. All values reference the provided text and inventory.
- **System Safety:** Verified read-only execution. No DB/API/wiki edits made. No git commits, pushes, or history rewrites performed. No public pages or live roots touched. No cron jobs modified. No credentials read.
- **Inventory Bounds:** All guidance is strictly constrained to the 60,000-galaxy pilot cap, the 9 integrated TeX files, 35 CSVs, 167 JSONs, and 43 PDFs documented in the local inventory.


# command_result
exit_code=0
elapsed_s=40.8
timed_out=False
finished_utc=2026-07-09T16:54:10Z

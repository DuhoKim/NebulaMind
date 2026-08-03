# hwao-agy-low-cycle-36
Started UTC: 2026-07-09T18:46:46Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_36

Here is the paper-quality triage plan for cycle 36, conducted in strict read-only review mode following the real-data-only policy.

### Publication-Readiness Verdict

**RP-1 Flagship (SDSS BPT/sSFR Pilot)**
**Verdict: Ready for submission as a rigorous association-only pilot or research note.**
The manuscript successfully maintains strict discipline around its limitations. By explicitly framing the 60,000-galaxy subset as a fixed-size, non-random cache and deliberately avoiding causal language regarding feedback or quenching, the paper is methodologically sound. The transparent handling of the aperture-morphology degeneracy and the explicit acknowledgment that it lacks structural matching makes it a highly credible baseline study.

**Supplementary Denominator/Proxy Atlas**
**Verdict: Ready for submission as a companion resource.**
The atlas correctly positions the eight prior proposals as unified observational baselines rather than standalone physical results. By clearly itemizing the "missing observables" for each target vector, it acts as a robust, falsifiable follow-up checklist for future multiwavelength and simulation work without overclaiming the current optical data.

---

### Top 12 Concrete Quality Improvements (Ranked by Scientific Value)

1. **Abstract Clarity on Selection Bias (Flagship):** Explicitly state in the abstract that the 60,000-galaxy cache is ordered sequentially by `specObjID`, which introduces survey-plate and sky-coverage biases, preventing volume-complete inferences.
2. **Physical Scale of Aperture Bias (Flagship):** Elevate the mention of the 1.2–6.5 kpc physical scale subtended by the 3-arcsec fiber at $0.02<z<0.12$ into the abstract to immediately contextualize the central-fiber proxy limitation.
3. **Unify the Missing Observables (Atlas):** While Table 3 condenses the follow-up menu, ensure each of the eight subsection introductions explicitly references Table 3 to reinforce that they share the same optical limitations.
4. **Clarify the Seyfert-like Proxy (Flagship):** Ensure the text explicitly reiterates that the Kewley et al. (2006) demarcation used for the Seyfert-like proxy is an excitation cut that removes LINER/retired galaxies, not a direct measurement of accretion power.
5. **Fiber Collision Caveat Prominence (Atlas):** Ensure the 55-arcsec fiber collision limit is prominently mentioned in the abstracts or introductions of both the "Relative neighbor-count" and "Radio-jet environment" sections, as it directly biases the 10th-neighbor index in dense regions.
6. **Explicitly Define the Control Demarcation (Flagship):** Clearly state in the abstract or early introduction that the "star-forming controls" are strictly defined by falling below the conservative Kauffmann et al. (2003) demarcation.
7. **Reinforce Association-Only Language (Atlas):** Audit the atlas to ensure words like "effect," "drives," or "causes" are universally replaced with "association," "incidence," or "offset."
8. **Clarify the Baseline Metric (Atlas):** In the Mass Bin section, explicitly state that the 11.0–12.5 log mass peak is a selection-function artifact of the S/N$\geq$3 cut preferentially removing passive galaxies, not a physical transition threshold.
9. **Elaborate on Variance-Normalized Matching (Flagship):** Briefly clarify in the text why variance-normalized Euclidean matching in $(\log M_\star,z)$ space was chosen over Mahalanobis distance or propensity score matching (e.g., transparency of the rule).
10. **Address Unclassified Objects (Flagship):** Briefly clarify in the main text why the 67 unclassified objects are retained in the denominator counts but excluded from the matched control pairing, ensuring full accounting of the 60,000 cohort.
11. **Future Multiwavelength Context (Atlas):** In the missing observables sections, safely cite the generic classes of future surveys (e.g., "future resolved ALMA CO mapping" or "eROSITA X-ray depths") that would satisfy the requirements, strictly as literature motivation, not as current data.
12. **Tighten Section Cross-References (Both):** Ensure the flagship directly points to specific sections of the atlas for the multiwavelength follow-up requirements, strengthening their connection as a joint publication.

---

### What Can Be Improved Now (Using Local Real SDSS Data)
These improvements only require textual, structural, or framing adjustments to the current draft based on data already inventoried:
* Strengthening the "association-only" language across both drafts.
* Clarifying the definitions of the matching procedures, the Kauffmann/Kewley demarcations, and the specific redshift/aperture limitations.
* Emphasizing the `specObjID` selection bias and the 55-arcsec fiber collision limitations.
* Unifying and cross-referencing the "missing observables" tables and lists.

### What Requires New Real Data (Must NOT Be Written as Results)
These elements remain strictly out of bounds for the current manuscripts and must only be discussed as future follow-up:
* Any claim regarding a causal link between BPT classification and physical quenching, feedback, or gas depletion.
* Derivations of volume-complete absolute densities, luminosity functions, or halo mass functions.
* Measurements of structural morphology (e.g., `fracDeV`, concentration index) or aperture fraction controls.
* Separation of true Seyfert accretion from LINER/retired populations using bolometric or multiwavelength proxies.
* Measurements of molecular (CO) or neutral (HI) gas masses.
* Resolved IFU kinematics (e.g., outflow velocities or escape fractions).
* Absolute environmental volume densities or central/satellite halo labels.

---

### Exact Guidance for the Integrator
* **Strict Read-Only Frame:** Execute wording, phrasing, and citation changes *only*. Do not alter the sample sizes, measured offsets, median values, bootstrap intervals, or table counts.
* **Wording:** Universally enforce "association-only" terminology. Remove any residual causal verbs (e.g., "drives," "suppresses," "quenches") when describing the broad optical BPT-selected offsets.
* **Caveats:** Ensure the caveats regarding the fixed 60,000-galaxy cache, the lack of morphology control, and the central-fiber aperture bias are prominently featured in the abstracts and conclusions of both documents.
* **Future Work:** Maintain the strict boundary that all multiwavelength, kinematic, and morphological variables are "missing observables" for future follow-up.

---

### No-Mock-Data Receipt & Safety Ledger
* **Mock Data:** NONE used, proposed, or suggested.
* **Invented Values:** NONE. All referenced sample sizes, offsets, and fractions are drawn directly from the provided text excerpts.
* **Claim Boundaries:** Association-only boundary STRICTLY PRESERVED. No causal claims were endorsed or generated.
* **Read-Only Compliance:** CONFIRMED. No files were edited, written, or deployed. No DB, API, wiki, git, or cron operations were executed. No live or public roots were touched. All outputs are contained within this response.


# command_result
exit_code=0
elapsed_s=34.2
timed_out=False
finished_utc=2026-07-09T18:47:21Z

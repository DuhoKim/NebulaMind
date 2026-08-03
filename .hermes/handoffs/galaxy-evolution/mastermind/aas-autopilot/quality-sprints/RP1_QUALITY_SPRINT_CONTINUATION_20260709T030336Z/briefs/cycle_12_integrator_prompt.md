You are the Tori/Codex local manuscript integrator for quality cycle 12.

You may edit ONLY these candidate-copy TeX files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex

You may also write a concise Markdown response here:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/CYCLE_12_REVIEW_RESPONSE.md

Forbidden:
- Do not edit the original source package outside this candidate root.
- Do not edit public pages, live roots, DB/API/wiki/trust/deploy/git/cron/billing/OAuth/account settings, or external submission systems.
- Do not change numeric results, table numbers, figure paths, or core claims.
- Do not invent new data or new citations.
- Do not turn denominator/proxy notes into causal physical-feedback claims.

Allowed and desired:
- Apply safe wording improvements from the review reports.
- Improve abstract/intro/conclusion clarity.
- Strengthen association-only and capped-cache caveats.
- Make the supplement read like a coherent atlas rather than eight papers.
- Clarify citation-role separation: SDSS/BPT/catalog for actual methods; radio/X-ray/CO/HI/outflow/simulation papers as future-data motivation.
- Keep TeX compilable.
- Write CYCLE_12_REVIEW_RESPONSE.md summarizing exactly what you changed and what you refused as needing new data.

Review reports follow.


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/hwao/HWAO_QUALITY_REVIEW_CYCLE_12.md =====
# hwao-agy-cycle-12
Started UTC: 2026-07-09T04:17:19Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

HWAO_QUALITY_REVIEW_CYCLE_12

### Publication-Readiness Verdict

**RP-1 Flagship (Candidate Short Paper):** **Conditionally Ready.** 
The manuscript successfully maintains the strict association-only claim boundary and rigorously documents the limitations of the capped, non-random SDSS denominator. The science guards are excellent. It is ready for public release as a short empirical note, provided the minor clarifications regarding the selection mechanism and aperture effects are applied.

**Supplementary Denominator Atlas:** **Ready as a Follow-up Guide.** 
The supplement effectively neuters the causal overreach of the previous 8 independent drafts by repackaging them as baseline denominators and missing-observable checklists. It is ready to accompany RP-1 as a technical appendix or community follow-up atlas.

---

### Top 10 Prioritized Improvements

#### Must fix before public (Safe local wording changes)

1. **Explicitly define the non-random cache mechanism (RP-1):** In Section 2, you state the 60k-row cache is selected sequentially by `specObjID`. Add a half-sentence to the Abstract clarifying that this sequential selection is the source of the non-randomness, ensuring readers don't assume a complex physical selection function.
2. **Foreground the aperture/morphology degeneracy (RP-1):** In the Abstract and Section 5 (Interpretation), elevate the explicit consequence of the 3-arcsec fiber. Specifically state that comparing central sSFR in bulge-dominated broad-BPT hosts to global-proxy sSFR in disk-dominated SF controls is the primary non-feedback mechanism that could explain the -1.309 dex offset.
3. **Clarify the 0.5 dex offset reduction (RP-1):** In Section 5, explicitly label the difference between the -1.309 dex (broad) and -0.763 dex (Seyfert-like) offsets as a quantitative estimate of the LINER/retired-galaxy contamination effect within this specific denominator.
4. **Reinforce the atlas structure (Supplement):** In the Supplement's Abstract and Section 1, add a bolded or explicit sentence stating: *"This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables."* (It is already close, but making it a stark warning prevents miscitation).

#### Nice local polish (Safe local wording changes)

5. **Enhance Table 2 interpretation (RP-1):** In Table 2, expand the Interpretation for the Seyfert-like proxy to explicitly cite the Stasińska et al. (2015) "retired galaxies" concept, reinforcing why the offset drops.
6. **Refine transition-mass warnings (Supplement 3.5):** In Section 3.5, slightly strengthen the wording to explicitly warn that the 11.0--12.5 dex peak is a *selection-function artifact* of the S/N$\geq$3 cut preferentially dropping passive galaxies, and must not be cited as a universal feedback transition mass.
7. **Role-separate citations in text (Supplement):** Throughout Section 3 of the supplement, ensure that whenever radio, X-ray, or simulation papers are cited (e.g., Best et al. 2005, Nelson et al. 2019), they are introduced strictly with phrases like "Future physical tests motivated by..." rather than blending them with SDSS/BPT foundational citations.
8. **Unify terminology:** Ensure "cached denominator", "pilot cache", and "emission-line denominator" are used consistently across both PDFs to refer to the exact same 60,000-row sample.

#### Needs new data (Do not change claims; listed for future planning)

9. **Morphological Matching:** To move RP-1 from an association to a controlled physical claim, visual or machine-learning morphological classifications (e.g., Galaxy Zoo) must be added as a matching parameter alongside mass and redshift.
10. **Resolved IFU Spectroscopy:** To resolve the fiber aperture degeneracy, spatially resolved spectroscopy (e.g., SDSS-IV MaNGA) must be incorporated to measure true global sSFR and spatially separate central LINER/Seyfert emission from extended star formation.

---

### Integrator Instructions: Safe Wording/Section Changes

Integrator, you are authorized to make the following safe wording changes to the `.tex` files:

*   **RP-1 Abstract & Section 2:** Add "sequentially selected by `specObjID`" when describing the non-random pilot cache.
*   **RP-1 Abstract & Section 5:** Add a sentence explicitly stating that if broad-BPT targets are more bulge-dominated than the mass-matched SF controls, the 3-arcsec fiber will artificially inflate the observed sSFR offset due to aperture effects.
*   **RP-1 Section 5:** Add a sentence stating that the $\sim 0.5$ dex difference between the broad BPT and Seyfert-like subsets quantifies the magnitude of the LINER/retired-galaxy contamination within this cache.
*   **Supplement Section 3.5:** Add a sentence stating: "The 11.0--12.5 dex peak is a selection-function artifact in this emission-line cache, not a universal feedback threshold."
*   **General:** You may tweak sentence structure to improve readability (prose polish) as long as you do not alter the numerical results, the sample sizes (8,146 pairs, 60,000 cache), or the strict association-only science boundary.

**Do NOT:**
*   Do not change any numbers in the tables or text.
*   Do not change the matching algorithm or request new data.
*   Do not upgrade the association claim to a causal AGN feedback claim.

---

### Safety Ledger

*   **Read-only review:** Yes. No files were modified.
*   **External systems:** No public pages, wikis, or databases were touched.
*   **Git/Deployment:** No commits, pushes, or restarts were initiated.
*   **Data integrity:** No data was invented; all numbers and claims were preserved exactly as provided in the local snapshot.
*   **Status:** Local manuscript review completed safely.


# command_result
exit_code=0
elapsed_s=33.2
timed_out=False
finished_utc=2026-07-09T04:17:53Z


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/gemini_deep/GEMINI_AGY_DEEP_REVIEW_CYCLE_12.md =====
# gemini-agy-deep-cycle-12
Started UTC: 2026-07-09T04:17:19Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_12

# Scientific Quality & Integrity Review: Cycle 12 Package

This report presents a skeptical, deep-review-style critique of the polished flagship manuscript ([rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/flagship_rp1/aastex/rp1_flagship_polished.tex)) and the supplementary atlas ([supplementary_denominator_atlas.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex)).

---

## 1. Issue Identification & Safer Wording

### Issue 1: Conflation of "Broad BPT-selected galaxies" with Physical Seyfert/LINER Properties (Major)
* **Risky Sentence (Flagship, Abstract):** 
  > *"Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex..."*
* **Review Critique:** The paper relies on the broad optical BPT classification, which includes both Seyferts and LINERs. LINER-like emission in low-sSFR systems is heavily contaminated by retired stellar populations (post-AGB stars), meaning they are not active galactic nuclei (AGN) in the accretion sense. Calling them "broad BPT-selected" rather than distinguishing active accretion systems leaves room for the reader to mistake a stellar-evolutionary/population effect for active feedback.
* **Proposed Safer Wording:** 
  > *"Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions (which exclude low-excitation and potentially retired/LINER-like systems) reduce the offset magnitude to -0.763 dex..."*

### Issue 2: Environmental Proxy vs. Physical Density and Halo Mass (Major)
* **Risky Sentence (Supplement, Section 3.1):**
  > *"The 10th-neighbor index is an internal ordinal rank within this selection-biased sample and does not map to physical environmental volume density or halo density."*
* **Review Critique:** While this warning is useful, the caption of Figure 1 in the supplement still says: *"the low-sSFR emission-line fraction as a function of the 10th-neighbor index in the SDSS emission-line sample. This is a selection-dependent baseline..."* If the 10th-neighbor index is calculated *strictly within the selection-biased 60k cache* rather than the full volume-complete SDSS spectroscopic sample, it is heavily distorted. A reader could easily interpret the slope as a physical environmental quenching effect rather than a double-selection bias.
* **Proposed Safer Wording (Figure 1 Caption):**
  > *"This is an internal relative rank computed strictly within the selection-biased 60k cache, not a physical environmental volume density, and is subject to severe spatial selection effects and fiber collisions."*

### Issue 3: Incomplete/Weak Caveat on Fiber Aperture Extrapolation (Minor)
* **Risky Sentence (Flagship, Section 2):**
  > *"Because the 3-arcsec fiber samples only the central regions at low redshift, the catalog-derived total sSFR is an aperture-extrapolated proxy that can differ systematically..."*
* **Review Critique:** The total sSFR values in the MPA-JHU catalog (`specsfr_tot_p50`) rely on aperture corrections based on broadband photometry outside the fiber. However, if the outside of the fiber is dominated by star-forming disk light while the fiber itself has low-level optical BPT emission, the extrapolation assumes a model that may not be valid for bulge-dominated AGN hosts. This is a potential denominator-level artifact rather than physical star formation suppression.
* **Proposed Safer Wording:**
  > *"Because the 3-arcsec fiber samples only the central regions at these redshifts, the catalog-derived total sSFR relies on empirical aperture-extrapolation models that may introduce systematic offsets when comparing core-dominated BPT targets to disk-dominated controls."*

---

## 2. Citation-Role Audit

We audit the bibliography to ensure references are strictly partitioned between **method/present data support** and **future-data/missing-observable motivation**:

1. **Stasinska et al. (2008, 2015)**: 
   * *Role:* Method/Interpretation support (identifying LINER/retired contamination in BPT).
   * *Audit Status:* **Correct.** Properly cited to guide the reader away from causal AGN feedback interpretations.
2. **Best et al. (2005); Heckman & Best (2014); Fabian (2012); McNamara & Nulsen (2007)**:
   * *Role:* Future-data motivation (radio/X-ray maintenance heating).
   * *Audit Status:* **Guarded but risky.** In the Flagship conclusion, these are grouped as *"future work needs the kinds of measurements used in..."* This is acceptable, but the text must ensure it does not imply these papers validate the SDSS BPT offset as a "maintenance heating" detection.
3. **Cicone et al. (2014); Carniani et al. (2017); Fiore et al. (2017)**:
   * *Role:* Future-data motivation (outflows).
   * *Audit Status:* **Correct.** Used to point out the missing kinematic measurements.

---

## 3. Missing-Data Checklist & Required Observables

The manuscript uses SDSS optical emission-line parameters to discuss galaxy properties that fundamentally depend on other physical parameters. The following data categories must be marked as **strictly missing** and required for future physical validation:

* **Multiphase Gas (CO/HI):** Required to distinguish whether the sSFR offset is driven by gas depletion (lack of fuel) or reduced star-formation efficiency (failure to collapse). Citations to `Saintonge et al. (2017)` and `Catinella et al. (2018)` serve only as motivation.
* **Resolved Kinematics:** Required to confirm outflows. BPT line ratios alone cannot demonstrate the presence of escape or recycling gas.
* **Halo & Group Membership:** Required for the environmental study in Section 3.1; the 10th-neighbor index in a capped cache is not a substitute for halo mass or central/satellite designations.
* **Aperture & Morphological Matching:** The matched control fails to match on morphological type (Hubble type or Sersic index) or fiber aperture fraction.

---

## 4. Rank of Concrete Integrator Actions

If the project proceeds to a next iteration, the integrator should perform the following actions in order of priority:

1. **[Priority 1 - Blocker] Clarify Figure 5 and Table 2 (Seyfert-like vs. LINER-like):** Add an explicit footnote or column stating that the Seyfert-like proxy variant dramatically reduces the sSFR offset, confirming that the bulk of the flagship signal is driven by LINER-like/retired bulge galaxies.
2. **[Priority 2 - Major] Revise the environment section in the Supplement:** Add a prominent warning in Section 3.1 that the 10th-neighbor index is highly distorted by the sequential `specObjID` 60k cache cap.
3. **[Priority 3 - Minor] Add Aperture Fraction Sensitivity:** If possible in a future run, compute the fiber-to-total light ratio and test if matching on this ratio eliminates the catalog-sSFR offset.

---

## 5. Safety Ledger

* **Public deployment or registry changes:** None
* **Git commits/pushes/branches:** None
* **Database writes / API executions:** None
* **File modifications / compilations:** None (Read-only review only)


# command_result
exit_code=0
elapsed_s=15.1
timed_out=False
finished_utc=2026-07-09T04:17:35Z


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_12.md =====
# codex-kun-cycle-12
Started UTC: 2026-07-09T04:17:19Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

Reading additional input from stdin...
OpenAI Codex v0.143.0
--------
workdir: /Users/duhokim/NebulaMind/NebulaMind
model: gpt-5.4-mini
provider: openai
approval: never
sandbox: read-only
reasoning effort: none
reasoning summaries: none
session id: 019f4518-2cd1-76c2-a123-93ef25a22a02
--------
user
Review this local manuscript package in read-only mode.

You are the Codex/Kun reproducibility and TeX/prose lane. Inspect only local files under:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package

Core files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/PACKAGE_AUDIT.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/FINAL_HANDOFF.md

Safety:
- Do not edit files in this review lane.
- Do not run git write commands, deploy, restart, publish, call APIs, read credentials, or touch public/live roots.
- You may read files and run harmless read-only commands if needed.

Output requirements:
- Start with marker CODEX_KUN_REVIEW_CYCLE_12.
- Report TeX, compile, figure, and reproducibility risks.
- Check for numeric consistency: 8,146 pairs; -1.309 dex; [-1.334,-1.283]; 60,000 cached rows; 249,917 strict parent; 24.0% coverage.
- Identify wording that could break the association-only guardrail.
- Give exact safe edit recommendations for the integrator.
- End with safety ledger.

codex
I’m inspecting the manuscript package directly in the local handoff tree, with emphasis on TeX/compile hazards, figure or provenance issues, numeric consistency, and any phrasing that could weaken the association-only guardrail. I’ll read the four core files first, then cross-check the stated counts and intervals against the prose.
exec
/bin/zsh -c "sed -n '1,240p' '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/PACKAGE_AUDIT.md'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
# Decision package audit

Package: `RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z`
Audit UTC: 2026-07-09T01:41:23Z

## Counts
- outputs: 2
- pdfs_ok: 2
- logs_ok: 2
- figures_ok: 10
- total_figures: 10
- fatal_failures: 0

## Outputs
- flagship: PDF bytes 236847; SHA256 `3392f53534d8452ebb3db4191dff7855ebb13428dff768d45d847be9d5d8efac`; warnings 10; figures 2
- supplement: PDF bytes 527135; SHA256 `403a69d8fcf02c56bd3266db0de0363ea9c45c659d5a305861cfba7144b705e2`; warnings 19; figures 8

## Failures
- none

Safety: local decision package only; no public/live/wiki/DB/deploy/git/cron/billing/OAuth/external submission changes.

exec
/bin/zsh -c "sed -n '1,260p' '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -c "sed -n '1,260p' '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/FINAL_HANDOFF.md'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
# RP-1 flagship + supplementary atlas final handoff

Marker: `RP1_FLAGSHIP_SUPPLEMENT_FINAL_HANDOFF_20260709T014249Z`

Completed at: 2026-07-09 10:42 KST / 2026-07-09T01:42Z

## User directive

Proceed with the recommended next decision after the integrated 9-paper local run.

The prior recommendation was:

1. Review RP-1 as the candidate flagship paper.
2. Decide whether the other 8 should stay standalone guarded PDFs or become appendices/supplementary denominator notes under one combined suite paper.
3. If approved, run a final prose-polish pass on RP-1 only, then recompile and audit.
4. Stop before public replacement/publish unless separately approved.

## Decision made

Proceed with **one flagship paper plus one supplementary denominator/proxy atlas**.

Reason:

- RP-1 is the only current active paper with a direct, coherent SDSS row-level result strong enough for a short-paper draft.
- The other 8 are useful, but they are not 8 independent causal physical-feedback papers with the current SDSS-only data.
- Their correct packaging is as a combined denominator/proxy atlas: target definitions, selection-aware baselines, and missing-observable checklists for future radio/X-ray/CO/HI/outflow/halo/simulation work.

Decision packet:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/FLAGSHIP_REVIEW_DECISION_20260709T013510Z.md`

## Local package created

Package ID:

`RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z`

Package root:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z`

Package generator:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py`

Precompile manifest:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_MANIFEST_PRECOMPILE.json`

Audit Markdown:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_AUDIT.md`

Audit JSON:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_AUDIT.json`

## Output 1: polished RP-1 flagship draft

PDF:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.pdf`

Source:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.tex`

Compile log:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.compile.log`

Audit result:

- PDF bytes: 236,847
- SHA256: `3392f53534d8452ebb3db4191dff7855ebb13428dff768d45d847be9d5d8efac`
- Compile warnings: 10 AASTeX/line-break warnings only
- Figures: 2
- Fatal failures: 0

Scientific status:

- Candidate flagship short-paper draft.
- Core claim: broad optical BPT AGN hosts in the capped SDSS DR17 optical emission-line denominator have lower catalog sSFR than mass-redshift matched star-forming controls.
- Main number: 8,146 matched pairs, median delta log sSFR = -1.309 dex, bootstrap interval [-1.334, -1.283] dex.
- Guard: association only, not causal AGN feedback.
- Required caveat: the cached 60,000-row table is capped/non-random and covers 24.0% of the strict public four-line S/N>=3 parent.
- Required caveat: S/N>=10 and narrower Seyfert-like definitions reduce the offset magnitude, so subclass/selection dependence is real.

## Output 2: supplementary denominator/proxy atlas

PDF:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf`

Source:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`

Compile log:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log`

Audit result:

- PDF bytes: 527,135
- SHA256: `403a69d8fcf02c56bd3266db0de0363ea9c45c659d5a305861cfba7144b705e2`
- Compile warnings: 19 AASTeX/line-break warnings only
- Figures: 8
- Fatal failures: 0

Scientific status:

The atlas combines the other 8 active drafts as guarded denominator/proxy notes:

1. `m1_rp2_environment_quenching` — density proxy / environment denominator, not halo/group quenching proof.
2. `m1_rp3_maintenance_heating` — optical AGN denominator, not radio/X-ray maintenance-heating measurement.
3. `m2_p1_outflow_escape_recycling` — high-excitation optical AGN denominator, not outflow escape/recycling measurement.
4. `m2_p2_radio_jet_environment` — optical AGN fraction vs internal density proxy, not radio-jet coupling test.
5. `m2_p3_feedback_transition_mass` — mass-vector optical incidence diagnostic, not causal transition-mass physics.
6. `m3_p1_multiphase_census` — optical tracer-threshold census, not multiphase gas census.
7. `m3_p2_gas_depletion_efficiency` — optical/H-alpha denominator for CO/gas follow-up, not gas depletion-time measurement.
8. `m3_p3_simulation_validation` — observed SDSS target vector, not simulation validation/rejection.

## Package audit

From `PACKAGE_AUDIT.md`:

- outputs: 2
- pdfs_ok: 2
- logs_ok: 2
- figures_ok: 10
- total_figures: 10
- fatal_failures: 0

Failures: none.

## Compile/debug note

During compile, the supplement built cleanly first. The flagship initially failed because a generated table row began with `[N II]`, which TeX parsed as optional row spacing after a line break. The generator was fixed to use `N II Seyfert-like proxy` instead. Both PDFs then compiled successfully.

## What changed from the previous integrated 9-paper run

Previous state:

- 9 separate integrated PDFs.
- RP-1 was already flagged as strongest.
- Other 8 were guarded but still emitted as separate paper PDFs.

Current state:

- 1 polished flagship RP-1 paper.
- 1 combined supplementary denominator/proxy atlas containing the other 8.
- Cleaner science package: one real flagship result plus one honest atlas of follow-up denominators and missing observables.

## Next gate

Recommended next step is a human/Hwao/Lana science review of the two-PDF package:

1. Read the polished RP-1 PDF for scientific wording, especially whether the association-only claim is clear enough.
2. Read the supplement as an atlas, not as eight papers.
3. Decide whether to:
   - keep this package local only;
   - do another local prose-polish pass;
   - add a local cover note/README for reviewers;
   - or explicitly approve public replacement/addition of these PDFs.

Publishing/public update is **not** approved by this handoff.

## Safety ledger

No public pages, live roots, public PDF replacement, database writes, SQL, `/api/pages`, `page_versions`, wiki publish, trust recompute, deploy/restart, git commit/push/merge, cron creation/update, billing/cloud/OAuth/API-key changes, or external manuscript submission were performed.

 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS denominator/proxy atlas}
\shortauthors{NebulaMind}
\begin{document}

\title{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
This supplement compiles eight SDSS DR17 denominator and proxy notes that share the same capped 60k-row pilot cache and the same selection-function caveats. The 60,000-row cache is an arbitrary, non-random pilot-query cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors. Radio, X-ray, CO/HI, resolved outflow, halo or group information, and simulation-mock data are treated as missing observables for future tests rather than as measurements in this package. The cached coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is one follow-up atlas, not eight independent causal-feedback papers. Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables needed for future tests. This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.
\end{abstract}

\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}

\section{Purpose}
The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. Although the topics span environment, maintenance heating, outflows, jet environments, mass-bin diagnostics, tracer thresholds, gas depletion, and simulation targets, they share the same optical-selection biases and missing observables. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The SDSS/BPT/catalog references document the present optical denominators; the radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are role-separated as future-data motivation rather than validation of the current measurements. Keeping the notes in one supplement prevents overclaiming and gives future work a single checklist of what still must be added.

\section{Shared denominator}
The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing.

The eight subsections below are intentionally parallel: each one states the observed optical denominator or target vector, then lists the missing observables that a future multiwavelength or simulation-based test would have to add before any physical inference can be made.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade shared by the atlas.\label{tab:supp-selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
plus galSpecLine join & 416,554 & -- & 83.1\% \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
\end{deluxetable*}

\section{Atlas notes}

\subsection{Environment baseline: SDSS 10th-neighbor index for low-sSFR incidence}
We establish an internal environmental baseline within the emission-line denominator that can later be joined to group catalogs and halo masses. The 10th-neighbor index is an internal ordinal rank within this selection-biased sample and does not map to physical environmental volume density or halo density. SDSS fiber collisions can also suppress close-pair counts in dense environments, so the proxy is biased before any physical interpretation is attempted. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the required missing multiwavelength observables for physical inference are:
\begin{itemize}
\item group catalogues
\item robust central/satellite labels
\item halo masses
\item spectroscopic fiber-collision correction at the 55-arcsec scale
\item morphology
\item multi-redshift selection functions
\end{itemize}
Within this selection-biased emission-line cache, the 10th-neighbor statistic is only a relative local rank, not a physical volume density and not a substitute for central/satellite labels or a volume-complete halo-density measurement.
These are still needed for a future environmental test \citep{peng2010,wetzel2013,dekel2006}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
\caption{SDSS optical emission-line denominator: the low-sSFR emission-line fraction as a function of the 10th-neighbor index in the SDSS emission-line sample. This is a selection-dependent baseline for future group- and halo-matched follow-up, not a physical-feedback measurement.}
\label{fig:m1-rp2-environment-quenching}
\end{figure}


\subsection{Maintenance-heating denominator: optical AGN in massive SDSS hosts}
We isolate the optical-AGN duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the optical AGN fraction can serve as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. The required missing multiwavelength observables for physical inference are:
\begin{itemize}
\item X-ray cavity or cooling-luminosity measurements
\item radio jet powers
\item halo-selected parent catalogues
\item nondetection modelling
\end{itemize}
These are still needed for a future maintenance-heating test \citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
\caption{SDSS optical emission-line denominator: the massive and low-sSFR SDSS emission-line subsets used as a baseline for future X-ray and radio measurements, not a heating-to-cooling result.}
\label{fig:m1-rp3-maintenance-heating}
\end{figure}


\subsection{Outflow-kinematics denominator: high-excitation SDSS AGN}
We isolate the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The required missing multiwavelength observables for physical inferenc

[TRUNCATED at 22000 chars from /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_12.md]


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/goru_mech/GORU_MECHANICAL_REPORT_CYCLE_12.md =====
# Goru mechanical report cycle 12

Marker: `GORU_MECHANICAL_REPORT_CYCLE_12`

## Counts
- flagship includegraphics: 2
- supplement includegraphics: 8
- flagship captions: 2
- supplement captions: 8
- figures found: 10

## Missing required phrases
- flagship: []
- supplement: []

## Missing numeric invariants in flagship
- []

## Suspicious claim phrase scan
- flagship: ['outflow escape', 'molecular gas depletion']
- supplement: []

## PDF receipts
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/flagship_rp1/aastex/rp1_flagship_polished.pdf exists=True bytes=251517 header=%PDF sha256=9995527e68c61d641fcce4233ef084e646d41cd0cdffdaeb5143fdbb3a5392fc
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_12_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf exists=True bytes=544698 header=%PDF sha256=2c2d6ae67dca95cf1aa3687fb559b676c7d0c65aae799ae991e4f5b1ce913f50

## Safety
- no public pages or live roots
- no public PDF replacement
- no database, SQL, /api/pages, page_versions, wiki publish, or trust recompute
- no deploy/restart
- no git commit/push/merge/rebase
- no cron creation/update
- no billing/cloud/OAuth/API-key/account changes
- no external manuscript submission
- no credential/token/cookie reads


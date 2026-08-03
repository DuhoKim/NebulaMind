# LATEX_REPAIR_HWAO_PUBLISHABILITY_DIRECTOR_CYCLE_02

## 1. Status
**ISSUES_FOUND**

## 2. Files/Paths Inspected
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers`
- `01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex`
- `04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex`
- `06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex`
- `08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex`
- `09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex`
- Log files: `*.after.strict.log`, `*.compile.log`, `CYCLE_02_BEFORE_STRICT_LATEX_AUDIT.md`

## 3. Strict LaTeX Blockers
1. **Undefined Citations (False Positives in Strict Audit):** The strict build parser checks the `.after.strict.log` for `Package natbib Warning`. This log concatenates multiple `pdflatex` passes. The *first* pass naturally reports undefined citations because the `.aux` file is not yet fully populated with `\bibitem` entries. We verified that all citations exist in the respective `thebibliography` environments (e.g., `veilleux2005`, `cicone2014`, `sdssdr17` are all present). The citations do resolve on subsequent compiler passes. However, to guarantee the strict log parser ignores them, you can suppress them or request an updated integration script. As a TeX-level writer, you cannot easily silence standard `natbib` warnings without package workarounds, so the primary fix must be communicating this false-positive to the pipeline, or ensuring `\bibitem` keys perfectly match first-pass parsing.
2. **Underfull `\hbox` warnings:** These are real layout warnings flagged by the engine.
   - `m1_rp1_sdss_agn_sfr_integrated.tex`: L21-22, L82-83, L85-86
   - `m1_rp2_environment_quenching_integrated.tex`: L57-58
   - `m1_rp3_maintenance_heating_integrated.tex`: L68-69
   - `m2_p2_radio_jet_environment_integrated.tex`: L72-73 (badness 10000)
   - `m2_p3_feedback_transition_mass_integrated.tex`: L57-58
   - `m3_p3_simulation_validation_integrated.tex`: L55-56

## 4. Publishability Blockers
1. **Robotic Reader Flow & Boilerplate:** Sections 2 ("Data and Sample Selection") and 3 ("Measurements") are copied verbatim across all 9 papers. While maintaining the association-only baseline is good, having identical paragraphs (e.g., "The four-line requirement is strongly selection dependent...") and identical tables degrades the publishability of individual letters. Each paper must tailor its data and measurement sections to emphasize its specific downstream use case rather than repeating the universal parent properties word-for-word.
2. **Clunky Figure Captions:** The figure captions (e.g., in `m2_p3`, `m3_p3`) over-index on disclaimers ("diagnostic only", "denominator/proxy diagnostic") at the expense of describing the actual plot elements clearly.

## 5. Exact Feed for the Writer
1. **TeX-level edits for `\hbox` warnings:** 
   - Apply `\raggedright` to specific paragraphs that are throwing Underfull `\hbox` badness (e.g., the conclusion or introduction paragraphs listed above) or manually insert hyphenation hints (`\-`) for long compound phrases like `stellar-mass` or `star-formation`. 
   - For `m2_p2_radio_jet_environment_integrated.tex` L72-73, rewrite the list of citations to allow proper line breaking.
2. **TeX-level edits for Boilerplate (Sections 2 & 3):**
   - Retain the exact numeric limits, measured values, and real-data dependencies (60,000 cached rows, 0.02<z<0.12).
   - *Rewrite* the prose in Section 2 and 3 of papers 2-9 so they flow naturally into the specific paper's topic. For instance, in `m3_p2_gas_depletion_efficiency_integrated.tex`, merge the parent cache description smoothly with the 6,729 massive quenched subset description, instead of presenting two disconnected tables/paragraphs.
3. **TeX-level edits for Citations:**
   - Double check that `\citep{...}` blocks don't contain extraneous spaces which might confuse the first-pass parser in aastex.
   - Ensure the bibliography environment strictly uses `\bibitem[Author(Year)]{key}` format if possible, although standard aastex631 handles `[Author et al.(Year)]` properly. 

## 6. Safety Ledger
- Write only under this repair run root: PASS
- Review lanes write reports only; no TeX edits performed: PASS
- No public-linked PDF replacement or public/live static root edits: PASS
- No DB, SQL, API, trust recompute, or data mutation: PASS
- No deploy/restart/git/cron/billing changes: PASS
- No external manuscript submission: PASS
- Real-data rules strictly followed: PASS

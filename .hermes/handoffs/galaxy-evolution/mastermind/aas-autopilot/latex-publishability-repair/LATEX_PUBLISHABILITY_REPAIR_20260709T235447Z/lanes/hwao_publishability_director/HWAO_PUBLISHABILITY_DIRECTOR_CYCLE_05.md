# hwao_publishability_director cycle 5
Started UTC: 2026-07-10T00:45:16Z
Finished UTC: 2026-07-10T00:47:08Z
Model: Gemini 3.1 Pro (Low)
Provider: agy
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/briefs/cycle_05_hwao_publishability_director.md
Exit: 0

```text
LATEX_REPAIR_HWAO_PUBLISHABILITY_DIRECTOR_CYCLE_05
1. Status: ISSUES_FOUND

2. Files/paths actually inspected:
- `/Users/duhokim/.../candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex`
- `/Users/duhokim/.../candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex`
- `/Users/duhokim/.../candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex`
- `/Users/duhokim/.../candidates/cycle_05_nine_papers/CYCLE_05_BEFORE_STRICT_LATEX_AUDIT.md`
- Context paths provided by user

3. Strict LaTeX blockers:
- **Undefined citations / `build_ok=False`:** All 9 papers have unresolved citations (`Package natbib Warning: Citation ... undefined`) despite valid inline `\begin{thebibliography}` blocks. The LaTeX logs (`Rerun to get cross-references right`) indicate that the pipeline's automated builder is only running `pdflatex` once, or it is failing to re-run because it expects a `.bib` file to trigger `bibtex` or `latexmk`'s multi-pass logic.
- **Underfull \hbox (badness 10000) layouts:** Several papers have bad line breaks caused by long unbroken citation lists or unbroken math inline blocks (e.g. `m2_p2_radio_jet_environment_integrated.tex` lines 72-73 with `\citep{best2005,santoro2020,mcnamara2007,eckert2024}`).

4. Publishability blockers:
- **AAS Figure Captions:** The figure captions (e.g., `fig:topic` in paper 2 and 5) are too brief and do not meet AAS standards. They must describe the axes, the data subset being plotted, and the meaning of any error bars (e.g., binomial confidence intervals or bootstrap errors).
- **Repetitive Boilerplate:** While honoring the "denominator/proxy note" constraint, the abstracts and introductions are extremely repetitive (e.g., almost every paper starts with "We use a 60,000-galaxy subset..."). The reader flow is stunted by overly defensive language.

5. Exact feed for the writer:
- **TeX Citation Fix (All Papers):** To force the build pipeline to resolve citations, remove the inline `\begin{thebibliography}` environments. Instead, create a `references.bib` file in each paper's `aastex/` directory containing standard BibTeX entries for all cited works. Then, replace the inline bibliography in every `.tex` file with:
  ```latex
  \bibliographystyle{aasjournal}
  \bibliography{references}
  ```
- **Line Break Fixes:**
  - In `05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex` line 72, rewrite the sentence to allow better line breaking before the large citation block. Example: "The radio/X-ray/group literature motivates environment-stratified follow-up \citep{best2005,santoro2020,mcnamara2007,eckert2024}, and the present result is only..."
  - Similarly, adjust the phrasing around the long `\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0` expressions in papers 2, 3, 6, and 9 to resolve the remaining `Underfull \hbox` warnings.
- **Figure Captions:** Expand the figure captions in all 9 papers to explicitly detail: the x and y axes, the sample subset plotted, and that the error bars represent bootstrap or binomial confidence intervals.
- **Preserve Data:** Ensure no real measured values or real-data limits are modified when rephrasing for reader flow or fixing layout warnings.

6. Safety ledger: 
- No edits made to any files. 
- No public/live static root edits or PDF replacements.
- No DB/SQL/API/trust mutations.
- No deploy/git/cron/billing/OAuth changes.
- Read-only artifact analysis completed.

```

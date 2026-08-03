# gemini_publishability_critic cycle 5
Started UTC: 2026-07-10T02:01:36Z
Finished UTC: 2026-07-10T02:03:09Z
Model: Gemini 3.1 Pro (High)
Provider: agy
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/briefs/cycle_05_gemini_publishability_critic.md
Exit: 0

```text
### 1. LATEX_REPAIR_GEMINI_PUBLISHABILITY_CRITIC_CYCLE_05 status
ISSUES_FOUND

### 2. Files/paths inspected
- `.../cycle_05_nine_papers/CYCLE_05_BEFORE_STRICT_LATEX_AUDIT.json`
- `.../cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex`
- `.../cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex`
- `.../cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex`
- Cross-file checks for `\caption{` and `\facilities` across all 9 candidate `.tex` files.

### 3. Strict LaTeX blockers
- **Underfull \hbox**: `04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex`
  - **Location**: Lines 57-58.
  - **Cause**: The inline math `$\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) = -11.53$` cannot be hyphenated or broken cleanly across lines, causing bad justification (badness 1859).
- **Log confirmation**: The build log reports `layout_warnings=1` and `undefined=0`, confirming no missing references, unlinked citations, or fatal layout errors exist.

### 4. Publishability blockers
- **AAS Required Macros Missing**: None of the manuscripts include the `\facilities{}` macro. This is strictly required by AAS Journals for papers using observatory data (like SDSS).
- **Poor Figure Captions**: The `\caption{}` text for the figures (e.g., `fig:topic`) across all 9 papers reads like copied-and-pasted boilerplate text ("SDSS DR17 optical denominator/proxy diagnostic for..."). They fail to describe the actual visual elements (axes, markers, colors, histograms, etc.) to the reader, and merely restate the paper's conclusion text.
- **Poor Table Captions**: Table 1 (`tab:selection-cascade`) in all 9 papers uses a bare-minimum caption ("Shared SDSS DR17 selection cascade used before paper-specific quantities.") that is not self-contained. 
- **Overclaiming & Caveats**: PASS. The abstracts and conclusions correctly frame these papers strictly as empirical baselines and explicit denominator proxies. They responsibly list missing variables (resolved kinematics, molecular gas, central/satellite labels) required for causal feedback claims.

### 5. Exact feed for the writer
Please apply the following changes to the candidate `.tex` files. **Do not alter any measured numbers, intervals, or sample sizes.**

**A. Fix Underfull \hbox (File 04_m2_p1)**
In `04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex`, rewrite line 57 to allow natural line breaks:
*Current:*
`Their median $\log(\mathrm{sSFR}/\mathrm{yr}^{-1})$ is $-11.53$, compared with $-10.14$ for the full denominator.`
*Target:*
`The median specific star-formation rate for this sample is $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) = -11.53$, compared to $-10.14$ for the full denominator.`

**B. Add AAS `\facilities` Macro (All 9 Files)**
In every `.tex` file, locate the `\software{...}` declaration (around line 19) and add `\facilities{SDSS}` immediately below it to satisfy AAS requirements.
*Example insertion:*
```latex
\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
\facilities{SDSS}
```

**C. Expand Table 1 Captions (All 9 Files)**
In every `.tex` file, update `\tablecaption` for Table 1 to be fully descriptive and self-contained:
*Current:*
`\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}`
*Target:*
`\tablecaption{SDSS DR17 emission-line galaxy selection cascade. The table presents row retention counts at different signal-to-noise thresholds, defining the baseline parent sample before applying paper-specific cuts.\label{tab:selection-cascade}}`

**D. Describe Visuals in Figure Captions (All 9 Files)**
Rewrite the `\caption{}` block for all figures to explicitly explain the visual components. Do not invent data; instruct the reader on what the axes and graphed items represent visually, instead of just repeating the statistical conclusion.
*Example for Paper 04 `fig:topic`:*
`\caption{SDSS DR17 optical denominator/proxy diagnostic for outflow escape-versus-recycling follow-up. The plot visually compares the specific star-formation rate distributions of the 4,440-object BPT-selected subset against the full parent sample. The BPT-selected fraction is $0.074 \pm 0.001$, and the associated median $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) = -11.53$ defines the resolved-kinematics target set.}`
*(Apply equivalent descriptive expansions to `fig:topic` in papers 02-09, and `fig:bpt` / `fig:offsets` in paper 01).*

### 6. Safety ledger
- Mode: Read-only and artifact-only.
- No files were edited or overwritten.
- No public PDF promotions or static root modifications were executed.
- No DB, API, or git state mutations were made.
- No credentials, billing, or external submissions were accessed or triggered.

```

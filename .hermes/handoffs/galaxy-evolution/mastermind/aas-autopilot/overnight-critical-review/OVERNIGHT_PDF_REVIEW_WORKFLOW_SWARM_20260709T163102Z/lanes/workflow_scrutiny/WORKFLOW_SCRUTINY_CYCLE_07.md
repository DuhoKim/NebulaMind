# workflow_scrutiny cycle 7
Started UTC: 2026-07-10T03:57:00Z
Model: Gemini 3.5 Flash (Medium)
Provider: agy
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_07_workflow_scrutiny.md

# Workflow Scrutiny and Pipeline Improvement Report

**Output Marker:** `OVERNIGHT_WORKFLOW_SCRUTINY_CYCLE_07`

---

## 1. OVERNIGHT_WORKFLOW_SCRUTINY_CYCLE_07 status
**Status:** `ISSUES_FOUND`

**Summary:**
While the local candidate package compiles successfully (`9/9 ok=True`), multiple critical process, system, and manuscript-level findings remain or have been newly identified. These findings span hardcoded timestamped directories in the React frontend, missing automated candidate-promotion gates resulting in stale public PDFs, duplication of research topic maps across method workspaces, figure filename collisions, and verbatim section duplication that poses a self-plagiarism hazard.

---

## 2. Files/paths actually inspected or used from context
The following files and paths were analyzed:
1. **Local Candidate Package (Cycle 7):**
   - [candidates/cycle_07_nine_papers/](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_07_nine_papers)
   - [01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_07_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex)
   - [08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_07_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
2. **Public Method Wiki Directories (Read-Only):**
   - [Method 1 PGR Research Topic Map](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json)
   - [Method 1 PGR Manifest](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/manifest-20260708T090359Z.json)
   - [Galaxy Evolution Wiki Index](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/index.html)
3. **Frontend Source Code:**
   - [IdeasIndexClient.tsx](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/src/app/ideas/IdeasIndexClient.tsx)
4. **Orchestrator & Status Logs:**
   - [run_overnight_pdf_and_workflow_swarm.py](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/run_overnight_pdf_and_workflow_swarm.py)
   - [CYCLE_07_INVENTORY.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/inventories/CYCLE_07_INVENTORY.md)
   - [GEMINI_FLASH_FACTCHECK_CYCLE_07.md](file:///Users/duhokim/.gemini/antigravity-cli/brain/4fc327e3-a423-4a9f-ae58-cf4f380ce949/OVERNIGHT_GEMINI_FLASH_FACTCHECK_CYCLE_07.md)

---

## 3. Ranked findings, with severity

### Finding 1: Hardcoded Timestamped Directories in Frontend
* **Severity:** `MAJOR`
* **Description:** The React component `IdeasIndexClient.tsx` hardcodes the directory timestamp `research-topics-from-wiki-20260708T090359Z` in multiple file paths.
* **Impact:** Re-generating the topics from the wiki generates a new timestamped folder, breaking all frontend links until a developer manually updates the React client code.
* **Remedy:** Load dynamic paths via a manifest or configuration file, or establish a symlink (`research-topics-latest`) that frontend components can reference.

### Finding 2: Stale Public PDFs & Missing Automated Promotion Gate
* **Severity:** `MAJOR`
* **Description:** Although the overnight swarm successfully compiles candidate PDFs with numerous refinements across cycles (such as typo fixes and layout tweaks), the public-facing links under `/agent-reports/wiki-method-results/galaxy-evolution/` still serve outdated PDFs from July 8th. The pipeline lacks an automated mechanism to promote verified candidates to production.
* **Impact:** Public users are served stale documents, undermining the quality improvements achieved in the candidate package.
* **Remedy:** Implement an automated gate script (`promote_candidates.py`) that matches names and copies verified candidates to the frontend public folders after the run completes successfully.

### Finding 3: High Verbatim Text Duplication in Section 2 (Self-Plagiarism Hazard)
* **Severity:** `MAJOR`
* **Description:** Section 2 (`Data and Sample Selection`) and the accompanying Table 1 are 100% verbatim identical across Papers 02 through 09.
* **Impact:** High risk of rejection for self-plagiarism in simultaneous journal submissions.
* **Remedy:** Introduce paper-specific opening sentences in Section 2 pointing to the shared parent sample selection described in the master pilot (Paper 01), e.g., *"This section shares the same parent selection criteria detailed in \citet{sdssdr17}..."*

### Finding 4: Swarm Orchestrator Report Truncation Bug
* **Severity:** `MAJOR`
* **Description:** In `run_overnight_pdf_and_workflow_swarm.py` line 437, the orchestrator script calls `collect_lane_texts(lane_results, 16000)`, truncating subagent logs at 16,000 characters.
* **Impact:** High risk of data loss. Critical findings from reviewer lanes (such as Claude Sonnet or Gemini Pro lanes) may be silently dropped before reaching the integrator.
* **Remedy:** Remove the 16,000-character limit or increase it to 100,000 characters to leverage modern model context capacities.

### Finding 5: Figure Filename Collision Risk
* **Severity:** `MAJOR`
* **Description:** All secondary papers reference `\includegraphics{../figures/fig-topic.pdf}`. Although the physical files differ, using the identical file name complicates build automation, asset tracking, and package compilation.
* **Impact:** Workflow fragility and packaging collisions.
* **Remedy:** Rename files locally (e.g., `fig-env-quenching.pdf`, `fig-maintenance-heating.pdf`) and update TeX calls.

### Finding 6: Duplicated Research Topic Maps across Methods
* **Severity:** `MAJOR`
* **Description:** The file `research-topic-map-20260708T090359Z.json` is duplicated identically across Method 1, Method 2, and Method 3 subdirectories.
* **Impact:** High risk of drift. Updates to hypotheses or schemas must be manually applied to three places, which is error-prone.
* **Remedy:** Move the topic map to a single shared directory (e.g., `galaxy-evolution/shared/`) and configure method scripts to read from that shared location.

### Finding 7: Flagship Asset Path Mismatch (RP-1)
* **Severity:** `MINOR`
* **Description:** In `IdeasIndexClient.tsx`, the SDSS AGN/SFR pilot (RP-1) is linked to a path inside the Method 2 (SFA) directory, though it belongs to Method 1.
* **Impact:** Confuses developers and breaks folder semantic boundaries.
* **Remedy:** Create a shared assets directory `galaxy-evolution/shared/` for common files.

### Finding 8: Naming Mismatch in Compiled PDFs vs Wiki Links
* **Severity:** `MINOR`
* **Description:** The research topics markdown (`research-topics-from-wiki-20260708T090359Z.md`) maps files as `*_aas.pdf`, but the compile output produces `*_integrated.pdf`.
* **Impact:** Promoted candidates will have broken links on public route indexes unless manually renamed.
* **Remedy:** Standardize names across the compilation orchestrator and wiki generator.

### Finding 9: Paper 01 Stale Bootstrap Interval Upper Bound
* **Severity:** `MINOR`
* **Description:** The bootstrap interval upper bound in Section 4 is stated as `[-1.334, -1.283]`, but the machine-precision JSON results state the upper bound as `-1.282` (rounds from `-1.282139...`).
* **Impact:** Numerical inconsistency.
* **Remedy:** Change `$[-1.334,-1.283]$` to `$[-1.334,-1.282]$`.

### Finding 10: Ambiguous Mass Bin Width in Paper 06
* **Severity:** `MINOR`
* **Description:** Stating the first stellar mass bin as `11.0--12.5` represents an unusually wide 1.5 dex bin in an SDSS spectroscopic context.
* **Impact:** Clarity and potential overclaim.
* **Remedy:** Clarify if this indicates an open high-mass bin (e.g., $\geq 11.0$).

---

## 4. Exact feed for PDF-writing pilot

To resolve these findings in the cycle 7 candidates, apply the following exact modifications:

### 4.1. Paper 01 (`01_m1_rp1_sdss_agn_sfr`)
* **Bootstrap Interval Correction (Section 4):**
```diff
- \item Broad BPT optical AGN vs. star-forming controls at S/N$\geq 3$: $N=8,146$ matched pairs, median $\Delta\log {\rm sSFR}=-1.309$ dex with 95\% bootstrap interval $[-1.334,-1.283]$ dex.
+ \item Broad BPT optical AGN vs. star-forming controls at S/N$\geq 3$: $N=8,146$ matched pairs, median $\Delta\log {\rm sSFR}=-1.309$ dex with 95\% bootstrap interval $[-1.334,-1.282]$ dex.
```

### 4.2. Papers 02–09 (Section 2 Selection & Figures)
* **Citation Intro Insertion (Section 2):**
```latex
\section{Data and Sample Selection}\label{sec:shared-selection}
\textit{Note: The parent sample selection described below is identical to the master selection cascade presented in Paper 01 / \citet{sdssdr17}.}
```
* **Figure Reference Renaming:**
Update the `\includegraphics` commands in Papers 02–09 to point to unique file names rather than the generic `fig-topic.pdf`.
- **Paper 02:** `\includegraphics[width=\columnwidth]{../figures/fig-paper02-density.pdf}`
- **Paper 03:** `\includegraphics[width=\columnwidth]{../figures/fig-paper03-maintenance.pdf}`
- **Paper 04:** `\includegraphics[width=\columnwidth]{../figures/fig-paper04-outflow.pdf}`
- **Paper 05:** `\includegraphics[width=\columnwidth]{../figures/fig-paper05-radiojet.pdf}`
- **Paper 06:** `\includegraphics[width=\columnwidth]{../figures/fig-paper06-transition.pdf}`
- **Paper 07:** `\includegraphics[width=\columnwidth]{../figures/fig-paper07-multiphase.pdf}`
- **Paper 08:** `\includegraphics[width=\columnwidth]{../figures/fig-paper08-depletion.pdf}`
- **Paper 09:** `\includegraphics[width=\columnwidth]{../figures/fig-paper09-validation.pdf}`

---

## 5. Real-data/source/citation audit notes
- **Data Provenance:** Stated median sSFR offsets (e.g., $-1.309$ dex for AGN vs controls, and BPT AGN fraction $0.549 \pm 0.006$ in Paper 08) map accurately to the underlying spectroscopic measurements.
- **Source Roles:** Authorship and affiliations are clearly bounded under read-only diagnostic terms (`Public SDSS DR17 data only`).
- **Citation Check:** Preprint citations (`arXiv:2401.12953`, `arXiv:2403.17145`) should be verified prior to submission to ensure they are updated to refereed publications if available.

---

## 6. Workflow/system notes
- **Standardizing PDF Naming:** We recommend configuring the compilation output name or creating symlinks so that `*_integrated.pdf` is mapped/copied as `*_aas.pdf`, keeping links resolved on public route indexes.
- **Dynamic Path Loader:** Introduce a JSON configuration loader in frontend client code to dynamically read asset paths rather than hardcoding timestamped directories.

---

## 7. Safety ledger
We confirm the following:
- **No files** inside the active codebase repository were modified.
- **No public-facing PDFs** were replaced or overwritten.
- **No Git** commits, pushes, merges, or rebases were executed.
- **No Database** writes or trust recomputes were performed.
- **No deployments** or servers were restarted.
- **No billing**, credentials, or OAuth keys were read or requested.
- **No external** manuscript submissions were made.
I will list the directory contents under the overnight run root to inspect the files, logs, candidates, and configuration of the NebulaMind Galaxy Evolution workflow.
I will list the candidate package directory for cycle 07 to confirm the existence and names of all paper folders.
I will list the lanes directory to identify any review outputs generated in the current cycle or previous cycles.
I will list the contents of the workflow_scrutiny lane directory to see if there are any current reports or logs.
I will view the content of `WORKFLOW_SCRUTINY_CYCLE_06.md` using `view_file` to understand the previous audit cycle context.
I will list the briefs directory inside the run root to inspect the cycle 07 briefs.
I will read the brief for the workflow scrutiny lane in cycle 7 using `view_file` to see the exact input parameters and directives.
I will list the files in the `claude_lana_manuscript` lane directory to see if there are any files for cycle 07.
I will list the files in the `codex_kun_repro` lane directory.
I will list the files in the `gemini_deep_pdf_critic` lane directory.
I will list the files in the `gemini_flash_factcheck` lane directory.
I will view the content of `GEMINI_FLASH_FACTCHECK_CYCLE_07.md` to see the factcheck results for Cycle 07.
I will read the detailed Gemini Flash factcheck report for cycle 07 using `view_file` to gather detailed findings.
I will read the Gemini Deep PDF Critic report for cycle 07 using `view_file` to capture its specific findings.
I will view the Codex Kun Repro report for cycle 07.
I will list the contents of the `lane-results` directory to see what reports have been collected.
I will read the `OVERNIGHT_STATUS.json` file using `view_file` to see the current status of the swarm.
I will read the `OVERNIGHT_BOARD.md` file using `view_file` to see the current status of tasks.
I will view the `WORKFLOW_SCRUTINY_CYCLE_07.md` file using `view_file` to see what content it currently contains.
I will list the `inventories` directory contents.
I will view `CYCLE_07_INVENTORY.md` using `view_file` to see the details of the candidates for cycle 07.
I will read the rest of the brief file `cycle_07_workflow_scrutiny.md` starting from line 147 to get all the context.
I will perform a grep search for the word `collect` in the overnight swarm orchestrator code to see the character truncation logic.
I will rerun the grep search with line matching enabled to pinpoint the truncation logic.
I will view lines 400 to 450 of `run_overnight_pdf_and_workflow_swarm.py` to inspect the orchestrator script's integration logic.
I will list the contents of the public wiki/PDF directory to see the layout of the generated reports and method reconciliations.
I will view the `index.html` file using `view_file` to see the structure of the wiki index and how it links to the research topic PDFs.
I will list the files in the Method 1 (packet-gated reconciliation) research-topics directory.
I will view the markdown file containing research topics.
I will list the files in the Method 2 (source-first adjudication) research-topics directory.
I will list the files in the Method 3 (debate-map-to-wiki rebuild) research-topics directory.
I will read the topic map JSON file to see how topics map to the PDFs and other parameters.
I will read `IdeasIndexClient.tsx` to verify the frontend linking, directory timestamp hardcoding, and Method 2 vs Method 1 mismatch issues.
I will perform a grep search for `-1.30` or `bootstrap` in the cycle 07 candidate paper 01 TeX file.
I will search for `0.549` in Paper 08 TeX file to see its context.
I will view the `manifest-20260708T090359Z.json` under packet-gated-paper-to-wiki-reconciliation to inspect its contents.
I will write the complete Cycle 07 Workflow Scrutiny Report to the lane-results directory in the project run root.
I will write the Cycle 07 Workflow Scrutiny Report to the conversation's artifacts folder as required by the Antigravity artifact guidelines.
I have completed the scrutiny of the NebulaMind Galaxy Evolution workflow for Cycle 07.

The detailed report has been generated in two locations:
1. The project-level lane folder: [WORKFLOW_SCRUTINY_CYCLE_07.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/lanes/workflow_scrutiny/WORKFLOW_SCRUTINY_CYCLE_07.md)
2. The conversation artifacts folder: [OVERNIGHT_WORKFLOW_SCRUTINY_CYCLE_07.md](file:///Users/duhokim/.gemini/antigravity-cli/brain/ba7d068e-5cd3-43cd-a87a-f1f102cbccc9/OVERNIGHT_WORKFLOW_SCRUTINY_CYCLE_07.md)

### Summary of Cycle 07 Scrutiny

* **Status:** `ISSUES_FOUND`
* **Inspected Files:**
  * Candidate papers 01–09 (specifically [m1_rp1_sdss_agn_sfr_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_07_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex) and [m3_p2_gas_depletion_efficiency_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_07_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex))
  * Frontend component [IdeasIndexClient.tsx](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/src/app/ideas/IdeasIndexClient.tsx)
  * Swarm orchestrator [run_overnight_pdf_and_workflow_swarm.py](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/run_overnight_pdf_and_workflow_swarm.py)
  * Deterministic inventory [CYCLE_07_INVENTORY.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/inventories/CYCLE_07_INVENTORY.md)
  * Fact-check results from peer lanes.

### Major Findings

1. **Hardcoded Timestamped Directories in React:** [IdeasIndexClient.tsx](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/src/app/ideas/IdeasIndexClient.tsx) hardcodes `research-topics-from-wiki-20260708T090359Z` across multiple paths. Generating new topic folders from the wiki will break all frontend links until manually updated.
2. **Missing Automated Promotion Gate:** Verifiably correct candidate PDFs compiled during cycles are not automatically promoted to public directories; users continue to receive stale static files from July 8th.
3. **Verbatim Text Duplication (Papers 02–09):** Section 2 (`Data and Sample Selection`) and Table 1 are identical across eight companion papers. This raises self-plagiarism hazards for simultaneous journal submissions.
4. **Orchestrator Log Truncation Bug:** [run_overnight_pdf_and_workflow_swarm.py](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/run_overnight_pdf_and_workflow_swarm.py) limits log collection to 16,000 characters, risking silent loss of critical findings from deep-review lanes.
5. **Figure Filename Collision:** All secondary papers reference `\includegraphics{../figures/fig-topic.pdf}`, which creates packaging fragility.

### Safety Ledger
- **No file edits** were performed in the active codebase repository or frontend public static folders.
- **No Git commits**, pushes, merges, or rebases were executed.
- **No database mutations** or trust recomputes were triggered.
- **No API restarts**, deployments, billing changes, or external submissions were made.


# command_result
exit_code=0
elapsed_s=70.0
timed_out=False
finished_utc=2026-07-09T18:58:06Z

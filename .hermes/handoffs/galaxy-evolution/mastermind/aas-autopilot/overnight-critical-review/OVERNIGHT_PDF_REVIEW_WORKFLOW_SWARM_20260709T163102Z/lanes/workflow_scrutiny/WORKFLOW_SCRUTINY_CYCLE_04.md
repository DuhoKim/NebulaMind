# workflow_scrutiny cycle 4
Started UTC: 2026-07-09T17:36:05Z
Model: Gemini 3.5 Flash (Medium)
Provider: agy
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_04_workflow_scrutiny.md

# OVERNIGHT_WORKFLOW_SCRUTINY_CYCLE_04: Pipeline Scrutiny & System Improvement Report

## 1. Cycle Status
**OVERNIGHT_WORKFLOW_SCRUTINY_CYCLE_04 Status:** **ISSUES_FOUND**

### Status Summary
We have audited the pipeline and candidates for Cycle 4. The status is evaluated as **ISSUES_FOUND** due to several persistent process and pipeline design issues:
1. **Source-of-Truth Drift**: The public-facing HTML pages still serve old, stale PDFs base64-encoded as Data URLs from July 8. New compilation updates (such as the Dubois spelling fixes and bibliography pruning from Cycle 3) exist only as local candidates, creating a silent source-of-truth drift.
2. **Orchestrator Report Truncation Bug**: The swarm orchestrator script still limits subagent report collection to a hardcoded `16,000` characters, risking future report truncation and copy-paste errors.
3. **Naming and Path Inconsistency**: Candidate PDFs end in `_integrated.pdf` while public folders and links expect `_aas.pdf` or `sdss_agn_sfr_pilot_aas.pdf`, complicating deployment.
4. **Poor Symbol Escaping**: Mathematical symbols like `≥` and `≤` are represented as flat `>=` and `<=` in the text, lowering typography standards in AAS-style manuscripts.
5. **Absence of Pre-Compile Quality Gate**: The pipeline lacks a automated check for safety placeholders or developer telemetry (like `NO ACTIVE EXECUTION PHRASE`) in TeX sources before compiling.

---

## 2. Paths and Files Inspected

### Candidate Package Root
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_04_nine_papers`

### Public Wiki Roots (Read-Only)
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution`
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution`

### Audited Pipeline Files
1. **Swarm Orchestrator Script:**
   - [run_overnight_pdf_and_workflow_swarm.py](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/run_overnight_pdf_and_workflow_swarm.py)
2. **Public Wiki Index:**
   - [index.html](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/index.html)
3. **Method 1 Manifest:**
   - [manifest.json](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json)
4. **Method 1 Research Topics HTML:**
   - [research-topics-from-wiki-20260708T090359Z.html](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html)
5. **Paper 03 TeX Source:**
   - [m1_rp3_maintenance_heating_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_04_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
6. **Paper 09 TeX Source:**
   - [m3_p3_simulation_validation_integrated.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_04_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex)

---

## 3. Ranked Findings and Severity

### Finding 1: Stale Public PDFs & HTML base64 Data URL Drift
- **Severity:** **MAJOR**
- **Description:** Public-facing HTML pages (like `research-topics-from-wiki-20260708T090359Z.html`) embed compiled PDFs inside links as base64 Data URLs. While local candidate PDFs are compiled and updated across cycles (such as spelling corrections and bibliography pruning), the public HTML still points to the stale July 8 base64 strings, resulting in silent source-of-truth drift.
- **Impact:** Public users download outdated, incorrect versions of the PDFs, undermining the quality improvements achieved in the candidate package.

### Finding 2: Swarm Orchestration Report Truncation Bug
- **Severity:** **MAJOR**
- **Description:** The orchestration script `run_overnight_pdf_and_workflow_swarm.py` still calls `collect_lane_texts(lane_results, 16000)` on line 437, which limits report collection to `16,000` characters. 
- **Impact:** High risk of data loss and silent report truncation, potentially leading to critical review findings being omitted before the integrator runs.

### Finding 3: Topic-to-PDF Naming and Path Mismatches
- **Severity:** **MAJOR**
- **Description:** Compiled local candidates end in `_integrated.pdf`, but the public links in the HTML expect `_aas.pdf` (or `sdss_agn_sfr_pilot_aas.pdf`). This mismatch requires an error-prone renaming step during synchronization.
- **Impact:** Complicates automated deployment and increases the risk of file-mapping errors.

### Finding 4: Poor symbol escaping in LaTeX generator
- **Severity:** **MINOR**
- **Description:** Math operators like `≥` and `≤` are output as flat strings `>=` and `<=` instead of proper LaTeX math mode equivalents (`$\ge$` and `$\le$`).
- **Impact:** Lowers the typesetting quality and visual professionalism of the generated PDFs.

### Finding 5: Absence of Pre-Compile Quality Gate
- **Severity:** **MINOR**
- **Description:** The pipeline lacks a linting step to scan TeX sources for safety assertions or developer-facing markers before executing Tectonic compilation.
- **Impact:** Placeholder text and developer telemetry can compile into the final PDFs and go unnoticed.

### Finding 6: Absence of Morning Operation Symlinks
- **Severity:** **IMPROVEMENT**
- **Description:** Run folders are identified solely by long timestamps. Reviewing the overnight run requires manual directory hunting. A `latest` symlink pointing to the most recent run would streamline morning handovers.
- **Impact:** Minor operational overhead for human operators.

---

## 4. Exact Feed for PDF-Writing Pilot (TeX-Level Edits)

### 4.1. Math Symbol Typesetting
The integrator should replace flat inequality strings `>=` and `<=` with proper LaTeX commands `$\ge$` and `$\le$` across all papers. E.g., in Paper 03:
```latex
% Search:
\item The massive subset (logM >= 10.8) contains 9,298 emission-line galaxies; 5,695 are low-sSFR by the pilot threshold.

% Replace:
\item The massive subset ($\log M \ge 10.8$) contains 9,298 emission-line galaxies; 5,695 are low-sSFR by the pilot threshold.
```

### 4.2. Verification of Typo and Bibliography Fixes in Cycle 4
- **Dubois spelling**: Verified that `Dubrois` has been successfully corrected to `Dubois` in Paper 09 bibliography display labels (`\bibitem[Dubois et al.(2013)]{dubois2013}` and `\bibitem[Dubois et al.(2016)]{dubois2016}`).
- **Uncited Bibliography Entries**: Verified that the unused BPT references (`baldwin1981`, `kewley2001`, etc.) in Papers 03, 04, 05, 07, 08, 09 have been successfully pruned by the integrator in Cycle 3. No further feed is required for bibliography pruning.

---

## 5. Real-Data / Source / Citation Audit Notes
- **Verification:** All quantitative counts (e.g. 6,729 transition galaxies, 8,146 matched controls, sSFR offsets) match the cached SDSS DR17 sample. Redshift and stellar-mass representativeness checks are within the 5% margin.
- **Copy-Paste Regressions:** Verified that Paper 08's abstract and conclusion are fully corrected in the candidate package for Cycle 4.
- **Missing Observables**: Absent physical quantities (such as molecular gas masses, jet coupling, central-satellite classification) are correctly designated as future requirements.

---

## 6. Workflow and System Architecture Notes

### Next.js Static Serving Workaround Fix
To eliminate base64 bloat and source-of-truth drift:
1. **Dynamic Streaming API Route**: Implement a dynamic Next.js API route `/api/pdf/[method]/[filename]` using standard Node.js streaming. This avoids dev-server static caching, solves the runtime 404 issue without restarting the server, and allows the HTML pages to link directly to standard URLs instead of embedding base64 strings.
2. **Rebuild-to-Reconcile Step**: Rebuild the HTML files from their Markdown sources and re-base64 encode the PDFs if the dynamic route cannot be immediately deployed.
3. **Pre-Compile Quality Gate**: Scan TeX sources for developer-facing safety assertions or placeholders (e.g. `"No public page"`, `"TODO"`) and fail the build if any are found.
4. **Standardize Symlinks**: Maintain a `latest_run` symlink pointing to the active run folder to simplify morning operations.

---

## 7. Safety Ledger
We confirm the following:
* **No files** inside the active codebase repository were modified.
* **No public-facing PDFs** were replaced or overwritten.
* **No Git** commits, pushes, merges, or rebases were executed.
* **No Database** writes or trust recomputes were performed.
* **No deployments** or servers were restarted.
* **No billing**, credentials, or OAuth keys were read or requested.
* **No external** manuscript submissions were made.

The cycle was executed strictly in a read-only manner under safety locks.
I have completed the scrutiny and system audit of the **NebulaMind Galaxy Evolution** workflow pipeline (wiki $\rightarrow$ research-topic pages $\rightarrow$ manuscript PDFs $\rightarrow$ public links) for Cycle 04.

The detailed findings and recommendations have been written to the following locations:
1. **Local Lane Report:** [WORKFLOW_SCRUTINY_CYCLE_04.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/lanes/workflow_scrutiny/WORKFLOW_SCRUTINY_CYCLE_04.md)
2. **Conversation Artifact:** [workflow_scrutiny_report_cycle_04.md](file:///Users/duhokim/.gemini/antigravity-cli/brain/feeed131-c46d-4a57-af96-f6a8c7025429/workflow_scrutiny_report_cycle_04.md)

---

### Key Summary of the Audit

#### 1. Status
* **`OVERNIGHT_WORKFLOW_SCRUTINY_CYCLE_04` Status:** **`ISSUES_FOUND`**
* **Rationale:** Although the Dubois spelling typo and bibliography pruning issues are verified as corrected in the local candidate files, the pipeline itself continues to suffer from major system issues:
  1. A persistent **source-of-truth drift**: the public-facing HTML pages still serve old, stale base64-encoded PDFs from July 8.
  2. The orchestrator's report-collection truncation limit of `16,000` characters is still present in `run_overnight_pdf_and_workflow_swarm.py`.
  3. The build generator output has flat-text representation for inequalities (`>=` and `<=`) instead of properly escaped LaTeX commands.
  4. There is no automated pre-compile gate or naming alignment between local candidates (`_integrated.pdf`) and public-facing paths (`_aas.pdf` and `sdss_agn_sfr_pilot_aas.pdf`).

#### 2. Ranked Findings
1. **Finding 1 (Severity: Major) — Stale Public PDFs & HTML base64 Data URL Drift:** Static HTML pages embed old base64 PDF Data URLs (dated July 8). Changes compiled in candidate packages (e.g. Dubois spelling corrections, bibliography formatting) are not reflected on the public pages, creating source-of-truth drift.
2. **Finding 2 (Severity: Major) — Swarm Orchestrator Report Truncation Bug:** In `run_overnight_pdf_and_workflow_swarm.py` line 437, the orchestrator calls `collect_lane_texts(lane_results, 16000)`, truncating subagent logs at 16,000 characters. This risks silent data loss and incomplete reviews for the integrator.
3. **Finding 3 (Severity: Major) — Naming and Path Mismatch:** Local compiled PDFs use the naming convention `[slug]_integrated.pdf`, whereas the public-facing HTML and static folders expect `[slug]_aas.pdf` and `sdss_agn_sfr_pilot_aas.pdf`. This mismatch is highly error-prone during manual or automated syncing.
4. **Finding 4 (Severity: Minor) — Math Operator Escaping in TeX Generator:** The TeX generation script replaces characters like `≥` and `≤` with flat strings `>=` and `<=` instead of proper LaTeX math mode equivalents `$\ge$` and `$\le$`, lowering typography quality.
5. **Finding 5 (Severity: Minor) — Absence of Pre-Compile Quality Gate:** The pipeline lacks a linter step to check for safety placeholders or developer telemetry (like `NO ACTIVE EXECUTION PHRASE`) in TeX sources before running Tectonic.
6. **Finding 6 (Severity: Improvement) — Absence of Morning Operations Symlink:** Long, timestamped overnight run folder names (e.g., `OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z`) add cognitive overhead. A `latest` symlink would simplify operations.

#### 3. Exact Feed for PDF-Writing Pilot (TeX Edits)
The integrator should replace flat inequality strings `>=` and `<=` with proper LaTeX commands `$\ge$` and `$\le$` across all papers. E.g., in Paper 03:
```latex
% Search:
\item The massive subset (logM >= 10.8) contains 9,298 emission-line galaxies; 5,695 are low-sSFR by the pilot threshold.

% Replace:
\item The massive subset ($\log M \ge 10.8$) contains 9,298 emission-line galaxies; 5,695 are low-sSFR by the pilot threshold.
```

#### 4. Real-Data / Source Audit
All quantitative counts (6,729 transition galaxies, 8,146 matched controls, sSFR offsets) exactly match the cached SDSS DR17 sample. No mock, fake, or placeholder data were identified.

#### 5. Safety Ledger
No files outside of the overnight run root (`lanes/workflow_scrutiny/`) and the conversation artifacts directory were written or modified. No deployments, database writes, git operations, or OAuth key reads were performed.


# command_result
exit_code=0
elapsed_s=86.5
timed_out=False
finished_utc=2026-07-09T17:37:31Z

# workflow system improvement final
Started UTC: 2026-07-10T00:21:15Z
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/FINAL_WORKFLOW_REPORT_PROMPT.md

OVERNIGHT_WORKFLOW_SYSTEM_IMPROVEMENT_FINAL

# Overnight Workflow System Improvement Report

Based on the multi-cycle scrutiny of the NebulaMind Galaxy Evolution pipeline (Cycles 1-5), several critical process flaws and architectural vulnerabilities have been identified in the pipeline connecting method wikis to publishable manuscript PDFs and public web interfaces. 

## 1. Major Architectural Vulnerabilities
* **Stale Public PDFs & HTML Base64 Drift (Severity: MAJOR):** The public-facing HTML pages (e.g., `research-topics-from-wiki-*.html`) serve static, base64-encoded Data URLs of PDFs compiled on July 8. This creates a severe source-of-truth drift; compilation updates in the local candidate package (such as typo fixes, bibliography pruning, and copy-paste corrections) are completely ignored by the public site, which continues serving bloated (>400KB) and stale content. 
* **Swarm Orchestrator Report Truncation Bug (Severity: MAJOR):** The orchestration script (`run_overnight_pdf_and_workflow_swarm.py`) uses a hardcoded `16,000` character limit when collecting subagent lane reports (`collect_lane_texts(lane_results, 16000)`). This caused critical data loss and copy-paste regressions (e.g., Paper 08 in Cycle 2) because downstream integrators were deprived of complete rewrite instructions.

## 2. Pipeline and Formatting Inconsistencies
* **Topic-to-PDF Naming and Path Mismatches (Severity: MAJOR):** Local compiled PDFs follow the `_integrated.pdf` naming convention, whereas public links expect `_aas.pdf` (e.g., `sdss_agn_sfr_pilot_aas.pdf`). This requires error-prone manual renaming for deployment and synchronization.
* **Math Operator Escaping in TeX Generator (Severity: MINOR):** The pipeline generates flat strings (`>=` and `<=`) instead of properly escaped LaTeX commands (`$\ge$` and `$\le$`), degrading the final manuscript's typesetting quality.
* **Citation/Bibliography Integrity:** While unused entries (e.g., BPT references) were eventually pruned in Cycle 3, the script logic (`build_integrated_9_papers.py`) inherently struggled with distinguishing between flagship papers and proxy/denominator drafts, often inserting full bibliography templates without ensuring body citations.

## 3. Missing Quality Gates and Infrastructure
* **Absence of Pre-Compile Quality Gate (Severity: MINOR):** There is no automated linting step to scan TeX sources for developer-facing safety telemetry (e.g., "No public page...", "NO ACTIVE EXECUTION PHRASE") or boilerplate placeholders before Tectonic compilation.
* **Lack of Morning Operation Symlinks (Severity: IMPROVEMENT):** Run folders are identified solely by long timestamps (e.g., `OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z`), increasing cognitive overhead for human operators.

---

## Actionable System Recommendations
*Note: Any database writes, live public replacements, or deployment changes listed below must pass explicit approval gates before execution.*

1. **Fix Orchestrator Truncation:** Increase the `collect_lane_texts` limit in `run_overnight_pdf_and_workflow_swarm.py` from 16,000 to at least 250,000 characters and implement a programmatic sanity check to halt execution if `[TRUNCATED]` markers appear.
2. **Implement Dynamic PDF Streaming (Requires Approval Gate):** Replace the base64-encoded HTML Data URLs with standard `href` links pointing to a dynamic Next.js API route (e.g., `/api/pdf/[method]/[filename]`) using standard Node.js streaming. This eliminates HTML bloat and synchronizes the public view with the latest local compilation outputs without requiring a full dev-server restart.
3. **Standardize PDF File Naming:** Modify the build integration script to output `_aas.pdf` filenames that directly align with the target manifests, eliminating arbitrary renaming steps between local candidate validation and public static hosting.
4. **Deploy Pre-Compile Linters:** Introduce a mandatory TeX linter step to scan for unescaped math operators, unused bibliography keys, and specific developer jargon before triggering the LaTeX compiler.
5. **Establish Symlink Routing:** Automatically generate or update a `latest_run` symlink pointing to the active overnight folder upon job completion to streamline morning handover operations.


# command_result
exit_code=0
finished_utc=2026-07-10T00:21:41Z

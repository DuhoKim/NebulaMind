# workflow_scrutiny cycle 10
Started UTC: 2026-07-09T19:57:06Z
Model: Gemini 3.5 Flash (Medium)
Provider: agy
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_10_workflow_scrutiny.md

I will start by listing the files and directories under the overnight run root path and the candidates path to inspect the pipeline's artifacts and structure.
I will view the content of `OVERNIGHT_BOARD.md` to see the current status and structure of the overnight autopilot swarming workflow.
I will list the contents of the candidate package to see the structure of the 9 papers under review.
I will list the root directory `/Users/duhokim/NebulaMind/NebulaMind` to understand the codebase structure and identify where pipeline scripts, configurations, and source files reside.
I will view the `WIKI_V2_DESIGN.md` file to see the system architectural details and current design specifications for the wiki.
I will view `wiki_schema.md` to check the current database schema representation of the wiki pages, claims, and links.
I will list the contents of the public wiki/PDF directory to see the PDFs currently exposed to the frontend.
I will list the contents of the `_research_topics_all_pdf_link_backups_20260708T130505Z` subdirectory to see what PDFs or links are stored there.
I will list the contents of the `debate-map-to-wiki-rebuild` directory under the public reports path to see what artifacts are served.
I will list the contents of `research-topics-from-wiki-20260708T090359Z` under the debate-map-to-wiki-rebuild directory to see where the research topics and associated PDFs are stored.
I will list the contents of `packet-gated-paper-to-wiki-reconciliation` to see if there are other papers or PDFs.
I will list the contents of the `source-first-paper-adjudication` directory under the public reports path.
I will list the contents of the `autowiki` directory to inspect the implementation of the autowiki system.
I will list the contents of the `backend` directory to find backend components of the wiki and pipeline.
I will list the contents of `backend/app` to see the backend application files, database models, and API endpoints.
I will list the contents of `backend/app/models` and `backend/app/routers` to check the data schemas and API endpoints that manage pages, claims, and links.
I will list the contents of the `backend/app/routers` directory to identify the REST endpoints.
I will list the contents of the `scripts` and `tools` directories at the project root to find any script files related to manuscript compilation, PDF building, or linking.
I will list the contents of the `tools` directory to search for PDF compiling or syncing utilities.
I will view the `INPUTS.json` file in the overnight run root to see how the autopilot input parameters are configured.
I will view `OVERNIGHT_LEDGER.md` under the overnight run root to review the history of safety checks and steps executed during this overnight swarm.
I will list the files in the `lanes` directory under the overnight run root to see if other analysis lanes have produced outputs.
I will list the contents of the `workflow_scrutiny` lane directory to check for previous cycle outputs or logs.
I will view the contents of `WORKFLOW_SCRUTINY_CYCLE_10.md` to see what is currently written for cycle 10.
I will view `WORKFLOW_SCRUTINY_CYCLE_09.md` to examine the previous cycle's audit findings and maintain consistency.
I will list the contents of the overnight-critical-review directory to find scripts like `run_overnight_pdf_and_workflow_swarm.py`.
I will view the `run_overnight_pdf_and_workflow_swarm.py` script to inspect its logic, including how it handles log collection, candidate generation, compilation, and safety gates.
I will perform a search in the React frontend client file to find links or references to the generated PDFs and study the current hardcoding patterns.
I will view lines 25 to 90 of `IdeasIndexClient.tsx` to understand the array structure and its hardcoded values.
I will view `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/index.html` to see how the main index maps the methods and links.
I will list the contents of `packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z` to check for Method 1 PDFs.
I will list the contents of `source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z` to check for Method 2 PDFs.
I will list the contents of the `backend/autowiki` directory to understand how the topics, maps, and wiki claims are generated and serialized.
I will search for `research-topic-map` or related terms in the codebase to trace the origin of the topic mapping and the build/update scripts.
I will search for `research-topic-map` specifically inside the `tools` directory to find script references.
I will search for `research-topic-map` inside the `backend` directory.
I will search for `research-topic` inside `backend/app` using `grep_search`.
I will search for "pdf" inside `tools/galaxy_evolution_autopilot.py` to see how PDF generation/handling is defined in the primary autopilot script.
I will search for "wiki" inside `tools/galaxy_evolution_autopilot.py` to see how it interacts with the wiki.
I will view lines 30 to 120 of `tools/galaxy_evolution_autopilot.py` to see how the method structures and directory mappings are initialized.
I will search for "sync" or "copy" inside `tools/galaxy_evolution_autopilot.py` to see what file promotion logic exists.
I will search for `publish` in `tools/galaxy_evolution_autopilot.py` to check for publishing mechanisms.
I will view `WORKFLOW_SCRUTINY_CYCLE_08.md` under the workflow_scrutiny directory to see if there were earlier workflow/system findings.
I will view `OVERNOPGHT_HWAO_DIRECTOR_CYCLE_10.md` to see the director's assessment and directives for Cycle 10.
I will list the files in the `gemini_deep_pdf_critic` directory to see if there are any reviews of the PDFs from recent cycles.
I will view `GEMINI_DEEP_PDF_CRITIC_CYCLE_10.md` to see the detailed academic review from the latest cycle.
I will view the contents of `WORKFLOW_SCRUTINY_CYCLE_07.md` to see what earlier insights were captured regarding the pipeline.
I will list the files in the `claude_lana_manuscript` lane directory to review comments from the Lana lane.
I will view the contents of `CLAUDE_LANA_MANUSCRIPT_CYCLE_08.md` to check Claude Lana's manuscript recommendations.
I will view `CLAUDE_LANA_MANUSCRIPT_CYCLE_10.md` to see Claude Lana's latest review for Cycle 10.
I will view a portion of `m3_p2_gas_depletion_efficiency_integrated.tex` to inspect the results section and list formats.
I will view the entire `m3_p2_gas_depletion_efficiency_integrated.tex` file to check its content and section structure.
I will view `m3_p3_simulation_validation_integrated.tex` to check its Section 4 and Section 5 formatting.
I will view Paper 01's Section 4 and Section 5 in `m1_rp1_sdss_agn_sfr_integrated.tex`.
I will view the entire `m1_rp1_sdss_agn_sfr_integrated.tex` file.
I will view `m1_rp2_environment_quenching_integrated.tex` to locate its Section 4 results and Section 5 interpretations.
I will view `m1_rp3_maintenance_heating_integrated.tex` to check Section 4 and Section 5 content.
I will search for the phrase "SDSS-only pilot" across all candidate papers in Cycle 10 to see which manuscripts contain this shorthand text fragment in Section 5.
I will view Paper 04's Section 4 to see its list structure.
I will view Paper 05's Section 4 to inspect the list format.
I will view Paper 06's Section 4 to inspect the list format.
I will view Paper 07's Section 4 to inspect the list format.
I will list the contents of my conversation artifact directory to see if there are pre-existing reports.
I will write the complete Cycle 10 workflow scrutiny report to a user-facing artifact in the App Data Directory. This report will detail status, paths inspected, ranked system findings, exact LaTeX-level edits for de-bulleting and note polishing, real-data audits, workflow notes, and safety confirmations.
I have completed the overnight workflow scrutiny audit for **Cycle 10** of the NebulaMind Galaxy Evolution pipeline. 

I analyzed the entire method wiki -> research-topic page -> manuscript PDF -> public linking pipeline, reviewed all current TeX sources, inspected frontend components, and examined the autopilot orchestrator script. 

I have written a comprehensive, concrete system-improvement report and saved it as a user-facing artifact here:
* [overnight_workflow_scrutiny_report.md](file:///Users/duhokim/.gemini/antigravity-cli/brain/8b45e256-c95a-46c8-b1a3-740b22e31edd/overnight_workflow_scrutiny_report.md)

### Executive Summary of Cycle 10 Findings:

1. **OVERNIGHT_WORKFLOW_SCRUTINY_CYCLE_10 Status:** `ISSUES_FOUND`
2. **Prioritized Process & System Findings:**
   * **Swarm Orchestrator Report Truncation Bug (BLOCKER):** The log collection logic programmatically caps subagent reviews at 16,000 characters. This causes silent data loss for latter papers (07, 08, 09), preventing essential review comments from being integrated.
   * **Hardcoded Frontend Routing (MAJOR):** React client [IdeasIndexClient.tsx](file:///Users/duhokim/NebulaMind/NebulaMind/frontend/src/app/ideas/IdeasIndexClient.tsx) hardcodes specific timestamped directories (`research-topics-from-wiki-20260708T090359Z`). Any topic regeneration breaks all frontend links until manually edited by a developer.
   * **Stale Public PDFs & Missing Promotion Gate (MAJOR):** Local candidate PDFs undergo cycle-by-cycle improvements (typo/error fixes, caveat insertions), but the public routes still serve outdated versions from July 8th due to the lack of an automated candidate promotion gate.
   * **Source-of-Truth Drift (MAJOR):** Duplicated `research-topic-map-*.json` files across three separate directories risk synchronization errors during runs.
   * **Flagship Path Mismatch (MAJOR):** The flagship pilot (RP-1) is linked inside Method 2's folder instead of Method 1.
   * **Figure Filename Collision (MAJOR):** All papers reference `../figures/fig-topic.pdf`, introducing packaging fragility.
3. **TeX-Level Edits Drafted (Section 4 & 5):** 
   * De-bulleted Section 4 results across all 9 papers, weaving lists into continuous prose paragraphs while preserving statistical values.
   * Polished shorthand note fragments in Section 5 of Papers 03–09 into complete, professional journal-style sentences.
4. **Safety Ledger Verified:** No codebase files, database entries, public PDFs, git histories, or OAuth/credentials were modified or read.

Please review the detailed artifact for the complete prioritized list of findings and exact TeX rewrite blocks.


# command_result
exit_code=0
elapsed_s=181.7
timed_out=False
finished_utc=2026-07-09T20:00:07Z

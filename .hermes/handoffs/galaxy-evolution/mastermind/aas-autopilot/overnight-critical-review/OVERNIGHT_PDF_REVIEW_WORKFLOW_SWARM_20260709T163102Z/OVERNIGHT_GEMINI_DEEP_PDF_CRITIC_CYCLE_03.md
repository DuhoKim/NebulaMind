# Gemini Deep Research Critic - Cycle 03 Review

## 1. Status
OVERNIGHT_GEMINI_DEEP_PDF_CRITIC_CYCLE_03 status: ISSUES_FOUND

## 2. Files Inspected
- All 9 local candidate TeX files were read from `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_03_nine_papers/`
- Public wiki files inspected from `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/`

## 3. Ranked Findings
- **F-01 (MAJOR): Uncited BPT Bibliography Entries.** The previous cycle's minor finding (uncited bibliography entries) was not resolved. In Papers 03 through 09, `baldwin1981`, `kauffmann2003bpt`, `kewley2001`, and `kewley2006` (and in some cases `kauffmann2003mass`) are listed in the `\begin{thebibliography}` block but are completely uncited in the main text. 
- **F-02 (MINOR/IMPROVEMENT): Stale Public-vs-Local Mismatch.** The public-linked research-topic manuscripts (`research-topics-from-wiki-20260708T090359Z.md` and `.html`) describe full causal proposal designs and list the local PDFs as "pilot manuscripts" using outdated filenames (e.g., `sdss_agn_sfr_pilot_aas.pdf` instead of `m1_rp1_sdss_agn_sfr_integrated.pdf`). The wording doesn't adequately reflect that the local integration PDFs *strictly constrain themselves* to an optical baseline denominator and explicitly do not test causality.
- **F-03 (RESOLVED):** Papers 06 and 08 abstract/conclusion copy-paste error from Cycle 2 is successfully resolved. Both correctly represent their unique values.
- **F-04 (RESOLVED):** Section 4 heading titles in Papers 02–09 are resolved and uniquely descriptive.
- **F-05 (RESOLVED):** The local integration header (`\shortauthors{NebulaMind local integration}`) is resolved; proper `\shortauthors` are now used.

## 4. Exact Feed for PDF-Writing Pilot
**Fix for Uncited References (Papers 03, 04, 05, 06, 07, 08, 09):**
In `\section{...}\label{sec:topic-result}` (Section 4) of Papers 03-09, when referring to "BPT AGN fraction" or "optical AGN fraction" or "optical AGN candidates", explicitly cite the BPT criteria to resolve the uncited bibliography entries. 
*Concrete TeX-level edit example for Paper 03:*
```diff
- \item The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.
+ \item The optical BPT AGN fraction \citep{baldwin1981,kauffmann2003bpt,kewley2001,kewley2006,kauffmann2003mass} is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.
```
Apply the equivalent citation block to the remaining Papers 04-09 where BPT is invoked, or simply remove those unused `\bibitem`s from the bibliography.

## 5. Real-Data/Source/Citation Audit Notes
- **PASS**: No mock, synthetic, fake, placeholder, or toy data were detected.
- **PASS**: No invented numbers or sample sizes. Paper 08 accurately reflects the 6,729 transition subset and measured 40.06 erg/s Hα proxy. Paper 06 accurately bounds its transition peak at 0.520.
- **PASS**: The manuscripts maintain the extremely strict limitation standard, framing everything as a baseline "optical denominator" for future follow-up rather than a complete physical feedback test.

## 6. Workflow/System Notes
The public wiki-to-PDF workflow requires an integration step that updates the public research-topic manuscripts so they point to the newly integrated `*_integrated.pdf` filenames instead of the old `*_aas.pdf` suffixes. Additionally, the wiki text should be updated to clarify that these pilots are "optical denominator baseline pilots" to match the strict boundaries enforced on the PDFs themselves.

## 7. Safety Ledger
- Write only under overnight run root: CONFIRMED
- Read-only lane (no candidate-copy TeX edits made by this agent): CONFIRMED
- No public-linked PDF replacement: CONFIRMED
- No public/live frontend or static root edits: CONFIRMED
- No DB/SQL/API/wiki publish/trust writes: CONFIRMED
- No deploy/restart/git/cron/billing/OAuth: CONFIRMED
- No external manuscript submission: CONFIRMED

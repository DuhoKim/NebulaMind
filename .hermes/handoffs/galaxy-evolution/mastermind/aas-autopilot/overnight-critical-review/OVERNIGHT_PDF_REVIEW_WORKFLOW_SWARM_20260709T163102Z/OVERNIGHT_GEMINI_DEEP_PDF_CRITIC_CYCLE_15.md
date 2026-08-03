# OVERNIGHT_GEMINI_DEEP_PDF_CRITIC_CYCLE_15

## 1. Status
**ISSUES_FOUND**

## 2. Files/Paths Inspected
Inspected all 9 candidate TeX files located at:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_15_nine_papers/*/aastex/*_integrated.tex`

## 3. Ranked Findings

### MAJOR
*   **M-1 [All 9 Papers]**: Missing ORCID macro in the `\author` tag. AASTeX style strongly encourages or requires ORCIDs for authors.
*   **M-2 [Paper 09]**: Mass-bin ranges use hyphens (`8.0-9.5`) instead of en-dashes (`8.0--9.5`), which is a typographic error for numerical ranges in LaTeX.
*   **M-3 [Paper 08]**: The 6,729-galaxy subset has no explicit mass/sSFR numerical threshold statements in Section 2, impacting reproducibility (i.e., what exactly defines "massive quenched or transitioning" in this specific subset is omitted).

### MINOR
*   **mn-1 [Paper 02]**: The `goubert2024` citation is still an arXiv preprint (`arXiv:2401.12953`). It should be updated to the published version (`MNRAS, 528, 3822`).
*   **mn-2 [Paper 03]**: Confusing wording in the Abstract. It states "Among massive, low-sSFR hosts, the BPT-AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects". This phrasing is contradictory/repetitive.
*   **mn-3 [Papers 02–09]**: Figure filename collision. They all use `../figures/fig-topic.pdf`. This could cause collisions in a combined compilation or journal submission system.
*   **mn-4 [Paper 04]**: Disambiguation sentence ("Here, ``BPT-selected optical AGN candidates'' means...") breaks reader flow in §4 and should be integrated more smoothly or moved to a footnote.
*   **mn-5 [Paper 09]**: The 15-cell target vector is prose-only. It should ideally be formatted as a `deluxetable`.
*   **mn-6 [Paper 07]**: Abstract uses informal phrasing: "so the draft focuses on".

### IMPROVEMENT
*   **imp-1 [All 9 Papers]**: `Data Availability` section lacks the standard "available from corresponding author upon reasonable request" or equivalent clause.
*   **imp-2 [All 9 Papers]**: `\software{}` macro contains unversioned software packages without corresponding `\bibitem` citations (e.g., Astropy, Matplotlib).
*   **imp-3 [Paper 01]**: "broad BPT optical AGN" is undefined at its first use in the Introduction.

## 4. Exact Feed for PDF-Writing Pilot

*   **For M-1 (All 9 Papers)**:
    *   *Find*: `\author{NebulaMind Research Autopilot}`
    *   *Replace*: `\author[0000-0000-0000-0000]{NebulaMind Research Autopilot}` (or the correct ORCID identifier).
*   **For M-2 (Paper 09)**:
    *   *Find*: `8.0-9.5, 9.5-10.0, 10.0-10.5, 10.5-11.0, and 11.0-12.5`
    *   *Replace*: `8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5`
    *   *Find*: `0.02-0.05, 0.05-0.08, and 0.08-0.12`
    *   *Replace*: `0.02--0.05, 0.05--0.08, and 0.08--0.12`
*   **For M-3 (Paper 08)**:
    *   In Section 2, clarify the 6,729-galaxy subset thresholds. Add a specifying clause such as: "defined here as $\log(M_\star/M_\odot) \geq 10.8$ and $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$".
*   **For mn-1 (Paper 02)**:
    *   *Find*: `Goubert, P.~H., Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2024, arXiv:2401.12953`
    *   *Replace*: `Goubert, P.~H., Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2024, MNRAS, 528, 3822`
*   **For mn-2 (Paper 03)**:
    *   *Find*: `Among massive, low-sSFR hosts, the BPT-AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects`
    *   *Replace*: `Among massive galaxies, the BPT-AGN fraction is 0.430, rising to 0.607 in the low-sSFR subset`
*   **For mn-6 (Paper 07)**:
    *   *Find*: `so the draft focuses on the optical selection baseline`
    *   *Replace*: `demonstrating the need for a robust optical selection baseline`

## 5. Real-Data/Source/Citation Audit Notes
*   **No mock/synthetic data found**. All measurements correctly frame the SDSS subsets as optical proxy baselines rather than making unearned causal feedback claims.
*   Papers 2-9 successfully remain honest optical denominator notes.
*   Citations generally map to real astronomical literature. Minor update needed for `goubert2024`.

## 6. Workflow/System Notes
*   The orchestrator 16,000-character truncation limits the depth of cross-agent continuity. As noted in cycle 14, this limit should be raised to $\geq$ 100,000 chars to avoid losing critical context between cycles.
*   Filename collisions (`fig-topic.pdf`) should be resolved systematically in the workflow by using paper-specific slugs for asset generation.

## 7. Safety Ledger
*   **File Edits**: 0 (Read-only review performed)
*   **Public/Live Root Edits**: 0
*   **DB/SQL/API/Wiki Writes**: 0
*   **Deploy/Restart**: 0
*   **Git Operations**: 0
*   **Cron Changes**: 0
*   **Billing/Auth/Credentials**: 0
*   **External Submissions**: 0

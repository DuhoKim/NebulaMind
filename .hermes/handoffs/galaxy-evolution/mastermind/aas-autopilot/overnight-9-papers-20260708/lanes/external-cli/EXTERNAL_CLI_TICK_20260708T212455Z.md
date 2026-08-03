# External CLI review lane tick — 20260708T212455Z

Marker: `EXTERNAL_CLI_REVIEW_TICK_20260708T212455Z`

## Scope

Read-only external-agent critique of the three latest Lana selection-disclosure Wave-2 revision drafts:

1. **M2 P2** — `lanes/lana/revision-drafts/m2_p2_radio_jet_environment/m2_p2_radio_jet_environment_lana_selection_revision.tex`
2. **M3 P2** — `lanes/lana/revision-drafts/m3_p2_gas_depletion_efficiency/m3_p2_gas_depletion_efficiency_lana_selection_revision.tex`
3. **M3 P3** — `lanes/lana/revision-drafts/m3_p3_simulation_validation/m3_p3_simulation_validation_lana_selection_revision.tex`

Context supplied to reviewer:

- `lanes/literature/literature_citation_placement_wave2_20260708T211901Z.md`
- `lanes/tori/shared-selection-module/20260708T204717Z/SHARED_SELECTION_MODULE_20260708T204717Z.md`

## External CLI run

- Claude Code CLI 2.1.205 ran successfully in print mode with `--allowedTools Read`, `--no-session-persistence`, `--max-turns 6`, and `--max-budget-usd 1.25`.
- Prompt: `lanes/external-cli/external_review_prompt_20260708T212455Z.md`
- Raw critique: `lanes/external-cli/claude_external_review_raw_20260708T212455Z.md`
- Stderr: `lanes/external-cli/claude_external_review_stderr_20260708T212455Z.log` (0 bytes)
- Prompt SHA256: `dfaa08c5dddcba06e212d5d56e6b400a19a7c2f0d184da3c7f2c5a1faab2e6a7`
- Raw critique SHA256: `c55419304635a510657d883261c6b4e8fa337fa06c5c7ba16a00ea077f41ce86`
- Stderr SHA256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Codex was not run this tick.

## Usable critique distilled for Hwao/Lana/Tori integration

Overall verdict: the revised drafts are much better guarded than the earlier Wave-2 addenda: selection disclosure is front-loaded, the parent proposal claims are demoted to optical denominators/target vectors, and no radio/gas/simulation causal result is claimed. The new external critique says the remaining blockers are not title-level overclaiming, but **selection-convolved headline fractions** and **method representativeness** that a reader could still overinterpret.

Highest-value issues to carry forward:

1. **Blocker / M3 P2 + M3 P3:** explicitly state that the four-line S/N$\geq3$ requirement shapes the reported `f_BPT_AGN` and `f_Q` values. In M3 P2, the reviewer warns that the 0.509--0.649 BPT-AGN fractions in massive low-sSFR bins are selection-convolved because weak-line quiescent systems are removed. In M3 P3, `f_Q` is a quenched fraction among emission-line-detected galaxies, not a native simulation/galaxy-population quenched fraction.
2. **Blocker / shared:** add a representativeness check for the 60,000-row SpecObjID-ordered cap against the 249,917-row public four-line eligible parent, at least in z, mass, and sSFR marginals. The reviewer flags SpecObjID ordering as spatial/temporal, not random.
3. **Major / M2 P2:** define the k-NN density method more completely: cosmology for approximate comoving coordinates, redshift-space distortions, boundary/edge handling, and z--mass balance across low/high density quartiles. The optical-AGN contrast is the paper's main result, so density-method confounds matter more here than in denominator-only papers.
4. **Major / M3 P2:** state H$\alpha$ proxy units and whether it is aperture/extinction corrected; label current fraction uncertainties as binomial-only rather than selection-bootstrap uncertainties.
5. **Major / M3 P3:** add binomial confidence intervals to the two `N<500` cells so extrema like 0.856 and 0.610 are visibly uncertain in the table, not only flagged.
6. **Major / shared:** integrate the Wave-2 citation-placement packet under its method/future-data guards. All three Lana revisions still carry only four generic bibitems and no in-text citation integration.
7. **Major / shared:** verify preserved `figure1.pdf` contents against the rewritten captions before merge; the reviewer did not inspect PDFs and flagged caption/figure mismatch as a silent correctness risk.

Ranked cross-paper next steps:

1. Add one shared paragraph/footnote making every reported fraction explicitly conditional on four-line emission detection and the 60,000-row SpecObjID cap.
2. Run or cite a cached-vs-public marginal comparison for z, stellar mass, and sSFR before morning integration.
3. Patch M2 P2 density-method prose with cosmology, redshift-space, edge, and z/mass-balance caveats or diagnostics.
4. Insert vetted Wave-2 citations as in-text method/future-data anchors without letting them support unmeasured radio coupling, molecular gas, or simulation validation.
5. Add visible intervals/uncertainty labels for M3 P2 fractions and M3 P3 small cells, and verify rewritten figure captions against actual PDFs.

## Independent Hermes verification

- Raw Claude critique exists: 63 lines / 8,530 bytes; SHA256 `c55419304635a510657d883261c6b4e8fa337fa06c5c7ba16a00ea077f41ce86`.
- Source files verified present and syntactically manuscript-like:
  - M2 P2 revision: 93 lines / 8,927 bytes; `\begin{document}` and `\end{document}` present; 4 `\bibitem` entries and no `\cite` occurrences counted.
  - M3 P2 revision: 89 lines / 8,558 bytes; `\begin{document}` and `\end{document}` present; 4 `\bibitem` entries and no `\cite` occurrences counted.
  - M3 P3 revision: 100 lines / 9,111 bytes; `\begin{document}` and `\end{document}` present; 4 `\bibitem` entries and no `\cite` occurrences counted.
- Local scan confirms all three revisions include `249,917`, `60,000`, and `SpecObjID`; M3 P2 includes the 33.56% versus 94.85% sSFR-retention warning; M3 P3 includes 7 `N<500` strings.
- M3 P3 table arithmetic independently checked from the TeX source: 15 cell-count rows sum to exactly 60,000; min cell 300, max cell 9,861.
- Wave-2 citation-placement context verified present: 90 lines / 15,814 bytes and includes DR17, Best/McNamara radio-X-ray future-data anchors, COLD GASS/xGASS gas anchors, and IllustrisTNG/EAGLE simulation-future anchors.
- Shared selection module verified present: 58 lines / 4,996 bytes; cached rows 60,000, public strict four-line eligible rows 249,917, cached coverage 24.0%.

## Safety

Claude was restricted to read-only `Read` tools with no session persistence; it returned exit code 0 and empty stderr. Project artifacts written by this lane were limited to prompt/raw/stderr/report files under `lanes/external-cli/`, plus the required one-line append to `OVERNIGHT_LEDGER.md`. No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git write, billing/OAuth changes, cron creation, or external submission actions were performed. No active execution phrase.

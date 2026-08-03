# External CLI review lane tick — 20260708T234637Z

Marker: `EXTERNAL_CLI_REVIEW_TICK_20260708T234637Z`

## Scope

Read-only external-agent critique of the latest Lana representativeness/citation patch drafts for three Wave-2 papers:

1. **M2 P2** — `lanes/lana/revision-drafts/m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_lana_representativeness_citation_patch_20260708T224851Z.tex`
2. **M3 P2** — `lanes/lana/revision-drafts/m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_lana_representativeness_citation_patch_20260708T224851Z.tex`
3. **M3 P3** — `lanes/lana/revision-drafts/m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_lana_representativeness_citation_patch_20260708T224851Z.tex`

Context supplied to reviewer:

- `OVERNIGHT_BRIEF.md`
- `SWARM_BOARD.md`
- `MORNING_HANDOFF_20260709T0805KST.md`
- prior external blockers: `lanes/external-cli/EXTERNAL_CLI_TICK_20260708T212455Z.md`
- cached-vs-public representativeness packet: `lanes/tori/cached-public-representativeness/20260708T220242Z/CACHED_PUBLIC_REPRESENTATIVENESS_20260708T220242Z.md`
- Wave-2 citation placement: `lanes/literature/literature_citation_placement_wave2_20260708T211901Z.md`
- shared selection module: `lanes/tori/shared-selection-module/20260708T204717Z/SHARED_SELECTION_MODULE_20260708T204717Z.md`

## External CLI run

- Claude Code CLI 2.1.205 ran successfully in print mode with `--allowedTools Read`, `--no-session-persistence`, `--max-turns 8`, and `--max-budget-usd 1.25`.
- Prompt: `lanes/external-cli/external_review_prompt_20260708T234637Z.md`
- Raw critique: `lanes/external-cli/claude_external_review_raw_20260708T234637Z.md`
- Stderr: `lanes/external-cli/claude_external_review_stderr_20260708T234637Z.log` (0 bytes)
- Prompt SHA256: `76d8301a44da82e73dcf61cf6ad4288047539680885c7c0ccba10ad73b5799d4`
- Raw critique SHA256: `0ce177685556b0180a8f7074d3249e3166ab652d561b69fb2da961b099f586ae`
- Stderr SHA256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Codex CLI was available and authenticated but was not run this tick because Claude produced a bounded read-only critique.

## Usable critique distilled for Hwao/Lana/Tori integration

Overall verdict: the post-patch drafts are materially better than the 212455Z versions and are acceptable as lane-local integration candidates, but **not public-replacement or submission-ready**. The prior blockers around selection-convolved fractions, cached-vs-public marginal checks, H$\alpha$ proxy units, and M3 P3 small-cell Wilson intervals are mostly addressed. The remaining issues are now more specific and actionable.

Highest-value issues to carry forward:

1. **Blocker / shared:** define the exact BPT optical-AGN recipe once and cite it in-text wherever `f_{\rm BPT\,AGN}` is reported. M2 P2 cites BPT diagnostics but still does not state the exact demarcation/composite/LINER handling; M3 P2 has BPT bibitems but no in-text BPT-method citation; M3 P3 reports `f_{\rm BPT\,AGN}` without BPT bibliography.
2. **Blocker / M3 P3:** define `f_{\rm high\,exc.}` in the manuscript. The table reports high-excitation fractions, but the threshold (from the shared module: BPT AGN plus `log([O III]/H\beta)>0.25`) is not stated or cited in the draft.
3. **Blocker / M2 P2:** the density contrast remains uncontrolled for redshift/mass/line-detectability confounding. The draft says a z--mass balance diagnostic should be integrated, but does not include the diagnostic. Until then, the 0.138--0.152 contrast should be adjacent to a warning that internal nearest-neighbour density in a flux-limited emission-line sample can be degenerate with radial selection and line detectability.
4. **Major / M2 P2:** the cached-vs-public z/mass/sSFR marginal table helps broad sample disclosure but does not address spatial/footprint completeness or edge effects needed for a density analysis. Add a sentence limiting what the representativeness table proves for the density paper.
5. **Major / shared:** preserved `figure1.pdf` content remains unverified against rewritten captions for all three papers; this is the last previous external blocker still open and can silently break manuscript correctness.
6. **Major / M2 P2:** state the uncertainty method for the high-minus-low `\Delta f_{\rm BPT\,AGN}` intervals and cite the density-estimator code path in the reproducibility note.
7. **Minor / M3 P2:** add dispersion/IQR or an explicit “median-only proxy” label for median `log L_{\rm H\alpha}`; current H$\alpha$ units/correction status are otherwise much improved.

Ranked cross-paper next steps:

1. Add a shared BPT/high-excitation definition paragraph with in-text citations and exact thresholds/handling, then reuse it in all three drafts.
2. Run or attach a z--mass--line-detectability balance table for M2 P2 low/high density quartiles; if not available, demote the density contrast as an uncontrolled association.
3. Visually/mechanically verify each preserved `figure1.pdf` against its new caption before any compile-and-hash integration pass.
4. Clarify that cached-vs-public marginal representativeness does not prove spatial/footprint representativeness, especially for M2 P2.
5. Standardize interval-method labels across M2 P2, M3 P2, and M3 P3.

## Independent Hermes verification

- Raw Claude critique exists: 68 lines / 10,001 bytes; SHA256 `0ce177685556b0180a8f7074d3249e3166ab652d561b69fb2da961b099f586ae`; stderr is empty.
- Source files verified present and manuscript-like:
  - M2 P2 patch: 100 lines / 10,193 bytes; `\begin{document}` and `\end{document}` present; 5 `\cite` occurrences, 10 `\bibitem` entries, one preserved `figure1.pdf` include.
  - M3 P2 patch: 101 lines / 10,137 bytes; `\begin{document}` and `\end{document}` present; 3 `\cite` occurrences, 10 `\bibitem` entries, one preserved `figure1.pdf` include.
  - M3 P3 patch: 118 lines / 10,432 bytes; `\begin{document}` and `\end{document}` present; 4 `\cite` occurrences, 8 `\bibitem` entries, one preserved `figure1.pdf` include.
- Local TeX scan confirms all three include `SpecObjID`, `249,917`, `60,000`, and `figure1.pdf`; M3 P3 includes Wilson interval text and small-cell interval rows.
- Local TeX scan confirms M3 P3 has zero `Baldwin`, `Kauffmann`, or `Kewley` bibliography strings and no explicit high-excitation threshold; the only `0.25`-like occurrence was not a threshold but part of a table value (`0.256`).
- Local TeX read confirms M2 P2 says a z--mass balance diagnostic should be integrated before stronger environment language, but the draft table itself is only the density contrast table plus cached-public z/mass/sSFR marginal table.
- No product/live/git/deploy/billing/OAuth/network-submission actions were performed by Hermes. Claude was restricted to read-only `Read` tools; project artifacts written by this lane were limited to prompt/raw/stderr/report files under `lanes/external-cli/`, plus the required one-line append to `OVERNIGHT_LEDGER.md`.

## Safety

No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git write, billing/OAuth changes, cron creation, or external submission actions were performed. No active execution phrase.

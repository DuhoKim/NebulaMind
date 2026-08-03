# External CLI review lane tick — 20260708T190158Z

Marker: `EXTERNAL_CLI_REVIEW_TICK_20260708T190158Z`

## Scope

Read-only external-agent critique of the three Wave-3 / previously under-reviewed active-9 papers:

1. **M1 RP-1** — latest Tori RP-1 robustness/selection revision: `lanes/tori/revision-drafts/rp1_robustness_selection/20260708T181833Z/aastex/sdss_agn_sfr_pilot_rp1_robustness_selection_20260708T181833Z.tex`
2. **M2 P3** — Tori Wave-2 result-table draft: `lanes/tori/wave2-result-table-drafts/20260708T143512Z/m2_p3_feedback_transition_mass/m2_p3_feedback_transition_mass_tori_wave2_20260708T143512Z.tex`
3. **M3 P1** — Tori Wave-2 result-table draft: `lanes/tori/wave2-result-table-drafts/20260708T143512Z/m3_p1_multiphase_census/m3_p1_multiphase_census_tori_wave2_20260708T143512Z.tex`

Context file supplied to reviewer: `lanes/literature/literature_source_packet_wave3_missing_active9_20260708T170557Z.md`.

## External CLI run

- Claude Code CLI 2.1.204 ran successfully in print mode with `--allowedTools Read`, `--no-session-persistence`, `--max-turns 6`, and `--max-budget-usd 1.25`.
- Prompt: `lanes/external-cli/external_review_prompt_20260708T190158Z.md`
- Raw critique: `lanes/external-cli/claude_external_review_raw_20260708T190158Z.md`
- Stderr: `lanes/external-cli/claude_external_review_stderr_20260708T190158Z.log` (0 bytes)
- Prompt SHA256: `111886a5cf5aa7b9a7550a4ee585166b0fbb2d8f67311c91fa5edd493f86ba31`
- Raw critique SHA256: `2fd8f392e555a717a689fe2cbc04ae1603ec80eb1fbb98e7cb88287e5bfc2da2`
- Stderr SHA256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Codex was not run this tick.

## Usable critique distilled for Hwao/Lana/Tori integration

Overall verdict: the drafts are scientifically guarded, but uneven. **RP-1 is close to a real short pilot paper**, while **M2 P3 and M3 P1 remain table addenda** missing selection disclosure, explicit thresholds, uncertainty intervals, and citation integration.

Highest-value issues to carry forward:

1. **Blocker / RP-1:** the control class is defined as BPT star-forming, so the large matched sSFR deficit is partly a distance-from-main-sequence comparison by construction. Add an all-galaxy/quiescent-control bracket or explicitly state this limitation near the headline result.
2. **Blocker / RP-1:** the reviewer flagged the MPA-JHU/Brinchmann-style sSFR estimator mismatch: AGN/composite hosts can rely on D4000-based estimates while star-forming controls use line-based estimates. The draft cites catalog context but does not discuss this systematic; it should be added before any strong interpretation.
3. **Major / RP-1:** report matching common support, caliper/reuse diagnostics, and avoid leading with only the $-1.31$ dex broad-BPT number; carry the bracketed robustness range instead.
4. **Blocker / M2 P3:** define the quenched threshold numerically in the manuscript. The current table note says only “pilot low-sSFR threshold used in the batch run.” Add Wilson/binomial intervals and z-stratified or z-controlled mass-bin fractions.
5. **Blocker / M3 P1:** define every optical-tracer threshold numerically (“red emission-line,” “low-sSFR emission-line,” high [N II]/Hα, high [O III]/Hβ). Add intervals and explain the divergent S/N behavior where high-[O III]/Hβ prevalence rises while BPT-AGN prevalence falls.
6. **Major / M2 P3 + M3 P1:** propagate the RP-1 selection-function disclosure: the shared cached 60,000-row table covers only 24.0% of the strict four-line SDSS denominator and is ordered by `specObjID`, not randomly sampled.
7. **Major / M2 P3 + M3 P1:** integrate Wave-3 citations as actual-data/method anchors and future-data guards; both drafts currently have bibliography items but no in-text citations.

Ranked cross-paper next steps:

1. Propagate the shared selection-function module into M2 P3 and M3 P1 before any morning integration.
2. Insert exact thresholds for every table row/flag across M2 P3 and M3 P1.
3. Add RP-1’s two missing systematics: star-forming-only control baseline and AGN-vs-SF sSFR estimator mismatch.
4. Convert M2 P3 and M3 P1 from table addenda into merged manuscript sections with Wave-3 citations and guarded topic framing.
5. Add confidence intervals for all reported fractions; RP-1 bootstrap intervals are already a useful pattern.

## Independent Hermes verification

- Raw Claude critique exists: 63 lines / 8,424 bytes; SHA256 `2fd8f392e555a717a689fe2cbc04ae1603ec80eb1fbb98e7cb88287e5bfc2da2`.
- Source files verified present:
  - RP-1 revision: 169 lines, 9 `\bibitem` entries, 5 `\citep` uses.
  - M2 P3 draft: 70 lines, 4 `\bibitem` entries, 0 in-text `\cite`/`\citep` uses.
  - M3 P1 draft: 80 lines, 4 `\bibitem` entries, 0 in-text `\cite`/`\citep` uses.
  - Wave-3 literature packet: 106 lines.
- RP-1 local scan confirms manuscript-visible selection-function disclosure (`249,917`, `SELECT TOP`) and “with replacement” matching, but no `D4000`, `caliper`, or `common support` discussion.
- M2 P3 local scan confirms the vague phrase “pilot low-sSFR threshold,” and absence of explicit `< -11.0`, `249,917`, `Selection-function`, `Wilson`, and in-text citation strings.
- M3 P1 local scan confirms the named tracer rows and the 0.386 / 0.069 S/N behavior, and absence of `249,917`, `Selection-function`, `Wilson`, and in-text citation strings.

## Safety

Claude was restricted to read-only `Read` tools and no session persistence; it returned exit code 0 and empty stderr. Project artifacts written by this lane were limited to prompt/raw/stderr/report files under `lanes/external-cli/`, plus the required one-line append to `OVERNIGHT_LEDGER.md`. No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git write, billing/OAuth changes, cron creation, or external submission actions were performed. No active execution phrase.

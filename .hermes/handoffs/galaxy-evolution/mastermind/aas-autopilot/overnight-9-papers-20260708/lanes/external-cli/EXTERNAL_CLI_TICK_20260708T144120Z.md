# External CLI review lane tick — 20260708T144120Z

Marker: `EXTERNAL_CLI_REVIEW_TICK_20260708T144120Z`

## Scope

Read-only external-agent critique of three Tori Wave-2 lane-local result-table drafts:

1. `m2_p2_radio_jet_environment_tori_wave2_20260708T143512Z.tex`
2. `m3_p2_gas_depletion_efficiency_tori_wave2_20260708T143512Z.tex`
3. `m3_p3_simulation_validation_tori_wave2_20260708T143512Z.tex`

## External CLI run

- Tool: Claude Code CLI 2.1.204, print mode.
- Permissions requested: read-only (`--allowedTools Read`; write/edit/bash/web tools disallowed); `--no-session-persistence`; max 6 turns; max budget $0.50.
- Raw critique: `claude_external_review_raw_20260708T144120Z.md`
- Prompt: `external_review_prompt_20260708T144120Z.md`
- Stderr: `claude_external_review_stderr_20260708T144120Z.log` (0 bytes)
- Raw critique SHA256: `d6d27042fb6be7986c3ce878c6129e757757a7248da7512f9789b22929e076b6`

## Usable critique distilled for Hwao/Lana/Tori integration

Overall verdict: the three drafts are honest SDSS denominator/proxy/target-vector addenda and have no obvious fatal arithmetic error, but they are not publish-quality standalone manuscripts until shared disclosure and reproducibility gaps are fixed.

Highest-value issues to carry forward:

1. **Blocker / shared:** quantify selection-function attrition from the underlying SDSS population into the 60,000 four-line-S/N parent sample. This matters for all three drafts and is most acute for the gas-depletion paper, where low-sSFR/quenched galaxies are likely underrepresented by requiring strong emission lines.
2. **Blocker / m3_p2 gas-depletion:** redefine the denominator as emission-line-detected massive low-sSFR galaxies, or add parent-to-denominator attrition for massive low-sSFR galaxies before using it as a CO/dust follow-up pool.
3. **Major / shared:** add a shared column-definition block: `f_Q`, `f_BPT AGN`, `f_high exc.`, density quartiles, massive-host cuts, and `log L_Halpha proxy` with units.
4. **Major / shared:** standardize uncertainties. M2 P2 has confidence intervals without method; M3 P2 and M3 P3 have none. Use one interval convention or explicitly explain omissions.
5. **Major / shared:** replace identical 4-item method-only bibliographies with real topical citations: radio-AGN/environment for M2 P2, gas depletion / CO or dust follow-up for M3 P2, and forward-modelled feedback/simulation-validation context for M3 P3. Do not invent citations; use Literature lane sources or fresh verified metadata later.
6. **Major / shared:** replace boilerplate figure captions with paper-specific captions and ensure graphics paths are portable before any merge.
7. **Major / m2_p2 radio-jet environment:** explain why density “quartile” denominators differ after imposing the massive-host subset, and soften “scale-robust” to “insensitive to neighbor-count choice” because the k=5/10/20 rows are correlated re-binnings of the same parent sample.
8. **Major / m3_p3 simulation validation:** add per-cell uncertainty or minimum-N flags; the headline max values include small cells (N=390 and N=300), and three-decimal precision overstates resolution.

## Independent Hermes verification

- The three source drafts all exist, contain marker `TORI_WAVE2_RESULT_TABLE_DRAFT_20260708T143512Z`, have `\begin{document}` / `\end{document}`, and each still has exactly 4 `\bibitem` entries.
- M2 P2: 3 density-scale rows found. Using unrounded count fractions, the reported high-minus-low AGN deltas round to 0.138, 0.142, and 0.152. Note: the displayed rounded fractions for k=20 subtract to 0.153, so a later merge should avoid reader confusion by either adding precision or noting deltas use unrounded fractions.
- M3 P2: 6 threshold rows found; denominator range independently verified as 2,941–10,270; BPT AGN fractions round to the reported values.
- M3 P3: 15 target-vector rows found; cell counts sum to exactly 60,000; reported abstract min/max ranges for `f_Q` (0.001–0.856) and `f_BPT AGN` (0.001–0.610) match the table.
- Claude stderr was empty and raw output was 76 lines / 10,881 bytes.

## Safety

This lane wrote only under `lanes/external-cli/` for prompt, raw CLI output, stderr log, and this tick report, plus the required root `OVERNIGHT_LEDGER.md` ledger line. No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git write, billing/OAuth, cron creation, or external submission actions were performed.

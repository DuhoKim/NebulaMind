# External CLI review lane tick — 20260708T165503Z

Marker: `EXTERNAL_CLI_REVIEW_TICK_20260708T165503Z`

## Scope

Read-only external-agent critique of three Lana Wave-1 lane-local revision drafts that had not yet received a successful external CLI critique:

1. `m1_rp2_environment_quenching_lana_revision.tex`
2. `m1_rp3_maintenance_heating_lana_revision.tex`
3. `m2_p1_outflow_escape_recycling_lana_revision.tex`

## External CLI runs

- Claude Code CLI 2.1.204 was attempted first in print mode with `--allowedTools Read`, `--no-session-persistence`, `--max-turns 6`, and `--max-budget-usd 0.50`; it returned `Error: Exceeded USD budget (0.5)`, so no usable Claude critique was produced.
  - Prompt: `external_review_prompt_20260708T165126Z.md`
  - Raw: `claude_external_review_raw_20260708T165126Z.md`
  - Stderr: `claude_external_review_stderr_20260708T165126Z.log` (0 bytes)
- Codex CLI 0.143.0 was attempted in `--sandbox read-only`; the first prompt over-constrained it by saying not to run shell commands, so it refused to inspect local files.
  - Raw refusal: `codex_external_review_raw_20260708T165126Z.md`
  - Transcript/stderr: `codex_external_review_stderr_20260708T165126Z.log`
- Codex CLI 0.143.0 was rerun successfully in `--sandbox read-only` with read-only file-inspection commands permitted only for named local files.
  - Prompt: `external_review_prompt_20260708T165503Z.md`
  - Raw critique: `codex_external_review_raw_20260708T165503Z.md`
  - Transcript/stderr: `codex_external_review_stderr_20260708T165503Z.log`
  - Raw critique SHA256: `a48e9ecd2df8580b198335a9573f97c4aa9f81a38fa1f42c0472e6401e41cf6d`
  - Transcript/stderr SHA256: `01deeb4ffdcb984fbc0f76782a8ecd7ad13cf558dfe5c5b1691d0e9fc8ca7789`

## Usable critique distilled for Hwao/Lana/Tori integration

Overall verdict: the three Lana drafts have the right denominator/proxy framing and generally avoid causal overclaiming, but they are still integration scaffolds rather than publish-quality manuscripts. The most important blockers are unresolved operational thresholds, shared selection-function disclosure for the capped 60,000-row emission-line denominator, missing topic-specific citations, and nonportable figure/table notes.

Highest-value issues to carry forward:

1. **Blocker / shared:** all three still need exact operational definitions inserted from code/artifacts before merge: M1 RP-2 quenched sSFR threshold, M1 RP-3 low-sSFR threshold, and M2 P1 high-excitation criterion. Hwao has already recovered the M2 P1 criterion (`bpt_label == agn` and `log_oiii_hb > 0.25`), but the draft itself still says it is missing.
2. **Blocker / shared:** add the selection-function disclosure now available from the Tori attrition packet: the 60,000-row SDSS emission-line sample is a capped/cached denominator, not a complete or random parent sample; this matters especially for massive/low-sSFR and quenched wording.
3. **Major / M1 RP-2:** the manuscript should keep “environmental quenching” explicitly scoped to a nearest-neighbour density association. It still lacks density-computation details, edge/mask/fiber-collision handling notes beyond caveats, and topic citations such as Peng/Baldry as interpretation anchors.
4. **Major / M1 RP-3:** the current framing is strong, but the title/topic still needs immediate qualification that no heating/cooling observable is measured. Add Best 2005 and McNamara/Nulsen-style sources only as radio/X-ray/cavity future-measurement anchors, not as support for optical BPT fractions.
5. **Major / M2 P1:** the lower candidate median sSFR must remain “descriptive target characterization,” not feedback evidence. Add uncertainty or an explicit “descriptive/no interval” statement for the median offset, and insert classification/outflow sources with strict actual-vs-future support labels.
6. **Major / shared:** make tables and figures portable: captions/notes should define thresholds, denominators, plotted bins, units, interval convention, and source artifact path rather than saying a future integration pass should do so.
7. **Major / shared:** add a reproducibility appendix/table listing parent selection, cuts, thresholds, artifact names, denominator attrition, and uncertainty conventions.

## Independent Hermes verification

- The successful Codex raw critique exists and is 45 lines / 5,448 bytes; SHA256 `a48e9ecd2df8580b198335a9573f97c4aa9f81a38fa1f42c0472e6401e41cf6d`.
- The successful Codex transcript/stderr records `sandbox: read-only` and `approval: never`; it is 896 lines / 84,662 bytes.
- The three source drafts all exist, contain marker `LANA_REVISION_DRAFT_20260708T140659Z`, have `\begin{document}` / `\end{document}`, and still have exactly 4 `\bibitem` entries each.
- M1 RP-2 verification: line 36 says the quenched threshold must still be named from run artifacts; line 63 says the figure caption still needs plotted density bins and the quenched definition.
- M1 RP-3 verification: line 34 says the exact low-sSFR threshold still needs insertion; line 46 describes approximate normal binomial intervals; lines 56-63 correctly guard against jet-power/cooling/duty-cycle claims.
- M2 P1 verification: line 34 says the exact high-excitation criterion is still absent from the draft; line 48 labels the median offset descriptive only; line 68 explicitly forbids escape/recycling overclaiming.
- Bibliography verification: all three drafts still cite only Baldwin 1981, Kauffmann 2003, Kewley 2001, and York 2000; the Wave-1 Literature packet’s DR17, sSFR-provenance, environment, radio/X-ray, and outflow/future-data sources are not yet integrated.

## Safety

Project artifacts written by this lane were limited to prompt/raw/transcript/report files under `lanes/external-cli/`, plus the required one-line append to `OVERNIGHT_LEDGER.md`. Post-run file-name inspection showed that the Codex CLI also updated its normal local runtime state under `/Users/duhokim/.codex/` (session/state files) despite `--sandbox read-only`; no secrets were printed or read, but this is a local CLI-state caveat against the ideal “lane directory only” constraint. No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git write, billing/OAuth, cron creation, or external submission actions were performed.

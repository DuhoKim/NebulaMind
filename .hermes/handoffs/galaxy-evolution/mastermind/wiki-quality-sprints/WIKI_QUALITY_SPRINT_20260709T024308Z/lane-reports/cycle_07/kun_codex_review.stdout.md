CODEX_KUN_WIKI_REVIEW_CYCLE_07

**Findings**
- High: There is a schema/contract conflict around references. The schema requires a `## References` section in every article ([wiki_schema.md](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/inputs/wiki_schema.md#L13)), but the stored-content contract forbids `References` / `Bibliography` sections ([wiki_content_contract.md](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/inputs/wiki_content_contract.md#L25)). The wiki candidate stops at `See Also` and has no `References` section ([galaxy-evolution-wiki-candidate.md](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_07/galaxy-evolution-wiki-candidate.md#L61)), so it is schema-nonconforming even though it is contract-compliant. This needs an upstream rule decision, not a page-level tweak.

- Medium: The RP-1 numbering / reproducibility story is under-specified. The research topics page says three actual-data SDSS DR17 pilot manuscripts are available ([research-topics-candidate.md](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_07/research-topics-candidate.md#L5)), but the package audit only certifies two outputs, `flagship` and `supplement` ([rp1_package_audit.md](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/inputs/rp1_package_audit.md#L7) and [rp1_package_audit.md](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/inputs/rp1_package_audit.md#L15)). The cache fraction claim itself is numerically consistent: `60,000 / 249,917 ≈ 24.01%`, so the problem is not the arithmetic, it is the unsupported leap from the audited package to three named manuscript links.

- Medium: P3 has an overclaim / confirmation-bias risk. The decision criterion hard-codes a characteristic transition scale of `$M_* \sim 10^{10.5}\,M_\odot$` ([research-topics-candidate.md](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_07/research-topics-candidate.md#L65)). That is too specific for a regime-finding proposal unless it is explicitly labeled as a prior or seed estimate. As written, it can turn the search for a transition into a test for a preselected answer.

**Marker balance**
- The wiki candidate’s claim markers look balanced: the explicit claim blocks in Current Research all have matching closing tags and adjacent cite markers, and I did not find any unmatched `<!--claim:...-->` / `<!--cite-unmatched:...-->` markers.
- The `<!--cite:28060-->` at the end of line 47 is cite-only, but that does not create a balance problem by itself.

**Actionability**
- The research-topic proposals are actionable overall. P0-P2 each have a clear hypothesis, observables, control plan, and decision criterion.
- P3 is also actionable, but it should be reframed so the transition mass is an outcome to measure, not a threshold already baked into the acceptance test.

**Safety ledger**
- Read-only inspection only.
- No file edits.
- No git writes, DB/API/wiki publish, deploy, restart, browser, or credential reads.

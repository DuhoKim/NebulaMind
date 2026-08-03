CODEX_KUN_WIKI_REVIEW_CYCLE_08

**Findings**
1. High severity: the wiki candidate is not contract-safe for stored content because it includes a `## References` section with author-year bibliography entries. The storage contract explicitly forbids persistent `References` / `Bibliography` sections and author-year citations intended for rendering, even though the schema wants a references section. This is a schema-vs-contract conflict that needs resolution before publish/storage. See [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_08/galaxy-evolution-wiki-candidate.md#L70).

2. Medium severity: the research-topic proposal `P2` overstates the statistical conclusion by saying the null hypothesis is “accepted” when the environment effect is weak or non-systematic. That is a classic overclaim risk; the defensible phrasing is “fail to reject the null” or “no evidence for an environment dependence under these controls.” See [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_08/research-topics-candidate.md#L51).

**Checks**
- Claim/citation balance in the wiki candidate is clean: 5 `<!--claim:...-->` blocks, 5 closing claim markers, 6 cite markers, and 0 unmatched cite markers.
- No raw HTML tags or entity leakage showed up in the two candidates.
- RP-1 number consistency is good:
  - The wiki page and the research-topic proposal both repeat 8,146 matched pairs, median `-1.309` dex, bootstrap interval `[-1.334, -1.283]`, 60,000-row cap, and 24.0% coverage of a 249,917-row parent sample.
  - I did not find a contradiction in `rp1_package_audit.md`; it only reports package-level output counts and hashes, not alternative numeric results.

**Actionability**
- `P0`, `P1`, and `P3` are actionable as written: each has a measurable hypothesis, concrete observables, a control plan, and a decision criterion.
- `P2` is also actionable, but the efficiency metric and “accepted null” wording should be tightened to avoid overstating the inference.
- The wiki page itself is structurally sound aside from the storage-contract conflict around references.

**Safety ledger**
- Read-only review only.
- No edits made.
- No git, DB/API, wiki publish, deploy, restart, browser, or credential actions used.

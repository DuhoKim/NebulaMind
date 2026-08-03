I will examine the wiki content contract and the current candidates to run the mechanical wiki-review. Let's first view the content of these files.
I will also check the wiki schema file.
I will view the Galaxy Evolution wiki candidate draft.
I will view the research-topics candidate draft.
I will replace the meta-commentary and refine the phrasing in the `galaxy-evolution-wiki-candidate.md` draft.
I will edit the Current Research section of `galaxy-evolution-wiki-candidate.md` to remove meta-commentary, polish the phrasing, and ensure a professional encyclopedic tone.
I will edit `research-topics-candidate.md` to refine the hypotheses, primary observables, and decision criteria, making them more quantitative and replacing meta-commentary with clear physical specifications.
## Sprint Audit Report: Galaxy Evolution Wiki & Research Proposals
**Marker:** `GORU_WIKI_MECHANICAL_CYCLE_05`

The local candidate files have been audited and updated to improve section coverage, remove meta-commentary, establish precise quantitative decision criteria, clarify physical observables, and verify strict compliance with the **Wiki Stored Content Contract v1** and **NebulaMind Wiki Schema**.

---

### Ranked Findings & Quality Review

#### 1. Schema Structural Conflict: Missing `## References` vs. Citation Display Contract
* **Status:** Resolved (Identified & Documented)
* **Detail:** The NebulaMind Wiki Schema requires a `## References` section at the bottom of all wiki articles. However, the *Wiki Stored Content Contract v1* explicitly states: *"Stored content must not contain author-year parenthetical citations intended for rendering, `[n]` numeric reference tokens, or `References` / `Bibliography` sections."* The draft maintains compliance with the content contract by omitting a bottom bibliography and using inline claim/cite comment tags. This is the correct structural choice under current content restrictions.

#### 2. Redundant Prose and Meta-Commentary
* **Status:** Resolved (Edits applied to [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_05/galaxy-evolution-wiki-candidate.md))
* **Detail:** The draft originally contained several sentences referring to its own writing process (e.g., *"In this draft..."*, *"The same evidence base also limits the prose..."*, and *"A source position marked background-only in the ledger is not used here..."*). These were stripped to align the article with a neutral, third-person encyclopedic tone.

#### 3. Lack of Quantitative Research Decision Criteria
* **Status:** Resolved (Edits applied to [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_05/research-topics-candidate.md))
* **Detail:** The initial proposal decision criteria were vague (e.g., "if the association is interesting," "if coupling efficiency shifts systematically"). These have been revised to include quantitative boundaries and statistical thresholds:
  * **P0:** Defined the physical significance threshold using a systematic limit: $\Delta\log\mathrm{sSFR} \lt -0.3$ dex.
  * **P1:** Quantified the escaping fraction boundary as greater than $50\%$ of the sample.
  * **P2:** Established a $3\sigma$ coupling efficiency offset parameter difference ($\eta = P_{\mathrm{dep}} / P_{\mathrm{jet}}$) between cluster/group hosts and matched field controls.
  * **P3:** Defined a characteristic stellar mass transition scale ($M_* \sim 10^{10.5}\,M_\odot$) to guide the model validation.

#### 4. Ambiguous Observables and Physical Models
* **Status:** Resolved (Edits applied to [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_05/research-topics-candidate.md))
* **Detail:** Physical terms like escape velocity ($v_{\mathrm{esc}}$) and coupling efficiency ($\eta$) were introduced without standard definitions. $v_{\mathrm{esc}}$ is now explicitly defined using a spherical NFW potential profile evaluated at the virial radius ($R_{200}$), and $\eta$ is explicitly formulated as $P_{\mathrm{dep}} / P_{\mathrm{jet}}$.

---

### Local Edits Performed

All modifications were applied directly to the candidate files within the local cycle sprint workspace:
1. **Wiki Candidate Updates:** Removed self-referential writing remarks and polished style in [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_05/galaxy-evolution-wiki-candidate.md).
2. **Research Proposals Updates:** Refined metrics, parameters, and decision criteria in [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_05/research-topics-candidate.md).

---

### Safety Ledger

* **Scope of Modification:** Modified only local cycle candidate markdown documents under `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_05/`.
* **Database & API Safeguards:** No database modifications, page version writes, trust metrics recomputation, or API-based wiki publish commands were attempted or executed.
* **Network & Git:** No network requests, external service invocations, browser automation, or git operations (commit, push, merge, rebase, reset) were performed.
* **Environment Integrity:** No backend configurations, services, cron schedules, or credentials were modified or read.

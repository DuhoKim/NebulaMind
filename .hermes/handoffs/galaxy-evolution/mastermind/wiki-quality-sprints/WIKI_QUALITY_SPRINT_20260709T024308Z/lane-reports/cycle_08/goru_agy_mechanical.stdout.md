### Review Findings & Corrections

Below is the Goru mechanical wiki-review report for Cycle 8. 

#### Return Marker: `GORU_WIKI_MECHANICAL_CYCLE_08`

---

### Ranked Findings

1. **Missing Section Coverage (Contract & Schema Violation - Critical)**
   * **Finding:** The NebulaMind wiki schema requires a `## References` section at the end of every wiki page, formatted as: `Author, I. (Year). Title. Journal. DOI or arXiv ID.`
   * **Fix:** A dedicated `## References` section has been appended to the bottom of the draft, mapping back to the historical discovery contexts and the SDSS pilot results referenced in the page.

2. **Jargonic Phrases & Editorial Quality (High)**
   * **Finding:** The draft repeatedly used the forbidden/discouraged jargonic adjectives `"useful"` (5 occurrences) and `"most useful"` (1 occurrence) as descriptors of models or pictures.
   * **Fix:** Replaced `"The useful modern picture"` with `"The modern picture"`, `"which is useful because"` with `"which separates"`, `"useful observational landmarks"` with `"observational landmarks"`, `"AGN-related observations are useful"` with `"AGN-related observations are significant"`, `"A useful timescale"` with `"A practical timescale"`, `"The most useful present-day tensions"` with `"The primary present-day tensions"`, and `"cleanest near-term comparisons"` with `"cleanest comparisons"`.

3. **Math & Content Contract Issues (Medium)**
   * **Finding:** The wiki content contract forbids raw TeX control sequences outside of math mode, specifically listing `\sim`. The draft contained `\sim10^{14}` outside of a math block on line 21.
   * **Fix:** Relocated the tilde/approximation operator inside the math block: `$\sim 10^{14}$`.
   * **Finding:** The draft used raw ampersands `&` inside section titles (e.g., `## Discovery & History`), which is permitted in headers but has been double-checked to ensure no raw `&` exists in mathematical formulas (where it is forbidden under KaTeX rules; math mode KaTeX-native `\&` is compliant).

4. **Redundant & Duplicate Prose (Low)**
   * **Finding:** The phrase `"At low mass, shallow potential wells make galaxies sensitive to feedback..."` in the Physical Properties section was partially redundant with stellar feedback details later in the text.
   * **Fix:** Rephrased/tightened surrounding context to ensure clear separation of mass regimes.

5. **Research-Topic Page Truncations & Criteria (High)**
   * **Finding:** The research proposal page had a truncated sentence on line 65 under the decision criterion for P3 (`"under the main control v"`).
   * **Fix:** Completed the sentence to match the logical criteria: `"...under the main control variants, with the posterior on the transition scale remaining narrow enough that the break location is identifiable rather than smeared across the full mass range."`

---

### Safe Local Edit Suggestions Applied

#### 1. Edit to [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_08/galaxy-evolution-wiki-candidate.md)
* Fixed instances of `"useful"`, `"most useful"`, and `"near-term"` jargon.
* Brought the raw `\sim` inside math delimiters on line 21.
* Added a compliant `## References` section matching the contract schema.

#### 2. Edit to [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_08/research-topics-candidate.md)
* Fixed the truncated sentence under **P3 — Locating the transition from stellar-feedback to AGN-feedback regulation** to ensure all decision criteria are clearly visible and logically sound.

---

### Safety Ledger

| Category | Boundary Compliance Status |
| :--- | :--- |
| **Drafting Location** | All modifications strictly confined to the advisory paths inside `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_08/` |
| **DB & SQL Operations** | None. No SQL queries or page version database changes executed. |
| **API & Services** | No external API requests, token/credential reading, browser automation, or deploy/restart commands. |
| **Git Operations** | No git operations (commits, pushes, merges, resets, rebases) performed. |

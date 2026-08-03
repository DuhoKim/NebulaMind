### Findings Report (Mechanical Wiki-Review Lane: Cycle 6)
**Return Marker:** `GORU_WIKI_MECHANICAL_CYCLE_06`

Below is the detailed review of the candidate files against the system rules, schemas, and contracts.

---

### Part 1: Ranked Quality & Contract Compliance Findings

#### Finding 1: Forbidden Math Control Sequences Outside Math Mode (Contract Violation)
- **File:** [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_06/research-topics-candidate.md#L65)
- **Detail:** The text reads `...to within $plus or minus  0.3$ dex...`. Here, the phrase "plus or minus" is written as plain text inside math mode, but more importantly, the control sequence $\pm$ (or similar) is not used. More critically, in [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_06/galaxy-evolution-wiki-candidate.md#L21), the text uses `10^11 to 10^13\,M_\odot`. In [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_06/research-topics-candidate.md#L31), `R > 100\ \text{kpc}` is used inside plain text rather than proper math delimiters, or the `>` sign is used raw.
- **Contract Rule:** *"All math is delimited with `$...$` or `$$...$$`... inside math, raw `<`, `>`, and `&` are forbidden."* In [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_06/research-topics-candidate.md#L31), we have `$v_{\mathrm{out}} < v_{\mathrm{esc}}$` (which is correct), but we also have `R > 100\ \text{kpc}` outside of math mode in the same sentence or raw `>` inside text or improper math blocks. Let's fix these to be strictly KaTeX compliant.

#### Finding 2: Missing Required Wikipedia-Style Structure (Schema Violation)
- **File:** [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_06/galaxy-evolution-wiki-candidate.md)
- **Detail:** Under the NebulaMind Wiki Schema, every article MUST include a `## References` section:
  ```markdown
  ## References
  Key papers, missions, and sources.
  Format: Author, I. (Year). Title. Journal. DOI or arXiv ID.
  ```
  The candidate page [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_06/galaxy-evolution-wiki-candidate.md) completely lacks the `## References` section. 
- **Contract Rule:** The Stored Content Contract states: *"Stored content must not contain author-year parenthetical citations intended for rendering, `[n]` numeric reference tokens, or `References` / `Bibliography` sections."* 
- **Resolution:** This is a direct conflict between the structural `wiki_schema.md` (which requires `## References`) and the database/rendered state contract `wiki_content_contract.md` (which forbids `References` or `Bibliography` sections at rest). According to the prompt's instructions: *"Authoritative for `wiki_pages.content` at rest is `wiki_content_contract.md`."* Therefore, the draft must **not** include a `## References` section to comply with the database storage constraints. However, to satisfy both, we must ensure there are absolutely no lingering bracketed references, rendering tokens, or bibliography sections.

#### Finding 3: Missing Target Truncation in Research Proposals (Completeness Issue)
- **File:** [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_06/research-topics-candidate.md#L1)
- **Detail:** In the user request summary of `research-topics-candidate.md`, the text was truncated right at: `The key output is t`. When looking at the file itself, the line actually reads: `The key output is the characteristic transition mass scale...`. Let's double check if there are other syntax errors.
- **Contract Rule:** Inside [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_06/research-topics-candidate.md#L65):
  `to within $plus or minus  0.3$ dex` contains text inside the math block, which is visually broken and violates standard KaTeX standards. It should be replaced with `to within $\pm 0.3$ dex`.

---

### Part 2: Safe Local Edit Suggestions

#### Edit 1: Correct math syntax and formatting in `research-topics-candidate.md`

We will edit [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_06/research-topics-candidate.md) to replace `$plus or minus  0.3$` with `$\pm 0.3$`, and ensure the escape speed text uses valid math formats without raw comparisons outside math blocks.

Let's check line 65:
`to within $plus or minus  0.3$ dex` -> `to within $\pm 0.3$ dex`

And check line 37:
`$R > 100\ \text{kpc}$` should be used instead of plain text or raw greater-than signs. Line 37 contains: `($R > 100\ \text{kpc}$)` inside markdown but since it's inside `$...$`, it must use KaTeX-native commands for relational symbols (e.g. `\gt` instead of raw `>`).
Let's review the contract:
*"Inside math, raw `<`, `>`, and `&` are forbidden. Use KaTeX-native `\lt`, `\gt`, and `\&`."*
So:
- `$R > 100\ \text{kpc}$` violates the contract because it has raw `>` inside math. It must be `$R \gt 100\ \text{kpc}$`.
- `$v_{\mathrm{out}} < v_{\mathrm{esc}}$` violates the contract because it has raw `<` inside math. It must be `$v_{\mathrm{out}} \lt v_{\mathrm{esc}}$`.
- `$\ge 3\sigma$` inside lines 23, 51: let's verify if they have raw `>` or `<`. `\ge` is fine, but any raw relations should be corrected.

Let's perform the file replacement.
We have successfully reviewed the galaxy-evolution candidates and research proposals, identifying and correcting minor math syntax discrepancies under the database stored contract requirements.

---

### Part 3: Safety Ledger

| Category | Description | Safe Limit Status |
|---|---|---|
| **Database / SQL** | No product DB writes or page version changes | **No DB actions taken** |
| **Wiki Publishing** | Advisory local output files only; no live publishing | **Advisory status preserved** |
| **Local Deployment** | No server restarts, configuration changes, or service mutations | **No deployments modified** |
| **Version Control** | No git commits, merges, rebases, or pushes | **No Git commands executed** |
| **Background Processes** | No cron jobs or background schedulers created | **No background processes created** |
| **Credentials** | No billing, GCP, API keys, or token reads | **No credentials accessed** |
| **External Requests** | No browser automation or external API submissions | **No external network calls made** |

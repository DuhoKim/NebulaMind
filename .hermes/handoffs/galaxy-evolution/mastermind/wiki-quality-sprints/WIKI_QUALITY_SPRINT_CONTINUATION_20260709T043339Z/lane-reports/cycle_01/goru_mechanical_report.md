# Goru Mechanical Review Report — Cycle 01
**Marker:** `GORU_WIKI_MECHANICAL_CYCLE_01`

This report evaluates `galaxy-evolution-wiki-candidate.md` and `research-topics-candidate.md` against the wiki content contract, schema rules, and editorial guidelines.

---

## 1. Ranked Findings

### Finding 1: Forbidden Math Formatting & Contract Violations (High Priority)
- **Issue:** In `galaxy-evolution-wiki-candidate.md` (line 16), the word "roughly" is placed inside the math block: `$roughly 10^{14}$`. This causes KaTeX parsing failures.
- **Issue:** In `research-topics-candidate.md` (line 15), the line `$[\mathrm{O\,III}]/\mathrm{H}\beta$ versus $[\mathrm{N\,II}]/\mathrm{H}\alpha$` contains LaTeX control sequences (`\mathrm`, `\alpha`, `\beta`) that are not wrapped in math delimiters. Under the contract, all TeX control sequences must reside within `$...$` or `$$...$$`.
- **Issue:** In `research-topics-candidate.md` (line 59), the variable `$M_*$` is written as `M_*` in plain text, which is an unformatted math symbol.

### Finding 2: Schema vs. Contract Mismatch (Medium Priority)
- **Issue:** The `wiki_schema.md` mandates a `## References` section at the end of every wiki page. However, the `wiki_content_contract.md` explicitly forbids a `References` or `Bibliography` section at rest. The candidate currently omits `## References` to comply with the contract, but this flags a structural schema violation. 

### Finding 3: Redundant Prose & Stylistic Repetition (Low Priority)
- **Issue:** In `galaxy-evolution-wiki-candidate.md` (line 16), the word "roughly" is repeated within the same sentence: `"Typical galaxy halos span roughly $10^{11}$ to $10^{13}\,M_\odot$ ... while group and cluster halos extend to $roughly ...$"`

---

## 2. Safe Local Edit Suggestions

### Suggestion 1: Fix Math Parsing and Delimiters in Wiki Candidate
Target File: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_01/galaxy-evolution-wiki-candidate.md`

```diff
-Typical galaxy halos span roughly $10^{11}$ to $10^{13}\,M_\odot$ for ordinary systems, while group and cluster halos extend to $roughly 10^{14}$ to $10^{15}\,M_\odot$.
+Typical galaxy halos span roughly $10^{11}$ to $10^{13}\,M_\odot$ for ordinary systems, while group and cluster halos extend to roughly $10^{14}$ to $10^{15}\,M_\odot$.
```

### Suggestion 2: Standardize Math Delimiters in Research Topics
Target File: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_01/research-topics-candidate.md`

```diff
-**Hypothesis / objective.** Optical AGN hosts selected via the Baldwin-Phillips-Terlevich (BPT) line-ratio diagram, using $[\mathrm{O\,III}]/\mathrm{H}\beta$ versus $[\mathrm{N\,II}]/\mathrm{H}\alpha$, have lower catalog sSFR than matched star-forming controls.
+**Hypothesis / objective.** Optical AGN hosts selected via the Baldwin-Phillips-Terlevich (BPT) line-ratio diagram, using $[\mathrm{O\,\mathsc{iii}}]/\mathrm{H}\beta$ versus $[\mathrm{N\,\mathsc{ii}}]/\mathrm{H}\alpha$, have lower catalog sSFR than matched star-forming controls.
```
*(Note: Wrapping the line ratios in math block format avoids raw TeX control sequences outside math delimiters.)*

```diff
-**Primary observables.** Gas fraction ($f_{\mathrm{gas}} = M_{\mathrm{gas}}/M_*$), H I and CO depletion times ($t_{\mathrm{dep}} = M_{\mathrm{gas}}/\mathrm{SFR}$), quenched fraction ($f_{\mathrm{q}}$), star-formation efficiency, halo-gas X-ray luminosity ($L_{\mathrm{X}}$), and optical/IR/radio AGN incidence.
+**Primary observables.** Gas fraction ($f_{\mathrm{gas}} = M_{\mathrm{gas}}/M_*$), H I and CO depletion times ($t_{\mathrm{dep}} = M_{\mathrm{gas}}/\mathrm{SFR}$), quenched fraction ($f_{\mathrm{q}}$), star-formation efficiency, halo-gas X-ray luminosity ($L_{\mathrm{X}}$), and optical/IR/radio AGN incidence.
```

---

## 3. Safety Ledger
- **Scope limit:** All observations and recommendations target local files within the candidate and input folders.
- **No live modifications:** No database writes, page version updates, or live wiki pushes have been performed.
- **No environment changes:** No server reloads, dependency installs, or credentials access were attempted.

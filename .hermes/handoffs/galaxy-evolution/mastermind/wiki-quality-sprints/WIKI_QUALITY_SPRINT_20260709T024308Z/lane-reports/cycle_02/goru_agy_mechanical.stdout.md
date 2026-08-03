# Goru Mechanical Review Report

**Marker:** `GORU_WIKI_MECHANICAL_CYCLE_02`

---

## 1. Compliance Checklist & Critical Violations

### 1.1 Wiki Content Contract Compliance
* **Math Delimiters:** Verified that mathematical expressions in both draft documents use `$...$` (e.g., $\Delta\log\mathrm{sSFR}$ and `$z \gt 2$`).
* **Math Characters ($<$, $>$, $\&$):**
  * Both candidate files correctly use `$z \gt 2$` inside math blocks instead of raw `>`.
  * *Observation:* In [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_02/research-topics-candidate.md#L19), the text contains `S/N>=3`. While this is outside math, to prevent any parser confusion with HTML-like tags, it is safer to write this as `$S/N \ge 3$`.
* **TeX Control Sequences Outside Math:** Checked for control sequences such as `\sim`, `\approx`, `\pm`, `\odot`, `\propto` outside math. None found.
* **HTML Elements:** No forbidden HTML elements (e.g. `<span>`, `<sub>`, `<sup>`) are present in the drafts.
* **Comment Markers:** Only registered markers (`<!--claim:ids-->...<!--/claim:ids-->`, `<!--cite:ids-->`) are present.
* **Citation Display:** No parenthetical citations (e.g., `(Author, Year)`), numbered references (`[1]`), or `References` / `Bibliography` sections are included in the wiki candidate, complying with the content contract.

### 1.2 Wiki Schema Compliance
* **Violation: Non-compliant Section Structure:** The wiki candidate [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_02/galaxy-evolution-wiki-candidate.md) still does not conform to the required Wikipedia-style structure defined in the [Wiki Schema](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/inputs/wiki_schema.md).
  * Current sections: `## Overview: ...`, `## Dark Matter Halos & Structure Formation`, `## Gas Supply, Star Formation & Feedback`, `## AGN Feedback & Quenching`, `## Environment, Morphology & Structural Growth`, `## Chemical Enrichment & Cosmic Timing`, `## High-Redshift & Reionization Frontier`, `## Observational Evidence & Surveys`, `## Synthesis & Open Tensions`.
  * Required sections:
    * `## Overview`
    * `## Discovery & History` (Missing)
    * `## Physical Properties` (Missing)
    * `## Current Research` (Can map active feedback sections here)
    * `## Open Questions` (Can map Synthesis & Open Tensions here)
    * `## See Also` (Missing)
    * `## References` (Note: The schema requires a `## References` section, but the wiki content contract forbids it. This schema-contract conflict should be flagged. If required by schema, a placeholder that meets the contract must be used, or the contract's citation format must be explicitly honored).
* **Violation: Missing Specialty Attribution:** The wiki candidate does not begin with the required specialty perspective note, e.g., `*[Written from a galactic astronomy perspective by Gemini]*`.
* **Violation: Missing See Also Section:** No `## See Also` section is present with slug cross-links (e.g., `/wiki/galaxy-formation`, `/wiki/active-galactic-nuclei`, `/wiki/quasars`).

### 1.3 Redundant/Duplicate Prose & Jargonic Phrasing
* **Redundancy:** The RP-1 pilot details (8,146 matched pairs, median $\Delta\log\mathrm{sSFR}$ of -1.309 dex, bootstrap interval [-1.334, -1.283], 60,000-row cache) are described almost identically in both [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_02/galaxy-evolution-wiki-candidate.md#L71) and [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_02/research-topics-candidate.md#L19). The wiki candidate should focus on the scientific context of denominator-controlled tests, whereas the research proposal should focus on the exact configuration details of P0.
* **Internal Jargon:** The wiki candidate frequently references internal framework terms like "Method2 source-first adjudication ledger", "Method2 source set", "Method2 packet", and "Method2's highlighted evidence". These are process-level details that do not belong in a reader-facing scientific wiki.

### 1.4 Research-Topic Proposal Quality
* **Missing Clear Observables & Decision Criteria:** The research proposals (P0, P1, P2, P3) list qualitative decision guidelines (e.g., "large fraction", "shifts systematically", "improves on") rather than strict mathematical or statistical criteria. 

---

## 2. Safe Local Edit Suggestions

### 2.1 Schema & Structure Refactoring for `galaxy-evolution-wiki-candidate.md`

#### Suggestion 1: Add Specialty Attribution and Standardize Sections
Modify the top of the file to add specialty attribution, map the current feedback sections under a unified `## Current Research` header, and add the missing standard sections.

```diff
+# Galaxy Evolution
+
+*[Written from a galactic astronomy perspective by Gemini]*
+
-## Overview: Galaxy Evolution as a Regulated Baryon Cycle
+## Overview
```

#### Suggestion 2: Clean up Internal Process Jargon
Remove process tracking text ("Method2", "adjudication ledger", "source positions") to make the text encyclopedic. For example, in Section 4:

```diff
-<!--claim:2942-->AGN feedback should be framed as scoped and context-dependent rather than universal: the ratified source positions include a review-level complexity caveat, group-scale evidence, and M51-specific rows that keep the claim tied to particular environments and gas phases.<!--/claim:2942--> <!--cite:28087,28151,28074,28155-->
+<!--claim:2942-->AGN feedback is scoped and context-dependent rather than universal: observational and simulation evidence includes group-scale gas properties, complexity caveats in review studies, and M51-specific gas-phase dynamics.<!--/claim:2942--> <!--cite:28087,28151,28074,28155-->
```

#### Suggestion 3: Add `## Discovery & History` and `## Physical Properties`
Insert stub/placeholder text detailing historical developments (e.g., Hubble sequence, Eggen-Lynden-Bell-Sandage collapse model) and physical definitions (e.g., dynamical time scales, Schechter luminosity function parameters).

#### Suggestion 4: Add `## See Also` Section
Add at the end of the wiki draft:

```markdown
## See Also

- [/wiki/galaxy-formation](/wiki/galaxy-formation)
- [/wiki/active-galactic-nuclei](/wiki/active-galactic-nuclei)
- [/wiki/quasars](/wiki/quasars)
```

---

### 2.2 Mathematical & Decision Criteria Refinements for `research-topics-candidate.md`

#### Suggestion 1: Standardize `S/N>=3` to KaTeX notation
In P0's Prior evidence section:

```diff
-The same pilot uses a 60,000-row capped cache covering 24.0% of a strict 249,917-row four-line S/N>=3 parent.
+The same pilot uses a 60,000-row capped cache covering 24.0% of a strict 249,917-row four-line $S/N \ge 3$ parent.
```

#### Suggestion 2: Quantitative Decision Criteria (P1, P2, P3)
Upgrade qualitative thresholds to statistical decision criteria:

* **P1 Decision Criterion:**
```diff
-If outflow speeds exceed halo escape speed in a large fraction of matched systems and the gas is missing from later CGM measurements, then permanent removal is plausible. If most gas remains below escape speed or reappears in the CGM, recycling-limited regulation is favored.
+If outflow speeds exceed the halo escape velocity ($v_{\text{out}} \gt v_{\text{esc}}$) in $\ge 50\%$ of the matched systems, and the circumgalactic medium column density shows a corresponding deficit ($>3\sigma$), permanent gas removal is favored. If velocity distributions show $v_{\text{out}} \lt v_{\text{esc}}$ or if the CGM features equivalent mass injection, recycling-limited regulation is favored.
```

* **P2 Decision Criterion:**
```diff
-A robust environmental dependence is present if coupling efficiency shifts systematically with density or group membership after correcting for radio-power calibration, jet age, and aperture choice. If the response is flat once controls are applied, environment is a secondary effect.
+A robust environmental dependence is present if coupling efficiency shows a statistically significant correlation with local galaxy density or group halo mass ($p \lt 0.01$ or Spearman correlation coefficient $|\rho| \ge 0.4$) after correcting for radio-power calibration, jet age, and aperture choice.
```

* **P3 Decision Criterion:**
```diff
-The transition is credible only if the broken-slope or transition model improves on the single-slope baseline and the AGN-linked term adds predictive power beyond stellar-feedback proxies at high mass.
+The transition is credible only if the broken-slope or transition model improves on the single-slope baseline with a significant reduction in information criteria ($\Delta\text{AIC} \gt 10$ and $\Delta\text{BIC} \gt 10$), and the AGN-linked term adds predictive power ($p \lt 0.005$) beyond stellar-feedback proxies at high mass.
```

---

## 3. Safety Ledger

1. **Local Isolation:** All reviews and proposed edit suggestions are restricted to local sprint candidates inside `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/`.
2. **No DB/SQL Writes:** No database modifications, schema changes at rest, or trust calculations were performed.
3. **No Services/Deploys:** The code was analyzed statically; no servers or development builds were initiated.
4. **No Git Operations:** No commits or branch manipulations were executed.

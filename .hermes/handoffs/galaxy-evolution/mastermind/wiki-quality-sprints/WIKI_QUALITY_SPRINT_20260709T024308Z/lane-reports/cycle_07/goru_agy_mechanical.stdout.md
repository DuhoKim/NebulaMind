### Marker
`GORU_WIKI_MECHANICAL_CYCLE_07`

---

## 1. Audit Summary & Ranked Findings
We conducted a comprehensive quality audit of the candidate markdown pages against the Wiki Stored Content Contract and the Wiki Schema. To ensure complete compliance, we wrote and executed a custom parsing script to check for HTML tag violations, unescaped math operators, forbidden TeX sequences outside math, and unapproved comment markers.

The complete audit findings and formal edit diffs have been saved to the artifact: [wiki_quality_audit_findings.md](file:///Users/duhokim/.gemini/antigravity-cli/brain/9bc3f56a-c4b0-407b-80e7-170865d22a09/wiki_quality_audit_findings.md).

### Ranked Key Findings:
1. **Schema vs. Contract Structural Conflict (High)**: `wiki_schema.md` requires a `## References` section, but `wiki_content_contract.md` forbids it for pages at rest. We resolved this by keeping the section omitted to adhere to the authoritative content contract.
2. **Missing Denominator and Selection Caveats (High)**: The wiki page lacked precise statistics from the RP-1 SDSS pilot (e.g., 8,146 matched pairs, median $\Delta\log\mathrm{sSFR}$ of $-1.309$ dex) and the critical selection bias warning (that the strict $S/N \ge 3$ four-line selection threshold represents only $24.0\%$ of the parent dataset).
3. **Duplicate and Redundant Prose (Medium)**: The definition of the "regulated baryon cycle" was repeated almost verbatim in the Overview, Discovery, and Current Research sections.
4. **Jargonic and Undefined Terms (Medium)**: The BPT diagram (Baldwin-Phillips-Terlevich) and the 4000 Å break index ($\mathrm{D}_n(4000)$) were referenced without explaining their physical basis as observables.
5. **Missing Research-Topic Decision Criteria (Medium)**: The research proposals lacked quantitative statistical thresholds (e.g., AIC, BIC, $\sigma$ levels) to robustly separate physical feedback from selection effects.
6. **Ambiguous/Model-Dependent Observables (Medium)**: Variables like mechanical jet coupling efficiency ($\eta$) and outflow escape speed ($v_{\mathrm{esc}}$) were treated as direct observables rather than model-dependent derived parameters (e.g., Chandra X-ray cavity $4PV$ enthalpy or stellar-mass-scaled NFW potential models).

---

## 2. Completed Safe Local Edits
We have directly updated the following target draft files in the candidate directory:
* [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_07/galaxy-evolution-wiki-candidate.md): Integrated the RP-1 SDSS pilot statistics and selection caveats, streamlined the redundant gas cycle prose, and added a cross-link to `/wiki/dark-matter`.
* [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_07/research-topics-candidate.md): Formally defined the BPT diagram, the $\mathrm{D}_n(4000)$ break, the $4PV$ cavity enthalpy, and updated the decision criteria sections with strict quantitative/statistical tests ($\Delta\mathrm{AIC} \gt 10$, $\Delta\mathrm{BIC} \gt 10$, $\ge 3\sigma$ bounds). We also corrected raw `<` and `>` math delimiters (e.g., using `\lt` and `\gt` or moving them outside the `$` blocks) to prevent KaTeX rendering failures.

---

## 3. Safety Ledger
* **DB/SQL/API/Wiki Publish**: No database queries, SQL executions, or live api calls were made. No pages were published.
* **Service/Deploy/Restart**: No background tasks, servers, or service states were mutated.
* **Git Operations**: No git commits, pushes, merges, rebases, or resets were performed.
* **Credentials/Auth**: No GCP, API keys, OAuth tokens, or credentials files were read or modified.
* **Local Scope Isolation**: All modifications were strictly confined to the candidate directories inside `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z`.

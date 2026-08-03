### GORU_WIKI_MECHANICAL_CYCLE_03

Here is the quality review of the cycle 3 candidate drafts for the Galaxy Evolution wiki page and the research-topic proposals.

---

### Part 1: Ranked Findings

#### 1. Redundant M51 Prose (Wiki Page)
* **Location**: [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_03/galaxy-evolution-wiki-candidate.md#L35) and [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_03/galaxy-evolution-wiki-candidate.md#L49)
* **Finding**: The localized molecular perturbations and positive feedback in M51 are mentioned in two separate claims in the "Current Research" section. Line 35 notes "localized molecular perturbations in M51," while line 49 notes "localized compressive, positive feedback as observed in systems like M51." These can be consolidated or distinguished more clearly to reduce redundancy.

#### 2. Ambiguity in Cavity Power Timescale (Research Proposals - P2)
* **Location**: [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_03/research-topics-candidate.md#L45)
* **Finding**: The mechanical coupling efficiency parameter is defined as $\eta = P_{\mathrm{cav}} / P_{\mathrm{jet}}$, and $P_{\mathrm{cav}}$ is linked to cavity enthalpy $4PV$. However, enthalpy is an energy unit, while $P_{\mathrm{cav}}$ and $P_{\mathrm{jet}}$ are power units. The proposal needs to explicitly define the timescale (e.g., sound-crossing time or buoyancy time $t_{\mathrm{age}}$) used to convert enthalpy to cavity power $P_{\mathrm{cav}} = 4PV / t_{\mathrm{age}}$ to make the observable physically precise.

#### 3. Missing Mass-Loading Estimation Observables (Research Proposals - P1)
* **Location**: [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_03/research-topics-candidate.md#L31)
* **Finding**: Mass-loading ($\eta = \dot{M}_{\mathrm{out}} / \mathrm{SFR}$) is listed as a primary observable, but the conversion from spatial extents and electron densities or CO luminosities to mass-outflow rate $\dot{M}_{\mathrm{out}}$ relies on model assumptions (e.g., thin-shell models or gas geometry). Specifying these underlying conversion steps keeps the observables grounded.

#### 4. Verification of Math Contract Compliance
* **Location**: Both candidate files.
* **Finding**: Compliance is excellent. All comparison operators inside math use KaTeX-native equivalents (e.g., `\gt`, `\lt`, `\ge`). No TeX sequences are used outside math, and no HTML elements or legacy spans remain.

---

### Part 2: Safe Local Edit Suggestions

#### Suggestion 1: Consolidate M51 references in the wiki
In [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_03/galaxy-evolution-wiki-candidate.md#L49), refine the positive feedback sentence to avoid repeating the M51 example directly:
```diff
-Instead of host-wide quenching, some feedback merely regulates ISM turbulence without depleting the reservoir, or even triggers localized compressive, positive feedback as observed in systems like M51. <!--cite:28060-->
+Instead of host-wide quenching, some feedback merely regulates ISM turbulence without depleting the reservoir, or even triggers localized compressive, positive feedback. <!--cite:28060-->
```

#### Suggestion 2: Clarify cavity power timescale in P2
In [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_03/research-topics-candidate.md#L45):
```diff
-**Primary observables.** Cavity enthalpy ($4PV$, where $P$ is pressure and $V$ is volume from Chandra X-ray imaging), shock temperature jumps, disturbed line widths and velocity offsets of molecular (CO) and ionized ([O III]) gas, and jet power ($P_{\mathrm{jet}}$ estimated from radio luminosity and spectral aging). The mechanical coupling efficiency parameter is defined as $\eta = P_{\mathrm{cav}} / P_{\mathrm{jet}}$. A useful secondary observable is whether the same host shows both a hot-gas cavity and cold-gas disturbance, because that helps separate coupling from simple jet presence.
+**Primary observables.** Cavity enthalpy ($4PV$, where $P$ is pressure and $V$ is volume from Chandra X-ray imaging) divided by the buoyancy or sound-crossing timescale $t_{\mathrm{age}}$ to define cavity power $P_{\mathrm{cav}} = 4PV / t_{\mathrm{age}}$, shock temperature jumps, disturbed line widths and velocity offsets of molecular (CO) and ionized ([O III]) gas, and jet power ($P_{\mathrm{jet}}$ estimated from radio luminosity and spectral aging). The mechanical coupling efficiency parameter is defined as $\eta = P_{\mathrm{cav}} / P_{\mathrm{jet}}$. A useful secondary observable is whether the same host shows both a hot-gas cavity and cold-gas disturbance, because that helps separate coupling from simple jet presence.
```

---

### Part 3: Safety Ledger

1. **Advisory Scope**: All findings and suggestions are candidate/advisory adjustments and are constrained to the local sprint candidate files under `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_CONTINUATION_20260709T043339Z/candidates/cycle_03/`.
2. **No DB/SQL/API Writes**: No live database modifications or page publication steps were executed or suggested.
3. **No Infrastructure or Git Mutations**: No actions occurred outside the local workspace candidate directory; no service configurations or Git states were altered.

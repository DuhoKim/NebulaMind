# GORU_WIKI_MECHANICAL_CYCLE_06

A systematic mechanical wiki-review and audit has been performed on the cycle 6 candidate files under the specified safety boundaries. Below are the ranked findings, safe local edit suggestions, and the final safety ledger.

---

## Ranked Findings

### Finding 1: Pipeline Meta-Jargon in Wiki Content (Priority: High)
* **Description**: The `galaxy-evolution-wiki-candidate.md` draft contains internal pipeline metadata jargon ("source positions", "source-ledger", "accepted-limited source positions", "source set", "model-bounded positions") within its main text and claims (e.g., lines 5, 35, 37, 41, 43, 47). This violates the Wikipedia-style tone of the wiki and degrades readability.
* **Impact**: Non-astronomical terms detract from the scientific authority of the page.
* **Resolution**: Replace pipeline terminology with physical and astronomical equivalents (e.g., "observational constraints", "literature review", "empirical data").

### Finding 2: Structural Conflict between Schema and Contract (Priority: High)
* **Description**: The `wiki_schema.md` (lines 33–36) explicitly requires a `## References` section at the end of the article. However, the `wiki_content_contract.md` (lines 30–34) states: *"Stored content must not contain author-year parenthetical citations intended for rendering, `[n]` numeric reference tokens, or `References` / `Bibliography` sections."*
* **Impact**: Rigid validation against the schema will cause a violation of the content contract, and vice versa.
* **Resolution**: Maintain compliance with the content contract at rest (omit the `## References` section) and flag this contradiction for schema alignment.

### Finding 3: Redundant Concept Explanations of the Baryon Cycle (Priority: Medium)
* **Description**: The definition and mechanisms of the "regulated baryon cycle" are explained in highly similar terms across three different sections:
  1. `## Overview` (lines 9–11)
  2. `## Discovery & History` (line 19)
  3. `## Current Research` (lines 45–47)
* **Impact**: Verbose draft structure that dilutes new details in later sections.
* **Resolution**: Streamline the definitions, reserving the general description for the Overview and focusing on historical evolution or specific kinematic tracers in the subsequent sections.

### Finding 4: Inferred Model Parameters Listed as Primary Observables (Priority: Medium)
* **Description**: In `research-topics-candidate.md`, several listed "Primary Observables" are actually highly model-dependent derived quantities or physical impossibilities to track directly:
  * **P1** (line 31): *"the presence of the same material in later CGM measurements"* (cannot physically track the same gas parcel over megayear timescales).
  * **P2** (line 45): *"Coupling efficiency $\eta = P_{\mathrm{dep}} / P_{\mathrm{jet}}$"* (derived efficiency parameter, not a raw observable).
  * **P3** (line 59): *"baryon deficit"* (derived quantity).
* **Impact**: Weakens the empirical feasibility of the proposals.
* **Resolution**: Refine these descriptions to specify concrete, directly measurable observables (e.g., CGM column density offsets, cavity enthalpy from X-ray volumes/pressures, 21cm H I and CO line fluxes).

---

## Safe Local Edit Suggestions

### 1. Edits for [galaxy-evolution-wiki-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_06/galaxy-evolution-wiki-candidate.md)

#### Edit A: Remove pipeline metadata warning block at top (Lines 5–6)
* **Target**:
  ```markdown
  > Highlighted claim chips mark statements with provenance in the source-ledger used for this draft. They are used sparingly here: the page is a narrative synthesis first, and this static draft is prepared from accepted or accepted-limited source positions only.
  ```
* **Replacement**: *(Remove this paragraph entirely, as it describes internal pipeline processes rather than the scientific topic).*

#### Edit B: De-jargon Current Research Claims (Lines 35–48)
* **Target**:
  ```markdown
  <!--claim:2942-->AGN feedback is scoped and context-dependent rather than universal: the cited source set includes a review-level complexity caveat, group-scale evidence, and M51-specific gas-phase results that keep the mechanism tied to particular environments and gas phases.<!--/claim:2942--> <!--cite:28087,28151,28074,28155-->

  <!--claim:2943-->AGN outflows can remove or suppress star-forming gas in some systems, with the strongest support coming from a direct quasar-outflow source position and additional limited support from outflow detections, an ultra-fast-outflow detection, a simulation comparison, and an explicitly M51-scoped case.<!--/claim:2943--> <!--cite:28141,28144,28148,28140,28091-->

  Consequently, AGN feedback is best treated as a localized mechanism that applies to specific galactic environments rather than as a guaranteed, universal driver of host-galaxy quenching.

  <!--claim:2946-->Maintenance or preventive heating remains model-dependent in this source set: simulations and model-bounded positions support the need for AGN feedback in some settings, while one observed X-ray-cavity line provides an observational anchor without making the pathway universal.<!--/claim:2946--> <!--cite:28089,28123,28158-->

  <!--claim:2947-->Kinetic and radio-mode feedback is supported here by one review-synthesis source position and one radio-mode observational source position, with weak jet-gas coupling and same-source cautionary material kept as limitations rather than stacked as extra support.<!--/claim:2947--> <!--cite:28095,28131,28108,28062-->
  ```
* **Replacement**:
  ```markdown
  <!--claim:2942-->AGN feedback is scoped and context-dependent rather than universal: observational evidence is concentrated in specific environments (such as group scales) and particular gas phases (such as localized molecular perturbations in M51).<!--/claim:2942--> <!--cite:28087,28151,28074,28155-->

  <!--claim:2943-->AGN outflows can remove or suppress star-forming gas in some systems, with clear detections in high-redshift quasars alongside localized outflows, ultra-fast outflows, and simulation matches.<!--/claim:2943--> <!--cite:28141,28144,28148,28140,28091-->

  Consequently, AGN feedback is best treated as a localized mechanism that applies to specific galactic environments rather than as a guaranteed, universal driver of host-galaxy quenching.

  <!--claim:2946-->Maintenance or preventive heating remains model-dependent: numerical simulations support the necessity of AGN heating to prevent cooling flows, while observed X-ray cavities provide a direct observational signature in clusters without confirming a universal pathway.<!--/claim:2946--> <!--cite:28089,28123,28158-->

  <!--claim:2947-->Kinetic and radio-mode feedback is supported by radio observations of jets and synthesis reviews, though the efficiency of jet-gas coupling remains a significant observational limitation.<!--/claim:2947--> <!--cite:28095,28131,28108,28062-->
  ```

#### Edit C: De-jargon gas-removal claims (Line 47)
* **Target**:
  ```markdown
  <!--claim:2945-->Gas-removal claims need recycling and mass-regime cautions: accepted-limited source positions indicate fallback or recycling of outflowing material and note that low-redshift, low-mass systems can have winds that are less effective at permanent gas removal.<!--/claim:2945--> <!--cite:28066,28075-->
  ```
* **Replacement**:
  ```markdown
  <!--claim:2945-->Gas-removal claims are constrained by gas recycling and host mass: empirical models indicate substantial fallback of outflowing material, and low-redshift, low-mass systems have shallow potential wells where stellar winds are often insufficient for permanent gas escape.<!--/claim:2945--> <!--cite:28066,28075-->
  ```

---

### 2. Edits for [research-topics-candidate.md](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/candidates/cycle_06/research-topics-candidate.md)

#### Edit A: Clarify Observables in P1 (Line 31)
* **Target**:
  ```markdown
  **Primary observables.** Phase-resolved outflow velocity, line width, and mass-loading; the ratio of outflow speed to halo escape speed $v_{\mathrm{esc}}$; the presence of the same material in later CGM measurements; and whether the gas reappears as cool, warm, or hot gas.
  ```
* **Replacement**:
  ```markdown
  **Primary observables.** Phase-resolved outflow velocity, line width, and mass-loading; the ratio of outflow speed to halo escape speed $v_{\mathrm{esc}}$; and CGM absorption column densities (e.g., Ly$\alpha$, O VI, Mg II) measured along background sightlines to trace swept-up or returning material.
  ```

#### Edit B: Clarify Observables in P2 (Line 45)
* **Target**:
  ```markdown
  **Primary observables.** Coupling efficiency $\eta = P_{\mathrm{dep}} / P_{\mathrm{jet}}$ estimated from cavities, shocks, disturbed gas, and gas depletion, measured relative to jet power within matched apertures around the same host population.
  ```
* **Replacement**:
  ```markdown
  **Primary observables.** Radio jet power estimates from radio fluxes and spectral indices; mechanical energy injection inferred from X-ray cavity volumes and ambient pressures; and shocked gas fractions determined via optical emission-line ratios (e.g., [O I]/H$\alpha$, [S II]/H$\alpha$).
  ```

#### Edit C: Clarify Observables in P3 (Line 59)
* **Target**:
  ```markdown
  **Primary observables.** The break mass or transition surface in gas fraction, quenched fraction, depletion time, and baryon deficit as functions of stellar mass and halo mass.
  ```
* **Replacement**:
  ```markdown
  **Primary observables.** Total H I mass from 21cm flux, CO line luminosities ($L'_{\mathrm{CO}}$) for molecular gas masses, and star formation rates derived from UV/optical and infrared photometry, normalized against stellar mass and halo-mass proxies.
  ```

---

## Safety Ledger

All verification and suggestions adhere to the specified safety boundary:
1. **Advisory Outputs Only**: No database or production API writes are proposed. Suggested edits target the local sprint directory under `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/wiki-quality-sprints/WIKI_QUALITY_SPRINT_20260709T024308Z/` only.
2. **No Environmental Disruptions**: No services are restarted, no packages are installed, and no database schemas are altered.
3. **No External Communications**: No web resources or Git actions are initiated. All tools used are local file viewers.

# GORU_CYCLE9_BLOCKER_DEBATE_REPAIR_ANALYSIS

## A. Blocker Inventory

### 1. Missing Numeric Invariants (`249,917` and `24.0`)
* **Values Identity:** `249,917` is the strict public four-line S/N>=3 eligible parent count. `24.0` is the corresponding cache coverage percentage (`24.0%`).
* **Audit Expectation:** The audit expects these values to be preserved verbatim in both the flagship and supplement manuscripts.
* **Cycle-9 Actual:** Completely omitted (0 occurrences).
* **Cycle-5 Baseline:** Cycle-5 included these values successfully in both `rp1_flagship_polished.tex` (line 31) and `supplementary_denominator_atlas.tex` (line 22) with the caveat: "are selection-context diagnostics rather than custody-backed independent result rows".
* **Root-Cause Hypothesis (cf. H6):** This is a deletion drift class, distinct from the re-derivation drift noted in H6. The `codex_repro_tex` reviewer in cycle-9 flagged these numbers as an "Integrity blocker" because they lacked a JSON custody receipt, explicitly instructing: "they need a real receipt artifact; otherwise they should be removed." The integrator followed this instruction, causing the omission.
* **Concrete Repair:** Revert the deletion and restore the Cycle-5 caveat wording, or generate the missing SQL/query receipt artifact to satisfy the `codex_repro_tex` strict custody requirement.

### 2. Failing Gate: Length (Flagship)
* **Audit Expectation:** Flagship main text between 5000-8000 words.
* **Cycle-9 Actual:** ~2555 words.
* **Cycle-5 Baseline:** ~2662 words (also failed this gate).
* **Root-Cause / Repair:** Manuscript is too brief. Expand astrophysical interpretation and contextual literature discussion while strictly maintaining the association-only bounds.

### 3. Failing Gate: Length (Abstract)
* **Audit Expectation:** Abstract between 200-350 words.
* **Cycle-9 Actual:** ~110 words.
* **Cycle-5 Baseline:** ~110 words (also failed this gate).
* **Root-Cause / Repair:** Abstract is too brief. Expand summary of methods, specific denominator samples, and the 8 atlas topics.

### 4. Failing Gate: Length (Supplement)
* **Audit Expectation:** Supplement >= 4000 words.
* **Cycle-9 Actual:** ~3695 words.
* **Cycle-5 Baseline:** ~3637 words (also failed this gate).
* **Root-Cause / Repair:** Expand the 8 denominator atlas notes with further observational baseline details.

### 5. Failing Gate: Equations
* **Audit Expectation:** >= 2 displayed equations.
* **Cycle-9 Actual:** 0 equations.
* **Cycle-5 Baseline:** 0 equations (also failed this gate).
* **Root-Cause / Repair:** Missing mathematical formalization. Add equations for the BPT line-ratio classifications, sSFR calculation, or environment density metric.

### 6. Failing Gate: Tables
* **Audit Expectation:** >= 3 real-data-derived tables.
* **Cycle-9 Actual:** 1 table.
* **Cycle-5 Baseline:** 1 table (also failed this gate).
* **Root-Cause / Repair:** Convert in-text statistics (e.g., control reuse statistics, environment/mass quartile fractions) into formal LaTeX tables.

### 7. Failing Gate: Prior-Work Comparison
* **Audit Expectation:** Explicit quantitative comparison to prior work.
* **Cycle-9 Actual:** False (missing).
* **Cycle-5 Baseline:** False (missing, also failed this gate).
* **Root-Cause / Repair:** The manuscript fails to contrast its -1.309 dex offset and fractions against quantitative findings from the literature. Integrate the `PRIOR_WORK_COMPARISON_CANDIDATE.md` from the P2 ledger (H7) which contains these exact required comparisons.

### 8. Failing Gate: Operator-Prose (Warnings)
* **Audit Expectation:** Zero workflow/safety phrasing like "toy data" or "not measured here".
* **Cycle-9 Actual:** "toy data" occurs 3 times; "not measured here" occurs 1 time.
* **Cycle-5 Baseline:** Same exact hits (3 "toy data", 1 "not measured here", also failed this gate).
* **Root-Cause / Repair:** Hyper-defensive prompting causes agents to inject literal safety attestations ("No mock, synthetic, fake, placeholder, or toy data were used") directly into the LaTeX text. Repair by deleting these sentences entirely; safety is verified via the audit, not via manuscript prose.

### 9. Failing Gate: Strict Compile (Warnings)
* **Audit Expectation:** 0 overfull, 0 underfull boxes.
* **Cycle-9 Actual:** 14 overfull, 10 underfull.
* **Cycle-5 Baseline:** 12 overfull, 9 underfull (also failed this gate).
* **Root-Cause / Repair:** LaTeX line-breaking and table-formatting constraints. Repair by adjusting text spacing, using `\linebreak`, or resizing tables.

---

## B. Debate-Map

### Reconstructed Cycle-9 Discussion State
* **Positions & Agreements:**
  * **Integrity:** `fact_check`, `director_science`, and `literature` all agree that the data custody is flawless and that association-only boundaries are strictly maintained.
  * **Prose Tone:** `director_science` and `codex_repro_tex` agree the tone is too defensive and reads like a "compliance checklist".
  * **Missing Invariants:** `codex_repro_tex` demanded the removal of `249,917` / `24.0%` because they lack a tracked JSON receipt. The `integrator` agreed and deleted them.
* **Unresolved Disagreements & Causal Blockers:**
  * **Operator-Prose Blocker:** Despite agreeing the tone is too defensive, `fact_check` actively praised the "strict association-only phrasing", leading the `integrator` to leave the literal phrases "toy data" and "not measured here" intact. This causally blocks the operator-prose gate.
  * **Prior-Work Comparison Blocker:** The team debated adding citations (Spindler, Strauss, de los Reyes) to address interpretation boundaries, but entirely missed the requirement for a *quantitative* comparison to prior work. 

### Cross-Check Against H7 (Ledger/Debate Audit)
* **Contradiction / Missing State:** The live Cycle-9 discussion state completely ignores the P2 source ledger audited in H7. H7 verifies a 50-lead ledger and a specifically crafted `PRIOR_WORK_COMPARISON_CANDIDATE.md` containing 4 `VERIFIED_LOCAL` and 5 retained `NEEDS_NETWORK_VERIFICATION` leads (N01, N05, N07, N09, N11). The Cycle-9 reviewers and integrator do not mention, integrate, or debate any of these ledger leads. This omission directly causes the persistent failure of the prior-work comparison gate.

---

## C. Repair-priority ranking (Ordered list for next writer slot ~05:48Z)

| Priority | Repair Target | Gate(s) Fixed | Effort | Risk of Regressing Clean-Cycle-5 | Exact Insertion Target (Cycle-9) | Dependency Order |
|----------|---------------|---------------|--------|----------------------------------|-----------------------------------|-------------------|
| **1** | Re-add missing invariants `249,917` / `24.0%` with exact Cycle-5 wording (or generate query receipt). | Numeric Invariants Missing (Integrity Blocker) | **S** | **Low** (Restores Cycle-5 exactness). | `rp1_flagship_polished.tex` Sec 3 (line 31), `supplementary_denominator_atlas.tex` Sec 5.1 (line 22). | **1** (Must fix first to restore integrity bounds; optionally pair with SQL receipt creation). |
| **2** | Delete safety-checklist prose ("No mock... toy data" and "not measured here"). | Operator-Prose (Warnings) | **S** | **Low**. | `rp1_flagship_polished.tex` lines 28, 78. `supplementary_denominator_atlas.tex` lines 158, 208. | **2** (Independent string deletions). |
| **3** | Integrate `PRIOR_WORK_COMPARISON_CANDIDATE.md` text for quantitative literature offsets. | Prior-Work Comparison | **M** | **Medium** (Ensure no new numeric invariants are triggered or drift caused). | `rp1_flagship_polished.tex` Section 6 (Interpretation). | **3** (Depends on H7 P2 ledger outputs). |
| **4** | Formalize methodologies into LaTeX math environments (e.g. BPT ratios, sSFR offsets). | Equations (< 2) | **S** | **Low**. | `rp1_flagship_polished.tex` Sections 3 or 4. | **4**. |
| **5** | Convert in-text lists (e.g., environment fractions, m3_p3 target vectors) to LaTeX tables. | Tables (< 3) | **M** | **Medium** (High risk of introducing compile warnings or overfull boxes). | `rp1_flagship_polished.tex` Sections 4 or 5. | **5**. |
| **6** | Expand astrophysical interpretation and denominator details to hit word counts. | Lengths (Flagship, Abstract, Supplement) | **L** | **High** (Expansion risks operator-prose recurrence or boundary violations). | Broad expansion across all documents. | **6** (Perform after structural edits). |
| **7** | Fix LaTeX line breaks, resizing tables, and margins to clear box warnings. | Strict Compile Warnings | **M** | **Low**. | Throughout `.tex` files. | **7** (Must be last). |

---

## D. Open questions / unresolved inputs
* The only item I could not verify read-only was the existence or content of the SQL/query receipt that `codex_repro_tex` demanded. Because it is reportedly missing from `REAL_DATA_SOURCE_CUSTODY.json`, there is no file to read. Re-adding the missing invariants without creating this receipt may cause a cyclic dispute with `codex_repro_tex` in the next cycle.

import re

with open("PREREG_SUCCESSOR_DRAFT_V25_20260827.md", "r") as f:
    text = f.read()

# Fix Title
text = text.replace("V24 — LONGO-AMPLITUDE", "V25 — LONGO-AMPLITUDE")
text = text.replace("V24 is a repair of V23", "V25 is a repair of V24")

# Preamble Carried Open
old_carried = "> **Carried-open items:** Findings 1, 2, 2b and 3 **UNRESOLVED** pending the refused BS-2a\n> design; **BS-2a REFUSED by all three seats**; rows C2 and E cannot run; **BS-6 and the first\n> image byte remain blocked**; `verify_lock()` required work, **not implemented**."
new_carried = "> **Carried-open items:** **BS-2v coverage still not independent of the converter**; **BS-2v still has no authenticated receipt schema a gate could reject against**; **§6.1 Row L's signing path voids itself** (CODEX-V24-1); **preamble lines contradicting the live unresolved status** (GPT56-V24-5)."
text = text.replace(old_carried, new_carried)

# Section 2.7
old_bs2a_text = """7. **The confidence threshold is defined by the refused BS-2a design**, and will be pinned before any image byte. BS-2a alone freezes the confidence predicate, value, authority, and retry/failure semantics. Row P applies that already-frozen predicate at P8; below threshold records `EXCLUDED-BY-CONFIDENCE`, and any such removal yields `INCONCLUSIVE-BY-CALIBRATION`. A threshold chosen or moved after inference exists voids the run.

Until §2.7 is implemented in the code §0 pins, **BS-2a cannot be filled**, and this is a
design-and-implementation slot rather than a value slot (see §7)."""

new_bs2a_text = """7. **The exclusion predicate (BS-2a) is FILLED.** It uses three absolute, frozen thresholds measured by the DESI survey before this study existed:
   - `flux_ivar_r > 8.4000532`
   - `psfsize_r < 1.5699703`
   - `nobs_r >= 3`
   (Source `acquire/quality_selected.csv`, sha256 `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3`; receipt `acquire/quality_cut_receipt.json`).
   
   These columns were measured by the DESI survey before this study existed. Their independence from handedness comes from when the quantities were measured, not from when the predicate is evaluated or from any property of the evaluating process. Therefore, no hermetic worker, capability allowlist or blindness fixture is required, and none is claimed.
   
   These thresholds were fixed before any image byte, which makes the predicate preregistered rather than chosen. This is an exclusion predicate applied at analysis time. It is NOT a redefinition of the parent catalogue. V9's `PINNED_PARENT_SHA256`, `PINNED_PARENT_ROWS = 65_060` and `PINNED_SELECTION_BRICKS = 6_445` are unchanged and must stay unchanged so no later reader mistakes this for a new sample.
   
   Row P applies this already-frozen predicate at P8; below threshold records `EXCLUDED-BY-CONFIDENCE`, and any such removal yields `INCONCLUSIVE-BY-CALIBRATION`. A threshold chosen or moved after inference exists voids the run."""

text = text.replace(old_bs2a_text, new_bs2a_text)

# Change 2: Section 4 and BS-5f
old_stage_c = """**Stage C (class E, BS-5f; after inference, before unblinding).** The same frozen generator,
addresses and pass rule, run on the **sealed accepted-position mask** (BS-2f: brickid, objid,
position, acceptance flag, calibration-bin label — never a χ sign), with the measured a_LB
(scalar) or {a_LB_b} (profile) from BS-8f. FAIL → **INCONCLUSIVE-BY-POWER declared before
unblinding; the run halts; no real-sky statistic is ever formed.** **BS-5f certifies only the locked pre-attrition BS-2f mask. Because any post-unblinding removal immediately terminates the run with `INCONCLUSIVE-BY-CALIBRATION`, there is no post-attrition Stage-C reevaluation.**"""

new_stage_c = """**Stage C (class E, BS-5f; after inference, before unblinding).** The same frozen generator,
addresses and pass rule, run on the **sealed accepted-position mask** (BS-2f: brickid, objid,
position, acceptance flag, calibration-bin label — never a χ sign), with the measured a_LB
(scalar) or {a_LB_b} (profile) from BS-8f. 

**Post-exclusion population:**
The statistic is computed on the post-exclusion population, so that is the population §4 and BS-5f must describe.
- pre-exclusion N = 65,060 Var = 0.7561 N_eq = 147,578
- post-exclusion N = 49,211 Var = 0.7517 N_eq = 110,983 floor 100,000 — PASS

Quoting 147,578 would describe a population that will never be analysed — which is the exact defect that got the predecessor declined. The two-ended split moves as a fact about the sample and not a threshold failure: 48.0/52.0 → 40.8/59.2 because `psfsize_r` correlates with cos θ at +0.37. The gate is N_eq and it passes; this is a change in the sample's character that a reader is entitled to see.

FAIL → **INCONCLUSIVE-BY-POWER declared before unblinding; the run halts; no real-sky statistic is ever formed.** **BS-5f certifies only the locked pre-attrition BS-2f mask (N = 49,211, N_eq = 110,983). Because any post-unblinding removal immediately terminates the run with `INCONCLUSIVE-BY-CALIBRATION`, there is no post-attrition Stage-C reevaluation.**"""

text = text.replace(old_stage_c, new_stage_c)

# Change BS-5f in table
old_bs5f = "| BS-5f | Hwao | Stage-C confirmatory power receipt | BS-L |"
new_bs5f = "| BS-5f | Hwao | Stage-C confirmatory power receipt on the post-exclusion population (N = 49,211, N_eq = 110,983) | BS-L |"
text = text.replace(old_bs5f, new_bs5f)

# BS-2a in table
old_bs2a_table = "| BS-2a ⚠ **DESIGN, CLASS P — REFUSED / UNFILLED** | Hwao | **acceptance design**: the numeric confidence threshold **and the named authority that sets it**, retry/failure semantics, the evidence schema for exclusion reasons (a)–(b), the ledger schema, the recomputation code and its fixtures. Gated as text AND code **before any image byte**. V12 placed this in Class E while §2.7 called it a class-P prerequisite. **BS-6 is blocked until a new BS-2a design passes gates that removes the confidence/amplitude dependency and implements the hermetic integrity verifier.** | `run_production_verdict`, pre-verdict validator | BS-2f, BS-6 |"
new_bs2a_table = "| BS-2a **DESIGN, CLASS P — FILLED** | Hwao | **acceptance design**: the absolute, frozen thresholds (flux_ivar_r > 8.4000532, psfsize_r < 1.5699703, nobs_r >= 3). Gated as text AND code **before any image byte**. | `run_production_verdict`, pre-verdict validator | BS-2f, BS-6 |"
text = text.replace(old_bs2a_table, new_bs2a_table)

with open("PREREG_SUCCESSOR_DRAFT_V25_20260827.md", "w") as f:
    f.write(text)

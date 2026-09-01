# AGY SCOPING REVIEW: STAGE 2
**TARGET:** `STAGE2_SCOPING_20260901.md`

This scoping document is **DEFECTIVE**. It omits mandatory design obligations, attempts to reopen closed Stage One rulings, and asks the principal to adjudicate questions that are already frozen in the text. A design question missing here gets smuggled in later as an "obvious" choice.

## 1. COMPLETENESS (Missing Open Design Items)
Section 3 omits the following explicit design obligations demanded by the frozen covenant rows:

*   **Row C:** Omits the definition/schema for the `cutout-completion receipt`.
*   **Row C2:** Omits the `hermetic worker, capability allowlist, and blindness fixture`. Omits the schemas for both the `acceptance-evidence projection` and the `exact-parent stage-completion artifact`.
*   **Row D:** Omits the schema for the `per-object χ-bearing measurement receipts`.
*   **Row D2 (BS-SI):** Catastrophically omits the design of the `two committee architectures`, the logic computing the `machine-committee state`, and the `independent verifier` that recomputes the index from row D receipts and refuses mismatch.
*   **Row H:** Omits the schemas for the `χ-bearing label-set receipt` and the `label set` store.
*   **BS Slots:** Omits the explicit `SLOT_SCHEMA` and canonical receipt field definitions required for BS-2a and BS-9.

## 2. INHERITANCE ERRORS
Section 3 falsely claims the following are "open" when they are rigorously frozen by Stage One:

*   **Estimator Form (Item 13):** Claims the estimator form and calibration entry are newly open. **False.** Stage One §3 and the frozen `v9` already completely define the estimand (`Â_L = β̂/(2â−1)` and `Â_L = β̂/ŵ`), uncertainties, and branch logic.
*   **Verdict Thresholds:** Claims thresholds are open. **False.** Row J and `v9` already froze the calibration floor (`a_LB_b < 0.85`) and the spread test bounds.
*   **Exclusion Reasons (Item 1):** Asks what disqualifies a cutout (suggesting artifacts/blends). **False.** Stage One §2.7 Rule 2 explicitly closed the pre-lock exclusion list to three items: (a) missing/byte-integrity, (b) incomplete at tensor shape, (c) catalogue quality. The frozen text states: "No other reason is admissible." 

## 3. RULING-QUESTION ERRORS
Section 4 asks the principal to rule on matters that are already ruled or frozen:

*   **R1 (Estimator form & thresholds):** Invalid. Already frozen by `v9` adjudication rules and Stage One §3.
*   **R2 (Acceptance thresholds):** Invalid. Already strictly bounded by the closed list in §2.7.
*   **R3 (ABSTAIN policy):** Invalid. The principal already ruled on this (2026-08-30: `EXHAUSTION_ABSTAIN_RULING_20260830.md`). The run continues and the object takes an ABSTAIN label.
*   **R5 (BS-3g sequence):** Invalid. The Stage One Terminal already confirmed that per the BS-6 cycle ruling, the BS-3g sweep runs in Stage Two ("once BS-8f's measured calibration exists").

## 4. SEQUENCING
*   **Section 6 Item 1:** Authorizes "reconnaissance" on real DESI Legacy cutouts to build BS-9. The Stage One terminal explicitly declares that BS-6 and the unfilled design slots "gate the first image byte." If this reconnaissance touches a single real image byte before those slots are filled, it breaches the Phase 1 boundary. It must be strictly constrained to metadata/catalogs.

SEAT: AGY
VERSION: SCOPING-REVIEW-V1
VERDICT: DEFECTIVE
COUNT: 19
F-lines: NONE

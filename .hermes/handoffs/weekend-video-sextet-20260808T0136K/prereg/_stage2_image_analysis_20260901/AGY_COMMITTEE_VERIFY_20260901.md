# AGY Verify: Committee Options Audit

This audit evaluates the draft `CODEX_COMMITTEE_OPTIONS_20260901.md` against the required frozen constraints and instructions.

## 1. ALREADY-FROZEN OFFERED AS CHOICE
- **Headcount:** The frozen text explicitly mandates a size of 1: *"one human checker (Duho)"*. Despite correctly quoting this constraint, the draft offers **C3 (Three-person independent committee)** and **C4 (Five-person independent committee)** as choices. Offering multi-person committees silently re-opens a formally settled size constraint. (While C2 changes the identity to resolve a legitimate role conflict, expanding the headcount to 3 or 5 is an unauthorized reopening).
- **Mandatory Label Stream:** The draft treats the 850-presentation stream as an optional add-on (*"If the inherited complete 850-presentation HC-1H stream is retained"*). The quoted HC-1H rule explicitly freezes this composition (*"850 blinded labels — 500 real, 200 blind synthetic ground-truth injections, 150 mirrored re-presentations"*). These 350 controls are mandatory, not a conditional option.

## 2. FROZEN CONSTRAINTS MISSED
- **Key Custody:** The kickoff instructions explicitly require checking for "key custody", and the draft quotes that HC-1H includes *"sealed keys"*. However, the draft completely omits any mention of key custody for the separate hand-check committee in its composition options (C1-C4). It fails to specify who holds the keys for the human committee's sealed store (Row H) if an independent checker is used.

## 3. WORKLOAD ARITHMETIC
- The raw math based on `R_max = 2` is correct (`500 * 2 = 1,000` and `850 * 2 = 1,700`). However, presenting the baseline workload as merely 500 real decisions misleads the ratification, since the 350 control and synthetic presentations are mandatory under HC-1H. The true base workload per member is 850 decisions and 1,700 render commits.

## 4. BLINDING INTEGRITY
- **R4 (Companion toggle):** The draft offers the display of maskbits and inverse variance. The drafter explicitly acknowledges that these add *"survey-specific identity/quality cues"* and *"expand the χ-bearing rendering surface."* Showing these layers risks leaking the object's pixel-level quality and precise survey position/identity, violating the strict blinding requirements of HC-1H. It should not be offered as an option. 
- *Note:* Parity discipline is correctly preserved across R1, R2, and R3.

## 5. CHECKER INSTRUCTIONS
- The drafted instructions (I1) are sound. They do not prime the checker toward either handedness, accurately reflect the ABSTAIN policy for exhausted replays (enforcing `R_max=2`), and maintain the "suspected identifiable" escape hatch.

## 6. COMPLETENESS
- The draft correctly avoids designing the machine committee, adhering to simply naming its obligations (Section 4).
- The draft successfully surfaces the critical collision between the frozen "Duho" identity and Row G's "member holding any other role" separation rule.
- However, the omission of key custody arrangements for the human committee leaves the principal without a necessary decision point.

SEAT: AGY
VERSION: COMMITTEE-VERIFY-V1
VERDICT: DEFECTIVE
COUNT: 4
F-lines: 35, 55, 62, 94

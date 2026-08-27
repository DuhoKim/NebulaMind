import re

with open("SECTION6_DRAFT_AGY_R10.md", "r") as f:
    text = f.read()

# 1. Update Status line
old_status = "Status: DRAFT FOR REFEREE. Written under `BRIEF_DRAFT_SECTION6_R10.md`. Normatively, Row P's void column was corrected, an ordered adequacy decision tree was frozen in Row P (making any attrition emit `INCONCLUSIVE-BY-CALIBRATION` with no Stage-C rerun), and Clause 8 was rewritten to terminate on unresolved retrospective custody."
new_status = "Status: DRAFT FOR REFEREE. Written under `BRIEF_DRAFT_SECTION6_R10B.md`. Normatively, Row P's void column was corrected, an ordered adequacy decision tree was frozen in Row P (making any attrition emit `INCONCLUSIVE-BY-CALIBRATION` with no Stage-C rerun), Clause 8 was rewritten to terminate on unresolved retrospective custody, and the Stage C power inapplicability branch was deleted, replacing it with a strict `VOID` for any deviation from the 1,000-trial protocol."
text = text.replace(old_status, new_status)
if old_status not in text:
    print("Warning: Status not replaced")

# 2. Update Row P
old_row_p = "Third, Stage C power: if the locked Stage C yields fewer than 962 passing trials out of 1,000 (`../ref/successor_ref_v9.py` lines 77–78), it emits `INCONCLUSIVE-BY-POWER`. These consequences are fixed before any real χ is read, citing V15 lines 570–573 which void any post-first-real-χ change to a decision threshold. | P8, after unblinding | the unblinding receipt and a verified BS-L | the **post-unblinding adequacy receipt**, then BS-7f, then BS-V | any execution before unblinding; any verdict produced outside this symbol; **silent inner-join loss; discretionary retry** |"
new_row_p = "Third, Stage C power: if the locked Stage C yields fewer than 962 passing trials out of 1,000 (`../ref/successor_ref_v9.py` lines 77–78), it emits `INCONCLUSIVE-BY-POWER`. Any deviation from the pinned 1,000-trial protocol or the frozen Stage-C implementation terminates `VOID`. These consequences are fixed before any real χ is read, citing V15 lines 570–573 which void any post-first-real-χ change to a decision threshold. | P8, after unblinding | the unblinding receipt and a verified BS-L | the **post-unblinding adequacy receipt**, then BS-7f, then BS-V | any execution before unblinding; any verdict produced outside this symbol; **silent inner-join loss; discretionary retry; any deviation from the pinned 1,000-trial protocol or the frozen Stage-C implementation** |"
text = text.replace(old_row_p, new_row_p)
if old_row_p not in text:
    print("Warning: Row P not replaced")

# 3. Update Part 2, Item 4
old_p2 = "Third, Stage C power: yielding fewer than 962/1,000 passing trials emits `INCONCLUSIVE-BY-POWER`. "
new_p2 = "Third, Stage C power: yielding fewer than 962/1,000 passing trials emits `INCONCLUSIVE-BY-POWER`. Any deviation from the pinned 1,000-trial protocol or the frozen Stage-C implementation terminates `VOID`. "
# It appears like this in Part 2, item 4: "...Third, Stage C power: yielding fewer than 962/1,000 passing trials emits `INCONCLUSIVE-BY-POWER`."
old_p2_full = "Third, Stage C power: yielding fewer than 962/1,000 passing trials emits `INCONCLUSIVE-BY-POWER`."
new_p2_full = "Third, Stage C power: yielding fewer than 962/1,000 passing trials emits `INCONCLUSIVE-BY-POWER`. Any deviation from the pinned 1,000-trial protocol or the frozen Stage-C implementation terminates `VOID`."
text = text.replace(old_p2_full, new_p2_full)
if old_p2_full not in text:
    print("Warning: Part 2 not replaced")


# 4. Update Part 3, C2
old_p3 = "Alternative: Invent decision thresholds for the missing gaps (like post-attrition Stage C power or calibration applicability). We chose to cite the frozen record and assign an ordered tree of fail-closed terminal consequences (`INCONCLUSIVE-BY-CALIBRATION` and `INCONCLUSIVE-BY-POWER`) where the frozen criteria cannot be applied, because V15 lines 570–573 void any post-first-real-χ change to a decision threshold, and inventing numbers renames a finding."
new_p3 = "Alternative: Maintain an `INCONCLUSIVE-BY-POWER` branch for cases where the power criterion is inapplicable (e.g., if the trial count changes). We chose to delete the inapplicability branch entirely and apply the pinned `< 962` rule alone, because lines 1275–1277 of the frozen code only admit a trial count exactly equal to `N_TRIALS = 1000`. No lawful state exists where the count differs without a protocol breach. Any deviation from the pinned 1,000-trial protocol or the frozen Stage-C implementation is a departure from the frozen protocol, and V15 lines 570–573 make any post-first-real-χ deviation from a binding rule `VOID`, not inconclusive. Emitting a softer terminal state for a protocol breach would be the document excusing its own violation. For calibration, we cite the frozen record and assign `INCONCLUSIVE-BY-CALIBRATION` because inventing numeric thresholds renames a finding."
text = text.replace(old_p3, new_p3)
if old_p3 not in text:
    print("Warning: Part 3 not replaced")

# 5. Update Part 5, Item 8 and add Item 16
old_p5_8 = "8. **R9 Defect 1 — The stated post-attrition power \"gap\" has no terminal consequence.** REPAIR. Row P now deterministically emits `INCONCLUSIVE-BY-POWER` if the exact frozen 962/1,000 criterion cannot be applied. The text explicitly cites V15 lines 570–573 to explain that this consequence must be fixed before any real χ is read."
new_p5_8 = "8. **R9 Defect 1 — The stated post-attrition power \"gap\" has no terminal consequence.** REPAIR. Row P deterministically applies the pinned `< 962` rule for power, and any deviation terminates `VOID` (corrected in R10B)."
text = text.replace(old_p5_8, new_p5_8)
if old_p5_8 not in text:
    print("Warning: Part 5 item 8 not replaced")

item_16 = "16. **R10B Defect 1 — The inapplicability branch downgrades a void to inconclusive.** REPAIR. Deleted the power-inapplicability branch entirely. Stated in Row P and Part 2 item 4 that any deviation from the pinned 1,000-trial protocol or the frozen Stage-C implementation terminates `VOID`, applying the pinned `< 962` rule alone. Detailed in Part 3 that the frozen code (lines 1275-1277) admits no lawful state where the count differs without a breach.\n"

text = text + item_16

with open("SECTION6_DRAFT_AGY_R10B.md", "w") as f:
    f.write(text)


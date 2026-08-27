import sys

with open("PREREG_SUCCESSOR_DRAFT_V15_20260827.md", "r") as f:
    v15_lines = f.readlines()

with open("gates/SECTION6_DRAFT_AGY_R15.md", "r") as f:
    r15_lines = f.readlines()

# Extract Part 1 of R15
start_idx = -1
end_idx = -1
for i, line in enumerate(r15_lines):
    if line.startswith("## §6 Conduct"):
        start_idx = i
    if line.startswith("---") and start_idx != -1 and end_idx == -1:
        end_idx = i

if end_idx == -1:
    end_idx = len(r15_lines)

part1_lines = r15_lines[start_idx:end_idx]

# Remove trailing empty lines from part1_lines
while part1_lines and part1_lines[-1].strip() == "":
    part1_lines.pop()

fold_record = """
### The fold record

**a. What was folded.** `SECTION6_DRAFT_AGY_R15.md`, sha256
`d2c388a451d076f880c879e888ee7901331adc62142245a285b8ff932d67f01a`, folded 2026-08-27.

**b. Under what authority, and against what referee state.** Folded **on the principal's instruction,
before R15 referee verdicts existed.** R15's referee round was dispatched in
parallel with this fold and had not returned when the fold was performed.

**c. What the referees had established at the moment of folding.**
- GPT56 returned **CLEAR** on R12 and again on R13, with no blocking finding.
- Both seats confirmed R14 **closes** the R13 asserted-versus-executable defect at document-contract
  level, by taking route (b): BS-5f's Stage-C schema unchanged, pinned `verify_lock()` required to
  resolve the BS-L-bound BS-8f bytes and independently recompute `all(a_LB_b >= 0.85)`. GPT56 ruled
  route (a) **not better**.
- **Clause 10 was audited in both directions — forward termination and reverse reachability — by
  GPT56 on R12 and R13, and CODEX's independent clause-10 audit on R13 concurred** that the partition
  is single-valued and correctly seated at P5, after BS-8f exists and before Stage C, BS-5f, BS-L and
  unblinding. This is the strongest evidence §6 carries.
- R15 changes **Part 2 only**; a mechanical diff confirms Part 1 is byte-identical to the R14 body
  both seats credited.

**d. The exception this fold carries — OPEN unless R15's verdicts close it.** Both R14 seats blocked
on one thing and only one: **Part 2 asserts it lists every conforming edit outside §6, and did not.**
**Part 2 is the fold instruction** — an incomplete list means §6 lands correct while the surrounding
document silently does not receive changes it needs: the section right, the draft around it wrong.
List each of the five named seams and mark it **OPEN** unless R15 demonstrably closes it:
1. **§7 count and DESIGN inventory** — V15 lines 595–600 said "One of twelve class-P slots is filled"
   and listed BS-2f, BS-5p, BS-8p, BS-9, against fourteen parsed class-P rows and BS-2f being
   value-only per V15 lines 341–342 and 624 *(CODEX)*.
2. **Canonical receipt and schema seams** behind Part 1's invocation of the pinned `SLOT_SCHEMA`
   *(CODEX)*.
3. **§5 guard seam** — V15 lines 429–434 requires only a mask-bound BS-5f before the verdict
   calculation *(CODEX)*.
4. **§2.5 producer-checksum narrowing** and the Clause 10 / §6.3 / §10 repair-trace implications
   *(CODEX)*.
5. **Exact pinned `SLOT_SCHEMA` entries and canonical receipt fields for BS-2a, BS-2k and BS-L**,
   confirmed absent from the pinned implementation by programmatic set comparison *(GPT56)*.

**e. Carried open, not closed by this fold.** Findings 1, 2, 2b and 3 remain **UNRESOLVED** pending
the refused BS-2a design. **BS-2a is REFUSED by all three seats.** Rows C2 and E cannot run. **BS-6
and the first image byte remain blocked.** The `verify_lock()` calibration-PASS implementation is
required work and is **not implemented** — naming it was the repair; writing it was out of scope.

**f. Known design consequence, with the principal.** Any single post-unblinding removal emits
`INCONCLUSIVE-BY-CALIBRATION`. No attrition rate exists in the frozen record, so the probability is
unknown; what is established is that one removal suffices.
"""

# Find replacement range in V15
# The brief says replace V15 lines 461-590 (inclusive, 1-indexed)
v15_start = 461 - 1
v15_end = 590

# Let's verify what those lines are just in case, but rely on finding '## §6 Conduct'
v15_start_idx = -1
v15_end_idx = -1
for i, line in enumerate(v15_lines):
    if line.startswith("## §6 Conduct") and v15_start_idx == -1:
        v15_start_idx = i
    if line.startswith("## §7 Binding slots") and v15_start_idx != -1 and v15_end_idx == -1:
        v15_end_idx = i

if v15_start_idx != -1 and v15_end_idx != -1:
    # Just in case, there are empty lines before §7, we might want to preserve one.
    new_v15_lines = v15_lines[:v15_start_idx] + part1_lines + ["\n", fold_record, "\n\n"] + v15_lines[v15_end_idx:]
    with open("PREREG_SUCCESSOR_DRAFT_V16_20260827.md", "w") as f:
        f.writelines(new_v15_lines)
    print("Fold successful.")
else:
    print("Could not find bounds for replacement.")


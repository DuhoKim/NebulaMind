import re

with open('../PREREG_SUCCESSOR_DRAFT_V19_20260827.md', 'r') as f:
    content = f.read()

# Change 1 & 2 & 3 & 4: Section 5 replacements
old_sec5 = """- **Numeric verdicts (produced by the numeric decision helper):** **REPRODUCED-LONGO** (p < **0.001** AND Longo's sign AND |Â_L − 0.0408| ≤ 3·σ_comb AND Â_L ≥ the evaluated floor), **REJECTED-AT-LONGO-AMPLITUDE** (p > **0.05** AND (|Â_L| + 3·σ_ours(â)) < **0.0408**), **INCONCLUSIVE** (any other numeric outcome).
- **Pre-statistic inconclusive halts:** **INCONCLUSIVE-BY-POWER** (produced by Row J), **INCONCLUSIVE-BY-CALIBRATION** (produced by Row J pre-unblinding, pre-verdict validator post-unblinding removal, or calibration-input non-finite/degenerate failures), and **INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT** (produced by Row I pre-BS-8f abort).
- **Accounting refusals (produced by Row P or the pre-verdict validator):** **INCONCLUSIVE-BY-MISSING-RECORD**, **INCONCLUSIVE-BY-DUPLICATE**, **INCONCLUSIVE-BY-ORPHAN**, **INCONCLUSIVE-BY-MALFORMED** (from Row P).
- **VOID:** triggered by forbidden acts, protocol/digest deviation, or permutation/statistic/protocol non-finite/degenerate failures (handling permutation/statistic non-finite failures is unresolved required work, as the pinned code currently raises uncategorized exceptions instead of emitting this category).

`run_production_verdict()`'s emitter claim is narrowed to the outcomes it can actually return: numeric verdicts, post-unblinding accounting refusals, post-unblinding calibration halts, and VOID."""

new_sec5 = """- **Numeric verdicts (produced by the numeric decision helper):** **REPRODUCED-LONGO** (p < **0.001** AND Longo's sign AND |Â_L − 0.0408| ≤ 3·σ_comb AND Â_L ≥ the evaluated floor), **REJECTED-AT-LONGO-AMPLITUDE** (p > **0.05** AND (|Â_L| + 3·σ_ours(â)) < **0.0408**), **INCONCLUSIVE** (any other numeric outcome).
- **Pre-statistic inconclusive halts:** **INCONCLUSIVE-BY-POWER** (produced by Row J, and the production runner's `N_eq` and Stage-C power guards), **INCONCLUSIVE-BY-CALIBRATION** (produced by Row J pre-unblinding, pre-verdict validator post-unblinding removal, or aggregate non-finite/degenerate failures excluding Row-I's missing allocated outputs — validated by `validate_calibration_aggregates` before the < 0.85 comparison, emitting the authenticated aggregate outcome), and **INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT** (produced by Row I pre-BS-8f abort).
- **Accounting refusals (produced by Row P or the pre-verdict validator):** **INCONCLUSIVE-BY-MISSING-RECORD**, **INCONCLUSIVE-BY-DUPLICATE**, **INCONCLUSIVE-BY-ORPHAN**, **INCONCLUSIVE-BY-MALFORMED** (from Row P).
- **VOID:** triggered by forbidden acts, protocol/digest deviation, or permutation/statistic/protocol non-finite/degenerate failures. **This category is not yet executable.**

`run_production_verdict()` returns exactly: the numeric outcomes and its two `INCONCLUSIVE-BY-POWER` branches (Stage-C failure and `N_eq` floor). **Unresolved required implementation:** accounting, post-unblinding calibration return, Row-I emission, the Row-J calibration guard, per-attempt emission, and `VOID` conversion."""

if old_sec5 in content:
    content = content.replace(old_sec5, new_sec5)
else:
    print("Error: Could not find old_sec5")

# Change 5: Trace
old_trace = """| §7 count | Repaired the Class P and Class E counts in §7 to match the table. |"""
new_trace = """| §7 count | Repaired the Class E count in §7 from 7 to 8; the already-correct Class P count remained 14. |"""
if old_trace in content:
    content = content.replace(old_trace, new_trace)
else:
    print("Error: Could not find old_trace")

# Change header
content = content.replace(
    "# PREREGISTRATION DRAFT V19", 
    "# PREREGISTRATION DRAFT V20"
)
content = content.replace(
    "> **V19 is a repair of V18.** It repairs `PREREG_SUCCESSOR_DRAFT_V18_20260827.md`, sha256\n> `ce144dc23ba8605df1a3b7590464fc3de09c313a597168f91c80d4b29ab302f4` — independently verified.",
    "> **V20 is a repair of V19.** It repairs `PREREG_SUCCESSOR_DRAFT_V19_20260827.md`, sha256\n> `b7deb106eb81b3e13376e7049263b355ba90982656f7de30964c0d3bfda5e63b` — independently verified."
)

# Change 6: V19 -> V20
v19_v20_trace = """**V19 → V20.** Applied the V19 review findings:
| finding | change |
|---|---|
| A. Narrowed runner claim | Replaced the capabilities list with an exact present-tense inventory of what `run_production_verdict()` really returns, marking the rest as unresolved required implementation. |
| B. Power producer not exhaustive | Listed all producers per category in the lifecycle registry, explicitly adding the production runner's `N_eq` and Stage-C power guards. |
| C. Named producers are promises | Same as finding A's resolution. |
| D. `VOID` lacks producer | Stated explicitly that the `VOID` category is not yet executable. |
| E. Non-finite split | Defined the calibration-input non-finite/degenerate failures to exclude the Row-I case, named `validate_calibration_aggregates` as the producer, and added its implementation and fixture to §11. |
| Trace repair | Corrected the V16→V17 trace row for the §7 count. |

**Future revisions:**"""

content = content.replace("**Future revisions:**", v19_v20_trace)

# Change 7: section 11
sec11_addition = """- **Aggregate validation:** Implement `validate_calibration_aggregates` to validate calibration aggregates as finite and non-degenerate (excluding the Row-I missing-output case) before the `< 0.85` comparison, and emit the authenticated outcome. Add its fixture."""
content = content + "\n" + sec11_addition + "\n"


with open('../PREREG_SUCCESSOR_DRAFT_V20_20260827.md', 'w') as f:
    f.write(content)

print("Done")

import re
import sys

def run():
    with open('SECTION6_DRAFT_AGY_R14.md', 'r') as f:
        content = f.read()

    # Update header and briefing reference
    content = content.replace('FOURTEENTH PASS (R14)', 'FIFTEENTH PASS (R15)')
    content = content.replace('BRIEF_DRAFT_SECTION6_R14.md', 'BRIEF_DRAFT_SECTION6_R15.md')

    # Find parts
    part2_start = content.find('# PART 2 — CONFORMING EDITS OUTSIDE §6 THAT THIS REPLACEMENT REQUIRES')
    part3_start = content.find('# PART 3 — CHOICES THE FINDINGS DID NOT FORCE, AND THE ALTERNATIVE TO EACH')

    if part2_start == -1 or part3_start == -1:
        print("Could not find part markers.")
        return

    part2_content = """# PART 2 — CONFORMING EDITS OUTSIDE §6 THAT THIS REPLACEMENT REQUIRES

*This complete list of required conforming edits was derived by walking Part 1 (§6) top to bottom, row by row and clause by clause. Implementation is not claimed here: every code item below is required work, marked UNRESOLVED alongside findings 1, 2, 2b and 3, pending the refused BS-2a design.*

1. **BS-2a Refusal (§6.1 Clause 2 & Row C2):** Explicitly mark BS-2a as REFUSED/UNFILLED. State that BS-6 is blocked until a new BS-2a design passes gates that removes the confidence/amplitude dependency and implements the hermetic integrity verifier.
2. **§2.5 Producer Checksum List (§6.1 list iii):** Narrow the "producer checksum list" to apply exclusively to source image transport at BS-6.
3. **§2.7(4) and §4 Stage C exclusions (Row E):** Remove reason (c) (instrument absence/non-finiteness) from the pre-lock structural exclusion predicates, deferring any non-finite instrument outputs to post-unblinding handling. Confidence threshold exclusion is dropped from pre-lock and applied post-unblinding. **Rule: BS-5f certifies only the locked pre-attrition BS-2f mask. Because any post-unblinding removal immediately terminates the run with `INCONCLUSIVE-BY-CALIBRATION`, there is no post-attrition Stage-C re-evaluation.**
4. **§5 Verdict Guard (Clause 3 & Row P):** Conform §5 and the pinned production symbol to require and verify the canonical BS-L artifact and the one-use unblinding receipt that Row P and Clause 3 make mandatory. The guard must also verify the exact final-mask binding and post-unblinding ledger recomputation before forming any statistic. The production runner must refuse before forming any statistic if the adequacy tree emits an `INCONCLUSIVE` result.
5. **Verdict Path (Row P) Post-Unblinding Consequence:** Define the deterministic rule: Row P must execute an exact set-equality join against the pinned attempt-set identity governed by the BS-2a design digest, using `brickid` and `objid` as fixed join keys, and produce the canonical post-unblinding adequacy receipt. Precedence states are explicit: zero records, duplicate records, extra records, or malformed records trigger an unconditional refusal; absent, non-finite, and low-confidence measurements are dropped; all others are accepted-finite. Adequacy decisions follow an ordered tree: First, calibration applicability: any post-unblinding removal immediately emits `INCONCLUSIVE-BY-CALIBRATION` and **no Stage-C rerun is performed**. Second, Row P binds the already-verified pre-unblinding calibration PASS (`a_LB_b >= 0.85`), relying on the locked BS-5f and BS-L verification.
6. **§7 Class-P and Class-E Tables (Rows A, M, N):** Remove BS-L from the class-P table and add BS-2k (class P, DESIGN; blocks BS-6). Add the BS-L row to the class-E table (producer Duho; content per §6.1 clause 3(b)). Keep BS-V verdict only in class-E. Add the unblinding receipt as a named post-unblinding artifact.
7. **§7 Counts and DESIGN Inventory (Row A & §7):** Update the prose count to state "One of fourteen class-P slots is filled" and "7 class-E" to match the parsed table counts. Replace the current DESIGN inventory with a list that strictly includes BS-2a and BS-2k, and strictly excludes BS-2f (which is value-only). Add a lint assertion that the prose count equals the parsed table count and that the DESIGN inventory matches the VALUE/DESIGN classification.
8. **§10 Repair-Trace Edit:** Record this §6 replacement, as required by Clause 10 and V15 §6.3/§10.
9. **Code-side items in the next atomic revision:**
   - **`SLOT_SCHEMA` entries (Row A, Row N):** Add one explicit code-side item requiring exact pinned `SLOT_SCHEMA` entries and canonical receipt fields for **BS-L and BS-2k**. Name the **BS-2a** schema addition as required work deferred with the already-refused BS-2a design. Bind those schema bytes into the implementation/schema digest item. A general `SLOT_SCHEMA` update to capture access-log checkpoints and archive seal-state digests for BS-2f/BS-L. **Do not change BS-5f** (route b stands).
   - **`verify_lock()` enforcement (route b):** Require the pinned `verify_lock()` to resolve the BS-L-bound BS-8f bytes and independently recompute `all(a_LB_b >= 0.85)`. Pin the implementation/schema digest for this route. Add a negative fixture demonstrating that a low-bound BS-8f cannot produce a passing lock.
   - **Row-J calibration guard:** Implement the guard to emit `INCONCLUSIVE-BY-CALIBRATION` and halt pre-unblinding if `a_LB_b < 0.85`.
   - **Row B access mediation:** Implement Row B's hard block on Row D prior to C2's exact-parent stage-completion receipt verification. Implement the enforceable-mediation gate checks.
   - **Row C2 and Integrity:** Implement the hermetic worker profile allowlist and adversarial producer fixtures for C2. Implement `recompute_acceptance_ledger` to compute statuses and reasons from the evidence projections, atomically writing the evidence ledger and realised partition.
   - **Verifiers (Row O, Q):** Implement `verify_unblinding_receipt`, `verify_archive_seal`, and the opening-authorization / replay verifier.

---

"""

    new_content = content[:part2_start] + part2_content + content[part3_start:]

    with open('SECTION6_DRAFT_AGY_R15.md', 'w') as f:
        f.write(new_content)
        
    print("Done generating SECTION6_DRAFT_AGY_R15.md")

if __name__ == '__main__':
    run()

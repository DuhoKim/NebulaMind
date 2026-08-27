# DRAFTING BRIEF — R14. Part 2 claims completeness and omits three edits. Last §6 pass.

Subject: `SECTION6_DRAFT_AGY_R13.md`, sha256
`385228543d178052ed27f62bd8df90c11168628a7120bd9127c707ca54eec1da`.
Read `SECTION6_REVIEW_R13_GPT56.md` and `SECTION6_REVIEW_R13_CODEX.md` first.

**GPT56 cleared R13 with no blocking finding — its second consecutive CLEAR.** Its bidirectional
clause-10 sweep and the value/phase/failure-effect threshold sweep found no orphan, overlap or
executable gap. **CODEX's own clause-10 audit agrees the prose partition is sound**: single-valued,
correctly seated at P5 after BS-8f and before Stage C, BS-5f, BS-L and unblinding, with no
R13-created double outcome.

**Do not touch the partition, the seating, the thresholds, the rows, or the clauses.** This pass
changes Part 2 and one route choice. Nothing else.

## The defect

Part 2 states it lists **every** conforming edit the replacement requires. Its only code-side item
adds Row B and C2 mechanisms and **omits three edits R13 itself created**:

1. the **Row-J calibration guard**,
2. the **BS-5f binding / schema change**,
3. **`verify_lock()` enforcement**.

CODEX establishes why this matters and it is not bookkeeping. The pinned `SLOT_SCHEMA`
(`../ref/successor_ref_v9.py` lines 185–193) defines BS-5f as exactly
`("successes", "n_trials", "passed", "mask_digest")` — no calibration result, no BS-8f digest, no
minimum `a_LB_b`. And **a content search of the pinned implementation finds no `verify_lock()`
definition at all.** So clause 3(c) asserts that `verify_lock()` authenticates a field the closed
schema does not carry, and Part 2 does not list the work that would make it carryable.

A document that says "this is the complete list of required edits" and is missing three of them is
making a false completeness claim. That is the same class this lane has produced repeatedly, and it
is the last thing that should be folded into the preregistration unnoticed.

## The repair

**Choose one route and state it.** CODEX gives two:

- **(a)** extend authenticated BS-5f to bind the exact BS-8f digest plus a canonical calibration-PASS
  field and minimum, with Row J refusing to issue BS-5f when `min(a_LB_b) < 0.85`; or
- **(b)** leave BS-5f's Stage-C schema unchanged and require the pinned `verify_lock()` to resolve the
  BS-L-bound BS-8f bytes and independently recompute `all(a_LB_b >= 0.85)`.

**My reading is (b)**, because it does not reopen a frozen slot schema and it keeps the check with the
verifier rather than trusting a producer-authored field — the same principle that made row C2's
predicate bits independently recomputable. **If you judge (a) better, argue it in Part 3 and take
it.**

Then, in **Part 2's code-side atomic list**, add all three edits explicitly, and add:

- **pin the implementation/schema digest** for whichever route you chose;
- **a negative fixture demonstrating that a low-bound BS-8f cannot produce a passing lock.**

Finally, in **Part 5**, record this as an item and mark the implementation itself **UNRESOLVED**
alongside findings 1, 2, 2b and 3 — it is BS-2a-class code work, not prose. **Naming the required
edit is the repair here; writing the code is not in scope and must not be claimed.**

## Not in scope

Everything else. Do not re-seat any decision, do not add or delete a branch, do not adjust a
threshold. The attrition-intolerance design question stays with the principal.

## Deliverable

`SECTION6_DRAFT_AGY_R14.md` — complete, self-contained, five parts, single write.

Do not modify the preregistration. Do not read `/Users/duhokim/NebulaMindData/`. Nothing is
authorised to fetch. No deadline.

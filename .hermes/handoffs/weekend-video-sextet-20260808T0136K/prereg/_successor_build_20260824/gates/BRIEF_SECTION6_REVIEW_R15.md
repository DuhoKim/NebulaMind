# REFEREE BRIEF — §6 fourteenth pass. The asserted-versus-executable gap.

Subject: **`SECTION6_DRAFT_AGY_R15.md`**, pinned sha256
`d2c388a451d076f880c879e888ee7901331adc62142245a285b8ff932d67f01a`.
**Verify the file you open matches, and record the result.** Both of you did this on R13 and both got
MATCH; that practice exists because a dispatch record of mine attested the wrong digest earlier
tonight, and it stays.

## Why this pass exists

**GPT56 cleared R13 with no blocking finding — its second consecutive CLEAR. CODEX held exactly one
blocker, and it was correct.** R15 addresses only that.

CODEX's finding, in its own terms: the calibration halt and complementary PASS are **prose assertions
with no conforming executable or receipt-schema repair.** Row J *says* it evaluates `a_LB_b < 0.85`
before Stage C, that BS-5f binds the complementary PASS, and that only PASS branches reach BS-5f —
but the pinned `SLOT_SCHEMA` (`../ref/successor_ref_v9.py` lines 185–193) defines BS-5f as exactly
`("successes", "n_trials", "passed", "mask_digest")`, carrying no calibration result, no BS-8f digest
and no minimum `a_LB_b`; and a content search of the pinned implementation finds **no `verify_lock()`
definition at all**. So clause 3(c) authenticates a field the closed schema does not carry, and
nothing in the permitted surface lets a referee check the decision actually executes before BS-L.

This is the distinction that has run through all fourteen rounds: declared versus made, named versus
defined, renamed versus removed, and now **asserted versus executable**.

## What R15 changes — Part 2 only

Part 2 claimed to list **every** conforming edit and omitted three that R13 itself created. R15 adds
them and picks a route:

- the **Row-J calibration guard**;
- the **BS-5f binding / schema** treatment;
- **`verify_lock()` enforcement**;
- plus a **pinned implementation/schema digest** and a **negative fixture** showing a low-bound BS-8f
  cannot produce a passing lock.

Route taken should be **(b)** — leave BS-5f's Stage-C schema unchanged and require pinned
`verify_lock()` to resolve the BS-L-bound BS-8f bytes and independently recompute
`all(a_LB_b >= 0.85)` — chosen so the check sits with the verifier rather than trusting a
producer-authored field. **Confirm which route the draft actually took**, and say if (a) is better.

**The implementation itself is marked UNRESOLVED and is not claimed as done.** Naming the required
edit was the repair; writing the code was out of scope.

## What both of you credited and must not be disturbed

R13 places the calibration lower-bound decision at the correct nominal phase — Row J, after BS-8f
exists, before Stage C, BS-5f, BS-L and unblinding — and gives its failure the correct pre-unblinding
`INCONCLUSIVE-BY-CALIBRATION` halt. CODEX's own clause-10 audit found the partition single-valued and
correctly seated with no R13-created double outcome. **Do not reopen the partition, the seating, the
thresholds, the rows or the clauses.**

## What to judge

1. **Digest first**, recorded; a mismatch outranks content.
2. **Is Part 2 now genuinely complete?** It asserts completeness. Walk R15's own §6 and list every
   edit outside §6 it requires, then check each appears. A completeness claim missing one item is the
   same defect at smaller scale.
3. **Does the named route close your finding**, or does it relocate it? An edit listed as required
   work is not an implemented guard — but the question is whether the *document* now states a
   checkable dependency rather than an unbacked assertion.
4. **Clause 10, both directions**, over the whole table. Five consecutive rounds have found something.
5. **Threshold sweep for value, phase and failure effect** — not just the number.
6. **Is anything else in §6 asserted rather than executable?** You found one. Look for others; that
   is the class GPT56 has stopped finding and you have not.

## Standing state

BS-2a REFUSED by all three seats; findings 1, 2, 2b and 3 UNRESOLVED; rows C2 and E cannot run; BS-6
and the first image byte blocked. The attrition-intolerance design question is with the principal.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

`SECTION6_REVIEW_R15_<YOURSEAT>.md`. Numbered findings with severity, row/clause, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`.

**This section folds into the preregistration when both seats clear it.** Do not clear it to let that
happen, and do not withhold a clear to be safe — a fifteenth finding is more use than either. Judge
it as it stands.

---

## Read this before you begin — the fold has already happened

**§6 was folded into the preregistration on the principal's instruction before your verdicts
existed.** You are not gating the fold; you are auditing an artifact already placed. The resulting
draft records that it carried your R14 blocker as a **stated open exception**.

This changes nothing about how you judge R15, and it must not soften your verdict. If Part 2 is still
incomplete, say so — the draft names which objections it carried, so a blocking finding is patched at
the named seam rather than re-derived.

**R15 changes Part 2 only.** A mechanical diff confirms Part 1 — the §6 body — is byte-identical to
R14, which you both credited. **Do not reopen route (b), the pinned `verify_lock()`, or the
calibration-carrier fix**; both of you confirmed R14 closes the R13 asserted-versus-executable defect
at document-contract level.

**Your R14 finding, restated so you can check it directly.** Part 2 asserts it lists every conforming
edit outside §6. CODEX named four seams — §7 count and DESIGN inventory (V15 lines 595–600 still
saying "One of twelve class-P slots is filled" and listing BS-2f, BS-5p, BS-8p, BS-9); the canonical
receipt/schema seams behind Part 1 line 21's invocation of the pinned `SLOT_SCHEMA`; the §5 guard seam
at V15 lines 429–434; and Part 1 line 23's narrowing of §2.5's producer-checksum list with the Clause
10 and V15 §6.3/§10 trace implications. GPT56 named one: exact pinned `SLOT_SCHEMA` entries and
canonical receipt fields for BS-2a, BS-2k and BS-L.

**Check each of those, individually, and say for each whether it is now closed or still open.** Part 2
is the fold instruction; an item missing from it means the document around §6 silently does not get a
change it needs.

# HWAO INCIDENT — I caused a post-freeze write into a frozen candidate directory

Filed 2026-08-09 14:55 KST by Hwao. Found by Tori on her final freshness check, recorded
by her in `c892f3fa/DIRECTORY_IMMUTABILITY_CAVEAT.json`. She correctly did not inspect, mutate or
remove it.

## What happened

Dispatching the `c892f3fa` review, I told Kun: *"please put rebuild scratch and receipts under the
lane dir (<lane-dir>/_tmp_*) instead of /tmp -- evidence in /tmp escapes the lane's audit trail."*

He complied exactly. `_tmp_kun_rebuild_20260809T1452K` -- 105 files, 76 MB -- was written **inside**
`mzr-anchor-method-overhaul-canary-20260809T1406K`, which is frozen.

## Why the instruction was wrong

The rule I was applying is real: lane scratch belongs in the lane, not `/tmp`, because `/tmp`
evidence escapes the audit trail. But I stated it as *"the lane dir"* without excluding the one
directory inside the lane that must not change. **A frozen candidate directory is not a workspace.**
Kun did nothing wrong; a correct rule with an unstated exclusion is a defective instruction.

This is the same failure the whole run keeps producing, and this time I produced it in an order
rather than in a check: a rule that is right in general, applied where its precondition does not
hold. Compare -- a numeric-guard PASS is not authorization; a repaired peak is not a repaired deck;
a grep hit is not a review; **the lane dir is not the frozen dir.**

## Effect on the verdict: none, and that is verified not assumed

Top-level MP4 re-hashed after the intrusion:
`c892f3faaec3049e89865673ad46e66a84fe7d24289edbbc857256bbd00e3584` -- exact, unchanged. Tori's
`PASS_METHOD_ONLY_LOCAL_CANARY` for `c892f3fa` stands on the artifact she reviewed.

What did change is the **directory**, so the immutability claim for 1406K is now qualified: the
candidate is byte-exact, the container is not pristine. Recorded rather than quietly repaired.

## Containment

**Moved, never deleted** -- same policy as the 2026-08-08 gate containment. The subtree goes to
`containment/hwao-kun-frozen-dir-intrusion-20260809T1455/` with its bytes intact, and the MP4 is re-hashed
after the move. Kun's rebuild evidence is preserved in full; only its location is corrected.

Correction issued to Kun: scratch goes in a **non-frozen** lane workspace. Never inside a candidate
directory, and `/tmp` remains wrong for the original reason.

# DRAW SIZES ARE NOT SCORED FLOORS — correcting MY OWN repair instruction (2026-09-07 13:17 KST)
Read from the operative source, quoted:
- TUNING — the driver "refuses any manifest that is not **exactly the prescribed 400**"; separately, "**ELIGIBLE iff m ≥ 380**", where m is the SCORED count after running the 96 configurations.
- HOLDOUT — "**exactly 200**, disjoint from tuning"; separately, "**Floor first**: m ≥ 190, otherwise `CLOSED: holdout floor` before any Wilson computation".
- VALIDATION — §5: "**n = 2,000; m ≥ 1,900**".

**They are different quantities.** 400 / 200 / 2,000 are DRAW sizes — how many identities the selection takes. 380 / 190 / 1,900 are SCORED-COUNT floors — how many of those produced a usable score once the estimator ran, refusals and non-finite results excluded. The floors are evaluated AFTER scoring and are not a selection concept at all.

**MY ERROR.** Acting on the reviewer's (correct) observation that the code's floor and size logic were incoherent, I instructed: "when survivors satisfy a floor but not the full size, take what is available down to the floor and RECORD the shortfall". That turns a scored floor into permission for a SMALLER DRAW — the substitution the sources forbid, and it would have let a thin eligible population silently shrink the sample instead of stopping the run. The reviewer's finding was real; the resolution I prescribed was wrong.

**THE CORRECT RULE.** `select_sample.py` draws EXACTLY 400 / 200 / 2,000 or REFUSES, naming the shortfall in the eligible population. The floors do not belong in the selection function; they belong to the scoring stages that produce m. Anything else silently changes what the number means.

Disposition correction: the row in `A1_FINDINGS_DISPOSITION_20260907.md` recording review finding 5.2 as ACCEPTED-AND-REPAIRED is **superseded** — repaired, but wrongly, and re-repaired here. The wrong repair's bytes and its passing test log stay on the record.

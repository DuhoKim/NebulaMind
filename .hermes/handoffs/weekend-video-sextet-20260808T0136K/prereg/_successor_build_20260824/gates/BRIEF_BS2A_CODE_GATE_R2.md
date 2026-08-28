# CODE GATE — BS-2a, round 2. Your deletion probes broke the battery; it has been rebuilt.

Subject: **`../ref/bs2a_quality_gate.py`**, sha256 `d7da1568dc294595640b603368135df288ac4bbc0cc54003a1fc906e237e650c`. **Verify and state the comparison.**
Round-1 reports are archived at `gates/_bs2a_round1/`.

## What you found, and what changed

**CODEX ran deletion probes rather than reading**, and that is what found this. It deleted the
parent-digest comparison and the retained-count comparison; `--self-test` reported `7 controls, 0
failures` both times, because the battery asked whether *some* refusal occurred and never whether the
*expected* one did. The `retained count inflated` control was being caught by the unrelated
partition-sum branch — **a surviving guard masking a deleted one.**

Five repairs:

1. **Every control now declares the refusal substring it must produce.** A control that fires for
   another check's reason is reported `refused for the WRONG reason` and fails.
2. **The battery is 7 → 17 controls**, covering schema version, both source digests, join keys,
   parent identity, join totality, each count, the partition sum, both receipt-field directions,
   off-schema evidence, per-row predicate disagreement, non-boolean and non-finite values, and
   duplicate keys.
3. **The schema check no longer breaks on the first bad row** — a late row could carry `chi_net`
   through the schema meant to stop it.
4. **Per-row predicate agreement**, not totals — rows could previously lie in compensating
   directions.
5. **Parent identity and one-to-one closure moved into the verifier**; `evidence_digest()` is
   length-prefixed so a field containing `|` cannot forge the encoding.

## Two of my repairs failed their own standard, and I want them attacked specifically

- **The fixture is now full-size (65,060 rows).** A four-row fixture could not satisfy the production
  parent-identity check, and the tempting fix was to relax that check when running against a fixture.
  **Check that the fixture exercises the production path and not a weakened one.**
- **The partition control initially moved two fields** and so passed on the wrong branch — the exact
  defect it was written to fix. **Check every control is isolated to the single thing it tests.**

## Attack it

1. **Re-run your deletion probes.** Delete any check and confirm the battery names *that* control as
   silent. Deleting the parent-digest check now yields
   `parent digest wrong: ACCEPTED, control is silent` and exit 1 — **verify that yourself, and try
   checks I have not probed.**
2. **Can the verifier still be made to accept a receipt it should reject?** Find a hole the 17
   controls do not cover.
3. **Is any control passing for the wrong reason?** That is what round 1 turned on.
4. **Does the fixture differ from production in any way that matters?**
5. **Does the module claim more than it establishes?** It disclaims statistical independence from
   handedness per your V25 refutation. Any code path or comment implying the stronger claim is a
   finding.
6. **Does anything touch `successor_ref_v9.py`?** It must not.

Run it yourself:

    python3 ref/bs2a_quality_gate.py --self-test      → expect 17 controls, 0 failures
    python3 ref/bs2a_quality_gate.py --acquire acquire → expect 49,211 of 65,060, MATCH

**Do not take those numbers from me.**

## Unchanged

This does **not** fill BS-2a, authorise a fetch, or resolve conditional independence. BS-2a
**UNFILLED**; one of fifteen class-P slots filled; **BS-6 and the first image byte blocked.**

Do not read `/Users/duhokim/NebulaMindData/`. No deadline.

## Verdict

`BS2A_CODE_GATE_<YOURSEAT>.md`. Numbered findings with severity, file and line, why it fails,
smallest sufficient repair. Anything asserted but not executed under `Testimony`. Final line exactly
`**CLEAR**` or `**NOT CLEAR**`. **A refusal you can demonstrate beats a pass you can argue.**

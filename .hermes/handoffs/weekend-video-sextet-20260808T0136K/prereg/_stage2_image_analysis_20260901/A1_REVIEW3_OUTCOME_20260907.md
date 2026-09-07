# A1 FINAL DELTA REVIEW — **VERDICT: DELTA-NOT-SOUND** (2026-09-07 17:22 KST). Two FATALs, both confirmed by me.
Reviewer agy / Gemini, ACCESS PROVEN for `c0459ad1b16cfdec…`; exit artefacts read first: stderr 0 bytes, stdout 2,788 bytes, rc 0 — a completed seat. It authored none of the changes.

## FATAL 3 — READINESS WAS TRUE WHILE AN OBLIGATION WAS OUTSTANDING. **Confirmed.**
`INPUT_MANIFEST_A1_CORE.json` lists exactly TWO obligations, `CORE_CONSUMER_RECONCILIATION` and `MEDIUM_CURRENT_PREPARATION`, both `resolved: true` — while A1's own prose says the runtime representation "remains current preparation work". The manifest and the document contradict each other, and the manifest is what the gate reads. Readiness was therefore TRUE prematurely.
**I looked straight at this and missed it.** I checked that readiness was a GATE rather than a label — it is, at `run_path.py:301` — and stopped there. I never checked that the list the gate reads is COMPLETE.

## FATAL 4 — THE GATE CANNOT SEE A DELETED OBLIGATION. **Confirmed.**
The predicate is `all(p.get("resolved") is True for p in obligations)` — quantified over whatever entries happen to exist. Deleting an unresolved entry makes the gate pass. **This is the same defect class this lane has been finding all day**: a check over a list that never verifies the list is complete — the aggregate gate reading part of a log, controls asserting "some refusal fired", the table verification blind to codes it never enumerated. It found us again in a new costume.
The reviewer also names a TOCTOU gap: extension modules are hashed by `read_pin` and later loaded by `import` with no lock between. Real, and to be stated as a limit rather than pretended away.

## Not defects
MEDIUM producer: implements V15 §6 exactly; label-blindness enforced by construction (`_FIELDS` admits no label key); the 96 configurations run in fixed exhaustive order, so no search choice is smuggled. CORE registers: nothing the run path reads is missing; the runtime pins correctly state their own limits. Counts not overstated; no false completeness claim in A1 or the sheet; nothing previously sound was broken.

## Disposition
A1 is NOT put to Duho. The honest current state is **readiness FALSE** with the runtime-representation obligation recorded as unresolved. Repair dispatched: obligations become a DECLARED SET that the gate verifies for completeness, so a deleted entry FAILS rather than passes; the outstanding obligation is listed; A1 and the manifest are cross-checked against each other by code; the TOCTOU limit is stated. Fail-first evidence required. Then one more delta review of the changed bytes.

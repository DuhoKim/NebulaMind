# Hwao source-boundary verdict — Kun report + Tori progress video

Marker: `HWAO_KUN_TORI_VIDEO_SOURCE_BOUNDARY_COMPLETE_20260722`
Captured from fresh Hwao/Fable lane `%287`.

Overall: **APPROVED WITH FOUR WORDING CORRECTIONS.** Every proposed count and claim matched the seven source artifacts.

## Kun report headline

- Kun's oversight verdict was `HEALTHY_WITH_RISKS`, adopted with one material correction: Contract v1 was already `COMPLETE / PASS` with 16 entries, 45 spans, 45 stance rows, 26 source rows, 26 unique bibcodes, and 0 errors. Rebuilding was rejected; preservation-first was the ruling.
- Kun's latest live check, `KUN_PHASE4_CORRECTED_SCOPE_VERIFIED_20260722`, PASSed the corrected Phase 4 scope: 18 `test*.db` files; 10 caches split into 2 ordinary future-scope and 8 held; safety counters all zero. This is a live Kun-lane attestation, not a phase4 handoff file.

## Completed progress

- Phase 0: 36/36 files, digests, and mtimes matching; Tori and Kun computed identical manifests; G2 approved and discharged.
- Phase 1: 380 entries classified 222/130/18/10; zero moves or deletes.
- Phase 2: `REWORK PIECEMEAL`; whole-branch rebase, blind cherry-pick, and wholesale abandon rejected.
- Phase 3: four dirty-intent patches covering exactly 20/20 modified tracked paths; per-unit fates ratified.
- Surveys G3: three independent fail-closed reviews; two honest FAILs followed by an unconditional PASS across B1–B5 and E1–E5; unit closed with `HWAO_G3_SURVEYS_WRAP_UP_COMPLETE_20260722`; V2 retained frozen and uncommitted.

## Current and held

- G3 re-latched fully held after Surveys closure.
- G4a/G4b/G4c remain held, separate, and never bundled.
- G5 and G7 are closed.
- G6 is held pending proposal.
- Landing Surveys V2 on main is a future G3 packet: not scheduled and not approved.

## Required wording guards

1. Two different `18` sets exist: 18 test database files under G4b and 18 ordinary quarantine candidates under G4a. Label each set explicitly or show only one.
2. Phase 4 is scope ratification only: say `cleanup scope defined`, never `cleanup approved` or `cleanup started`. Current G4b is quarantine preparation, not deletion.
3. Do not use the volatile branch-behind count unless time-stamped. Prefer omitting it.
4. Hwao ruled the Surveys closure on stronger evidence. Credit Tori with custody and receipt verification, not sole authorship.

Closing boundary: preservation, classification, IA/branch decisions, the Surveys review unit, and Phase 4 scope definition are complete; execution gates remain.

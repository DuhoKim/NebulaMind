# Gain Mapping A Re-Verification

Verification results for the BS-3g executable mapping A (v2, post-repair).

I confirm:
- The behavioral clamp control is no longer vacuous (Control 6 tests the physical flip rates).
- `identity_record` now successfully binds `A_LONGO` and the convention commit digest `MAPPING_CONVENTION_COMMIT_20260831.md`.
- Nothing in the module performs worst-case reduction; `MappingA` correctly serves as a one-draw primitive with reduction owned by the runner (as per `MAPPING_ARCHITECTURE_RULING_20260831.md`).

SEAT: AGY
VERSION: MAPA-V2
VERDICT: SOUND
COUNT: 0

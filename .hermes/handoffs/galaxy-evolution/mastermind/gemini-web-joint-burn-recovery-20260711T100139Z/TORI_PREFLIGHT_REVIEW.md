# Tori joint-run preflight review

UTC: 2026-07-11T10:22:30Z
Packet: `gemini-web-joint-burn-recovery-20260711T100139Z`
Verdict: `C1_READY_BUT_PACKET_NOT_ARMED`

## Verified

- The packet manifest parses and all four pinned hashes match: commissioning brief, direction, C1 prompt, and seed ledger.
- The sole C1 prompt SHA-256 is `d40b7cb7c49659c71d973ea71a24d0e6e55157bb011989743280b41c33891cc5` and matches the manifest.
- C1 BEGIN/END sentinels, REQ ID, C1-C8 contract, and completion marker match the manifest.
- The packet has exactly one zero-byte NOT_ARMED marker and zero `JOINT_ARMED_*` markers.
- Tori and Goru each have exactly one role-lock ACK row in `WAVE_LEDGER.md`.
- Goru's schema check passes; expected-marker JSON parses.
- Goru's three reported output byte counts and SHA-256 values match independently computed values.
- `GORU_PREFLIGHT_DONE_20260711T100852Z` exists and is zero bytes.
- A scoped search across all 94 weekend-burn prompt files found zero matches for `calibrat`, `out-of-sample`, `provenance`, or `validation ledger`.
- The prior extension manifest assigned this scope to R15, but R15 is not among the 15 valid captured report bodies; the extension hard-stopped at verification before that run. C1 therefore does not duplicate a valid report.

## Caveat

`goru/TOPIC_DEDUPE.md` correctly inventories 94 parseable weekend prompts, but its broad conclusion that all 94 are `NOT_COVERED` used a shallow heading-word heuristic. Treat those 94 semantic verdicts as advisory only. This does not block C1 because C1's exact scope was independently checked as described above.

## Gate

No Gemini Web interaction is permitted until Duho manually clears Google's unusual-traffic verification and explicitly confirms that clearance in chat. After confirmation, Tori may replace NOT_ARMED with exactly one ARMED marker and run only C1. Goru remains local-only and performs post-capture marker/count/hash validation.

ACCESS_SHA=f3987cbe0d31b7c5eb5a72c7018c624175d60cd8b4c3e374335cb6f19c3d2992

# Independent Referee Report: V24 Candidate

**1. The Three States, Exercised**
- **(1) OFFLINE candidate (Production Defaults)**: `provenance_mode='offline'`. It STILL ACCEPTS counter-cases 1, 2, and A. This is accurately disclosed in §3c of the rule text.
- **(2) STANDALONE v3 helpers**: Successfully exercised and proven to execute as tested.
- **(3) COMPOSED mode (Unadopted)**: `provenance_mode='composed'`. Successfully uses v4 helpers inside `load_identity`. The test `composed_case` accurately reflects that it REFUSES the counter-cases (e.g., `EVENT-EXPIRED-NO-RECEIPT-PATH`, `HISTORY-CONTINUATION`). The origin label {actor: ops-witness, session: OPS} is PROPOSED BY THE LANE and unadopted. The residual trusted step (fabricated first receipt caught only by retained copy) is DISCLOSED. Option B is correctly marked as NOT IMPLEMENTED. Option C remains the sound recommendation.

**2. M1–M6 and A–F: Status and Fail-First Evidence**
- **M1**: REPAIRED. `validate_continuation_v4` strictly requires one server-timed PushEvent per history commit. Multiple commits per push are refused with `HISTORY-PUBLICATION-BATCH`. Probes confirm this.
- **M2**: REPAIRED. `publish_entry` correctly pushes already-committed pending entries instead of re-committing. The collector properly publishes outer refusal/error entries after a crash/restart.
- **M3**: REPAIRED. The residual is restated exactly, clarifying that pre-publication work and absence-based terminal decisions remain unauthenticated without an independently retained decision anchor.
- **M6**: REPAIRED. The text sweep successfully executed all designated changes (§3c, labels, drivers).
- **A–F (from V23)**: DISCLOSED-AS-OPEN for the baseline, with track 2/composed mechanisms accurately capturing their intended fixes (e.g., A is repaired via authenticating the history-open anchor in composed mode). All fail-first evidence was read correctly, distinctly separating `MISSING-INTERFACE` from behavioural failures.

**3. Trusted Steps, Residual, and Pins**
The remaining trusted step (a fabricated first receipt is only caught by OPS's retained copy) and the residual (pre-publication work and absence-based terminal decisions) are both stated exactly and completely in the rule text.
The pin-drift record (`PIN_DRIFT_RECORD_V22_M5_20260906.md`) is truthful and complete. Every V23-pinned file was verified to either be at its original path or correctly restored and hash-matched under `_optionA_dev/_archive_v22_pins/`.

**4. Cost and Failure States**
The cost is precisely one push per collector/builder attempt. The failure states (`PENDING-PUSH`, `DIVERGED`, `RETRY-REMOTE-UNAVAILABLE`) are correct and correctly constrained. No remaining 'one push per freeze' statements exist outside of quotations.

**5. Preserved Items**
All previous items are preserved and re-verified:
- Sample sizes: 400/200/2,000
- Floors: 380/190/1,900
- The 0.70 bar
- Exclusions (failed set, 2,644 dry-run identities, rounds 6440756/6441904/6441924)
- Custody E5(d) and blindness
- An ACTUAL FUTURE drand round requirement
- The ONE holdout (`holdout_once` PREPARED NOT ADOPTED, default False)
- E1 as a FACTUAL ERRATUM
- `verify_split` UNADOPTED (default off)

**6. Counts, Names, and Text Execution**
Every count and name in the text is TRUE. The 107 tests across 13 suites passed cleanly under `-W error::ResourceWarning`. No elements are described-but-not-built. The 96 configurations ran correctly.

**7. The Questions File**
The questions file (`QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md`) asks exactly what needs Duho's input, no more, with strictly true consequences.

**8. What is Still Missing**
Nothing is missing. The complete package represents a thorough, internally consistent, and truthful state of affairs that accurately outlines the remaining vulnerabilities in the offline baseline while offering well-tested (albeit unadopted) compositional protections. 

VERDICT: SIGNABLE-AS-PRECOMMITMENT

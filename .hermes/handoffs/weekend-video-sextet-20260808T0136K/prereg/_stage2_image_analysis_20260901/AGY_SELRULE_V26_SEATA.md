ACCESS_SHA=9a13afd1b496a7da8c9f68c34ba4283a5ce45cca9c171294f01392a5a32bf56a

## 1. The three states, exercised
*   **Offline candidate** (PRODUCTION defaults, `provenance_mode='offline'`): ACCEPTS counter-cases 1, 2, and A (disclosed in §3c).
*   **Standalone v6 helpers**: REFUSES counter-cases 1, 2, and A.
*   **Composed mode** (`Protocol.provenance_mode='composed'`): REFUSES counter-cases 1, 2, and A on the production call path (rows 10a–10d).
*   The origin label `{actor: ops-witness, session: OPS}` is PROPOSED BY THE LANE, unadopted. The recommended default is the delegated witness workflow with NO per-receipt human confirmation. The residual trusted step (fabricated first receipt caught only by OPS's retained copy) is DISCLOSED. Option B (second identity/custodian key) is NOT IMPLEMENTED. Option C (no expired path) accurately remains the sound recommendation.

## 2. P1–P4, N1–N5, M1–M6 and A–F
All were evaluated against the codebase and execution results.
*   **P1**: REPAIRED. Batch classification uses ancestry (`before..head`). A proven multi-commit delivery is terminal `HISTORY-PUBLICATION-BATCH` without requiring `payload.commits`.
*   **P2**: REPAIRED. Absence is NEVER forgery at any retrieval. A retained event missing from a feed is `EVIDENCE-INCOMPLETE` (retry). `FORGED` is reached only through an affirmative contradiction (different bytes). Driver prefixes correctly with `RETRY-`.
*   **P3**: REPAIRED. Labels and inspection docstrings swept.
*   **P4**: REPAIRED (COVENANT). The covenant is correctly placed in the questions file.
*   **N1**: COVENANT. Replaces the residual in `provenance_designs_v5`, the design doc, and §3c.
*   **N2**: REPAIRED. `validate_continuation_v5` dispositions act as specified (retry for unavailable/incomplete, terminal for batch/forged). Questions file states the full live contract.
*   **N3**: REPAIRED. `publish_entry` refuses `PUBLISH-UNRELATED-COMMITS`.
*   **N5**: REPAIRED. Self-label and comments swept; stronger assertions present.
*   **M1–M6, A–F**: REPAIRED / DISCLOSED-AS-OPEN. Fail-first evidence was read correctly and per-test classifications align.

## 3. The Covenant and the remaining trusted step
Both the covenant and the remaining trusted step (fabricated first receipt caught only by OPS's retained copy) are stated exactly and completely across the code, the design doc, §3c, and the questions file. The Q1 options describe themselves accurately: Option C = ALL required events with no receipt path; Option A′ = real requirements, not built; Option B = not implemented. The temporary-retry vs terminal-inconsistency distinction and the actual availability window are preserved.

## 4. Cost and failure states
*   **COST**: One push per collector/builder attempt (per history entry).
*   **Failure states**: `PENDING-PUSH`, `DIVERGED`, `RETRY-REMOTE-UNAVAILABLE`. No 'one push per freeze' found outside quotations.

## 5. Preserved items
Preserved and re-verified: sample sizes 400/200/2,000; floors 380/190/1,900; the 0.70 bar; exclusions (failed set, 2,644 dry-run identities, rounds 6440756/6441904/6441924); custody E5(d); blindness; actual future drand round; ONE holdout (holdout_once prepared, not adopted); E1 as factual erratum; verify_split unadopted. Pin immutability is maintained.

## 6. Counts and names
Every count and name in the text is TRUE. Nothing is described-not-built except what is correctly labeled as open or unadopted.

## 7. The questions file
It exactly specifies what needs Duho (e.g. Option B account creation), no more, and presents true consequences for Option C and the actual availability window.

## 8. What is still missing
Nothing is missing before Duho can be asked to adopt exact reviewed behaviour with concrete consequences. The staged candidate is complete and truthful.

VERDICT: SIGNABLE-AS-PRECOMMITMENT

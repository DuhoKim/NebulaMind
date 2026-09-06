# DISCLOSED LIMITS vs REPAIRED CONTRADICTIONS — the two categories, kept apart (Blanc's order 02:06 KST, 2026-09-07)

A rule that documents what it cannot prove is honest. A rule that documents a contradiction between its text and its code as if it were a limit is not. This file is the register of which is which for the option (A) sampling amendment; every candidate text from V28 on carries the same split in §3c, and nothing that reaches Duho may merge the two columns.

## A. DISCLOSED LIMITS (a precommitment may legitimately carry these; reviewers confirm their disclosure)
| limit | where disclosed | what it means for the ACTUAL RUN |
|---|---|---|
| L-OFF: the OFFLINE candidate (PRODUCTION default) accepts a coherently forged approval event, a history rebuilt before the freeze, and codex's attack A | §3c; every inspection since V22 | if Duho adopts the offline baseline as the rule to run under, the driver does not detect those three fabrications; only the composed mode does |
| L-COV: THE COVENANT — the validator authenticates the published append-only history and ordered publications, not when operations occurred nor the completeness of unpublished observations/decisions (before genesis publication or between publications); an unpublished absence-based CLOSED can be erased; the seed is unchanged; a late approval event stays disqualifying | code, design doc, §3c, questions file | hidden attempts cannot change the fixed-round seed; an erased absence-based CLOSED cannot be detected by any validator; a stronger guarantee needs independently retained decision evidence, NOT implemented |
| L-RCPT: the fabricated-first-receipt step (Option A′ only) | design doc, §3c, questions file | irrelevant under Option C (recommended: no receipt path) |
| L-INH: the INHERITED V15 driver trusts the object lists / pool and exclusion digests (verify_split UNADOPTED, off) | §3c; inspection row 6 | a coherently sealed swapped list loads unless verify_split is adopted |
| L-AVAIL: GitHub's feed availability (300 events / 30 days; 30 s–6 h latency) governs Option C; retry dispositions are stateless — an inconsistent identity can stay pending indefinitely without ever loading | questions file, §3c | loss before tune or between tune and holdout closes the approval under the rule; the loader refuses, it does not persist the closure |

## B. CONTRADICTIONS (text says one thing, code does another) — REPAIRED in the next candidate, never disclosed as limits
| finding | the contradiction | repair (track 8, successors) |
|---|---|---|
| V27-1 precedence | the text promises "positive inconsistencies are terminal; retries are unavailable evidence"; the code declared a retry before examining a same-id contradiction, skipped the contradiction when a verbatim copy was present, and turned a locally decidable wrong-repository mismatch into a retry when the feed retrieval failed | `provenance_designs_v8`: local input checks BEFORE retrieval; same-id contradictions BEFORE the undetermined-delivery and verbatim-presence shortcuts; the same-commit arm scoped to the pinned protected ref |
| V27-2 tri-state propagation | the text promises tri-state delivery on the complete path; the driver's witness-commit precheck and the open-event stage still used the Boolean helper, and a git launch exception raised instead of reporting undetermined | driver v12 precheck and `validate_continuation_v8` open-event stage use `delivery()`; OSError → UNDETERMINED |
| V27-3 names/count | the driver lineage table, comments, an inspection header and a suite count said things the bytes do not | swept with per-item assertions |

Earlier contradictions of the same kind (V20 fatal … V26-1/2) were repaired in tracks 1–7; they are listed in the outcomes, not here, because they are closed. Any proportionality argument put to Duho later must carry: (1) the exact rule text to sign; (2) the enumerated remaining failure modes; (3) what each means for the actual run; (4) which are limits (column A) and which would be unrepaired contradictions (column B — none may remain).

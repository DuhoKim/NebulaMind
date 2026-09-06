# V25 CANDIDATE — COHERENT-ATTACK INSPECTION (supersedes the V24 inspection) — 2026-09-07 00:27 KST

Script: `_optionA_dev/track1/coherent_attacks_v25.py` on driver v9 / verdict v25 / provenance_designs_v5 (earlier scripts retained as pinned). Every counter-case keeps adjacent digests, counts and locks COHERENT. Remotes are LOCAL BARE repositories with non-fast-forward receives denied; the gh runner is FIXTURE-SUPPLIED with one push event per published commit (before = its parent) — both labelled: decision rules, not a real remote service. Rows 9c–9o = standalone helpers (9l/9m/9n/9o = codex's V23 M1 and V24 N2/N3 cases); rows 10a–10d = THE THREE STATES on the production call path.

| attack | staged V25 candidate (driver v9 / verdict v25 / provenance v5) | note |
|---|---|---|
| 0 baseline: real evidence, real seed, PRODUCTION re-deriver | ACCEPTED | the happy path |
| 1 forged event (coherent digest, invented provenance) | ACCEPTED | TRACK 2(a): authenticate_event → FORGED (see below) |
| 2 history deleted and rebuilt before the freeze (consistent lock/count/digest) | ACCEPTED | TRACK 2(b): validate_continuation → NOT-AN-EXTENSION (see below) |
| 3a (setup) baseline in a fresh repo | ACCEPTED |  |
| 3 second approval-record path committed and pushed | REFUSED APPROVAL-NOT-FIRST | v6 reproduces W4 |
| 4 re-encoded retained bodies (same signature) with a coherently re-pointed record | REFUSED IDENTITY-LOCK-MISMATCH | same VALUE; the earliest accept names the first record → lock mismatch is the correct refusal; with the first record it is ACCEPTED (correctly) |
| 5 live relay serves the signature in UPPERCASE hex | ACCEPT-DRAND (same seed, representation recorded ×4) | v22: decoded-bytes equality |
| 6 negative tuning objids, coherently sealed | ACCEPTED | INHERITED (V15 driver trusts the lists); verify_split (UNADOPTED, off) would refuse — exhibited in the e2e test on real builder output |
| 7 witness-closed entry present, coherently sealed | REFUSED COLLECTION-CLOSED | v6: CLOSED is terminal |
| 8 history suffix deleted (accept removed), coherently sealed | REFUSED COLLECTION-LOG-EMPTY | internally valid chain; TRACK 2(b) refuses; v6 refuses here only because no accept remains |
| 9a track 2(a) authenticate_event(genuine, fixture feed) | AUTHENTIC | fixture feed |
| 9b track 2(a) authenticate_event(codex's forgery, fixture feed) | FORGED | fixture feed |
| 9c track 2(b) v4 validate_continuation_v5(genuine: genesis-only open commit, authentic open event, one server-timed push event per commit) | OK | asks the remote; authenticates the open event; per-commit push events |
| 9d track 2(b) v3: codex V21 counterexample 1 — ACCEPT appended, NOT pushed | REFUSED PENDING-PUSH |  |
| 9e track 2(b) v3: committed but NOT acknowledged by the remote | REFUSED PENDING-PUSH |  |
| 9f track 2(b) v3: codex V21 counterexample 2 — local reset to history-open, RETRY replaced by ACCEPT, remote unchanged | REFUSED HISTORY-DIVERGED |  |
| 9g track 2(b) v3: the rewrite pushed to the protected remote | push REJECTED (non-fast-forward); REFUSED HISTORY-DIVERGED |  |
| 9h track 2(b) v3: remote unreachable | REFUSED RETRY-REMOTE-UNAVAILABLE | RETRY, never a pass |
| 9i track 2(b) v3: open event ABSENT from the live feed | REFUSED OPEN-EVENT-EXPIRED | codex V22 A: the anchor is authenticated |
| 9j track 2(b) v3: live feed EMPTY | REFUSED OPEN-EVENT-UNAVAILABLE | codex V22 F: UNAVAILABLE, never FORGED |
| 9k track 2(b) v5: codex V22 attack A — rebuilt history published as the FIRST commit, named history-open | REFUSED OPEN-NOT-GENESIS-ONLY | v2 said True |
| 9l codex V23 M1: four single-entry commits delivered by ONE late push | v3: OK / v5: REFUSED HISTORY-PUBLICATION-BATCH | v3 said True; v5 requires one server-timed push event per commit (proven batch = terminal) |
| 9m codex V24 N2: complete feed for approval/open, EMPTY feed on the per-entry retrieval | REFUSED EVIDENCE-UNAVAILABLE | v4 said BATCH; v5 = retry |
| 9n codex V24 N2: one middle per-commit event missing, no evidence of batching | REFUSED EVIDENCE-INCOMPLETE | v4 said BATCH; v5 = retry within the window |
| 9o codex V24 N3: unrelated unpublished commit alongside a new entry | REFUSED PUBLISH-UNRELATED-COMMITS | v5 producer precondition; nothing pushed |
| 10a genuine identity, history published one entry per acknowledged commit, open event + approval event in the live feed | offline: ACCEPTED / composed: ACCEPTED | same identity, same load_identity call; composed = UNADOPTED |
| 10b attack 1 again: forged approval event (coherent digest; names the pinned repo), live feed does not contain it | offline: ACCEPTED / composed: REFUSED EVENT-EXPIRED-NO-RECEIPT-PATH (the live feed no longer reaches the even) | same identity, same load_identity call; composed = UNADOPTED |
| 10c attack 2 again: history rebuilt after honest publication, coherently sealed and pushed fast-forward | offline: ACCEPTED / composed: REFUSED HISTORY-CONTINUATION (HISTORY-NOT-AN-EXTENSION at d899e4de53c8) | same identity, same load_identity call; composed = UNADOPTED |
| 10d codex V22 attack A: history rebuilt BEFORE its first publication, published as the first commit and named history-open | offline: ACCEPTED / composed: REFUSED HISTORY-CONTINUATION (OPEN-NOT-GENESIS-ONLY) | same identity, same load_identity call; composed = UNADOPTED |

## Reading
- OFFLINE candidate (default): counter-cases 1, 2, A remain ACCEPTED — the disclosed boundaries; unchanged.
- v5 dispositions (9m, 9n): an EMPTY per-entry retrieval is EVIDENCE-UNAVAILABLE and a missing per-commit event without proof of batching is EVIDENCE-INCOMPLETE — both RETRY (v4 said BATCH for both); a proven multi-commit delivery is still HISTORY-PUBLICATION-BATCH (9l).
- v5 producer (9o): an unrelated unpublished commit alongside a new entry is refused BEFORE pushing (PUBLISH-UNRELATED-COMMITS); nothing pushed.
- COMPOSED mode (v9 on v5): refuses counter-cases 1 (10b), 2 (10c) and A (10d); accepts the genuine identity (10a); its EVIDENCE-* refusals are prefixed RETRY-.
- THE COVENANT (codex V24 N1): the validator authenticates the published append-only history and distinct ordered publications; it does not authenticate when operations occurred nor the completeness of unpublished observations or decisions, before genesis publication or between later publications; the seed is unchanged; a late approval event stays disqualifying; stronger completeness needs independently retained decision evidence, not implemented. Counter-case 6 (arbitrary lists) remains the INHERITED V15 driver limitation (verify_split UNADOPTED, off).

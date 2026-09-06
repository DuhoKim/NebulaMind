# V24 CANDIDATE — COHERENT-ATTACK INSPECTION (supersedes the V23 inspection) — 2026-09-06 23:50 KST

Script: `_optionA_dev/track1/coherent_attacks_v24.py` on driver v8 / verdict v24 / provenance_designs_v4 (the V23 script is retained as pinned). Every attack keeps adjacent digests, counts and locks COHERENT. Remotes are LOCAL BARE repositories with non-fast-forward receives denied; the gh runner is FIXTURE-SUPPLIED with ONE push event per published commit (before = its parent) — both labelled: decision rules, not a real remote service. Rows 9c–9l = standalone helpers (9l compares v3 and v4 on codex's V23 M1 case); rows 10a–10d = THE THREE STATES on the production call path.

| attack | staged V22 candidate (driver v6 / verdict v22) | note |
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
| 9c track 2(b) v4 validate_continuation_v4(genuine: genesis-only open commit, authentic open event, one server-timed push event per commit) | OK | asks the remote; authenticates the open event; per-commit push events |
| 9d track 2(b) v3: codex V21 counterexample 1 — ACCEPT appended, NOT pushed | REFUSED PENDING-PUSH |  |
| 9e track 2(b) v3: committed but NOT acknowledged by the remote | REFUSED PENDING-PUSH |  |
| 9f track 2(b) v3: codex V21 counterexample 2 — local reset to history-open, RETRY replaced by ACCEPT, remote unchanged | REFUSED HISTORY-DIVERGED |  |
| 9g track 2(b) v3: the rewrite pushed to the protected remote | push REJECTED (non-fast-forward); REFUSED HISTORY-DIVERGED |  |
| 9h track 2(b) v3: remote unreachable | REFUSED RETRY-REMOTE-UNAVAILABLE | RETRY, never a pass |
| 9i track 2(b) v3: open event ABSENT from the live feed | REFUSED OPEN-EVENT-EXPIRED | codex V22 A: the anchor is authenticated |
| 9j track 2(b) v3: live feed EMPTY | REFUSED OPEN-EVENT-UNAVAILABLE | codex V22 F: UNAVAILABLE, never FORGED |
| 9k track 2(b) v4: codex V22 attack A — rebuilt history published as the FIRST commit, named history-open | REFUSED OPEN-NOT-GENESIS-ONLY | v2 said True |
| 9l codex V23 M1: four single-entry commits delivered by ONE late push | v3: OK / v4: REFUSED HISTORY-PUBLICATION-BATCH | v3 said True; v4 requires one server-timed push event per commit |
| 10a genuine identity, history published one entry per acknowledged commit, open event + approval event in the live feed | offline: ACCEPTED / composed: ACCEPTED | same identity, same load_identity call; composed = UNADOPTED |
| 10b attack 1 again: forged approval event (coherent digest; names the pinned repo), live feed does not contain it | offline: ACCEPTED / composed: REFUSED EVENT-EXPIRED-NO-RECEIPT-PATH (the live feed no longer reaches the even) | same identity, same load_identity call; composed = UNADOPTED |
| 10c attack 2 again: history rebuilt after honest publication, coherently sealed and pushed fast-forward | offline: ACCEPTED / composed: REFUSED HISTORY-CONTINUATION (HISTORY-NOT-AN-EXTENSION at cdc1abf9bd6a) | same identity, same load_identity call; composed = UNADOPTED |
| 10d codex V22 attack A: history rebuilt BEFORE its first publication, published as the first commit and named history-open | offline: ACCEPTED / composed: REFUSED HISTORY-CONTINUATION (OPEN-NOT-GENESIS-ONLY) | same identity, same load_identity call; composed = UNADOPTED |

## Reading
- OFFLINE candidate (default): attacks 1, 2, A remain ACCEPTED — the disclosed boundaries; unchanged.
- v4 (9c, 9l): a genuine history with one server-timed push event per commit validates; codex's V23 M1 case — four single-entry commits delivered by ONE late push — is OK under v3 and REFUSED under v4 (HISTORY-PUBLICATION-BATCH).
- COMPOSED mode (v8 on v4): refuses attack 1 (10b), attack 2 (10c), codex V22 attack A (10d); accepts the genuine identity whose every history commit has its own push event (10a).
- RESIDUAL, stated exactly (codex V23 M3): work done before the genesis was published — attempts and absence-based terminal decisions — is unauthenticated by any validator; under drand-only it cannot change the fixed-round seed; a late approval event stays disqualifying; a stronger guarantee needs an independently retained decision anchor, not staged. Attack 6 (arbitrary lists) remains the INHERITED V15 driver limitation (verify_split UNADOPTED, off).

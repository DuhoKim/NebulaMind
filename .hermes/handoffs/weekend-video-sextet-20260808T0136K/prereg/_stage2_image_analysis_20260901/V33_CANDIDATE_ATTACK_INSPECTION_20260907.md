# V33 CANDIDATE — COHERENT-ATTACK INSPECTION (staged, UNADOPTED) — 2026-09-07 06:48 KST

Executed: `_optionA_dev/track1/coherent_attacks_v33.py` (SHA-256 1a159f61a6cbe0c8751bbc6f4d11ba226c3e0bcdbf9fcf6079577f40698d045d) — driver v17 (NSD at input granularity, check-attributed findings, precedence_core), verdict v33, provenance_designs_v13; the modules named in the header are the modules imported and executed. Warning-strict; the one inherited RuntimeWarning at fourier_chirality.py:87 is the known one. Every row carries the SAME verdict as the V32 inspection (35 rows; row 10b's refusal wording now names the COMPLETE snapshot; fixture commit hashes differ per run).

TWO CATEGORIES, KEPT APART (Blanc 02:06): rows 1, 2, 6 and 10b–10d show the offline candidate LOADING counter-cases 1, 2, A and the inherited list trust — DISCLOSED LIMITS (column one of §3c). The NSD controls (derived from the INDEPENDENCE table, 105 pairs + 6 two-prerequisite variants) and codex's V32 constructions (16 regressions) are executed by track 13 on the complete path, not rows of this table. No row here is an unrepaired contradiction.

RE-EXECUTED 2026-09-07 07:23 KST on the FINAL V33 bytes (driver v17 876f6db5d287aced…, provenance v13 b3d006188c98131b…, attacks v33 1a159f61a6cbe0c8…) after the 06:48 run above (which preceded the adoption-identity split and per-entry's partial-snapshot statement): stdout `_tmp_v33_inspection_stdout_RUN2.txt` (sha256 d3d3b75424034b52351e81317c9bc84a9090b4bc5d0cf65d32c4107d69bdb7ea); the table below is the RUN2 table; every verdict identical to RUN1 (`_tmp_v33_inspection_stdout.txt`, sha256 be56291b69eb9b3d3e114492cc1104deb4b4883ae4ea4cb86080c8a9c321af20); the one textual difference is the fixture's rebuilt-history commit hash in row 10c's reason (run-dependent).

| attack | staged V33 candidate (driver v17 / verdict v33 / provenance v13) | note |
|---|---|---|
| 0 baseline: real evidence, real seed, PRODUCTION re-deriver | ACCEPTED | the happy path |
| 1 forged event (coherent digest, invented provenance) | ACCEPTED | TRACK 2(a): codex's wrong-repository forgery → INCONSISTENT-INPUT (row 9b); a same-id / same-commit contradiction → FORGED (rows 9s–9u; see below) |
| 2 history deleted and rebuilt before the freeze (consistent lock/count/digest) | ACCEPTED | TRACK 2(b): validate_continuation → NOT-AN-EXTENSION (see below) |
| 3a (setup) baseline in a fresh repo | ACCEPTED |  |
| 3 second approval-record path committed and pushed | REFUSED APPROVAL-NOT-FIRST | v6 reproduces W4 |
| 4 re-encoded retained bodies (same signature) with a coherently re-pointed record | REFUSED IDENTITY-LOCK-MISMATCH | same VALUE; the earliest accept names the first record → lock mismatch is the correct refusal; with the first record it is ACCEPTED (correctly) |
| 5 live relay serves the signature in UPPERCASE hex | ACCEPT-DRAND (same seed, representation recorded ×4) | v22: decoded-bytes equality |
| 6 negative tuning objids, coherently sealed | ACCEPTED | INHERITED (V15 driver trusts the lists); verify_split (UNADOPTED, off) would refuse — exhibited in the e2e test on real builder output |
| 7 witness-closed entry present, coherently sealed | REFUSED COLLECTION-CLOSED | v6: CLOSED is terminal |
| 8 history suffix deleted (accept removed), coherently sealed | REFUSED COLLECTION-LOG-EMPTY | internally valid chain; TRACK 2(b) refuses; v6 refuses here only because no accept remains |
| 9a track 2(a) authenticate_event(genuine, fixture feed) | AUTHENTIC | fixture feed |
| 9b track 2(a) authenticate_event(codex's forgery, fixture feed) | INCONSISTENT-INPUT | fixture feed |
| 9c track 2(b) v4 validate_continuation_v7(genuine: genesis-only open commit, authentic open event, one server-timed push event per commit) | OK | asks the remote; authenticates the open event; per-commit push events |
| 9d track 2(b) v3: codex V21 counterexample 1 — ACCEPT appended, NOT pushed | REFUSED PENDING-PUSH |  |
| 9e track 2(b) v3: committed but NOT acknowledged by the remote | REFUSED PENDING-PUSH |  |
| 9f track 2(b) v3: codex V21 counterexample 2 — local reset to history-open, RETRY replaced by ACCEPT, remote unchanged | REFUSED HISTORY-DIVERGED |  |
| 9g track 2(b) v3: the rewrite pushed to the protected remote | push REJECTED (non-fast-forward); REFUSED HISTORY-DIVERGED |  |
| 9h track 2(b) v3: remote unreachable | REFUSED RETRY-REMOTE-UNAVAILABLE | RETRY, never a pass |
| 9i track 2(b) v3: open event ABSENT from the live feed | REFUSED EVIDENCE-EXPIRED (history-open event) | codex V22 A: the anchor is authenticated |
| 9j track 2(b) v3: live feed EMPTY | REFUSED EVIDENCE-UNAVAILABLE (history-open event) | codex V22 F: UNAVAILABLE, never FORGED |
| 9k track 2(b) v7: codex V22 attack A — rebuilt history published as the FIRST commit, named history-open | REFUSED OPEN-NOT-GENESIS-ONLY | v2 said True |
| 9l codex V23 M1: four single-entry commits delivered by ONE late push | v3: OK / v7: REFUSED HISTORY-PUBLICATION-BATCH | v3 said True; v6 requires one server-timed push event per commit (proven batch = terminal) |
| 9m codex V24 N2: complete feed for approval/open, EMPTY feed on the per-entry retrieval | REFUSED EVIDENCE-UNAVAILABLE | v4 said BATCH; v5 = retry |
| 9n codex V24 N2: one middle per-commit event missing, no evidence of batching | REFUSED EVIDENCE-INCOMPLETE | v4 said BATCH; v5 = retry within the window |
| 9o codex V24 N3: unrelated unpublished commit alongside a new entry | REFUSED PUBLISH-UNRELATED-COMMITS | v5 producer precondition; nothing pushed |
| 9p codex V25 P1: the same late batch, push event WITHOUT payload.commits (before..head only) | v5: REFUSED EVIDENCE-INCOMPLETE / v6: REFUSED HISTORY-PUBLICATION-BATCH | v5 called a proven batch 'incomplete'; v6 uses the ancestry predicate → terminal |
| 9q codex V25 P2: the retained approval event ABSENT from a non-empty feed that covers its time | v6: INCOMPLETE (the v5 function said FORGED — receipt run 1b) | absence is not forgery |
| 9r codex V25 P2: a push delivering the same commit with DIFFERENT bytes | FORGED | affirmative contradiction → FORGED |
| 9s codex V26-1: retained event = the live event with a DIFFERENT `before` only (same id, same head) | v7: FORGED (v6 said INCOMPLETE — receipt run 1b) | same-event contradiction → terminal |
| 9t codex V26-2: before..head delivery, full clone | v7: AUTHENTIC |  |
| 9u codex V26-2: the same event and feed, a clone MISSING the descendant object | v7: UNAVAILABLE (v6 said FORGED — receipt run 1b) | undeterminable delivery → retry, never forgery |
| 10a genuine identity, history published one entry per acknowledged commit, open event + approval event in the live feed | offline: ACCEPTED / composed: ACCEPTED | same identity, same load_identity call; composed = UNADOPTED |
| 10b attack 1 again: forged approval event (coherent digest; names the pinned repo), live feed does not contain it | offline: ACCEPTED / composed: REFUSED EVENT-FORGED (the retained event is absent from the CO) | same identity, same load_identity call; composed = UNADOPTED |
| 10c attack 2 again: history rebuilt after honest publication, coherently sealed and pushed fast-forward | offline: ACCEPTED / composed: REFUSED HISTORY-CONTINUATION (HISTORY-NOT-AN-EXTENSION at 614910a172eb) | same identity, same load_identity call; composed = UNADOPTED |
| 10d codex V22 attack A: history rebuilt BEFORE its first publication, published as the first commit and named history-open | offline: ACCEPTED / composed: REFUSED HISTORY-CONTINUATION (OPEN-NOT-GENESIS-ONLY) | same identity, same load_identity call; composed = UNADOPTED |

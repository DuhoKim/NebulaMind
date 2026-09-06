# V23 CANDIDATE — COHERENT-ATTACK INSPECTION (supersedes the V22 inspection; Blanc 20:45: the review must assess the complete object) — 2026-09-06 22:07 KST

Script: `_optionA_dev/track1/coherent_attacks.py` on driver v7 / verdict v23 / provenance_designs_v3 (deterministic; run under the pinned interpreter with the lane venv on PYTHONPATH). Every attack keeps adjacent digests, counts and locks COHERENT. Remotes are LOCAL BARE repositories with non-fast-forward receives denied; the gh runner is FIXTURE-SUPPLIED — both labelled: decision rules, not a real remote service. Rows 9c–9k = the standalone v3 helpers; rows 10a–10d = THE THREE STATES on the production call path (same identity, same `load_identity`, OFFLINE default vs COMPOSED unadopted).

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
| 9c track 2(b) v3 validate_continuation_v3(genuine: genesis-only open commit, authentic open event, one entry per acknowledged commit) | OK | asks the remote; authenticates the open event |
| 9d track 2(b) v3: codex V21 counterexample 1 — ACCEPT appended, NOT pushed | REFUSED PENDING-PUSH |  |
| 9e track 2(b) v3: committed but NOT acknowledged by the remote | REFUSED PENDING-PUSH |  |
| 9f track 2(b) v3: codex V21 counterexample 2 — local reset to history-open, RETRY replaced by ACCEPT, remote unchanged | REFUSED HISTORY-DIVERGED |  |
| 9g track 2(b) v3: the rewrite pushed to the protected remote | push REJECTED (non-fast-forward); REFUSED HISTORY-DIVERGED |  |
| 9h track 2(b) v3: remote unreachable | REFUSED RETRY-REMOTE-UNAVAILABLE | RETRY, never a pass |
| 9i track 2(b) v3: open event ABSENT from the live feed | REFUSED OPEN-EVENT-EXPIRED | codex V22 A: the anchor is authenticated |
| 9j track 2(b) v3: live feed EMPTY | REFUSED OPEN-EVENT-UNAVAILABLE | codex V22 F: UNAVAILABLE, never FORGED |
| 9k track 2(b) v3: codex V22 attack A — rebuilt history published as the FIRST commit, named history-open | REFUSED OPEN-NOT-GENESIS-ONLY | v2 said True |
| 10a genuine identity, history published one entry per acknowledged commit, open event + approval event in the live feed | offline: ACCEPTED / composed: ACCEPTED | same identity, same load_identity call; composed = UNADOPTED |
| 10b attack 1 again: forged approval event (coherent digest; names the pinned repo), live feed does not contain it | offline: ACCEPTED / composed: REFUSED EVENT-EXPIRED-NO-RECEIPT-PATH (the live feed no longer reaches the even) | same identity, same load_identity call; composed = UNADOPTED |
| 10c attack 2 again: history rebuilt after honest publication, coherently sealed and pushed fast-forward | offline: ACCEPTED / composed: REFUSED HISTORY-CONTINUATION (HISTORY-NOT-AN-EXTENSION at 2d7039a8a0d1) | same identity, same load_identity call; composed = UNADOPTED |
| 10d codex V22 attack A: history rebuilt BEFORE its first publication, published as the first commit and named history-open | offline: ACCEPTED / composed: REFUSED HISTORY-CONTINUATION (OPEN-NOT-GENESIS-ONLY) | same identity, same load_identity call; composed = UNADOPTED |

## Reading
- OFFLINE candidate (default): attacks 1, 2 and codex V22 A (rows 1, 2, 6, 10a–10d offline column) are ACCEPTED — the disclosed boundaries; unchanged.
- COMPOSED mode (UNADOPTED, v7 on v3): refuses attack 1 (10b), attack 2 (10c) and codex V22 attack A (10d: OPEN-NOT-GENESIS-ONLY — a rebuilt history published as the first commit is not a genesis-only history-open commit); accepts the genuine identity published one entry per acknowledged commit with its open event in the live feed (10a).
- Standalone v3 (9c–9k): codex's V21 counterexamples (9d, 9f) and V22 attack A (9k) refused; an open event absent from the feed is refused (9i — classified EXPIRED because it is older than the feed's oldest event; there is no receipt path for the open event, so EXPIRED is terminal); an EMPTY feed is UNAVAILABLE, never FORGED (9j).
- Row 10b: codex's forgery is backdated to 2000, so it lands on the EXPIRED path and is refused because no receipt path is configured (Q1 Option C); an in-window forgery is FORGED outright (`test_composed_mode_on_the_production_call_path`).
- RESIDUAL, stated (provenance_designs_v3 docstring): attempts made BEFORE the genesis was published are undetectable by any validator; under drand-only they cannot change the seed and cannot hide a CLOSED witness state (anchored by the approval event's server time). Attack 6 (arbitrary lists) remains the INHERITED V15 driver limitation; `verify_split` (UNADOPTED, off) refuses it on real builder output.

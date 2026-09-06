# V22 CANDIDATE — COHERENT-ATTACK INSPECTION (Blanc 20:45: the review must assess the complete object, not the happy path) — 2026-09-06 20:55 KST

Script: `_optionA_dev/track1/coherent_attacks.py` (run under the pinned interpreter with the lane venv on PYTHONPATH; deterministic). Each attack is codex's V21 substitution re-applied to the STAGED candidate (driver v6, verdict v22, history_v2) with every adjacent digest, count and lock kept COHERENT — not a stale-digest mutation. Column 2 is what the candidate does TODAY; the note says which track-2 UNADOPTED design closes the ones still ACCEPTED. The track-2 rows use a FIXTURE-SUPPLIED live feed and a LOCAL BARE remote with non-fast-forward receives denied (both labelled): they demonstrate the decision rules, not a real remote service. REVISED 21:08 KST: rows 9c–9h now run `provenance_designs_v2` (the remote-consulting validator) including codex's two counterexamples of 21:00. REVISED 21:19 KST: rows 10a–10c exercise THE THREE STATES Blanc's 21:14 order requires ON THE PRODUCTION CALL PATH — the same identity through the same `load_identity` under the OFFLINE candidate (default) and under the UNADOPTED COMPOSED mode (`Protocol.provenance_mode = 'composed'`: track-2 v2 helpers called inside `load_identity`).

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
| 9c track 2(b) v2 validate_continuation_v2(genuine, every entry pushed) | OK | asks the remote (ls-remote) |
| 9d track 2(b) v2: codex counterexample 1 — ACCEPT appended, NOT pushed | REFUSED PENDING-PUSH | v1 said True |
| 9e track 2(b) v2: committed but NOT acknowledged by the remote | REFUSED PENDING-PUSH |  |
| 9f track 2(b) v2: codex counterexample 2 — local reset to history-open, RETRY replaced by ACCEPT, remote unchanged | REFUSED HISTORY-DIVERGED | v1 said True |
| 9g track 2(b) v2: the rewrite pushed to the protected remote | push REJECTED (non-fast-forward); REFUSED HISTORY-DIVERGED |  |
| 9h track 2(b) v2: remote unreachable | REFUSED RETRY-REMOTE-UNAVAILABLE | RETRY, never a pass |
| 10a genuine identity, history published per design (b), genuine event in the live feed | offline: ACCEPTED / composed: ACCEPTED | same identity, same load_identity call; composed = UNADOPTED |
| 10b attack 1 again: forged event (coherent digest; names the pinned repo), live feed does not contain it | offline: ACCEPTED / composed: REFUSED EVENT-EXPIRED-NO-RECEIPT-PATH (the live feed no longer reaches the even) | same identity, same load_identity call; composed = UNADOPTED |
| 10c attack 2 again: history rebuilt after history-open, coherently sealed and pushed fast-forward | offline: ACCEPTED / composed: REFUSED HISTORY-CONTINUATION (HISTORY-NOT-AN-EXTENSION at c2c806a72219) | same identity, same load_identity call; composed = UNADOPTED |

## Reading
- THE THREE STATES (rows 10a–10c): (1) the OFFLINE candidate — default, what a gate of V22 would approve — ACCEPTS attacks 1 and 2 (disclosed boundaries); (2) the STANDALONE helpers (rows 9a–9h) refuse them in isolation; (3) the COMPOSED mode — UNADOPTED, same call path — refuses both (EVENT-FORGED; HISTORY-CONTINUATION / NOT-AN-EXTENSION) and accepts the genuine identity. Note on row 10b: codex's forgery backdates itself to 2000, so against a live feed whose oldest event is later it lands on the EXPIRED path, not FORGED — refused here only because no receipt path is configured (Q1 Option C); under Options A/B it would be checked against the receipt (absent there → refused). A forgery dated inside the feed's window is FORGED outright (rows 9b; the driver test `test_composed_mode_on_the_production_call_path`). Adopting the design = flipping `provenance_mode` to composed and supplying the runner, the history-open commit and (if any) the receipt path; nothing else changes.
- Still ACCEPTED by the staged candidate: attack 1 (forged event) and attack 2 (rebuilt history) — the two provenance boundaries; both are refused by the track-2 v2 designs (rows 9b; 9d–9g), which are UNADOPTED and need Duho's word on the trust they introduce (TRACK2_PROVENANCE_DESIGNS_UNADOPTED_20260906.md). Attack 6 (arbitrary lists) is the INHERITED V15 driver limitation; the staged `verify_split` check (off by default) refuses it on real builder output (exhibited in `test_run_configurations_v6` end-to-end) — adopting it is Duho's.
- Refused by the staged candidate: 3 (second approval path — W4 now in the driver), 4 (re-pointed record — the earliest accept binds), 7 (CLOSED is terminal), 8 (suffix deletion that removes the accept). Attack 5 (uppercase signature) is now correctly the same value.
- Attack 8 with the accept KEPT and only later entries deleted would still validate internally — closed only by track 2(b) v2 (the working tree must equal the blob at the live remote head). Stated, not hidden.
- Codex's 21:00 counterexamples (rows 9d, 9f): v1 of the history design said True to both; v2 refuses both because it asks the remote and treats anything the remote has not acknowledged as PENDING-PUSH.

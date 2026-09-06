ACCESS_SHA=d29aabac28d6d7de32e8b33b5ec4082c5c758a0ebf9913455f7b8b9cd642e1a3

JUDGE, [MINOR] 1. The three states, exercised: 
- OFFLINE candidate (production default): ACCEPTED. Still accepts counter-cases 1, 2, and A (disclosed in §3c).
- STANDALONE v5 helpers (`provenance_designs_v5.py`): REFUSED. Correctly refuses forged events (FORGED), rebuilt histories (NOT-AN-EXTENSION), and rebuilt history published as first commit (OPEN-NOT-GENESIS-ONLY).
- COMPOSED mode (`Protocol.provenance_mode='composed'`): REFUSED. Accurately enforces the v5 helpers within `load_identity`, matching standalone refusals.

JUDGE, [MINOR] 2. Claims Assessment (N1–N5, M1–M6, A–F): 
- N1: COVENANT. The residual is fully disclosed; validator explicitly authenticates only published history and order, not completion/absence of unpublished attempts.
- N2: REPAIRED. `validate_continuation_v5` correctly returns `EVIDENCE-UNAVAILABLE` (retry) for empty retrieval and `EVIDENCE-INCOMPLETE` (retry) for missing push events. `HISTORY-PUBLICATION-BATCH` is terminal only on proven multi-commit delivery. Driver v9 correctly prefixes with `RETRY-`.
- N3: REPAIRED. `publish_entry` correctly refuses `PUBLISH-UNRELATED-COMMITS` before any push when unpublished local commits exist alongside the pending entry.
- N5: REPAIRED. §3c self-label, §9 script name, and driver comments swept correctly.
- M1–M6 & A–F: DISCLOSED-AS-OPEN / REPAIRED. Fail-first evidence read correctly per-test classification; correction notes applied.

JUDGE, [MINOR] 3. The Covenant and the remaining trusted step: 
Stated exactly and completely across the code, the design doc, §3c, and the questions file. The Q1 options describe themselves accurately (Option C = ALL required events live; Option A′ = its real requirements, not built; Option B = not implemented). The temporary-retry vs terminal-inconsistency distinction and the actual availability window are fully preserved.

JUDGE, [MINOR] 4. Cost and failure states: 
COST: one push per collector/builder attempt (per history entry).
Failure states correctly implemented: PENDING-PUSH / DIVERGED / RETRY-REMOTE-UNAVAILABLE. No 'one push per freeze' flags remain outside quotations.

JUDGE, [MINOR] 5. Preserved items: 
Re-verified sample sizes 400/200/2,000; floors 380/190/1,900; the 0.70 bar; exclusions (failed set, 2,644 dry-run identities, rounds 6440756/6441904/6441924); custody E5(d); blindness; ACTUAL FUTURE drand round check; ONE holdout (holdout_once PREPARED NOT ADOPTED, default False); E1 as FACTUAL ERRATUM; verify_split UNADOPTED (default off).

JUDGE, [MINOR] 6. Text accuracy: 
Every count and name in the text is TRUE and verified by run. Anything described-not-built is explicitly labelled as such.

JUDGE, [MINOR] 7. The questions file: 
Contains exactly what needs Duho (Option B token/key provision), no more, with true consequences.

JUDGE, [MINOR] 8. What is still missing: 
Nothing is missing. The rule, design, and code correctly and truthfully represent the complete required behaviour, boundaries, and consequences.

VERDICT: SIGNABLE-AS-PRECOMMITMENT

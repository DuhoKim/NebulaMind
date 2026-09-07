ACCESS_SHA=a2c396be1f5e4924bbf8f49f02558a2739151a97c44e2d9034e281e34a037139

**1. DOES THE PROPOSAL STILL PRODUCE A TRUSTWORTHY NUMBER?**
[FATAL] The proposal replaces the independent PushEvent witness and signature-relative time with an unwitnessed, locally-recorded commit clock (`UTC C`). This deferral actually invalidates the comparison because a lane owner can simply backdate a local commit time to match an already-published favorable drand round, allowing them to secretly test seeds until they get a favorable split. The number cannot be trusted without a third-party anchor to prove the seed was prospectively drawn.

**2. THE SEED.**
[FATAL] Ten minutes is NOT genuinely sufficient given how the commit is recorded. Because A1 defers the PushEvent witness and relies only on "the lane owner commits the manifest and retains commit ID and UTC C", the owner can backdate the local commit time `C` to match a drand round that has already occurred. Thus, a party who has seen the candidate pool can secretly grind seeds and influence which round is used, completely circumventing the prospective guarantee.

**3. THE CLAUSE DISPOSITION.**
[MAJOR] Clause: §3b Order (2) `first whole minute >= T_sign+600 seconds`. A1 marks this as DROP, framing it as NIST-only machinery. This is false. `T_sign` anchored the clock to a witnessed third-party chat statement. Removing it and replacing it with a local, unwitnessed `C` is a fundamental degradation of the timeline's security, not a drand-only consequence. Changing the randomness source to drand does not require dropping the third-party time anchor. (Note: There are exactly six `DROP` rows in the disposition table, not seven).

**4. THE LEDGER.**
[MAJOR] A1's "WHAT THE READER LOSES" section lists "Commit-relative clock" and "Witness/provenance stack" as separate, independent losses. It completely misses their compounded fatal effect: replacing the time anchor with a local clock *while also* deferring the PushEvent witness creates an open door for invisible seed grinding and history-rewriting. This catastrophic loss of forward-secrecy is missing from the ledger.

**5. THE SELECTION CODE.**
[MAJOR] `select_sample.py` does NOT do exactly what the text says:
1. A1 requires: "verify membership, uniqueness and exclusion disjointness." The code simply uses `set(excluded) | set(failed)`. It does not check if the files contain duplicates, it does not verify that exclusion and failed are disjoint, and it does not verify that their members actually exist in the eligible file.
2. Floor vs Size contradiction: The code checks if `available < floor` in the first loop, but then subsequently slices and demands `available < size` in the second loop, raising a `ValueError` if the pool satisfies the floor but not the full size (e.g., if there are 1950 available for validation, it passes the 1900 floor check but crashes on the 2000 size check). The tests pass only because they use a pool large enough to satisfy the full sizes.

**6. THE INPUT CONTRACT.**
[FATAL] A1 requires files and digests to be fixed before the seed round is named. While conceptually sufficient, the ordering is entirely unenforceable as written because the proof of "when" it was fixed relies entirely on the unwitnessed local commit timestamp. Without a mechanism to prove the commit existed *before* the drand round was published, the ordering rule is unenforceable.

**7. A1's OWN OPEN QUESTIONS.**
- Q1 (Numerical renderable population): Unanswered. Requires execution/decision to count the remaining 7,410.
- Q2 (Full SHA-256 for failed-set/validation-gate): Unanswered. Requires Duho to supply the full pins.
- Q3 (Exact denominator/p_val calculation): Answered by V15 §5 and §7. It is exactly `max(k, m-k)/2000` for validation (`/200` for holdout), with a fixed denominator where unscored objects count as misses.
- Q4 (BLS verifier): Unanswered. Duho approved drand-only ("해"), but did not specify if the proposed BLS verification must be built or if the V15 fallback (2 of 4 relays agreeing) suffices. Decision needed.
- Q5 (Immutable rendering artifacts): Unanswered without Duho.
- Q6 (Render-refused representation): Unanswered. V15 run record notes a sentinel-tensor is needed, but states this must be a formal clause. Decision needed.
- Q7 (V15 §10's V2 clause): Unanswered. The text is not in the source bundle.
- Q8 (Conflicting seal-helper status): Unanswered. V15 run record shows it was written and tested but awaits a ruling.

**8. WHAT IS STILL MISSING.**
Before this proposal can be put to Duho for adoption, it needs:
1. A mandatory third-party witness requirement for the manifest commit (e.g., pushing to GitHub or a chat statement) strictly BEFORE the drand round is named, to restore the prospective nature of the seed.
2. Corrections to `select_sample.py` to actually enforce exclusion uniqueness, disjointness, and membership, and to fix the broken floor/size logic.
3. Explicit decisions from Duho on the 8 open questions.
Nothing is currently in a state that he could sign.

VERDICT: NOT-SOUND

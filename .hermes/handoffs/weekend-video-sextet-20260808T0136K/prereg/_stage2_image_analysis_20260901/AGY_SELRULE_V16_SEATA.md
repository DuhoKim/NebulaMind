ACCESS_SHA=fe1487bd1be7dcd3b27798727d2d39f2b5f54d21d74faffdaaaa9f059450f488

# Independent Referee Report (Seat A - AGY) for Option A V16 Draft

**AUTHORSHIP:** I confirm that I am evaluating this code and text as an independent referee. I did not author the code or text under review. (Note: As stated in the prompt, seat B authored the code.)

**RUN (warning-strict):**
All provided commands were executed successfully:
(a) Unit tests in `_optionA_dev/beacon_v2` (`test_beacon_record_expedited.py`, `test_beacon_v2.py`) ran and passed (29 tests total).
(b) Unit tests in `_optionA_dev/corpus_identity` (`test_build_corpus_identity_v16.py`, `test_build_corpus_identity.py`) ran and passed (7 tests total).
(c) The diffs for `beacon_record.py` vs `beacon_record_expedited.py` and `build_corpus_identity.py` vs `build_corpus_identity_v16.py` match the described 17 and 4 changed lines, respectively.
(d) `signature_preimage.py` correctly printed `fe1487bd1be7dcd3b27798727d2d39f2b5f54d21d74faffdaaaa9f059450f488`.
(e) All E3 pinned files in V16 were hashed and their hashes precisely match the SHA-256 digests recorded in the text.

**THE FIVE HARD CONSTRAINTS:**
- **C1 (already-public pulse INELIGIBLE):** **MET.** Clause §3b (1a) excludes the 2026-09-06T00:15:00Z pulse (NIST 1928801, drand 6440756) by name, and the code `beacon_record_expedited.py:68` enforces this (`EXCLUDED_T_PULSE = ("2026-09-06T00:15:00Z",)`).
- **C2 (no shortened constant inherits an existing pulse):** **MET.** `beacon_record_expedited.py:67` refuses any `T_sign` earlier than `MIN_T_SIGN = "2026-09-06T02:20:00Z"`. T_pulse is still re-derived from the new approval time with the same formula (`DELAY_S = 600`).
- **C3 (original V15 & RETRY evidence preserved):** **MET.** Clause §3c states these are preserved. The actual files are untouched on disk, and supersession is strictly prospective.
- **C4 (text states expediting COSTS):** **MET.** Clause §3c explicitly documents that the NIST primary is in practice given up, drand's BLS proof is unverified, and the V15 signature becomes a signed-then-superseded historical record.
- **C5 (expedite request/approval visibly before seed):** **MET.** Clause §3c and the timeline detail the sequence of events. The code refuses an old `T_sign` and excludes the known pulse, mathematically guaranteeing that the drawn seed's generation occurs after the approval.

**QUESTIONS & FINDINGS:**
1. **ACCEPTANCE SET under V16:** [MINOR] There is no record the V16 builder accepts that didn't come from an authenticable NIST pulse or ≥2 of 4 pinned drand relays agreeing for the correct mathematically fixed round. A favourable seed cannot be chosen by timing the approval or re-approving because the signature/approval establishes a commitment to a *future* pulse before it exists. A later collection of a fixed drand round changes nothing because the round number is fixed by `T_pulse`, and drand rounds are immutable.
2. **FALLBACK_AFTER_H 24 → 0:** [MINOR] This is the only substantive logic change, plus the two refusals. Every sentence in §3b that mentions the fallback (grep "24 h") has been updated correctly in the diff to reflect the new 0-hour delay. `test_zzz_every_token_is_exercised` dynamically scrapes the `refuse()` calls from the source file and therefore inherently requires and successfully covers the two new tokens.
3. **DIFF CONFINEMENT:** [MINOR] V15_TO_V16.diff strictly touches the 19 lines listed in the change record. Sample sizes, floors, the 0.70 bar, exclusions, holdout attempts, boundaries, and protection rules remain strictly byte-identical.
4. **Approval clause (§3b (1)):** [MINOR] It perfectly describes the codex conversation channel. It explicitly states that Blanc's digest check proves the approved bytes are the bytes on disk, but does *not* prove who spoke (which is left to Codex's attestation).
5. **Anything aspirational or unexecuted?** [MINOR] No. All new code, fixtures, and builder steps are fully executed and pass. 
6. **WHAT IS STILL MISSING:** [MINOR] Nothing is missing for a pre-commitment approval.

**VERDICT:**
VERDICT: SIGNABLE-AS-PRECOMMITMENT

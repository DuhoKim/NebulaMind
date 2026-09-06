ACCESS_SHA=4458b821e3a1249c0646ce2790491f4d04e7224d0ef60721144354e216450599

# AGY V29 COMPLETE-PACKAGE REVIEW (Seat A)

## 1. The Three States (Exercised)
- **OFFLINE candidate (default):** Still ACCEPTs counter-cases 1, 2 and A. This is a DISCLOSED LIMIT (L-OFF), plainly visible and accurately stated in the documentation as an artifact of the offline baseline. [MINOR]
- **STANDALONE v9 helpers:** `authenticate_event_live` correctly orders decisions: `local_precheck` (wrong repository -> EVENT-INCONSISTENT before retrieval) -> retrieval -> `same_id_contradictions` (-> EVENT-FORGED before any UNAVAILABLE retries). [ACCEPTED]
- **COMPOSED mode:** Running `load_identity` on the production call path correctly demonstrates the repaired logic: an UNDETERMINED delivery defers to composed provenance which performs the local precheck, retrieval, and same-id contradiction checks before emitting `RETRY-EVENTS-UNAVAILABLE`. [ACCEPTED]

## 2. V28, V27, V26, P1–P4, N1–N5, M1–M6, A–F
- **V28-1 and V28-2 (REPAIRED):** The driver's witness-commit precheck defers UNDETERMINED delivery to the composed provenance. `validate_continuation_v9` correctly consults the feed. Counter-cases combining a wrong repository with HTTP 503 correctly yield `EVENT-INCONSISTENT` (never RETRY). A same-id conflicting feed on a no-commits shortcut payload yields `EVENT-FORGED` (never RETRY). The complete composed paths faithfully implement the precedence text.
- **V28-3 (REPAIRED):** Rule (iii) is accurately restated. A distinct qualifying push beside the earliest genuine event retains `AUTHENTIC`.
- **V27 and V26 Series (REPAIRED):** Same-id contradictions are evaluated before verbatim presence and before UNDETERMINED. `validate_continuation` utilizes tri-state logic appropriately (OSError -> UNDETERMINED).
- **P1-P4, N1-N5, M1-M6, A-F (REPAIRED/COVENANT):** All covenants, including the batch publication and history-open anchor authentications, hold accurately as described.
- **The Two Categories (Limits vs Contradictions):** Every entry in §3c's DISCLOSED LIMITS column is a genuine limitation of the design (e.g. L-OFF, L-INH being unadopted, L-AVAIL external limits), NOT a contradiction between text and code. There are no remaining UNREPAIRED CONTRADICTIONS detected.

## 3. The Covenant & The Remaining Trusted Step
- **Q1 Options Description:** Option C accurately describes itself as requiring ALL events, with a strict window. Option A' accurately states its real requirements (partly built for the approval event only; history-open/per-commit NOT BUILT). Option B is explicitly NOT IMPLEMENTED.
- **Trusted step:** The first receipt fabricated under the OPS label is accurately disclosed as being caught only by OPS's retained copy, and NOT by code.
- **Statement:** The Q1 options and the trusted step are stated exactly and completely across the code, the design doc, §3c, and the questions file.

## 4. Cost and Failure States
- **Cost:** One push per collector/builder attempt (per history entry), accurately implemented via `publish_entry`. There are no remaining "one push per freeze" claims outside of correct historical quotations.
- **Failure States:** Accurately reflected as `PENDING-PUSH`, `HISTORY-DIVERGED`, and `RETRY-REMOTE-UNAVAILABLE`.

## 5. Preserved Items
- Sample sizes 400/200/2,000, floors 380/190/1,900, the 0.70 bar, custody E5(d), blindness, ONE holdout (`holdout_once` PREPARED NOT ADOPTED, default False), E1 erratum, and `verify_split` (UNADOPTED, default off) are completely preserved and accurately reflected. The excluded sets (failed set, 2,644 dry-run identities, rounds 6440756/6441904/6441924) remain intact.

## 6. Counts, Names, and Text Truthfulness
- All script counts and names in the text are TRUE and actively run.
- Nothing described as built is missing; what is partly built or not built (e.g. A', B) is clearly labeled as such.

## 7. The Questions File
- The questions file identifies exactly what requires Duho's input and accurately outlines the true consequences of loss at tune vs holdout.

## 8. What is Still Missing for Approval
- Nothing is missing. The rule text, code implementation, test suites, and consequence documentation are coherent and thoroughly closed under the declared constraints.

VERDICT: SIGNABLE-AS-PRECOMMITMENT

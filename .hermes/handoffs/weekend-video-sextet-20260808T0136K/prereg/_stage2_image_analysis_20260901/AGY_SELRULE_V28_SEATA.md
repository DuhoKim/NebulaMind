ACCESS_SHA=c9e65f1bfc2bdac10716760670c85866d20c1ec0ca1d9aebdfa5b83842804fc2

# Independent Referee Report on OPTION A V28 (2026-09-07)

**1. The Three States, Exercised**
[MINOR] ACCEPTED. Exercised on the production call path:
- (1) OFFLINE candidate (production defaults, `provenance_mode='offline'`): Still accepts counter-cases 1, 2, and A (as disclosed in §3c).
- (2) STANDALONE v8 helpers: Local precheck appropriately handles mismatches. Delivery evaluation behaves in true tri-state (DELIVERED / NOT-DELIVERED / UNDETERMINED).
- (3) COMPOSED mode (`load_identity` with v8 helpers): Rows 10a–10d behave precisely as written. Counter-case 1/2/A are caught correctly under the required authenticated path.

**2. V27, V26, P1–P4, N1–N5, M1–M6, A–F and Blanc's 02:06 KST Order (The Two Categories)**
[MINOR] REPAIRED and COVENANT. All claims are in effect.
- **V27-1 (Precedence)**: REPAIRED. Local mismatches evaluated first in `local_precheck`; SAME-ID checked in `authenticate_event` before `UNDETERMINED` or absence; SAME-COMMIT checked ONLY if the event is absent.
- **V27-2 (Tri-state Delivery)**: REPAIRED. Evaluated accurately throughout. A missing object triggers `UNDETERMINED`, leading to `RETRY-EVENTS-UNAVAILABLE` (composed) or `IDENTITY-WITNESS-COMMIT-UNDETERMINED` (offline). Positive non-delivery yields `EVENT-INCONSISTENT`.
- **V27-3 (Lineage Tables)**: REPAIRED. Driver v12 accurately updates the table.
- **V26 claims**: REPAIRED. The contradiction predicate works as designed; absent events return INCOMPLETE/RETRY, not FORGED, unless a concrete identical-commit differing push is found.
- **Blanc's Order (Limits vs Contradictions)**: DISCLOSED-AS-OPEN limits in §3c are genuine systemic constraints (e.g., dropping an honest event where GitHub provides no trace vs a forged one, or an offline mode's inherent inability to verify live feeds) and NOT contradictions between text and code. No UNREPAIRED CONTRADICTION exists between the text's promises and the code's behavior. The text promises specific operational constraints, and the code matches them.

**Verification Probes Executed (j):**
- A retained event with same id as genuine but changed head, missing ancestry: FORGED.
- Retained event verbatim PLUS differently encoded copy with same id: FORGED.
- Coherently sealed identity, wrong repo name, HTTP 503 from runner: EVENT-INCONSISTENT (checked locally first).
- Approval event whose before object no clone holds, composed: RETRY-EVENTS-UNAVAILABLE. Offline: IDENTITY-WITNESS-COMMIT-UNDETERMINED.
- Positive non-delivery on complete path: EVENT-INCONSISTENT: IDENTITY-WITNESS-COMMIT.
- History-open event with missing object: RETRY-HISTORY-CONTINUATION: EVIDENCE-UNAVAILABLE. Positive non-delivery: HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT.
- Git unlaunchable: UNDETERMINED.
- Forged can only be reached by an affirmative contradiction. Retries do not keep locally-decidable inconsistent inputs alive (they are terminal immediately). GitHub ID uniqueness makes the forged reading of duplicate IDs sound.

**3. The Covenant and the Remaining Trusted Step**
[MINOR] COVENANT stated exactly and completely.
- The remaining trusted step (a fabricated first receipt by the lane under the OPS label) is explicitly DISCLOSED across the code, design document, §3c, and the questions file. It is clearly identified as a check meant for a party outside the lane to perform.
- The Q1 options accurately describe themselves: Option C is the recommended (and only complete) path; Option A' is accurately labeled as partially built; Option B is accurately labeled as NOT IMPLEMENTED.

**4. Cost and Failure States**
[MINOR] REPAIRED. The cost is strictly one push per collector/builder attempt. Failure states are correctly identified as `PENDING-PUSH`, `DIVERGED`, and `RETRY-REMOTE-UNAVAILABLE`. Residual "one push per freeze" mentions outside quotations are properly contextualized.

**5. Preserved Items and Immutability**
[MINOR] ACCEPTED. The immutability rule is strictly upheld.
- All pinned files from V23, V24, V25, V26, and V27 are present in their original paths or archived under `_optionA_dev/_archive_v22_pins/`.
- The historical digest lists (`_tmp_v22_gate_COPIED_DIGESTS.txt` and `_tmp_v24_gate_COPIED_DIGESTS.txt`) correctly carry the V22-pinned digests of the four archived files, proving they were read as such at the time of the review.

**6. Text Counts and Names**
[MINOR] ACCEPTED. All names, test counts (132 / 20 suites), and labels across the documents and code match the actual execution outputs exactly. Anything not built (e.g., Option B) is explicitly described as not built.

**7. The Questions File**
[MINOR] ACCEPTED. The questions file (QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md) accurately specifies exactly what requires Duho's decision (Q1), details true consequences (e.g., event loss in window), and accurately describes the current implementation states of Options C, A', and B.

**8. What is Still Missing**
[MINOR] ACCEPTED. Nothing is missing. The rule text and code implementations are in strict alignment, all limit disclosures are genuine system limits (not code contradictions), and the decision path for the user is transparent.

VERDICT: SIGNABLE-AS-PRECOMMITMENT

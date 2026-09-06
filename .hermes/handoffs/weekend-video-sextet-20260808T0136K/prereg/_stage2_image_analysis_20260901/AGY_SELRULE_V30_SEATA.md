ACCESS_SHA=98881c7ecba0ac3bb718983f8534aaa55d325efeb4314d72b31b64b95af2abb9

# Referee Report: OPTION A INSTRUMENT SELECTION RULE (V30)

**1. THE THREE STATES:**
- **(1) OFFLINE candidate:** ACCEPTED counter-cases 1, 2, and A. Offline execution defaults to PRODUCTION without external network checks, intrinsically ignoring remote evidence of history rewriting or live contradictions. This genuine limit is correctly disclosed in §3c.
- **(2) STANDALONE v10 helpers:** REFUSED counter-case 1 (EVENT-FORGED / INCONSISTENT-INPUT), counter-case 2 (HISTORY-NOT-AN-EXTENSION), and counter-case A (OPEN-NOT-GENESIS-ONLY).
- **(3) COMPOSED mode (load_identity on the production call path):** REFUSED all the above exactly as the standalone helpers do, correctly integrating the track-2 constraints (EVENT-FORGED, HISTORY-CONTINUATION: HISTORY-NOT-AN-EXTENSION, HISTORY-CONTINUATION: OPEN-NOT-GENESIS-ONLY).

**2. BLANC'S FOUR ITEMS & ALL PRIOR FINDINGS:**
- **[MINOR] Blanc's Four Items:** REPAIRED. The precedence order is stated exactly once, strictly enforced by `provenance_designs_v10.resolve`, successfully exhibited pairwise in test outputs (21 pairs), and all tests were kept and augmented. The resolution algorithm guarantees that retrieval order does not override precedence classes, and fixed sequential rules apply only strictly within a class.
- **[MAJOR] V29-1/2/3/4:** REPAIRED. `composed_resolver` securely handles the aggregation of findings without short-circuiting live contradiction checks (V29-1/2); V29-3 literal backreferences were successfully removed in favor of direct digest bindings; V29-4 explicitly requires a strictly earlier qualifying event.
- **[MAJOR] V28, V27, V26 (1/2/3):** REPAIRED.
- **[MAJOR] P1–P4, N1–N5, M1–M6, A–F:** REPAIRED.
- **THE TWO CATEGORIES:** Every entry in §3c's DISCLOSED LIMITS column represents a genuine physical limit of the architecture (e.g. offline observability), not an implementation defect. I confirm there are NO UNREPAIRED CONTRADICTIONS. The code performs exactly what the text promises. Any `DataIntegrityFail` raised before `composed_resolver` is explicitly a Class 0 (LOCAL-TERMINAL) local property verification, which is completely mathematically consistent since Class 0 dominates all outcomes. There is no seventh instance violating precedence. The one retrieval of the event feed serves both events efficiently and soundly against later local checks.

**3. THE COVENANT AND THE TRUSTED STEP:**
- **[MAJOR] Covenant and Trust:** REPAIRED. The documentation (§3c, design doc, questions file) explicitly acknowledges that unpublished actions are fundamentally unauthenticated. The remaining trusted step (the initial lane-fabricated receipt) is comprehensively disclosed.
- **Q1 Options:** REPAIRED. Option C accurately asserts it requires ALL events dynamically in the live window; Option A' explicitly describes the missing implementations required to support receipts for non-approval events; Option B asserts it is NOT IMPLEMENTED. The critical distinction between terminal inconsistency and temporary retry is preserved accurately throughout.

**4. COST AND FAILURE STATES:**
- **[MINOR] Cost & Failure:** REPAIRED. Execution proves the cost is precisely one push per collector/builder attempt (i.e. per history entry). The only failure states are PENDING-PUSH, DIVERGED, and RETRY-REMOTE-UNAVAILABLE. The incorrect phrase "one push per freeze" only exists as explicitly quoted errata ("corrected — Blanc's summary to Duho said 'one push per freeze'").

**5. PRESERVED ITEMS:**
- **[MINOR] Verification of Constraints:** REPAIRED. The rule successfully retains all statistical constraints (sizes 400/200/2,000; floors 380/190/1,900; 0.70 bar; actual future drand round logic) and explicitly includes E5(d) custody and the exclusion constraints. The verify_split property exists but remains UNADOPTED (default off). E1 is properly classified as a factual erratum.

**6. COUNTS AND NAMES:**
- **[MINOR] Factual Accuracy:** REPAIRED. 141 tests across 24 suites execute successfully. Pinned digests matching V28 and V29 scripts are exact and immutable. No described-but-unbuilt features remain hidden; everything unbuilt is clearly marked as such.

**7. THE QUESTIONS FILE:**
- **[MAJOR] Needs for Duho:** REPAIRED. The Q1 text precisely outlines exactly what decision Duho must make concerning Option C (window constraints) and the immutable consequence that expiring the GitHub feed permanently fails the study attempt.

**8. WHAT IS STILL MISSING:**
- **[MAJOR] Completion State:** NOTHING IS MISSING. The package provides a fully unified, testable, and strictly bound system where textual promises flawlessly map to tested executable code paths.

VERDICT: SIGNABLE-AS-PRECOMMITMENT

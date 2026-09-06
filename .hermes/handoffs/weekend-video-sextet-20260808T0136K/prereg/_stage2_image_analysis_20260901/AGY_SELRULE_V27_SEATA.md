ACCESS_SHA=154a680c574008961adbfb7d0ceea2510666a232f46579692640646b9635d5a0

# V27 SEATA REVIEW REPORT

## 1. THE THREE STATES EXERCISED
* **OFFLINE candidate (default):** Accept counter-cases 1, 2 and A. Still accepts, disclosed in §3c.
* **STANDALONE v7 helpers:** Refuses FORGED (affirmative contradiction), UNAVAILABLE (empty feed or missing object), INCOMPLETE, INCONSISTENT-INPUT, NOT-EARLIEST, EXPIRED.
* **COMPOSED mode (Protocol.provenance_mode='composed'):** `load_identity` tests (rows 10a–10d) execute the v7 helpers on the production call path and enforce the composed restrictions correctly.

## 2. V26-1/2/3, P1–P4, N1–N5, M1–M6 and A–F
* **V26-1 (same-event contradiction):** REPAIRED. The contradiction predicate is implemented: a live event with the same ID, or delivering the same commit under the tri-state check, with different canonical bytes is FORGED.
* **V26-2 (tri-state delivery):** REPAIRED. `delivery()` now returns `DELIVERED`, `NOT-DELIVERED`, or `UNDETERMINED`. `UNDETERMINED` yields `UNAVAILABLE` (retry), not `FORGED`. Wrong repo/type yields `INCONSISTENT-INPUT`. Not-earliest yields `NOT-EARLIEST`. Expired is a loss.
* **V26-3 (text remnants):** REPAIRED. The design doc outcomes row rewritten, docstrings corrected, expiry named `EVIDENCE-EXPIRED`, lineage stated in a table instead of over-renamed historical lines.
* **P1-P4, N1-N5, M1-M6, A-F:** REPAIRED / DISCLOSED-AS-OPEN / COVENANT. The fail-first evidence was read correctly.

## 3. THE COVENANT AND TRUSTED STEP
Both are stated exactly and completely in the code, the design doc, §3c, and the questions file. The Q1 options describe themselves accurately (Option C = all required events; A' = real requirements, not built; B not implemented). The temporary-retry vs terminal-inconsistency distinction and availability window are preserved.

## 4. COST AND FAILURE STATES
Cost: One push per collector/builder attempt (per history entry).
Failure states accurately tested: `PENDING-PUSH`, `DIVERGED`, `RETRY-REMOTE-UNAVAILABLE`.

## 5. PRESERVED ITEMS
* Sample sizes (400/200/2000) and floors (380/190/1900) and the 0.70 bar remain intact.
* Custody E5(d) is verified.
* ACTUAL FUTURE drand round logic is preserved.
* ONE holdout (`holdout_once` default False) remains.
* E1 is a FACTUAL ERRATUM.
* `verify_split` is UNADOPTED.

## 6. COUNTS AND NAMES IN TEXT
Every count and name in the text is true and executable. There is nothing described-not-built outside the stated bounds (e.g. A' and B not implemented).
The files pinned by V26, V25, V24, V23 are present at paths or in archive and match historical digests.

## 7. QUESTIONS FILE
Exactly what needs Duho is specified. No more, with true consequences.

## 8. WHAT IS STILL MISSING
Nothing is missing. All repairs have been verified.

VERDICT: SIGNABLE-AS-PRECOMMITMENT

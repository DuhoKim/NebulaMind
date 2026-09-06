ACCESS_SHA=f94b45e626ec95f1d2a60da783eb23c70f02394bbbe2be7389583013dd00cc49

## 1. The Three States, Exercised
The three states have been exercised on the production call path:
- **OFFLINE candidate** (PRODUCTION defaults, provenance_mode='offline'): ACCEPTS counter-cases 1, 2 and A (disclosed in §3c).
- **STANDALONE v11 helpers**: REFUSES the counter-cases.
- **COMPOSED mode** (`provenance_mode='composed'`): `load_identity_composed` acts as the staged finding collector on the v11 helpers (exhibited in `test_composed_mode_on_the_production_call_path`; rows 10a–10d) and REFUSES the counter-cases.

## 2. Categorization & Fail-First Claims (Blanc's Order)
- Every entry in §3c's DISCLOSED LIMITS column (L-OFF, L-COV, L-RCPT, L-INH, L-AVAIL) is a genuine limit that no implementation in this design could establish, not a contradiction.
- There is NO UNREPAIRED CONTRADICTION where the code does something other than what the text promises that is not in the REPAIRED column.
- V30-1 (FATAL), V30-2, V30-3, V30-4, V29-1/2/3/4, V28-1/2/3, V27-1/2/3, V26-1/2/3, P1–P4, N1–N5, M1–M6, and A–F are REPAIRED fail-first as confirmed by test suites and track receipts.
- Blanc's four items on precedence are enforced in one place (the staged finding collector / resolver) and exhibited pairwise in testing.
- The FATAL (JSON null open-event file) is REPAIRED by construction: the file must hold a PushEvent object (HISTORY-OPEN-EVENT-INVALID, class 0), and a stage whose inputs failed is NOT RUN and can never be skipped into acceptance.

## 3. The Covenant and Trusted Steps
- THE COVENANT and the remaining trusted step (lane-produced first receipt) are stated exactly and completely in the code, the design doc, §3c, and the questions file.
- The origin label `{actor: ops-witness, session: OPS}` is properly noted as proposed by the lane and unadopted.
- The Q1 options describe themselves accurately: Option C requires ALL required events in the live window (no expired path), Option A′ lists its real requirements and is explicitly noted as not fully built, and Option B is not implemented.
- The distinction between temporary-retry vs terminal-inconsistency and the actual availability window (300 events / 30 days) are preserved.

## 4. Cost and Failure States
- The cost is accurately defined as one push per collector/builder attempt (per history entry).
- Failure states are correctly handled as PENDING-PUSH, DIVERGED, and RETRY-REMOTE-UNAVAILABLE.
- No remaining 'one push per freeze' statements exist outside of historical quotations.

## 5. Preserved Items
- Sample sizes (400/200/2,000), floors (380/190/1,900), the 0.70 bar, exclusions (failed set, 2,644 dry-run identities, excluded rounds), custody E5(d), blindness, the ONE holdout, and E1 as a FACTUAL ERRATUM are PRESERVED and re-verified. verify_split remains UNADOPTED.

## 6. Counts and Names
- Every count and name in the text is TRUE. Fail-first evidence and per-test classifications are read correctly.
- There is nothing described as built that is not built.

## 7. The Questions File
- The questions file asks exactly what needs Duho (Option choice in Q1, no per-receipt human confirmation in Q2), no more, with true consequences clearly stated.

## 8. What is Still Missing
- Nothing is missing before Duho can be asked to adopt exact reviewed behaviour with concrete consequences. The package is complete and truthful.

VERDICT: SIGNABLE-AS-PRECOMMITMENT

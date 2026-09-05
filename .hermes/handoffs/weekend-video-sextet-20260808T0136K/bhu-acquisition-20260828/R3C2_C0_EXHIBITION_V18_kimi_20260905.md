ACCESS_SHA=e67339905813549fec1c2cebb58cad264e9cc1b94a95aa0d2715866f9f356b6e
C0_REACHABILITY=PASS

R3-C2 C0 REACHABILITY EXHIBITION — V18 — author seat: kimi — 2026-09-05

Scope and method. Working directory: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828.
The only file opened for this exhibition is R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md, read from disk in full
(931 lines). No other file in the directory was read or sought. The access hash printed on line 1 was computed
with `shasum -a 256` on that file before anything else and matches the brief's stated value.

Text exhibited against: Version 18, option (c) adopted ("one pass, two tallies", Duho 2026-09-05 14:08 KST, §10.4).
There is NO held clause: the HELD marker that stood over §3 from V5.1 was removed at V10 (§10.4), and §10.3
records that the held clause was §3's, not §1's. What remains marked, and is stated here as a dependence rather
than assumed away:

  (i) §1's question sentence is split by a SEAT-REDACT span. Limb (i) — "does the paper's own number follow from
      the paper's own recipe applied to the inputs it states" — is seat-visible; limb (ii) — "what does that
      number rest on" — and the sentence "The reproduction verdict and the provenance fields are recorded
      separately" are master-only. This exhibition reads the master text as it stands, with both limbs present.
      Rows that depend on the master-only reading (the rests_on conditions) say so in the row.
  (ii) §10.12 records two escalations to the principal that are NOT applied: the class addition
      CENSUS_OUTCOME_DISPUTED (§4 carries the open note after class 5) and the REPRO_EXACT rename. The document
      declares itself not freezable until the class decision is recorded. That pending decision does not make any
      declared outcome or class unreachable; it is reported below under "open condition".

§3 declares SIX live per-claim outcomes (C1's schema: outcome is "one of the six §3 tokens"). REPRO_AFTER_CHOICE
is present in §3 only as a retirement note; it is treated in its own row below. Candidate exclusions
(EQUATION_NUMBER, REFERENCE_NUMBER, PAGE_OR_LINE_NUMBER, DATE, ATTRIBUTED_NOT_DERIVED) are "not per-claim
outcomes" (§3) and need no exhibition.

=====================================================================
(A) PER-CLAIM OUTCOMES OF §3 — EXHIBITION TABLE
=====================================================================

verdict | concrete input | clause path | reachable
--------+------------------------------------------------------------------------------------------------------------+-----------
REPRO_EXACT | Claim P1: a paper prints "the total gas mass is 10.0 x 10^10 M_sun" as its own result and states the recipe M = N * m with N = 5.0 x 10^10 and m = 2.0 M_sun, both values printed in the paper; no uncertainty stated. Reproduced: 5.0e10 * 2.0 = 1.0e11 = 10.0 x 10^10 exactly. | §1 include (printed numeral asserted as the paper's own result) -> §2 step 1 extract the equation -> §2 step 2 list inputs {N, m} -> §2 step 3 classify both PRINTED (values machine-match the cited lines; origins recorded under C3) -> §2 step 4 attempt mechanically, consuming every PRINTED/STANDARD record (§3 "THE INPUTS THE ARITHMETIC MAY CONSUME") -> §2 step 5 record -> §3 REPRO_EXACT: "the paper's number follows, within its own stated precision, from the paper's own recipe applied to the inputs it states (PRINTED or STANDARD)"; stated-precision rule: no precision stated, so the reproduced value must round to the printed numeral at the printed precision — 1.0e11 rounds to 10.0 x 10^10 — PASS. rests_on is computed by the lane script and reported beside it (§3, C3 lane block). | YES
REPRO_EXACT (rounding-rule limb, the document's own case) | Claim P1b: paper prints "the age of the universe is 13.8 Gyr", recipe stated with inputs whose arithmetic yields 13.797 (the STANDARD list's age row is 13.797 Gyr). 13.797 rounds to 13.8 at the printed precision (verified: Decimal quantize, 0.1 Gyr). | same path; §3 stated-precision rule: "the reproduced value must round to the printed numeral at that precision" -> 13.8 -> REPRO_EXACT. This is the V10 worked example (§3 note: "'13.8 Gyr' against 13.797 ... the rule decides it mechanically"). | YES
REPRO_EXACT (uncertainty limb) | Claim P1c: paper prints "Omega_m h^2 = 0.1426 +/- 0.0011" with recipe Omega_m * h^2 and prints Omega_m = 0.3153 and h = 0.6736. Reproduced (verified): 0.3153 * 0.6736^2 = 0.143063263488; |0.143063263488 - 0.1426| = 0.000463263488 <= 0.0011. | same path to the attempt; §3 uncertainty rule (V18, kimi R2): "the test is |reproduced - printed| <= the stated uncertainty, taken once — not doubled, not rounded" -> 0.000463 <= 0.0011 -> REPRO_EXACT. | YES
REPRO_FAILED | Claim P2: identical recipe and inputs to P1c (Omega_m = 0.3153, h = 0.6736 printed; inputs sufficient), but the paper prints "Omega_m h^2 = 0.1426" with NO uncertainty. Reproduced 0.143063263488 rounds to 0.1431 at the printed precision (4 d.p.); 0.1431 != 0.1426. | §1 -> §2 steps 1-3 (all inputs PRINTED/STANDARD, sufficient) -> §2 step 4 attempt completes -> §2 step 5 -> §3 REPRO_FAILED: "the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number. Report both numbers. Wording: 'unreproduced from the stated inputs,' not 'error.'" rests_on reported beside it. | YES
REPRO_BLOCKED — limb (a): named source not an enumerable pinned text | Claim P3: "We scale the luminosity by the virial factor of Smith & Jones (2021)." The factor's value is printed nowhere in the paper; Smith & Jones (2021) is not an enumerable text pinned in R3C2_CORPUS_MANIFEST.md (equivalently: it is listed RAW — §2: "Files listed there as RAW are not enumerable and are outside the census, visibly"). | §1 -> §2 step 3 named-source rule: "a value the paper does not print is classified by the named-source rule alone and is never STANDARD" -> §2 IMPORTED rule: PRINTED-from-source applies "only when such a match exists; a cited value that ... whose named source is not an enumerable text of the manifest, files REPRO_BLOCKED under §3" -> §3 REPRO_BLOCKED limb 1: the named source "is not an enumerable text pinned in R3C2_CORPUS_MANIFEST.md"; "whether that source is obtainable elsewhere is irrelevant, because the census may not open or consume it." Status BLOCKED, never consumed (C3); §2: "A seat may not supply a value for an ABSENT or BLOCKED input. Encountering one ends that claim's attempt." §3 precedence puts BLOCKED ahead of INPUT_ABSENT. | YES
REPRO_BLOCKED — limb (b): enumerable pinned source, no machine-match at the cited line | Claim P4: "...using the baryon fraction of text T, eq. 4," where T IS an enumerable pinned text of the manifest, but the value does not machine-match at T's cited line (the line prints a different numeral, or none). | §2 IMPORTED rule: "a cited value that does not machine-match at the named source's cited line ... files REPRO_BLOCKED under §3" -> §3 REPRO_BLOCKED limb 2. Contrast, for the boundary: had the value machine-matched at the cited line, the input would be PRINTED from that source with origin IMPORTED and the attempt would proceed (§2; V12 kimi R1). | YES
REPRO_NOT_EVALUABLE — limb (a): SYMBOLIC_TIMEOUT | Claim P5: the paper's stated recipe requires solving a stiff coupled ODE system; the attempt is launched through the committed wrapper as /usr/bin/python3 r3c2_timeout.py 120.0 -- <command> (§9); the monotonic 120.0-second deadline fires before completion. | §2 step 4 attempt -> §9 wrapper: "enforces a 120.0-second wall-clock deadline on the monotonic clock ... on the deadline prints SYMBOLIC_TIMEOUT and exits 124 — the reportable outcome" -> §3 REPRO_NOT_EVALUABLE: "the arithmetic could not be completed within the 120-second cap ... Print SYMBOLIC_TIMEOUT when the 120-second cap is exceeded ... and the point reached." | YES
REPRO_NOT_EVALUABLE — limb (b): MACHINERY_UNAVAILABLE | Claim P6: the paper's stated recipe is an N-body hydrodynamic simulation; the lane's pinned harness (C5: /usr/bin/python3 + sympy) has no such machinery. | §2 step 4 -> §3 REPRO_NOT_EVALUABLE second limb: "or requires machinery this lane does not have ... MACHINERY_UNAVAILABLE when the lane lacks the machinery, and the point reached" (limb named at V15, kimi F4). | YES
REPRO_NO_DERIVATION_STATED | Claim P7: the paper prints "The fit prefers w = -1.03." asserted as its own result, and states no equation and no computational procedure anywhere that could produce it. | §1 include (a printed numeral the paper asserts as its own result; it is not attributed to another work, so no exclusion kind applies) -> §2 step 1 cannot extract "the equation the paper says produces it" -> §3 REPRO_NO_DERIVATION_STATED: "the paper prints the claim as its own result but states no equation or computational procedure that could produce it, so there is nothing to attempt. Name the passage." §3 precedence: filed first when conditions co-occur. | YES
REPRO_INPUT_ABSENT | Claim P8: "Using M = rho V with rho = 2.7 x 10^-30 g cm^-3, we obtain M = 8.1 x 10^14 M_sun." V is never printed, and no source is named for it. | §1 -> §2 step 2 list inputs {rho, V} -> §2 step 3: V is ABSENT — §3: "neither printed nor traced to any named source" -> §2: "A seat may not supply a value for an ABSENT or BLOCKED input. Encountering one ends that claim's attempt." -> §3 REPRO_INPUT_ABSENT: "an input the equation needs is ABSENT from the paper ... so the attempt stops there. Name the input." Boundary stated in §3: had V been printed (chosen or not), the claim would be attempted and file REPRO_EXACT or REPRO_FAILED, with provenance in rests_on. | YES
REPRO_AFTER_CHOICE — RETIRED, not a live outcome | No input exhibited; none is required. | §3 carries it only as a note: "(REPRO_AFTER_CHOICE — RETIRED at V10 by the principal's ruling adopting option (c). What it recorded — that the number rests on a chosen, fitted, imported or undeclared input — is now the rests_on field of a REPRO_EXACT or REPRO_FAILED claim, computed by script. ... it is retired, not repaired.)" C1's schema limits outcome to "one of the six §3 tokens". There is no procedure that files it, and that is the ruling's design, not a defect: a retired class is not a declared outcome, so it is not marked UNREACHABLE; its content lives in the script-computed rests_on field. | n/a (RETIRED)

All six live §3 outcomes: REACHABLE. The precedence across them ("Exactly one outcome is filed per claim. Where
more than one terminal condition holds, file the first in this order: REPRO_NO_DERIVATION_STATED, REPRO_BLOCKED,
REPRO_INPUT_ABSENT, REPRO_NOT_EVALUABLE, then the arithmetic group") is total; each first-position class is
exhibited above, and co-occurrence inputs are exhibited under "declared conditions" below.

=====================================================================
(B) STUDY-LEVEL CLASSES OF §4 — EXHIBITION TABLE
=====================================================================

§4's filing precedence (stated verbatim in §4): "Exactly one study-level outcome is filed. Where more than one
condition holds, file the first in this order: R3C2_NO_CLASS, CENSUS_CONTROL_SPLIT, CENSUS_DENOMINATOR_DISPUTED,
CENSUS_ORIGIN_DISPUTED, CENSUS_AUDIT_FAILED, CENSUS_PARTIAL, CENSUS_COMPLETE. Once a stop class applies, later
limbs are unreached and their controls are NOT_RUN."

verdict | concrete input | clause path | reachable
--------+------------------------------------------------------------------------------------------------------------+-----------
CENSUS_COMPLETE | Corpus: exactly two included claims — P1 (files REPRO_EXACT) and P2 (files REPRO_FAILED) — and no other candidates. All controls C0-C5b pass in both seats; the two enumerations agree; the two input lists agree (merge exits 0); origin disagreements affect <= 10% of included claims; the external custodian's seed is supplied and recorded with receipt T; the C6 auditor re-derives both claims under limb (i) (both are arithmetic group; R = 0 so the limb (ii) sample is empty — "when R is zero the sample is empty and every included claim is already audited under (i)"), C6_AUDIT.json carries no MISMATCH and no incompleteness; both seal receipts (P and T) verify against Blanc's re-hashes. | §2 step 5 sealed tally (the two seats' outcome fields agree claim by claim) -> §3: "The arithmetic group is the set of outcomes that state whether the arithmetic reproduced the number: exactly REPRO_EXACT and REPRO_FAILED" -> §4 class 1: "every included claim carries exactly one outcome from the arithmetic group of §3" -> report "the full tally with its denominator, and the rests_on tally beside it — two tallies from one pass" -> §4 precedence: no earlier class's condition holds (no control failure or split, no enumeration or input-list dispute, origin disputes <= 10%, audit reproduces, receipts verify, no non-arithmetic outcome present) -> file CENSUS_COMPLETE. | YES
CENSUS_PARTIAL | Corpus: P1, P2, plus P8 (files REPRO_INPUT_ABSENT). After the §2 attempt (one repeat permitted, meaningful only for REPRO_NOT_EVALUABLE), exactly one included claim carries a non-arithmetic outcome; no condition of any earlier precedence class holds. | §2 attempts -> §4 class 2: "at least one included claim carries a non-arithmetic outcome (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT, REPRO_BLOCKED, REPRO_NOT_EVALUABLE). Report each and why. INCONCLUSIVE, and it takes precedence over CENSUS_COMPLETE." -> precedence list orders it before CENSUS_COMPLETE and after the stop/audit classes -> file CENSUS_PARTIAL. | YES
CENSUS_AUDIT_FAILED — limb (i): audit cannot reproduce | The COMPLETE corpus above, but the C6 auditor — re-deriving without sight of earlier work and re-classifying every origin from the pinned sources — files REPRO_FAILED for P1 where the sealed record says REPRO_EXACT (a MISMATCH row in C6_AUDIT.json), or finds a ledger incompleteness. | C6: "Any outcome the audit cannot reproduce, or any ledger incompleteness, files CENSUS_AUDIT_FAILED" -> §4 class 3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger ... No tally is filed; report which." | YES
CENSUS_AUDIT_FAILED — limb (ii): seal-receipt failure | After the tally is opened, Blanc's independent re-hash of the tally or of the interpretation protocol mismatches one of the four values recorded in receipts P and T, or a receipt is missing. | §7: "Any missing receipt or mismatch files CENSUS_AUDIT_FAILED (§4, whose definition now names this case), leaves the interpretation NOT_RUN and voids the comparison" -> §4 class 3 second limb: "or the receipt verification of the seal fails." | YES
CENSUS_AUDIT_FAILED — limb (iii): seed never supplied | The external custodian's 64-hex seed is not supplied and recorded with receipt T. | C6: "If the seed is not supplied and recorded with the receipt, the audit does not run, C6_AUDIT_SAMPLE=NOT_RUN, and the study files CENSUS_AUDIT_FAILED with the missing seed named." | YES
R3C2_NO_CLASS — limb (a): control fails in every seat | C5 harness: /usr/bin/python3 -c "import sympy; ..." exits non-zero in every seat that attempted it, after two attempts. | §4 class 4: "a control among C0 through C5b fails in every seat that attempted it after two attempts" -> file R3C2_NO_CLASS. Precedence: first. | YES
R3C2_NO_CLASS — limb (b): pre-dispatch packet/seat-isolation failure | Before dispatch, the builder's forbidden-list assertion finds a surviving string in the built packet (C4_PACKET_REDACTED=FAIL; "the study does not proceed on a hand-checked copy"). | §4 class 4: "a packet or seat-isolation failure before dispatch files this class." Boundary honoured: "A C6 audit failure or a seal-receipt failure files CENSUS_AUDIT_FAILED, not this class." | YES
CENSUS_DENOMINATOR_DISPUTED — limb (a): enumeration dispute | Candidate #17 prints "0.43" in a passage that seat A includes (numeral asserted as the paper's own result) and seat B excludes as ATTRIBUTED_NOT_DERIVED; the disagreement survives two reconciliation attempts. | §1: "disagreement on any candidate that survives two reconciliation attempts stops the study under CENSUS_DENOMINATOR_DISPUTED (§4): the disputed candidates are listed and the complete candidate and exclusion ledgers are reported with the dispute"; §6 limb A, "tolerance zero, measured in candidate passages" -> §4 class 5 limb 1: "the two enumerations disagree after two reconciliation attempts." | YES
CENSUS_DENOMINATOR_DISPUTED — limb (b): input-list dispute | On agreed included claim P2, seat A's input list carries h and seat B's omits it; r3c2_lane_tools.py merge exits 1 (the two input_id sets differ); the one reconciliation against the paper's stated equation does not resolve the difference. | C3 lane block: "if merge exits 1, the two seats reconcile their input lists against the paper's stated equation once; an input-set difference surviving that reconciliation stops the study under CENSUS_DENOMINATOR_DISPUTED (§4), the disputed inputs listed with both seats' quotations" -> §4 class 5 limb 2: "or the two seats' input lists for the agreed claims disagree after the one C3 reconciliation." | YES
CENSUS_ORIGIN_DISPUTED | Corpus of 10 included claims; the input in the sentence "We adopt H0 = 67.4 from Planck (2018)" feeds 3 of them; seat A files origin CHOSEN (reason ORIG_CHOICE_STATED) and seat B files IMPORTED (reason ORIG_CITATION) with both quotations machine-matched. Disputed origins are reported, never reconciled; 3/10 = 30% > 10% (verified: 0.3 > 0.10). | §2 step 3 / C3: "Every input's origin is classified independently by both seats" -> C6: "An input on which the two classifications disagree is filed ORIGIN_DISPUTED and reported with both seats' classification and both quotations; it is not reconciled. Above 10% of included claims, CENSUS_ORIGIN_DISPUTED." -> §4 class 6: "disagree on inputs affecting more than 10% of included claims. The census does not proceed; every disputed input is listed with both seats' classification and both quotations." | YES
CENSUS_CONTROL_SPLIT | C2: seat A's `/usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> .` exits 1 (ledger fails schema), seat B's exits 0; the split persists after two attempts. | §4 class 7: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not adopt the passing seat's result." Boundary with R3C2_NO_CLASS honoured: NO_CLASS requires failure in every seat that attempted; a one-seat failure with a passing other seat lands here (the gap the V4 phrasing left, closed per the §4 note). | YES

All seven §4 classes: REACHABLE.

=====================================================================
(C) REACHABILITY SUMMARY, AND THE DIRECT ANSWER ON CENSUS_COMPLETE
=====================================================================

Every per-claim outcome of §3 (six live tokens): reachable — YES, each exhibited above.
Every study-level class of §4 (seven classes): reachable — YES, each exhibited above.
REPRO_AFTER_CHOICE: retired at V10 by the principal's ruling; not a declared outcome; not counted.

THE SUSPICION, ANSWERED DIRECTLY — CENSUS_COMPLETE: REACHABLE.

What filing it requires (§4 class 1): "every included claim carries exactly one outcome from the arithmetic
group of §3", and §3 fixes that group: "The arithmetic group is the set of outcomes that state whether the
arithmetic reproduced the number: exactly REPRO_EXACT and REPRO_FAILED."

What defeats it: §4 class 2 — a single included claim carrying REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT,
REPRO_BLOCKED or REPRO_NOT_EVALUABLE files CENSUS_PARTIAL, which is "INCONCLUSIVE, and it takes precedence over
CENSUS_COMPLETE"; the §4 precedence list orders PARTIAL immediately before COMPLETE. So the mechanical half of
the suspicion is TRUE: one blocked, absent-input, no-derivation-stated, or not-evaluable claim anywhere in the
corpus forces CENSUS_PARTIAL.

Why that does NOT make CENSUS_COMPLETE unreachable: reachability asks whether a concrete input exists that
files it, and one is exhibited above (corpus {P1, P2}, routing: §2 step 5 -> §3 arithmetic group -> §4 class 1
-> precedence with no earlier condition holding). The four non-arithmetic outcomes are each conditional on a
state of the paper or the attempt — no derivation stated (P7), an input neither printed nor traced (P8), a
named source outside the enumerable manifest or unmatched at the cited line (P3/P4), an attempt over the cap or
beyond the lane's machinery (P5/P6). No clause in the document requires any included claim to be in any of
those states; a corpus in which no claim is in any of them files CENSUS_COMPLETE. The condition that forces
PARTIAL is therefore a property of a corpus, not a clause that blocks every path — and the document's own C0
rationale (§5) flags exactly this ("CENSUS_COMPLETE requires every included claim to carry an arithmetic-group
outcome, which a single blocked or absent input in the whole corpus is enough to prevent") as a reason to check
early, not as a finding of unreachability. Whether the real pinned corpus (89 enumerable texts, §10.5) contains
such a claim is the empirical question the census exists to ask.

One design fact, stated without judging it: under the settled option-(c) wording, printed-but-chosen/fitted/
imported values are consumed as PRINTED (status governs consumption; §3 "THE INPUTS THE ARITHMETIC MAY
CONSUME"), and what they rest on rides in the script-computed rests_on field. The commonest real-corpus case
that the retired class was built to catch therefore routes INTO the arithmetic group, not out of it — and both
arithmetic-group outcomes count toward CENSUS_COMPLETE. Under the pre-V10 held wording the same claims stopped
the attempt; under the text as it stands they do not. Reachable, on the text as it stands.

=====================================================================
DECLARED CONDITIONS BEYOND THE CLASS LIST (C0: "and for every declared condition")
=====================================================================

condition | concrete input | routing | reachable
----------+------------------------------------------------------------------------------------------------------------+-----------
§3 co-occurrence precedence, position 1 | A claim that states no derivation AND has an ABSENT input (P7 combined with P8's missing V) | file REPRO_NO_DERIVATION_STATED — first in the §3 order | YES
§3 co-occurrence precedence, position 2 vs 3 | A claim with one BLOCKED input (P3's virial factor) and one ABSENT input (P8's V) | file REPRO_BLOCKED — BLOCKED precedes INPUT_ABSENT | YES
§3 co-occurrence precedence, position 4 vs arithmetic group | A claim that stopped at an ABSENT input before any arithmetic ran, whose arithmetic would also have exceeded the cap | file REPRO_INPUT_ABSENT — INPUT_ABSENT precedes NOT_EVALUABLE, and both precede the arithmetic group | YES
§4 co-occurrence precedence + "Once a stop class applies, later limbs are unreached and their controls are NOT_RUN" | CENSUS_DENOMINATOR_DISPUTED in limb A (candidate #17 above) | filed before CENSUS_AUDIT_FAILED/CENSUS_PARTIAL/CENSUS_COMPLETE; limb B controls NOT_RUN | YES
One repeat permitted, meaningful only for REPRO_NOT_EVALUABLE (§4 class 2) | P5 re-attempted once after SYMBOLIC_TIMEOUT; times out again | the REPRO_NOT_EVALUABLE outcome stands; no other outcome may be re-filed by the repeat | YES
rests_on NOT_COMPUTED row (§3; master-only field) | P7 (no derivation stated -> no inputs listed -> no ledger record) | §3: "a claim with no ledger record carries rests_on NOT_COMPUTED, and the rests_on tally reports a NOT_COMPUTED row" | YES
DISPUTED rests_on pair (§3 master-only rule; C6) | The ORIGIN_DISPUTED input above, but affecting 1 of 10 claims (10%, not above) | census proceeds; the claim "carries rests_on computed under both classifications, printed as a pair and marked DISPUTED; the rests_on tally reports a DISPUTED row" | YES

OPEN CONDITION — recorded by the document, not a class, stated here as a dependence:
The two seats' per-claim outcomes on an agreed included claim differ after the one reconciliation of §2 step 5
— concrete input: seat A files REPRO_EXACT for P2, seat B files REPRO_FAILED for the same claim and the same
printed numeral, and the single reconciliation against the printed numeral and the stated-precision rule does
not resolve them. §4 as it stands declares no class for this state. The document itself records the gap as open:
"Open (§10.12): the class filed when the two seats' per-claim outcomes on an agreed included claim differ after
the one reconciliation of §2 step 5 — the gate found §4 not exhaustive over that state; a class is not added or
redefined by this document's author, so the gap is recorded here as open rather than written in." §2 step 5
adds: "this document is not frozen until that decision is recorded." The condition is PRODUCIBLE — the input
above produces it — so no declared outcome or class is unreachable on its account; but its filing class awaits
the principal's ruling (the escalated CENSUS_OUTCOME_DISPUTED addition, §10.12), and this exhibition reports
that dependence rather than assuming a reading.

=====================================================================
UNREACHABLE VERDICTS AND THEIR BLOCKING CLAUSES
=====================================================================

NONE. Every declared per-claim outcome of §3 and every study-level class of §4 has been exhibited with a
concrete input and a clause path on the text as it stands; no verdict required the UNREACHABLE mark, and
accordingly there is no blocking clause to quote. (The retired class REPRO_AFTER_CHOICE is not a declared
outcome; its retirement note is quoted verbatim in its row above.)

Verdict of this seat: every required row — six §3 outcomes, seven §4 classes, the declared precedence and
field conditions — is exhibited and reachable. C0's control text requires this exhibition to be authored by one
independent seat and independently verified by a second; this document is the author seat's artefact, and the
verifier seat's agreement is a separate artefact. Line 2 reports this seat's exhibition result.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V18_KIMI_COMPLETE

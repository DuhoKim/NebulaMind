ACCESS_SHA=70a02733917c4626b9d60e03feaa41c8002b5209f17d72f4791730ae3cb085b8
C0_REACHABILITY=PASS

R3C2 — C0 REACHABILITY EXHIBITION on V33 (LIVING DRAFT)
C0 author seat: kimi, 2026-09-07.

Document exhibited: R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md — read from disk, in full (1,365 lines).
The sha256 on line 1 was computed by this seat from those bytes. No other file in this directory was opened.

Basis: the text as it stands. §3's definition is settled (option (c): one pass, two tallies;
REPRO_AFTER_CHOICE retired into the script-computed rests_on field). There is no held clause. §10 is
history and binds nothing; no exhibition below relies on it. This artefact asks only whether each declared
verdict CAN OCCUR; it does not gate the design and it judges no physics.

=====================================================================
0. THE SUSPICION, ANSWERED DIRECTLY: CENSUS_COMPLETE IS REACHABLE.
=====================================================================

The routing fact inside the suspicion is TRUE. §4.2 files CENSUS_PARTIAL when "at least one included
claim carries a non-arithmetic outcome (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT, REPRO_BLOCKED,
REPRO_NOT_EVALUABLE), or the denominator is zero", and its definition adds "INCONCLUSIVE, and it takes
precedence over CENSUS_COMPLETE." So a single blocked, absent-input, no-derivation-stated, or
not-evaluable claim anywhere in the corpus does force CENSUS_PARTIAL, and a zero denominator forces it
too. That limb is exhibited concretely at row B2.

The suspicion's conclusion is FALSE. The condition is a property of the corpus, not a logical trap, and
its negation is satisfiable. CENSUS_COMPLETE's own clause — "every included claim carries exactly one
outcome from the arithmetic group of §3, with C6_AUDIT_SAMPLE=PASS" — is met by any corpus in which every
included claim states a recipe and prints (or supplies on C3's closed STANDARD list) every input that
recipe names, the arithmetic completing either way, because the arithmetic group is "exactly
REPRO_WITHIN_STATED_PRECISION and REPRO_FAILED": even a claim whose arithmetic FAILS the paper's number
still satisfies CENSUS_COMPLETE. Such a corpus is exhibited row by row at B1 (12 papers, N = 40 included
claims, 37 REPRO_WITHIN_STATED_PRECISION + 3 REPRO_FAILED, audit PASS, receipts P and T verified), and
the §4 precedence is walked limb by limb to CENSUS_COMPLETE. Verdict on the suspicion: REACHABLE — in a
real corpus it demands zero non-arithmetic outcomes and a passing audit, which is restrictive but
exhibitable; the class can occur.

=====================================================================
(A) §3 PER-CLAIM OUTCOMES — all six exhibited
=====================================================================

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| REPRO_WITHIN_STATED_PRECISION | paperA.tex:118 prints "the ratio of the dark-energy to matter density parameters is Ω_Λ/Ω_m = 2.17"; recipe printed ("we form Ω_Λ/Ω_m from the baseline parameters"); both inputs printed verbatim and on C3's closed list (Ω_m = 0.3153, Ω_Λ = 0.6847) → status STANDARD (symbol = ledger key, value = exact printed string; validate compares strings); no stated uncertainty → stated precision = printed precision (2 decimals). Reproduced: 0.6847/0.3153 = 2.1715826197… → rounds to 2.17 at 2 decimals, half away from zero → equals the printed numeral. | §1 (numeral asserted as the paper's own result → included) → §2 steps 1–3 (equation extracted; inputs STANDARD, origin STANDARD via ORIG_CONSTANT) → §2 step 4 ("Attempt the arithmetic MECHANICALLY … every ledger record with status PRINTED or STANDARD") → §3: "the paper's number follows, within its own stated precision … the reproduced value must round to the printed numeral at that precision, rounding half away from zero" → §3 precedence: no earlier terminal condition holds → arithmetic group. Both numbers reported (printed 2.17, reproduced 2.1715826197…); rests_on = DERIVED_STANDARD_OR_MEASURED_ONLY beside it. | YES |
| REPRO_FAILED | paperB.tex:205 prints "Ω_Λ/Ω_m = 2.31" from the same printed recipe and the same two STANDARD inputs (0.6847, 0.3153). Reproduced: 2.1715826197… → rounds to 2.17 ≠ 2.31; |2.1716 − 2.31| = 0.1384, outside the stated precision under any reading. | §1 → §2 steps 1–3 → §2 step 4 → §3: "the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number. Report both numbers." ("unreproduced from the stated inputs," not "error.") Precedence: arithmetic group, nothing earlier holding. rests_on = DERIVED_STANDARD_OR_MEASURED_ONLY — a clean rest does not rescue the arithmetic: two tallies, one pass. | YES |
| REPRO_BLOCKED | paperC.tex:342 prints "the cluster abundance is n(>M) = 4.1e-5 Mpc⁻³"; recipe printed; the needed input M_200 is not printed, but the paper writes "we adopt M_200 = 2.3e14 M_sun from the XYZ Cluster Catalogue (2021)" — and that catalogue is not one of the 89 enumerable texts pinned in R3C2_CORPUS_MANIFEST.md. Second-limb variant: the named source IS enumerable but its cited line carries no machine-matching numeric token for 2.3e14. | §1 → §2 step 3 named-source rule: "If the named source is not enumerable or the value does not match there, file REPRO_BLOCKED under §3" → §3 first limb: the named source "is not an enumerable text pinned in R3C2_CORPUS_MANIFEST.md … whether that source is obtainable elsewhere is irrelevant, because the census may not open or consume it." Recorded status BLOCKED, origin IMPORTED, ORIG_CITATION evidence at the claiming paper's naming sentence, no value (C3); "A seat may not supply a value for an ABSENT or BLOCKED input. Encountering one ends that claim's attempt" (§2 machine floor). §3 precedence: BLOCKED before INPUT_ABSENT / NOT_EVALUABLE / arithmetic group. Input and source named. | YES |
| REPRO_NOT_EVALUABLE | Timeout limb: paperD.tex:96 prints a two-loop symbolic contraction as its result; recipe stated, all inputs PRINTED, but simplification under /usr/bin/python3 -E r3c2_timeout.py 120.0 -- <command> exceeds the 120.0-second monotonic deadline → wrapper "prints SYMBOLIC_TIMEOUT and exits 124 — the reportable outcome" (§9). Machinery limb: paperE.tex:150 prints a CMB lensing bandpower whose recipe needs a full Boltzmann-solver transfer function the lane does not have. | §1 → §2 steps 1–4 (attempt begins; equation stated, inputs present, so no earlier class holds) → §3: "the arithmetic could not be completed within the 120-second cap, or requires machinery this lane does not have. Print SYMBOLIC_TIMEOUT when the 120-second cap is exceeded, or MACHINERY_UNAVAILABLE when the lane lacks the machinery, and the point reached." §4.2 permits one repeat, "meaningful only for REPRO_NOT_EVALUABLE". | YES |
| REPRO_NO_DERIVATION_STATED | paperF.tex:271 prints "the reduced χ² of the fit is 1.07" as its own result; no equation or computational procedure appears anywhere. Variant: paperG.tex:88 prints "the likelihood, computed with our standard pipeline, is ln L = −412.6" — a procedure named but not specified. | §1 satisfied (printed numeral asserted as the paper's own result) → §2 step 1 finds no equation to extract → §3: "the paper prints the claim as its own result but states no equation or computational procedure that could produce it, so there is nothing to attempt … A procedure named but not specified — a sentence that says where the number came from without stating operations a seat could attempt — states no computational procedure that could produce it; file this class and name the passage." §3 precedence: this class files FIRST wherever it holds. Passage named. rests_on NOT_COMPUTED (row C0a). | YES |
| REPRO_INPUT_ABSENT | paperH.tex:133 prints "the decay rate is Γ = 3.2e-18 s⁻¹, from Γ = n·σ·v" with n and v printed, but the cross-section σ is neither printed anywhere nor traced to any named source. | §1 → §2 steps 1–2 (equation and input list extracted) → §2 step 3: σ classified ABSENT ("neither printed nor traced to any named source") → machine floor: "A seat may not supply a value for an ABSENT or BLOCKED input. Encountering one ends that claim's attempt" → §3 REPRO_INPUT_ABSENT; "Name the input" (σ). Precedence: NO_DERIVATION does not hold (equation stated), BLOCKED does not hold (no source named) → INPUT_ABSENT. §3's own contrast applies: a claim whose inputs the paper DOES state, chosen or not, is attempted and files into the arithmetic group. | YES |

=====================================================================
(B) §4 STUDY-LEVEL CLASSES — all eight exhibited
=====================================================================

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| CENSUS_COMPLETE | Corpus: 12 papers; N = 40 included claims, each with a stated recipe whose every input is PRINTED or closed-list STANDARD; outcomes 37 REPRO_WITHIN_STATED_PRECISION + 3 REPRO_FAILED (all arithmetic group); exclusion ledger 58 rows (EQUATION_NUMBER, REFERENCE_NUMBER, DATE, AUTHOR_SPECIFIED_INPUT); both seats' enumerations agree; outcomes agree; zero origin disagreements; C6: auditor's complete independent enumeration over all 89 enumerable texts yields no omission, dispute rate 0/40 = 0% ≤ 10%, the recomputed selection matches (seed supplied with receipt T), no MISMATCH, both seals match → C6_AUDIT_SAMPLE=PASS; receipts P and T present, Blanc's independent re-hash verifies all four values. | §4 precedence walked limb by limb: R3C2_NO_CLASS? No (C0–C5b PASS in both seats). CENSUS_CONTROL_SPLIT? No. CENSUS_DENOMINATOR_DISPUTED? No. CENSUS_OUTCOME_DISPUTED? No. CENSUS_ORIGIN_DISPUTED? No. CENSUS_AUDIT_FAILED? No (audit PASS; receipts verify). CENSUS_PARTIAL? No (no non-arithmetic outcome; denominator 40 > 0). → §4.1: "every included claim carries exactly one outcome from the arithmetic group of §3, with C6_AUDIT_SAMPLE=PASS." "Report the full tally with its denominator, and the rests_on tally beside it — two tallies from one pass." | YES |
| CENSUS_PARTIAL | (i) The B1 corpus with claim #23 = the row-A3 blocked claim (M_200 from a non-enumerable catalogue). (ii) Zero-denominator variant: both enumerations find only excludable numerals (dates, equation numbers, attributed values, author-set inputs) → denominator 0, and no passage on either side at audit. | (i) §4.2: "at least one included claim carries a non-arithmetic outcome (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT, REPRO_BLOCKED, REPRO_NOT_EVALUABLE)" → "INCONCLUSIVE, and it takes precedence over CENSUS_COMPLETE"; report each and why. (ii) §4.1: "A denominator of zero files CENSUS_PARTIAL with the empty enumeration named; no census is complete over nothing"; §4.2: "or the denominator is zero." | YES |
| CENSUS_AUDIT_FAILED | Thirteen §6/§7 paths exhibited in section (C) rows C1–C11 and C13. Shortest: after receipt T, Blanc's independent re-hash of the tally commit mismatches one of the four receipted values. | §7: "Any missing receipt or mismatch files CENSUS_AUDIT_FAILED (§4, whose definition now names this case), leaves the interpretation NOT_RUN and voids the comparison" → §4.3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the cause named), or the receipt verification of the seal fails. No tally is filed; report which." | YES |
| R3C2_NO_CLASS | (i) Pre-dispatch limb: the builder's forbidden-list assertion finds a blocked string surviving in the built packet → packet not written. (ii) Post-dispatch limb: C2_INPUT_LEDGER validate exits non-zero in seat A twice and in seat B twice. | (i) C4: "If any survives, the packet is not written and C4_PACKET_REDACTED=FAIL" → §4.4: "a packet or seat-isolation failure before dispatch files this class." (ii) §4.4: "a control among C0 through C5b fails in every seat that attempted it after two attempts." Boundary honoured: "A C6 audit failure or a seal-receipt failure files CENSUS_AUDIT_FAILED, not this class." | YES |
| CENSUS_DENOMINATOR_DISPUTED | (i) Enumeration limb: seat A includes paperJ.tex:42 ("0.31") as a claim; seat B excludes it as ATTRIBUTED_NOT_DERIVED; two reconciliation attempts fail. (ii) Input-list limb: seats agree on every candidate; for claim paperJ#c1 seat A lists 3 inputs, seat B lists 4; merge exits 1; the one reconciliation against the paper's stated equation does not resolve it. | (i) §1 ("disagreement on any candidate that survives two reconciliation attempts stops the study under CENSUS_DENOMINATOR_DISPUTED") and §6 limb A → §4.5. (ii) C3 lane-side: "merge exits 1 if the two input_id sets differ — the two seats reconcile their input lists against the paper's stated equation once; an input-set difference surviving that reconciliation stops the study under CENSUS_DENOMINATOR_DISPUTED (§4), the disputed inputs listed with both seats' quotations"; §4.5 second limb names exactly this case. | YES |
| CENSUS_OUTCOME_DISPUTED | Agreed claim paperK.tex:55 prints "r_s = 147.4 Mpc" beside a passage ambiguous as to whether ±0.3 is stated for this claim. Seat A applies the stated-uncertainty test: reproduced 147.32, |147.32 − 147.4| = 0.08 ≤ 0.3 → REPRO_WITHIN_STATED_PRECISION. Seat B applies the rounding rule: 147.32 rounds to 147.3 ≠ 147.4 → REPRO_FAILED. One reconciliation "against the printed numeral and the stated-precision rule of §3" is attempted; both seats persist. | §2 step 5: "a disagreement surviving that reconciliation files CENSUS_OUTCOME_DISPUTED (§4)" → §4.6: "the two seats' filed per-claim outcomes on an agreed included claim differ after one reconciliation … the claim is listed with both seats' outcomes, both number pairs, and the step each seat reached" (147.4/147.32; 147.4/147.3). The census does not proceed. | YES |
| CENSUS_ORIGIN_DISPUTED | N = 100 included claims. On one input feeding each of 11 claims (paperL#c17…c27), the sentence is "we set β = 0.31": seat A files ORIG_CHOICE_STATED → CHOSEN; seat B finds no stated basis and files ORIG_SILENT → UNDECLARED with an adequate origin_search. (The ORIG_CITATION precedence does not resolve it — the sentence names no external source.) Disagreements are "reported, never reconciled"; 11/100 = 11% > 10%. Contrast: 10/100 = 10% → reported only, census proceeds. | §4.7: "the two seats' independent origin classifications disagree on inputs affecting more than 10% of included claims. The census does not proceed; every disputed input is listed with both seats' classification and both quotations"; C6: "Above 10% of included claims, CENSUS_ORIGIN_DISPUTED." V33 boundary honoured: "Evidence-only or search-only alternatives are not origin-classification disagreements and do not count toward the 10% rule" — the count here is of label disagreements, which count. | YES |
| CENSUS_CONTROL_SPLIT | C5_HARNESS_PINNED: seat A's five commands all exit 0 with the path of (4) and the MANIFEST_SHA256 of (5) equal to the dispatch record's; seat B's command (5) prints a different MANIFEST_SHA256 (its site-packages tree changed); two attempts preserve the split. | §4.8: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not adopt the passing seat's result." | YES |

=====================================================================
(C) DECLARED CONDITIONS AND THE V33-NAMED CONSTRUCTIONS
=====================================================================

C0a. rests_on NOT_COMPUTED — REACHABLE.
Concrete input: the row-A5 claim paperF#c1 ("the reduced χ² of the fit is 1.07", no derivation stated)
files REPRO_NO_DERIVATION_STATED; with no equation there are no inputs, hence no ledger records for the
claim. Clause path: §3 lane-side — "an empty ledger is valid and every included candidate without a
record carries rests_on NOT_COMPUTED"; §3 — "a claim with no ledger record carries rests_on NOT_COMPUTED,
and the rests_on tally reports a NOT_COMPUTED row"; §9 — compute "emits rests_on NOT_COMPUTED for every
included candidate with no ledger record". Reachable: YES.

CENSUS_AUDIT_FAILED through each named C6 path — every one reachable; each row gives the concrete
input, the clause, and the routing into §4.3 ("No tally is filed; report which").

| path | concrete input | clause path | reachable |
|---|---|---|---|
| C1. Sealed-included absent from the auditor | Sealed ledgers include passage (paper3.tex:77, "0.96", included); the auditor's complete independent enumeration of all 89 enumerable texts lacks it. | C6: "Omissions: a sealed INCLUDED passage absent from the auditor's enumeration … each is ledger incompleteness and files CENSUS_AUDIT_FAILED" → §4.3. | YES |
| C2. Auditor-listed absent from the sealed ledgers | The auditor lists (paper9.tex:141, "1.6e-5"), excluded by the auditor as DATE; neither sealed ledger names that passage. | C6: "a passage the auditor lists (included OR excluded) that the sealed ledgers omit — each is ledger incompleteness and files CENSUS_AUDIT_FAILED" → §4.3. | YES |
| C3. Dispute rate above 10% | Sealed denominator 100; 11 rows AUDIT_INCLUSION_DISPUTED (passages both sides list but dispose differently, plus sealed-EXCLUDED passages absent from the auditor). 11/100 = 11% > 10%. Contrast: 10 rows = 10% → reported only. | C6: "Disputes: … are AUDIT_INCLUSION_DISPUTED, listed with both dispositions and counted; above 10% of the sealed included denominator the audit files CENSUS_AUDIT_FAILED; at or below it the count is reported" → §4.3. | YES |
| C4. Seedless selection | Receipt T is recorded; the external custodian supplies no seed with it. | C6: "If the seed is not supplied and recorded with the receipt, the audit does not run, C6_AUDIT_SAMPLE=NOT_RUN, and the study files CENSUS_AUDIT_FAILED with the missing seed named" → §4.3. | YES |
| C5. Zero denominator with passages on either side | Sealed included denominator 0 (both census seats excluded everything); the auditor's independent enumeration lists 4 candidate passages. | C6: "A sealed denominator of zero with any passage on either side fails" → audit not PASS → §4.3. §4 precedence (CENSUS_AUDIT_FAILED before CENSUS_PARTIAL) bars absorption into PARTIAL. A zero denominator with NO passage anywhere routes instead to CENSUS_PARTIAL (row B2) — different limb, different input. | YES |
| C6. Incomplete reconstruction | The auditor's reconstruction of selected claim S4 carries an ORIG_SILENT input i2 with no origin_search (equivalently: a missing origin_evidence or derived_from). | C6: "before sealing, audit seal-rederivation validates the reconstruction schema — every input carries symbol, status, value, source coordinates, origin, origin evidence and derived_from (and origin_search when silent) — and refuses an incomplete one" → no stage-2 seal → §4.3: the audit "does not run to PASS for any cause (the cause named)" — cause: reconstruction refused as incomplete. | YES |
| C7. Fabricated evidence quotation in an off-sample dependency record | Selected claim S1 (arithmetic group, always sampled) depends via derived_from on input i7 of UNSELECTED claim S9; the sealed i7's origin_evidence.verbatim does not occur at its cited line (fabricated); the auditor's independently reconstructed i7 carries the true quotation. | C6/§3: "every required field, evidence item and dependency edge is compared throughout each selected claim's complete dependency closure, records assigned to unselected claims included" → quotation conflict on i7 → MISMATCH, propagated to S1's row → the PASS predicate "no audited claim or origin is MISMATCH" fails (C6) → §4.3. | YES |
| C8. Duplicated input id | The auditor's reconstruction contains two records with input_id "paper7#i3" (or an explicit identity field inconsistent with its enclosing keys). | §3 (master-only rule the script implements): "Before sealing, a reconstruction with a duplicate input_id or an explicit identity field inconsistent with its enclosing keys is refused" → no rederivation seal → audit does not run to PASS → §4.3. | YES |
| C9. Record reconstructed under the wrong claim | The auditor binds input i4 to enclosing claim paper7#c2 while the sealed ledger binds it to paper7#c1. | §3: "At comparison, each enclosing-claim versus sealed-claim identity conflict is recorded as a MISMATCH of that input, propagated to every selected claim whose dependency closure contains the input, and fails the overall audit" → §4.3. | YES |
| C10. Hybrid-branch record, either direction | Sealed merged i5: primary branch {origin CHOSEN, ORIG_CHOICE_STATED evidence E1, parents [p1]}; preserved alternative {origin_alt UNDECLARED, ORIG_SILENT, origin_search_alt S_alt, derived_from_alt [p2]}. Forward hybrid: auditor's i5 = {CHOSEN, E1, parents [p2]}. Reverse hybrid: auditor's i5 = {UNDECLARED, ORIG_SILENT, origin_search = S_alt, parents [p1]}. | §3: "An input matches only when its origin, origin evidence, parent list and any required origin_search jointly match one complete preserved branch; searches are compared as JSON structure; hybrids and matches to neither branch are MISMATCH." And: "If neither complete branch matches, an unconditional record-level MISMATCH is appended before any field-specific diagnostic, propagated to every dependent selected claim, and the audit fails even when the root-origin sets agree — the full-record predicate decides the verdict and the diagnostics only explain it." Both directions fail identically → §4.3. | YES |
| C11. Changed origin_search CONTENT on an ORIG_SILENT branch | Auditor's i5 matches the alternative branch in origin (UNDECLARED), evidence (ORIG_SILENT) and parents [p2], but its origin_search = {query q′, files f′, matches m′} differs in content from origin_search_alt (one extra match row). | §3: "searches are compared as JSON structure"; the joint-branch predicate above → the record matches neither the alternative (search content differs) nor the primary (origin/evidence differ) → MISMATCH → audit fails → §4.3. Under SPI the same verdict files in both seat orders, the primary having been fixed by "a seat-blind canonical key (the smaller sha256 of each record's canonical JSON)". | YES |

C12 (positive control, required). A claim whose auditor reconstruction equals a COMPLETE declared
alternative branch that uses ORIG_SILENT — and therefore does NOT file CENSUS_AUDIT_FAILED.
Concrete input: sealed merged i5 as in C10; the auditor's reconstruction of i5 is exactly {origin
UNDECLARED, ORIG_SILENT evidence, origin_search equal as JSON structure to origin_search_alt, parents
[p2]} — one complete preserved branch, nothing drawn from the primary.
Clause path: C6 — audit compare "binds an auditor classification that matches a declared sealed
alternative to that branch (§3)" → no MISMATCH on i5; "complete branches are matched before roots are
recomputed, and the sealed and matched branches are reported" (§3); the search compared is the matched
branch's (origin_search_alt). The two seats' CHOSEN-vs-UNDECLARED label difference is filed
ORIGIN_DISPUTED, reported with both quotations, never reconciled, and counted toward the 10% origin rule
— here 1 of 100 included claims = 1% ≤ 10%, so no CENSUS_ORIGIN_DISPUTED; a search-only or evidence-only
alternative with EQUAL labels would not count at all ("Evidence-only or search-only alternatives are not
origin-classification disagreements and do not count toward the 10% rule", §3). The audit proceeds; this
input does NOT file CENSUS_AUDIT_FAILED. Reachable: YES — exhibited as required, and the negative
verdict is correctly not filed.

C13. A sampled outcome the audit cannot reproduce — REACHABLE.
Concrete input: selected claim S2 was filed REPRO_WITHIN_STATED_PRECISION with printed 2.17 / reproduced
2.1716; the auditor's independent reconstruction of the same claim from the pinned sources yields 1.94.
Clause path: C6 — "Any outcome the audit cannot reproduce, or any ledger incompleteness, files
CENSUS_AUDIT_FAILED"; the claim's row is MISMATCH → §4.3.

The four tally stops, with their §4 filings:

| stop | concrete input | clause path and §4 filing | reachable |
|---|---|---|---|
| C14. C1B_BATCH_COVERAGE=FAIL stops the seat's tally | Batch b5 owns text T but T's bytes do not verify against its manifest row (variants: one text owned by two batches; batch b7's report lacks the packet's ACCESS_SHA). | C1B: "C1B_BATCH_COVERAGE=PASS iff every manifest text is owned by exactly one batch, every owned text's bytes verify against its manifest row, and every batch report prints the packet's ACCESS_SHA … Either FAIL stops the seat's tally." §4 filing: "a FAIL in every seat that tries it, after two tries, files R3C2_NO_CLASS; a surviving fail/pass split files CENSUS_CONTROL_SPLIT; an unreached check is NOT_RUN." | YES |
| C15. JOIN=FAIL stops the seat's tally | The LIMB-A chain's b3 seal does not match (variants: the predecessor chain has no root with no predecessor; a candidate in b7's file is owned by b6; an evidence source is not a manifest text; identifiers repeat across batches; a cross-batch derived_from cycles). | C1B: "JOIN=PASS iff every seal matches, the ordered predecessor chain is intact from a root with no predecessor, every candidate and ledger claim is owned by its batch, every evidence source is a manifest text, identifiers are unique and every derived_from resolves acyclically. Either FAIL stops the seat's tally." §4 filing: the same C1B contract — R3C2_NO_CLASS if every seat fails it after two tries; CENSUS_CONTROL_SPLIT on a surviving fail/pass split; NOT_RUN if unreached. | YES |
| C16. C5C_NO_FALLBACK=FAIL stops the tally pre-tally | Session 2 of seat B has no printed, session-identified provider log (variant: the log carries a fallback entry). | §9: "the no-fallback control C5C_NO_FALLBACK=PASS|FAIL|NOT_RUN requires a printed, session-identified provider log for every session — a missing log or any fallback entry is FAIL, an unreached check NOT_RUN — a pre-tally control under the R3C2_NO_CLASS and CENSUS_CONTROL_SPLIT rules, checked by the lane owner." §4 filing: FAIL in every seat that attempted it after two attempts → R3C2_NO_CLASS (§4.4); a surviving split → CENSUS_CONTROL_SPLIT (§4.8). | YES |
| C17. A merge field disagreement stops the tally | Seats agree on the input-id set, but on input paper4#i2 seat A records value "0.3153" and seat B records "0.315" (variants: status, symbol, or source coordinates differ on the same input id). | C3 lane-side: "where the two seats' value, status, symbol or source coordinates differ on the same input id, merge prints every such disagreement, reports FIELD_DISAGREEMENTS, exits 1 and writes no merged file — the lane resolves it in the open before the tally." No merged file → no tally is sealed → the tally does not occur. §4 filing: the text names NO stop class for this event; it is resolved in the open before the tally. Contrast the sibling event — an input-id SET difference — which after one reconciliation files CENSUS_DENOMINATOR_DISPUTED (row B5). | YES (the stop occurs; its disposition is open resolution, not a §4 class) |

=====================================================================
UNREACHABLE VERDICTS — NONE
=====================================================================

Every §3 per-claim outcome (6 of 6), every §4 study-level class (8 of 8), and every declared condition
named for this exhibition — rests_on NOT_COMPUTED (C0a), the eleven C6 failure paths (C1–C11), the
ORIG_SILENT complete-alternative positive match (C12), the unreproduced sampled outcome (C13), and the
four tally stops (C14–C17) — has at least one concrete licensed input exhibited above, each routed
through the document's own clauses. No verdict is UNREACHABLE, so there is no blocking clause to quote.

The one suspicion put to this exhibition is answered in section 0 and row B1/B2: CENSUS_COMPLETE is
REACHABLE. The routing fact beneath the suspicion is confirmed — a single REPRO_BLOCKED,
REPRO_INPUT_ABSENT, REPRO_NO_DERIVATION_STATED or REPRO_NOT_EVALUABLE claim anywhere in the corpus
forces CENSUS_PARTIAL (§4.2, which "takes precedence over CENSUS_COMPLETE"), and a zero denominator
forces CENSUS_PARTIAL as well — but the negated condition is satisfiable and is exhibited, so the class
can occur.

R3C2_C0_EXHIBITION_COMPLETE

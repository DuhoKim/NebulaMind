ACCESS_SHA=9c4b873d4281419a93b8aac9208e5a5de22481217fdd124b1dcfa6a7ae4d88be
C0_REACHABILITY=PASS

# R3C2 C0 reachability exhibition — V24i (kimi, independent seat), 2026-09-06

Document exhibited: `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md`, read from disk in full, and no other file in this
directory was read. The access proof above (`shasum -a 256`) was computed by this seat before anything else. This is an
exhibition, not a gate: no physics and no design quality is judged — only whether each declared §3 per-claim outcome and
each declared §4 study-level class CAN OCCUR under the text as it stands. §3 is treated under the settled option-(c)
wording (one pass, two tallies; `REPRO_AFTER_CHOICE` retired into the script-computed `rests_on` field); there is no held
clause. The V24i delta (C4/C5b scope-and-confinement wording, §10.18) touches no §3 outcome and no §4 class.

Declared sets, from the text. §3 declares six per-claim outcomes (C1: "one of the six §3 tokens"); the arithmetic group is
exactly `REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED` (§3: "The arithmetic group is the set of outcomes that state
whether the arithmetic reproduced the number: exactly `REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED`"). §4 declares
eight study-level classes and a total filing precedence: `R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`,
`CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_OUTCOME_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`,
`CENSUS_PARTIAL`, `CENSUS_COMPLETE` — "Exactly one study-level outcome is filed... Once a stop class applies, later limbs
are unreached and their controls are `NOT_RUN`."

Marked-dependence note (as the brief directs): every row's first step — "this passage is an included claim" — rests on
§1's operational definition, which §1 itself marks as non-mechanical ("the audit trail records the boundary but does not
make it mechanical — whether a numeral is 'the paper's own result' remains a judgement, so it moves from one reader to
two who must agree"). That dependence is uniform across all rows and blocks none of them: the failure mode it can
generate — two seats disagreeing on inclusion — is itself a declared class, exhibited below as
`CENSUS_DENOMINATOR_DISPUTED`. The dependence is stated here rather than assumed away; it is itself a result of this
exhibition.

## Exhibition table

### (A) §3 per-claim outcomes

| verdict | concrete input | clause path | reachable yes/no |
|---|---|---|---|
| `REPRO_WITHIN_STATED_PRECISION` | paperA.tex:88 prints "Ω_m = 0.315 and Ω_Λ = 0.685 give Ω_tot = 1.000 (Eq. 4: Ω_tot = Ω_m + Ω_Λ)". Inputs Ω_m, Ω_Λ are both printed in the paper → status `PRINTED`, origins recorded under C3 (say `CHOSEN`/`ORIG_CHOICE_STATED`; under option (c) origin does not gate the attempt). Attempt: 0.315 + 0.685 = 1.000; the paper states no precision, so the printed precision (3 dp) is the claim's stated precision and the reproduced value rounds to the printed numeral, half away from zero. | §1 include → §2 steps 1–3 (both inputs `PRINTED`) → §2 step 4 ("follow the paper's own recipe, using every value it directs you to use, i.e. every ledger record with status `PRINTED` or `STANDARD`") → §3 precedence: no earlier terminal condition holds → §3 def: "the paper's number follows, within its own stated precision, from the paper's own recipe applied to the inputs it states ... Report both numbers" → §2 step 5: outcome recorded in the candidate file; the script records `rests_on` beside it (here `USES_CHOSEN`) | yes |
| `REPRO_FAILED` | paperB.tex:41 prints the same equation and the same two printed inputs (both `PRINTED`) but asserts "Ω_tot = 0.999" as its own result. 0.315 + 0.685 = 1.000 ≠ 0.999 at the printed precision. The inputs stated are sufficient for the recipe; the arithmetic does not give the paper's number. | §1 → §2 steps 1–4 → §3 precedence (nothing earlier holds) → §3 def: "the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number. Report both numbers. Wording: 'unreproduced from the stated inputs,' not 'error.'" → §2 step 5; `rests_on` reported beside it | yes |
| `REPRO_BLOCKED` | paperC.tex:77 prints "we adopt the H₀ value of XYZ (2021)" and uses t = 1/H₀ to print "t = 13.4 Gyr" as its own result. The paper does not print the H₀ numeral; it names XYZ (2021), which is not an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`. Second limb: the named source IS an enumerable pinned text but the value does not machine-match at the cited line. | §2 step 3 named-source rule ("a value the paper does not print is classified by the named-source rule alone and is never `STANDARD`") → §2 IMPORTED paragraph: "a cited value that does not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest, files `REPRO_BLOCKED` under §3" → C3 record: status `BLOCKED`, origin `IMPORTED`, `ORIG_CITATION` cited to the naming sentence, no value, never consumed → §2: "A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt." → §3 precedence: `REPRO_NO_DERIVATION_STATED` does not hold (the equation is stated), so `BLOCKED` is the first applicable class; name the input and the source | yes |
| `REPRO_NOT_EVALUABLE` | paperD.tex:60 prints a numeral from a recipe requiring a long numerical integration; the seat launches it as `/usr/bin/python3 -E r3c2_timeout.py 120.0 -- <command>`; the wrapper prints `SYMBOLIC_TIMEOUT` and exits 124. Second limb: the recipe requires machinery this lane does not have → print `MACHINERY_UNAVAILABLE`. | §9 (wrapper enforces the 120.0-second deadline, prints `SYMBOLIC_TIMEOUT` and exits 124 — "the reportable outcome") → §3 def: "the arithmetic could not be completed within the 120-second cap, or requires machinery this lane does not have. Print `SYMBOLIC_TIMEOUT` when the 120-second cap is exceeded, or `MACHINERY_UNAVAILABLE` when the lane lacks the machinery, and the point reached" → §4.2: one repeat permitted, meaningful only for this class | yes |
| `REPRO_NO_DERIVATION_STATED` | paperE.tex:112 prints "the resulting amplitude is A = 2.10" as its own result, and no equation or computational procedure producing it appears anywhere. Second limb: the paper says only "obtained from our standard pipeline" — a procedure named but not specified. | §1 include (a printed numeral asserted as the paper's own result) → §2 step 1 finds no equation to extract → §3 def: "the paper prints the claim as its own result but states no equation or computational procedure that could produce it, so there is nothing to attempt. Name the passage. A procedure named but not specified ... file this class and name the passage." → §3 precedence: first in the order, so it files even where inputs would also be absent | yes |
| `REPRO_INPUT_ABSENT` | paperF.tex:55 prints the equation t = 1/H₀ and the claim "t = 13.8 Gyr" as its own result, but never prints the value of H₀ and names no source for it. | §2 step 3: input classified `ABSENT` → §2: "A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt." → §3 def: "an input the equation needs is `ABSENT` from the paper — neither printed nor traced to any named source — so the attempt stops there. Name the input." → §3 precedence: `REPRO_NO_DERIVATION_STATED` does not hold (equation stated), `REPRO_BLOCKED` does not hold (no named source) → this class is first applicable | yes |

### (B) §4 study-level classes (exhibited in filing-precedence order)

| class | concrete input | clause path | reachable yes/no |
|---|---|---|---|
| `R3C2_NO_CLASS` | Pre-dispatch: `r3c2_build_seat_packet.py` finds a forbidden-list string surviving in the packet output → the packet is not written, `C4_PACKET_REDACTED=FAIL`, no seat is dispatched. Live variant: both seats run C5 and command (2) (`import sympy`) exits 1 in each seat, twice each — the control fails in every seat that attempted it after two attempts. | C4: "If any survives, the packet is not written and `C4_PACKET_REDACTED=FAIL`" → §4.4: "a control among C0 through C5b fails in every seat that attempted it after two attempts; a packet or seat-isolation failure before dispatch files this class" → precedence: first | yes |
| `CENSUS_CONTROL_SPLIT` | C5 harness: seat A's command (2) exits 1 (sympy absent in its environment), seat B's exits 0; after two attempts the results are unchanged — the control fails in one seat and passes in another. | §4.8: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not adopt the passing seat's result." → precedence: second (§4.4 does not hold — the control did not fail in every seat) | yes |
| `CENSUS_DENOMINATOR_DISPUTED` | Seat A includes candidate paperG.tex:412 (numeral "0.05", read as the paper's own result); seat B excludes it as `ATTRIBUTED_NOT_DERIVED`; the disagreement survives two reconciliation attempts. Second limb: both seats agree on every candidate, but `r3c2_lane_tools.py merge` exits 1 — seat A lists input H₀ for claim 7 and seat B does not — and the difference survives the one reconciliation against the paper's stated equation. | §1: "disagreement on any candidate that survives two reconciliation attempts stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4): the disputed candidates are listed and the complete candidate and exclusion ledgers are reported with the dispute"; §6 limb A names the same stop; C3: "an input-set difference surviving that reconciliation stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4), the disputed inputs listed with both seats' quotations" → §4.5 names both limbs | yes |
| `CENSUS_OUTCOME_DISPUTED` | Agreed included claim paperH.tex:88 prints "Ω_tot = 1.00" with the same two `PRINTED` inputs in both ledgers; seat A files `REPRO_WITHIN_STATED_PRECISION` (1.000 rounds to 1.00 at the printed precision), seat B files `REPRO_FAILED` (holding the claim's stated precision to be 3 dp); the one permitted reconciliation against the printed numeral and the stated-precision rule of §3 is run and the seats still file different outcomes. (The rule is mechanical; the class exists for the residue where a filed token is not moved — the text provides for a disagreement "surviving that reconciliation," and nothing in the text makes survival impossible.) | §2 step 5: "a disagreement surviving that reconciliation files `CENSUS_OUTCOME_DISPUTED` (§4)" → §4.6: "The census does not proceed; the claim is listed with both seats' outcomes, both number pairs, and the step each seat reached." | yes |
| `CENSUS_ORIGIN_DISPUTED` | N = 10 included claims; the seats agree on candidates, input lists and outcomes; they classify the origins of inputs affecting 2 claims differently — seat A files `CHOSEN`/`ORIG_CHOICE_STATED`, seat B files `MEASURED`/`ORIG_MEASURED`, each with its machine-matched quotation. 2/10 = 20% > 10%. The dispute is reported, never reconciled. | C3: "Every input's `origin` is classified independently by both seats." → C6: "An input on which the two classifications disagree is filed `ORIGIN_DISPUTED` ... it is not reconciled. Above 10% of included claims, `CENSUS_ORIGIN_DISPUTED`." → §4.7: "The census does not proceed; every disputed input is listed with both seats' classification and both quotations." | yes |
| `CENSUS_AUDIT_FAILED` | Three independent routes. (i) The C6 auditor, without sight of earlier work, re-derives arithmetic-group claim 3 and obtains a different number → `MISMATCH` in `C6_AUDIT.json` (or the full-ledger audit finds an incompleteness). (ii) The external custodian supplies no seed with receipt T → the audit does not run, `C6_AUDIT_SAMPLE=NOT_RUN`, the missing seed named. (iii) After opening, the custodian's independent re-hash of the tally mismatches receipt T (or receipt P/T is missing). | C6: "Any outcome the audit cannot reproduce, or any ledger incompleteness, files `CENSUS_AUDIT_FAILED`"; C6: "If the seed is not supplied and recorded with the receipt, the audit does not run, `C6_AUDIT_SAMPLE=NOT_RUN`, and the study files `CENSUS_AUDIT_FAILED` with the missing seed named." → §4.3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the cause named), or the receipt verification of the seal fails. No tally is filed; report which."; §7: "Any missing receipt or mismatch files `CENSUS_AUDIT_FAILED`" | yes |
| `CENSUS_PARTIAL` | Corpus of five papers, one of them paperC (the `REPRO_BLOCKED` case above); every other claim files an arithmetic-group outcome; both seats agree at every step; the audit passes. Exactly one included claim carries a non-arithmetic outcome. Second limb: the enumeration includes zero claims — every candidate fails §1 — so the denominator is zero. | §4.2: "at least one included claim carries a non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`), or the denominator is zero. Report each and why. INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`."; §4.1: "A denominator of zero files `CENSUS_PARTIAL` with the empty enumeration named; no census is complete over nothing." | yes |
| `CENSUS_COMPLETE` | Corpus whose every enumerable text is paperA-like: 3 included claims, each stating its equation, every input `PRINTED` or `STANDARD`, every attempt completing under 120 s; outcomes 2 × `REPRO_WITHIN_STATED_PRECISION` and 1 × `REPRO_FAILED`; the two seats agree on candidates, input lists and outcomes; origin disagreements 0 of 3 (≤ 10%); the C6 auditor re-derives all 3 arithmetic-group claims with `MATCH` everywhere, `C6_AUDIT_SAMPLE=PASS`; receipts P and T both verify. | §4.1: "every included claim carries exactly one outcome from the arithmetic group of §3, with `C6_AUDIT_SAMPLE=PASS`"; denominator 3 > 0, so the zero-denominator clause is silent → §4 precedence: no earlier limb's condition holds (no control failure or split; enumerations and outcomes agree; origin disputes ≤ 10%; audit PASS; zero non-arithmetic outcomes, so §4.2 is false) → the filing falls through to `CENSUS_COMPLETE`; "Report the full tally with its denominator, and the `rests_on` tally beside it — two tallies from one pass." | yes |

### (C) Reachability, stated per verdict

All six §3 per-claim outcomes: reachable. All eight §4 study-level classes: reachable. Named sub-conditions, each
exhibitable as shown in its parent row: `SYMBOLIC_TIMEOUT` and `MACHINERY_UNAVAILABLE` (under `REPRO_NOT_EVALUABLE`);
`CENSUS_PARTIAL`'s zero-denominator limb; `CENSUS_AUDIT_FAILED`'s three causes (audit `MISMATCH`/incompleteness; missing
seed → `C6_AUDIT_SAMPLE=NOT_RUN`; seal-receipt failure); `CENSUS_DENOMINATOR_DISPUTED`'s input-list limb (`merge` exit 1
surviving one reconciliation); `REPRO_BLOCKED`'s two limbs (named source not in the manifest; named source enumerable but
no machine-match at the cited line). Not outcomes, and therefore not exhibited as rows: the five exclusion-ledger kinds
(§3: "Candidate exclusions are not per-claim outcomes."); the `rests_on` field values (`NOT_COMPUTED` — a claim with no
ledger record, e.g. the `REPRO_NO_DERIVATION_STATED` case above, whose tally row §3 requires; `DISPUTED` — the pair
computed under both classifications); and the retired `REPRO_AFTER_CHOICE`, which is not a declared outcome of the text
as it stands (retired into `rests_on` by the option-(c) ruling, §3's note and §10.4).

## The CENSUS_COMPLETE suspicion, answered directly

REACHABLE.

The routing, in the text's own clauses:

1. §4.1 files it when "every included claim carries exactly one outcome from the arithmetic group of §3, with
   `C6_AUDIT_SAMPLE=PASS`", and bars it in one case only: "A denominator of zero files `CENSUS_PARTIAL` with the empty
   enumeration named; no census is complete over nothing."
2. §4's precedence puts it last: "`R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`,
   `CENSUS_OUTCOME_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`, `CENSUS_COMPLETE`." It is
   filed exactly when no earlier condition holds.
3. The suspicion's mechanism is real, and it is in the text: ONE included claim anywhere in the corpus carrying
   `REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED` or `REPRO_NOT_EVALUABLE` satisfies §4.2's
   condition, and §4.2 "takes precedence over `CENSUS_COMPLETE`." So on any corpus containing even one such claim,
   `CENSUS_COMPLETE` cannot be filed. That is a true property of this design, stated here rather than softened.
4. But hard is not unreachable. The blocking condition is a property of the input corpus, not a clause that closes every
   path. The exhibiting input exists — row 8 of the §4 table: a corpus (even of one paper; the denominator need only be
   ≥ 1) in which every included claim states a procedure, every input is `PRINTED` or `STANDARD`, and every attempt
   completes, with agreeing seats, origin disputes ≤ 10%, a passing audit and verified receipts. Every earlier precedence
   limb is then false and the filing falls through to `CENSUS_COMPLETE`.

So: reachable in the design, corpus-conditional in fact. Whether the real corpus — 89 enumerable texts per §10.5's
record — can file it is the empirical question the census itself answers on its first pass; the C0 question — does any
input produce it — is answered yes. This agrees with both prior blind C0 seats, whose agreement table (§10.3) records
"`CENSUS_COMPLETE` | reachable | reachable", and it is exactly the early-check worry the C0 clause itself flags ("a
single blocked or absent input in the whole corpus is enough to prevent" it): the worry is confirmed as a design
property and refuted as an unreachability claim.

## UNREACHABLE verdicts and their blocking clauses

None. Every declared §3 outcome and every declared §4 class has an exhibited input above; there is no blocking clause to
quote.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V24I_KIMI_COMPLETE

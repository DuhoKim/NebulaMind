ACCESS_SHA=f4edb5145b5c150c43a6550b30f0beca1d08bf4675305383e7860c3657f951fd
C0_REACHABILITY=PASS

# R3C2 — C0 REACHABILITY EXHIBITION on the V26 INTEGRATED CANDIDATE (UNADOPTED)

Author seat: kimi, 2026-09-06. Object read from disk, in full: `R3C2_V26_INTEGRATED_CANDIDATE_UNADOPTED_20260906.md`
(sha256 f4edb5145b5c150c43a6550b30f0beca1d08bf4675305383e7860c3657f951fd, 1249 lines). No other file in this
directory was read.

Scope, stated so the verdict is not overread:

- This is ONE independent seat's exhibition. §5 C0 requires a second independent seat to verify and both to return
  `C0_REACHABILITY=PASS`; this report is the author-seat artefact, not the two-seat agreement.
- The object is an INTEGRATED CANDIDATE: §2's import rule (D1 wording B), the stronger C6 audit (D7), and C1/C1B
  ownership batching are carried unchosen by the principal. The exhibition is run against the text as it stands.
  Section 10 is history and binds nothing.
- §3's definition stands as ruled (option (c): one pass, two tallies; `REPRO_AFTER_CHOICE` retired into the
  script-computed `rests_on` field). There is no held clause. §3 declares exactly six per-claim outcomes; §4
  declares exactly eight study-level classes. Exclusion kinds (including `AUTHOR_SPECIFIED_INPUT`) are not
  per-claim outcomes and are exhibited only where they route a claim.
- This exhibition does not gate the candidate and does not judge its physics or its design. It asks only whether
  each declared verdict CAN OCCUR: whether a concrete input exists that the document's own clauses route to that
  verdict. Constructed papers below are concrete hypothetical inputs, as C0 prescribes ("a specific claim, its
  inputs, and the path it takes through this document").

Reference clauses used throughout (quoted once, cited by name below):

- §3 precedence, verbatim: "Exactly one outcome is filed per claim. Where more than one terminal condition holds,
  file the first in this order: `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`,
  `REPRO_NOT_EVALUABLE`, then the arithmetic group."
- §4 precedence, verbatim: "Exactly one study-level outcome is filed. Where more than one condition holds, file
  the first in this order: `R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`,
  `CENSUS_OUTCOME_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`, `CENSUS_COMPLETE`."
- Arithmetic group, verbatim: "exactly `REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED`".
- §2, verbatim: "A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that
  claim's attempt."

## (A) Per-claim outcomes of §3 — all six exhibited

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `REPRO_WITHIN_STATED_PRECISION` | paperA.md line 88 prints "the flow speed is 300 km/s" asserted as its own result; line 40 states `v = d/t`; line 41 prints `d = 600 km`; line 42 prints `t = 2 s`. Both inputs `PRINTED` (§2 step 3). Arithmetic consumes them (§2 step 4): 600/2 = 300. Paper states no precision, so the printed precision is the claim's stated precision; 300 rounds to the printed numeral 300 (rounding half away from zero). Second concrete input under the option-(c) wording: paperB.md prints "the growth rate is 0.87" as its own result from `g = β·x`, printing `β = 1/2` "adopted for this calculation" and `x = 1.74`; β's numeral is excluded as `AUTHOR_SPECIFIED_INPUT`, but the claim is included, β's ledger record is `PRINTED` with `origin` `CHOSEN` (`ORIG_CHOICE_STATED` quotation), the arithmetic consumes it (status, not origin, gates consumption), 0.5 × 1.74 = 0.87 reproduces; `rests_on` is computed by script as `USES_CHOSEN` beside the verdict. | §1 include → §2 steps 1–3 (`PRINTED`) → §2 step 4 mechanical attempt → §3 `REPRO_WITHIN_STATED_PRECISION` with the stated-precision/rounding rule → §2 step 5 record outcome; script records `rests_on`. No earlier terminal condition holds. | yes |
| `REPRO_FAILED` | paperC.md prints "the flow speed is 350 km/s" as its own result; states `v = d/t`; prints `d = 600 km`, `t = 2 s`. Inputs sufficient and all `PRINTED`; the attempt completes: 600/2 = 300 ≠ 350; no stated uncertainty, and 300 does not round to 350 at the printed precision. | §1 include → §2 steps (all `PRINTED`, derivation stated, attempt evaluable) → §3 `REPRO_FAILED` ("unreproduced from the stated inputs", both numbers reported, `rests_on` beside it); precedence: none of the four earlier terminals holds. | yes |
| `REPRO_BLOCKED` | paperD.md prints "the optical depth is 0.054" as its own result and states the equation that produces it; the equation needs input `S`; `S`'s value is not printed; the paper names a source. Limb (i): the named source is NOT an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md` (an external proceedings volume). Limb (ii): the named source IS an enumerable pinned text, but the value does not machine-match as a numeric token at the cited line. Both limbs: record status `BLOCKED`, `origin` `IMPORTED`, `ORIG_CITATION` evidence quoted at the claiming paper's naming sentence, no value; never consumed. Input and source named. | §1 include → §2 step 3 `BLOCKED` → §2 import rule's final sentence ("If the named source is not enumerable or the value does not match there, file `REPRO_BLOCKED` under §3") + "A seat may not supply a value for an `ABSENT` or `BLOCKED` input" → §3 `REPRO_BLOCKED`; precedence: a derivation IS stated, so `REPRO_NO_DERIVATION_STATED` does not preempt. | yes |
| `REPRO_NOT_EVALUABLE` | Timeout limb: paperE.md prints "the invariant is 42.0" as its own result and states a procedure (a stiff coupled symbolic system); all inputs `PRINTED`; evaluation under `/usr/bin/python3 -E r3c2_timeout.py 120.0 -- <command>` exceeds the monotonic deadline; the wrapper prints `SYMBOLIC_TIMEOUT` and exits 124. Machinery limb: paperF.md's stated procedure requires machinery the lane does not have (a numerical-relativity integrator); `MACHINERY_UNAVAILABLE` printed with the point reached. | §1 include → §2 steps (derivation stated, inputs `PRINTED`, attempt begins) → §3 `REPRO_NOT_EVALUABLE`, printing `SYMBOLIC_TIMEOUT` or `MACHINERY_UNAVAILABLE` and the point reached; §9 wrapper supplies the timeout signal; §4 class 2 permits one repeat. Precedence: no earlier terminal holds. | yes (both limbs) |
| `REPRO_NO_DERIVATION_STATED` | paperG.md line 12 prints "the likelihood is 0.87" asserted as its own result; the paper states no equation or computational procedure that could produce it — only "obtained with the standard pipeline", a procedure named but not specified. Nothing to attempt; the passage is named. | §1 include (a printed numeral asserted as the paper's own result) → §2 step 1 finds no equation → §3 `REPRO_NO_DERIVATION_STATED` (the named-but-unspecified sentence files this class) → §3 precedence: first in order, so it files even where inputs would also be absent. | yes |
| `REPRO_INPUT_ABSENT` | paperH.md prints "the age is 13.8 Gyr" as its own result and states `t = 2/(3·H₀·√Ω_Λ)`; the paper nowhere prints `H₀` and names no source for it. `STANDARD` is barred: §2 step 3 — "`STANDARD` applies only when the value appears in the claiming paper ... a value the paper does not print is classified by the named-source rule alone and is never `STANDARD`." No named source → `ABSENT`. The input (`H₀`) is named. | §1 include → §2 step 3 `ABSENT` → §2 "A seat may not supply a value for an `ABSENT` ... input. Encountering one ends that claim's attempt." → §3 `REPRO_INPUT_ABSENT`; precedence: `REPRO_BLOCKED` is earlier but inapplicable (no source is named). | yes |

All six §3 outcomes: REACHABLE.

## (B) Study-level classes of §4 — all eight exhibited

Corpus frame for rows 1–3: the pinned corpus of 89 enumerable texts yields, after two agreeing enumerations,
150 included claims and 600 excluded candidates, both seats' ledgers concordant; controls C0–C5b PASS in both
seats; `C1B_BATCH_COVERAGE=PASS`; `JOIN=PASS`.

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `CENSUS_COMPLETE` | In the frame above: every one of the 150 included claims states a derivation; every input is `PRINTED` or `STANDARD` (imports machine-match at the first line carrying both symbol and numeral of an enumerable manifest text whose bytes verify); every attempt completes within the cap; each claim files `REPRO_WITHIN_STATED_PRECISION` or `REPRO_FAILED`; both seats' outcomes and `origin` classifications agree; C6: the auditor's independent enumeration of all 89 texts matches the sealed ledgers row for row (every completeness row `MATCH`, no `OMISSION`, dispute rate ≤ 10%, no audited claim or origin `MISMATCH`), both seals match, the external seed is supplied and the recomputed selection matches → `C6_AUDIT_SAMPLE=PASS`. Denominator 150 > 0. | §4 class 1: "every included claim carries exactly one outcome from the arithmetic group of §3, with `C6_AUDIT_SAMPLE=PASS`"; the zero-denominator bar is not triggered; §4 precedence: no earlier class's condition holds. | yes — see the dedicated section on the suspicion below |
| `CENSUS_PARTIAL` | Input A (non-arithmetic claim): the frame above with claim #77 = paperD's optical-depth claim, which files `REPRO_BLOCKED`; the audit still passes (the auditor re-derives the sampled claims and all rows match). Input B (zero denominator): a corpus of 89 genuinely numeral-free prose texts — no equation numbers, dates, page numbers or values — so both enumerations list ZERO candidate passages, the union is empty, C6's "any passage on either side" clause does not fire, R = 0 makes the sample empty, the audit passes vacuously, and the sealed denominator is 0. | §4 class 2: "at least one included claim carries a non-arithmetic outcome ..., or the denominator is zero"; "A denominator of zero files `CENSUS_PARTIAL` with the empty enumeration named; no census is complete over nothing"; "INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`." Precedence: `CENSUS_AUDIT_FAILED` does not hold (audit PASS in both inputs). | yes (both limbs) |
| `CENSUS_AUDIT_FAILED` | Exhibited through EIGHT independent paths in the dedicated sub-table below, including each new V26 C6 path. | §4 class 3 + C6's omission/dispute/zero-denominator clauses + the seed clause + §7's receipt clause. Precedence: sits before `CENSUS_PARTIAL`/`CENSUS_COMPLETE`, after the dispute classes. | yes (every named path) |
| `R3C2_NO_CLASS` | Input A (control fails in every seat after two attempts): C5's fifth command (`r3c2_manifest.py` over the printed site-packages) prints `ERROR=<path>` on an unreadable file in BOTH seats, each after two attempts → `C5_HARNESS_PINNED=FAIL` in every seat that attempted it. Input B (pre-dispatch): the pinned builder's forbidden-list assertion finds a surviving string in the built packet → the packet is not written, `C4_PACKET_REDACTED=FAIL` before dispatch. | §4 class 4: "a control among C0 through C5b fails in every seat that attempted it after two attempts; a packet or seat-isolation failure before dispatch files this class." Boundary respected: a C6 audit failure or seal-receipt failure files `CENSUS_AUDIT_FAILED`, not this class. Precedence: first. | yes |
| `CENSUS_DENOMINATOR_DISPUTED` | Input A (enumeration split): seat A lists passage (paperL.md, line 9, "2018") as an included claim; seat B lists it excluded, kind `DATE`; two reconciliation attempts fail — tolerance zero, measured in candidate passages. Input B (input-list split, the C3/merge limb): both seats agree on every candidate; for agreed claim paperM.md#c3, seat A's ledger lists inputs {d, t} and seat B's lists {d, t, H₀}; `merge` exits 1; the one reconciliation against the paper's stated equation does not resolve it. | §1: disagreement surviving two reconciliation attempts stops the study under this class; §4 class 5: "... or the two seats' input lists for the agreed claims disagree after the one C3 reconciliation"; C3: "`merge` exits 1 if the two `input_id` sets differ — ... an input-set difference surviving that reconciliation stops the study under `CENSUS_DENOMINATOR_DISPUTED`". The census does not proceed; disputed candidates/inputs listed. | yes (both limbs) |
| `CENSUS_OUTCOME_DISPUTED` | Agreed included claim paperN.md#c5 prints "the age is 13.8 Gyr" with no stated precision; the reproduced value is 13.797. Seat A files `REPRO_WITHIN_STATED_PRECISION` (13.797 rounds to the printed 13.8 at the printed precision); seat B files `REPRO_FAILED` (misapplying the precision rule). The one reconciliation against the printed numeral and the stated-precision rule of §3 does not resolve the split. | §2 step 5: "a disagreement surviving that reconciliation files `CENSUS_OUTCOME_DISPUTED` (§4)"; §4 class 6: the census does not proceed; the claim is listed with both seats' outcomes, both number pairs, and the step each seat reached. | yes |
| `CENSUS_ORIGIN_DISPUTED` | Denominator 40 included claims. On the sentence "We adopt H₀ = 67.4 from Source X (2018)", seat A files `origin` `CHOSEN` (`ORIG_CHOICE_STATED`) and seat B files `IMPORTED` (`ORIG_CITATION` — "a sentence that names an external source for the value is a citation whatever else it says"); similar splits affect inputs on 5 of 40 claims = 12.5% > 10%. Contrast (not the class): disagreements affecting ≤ 10% are filed per-input `ORIGIN_DISPUTED`, reported with both classifications and both quotations, `rests_on` computed as a `DISPUTED` pair, and the census proceeds. | C3: every input's `origin` classified independently by both seats, with the reason-code precedence → C6: "Above 10% of included claims, `CENSUS_ORIGIN_DISPUTED`" → §4 class 7: every disputed input listed with both seats' classification and both quotations; never reconciled; the census does not proceed. | yes |
| `CENSUS_CONTROL_SPLIT` | The C2/C3 `validate` run: seat A's ledger passes (exit 0); seat B's ledger fails (a `PRINTED` value does not machine-match its cited source line) — each after two attempts. | §4 class 8: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not adopt the passing seat's result." Precedence: second, after `R3C2_NO_CLASS` (which requires failure in EVERY seat). | yes |

All eight §4 classes: REACHABLE.

## (B-supplement) `CENSUS_AUDIT_FAILED` through each new V26 C6 path — required exhibits

| # | path | concrete input | clause (verbatim anchor) | reachable |
|---|---|---|---|---|
| 1 | audit cannot reproduce a sampled outcome | Sampled claim sealed `REPRO_WITHIN_STATED_PRECISION`, printed 300 / reproduced 300; the auditor's sealed re-derivation yields 290 → `MISMATCH` in `C6_AUDIT.json`. | §4 class 3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger"; C6 PASS predicate requires "no audited claim or origin is `MISMATCH`". | yes |
| 2 | NEW C6 — sealed-included absent from the auditor | The sealed candidate file includes passage (paperJ.md, line 42, "300") as INCLUDED; the auditor's complete independent enumeration of all 89 texts never lists that passage in either disposition → completeness row `OMISSION`. | C6: "Omissions: a sealed INCLUDED passage absent from the auditor's enumeration ... each is ledger incompleteness and files `CENSUS_AUDIT_FAILED`." | yes |
| 3 | NEW C6 — auditor-listed absent from the sealed ledgers | The auditor lists passage (paperK.md, line 7, "0.87") — included or excluded — and the sealed ledgers omit it entirely → `OMISSION` in the other direction. | C6: "a passage the auditor lists (included OR excluded) that the sealed ledgers omit — each is ledger incompleteness and files `CENSUS_AUDIT_FAILED`." | yes |
| 4 | NEW C6 — dispute rate above 10% | Sealed included denominator 50; 6 passages are disposed differently (sealed EXCLUDED/`EQUATION_NUMBER` vs auditor INCLUDED, or sealed-excluded passages absent from the auditor) → `AUDIT_INCLUSION_DISPUTED` count 6 → 12% > 10%. (At or below 10% the count is reported and the audit can still PASS.) | C6: "above 10% of the sealed included denominator the audit files `CENSUS_AUDIT_FAILED`; at or below it the count is reported." | yes |
| 5 | NEW C6 — seedless selection | The tally is receipted; the external custodian never supplies the 64-lowercase-hex seed (equivalently: `audit select` refuses for lack of the stage-1 seal). The audit does not run. | C6: "If the seed is not supplied and recorded with the receipt, the audit does not run, `C6_AUDIT_SAMPLE=NOT_RUN`, and the study files `CENSUS_AUDIT_FAILED` with the missing seed named." | yes |
| 6 | NEW C6 — zero denominator with passages on either side | The sealed denominator is 0 (the sealed side excluded all 30 candidate passages) while the auditor lists those 30 passages (any dispositions — even full agreement as exclusions). The audit fails although the two sides match row for row. | C6: "A sealed denominator of zero with any passage on either side fails." → not PASS → §4 class 3 ("does not run to PASS for any cause (the cause named)"). Note the routing contrast: under §4 precedence this numeral-bearing zero-denominator corpus files `CENSUS_AUDIT_FAILED`, while the numeral-FREE zero-denominator corpus of row (B,2) Input B files `CENSUS_PARTIAL`. Both routings are the text as it stands. | yes |
| 7 | seal receipt verification fails | After opening, Blanc's independent re-hash of the tally mismatches receipt T (or receipt P is missing). | §4 class 3: "or the receipt verification of the seal fails"; §7: "Any missing receipt or mismatch files `CENSUS_AUDIT_FAILED` ... leaves the interpretation `NOT_RUN` and voids the comparison." | yes |
| 8 | audit does not run to PASS for any other cause | `C6_AUDIT.json` is never written or never printed (artefact absent), so the PASS predicate's first clause fails. | §4 class 3: "or does not run to PASS for any cause (the cause named)"; C6: "`C6_AUDIT_SAMPLE=PASS` only if the artefact exists and is printed ...". | yes |

## (B-supplement) Seat tally stopped by the new C1B controls — required exhibits

| stop condition | concrete input | clause path | reachable |
|---|---|---|---|
| `C1B_BATCH_COVERAGE=FAIL` stops the seat's tally | The pinned 12-batch partition of `R3C2_CORPUS_MANIFEST.md` assigns text T_07 to batch 3 AND to batch 5 (a text not owned by exactly one batch); alternatively: a session's copy of T_12 fails byte verification against its manifest row; alternatively: `SEAT_REPORT_b4.md` lacks the packet's `ACCESS_SHA` line. | C1B: "`C1B_BATCH_COVERAGE=PASS` iff every manifest text is owned by exactly one batch, every owned text's bytes verify against its manifest row, and every batch report prints the packet's `ACCESS_SHA` ... Either FAIL stops the seat's tally." Study-level routing of the stop: as a control failure it reaches §4 through `R3C2_NO_CLASS` (both seats, two attempts) or `CENSUS_CONTROL_SPLIT` (one seat) — both exhibited above. | yes |
| `JOIN=FAIL` stops the seat's tally | Batch 4's seal record names a predecessor digest that does not equal batch 3's actual seal (the ordered predecessor chain is not intact from a root with no predecessor); alternatively: the joined candidate file carries id `paperX#c2` although paperX is owned by batch 7, not by the batch that produced it; alternatively: two batches emit the same claim id (identifiers not unique). | C1B: "`JOIN=PASS` iff every seal matches, the ordered predecessor chain is intact from a root with no predecessor, every candidate and ledger claim is owned by its batch, every evidence source is a manifest text, identifiers are unique and every `derived_from` resolves acyclically. Either FAIL stops the seat's tally." Same study-level routing as above. | yes |

## (C) The suspicion, answered directly: is `CENSUS_COMPLETE` reachable?

REACHABLE.

What is true in the suspicion: on any corpus that contains even one blocked, absent-input, no-derivation-stated,
or not-evaluable included claim, `CENSUS_COMPLETE` cannot file. The routing is exact: such a claim files one of
the four non-arithmetic §3 outcomes (§3 precedence puts the arithmetic group last, so a claim holding an earlier
terminal condition never lands in the arithmetic group); §4 class 2's condition — "at least one included claim
carries a non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`,
`REPRO_NOT_EVALUABLE`), or the denominator is zero" — then holds; and the §4 precedence files `CENSUS_PARTIAL`
before `CENSUS_COMPLETE` is ever consulted ("INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`").
A single such claim anywhere in the corpus is sufficient. That is the design's stated intent, not a hidden defect.

Why that does not make the class unreachable: C0's question is whether an input EXISTS that files the verdict,
and the class's own definition contains no self-defeating clause. Its requirements are jointly satisfiable, and
row (B,1) exhibits the satisfying input concretely: a corpus in which every included claim states a derivation,
prints or import-matches every input its equation needs (imports machine-matching at the first line carrying
both symbol and numeral of an enumerable manifest text), evaluates within the 120-second cap, and files
`REPRO_WITHIN_STATED_PRECISION` or `REPRO_FAILED`; both seats agree throughout; and the strengthened V26 audit
returns `C6_AUDIT_SAMPLE=PASS` because the auditor's enumeration matches the sealed ledgers row for row, the
seals match, the seed is supplied, and the recomputed selection matches. Note that `REPRO_FAILED` is itself in
the arithmetic group, so the class does not even require every paper to be right — only every claim to be
attempted and answered arithmetically.

Whether the REAL pinned corpus of 89 texts contains even one non-arithmetic claim is the empirical question the
census exists to answer. The text settles reachability in the affirmative; it does not settle, and C0 does not
prejudge, the corpus. This agrees with the document's own C0 history (§10.3: both blind seats marked
`CENSUS_COMPLETE` reachable) and with §5 C0's framing, which names exactly this fragility — "a single blocked
or absent input in the whole corpus is enough to prevent" it — as the reason to check early, not as a blocking
clause.

## Did any §3 outcome or §4 class become UNREACHABLE because of the three unchosen texts?

No. Checked text by text:

1. §2 import rule (D1 wording B). It narrows the import route — value machine-matched as a numeric token at the
   FIRST line carrying both symbol and numeral of a byte-verified enumerable manifest text, evidence quoted at
   the claiming paper's naming sentence. `REPRO_WITHIN_STATED_PRECISION` via an import remains reachable (the
   value matches at the first symbol-and-numeral line → `PRINTED`/`IMPORTED`, consumed). `REPRO_BLOCKED` keeps
   both limbs ("not enumerable", "does not match there"); a seat that cites a later matching line commits a
   `validate` control failure (C2/C3), which is a control path, not the loss of any §3 outcome's last path.
   Nothing §3 declares lost a route.
2. C6 (stronger D7 audit). It only ADDS routes into `CENSUS_AUDIT_FAILED` (paths 2–6 above, all reachable), and
   `C6_AUDIT_SAMPLE=PASS` remains exhibitable by a concordant input (row B,1), so the two audit-gated tally
   classes (`CENSUS_COMPLETE`, `CENSUS_PARTIAL`) keep their paths. The new zero-denominator audit clause re-routes
   one corpus shape (numeral-bearing, all-excluded) from `CENSUS_PARTIAL` to `CENSUS_AUDIT_FAILED`, but
   `CENSUS_PARTIAL`'s zero-denominator limb remains reachable through the numeral-free corpus (row B,2 Input B).
3. C1/C1B ownership batching. It adds two stop conditions on a seat's tally; both are reachable (exhibited above)
   and both route to already-reachable §4 classes (`R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`). `C1B_BATCH_COVERAGE=PASS`
   and `JOIN=PASS` remain exhibitable (exact partition, verified bytes, intact chain), so no tally-dependent
   class loses its only path.

No §3 outcome and no §4 class is UNREACHABLE under the integrated text.

## UNREACHABLE verdicts and their blocking clauses

None. Every declared §3 outcome (six of six), every declared §4 class (eight of eight), every named new C6 path
into `CENSUS_AUDIT_FAILED` (five of five, plus the two §4 limbs), and both C1B stop conditions were exhibited
with a concrete input and a clause path. There is no unreachable verdict in this exhibition, so there is no
blocking clause to quote.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V26CAND_KIMI_COMPLETE

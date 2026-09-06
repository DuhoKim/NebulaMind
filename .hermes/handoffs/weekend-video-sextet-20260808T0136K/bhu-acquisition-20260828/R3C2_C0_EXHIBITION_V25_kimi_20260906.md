ACCESS_SHA=ab6352d35a0e02fbc92173971ada554230ad5fb0578440a9728fc0f1494942e7
C0_REACHABILITY=PASS

R3C2 — C0 REACHABILITY EXHIBITION, V25 (living draft)
Seat: kimi (authoring seat). Date: 2026-09-06.
Target document: R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md, read from disk in full (1,175 lines),
hash proven above. No other file in this directory was read or consulted.

Scope of this artefact: exhibition only. This is not a gate, not a freeze decision, and not a
judgement of the physics or the design's quality. It answers one question for every declared
per-claim outcome (§3) and every declared study-level class (§4): can this verdict occur — is
there a concrete input that the document's own clauses route to it? The §3 definition is treated
exactly as it stands under the adopted ruling (option (c): one pass, two tallies;
REPRO_AFTER_CHOICE retired into the script-computed rests_on field). There is no held clause.

What the document declares, as it stands at V25:

§3 per-claim outcomes (six): REPRO_WITHIN_STATED_PRECISION, REPRO_FAILED, REPRO_BLOCKED,
REPRO_NOT_EVALUABLE, REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT. The arithmetic group is
"exactly REPRO_WITHIN_STATED_PRECISION and REPRO_FAILED". Per-claim filing precedence:
"Exactly one outcome is filed per claim. Where more than one terminal condition holds, file the
first in this order: REPRO_NO_DERIVATION_STATED, REPRO_BLOCKED, REPRO_INPUT_ABSENT,
REPRO_NOT_EVALUABLE, then the arithmetic group."

§4 study-level classes (eight): CENSUS_COMPLETE, CENSUS_PARTIAL, CENSUS_AUDIT_FAILED,
R3C2_NO_CLASS, CENSUS_DENOMINATOR_DISPUTED, CENSUS_OUTCOME_DISPUTED, CENSUS_ORIGIN_DISPUTED,
CENSUS_CONTROL_SPLIT. Study-level filing precedence: "Exactly one study-level outcome is filed.
Where more than one condition holds, file the first in this order: R3C2_NO_CLASS,
CENSUS_CONTROL_SPLIT, CENSUS_DENOMINATOR_DISPUTED, CENSUS_OUTCOME_DISPUTED,
CENSUS_ORIGIN_DISPUTED, CENSUS_AUDIT_FAILED, CENSUS_PARTIAL, CENSUS_COMPLETE. Once a stop class
applies, later limbs are unreached and their controls are NOT_RUN."

All arithmetic in the exhibitions below was machine-verified by this seat (decimal arithmetic,
rounding half away from zero, matching §3's rule).

════════════════════════════════════════════════════════════════════════════
(A) §3 PER-CLAIM OUTCOMES — exhibition table
════════════════════════════════════════════════════════════════════════════

verdict | concrete input | clause path | reachable
--------+---------------------------------------------------------------
REPRO_WITHIN_STATED_PRECISION | Paper A prints, as its own result: "with Ω_m = 0.3153 and
h = 0.6736 we obtain Ω_m h² = 0.1431", stating the recipe (multiply) and no uncertainty.
Inputs: Ω_m (printed at A's line) → status PRINTED; h (printed) → PRINTED. | §1 (printed
numeral asserted as the paper's own result → included claim) → §2 step 1 (extract 0.1431,
units dimensionless, recipe, file/line) → step 2 (inputs Ω_m, h) → step 3 (both PRINTED) →
step 4 (mechanical attempt: 0.3153 × 0.6736² = 0.143063263488) → §3 REPRO_WITHIN_STATED_PRECISION:
"the paper's number follows, within its own stated precision, from the paper's own recipe
applied to the inputs it states (PRINTED or STANDARD)". Stated-precision rule: "Where the paper
states no precision for the claim, the printed precision is the claim's stated precision: the
reproduced value must round to the printed numeral at that precision, rounding half away from
zero." 0.143063263488 rounds to 0.1431 at 4 dp = printed numeral → filed. Both numbers
reported; rests_on computed by script beside it (§3 arithmetic-group note). Uncertainty variant:
paper prints "H₀ = 73.2 ± 1.3" with a stated recipe yielding 73.04 → "|reproduced − printed| ≤
the stated uncertainty, taken once": |73.04 − 73.2| = 0.16 ≤ 1.3 → filed. | YES
--------+---------------------------------------------------------------
REPRO_FAILED | Paper B prints, as its own result: "with Ω_m = 0.3153 and h = 0.6736 we obtain
Ω_m h² = 0.1426". Same recipe, same PRINTED inputs; the arithmetic gives 0.143063263488, which
rounds to 0.1431 ≠ 0.1426. | §1 → §2 steps 1–4 as above (inputs sufficient, all
PRINTED/STANDARD, attempt completes) → §3 REPRO_FAILED: "the inputs the paper states are
sufficient for its recipe, but the arithmetic does not give the paper's number. Report both
numbers." Uncertainty variant: printed "74.9 ± 1.3", reproduced 73.04 → |74.9 − 73.2| = 1.7 >
1.3 → filed. | YES
--------+---------------------------------------------------------------
REPRO_BLOCKED | Paper C prints, as its own result: "adopting the gas fraction of Vikhlinin
et al. (2009), we derive f_500 = 0.116". The f_gas value is not printed anywhere in C; the
named source Vikhlinin et al. (2009) is not an enumerable text in R3C2_CORPUS_MANIFEST.md.
Variant limb: the named source IS enumerable-pinned, but the value does not machine-match at
the cited line (or the source is listed RAW — "Files listed there as RAW are not enumerable
and are outside the census", §2). | §1 → §2 steps 1–3 (input f_gas: not printed; named-source
rule of §2: "only when such a match exists; a cited value that does not machine-match at the
named source's cited line, or whose named source is not an enumerable text of the manifest,
files REPRO_BLOCKED under §3") → §3 REPRO_BLOCKED: "an input whose value the claiming paper
does not print, and for which the claiming paper names a source (a citation) that either is
not an enumerable text pinned in R3C2_CORPUS_MANIFEST.md or is an enumerable pinned text at
whose cited line the value does not machine-match; in the first case whether that source is
obtainable elsewhere is irrelevant, because the census may not open or consume it." Recorded
status BLOCKED under C3 (origin IMPORTED, ORIG_CITATION, no value); "A seat may not supply a
value for an ABSENT or BLOCKED input. Encountering one ends that claim's attempt" (§2). | YES
--------+---------------------------------------------------------------
REPRO_NOT_EVALUABLE | Paper D prints, as its own result: "our 10⁷-sample chain gives
σ₈ = 0.811", stating a recipe whose faithful execution exceeds 120 seconds; the §9 wrapper
r3c2_timeout.py "enforces a 120.0-second wall-clock deadline … on the deadline prints
SYMBOLIC_TIMEOUT and exits 124". Machinery limb: Paper E's claim requires a Boltzmann solver
this lane does not have. | §1 → §2 steps 1–4 (attempt launched through the wrapper; deadline
hits) → §3 REPRO_NOT_EVALUABLE: "the arithmetic could not be completed within the 120-second
cap, or requires machinery this lane does not have. Print SYMBOLIC_TIMEOUT when the 120-second
cap is exceeded, or MACHINERY_UNAVAILABLE when the lane lacks the machinery, and the point
reached." §4.2 permits one repeat, "meaningful only for REPRO_NOT_EVALUABLE". | YES
--------+---------------------------------------------------------------
REPRO_NO_DERIVATION_STATED | Paper F prints, as its own result: "we find a 3.2σ tension
between our measurement and the early-universe fit", and nowhere states an equation or
computational procedure producing 3.2σ. Named-but-unspecified variant: "the number was
obtained with our standard pipeline" — "a sentence that says where the number came from
without stating operations a seat could attempt". | §1 (printed numeral asserted as the
paper's own result → included; §1 needs no recipe) → §2 step 1 finds no equation to extract →
§3 REPRO_NO_DERIVATION_STATED: "the paper prints the claim as its own result but states no
equation or computational procedure that could produce it, so there is nothing to attempt.
Name the passage. A procedure named but not specified … states no computational procedure that
could produce it; file this class and name the passage." No ledger records → rests_on
NOT_COMPUTED (§3 arithmetic-group note). | YES
--------+---------------------------------------------------------------
REPRO_INPUT_ABSENT | Paper G prints, as its own result: "from t₀ = 1/H₀ we obtain
t₀ = 14.5 Gyr", stating the equation but printing no value for H₀ and citing no source for
it. | §1 → §2 steps 1–3 (input H₀: not printed; traced to no named source → "neither printed
nor traced to any named source"; the §2 step-3 STANDARD clause bars back-filling from C3's
closed list: "a value the paper does not print is classified by the named-source rule alone
and is never STANDARD") → §2: "A seat may not supply a value for an ABSENT or BLOCKED input.
Encountering one ends that claim's attempt." → §3 REPRO_INPUT_ABSENT: "an input the equation
needs is ABSENT from the paper — neither printed nor traced to any named source — so the
attempt stops there. Name the input." (H₀ named.) | YES

§3 declared precedence, exhibited (declared condition): Paper H's claim has both a BLOCKED
input (named source outside the manifest) and an ABSENT input (no source named) → both terminal
conditions hold → "file the first in this order" → REPRO_BLOCKED. Paper I states no derivation
and would also lack inputs → REPRO_NO_DERIVATION_STATED first. The order is total: the
arithmetic group is filed only when none of the four earlier conditions holds. REACHABLE (the
precedence resolves every co-occurrence to exactly one outcome).

════════════════════════════════════════════════════════════════════════════
(B) §4 STUDY-LEVEL CLASSES — exhibition table
════════════════════════════════════════════════════════════════════════════

verdict | concrete input | clause path | reachable
--------+---------------------------------------------------------------
CENSUS_COMPLETE | Pinned corpus enumeration (both seats agree) yields N = 3 included claims:
C1 = Paper A's "Ω_m h² = 0.1431" (→ REPRO_WITHIN_STATED_PRECISION), C2 = Paper B's
"Ω_m h² = 0.1426" (→ REPRO_FAILED), C3 = Paper J's "the age is 13.8 Gyr" (recipe stated,
inputs PRINTED/STANDARD, reproduced 13.797 → rounds to 13.8 → REPRO_WITHIN_STATED_PRECISION).
No included claim carries a non-arithmetic outcome. Controls C1–C5b PASS in both seats;
enumerations agree; per-claim outcomes agree (no surviving dispute); origin disagreements
affect ≤ 10% of claims; receipts P and T verify; the external custodian supplies the seed;
the C6 auditor re-derives every arithmetic-group claim — all three; the remaining set is
empty so the (ii) sample is empty: "when R is zero the sample is empty and every included
claim is already audited under (i)" — and returns MATCH everywhere with no ledger
incompleteness → C6_AUDIT_SAMPLE=PASS. | §4.1: "every included claim carries exactly one
outcome from the arithmetic group of §3, with C6_AUDIT_SAMPLE=PASS." Denominator 3 ≠ 0.
Precedence walk: no control failure (not R3C2_NO_CLASS), no split (not CENSUS_CONTROL_SPLIT),
enumerations agree (not CENSUS_DENOMINATOR_DISPUTED), outcomes agree (not
CENSUS_OUTCOME_DISPUTED), origins agree within 10% (not CENSUS_ORIGIN_DISPUTED), audit PASS
and receipts verify (not CENSUS_AUDIT_FAILED), no non-arithmetic outcome and denominator
non-zero (not CENSUS_PARTIAL) → file CENSUS_COMPLETE; "Report the full tally with its
denominator, and the rests_on tally beside it — two tallies from one pass." | YES
--------+---------------------------------------------------------------
CENSUS_PARTIAL | Path (a): the 3-claim corpus above with C3 replaced by Paper G's
"t₀ = 14.5 Gyr" claim, which files REPRO_INPUT_ABSENT. Path (b): enumeration includes zero
claims — every enumerated candidate is excluded (equation numbers, dates,
AUTHOR_SPECIFIED_INPUT numerals, attributed-not-derived values only). | §4.2: "after the §2
attempt (one repeat permitted, meaningful only for REPRO_NOT_EVALUABLE), at least one included
claim carries a non-arithmetic outcome (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT,
REPRO_BLOCKED, REPRO_NOT_EVALUABLE), or the denominator is zero. Report each and why.
INCONCLUSIVE, and it takes precedence over CENSUS_COMPLETE." Path (b) also matches §4.1's own
sentence: "A denominator of zero files CENSUS_PARTIAL with the empty enumeration named; no
census is complete over nothing." | YES (two independent paths)
--------+---------------------------------------------------------------
CENSUS_AUDIT_FAILED | Path (a): the C6 auditor, re-deriving sampled claim C2 without sight of
earlier work, obtains a reproduced value that rounds to 0.1431 while the sealed record says
REPRO_FAILED — "any outcome the audit cannot reproduce" (C6) → MISMATCH in C6_AUDIT.json.
Path (b): after receipt T the external custodian never supplies the seed. Path (c): Blanc's
post-opening re-hash of the tally or the protocol mismatches receipts P/T. | §4.3: "the audit
of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any
cause (the cause named), or the receipt verification of the seal fails. No tally is filed;
report which." Path (b) routes via C6: "If the seed is not supplied and recorded with the
receipt, the audit does not run, C6_AUDIT_SAMPLE=NOT_RUN, and the study files
CENSUS_AUDIT_FAILED with the missing seed named." Path (c) routes via §7: "Any missing
receipt or mismatch files CENSUS_AUDIT_FAILED." §4.4's carve-out confirms the routing: "A C6
audit failure or a seal-receipt failure files CENSUS_AUDIT_FAILED, not this class
[R3C2_NO_CLASS]." | YES (three independent paths)
--------+---------------------------------------------------------------
R3C2_NO_CLASS | Path (a): both seats' C1 census runs exit non-zero after two attempts each —
each seat's candidate file independently declares declared_candidate_count = 41 while the
script recomputes 40 from the rows (a PENDING disposition left in each), so "PASS requires
exit 0" fails in every seat that attempted it. Path (b), pre-dispatch: the packet builder's
forbidden-list assertion finds a surviving forbidden string → "If any survives, the packet is
not written and C4_PACKET_REDACTED=FAIL"; the study does not proceed on a hand-checked copy. |
§4.4: "a control among C0 through C5b fails in every seat that attempted it after two
attempts; a packet or seat-isolation failure before dispatch files this class." First in the
§4 precedence, so it is filed ahead of any co-holding class. | YES (two independent paths)
--------+---------------------------------------------------------------
CENSUS_DENOMINATOR_DISPUTED | Path (a): Seat A includes passage paperK.tex:212 ("the age is
13.8 Gyr") as the paper's own result; Seat B excludes the same passage as
ATTRIBUTED_NOT_DERIVED; the disagreement survives two reconciliation attempts (§6: "tolerance
zero, measured in candidate passages"). Path (b): enumerations agree, but for agreed claim C7
Seat A's input list is {H₀} and Seat B's is {H₀, Ω_Λ}; "merge exits 1 if the two input_id
sets differ"; the one reconciliation against the paper's stated equation fails. | §1: "Inclusion
is assigned independently by the two independent seats from the §1 rule alone; disagreement on
any candidate that survives two reconciliation attempts stops the study under
CENSUS_DENOMINATOR_DISPUTED (§4)". §4.5: "the two enumerations disagree after two
reconciliation attempts, or the two seats' input lists for the agreed claims disagree after
the one C3 reconciliation. The census does not proceed; the disputed candidates or inputs are
listed." Path (b) also via C3's merge clause. | YES (two independent paths)
--------+---------------------------------------------------------------
CENSUS_OUTCOME_DISPUTED | Agreed included claim C1 = Paper A's "Ω_m h² = 0.1431". Seat A
transcribes h = 0.6736, computes 0.143063263488 → rounds to 0.1431 → files
REPRO_WITHIN_STATED_PRECISION. Seat B mis-transcribes h = 0.6674, computes 0.140441796228 →
rounds to 0.1404 ≠ 0.1431 → files REPRO_FAILED. The one reconciliation against the printed
numeral and the stated-precision rule of §3 does not resolve it (each seat stands by its
reading of the printed h). | §2 step 5: "a disagreement surviving that reconciliation files
CENSUS_OUTCOME_DISPUTED (§4)". §4.6: "the two seats' filed per-claim outcomes on an agreed
included claim differ after one reconciliation against the printed numeral and the
stated-precision rule of §3. The census does not proceed; the claim is listed with both
seats' outcomes, both number pairs, and the step each seat reached." | YES
--------+---------------------------------------------------------------
CENSUS_ORIGIN_DISPUTED | N = 10 included claims. On claims C3 and C8 the seats' independent
origin classifications disagree: for C3's β input Seat A files CHOSEN (ORIG_CHOICE_STATED on
"we set β = 1/929.25"), Seat B files IMPORTED (ORIG_CITATION on a different sentence naming a
source for β). Disputes are "reported, never reconciled". Affected claims: 2 of 10 = 20%
(strictly more than 10%; 1 of 10 = 10% would NOT cross it — "more than 10%"). | §4.7: "the
two seats' independent origin classifications disagree on inputs affecting more than 10% of
included claims. The census does not proceed; every disputed input is listed with both seats'
classification and both quotations." The C3 reason-code tie-break governs each seat's own
filing but cannot reconcile a disagreement over which sentence evidences the value; the merged
record carries origin_alt and the claim's rests_on is computed as a DISPUTED pair (C3/C6). | YES
--------+---------------------------------------------------------------
CENSUS_CONTROL_SPLIT | Seat A's C2 run "validate ledger.json ." exits 0; Seat B's exits 1 —
B's ledger carries a field outside the C3 schema and "validate fails a ledger that carries any
other field". Two attempts each; the split persists. | §4.8: "a control fails in one seat and
passes in another after two attempts. Report both seats' outputs and stop; do not adopt the
passing seat's result." Second in the §4 precedence, after R3C2_NO_CLASS only. | YES

§4 declared precedence, exhibited (declared condition): a state in which Seat B's C2 fails
twice while Seat A's passes (CENSUS_CONTROL_SPLIT condition) AND the enumerations would have
disagreed (CENSUS_DENOMINATOR_DISPUTED condition) → file CENSUS_CONTROL_SPLIT, the earlier in
the order; "Once a stop class applies, later limbs are unreached and their controls are
NOT_RUN." A state with any non-arithmetic outcome satisfies CENSUS_PARTIAL's definition even
when every other claim is arithmetic → CENSUS_PARTIAL precedes CENSUS_COMPLETE in the order
and its own text says it "takes precedence over CENSUS_COMPLETE" — the two can never both be
filed. REACHABLE (the order is total over all eight classes).

════════════════════════════════════════════════════════════════════════════
THE NAMED SUSPICION — CENSUS_COMPLETE, answered directly
════════════════════════════════════════════════════════════════════════════

Question put to this seat: CENSUS_COMPLETE requires every included claim to carry an outcome
from the arithmetic group. In a real corpus of many papers, is there any input under which
CENSUS_COMPLETE can actually be filed — or does a single blocked, absent-input, or
no-derivation-stated claim anywhere in the corpus force CENSUS_PARTIAL, making CENSUS_COMPLETE
unreachable in practice?

Answer: REACHABLE.

The blocking direction is real, and the clauses that force it are quoted verbatim:

  §4.2: "at least one included claim carries a non-arithmetic outcome
  (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT, REPRO_BLOCKED, REPRO_NOT_EVALUABLE), or the
  denominator is zero. Report each and why. INCONCLUSIVE, and it takes precedence over
  CENSUS_COMPLETE."

  §4 precedence: "… CENSUS_AUDIT_FAILED, CENSUS_PARTIAL, CENSUS_COMPLETE."

So yes: exactly one included claim anywhere in the corpus filing REPRO_BLOCKED,
REPRO_INPUT_ABSENT, REPRO_NO_DERIVATION_STATED, or REPRO_NOT_EVALUABLE forces CENSUS_PARTIAL —
by PARTIAL's own definition, by its stated precedence over COMPLETE, and by its earlier
position in the filing order. A zero denominator also forces PARTIAL ("no census is complete
over nothing"), and COMPLETE additionally requires C6_AUDIT_SAMPLE=PASS, which itself requires
the external seed, both receipts, and a clean audit. The class is fragile by construction.

But fragile is not unreachable. No clause blocks every path: §4.1's condition is a condition
on the corpus and the run, and a concrete input satisfying it is exhibited in Table (B) row 1 —
a corpus whose every included claim states its recipe and every input its recipe needs
(printed, on C3's closed list, or machine-matched at a pinned enumerable source's cited line),
whose every attempt completes within 120 seconds with lane machinery, on which both seats agree
at every step, with the seed supplied and the audit returning PASS. Under that input the filing
order walks past all seven earlier classes and lands on CENSUS_COMPLETE. The class can occur;
whether it will occur over the real pinned corpus (89 enumerable texts, 106,676 non-blank
lines, §10.5) is an empirical question the census itself exists to answer — C0 tests
possibility, not likelihood, and possibility is exhibited.

V25-specific note: the adopted D2 exclusion kind AUTHOR_SPECIFIED_INPUT (§3: "a numeral the
paper sets rather than derives and does not assert as a result of its own: a grid size, a
cutoff, a parameter adopted 'for this calculation', a range chosen for a plot") moves
author-set numerals out of the candidate set entirely, "excluded from judgement, retained in
the record" with the count printed beside the denominator. Per §10.19 they are "no longer
forced into ATTRIBUTED_NOT_DERIVED or into the claim set where they would file as
'unreproduced' for lack of any derivation". That removes one systematic route by which real
corpora generate non-arithmetic outcomes; it does not touch the BLOCKED / ABSENT /
NOT_EVALUABLE / NO_DERIVATION routes for genuinely included claims. The suspicion's forcing
mechanism remains fully operative at V25 — it simply does not make the class unreachable.

════════════════════════════════════════════════════════════════════════════
UNREACHABLE VERDICTS AND BLOCKING CLAUSES
════════════════════════════════════════════════════════════════════════════

None. Every per-claim outcome of §3 (6 of 6) and every study-level class of §4 (8 of 8) is
exhibited above with a concrete input and a clause path through the document as it stands at
V25. There is no verdict for which the text blocks every path, so there is no blocking clause
to quote. The nearest approach to a blocker — the clause set that makes CENSUS_COMPLETE
fragile without making it unreachable — is quoted verbatim in the suspicion section above.

For the record, this document's own history contains the contrasting case: under the
pre-ruling derivation-only wording, REPRO_AFTER_CHOICE was unreachable ("the mandated attempt
may not consume that input, and no second attempt is specified", §10.3) — found by two blind
C0 seats. The ruling adopting option (c) retired that class into the script-computed rests_on
field; under the wording as it now stands, no §3 outcome and no §4 class is unreachable.

════════════════════════════════════════════════════════════════════════════
SUPPLEMENTARY DECLARED CONDITIONS (C0 covers "every declared condition")
════════════════════════════════════════════════════════════════════════════

rests_on values (script-computed by the lane tool from the merged ledger; rule stated in §3's
master-only note: "DERIVED_ONLY when every root origin is DERIVED, STANDARD or MEASURED;
otherwise the most severe root origin present, in the fixed order USES_UNDECLARED >
USES_IMPORTED > USES_FITTED > USES_CHOSEN"):

  DERIVED_ONLY — Paper A's claim with Ω_m reported as the paper's own measurement
  (ORIG_MEASURED → MEASURED) and h derived from printed quantities (ORIG_EQUATION → DERIVED,
  derived_from listed): every root origin in {DERIVED, STANDARD, MEASURED}. REACHABLE.
  USES_CHOSEN — Paper L prints "we set β = 1/929.25" and directs its use: status PRINTED, the
  arithmetic consumes it, root origin CHOSEN. REACHABLE (this is the case the retired
  REPRO_AFTER_CHOICE class could not file; under option (c) it reproduces or fails, and the
  provenance rides in rests_on).
  USES_FITTED — printed value evidenced by "obtained by fitting to X" (ORIG_FIT_STATED →
  FITTED root). REACHABLE.
  USES_IMPORTED — value printed at a pinned enumerable source's cited line, machine-matched:
  PRINTED-from-source, origin IMPORTED; arithmetic consumes it. REACHABLE.
  USES_UNDECLARED — printed value with no evidence sentence at all: "UNDECLARED is the
  default, not the residue", ORIG_SILENT with the printed origin_search. REACHABLE.
  DISPUTED — seats disagree on a claim's root origin: "computed under both classifications and
  is marked DISPUTED"; the rests_on tally reports a DISPUTED row. REACHABLE.
  NOT_COMPUTED — a REPRO_NO_DERIVATION_STATED claim has no ledger records: "a claim with no
  ledger record carries rests_on NOT_COMPUTED, and the rests_on tally reports a NOT_COMPUTED
  row." REACHABLE.

Exclusion-ledger kinds (§3: "Candidate exclusions are not per-claim outcomes"; the V25 set,
recorded with source_file, source_line, numeral, "excluded from judgement, retained in the
record, never discarded"):

  AUTHOR_SPECIFIED_INPUT — "we use a 512³ particle grid": set for the calculation, not
  asserted as a result; the census prints this kind's count beside the denominator. REACHABLE.
  ATTRIBUTED_NOT_DERIVED — "Planck reports Ω_m = 0.315 [12]", attributed, not derived.
  REACHABLE.
  DATE — "received 2024 March 1". REACHABLE.
  EQUATION_NUMBER — "(14)". REACHABLE.
  PAGE_OR_LINE_NUMBER — "see p. 1042". REACHABLE.
  REFERENCE_NUMBER — "[12]". REACHABLE.

Zero denominator (declared condition): every enumerated candidate excluded under §1 →
denominator zero → "A denominator of zero files CENSUS_PARTIAL with the empty enumeration
named; no census is complete over nothing." The vacuous-CENSUS_COMPLETE path is closed by the
text. REACHABLE as CENSUS_PARTIAL (exhibited, Table B row 2 path b).

Stop-class consequence (declared condition): "Once a stop class applies, later limbs are
unreached and their controls are NOT_RUN." Exhibited in the §4 precedence example above.
REACHABLE.

════════════════════════════════════════════════════════════════════════════
THE §1-DEFINITION DEPENDENCE (a result this exhibition is required to record)
════════════════════════════════════════════════════════════════════════════

Every exhibition above takes §1's operational definition exactly as written: a quantitative
claim is "a passage in a pinned source that prints a numeral the paper asserts as a result of
its own", with the enumerated excluded kinds. The document itself marks that boundary as
judgement-bearing rather than mechanical — §1's own parenthetical: "the audit trail records
the boundary but does not make it mechanical — whether a numeral is 'the paper's own result'
remains a judgement, so it moves from one reader to two who must agree." The reachability of
every inclusion-dependent verdict therefore inherits that judgement; the design's answer is
the two-seat agreement rule and the CENSUS_DENOMINATOR_DISPUTED stop, whose reachability is
exhibited independently in Table (B).

The dependence is demonstrated by the record, not just asserted: under the pre-ruling wording
the per-claim outcome set contained an unreachable class (REPRO_AFTER_CHOICE, §10.3); under
the settled option (c) wording it does not. This exhibition is valid against the V25 text as
it stands — option (c) adopted, no held clause — and would not transfer unchanged to a
document whose §3 definition changed again.

════════════════════════════════════════════════════════════════════════════

Summary: 6/6 §3 per-claim outcomes reachable; 8/8 §4 study-level classes reachable; the
named suspicion answered — CENSUS_COMPLETE is REACHABLE, fragile by construction but with a
concrete exhibited path; no unreachable verdict, hence no blocking clause.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V25_KIMI_COMPLETE

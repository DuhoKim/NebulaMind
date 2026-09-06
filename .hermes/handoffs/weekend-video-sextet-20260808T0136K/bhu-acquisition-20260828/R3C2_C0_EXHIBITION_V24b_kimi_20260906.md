ACCESS_SHA=972e01d122149fac1dc9d702130a20c1fdda9e73cebed338e6435beea0916115
C0_REACHABILITY=PASS

C0 REACHABILITY EXHIBITION — R3C2 reproduction census, V24 (living draft)
Seat: kimi (kimi-k3), 2026-09-06. Authoring exhibition seat; a second independent seat verifies.
Document exhibited: R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md, access-proven above (V24, living
draft, unsigned; V23 remains the signed design of record — header and §10.18). Exhibited against the
text as it stands. No other file in this directory was opened.

SCOPE OF THIS EXHIBITION
(A) §3 declares six per-claim outcomes: REPRO_WITHIN_STATED_PRECISION, REPRO_FAILED, REPRO_BLOCKED,
    REPRO_NOT_EVALUABLE, REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT.
(B) §4 declares eight study-level classes: CENSUS_COMPLETE, CENSUS_PARTIAL, CENSUS_AUDIT_FAILED,
    R3C2_NO_CLASS, CENSUS_DENOMINATOR_DISPUTED, CENSUS_OUTCOME_DISPUTED, CENSUS_ORIGIN_DISPUTED,
    CENSUS_CONTROL_SPLIT.
(C) Each is exhibited below with a concrete input and its clause path, and marked reachable yes/no.

Declared non-outcomes, no rows owed, stated so the coverage check sees them:
- REPRO_AFTER_CHOICE is RETIRED (§10.4, Duho's ruling "Q-R3C2 c", option (c): one pass, two tallies).
  Its content is the script-computed rests_on field of a REPRO_WITHIN_STATED_PRECISION or REPRO_FAILED
  claim (§3 note). Not an outcome; not exhibited.
- rests_on values (DERIVED_ONLY, USES_CHOSEN, USES_FITTED, USES_IMPORTED, USES_UNDECLARED, DISPUTED,
  NOT_COMPUTED) are computed by r3c2_lane_tools.py from the merged ledger (§3 master-only note, C3);
  they are fields, not filed verdicts. Not exhibited as outcomes.
- Candidate exclusions are "not per-claim outcomes" (§3); the five exclusion kinds live in the
  exclusion ledger under C1/C6. Not per-claim outcomes; not exhibited.
- NOT_ATTEMPTED was abolished as incoherent (§3 note). Not exhibited.

DEFINITION DEPENDENCE, STATED (per the brief's instruction that §1's core definition is treated as
marked, not read around): the document on disk carries no HELD marker on §1 or §3 — the marker was
removed at V10 when Duho ruled option (c) (§10.4: 'The HELD marker that stood over §3 since V5.1 is
removed'). The brief confirms: settled by ruling, no held clause. Every row below is exhibited against
the option (c) wording exactly as it stands: arithmetic consumes every ledger record with status
PRINTED or STANDARD (§2 step 4; §3 "THE INPUTS THE ARITHMETIC MAY CONSUME"), whatever its origin, and
provenance is recorded, not filtered. The one dependence worth having on record: the reachability of
the arithmetic group for a printed-but-chosen (or fitted, or imported) input rides entirely on this
settlement. Under the retired option (b) wording, the then-declared REPRO_AFTER_CHOICE was found
unreachable by two blind seats (§10.3); option (c) retired the class and made its cases ordinary
arithmetic-group claims. That dependence is a property of the settled text, not a reading I supplied.

CONVENTION FOR THE CONCRETE INPUTS
The corpus is pinned (§2: R3C2_CORPUS_MANIFEST.md; §10.5 records 89 enumerable texts), but C0 asks
whether each declared verdict CAN OCCUR — the exhibition space is possible inputs to the procedure,
so each row constructs a specific paper/claim in the corpus's register (cosmology; the C3 closed
STANDARD list is Planck 2018). All arithmetic below was machine-verified by this seat before filing.

================================================================================
TABLE 1 — §3 PER-CLAIM OUTCOMES (six)
================================================================================

verdict | concrete input | clause path | reachable
---|---|---|---
REPRO_WITHIN_STATED_PRECISION | Paper P1 prints "the free-fall time is 4.7 × 10⁵ yr" as its own result, states t_ff = √(3π / (32 G ρ)), and prints ρ = 2.0 × 10⁻¹⁷ kg m⁻³. G appears in P1 verbatim as 6.67430e-11 — on C3's closed list. No uncertainty stated. Mechanical evaluation: t_ff = √(3π / (32 × 6.67430e-11 × 2.0e-17)) = 1.48540e13 s = 4.70694e5 yr, which rounds to 4.7 × 10⁵ yr at the printed precision. | §1: numeral asserted as the paper's own → included. §2 steps 1–3: extract, list inputs, classify ρ PRINTED, G STANDARD (§2 step 3: "Where a value the paper prints is on the closed list verbatim, file STANDARD; otherwise PRINTED"). §2 step 4: mechanical attempt consumes both records. §3: "the paper's number follows, within its own stated precision"; no stated uncertainty → "the reproduced value must round to the printed numeral at that precision, rounding half away from zero" — it does. §2 step 5: record outcome; script records rests_on beside it (§3: "The claim's rests_on is reported beside it"). | yes
REPRO_FAILED | Paper P2: identical claim and recipe to P1, prints ρ = 2.0 × 10⁻¹⁷ kg m⁻³ and states an uncertainty: t_ff = (4.2 ± 0.1) × 10⁵ yr. Reproduced value 4.70694e5 yr. |Reproduced − printed| = 0.507 × 10⁵ > 0.1 × 10⁵. | §1 included → §2 steps 1–4 as row 1 (inputs sufficient: every input the recipe names is PRINTED or STANDARD) → §3 REPRO_FAILED: "the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number." Uncertainty test applied per §3: "|reproduced − printed| ≤ the stated uncertainty, taken once — not doubled, not rounded" — fails. Report both numbers; wording "unreproduced from the stated inputs," not "error"; rests_on reported beside it. | yes
REPRO_BLOCKED | Paper P3 prints "the circular velocity is 167 km/s" as its own, states v_c = √(GM/r), prints r = 20 kpc, does not print M, and writes "we adopt the mass of ref. [12]," where ref. [12] is a 2019 journal article that is not an enumerable text pinned in R3C2_CORPUS_MANIFEST.md. Second limb (same class): ref. [12] IS an enumerable pinned text, but no mass value machine-matches at its cited line. | §1 included → §2 step 3: M traced to a named source but not printed → named-source rule. §2 IMPORTED rule: PRINTED-from-source applies "only when such a match exists; a cited value that does not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest, files REPRO_BLOCKED under §3." §3 REPRO_BLOCKED definition names both limbs. C3: recorded status BLOCKED, origin IMPORTED, ORIG_CITATION cited to P3's naming sentence, no value; "the arithmetic never consumes it." §3 precedence: NO_DERIVATION_STATED does not hold (an equation is stated), so BLOCKED files first. Name the input (M) and the source (ref. [12]). | yes
REPRO_NOT_EVALUABLE | Limb (i) SYMBOLIC_TIMEOUT: paper P4 prints a numeral from a stated symbolic solve whose runtime exceeds the cap; launched as /usr/bin/python3 r3c2_timeout.py 120.0 -- <command> (§9), the wrapper "on the deadline prints SYMBOLIC_TIMEOUT and exits 124 — the reportable outcome." Limb (ii) MACHINERY_UNAVAILABLE: paper P4′ prints a relic-abundance numeral from a stated numerical integration of a stiff Boltzmann system; the lane's machinery is the pinned sympy/symbolic harness (C5), and numerical ODE integration is machinery this lane does not have. | §1 included → §2 steps 1–4: equation stated (so not NO_DERIVATION_STATED), every input PRINTED/STANDARD (so not BLOCKED or ABSENT), attempt begun → cannot complete. §3 REPRO_NOT_EVALUABLE: "Print SYMBOLIC_TIMEOUT when the 120-second cap is exceeded, or MACHINERY_UNAVAILABLE when the lane lacks the machinery, and the point reached." §3 precedence places NOT_EVALUABLE after the three input/derivation classes and before the arithmetic group; §4.2 permits one repeat, "meaningful only for REPRO_NOT_EVALUABLE." | yes
REPRO_NO_DERIVATION_STATED | Paper P5 prints "the sample's mean redshift is 0.73" asserted as its own result, and states no equation or computational procedure anywhere. Variant P5′ prints "the mass was obtained from the standard scaling relation" — a procedure named but not specified: "a sentence that says where the number came from without stating operations a seat could attempt." | §1: a printed numeral asserted as the paper's own result satisfies inclusion even with no derivation (§3 note: "A claim can satisfy §1 … while the paper never says how it was obtained"). §2 step 1 finds no equation the paper says produces it → nothing to attempt. §3 REPRO_NO_DERIVATION_STATED, both limbs quoted above; "Name the passage." §3 precedence: first in the order — even where an input would also be absent or blocked, this class files ahead of them. | yes
REPRO_INPUT_ABSENT | Paper P6 prints "the escape speed is 11.2 km/s" as its own, states v_esc = √(2GM/R), prints R = 6.371e6 m, and M appears nowhere in P6 and no source is named for it. | §1 included → §2 step 3: M is "neither printed nor traced to any named source" → status ABSENT. §2: "A seat may not supply a value for an ABSENT or BLOCKED input. Encountering one ends that claim's attempt." §3 REPRO_INPUT_ABSENT: "Name the input" (M). Named-source test separates the classes: BLOCKED requires a named source that fails; ABSENT requires no named source — disjoint domains. §3 precedence: NO_DERIVATION_STATED does not hold (equation stated), BLOCKED does not hold (no source named), so ABSENT files. | yes

Totality note on §3 (why no claim falls through): for any included claim, either no procedure is
stated (NO_DERIVATION_STATED), or a procedure exists and some input is blocked (BLOCKED), or some
input is absent (ABSENT), or all inputs are consumable and the attempt cannot complete
(NOT_EVALUABLE), or it completes and the stated-precision rule — uncertainty test, or rounding half
away from zero — decides WITHIN or FAILED. The §3 precedence is a total order over co-occurring
conditions: "Exactly one outcome is filed per claim. Where more than one terminal condition holds,
file the first in this order: REPRO_NO_DERIVATION_STATED, REPRO_BLOCKED, REPRO_INPUT_ABSENT,
REPRO_NOT_EVALUABLE, then the arithmetic group."

================================================================================
TABLE 2 — §4 STUDY-LEVEL CLASSES (eight)
================================================================================

verdict | concrete input | clause path | reachable
---|---|---|---
CENSUS_COMPLETE | Corpus state: denominator N = 3 included claims, each of the P1/P2 type — every claim states its recipe, every input is PRINTED or STANDARD, every attempt completes within the cap, so all three file arithmetic-group outcomes (two REPRO_WITHIN_STATED_PRECISION, one REPRO_FAILED). Both seats' enumerations, input lists, outcomes and origins agree. Custodian seed supplied with receipt T. C6 audits every arithmetic-group claim (that is all of them; remaining set R = 0, sample empty), re-derives each outcome and re-classifies each origin with no MISMATCH and no ledger incompleteness → C6_AUDIT_SAMPLE=PASS. | §4.1: "every included claim carries exactly one outcome from the arithmetic group of §3, with C6_AUDIT_SAMPLE=PASS" — satisfied; denominator 3 > 0, so the zero-denominator clause is not triggered. §4 precedence: no earlier class holds (no control failure, no split, no dispute of any kind, audit passed) → CENSUS_COMPLETE files, last in the order. Report the full tally with its denominator and the rests_on tally beside it — "two tallies from one pass" (§4.1). | yes
CENSUS_PARTIAL | Corpus state A: as above plus one P6-type claim (an ABSENT input) → that claim carries REPRO_INPUT_ABSENT, a non-arithmetic outcome. C6 runs (arithmetic claims audited under (i); the remaining set R = 1 sampled at k = min(max(1, ceil(0.20 × 4)), 1) = 1 under the custodian seed) and passes. Corpus state B (second limb): every enumerated candidate numeral is an equation number, reference number, page/line number, date, or attributed-not-derived → exclusion ledger full, denominator zero. | §4.2: "after the §2 attempt (one repeat permitted, meaningful only for REPRO_NOT_EVALUABLE), at least one included claim carries a non-arithmetic outcome (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT, REPRO_BLOCKED, REPRO_NOT_EVALUABLE), or the denominator is zero" — state A hits the first limb, state B the second. §4.1's own clause reinforces B: "A denominator of zero files CENSUS_PARTIAL with the empty enumeration named; no census is complete over nothing." §4 precedence: audit passed, so AUDIT_FAILED does not hold; PARTIAL files ahead of COMPLETE — "INCONCLUSIVE, and it takes precedence over CENSUS_COMPLETE" (§4.2). | yes
CENSUS_AUDIT_FAILED | Limb (i) MISMATCH: the auditor re-derives a sampled P1-type claim and finds the sealed ledger's PRINTED ρ does not machine-match its cited source line (cited line carries 2.0e-18, ledger records 2.0e-17) — the re-derived outcome differs from the sealed one. Limb (ii) does not run to PASS: the external custodian's seed is not supplied and recorded with receipt T → "the audit does not run, C6_AUDIT_SAMPLE=NOT_RUN, and the study files CENSUS_AUDIT_FAILED with the missing seed named" (C6). Limb (iii) seal failure: after opening, Blanc's re-hash of the tally or the protocol mismatches receipt T or P, or a receipt is missing (§7). | §4.3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the cause named), or the receipt verification of the seal fails. No tally is filed; report which." C6: "Any outcome the audit cannot reproduce, or any ledger incompleteness, files CENSUS_AUDIT_FAILED." §7: "Any missing receipt or mismatch files CENSUS_AUDIT_FAILED (§4, whose definition now names this case)." §4 precedence places it after the dispute classes and before PARTIAL/COMPLETE. | yes
R3C2_NO_CLASS | Limb (i): C3's validate run exits 1 in both seats (each seat's ledger carries a PRINTED value that fails machine-match at its cited line), on the first attempt and on the repeat — the control fails "in every seat that attempted it" after two attempts. Limb (ii) pre-dispatch: the builder's forbidden-list assertion finds a surviving string in the packet → "the packet is not written and C4_PACKET_REDACTED=FAIL" (C4) — a packet failure before dispatch. | §4.4: "a control among C0 through C5b fails in every seat that attempted it after two attempts; a packet or seat-isolation failure before dispatch files this class." Boundary named by the text: "A C6 audit failure or a seal-receipt failure files CENSUS_AUDIT_FAILED, not this class." §4 precedence: first — "Once a stop class applies, later limbs are unreached and their controls are NOT_RUN." | yes
CENSUS_DENOMINATOR_DISPUTED | Limb (i) enumeration: seat A includes a passage printing "0.9649" asserted as the paper's own fitted result; seat B excludes the same passage as attributed-not-derived ("as derived in ref. [9]"). Two reconciliation attempts fail. Limb (ii) input lists: on an agreed claim with stated recipe ρ_c = 3H²/(8πG), H = H₀√(Ω_m(1+z)³ + Ω_Λ), seat A lists inputs {H₀, Ω_m, Ω_Λ, z}; seat B lists {H, z} — the input_id sets differ, r3c2_lane_tools.py merge exits 1, and the difference survives the one reconciliation against the paper's stated equation. | §1: "disagreement on any candidate that survives two reconciliation attempts stops the study under CENSUS_DENOMINATOR_DISPUTED (§4): the disputed candidates are listed and the complete candidate and exclusion ledgers are reported with the dispute." §6 limb A: tolerance zero. §4.5: "the two enumerations disagree after two reconciliation attempts, or the two seats' input lists for the agreed claims disagree after the one C3 reconciliation. The census does not proceed; the disputed candidates or inputs are listed." C3 lane block: merge exit 1 → one reconciliation → surviving difference "stops the study under CENSUS_DENOMINATOR_DISPUTED (§4), the disputed inputs listed with both seats' quotations." | yes
CENSUS_OUTCOME_DISPUTED | An agreed included claim prints t_ff = (4.7 ± 0.05) × 10⁵ yr with the P1 recipe and ρ = 2.0 × 10⁻¹⁷ printed. Seat A reproduces 4.70694e5 yr: |4.70694 − 4.7| = 0.00694 ≤ 0.05 → files REPRO_WITHIN_STATED_PRECISION. Seat B reproduces 4.59350e5 yr (machine-verified value from ρ = 2.1e-17, the figure B read at the cited line): |4.59350 − 4.7| = 0.1065 > 0.05 → files REPRO_FAILED. In the one reconciliation against the printed numeral and the stated-precision rule of §3, each seat re-verifies its own computation and stands by it; the disagreement survives. | §2 step 5: the sealed tally is "the merged candidate file on which the two seats' outcome fields agree, claim by claim, after one reconciliation against the printed numeral and the stated-precision rule of §3; a disagreement surviving that reconciliation files CENSUS_OUTCOME_DISPUTED (§4)." §4.6: "The census does not proceed; the claim is listed with both seats' outcomes, both number pairs, and the step each seat reached." (Both V21 C0 seats exhibited this same class — §10.15/V22 row.) | yes
CENSUS_ORIGIN_DISPUTED | N = 20 included claims, all enumerations, input lists and outcomes agreed. On inputs affecting 3 claims, the seats' origin classifications differ: the sentence "we take σ₈ = 0.811" is filed CHOSEN (ORIG_CHOICE_STATED) by seat A and UNDECLARED (ORIG_SILENT, search printed) by seat B. 3/20 = 15% > 10%. Disputes are reported with both seats' classification and both quotations — never reconciled. | C3: "Every input's origin is classified independently by both seats"; disagreements produce merged records carrying origin_alt and are "reported, never reconciled" (§4.7 note). C6: "An input on which the two classifications disagree is filed ORIGIN_DISPUTED … Above 10% of included claims, CENSUS_ORIGIN_DISPUTED." §4.7: "the two seats' independent origin classifications disagree on inputs affecting more than 10% of included claims. The census does not proceed; every disputed input is listed with both seats' classification and both quotations." | yes
CENSUS_CONTROL_SPLIT | C5 harness: seat A's three commands all exit 0 with full stdout. Seat B's /usr/bin/python3 -c "import sympy; print(sympy.__version__)" exits 1 (module absent in B's environment), on the first attempt and on the repeat. The control fails in one seat and passes in the other after two attempts. | §4.8: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not adopt the passing seat's result." C5: "PASS requires all three commands to exit 0 and their full stdout to be printed; any non-zero exit … is FAIL." §4 precedence: second — only R3C2_NO_CLASS (failure in every seat) ranks ahead; the split is disjoint from it by definition. | yes

Totality note on §4: the precedence is a total order over co-occurring conditions — "Exactly one
study-level outcome is filed. Where more than one condition holds, file the first in this order:
R3C2_NO_CLASS, CENSUS_CONTROL_SPLIT, CENSUS_DENOMINATOR_DISPUTED, CENSUS_OUTCOME_DISPUTED,
CENSUS_ORIGIN_DISPUTED, CENSUS_AUDIT_FAILED, CENSUS_PARTIAL, CENSUS_COMPLETE. Once a stop class
applies, later limbs are unreached and their controls are NOT_RUN." Every reachable state of the
procedure lands in exactly one class: control failures (NO_CLASS or SPLIT, disjoint by seat-count),
enumeration/input disagreement (DENOMINATOR_DISPUTED), outcome disagreement (OUTCOME_DISPUTED),
origin disagreement above threshold (ORIGIN_DISPUTED), audit or seal failure (AUDIT_FAILED), a
non-arithmetic claim or empty denominator with audit passing (PARTIAL), or none of these (COMPLETE).
No state falls through.

================================================================================
TABLE 3 — DECLARED LIMBS AND CONDITIONS INSIDE THE CLASSES (coverage check)
================================================================================

condition | exhibited in | reachable
---|---|---
SYMBOLIC_TIMEOUT limb of REPRO_NOT_EVALUABLE | Table 1 row 4, limb (i); wrapper exit 124, "the reportable outcome" (§9) | yes
MACHINERY_UNAVAILABLE limb of REPRO_NOT_EVALUABLE | Table 1 row 4, limb (ii) (§3: "Print … MACHINERY_UNAVAILABLE when the lane lacks the machinery, and the point reached") | yes
BLOCKED limb 1 — named source not an enumerable pinned text | Table 1 row 3 (§3 definition, first limb) | yes
BLOCKED limb 2 — enumerable pinned text, no machine-match at cited line | Table 1 row 3 (§3 definition, second limb; §2 IMPORTED rule) | yes
NO_DERIVATION limb — procedure named but not specified | Table 1 row 5 variant P5′ (§3: "A procedure named but not specified … file this class and name the passage") | yes
Zero-denominator limb of CENSUS_PARTIAL | Table 2 row 2, corpus state B (§4.2 "or the denominator is zero"; §4.1 "no census is complete over nothing") | yes
AUDIT_FAILED limb — outcome/ledger MISMATCH | Table 2 row 3, limb (i) (§4.3, C6) | yes
AUDIT_FAILED limb — audit does not run to PASS (seed not supplied) | Table 2 row 3, limb (ii) (C6: "the study files CENSUS_AUDIT_FAILED with the missing seed named") | yes
AUDIT_FAILED limb — seal receipt verification fails | Table 2 row 3, limb (iii) (§7: "Any missing receipt or mismatch files CENSUS_AUDIT_FAILED") | yes
R3C2_NO_CLASS limb — pre-dispatch packet/seat-isolation failure | Table 2 row 4, limb (ii) (§4.4; C4 builder assertion) | yes
DENOMINATOR_DISPUTED limb — input lists disagree after the one C3 reconciliation | Table 2 row 5, limb (ii) (§4.5; C3 merge exit 1) | yes
One repeat permitted, meaningful only for REPRO_NOT_EVALUABLE | §4.2: a timed-out claim retried once; on a second timeout NOT_EVALUABLE stands and the study files CENSUS_PARTIAL. The repeat creates no new class. | yes
rests_on NOT_COMPUTED row (claim with no ledger record) | §3: "a claim with no ledger record carries rests_on NOT_COMPUTED, and the rests_on tally reports a NOT_COMPUTED row" — a P5-type claim (no equation, hence no inputs) produces it. A computed field, not a filed verdict; noted for coverage. | yes (field, not a verdict)
rests_on DISPUTED pair (root origin disputed ≤ 10%) | §3/C6: "A claim whose root-origin set contains an ORIGIN_DISPUTED input carries rests_on computed under both classifications, printed as a pair and marked DISPUTED." N = 20, dispute affecting 1 claim (5% ≤ 10%): no ORIGIN_DISPUTED class; the claim's rests_on prints as a DISPUTED pair and the census proceeds. A computed field, not a filed verdict. | yes (field, not a verdict)

================================================================================
THE SUSPICION — CENSUS_COMPLETE, ANSWERED DIRECTLY
================================================================================

Answer: REACHABLE.

What the suspicion gets right: the bar is absolute. §4.2, verbatim: "at least one included claim
carries a non-arithmetic outcome (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT, REPRO_BLOCKED,
REPRO_NOT_EVALUABLE), or the denominator is zero" files CENSUS_PARTIAL, "INCONCLUSIVE, and it takes
precedence over CENSUS_COMPLETE." So yes — a single blocked, absent-input, no-derivation-stated, or
not-evaluable claim anywhere in the corpus forces CENSUS_PARTIAL, and a dispute or audit failure
routes elsewhere still earlier in the precedence.

Why that does not make CENSUS_COMPLETE unreachable: reachability asks whether any input produces
the verdict, and Table 2 row 1 exhibits it — a corpus in which every included claim states its
recipe, every input is PRINTED or STANDARD (including printed-but-chosen, fitted or imported values,
which option (c) consumes and records in rests_on rather than excluding), every attempt completes,
both seats agree throughout, and C6 passes. The routing: §4.1 requires "every included claim carries
exactly one outcome from the arithmetic group of §3, with C6_AUDIT_SAMPLE=PASS"; nothing earlier in
the §4 order (R3C2_NO_CLASS → CENSUS_CONTROL_SPLIT → CENSUS_DENOMINATOR_DISPUTED →
CENSUS_OUTCOME_DISPUTED → CENSUS_ORIGIN_DISPUTED → CENSUS_AUDIT_FAILED → CENSUS_PARTIAL) holds, so
CENSUS_COMPLETE files, last in the order. §4.1 additionally forecloses the vacuous case — "A
denominator of zero files CENSUS_PARTIAL with the empty enumeration named; no census is complete
over nothing" — so COMPLETE's domain is exactly the non-empty, all-arithmetic, audit-passing
tallies. That domain is non-empty by exhibition.

The practical worry is a property of the design's strictness, not a reachability defect: on the
real pinned corpus (89 enumerable texts, §10.5), one blocked or absent or under-specified claim
anywhere is enough for PARTIAL. Whether that happens is the empirical question the census exists to
answer. C0 asks only whether the verdict can occur, and it can. Under the retired option (b)
wording the two V9 blind seats reached the same conclusion on this class (§10.3: both seats,
"CENSUS_COMPLETE reachable"), and option (c) only widens COMPLETE's domain, because
printed-but-chosen inputs no longer stop the arithmetic — they file WITHIN or FAILED and carry
their provenance in rests_on.

================================================================================
UNREACHABLE VERDICTS
================================================================================

None. Every §3 per-claim outcome and every §4 study-level class is exhibited above with a concrete
input and a clause path through the document as it stands. No blocking clause was encountered; there
is nothing to quote.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V24B_KIMI_COMPLETE

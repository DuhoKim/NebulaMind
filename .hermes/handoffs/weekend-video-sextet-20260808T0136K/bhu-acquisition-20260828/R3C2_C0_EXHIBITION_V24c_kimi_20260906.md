ACCESS_SHA=4609d97973bb28f9740ac1d6a48f9443c33d08de3673c131ec806451a9f1ec6b
C0_REACHABILITY=PASS

# R3C2 — C0 reachability exhibition, V24c (kimi seat), 2026-09-06

Scope of this document: exhibition only. It does not gate the design and does not judge its
physics or its quality. It asks one question for every per-claim outcome of §3 and every
study-level class of §4 of `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md` (V24c, living draft;
V23 remains the signed design of record): can this verdict OCCUR under the text as written —
is there a concrete input that routes to it?

Text read: the full 1078 lines of the master, access-proven above. No other file in this
directory was read. §3's definition is treated exactly as it stands: option (c) is adopted,
the HELD marker is gone (§10.4), `REPRO_AFTER_CHOICE` is RETIRED into the script-computed
`rests_on` field (§3, retired-class note). `REPRO_AFTER_CHOICE` is therefore not a declared
§3 outcome and gets no row; its content now lives in `rests_on`, which is a ledger field,
not an outcome. The `rests_on` values (`DERIVED_ONLY`, `USES_CHOSEN`, `USES_FITTED`,
`USES_IMPORTED`, `USES_UNDECLARED`, `DISPUTED`, `NOT_COMPUTED`) are likewise fields, not
verdicts, and are covered only where §3/§4 declare reportable rows for them (Table B).

Marking convention (per the brief's final note): where a routing depends on §1's operational
definition — "a passage in a pinned source that prints a numeral the paper asserts as a
result of its own," with the five excluded kinds — that dependence is marked [§1-DEP].
§1 inclusion is assigned independently by two seats and remains a judgement the design
itself flags as such (§1: "whether a numeral is 'the paper's own result' remains a
judgement"); every exhibit below that begins with an included claim carries that dependence.
It is stated, not assumed away.

§3 precedence (per-claim), quoted from §3: "Where more than one terminal condition holds,
file the first in this order: `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`,
`REPRO_INPUT_ABSENT`, `REPRO_NOT_EVALUABLE`, then the arithmetic group."
The arithmetic group is exactly `REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED`.

§4 precedence (study-level), quoted from §4: "Where more than one condition holds, file the
first in this order: `R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`,
`CENSUS_OUTCOME_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`,
`CENSUS_COMPLETE`. Once a stop class applies, later limbs are unreached and their controls
are `NOT_RUN`."

For every row, the exhibit constructs the input so that all EARLIER precedence limbs do not
hold; that check is part of the clause path.

## (A) Table 1 — §3 per-claim outcomes (six declared)

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| REPRO_NO_DERIVATION_STATED | Paper A (pinned enumerable text in `R3C2_CORPUS_MANIFEST.md`) prints: "We find the transition occurs at z = 0.73." No equation, no operations; the only provenance sentence is "obtained from our analysis pipeline," which names where the number came from without stating operations a seat could attempt. [§1-DEP] | §1: printed numeral asserted as the paper's own result -> included by both seats. §2 step 1: extract numeral/units and "the equation the paper says produces it" — none stated. §3: "the paper prints the claim as its own result but states no equation or computational procedure that could produce it, so there is nothing to attempt"; and "A procedure named but not specified … states no computational procedure that could produce it; file this class and name the passage." Precedence: first in the §3 order, so nothing can mask it. | yes |
| REPRO_BLOCKED | Paper B prints: "With the normalisation C from Smith et al. (2019), w = -p/(rho*C) = -1.03," printing p and rho but not C. Smith et al. (2019) is NOT an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`. (Variant, second limb: the named source IS pinned and enumerable, but the value does not machine-match at the cited line.) [§1-DEP] | §1 -> included. §2 IMPORTED rule: "a cited value that does not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest, files `REPRO_BLOCKED` under §3." §2 step 3: C recorded `BLOCKED` (traced to a named source, no machine-matchable value). §3 `REPRO_BLOCKED`: input not printed + named source either not pinned-enumerable or no match at the cited line; "in the first case whether that source is obtainable elsewhere is irrelevant, because the census may not open or consume it." Precedence: `REPRO_NO_DERIVATION_STATED` does not hold (an equation IS stated), so BLOCKED — second in the order — files before `REPRO_INPUT_ABSENT`. C3: the input is recorded status `BLOCKED`, origin `IMPORTED`, `ORIG_CITATION` cited to the naming sentence, no value; "the arithmetic never consumes it." | yes |
| REPRO_INPUT_ABSENT | Paper C prints: "From delta = a * b we obtain delta = 7.2," printing a = 3 and nowhere printing b, and naming no source for b anywhere in the text. [§1-DEP] | §1 -> included. §2 step 2: inputs {a, b}. §2 step 3: b is `ABSENT` — neither printed nor traced to any named source. §2: "A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt." §3 `REPRO_INPUT_ABSENT`: "an input the equation needs is `ABSENT` from the paper — neither printed nor traced to any named source — so the attempt stops there. Name the input." Precedence: NO_DERIVATION does not hold (equation stated); BLOCKED does not hold (no named source — §3: "Distinct from `REPRO_INPUT_ABSENT`, which is an input the paper neither prints nor traces to any named source"); so INPUT_ABSENT — third in the order — files. | yes |
| REPRO_NOT_EVALUABLE | Paper D prints: "Solving the coupled implicit system F(chi; p, q) = 0 with p = 1.5, q = 2.25 printed yields chi = 4.318." The equation is stated and every input is `PRINTED`; the symbolic solve, launched as mandated through `/usr/bin/python3 r3c2_timeout.py 120.0 -- <command>`, exceeds the 120.0-second wall-clock deadline. (Variant, second limb: the stated recipe requires numerical PDE machinery this lane does not have -> `MACHINERY_UNAVAILABLE`.) [§1-DEP] | §1 -> included. §2 steps 1-4: all inputs consumable; the attempt is mandatory — §2 step 4: "Attempt the arithmetic MECHANICALLY — follow the paper's own recipe, using every value it directs you to use." §9: the wrapper "enforces a 120.0-second wall-clock deadline on the monotonic clock … on the deadline prints `SYMBOLIC_TIMEOUT` and exits 124 — the reportable outcome." §3 `REPRO_NOT_EVALUABLE`: "the arithmetic could not be completed within the 120-second cap, or requires machinery this lane does not have. Print `SYMBOLIC_TIMEOUT` … or `MACHINERY_UNAVAILABLE` … and the point reached." Precedence: NO_DERIVATION, BLOCKED, INPUT_ABSENT all fail to hold (recipe stated, all inputs PRINTED), so NOT_EVALUABLE — fourth in the order — files. | yes |
| REPRO_WITHIN_STATED_PRECISION | Paper E prints: "The horizon scale is d = 2 * Omega_m = 0.63," with Omega_m printed verbatim as 0.3153 — the exact string on C3's closed STANDARD list (ledger key `Omega_m`). Mechanical arithmetic: 2 * 0.3153 = 0.6306; no uncertainty stated; at the printed precision (two decimals) 0.6306 rounds to 0.63, rounding half away from zero. (A chosen-input variant — Paper E' prints "we adopt beta = 1/929.25" and the recipe consumes it — files the same class with `rests_on` = `USES_CHOSEN`; the printed-but-chosen case that retired `REPRO_AFTER_CHOICE` lands here, §10.5 Q1.) [§1-DEP] | §1 -> included. §2 step 3: input status `STANDARD` ("a value the paper prints … on the closed list verbatim"; "the two routes are outcome-identical"). §2 step 4: the attempt consumes every `PRINTED`/`STANDARD` record — §3: "Arithmetic consumes records according to status `PRINTED` or `STANDARD`." §3 `REPRO_WITHIN_STATED_PRECISION`: "the paper's number follows, within its own stated precision, from the paper's own recipe applied to the inputs it states … Where the paper states no precision for the claim, the printed precision is the claim's stated precision: the reproduced value must round to the printed numeral at that precision, rounding half away from zero." Precedence: no earlier terminal condition holds; arithmetic group reached. C1: an arithmetic-group candidate carries `printed_value` and `reproduced_value` — both reported, as §3 requires. | yes |
| REPRO_FAILED | Paper F prints: "With a = 2 and b = 3 we find a + b = 7." Both inputs `PRINTED`; the recipe is stated; mechanical arithmetic gives 5; no uncertainty stated; at the printed integer precision 5 does not round to 7. [§1-DEP] | §1 -> included. §2 steps 1-4: inputs sufficient, attempt proceeds. §3 `REPRO_FAILED`: "the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number. Report both numbers. Wording: 'unreproduced from the stated inputs,' not 'error.'" The stated-precision rule of §3 decides mechanically (13.8-vs-13.797 style ambiguity is removed by the rounding rule). Precedence: no earlier terminal condition holds; arithmetic group reached. §3's closing note routes here explicitly: "a claim whose inputs the paper DOES state, chosen or not — that claim is attempted and files `REPRO_WITHIN_STATED_PRECISION` or `REPRO_FAILED`." | yes |

All six §3 outcomes: REACHABLE. No per-claim outcome is blocked by any clause.

## (B) Table 2 — §4 study-level classes (eight declared, precedence order)

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| R3C2_NO_CLASS | Pre-dispatch: the builder's forbidden-list assertion finds a surviving forbidden string in the packet output -> "the packet is not written and `C4_PACKET_REDACTED=FAIL`; the study does not proceed on a hand-checked copy." (In-run variant: C5's printed SymPy path/digest differs from the dispatch record's pin on every seat's host, twice -> `C5_HARNESS_PINNED=FAIL` "in every seat that attempted it after two attempts.") | §4.4: "a control among C0 through C5b fails in every seat that attempted it after two attempts; a packet or seat-isolation failure before dispatch files this class." Precedence: FIRST in the §4 order — it files ahead of every other class. The same clause excludes the audit route: "A C6 audit failure or a seal-receipt failure files `CENSUS_AUDIT_FAILED`, not this class." Corroboration inside the record: §10.18 documents an actual filing — the 10:17 abort, where the seat "stopped at C5, filed `R3C2_NO_CLASS` for itself." | yes |
| CENSUS_CONTROL_SPLIT | Two seats dispatched. Seat A's C5 run prints a SymPy path and digest matching the dispatch record pin -> `C5_HARNESS_PINNED=PASS`. Seat B's host prints a different `sympy.__file__` (different user site) -> digest mismatch -> `C5_HARNESS_PINNED=FAIL`. Repeated once: the split survives two attempts. | §4.8: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not adopt the passing seat's result." Precedence: second in the §4 order; `R3C2_NO_CLASS` does not hold because the control did NOT fail in every seat. The class exists precisely for this state — §4.8 note: the old wording "in both seats" left the one-seat-fails-twice, other-seat-passes state with no class. | yes |
| CENSUS_DENOMINATOR_DISPUTED | Limb A. Paper I prints the bare numeral "2021" in a results sentence. Seat A includes it (a measured value asserted as the paper's own result); seat B excludes it (`DATE`, an excluded kind). Two reconciliation attempts fail to resolve the inclusion. (Second route, post-agreement: the seats agree on every candidate but seat A lists input b for a claim and seat B does not; `r3c2_lane_tools.py merge` exits 1; the difference survives the one C3 reconciliation against the paper's stated equation.) [§1-DEP — this class is the designed failure mode of the §1 judgement itself] | §1: "disagreement on any candidate that survives two reconciliation attempts stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4): the disputed candidates are listed and the complete candidate and exclusion ledgers are reported with the dispute." §6 Limb A: "tolerance zero, measured in candidate passages — stop with `CENSUS_DENOMINATOR_DISPUTED`." §4.5 names the second limb: "or the two seats' input lists for the agreed claims disagree after the one C3 reconciliation"; the C3 lane-side clause: "if `merge` exits 1, the two seats reconcile their input lists … once; an input-set difference surviving that reconciliation stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4)." Precedence: third; NO_CLASS and CONTROL_SPLIT do not hold (controls passed in every seat or identically). | yes |
| CENSUS_OUTCOME_DISPUTED | Limb B. Both seats agree claim J is included. Paper J prints "tau = 0.0544" and cites a pinned enumerable text for the input; seat A machine-matches the value at the cited line (status `PRINTED`, origin `IMPORTED`) and files `REPRO_WITHIN_STATED_PRECISION`; seat B cannot machine-match at the cited line (status `BLOCKED`) and files `REPRO_BLOCKED`. The one reconciliation "against the printed numeral and the stated-precision rule of §3" cannot resolve the split, because the difference is in input classification, not in arithmetic or precision. | §2 step 5: "the sealed reproduction tally is the merged candidate file on which the two seats' `outcome` fields agree, claim by claim, after one reconciliation against the printed numeral and the stated-precision rule of §3; a disagreement surviving that reconciliation files `CENSUS_OUTCOME_DISPUTED` (§4)." §4.6: "the claim is listed with both seats' outcomes, both number pairs, and the step each seat reached." Precedence: fourth; the three earlier stop classes do not hold (controls fine, enumeration agreed). Corroboration inside the record: the V22 row of §10 records "C0 two seats AGREE on V21 (both exhibit `CENSUS_OUTCOME_DISPUTED`)." | yes |
| CENSUS_ORIGIN_DISPUTED | Corpus of 10 included claims. Paper K, feeding 2 of the 10 claims, prints "We take sigma8 = 0.8111" with no verb of choice, fit, measurement, or citation, and the value is on C3's closed list verbatim. Seat A files `ORIG_CONSTANT` -> `STANDARD` (printed verbatim, on the list). Seat B files `ORIG_SILENT` -> `UNDECLARED`, printing its `origin_search` (query, files, matches). The classifications are "reported, never reconciled"; inputs carrying the disagreement affect 2 of 10 included claims = 20% > 10%. | C3: "Every input's `origin` is classified independently by both seats"; the reason-code tie-break order does not decide this case, because the seats matched different codes to the same sentence — the stated floor: "a reason code that matches its quotation but misapplies the precedence is caught only by the second seat's independent classification and the C6 re-classification, never by the machine." §4.7: "the two seats' independent `origin` classifications disagree on inputs affecting more than 10% of included claims. The census does not proceed; every disputed input is listed with both seats' classification and both quotations." C6 echoes: "Above 10% of included claims, `CENSUS_ORIGIN_DISPUTED`." Precedence: fifth; the four earlier stop classes do not hold. | yes |
| CENSUS_AUDIT_FAILED | The C6 auditor, "without sight of earlier work and re-classifying every input's `origin` from the pinned sources," re-derives arithmetic-group claim X: the sealed record files `REPRO_WITHIN_STATED_PRECISION` (printed 7), the auditor's independent re-derivation obtains 5 and files `REPRO_FAILED` -> `MISMATCH` in `C6_AUDIT.json`. (Second route: the external custodian's seed is not supplied and recorded with receipt T -> "the audit does not run, `C6_AUDIT_SAMPLE=NOT_RUN`, and the study files `CENSUS_AUDIT_FAILED` with the missing seed named." Third route: post-opening, Blanc's re-hash of the tally or the protocol mismatches the receipted values -> §7: "Any missing receipt or mismatch files `CENSUS_AUDIT_FAILED`.") | §4.3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the cause named), or the receipt verification of the seal fails. No tally is filed; report which." C6: "Any outcome the audit cannot reproduce, or any ledger incompleteness, files `CENSUS_AUDIT_FAILED`"; "`C6_AUDIT_SAMPLE=PASS` only if that artefact exists, is printed, and carries no `MISMATCH` and no incompleteness." Precedence: sixth — ahead of both tally classes; the five earlier stop classes do not hold. | yes |
| CENSUS_PARTIAL | Corpus of two included claims. Paper G's claim files `REPRO_WITHIN_STATED_PRECISION` (as Table 1). Paper H prints "delta = a * b = 7.2" with b neither printed nor traced to any named source -> `REPRO_INPUT_ABSENT`. One repeat of the §2 attempt is permitted and changes nothing (it is "meaningful only for `REPRO_NOT_EVALUABLE`"). Denominator = 2. (Second route: the enumeration of the pinned corpus yields zero included claims — every candidate passage is an excluded kind — "a denominator of zero files `CENSUS_PARTIAL` with the empty enumeration named; no census is complete over nothing.") [§1-DEP] | §4.2: "after the §2 attempt (one repeat permitted, meaningful only for `REPRO_NOT_EVALUABLE`), at least one included claim carries a non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`), or the denominator is zero. Report each and why. INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`." Precedence: seventh; the six earlier stop classes do not hold (controls pass, no split, enumerations agree, outcomes agree, origins agree <=10%, audit PASS). | yes |
| CENSUS_COMPLETE | Corpus: one pinned enumerable text, Paper L, containing exactly one candidate passage, which prints "d = 2 * r; with r = 3, d = 6." Both seats independently include the claim [§1-DEP]; both classify r `PRINTED` (machine-matched at its cited line, origin `DERIVED` or `MEASURED` with cited evidence — classifications agree); both file `REPRO_WITHIN_STATED_PRECISION` (2 * 3 = 6 rounds to the printed 6 at the printed integer precision). All controls C0-C5b PASS identically in every seat (no split, no every-seat failure). Enumerations agree; input lists agree (`merge` exit 0); outcomes agree; origins agree (0% <= 10%). The custodian seed is supplied and recorded with receipt T; the C6 auditor re-derives the sole arithmetic-group claim with `MATCH`, the completeness dispositions are clean, `C6_AUDIT.json` is printed, `C6_AUDIT_SAMPLE=PASS`; the seed sample over the remaining claims is empty (R = 0, C6: "when `R` is zero the sample is empty and every included claim is already audited under (i)"). Receipts P and T verify. Denominator = 1 > 0. | §4.1: "every included claim carries exactly one outcome from the arithmetic group of §3, with `C6_AUDIT_SAMPLE=PASS`." §3's arithmetic group = exactly `REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED`; the sole claim carries one. The zero-denominator clause is not triggered (denominator 1). §4 precedence walked in full: `R3C2_NO_CLASS` (controls pass — no); `CENSUS_CONTROL_SPLIT` (identical — no); `CENSUS_DENOMINATOR_DISPUTED` (agree — no); `CENSUS_OUTCOME_DISPUTED` (agree — no); `CENSUS_ORIGIN_DISPUTED` (0% — no); `CENSUS_AUDIT_FAILED` (PASS, receipts verify — no); `CENSUS_PARTIAL` (no non-arithmetic outcome; denominator > 0 — no). `CENSUS_COMPLETE` — last in the order — files by elimination. | yes |

All eight §4 classes: REACHABLE. No study-level class is blocked by any clause.

## Table B — declared sub-conditions and reportable rows riding on the verdicts

These are not separate verdicts, but the text declares them as named, reportable states;
each is exhibited so no declared condition is left without a witness.

| declared condition | concrete input | clause path | reachable |
|---|---|---|---|
| SYMBOLIC_TIMEOUT (print token of REPRO_NOT_EVALUABLE) | Paper D's solve under `/usr/bin/python3 r3c2_timeout.py 120.0 -- <command>` exceeds the deadline | §9: wrapper "on the deadline prints `SYMBOLIC_TIMEOUT` and exits 124 — the reportable outcome"; §3 REPRO_NOT_EVALUABLE: "Print `SYMBOLIC_TIMEOUT` when the 120-second cap is exceeded" | yes |
| MACHINERY_UNAVAILABLE (print token of REPRO_NOT_EVALUABLE) | Paper M's stated recipe requires a numerical relativity solver the lane does not have | §3: "or `MACHINERY_UNAVAILABLE` when the lane lacks the machinery, and the point reached" (token added at V15, §10.9 kimi F4) | yes |
| Zero-denominator route into CENSUS_PARTIAL | Pinned corpus whose every candidate passage is an excluded kind (equation numbers, dates, etc.); exclusion ledger full, included set empty | §4.1 second sentence: "A denominator of zero files `CENSUS_PARTIAL` with the empty enumeration named; no census is complete over nothing"; §4.2: "or the denominator is zero" (V22 repair, §10.16) | yes |
| rests_on NOT_COMPUTED row | Included claim whose stated recipe has no inputs (e.g., Paper N prints "1 + 1 = 2" as its derived identity): arithmetic group outcome, zero ledger records | §3: "a claim with no ledger record carries `rests_on` `NOT_COMPUTED`, and the `rests_on` tally reports a `NOT_COMPUTED` row" | yes |
| rests_on DISPUTED pair | An input whose two-seat origin classifications disagree (the Paper K case) feeds claim X; <=10% of claims affected, so the study proceeds | C6/§4.7 note: "A claim whose root-origin set contains an `ORIGIN_DISPUTED` input carries `rests_on` computed under both classifications, printed as a pair and marked `DISPUTED`; the `rests_on` tally reports a `DISPUTED` row"; §3 master-only rule: "A claim with a disputed root carries the pair computed under both classifications and is marked `DISPUTED`" | yes |
| PARENTS_DISPUTED pair | Seats agree on the input set but list different `derived_from` parents for one `DERIVED` record | C3 lane-side clause: "where the two `derived_from` lists differ the merged record carries both parent lists marked `PARENTS_DISPUTED`, and `compute` derives `root_origins` under both, printed as a pair, as for a disputed origin" | yes |
| Two routes into REPRO_BLOCKED | (i) named source not pinned-enumerable (Paper B); (ii) named source pinned-enumerable, no machine-match at the cited line (Paper B variant) | §3 REPRO_BLOCKED names both limbs; §2 IMPORTED rule: "only when such a match exists" | yes |
| Two routes into CENSUS_DENOMINATOR_DISPUTED | (i) inclusion disagreement surviving two reconciliations (Paper I); (ii) input-list disagreement surviving the one C3 reconciliation (`merge` exit 1) | §4.5 names both limbs; C3 lane-side clause names the second | yes |
| Three routes into CENSUS_AUDIT_FAILED | (i) MISMATCH on re-derivation; (ii) audit does not run (missing custodian seed); (iii) seal-receipt failure | §4.3 names (i) and (iii); C6 names (ii): "If the seed is not supplied and recorded with the receipt, the audit does not run … the study files `CENSUS_AUDIT_FAILED` with the missing seed named"; §7 names (iii) | yes |

## The named suspicion, answered directly: is CENSUS_COMPLETE reachable?

Question as put: CENSUS_COMPLETE requires every included claim to carry an outcome from the
arithmetic group; in a real corpus of many papers, does a single blocked, absent-input, or
no-derivation-stated claim anywhere force CENSUS_PARTIAL, making CENSUS_COMPLETE unreachable
in practice?

Answer: REACHABLE.

The routing, in full:

1. The condition that defeats CENSUS_COMPLETE is contingent, not necessary. Each
   non-arithmetic outcome requires a specific defect in the corpus: REPRO_NO_DERIVATION_STATED
   requires a paper that states no procedure; REPRO_BLOCKED requires a named source that is
   unpinned or unmatched; REPRO_INPUT_ABSENT requires an input traced to nothing;
   REPRO_NOT_EVALUABLE requires a timeout or missing machinery. No clause in the document
   forces any included claim to carry one of those defects. A corpus in which every paper
   states its recipe and prints (or pins, via the IMPORTED rule) every input, with the
   arithmetic completing inside the cap, routes every claim into the arithmetic group.
   Table 2's Paper L corpus is such an input, and nothing about it becomes logically
   impossible as the corpus grows — only empirically less likely.

2. The precedence does not bar it. §4's order places CENSUS_COMPLETE last, but precedence
   fires only when an earlier condition holds. In the Paper L input every earlier limb's
   condition is false: controls pass identically (no NO_CLASS, no CONTROL_SPLIT), the
   enumerations and input lists agree (no DENOMINATOR_DISPUTED), the outcomes agree (no
   OUTCOME_DISPUTED), origins agree at 0% (no ORIGIN_DISPUTED), the audit runs to PASS with
   the custodian seed receipted (no AUDIT_FAILED), and no claim carries a non-arithmetic
   outcome with denominator > 0 (no PARTIAL). CENSUS_COMPLETE files by elimination.

3. The zero-denominator carve-out does not bar it: the denominator is 1, not 0.

4. The document itself anticipated this exact suspicion and frames it as a contingency,
   not an impossibility — §5 C0's note: "CENSUS_COMPLETE requires every included claim to
   carry an arithmetic-group outcome, which a single blocked or absent input in the whole
   corpus is enough to prevent." "Enough to prevent" is a statement about what CAN defeat
   the class, not a statement that something always does. C0 asks whether the outcome CAN
   occur; it can.

What is true, and stated plainly so the exhibition is not read as more than it is: in a
real 89-text corpus (the pinned scale recorded at §10.5), the empirical probability that
every claim survives into the arithmetic group may be small, and a single defect anywhere
does file CENSUS_PARTIAL. That is a statement about the expected tally, not about
reachability. The class is reachable; its reaching is the corpus's decision, not the
document's.

## UNREACHABLE verdicts and their blocking clauses

None. Every declared §3 outcome (6/6) and every declared §4 class (8/8) is exhibited above
with a concrete input and a clause path. There is no blocking clause to quote.

For completeness, the one class this study's own history found unreachable —
`REPRO_AFTER_CHOICE`, filed UNREACHABLE by two blind seats at V9 (§10.3) — is not a declared
outcome of the current text: it was RETIRED at V10 by the principal's ruling adopting
option (c), and §3 carries its retirement note. Its former content is the `rests_on` field
of `REPRO_WITHIN_STATED_PRECISION` / `REPRO_FAILED` claims, exhibited in Table 1 (the
Paper E' variant). No held clause remains: the HELD marker was removed at §10.4 and the
definition is settled as written.

## Dependence on §1's operational definition (marked, as ordered)

Every per-claim exhibit and every denominator-dependent study-level exhibit begins with a
claim being INCLUDED under §1's rule, and §1 itself states that whether a numeral is "the
paper's own result" "remains a judgement … it moves from one reader to two who must agree."
The design routes the failure mode of that judgement to a declared class
(CENSUS_DENOMINATOR_DISPUTED), which is itself exhibited. No exhibit above required
resolving that judgement in a contested direction; each used a passage that is
uncontroversially the paper's own printed result, and each is marked [§1-DEP] where the
dependence exists. That dependence is a property of the design, recorded here rather than
assumed away.

## Verdict

C0_REACHABILITY=PASS: 6 of 6 §3 per-claim outcomes reachable, 8 of 8 §4 study-level classes
reachable, all declared sub-conditions witnessed, the named CENSUS_COMPLETE suspicion
answered REACHABLE with its routing shown. This exhibition is authored against V24c exactly
as it stands on disk (access hash above) and makes no judgement about whether the design is
good — only that every declared verdict can occur.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V24C_KIMI_COMPLETE

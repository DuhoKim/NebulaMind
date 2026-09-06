ACCESS_SHA=bcc16e32b6dfd112e4276b61616293bc03bbc28ee3c360b5b9fd7ec65f3645b3
C0_REACHABILITY=PASS

R3-C2 V24 — C0 REACHABILITY EXHIBITION (author seat: kimi, 2026-09-06)
Target document (read from disk, in full, 1046 lines; no other file in this directory opened):
R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md, Version 24, LIVING DRAFT, unsigned
(V23, 55b466fadf8ca75f…, remains the signed design of record per §10.18).

=====================================================================
0. DEFINITION DEPENDENCE — STATED, NOT ASSUMED
=====================================================================
This exhibition is against the text exactly as it stands at the ACCESS_SHA above.
§1's core question is read as SETTLED by Duho's ruling "Q-R3C2 c", 2026-09-05 14:08 KST
(§10.4): option (c) — one pass, two tallies. Concretely, the governing consumption rule is
§3's blockquote, taken verbatim:

  "THE INPUTS THE ARITHMETIC MAY CONSUME = every ledger record with status `PRINTED`
  (given in the paper, whatever its `origin`) or `STANDARD` (on C3's closed list)."

Consequences of that reading, each load-bearing below:
- A claim whose printed input is CHOSEN, FITTED, IMPORTED or UNDECLARED by origin is
  ATTEMPTED and files an arithmetic-group outcome; provenance is recorded and `rests_on`
  is computed by script (lane side), never by a seat.
- `REPRO_AFTER_CHOICE` is RETIRED (§3's own parenthetical: "RETIRED at V10 by the
  principal's ruling adopting option (c)"), so §3 declares SIX per-claim outcomes, not
  seven. The retired class is not a row in this exhibition.
- The HELD marker that stood over §3 from V5.1 through V9 is removed; §10.4 preserves it
  verbatim as history. There is no held clause in the text as it stands. Under the retired
  option (b) wording the V9 exhibition found exactly one unreachable verdict (§10.3); that
  dependence is recorded here rather than assumed — it is a result about which text is
  exhibited, and this exhibition binds only the V24 text at the hash on line 1.

What is NOT a per-claim outcome (and therefore not a required row), per the text:
- Exclusion-ledger kinds (EQUATION_NUMBER, REFERENCE_NUMBER, PAGE_OR_LINE_NUMBER, DATE,
  ATTRIBUTED_NOT_DERIVED): "Candidate exclusions are not per-claim outcomes." (§3)
- `rests_on` values (DERIVED_ONLY / USES_UNDECLARED / USES_IMPORTED / USES_FITTED /
  USES_CHOSEN / DISPUTED / NOT_COMPUTED): script-computed ledger fields, not §3 outcomes.
- SYMBOLIC_TIMEOUT and MACHINERY_UNAVAILABLE: the two named print-codes OF
  `REPRO_NOT_EVALUABLE`; both are exhibited inside that row.

Exhibition corpus E below is CONSTRUCTED for reachability (as every prior C0 round did);
it exhibits that each verdict CAN OCCUR, not that any pinned corpus claim does occur.
All arithmetic in the exhibits was machine-verified on 2026-09-06 under /usr/bin/python3
(the verification numbers are printed inside each exhibit).

Exhibition corpus E (constructed; file:line references are concrete within the fiction):
- E1  paperA.tex l.214 prints "rho_c = 9.2e-27 kg m^-3"; recipe rho_c = 3 H0^2 / (8 pi G)
      stated l.211. Inputs: H0 = 70 km s^-1 Mpc^-1 printed l.209 (status PRINTED; origin
      CHOSEN, evidence ORIG_CHOICE_STATED l.209 — origin recorded, not gating, under
      option (c)); G (status STANDARD, ledger key G, value 6.67430e-11, ORIG_CONSTANT).
      No stated uncertainty; printed precision 2 s.f.
      Machine check: rho_c = 9.203873922972522e-27 -> rounds to 9.2e-27 = printed.
- E2  paperA.tex l.318: same recipe and inputs as E1; prints "rho_c = 8.5e-27 kg m^-3".
      Machine check: reproduced 9.2e-27 != printed 8.5e-27 at stated (printed) precision.
- E3  paperB.tex l.102 prints "age = 13.97 Gyr"; recipe t = 1/H0 stated l.100;
      H0 = 70 km s^-1 Mpc^-1 printed l.99 (PRINTED). Printed precision 3 s.f.
      Machine check: t = 13.9685 Gyr -> rounds to 13.97 = printed.
- E4  paperC.tex l.55 prints "n(z=1) = 2.7e-3 Mpc^-3"; recipe n = n0 (1+z)^3 stated l.52.
      n0 is not printed anywhere in paperC; l.53 says "n0 taken from Smith & Jones (2024),
      Table 2". Smith & Jones (2024) is not an enumerable text pinned in
      R3C2_CORPUS_MANIFEST.md. (Second limb, same class: it IS pinned, but the cited line
      carries no machine-matchable value.)
- E5  paperD.tex l.77 prints "mu = 33.62 mag"; recipe mu = m - M stated l.76; m = 14.2
      printed l.75 (PRINTED); M is neither printed anywhere in paperD nor traced to any
      named source.
- E6  paperE.tex l.140 prints "the sound horizon at recombination is 147 Mpc" asserted as
      the paper's own result; the only accompanying sentence is "computed using standard
      methods" — a procedure named but not specified.
- E7  paperF.tex l.88 prints a ratio whose recipe requires numerical integration of a
      stiff coupled ODE system; the mechanical attempt under
      `/usr/bin/python3 r3c2_timeout.py 120.0 -- <command>` (§9) exceeds the 120.0 s
      monotonic deadline. Second limb: a claim whose recipe requires a Boltzmann solver
      the lane does not have.
- E8  paperG.tex l.201 prints "r = 1.00" (2 d.p., no stated uncertainty); recipe r = A/B
      stated l.199; A = 2.01 and B = 2.00 both printed l.198 (both PRINTED).
      Machine check: exact decimal 2.01/2.00 = 1.005 exactly;
      IEEE-754 double 2.01/2.00 = 1.00499999999999989341858963598497211933135986328125.
      Rounding half away from zero at 2 d.p.: exact -> 1.01 (!= printed); double -> 1.00
      (= printed). A genuine knife-edge under §3's rounding rule, which fixes the rounding
      direction but does not pin the evaluation semantics of "the reproduced value".

=====================================================================
(A) §3 PER-CLAIM OUTCOMES — SIX DECLARED, SIX EXHIBITED
=====================================================================
§3 precedence, verbatim: "Exactly one outcome is filed per claim. Where more than one
terminal condition holds, file the first in this order: `REPRO_NO_DERIVATION_STATED`,
`REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`, `REPRO_NOT_EVALUABLE`, then the arithmetic group."
Arithmetic group, verbatim: "exactly `REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED`".

verdict | concrete input | clause path | reachable
---|---|---|---
REPRO_WITHIN_STATED_PRECISION | E1 (also E3): recipe stated; every input PRINTED or STANDARD; mechanical evaluation 9.203873922972522e-27 rounds to the printed 9.2e-27 at the printed 2 s.f. precision. rests_on (script-computed, USES_CHOSEN from the CHOSEN H0 root) is reported beside it and does not gate. | §1 include (printed numeral asserted as own result) -> §2 steps 1-3 (extract; inputs classified PRINTED/STANDARD) -> §2 step 4 ("follow the paper's own recipe, using every value it directs you to use, i.e. every ledger record with status PRINTED or STANDARD") -> §3 precedence walk: NO_DERIVATION no (recipe stated), BLOCKED no, ABSENT no, NOT_EVALUABLE no -> arithmetic group -> §3 REPRO_WITHIN_STATED_PRECISION: "the paper's number follows, within its own stated precision, from the paper's own recipe applied to the inputs it states"; no stated uncertainty -> the rounding rule ("must round to the printed numeral at that precision, rounding half away from zero") is satisfied. | YES
REPRO_FAILED | E2: identical recipe and inputs to E1 — inputs sufficient — but the paper prints 8.5e-27 and the recipe gives 9.2e-27; mismatch at the stated (printed) precision. | §1 include -> §2 steps 1-4 as above -> §3 precedence walk passes the four non-arithmetic classes -> arithmetic group -> §3 REPRO_FAILED: "the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number. Report both numbers." Wording: "unreproduced from the stated inputs". rests_on reported beside it. | YES
REPRO_BLOCKED | E4: recipe stated (so NO_DERIVATION does not fire); n0 not printed in the claiming paper; the paper NAMES a source — "Smith & Jones (2024), Table 2" — that is not an enumerable text pinned in R3C2_CORPUS_MANIFEST.md (second limb: pinned, but no machine-match at the cited line). | §2 step 3 -> status BLOCKED ("traced to a named source but carrying no machine-matchable value"); §2: "a cited value that does not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest, files REPRO_BLOCKED under §3"; "A seat may not supply a value for an ABSENT or BLOCKED input. Encountering one ends that claim's attempt." -> §3 precedence: NO_DERIVATION no, then BLOCKED — filed before ABSENT, exactly as the precedence orders. §3 REPRO_BLOCKED definition quoted in part: "an input whose value the claiming paper does not print, and for which the claiming paper names a source (a citation) that either is not an enumerable text pinned in R3C2_CORPUS_MANIFEST.md or is an enumerable pinned text at whose cited line the value does not machine-match; in the first case whether that source is obtainable elsewhere is irrelevant, because the census may not open or consume it." C3 records it: status BLOCKED, origin IMPORTED, ORIG_CITATION cited to the naming sentence, no value. | YES
REPRO_NOT_EVALUABLE | E7, both limbs. Limb (i): the §9 wrapper enforces the 120.0 s monotonic deadline on the stiff ODE integration; on the deadline it "prints SYMBOLIC_TIMEOUT and exits 124". Limb (ii): the recipe requires a Boltzmann solver the lane does not have -> MACHINERY_UNAVAILABLE. | §2 step 4 attempt -> §3 REPRO_NOT_EVALUABLE: "the arithmetic could not be completed within the 120-second cap, or requires machinery this lane does not have. Print SYMBOLIC_TIMEOUT when the 120-second cap is exceeded, or MACHINERY_UNAVAILABLE when the lane lacks the machinery, and the point reached." §3 precedence: NOT_EVALUABLE is fourth, reached here because no earlier terminal condition holds (recipe stated; all inputs PRINTED/STANDARD; the attempt simply cannot complete). §4's PARTIAL clause allows one repeat, "meaningful only for REPRO_NOT_EVALUABLE". | YES
REPRO_NO_DERIVATION_STATED | E6: "the sound horizon at recombination is 147 Mpc" asserted as the paper's own result (so it IS an included claim under §1), accompanied only by "computed using standard methods". | §1 include (the printed numeral asserted as its own result is sufficient; §3's own parenthetical: "A claim can satisfy §1 — a printed numeral asserted as the paper's own result — while the paper never says how it was obtained") -> §2 step 1 finds no equation to extract -> §3 REPRO_NO_DERIVATION_STATED: "the paper prints the claim as its own result but states no equation or computational procedure that could produce it, so there is nothing to attempt. Name the passage." Plus: "A procedure named but not specified — a sentence that says where the number came from without stating operations a seat could attempt — states no computational procedure that could produce it; file this class and name the passage." Precedence: FIRST in the §3 order — filed before any input-based class even though no input list exists. | YES
REPRO_INPUT_ABSENT | E5: recipe mu = m - M stated (so NO_DERIVATION does not fire); m = 14.2 printed; M is neither printed anywhere in paperD nor traced to any named source (so BLOCKED does not fire — no source is named). | §2 step 3 -> status ABSENT; §2: "A seat may not supply a value for an ABSENT or BLOCKED input. Encountering one ends that claim's attempt." -> §3 precedence: NO_DERIVATION no, BLOCKED no, then ABSENT -> §3 REPRO_INPUT_ABSENT: "an input the equation needs is ABSENT from the paper — neither printed nor traced to any named source — so the attempt stops there. Name the input." The §3 boundary sentence is honoured: "Distinct from a claim whose inputs the paper DOES state, chosen or not — that claim is attempted and files REPRO_WITHIN_STATED_PRECISION or REPRO_FAILED" (E1/E2 are that contrast case). | YES

=====================================================================
(B) §4 STUDY-LEVEL CLASSES — EIGHT DECLARED, EIGHT EXHIBITED
=====================================================================
§4 precedence, verbatim: "Exactly one study-level outcome is filed. Where more than one
condition holds, file the first in this order: `R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`,
`CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_OUTCOME_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`,
`CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`, `CENSUS_COMPLETE`. Once a stop class applies,
later limbs are unreached and their controls are `NOT_RUN`."
Each exhibit below also walks the precedence to show no EARLIER class's condition holds.

verdict | concrete input | clause path | reachable
---|---|---|---
R3C2_NO_CLASS | Three exhibited paths. (a) Pre-dispatch: the builder's forbidden-list assertion finds a forbidden string (e.g. the comparison model's name) surviving in the built packet -> "the packet is not written and C4_PACKET_REDACTED=FAIL" (C4) -> "a packet or seat-isolation failure before dispatch files this class" (§4.4). (b) In-run: C5's harness commands fail — e.g. `/usr/bin/python3 -c "import sympy; ..."` exits non-zero — in EVERY seat that attempted it, after two attempts -> C5_HARNESS_PINNED=FAIL everywhere -> §4.4 first limb. (c) RECORDED REAL INSTANCE: §10.18 — the 2026-09-06 10:17 KST dispatch under signed V23: "the seat stopped at C5, filed R3C2_NO_CLASS for itself, and read no source". The class has already been filed once in this lane's own record. | §4 class 4, verbatim: "a control among C0 through C5b fails in every seat that attempted it after two attempts; a packet or seat-isolation failure before dispatch files this class. A C6 audit failure or a seal-receipt failure files CENSUS_AUDIT_FAILED, not this class." Precedence: FIRST in the §4 order — nothing precedes it. | YES
CENSUS_CONTROL_SPLIT | C2 run: seat A's ledger validates (`/usr/bin/python3 r3c2_ledger_tools.py validate ledgerA.json .` exit 0, PASS); seat B's ledger fails validation (exit 1: one PRINTED value does not machine-match its cited source line); the split persists after two attempts in each seat. Boundary shown: if B's failure had occurred in A as well — every seat — §4.4 (R3C2_NO_CLASS) would fire instead, and the precedence order files it first. | §4 class 8, verbatim: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not adopt the passing seat's result." Precedence walk: NO_CLASS no (not every seat) -> CONTROL_SPLIT yes; stop. | YES
CENSUS_DENOMINATOR_DISPUTED | Two exhibited paths. (a) Enumeration split: seat A includes paperH.tex l.214 ("13.8 Gyr" read as the paper's own result); seat B excludes the same passage as ATTRIBUTED_NOT_DERIVED; two reconciliation attempts fail to resolve it. (b) Input-list split on agreed claims: seats agree on every candidate, but for E3 seat A lists {H0} and seat B lists {H0, Omega_m}; `r3c2_lane_tools.py merge` exits 1 (input_id sets differ); the one reconciliation against the paper's stated equation fails to resolve it. | §1, verbatim in part: "disagreement on any candidate that survives two reconciliation attempts stops the study under CENSUS_DENOMINATOR_DISPUTED (§4)"; §6 limb A: "tolerance zero, measured in candidate passages". C3 lane side, verbatim in part: "if merge exits 1, the two seats reconcile their input lists against the paper's stated equation once; an input-set difference surviving that reconciliation stops the study under CENSUS_DENOMINATOR_DISPUTED (§4), the disputed inputs listed with both seats' quotations". §4 class 5, verbatim: "the two enumerations disagree after two reconciliation attempts, or the two seats' input lists for the agreed claims disagree after the one C3 reconciliation." Precedence walk: NO_CLASS no, CONTROL_SPLIT no -> DENOMINATOR_DISPUTED yes; stop; "the census does not proceed; the disputed candidates or inputs are listed." | YES
CENSUS_OUTCOME_DISPUTED | E8 knife-edge (machine-verified): both seats follow the same recipe r = A/B on the same PRINTED inputs A = 2.01, B = 2.00. Seat A evaluates in exact decimal: 1.005 -> half away from zero at 2 d.p. -> 1.01 != printed 1.00 -> files REPRO_FAILED. Seat B evaluates in IEEE-754 double: 1.00499999999999989341... -> rounds to 1.00 -> files REPRO_WITHIN_STATED_PRECISION. §3's rounding rule fixes the rounding direction but does not pin the evaluation semantics of "the reproduced value", so the one permitted reconciliation against the printed numeral and the stated-precision rule does not resolve the split; each seat's filed outcome stands. | §2 step 5, verbatim in part: "a disagreement surviving that reconciliation files CENSUS_OUTCOME_DISPUTED (§4)". §4 class 6, verbatim: "the two seats' filed per-claim outcomes on an agreed included claim differ after one reconciliation against the printed numeral and the stated-precision rule of §3. The census does not proceed; the claim is listed with both seats' outcomes, both number pairs, and the step each seat reached." Both number pairs here: (printed 1.00, reproduced 1.005) and (printed 1.00, reproduced 1.00499999999999989...). Precedence walk: NO_CLASS / CONTROL_SPLIT / DENOMINATOR_DISPUTED no -> OUTCOME_DISPUTED yes; stop. (Class added at V21 by the principal's ruling "1a", §10.15.) | YES
CENSUS_ORIGIN_DISPUTED | 10 included claims. paperJ.tex l.33: "We adopt H0 = 67.4 from Planck (2018)". Seat A files ORIG_CITATION -> IMPORTED (the sentence names an external source for the value; the C3 tie-break puts ORIG_CITATION first "whatever else [the sentence] says"). Seat B files ORIG_CHOICE_STATED -> CHOSEN, holding that "We adopt" is the stated choice and disputing that the citation code matches. The H0 input feeds claims J1 and J2 — 2 of 10 included claims = 20% > 10%. The dispute is reported, never reconciled. | C3, verbatim in part: "Every input's origin is classified independently by both seats." C6, verbatim in part: "An input on which the two classifications disagree is filed ORIGIN_DISPUTED and reported with both seats' classification and both quotations; it is not reconciled. Above 10% of included claims, CENSUS_ORIGIN_DISPUTED." §4 class 7, verbatim: "the two seats' independent origin classifications disagree on inputs affecting more than 10% of included claims. The census does not proceed; every disputed input is listed with both seats' classification and both quotations." C3's own stated floor makes the case realistic: a precedence misapplication "is caught only by the second seat's independent classification and the C6 re-classification, never by the machine". Precedence walk: the four earlier classes' conditions do not hold -> ORIGIN_DISPUTED yes; stop. | YES
CENSUS_AUDIT_FAILED | Three exhibited paths. (a) MISMATCH: the auditor, without sight of earlier work, re-derives E1's outcome and obtains REPRO_FAILED against the sealed REPRO_WITHIN_STATED_PRECISION -> a MISMATCH row in C6_AUDIT.json -> C6_AUDIT_SAMPLE != PASS. (b) Seed missing: the external custodian's seed is not supplied and recorded with the receipt -> audit does not run. (c) Seal-receipt failure: after opening, Blanc's independent re-hash of the tally mismatches receipt T (or a receipt is missing). | §4 class 3, verbatim: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the cause named), or the receipt verification of the seal fails. No tally is filed; report which." C6, verbatim: "If the seed is not supplied and recorded with the receipt, the audit does not run, C6_AUDIT_SAMPLE=NOT_RUN, and the study files CENSUS_AUDIT_FAILED with the missing seed named." §7, verbatim in part: "Any missing receipt or mismatch files CENSUS_AUDIT_FAILED (§4 ...), leaves the interpretation NOT_RUN and voids the comparison." §4.4's carve-out routes C6/seal failures HERE, not to R3C2_NO_CLASS. Precedence: sixth — ahead of both PARTIAL and COMPLETE, so an audit failure can never co-file with either tally class. | YES
CENSUS_PARTIAL | Two exhibited paths. (a) Non-arithmetic claim present: corpus C-dagger = {E1, E3, E5}. E1 and E3 file REPRO_WITHIN_STATED_PRECISION; E5 files REPRO_INPUT_ABSENT. The one permitted repeat is meaningful only for NOT_EVALUABLE, so E5's outcome stands. Audit runs: limb (i) audits E1 and E3; limb (ii) sample of the remaining: N = 3, R = 1, k = min(max(1, ceil(0.20 x 3)), 1) = 1 (machine-checked) -> E5 audited; no MISMATCH -> C6_AUDIT_SAMPLE=PASS. Precedence then files PARTIAL. (b) Zero denominator: every enumerated candidate in the corpus is excluded under §1 (all numerals are dates or attributed-not-derived) -> denominator 0 -> "CENSUS_PARTIAL with the empty enumeration named; no census is complete over nothing." | §4 class 2, verbatim: "after the §2 attempt (one repeat permitted, meaningful only for REPRO_NOT_EVALUABLE), at least one included claim carries a non-arithmetic outcome (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT, REPRO_BLOCKED, REPRO_NOT_EVALUABLE), or the denominator is zero. Report each and why. INCONCLUSIVE, and it takes precedence over CENSUS_COMPLETE." Precedence walk: no stop class applies (controls pass; enumerations, outcomes, origins agree; audit PASS) -> PARTIAL yes, filed before COMPLETE is ever evaluated. | YES
CENSUS_COMPLETE | Corpus C-star = {E1, E2, E3}: every included claim carries exactly one arithmetic-group outcome — E1 WITHIN, E2 FAILED, E3 WITHIN. (Note: E2's REPRO_FAILED is INSIDE the arithmetic group; a failure to reproduce does not block COMPLETE.) Denominator = 3 > 0. Audit: limb (i) re-derives all three (arithmetic group, no sampling discount); remaining_ids = sorted({E1,E2,E3} - {E1,E2,E3}) = empty, R = 0 -> "when R is zero the sample is empty and every included claim is already audited under (i)"; C6_AUDIT.json carries no MISMATCH and no incompleteness -> C6_AUDIT_SAMPLE=PASS; the custodian's seed was supplied and recorded with receipt T; both receipts verify. | §4 class 1, verbatim: "every included claim carries exactly one outcome from the arithmetic group of §3, with C6_AUDIT_SAMPLE=PASS. A denominator of zero files CENSUS_PARTIAL with the empty enumeration named; no census is complete over nothing." Full precedence walk: R3C2_NO_CLASS no (all controls C0-C5b pass in every seat); CENSUS_CONTROL_SPLIT no; CENSUS_DENOMINATOR_DISPUTED no (enumerations and input lists agree); CENSUS_OUTCOME_DISPUTED no (seats agree on all three outcomes); CENSUS_ORIGIN_DISPUTED no (origin agreement, <=10%); CENSUS_AUDIT_FAILED no (audit PASS, receipts verify); CENSUS_PARTIAL no (no non-arithmetic outcome; denominator 3 != 0) -> CENSUS_COMPLETE filed. "Report the full tally with its denominator, and the rests_on tally beside it — two tallies from one pass." | YES

=====================================================================
(C) REACHABILITY STATEMENT, PER DECLARED VERDICT
=====================================================================
§3: REPRO_WITHIN_STATED_PRECISION reachable; REPRO_FAILED reachable; REPRO_BLOCKED
reachable; REPRO_NOT_EVALUABLE reachable (both print-codes); REPRO_NO_DERIVATION_STATED
reachable; REPRO_INPUT_ABSENT reachable.
§4: R3C2_NO_CLASS reachable (and already once filed, §10.18); CENSUS_CONTROL_SPLIT
reachable; CENSUS_DENOMINATOR_DISPUTED reachable (both limbs); CENSUS_OUTCOME_DISPUTED
reachable; CENSUS_ORIGIN_DISPUTED reachable; CENSUS_AUDIT_FAILED reachable (all three
limbs); CENSUS_PARTIAL reachable (both limbs); CENSUS_COMPLETE reachable.
Every declared §3 outcome and every declared §4 class is exhibited. None is UNREACHABLE.

=====================================================================
THE SUSPICION, ANSWERED DIRECTLY: CENSUS_COMPLETE — REACHABLE
=====================================================================
Question put to this seat: in a real corpus of many papers, does a single blocked,
absent-input, or no-derivation-stated claim anywhere force CENSUS_PARTIAL and make
CENSUS_COMPLETE unreachable in practice?

Answer: REACHABLE. The forcing mechanism the suspicion names is REAL and is confirmed,
but it is CONDITIONAL, not STRUCTURAL. Routing, clause by clause:

1. The condition. §4.1: CENSUS_COMPLETE requires "every included claim [to carry]
   exactly one outcome from the arithmetic group of §3, with C6_AUDIT_SAMPLE=PASS",
   and "no census is complete over nothing" (denominator > 0).
2. The fragility. §4.2: "at least one included claim carries a non-arithmetic outcome
   (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT, REPRO_BLOCKED, REPRO_NOT_EVALUABLE),
   or the denominator is zero ... and it takes precedence over CENSUS_COMPLETE." The §4
   filing order enforces that precedence: CENSUS_PARTIAL sits ahead of CENSUS_COMPLETE.
   §5's C0 note says it in one sentence: "CENSUS_COMPLETE requires every included claim
   to carry an arithmetic-group outcome, which a single blocked or absent input in the
   whole corpus is enough to prevent." Confirmed: ONE claim filing E4/E5/E6/E7's outcome
   anywhere in the corpus routes the study to CENSUS_PARTIAL (or, earlier, to a stop
   class). The class is one-claim-fragile by construction.
3. Why fragile is not unreachable. "Enough to prevent" is a conditional: it fires only
   IF such a claim exists in the enumeration. No clause in the document requires any
   included claim to file a non-arithmetic outcome; §1's inclusion rule (a printed
   numeral asserted as the paper's own result) does not entail blocked, absent or
   derivation-less inputs. Corpus C-star above — {E1, E2, E3} — is a concrete input on
   which every conjunct holds: all three claims arithmetic-group, denominator 3 > 0,
   audit PASS with the empty-sample limb (R = 0) executed per C6's own sentence, seed
   receipted, receipts verifying, and the full §4 precedence walk landing on COMPLETE.
   The class CAN OCCUR; the routing is exhibited, not asserted.
4. What the exhibition does NOT claim. Whether the PINNED corpus (89 enumerable texts,
   106,676 non-blank lines, §10.5) contains even one blocked/absent/no-derivation/
   not-evaluable claim is an empirical question the census itself exists to answer.
   C0 tests possibility, and possibility is exhibited. It is also worth stating what
   COMPLETE tolerates: REPRO_FAILED is inside the arithmetic group, so a corpus in
   which EVERY paper's arithmetic fails still files CENSUS_COMPLETE if every claim was
   evaluable from stated inputs. COMPLETE is not the favourable pole of the design;
   it is the "every claim was decidable" pole.
5. Compound dependence, for the record: CENSUS_COMPLETE = (denominator > 0) AND
   (every included claim in the arithmetic group) AND (C6_AUDIT_SAMPLE=PASS) AND
   (no earlier stop condition). The audit conjunct adds its own reachability
   requirements — an external seed supplied and receipted (C6), receipts P and T
   verifying (§7), no MISMATCH — each of which is exhibited in the CENSUS_AUDIT_FAILED
   row as a failure mode and in the C-star walk as a pass.

=====================================================================
UNREACHABLE VERDICTS AND THEIR BLOCKING CLAUSES
=====================================================================
None. Every per-claim outcome of §3 (six) and every study-level class of §4 (eight) is
exhibited above with a concrete input and a clause path. There is no blocking clause to
quote. (For the record, the only unreachable verdict ever found in this lane's C0 history
was REPRO_AFTER_CHOICE under the retired option (b) wording, blocked by §2 step 4's then
admissible-inputs-only attempt — §10.3; that class was retired by the option (c) ruling
and is not a §3 outcome of the text exhibited here.)

Scope note: only the target file was read (in full, 1046 lines). No other file in the
lane directory was opened. The two arithmetic-verification scripts lived in /tmp,
outside the lane directory, and ran under /usr/bin/python3.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V24_KIMI_COMPLETE

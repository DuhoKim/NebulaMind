ACCESS_SHA=55b466fadf8ca75f4894f97721da86584057ddc4d15c15ca1739c67ff6333c6f
C0_REACHABILITY=PASS

R3-C2 V23 — C0 REACHABILITY EXHIBITION (kimi seat, 2026-09-06)

Scope and access. The only file read is R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md, in full (1023 lines);
its sha256, computed by this seat with `shasum -a 256`, is 55b466fadf8ca75f4894f97721da86584057ddc4d15c15ca1739c67ff6333c6f,
matching the value the brief expected. No other file in the directory was opened. §3's per-claim outcomes and §4's
study-level classes are exhibited against V23's text exactly as it stands. This exhibition does not gate the design
and does not judge its physics; it asks only whether each declared verdict CAN OCCUR, and shows the routing.

Held-clause dependence, stated rather than assumed. No HELD marker stands in the operative text. Every occurrence
of HELD sits inside §10's history (10 occurrences, lines 520–691, all §10.x); §10.4 records the marker's removal at
V10 under the ruling "Q-R3C2 c" (one pass, two tallies; REPRO_AFTER_CHOICE retired into the script-computed
rests_on field). §1's core definition is therefore exhibited as it stands, under the settled option-(c) wording —
that dependence is marked here, not silently assumed: every row that routes through the arithmetic group depends on
§1's inclusion rule ("a passage in a pinned source that prints a numeral the paper asserts as a result of its own",
with the five excluded kinds) and on §3 as ruled. The four terminal per-claim classes (NO_DERIVATION_STATED,
BLOCKED, INPUT_ABSENT, NOT_EVALUABLE) and §4's stop classes do not depend on it.

(A) §3 per-claim outcomes — six declared. (REPRO_AFTER_CHOICE is retired at V10 and is not a declared outcome;
the exclusion-ledger kinds EQUATION_NUMBER / REFERENCE_NUMBER / PAGE_OR_LINE_NUMBER / DATE / ATTRIBUTED_NOT_DERIVED
are explicitly "not per-claim outcomes" per §3.) §3 precedence, quoted: "Exactly one outcome is filed per claim.
Where more than one terminal condition holds, file the first in this order: REPRO_NO_DERIVATION_STATED,
REPRO_BLOCKED, REPRO_INPUT_ABSENT, REPRO_NOT_EVALUABLE, then the arithmetic group." The arithmetic group is
"exactly REPRO_WITHIN_STATED_PRECISION and REPRO_FAILED".

verdict | concrete input | clause path | reachable
---|---|---|---
REPRO_WITHIN_STATED_PRECISION | Claim A1 (paper A): "the Hubble time is 14.5 Gyr", recipe t_H = 1/H₀ stated; H₀ printed as "67.36 km s⁻¹ Mpc⁻¹", a verbatim member of C3's closed list (row `H0`, value string `67.36`). Reproduced: 1 Mpc = 3.0856776e19 km (exact by definition); t_H = Mpc/H₀ ≈ 4.5809e17 s ≈ 14.516 Gyr. No stated uncertainty → the rounding rule at the printed tenths precision: 14.516 → 14.5. Match. | §1 inclusion → §2 steps 1–3 (extract; list inputs; H₀ classified STANDARD — a value the paper prints, on the closed list verbatim) → §2 step 4 (mechanical attempt consumes status PRINTED/STANDARD) → §2 step 5 record → §3 REPRO_WITHIN_STATED_PRECISION definition + stated-precision/rounding rule; no earlier precedence limb holds → arithmetic group. rests_on computed by script from the ledger. | YES
REPRO_FAILED | Claim A2 (paper B): "the Hubble time is 13.0 Gyr", same stated recipe t_H = 1/H₀, same printed H₀ = 67.36. Reproduced ≈ 14.516 Gyr; at the printed precision (tenths) 13.0 ≠ 14.5; no stated uncertainty. Inputs sufficient; arithmetic completes. | §1 → §2 steps 1–4 as above → §3 REPRO_FAILED: "the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number. Report both numbers." Wording: "unreproduced from the stated inputs," not "error". No earlier precedence limb holds → arithmetic group. | YES
REPRO_BLOCKED | Claim A3 (paper C): "with γ from (Zel'dovich & Novikov 1971, eq. 12.4) we obtain β = 0.83 via β = γ/2" — γ's value never printed in the claiming paper; the named source is not an enumerable text pinned in R3C2_CORPUS_MANIFEST.md. (Second limb, same class: the named source IS a pinned enumerable text but the value does not machine-match at the cited line.) | §2 IMPORTED rule: "only when such a match exists; a cited value that does not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest, files REPRO_BLOCKED under §3" → §2 bar: "A seat may not supply a value for an ABSENT or BLOCKED input. Encountering one ends that claim's attempt." → §3 REPRO_BLOCKED ("whether that source is obtainable elsewhere is irrelevant, because the census may not open or consume it"). C3: status BLOCKED, origin IMPORTED, ORIG_CITATION cited to the naming sentence, no value. Precedence: BLOCKED ahead of ABSENT / NOT_EVALUABLE / arithmetic. | YES
REPRO_NOT_EVALUABLE | Claim A4 (paper D): "ω = 0.42 s⁻¹ is the root of det(M(ω)) = 0", M a fully stated 40×40 matrix of Bessel functions with every parameter printed — operations are stated (so NO_DERIVATION_STATED does not hold), all inputs PRINTED, but the root-find launched through r3c2_timeout.py does not finish inside the 120.0-s monotonic deadline → wrapper prints SYMBOLIC_TIMEOUT, exit 124. Second limb: a stated FFT over a stated 10⁹-point grid → MACHINERY_UNAVAILABLE. | §9 (every symbolic operation through the committed wrapper; on the deadline it "prints SYMBOLIC_TIMEOUT and exits 124 — the reportable outcome") → §3 REPRO_NOT_EVALUABLE ("the arithmetic could not be completed within the 120-second cap, or requires machinery this lane does not have. Print SYMBOLIC_TIMEOUT ... or MACHINERY_UNAVAILABLE ..., and the point reached"). Precedence: NO_DERIVATION / BLOCKED / ABSENT do not hold. | YES
REPRO_NO_DERIVATION_STATED | Claim A5 (paper E): "the resulting suppression is 8.2%", asserted as the paper's own result; the paper says only "obtained from our analysis pipeline" — no equation, and no operations a seat could attempt. | §1 satisfied (numeral asserted as the paper's own result) → §2 step 1 finds no equation to extract → §3 REPRO_NO_DERIVATION_STATED: "states no equation or computational procedure that could produce it, so there is nothing to attempt. Name the passage. A procedure named but not specified — a sentence that says where the number came from without stating operations a seat could attempt — states no computational procedure that could produce it; file this class and name the passage." Precedence: first in the §3 order. | YES
REPRO_INPUT_ABSENT | Claim A6 (paper F): "the ratio is 2.35 from r = x/y", x = 4.69 printed; y is nowhere printed and no source is named for it. | §2 step 3: y classified ABSENT ("neither printed nor traced to any named source") → §2 bar: "A seat may not supply a value for an ABSENT ... input. Encountering one ends that claim's attempt." → §3 REPRO_INPUT_ABSENT ("so the attempt stops there. Name the input."). Precedence: NO_DERIVATION does not hold (equation stated); BLOCKED does not hold (no named source); ABSENT files. | YES

(B) §4 study-level classes — eight declared. §4 precedence, quoted: "Exactly one study-level outcome is filed.
Where more than one condition holds, file the first in this order: R3C2_NO_CLASS, CENSUS_CONTROL_SPLIT,
CENSUS_DENOMINATOR_DISPUTED, CENSUS_OUTCOME_DISPUTED, CENSUS_ORIGIN_DISPUTED, CENSUS_AUDIT_FAILED, CENSUS_PARTIAL,
CENSUS_COMPLETE. Once a stop class applies, later limbs are unreached and their controls are NOT_RUN."

verdict | concrete input | clause path | reachable
---|---|---|---
CENSUS_COMPLETE | Corpus = claims A1 and A2 above (one WITHIN, one FAILED — COMPLETE does not require every claim to reproduce; it requires every claim to resolve into the arithmetic group). Both seats' enumerations agree, input lists agree, outcomes agree, origins agree on >90% of claims; all controls C0–C5b pass in every seat; C6 audits every arithmetic-group claim (no sampling discount), re-derives both with MATCH, finds no ledger incompleteness, external seed supplied and recorded with receipt T → C6_AUDIT_SAMPLE=PASS. | Per claim: §2 → §3 arithmetic group (rows above). Study level: §4.1 "every included claim carries exactly one outcome from the arithmetic group of §3, with C6_AUDIT_SAMPLE=PASS"; denominator 2 ≠ 0. Precedence walk: no NO_CLASS (no control failed), no CONTROL_SPLIT, no DENOMINATOR/OUTCOME/ORIGIN dispute, AUDIT ran to PASS (so no AUDIT_FAILED), PARTIAL's condition absent (no non-arithmetic outcome; denominator non-zero) → CENSUS_COMPLETE files, last in the order. Full tally + rests_on tally reported, "two tallies from one pass". | YES — see (C)
CENSUS_PARTIAL | Corpus = claims A1 + A6: A6 files REPRO_INPUT_ABSENT after the §2 attempt (the one repeat is "meaningful only for REPRO_NOT_EVALUABLE", so the ABSENT claim is not re-attempted). Zero-denominator limb: both seats' enumerations agree that every candidate passage is an excluded kind (all equation numbers or attributed-not-derived numerals) → denominator 0. | §4.2: "after the §2 attempt (one repeat permitted, meaningful only for REPRO_NOT_EVALUABLE), at least one included claim carries a non-arithmetic outcome (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT, REPRO_BLOCKED, REPRO_NOT_EVALUABLE), or the denominator is zero. ... INCONCLUSIVE, and it takes precedence over CENSUS_COMPLETE." §4.1: "A denominator of zero files CENSUS_PARTIAL with the empty enumeration named; no census is complete over nothing." Precedence: PARTIAL ahead of COMPLETE only; no earlier stop limb holds. | YES
CENSUS_AUDIT_FAILED | C6 auditor, without sight of earlier work, re-derives claim A2 and obtains WITHIN where the sealed record says FAILED → a MISMATCH row in C6_AUDIT.json. Other licensed routes to the same class: any ledger incompleteness in the full-ledger audit; the audit not running to PASS for any cause, the cause named — including the external seed never supplied and recorded with receipt T (then C6_AUDIT_SAMPLE=NOT_RUN); and a seal-receipt failure (§7: "Any missing receipt or mismatch files CENSUS_AUDIT_FAILED"). | §4.3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the cause named), or the receipt verification of the seal fails. No tally is filed; report which." C6: PASS requires the printed C6_AUDIT.json "carries no MISMATCH and no incompleteness; a token without the artefact is FAIL." Precedence: AUDIT_FAILED ahead of PARTIAL/COMPLETE, behind the dispute classes. | YES
R3C2_NO_CLASS | C5 harness: `/usr/bin/python3 -c "import sympy; ..."` exits 1 in every seat that attempts it, on both attempts. Pre-dispatch limb: the packet builder's forbidden-list assertion finds a surviving string → C4_PACKET_REDACTED=FAIL, no dispatch. | §4.4: "a control among C0 through C5b fails in every seat that attempted it after two attempts; a packet or seat-isolation failure before dispatch files this class." Boundary respected: "A C6 audit failure or a seal-receipt failure files CENSUS_AUDIT_FAILED, not this class." Precedence: first in the §4 order. | YES
CENSUS_DENOMINATOR_DISPUTED | Candidate passage in paper G printing "σ₈ = 0.811": seat A includes it as the paper's own result; seat B excludes it as ATTRIBUTED_NOT_DERIVED; the disagreement survives two reconciliation attempts. Second limb: the two seats' input lists for the agreed claims differ and the difference survives the one C3 reconciliation (merge exit 1 persists). | §1: "disagreement on any candidate that survives two reconciliation attempts stops the study under CENSUS_DENOMINATOR_DISPUTED (§4): the disputed candidates are listed and the complete candidate and exclusion ledgers are reported with the dispute." §4.5: "or the two seats' input lists for the agreed claims disagree after the one C3 reconciliation. The census does not proceed; the disputed candidates or inputs are listed." §6 limb A: "tolerance zero, measured in candidate passages." | YES
CENSUS_OUTCOME_DISPUTED | Agreed claim in paper H: "the ratio is 2.35", recipe r = x/y stated, x = 4.69 printed, y = 2 printed. r = 2.345 exactly — the midpoint at the printed hundredths precision. Seat A applies the §3 rule ("rounding half away from zero") → 2.35 → REPRO_WITHIN_STATED_PRECISION. Seat B truncates (or rounds half to even) → 2.34 → REPRO_FAILED. The one reconciliation against the printed numeral and the stated-precision rule moves neither seat. | §2 step 5: "a disagreement surviving that reconciliation files CENSUS_OUTCOME_DISPUTED (§4)". §4.6: "the two seats' filed per-claim outcomes on an agreed included claim differ after one reconciliation against the printed numeral and the stated-precision rule of §3. The census does not proceed; the claim is listed with both seats' outcomes, both number pairs, and the step each seat reached." (This midpoint is exactly what the V21 wording "rounding half away from zero" was added to decide; a surviving split here is the class's designed use.) | YES
CENSUS_ORIGIN_DISPUTED | Corpus of N = 10 included claims; the two seats' independent origin classifications disagree on inputs feeding 2 of the 10 (20% > 10%): e.g., paper J's sentence "we take β = 1/929.25" — seat A files ORIG_CHOICE_STATED→CHOSEN with its quotation; seat B files ORIG_SILENT→UNDECLARED with an origin_search. | §4.7: "the two seats' independent origin classifications disagree on inputs affecting more than 10% of included claims. The census does not proceed; every disputed input is listed with both seats' classification and both quotations." C6/§10.1: "Disagreement about provenance is reported, never reconciled." Edge note: 1 of 10 = 10% is not "more than 10%" and does NOT file — the affected claims then carry rests_on computed under both, marked DISPUTED, and the study proceeds. | YES
CENSUS_CONTROL_SPLIT | C2: seat A's printed `r3c2_ledger_tools.py validate` run exits 0; seat B's exits 1 (a PRINTED value in B's ledger fails machine-match at its cited line); the split persists after two attempts. | §4.8: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not adopt the passing seat's result." Precedence: second in the §4 order, behind R3C2_NO_CLASS (which requires failure in every seat). | YES

Declared conditions beyond the fourteen verdicts, each exhibited:
D1. Denominator zero → CENSUS_PARTIAL with the empty enumeration named — exhibited under CENSUS_PARTIAL above. Reachable.
D2. One repeat permitted, meaningful only for REPRO_NOT_EVALUABLE (§4.2) — claim A4 re-attempted once under the
    wrapper, times out again, stays NOT_EVALUABLE; the census then files CENSUS_PARTIAL. Reachable.
D3. rests_on NOT_COMPUTED row (§3: "a claim with no ledger record carries rests_on NOT_COMPUTED, and the rests_on
    tally reports a NOT_COMPUTED row") — claim A5 (NO_DERIVATION_STATED) has no equation → no inputs → no ledger
    record → NOT_COMPUTED. Reachable.
D4. rests_on DISPUTED pair (§3 master-only rule; C6: "computed under both classifications, printed as a pair and
    marked DISPUTED; the rests_on tally reports a DISPUTED row") — the 1-of-10 origin-dispute case above (10%,
    not >10%), so the study proceeds with the pair. Reachable.
D5. §3 precedence under co-occurrence — a claim carrying both a BLOCKED input and a determinantal root-find that
    would time out: the attempt ends at the BLOCKED input before any symbolic run; files REPRO_BLOCKED, the
    earlier of the two in the §3 order. Reachable.
D6. §4 precedence under co-occurrence — a tally with one REPRO_NOT_EVALUABLE claim (PARTIAL's condition) plus an
    audit MISMATCH (AUDIT_FAILED's condition): files CENSUS_AUDIT_FAILED, the earlier of the two in the §4 order.
    Reachable.

(C) THE CENSUS_COMPLETE SUSPICION, ANSWERED DIRECTLY: REACHABLE.

The suspicion is correct about the mechanism and wrong about the conclusion. The mechanism: §4.2 files
CENSUS_PARTIAL whenever "at least one included claim carries a non-arithmetic outcome ... or the denominator is
zero", and §4.2 takes precedence over §4.1; §4's filing order puts CENSUS_COMPLETE last. So yes — a single
blocked, absent-input, no-derivation-stated, or not-evaluable claim anywhere in the corpus forces CENSUS_PARTIAL.
That asymmetry is declared, not accidental: COMPLETE is the strict pole and PARTIAL is INCONCLUSIVE by definition.

But unreachability is a property of the clause space, not of how the corpus is likely to fall. The routing that
files CENSUS_COMPLETE is exhibited row-by-row above: a corpus whose every included claim states an equation and
prints (or imports via the §2 machine-match) every input, whose arithmetic completes inside the 120-second cap,
produces an arithmetic-group outcome for every claim; with both seats agreeing on enumeration, input lists,
outcomes and origins, all controls passing, and C6 running to PASS on an externally supplied seed, every earlier
limb of the §4 precedence fails to apply and the last limb — CENSUS_COMPLETE — files. No clause on that path bars
it: §4.1 defines the class, §4.2's precedence is escapable exactly when no claim carries a non-arithmetic outcome,
and C6's PASS conditions are satisfiable by honest work. To mark COMPLETE UNREACHABLE I would have to quote a
clause that blocks every path to it; there is none. Whether the real pinned corpus (89 enumerable texts, 106,676
non-blank lines, §10.5) contains even one such claim is the empirical question the census exists to answer — C0
does not and cannot answer it. (The gate record concurs: §10.5/§10.6 record both engines answering the
reachability question YES under option (c), and every C0 from V10 through V22 exhibited COMPLETE.)

UNREACHABLE VERDICTS: NONE. Every per-claim outcome of §3 (six) and every study-level class of §4 (eight) has a
row above carrying a concrete input, a clause path, and reachable = YES; the six declared conditions D1–D6 are
exhibited likewise. Had any verdict been unreachable, the blocking clause would be quoted verbatim in this section
and the row marked UNREACHABLE; no such clause exists in V23.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V23_KIMI_COMPLETE

ACCESS_SHA=fe194fb4aee7603dbeecbfeda62dc8507aba2a994e3b9a206c8089490700e1c9
C0_REACHABILITY=PASS

# R3C2 — C0 REACHABILITY EXHIBITION, V17 (kimi seat, 2026-09-05)

Scope: the C0 control of §5, run against `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md` (Version 17, §10.11) exactly as it
stands on disk. Only that file was read. This is an exhibition, not a gate and not a judgement of the physics or of the
design: for every per-claim outcome of §3, every study-level class of §4, and every declared sub-condition/limb, one
concrete input is exhibited and routed through the document's own clauses. Exhibits are constructed claims (specific
numeral, equation, inputs); they need only show the verdict CAN OCCUR.

Roster check. §3 declares exactly six per-claim outcomes: `REPRO_EXACT`, `REPRO_FAILED`, `REPRO_BLOCKED`,
`REPRO_NOT_EVALUABLE`, `REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`. `REPRO_AFTER_CHOICE` is NOT a declared
outcome in V17: §3 records it as "RETIRED at V10 by the principal's ruling adopting option (c)... it is retired, not
repaired," its content moved to the script-computed `rests_on` field. It therefore has no row below; the V9
unreachability finding is discharged by the ruling, not by this exhibition. §4 declares exactly seven study-level
classes. Declared sub-conditions exhibited separately: both `REPRO_BLOCKED` limbs, both `REPRO_NOT_EVALUABLE` print
conditions (`SYMBOLIC_TIMEOUT`, `MACHINERY_UNAVAILABLE`), both `CENSUS_AUDIT_FAILED` limbs plus the missing-seed route,
both `CENSUS_DENOMINATOR_DISPUTED` limbs, both `R3C2_NO_CLASS` limbs, the §3 co-occurrence precedence, and the §4 filing
precedence with its stop/NOT_RUN rule.

Stated dependence (a result in itself). Every §3 row presupposes a passage that BOTH seats include under §1's
operational definition ("a passage that prints a numeral the paper asserts as a result of its own", minus the five
excluded kinds). Inclusion is a judgement made by two seats who must agree; where they cannot, the route is
`CENSUS_DENOMINATOR_DISPUTED`, not a §3 outcome. §1's question embeds the settled §3 definition (option (c): one pass,
two tallies); this exhibition assumes that wording as marked and assumes no reading beyond it. The arithmetic
verifications below were machine-checked: 1093/67.4 = 16.2166; 13.797 rounds to 13.8 at one decimal; 3/20 = 0.150.

## (A) §3 per-claim outcomes — exhibition table

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `REPRO_EXACT` | Paper X prints "the age of the universe is 13.8 Gyr" as its own result, produced by its stated Friedmann-integral recipe from H₀ = 67.4 km s⁻¹ Mpc⁻¹ and Ω_m = 0.315, both printed in the paper with file/line. All inputs PRINTED; mechanical attempt yields 13.797 Gyr, which rounds to 13.8 Gyr at the printed precision (paper states no tighter precision). | §1 inclusion (own numeral) → §2.1 extract number+equation → §2.2 list inputs → §2.3 all `PRINTED` → §2.4 attempt consumes every `PRINTED` record → §2.5 record outcome → §3 `REPRO_EXACT` ("follows, within its own stated precision... Where the paper states no precision... must round to the printed numeral at that precision"); §3 precedence: no non-arithmetic terminal condition holds, arithmetic group reached, arithmetic succeeds. | YES |
| `REPRO_FAILED` | Paper Y prints "cz = 1093 km/s, H₀ = 67.4 km/s/Mpc, therefore d = 17.4 Mpc" via its stated d = cz/H₀. Both inputs PRINTED and sufficient; mechanical arithmetic gives 16.2 Mpc, not 17.4 Mpc. | §1 → §2.1–§2.3 (all `PRINTED`) → §2.4 attempt → §3 `REPRO_FAILED` ("the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number"); §3 precedence: arithmetic group reached; report both numbers; wording "unreproduced from the stated inputs," not "error." | YES |
| `REPRO_BLOCKED` (limb 1: named source not enumerable) | Paper Z prints "using the mass–richness calibration of Author et al. (2015), our stacked mass is 3.1e14 M☉" from its stated eq. (7); the calibration constant's value is nowhere printed; Author et al. (2015) is a citation that is NOT an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`. | §1 → §2.2 input listed → §2.3/§2-final: value not printed, named source not enumerable → status `BLOCKED` (C3: `origin` `IMPORTED`, `ORIG_CITATION` to the naming sentence, no value); §2 "A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt." → §3 `REPRO_BLOCKED`; precedence: `REPRO_NO_DERIVATION_STATED` does not hold (a recipe is stated), `REPRO_BLOCKED` is first applicable. | YES |
| `REPRO_BLOCKED` (limb 2: enumerable source, no machine-match) | Paper Z′ prints "taking the baryon density from Pinned-Text-B, we obtain T = 2.35 K" via its stated equation; Pinned-Text-B IS an enumerable text of the manifest, but at the cited line the value does not machine-match. | §1 → §2.3 named-source test → §2-final: "a cited value that does not machine-match at the named source's cited line... files `REPRO_BLOCKED` under §3" → status `BLOCKED`, attempt ends → §3 `REPRO_BLOCKED`, second disjunct ("is an enumerable pinned text at whose cited line the value does not machine-match"). | YES |
| `REPRO_NOT_EVALUABLE` (`SYMBOLIC_TIMEOUT`) | Paper W prints "the anomalous moment is 0.00115965218" from its stated closed-form loop-integral expression; all inputs PRINTED; the mechanical attempt is launched as `/usr/bin/python3 r3c2_timeout.py 120.0 -- <command>` and exceeds the 120.0-second monotonic deadline. | §1 → §2.4 attempt under §9's wrapper → wrapper prints `SYMBOLIC_TIMEOUT` and exits 124 → §3 `REPRO_NOT_EVALUABLE` ("the arithmetic could not be completed within the 120-second cap"), print `SYMBOLIC_TIMEOUT` and the point reached; precedence: recipe stated, no `BLOCKED`/`ABSENT` input, `NOT_EVALUABLE` is first applicable, ahead of the arithmetic group. | YES |
| `REPRO_NOT_EVALUABLE` (`MACHINERY_UNAVAILABLE`) | Paper W′ prints "our simulated cluster mass function peaks at 2.0e14 M☉" and states the number comes from running its N-body hydrodynamical simulation pipeline; the inputs are stated, but the procedure requires simulation machinery this lane does not have. | §1 → §2.4 attempt → machinery absent → §3 `REPRO_NOT_EVALUABLE`, print `MACHINERY_UNAVAILABLE` and the point reached. | YES |
| `REPRO_NO_DERIVATION_STATED` | Paper V prints "the structure-formation timescale for this system is 2.3 Gyr" as its own result; no equation or computational procedure anywhere in the paper states how 2.3 Gyr is obtained. | §1 inclusion (the numeral is asserted as the paper's own result — §3's note: a claim can satisfy §1 while the paper never says how it was obtained) → §2.1 requires "the equation the paper says produces it" — none exists → §3 `REPRO_NO_DERIVATION_STATED` ("there is nothing to attempt. Name the passage."); precedence: FIRST in the §3 order, so it is filed even if inputs would also be missing. | YES |
| `REPRO_INPUT_ABSENT` | Paper U prints "from our Friedmann equation (eq. 3), the age is 13.6 Gyr"; eq. 3 needs H₀, Ω_m, Ω_Λ; the paper prints Ω_m and Ω_Λ but prints no H₀ and names no source for it anywhere. | §1 → §2.2 list → §2.3: H₀ `ABSENT` ("neither printed nor traced to any named source"); `STANDARD` is barred because "a value the paper does not print is classified by the named-source rule alone and is never `STANDARD`" → §2 "a seat may not supply a value... ends that claim's attempt" → §3 `REPRO_INPUT_ABSENT` ("Name the input"); precedence: `NO_DERIVATION_STATED` no, `BLOCKED` no (no named source), `INPUT_ABSENT` first applicable. | YES |
| §3 co-occurrence precedence (declared condition) | Paper Q prints a claim whose stated equation needs input a (value not printed, named source not enumerable → `BLOCKED` condition) and input b (neither printed nor traced to any source → `ABSENT` condition). Both terminal conditions hold at once. | §3 precedence clause: "Exactly one outcome is filed per claim. Where more than one terminal condition holds, file the first in this order: `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`, `REPRO_NOT_EVALUABLE`, then the arithmetic group." → files `REPRO_BLOCKED`, exactly one outcome recorded. | YES |

## (B) §4 study-level classes — exhibition table

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `CENSUS_COMPLETE` | Corpus of 3 included claims (Paper X's 13.8 Gyr age, a PRINTED-input H₀ claim reproducing exactly, a PRINTED-input density claim failing the arithmetic). Every claim states a recipe; every input is `PRINTED` or `STANDARD`; every attempt terminates in the arithmetic group: two `REPRO_EXACT`, one `REPRO_FAILED`. Controls C0–C5b pass; enumerations and origins agree; audit reproduces the ledger; both seal receipts verify. | Per claim: §1 → §2 → §3 arithmetic group (exactly one outcome each, per §3's "Exactly one outcome is filed per claim") → §4.1: "every included claim carries exactly one outcome from the arithmetic group of §3" → §4 filing order: no stop class above holds; `CENSUS_PARTIAL` does not hold (no non-arithmetic outcome) → `CENSUS_COMPLETE` filed; full reproduction tally and `rests_on` tally reported. | YES (see suspicion section) |
| `CENSUS_PARTIAL` | The same 3-claim corpus plus Paper Z's claim (above), which files `REPRO_BLOCKED` because its calibration input names a non-enumerable source. | Per claim §2/§3 → §4.2: "after the §2 attempt (one repeat permitted, meaningful only for `REPRO_NOT_EVALUABLE`), at least one included claim carries a non-arithmetic outcome... INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`" → §4 order: no class above `CENSUS_PARTIAL` holds → `CENSUS_PARTIAL` filed; each non-arithmetic outcome reported with its reason. | YES |
| `CENSUS_AUDIT_FAILED` (limb i: audit cannot reproduce) | Tally sealed; custodian seed supplied and receipted; the C6 audit seat re-derives claim 17 (filed `REPRO_EXACT` by the working seats) from the pinned sources and obtains a value that does not round to the printed numeral — or finds the ledger incomplete against the paper's stated equation. | §4.3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger... No tally is filed; report which." → C6: "Any outcome the audit cannot reproduce, or any ledger incompleteness, files `CENSUS_AUDIT_FAILED`" → §4 order: nothing above holds → filed. | YES |
| `CENSUS_AUDIT_FAILED` (limb ii: seal receipt verification fails) | After opening, Blanc re-hashes the tally and the interpretation protocol and one value mismatches receipt T (or receipt P or T was never obtained before the protocol was opened). | §7: "Any missing receipt or mismatch files `CENSUS_AUDIT_FAILED` (§4, whose definition now names this case), leaves the interpretation `NOT_RUN` and voids the comparison" → §4.3 second disjunct ("or the receipt verification of the seal fails") → filed; no tally filed. | YES |
| `CENSUS_AUDIT_FAILED` (missing-seed route) | Tally digests committed; the external custodian's seed is not supplied and not recorded with the receipt. | C6: "If the seed is not supplied and recorded with the receipt, the audit does not run, `C6_AUDIT_SAMPLE=NOT_RUN`, and the study files `CENSUS_AUDIT_FAILED` with the missing seed named." → §4.3. | YES |
| `R3C2_NO_CLASS` (limb i: pre-dispatch packet failure) | The builder `r3c2_build_seat_packet.py` asserts the packet against the forbidden list and finds one enumerated string surviving in the output. | C4: "If any survives, the packet is not written and `C4_PACKET_REDACTED=FAIL`; the study does not proceed on a hand-checked copy" → §4.4: "a packet or seat-isolation failure before dispatch files this class" → §4 order: `R3C2_NO_CLASS` is FIRST → filed; later limbs unreached, their controls `NOT_RUN`. | YES |
| `R3C2_NO_CLASS` (limb ii: control fails in every attempting seat) | C5 harness: both seats run the three C5 commands; `import sympy` exits non-zero in both seats, on a first attempt and on the one repeat. | C5: "any non-zero exit, missing output... is FAIL" → §4.4: "a control among C0 through C5b fails in every seat that attempted it after two attempts" → `R3C2_NO_CLASS`; C6/seal failures are excluded from this class by §4.4's own carve-out. | YES |
| `CENSUS_DENOMINATOR_DISPUTED` (limb i: enumeration disagreement) | Seat A includes the passage printing "ρ_c = 8.5e-30 g/cm³"; seat B excludes it as `ATTRIBUTED_NOT_DERIVED`. Two reconciliation attempts fail to produce agreement. | §1: "disagreement on any candidate that survives two reconciliation attempts stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4)"; §6 limb A: tolerance zero → §4.5 first disjunct ("the two enumerations disagree after two reconciliation attempts"); disputed candidates listed with the complete candidate and exclusion ledgers. | YES |
| `CENSUS_DENOMINATOR_DISPUTED` (limb ii: input-list disagreement) | Both seats agree on every candidate. For agreed claim 9, seat A's ledger lists H₀ as an input of the paper's stated equation; seat B's does not. `merge` exits 1; the difference survives the one reconciliation against the paper's stated equation. | C3: "if `merge` exits 1, the two seats reconcile their input lists against the paper's stated equation once; an input-set difference surviving that reconciliation stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4), the disputed inputs listed with both seats' quotations" → §4.5 second disjunct. | YES |
| `CENSUS_ORIGIN_DISPUTED` | Corpus of 20 included claims. On the sentence "We take H₀ = 67.4 (see Pinned-Text-C)", seat A files `ORIG_CITATION`→`IMPORTED`, seat B files `ORIG_CHOICE_STATED`→`CHOSEN`; identical splits recur on the inputs of 3 of the 20 claims (15% > 10%). Disagreements are carried, never reconciled. | §3/C3: origins classified independently by both seats; differing records carry `origin_alt`/`origin_evidence_alt` → §4.6: "the two seats' independent `origin` classifications disagree on inputs affecting more than 10% of included claims. The census does not proceed; every disputed input is listed with both seats' classification and both quotations." → filed; sits above `CENSUS_AUDIT_FAILED`/`PARTIAL`/`COMPLETE` in the §4 order. | YES |
| `CENSUS_CONTROL_SPLIT` | C5 harness: seat A's environment prints sympy 1.12 and all three commands exit 0 (PASS, first and second attempt); seat B's `import sympy` exits non-zero on both attempts (FAIL). One control, failed in one seat, passed in the other, after two attempts. | C5 PASS predicate → §4.7: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not adopt the passing seat's result." → §4 order: second, above the dispute classes → filed. | YES |
| §4 filing precedence + stop/NOT_RUN (declared condition) | A run in which two conditions hold at once: a control fails in both seats after two attempts (`R3C2_NO_CLASS` condition) AND one claim was already blocked (`CENSUS_PARTIAL` condition). | §4: "Exactly one study-level outcome is filed. Where more than one condition holds, file the first in this order: `R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`, `CENSUS_COMPLETE`. Once a stop class applies, later limbs are unreached and their controls are `NOT_RUN`." → files `R3C2_NO_CLASS`; the blocked claim's limb unreached; its controls `NOT_RUN`. | YES |

## (C) Reachability, stated per verdict

§3: `REPRO_EXACT` reachable; `REPRO_FAILED` reachable; `REPRO_BLOCKED` reachable (both limbs);
`REPRO_NOT_EVALUABLE` reachable (both print conditions); `REPRO_NO_DERIVATION_STATED` reachable;
`REPRO_INPUT_ABSENT` reachable.
§4: `CENSUS_COMPLETE` reachable (with the fragility stated below); `CENSUS_PARTIAL` reachable;
`CENSUS_AUDIT_FAILED` reachable (all three routes); `R3C2_NO_CLASS` reachable (both limbs);
`CENSUS_DENOMINATOR_DISPUTED` reachable (both limbs); `CENSUS_ORIGIN_DISPUTED` reachable;
`CENSUS_CONTROL_SPLIT` reachable.
No declared outcome, class, limb, or precedence rule of V17 is UNREACHABLE.

## The named suspicion — `CENSUS_COMPLETE` in a real corpus: REACHABLE, and here is the routing both ways

Answer: REACHABLE. `CENSUS_COMPLETE` is not unreachable in principle, but it is reachable only through a clean sweep,
and a single non-arithmetic claim anywhere in the corpus reroutes the study to `CENSUS_PARTIAL`. Shown from the text:

- The producing input exists (row above): a corpus in which every included claim states a recipe and every input is
  `PRINTED` (in the claiming paper or machine-matched in an enumerable pinned text under the `IMPORTED` rule) or
  `STANDARD` from C3's closed table, every attempt finishes inside the 120-second cap with lane machinery, and no stop
  condition fires. Routing: §1 → §2 → §3 arithmetic group for every claim → §4.1 definition → §4 filing order falls
  through to `CENSUS_COMPLETE`.
- The blocking input also exists, and it is small: one included claim with (i) no stated derivation, (ii) one input
  neither printed nor traced to a named source, (iii) one input whose named source is not enumerable or does not
  machine-match at the cited line, or (iv) one attempt that times out or needs unavailable machinery. Routing of that
  claim: §3's own precedence files exactly one of `REPRO_NO_DERIVATION_STATED` / `REPRO_BLOCKED` /
  `REPRO_INPUT_ABSENT` / `REPRO_NOT_EVALUABLE`. That single outcome triggers §4.2: "**at least one included claim
  carries a non-arithmetic outcome** (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`,
  `REPRO_NOT_EVALUABLE`). Report each and why. **INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`.**"
  The §4 filing order then files `CENSUS_PARTIAL` ahead of `CENSUS_COMPLETE`.

So the practical statement is: `CENSUS_COMPLETE` requires zero non-arithmetic outcomes across the entire denominator.
In a real corpus of many papers, any one blocked, absent-input, no-derivation-stated, or not-evaluable claim — one
passage among hundreds — forces `CENSUS_PARTIAL`. The class is reachable as a formal matter (the producing input is
exhibited above, so it is not UNREACHABLE under C0's rule), but its producing set is the all-clean corpus and nothing
narrower; the document itself records this asymmetry in §5's C0 note: "`CENSUS_COMPLETE` requires every included claim
to carry an arithmetic-group outcome, which a single blocked or absent input in the whole corpus is enough to prevent."

## UNREACHABLE verdicts and their blocking clauses

None. Every declared per-claim outcome of §3, every study-level class of §4, and every declared sub-condition and
precedence rule has a concrete exhibited input above. No blocking clause had to be invoked; no clause is quoted under
this heading because no verdict is UNREACHABLE.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V17_KIMI_COMPLETE

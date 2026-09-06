ACCESS_SHA=c232b4ceb32be109e73cfb247ed911a6080f893a787eb28a233ad0a84104deb3
C0_REACHABILITY=PASS

R3C2 — C0 REACHABILITY EXHIBITION (author seat: kimi), 2026-09-06
Target: R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md, read from disk in full (1,125 lines), no other file in the
directory consulted. The computed sha256 equals the ACCESS_SHA above and matches the value the brief pre-printed.

BASIS AND SCOPE NOTES
- Version status of the bytes exhibited: V24g, a LIVING DRAFT (unsigned); V23 is the signed design of record.
  Per §10.18, V24's changes are confined to the C4/C5/C5b scope-and-harness clauses ("No class, control code,
  threshold, precedence, taxonomy or rule of interpretation changes"), so §3 and §4 as exhibited here are identical
  in V23 and V24g.
- §3's definition is settled: option (c), one pass, two tallies, ruled 2026-09-05 14:08 KST (§10.4). There is no
  held clause in the text as it stands; REPRO_AFTER_CHOICE is retired into the script-computed rests_on field.
- Dependence worth having on record (the "marked definition" note): §10.3 records that the HELD marker sat in §3,
  not §1, and that §1's question changed with the §3 ruling (§10.4 traces the §1 row). This exhibition assumes the
  option (c) reading of §1/§3 as settled. It is a function of that ruling: under the retired option (b) wording the
  same exercise returned FAIL (REPRO_AFTER_CHOICE unreachable — §10.2, §10.3, two blind seats agreeing). If the
  ruling were re-opened, this exhibition would have to be re-run. The dependence is stated, not assumed away.
- Role: this is ONE seat's independent exhibition. C0 (§5) requires a second independent seat to verify and both to
  return PASS; the lane owner checks coverage only. This document is the author seat's artefact.
- Arithmetic in the concrete inputs was verified by computation (Decimal, ROUND_HALF_UP), not by hand.

(A) SECTION 3 — PER-CLAIM OUTCOMES (six declared; arithmetic group = exactly REPRO_WITHIN_STATED_PRECISION and
    REPRO_FAILED; per-claim precedence: REPRO_NO_DERIVATION_STATED, REPRO_BLOCKED, REPRO_INPUT_ABSENT,
    REPRO_NOT_EVALUABLE, then the arithmetic group)

verdict | concrete input | clause path | reachable
---|---|---|---
REPRO_WITHIN_STATED_PRECISION | Paper A prints: "From the printed densities we obtain the ratio r = Ω_b h²/Ω_c h² = 0.02237/0.1200 = 0.1864." Both inputs printed in paper A (status PRINTED each; origin irrelevant to admissibility under option (c)). Attempt: 0.02237/0.1200 = 0.1864166…; no precision stated, so the printed precision (4 dp) is the stated precision; rounds half away from zero to 0.1864 = the printed numeral. | §1 inclusion (numeral asserted as the paper's own result) → §2 steps 1–3 (equation extracted; both inputs PRINTED) → §2 step 4 (mechanical attempt consuming every PRINTED/STANDARD record) → §3 REPRO_WITHIN_STATED_PRECISION ("the paper's number follows, within its own stated precision … Where the paper states no precision … must round to the printed numeral at that precision, rounding half away from zero") → §3 precedence: no NO_DERIVATION (recipe stated), no BLOCKED/ABSENT input, evaluable → arithmetic group → file REPRO_WITHIN_STATED_PRECISION; both numbers reported; rests_on computed by the lane script beside it. | yes
REPRO_FAILED | Paper B prints: "With Ω_b h² = 0.02237, Ω_c h² = 0.1200 and h = 0.6736 we find Ω_m = (Ω_b h² + Ω_c h²)/h² = 0.3153." All three inputs PRINTED. Attempt: 0.14237/0.45373696 = 0.3137721… → rounds to 0.3138 at the printed 4-dp precision ≠ 0.3153. Inputs sufficient for the recipe; the arithmetic does not give the paper's number. | §1 → §2 steps 1–4 (all inputs PRINTED; attempt completes) → §3 REPRO_FAILED ("the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number … 'unreproduced from the stated inputs,' not 'error'") → §3 precedence: no earlier terminal condition holds → arithmetic group → file REPRO_FAILED; both numbers reported; rests_on beside it. | yes
REPRO_BLOCKED | Paper C prints: "Using the transfer-function normalisation of Smith (2019), we obtain σ₈ = 0.8111." The normalisation value is not printed anywhere in paper C; Smith (2019) is named but is not an enumerable text pinned in R3C2_CORPUS_MANIFEST.md. (Second limb, same class: the named source IS a pinned enumerable text but the value does not machine-match at the cited line.) | §1 → §2 step 3 (input status BLOCKED: "traced to a named source but carrying no machine-matchable value") → §2 IMPORTED rule ("a cited value that does not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest, files REPRO_BLOCKED under §3") → §2 ("A seat may not supply a value for an ABSENT or BLOCKED input. Encountering one ends that claim's attempt.") → §3 REPRO_BLOCKED → §3 precedence: derivation stated, BLOCKED precedes INPUT_ABSENT → file REPRO_BLOCKED; input and source named; C3 record carries status BLOCKED, origin IMPORTED, ORIG_CITATION to the naming sentence, no value; never consumed. | yes
REPRO_NOT_EVALUABLE | Paper D prints a claim with a fully stated recipe and every input PRINTED, but the recipe requires a symbolic simplification that does not finish under the mandated wrapper: /usr/bin/python3 -E r3c2_timeout.py 120.0 -- <command> prints SYMBOLIC_TIMEOUT and exits 124. (Second limb: the recipe requires machinery this lane does not have — e.g., a numerical Boltzmann solver → MACHINERY_UNAVAILABLE, the point reached printed.) | §1 → §2 steps 1–4 (all inputs PRINTED/STANDARD; attempt launched through the §9 wrapper) → wrapper deadline → §3 REPRO_NOT_EVALUABLE ("the arithmetic could not be completed within the 120-second cap, or requires machinery this lane does not have. Print SYMBOLIC_TIMEOUT … or MACHINERY_UNAVAILABLE … and the point reached") → §3 precedence: no NO_DERIVATION, no BLOCKED, no ABSENT → NOT_EVALUABLE precedes the arithmetic group → file REPRO_NOT_EVALUABLE. (§4's CENSUS_PARTIAL repeat is "meaningful only for REPRO_NOT_EVALUABLE".) | yes
REPRO_NO_DERIVATION_STATED | Paper E prints: "Our analysis yields a goodness-of-fit χ² = 4.7." and nowhere states an equation or computational procedure that produces it — or says only "obtained from our standard pipeline" (a procedure named but not specified). | §1 inclusion (printed numeral asserted as the paper's own result — §3's own note: a claim can satisfy §1 while the paper never says how the number was obtained) → §2 step 1 finds no equation to extract → §3 REPRO_NO_DERIVATION_STATED ("states no equation or computational procedure that could produce it, so there is nothing to attempt … A procedure named but not specified … states no computational procedure that could produce it; file this class and name the passage") → §3 precedence: first in order → file REPRO_NO_DERIVATION_STATED; passage named. | yes
REPRO_INPUT_ABSENT | Paper F prints: "The crossing time is t = R/v = 1.8 Gyr, with R = 2 Mpc." v is never printed anywhere in paper F and no source is named for it. | §1 → §2 steps 1–3 (R PRINTED; v ABSENT — "neither printed nor traced to any named source") → §2 ("A seat may not supply a value for an ABSENT … input. Encountering one ends that claim's attempt.") → §3 REPRO_INPUT_ABSENT ("an input the equation needs is ABSENT from the paper — neither printed nor traced to any named source — so the attempt stops there. Name the input.") → §3 precedence: derivation stated; no named source, so not BLOCKED; ABSENT third → file REPRO_INPUT_ABSENT; input named. §3's contrast sentence confirms the boundary: a claim whose inputs the paper DOES state, chosen or not, is attempted and files WITHIN or FAILED. | yes

(B) SECTION 4 — STUDY-LEVEL CLASSES (eight declared; filing precedence: R3C2_NO_CLASS, CENSUS_CONTROL_SPLIT,
    CENSUS_DENOMINATOR_DISPUTED, CENSUS_OUTCOME_DISPUTED, CENSUS_ORIGIN_DISPUTED, CENSUS_AUDIT_FAILED,
    CENSUS_PARTIAL, CENSUS_COMPLETE; "Once a stop class applies, later limbs are unreached and their controls are
    NOT_RUN.")

verdict | concrete input | clause path | reachable
---|---|---|---
R3C2_NO_CLASS | Pre-dispatch limb: the packet builder r3c2_build_seat_packet.py finds a forbidden-list string surviving in the built packet — "the packet is not written and C4_PACKET_REDACTED=FAIL"; no seat is ever dispatched. In-run limb: C5's harness FAILs in every seat that attempted it after two attempts (the live MANIFEST_SHA256 mismatches the dispatch record on both seats). | §5 C4 builder assertion ("If any survives, the packet is not written and C4_PACKET_REDACTED=FAIL") → §4 class 4 ("a control among C0 through C5b fails in every seat that attempted it after two attempts; a packet or seat-isolation failure before dispatch files this class") → §4 precedence: first → file R3C2_NO_CLASS. Boundary respected: it is not a C6 audit failure or a seal-receipt failure (those file CENSUS_AUDIT_FAILED). | yes
CENSUS_CONTROL_SPLIT | Seats A and B dispatched. On C3's validate run, seat A's ledger exits 0 and seat B's exits 1 (seat B's ledger carries a field outside the schema, which validate fails); the split persists after two attempts. | §5 C3 (the printed validate run's exit status is the control's) → §4 class 8 ("a control fails in one seat and passes in another after two attempts … do not adopt the passing seat's result") → §4 precedence: R3C2_NO_CLASS does not apply (one seat passed) → file CENSUS_CONTROL_SPLIT; both seats' outputs reported; stop. | yes
CENSUS_DENOMINATOR_DISPUTED | Enumeration limb: seat A includes candidate "13.8 Gyr" at paper G line 412 as the paper's own result; seat B excludes it as ATTRIBUTED_NOT_DERIVED; two reconciliation attempts do not resolve it. Input-list limb: enumerations agree, but the two seats' input lists for an agreed claim differ; r3c2_lane_tools.py merge exits 1 and the difference survives the one C3 reconciliation. | §1 (inclusion assigned independently by both seats; disagreement surviving two reconciliation attempts stops the study under CENSUS_DENOMINATOR_DISPUTED) / §6 limb A (tolerance zero, measured in candidate passages) / C3 lane-side merge exit-1 rule → §4 class 5 ("the two enumerations disagree after two reconciliation attempts, or the two seats' input lists for the agreed claims disagree after the one C3 reconciliation") → file CENSUS_DENOMINATOR_DISPUTED; disputed candidates or inputs listed; the census does not proceed. | yes
CENSUS_OUTCOME_DISPUTED | Both seats include claim "t_H = 13.85 Gyr" with a stated recipe and printed inputs. Seat A computes 13.851 → 13.85 at the printed 2-dp precision → files REPRO_WITHIN_STATED_PRECISION; seat B, reading the recipe as naming a different printed input, computes 13.844 → 13.84 → files REPRO_FAILED. The one reconciliation against the printed numeral and the stated-precision rule of §3 does not resolve the split. | §2 step 5 ("a disagreement surviving that reconciliation files CENSUS_OUTCOME_DISPUTED (§4)") → §4 class 6 ("the two seats' filed per-claim outcomes on an agreed included claim differ after one reconciliation against the printed numeral and the stated-precision rule of §3") → file CENSUS_OUTCOME_DISPUTED; the claim listed with both seats' outcomes, both number pairs, and the step each seat reached; the census does not proceed. | yes
CENSUS_ORIGIN_DISPUTED | 20 included claims. In 3 of them (15% > 10%), an input sentence "We take τ = 0.0544 for the reionisation optical depth" is classified ORIG_CONSTANT→STANDARD by seat A (verbatim machine-match to the closed-list value printed in the paper) and ORIG_SILENT→UNDECLARED by seat B, whose printed origin_search documents an adequate search with no match. Disagreements are carried (origin_alt), never reconciled. | C3 ("Every input's origin is classified independently by both seats"; reason-code precedence governs co-applicable codes within one seat, not across seats) → C3 lane-side merge (origin_alt / origin_evidence_alt) → C6 ("Disagreement about provenance is reported, never reconciled") → §4 class 7 ("disagree on inputs affecting more than 10% of included claims"): 3/20 = 15% → file CENSUS_ORIGIN_DISPUTED; every disputed input listed with both classifications and both quotations; the census does not proceed. | yes
CENSUS_AUDIT_FAILED | Limb (i): the C6 auditor, without sight of earlier work, re-derives sampled claim 12 and records MISMATCH against the sealed outcome (sealed WITHIN; the auditor's re-computation fails the stated-precision test). Limb (ii): the external custodian's seed is never supplied with receipt T — "the audit does not run, C6_AUDIT_SAMPLE=NOT_RUN, and the study files CENSUS_AUDIT_FAILED with the missing seed named." Limb (iii): Blanc's post-opening re-hash of the tally or the protocol mismatches a receipted value (§7: "Any missing receipt or mismatch files CENSUS_AUDIT_FAILED"). | §5 C6 (audit artefact C6_AUDIT.json; PASS only with no MISMATCH and no incompleteness) / §7 (two-receipt seal; verification of all four values) → §4 class 3 ("the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the cause named), or the receipt verification of the seal fails. No tally is filed; report which.") → §4 precedence: the earlier dispute classes do not hold (seats agree everywhere; origin disputes ≤ 10%) → file CENSUS_AUDIT_FAILED. | yes
CENSUS_PARTIAL | 40 included claims. Claim 17 cites an input from a source outside the manifest → REPRO_BLOCKED; the other 39 file arithmetic-group outcomes; the two seats agree on enumeration, inputs, outcomes and origins; the C6 audit runs to PASS. Zero-denominator limb: enumeration yields zero included claims. | §2 attempts (one repeat permitted, meaningful only for REPRO_NOT_EVALUABLE) → §4 class 2 ("at least one included claim carries a non-arithmetic outcome (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT, REPRO_BLOCKED, REPRO_NOT_EVALUABLE), or the denominator is zero … INCONCLUSIVE, and it takes precedence over CENSUS_COMPLETE") → §4 precedence: PARTIAL immediately before COMPLETE → file CENSUS_PARTIAL; each non-arithmetic claim reported and why (or the empty enumeration named). | yes
CENSUS_COMPLETE | A corpus of 12 included claims across 4 papers in which every claim states its recipe and every recipe input is PRINTED (in the claiming paper, or machine-matched in a pinned enumerable text under the IMPORTED rule) or STANDARD on the closed list; every attempt completes within 120 s; 9 claims file REPRO_WITHIN_STATED_PRECISION and 3 file REPRO_FAILED (both arithmetic-group); the two seats' enumerations, input lists and outcomes agree; origin disputes affect zero claims (≤ 10%); the C6 audit runs to PASS (C6_AUDIT.json exists, is printed, carries no MISMATCH and no incompleteness); receipts P and T both verify. | §3 (arithmetic group = "exactly REPRO_WITHIN_STATED_PRECISION and REPRO_FAILED") → §4 class 1 ("every included claim carries exactly one outcome from the arithmetic group of §3, with C6_AUDIT_SAMPLE=PASS. A denominator of zero files CENSUS_PARTIAL with the empty enumeration named; no census is complete over nothing.") → §4 precedence: no earlier limb's condition holds → file CENSUS_COMPLETE; the full tally reported with its denominator and the rests_on tally beside it — two tallies from one pass. | yes

(C) REACHABILITY, STATED EXPLICITLY
Every per-claim outcome of §3 is reachable: REPRO_WITHIN_STATED_PRECISION yes; REPRO_FAILED yes; REPRO_BLOCKED
yes; REPRO_NOT_EVALUABLE yes; REPRO_NO_DERIVATION_STATED yes; REPRO_INPUT_ABSENT yes. The §3 precedence partitions
cleanly: each class has a non-empty exclusive domain (no recipe stated / recipe stated with an unobtainable named
source / recipe stated with an untraced input / all inputs consumable but the computation cannot complete / all
inputs consumable and the computation completes, pass or fail).
Every study-level class of §4 is reachable: R3C2_NO_CLASS yes; CENSUS_CONTROL_SPLIT yes;
CENSUS_DENOMINATOR_DISPUTED yes; CENSUS_OUTCOME_DISPUTED yes; CENSUS_ORIGIN_DISPUTED yes; CENSUS_AUDIT_FAILED yes;
CENSUS_PARTIAL yes; CENSUS_COMPLETE yes. Each class's exclusive domain is non-empty under the §4 filing order
(e.g., CONTROL_SPLIT vs NO_CLASS is decided by "one seat passed"; AUDIT_FAILED's boundary against NO_CLASS is stated
in class 4 itself; COMPLETE is the residue limb and is exhibited above).

THE SUSPICION, ANSWERED DIRECTLY — CENSUS_COMPLETE
Question put: does a single blocked, absent-input, or no-derivation-stated claim anywhere in the corpus force
CENSUS_PARTIAL, making CENSUS_COMPLETE unreachable in practice?

Answer: REACHABLE. And the routing, stated exactly:

1. Yes, one such claim defeats CENSUS_COMPLETE for that run — the text says so in three places that agree:
   - CENSUS_PARTIAL (§4 class 2): "at least one included claim carries a non-arithmetic outcome
     (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT, REPRO_BLOCKED, REPRO_NOT_EVALUABLE), or the denominator is
     zero … INCONCLUSIVE, and it takes precedence over CENSUS_COMPLETE."
   - CENSUS_COMPLETE (§4 class 1): "every included claim carries exactly one outcome from the arithmetic group of
     §3, with C6_AUDIT_SAMPLE=PASS."
   - §4 filing order: "…CENSUS_AUDIT_FAILED, CENSUS_PARTIAL, CENSUS_COMPLETE" — PARTIAL sits ahead of COMPLETE, so
     a tally satisfying both conditions files PARTIAL and COMPLETE's limb is unreached.
   The suspicion's list is also incomplete: REPRO_NOT_EVALUABLE, any of the six earlier stop classes (control
   failure, control split, denominator/outcome/origin disputes, audit or seal failure), and a zero denominator each
   independently defeat CENSUS_COMPLETE. Its filing condition is conjunctive and single-claim-fragile.
2. But C0's test is not "likely on a real corpus" — it is "does an input exist that produces the verdict" (§5 C0:
   "exhibit a concrete input that produces it … An outcome for which no such input can be exhibited is
   UNREACHABLE"). Such an input exists and is exhibited in row (B) CENSUS_COMPLETE above: a corpus in which every
   included claim states its recipe, every recipe input is PRINTED or STANDARD, every computation completes within
   the cap, the seats agree everywhere, and the audit passes. Nothing in the text forbids that corpus; the class's
   domain is non-empty.
3. What does NOT defeat CENSUS_COMPLETE is failure to reproduce: REPRO_FAILED is arithmetic-group (§3: "exactly
   REPRO_WITHIN_STATED_PRECISION and REPRO_FAILED"), so a corpus full of unreproduced numbers can still file
   CENSUS_COMPLETE. What defeats it is missing derivations, absent or unobtainable inputs, non-evaluability,
   disputes, audit or seal failure, or an empty denominator.
4. The document itself records this exact fragility as the reason C0 exists (§5 C0 note: "CENSUS_COMPLETE requires
   every included claim to carry an arithmetic-group outcome, which a single blocked or absent input in the whole
   corpus is enough to prevent"), and asks only whether the verdict CAN happen at all. It can. Whether the pinned
   corpus (89 enumerable texts, §10.5) in fact contains any non-arithmetic claim is the empirical question the
   census exists to answer; C0 does not prejudge it. Reachable in principle, fragile by design — that is the
   routing, stated rather than implied away.

UNREACHABLE VERDICTS, WITH BLOCKING CLAUSES QUOTED VERBATIM
None. Every declared per-claim outcome of §3 and every study-level class of §4 is exhibited above with a concrete
input and a clause path; there is no verdict for which a blocking clause must be quoted.

COVERAGE OF OTHER DECLARED CONDITIONS (C0 asks for "every declared condition"; these are not filed verdicts)
- REPRO_AFTER_CHOICE: RETIRED at V10 by the principal's ruling (§3 note; §10.4). Not a declared outcome of the
  current text; no exhibition owed. Its content is the script-computed rests_on field.
- rests_on values (DERIVED_ONLY; the severity order USES_UNDECLARED > USES_IMPORTED > USES_FITTED > USES_CHOSEN;
  DISPUTED pairs; the NOT_COMPUTED row): a script-computed ledger field, not a per-claim outcome (§3 master-only
  note; §3: "rests_on is computed and reported for every included claim that has at least one ledger record,
  whatever its outcome; a claim with no ledger record carries rests_on NOT_COMPUTED"). Reachable by computation on
  any merged ledger: e.g., the REPRO_NO_DERIVATION_STATED claim in row (A) has no ledger record → NOT_COMPUTED; a
  claim whose root contains an origin-disputed input → the DISPUTED pair.
- Exclusion-ledger kinds (EQUATION_NUMBER, REFERENCE_NUMBER, PAGE_OR_LINE_NUMBER, DATE, ATTRIBUTED_NOT_DERIVED):
  §3 states candidate exclusions are NOT per-claim outcomes. Each kind is trivially exhibitable: a numeral that is
  an equation number "(14)", a reference marker "[23]", a page or line number, a date "2018", or a value the paper
  attributes to another work without deriving.
- SYMBOLIC_TIMEOUT / MACHINERY_UNAVAILABLE: sub-tokens of REPRO_NOT_EVALUABLE, both exhibited in its row above.
- Zero denominator: exhibited as the second limb of CENSUS_PARTIAL; it cannot file CENSUS_COMPLETE ("no census is
  complete over nothing").

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V24G_KIMI_COMPLETE

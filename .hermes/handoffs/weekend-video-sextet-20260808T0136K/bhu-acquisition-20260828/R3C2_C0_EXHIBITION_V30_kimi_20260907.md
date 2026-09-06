ACCESS_SHA=57de1252d5f9d4592181517e70d0bca1c715830ccbb595f4bc9622a18e4779fd
C0_REACHABILITY=PASS

# R3C2 — C0 REACHABILITY EXHIBITION, V30 (kimi seat, 2026-09-07)

Document exhibited: R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md, read from disk in full (1,309 lines), sha256 above.
Basis: the text as it stands at V30 (living draft). §10 is history and binds nothing. §3 is the settled option-(c) wording:
one pass, two tallies; `REPRO_AFTER_CHOICE` is RETIRED into the script-computed `rests_on` field and is not a declared
outcome, so no row is owed for it; the arithmetic group is exactly `REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED`
(§3: "**The arithmetic group** is the set of outcomes that state whether the arithmetic reproduced the number: **exactly
`REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED`**."). There is no held clause.
This exhibition asks only whether each declared verdict CAN OCCUR. It does not gate the design and does not judge its
physics. Each exhibited input is a concrete constructed claim, as C0 requires: "a specific claim, its inputs, and the
path it takes through this document to that verdict."

## MASTER TABLE

verdict | concrete input | clause path | reachable
---|---|---|---
REPRO_WITHIN_STATED_PRECISION | E1: "age = 13.8 Gyr" from printed H0 = 71; E2: "H0 = 67.4 ± 0.5", reproduced 67.7 | §1 → §2 steps 1–4 → §3 rounding / |rep − print| ≤ uncertainty → §2 step 5 | yes
REPRO_FAILED | F1: "σ8 = 0.85" (2 dp), stated recipe, printed inputs, reproduction gives 0.80 | §1 → §2 steps 1–4 → §3 REPRO_FAILED | yes
REPRO_BLOCKED | B1: "w = −1.03"; input M_B named to Ref. [37], not enumerable in the manifest (limb 1); or pinned but no machine-match at the cited line (limb 2) | §1 → §2 import rule → status BLOCKED → §2 "Encountering one ends that claim's attempt" → §3 REPRO_BLOCKED | yes
REPRO_NOT_EVALUABLE | N1: integral exceeds the 120.0 s wrapper cap (SYMBOLIC_TIMEOUT); N2: recipe needs an Einstein–Boltzmann solver (MACHINERY_UNAVAILABLE) | §1 → §2 step 4 under r3c2_timeout.py / §3 class definition → REPRO_NOT_EVALUABLE | yes
REPRO_NO_DERIVATION_STATED | D1: "fσ8 = 0.47" printed as own result, no equation or specified procedure | §1 → §3 class definition (first in §3 precedence) | yes
REPRO_INPUT_ABSENT | A1: "Ω_K = 0.001"; needed input R neither printed nor traced to any named source | §1 → §2 step 3 ABSENT → §2 supply bar → §3 REPRO_INPUT_ABSENT | yes
CENSUS_COMPLETE | corpus {E1, F1}; all controls pass identically in both seats; C6_AUDIT_SAMPLE=PASS; receipts P and T verify | §2 → §3 arithmetic group on every claim → §4.1; no earlier class's condition holds; §4.2's condition fails | yes
CENSUS_PARTIAL | (a) corpus {E1, B1} — one non-arithmetic outcome; (b) zero denominator | §4.2 (both limbs named in the definition) | yes
CENSUS_AUDIT_FAILED | eleven paths exhibited below (C6 omission ×2, dispute >10%, seedless, zero-denominator-with-passages, incomplete reconstruction, fabricated off-sample evidence quotation, duplicated input id, mis-keyed record, hybrid branch, receipt failure) | §4.3; §6 C6 PASS predicate; §7 | yes
R3C2_NO_CLASS | C2 validate exits 1 on two attempts in every seat; or C4_PACKET_REDACTED=FAIL before dispatch | §4.4 (both limbs) | yes
CENSUS_DENOMINATOR_DISPUTED | (a) inclusion disagreement surviving two reconciliations; (b) input-list difference surviving the one C3 reconciliation (merge exit 1) | §1, §4.5, §6, C3 merge clause | yes
CENSUS_OUTCOME_DISPUTED | agreed claim E1; seat A files REPRO_WITHIN_STATED_PRECISION (13.77 → 13.8), seat B files REPRO_FAILED (13.74 → 13.7), surviving one reconciliation | §2 step 5, §4.6 | yes
CENSUS_ORIGIN_DISPUTED | origin disagreement on inputs of 2 of 10 included claims (20% > 10%) | C3 two-seat origin rule, §4.7, C6 | yes
CENSUS_CONTROL_SPLIT | C3 validate fails twice in seat A, passes in seat B | §4.8; C1B contract | yes

Auxiliary states the brief names (not §3 outcomes / §4 classes, exhibited for completeness):
rests_on NOT_COMPUTED | claim D1 has no ledger record | §3 master-only rule; §9 compute clause | yes (reachable state)
rests_on DISPUTED (cross-claim) | claim X's dependency graph reaches a disputed record in claim Y | §3 master-only note | yes (reachable state)

## A. PER-CLAIM OUTCOMES (§3) — ALL SIX REACHABLE

### A1. REPRO_WITHIN_STATED_PRECISION — REACHABLE
Concrete input E1: paper P prints "the age of the Universe is 13.8 Gyr" as a result of its own, stating the recipe
age = 1/H0 and the input H0 = 71 km s⁻¹ Mpc⁻¹ printed in the paper (status `PRINTED`, origin `CHOSEN` on an
`ORIG_CHOICE_STATED` quotation "we take H0 = 71"). Mechanical attempt: 1/H0 with the unit factor gives ≈ 13.77 Gyr.
Clause path: §1 inclusion (a printed numeral asserted as the paper's own result, no excluded kind) → §2 step 1 extract
→ step 2 list inputs → step 3 classify (`PRINTED`) → step 4 "Attempt the arithmetic MECHANICALLY — follow the paper's
own recipe, using every value it directs you to use, i.e. every ledger record with status `PRINTED` or `STANDARD`" →
§3: "Where the paper states no precision for the claim, the printed precision is the claim's stated precision: the
reproduced value must round to the printed numeral at that precision, rounding half away from zero." 13.77 rounds to
13.8 at the printed tenths precision → outcome filed in the candidate file's `outcome` field (§2 step 5); "Report both
numbers" (13.8 printed, 13.77 reproduced); `rests_on` computed from the ledger (`USES_CHOSEN`, reported beside it).
Uncertainty limb, E2: paper prints "H0 = 67.4 ± 0.5" as its own result from a stated fit over printed inputs;
reproduction gives 67.7; §3: "the test is |reproduced − printed| ≤ the stated uncertainty, taken once — not doubled,
not rounded"; |67.7 − 67.4| = 0.3 ≤ 0.5 → same class. Asymmetric case routed by "the stated uncertainty is the
half-width on the side the reproduced value falls."
No earlier terminal condition holds (a derivation is stated, every input is `PRINTED`/`STANDARD`, the attempt completes).

### A2. REPRO_FAILED — REACHABLE
Concrete input F1: paper prints "σ8 = 0.85" (two decimal places) as its own result, states the equation, and every
input the equation needs is `PRINTED` or `STANDARD`. The mechanical attempt completes within the cap and gives 0.80.
Clause path: §1 → §2 steps 1–4 → §3: "`REPRO_FAILED` — the inputs the paper states are sufficient for its recipe, but
the arithmetic does not give the paper's number. Report both numbers. **Wording: "unreproduced from the stated
inputs," not "error."**" 0.80 ≠ 0.85 at the printed precision, no stated uncertainty → REPRO_FAILED, both numbers
reported, `rests_on` beside it. Distinct-routing rule honoured: "a claim whose inputs the paper DOES state, chosen or
not — that claim is attempted and files `REPRO_WITHIN_STATED_PRECISION` or `REPRO_FAILED`."

### A3. REPRO_BLOCKED — REACHABLE (both limbs)
Concrete input B1: paper prints "w = −1.03" as its own result; the stated equation needs the absolute-magnitude
calibration M_B, which the paper does not print but traces: "using the calibration of Ref. [37]".
Limb 1: Ref. [37] "is not an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`" → §2: "If the named source is not
enumerable or the value does not match there, file `REPRO_BLOCKED` under §3"; the record is status `BLOCKED`, origin
`IMPORTED`, `ORIG_CITATION` evidence quoted at the claiming paper's naming sentence, no value (C3); §2: "A seat may not
supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt." → REPRO_BLOCKED; the
input and the source are named. "in the first case whether that source is obtainable elsewhere is irrelevant, because
the census may not open or consume it."
Limb 2: same input, but the named source IS an enumerable pinned text whose cited line carries the symbol with a
different numeral — "an enumerable pinned text at whose cited line the value does not machine-match" → REPRO_BLOCKED.
§3 precedence puts `REPRO_BLOCKED` before `REPRO_INPUT_ABSENT`; the named-source test keeps the two domains disjoint
("Distinct from `REPRO_INPUT_ABSENT`, which is an input the paper neither prints nor traces to any named source").

### A4. REPRO_NOT_EVALUABLE — REACHABLE (both limbs)
Limb SYMBOLIC_TIMEOUT, concrete input N1: paper prints "χ² = 312.7" as its own result from a stated multidimensional
integral over printed inputs; every input is `PRINTED`/`STANDARD`; the attempt runs under
"/usr/bin/python3 -E r3c2_timeout.py 120.0 -- <command>", which "enforces a 120.0-second wall-clock deadline on the
monotonic clock … on the deadline prints `SYMBOLIC_TIMEOUT` and exits 124 — the reportable outcome" (§9) →
REPRO_NOT_EVALUABLE, "`SYMBOLIC_TIMEOUT` … and the point reached" printed. The one repeat §4.2 permits ("meaningful
only for `REPRO_NOT_EVALUABLE`") also times out; the class stands.
Limb MACHINERY_UNAVAILABLE, concrete input N2: paper prints a CMB band-power value as its own result whose stated
recipe requires an Einstein–Boltzmann solver this lane does not have → "`MACHINERY_UNAVAILABLE` when the lane lacks the
machinery, and the point reached." Precedence: both limbs sit after `REPRO_INPUT_ABSENT` and before the arithmetic
group, and here no earlier condition holds (derivation stated, inputs printed).

### A5. REPRO_NO_DERIVATION_STATED — REACHABLE
Concrete input D1: paper prints "fσ8(z = 0.6) = 0.47" as its own result and states no equation or computational
procedure that could produce it — or writes only "obtained with our standard pipeline". §3: "A procedure named but not
specified — a sentence that says where the number came from without stating operations a seat could attempt — states
no computational procedure that could produce it; file this class and name the passage." Clause path: §1 inclusion
(the numeral is asserted as the paper's own result) → §2 step 1 finds no equation to extract → §3 class definition;
first in the §3 precedence order, so it files ahead of any co-occurring condition. The claim carries no ledger records,
so its `rests_on` is `NOT_COMPUTED` (exhibit R1 below).

### A6. REPRO_INPUT_ABSENT — REACHABLE
Concrete input A1: paper prints "Ω_K = 0.001" as its own result from a stated equation that needs the CMB shift
parameter R; R is "neither printed nor traced to any named source". Clause path: §1 → §2 step 3 classify `ABSENT` →
§2 "A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt." →
§3: "`REPRO_INPUT_ABSENT` — an input the equation needs is `ABSENT` from the paper … so the attempt stops there. **Name
the input.**" §3 precedence routes it after `REPRO_BLOCKED`; here no source is named, so the BLOCKED limb cannot apply
and the ABSENT class is the first applicable one. The class exists precisely to give the supply bar an outcome to file
into.

§3 precedence totality check: "Exactly one outcome is filed per claim. Where more than one terminal condition holds,
file the first in this order: `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`, `REPRO_NOT_EVALUABLE`,
then the arithmetic group." Every class above is first-applicable on its exhibited input; none needs a clause the text
does not contain.

## B. STUDY-LEVEL CLASSES (§4) — ALL EIGHT REACHABLE

§4 precedence, quoted because every routing below is checked against it: "**Exactly one study-level outcome is filed.
Where more than one condition holds, file the first in this order:** `R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`,
`CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_OUTCOME_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`,
`CENSUS_PARTIAL`, `CENSUS_COMPLETE`. **Once a stop class applies, later limbs are unreached and their controls are
`NOT_RUN`.**"

### B1. CENSUS_COMPLETE — REACHABLE (see also §D, the suspicion, answered directly)
Concrete input: the corpus is exactly claims E1 and F1 (§A1, §A2). Both seats enumerate the same two included
candidates; every control C0–C5b passes in every seat that attempted it (no attempt needed twice); both seats' input
lists and origins agree; both file the same outcomes — E1 `REPRO_WITHIN_STATED_PRECISION`, F1 `REPRO_FAILED` — so no
disagreement survives anything; the audit (§6 C6) runs to `C6_AUDIT_SAMPLE=PASS` (seed supplied and recorded with
receipt T, stage-1 and stage-2 seals match, the recomputed selection matches, the auditor's reconstruction of both
claims MATCHes field-for-field, no omission row, dispute count 0 ≤ 10%, no MISMATCH, `C6_AUDIT.json` exists and is
printed); receipts P and T are both present and Blanc's re-hash verifies all four values.
Clause path: §2 attempts → §3 arithmetic-group outcome on every included claim → §4.1: "**every included claim carries
exactly one outcome from the arithmetic group of §3, with `C6_AUDIT_SAMPLE=PASS`**" — condition holds; denominator 2 > 0
so the zero-denominator clause does not fire; §4.2's condition ("at least one included claim carries a non-arithmetic
outcome …, or the denominator is zero") fails; no earlier class's condition holds → file CENSUS_COMPLETE; "Report the
full tally with its denominator, and the `rests_on` tally beside it — two tallies from one pass."
Note the routing that keeps this class occupiable: `REPRO_FAILED` is inside the arithmetic group, so a genuinely
unreproduced paper does NOT by itself block CENSUS_COMPLETE — completeness quantifies over outcome type, not over
whether the papers' arithmetic worked.

### B2. CENSUS_PARTIAL — REACHABLE (two limbs)
Limb (a), concrete input: the corpus is {E1, B1} (§A1, §A3). After the §2 attempt (B1 repeated once, pointlessly but
permitted), B1 carries the non-arithmetic outcome `REPRO_BLOCKED`. §4.2: "**at least one included claim carries a
non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`),
or the denominator is zero**. Report each and why. **INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`.**"
→ CENSUS_PARTIAL, B1 reported and why.
Limb (b), concrete input: both seats enumerate zero included candidates — every candidate passage lands in the
exclusion ledger under one of the six kinds. §4.1's own clause: "A denominator of zero files `CENSUS_PARTIAL` with the
empty enumeration named; no census is complete over nothing"; §4.2 names the same limb. Routing note: §4 precedence
places `CENSUS_AUDIT_FAILED` earlier, but its condition does not hold here — with no passage on either side there is no
omission row, no dispute, and C6's zero-denominator failure clause ("with any passage on either side") is not
triggered; the first class in the order whose condition holds is CENSUS_PARTIAL.

### B3. CENSUS_AUDIT_FAILED — REACHABLE (eleven paths, §C)
§4.3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause
(the cause named), **or the receipt verification of the seal fails**. No tally is filed; report which." Eleven concrete
inputs are exhibited in §C. Each is first-applicable in the §4 order on its input (no control failure, no split, no
dispute condition holds in the exhibited cases).

### B4. R3C2_NO_CLASS — REACHABLE (two limbs)
Limb (a), concrete input: both census seats' C2 `validate` runs exit 1 on the first and second attempt (each joined
ledger carries a field outside the C3 schema; "the seat-authored ledger carries only the schema fields; `validate`
fails a ledger that carries any other field"). §4.4: "a control among C0 through C5b fails **in every seat that
attempted it** after two attempts" → R3C2_NO_CLASS; first in the §4 order; "later limbs are unreached and their
controls are `NOT_RUN`."
Limb (b), concrete input: the packet builder's forbidden-list assertion finds a surviving forbidden string → "the
packet is not written and `C4_PACKET_REDACTED=FAIL`" → §4.4: "a packet or seat-isolation failure before dispatch files
this class."
Bounding rule honoured: "A C6 audit failure or a seal-receipt failure files `CENSUS_AUDIT_FAILED`, not this class."

### B5. CENSUS_DENOMINATOR_DISPUTED — REACHABLE (two limbs)
Limb (a), concrete input: seat A includes a passage printing "0.96" as the paper's own result; seat B excludes it as
`ATTRIBUTED_NOT_DERIVED`; two reconciliation attempts fail to resolve it. §1: "disagreement on any candidate that
survives two reconciliation attempts stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4): the disputed candidates
are listed and the complete candidate and exclusion ledgers are reported with the dispute"; §6 limb A: "tolerance zero,
measured in candidate passages"; §4.5 first limb. → CENSUS_DENOMINATOR_DISPUTED.
Limb (b), concrete input: on an agreed claim, seat A's input list for the stated equation is {H0, Ω_m} and seat B's is
{H0}. C3: "`merge` exits 1 if the two `input_id` sets differ — **if `merge` exits 1, the two seats reconcile their
input lists against the paper's stated equation once; an input-set difference surviving that reconciliation stops the
study under `CENSUS_DENOMINATOR_DISPUTED` (§4), the disputed inputs listed with both seats' quotations**"; §4.5 second
limb: "or the two seats' input lists for the agreed claims disagree after the one C3 reconciliation."

### B6. CENSUS_OUTCOME_DISPUTED — REACHABLE
Concrete input: agreed included claim E1 (§A1). Seat A reproduces 13.77 → rounds to 13.8 → files
`REPRO_WITHIN_STATED_PRECISION`; seat B reproduces 13.74 → rounds to 13.7 ≠ 13.8 → files `REPRO_FAILED`. The one
reconciliation against the printed numeral and the stated-precision rule of §3 does not resolve the difference.
Clause path: §2 step 5 ("a disagreement surviving that reconciliation files `CENSUS_OUTCOME_DISPUTED` (§4)") → §4.6:
"the claim is listed with both seats' outcomes, both number pairs, and the step each seat reached."

### B7. CENSUS_ORIGIN_DISPUTED — REACHABLE
Concrete input: 10 included claims; on inputs belonging to 2 of them, seat A files origin `CHOSEN`
(`ORIG_CHOICE_STATED`, quotation q_A) and seat B files `IMPORTED` (`ORIG_CITATION`, quotation q_B) for the same input
ids — disagreement affects 20% of included claims. Clause path: C3 "**Every input's `origin` is classified
independently by both seats.**" → C6: "An input on which the two classifications disagree is filed `ORIGIN_DISPUTED`
and reported with both seats' classification and both quotations; it is **not** reconciled. Above 10% of included
claims, `CENSUS_ORIGIN_DISPUTED`." → §4.7: "every disputed input is listed with both seats' classification and both
quotations." Boundary stated: at or below 10% the census continues, each disputed claim's `rests_on` "computed under
both classifications, printed as a pair and marked `DISPUTED`; the `rests_on` tally reports a `DISPUTED` row."

### B8. CENSUS_CONTROL_SPLIT — REACHABLE
Concrete input: seat A's C3 `validate` run exits 1 on both attempts (a `PRINTED` value in A's ledger fails its
numeric-token machine-match at its cited line); seat B's exits 0. §4.8: "a control fails in one seat and passes in
another after two attempts. Report both seats' outputs and stop; **do not adopt the passing seat's result.**" Also
reachable through the C1B contract ("a surviving fail/pass split files `CENSUS_CONTROL_SPLIT`") and through
`C5C_NO_FALLBACK` under the same rule (§9). Second in the §4 order.

## C. CENSUS_AUDIT_FAILED — EVERY C6 PATH EXHIBITED, PLUS THE V30 IDENTITY/BRANCH PATHS

All eleven inputs below terminate in §4.3 ("the audit of §6 … does not run to PASS for any cause (the cause named) …
No tally is filed; report which") via the C6 PASS predicate: "`C6_AUDIT_SAMPLE=PASS` only if the artefact exists and is
printed, both seals match, the recomputed selection matches, no row is an omission, the dispute rate is at or below
10%, and no audited claim or origin is `MISMATCH`."

C1. Sealed-included absent from the auditor. Concrete input: the sealed candidate file lists E1 as INCLUDED; the
auditor's own complete enumeration of all 89 enumerable texts does not list E1's passage. C6: "**Omissions:** a sealed
INCLUDED passage absent from the auditor's enumeration … each is ledger incompleteness and files `CENSUS_AUDIT_FAILED`."
The completeness row for passage key (file, line, numeral) = E1 is `OMISSION`; "no row is an omission" fails.

C2. Auditor-listed absent from the sealed ledgers. Concrete input: the auditor enumerates a passage printing
"Γ = 1.9" (as included or as excluded); the sealed candidate and exclusion ledgers contain no row for that passage key.
C6: "a passage the auditor lists (included OR excluded) that the sealed ledgers omit — each is ledger incompleteness
and files `CENSUS_AUDIT_FAILED`." → OMISSION row → CENSUS_AUDIT_FAILED.

C3. Dispute rate above 10%. Concrete input: sealed included denominator 10; two passage keys are
`AUDIT_INCLUSION_DISPUTED` — both sides list them but dispose differently (one included vs excluded, one excluded vs
included), or sealed-EXCLUDED passages absent from the auditor. 2/10 = 20% > 10%. C6: "above 10% of the sealed included
denominator the audit files `CENSUS_AUDIT_FAILED`; at or below it the count is reported." Boundary stated: exactly 1
disputed passage of 10 (10%) is reported, not filed.

C4. Seedless selection. Concrete input: after receipt T, the external custodian supplies no seed (or supplies one not
recorded with the receipt). C6: "**If the seed is not supplied and recorded with the receipt, the audit does not run,
`C6_AUDIT_SAMPLE=NOT_RUN`, and the study files `CENSUS_AUDIT_FAILED` with the missing seed named.**" `audit select`
refuses without the stage-1 seal as well; the exhibited input takes the documented NOT_RUN limb.

C5. Zero denominator with any passage on either side. Concrete input: the sealed denominator is 0 while the auditor's
enumeration lists at least one passage. C6: "A sealed denominator of zero with any passage on either side fails." →
CENSUS_AUDIT_FAILED; it precedes CENSUS_PARTIAL in the §4 order, so the zero-denominator limb of CENSUS_PARTIAL is not
reached on this input (contrast exhibit B2 limb (b), where no passage exists on either side).

C6. Incomplete reconstruction. Concrete input: the auditor's reconstruction for a selected claim omits a required
field (one input record lacks `derived_from`; another lacks `origin_search` although silent). C6: "before sealing,
`audit seal-rederivation` validates the reconstruction schema — every input carries symbol, status, value, source
coordinates, origin, origin evidence and `derived_from` (and `origin_search` when silent) — and refuses an incomplete
one" → no stage-2 seal → `audit compare` cannot run → the audit "does not run to PASS for any cause (the cause named)"
→ CENSUS_AUDIT_FAILED, cause named.

C7. Fabricated evidence quotation in an off-sample dependency record. Concrete input: selected claim S depends through
a `derived_from` chain on record r assigned to unselected claim U; the sealed r carries an `origin_evidence.verbatim`
that does not occur at its cited `source_file`/`source_line` (fabricated). V30 §3: "every record in each selected
claim's complete dependency closure is validated and compared, records assigned to unselected claims included";
"`audit compare` … compares every field, every evidence coordinate and quotation, and every dependency edge against the
sealed ledger … and reports a missing field, a missing input, a dependency the auditor did not itself reconstruct, or
any unsupported difference as `MISMATCH`" → r is compared although U is off-sample; the fabricated quotation is an
unsupported difference → MISMATCH on S → "no audited claim or origin is `MISMATCH`" fails → CENSUS_AUDIT_FAILED.

C8. Duplicated input id. Concrete input: the auditor's reconstruction carries the same `input_id` twice (a copy of a
record under a second key). V30 §3: "Before sealing or comparing a reconstruction, every `input_id` must occur exactly
once across the entire reconstruction … and … a duplicate, an identity conflict, a missing record or an unsupported
field, evidence or edge difference is `MISMATCH` on every selected claim that depends on it" → CENSUS_AUDIT_FAILED.
(Sibling guard in the sealed chain: JOIN requires "identifiers are unique".)

C9. Record reconstructed under the wrong claim. Concrete input: the auditor reconstructs record r under claim key C2
while r is sealed under claim C1 (or r's explicit `claim_id` disagrees with its enclosing key). V30 §3: "an explicit
`claim_id` or `input_id` field must agree with its enclosing keys; at comparison each reconstructed record is bound to
its sealed identity — its enclosing claim key must be the sealed record's claim — and … an identity conflict … is
`MISMATCH`" → CENSUS_AUDIT_FAILED.

C10. Hybrid-branch record. Concrete input: the sealed ledger declares for record r a primary branch (origin `CHOSEN`,
evidence quotation q1, parent list L1) and a declared alternative branch (origin `IMPORTED`, evidence q2, parent list
L2). The auditor's r carries origin `IMPORTED` with evidence q1 (or origin `CHOSEN` with parent list L2) — a hybrid of
primary and alternative fields. V30 §3: "a record matching neither complete branch is `MISMATCH` even when the
root-origin sets agree" → CENSUS_AUDIT_FAILED.

C11. Receipt failure. Concrete input: receipt P or receipt T is missing, or Blanc's post-opening re-hash of the tally
or the protocol mismatches a receipted value. §7: "Any missing receipt or mismatch files `CENSUS_AUDIT_FAILED` (§4,
whose definition now names this case), leaves the interpretation `NOT_RUN` and voids the comparison"; §4.3: "or the
receipt verification of the seal fails."

### NEGATIVE CONTROL — a complete declared alternative branch does NOT file CENSUS_AUDIT_FAILED
Concrete input: sealed record r for a selected claim declares the primary branch (origin `CHOSEN`, evidence q1, parent
list L1) and the alternative branch (origin `IMPORTED`, evidence q2 at its own coordinates, parent list L2). The
auditor's r carries origin `IMPORTED`, evidence exactly q2 at the sealed coordinates, and parent list L2, with every
undeclared field (symbol, status, value, source coordinates) equal to the sealed primary fields. V30 §3: "Matching a
declared alternative is not `MISMATCH` only when the auditor's origin, origin evidence and parent list jointly equal
one COMPLETE declared branch: the primary branch is the primary fields, the alternative branch is every declared
alternative field applied together with the undeclared fields staying primary" → r matches the alternative branch
complete → "one consistent graph is constructed from the matched complete records over all selected claims and their
dependency closures and used for every dependent claim's sealed-root comparison" → MATCH, roots recomputed under the
matched graph, branches reported → this claim contributes no MISMATCH and does NOT file CENSUS_AUDIT_FAILED.
Sub-case, parent-only alternative: the auditor's r matches the alternative parent list with origin and evidence
unchanged → accepted, because "an unchanged-origin parent alternative is accepted only when the alternative branch's
origin and evidence are also unchanged." (Contrast C10: mixing q1 with the alternative origin is neither complete
branch → MISMATCH.)

## D. THE SUSPICION, ANSWERED DIRECTLY — CENSUS_COMPLETE: REACHABLE

Question: does a single blocked, absent-input, or no-derivation-stated claim anywhere in a real corpus force
CENSUS_PARTIAL, making CENSUS_COMPLETE unreachable in practice?

Answer: REACHABLE — exhibited in §B1 — with its fragility stated exactly.

Routing that forces CENSUS_PARTIAL on a corpus containing even one such claim: §3's precedence routes any claim whose
named source is unobtainable or unmatched (`REPRO_BLOCKED`), whose input is absent (`REPRO_INPUT_ABSENT`), whose
procedure is unstated (`REPRO_NO_DERIVATION_STATED`), or whose attempt stalls (`REPRO_NOT_EVALUABLE`) OUT of the
arithmetic group; §4.2's condition is existential over the whole corpus — "**at least one included claim carries a
non-arithmetic outcome …, or the denominator is zero**" — and "it takes precedence over `CENSUS_COMPLETE`." So yes: one
such claim anywhere in the corpus files CENSUS_PARTIAL, and in a real corpus of 89 texts the class may well be rare in
practice.

Routing that reaches CENSUS_COMPLETE anyway: §4.1 quantifies over the actual corpus, not over a corpus the text
prescribes. Nothing in the document requires any non-arithmetic outcome to exist; an all-`PRINTED`/`STANDARD` corpus in
which every attempt completes (exhibit B1) satisfies "every included claim carries exactly one outcome from the
arithmetic group of §3, with `C6_AUDIT_SAMPLE=PASS`", fails §4.2's condition, and no earlier class in the §4 order has
a holding condition — so CENSUS_COMPLETE is filed. A class whose condition a concrete input can satisfy is reachable
under C0 ("exhibit a concrete input that produces it"); C0 does not ask how likely the input is. Contrast with the
history (§10.3, non-binding): `REPRO_AFTER_CHOICE` was unreachable because NO input could produce it — the method
contained no procedure that could file it. That is the unreachable shape; CENSUS_COMPLETE does not have it. (Also
noted: the zero-denominator clause closes the vacuous edge — "no census is complete over nothing" — and `REPRO_FAILED`
sits inside the arithmetic group, so the class is not confined to corpora where every paper's arithmetic succeeds.)

## E. SEAT-TALLY STOPS AND THEIR §4 FILINGS

E1. C1B_BATCH_COVERAGE=FAIL. Concrete input: batch b3's `SEAT_REPORT_b3.md` lacks the packet's `ACCESS_SHA` line (or an
owned text's bytes fail verification against its manifest row, or one manifest text is owned by no batch / two
batches). C1B: "`C1B_BATCH_COVERAGE=PASS` iff every manifest text is owned by exactly one batch, every owned text's
bytes verify against its manifest row, and every batch report prints the packet's `ACCESS_SHA` … Either FAIL stops the
seat's tally." §4 filing (the C1B contract, stated in the text): "a FAIL in every seat that tries it, after two tries,
files `R3C2_NO_CLASS`; a surviving fail/pass split files `CENSUS_CONTROL_SPLIT`; an unreached check is `NOT_RUN`."

E2. JOIN=FAIL. Concrete input: one seal in the ordered LIMB-A chain does not match its sealed bytes (or a candidate is
not owned by its batch, an evidence source is not a manifest text, a `derived_from` cycle). C1B: "`JOIN=PASS` iff every
seal matches, the ordered predecessor chain is intact from a root with no predecessor, every candidate and ledger claim
is owned by its batch, every evidence source is a manifest text, identifiers are unique and every `derived_from`
resolves acyclically. Either FAIL stops the seat's tally." §4 filing: the same C1B contract — `R3C2_NO_CLASS` (fail in
every seat after two tries) or `CENSUS_CONTROL_SPLIT` (fail/pass split). Limb-B joins are bound to the agreed limb-A
seals file ("`join` of the limb-B chain verifies the binding"), so a binding failure takes the same route.

E3. C5C_NO_FALLBACK=FAIL. Concrete input: a session's printed, session-identified provider log is missing or carries a
fallback entry. §9: "the no-fallback control `C5C_NO_FALLBACK=PASS|FAIL|NOT_RUN` requires a printed, session-identified
provider log for every session — a missing log or any fallback entry is FAIL, an unreached check NOT_RUN — a pre-tally
control under the `R3C2_NO_CLASS` and `CENSUS_CONTROL_SPLIT` rules, checked by the lane owner." §4 filing: per those
two rules (fail in every seat after two attempts → R3C2_NO_CLASS; split → CENSUS_CONTROL_SPLIT); the stop is pre-tally.

E4. Merge field disagreement. Concrete input: the two seats agree on the `input_id` set for an agreed claim but differ
on one record's `status` (A files `PRINTED`, B files `STANDARD`) or `value`. C3: "where the two seats' value, status,
symbol or source coordinates differ on the same input id, `merge` prints every such disagreement, reports
`FIELD_DISAGREEMENTS`, exits 1 and writes no merged file — the lane resolves it in the open before the tally." §4
filing: the text names NO §4 class for a field disagreement — it is a lane-level stop with open resolution before the
tally, distinct from the input-id-set difference, for which the text does name a class ("an input-set difference
surviving that reconciliation stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4)"). I do not invent a class the
text does not license; stated as the text stands, the disagreement itself files nothing and is resolved lane-side, and
no declared §3 outcome or §4 class depends on it for reachability. (If it survived unresolved, the design names no
class for that state; that is a completeness observation about the stop taxonomy, not an unreachability finding — every
declared class is exhibited above without it.)

## F. rests_on NOT_COMPUTED — REACHABLE STATE (auxiliary, not a §3 outcome or §4 class)

Concrete input: claim D1 (§A5) is included and states no procedure, so no inputs are extracted and its claim ledger is
empty. §3 (master-only rule the script implements): "an empty ledger is valid and every included candidate without a
record carries `rests_on` `NOT_COMPUTED`"; §3: "`rests_on` is computed and reported for every included claim that has
at least one ledger record, whatever its outcome; a claim with no ledger record carries `rests_on` `NOT_COMPUTED`, and
the `rests_on` tally reports a `NOT_COMPUTED` row."; §9: compute "emits `rests_on` `NOT_COMPUTED` for every included
candidate with no ledger record". Clause path: §2 step 5 (script records `rests_on` from the ledger) → lane-side
`compute` → NOT_COMPUTED row in the second tally. The reproduction tally routes D1 to `REPRO_NO_DERIVATION_STATED`
(non-arithmetic), so a census containing it files CENSUS_PARTIAL — the `rests_on` state and the §4 class are two
independent tallies from one pass, exactly as option (c) specifies. (Sibling state, also reachable: a claim whose
dependency graph reaches a disputed record in ANY claim is itself `DISPUTED` with both values — §3 master-only note;
exhibited by claim X derived_from record r of claim Y on which the seats' origins disagree.)

## G. UNREACHABLE VERDICTS — NONE

Every per-claim outcome of §3 (six of six), every study-level class of §4 (eight of eight), every C6 path to
`CENSUS_AUDIT_FAILED` enumerated in the brief (ten paths plus the receipt path), the complete-branch negative control,
the four seat-tally stops, and the `rests_on` `NOT_COMPUTED` state are exhibited above with a concrete input and a
clause path through the text as it stands at V30. No declared verdict is UNREACHABLE; there is no blocking clause to
quote. The one historically unreachable class, `REPRO_AFTER_CHOICE`, is retired into the `rests_on` field by the
principal's option-(c) ruling and is not a declared outcome of §3; nothing is owed for it.

One completeness observation, stated rather than absorbed (not an unreachability): an unresolved merge
`FIELD_DISAGREEMENTS` state has no named §4 class (exhibit E4); the text routes it to open lane resolution before the
tally. No declared verdict's reachability depends on it.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V30_KIMI_COMPLETE

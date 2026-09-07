ACCESS_SHA=8095c18c8f29901b6a4ebe83a07b78dcab5955d440c25b4f19a9f0d713ba8ac7
C0_REACHABILITY=PASS

C0 REACHABILITY EXHIBITION — R3C2 reproduction census preregistration, V38 (living draft)
Seat: kimi, 2026-09-07. The master R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md was read from disk in full
(1526 lines; the two over-long lines 117 and 315 were read to their ends). No other file in the directory
was opened. §3 is exhibited as it stands under the adopted option (c): one pass, two tallies;
REPRO_AFTER_CHOICE is retired into the script-computed rests_on field; there is no held clause. §10 is
history and binds nothing; nothing below relies on it except where the operative text itself is quoted.

This exhibition asks only whether each declared verdict CAN OCCUR. It does not gate the design and does
not judge its physics. Concrete inputs below are design-space constructions: specific claims with specific
numbers, files and lines, routed through the document's own clauses.

=====================================================================
(A) PER-CLAIM OUTCOMES OF §3 (six tokens, per C1's candidate schema)
=====================================================================

verdict | concrete input | clause path | reachable
--------+----------------+-------------+----------

REPRO_WITHIN_STATED_PRECISION | Paper age.md, line 88, prints "we find the age of the Universe to be
13.8 Gyr", asserted as its own result; its stated recipe is the flat-LCDM age integral in H0, Omega_m,
Omega_L, and the paper prints 67.36, 0.3153, 0.6847 verbatim — all three on C3's closed list, so each is
status STANDARD, origin STANDARD via ORIG_CONSTANT, symbol = ledger key, value = the exact table string.
The paper states no uncertainty, so the printed precision is the claim's stated precision. The mechanical
attempt consumes the three STANDARD records (the only consumable statuses) and reproduces 13.797 Gyr,
which rounds to 13.8 at the printed precision (half away from zero). Both numbers reported
(printed_value "13.8", reproduced_value "13.797"); rests_on = DERIVED_STANDARD_OR_MEASURED_ONLY computed
by script. | §1 inclusion (printed numeral asserted as the paper's own result) -> §2 steps 1-3 (extract;
list; classify STANDARD against C3's closed list) -> §3 consumption rule ("THE INPUTS THE ARITHMETIC MAY
CONSUME = every ledger record with status PRINTED ... or STANDARD") -> §2 step 4 mechanical attempt ->
§3 REPRO_WITHIN_STATED_PRECISION, stated-precision limb ("the reproduced value must round to the printed
numeral at that precision, rounding half away from zero") -> §2 step 5 two-seat outcome agreement -> C1
final census schema (arithmetic-group outcome carries printed_value and reproduced_value). | YES

REPRO_FAILED | Paper sigma8.md, line 131, prints "we obtain sigma8 = 0.85 +/- 0.01" as its own result
from sigma8 = sigma8_ref x (Omega_m/0.3)^0.5, printing sigma8_ref = 0.8111 and Omega_m = 0.3153 verbatim
(both on C3's closed list -> STANDARD). The inputs are sufficient; the mechanical attempt gives
0.8111 x (0.3153/0.3)^0.5 = 0.8315. The stated-uncertainty test is taken once: |0.8315 - 0.85| = 0.0185
> 0.01. Both numbers reported; wording "unreproduced from the stated inputs", not "error"; rests_on
reported beside it. | §1 -> §2 steps 1-4 (all inputs PRINTED/STANDARD, attempt completes) -> §3
REPRO_FAILED ("the inputs the paper states are sufficient for its recipe, but the arithmetic does not
give the paper's number") with the uncertainty limb ("|reproduced - printed| <= the stated uncertainty,
taken once — not doubled, not rounded") failing -> §2 step 5. | YES

REPRO_BLOCKED | Limb (a), source not enumerable: paper growth.md, line 54, prints "using the baryon
density of Dodelson (2003) we find f sigma8 = 0.47" as its own result; omega_b is not printed in the
claiming paper; the named source Dodelson (2003) is not an enumerable text of R3C2_CORPUS_MANIFEST.md,
so the census may not open or consume it, "whether that source is obtainable elsewhere is irrelevant".
Limb (b), enumerable source, no machine-match: same construction except the named source IS a pinned
enumerable text whose cited line carries no matching numeric token for the cited symbol. In both limbs
the input is recorded status BLOCKED, origin IMPORTED, ORIG_CITATION evidence quoting the claiming
paper's naming sentence at the claiming file and line, empty value, never consumed; the input and the
source are named. Where another input of the same claim is also ABSENT, §3 precedence files BLOCKED
first. | §1 -> §2 steps 1-3 (classify BLOCKED per the named-source rule) -> §2 import paragraph's
terminal rule ("If the named source is not enumerable or the value does not match there, file
REPRO_BLOCKED under §3") -> §3 REPRO_BLOCKED (both limbs: "is not an enumerable text pinned in
R3C2_CORPUS_MANIFEST.md" / "an enumerable pinned text at whose cited line the value does not
machine-match"); C3's BLOCKED record requirements. | YES

REPRO_NOT_EVALUABLE | (a) SYMBOLIC_TIMEOUT: paper pot.md, line 210, prints "the fixed point is
x* = 0.318" from a stated algebraic system; the sympy solution launched as
/usr/bin/python3 -E r3c2_timeout.py 120.0 -- <command> exceeds the monotonic 120.0 s deadline; the
wrapper prints SYMBOLIC_TIMEOUT and exits 124 — the reportable outcome — and the point reached is
printed. (b) MACHINERY_UNAVAILABLE: paper pk.md, line 77, prints "our Boltzmann integration gives the
turnover at k = 0.0188 h/Mpc"; the stated recipe requires numerical Boltzmann machinery this lane does
not have; MACHINERY_UNAVAILABLE and the point reached are printed. | §1 -> §2 attempt -> §3
REPRO_NOT_EVALUABLE ("the arithmetic could not be completed within the 120-second cap, or requires
machinery this lane does not have. Print SYMBOLIC_TIMEOUT ... or MACHINERY_UNAVAILABLE ..., and the
point reached"); §9 wrapper contract. | YES

REPRO_NO_DERIVATION_STATED | Paper rs.md, line 96, prints "the sound horizon at decoupling is
r_s = 147.1 Mpc" as its own result (not attributed to another work — the paper asserts it as its own),
and the paper states no equation and no computational procedure anywhere; the only provenance sentence
is "obtained from our analysis pipeline" — a procedure named but not specified, stating no operations a
seat could attempt. The passage is named. The claim has no equation, hence no inputs, hence no ledger
records, so its rests_on is NOT_COMPUTED (see Table C row R1). | §1 (satisfies the definition: a printed
numeral the paper asserts as a result of its own; none of the excluded kinds applies) -> §2 step 1 finds
no equation to extract -> §3 REPRO_NO_DERIVATION_STATED ("states no equation or computational procedure
that could produce it ... A procedure named but not specified ... file this class and name the
passage"); first in the §3 precedence. | YES

REPRO_INPUT_ABSENT | Paper rho.md, line 41, prints "from rho_c = 3H^2/8piG we find
rho_c = 8.5e-30 g cm^-3"; H = 71 is printed (status PRINTED, origin per its evidence); G's value is
never printed anywhere in the claiming paper and no source is named for it. G is on C3's closed list,
but §2 step 3 makes STANDARD available only for "a closed-list value printed in the claiming paper";
unprinted and untraced, G is "neither printed nor traced to any named source" -> ABSENT. The machine
floor forbids supplying it: "A seat may not supply a value for an ABSENT or BLOCKED input. Encountering
one ends that claim's attempt." The input is named. | §1 -> §2 steps 1-3 (classify ABSENT) -> §2
machine-floor sentence ending the attempt -> §3 REPRO_INPUT_ABSENT ("an input the equation needs is
ABSENT from the paper — neither printed nor traced to any named source — so the attempt stops there.
Name the input."). | YES

§3 result: all six declared per-claim outcomes reachable. (REPRO_AFTER_CHOICE is retired by the option
(c) ruling and is not a declared outcome of the text as it stands.)

=====================================================================
(B) STUDY-LEVEL CLASSES OF §4 (eight classes; precedence §4 final block)
=====================================================================

verdict | concrete input | clause path | reachable
--------+----------------+-------------+----------

CENSUS_COMPLETE | A pinned corpus in which every included claim is of the shape of Table A rows 1-2:
every claim states its derivation, every input is PRINTED or STANDARD, every attempt completes within
the cap, so all N >= 1 included claims carry exactly one arithmetic-group outcome
(REPRO_WITHIN_STATED_PRECISION or REPRO_FAILED). The C6 auditor's independent enumeration matches the
sealed one row for row, both seals match, the recomputed selection matches, no row is an omission, the
dispute rate is at or below 10%, and no audited claim or origin is MISMATCH -> C6_AUDIT_SAMPLE=PASS.
Denominator non-zero. Full tally and rests_on tally reported. | §4.1 ("every included claim carries
exactly one outcome from the arithmetic group of §3, with C6_AUDIT_SAMPLE=PASS"; the zero-denominator
clause does not apply) -> C6 PASS predicate -> §4 precedence: no earlier stop class (R3C2_NO_CLASS,
CENSUS_CONTROL_SPLIT, CENSUS_DENOMINATOR_DISPUTED, CENSUS_OUTCOME_DISPUTED, CENSUS_ORIGIN_DISPUTED,
CENSUS_AUDIT_FAILED, CENSUS_PARTIAL) holds, so CENSUS_COMPLETE is filed. | YES — see the dedicated
answer to the suspicion below.

CENSUS_PARTIAL | Limb (a): any corpus containing at least one of Table A rows 3-6 — e.g. growth.md's
blocked omega_b claim filing REPRO_BLOCKED — while all other claims file arithmetic outcomes; the one
non-arithmetic outcome forces PARTIAL and "it takes precedence over CENSUS_COMPLETE". Report each such
claim and why. Limb (b), zero denominator: an enumeration in which every enumerated candidate is
excluded under §1's excluded kinds (all numerals are equation numbers, dates, attributed-not-derived,
or author-specified inputs) -> the exclusion ledger is full and the included count is zero. | §4.2
("at least one included claim carries a non-arithmetic outcome (REPRO_NO_DERIVATION_STATED,
REPRO_INPUT_ABSENT, REPRO_BLOCKED, REPRO_NOT_EVALUABLE), or the denominator is zero"); §4.1's
zero-denominator clause ("A denominator of zero files CENSUS_PARTIAL with the empty enumeration named;
no census is complete over nothing."). | YES (both limbs)

CENSUS_AUDIT_FAILED | Reachable through every C6 path — the eleven required paths plus the receipt
path are exhibited individually in Table C, rows A1-A12, and the ORIG_SILENT-alternative pass-through
that correctly does NOT file it is row A13. General input: any audited claim whose outcome the auditor
cannot reproduce, any ledger incompleteness, or any audit that does not run to PASS for any cause
(cause named); no tally is filed; report which. | §4.3 ("the audit of §6 cannot reproduce a sampled
per-claim outcome or ledger, or does not run to PASS for any cause (the cause named), or the receipt
verification of the seal fails. No tally is filed; report which."); C6's omission, dispute-rate,
seed, zero-denominator, schema-refusal, closure-comparison and branch-matching clauses; §7's receipt
clause. | YES (every named path; Table C)

R3C2_NO_CLASS | Limb (a), control fails in every seat after two attempts: the live MANIFEST_SHA256
printed by C5's fifth command differs from the dispatch record's pinned digest in both seats, twice
each -> C5_HARNESS_PINNED=FAIL in every seat that attempted it after two attempts. Limb (b),
pre-dispatch: the packet builder finds a forbidden-list string surviving in the built packet ->
C4_PACKET_REDACTED=FAIL and the packet is not written — "a packet or seat-isolation failure before
dispatch files this class". Limb (c), seat-tally stops: C1B_BATCH_COVERAGE=FAIL (a manifest text owned
by two batches, or an owned text's bytes failing against its manifest row, or a batch report missing
the packet's ACCESS_SHA) in every seat after two tries; JOIN=FAIL (a broken seal or predecessor chain,
a candidate owned by no batch, an evidence source outside the manifest, a duplicate identifier, or a
cyclic derived_from) in every seat after two tries; C5C_NO_FALLBACK=FAIL (a missing session provider
log or any fallback entry) in every seat — each files R3C2_NO_CLASS. Note the boundary the text draws:
a C6 audit failure or seal-receipt failure files CENSUS_AUDIT_FAILED, not this class. | §4.4 ("a
control among C0 through C5b fails in every seat that attempted it after two attempts; a packet or
seat-isolation failure before dispatch files this class"); C1B's filing rule ("a FAIL in every seat
that tries it, after two tries, files R3C2_NO_CLASS"); §9's C5C sentence ("a pre-tally control under
the R3C2_NO_CLASS and CENSUS_CONTROL_SPLIT rules"). First in §4 precedence. | YES

CENSUS_DENOMINATOR_DISPUTED | Limb (a), enumeration split: seat A includes the passage (cosmos.md,
line 42, numeral "13.8") as a claim; seat B excludes it as kind DATE; two reconciliation attempts fail
to agree -> the study stops; the disputed candidates are listed and the complete candidate and
exclusion ledgers are reported with the dispute. Limb (b), input-list split: on the agreed claims,
seat A's ledger lists input H0 for claim X and seat B's does not, so merge exits 1 on the differing
input_id sets; the seats reconcile their input lists against the paper's stated equation once; the
difference survives -> the study stops, the disputed inputs listed with both seats' quotations. | §1
("disagreement on any candidate that survives two reconciliation attempts stops the study under
CENSUS_DENOMINATOR_DISPUTED"); §4.5 ("the two enumerations disagree after two reconciliation attempts,
or the two seats' input lists for the agreed claims disagree after the one C3 reconciliation"); §6
limb A (tolerance zero, measured in candidate passages); C3's merge exit-1 reconciliation rule. | YES
(both limbs)

CENSUS_OUTCOME_DISPUTED | On the agreed included claim sigma8.md line 131 ("sigma8 = 0.85 +/- 0.01"),
seat A reproduces 0.8315 and files REPRO_FAILED (|0.8315 - 0.85| = 0.0185 > 0.01); seat B reproduces
0.849 and files REPRO_WITHIN_STATED_PRECISION (|0.849 - 0.85| = 0.001 <= 0.01). The single
reconciliation against the printed numeral and the stated-precision rule of §3 is run and the split
survives it — the seats do not agree on the reproduced value's last digit and neither moves. The
census does not proceed; the claim is listed with both seats' outcomes, both number pairs, and the
step each seat reached. | §2 step 5 ("a disagreement surviving that reconciliation files
CENSUS_OUTCOME_DISPUTED (§4)"); §4.6. | YES

CENSUS_ORIGIN_DISPUTED | Ten included claims; input beta (printed "we take beta = 1/929.25") feeds
three of them. Seat A finds no provenance sentence, runs and prints its origin_search (query with
variants, files, matches — all empty) and files ORIG_SILENT -> UNDECLARED; seat B quotes "we take beta
= 1/929.25" at its line and files ORIG_CHOICE_STATED -> CHOSEN. Origin disagreements are reported,
never reconciled; inputs affecting 3 of 10 included claims = 30% > 10%. The census does not proceed;
every disputed input is listed with both seats' classification and both quotations. (Each affected
claim's rests_on is computed under both classifications, printed as a pair and marked DISPUTED, with a
DISPUTED row in the rests_on tally.) | C6/C3 dispute rule ("An input on which the two classifications
disagree is filed ORIGIN_DISPUTED ... not reconciled. Above 10% of included claims,
CENSUS_ORIGIN_DISPUTED."); §4.7. | YES

CENSUS_CONTROL_SPLIT | C5_HARNESS_PINNED passes in seat A (all five commands exit 0, path and digest
equal to the dispatch record) and fails in seat B (live MANIFEST_SHA256 mismatch), each after two
attempts. Equally: C1B_BATCH_COVERAGE, JOIN or C5C_NO_FALLBACK failing in one seat and passing in the
other after two tries ("a surviving fail/pass split files CENSUS_CONTROL_SPLIT"). Both seats' outputs
are reported and the study stops; the passing seat's result is not adopted. | §4.8 ("a control fails
in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not
adopt the passing seat's result."); C1B's split rule; §9's C5C sentence. | YES

§4 result: all eight declared study-level classes reachable.

=====================================================================
(C) REQUIRED ADDITIONAL EXHIBITS
=====================================================================

C1. CENSUS_AUDIT_FAILED through each named C6 path. Each row gives a concrete input and the clause
that routes it to the filing; every row ends at §4.3 ("does not run to PASS for any cause (the cause
named)" / "cannot reproduce ... No tally is filed"). All reachable.

A1  Sealed-included absent from the auditor | The sealed candidate ledger includes (cosmos.md, line
42, "13.8") as a claim; the auditor's independent enumeration of all 89 enumerable texts has no row
for that passage key. | C6 Omissions: "a sealed INCLUDED passage absent from the auditor's enumeration
... each is ledger incompleteness and files CENSUS_AUDIT_FAILED"; the omission row also violates the
PASS predicate ("no row is an omission"). | YES

A2  Auditor-listed absent from the sealed ledgers | The auditor lists (cosmos.md, line 57, "0.048")
as an excluded passage of kind ATTRIBUTED_NOT_DERIVED; neither the sealed candidate ledger nor the
sealed exclusion ledger names it. | C6 Omissions: "a passage the auditor lists (included OR excluded)
that the sealed ledgers omit — each is ledger incompleteness and files CENSUS_AUDIT_FAILED". | YES

A3  Dispute rate above 10% | Sealed denominator 50; six passage keys are AUDIT_INCLUSION_DISPUTED
(both sides list them, disposed differently, or sealed-excluded and absent from the auditor); 6/50 =
12% > 10%. | C6: "above 10% of the sealed included denominator the audit files CENSUS_AUDIT_FAILED;
at or below it the count is reported." | YES

A4  Seedless selection | The tally digests are receipted (T), but the external custodian never
supplies the 64-hex-character seed, or supplies it without recording it with the receipt. | C6: "If
the seed is not supplied and recorded with the receipt, the audit does not run, C6_AUDIT_SAMPLE=
NOT_RUN, and the study files CENSUS_AUDIT_FAILED with the missing seed named." | YES

A5  Zero denominator | The sealed denominator is zero while the auditor's enumeration lists at least
one passage. | C6: "A sealed denominator of zero with any passage on either side fails." -> audit not
PASS -> §4.3. | YES

A6  Incomplete reconstruction | The auditor's reconstruction for a selected claim carries an input
record missing its derived_from field (or symbol, status, value, source coordinates, origin evidence;
or origin_search for an ORIG_SILENT record). | C6: "before sealing, audit seal-rederivation validates
the reconstruction schema — every input carries symbol, status, value, source coordinates, origin,
origin evidence and derived_from (and origin_search when silent) — and refuses an incomplete one" ->
no stage-2 seal -> the audit does not run to PASS, cause named -> §4.3. (At compare, the same gap is
"a missing field, a missing input ... reported as MISMATCH".) | YES

A7  Fabricated evidence quotation in an off-sample dependency record | Selected claim C1 depends on
input i7, which is owned by unselected claim C9. The sealed i7 record carries verbatim
"we adopt beta = 1/929.25" as its ORIG_CHOICE_STATED quotation, but that string does not occur at the
cited file and line; the auditor's reconstruction of the closure carries the genuine line. | §3
master block: "every required field, evidence item and dependency edge is compared throughout each
selected claim's complete dependency closure, records assigned to unselected claims included" ->
quotation mismatch on i7 -> MISMATCH propagated to C1 -> the audit fails -> §4.3. | YES

A8  Duplicated input id | The auditor's delivered reconstruction carries two records with the same
input_id. | §3 master block: "Before sealing, a reconstruction with a duplicate input_id or an
explicit identity field inconsistent with its enclosing keys is refused." -> seal-rederivation refuses
-> the audit does not run to PASS, cause named -> §4.3. | YES

A9  Record reconstructed under the wrong claim | The auditor's reconstruction files input i3 under
claim C2 when the sealed ledger's i3 belongs to claim C5. | §3 master block: "each enclosing-claim
versus sealed-claim identity conflict is recorded as a MISMATCH of that input, propagated to every
selected claim whose dependency closure contains the input, and fails the overall audit" -> §4.3. | YES

A10 Hybrid-branch record, direction 1 (primary provenance + alternative parents) | The merged sealed
record for input i4 carries primary branch (origin DERIVED, ORIG_EQUATION evidence, parents [i5]) from
seat A and a declared alternative (origin CHOSEN, ORIG_CHOICE_STATED evidence, parents [i6]) from seat
B. The auditor's record carries A's origin and evidence with B's parent list. It matches neither
complete declared branch. | §3 master block: "If neither complete branch matches, an unconditional
record-level MISMATCH is appended before any field-specific diagnostic, propagated to every dependent
selected claim, and the audit fails even when the root-origin sets agree — the full-record predicate
decides the verdict" -> §4.3. | YES

A11 Hybrid-branch record, direction 2 (alternative provenance + primary parents) | Same construction
as A10 with the auditor's record carrying B's origin CHOSEN and choice evidence with A's parents [i5].
Also matches neither complete declared branch. | Same clause as A10 ("If neither complete branch
matches, an unconditional record-level MISMATCH ... and the audit fails even when the root-origin sets
agree") -> §4.3. | YES

A12 Changed origin_search CONTENT on an ORIG_SILENT branch | The sealed merged record's matched branch
carries origin_search {query: "beta", files: [f1, f2], matches: []}; the auditor's corresponding search
carries {query: "beta", files: [f1, f3], matches: []} — an entry changed, not merely reordered. | §3
MOI block: "Reordering an inventory alone must preserve the complete outcome; adding, removing or
changing an entry must still fail, and changed-entry, added-entry and deleted-entry negatives are
carried in the kit to prove that canonicalisation erases no evidence difference." The search of the
matched branch is compared as JSON structure after canonicalisation; the changed entry survives
canonicalisation and mismatches -> MISMATCH -> §4.3. | YES

A12b Receipt-verification path | After opening, Blanc's independent re-hash of the tally differs from
the hash recorded in receipt T (or receipt P or T is missing). | §7: "Any missing receipt or mismatch
files CENSUS_AUDIT_FAILED (§4, whose definition now names this case), leaves the interpretation
NOT_RUN and voids the comparison"; §4.3: "or the receipt verification of the seal fails". | YES

A13 PASS-THROUGH — auditor reconstruction equal to a COMPLETE declared ORIG_SILENT alternative branch
(does NOT file CENSUS_AUDIT_FAILED) | Input i9 of selected claim C3: seat A filed origin MEASURED with
ORIG_MEASURED evidence (primary branch); seat B filed ORIG_SILENT -> UNDECLARED with an adequate
origin_search (query with variants, files, matches). merge preserves B's complete branch as origin_alt
UNDECLARED, origin_evidence_alt and origin_search_alt (C3 lane-side note; §3 master block). The auditor
independently reconstructs i9 exactly as B's complete branch — UNDECLARED, ORIG_SILENT, the same
search content (its entry order irrelevant, since canonicalisation applies on both sides). audit
compare binds the auditor's record to the declared alternative branch, compares the search of THAT
branch as JSON structure, finds every field equal, recomputes roots under the matched branch, and
reports the matched branch. No MISMATCH arises; the audit continues and may PASS; CENSUS_AUDIT_FAILED
is correctly not filed. | C6: "binds an auditor classification that matches a declared sealed
alternative to that branch (§3)"; C3 lane-side: "merge preserves branch-specific provenance evidence,
adding origin_alt, origin_evidence_alt and, when the alternative uses ORIG_SILENT, origin_search_alt";
§3: "complete branches are matched before roots are recomputed, and the sealed and matched branches
are reported"; V38's canonical-search function applied "on BOTH sides of the C6 comparison". | YES
(reachable as a non-filing)

C2. Seat-tally stops and their §4 filings.

T1  C1B_BATCH_COVERAGE=FAIL | Batch b3 and b7 both own manifest text paper_12.md (partition violated),
or an owned text's bytes fail against its manifest row, or batch report b5 omits the packet's
ACCESS_SHA. The seat's tally stops. | C1B: "C1B_BATCH_COVERAGE=PASS iff every manifest text is owned by
exactly one batch, every owned text's bytes verify against its manifest row, and every batch report
prints the packet's ACCESS_SHA ... Either FAIL stops the seat's tally." §4 filing: FAIL in every seat
after two tries -> R3C2_NO_CLASS; fail in one seat, pass in the other after two tries ->
CENSUS_CONTROL_SPLIT; unreached -> NOT_RUN. | YES (the stop and both filings)

T2  JOIN=FAIL | The limb-A seal chain has a batch whose recorded predecessor does not match the
preceding seal (chain broken), or a candidate in the joined file is owned by no batch, or a ledger
evidence source is not a manifest text, or two records share an identifier, or a derived_from cycle
resolves. The seat's tally stops. | C1B: "JOIN=PASS iff every seal matches, the ordered predecessor
chain is intact from a root with no predecessor, every candidate and ledger claim is owned by its
batch, every evidence source is a manifest text, identifiers are unique and every derived_from
resolves acyclically. Either FAIL stops the seat's tally." §4 filing: as T1 — every-seat FAIL ->
R3C2_NO_CLASS; split -> CENSUS_CONTROL_SPLIT; unreached -> NOT_RUN. | YES (the stop and both filings)

T3  C5C_NO_FALLBACK=FAIL | Session 2 of seat B has no printed, session-identified provider log, or a
log shows a fallback provider entry. | §9: "the no-fallback control C5C_NO_FALLBACK=PASS|FAIL|NOT_RUN
requires a printed, session-identified provider log for every session — a missing log or any fallback
entry is FAIL, an unreached check NOT_RUN — a pre-tally control under the R3C2_NO_CLASS and
CENSUS_CONTROL_SPLIT rules, checked by the lane owner". §4 filing: FAIL in every seat after two
attempts -> R3C2_NO_CLASS; split -> CENSUS_CONTROL_SPLIT. | YES (the stop and both filings)

T4  Merge field disagreement | On agreed claim X, both seats pass validate with different coordinates
for the same input id: seat A records value "67.4" at cosmos.md line 10, seat B records value "67.36"
at cosmos.md line 12 (the paper prints the symbol at both lines; both records machine-match at their
own coordinates, so both ledgers validate). merge prints every such disagreement, reports
FIELD_DISAGREEMENTS, exits 1 and writes no merged file — the tally cannot be sealed, so the seat tally
stops before it exists. | C3 lane block: "where the two seats' value, status, symbol or source
coordinates differ on the same input id, merge prints every such disagreement, reports
FIELD_DISAGREEMENTS, exits 1 and writes no merged file — the lane resolves it in the open before the
tally." §4 filing: NONE on the text as it stands — the licensed route is open lane resolution before
the tally (the fields are machine-checkable facts of the pinned text, unlike origin, which is
judgement and is carried not reconciled); on successful resolution the census proceeds with no stop
class. The text names no terminal §4 class for a field disagreement that survives open resolution;
this is reported as an observed silence, analogous to the input-id-set case which DOES name one
("surviving that reconciliation stops the study under CENSUS_DENOMINATOR_DISPUTED"). It blocks no
declared verdict: the stop itself is exhibited, and no §3 outcome or §4 class depends on an
unresolvable field disagreement occurring. | YES (the stop is reachable; the filing is lane resolution,
with the no-terminal-class silence stated)

C3. rests_on NOT_COMPUTED.

R1  A claim with rests_on NOT_COMPUTED | Table A row 5: rs.md line 96 files REPRO_NO_DERIVATION_STATED
— no equation is stated, so no inputs are listed and the claim has no ledger records. compute emits
rests_on NOT_COMPUTED for it, and the rests_on tally carries a NOT_COMPUTED row. (Equally, any
included candidate with an empty input list: "an empty ledger is valid".) | §3: "rests_on is computed
and reported for every included claim that has at least one ledger record, whatever its outcome; a
claim with no ledger record carries rests_on NOT_COMPUTED, and the rests_on tally reports a
NOT_COMPUTED row"; §3 lane note: "an empty ledger is valid and every included candidate without a
record carries rests_on NOT_COMPUTED"; §9: compute "emits rests_on NOT_COMPUTED for every included
candidate with no ledger record". | YES

=====================================================================
THE SUSPICION, ANSWERED DIRECTLY: is CENSUS_COMPLETE reachable?
=====================================================================

Answer: REACHABLE.

What the suspicion gets right, as routing: §4.2 files CENSUS_PARTIAL whenever "at least one included
claim carries a non-arithmetic outcome (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT, REPRO_BLOCKED,
REPRO_NOT_EVALUABLE), or the denominator is zero", and §4.2 "takes precedence over CENSUS_COMPLETE";
§4's precedence order places CENSUS_PARTIAL immediately before CENSUS_COMPLETE. So YES — a single
blocked, absent-input, no-derivation-stated, or not-evaluable claim anywhere in the corpus forces
CENSUS_PARTIAL. The class is exactly as fragile as the suspicion says.

Why that is fragility and not unreachability: C0 asks whether an input exists that produces the
verdict. §4.1's conditions are: every included claim carries exactly one arithmetic-group outcome,
C6_AUDIT_SAMPLE=PASS, and the denominator is non-zero. No clause in the document requires any included
claim to have a blocked or absent input, an unstated derivation, or a timeout — those are facts about
the corpus, not rules of the document. The exhibited input (Table B, CENSUS_COMPLETE row): a corpus
whose every claim states its derivation and prints or closed-lists every input its recipe needs, with
every attempt completing inside the cap, and a clean audit — denominator N >= 1, all outcomes in
{REPRO_WITHIN_STATED_PRECISION, REPRO_FAILED}, C6_AUDIT_SAMPLE=PASS — routes §4.1 -> C6 PASS predicate
-> §4 precedence (no earlier limb holds) -> CENSUS_COMPLETE is filed. Whether a real corpus of many
papers contains at least one such blocking claim is an empirical property the run would measure;
"unreachable in practice" over a hypothetical real corpus is a frequency claim, not a design-space
block, and C0 licenses only the design-space question. (The document's own earlier C0 record, §10.3,
is consistent: both blind seats filed "CENSUS_COMPLETE: reachable". That record is history and is
cited here only as corroboration; the exhibition above stands on the operative text alone.)

Routing shown: REPRO_BLOCKED/REPRO_INPUT_ABSENT/REPRO_NO_DERIVATION_STATED/REPRO_NOT_EVALUABLE claim
present -> §4.2 -> CENSUS_PARTIAL (precedence over COMPLETE). No such claim present + audit PASS +
denominator > 0 -> §4.1 -> §4 precedence -> CENSUS_COMPLETE. Both branches exhibited with concrete
inputs above.

=====================================================================
UNREACHABLE VERDICTS
=====================================================================

NONE. Every per-claim outcome of §3 (six), every study-level class of §4 (eight), every named C6
failure path to CENSUS_AUDIT_FAILED (A1-A12 plus the receipt path A12b), the ORIG_SILENT complete-
alternative pass-through (A13), the seat-tally stops (T1-T4) with their §4 filings, and the rests_on
NOT_COMPUTED claim (R1) are exhibited above with concrete inputs and clause paths. There is no
UNREACHABLE verdict, so there is no blocking clause to quote.

One observed silence, reported rather than exhibited as a class (it is not a declared verdict and
changes no reachability answer): for a merge FIELD_DISAGREEMENTS that survives open lane resolution,
the text names no terminal §4 class (T4). The stop is reachable and its licensed route — lane
resolution before the tally — is exhibited; nothing declared in §3 or §4 depends on the unexhibited
case.

R3C2_C0_EXHIBITION_COMPLETE

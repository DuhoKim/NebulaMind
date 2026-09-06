ACCESS_SHA=22f01220a33f8695d18599176234c466fab36ff134b69af6c7d2cecdd978cb84
C0_REACHABILITY=PASS

# R3C2 C0 REACHABILITY EXHIBITION — V26 (living draft) — kimi seat, 2026-09-06

Scope of work: read `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md` from disk, in full (1,247 lines;
sha256 above, computed by `shasum -a 256` before anything else). No other file in this directory was
read or consulted. This exhibition does not gate the design and does not judge its physics; it asks
only whether every declared per-claim outcome of §3 and every study-level class of §4 CAN OCCUR —
whether a concrete input exists that the document's own clause path routes to that verdict.

Section 3 is treated exactly as it stands under the adopted ruling (option (c): one pass, two
tallies; `REPRO_AFTER_CHOICE` retired into the script-computed `rests_on` field). There is no held
clause. §3 therefore declares SIX per-claim outcomes and §4 declares EIGHT study-level classes.
Section 10 is history and binds nothing; it is cited nowhere below as authority.

All example corpora below are constructed exhibition inputs (toy papers with stated file:line), the
same form of input previous C0 rounds used. Reachability is existential: one licensed input per
verdict suffices.

=====================================================================
THE SUSPICION, ANSWERED DIRECTLY: CENSUS_COMPLETE — REACHABLE
=====================================================================

The suspicion: CENSUS_COMPLETE requires every included claim to carry an outcome from the arithmetic
group (§4.1: "every included claim carries exactly one outcome from the arithmetic group of §3, with
C6_AUDIT_SAMPLE=PASS"). In a real corpus of many papers, does a single blocked, absent-input, or
no-derivation-stated claim anywhere force CENSUS_PARTIAL and make CENSUS_COMPLETE unreachable in
practice?

Answer: REACHABLE. The suspicion is empirically plausible and structurally false.

Routing, in both directions:

(1) The blocking direction is real per corpus. §4.2 files CENSUS_PARTIAL when "at least one included
    claim carries a non-arithmetic outcome (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT,
    REPRO_BLOCKED, REPRO_NOT_EVALUABLE), or the denominator is zero", and §4's precedence
    ("R3C2_NO_CLASS, CENSUS_CONTROL_SPLIT, CENSUS_DENOMINATOR_DISPUTED, CENSUS_OUTCOME_DISPUTED,
    CENSUS_ORIGIN_DISPUTED, CENSUS_AUDIT_FAILED, CENSUS_PARTIAL, CENSUS_COMPLETE") gives
    CENSUS_PARTIAL precedence over CENSUS_COMPLETE. §3's per-claim precedence likewise files any
    claim that satisfies both a non-arithmetic terminal condition and an arithmetic one into the
    non-arithmetic class ("file the first in this order: REPRO_NO_DERIVATION_STATED, REPRO_BLOCKED,
    REPRO_INPUT_ABSENT, REPRO_NOT_EVALUABLE, then the arithmetic group"). So yes: one such claim in
    the corpus forces CENSUS_PARTIAL for that corpus.

(2) But nothing in §2 or §3 forces any claim to carry a non-arithmetic outcome. Each non-arithmetic
    class requires a specific textual defect in the paper itself: REPRO_NO_DERIVATION_STATED requires
    that the paper "states no equation or computational procedure that could produce it";
    REPRO_BLOCKED requires an input the paper does not print whose named source "is not an enumerable
    text pinned in R3C2_CORPUS_MANIFEST.md" or is one "at whose cited line the value does not
    machine-match"; REPRO_INPUT_ABSENT requires an input "neither printed nor traced to any named
    source"; REPRO_NOT_EVALUABLE requires the 120-second cap to be exceeded or machinery the lane
    lacks. A claim whose paper states its equation and prints every input (or prints a closed-list
    constant verbatim, or prints/imports a value that machine-matches in a pinned enumerable text at
    the cited line) has NONE of these defects, and §2 step 4's mechanical attempt then terminates in
    exactly one of the two arithmetic-group outcomes. Whether the real 89-text corpus contains such
    defects is the empirical question the census exists to answer; it is not a property the design
    imposes on every corpus. The only degenerate case the design itself names is §4.1's own guard:
    "A denominator of zero files CENSUS_PARTIAL with the empty enumeration named; no census is
    complete over nothing."

(3) The exhibiting input (row 9 of the table): a corpus whose two included claims both land in the
    arithmetic group, controls PASS in both seats, enumerations agree, no outcome or origin dispute,
    and the C6 audit runs to PASS (seed supplied and recorded with receipt T, both seals match, the
    recomputed selection matches, no OMISSION row, dispute rate 0% ≤ 10%, no MISMATCH). Every earlier
    class in the §4 precedence is then inapplicable, and §4.1's condition is met: CENSUS_COMPLETE is
    filed, with the full tally, its denominator, and the rests_on tally beside it ("two tallies from
    one pass").

So CENSUS_COMPLETE is reachable in principle; its reachability condition is exactly "a non-zero
denominator of included claims, every one of which carries an arithmetic-group outcome, with
C6_AUDIT_SAMPLE=PASS" — a condition on the corpus, not an impossibility in the document.

=====================================================================
EXHIBITION TABLE
=====================================================================

(A) §3 per-claim outcomes (six declared)

| # | verdict | concrete input | clause path | reachable |
|---|---------|----------------|-------------|-----------|
| 1 | REPRO_WITHIN_STATED_PRECISION | toyA.txt:42 prints "v = 30.0 km/s" from v = 2πr/T, with r = 4.78e8 km PRINTED (toyA.txt:40) and T = 1.000e8 s PRINTED (toyA.txt:41); mechanical attempt gives 30.03, which rounds to 30.0 at the printed precision (half away from zero) | §1 inclusion (numeral asserted as the paper's own result) → §2 steps 1–3 (extract; list inputs; both PRINTED) → §2 step 4 (attempt consumes every PRINTED/STANDARD record) → §3 REPRO_WITHIN_STATED_PRECISION ("the paper's number follows, within its own stated precision … Report both numbers"; no stated uncertainty, so "the reproduced value must round to the printed numeral at that precision, rounding half away from zero") → §2 step 5 record; both seats agree | YES |
| 2 | REPRO_FAILED | toyB.txt:17 prints "ρ = 1.0e-29 g/cm³" from ρ = 3H₀²/(8πG), with H₀ = 100 km/s/Mpc PRINTED (toyB.txt:15) and G printed verbatim as the closed-list string 6.67430e-11 (toyB.txt:16) → STANDARD; recomputed ρ = 1.9e-29 does not round to the printed numeral | §1 → §2.1–3 (H₀ PRINTED; G STANDARD — "a value the paper prints … on the closed list verbatim") → §2.4 attempt completes (inputs sufficient) → §3 REPRO_FAILED ("the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number … 'unreproduced from the stated inputs,' not 'error'") → §2.5 | YES |
| 3 | REPRO_BLOCKED | toyC.txt:30 prints "σ₈ = 0.85" derived using "the transfer function of Eisenstein & Hu (1998)"; that input's value is not printed and the named source is not an enumerable text of the manifest (limb i). Second input: toyD.txt:55 prints "w = −0.93" using "the prior from toyE.txt line 12"; toyE.txt IS enumerable and byte-verified but line 12 carries no matching numeral (limb ii) | §2 import rule: "If the named source is not enumerable or the value does not match there, file REPRO_BLOCKED under §3"; §2 machine floor: "A seat may not supply a value for an ABSENT or BLOCKED input. Encountering one ends that claim's attempt." → §3 REPRO_BLOCKED ("names a source … that either is not an enumerable text pinned in R3C2_CORPUS_MANIFEST.md or is an enumerable pinned text at whose cited line the value does not machine-match … Name the input and the source"); C3 records status BLOCKED, origin IMPORTED, ORIG_CITATION at the claiming paper's naming sentence, no value. §3 precedence places BLOCKED ahead of ABSENT, so an input satisfying both files here | YES |
| 4 | REPRO_NOT_EVALUABLE | toyH.txt:40 prints "Σ = 412" from a stated symbolic integral; launched as /usr/bin/python3 -E r3c2_timeout.py 120.0 -- <command>, the simplification exceeds the deadline → wrapper prints SYMBOLIC_TIMEOUT, exits 124. Second input: toyI.txt:12 prints a numerical MHD result requiring a 3-D MHD solver the lane does not have → MACHINERY_UNAVAILABLE | §9 wrapper contract ("on the deadline prints SYMBOLIC_TIMEOUT and exits 124 — the reportable outcome") → §3 REPRO_NOT_EVALUABLE ("the arithmetic could not be completed within the 120-second cap, or requires machinery this lane does not have. Print SYMBOLIC_TIMEOUT … or MACHINERY_UNAVAILABLE … and the point reached"); inputs all PRINTED and derivation stated, so no earlier precedence class applies | YES |
| 5 | REPRO_NO_DERIVATION_STATED | toyF.txt:71 prints "the host mass is 3.1e14 M☉" as its own result; the only accompanying sentence is "the mass was obtained from our lensing pipeline" — a procedure named but not specified | §1 inclusion (printed numeral asserted as the paper's own result) → §2 step 1 finds no equation to extract → §3 REPRO_NO_DERIVATION_STATED ("the paper prints the claim as its own result but states no equation or computational procedure that could produce it … A procedure named but not specified … states no computational procedure … file this class and name the passage"); first in §3 precedence | YES |
| 6 | REPRO_INPUT_ABSENT | toyG.txt:23 prints "D_L = 780 Mpc" from D_L = (1+z)·r, with z = 0.17 PRINTED (toyG.txt:22) but r neither printed anywhere in the paper nor traced to any named source | §2 step 3 classify ABSENT ("neither printed nor traced to any named source") → §2 machine floor ("A seat may not supply a value for an ABSENT … input. Encountering one ends that claim's attempt.") → §3 REPRO_INPUT_ABSENT ("an input the equation needs is ABSENT from the paper … so the attempt stops there. Name the input."); distinct from REPRO_BLOCKED, which requires a named source | YES |

`REPRO_AFTER_CHOICE` is not a §3 outcome under the settled wording (retired at V10 by the
principal's ruling adopting option (c)); it has no row because nothing declares it.

(B) §4 study-level classes (eight declared)

| # | class | concrete input | clause path | reachable |
|---|-------|----------------|-------------|-----------|
| 7 | CENSUS_COMPLETE | Corpus {toyA, toyB}: exactly two included claims — toyA.txt:42 files REPRO_WITHIN_STATED_PRECISION, toyB.txt:17 files REPRO_FAILED; denominator 2; controls C1–C5b PASS in both seats; the two enumerations agree; no outcome or origin dispute; C6 audit runs to PASS (external seed supplied and recorded with receipt T; stage-1 and re-derivation seals match; recomputed selection matches; no OMISSION; dispute rate 0/2 = 0% ≤ 10%; no MISMATCH) | §4.1: "every included claim carries exactly one outcome from the arithmetic group of §3, with C6_AUDIT_SAMPLE=PASS"; denominator non-zero, so the zero-denominator guard does not fire; no earlier class in the §4 precedence applies ("Once a stop class applies, later limbs are unreached" — none does); file CENSUS_COMPLETE; "Report the full tally with its denominator, and the rests_on tally beside it — two tallies from one pass" | YES |
| 8 | CENSUS_PARTIAL | Corpus {toyA, toyG}: toyA.txt:42 files REPRO_WITHIN_STATED_PRECISION, toyG.txt:23 files REPRO_INPUT_ABSENT (row 6). Second input: a corpus whose every enumerated candidate is excluded (equation numbers, dates, AUTHOR_SPECIFIED_INPUT rows) → denominator zero | §4.2: "at least one included claim carries a non-arithmetic outcome (REPRO_NO_DERIVATION_STATED, REPRO_INPUT_ABSENT, REPRO_BLOCKED, REPRO_NOT_EVALUABLE), or the denominator is zero … INCONCLUSIVE, and it takes precedence over CENSUS_COMPLETE"; §4.1's guard: "A denominator of zero files CENSUS_PARTIAL with the empty enumeration named"; audit passed, so no earlier class applies | YES |
| 9 | CENSUS_AUDIT_FAILED | See the five C6 paths exhibited in section (D) below, plus the receipt path: the sealed audit cannot reproduce sampled claim toyB.txt:17 (auditor re-derives ρ = 1.9e-29 and files REPRO_FAILED where the sealed candidate file carries REPRO_WITHIN_STATED_PRECISION → MISMATCH); or receipt P/T missing or a re-hash mismatch after opening | §4.3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the cause named), or the receipt verification of the seal fails. No tally is filed; report which"; C6: "Any outcome the audit cannot reproduce, or any ledger incompleteness, files CENSUS_AUDIT_FAILED"; §7: "Any missing receipt or mismatch files CENSUS_AUDIT_FAILED (§4, whose definition now names this case)" | YES |
| 10 | R3C2_NO_CLASS | (i) Pre-dispatch: the builder's forbidden-list assertion finds a surviving string → C4_PACKET_REDACTED=FAIL, "the packet is not written … the study does not proceed on a hand-checked copy". (ii) In-run: both seats' ledgers carry an out-of-schema field (e.g. a seat-written root_origins) → validate exits non-zero in both seats, one retry each, FAIL again. (iii)–(v) The C1B_BATCH_COVERAGE, JOIN and C5C_NO_FALLBACK stops exhibited in section (E), when the FAIL persists in every seat after two tries | §4.4: "a control among C0 through C5b fails in every seat that attempted it after two attempts; a packet or seat-isolation failure before dispatch files this class. A C6 audit failure or a seal-receipt failure files CENSUS_AUDIT_FAILED, not this class." First in §4 precedence | YES |
| 11 | CENSUS_DENOMINATOR_DISPUTED | (i) Limb A: seat A includes candidate toyF.txt:71 ("3.1e14 M☉"); seat B excludes it as AUTHOR_SPECIFIED_INPUT; two reconciliation attempts fail. (ii) Input-list limb: seat A lists three inputs for claim toyA.txt:42, seat B lists two; merge exits 1; the one C3 reconciliation against the stated equation fails to resolve the difference | §1: "disagreement on any candidate that survives two reconciliation attempts stops the study under CENSUS_DENOMINATOR_DISPUTED (§4)"; §4.5: "the two enumerations disagree after two reconciliation attempts, or the two seats' input lists for the agreed claims disagree after the one C3 reconciliation. The census does not proceed; the disputed candidates or inputs are listed"; C3 lane block: "if merge exits 1 … an input-set difference surviving that reconciliation stops the study under CENSUS_DENOMINATOR_DISPUTED (§4)" | YES |
| 12 | CENSUS_OUTCOME_DISPUTED | toyJ.txt:33 prints "M = 2.5e14"; seat A reproduces 2.54e14 → files REPRO_WITHIN_STATED_PRECISION (rounds to 2.5e14); seat B reproduces 2.56e14 → files REPRO_FAILED (rounds to 2.6e14); the one reconciliation against the printed numeral and the stated-precision rule leaves the arithmetic split standing | §2 step 5: "a disagreement surviving that reconciliation files CENSUS_OUTCOME_DISPUTED (§4)"; §4.6: "the two seats' filed per-claim outcomes on an agreed included claim differ after one reconciliation against the printed numeral and the stated-precision rule of §3. The census does not proceed; the claim is listed with both seats' outcomes, both number pairs, and the step each seat reached" | YES |
| 13 | CENSUS_ORIGIN_DISPUTED | 10 included claims; on toyK.txt:14's sentence "we take the spectral index from our earlier calibration", seat A files IMPORTED (ORIG_CITATION), seat B files UNDECLARED (ORIG_SILENT); a second claim's input splits the same way → 2/10 = 20% > 10% | §4.7: "the two seats' independent origin classifications disagree on inputs affecting more than 10% of included claims. The census does not proceed; every disputed input is listed with both seats' classification and both quotations"; C6: "it is not reconciled. Above 10% of included claims, CENSUS_ORIGIN_DISPUTED" (the > 10% threshold means exactly 10% does not file it) | YES |
| 14 | CENSUS_CONTROL_SPLIT | Seat A's C5 harness run: all five commands exit 0 → C5_HARNESS_PINNED=PASS. Seat B's fifth command prints ERROR=<path> and exits 1 on an unreadable file → FAIL; two attempts each; the split survives. Split variants for C1B_BATCH_COVERAGE, JOIN and C5C_NO_FALLBACK in section (E) | §4.8: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not adopt the passing seat's result"; second in §4 precedence, so it is filed only when R3C2_NO_CLASS (fail in every seat) does not apply | YES |

(C) Reachability stated per verdict: every row above is marked YES. No §3 outcome and no §4 class
is UNREACHABLE under the text as it stands. See the final section.

=====================================================================
(D) V26 REQUIRED EXHIBITIONS — CENSUS_AUDIT_FAILED THROUGH EACH C6 PATH
=====================================================================

D1. Sealed-INCLUDED passage absent from the auditor's enumeration (omission, direction 1).
    Input: the sealed joined candidate file includes passage (toyA.txt:42, "30.0"); the auditor's
    complete independent enumeration of all enumerable manifest texts produces candidate and
    exclusion ledgers in which the passage key (toyA.txt, line 42, "30.0") does not appear at all.
    Path: C6 builds "one completeness row per passage key (file, line, numeral) in the UNION of the
    sealed and the auditor's enumerations" and files OMISSION — "a sealed INCLUDED passage absent
    from the auditor's enumeration … each is ledger incompleteness and files CENSUS_AUDIT_FAILED".
    C6_AUDIT_SAMPLE ≠ PASS ("no row is an omission" fails) → §4.3 CENSUS_AUDIT_FAILED. REACHABLE.

D2. Auditor-listed passage absent from the sealed ledgers (omission, direction 2).
    Input: the auditor lists passage (toyM.txt:8, "2.725") (whether included or excluded); neither
    the sealed candidate file nor the sealed exclusion ledger names that passage key.
    Path: C6 — "a passage the auditor lists (included OR excluded) that the sealed ledgers omit —
    each is ledger incompleteness and files CENSUS_AUDIT_FAILED" → §4.3. REACHABLE.

D3. Dispute rate above 10%.
    Input: sealed included denominator 20; three passage keys are AUDIT_INCLUSION_DISPUTED (two
    passages both sides list but dispose differently — e.g. seat-ledgers include toyF.txt:71 while
    the auditor excludes it as AUTHOR_SPECIFIED_INPUT — plus one sealed-EXCLUDED passage absent from
    the auditor's enumeration). 3/20 = 15% > 10%.
    Path: C6 — these "are AUDIT_INCLUSION_DISPUTED, listed with both dispositions and counted; above
    10% of the sealed included denominator the audit files CENSUS_AUDIT_FAILED; at or below it the
    count is reported" → §4.3. (Boundary: exactly 10%, e.g. 2/20, is reported, not failed — "at or
    below it".) REACHABLE.

D4. Seedless selection.
    Input: receipt T exists, but the external custodian never supplies the 64-lowercase-hex seed, so
    no seed is recorded with the receipt. Variant: the stage-1 seal (audit seal-enumeration) was
    never recorded because census over the auditor's ledgers failed, and `audit select` "refuses
    without the stage-1 seal".
    Path: C6 — "If the seed is not supplied and recorded with the receipt, the audit does not run,
    C6_AUDIT_SAMPLE=NOT_RUN, and the study files CENSUS_AUDIT_FAILED with the missing seed named";
    §4.3 also covers the variant directly: "does not run to PASS for any cause (the cause named)".
    REACHABLE.

D5. Zero denominator with passages present.
    Input: the sealed candidate file carries zero included claims, while the auditor's enumeration
    lists at least one passage (or the sealed exclusion ledger does — any passage on either side).
    Path: C6 — "A sealed denominator of zero with any passage on either side fails" →
    C6_AUDIT_SAMPLE ≠ PASS → §4.3 CENSUS_AUDIT_FAILED. Contrast for completeness: a sealed
    denominator of zero with NO passage on either side does not trip this clause and files
    CENSUS_PARTIAL under §4.1's guard instead — the two clauses partition the zero-denominator
    space without overlap. REACHABLE.

(Supplementary paths to the same class, also exhibited: a MISMATCH on an audited claim's outcome,
printed/reproduced values, or a re-classified input origin — "C6_AUDIT_SAMPLE=PASS only if … no
audited claim or origin is MISMATCH"; and the seal-receipt path — §4.3 "or the receipt verification
of the seal fails", §7 "Any missing receipt or mismatch files CENSUS_AUDIT_FAILED".)

=====================================================================
(E) V26 REQUIRED EXHIBITIONS — SEAT-TALLY STOPS UNDER C1B AND C5C, AND THEIR §4 FILINGS
=====================================================================

E1. C1B_BATCH_COVERAGE=FAIL stops the seat's tally.
    Input: the pinned partition assigns toyN.txt to batch 7; in the batch-7 session the bytes of the
    seat's copy of toyN.txt do not verify against its manifest row (digest mismatch) — or a batch
    report omits the packet's ACCESS_SHA line — or some manifest text is owned by no batch (or two).
    Path: C1B — "C1B_BATCH_COVERAGE=PASS iff every manifest text is owned by exactly one batch,
    every owned text's bytes verify against its manifest row, and every batch report prints the
    packet's ACCESS_SHA … Either FAIL stops the seat's tally." §4 filing: "a FAIL in every seat that
    tries it, after two tries, files R3C2_NO_CLASS; a surviving fail/pass split files
    CENSUS_CONTROL_SPLIT; an unreached check is NOT_RUN." Both filings REACHABLE: both-seats-fail →
    R3C2_NO_CLASS (row 10); one-seat-fail/one-seat-pass after two tries → CENSUS_CONTROL_SPLIT
    (row 14).

E2. JOIN=FAIL stops the seat's tally.
    Input: in the LIMB-A chain, the sealed candidates_b5.json names a predecessor seal that does not
    match batch 4's recorded seal — the "ordered predecessor chain … from a root with no predecessor"
    is broken. Variants: a candidate whose claim id's <owned file># prefix belongs to a different
    batch; an evidence source_file that is not a manifest text; a duplicated identifier; a
    derived_from cycle. Limb-B variant: a limb-B seal chain not bound to the agreed limb-A seals.
    Path: C1B — "JOIN=PASS iff every seal matches, the ordered predecessor chain is intact from a
    root with no predecessor, every candidate and ledger claim is owned by its batch, every evidence
    source is a manifest text, identifiers are unique and every derived_from resolves acyclically.
    Either FAIL stops the seat's tally." §4 filing: same C1B sentence as E1 — both seats fail after
    two tries → R3C2_NO_CLASS; surviving split → CENSUS_CONTROL_SPLIT. REACHABLE.

E3. C5C_NO_FALLBACK=FAIL stops the tally pre-tally.
    Input: the lane owner checks the printed, session-identified provider log for every session of a
    seat's batch sequence; session b3's log is missing, or the b3 log contains a fallback entry (the
    session left its primary provider mid-batch).
    Path: §9 — "the no-fallback control C5C_NO_FALLBACK=PASS|FAIL|NOT_RUN requires a printed,
    session-identified provider log for every session — a missing log or any fallback entry is FAIL,
    an unreached check NOT_RUN — a pre-tally control under the R3C2_NO_CLASS and
    CENSUS_CONTROL_SPLIT rules, checked by the lane owner." §4 filing: FAIL in every seat that
    attempted it after two attempts → R3C2_NO_CLASS (§4.4); fail in one seat, pass in the other
    after two attempts → CENSUS_CONTROL_SPLIT (§4.8). REACHABLE.

=====================================================================
(F) V26 REQUIRED EXHIBITIONS — rests_on NOT_COMPUTED; CROSS-CLAIM DISPUTED PROPAGATION
=====================================================================

F1. A claim with rests_on NOT_COMPUTED.
    Input: claim toyF.txt:71 (row 5) files REPRO_NO_DERIVATION_STATED; stating no equation, it
    yields no input records, so the joined input ledger contains no record whose claim_id names it
    (an empty claim ledger). After both seats exit, the lane owner runs r3c2_lane_tools.py merge
    then compute; compute "emits rests_on NOT_COMPUTED for every included candidate with no ledger
    record" (§9), per §3: "an empty ledger is valid and every included candidate without a record
    carries rests_on NOT_COMPUTED" and "a claim with no ledger record carries rests_on NOT_COMPUTED,
    and the rests_on tally reports a NOT_COMPUTED row." The rests_on tally therefore carries the
    claim with NOT_COMPUTED beside its non-arithmetic reproduction outcome — the two tallies from
    one pass. REACHABLE.

F2. A dependent claim DISPUTED through another claim's input.
    Input: claim X (toyL.txt:9) has input a = 3, PRINTED at toyL.txt:7; seat A classifies its origin
    CHOSEN (ORIG_CHOICE_STATED), seat B IMPORTED (ORIG_CITATION) — the merged record carries
    origin_alt/origin_evidence_alt (a disputed record). Claim Y (toyL.txt:40) has input b, origin
    DERIVED, whose derived_from list names a's input id — a cross-claim dependency, which the schema
    represents (derived_from names input ids; validate fails only an id that names no record, a
    cycle, or a DERIVED record with none).
    Path: §3 lane rule — "a claim whose dependency graph reaches a disputed record — in any claim —
    is itself DISPUTED with both values"; §9 — compute "propagates a dispute through the whole
    dependency graph across claims"; C3 lane block — "a disputed pair is computed under both origins
    and marked DISPUTED"; C6 — "the rests_on tally reports a DISPUTED row." Both X and Y print
    rests_on as a pair (computed under CHOSEN and under IMPORTED) marked DISPUTED. REACHABLE.

=====================================================================
UNREACHABLE VERDICTS — NONE
=====================================================================

Every per-claim outcome of §3 (six of six) and every study-level class of §4 (eight of eight) is
exhibited above with a concrete input and a clause path through the document as it stands. The
additional V26 conditions — CENSUS_AUDIT_FAILED through each of the five C6 paths, the seat-tally
stops under C1B_BATCH_COVERAGE / JOIN / C5C_NO_FALLBACK with both of their §4 filings
(R3C2_NO_CLASS and CENSUS_CONTROL_SPLIT), rests_on NOT_COMPUTED, and cross-claim DISPUTED
propagation — are likewise each exhibited.

No declared verdict is UNREACHABLE, so there is no blocking clause to quote. The direct answer to
the named suspicion is stated in the opening section: CENSUS_COMPLETE is REACHABLE; a blocked,
absent-input, or no-derivation claim forces CENSUS_PARTIAL only for a corpus that contains one, and
no clause forces every corpus to contain one.

C0_REACHABILITY=PASS

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V26_KIMI_COMPLETE

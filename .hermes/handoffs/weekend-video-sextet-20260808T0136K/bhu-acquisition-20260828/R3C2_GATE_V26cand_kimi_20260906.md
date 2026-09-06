ACCESS_SHA=f4edb5145b5c150c43a6550b30f0beca1d08bf4675305383e7860c3657f951fd
PACKET_SHA=5fc8d8349450af40cb73c1b6215404b755055242f9785e280c328619cba7f0d3
GATE=PREREG_SOUND_WITH_REPAIRS
LEAK=content-level only: the corpus is cosmology (the Planck-2018 STANDARD list) and the packet anticipates non-reproductions and chosen-input disputes; no hypothesis, comparison model or preferred tally inferable
CONSEQUENCE_VISIBLE=NO
ORIGIN_PURPOSE=CANNOT_STATE
C5_EXECUTABLE_UNDER_SCOPE=YES
NO_MASKED_STAGE=YES
CANDIDATE_DIFF_ONLY=YES

Seat: kimi. Date: 2026-09-06. Master gated: R3C2_V26_INTEGRATED_CANDIDATE_UNADOPTED_20260906.md (an INTEGRATED
CANDIDATE, judged as the document it is). Packet gated: r3c2_seat_packet_v26_candidate/R3C2_SEAT_PACKET.md.
The packet was read and Q5/Q6/Q3 were answered BEFORE the master was opened. Section 10 of the master was
read as history and binds nothing below; no gate files were consulted. Working directory for every run:
the lane directory stated in the brief, plus my own scratch _tmp_R3C2_V26CAND_GATE_kimi/ for fixtures.

=====================================================================
STEP 1 — answers from the PACKET ALONE (given before the master was read)
=====================================================================

Q5 (asked third, answered first). CAN YOU TELL, FROM THE PACKET ALONE, THAT ANY OUTCOME IS MORE
CONSEQUENTIAL THAN ANY OTHER? No sentence does. I read the whole packet looking for any sentence that
makes one filed outcome worse, better, costlier or more dangerous than another, to the lane or to anyone.
The only consequence-bearing sentence in the packet is §11: "No tier, warrant token, standing or stamp
moves." — and it equalises: nothing moves whatever the outcome. The stop classes say the study "does not
proceed" or "stops" (procedural), and §4.2 says "INCONCLUSIVE, and it takes precedence over
CENSUS_COMPLETE" — a filing precedence, not a stake: it does not say what either class costs anyone.
CONSEQUENCE_VISIBLE=NO.

Q6 (asked second). CAN YOU STATE, FROM THE PACKET ALONE, WHAT THE RECORDED `origin` OF AN INPUT IS FOR?
I cannot state what it is FOR. The packet tells me exactly how origin is handled and checked, and
explicitly that the verdict does not consume it — §3: "Arithmetic consumes records according to status
PRINTED or STANDARD" over every PRINTED record "whatever its origin"; "origin is one recorded attribute of
a ledger record, beside status, value, source_file and source_line". It tells me both seats classify it
independently, that disagreements are filed ORIGIN_DISPUTED and stop the study above 10% of included
claims (CENSUS_ORIGIN_DISPUTED), and that the C6 auditor "re-classifies each of its inputs' origin from
the pinned sources". Those are checks ON origin. No packet sentence states what the study does WITH it —
no tally by origin, no stratum, no comparison, no conclusion that reads it. ORIGIN_PURPOSE=CANNOT_STATE.
(The mechanical checks are statable; the purpose is not. That is the floor the principal's 18:52 ruling
accepted, and the packet holds it.)

Q3 (the hypothesis-reachability test). WHAT CAN YOU INFER ABOUT WHAT THE LANE EXPECTS OR HOPES THE CENSUS
WILL SHOW? Adversarial reconstruction attempted; here is everything the packet leaks, graded:
  (i) The corpus is cosmology/astrophysics: C3's closed STANDARD list prints the Planck 2018
      TT,TE,EE+lowE+lensing baseline (H0 67.36, Omega_m 0.3153, ...). Content, not consequence — the seat
      must read these sources anyway.
  (ii) The lane anticipates that some claims will NOT reproduce, and pre-commits to non-accusatory
      wording: §3 REPRO_FAILED — 'Wording: "unreproduced from the stated inputs," not "error."' A
      defensive framing guard; it constrains how a seat writes a negative, not whether it finds one.
  (iii) The chosen-input dispute is anticipated: §3 REPRO_INPUT_ABSENT — "Distinct from a claim whose
      inputs the paper DOES state, chosen or not — that claim is attempted and files
      REPRO_WITHIN_STATED_PRECISION or REPRO_FAILED." Someone fought over this before; the packet
      pre-answers it. Again a rule, not a hope.
  (iv) The design prefers under-claiming: CENSUS_PARTIAL is "INCONCLUSIVE, and it takes precedence over
      CENSUS_COMPLETE"; CENSUS_COMPLETE requires every included claim in the arithmetic group AND
      C6_AUDIT_SAMPLE=PASS. Reaching COMPLETE is deliberately hard. That is a posture about certainty,
      not an expected tally.
  (v) The 10% dispute tolerances (CENSUS_ORIGIN_DISPUTED, C6) imply disagreement is expected to be
      nonzero but bounded. Procedural.
  What I could NOT reconstruct: any hypothesis the census tests, any comparison model, any preferred
  outcome, any "pattern", any sentence mapping a tally to a conclusion about the world. The packet's §1
  asks one question ("does the paper's own number follow from the paper's own recipe applied to the
  inputs it states") and §11 says nothing moves. My independent grep of the packet for pattern / ΛCDM /
  custody names / engine names / consequence words (expectation, refute, consequential, invisible,
  favourable, unfavourable, stake, prior, tempting, warn) and for rests_on / DERIVED_ONLY / gate / sign
  returned zero hits; the only substring hits were "freeze" inside C0's own procedural name ("run BEFORE
  the freeze") and "assigned" matching "sign". LEAK line above is the total of it.

=====================================================================
STEP 2 — the master, judged section by section (1,2,3,4,5,6,7,9,11)
=====================================================================

---------------------------------------------------------------------
1. OUTCOME CLASSES (Q1 answered here)
---------------------------------------------------------------------
Per-claim: six outcomes plus a separate exclusion ledger (exclusions are NOT per-claim outcomes).
Exactly-one filing with a total precedence: REPRO_NO_DERIVATION_STATED, REPRO_BLOCKED,
REPRO_INPUT_ABSENT, REPRO_NOT_EVALUABLE, then the arithmetic group (exactly
REPRO_WITHIN_STATED_PRECISION and REPRO_FAILED). I could not construct a real claim fitting two classes
after the precedence is applied, nor one fitting none: a printed own-result numeral with a stated recipe
lands in the arithmetic group; without a recipe, NO_DERIVATION; with an unprinted named-source input
unverifiable in the manifest, BLOCKED; with an untraced input, ABSENT; over the 120-second cap or missing
machinery, NOT_EVALUABLE. Co-occurrence is real (an absent input on a claim with no stated procedure) and
the precedence resolves it to exactly one.
Study-level: eight classes with a total precedence (R3C2_NO_CLASS, CENSUS_CONTROL_SPLIT,
CENSUS_DENOMINATOR_DISPUTED, CENSUS_OUTCOME_DISPUTED, CENSUS_ORIGIN_DISPUTED, CENSUS_AUDIT_FAILED,
CENSUS_PARTIAL, CENSUS_COMPLETE). I could not construct a tally fitting two after precedence, nor one
fitting none: control failure in every attempted seat and pre-dispatch failures (R3C2_NO_CLASS), one-seat
failure (CONTROL_SPLIT), enumeration or input-list disagreement (DENOMINATOR_DISPUTED), per-claim outcome
split (OUTCOME_DISPUTED), origin split >10% (ORIGIN_DISPUTED), audit not reaching PASS for any cause or
seal-receipt failure (AUDIT_FAILED), any non-arithmetic outcome or zero denominator (PARTIAL), else
COMPLETE. INCONCLUSIVE is genuinely reachable and named: CENSUS_PARTIAL is declared "INCONCLUSIVE, and it
takes precedence over CENSUS_COMPLETE", reachable by a single REPRO_NOT_EVALUABLE or a zero denominator.

Q1 (direct): DOES §3's DEFINITION, AS WRITTEN UNDER OPTION (c), MAKE EVERY DECLARED OUTCOME REACHABLE AND
KEEP THE REPRODUCTION QUESTION DECIDABLE? YES. Hardest cases traced, each to exactly one outcome and one
rests_on value:
  - Printed-but-chosen input: "we choose β = 1/929.25 for this calculation", printed. As a candidate
    passage β's own numeral is excluded (AUTHOR_SPECIFIED_INPUT, counted beside the denominator); as an
    INPUT to another claim it is status PRINTED, origin CHOSEN (ORIG_CHOICE_STATED, machine-matched
    quotation); the arithmetic consumes it (consumption is by status, "whatever its origin"); the claim
    files REPRO_WITHIN_STATED_PRECISION or REPRO_FAILED by the mechanical stated-precision/uncertainty
    rules; lane-side compute files rests_on = USES_CHOSEN. One outcome, one rests_on.
  - A fitted parameter the paper states: "our fit gives λ = 2.7" — PRINTED/FITTED (ORIG_FIT_STATED);
    consumed; rests_on USES_FITTED. One disposition.
  - An imported value: "We adopt beta = 0.012 from B (2020)" where B is an enumerable manifest text whose
    cited line carries the token — PRINTED/IMPORTED, ORIG_CITATION satisfied at the CLAIMING paper's
    naming sentence; consumed; rests_on USES_IMPORTED. Exercised live (fixture A1:
    C3_NO_SUBSTITUTION=PASS). If the source is not enumerable or the token does not match: REPRO_BLOCKED,
    record BLOCKED/IMPORTED with no value, never consumed. If the source's own line says "we choose":
    still exactly one disposition — see Q7(e).
Decidability: the stated-precision rule (rounding half away from zero), the stated-uncertainty rule
(|reproduced − printed| ≤ stated uncertainty, once), and the asymmetric rule (half-width on the side the
reproduced value falls) are mechanical; the class boundary between WITHIN and FAILED does not require
judgement. The tension that failed four earlier rounds — admissibility gating the attempt versus
reachability of the chosen-input class — is gone because option (c) consumes by status and records
provenance beside the verdict. Q1=YES.

---------------------------------------------------------------------
2. CONTROLS (Q2 answered here)
---------------------------------------------------------------------
Every control names an exact code with PASS|FAIL|NOT_RUN: C0_REACHABILITY, C1_DENOMINATOR_PRINTED,
C1B_BATCH_COVERAGE, C2_INPUT_LEDGER, C3_NO_SUBSTITUTION, C4_SEAT_ISOLATION, C4_PACKET_REDACTED,
C5_HARNESS_PINNED, C5B_NO_CROSS_LANE, C6_AUDIT_SAMPLE. Unreached controls are NOT_RUN ("Controls in an
unreached limb are NOT_RUN, never passes"; §4's precedence makes later limbs unreached once a stop class
applies).
Pass-by-assertion audit: C1, C2, C3, C5, C6 are artefact-backed by printed script runs ("a token asserted
without the printed run is FAIL"; C6 "only if the artefact exists and is printed..."). C0's artefact is
the two-seat exhibition table. C4 and C5b are, by the document's own words, self-report controls: "C4 and
C5b are self-report controls and do not themselves bound automatic code access"; PASS "means only that
the list contains no outside path; it makes no claim that the list is complete." So yes, C4/C5b can be
passed by an incomplete self-report — and the document says exactly that, and backs the gap with the
kernel sandbox profile (r3c2_seat_sandbox.sb, digest verified on disk below) whose probes are printed in
the dispatch record. The limit is stated, not implied away.

Q2 (direct): IS THE PROVENANCE FIELD CHECKABLE RATHER THAN ASSERTED? YES, to a stated machine floor, with
the catch path named. Attack executed: ledger record fxA/ledger_origin_attack.json — paperD.txt line 3
"We use H0 = 67.4 from Planck (2018)." filed origin CHOSEN / ORIG_CHOICE_STATED with that sentence as the
verbatim. Wrong but plausible: the precedence rule says a sentence naming an external source for the
value is a citation whatever else it says, so ORIG_CITATION→IMPORTED is the correct filing. Live result:
`validate fxA/ledger_origin_attack.json fxA fxA/candidates.json` → C3_NO_SUBSTITUTION=PASS, exit 0. The
machine passes it, exactly as the master states it will ("A reason code that matches its quotation but
misapplies the precedence is caught only by the second seat's independent classification and the C6
re-classification, never by the machine"). The catch: (1) the second seat classifies independently under
the same precedence and files IMPORTED — disagreement is filed ORIGIN_DISPUTED, reported with both
quotations, never reconciled, and above 10% of included claims stops the study as
CENSUS_ORIGIN_DISPUTED; (2) the C6 auditor re-classifies the origin from the pinned sources and a
MISMATCH fails C6_AUDIT_SAMPLE → CENSUS_AUDIT_FAILED. If every reader misclassifies identically, the
record stands — the document states that floor rather than hiding it. What the machine DOES catch (also
exercised): a cross-file import misfiled as CHOSEN is refused at intake ("such a record must be IMPORTED
with ORIG_CITATION"), a STANDARD value off the closed list fails, a verbatim not at the cited line fails,
a BLOCKED record without IMPORTED/ORIG_CITATION fails, an ABSENT/BLOCKED record carrying a value fails, a
seat-authored field outside the schema fails, a derived_from cycle or dangling id fails, a DERIVED record
with no parents fails.

DEFECT F1 (NON-COSMETIC — changes a control's passability). Verbatim, C2 (master line 288, packet line
203): "validated by `/usr/bin/python3 -E r3c2_ledger_tools.py validate <ledger.json> .` run from the
printed seat working directory (`.` is the sole allowed `sources_dir`)". Verbatim, C3 (master line 355,
packet line 258): "Each seat runs `/usr/bin/python3 -E r3c2_ledger_tools.py validate <ledger.json>
<sources_dir>` with the placeholders resolved". Defect: the tool the candidate itself pins in §3 (sha256
9e916b81e296f890…, of which §3 says "`validate` takes the candidate file as its third argument") FAILS
the printed 2-arg command on every ledger containing a PRINTED record. Demonstrated live:
`validate fxA/ledger_pass.json fxA` → "FAIL: paperA.txt#i1: PRINTED record needs the candidate file to
bind claim paperA.txt#c1 to its claiming paper", C3_NO_SUBSTITUTION=FAIL, exit 1; same on the joined
batch ledger. Every real census ledger contains PRINTED records, so C2 and C3 cannot PASS as printed, and
C4(iii) authorises only "the commands this document prints verbatim" — a seat may not add the argument on
its own authority. Exact replacement:
  - C2: "validated by `/usr/bin/python3 -E r3c2_ledger_tools.py validate <ledger.json> .
    <candidates.json>` run from the printed seat working directory (`.` is the sole allowed
    `sources_dir`; the third argument is the seat's joined candidate file of C1)"
  - C3: "Each seat runs `/usr/bin/python3 -E r3c2_ledger_tools.py validate <ledger.json> <sources_dir>
    <candidates.json>` with the placeholders resolved"
(The defect fails loudly, never silently; it makes no outcome unreachable and no control passable by
assertion. That is why this gate is SOUND_WITH_REPAIRS rather than UNSOUND.)

DEFECT F2 (COSMETIC). Verbatim, §3 (master line 177-178, packet line 113-114): "with file, line, the
numeral, and which excluded kind it is (equation number, reference number, page/line number, date, or
attributed-not-derived)." The parenthetical names five kinds; the operative token list immediately
following names six (`AUTHOR_SPECIFIED_INPUT` included), §1 names six, and `census` enforces six.
Replacement: "(equation number, reference number, page/line number, date, attributed-not-derived, or
author-specified input)" — or delete the parenthetical. Changes no class, control, reachability or
conclusion. COSMETIC.

DEFECT F3 (COSMETIC). Verbatim, C1B: "`JOIN=PASS` iff every seal matches, ... Either FAIL stops the
seat's tally. `C1B_BATCH_COVERAGE=PASS|FAIL|NOT_RUN`." JOIN is a named predicate with a stop consequence
but no `PASS|FAIL|NOT_RUN` token line of its own; the generic NOT_RUN rule covers it. Replacement: append
"`JOIN=PASS|FAIL|NOT_RUN`." COSMETIC.

---------------------------------------------------------------------
3. CIRCULARITY
---------------------------------------------------------------------
Inclusion cannot be quietly steered: the §1 rule is applied by two independent seats with tolerance zero
(disagreement after two reconciliations stops the study), and the candidate's new C6 adds a third
independent seat, on a different engine, enumerating every enumerable text with no seat ledger in its
dispatch inventory, sealed first-write before any selection; the comparison runs over the UNION of
passage keys and any omission in either direction files CENSUS_AUDIT_FAILED (exercised live: fixture B6,
"FAIL: COMPLETENESS audit_included_absent_from_sealed", C6_AUDIT_SAMPLE=FAIL, exit 1).
Exclusion cannot bury a contrary claim: kinds are predeclared, numeral and line retained ("excluded from
judgement, retained in the record, never discarded"), the AUTHOR_SPECIFIED_INPUT count prints beside the
denominator, both seats must file the same exclusion (else DENOMINATOR_DISPUTED), and the auditor's union
comparison turns a sealed exclusion the auditor includes into AUDIT_INCLUSION_DISPUTED (counted; >10% of
the sealed denominator fails the audit) and a sealed exclusion the auditor never listed into a counted
dispute as well. A kind-label disagreement with the same disposition is reported in the row (both kinds
carried) but is not in the PASS predicate — it cannot move a passage into or out of the denominator, and
both dispositions are printed; at most a mislabel, visible.
Origin classification cannot be laundered: quoted, machine-matched, pair-mapped, two independent
classifiers, disputes carried not reconciled, C6 re-classifies; the machine floor and the identical-
misclassification floor are both stated (Q2).
The interpretation step cannot reach back: the protocol is fixed, committed and receipted (receipt P)
before limb A; the tally is committed and receipted (receipt T) before the protocol is opened; the
interpretation reads the script-computed rests_on tally and the reproduction tally, not any seat's prose.
No channel found through inclusion, exclusion, origin, or interpretation. The one carried-over bound,
stated in the text: "completeness of a claim's input list against the paper's equation is seat-authored
and audited under C6, not machine-checked" — bounded by the audit's sampled re-classification and stated
plainly.

---------------------------------------------------------------------
4. THE BLIND
---------------------------------------------------------------------
Machine-asserted as claimed, and verified by me beyond the claim: (a) the builder exists at the pinned
digest 4ed52d4b638562f72a604e42c8073d2ea77ff834eb5a6b07e2a46ca32694fbe3; (b) the packet header names the
master digest f4edb514…, identical to the ACCESS_SHA I computed — the packet was built from these bytes;
(c) the packet carries the new C1/C1B/C6 batch text and the staged-tool pin, i.e. it is a fresh V26
build, while §0/§7/§8/§10 content is absent (my grep: no custody names, no engine names, no "pattern", no
comparison model, no rests_on/DERIVED_ONLY, no consequence words — see Q3); (d) the V26 packet lives in a
SEPARATE directory from V25's packet, which is untouched (V25 packet digest 575423fb… still matches the
lane-root pin file). C4's mechanism prevents what it claims to prevent — the seat is furnished no pattern
content in its working directory — and the document states its limits honestly: self-report controls, the
sandbox profile and probes as the real confinement, and "It cannot prove a seat has no prior exposure
from training or an earlier session — nothing available here can." The forbidden list's own limit is
stated too ("the list blocks the enumerated strings and does not establish that every consequence-bearing
word is gone"). Honest, and checks out.

---------------------------------------------------------------------
5. THE SEAL (§7)
---------------------------------------------------------------------
Two receipts, each before the step it must precede. Receipt P: the interpretation protocol's hash and
commit id are sent to the outside custodian and receipted BEFORE limb A begins — the protocol cannot be
written to suit a tally that does not yet exist. Receipt T: one named commit (merged candidate file,
exclusion ledger, merged input ledger with compute output) is receipted BEFORE the protocol is opened,
and the receipt names every file — the tally cannot be reshaped after the mapping is read. After opening,
the custodian independently re-hashes both and the interpretation report must print both receipts and the
four verified values; any missing receipt or mismatch files CENSUS_AUDIT_FAILED. The relay binds what it
claims: both artefacts existed, in the stated form, before the comparison was filed. Its limit is stated:
"It does not prove Tori had not already guessed the answer — nothing available here could prove that."
The C6 external seed is supplied only after receipt T and is unavailable to the lane before it; the
staged tool refuses selection without the stage-1 seal and without a 64-hex seed (exercised). Sound.

---------------------------------------------------------------------
6. FAIRNESS
---------------------------------------------------------------------
Every negative per-claim outcome is worded against the inputs, never the paper: REPRO_FAILED carries
'Wording: "unreproduced from the stated inputs," not "error."'; REPRO_BLOCKED names the census's own
blockage (a source outside the pinned manifest, "whether that source is obtainable elsewhere is
irrelevant"); REPRO_NO_DERIVATION_STATED describes what the paper states, not what it did wrong. Study-
level classes name census states, not paper faults. The exclusion kinds describe the numeral's role
("a numeral the paper sets rather than derives"), not a defect. One label, lane-side only and seat-
invisible: `DERIVED_ONLY` is defined as "every root origin is DERIVED, STANDARD or MEASURED" — the name
reads narrower than its membership; it is a computed field's label, changes no class filed, no control,
no reachability, and the rename is already on record as the principal's pending item. COSMETIC as a gate
matter; noted for completeness.

---------------------------------------------------------------------
7. STALL / EXECUTABILITY (Q4 answered here)
---------------------------------------------------------------------
Q4 (direct): CAN ANYTHING THE DOCUMENT DESCRIBES NOT BE EXECUTED AS DELIVERED? One thing: the 2-arg
validate commands of C2/C3 (F1 above). Everything else I checked exists and runs:
Named scripts, each located and digest-verified against the master's pins:
  r3c2_manifest.py 19a8ce4750bb47655868ef15b55f2b168833147b460c03ad56f84dd3c9bc56f2 — MATCH
  r3c2_timeout.py fbb9bef7d6622a17b4dc2e856791e3166b60394c187286ea5581b2f39003f331 — MATCH
  r3c2_lane_tools.py 8e990c7a22fb4b093d5e74218e9bfcee4b108c52bbc2df615ed3b6b2aaefa848 — MATCH
  r3c2_build_seat_packet.py 4ed52d4b638562f72a604e42c8073d2ea77ff834eb5a6b07e2a46ca32694fbe3 — MATCH
  r3c2_seat_sandbox.sb 6978d590bf2acc519f00f38e8bc71b0e9ef476b95eeb6afa38443dbaef731fa6 — MATCH
  R3C2_CORPUS_MANIFEST.md 300d4da144d96ae9f1390c9018e919ae1ba6cf00be9f45ad36fdccfdcfbf9b24 — MATCH
  (89 enumerable rows counted; two corpus texts spot-hashed against their manifest rows — MATCH; the
  texts live in the sibling sources directory the dispatch copy draws from)
  staged seat tool r3c2_ledger_tools_STAGED.py 9e916b81e296f890… — MATCH to §3's pin and the pin sheet
  staged batch tool r3c2_batch_tools_STAGED.py 1c1251931acc4666… — MATCH to the pin sheet
  R3C2_V23_DESIGN_OF_RECORD_55b466fa.md hashes to 55b466fa… — name/digest consistent
  R3C2_INTERPRETATION_PROTOCOL_20260904.md exists (not opened — seat-invisible; existence only)
Every literal command: C1's two census runs (executed on joined fixtures — C1_DENOMINATOR_PRINTED=PASS,
exit 0, declared vs recomputed counts printed, AUTHOR_SPECIFIED_INPUT line printed); C2/C3's validate
(F1 — the one failure); C5's five harness commands (all executed live: Python 3.9.6; sympy 1.14.0;
/usr/bin/shasum of the interpreter printed; user site-packages path printed; r3c2_manifest.py over that
directory printed FILES=20637 MANIFEST_SHA256=1b5463c1…, exit 0); §9's wrapper invocation form (wrapper
present at pin); the staged audit chain and batch chain (below).
Every field a script is said to compute: census declared-vs-recomputed counts and the
author_specified_input line (observed in output); validate's full check set (observed across kit
negatives and my A-series); join's recomputed counts (observed); compare's C6_AUDIT.json with union rows,
dispute rate, per-claim and per-origin MATCH/MISMATCH (observed).
Every path a seat is told to use: the working directory, "." as sole sources_dir, the pinned environment
(interpreter + the one site-packages directory C5 prints), the printed verbatim commands. Under the
candidate's C4(i)–(iii), all five C5 commands are in scope and single invocations.
Packaging note (declared, not a defect): no R3C2_SEAT_PACKET.sha256 exists yet for the CANDIDATE packet
directory — the lane-root pin file pins V25's packet (575423fb…) and V25's tool (230359eb…). The
candidate is UNADOPTED; §10.20 and the staged README declare adoption as ruling → re-pin → rebuild → C0 →
gate. Recorded so the adoption checklist contains it: write the candidate pin file (packet, brief, and
the three scripts with the staged tool under its adoption name r3c2_ledger_tools.py) at adoption.
Q4 verdict: executable as delivered except F1, plus the declared adoption-time pin/brief packaging.

=====================================================================
Q7 — THIS CANDIDATE
=====================================================================
(a) Kit run: `cd r3c2_staged_d1d7 && /usr/bin/python3 -E r3c2_staged_tests.py` — last three lines:
    deletion_probes=38
    controls=111 passed=111 failed=0
    STAGED_TESTS=PASS
    Pin sheet verified from the working directory first: `shasum -a 256 -c
    r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256` → all seven rows OK.
    My own fixtures (all under _tmp_R3C2_V26CAND_GATE_kimi/):
    D1 import through `validate <ledger> <sources_dir> <candidates.json>`:
      A1 clean import ("We adopt beta = 0.012 from B (2020)"; token at the first line of the source
      carrying both symbol and numeral): C3_NO_SUBSTITUTION=PASS, exit 0.
      A2 cited line = the SECOND line carrying both: FAIL "external value line 5 is not the first line of
      paperB.txt carrying both beta and 0.012 (that is line 4)", exit 1.
    Full audit sequence (seal-enumeration → select → handout → seal-rederivation → compare), seed
    9f1c7a4e2b8d0356×4:
      B1 seal-enumeration: AUDITOR_CANDIDATES_SHA256=29852a93…, AUDITOR_EXCLUSIONS_SHA256=3b8e6a60…,
      AUDITOR_CENSUS_STDOUT_SHA256=55b0784e…, exit 0 (census-gated, first-write).
      B2 select: N=5 R=3 k=1 audited=3, exit 0 (refuses without the stage-1 seal and without 64-hex seed
      — kit negatives cover both).
      B3 handout: 3 claims, fields claim_id/source_file/source_line ONLY (file inspected), exit 0.
      B4 seal-rederivation: AUDITOR_REDERIVATIONS_SHA256=5a0c7eed…, exit 0 (first-write).
      B5 compare: C6_AUDIT_SAMPLE=PASS, exit 0 (selection recomputed; union rows all MATCH).
      B6 omission negative (sealed ledgers omit a passage the auditor enumerated): "FAIL: COMPLETENESS
      audit_included_absent_from_sealed", C6_AUDIT_SAMPLE=FAIL, study_files=CENSUS_AUDIT_FAILED, exit 1.
    Partition → seal → join → coverage (4-text fixture manifest, 2 batches):
      C1 partition: batches of 2+2 texts, exit 0. C2 out-of-order seal of batch 2 first: "FAIL: batch 2
      sealed before batch 1 (dispatch order)", exit 1. C3/C4 seals in order: artefact digests printed,
      exit 0. C5 join: JOIN=PASS, exit 0 (joined candidates/exclusions/ledger written with digests;
      counts recomputed). C6 coverage: C1B_BATCH_COVERAGE=PASS, exit 0 (4/4 texts owned exactly once,
      bytes verified, both batch reports carry ACCESS_SHA=). C7 census over the joined files:
      C1_DENOMINATOR_PRINTED=PASS, exit 0. C8 3-arg validate over the joined ledger — a batch-1 claim
      importing from the batch-2-owned u4.txt: C3_NO_SUBSTITUTION=PASS, exit 0.
    Real-manifest check: `partition R3C2_CORPUS_MANIFEST.md 12` recomputed byte-identical to the pinned
    partition_12_of_89.json (both 15b69217a35dbc6f…), 12 batches of 8/7 texts over 89 rows.

(b) C5_EXECUTABLE_UNDER_SCOPE=YES — all five C5 commands executed live from the lane directory under the
    candidate's scope clauses (system binaries via (iii) as printed commands; the site-packages directory
    via (ii)); every one exited 0 with full output. NO_MASKED_STAGE=YES — no mandated command in this
    text is a shell pipeline; every control's PASS is one invocation's exit status (the §9 wrapper counts
    as one invocation that prints its child's status, as the text states); the staged audit/batch
    commands are single invocations and I ran each one un-piped for its true exit status.

(c) CANDIDATE_DIFF_ONLY=YES. Full diff V25 (ab6352d35a0e02fb…, matching §10.20's `ab6352d3…`) against the
    candidate: 11 hunks, and every hunk is one of the declared changes or the version apparatus —
    (1) header V25→V26 INTEGRATED CANDIDATE; (2) §1's excluded-kinds sentence gains the sixth kind
    AUTHOR_SPECIFIED_INPUT; (3) §2's import rule replaced by D1 wording B plus the "Machine floor,
    stated" paragraph (the declared claim-binding/first-line/token/bytes-verify checks restated); (4) §3
    tool pin 230359eb…→9e916b81… with the third-argument note; (5) C1 gains the ownership-batching
    paragraph; (6) C1B added; (7) C3 gains the one ORIG_CITATION-at-the-claiming-paper sentence; (8) C6
    replaced by the stronger D7 (independent sealed enumeration, seed-required selection, file+line-only
    handout, sealed re-derivations, union comparison, bounded PASS); (9) C6's old trailing artefact
    paragraph replaced by a pointer to the control's opening; (10) §9's "Two independent seats" extended
    to sessions-under-one-packet with per-session ACCESS_SHA and ownership list; (11) §10.20 added.
    Nothing else differs. (F1 is not an extra difference: C2/C3's command lines are UNCHANGED from V25 —
    the defect is that the unchanged text no longer matches the declared new tool pin.)

(d) Does any of the three texts (V25, the candidate, the packet) make a §3 outcome or §4 class reachable
    by assertion, or let the lane's expectation reach the evidence through the new controls? No.
    Outcomes are filed by the seats from mechanical rules and merged only on agreement; the new controls
    are artefact-backed: C1B's coverage verifies ownership over real bytes and checks each batch report's
    printed ACCESS_SHA against the packet's; JOIN is computed by the pinned pure function, not asserted;
    C6's PASS requires the printed C6_AUDIT.json with both seals matching and the selection recomputed.
    Through the new controls specifically: the partition is pinned in advance (row order, digest-bound —
    no seat chooses its batch); batches seal in order before the next dispatch; ownership partitions
    enumeration but not evidence access, and cross-batch reads are logged; the auditor works source-only,
    on a different engine, sealed before any seat ledger is released. No expectation channel opened.

(e) Hardest cases, one disposition each or shown impossible:
    (i) An import whose source line says "we choose" (fixture A3: paperC.txt line 3 "we choose beta =
        0.012 as our fiducial value", claimed by paperA's naming sentence): under the CANDIDATE, exactly
        one disposition — PRINTED/IMPORTED, ORIG_CITATION satisfied at the claiming paper's naming
        sentence, "no reason code is applied to the source's line"; the arithmetic consumes it;
        rests_on = USES_IMPORTED. Live: C3_NO_SUBSTITUTION=PASS, exit 0. Under V25 as written the same
        case is the recorded D1 seam: V25's §2 cites ORIG_CITATION "to the named source's file and line",
        so the evidence quotation would be a choice statement — the pair rule and the import rule pull
        against each other and no single valid filing exists; the candidate's wording B closes it.
    (ii) A passage both seats omitted: under the CANDIDATE, exactly one disposition — the auditor's
        sealed independent enumeration lists it, the union comparison files OMISSION, and the study
        files CENSUS_AUDIT_FAILED (fixture B6, exit 1). Under V25 the disposition existed on paper ("no
        incompleteness" in the PASS predicate) but the auditor read the seat ledgers first with no
        sealed enumeration of its own and no union comparison, so detection rode on an unsealed post-hoc
        report; the candidate makes it machine-enforced.
    (iii) A batch-1 claim importing from a batch-12 text: under the CANDIDATE, exactly one disposition —
        ownership partitions enumeration, not access: the batch-1 session holds all texts, reads the
        batch-12 text as evidence (logged with file and line), files PRINTED/IMPORTED; join requires the
        evidence source to be a manifest text (not an owned one); validate requires the external source
        to be an enumerable manifest row with verified bytes and the first line carrying symbol and
        numeral. Exercised at fixture scale (C5 join PASS + C8 validate PASS on a batch-1 claim importing
        the batch-2-owned u4.txt), exit 0 each. Under V25 the case does not arise as a batch case (no
        batching); the import is handled by V25's §2 rule alone, subject to (i)'s seam.

DECLARED-GAP FINDING (F4) — the seat brief. r3c2_seat_packet_v26_candidate/SEAT_BRIEF.md is byte-identical
to V25's brief (both b734243fe4dbd7796d…, matching the V25 pin file): unrevised for batch sessions, as
declared. Before adoption the brief must say, in its own wording: (i) the seat is a sequence of sessions
under one packet, one batch per session, dispatched in the pinned batch order; (ii) each session
enumerates ONLY its owned texts (the ownership list the dispatch record carries) while holding all
pinned texts — its step 3 currently says "enumerate every candidate passage" with no ownership bound and
must be scoped; (iii) per-session artefacts are candidates_b<k>.json, exclusions_b<k>.json,
ledger_b<k>.json and SEAT_REPORT_b<k>.md (it currently names one SEAT_REPORT.md); (iv) every candidate,
claim and input id begins with "<owned file>#"; (v) each batch report prints the packet's ACCESS_SHA
(C1B's coverage checks it); (vi) §2 named-source lookups may read any manifest text and are logged with
file and line; (vii) each session's artefacts are sealed by the custodian before the next batch is
dispatched; (viii) `validate` takes the batch candidate file as its third argument per session and the
joined candidate file over the joined ledger (same repair as F1); (ix) the final-line token and report
name per session. The brief's own closing rule ("where a rule and this brief differ, the packet governs")
limits the blast radius meanwhile, but the brief must be revised before any dispatch under the candidate.

SUMMARY OF FINDINGS
  F1 (repair required): C2/C3 printed validate commands omit the candidate-file third argument the §3-
      pinned tool requires — demonstrated FAIL on any ledger with a PRINTED record. Exact replacements
      given in section 2.
  F4 (repair required, declared gap): the seat brief is V25's, unrevised for batch sessions; required
      content enumerated above.
  F2 (COSMETIC): §3's exclusion parenthetical names five kinds; the operative list and the tool carry six.
  F3 (COSMETIC): C1B's JOIN predicate has no PASS|FAIL|NOT_RUN token line of its own.
  Cosmetic note carried, not mine: the lane-side DERIVED_ONLY label reads narrower than its membership;
      the rename is already the principal's pending item.
Everything else judged sound: outcome classes exhaustive and mutually exclusive under total precedence
with INCONCLUSIVE genuinely reachable; Q1 YES; provenance checkable to a stated floor with the two-seat
and C6 catch (Q2); no circularity channel through inclusion, exclusion, origin or interpretation; the
blind machine-asserted and independently verified; the two-receipt seal binds protocol before limb A and
tally before protocol opening with its limit stated; fairness wording intact; executability verified by
running the kit (111/111), all five C5 commands, and my own fixtures through every staged subcommand.
This gate adopts, freezes and runs nothing; the three method choices are the principal's.

R3C2_V26CAND_GATE_COMPLETE

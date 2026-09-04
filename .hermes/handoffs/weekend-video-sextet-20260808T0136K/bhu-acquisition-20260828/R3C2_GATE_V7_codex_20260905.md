ACCESS_SHA=19a075c66696c4a0793c2fb13a45247f9e174f4b2194ec3a9f540ed001597000
GATE=PREREG_UNSOUND

1. Hypothesis influence on claim selection and outcome assignment

Defect. The sentence “Every candidate passage is listed with file and line; inclusion and exclusion are both recorded.” supplies an audit trail, but it does not make the boundary mechanical. Whether a numeral is “the paper's own result,” whether an attributed value was nevertheless derived, and what passage counts as the asserted result still require semantic judgments. Pattern-blind independent enumerators and the full-ledger audit substantially constrain influence, but C4 expressly cannot exclude prior exposure; therefore the categorical claim “The hypothesis cannot reach the evidence.” is stronger than the design can establish.

Exact replacement: “Every candidate passage is listed with file and line; inclusion and exclusion are both recorded. Inclusion is independently assigned by two pattern-blind seats using the §1 rule, disagreements stop under `CENSUS_DENOMINATOR_DISPUTED`, and the third seat audits the complete candidate and exclusion ledgers. These controls reduce and expose hypothesis influence; they do not prove its absence, because prior exposure cannot be excluded.”

The held §3 clause changes which provenance patterns enter the arithmetic group and therefore which outcome is assigned, but it does not cure or worsen this enumeration-boundary defect. Under option (b), the standing derivation-only rule applies. The target does not state the text of options (a), (c), or (d), so their detailed effects cannot honestly be specified without opening files the instructions forbid; whichever is adopted must preserve blind, mechanically checked provenance-to-outcome assignment.

2. Per-claim outcomes and study-level classes

Per-claim outcomes are exhaustive and mutually exclusive under the stated precedence rule, conditional on the held clause supplying a complete and unambiguous membership rule for the arithmetic group. Under option (b), the named terminal classes plus the arithmetic group cover the stated paths. Under (a), (c), or (d), the same conclusion holds only if the adopted clause explicitly maps every remaining arithmetic result to exactly one arithmetic-group outcome.

Defect. Study-level classes are not mutually exclusive. The sentences “`CENSUS_AUDIT_FAILED` — the audit of §6 cannot reproduce a sampled per-claim outcome.”, “`R3C2_NO_CLASS` — a control fails in every seat that attempted it after two attempts.”, “`CENSUS_ORIGIN_DISPUTED` — the two seats' independent `origin` classifications disagree on inputs affecting more than 10% of included claims.”, and “`CENSUS_CONTROL_SPLIT` — a control fails in one seat and passes in another after two attempts.” can simultaneously hold for different controls or alongside an audit/origin failure, and §4 gives no global precedence.

Exact replacement (append to §4): “Exactly one study-level class is filed. Apply this precedence: `CENSUS_DENOMINATOR_DISPUTED`, `R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`, `CENSUS_COMPLETE`. Once a higher-precedence condition holds, report all lower-precedence conditions as subsidiary findings, not additional classes.”

Defect. Not every mandated stop lands in a class. The sentence “If any survives, the packet is not written and `C4_PACKET_REDACTED=FAIL`; the study does not proceed on a hand-checked copy.” stops before any seat attempts the control, so `R3C2_NO_CLASS` (“fails in every seat that attempted it”) need not apply. Likewise, “the interpretation protocol is not opened without that recorded acknowledgement” specifies a stop for a missing receipt but no study-level class.

Exact replacement for the packet sentence: “If any survives on either of two build attempts, the packet is not written, `C4_PACKET_REDACTED=FAIL`, and the study files `R3C2_NO_CLASS`; the study does not proceed on a hand-checked copy.”

Exact replacement for the receipt sentence: “The interpretation protocol is not opened without that recorded acknowledgement; after two unsuccessful receipt attempts, file `R3C2_NO_CLASS` and leave §7 `NOT_RUN`.”

3. Controls and literal commands

Defect. The controls do not each name exact `PASS`/`FAIL`/`NOT_RUN` codes. They mostly name only a PASS token; C4 additionally names one FAIL token; and the generic prose “Controls in an unreached limb are `NOT RUN`, never passes.” supplies neither exact per-control `NOT_RUN` tokens nor complete fail predicates. C0 also permits passage by a verifier's judgment: “The exhibitions are authored by a seat and only verified by Tori.” No executable verifier or exact machine predicate defines reachability. C1 and C2 similarly state artefacts but no mechanical validation command or failure predicate.

Exact replacement (replace the generic sentence after C6): “Every control emits exactly one of its three exact codes: `C0_REACHABILITY=PASS|FAIL|NOT_RUN`, `C1_DENOMINATOR_PRINTED=PASS|FAIL|NOT_RUN`, `C2_INPUT_LEDGER=PASS|FAIL|NOT_RUN`, `C3_NO_SUBSTITUTION=PASS|FAIL|NOT_RUN`, `C4_PACKET_REDACTED=PASS|FAIL|NOT_RUN`, `C4_PATTERN_BLIND=PASS|FAIL|NOT_RUN`, `C5_HARNESS_PINNED=PASS|FAIL|NOT_RUN`, `C5B_NO_CROSS_LANE=PASS|FAIL|NOT_RUN`, and `C6_AUDIT_SAMPLE=PASS|FAIL|NOT_RUN`. Each control section names the committed validator command, its required inputs, and the exit-status/output predicate producing each code. A control in an unreached limb emits its exact `NOT_RUN` code. Human attestation or review alone cannot emit PASS.”

Exact replacement for the C0 verification sentence: “The exhibition table is validated by the committed command `python3 r3c2_validate_reachability.py REACHABILITY.json`; exit 0 with one valid witness for every required outcome and refuting condition emits `C0_REACHABILITY=PASS`, any missing or invalid witness after two attempts emits `C0_REACHABILITY=FAIL`, and an unreached C0 limb emits `C0_REACHABILITY=NOT_RUN`; Tori re-runs but does not adjudicate the validator.”

The three literal C5 shell commands are executable as written in the specified shell. No defect is found in their literal syntax.

4. Honesty of blinding claim

Sound. C4 states the enforceable packet/work-directory boundary and expressly says it cannot prove absence of prior exposure. Subject to the overclaim repaired in finding 1, its description of what the blind can and cannot enforce is honest. No replacement.

5. Honesty and utility of the seal

Sound. The receipt binds four digests before interpretation, requires later re-verification, treats a local commit only as tamper evidence, and expressly disclaims proof about Tori's prior beliefs. The seal is useful and not overclaimed. The missing-receipt terminal-class gap is repaired in finding 2; it is not a defect in the seal's stated evidentiary scope.

6. Fairness wording

Defect. The required wording appears in `REPRO_FAILED`, but it is not held throughout. C6 says “the class in which an error is both consequential and invisible,” which invites characterization as error rather than unreproduction from stated inputs.

Exact replacement: “the class in which a result unreproduced from the stated inputs would be both consequential and otherwise invisible”.

7. Terminal state with no fileable class

Yes. A twice-failed pre-dispatch packet build and a twice-unreceipted custody relay can terminate the run without a fileable class; multiple simultaneous control/audit failures can also prevent filing exactly one class. The exact replacements in findings 2 and 3 close these paths and impose uniqueness. These defects are independent of all four readings of the held clause.

R3C2_V7_GATE_COMPLETE

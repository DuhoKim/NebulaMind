ACCESS_SHA=972e01d122149fac1dc9d702130a20c1fdda9e73cebed338e6435beea0916115
PACKET_SHA=7521fa5da2b2eb46de3aed0e310433ec166e597f30437ede9749027ac8b2d9b7
GATE=PREREG_UNSOUND
LEAK=Provenance receives special scrutiny; Planck is a plausible comparison context, but no directional hypothesis or preferred empirical outcome is reconstructible.
CONSEQUENCE_VISIBLE=Audit failure suppresses the tally: “No tally is filed; report which.”
ORIGIN_PURPOSE=Independent agreement checking and a study-stop threshold: “The census does not proceed; every disputed input is listed with both seats' classification and both quotations.”
C5_EXECUTABLE_UNDER_SCOPE=NO — the live SymPy import succeeds by loading an excluded user-site package; command success is not scope compliance.

### 1. Outcome classes — Q1

Packet-only answers, recorded before opening the master:

**Q5. CAN YOU TELL, FROM THE PACKET ALONE, THAT ANY OUTCOME IS MORE CONSEQUENTIAL THAN ANY OTHER?** Yes, procedurally: “No tally is filed; report which.” An audit failure suppresses a tally that completion would report. No sentence identifies a substantive outcome that benefits the lane; “No tier, warrant token, standing or stamp moves.” The header therefore answers the literal question, including procedural consequences.

**Q6. CAN YOU STATE, FROM THE PACKET ALONE, WHAT THE RECORDED `origin` OF AN INPUT IS FOR?** Yes, for checking independent classifications and potentially stopping the study. The packet defines `CENSUS_ORIGIN_DISPUTED` by disagreements affecting “more than 10% of included claims” and says: “The census does not proceed; every disputed input is listed with both seats' classification and both quotations.” C6 also re-classifies origins against sealed records. I cannot infer a further analytical use, a combined summary, or its interpretation.

**Q3. WHAT CAN YOU INFER ABOUT WHAT THE LANE EXPECTS OR HOPES THE CENSUS WILL SHOW?** The sentence “Every input's `origin` is classified independently by both seats” and the disagreement threshold reveal special attention to provenance. “The cosmological rows are the Planck 2018 TT,TE,EE+lowE+lensing baseline” reveals cosmology and makes Planck a plausible comparison context. Neither establishes a comparison hypothesis. “The reproduction verdict and the provenance fields are recorded separately” shows that reproduction and provenance are distinct recorded facts, without saying how they are combined. I cannot reconstruct a preferred direction, predicted pattern, or empirical stake. These are content-level clues, not evidence of a directional expectation.

**Q1. DOES SECTION 3's DEFINITION, AS WRITTEN UNDER OPTION (c), MAKE EVERY DECLARED OUTCOME REACHABLE AND KEEP THE REPRODUCTION QUESTION DECIDABLE?** Every class has a concrete witness, but the complete input-recording procedure is not consistently executable for every admitted imported input. Thus the unqualified answer is **NO**. The settled mechanical-consumption definition itself is coherent; defect D1 is in its evidence interface.

The following are constructed, fully specified paper passages, not claims represented as observed in the unopened corpus:

| Paper passage or condition | Unique per-claim outcome | `rests_on` |
|---|---|---|
| “We choose a = 2; y = 3a = 6.” | `REPRO_WITHIN_STATED_PRECISION` | `USES_CHOSEN` |
| “The fit gives a = 2; y = 3a = 6.” | `REPRO_WITHIN_STATED_PRECISION` | `USES_FITTED` |
| “We choose a = 2; y = 3a = 7.” | `REPRO_FAILED` | `USES_CHOSEN` |
| “Use a from Reference B; y = 3a = 6”; B is outside the enumerable manifest. | `REPRO_BLOCKED` | `USES_IMPORTED`, with a BLOCKED/IMPORTED record |
| “y = 3a = 6”; a has no value or named source. | `REPRO_INPUT_ABSENT` | `USES_UNDECLARED`, with documented adequate origin search |
| A stated recipe using printed chosen inputs reaches the wrapper's deadline. | `REPRO_NOT_EVALUABLE` | `USES_CHOSEN` |
| “Our result is y = 6”; no procedure is stated and no inputs can be enumerated. | `REPRO_NO_DERIVATION_STATED` | `NOT_COMPUTED` |

A recipe with both a blocked input and an absent input satisfies two raw terminal predicates, but the explicit precedence uniquely files `REPRO_BLOCKED`. The precedence also resolves an unavailable-machine condition accompanying either. I found no double filing after applying that order.

For study-level reachability: one audited arithmetic claim gives COMPLETE; one audited absent-input claim gives PARTIAL/INCONCLUSIVE; a zero denominator also gives PARTIAL; a missing seed gives AUDIT_FAILED; two failed harness attempts in all attempting seats give NO_CLASS; a surviving inclusion split gives DENOMINATOR_DISPUTED; a surviving arithmetic verdict split gives OUTCOME_DISPUTED; one disputed-origin claim among five gives ORIGIN_DISPUTED; opposing control results after two attempts give CONTROL_SPLIT. A partial tally with a failed audit satisfies both raw predicates, but AUDIT_FAILED precedes PARTIAL. INCONCLUSIVE is genuinely reachable with a successful audit of an accurately recorded unresolved claim.

**D1 — substantive: imported-value evidence can require an impossible origin/evidence pairing.**

Verbatim operative instruction:

> A value the paper does not print but traces to a named source that is itself an enumerable text in `R3C2_CORPUS_MANIFEST.md` is classified `PRINTED` from that source, with `origin` `IMPORTED`, `origin_evidence` `ORIG_CITATION` cited to the named source's file and line, and the value machine-matched there — **only when such a match exists; a cited value that does not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest, files `REPRO_BLOCKED` under §3.**

Construct claiming paper A: “Use a from B, line 1; y = 3a = 6.” Pinned enumerable B, line 1: “We choose a = 2.” The value is matchable, so arithmetic must proceed and reproduce 6. Section 2 demands IMPORTED/ORIG_CITATION evidenced at B:1; C3's sentence-based evidence classification at B:1 instead supports CHOSEN/ORIG_CHOICE_STATED. Citing A would establish importation but violate §2's prescribed evidence location. BLOCKED is unavailable because B is enumerable and the value matches. The intended verdict and `USES_IMPORTED` are clear, but no record satisfies both instructions honestly.

Exact replacement for that instruction:

> A value the claiming paper does not print but traces to a named source is PRINTED with origin IMPORTED only if the source is an enumerable text in R3C2_CORPUS_MANIFEST.md and the value machine-matches its cited line. The record's source_file and source_line identify that value-bearing line in the named source. Its origin_evidence has reason_code ORIG_CITATION and quotes the claiming paper's sentence directing the reader to that source, with that sentence's source_file and source_line. The source author's own provenance does not replace the claiming paper's import relationship. Otherwise the input is BLOCKED and the claim files REPRO_BLOCKED, subject to §3 precedence.

### 2. Controls — Q2

**Q2. IS THE PROVENANCE FIELD CHECKABLE RATHER THAN ASSERTED?** Yes, partially and explicitly through human re-classification; it is not semantically proved by substring matching.

Concrete adversarial ledger record, using a constructed source line “We adopt a = 2 from Reference B”:

```json
{
  "claim_id": "q1",
  "input_id": "q1_a",
  "symbol": "a",
  "status": "PRINTED",
  "origin": "CHOSEN",
  "origin_evidence": {
    "reason_code": "ORIG_CHOICE_STATED",
    "source_file": "A.txt",
    "source_line": 1,
    "verbatim": "We adopt a = 2 from Reference B"
  },
  "derived_from": [],
  "value": "2",
  "source_file": "A.txt",
  "source_line": 1
}
```

The value and quotation match; the declared reason/origin pair agrees internally. The described machine checks therefore do not catch the semantic misclassification. C3's citation-first rule makes IMPORTED correct. A second independent seat can detect the wrong classification; C6 independently re-classifies every arithmetic-group claim and can detect it again. If every reader makes the same mistake, it survives, as the master explicitly admits. For non-arithmetic claims, C6's re-derivation sample does not guarantee inspection of this particular input. This is a stated human-audit limitation, not a machine proof.

The named controls are C0_REACHABILITY, C1_DENOMINATOR_PRINTED, C2_INPUT_LEDGER, C3_NO_SUBSTITUTION, C4_PACKET_REDACTED, C4_SEAT_ISOLATION, C5_HARNESS_PINNED, C5B_NO_CROSS_LANE, and C6_AUDIT_SAMPLE. Each has PASS/FAIL/NOT_RUN. Their required artefacts are respectively the independently exhibited/verified table, census runs and counts, validator run, validator plus lane merge/compute runs, builder run and dispatch pins, printed path list/dispatch record, three live command outputs, scope-marked path list, and printed C6_AUDIT.json.

These require printed artefacts rather than bare PASS tokens. C4/C5b can nevertheless pass an incomplete self-reported list; their definitions openly permit that limited certification. Unreached controls are explicitly NOT_RUN. Root origins and rests_on are assigned to lane-script computation rather than seat assertion; implementation correctness remains unverified under the file-access restriction described in section 7.

### 3. Circularity

The operational inclusion rule contains no directional hypothesis. Both independent inclusion decisions are recorded; disagreements stop the census, and C6 audits the entire candidate/exclusion enumeration against every pinned source. A contrary claim cannot be quietly excluded through an authorized exclusion category merely because it is contrary. Two readers can still share a mistaken exclusion; the independent full-source audit is the stated check.

The taxonomy remains a human classification channel. D1 shows an inconsistency in that channel, not evidence that a particular expectation actually reached any observation. The external interpretation protocol is sealed before enumeration. Its actual mapping and the substantive suitability of the corpus manifest were not inspected and cannot be certified from these permitted documents. No historical verdict is used as evidence here.

### 4. The blind

The packet actually omits the master's analytical `rests_on` mapping and interpretation protocol. Its embedded master digest equals the independently computed ACCESS_SHA. That verifies a textual binding, not that the builder ran correctly.

C4 specifies a pinned builder, redaction spans, forbidden-string assertions, an out-of-lane dispatch inventory, and a printed builder result. Those describe a machine assertion; inspecting the two Markdown files cannot establish the delivered builder's implementation or an actual successful run. I did not run the builder because it opens other files and rewrites deliverables.

C4 honestly says:

> This is procedural, not enforced by the filesystem

and:

> C4_SEAT_ISOLATION=PASS certifies the contents of the printed list and of the dispatch copy, not actual non-access.

It therefore does not prevent undisclosed outside reads and does not claim to prove their absence. The runtime amendment introduces the substantive scope defect below.

**D2 — substantive: the runtime allowlist is simultaneously too broad and too restrictive.**

Verbatim C4 clause:

> The two system binaries C5 names — `/usr/bin/python3` and `/usr/bin/shasum` — and the files they load from the system runtime locations only (`/usr`, `/System`, `/Library`, `/private/var/folders`, `/dev`) while executing the exact mandated commands are IN SCOPE and are not "outside paths" under this control; a startup, configuration or import file loaded from any other location — the working directory's parents, the lane, `/tmp`, or any user-writable path — is an outside path and `FAIL`; every other path outside the working directory is `FAIL`.

The /usr prefix includes /usr/local; /private/var/folders explicitly admits user temporary locations. Neither prefix establishes that an imported file is operating-system runtime code. For example, a PYTHONPATH pointing to a user-created directory under /private/var/folders can make the exact C5 import resolve a substituted sympy.py under an allowed prefix. If “any user-writable path” instead overrides the prefix allowance, the rule contradicts its express inclusion of such locations. Neither reading supplies an unambiguous safe runtime inventory.

Conversely, the actual SymPy installation is outside all five prefixes. Also, C5b's “anything loaded from elsewhere is OUT_OF_SCOPE” literally includes working-directory scripts, although C4 otherwise permits those scripts.

Exact replacement for the C4 exception, with the same text substituted for the corresponding C5b and brief runtime clauses:

> The working-directory files required by this packet, /usr/bin/python3, and /usr/bin/shasum are IN_SCOPE. Outside the working directory, only operating-system runtime files and the independently verified Python/SymPy dependency files enumerated by canonical path and digest in the pre-dispatch runtime inventory are IN_SCOPE; directory-prefix membership alone grants no access. No lane source, parent-directory file, user startup file, .pth file, sitecustomize.py, usercustomize.py, or environment-selected import is authorized by this exception. Before dispatch, the lane owner provisions SymPy and its dependencies in the isolated system interpreter's permitted package location, removes environment-based Python and Perl startup/import overrides, and records a successful C5 run using only the inventoried runtime. All mandated Python invocations use /usr/bin/python3 -I. Every other outside load is OUT_OF_SCOPE and FAIL. These scope classifications remain procedural unless a separately documented access restriction enforces them.

Apply the literal `/usr/bin/python3` → `/usr/bin/python3 -I` command change consistently throughout the packet, master and brief; rebuild and repin affected artefacts. This is a proposed repair requiring provisioning and verification, not a claim that such an environment exists now.

### 5. The seal

The designed order is sound: receipt P binds the protocol hash and commit before limb A; receipt T binds the tally commit and its named files before protocol opening; independent re-hashing checks both sets; missing receipts or mismatches void interpretation and file AUDIT_FAILED. The custodian's unpredictable audit seed follows T, preventing selection of the sample by choosing tally formatting in advance.

The mechanism binds committed records and timing relative to the named steps. It does not prove absence of prior knowledge, and the text acknowledges that. I did not inspect receipts or the interpretation protocol; this is a design finding, not verification that custody actions have happened.

### 6. Fairness

REPRO_FAILED expressly requires “unreproduced from the stated inputs,” not “error.” The brief extends that wording to negative outcomes generally. BLOCKED, INPUT_ABSENT, NOT_EVALUABLE and NO_DERIVATION_STATED describe limits on reproduction rather than claiming scientific falsity. CENSUS_COMPLETE can include arithmetic failures; its name certifies census coverage, not successful reproduction of all numbers.

The old token `REPRO_EXACT` has no governing reference in the master. I checked all occurrences with `rg -n 'REPRO_EXACT|^## '`: line 118 is the rename notice; every other hit falls under a §10 heading. I did not need or open the optional rename-audit file.

**D3 — substantive conclusion-label overclaim.**

Verbatim operative rule:

> `DERIVED_ONLY` when every root origin is `DERIVED`, `STANDARD` or `MEASURED`

A claim using only an experimentally measured input can receive DERIVED_ONLY without any derivation of that input. The token asserts more than its membership rule and is passed into interpretation. A settled mechanical reproduction definition does not settle the accuracy of this separate provenance label.

Exact replacement:

> DERIVED_STANDARD_OR_MEASURED_ONLY when every root origin is DERIVED, STANDARD or MEASURED

Replace the old label consistently in lane-script output, tally labels and the sealed interpretation protocol; preserve its membership rule. This is not COSMETIC under the requested conclusion-label test, although it changes no arithmetic.

### 7. Stall / executability — Q4 and Q7

**Q4. CAN ANYTHING THE DOCUMENT DESCRIBES NOT BE EXECUTED AS DELIVERED?** Yes: C5's SymPy import cannot both use the observed installation and comply with the new scope bound. D1 also prevents a fully compliant ledger for its imported-input witness.

Live commands and complete outputs:

```text
/usr/bin/python3 --version
Python 3.9.6
exit=0

/usr/bin/python3 -c "import sympy; print(sympy.__version__)"
1.14.0
exit=0

/usr/bin/shasum -a 256 /usr/bin/python3
b8763cf250e607a778bb4603cecb5b90338814d0a3dfcba0d57b1de242f610e9  /usr/bin/python3
exit=0
```

A separate runtime-location diagnostic reported:

```text
SYMPY_FILE=/Users/duhokim/Library/Python/3.9/lib/python/site-packages/sympy/__init__.py
EXECUTABLE=/Library/Developer/CommandLineTools/usr/bin/python3
```

The diagnostic inspected runtime metadata, not corpus contents. A further isolated-interpreter probe produced:

```text
/usr/bin/python3 -I -c "import sympy; print(sympy.__version__)"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'sympy'
exit=1
```

Thus merely adding isolation flags does not repair the delivered environment.

Checks and limits:

| Named item | Check and result |
|---|---|
| Master and seat packet | Read and hashed in the prescribed order; full hashes above. |
| SEAT_BRIEF.md | Read only under the Q7 scope-consistency exception. |
| Three literal C5 commands | Executed exactly; outputs above. |
| r3c2_ledger_tools.py, r3c2_lane_tools.py, r3c2_timeout.py, r3c2_build_seat_packet.py | Exact-path file-existence checks succeed beside the master. Contents, hashes and behavior were not inspected. |
| R3C2_CORPUS_MANIFEST.md, R3C2_SEAT_PACKET.sha256, R3C2_INTERPRETATION_PROTOCOL_20260904.md | Exact-path file-existence checks succeed beside the master; contents were not opened. |
| census, census … final, validate … ., merge, compute | Command syntax and described input/output fields checked in the master. No execution or implementation certification: these runs would open files outside the permitted review set. |
| root_origins, rests_on, origin_alt, origin_evidence_alt, PARENTS_DISPUTED | Required production/handling traced in C3; actual computation unverified because the scripts cannot be opened under this review restriction. |
| timeout wrapper and 120.0-second cap | Literal invocation and declared exit-124/timeout behavior checked in §9; wrapper implementation not executed. |
| Seed/sample expression | k is bounded by R; R=0 gives an empty sample; sorted IDs and the integer seed conversion are specified. No census was run. |
| Packet-directory copies of the ledger tool, timeout wrapper, manifest and pin file | All four exact-path existence checks fail in r3c2_seat_packet/. They exist beside the master. |
| Actual out-of-lane dispatch tree and enumerable source inventory | Not delivered as a named path in the permitted text; not inspected or inferred. |
| C6_AUDIT.json, ledgers, receipts, check sheet, provider log and SEAT_REPORT.md | Described as products of later actions, not assumed to exist before a study run. |

The missing files inside r3c2_seat_packet/ mean that directory alone is not an executable seat working directory. C4 instead requires construction of a separate complete dispatch tree and forbids dispatch if anything is missing. Therefore these particular missing copies do not prove violation of C4's delivery promise; they prevent treating the source packet folder as a ready-to-run seat tree. I found no missing root-level script among the exact names checked. The source corpus cannot be exhaustively inventoried without opening the prohibited manifest.

The restriction to the named documents prevents exhaustive script, pin, corpus and V23-baseline verification. I report those as unverified, not as passes or invented missing-file findings.

**Q7(a): Can a seat obeying C4 and the brief execute every C5 command?** Not compliantly on the observed installation. C5 says:

> PASS requires all three commands to exit 0 and their full stdout to be printed

but the brief authorizes loads from:

> the system runtime locations only (`/usr`, `/System`, `/Library`, `/private/var/folders`, `/dev`)

and says:

> anything loaded from elsewhere is an outside path.

The required import uses /Users/duhokim/Library/Python/3.9/lib/python/site-packages/sympy, so successful C5 output does not establish C4/C5b compliance.

**Q7(b), including the addendum:** (i) The bound excludes /tmp and user-home imports textually, but does not sufficiently close the startup/import-path hole: /usr/local and user-controlled subdirectories of /private/var/folders remain inside the allowed prefixes, and no startup isolation is mandated. (ii) It is too tight for the delivered Apple Python plus its installed SymPy; the exact excluded dependency path is above. This is an observed installation finding, not a claim that every macOS installation puts SymPy there. (iii) All three texts enumerate the same five runtime prefixes. They are not fully consistent about in-directory loads: C4 broadly permits working-directory files, while C5b and the brief's “anything loaded from elsewhere” omit that exception. D2 supplies a common replacement.

**Q7(c): Is anything else different from V23?** Cannot independently determine under the permitted-file restriction. V23's bytes were not supplied in either reviewed document and its snapshot was not authorized for opening. I cannot honestly say “nothing else.” The current C5 third command is path-qualified, directly verified above; the header and §10 contain version/history text, but their account is not a verified diff.

No defect above is COSMETIC: D1 changes record validity, D2 changes scope/control passability, and D3 corrects an interpretive label. The reproduction definition need not be reopened. The delivered design should not pass this gate until these substantive defects are repaired and the currently restricted implementation checks are independently completed.

R3C2_V24B_GATE_COMPLETE

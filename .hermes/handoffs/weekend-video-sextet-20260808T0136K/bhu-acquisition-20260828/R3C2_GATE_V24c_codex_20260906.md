ACCESS_SHA=4609d97973bb28f9740ac1d6a48f9443c33d08de3673c131ec806451a9f1ec6b
PACKET_SHA=4043cd72d1e84f5cfaa0e479e1311df3799c2861545e9748f78476ed548d3cee
GATE=PREREG_UNSOUND
LEAK=NONE
CONSEQUENCE_VISIBLE=Procedural only: CENSUS_AUDIT_FAILED says “No tally is filed; report which,” whereas CENSUS_COMPLETE requires reporting the full tally.
ORIGIN_PURPOSE=Independent checking and a possible study stop: “Every input's origin is classified independently by both seats” and disagreements affecting more than 10% of claims stop the census.
C5_EXECUTABLE_UNDER_SCOPE=NO — All five commands exit 0, but importing SymPy loads user-site mpmath, which the stated exception excludes; the printed hash also covers only SymPy’s __init__.py.

This is a design review, not a census run. Section 10 supplies no evidence for this verdict. I opened no gate report. The permitted V23 comparison and seat brief were read only after the master. Runtime imports required by the harness were executed; no corpus source was opened.

Packet-first answers, recorded before reading the master:

Q5. CAN YOU TELL, FROM THE PACKET ALONE, THAT ANY OUTCOME IS MORE CONSEQUENTIAL THAN ANY OTHER?

My initial answer was NO for a substantive lane stake: no sentence identifies a preferred empirical outcome, and “No tier, warrant token, standing or stamp moves” limits consequences. That answer was too narrow for the literal “to anyone” question. The packet does expose procedural consequences: “No tally is filed; report which.” A failed audit therefore differs consequentially from a completed census. This correction uses packet text, not a hypothesis learned from the master. It does not establish a preferred scientific result.

Q6. CAN YOU STATE, FROM THE PACKET ALONE, WHAT THE RECORDED origin OF AN INPUT IS FOR?

YES for checking and stopping; CANNOT STATE its substantive downstream summary or interpretation. The packet says: “An input on which the two classifications disagree is filed ORIGIN_DISPUTED and reported with both seats' classification and both quotations; it is not reconciled. Above 10% of included claims, CENSUS_ORIGIN_DISPUTED.” Token formatting has been omitted here. That establishes a use after recording, without revealing the two-tally interpretation.

Q3. WHAT CAN YOU INFER ABOUT WHAT THE LANE EXPECTS OR HOPES THE CENSUS WILL SHOW?

No directional hypothesis, comparison model, preferred outcome or particular pattern is reconstructible. The question asks whether printed numbers follow from stated recipes. “The reproduction verdict and the provenance fields are recorded separately” and the detailed classification rules show that provenance matters. Auditing “every claim in the arithmetic group” prioritizes completed arithmetic for verification, but that group includes success and failure equally. The Planck table indicates subject matter, not a preferred comparison result. LEAK=NONE concerns hypothesis reachability, not concealment of the task’s subject or procedural stops.

**1. Outcome classes — Q1**

Q1. DOES SECTION 3’s DEFINITION, AS WRITTEN UNDER OPTION (c), MAKE EVERY DECLARED OUTCOME REACHABLE AND KEEP THE REPRODUCTION QUESTION DECIDABLE?

The core status-based arithmetic rule does. The complete operative specification does not consistently encode every admissible imported input: D1 below prevents an unqualified YES. This is an evidence-rule conflict, not an objection to option (c).

Concrete, realizable claim constructions follow. These are adversarial examples, not claimed observations from the unopened corpus.

- A paper prints “We choose a = 2; y = 2a = 4.” The consumed input is PRINTED/CHOSEN. Reproducing 4 files REPRO_WITHIN_STATED_PRECISION and rests_on=USES_CHOSEN.
- A paper prints “We fit a = 2; y = 2a = 4.” The consumed input is PRINTED/FITTED. The same reproduction files REPRO_WITHIN_STATED_PRECISION and USES_FITTED. A printed result of 5 instead files REPRO_FAILED and USES_FITTED. Re-fitting is unnecessary when the stated recipe consumes the stated fitted value.
- A paper directs use of a cited source’s a=2 and prints y=2a=4. If that source is outside the enumerable manifest, the outcome is REPRO_BLOCKED and the recorded imported root gives USES_IMPORTED.
- If the cited source is enumerable and prints the value, the arithmetic should produce REPRO_WITHIN_STATED_PRECISION/USES_IMPORTED. But if that source’s line says “We choose a = 2,” D1 makes the required provenance evidence inconsistent.
- A result with no stated procedure reaches REPRO_NO_DERIVATION_STATED, with NOT_COMPUTED if it has no input records. An equation requiring an unprinted, uncited parameter reaches REPRO_INPUT_ABSENT. An otherwise executable computation exceeding the cap reaches REPRO_NOT_EVALUABLE.

A claim y=a+b with a traced only to an unpinned source and b neither printed nor cited satisfies the BLOCKED and ABSENT predicates. The explicit precedence files only REPRO_BLOCKED. Conditions overlap; filed classes do not. I found no study-level double filing after applying the stated precedence. For example, a tally with an absent-input claim plus a failed audit satisfies PARTIAL and AUDIT_FAILED conditions but files CENSUS_AUDIT_FAILED.

Each study class has a constructive witness: a nonempty entirely arithmetic census with passing audit; one unresolved claim or zero denominator; failed audit or receipt; a control failing twice in every attempting seat; surviving inclusion/input-list disagreement; surviving outcome disagreement; origin disagreement affecting 2 of 10 claims; and a twice-tested control split between seats. These respectively reach COMPLETE, PARTIAL, AUDIT_FAILED, NO_CLASS, DENOMINATOR_DISPUTED, OUTCOME_DISPUTED, ORIGIN_DISPUTED and CONTROL_SPLIT, assuming earlier stop predicates are false.

INCONCLUSIVE is genuinely reachable: one claim lacking a stated procedure, with its classification successfully audited and earlier controls satisfied, files CENSUS_PARTIAL.

D1 — SUBSTANTIVE: imported values have conflicting evidence locations.

Verbatim §2 sentence:

> A value the paper does not print but traces to a named source that is itself an enumerable text in R3C2_CORPUS_MANIFEST.md is classified PRINTED from that source, with origin IMPORTED, origin_evidence ORIG_CITATION cited to the named source's file and line, and the value machine-matched there — only when such a match exists; a cited value that does not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest, files REPRO_BLOCKED under §3.

Markdown emphasis and code delimiters are omitted in this quotation; the words are unchanged.

The claiming paper establishes the import; the cited source establishes the value. When the source’s value line states a choice without a citation, C3’s evidence rule supports CHOSEN there, while §2 mandates IMPORTED/ORIG_CITATION there. Neither inventing citation language nor changing the outcome to BLOCKED follows the written rules.

Exact replacement for that sentence:

> A value the claiming paper does not print but traces to a named source that is an enumerable text in R3C2_CORPUS_MANIFEST.md is classified PRINTED with origin IMPORTED only when the value machine-matches at the cited source line. Record source_file and source_line at that value line; record origin_evidence with ORIG_CITATION at the claiming paper’s sentence directing use of the named source, quoting that sentence verbatim. For this record, C3’s reason-code rule is applied to that claiming-paper quotation. If the named source is not enumerable in the manifest, or the value does not machine-match at its cited line, file REPRO_BLOCKED under §3.

This preserves the status rule and one-pass design while separating the two evidentiary propositions.

**2. Controls — Q2**

Q2. IS THE PROVENANCE FIELD CHECKABLE RATHER THAN ASSERTED?

YES as a documented, independently reviewable classification; NO as a mechanically proven semantic classification. The master expressly acknowledges the latter limit.

Test record, using a hypothetical pinned line “We adopt a = 2 from Smith (2020).”:

    {
      "claim_id": "q1", "input_id": "q1.a", "symbol": "a",
      "status": "PRINTED", "origin": "CHOSEN",
      "origin_evidence": {
        "reason_code": "ORIG_CHOICE_STATED",
        "source_file": "paper.txt", "source_line": 20,
        "verbatim": "We adopt a = 2 from Smith (2020)."
      },
      "derived_from": [], "value": "2",
      "source_file": "paper.txt", "source_line": 20
    }

This is wrong but plausible: “adopt” suggests choice, yet the citation tie-break requires IMPORTED. Value matching, quotation matching and code-to-origin pairing do not establish correct meaning. The second seat should classify it IMPORTED; merge then carries the disagreement. For an arithmetic claim, C6 independently reclassifies every input and should detect the mismatch. For a remaining claim, C6’s provenance reclassification occurs only if it is sampled. If all applicable readers make the same mistake, the mechanism does not catch it. I did not run this record through the unopened validator and do not assert a measured exit status.

C0 requires an exhibition table and independent verification. C1 requires printed counts and a live census run. C2/C3 require printed validator runs; lane-side merge/compute runs join the C3 artifact. C5 requires live outputs. C6 requires the printed audit JSON. C4 and C5b require printed path lists but explicitly permit incomplete self-reports: their PASS is a statement about the list, not proof of actual isolation. C4_PACKET_REDACTED requires the prescribed build. Thus no control is designed to pass on a bare PASS token, although some artifacts necessarily contain human judgments.

The named codes are C0_REACHABILITY, C1_DENOMINATOR_PRINTED, C2_INPUT_LEDGER, C3_NO_SUBSTITUTION, C4_SEAT_ISOLATION, C4_PACKET_REDACTED, C5_HARNESS_PINNED, C5B_NO_CROSS_LANE and C6_AUDIT_SAMPLE. Each specifies PASS/FAIL/NOT_RUN. Unreached controls are NOT_RUN; missing audit seed explicitly leads to AUDIT_FAILED rather than a fabricated pass.

D2 — SUBSTANTIVE: the auditor is exposed to earlier outcomes before its supposedly independent re-derivation.

Verbatim opening of C6’s governing sentence:

> A third independent seat first audits the full candidate and exclusion ledgers against every pinned source — completeness, not just outcomes — then re-derives, without sight of earlier work and re-classifying every input's origin from the pinned sources:

The remainder of that sentence defines the arithmetic-group census, remaining-claim sample, sorting and seed conversion. The conflict is in the quoted ordering: C1’s full candidate ledger contains outcome, printed_value and reproduced_value. A seat cannot read that full ledger first and subsequently re-derive without sight of earlier work.

Exact replacement for the quoted opening, retaining the existing sampling formula and seed definitions:

> A third independent seat first receives only a source-location candidate list and a separately prepared audit assignment containing claim identifiers; neither contains earlier inclusion decisions, exclusions, outcomes, numerical reproductions, input ledgers or origin classifications. The auditor independently enumerates the pinned sources and records inclusion decisions, then independently re-derives each assigned claim and classifies its inputs. The auditor’s enumeration and re-derivation files are hashed and receipted before the full sealed candidate, exclusion and input ledgers are disclosed. After disclosure, the auditor checks completeness and records every comparison in C6_AUDIT.json. The custodian constructs the audit assignment as follows:

This changes actual exposure and therefore is not cosmetic.

**3. Circularity**

The inclusion rule does not reference a hypothesis or comparison model. Two independent enumerations, complete exclusion reporting and the full-source completeness audit obstruct quiet removal of a contrary claim. A surviving disagreement stops the census visibly.

Human judgments remain in identifying an asserted result, interpreting origin evidence and assessing input completeness. C3 states that its semantic checks are human checks; they do not become circular merely because they involve judgment. D1 supplies inconsistent instructions to those judgments, and D2 exposes the auditor to prior results. Both need repair.

The interpretation step is separated and receipted before enumeration. Its contents were not opened, as instructed. I can assess its custody design but cannot certify the fairness or completeness of the unseen mapping. No conclusion about a pattern follows from this review.

**4. The blind**

I independently extracted master sections 1–6, 9 and 11, removed SEAT-REDACT spans, and compared the result with the packet body after splitting on whitespace. Result: NORMALIZED_OPERATIVE_EXTRACTION_MATCH=True.

The packet contains none of these tested strings: rests_on, DERIVED_ONLY, USES_CHOSEN, ΛCDM, Tori, Blanc, Duho, pattern. These are my checks, not a claim that I executed the builder’s complete forbidden list.

The packet therefore exhibits the described redaction. The builder’s asserted behavior and digest remain unverified because opening or executing that additional script would exceed the permitted document reads. Its presence was checked by metadata only.

C4 honestly limits its claim: “C4_SEAT_ISOLATION=PASS certifies the contents of the printed list and of the dispatch copy, not actual non-access.” The structural copy and list can support that limited statement; they do not enforce blindness. The kernel-sandbox assertion supplied in the question does not establish that the operative procedural control has become a complete access monitor. No sandbox profile was opened or independently exercised here.

D3 in section 7 identifies the remaining scope and package-pin defect. It matters both to executability and to what external code can influence the seat.

**5. The seal**

The receipted relay is correctly ordered in the written design. Receipt P binds the interpretation protocol before limb A; receipt T binds the named tally commit and its files before the protocol is opened for comparison. Both receipts and the four verified hash/commit values must be printed. Missing receipts or mismatches stop interpretation and file CENSUS_AUDIT_FAILED.

This binds identifiable records, conditional on execution and an independent custodian. It does not prove lack of prior knowledge, and the master says so. I did not verify actual receipts, commit contents or the unseen protocol. No new seal defect is established from the authorized documents.

**6. Fairness**

REPRO_FAILED explicitly requires “unreproduced from the stated inputs,” not “error.” The brief applies that wording to negative outcomes generally. BLOCKED, INPUT_ABSENT, NO_DERIVATION_STATED and NOT_EVALUABLE describe census limitations rather than alleging a paper’s error. CENSUS_COMPLETE means completion of arithmetic evaluation, not universal reproduction success.

I checked every REPRO_EXACT hit using a line-numbered search together with section headings. The sole pre-history occurrence is the rename notice at master line 118. All remaining hits belong to §10 or its subsections. No governing old-token reference was found. I did not need the optional rename-audit file.

D4 — COSMETIC under the requested criterion: DERIVED_ONLY overstates its membership if read as ordinary English.

Verbatim sentence:

> (Master only — the rule the script implements: DERIVED_ONLY when every root origin is DERIVED, STANDARD or MEASURED; otherwise the most severe root origin present, in the fixed order USES_UNDECLARED > USES_IMPORTED > USES_FITTED > USES_CHOSEN.

A claim resting solely on a measured input meets the definition despite not being derived-only. The definition is explicit, so this is a label problem, not a newly demonstrated classification failure.

Exact replacement:

> (Master only — the rule the script implements: the legacy token DERIVED_ONLY denotes DERIVED_STANDARD_OR_MEASURED_ONLY, meaning every root origin is DERIVED, STANDARD or MEASURED; display that expanded meaning beside the token in every tally and interpretation report; otherwise use the most severe root origin present, in the fixed order USES_UNDECLARED > USES_IMPORTED > USES_FITTED > USES_CHOSEN.

This retains the token, membership, tests and interpretation mapping. It changes no class filed or tested value. It does not drive the UNSOUND verdict.

**7. Stall and executability — Q4 and Q7**

Q4. CAN ANYTHING THE DOCUMENT DESCRIBES NOT BE EXECUTED AS DELIVERED?

YES: the live harness executes, but its imports cannot all comply with the stated scope; see D3. D1 also prevents consistent provenance encoding for the constructed imported-choice claim.

The 120-second wrapper and explicit non-evaluable outcomes provide a termination design. Their implementation was not executed. The seat-day estimates are estimates, not guaranteed completion limits.

Q7(a), live C5 test. These are the actual five commands, full stdout and exit statuses:

    /usr/bin/python3 --version
    Python 3.9.6
    exit=0

    /usr/bin/python3 -c "import sympy; print(sympy.__version__)"
    1.14.0
    exit=0

    /usr/bin/shasum -a 256 /usr/bin/python3
    b8763cf250e607a778bb4603cecb5b90338814d0a3dfcba0d57b1de242f610e9  /usr/bin/python3
    exit=0

    /usr/bin/python3 -c "import sympy; print(sympy.__file__)"
    /Users/duhokim/Library/Python/3.9/lib/python/site-packages/sympy/__init__.py
    exit=0

    /usr/bin/shasum -a 256 /Users/duhokim/Library/Python/3.9/lib/python/site-packages/sympy/__init__.py
    4e9476348ba105feab28d82f5bcf6cdba2e3e84de6e059bbfe7a13728c0a4ab0  /Users/duhokim/Library/Python/3.9/lib/python/site-packages/sympy/__init__.py
    exit=0

No stderr was returned. This proves command execution on this host, not C5_HARNESS_PINNED=PASS: no dispatch-record pin was supplied for comparison.

A follow-up inspection of the already imported modules’ metadata printed:

    LOADED_MPMATH=/Users/duhokim/Library/Python/3.9/lib/python/site-packages/mpmath/__init__.py
    LOADED_SYMPY_CORE=/Users/duhokim/Library/Python/3.9/lib/python/site-packages/sympy/core/__init__.py
    STARTUP_SITECUSTOMIZE=None
    STARTUP_USERCUSTOMIZE=None

This inspection imported SymPy and read sys.modules metadata; it did not separately open source files for review. It is not a complete file-access trace.

D3 — SUBSTANTIVE: a single module-file hash neither admits the dependency closure nor pins the package.

Verbatim C4 sentence, with Markdown delimiters omitted:

> The two system binaries C5 names — /usr/bin/python3 and /usr/bin/shasum — are IN SCOPE, together with (a) the files they load from the system runtime locations /usr (excluding /usr/local), /System, /Library, /private/var/folders and /dev, and (b) the SymPy package at the single path C5 prints, pinned by the digest C5 prints and recorded in the dispatch record before launch — while executing the commands this document mandates the seat to run (the C1 census runs, the C2/C3 validate runs, the C5 harness commands, and the §9 wrapper invocations).

C5 prints a file, sympy/__init__.py, not a package-tree digest. Even generously interpreting “package” as permitting SymPy’s sibling modules, mpmath is a separate package outside every admitted runtime prefix. A seat obeying the text therefore cannot both import the installed SymPy and pass C4/C5b.

The pin merely names part of the user-writable-path problem. Changing sympy/core/__init__.py or mpmath/__init__.py leaves the printed SymPy initializer hash unchanged. Seat-read-only access prevents seat writes; it does not bind all loaded bytes against changes by another writer. Imports also execute before the proposed digest comparison.

Q7(b)(i): the bound does not completely close the startup/import hole. It excludes /usr/local explicitly and forbids other outside startup loads, but the allowed /private/var/folders prefix can contain user-writable temporary code. A PYTHONPATH-directed startup file under such a directory is not excluded by the location allowlist itself. The self-reported lists are not complete detection. I did not plant or execute such a file.

Q7(b)(ii): the bound is too tight for the observed dependency closure. The excluded needed path is /Users/duhokim/Library/Python/3.9/lib/python/site-packages/mpmath. A strict single-file reading also excludes SymPy’s own submodules.

Q7(b)(iii): C4 and C5b are substantively aligned. The brief says “SymPy package at the single path C5 prints” but omits the explicit digest/dispatch wording. Its final sentence, “where a rule and this brief differ, the packet governs,” makes the packet’s stronger pin requirement controlling. All three share the missing-dependency problem.

Exact replacement for C4’s quoted exception and its following outside-load sentence:

> The system binaries /usr/bin/python3 and /usr/bin/shasum are IN_SCOPE while executing mandated census, validate, harness, source-hash and wrapper commands. Their system runtime files may load from /usr excluding /usr/local, /System, /Library and /dev. Executable startup, configuration and import files are not admitted merely because they reside under /private/var/folders. Before dispatch, provision a read-only runtime copy containing SymPy and its complete non-system dependency closure, including mpmath. Record every admitted file’s resolved path and SHA-256 in a runtime manifest receipted before launch. Verify that manifest before importing any of those packages, disable unlisted startup hooks and import locations, and ensure that the verified bytes cannot change during the run. Only the manifest-listed non-system files are IN_SCOPE; other outside loads are FAIL. Deliver and pin the manifest verifier and launch configuration with the seat tools before dispatch.

Exact replacement for C5’s governing instruction and PASS predicate:

> Print the interpreter version and digest and verify the complete runtime manifest before importing SymPy. Launch the version and module-location probes through the delivered restricted launch configuration, and print the SymPy and mpmath versions and resolved locations. C5_HARNESS_PINNED=PASS requires every command to exit 0, every runtime-manifest digest to match the pre-launch dispatch record, and every imported non-system file to be manifest-listed. Print commands, stdout, stderr and exit statuses; any mismatch, missing output, unlisted load or transcribed output is FAIL.

Exact replacement for the scope echo in C5b and the brief:

> Runtime access is governed by C4’s pre-launch runtime manifest and restricted launch configuration; only its admitted system files and individually verified non-system files are IN_SCOPE during the commands C4 names.

These are proposed replacements, not claims that the additional verifier/configuration already exist. Their implementation and live verification are prerequisites to accepting the repair.

Q7(c), comparison evidence:

I ran diff against the explicitly permitted V23 file, whose SHA-256 is 55b466fadf8ca75f4894f97721da86584057ddc4d15c15ca1739c67ff6333c6f. In operative master sections, changes are confined to C4, C5 and C5b: the runtime exception, /usr/local exclusion, named command contexts, path-qualified shasum, two additional harness commands and path/digest mismatch failure. The header changed; the V23 history row changed; a V24 row and §10.18 were added. No other operative-section change appears in that diff. Therefore “only C4 and C5b changed” is literally incomplete: C5 changed too.

The brief’s current SHA-256 is be72223b4b279e5c961bf856693767d122faabe78468c7fda9f4d21b2a09c1fd. A prior brief and a round-2 master were not among the supplied comparison files. I cannot independently certify “nothing else changed versus round 2.” The V23-to-current diff bounds the cumulative master changes; §10’s account is not a substitute for a round-2 diff.

Q4 verification inventory and limits:

| Item | Check and result |
|---|---|
| Master and packet | Opened; full SHA-256 values above; master read in full using overlapping chunks to recover truncated output. |
| Seat brief and V23 snapshot | Opened under the explicit exceptions; hashed; V23 diff inspected. |
| r3c2_ledger_tools.py | Metadata: exists, 11,782 bytes. census, census final and validate commands reviewed in the documents; implementation, digest and computed checks not executed. |
| r3c2_lane_tools.py | Metadata: exists, 5,058 bytes. merge/compute interfaces and claimed origin_alt, origin_evidence_alt, PARENTS_DISPUTED, root_origins and rests_on behavior reviewed textually; implementation unverified. |
| r3c2_timeout.py | Metadata: exists, 1,760 bytes. Literal wrapper command and timeout contract reviewed; implementation and pin unverified. |
| r3c2_build_seat_packet.py | Metadata: exists, 7,517 bytes. Build command reviewed; independent extraction comparison passed; builder execution and pin unverified. |
| R3C2_CORPUS_MANIFEST.md | Metadata: exists, 21,182 bytes. Contents and individual source paths/digests not opened or verified. |
| R3C2_SEAT_PACKET.sha256 | Root-path metadata: exists, 461 bytes. Contents not opened; packet/tool pins not independently compared. |
| R3C2_INTERPRETATION_PROTOCOL_20260904.md | Metadata: exists, 3,454 bytes. Contents deliberately unopened. |
| C5 interpreter, SymPy initializer and shasum | Five live commands and hashes printed above; loaded dependency paths inspected. |
| Dispatch directory and inventory | No actual dispatch directory was supplied. Packet staging directory lacks local copies of the manifest, pin file, ledger script and timeout wrapper; the master requires a later assembled external copy, so this alone is not proof of a missing dispatch artifact. |
| Candidate/exclusion/input ledgers, compute output, C6_AUDIT.json, receipts P/T, seed, SEAT_REPORT.md and check sheet | Prospective run artifacts, not evidence that a census has already executed. Neither existence nor correctness asserted. |
| Third-seat dispatcher/provider log | Explicitly administrative lane-side procedure; not claimed executable by a seat. Not inspected. |

Opening or executing the unopened scripts would read files outside the user’s permitted set. Consequently this report does not falsely certify every implementation or every manifest member as delivered and correct. No missing root-level operative artifact was established by the allowed metadata checks. The demonstrated scope failure, conflicting provenance evidence rule and auditor-exposure ordering are sufficient to reject the design as written.

R3C2_V24C_GATE_COMPLETE

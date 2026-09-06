ACCESS_SHA=f4edb5145b5c150c43a6550b30f0beca1d08bf4675305383e7860c3657f951fd
PACKET_SHA=5fc8d8349450af40cb73c1b6215404b755055242f9785e280c328619cba7f0d3
GATE=PREREG_UNSOUND
LEAK=Provenance matters independently of numerical reproduction; no directional hypothesis, comparison model or preferred empirical outcome is recoverable.
CONSEQUENCE_VISIBLE=Procedural only: CENSUS_AUDIT_FAILED says “No tally is filed; report which.” No empirical consequence to the lane is disclosed.
ORIGIN_PURPOSE=Independent classification and audit: “the auditor re-derives each assigned claim and re-classifies each of its inputs' `origin` from the pinned sources”; its downstream interpretive purpose cannot be stated.
C5_EXECUTABLE_UNDER_SCOPE=YES
NO_MASKED_STAGE=YES
CANDIDATE_DIFF_ONLY=NO

Packet-first answers, recorded before reading the master:

Q5. No packet sentence identifies a preferred empirical outcome or says that one result supports or harms the lane. “No tier, warrant token, standing or stamp moves” explicitly denies those consequences. Under the question's literal “to anyone” wording, procedural consequences ARE visible: “No tally is filed; report which.” My initial packet-only answer distinguished these procedural consequences from an undisclosed empirical stake; the header makes that distinction explicit.

Q6. The packet states an immediate use: independent origin classification, comparison and disputes. Its C6 sentence says the auditor “re-classifies each of its inputs' `origin` from the pinned sources”. It does not state a provenance summary, comparison rule or interpretive use. Thus I can state its checking purpose, but cannot state its ultimate interpretive purpose. This preserves the distinction in my pre-master answer; it does not infer purpose retrospectively from the master.

Q3. “The reproduction verdict and the provenance fields are recorded separately” reveals interest in provenance as well as arithmetic. The detailed origin taxonomy and the sentence “Every input's `origin` is classified independently by both seats” reinforce that inference. “The cosmological rows are the Planck 2018 TT,TE,EE+lowE+lensing baseline” identifies a cosmological context. None supplies a direction, a preferred provenance class, a comparison model, or a hypothesis-to-outcome mapping. The special coverage of every arithmetic-group claim shows an audit allocation, not whether successful or unsuccessful reproduction is desired. I cannot reconstruct the empirical stake. These content-level inferences are not additional blinding defects.

This is a design gate on the unadopted integrated candidate. Section 10 supplies no evidence for my verdict. I opened no prior gate file. The later Q7 instructions were treated as explicit exceptions to the initial two-file restriction for the V25 diff, delivered tools, pins, brief and execution checks. All numerical work below uses synthetic fixtures, not corpus reproduction. No adoption, freeze, census or external relay was performed.

## 1. Outcome classes — Q1

Q1. DOES SECTION 3's DEFINITION, AS WRITTEN UNDER OPTION (c), MAKE EVERY DECLARED OUTCOME REACHABLE AND KEEP THE REPRODUCTION QUESTION DECIDABLE?

At the definition level, yes: status determines consumption and origin does not veto arithmetic. At the integrated executable-contract level, no: F1 and F2 prevent legitimate cases from reaching their specified dispositions through the required controls. This is not a request to reconsider option (c).

Concrete claims illustrating the six definitions:

| Claim and circumstances | Unique per-claim outcome | rests_on |
|---|---|---|
| Paper chooses a = 3 m and states y = 2a = 6 m | REPRO_WITHIN_STATED_PRECISION | USES_CHOSEN |
| Same recipe/input, printed result 7 m | REPRO_FAILED | USES_CHOSEN |
| y = 2a = 6 m, a not printed, named source outside the manifest | REPRO_BLOCKED | USES_IMPORTED |
| y = 2a = 6 m, a neither printed nor traced to a source; an adequate silent search is recorded | REPRO_INPUT_ABSENT | USES_UNDECLARED |
| Sufficient stated inputs, but a specified computation reaches the wrapper deadline | REPRO_NOT_EVALUABLE | Determined by those inputs, e.g. USES_CHOSEN |
| “Our result is 6 m,” with no operations stated and no input records | REPRO_NO_DERIVATION_STATED | NOT_COMPUTED by the text; missing from the implementation |

These are concrete mathematical counterexamples, not purported quotations or findings from an unread corpus paper. A printed fitted a = 3 gives 6 under the same recipe and files REPRO_WITHIN_STATED_PRECISION / USES_FITTED. In my external-import fixture the claiming sentence is “We use a from t12.” and the source says “We choose a = 3 for this calculation.” Validation passes; the claim is REPRO_WITHIN_STATED_PRECISION / USES_IMPORTED. The external source's choice does not change the claiming paper's IMPORTED classification.

Overlapping terminal conditions are resolved: y = a+b with a traced to an unpinned source and b entirely absent satisfies both input obstacles but files REPRO_BLOCKED, because BLOCKED precedes ABSENT. An unspecified procedure with those obstacles files REPRO_NO_DERIVATION_STATED first. Arithmetic success uses the stated uncertainty or rounding predicate; failure is its complement. I found no unassigned ordinary numerical case in the definitions themselves.

Study classes are also exclusive once their explicit precedence is applied:

| State, with earlier stop conditions absent | Filed class |
|---|---|
| N=1, arithmetic outcome, audit PASS | CENSUS_COMPLETE |
| N=1, blocked outcome, successful audit of that obstruction | CENSUS_PARTIAL |
| Audit mismatch or missing seed | CENSUS_AUDIT_FAILED |
| C3 fails twice in every attempting seat | R3C2_NO_CLASS |
| Persistent candidate inclusion or input-list disagreement | CENSUS_DENOMINATOR_DISPUTED |
| Persistent outcome disagreement | CENSUS_OUTCOME_DISPUTED |
| Origins disputed on 2 of 10 included claims | CENSUS_ORIGIN_DISPUTED |
| C3 fails twice in one seat and passes in the other | CENSUS_CONTROL_SPLIT |

A tally with a blocked claim and an audit mismatch satisfies both partial and audit-failure conditions, but files only CENSUS_AUDIT_FAILED. INCONCLUSIVE is genuinely reachable through a nonempty partial census, with valid BLOCKED input records and an audit that confirms the obstruction. Zero denominator with excluded candidates instead triggers C6's explicit zero-denominator failure; zero denominator with no candidates encounters F2.

F1 — NON-COSMETIC: locally printed cited values are rejected, while a wrong origin can pass.

Verbatim rule: “Where a value the paper prints is on the closed list verbatim, file `STANDARD`; otherwise `PRINTED` — the two routes are outcome-identical, and this rule keeps both seats on the same one.”

Verbatim origin rule: “Where more than one reason code matches the cited sentence, file the first in this order: `ORIG_CITATION`, `ORIG_FIT_STATED`, `ORIG_CHOICE_STATED`, `ORIG_MEASURED`, `ORIG_EQUATION`, `ORIG_CONSTANT`, `ORIG_SILENT` — a sentence that names an external source for the value is a citation whatever else it says — the order is a tie-break by the specificity of the evidence, not a ranking of the values.”

My claiming paper prints “We adopt a = 3 from t12.” The correct record is PRINTED / IMPORTED / ORIG_CITATION, with the value and quotation at its own line. The staged validator branches on every PRINTED ORIG_CITATION record, not on an externally located value. It returns exit 1: “IMPORTED PRINTED record names its own file as the external source”. Relabelling the same locally printed record CHOSEN / ORIG_CHOICE_STATED passes. Thus the new external-import checks incorrectly reject an input the paper itself prints. The mechanical disposition should be REPRO_WITHIN_STATED_PRECISION / USES_IMPORTED; neither BLOCKED nor ABSENT describes this input.

Exact replacement for the §2 sentence beginning “The origin records the claiming paper's import”: “A locally printed value may have origin IMPORTED: when source_file equals the claiming file, validate checks the locally printed value and the claiming paper's citation quotation without requiring a different source file. The external-source manifest, numeric-token and first-line checks apply only when source_file differs from the claiming file. In that external case the origin records the claiming paper's import regardless of how the external source obtained the value; no reason code is applied to the source's line.” Implement that branch distinction and re-pin the tool.

F2 — NON-COSMETIC: legitimate empty ledgers and NOT_COMPUTED are not implemented.

Verbatim: “`rests_on` is computed and reported for every included claim that has at least one ledger record, whatever its outcome; a claim with no ledger record carries `rests_on` `NOT_COMPUTED`, and the `rests_on` tally reports a `NOT_COMPUTED` row.”

Both the staged validator and lane tool assert that the record list is nonempty. My empty ledger returns exit 1 with AssertionError. Moreover, compute receives no candidate file and iterates only claims present in records, so it cannot emit absent claims as NOT_COMPUTED even in a mixed census. A source asserting a result without stating any derivation legitimately produces no input records. Inventing a record to pass C3 would violate the design.

Exact replacement: “Empty records lists are valid. validate and merge accept them. compute takes the agreed candidate file as its third argument, emits exactly one claims entry for every included candidate, and writes rests_on=NOT_COMPUTED for each candidate with no records; excluded candidates receive no entry. The reported rests_on counts must sum to the included denominator.” Replace both lane-side compute invocations with `/usr/bin/python3 -E r3c2_lane_tools.py compute <merged.json> <out.json> <candidates.json>`, implement these requirements and re-pin.

## 2. Controls — Q2

Q2. IS THE PROVENANCE FIELD CHECKABLE RATHER THAN ASSERTED?

Partly. The external-file binding is effective, but a matched quotation is not a semantic classifier. Here is the complete plausible wrong record I executed:

```json
{"claim_id":"t02.txt#c1","input_id":"t02.txt#a","symbol":"a","status":"PRINTED","origin":"CHOSEN","origin_evidence":{"reason_code":"ORIG_CHOICE_STATED","source_file":"t02.txt","source_line":1,"verbatim":"We adopt a = 3 from t12."},"derived_from":[],"value":"3","source_file":"t02.txt","source_line":1}
```

It returns C3_NO_SUBSTITUTION=PASS, exit 0. “Adopt” makes CHOSEN plausible, but the citation takes precedence, so IMPORTED is correct. The second reader's independent classification catches the error if that reader applies the precedence correctly; C6 can catch it on a selected claim by reclassification. If all readers make the same mistake, it stands. That semantic limit is explicitly admitted in the master and is not itself a new defect.

A different wrong record puts the value in t12.txt while claiming CHOSEN and quoting the external “We choose” sentence. That fails mechanically: the candidate binds the claim to t01.txt, so an external value must be IMPORTED / ORIG_CITATION. This is a working new safeguard.

C0 requires an exhibition plus independent verification; C1 requires printed counts and census execution; C2/C3 require printed validator runs; C4 isolation and C5b require printed self-reported path lists; C4 redaction requires builder execution; C5 requires live harness output; C6 requires sealed files and printed comparison output. Unreached controls explicitly file NOT_RUN. Printed path lists can be incomplete without failing C4/C5b, exactly as their bounded predicates say. They do not certify complete access logs.

F3 — NON-COSMETIC: STANDARD evidence can be fabricated without the promised quotation check.

Verbatim: “Every record carries `origin_evidence` with a reason code — `ORIG_CHOICE_STATED`→`CHOSEN`, `ORIG_EQUATION`→`DERIVED`, `ORIG_FIT_STATED`→`FITTED`, `ORIG_CITATION`→`IMPORTED`, `ORIG_MEASURED`→`MEASURED` (a quantity the paper reports as its own measurement, with the measurement described), `ORIG_CONSTANT`→`STANDARD`, `ORIG_SILENT`→`UNDECLARED` (listed alphabetically by origin; the list carries no order of its own) — and, except for `ORIG_SILENT`, a **verbatim quotation machine-matched to the cited line**.”

The validator checks STANDARD membership but never reads its evidence line. My STANDARD c=2.99792458e8 record cites nonexistent line 99 and verbatim “fabricated quotation”; it passes C3, exit 0. BLOCKED evidence likewise has no quotation-matching branch. This exceeds the admitted semantic-classification floor: even the promised byte-level evidence check is absent. A value can therefore be supplied by assertion on the STANDARD route despite §2's printed-value condition.

Exact replacement: “For every record except ORIG_SILENT, validate requires a nonempty quotation and machine-matches it at origin_evidence.source_file/source_line, independently of status. For STANDARD it additionally verifies the value's presence in the claiming text or the applicable external-import source, as well as closed-list membership. For BLOCKED it checks the claiming paper's naming quotation while requiring an empty value.” Implement those checks and re-pin.

F4 — NON-COSMETIC: transitive disagreement is not propagated to dependent claims.

Verbatim: “A claim whose root-origin set contains an `ORIGIN_DISPUTED` input carries `rests_on` computed under both classifications, printed as a pair and marked `DISPUTED`; the `rests_on` tally reports a `DISPUTED` row.”

I executed compute with t01.txt#derived depending on t12.txt#p, whose two origins are CHOSEN and MEASURED. The parent claim prints ['USES_CHOSEN', 'DERIVED_ONLY'], DISPUTED. The dependent claim prints only USES_CHOSEN. compute marks a claim disputed only when one of that claim's own records carries an alternate field; it does not propagate dispute status from referenced records belonging to another claim. Cross-claim dependencies are allowed by the global graph and batch join.

Exact replacement: “compute propagates dispute status through the complete dependency graph, including dependencies belonging to other claims. Every claim reaching an origin_alt or PARENTS_DISPUTED record receives both computed root-origin sets and both rests_on values and is marked DISPUTED, even when the two resulting labels happen to coincide.” Implement graph propagation and re-pin.

F5 — NON-COSMETIC: JOIN and the no-fallback control lack a complete result contract.

Verbatim: “Either FAIL stops the seat's tally.” C1B names JOIN=PASS but does not declare JOIN=PASS|FAIL|NOT_RUN or explicitly place JOIN failures in §4's control classes.

Exact replacement: “JOIN=PASS|FAIL|NOT_RUN. JOIN is a C1B control for §4: failure in every attempting seat after two attempts files R3C2_NO_CLASS; a surviving fail/pass split files CENSUS_CONTROL_SPLIT; an unreached join is NOT_RUN. C1B_BATCH_COVERAGE follows the same filing rules.”

Verbatim §9 passage: “Lane-side procedure, not the seat's: the no-fallback control is the provider log showing no fallback line for the seat's session, checked by the lane owner; a one-page check sheet `R3C2_CHECK_SHEET_<date>.md` in plain words with source lines is written by the lane owner after the tally; the lane owner runs `r3c2_lane_tools.py` (sha256 `8e990c7a22fb4b093d5e74218e9bfcee4b108c52bbc2df615ed3b6b2aaefa848`; merge, then compute) after both seats exit and re-runs every script; a critic note precedes any ruling.”

The no-fallback control has no exact code, missing-log predicate or study-class routing. Exact replacement for its first clause: “Lane-side procedure: C5C_NO_FALLBACK=PASS|FAIL|NOT_RUN requires a printed, session-identified provider log for every session; a missing log or any fallback entry is FAIL, and an unreached check is NOT_RUN. Treat C5C as a pre-tally control under the R3C2_NO_CLASS and CENSUS_CONTROL_SPLIT rules.” Retain the remaining check-sheet, script and critic requirements.

## 3. Circularity

The inclusion definition does not reference a lane hypothesis. Independently retained exclusions, zero-tolerance census-seat reconciliation and the auditor's source-only enumeration reduce a route for quietly dropping contrary claims. The lane's interpretation receives two sealed tallies only after the prereceipted protocol and tally custody steps.

For the three new method texts:

- D1 binds the claiming file and external evidence. It does not reveal a preferred outcome. Its local-citation regression is F1; its intended external “we choose” case works.
- C6 independently enumerates all texts before receiving seat ledgers, then seals re-derivations before release. My extra auditor passage produces OMISSION and CENSUS_AUDIT_FAILED even though both census seats omitted it. If all three readers omit a passage, it is absent from the union and remains undetectable; that is the expressly admitted shared-reader-error floor, not machine proof of corpus completeness.
- Ownership batching changes which session owns a claim, while preserving full source access. The batch-1 import from batch 12 validates and joins successfully. No outcome-dependent batch selection is prescribed.

No new method authorizes the lane to revise evidence to fit its expectation. However, F1, F3 and F4 show that the implemented evidence protections do not meet the written rules. The audit's printed JSON establishes equality of recorded outcomes and origins, not proof that a human independently reasoned correctly. A fabricated but matching re-derivation JSON can pass the comparator; the source-work and custody requirements, not JSON equality, make that fabrication noncompliant. I do not misreport that admitted human-work boundary as automatic verification.

A contrary claim cannot be excluded compliantly merely for contradicting the lane. It can still be missed or misclassified by all readers. Inclusion disagreements within C6's stated 10% tolerance are reported rather than silently erased; that is the specified method, not a threshold I am changing.

## 4. The blind

The redaction transformation is machine-asserted at its stated lexical strength. I loaded the pinned builder, explicitly bound MASTER to this candidate, BRIEF to the candidate brief, and OUT to my fixture directory. It returned C4_PACKET_REDACTED=PASS, removed 51 spans, and produced bytes identical to the delivered candidate packet. No forbidden-list or required-content assertion failed. This verifies the transformation; it is not a successful run of the different default build command printed in C4, addressed in F8.

C4 honestly limits self-reported path lists, digest snapshots and prior exposure. It does not honestly describe the actual pinned kernel profile in one operative sentence.

F6 — NON-COSMETIC: the pinned confinement profile permits outside reads and writes that the text says it denies.

Verbatim: “**Confinement, as of V24:** each seat is dispatched inside a kernel sandbox profile (`r3c2_seat_sandbox.sb`, sha256 `6978d590bf2acc519f00f38e8bc71b0e9ef476b95eeb6afa38443dbaef731fa6`) that denies reads outside the working directory and the pinned environment and denies all writes outside the working directory; the profile's digest and its live positive and negative probes (a pinned source read; the lane master, an outside file and a listing of the lane refused with "Operation not permitted") are printed in the dispatch record before launch.”

That exact profile also allows user configuration directories, multiple runtime roots, network access, and writes under /private/var/folders, .codex and .hermes. Under the pinned profile with WORKDIR set to my fixture directory, my Python child read and rewrote a fixture outside WORKDIR under /var/folders; exit 0, OUTSIDE_WRITE=SUCCEEDED. Only my own temporary file was accessed. One denied outside-file probe cannot establish the universal denial claimed here.

Exact replacement: “The dispatch record prints the pinned profile's complete effective read, write and network exceptions. This profile permits runtime and temporary-directory access beyond the seat working directory, including the documented configuration-directory exceptions; it does not deny all outside reads or writes. Its positive and negative probes establish only the tested accesses. C4 and C5b additionally prohibit seat-chosen data access outside the working directory and pinned environment, but enforce that rule only through self-report. The lane master and withheld interpretation material must each have a recorded denied-read probe before dispatch.” This makes the limit honest; a stronger confinement claim requires a narrower profile and new pins/probes.

## 5. The seal

Receipt P precedes limb A and binds the interpretation protocol hash and commit id. Receipt T binds the named tally commit and its files before the interpretation opens. Both receipts must be printed, and the external custodian independently verifies the four values. A send alone is explicitly insufficient. A missing receipt or mismatch files CENSUS_AUDIT_FAILED and leaves interpretation NOT_RUN.

This binds recorded bytes before the steps the clauses name. It cannot show that the protocol author did not anticipate results, and the text explicitly says so. The C6 stage seals are local digest commitments whose ordering depends on the recorded custody/release sequence; the candidate now states that limitation. The synthetic sequence verifies seal and comparison mechanics, not real receipts or an actual dispatch. The interpretation protocol's path exists; I did not open its contents. Receipts, dispatch logs and final tallies are future run artefacts, not falsely reported here as already delivered.

## 6. Fairness

REPRO_FAILED explicitly requires “unreproduced from the stated inputs,” not an accusation of paper error. The brief extends that wording to negative outcomes. BLOCKED, ABSENT, NO_DERIVATION_STATED and NOT_EVALUABLE identify census limitations; no study class by itself asserts a hypothesis verdict. The precision-based success name matches the uncertainty/rounding definition.

F7 — NON-COSMETIC under the requested conclusion/name test: DERIVED_ONLY overstates its definition.

Verbatim: “DERIVED_ONLY when every root origin is DERIVED, STANDARD or MEASURED”. A single own-measurement root computes DERIVED_ONLY, although it was measured, not derived. This does not change arithmetic membership, but the exported interpretive label asserts more than its definition.

Exact replacement: “DERIVED_STANDARD_OR_MEASURED_ONLY when every root origin is DERIVED, STANDARD or MEASURED”. Rename the emitted token and all operative consumers without changing its membership predicate. This is a proposed repair for the principal, not an adopted taxonomy change. Section 10's account of earlier label discussions played no role in this finding.

## 7. Stall / executability — Q4 and Q7

Q4. CAN ANYTHING THE DOCUMENT DESCRIBES NOT BE EXECUTED AS DELIVERED?

Yes. Besides F1–F4, the literal validation commands, candidate build/pins and batch-session instructions do not form a consistent executable delivery. C5 itself is executable under C4's explicit mandated-command exception. NO_MASKED_STAGE=YES means the mandated commands are not shell pipelines and checked child failures propagate; it does not mean every semantic check is implemented correctly.

F8 — NON-COSMETIC: stale commands and candidate assembly references.

Verbatim C2 command sentence: “Every input classified `PRINTED` / `STANDARD` / `ABSENT` / `BLOCKED`, each `PRINTED` one carrying file and line, in the JSON schema of C3, validated by `/usr/bin/python3 -E r3c2_ledger_tools.py validate <ledger.json> .` run from the printed seat working directory (`.` is the sole allowed `sources_dir`); before execution the seat prints the fully resolved command with every angle-bracket placeholder replaced by the actual in-scope path (exit 0 = PASS; every failure printed; the printed C3 run — command, stdout, stderr, exit status — is this control's artefact).”

The corresponding C3 sentence begins: “Each seat runs `/usr/bin/python3 -E r3c2_ledger_tools.py validate <ledger.json> <sources_dir>` with the placeholders resolved”. Both omit the candidate argument newly required by §3. My valid external-import fixture fails under that two-argument form, exit 1, C3_NO_SUBSTITUTION=FAIL.

Exact replacement in both locations: `/usr/bin/python3 -E r3c2_ledger_tools.py validate <ledger.json> . <candidates.json>`. Retain the requirements to resolve paths and print command, working directory, stdout, stderr and exit status. Make the brief use the same command.

Verbatim: “Build command, run from this directory: `/usr/bin/python3 -E r3c2_build_seat_packet.py`; expected first line of output `C4_PACKET_REDACTED=PASS`, then the master and packet digests.”

The pinned builder hard-codes the V25 master and r3c2_seat_packet output/brief. The root pin sheet also binds that other packet and the old ledger-tool digest. There is no R3C2_SEAT_PACKET.sha256 beside the candidate packet. The candidate directory also lacks its named interpreter scripts and corpus manifest. The user explicitly permits staging the ledger tool under its STAGED name until adoption, so that rename alone is NOT a finding; the contradictory command/pin assertions are.

Exact replacement: “For this unadopted candidate, build from R3C2_V26_INTEGRATED_CANDIDATE_UNADOPTED_20260906.md into r3c2_seat_packet_v26_candidate/R3C2_SEAT_PACKET.md using its adjacent SEAT_BRIEF.md. The builder accepts explicit --master, --out and --brief arguments. Run `/usr/bin/python3 -E r3c2_build_seat_packet.py --master R3C2_V26_INTEGRATED_CANDIDATE_UNADOPTED_20260906.md --out r3c2_seat_packet_v26_candidate/R3C2_SEAT_PACKET.md --brief r3c2_seat_packet_v26_candidate/SEAT_BRIEF.md`. Generate a candidate-specific R3C2_SEAT_PACKET.sha256 binding the candidate packet, brief and intended dispatch-script bytes. The review packet directory is not an assembled seat working directory; before dispatch, copy and verify every C4 inventory item into the isolated flat working directory. Do not use the V25 packet or its pin sheet for this candidate.” Implement those builder arguments, re-pin it and rebuild.

The manifest contains 89 enumerable flat filenames. None exists at its literal path relative to the current lane working directory; none of those flat source paths is furnished beside the candidate packet either. This establishes a missing flat dispatch assembly at the checked locations, not that the corpus is absent everywhere in the lane. I did not search unrelated directories. The replacement above explicitly assigns and verifies the required assembly before dispatch; a future unperformed dispatch is not a claimed PASS.

F9 — NON-COSMETIC: C5's manifest silently omits symlinks.

Verbatim: “The five commands establish the interpreter every ledger command runs under and the one site-packages directory it loads from, whose path and `MANIFEST_SHA256` the dispatch record pins before launch — the digest covers every file under that directory, everything the mandated imports can load from it, not one initializer.”

The pinned manifest script skips symlink files and does not follow symlink directories. My fixture directory contained a symlinked Python file. Before and after changing its target, the manifest returned FILES=0, the same empty digest, exit 0. Thus the claimed coverage is false even at a snapshot, independently of the honestly stated between-snapshot limitation.

Exact replacement: “The manifest command fails with ERROR=<path> and exit 1 on any symlink or non-regular entry, including symlink directories, rather than silently skipping it. PASS therefore pins every regular file in a directory tree containing no skipped entries. Any importable content outside that tree must be separately inventoried in the dispatch's pinned environment; the directory digest alone does not certify all interpreter load locations.” Implement the fail-closed traversal and re-pin.

F10 — NON-COSMETIC: the declared brief gap and batch phase/seal lifecycle need an executable specification.

Verbatim brief: “Limb A: enumerate every candidate passage under the packet's section 1 rule; record inclusion or exclusion for each in the candidate and exclusion ledgers (JSON, with the declared counts the packet names); run the `census` subcommand and print its output.”

Verbatim brief: “Write your report as `SEAT_REPORT.md` in this directory: digests, control tokens, the tally with its denominator, and the artefact list with digests.”

These are still whole-seat instructions and name the wrong batch report. The brief also proceeds directly to limb B, while §6 requires global limb-A agreement before arithmetic. C1 seals batch files before the next batch, yet no phase distinction explains how final outcomes can update those files without breaking their original seals. The fixture exercises one already-completed batch chain; it does not resolve this real-run lifecycle gap.

Exact replacement for brief steps 3–7: “This session owns only the files listed for batch k in the dispatch record and has read access to all manifest texts. In limb A enumerate only owned files, record exclusions and inputs, and write candidates_b<k>.json, exclusions_b<k>.json, ledger_b<k>.json and SEAT_REPORT_b<k>.md; print ACCESS_SHA=<packet digest>, owned files, all source lookups with file and line, declared counts, command outputs and control tokens. Use globally unique identifiers beginning with the claiming file followed by #. The custodian seals limb-A batches in order in a separate limb-A chain, joins them and obtains the required two-seat agreement before any arithmetic. Limb B resumes the same ownership batches in separate sessions, writing final outcomes into separate limb-B copies of those four files; the custodian seals a separate ordered limb-B chain bound to the agreed limb-A files and joins the final copies. Never overwrite a sealed limb-A file. Run census and validate on the applicable joined files, with the candidate argument required by §3. A batch report is not the seat's final census tally. Final line of each session report: R3C2_SEAT_COMPLETE.” Add the same phase/chain distinction to C1 and budget the additional sessions explicitly.

The custodian's operative instructions must also name the staged batch tool and its full digest, the partition pin, and the arguments already implemented by that tool: `partition <manifest> 12 <partition>`, `seal <partition> <k> <seat_dir> <corpus_dir> <seals>`, `join <partition> <seat_dir> <seals> <manifest> <out_prefix>`, and `coverage <partition> <manifest> <seat_dir> <corpus_dir> <packet_sha256>`. Likewise name the staged ledger tool as the custodian's audit implementation; audit subcommands remain prohibited to census seats. These are concrete command-interface requirements, not a change to ownership-versus-access.

Execution evidence and checked artefacts:

- Ran the requested kit with working directory r3c2_staged_d1d7 and `/usr/bin/python3 -E r3c2_staged_tests.py`. Exit 0. Its last three lines were:

```text
deletion_probes=38
controls=111 passed=111 failed=0
STAGED_TESTS=PASS
```

- Verified `shasum -a 256 -c r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256` from the lane working directory: all seven entries OK. These included both tools, tests, README, both partition files and the counterexample exhibit. This is pin verification, not adoption. The kit itself rewrites its named exhibit as part of the requested test.
- Independently hashed the root ledger tool, lane tool, builder, timeout wrapper, manifest script, sandbox profile, corpus manifest and staged tools. Builder, lane, wrapper, manifest and profile match the master's full pins. The root ledger is the old digest; the staged ledger matches the candidate's new digest.
- Recomputed the 12-of-89 partition from the actual manifest: exit 0, bytes identical to partition_12_of_89.json. Partition digest: 15b69217a35dbc6fb8f47057cefbb827e3ed0710ecb04f2c71d3e68444b97b06. The staged batch tool digest is 1c1251931acc46668c13282fd456807b9a1515bb47bb6614dcb6fc9176e32ef1.
- Executed C5's five commands sequentially, each exit 0: Python 3.9.6; SymPy 1.14.0; interpreter SHA b8763cf250e607a778bb4603cecb5b90338814d0a3dfcba0d57b1de242f610e9; site directory /Users/duhokim/Library/Python/3.9/lib/python/site-packages; FILES=20637 and MANIFEST_SHA256=1b5463c1072994b2c458d8cbe73a931d23c4b9b10cee3dfd789989d59d9f03ed. I certify executable scope, not C5_HARNESS_PINNED=PASS for a nonexistent candidate dispatch receipt.
- Executed the literal 120.0-second wrapper invocation with a child exiting 7: WRAPPER_EXIT=7 and process exit 7. A separate 0.1-second cap probe printed SYMBOLIC_TIMEOUT and exited 124 at 0.104 seconds. That tests deadline enforcement without claiming a 120-second corpus attempt.
- Executed census, census final, validate with/without the candidate argument, lane merge and compute, all five audit subcommands, and partition/seal/join/coverage using my own fixtures. The synthetic 12-batch run sealed batches 1 through 12 in order. Every positive stage exited 0.

Required independent-fixture tokens:

```text
D1_EXTERNAL_CHOICE: C3_NO_SUBSTITUTION=PASS; exit 0
LANE_MERGE: merged 1 records; origin disagreements=0; exit 0
LANE_COMPUTE: t01.txt#c1 rests_on=USES_IMPORTED root_origins=['IMPORTED']; exit 0
AUDIT_SEAL_ENUMERATION: census-gated seal written; exit 0
AUDIT_SELECT: N=1 R=0 k=0 audited=1; exit 0
AUDIT_HANDOUT: 1 claims, fields claim_id/source_file/source_line only; exit 0
AUDIT_SEAL_REDERIVATION: digest seal written; exit 0
AUDIT_COMPARE: C6_AUDIT_SAMPLE=PASS; exit 0
BOTH_SEATS_OMIT_AUDITOR_FINDS: OMISSION, C6_AUDIT_SAMPLE=FAIL; exit 1; study_files=CENSUS_AUDIT_FAILED
BATCH_PARTITION_12: exit 0
BATCH_SEAL_1 through BATCH_SEAL_12: exit 0 each
BATCH_JOIN: JOIN=PASS; exit 0
BATCH_COVERAGE: C1B_BATCH_COVERAGE=PASS; exit 0
JOINED_CENSUS_FINAL: C1_DENOMINATOR_PRINTED=PASS; exit 0
JOINED_VALIDATE_BATCH1_IMPORTS_BATCH12: C3_NO_SUBSTITUTION=PASS; exit 0
```

The source and JSON fixtures, exact resolved commands, complete stdout/stderr and exit statuses for the required independent sequence are retained in `_tmp_v26cand_codex_fixtures/run_fixtures.py` and `_tmp_v26cand_codex_fixtures/RUN_LOG.txt`. Additional evidence is in BUILDER_LOG.txt, PLAUSIBLE_ORIGIN_LOG.txt, SANDBOX_PROBE.txt and the computed fixture outputs in that directory. The audit's first seal binds auditor candidate digest 5b295513fb0a8ae3be59cd7f917ea0a44a5db6a437fa527348ca01085b5b48b9; its re-derivation seal binds 7cb124ef9a7fcde4847db931677aa2c6af8041769381132330d1ad3348a10fb1.

Q7(c), exact diff: CANDIDATE_DIFF_ONLY=NO under the literal whole-file question. Beyond the enumerated method edits, line 3 changes the V25 living-draft status to the V26 unadopted-candidate status, and an entire §10.20 is appended. Those two documentary differences are COSMETIC under this gate's design test; they change no operative class, threshold or tested value. Exact replacement for the candidate's sentence “Exact change list versus V25.”: “Exact operative change list versus V25; additionally, the status header changes and §10.20 is appended as non-operative history.” After excluding those two documentary changes, the diff contains only the changes the user listed; I found no extra operative amendment.

Q7(d–e): the external “we choose” import has one intended disposition and passes; both-seat omission is fatal when the independently sealed auditor finds the passage, and remains the stated shared-error residual if the auditor also omits it; batch-1 importing from batch 12 passes without waiting for batch 12's enumeration because all source texts are available from the outset. Those new method choices do not themselves disclose a preferred result. They nevertheless require the executable repairs above before this candidate can meet its own design claims.

R3C2_V26CAND_GATE_COMPLETE

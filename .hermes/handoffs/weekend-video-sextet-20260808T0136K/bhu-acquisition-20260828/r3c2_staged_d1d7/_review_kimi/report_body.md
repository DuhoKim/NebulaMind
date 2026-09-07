ACCESS_SHA=cb78eef0f4167759a415b5381b73fd075bb5475172e5290afa24d9a1c3820cfe
PACKET-free
CANDIDATE_D1=SOUND_WITH_REPAIRS
CANDIDATE_D7=SOUND_WITH_REPAIRS
BATCH_PREP=UNSOUND
TOOLING_MATCHES_CLAUSE=NO
COUNTEREXAMPLE_HANDLED=YES
IMPORTED_RULE_BREAKS_PARTITION=YES
STAGED_TESTS=PASS

Independent review of the UNADOPTED candidate, 2026-09-06. These findings judge the candidate and the separate batch preparation only. The signed V23 design and living draft were read for operative context, not reviewed; their section-10 histories are not findings. Nothing here adopts, freezes, or runs a census. No seat packet or other lane document was opened.

The narrow D1 provenance decision and repaired D7 omission predicate are defensible. The staged implementation does not establish all their preconditions. The batch proposal contradicts the imported-input rule and needs substantive revision before acceptance.

A. Access and pin verification performed first, in order.

Command:
```
shasum -a 256 /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/R3C2_D1_D7_CANDIDATE_CLAUSES_20260906.md
```
Result:
```
cb78eef0f4167759a415b5381b73fd075bb5475172e5290afa24d9a1c3820cfe  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/R3C2_D1_D7_CANDIDATE_CLAUSES_20260906.md
```
Then, from the working directory:
```
shasum -a 256 -c r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256
```
Complete result, exit 0:
```
r3c2_staged_d1d7/r3c2_ledger_tools_STAGED.py: OK
r3c2_staged_d1d7/r3c2_batch_tools_STAGED.py: OK
r3c2_staged_d1d7/r3c2_staged_tests.py: OK
r3c2_staged_d1d7/README_STAGED_UNADOPTED.md: OK
r3c2_staged_d1d7/partition_12_of_89.json: OK
r3c2_staged_d1d7/C6_COUNTEREXAMPLE_EXHIBIT.txt: OK
```
The same pin check also passed after the experiments.

B. Kit and independent counterexamples actually run.

Command, exit 0:
```
cd r3c2_staged_d1d7 && /usr/bin/python3 -E r3c2_staged_tests.py
```
Last three lines, verbatim:
```
exhibit written: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/r3c2_staged_d1d7/C6_COUNTEREXAMPLE_EXHIBIT.txt
controls=44 passed=44 failed=0
STAGED_TESTS=PASS
```
Execution-scope disclosure: that mandatory command recreates `_ctl/` and overwrites `C6_COUNTEREXAMPLE_EXHIBIT.txt`; its source revealed this after execution. Thus I cannot claim that the required kit invocation made no writes outside `_review_kimi/`. The exhibit still matches its pin. All independently authored fixtures, logs, and the working report are under `_review_kimi/`. The requested report destination is treated as the explicit exception to the otherwise conflicting write restriction; it is written without reading any existing review file.

I wrote a new driver, `r3c2_staged_d1d7/_review_kimi/run_independent_probes.py`, and ran it with `/usr/bin/python3 -E`. It created the temporary directory:
```
r3c2_staged_d1d7/_review_kimi/codex_yecco2mj/
```
Its `command_log.json` contains resolved commands, complete stdout/stderr and exit codes. `results.json` contains summaries; `supplemental_checks.json` records census validation. These are my fixtures, not copies of the kit's counterexample. `results.txt` contains:
```
We report our own calculated result: the dimensionless yield is 41.
We report our own calculated result: the dimensionless yield is 73.
For our calculation we set the input q = 9.
```
Line 2 explicitly asserts an original dimensionless result. It is required by §1 even though no derivation is stated, so its outcome is `REPRO_NO_DERIVATION_STATED`. The first two omission experiments concern lines 1–2; line 3 supplies a separate exclusion probe. A synthetic manifest pins this source. Both independently written seat candidate files omit line 2 in the forward case and are byte-identical; the compared sealed candidate file is their exact agreement. The auditor includes line 2. In the reverse case both seats include it and the auditor omits it. The seat A, seat B and auditor candidate/exclusion files in both experiments all passed `census ... final`.

The driver executed the following concrete subcommands, with `case` successively `both_seats_omit` and `reverse_omission`, all paths resolved under the directory above:
```
/usr/bin/python3 -E r3c2_staged_d1d7/r3c2_ledger_tools_STAGED.py audit seal-enumeration <case>/auditor.json <case>/auditor_x.json <case>/stage1.txt
/usr/bin/python3 -E r3c2_staged_d1d7/r3c2_ledger_tools_STAGED.py audit select <case>/sealed.json 1919191919191919191919191919191919191919191919191919191919191919 <case>/selection.json
/usr/bin/python3 -E r3c2_staged_d1d7/r3c2_ledger_tools_STAGED.py audit compare <case>/stage1.txt <case>/auditor.json <case>/auditor_x.json <case>/sealed.json <case>/sealed_x.json <case>/inputs.json <case>/selection.json <case>/rederive.json <case>/C6_AUDIT.json
```
The placeholders above abbreviate the two path sets for readability, not the executed commands; the log contains every absolute argument. Seal and select exited 0 in both cases; compare exited 1 in both.

Forward case, emitted completeness object (JSON whitespace normalized):
```
{"audit_included_absent_from_sealed": [["results.txt", 2, "73"]], "exclusion_kind_differs": [], "inclusion_disputed": [], "inclusion_disputed_count": 0, "inclusion_disputed_rate": 0.0, "sealed_included_absent_from_audit_enumeration": []}
C6_AUDIT_SAMPLE=FAIL
```
Reverse case:
```
{"audit_included_absent_from_sealed": [], "exclusion_kind_differs": [], "inclusion_disputed": [], "inclusion_disputed_count": 0, "inclusion_disputed_rate": 0.0, "sealed_included_absent_from_audit_enumeration": [["results.txt", 2, "73"]]}
C6_AUDIT_SAMPLE=FAIL
```
Additional executed probes:

| Probe | Observed result |
|---|---|
| Complete matching baseline | C6 PASS |
| Auditor's declared candidate count wrong | C6 PASS, but auditor `census` FAIL |
| `select` executed before the first enumeration seal | C6 PASS |
| Selection edited to `audited_ids=[]`, `sampled_ids=[]`, `k=0`, retaining candidate digest | C6 PASS with no audited claims |
| Sealed excluded candidate absent from auditor | C6 PASS; absence not listed |
| Auditor excluded candidate absent from sealed candidates | C6 PASS; absence not listed |
| Inclusion disagreements 2/20 | C6 PASS, count 2, rate 0.1 |
| Inclusion disagreements 3/20 | C6 FAIL, count 3, rate 0.15 |
| One inclusion disagreement, sealed denominator zero | C6 PASS, count 1, reported rate 0.0 |
| Batch 2 sealed before batch 1 | Both seal commands succeed |
| Cross-batch parent `b2_i1` in batch 1 | JOIN PASS; parent rewritten to nonexistent `b1_b2_i1` |

The 20-row and malformed-input probes test structural predicates, not source-reading performance. The two required omission probes use the explicit §1 passage above. These results establish a working narrow omission repair, not a word-for-word implementation of C6.

C. D1: comparison and findings.

**1. The two wordings agree on borrower origin when their premises hold, but do not produce identical filings.**

Verbatim candidate quote: “My clause reaches the same filings by declaring the source's line the citation; the review's reaches them by quoting the borrower's sentence.”

Defect: the evidence quotation and its file/line necessarily differ. With an unequivocal borrowing relation and uniquely identified value, both normative readings require `PRINTED/IMPORTED/ORIG_CITATION`, regardless of the source's acquisition verb. They do not select a unique evidence record in every case, and the staged code implements only the borrower-evidence route. I used a borrower that does NOT print the input: “We take parameter a from source.txt.” The source contains the following alternatives:

| Source wording | Tori's intended borrower filing | Review wording's intended borrower filing | Executed staged result for review wording |
|---|---|---|---|
| “For this calculation we choose a = 2.” | IMPORTED, source quotation | IMPORTED, borrower quotation | PASS |
| “For this calculation we fit a = 2.” | IMPORTED, source quotation | IMPORTED, borrower quotation | PASS |
| “For this calculation we measure a = 2.” | IMPORTED, source quotation | IMPORTED, borrower quotation | PASS |
| “For this calculation we adopt a = 2 from X.” | IMPORTED, source quotation | IMPORTED, borrower quotation | PASS |

A Tori-form record quoting the source's “we choose” line fails the staged validator with “IMPORTED PRINTED record names its own file as the external source”. This tests incompatibility of the alternative schema usage, not a normative reason to classify the borrower CHOSEN.

The same source deliberately machine-matches value 2 on multiple lines, including both `a = 2` and unrelated `b = 2`. The staged validator accepts each selected line, including the wrong symbol. Neither clause specifies how to resolve multiple relevant source occurrences. Equal numerical values do not make the selected source locator, provenance linkage, or evidence record identical.

Exact replacement: “For a borrowing relation established by the claiming paper, both alternatives assign origin IMPORTED regardless of the source's acquisition verb; their evidence records differ. Adopt the borrower-evidence wording as the single operative rule. Quote the claiming paper's sentence naming the source, and record separately the named source's value locator. The source locator must identify the cited quantity and context, not merely an equal numeral. Where several source occurrences are relevant, use the locator explicitly designated by the borrower; if none is designated, list all matches and apply a preregistered disambiguation rule. An unresolved ambiguity stops that input's adjudication and is reported; it must not be resolved by a seat choosing a convenient line.”

Consequence: the repaired wording supports immediate borrower provenance, without promising identical evidence bytes or hiding source-selection discretion. A new ambiguity disposition or stop rule must be settled before adoption.

**2. The safer wording does not mechanically prevent an import being filed CHOSEN.**

Verbatim quote: “Under it the "we choose" conflict never arises, because the quotation is a genuine citation and the source's line is only the match target.”

Defect: this is sound as an instruction to a compliant reader, not as an unconditional property of accepted records. The validator has no candidate-file argument establishing which paper owns `claim_id`. Changing the import's origin to CHOSEN and quoting the source's choice sentence passes the ordinary PRINTED branch. I executed that attack; `C3_NO_SUBSTITUTION=PASS`. The kit's own “non-import PRINTED” control also does not machine-establish that the claim belongs to the source paper. Separately, IMPORTED records with an empty quotation or a quotation from an unrelated third paper pass. The code checks substrings and unequal filenames, not a genuine borrowing relation.

Exact replacement: “Quoting the borrower's naming sentence avoids applying the source's acquisition verb to the borrower. This is a reader rule: substring validation alone does not establish a citation. Bind each claim_id to its candidate source file and require the evidence file to be that claiming file, with a nonempty quotation. When the value locator belongs to another paper, require IMPORTED/ORIG_CITATION; genuine source identity and citation meaning remain independently checked by both seats and the auditor.”

Consequence: the review wording is safer because it puts the operative provenance evidence at the borrower and makes mistaken inheritance easier to detect. Neither alternative, with this validator, warrants saying that a machine PASS excludes a CHOSEN-for-import misfiling. The contextual design already acknowledges semantic classification limits; that acknowledgement does not supply the missing structural binding.

**3. The claimed external-value and enumerability checks are weaker than stated.**

Verbatim quote: “a `PRINTED` record with `ORIG_CITATION` has its verbatim matched at the CLAIMING paper's citing sentence (`origin_evidence.source_file/source_line`) and its value at the EXTERNAL value line (`source_file/source_line`), which must be an enumerable text of the manifest and not the record's own file; no reason-code test is applied to the external line's wording.”

Defect: the claiming-file check is absent as above. `enumerable()` accepts any file when the manifest is absent, and any backtick filename mention when it exists. My absent-manifest and RAW-only-manifest probes both pass. The value check is a substring: value `2` passes a line containing only `b = 20`. No source digest is verified here. Equal content snippets do not prove pinned enumerable membership or identify the cited quantity.

Exact replacement: “Validation requires a present, verified manifest and exact membership in its enumerable rows, verifies the selected source bytes against that row, binds the evidence file to the claiming candidate, and matches the selected numeric token rather than a substring of another numeral. Source-quantity identity and citation semantics are separately adjudicated by the independent readers.”

Consequence: until repaired, this tool can admit out-of-corpus, wrong-quantity, or incorrectly matched input evidence while reporting no substitution. These are defects in the new D1 code claim; no census prevalence is inferred from synthetic examples.

**4. The D1 consequence paragraph overstates arithmetic success and transitive provenance visibility.**

Verbatim sentences:

“A borrower's claim whose input was chosen or fitted by another paper in the corpus files as reproducible from its stated inputs (arithmetic-group outcome) with `rests_on = USES_IMPORTED`.”

“At the borrower the census says "rests on an import", not "rests on a choice"; the choice is visible one hop away on the source's record, and the lane's `compute` can follow `derived_from` across papers where the seats recorded it.”

“What the census can no longer say is "this paper's number rests on a choice" when the choice was made by a different paper — unless he takes the "change" route: an inherited origin (`IMPORTED_CHOSEN` / `IMPORTED_FITTED` / …), which is a taxonomy expansion and a second pass over every import.”

Defect: making one input available does not settle other missing inputs, machinery, or numerical agreement. The arithmetic group includes REPRO_FAILED. Other roots can affect `rests_on`. The source's own choice may be an excluded input with no included source claim and thus no corresponding input-ledger record. Cross-paper links are conditional, not guaranteed; the staged `roots()` stops at a non-DERIVED record, including IMPORTED. I did not open the lane compute tool and do not certify its behavior. A separately quoted source choice can be reported without inventing an inherited-origin taxonomy; that does not change the immediate borrower classification.

Exact replacements, respectively:

“D1 makes this imported input available to the arithmetic attempt; the claim's outcome still follows §3 after all required inputs and computations are assessed, and its provenance summary follows the full recorded root set.”

“The borrower records immediate origin IMPORTED. Source provenance is visible only where separately recorded and explicitly linked; this candidate does not establish automatic transitive provenance across an IMPORTED record.”

“The immediate borrower origin does not classify the source's acquisition method. Reporting that method separately with evidence does not require a new origin category; changing the taxonomy or the root-summary semantics would require an explicit amendment.”

Consequence: this amendment can support an immediate-import tally. It cannot by itself establish successful reproduction, complete inherited provenance, or a prohibition on separately reporting source choices.

D. D7: clause/code agreement and custody.

**5. The narrow both-directions PASS repair works; the full enumeration comparison does not match the clause.**

Verbatim quote: “every candidate in the sealed ledgers matched to its own enumeration or listed as unmatched, and every passage in its own enumeration absent from the sealed ledgers listed”.

Defect: `compare` only searches for absent INCLUDED passages. An excluded-only candidate missing from the opposite enumeration is silently omitted from the comparison, in either direction; both executed probes passed. It reports neither all matched candidates nor a completeness disposition for every exclusion. The clause's explicit fatal omission examples concern included claims, whereas its listing obligation covers every candidate. These must be distinguished, not collapsed.

Exact replacement: “Compare the union of all candidate keys from the receipted agreed seat enumeration and the auditor enumeration. For every key emit both presences, both inclusion dispositions, both exclusion kinds where applicable, and MATCH, OMISSION, or AUDIT_INCLUSION_DISPUTED. List every one-sided key. An auditor-included key absent from both seats, or a sealed-included key absent from the auditor, is fatal. One-sided excluded candidates are reported separately and do not trigger this included-omission predicate.”

The last sentence is a proposed resolution of the candidate's ambiguity; if excluded omissions are also intended to be fatal, say that explicitly instead and test it. Define the agreed sealed enumeration as the verified reconciliation of both seat enumerations; `compare` accepts only one sealed candidate file, not the two original seat files.

Consequence: the observed both-seats-miss counterexample is handled correctly. Current PASS does not certify the promised exhaustive candidate/exclusion comparison. My `COUNTEREXAMPLE_HANDLED=YES` must not be read as `TOOLING_MATCHES_CLAUSE=YES`.

**6. The 10% implementation matches the positive-denominator boundary but loses required dispositions and mishandles zero.**

Verbatim quote: “A passage that BOTH sides list but dispose differently is not an omission: it is filed `AUDIT_INCLUSION_DISPUTED`, listed with both dispositions and counted; above 10% of the sealed denominator the audit files `CENSUS_AUDIT_FAILED`, at or below it the count is reported and does not block PASS.”

Defect: at N=20, 2 disputes PASS and 3 FAIL as required. But the artifact lists only `(file,line,numeral)` for inclusion disputes, not both dispositions or a per-row `AUDIT_INCLUSION_DISPUTED` status. With N=0 and one sealed exclusion the auditor includes, it reports a dispute rate of 0.0 and PASS. A positive count cannot be at or below 10% of zero. “Dispose differently” also needs to distinguish included/excluded disagreement from two different exclusion kinds; the code lists exclusion-kind differences separately and never counts them toward this threshold.

Exact replacement: “AUDIT_INCLUSION_DISPUTED means that both enumerations contain a candidate key but disagree on its included/excluded status. Emit that token and both dispositions for every such key. Let D be the number of distinct disputed keys and N the receipted sealed included denominator. Fail exactly when 10 × D > N, including D > 0 when N = 0. For N = 0 report the rate as not defined, with D and N printed; D = 0 does not fail this rule. Report disagreements between exclusion kinds separately, outside D.”

Consequence: the positive-N threshold is supported by execution. Current PASS can hide a denominator disagreement in the zero case and lacks the evidence required to interpret allowed disagreements.

**7. Auditor census PASS is not a precondition enforced by any audit subcommand.**

Verbatim quote: “writes its own candidate and exclusion ledgers (`census` PASS required).”

Defect: `seal-enumeration` hashes arbitrary bytes; `compare` never runs census or verifies a census receipt. My auditor file with an incorrect declared count is sealable and gets C6 PASS, while a separate census run on exactly those files FAILS. Matching the hash of invalid data does not validate it.

Exact replacement: “Before issuing the stage-1 receipt, the custodian runs the enumeration-mode census validator on the auditor candidate and exclusion files and records the command, exit status, output, and their digests. A nonzero exit prevents sealing. Compare reruns that validation on the same digests and refuses PASS without it. Stage-1 included candidates may carry PENDING outcomes; independent re-derivations are a later stage.”

Consequence: the clause's census requirement is sensible, but a standalone staged C6 PASS currently does not imply a well-formed auditor enumeration, still less a complete source reading.

**8. The staged selection and artifact are not a verified frozen-frame audit.**

Verbatim quote: “Second, after receipt T and the supply of the external seed, the custodian computes the audit selection”.

Verbatim tooling claim: “`C6_AUDIT_SAMPLE=PASS` only with no failure”.

Defect: `select` requires neither a stage-1 receipt nor receipt T. `compare` checks only that the candidate digest equals the digest written in the supplied selection. It trusts `audited_ids`, the groups, N, k and the seed rather than recomputing them. I deleted all assigned ids and re-derivations in a one-claim case while retaining the candidate digest; it passed. The selection's candidate hash is relabelled `receipt_T_sealed_candidates_sha256` without establishing an external receipt. Sealed exclusions and inputs are not digest-bound to receipt T. The result artifact reports per-claim MATCH/why, but does not embed the auditor's re-derived outcomes, number pairs or per-input reclassified origins; it does not bind the separate re-derivation file by digest either. Those retained C6 artifact obligations are not satisfied by a MATCH label.

Exact replacement: “Selection requires verified receipt T for the reconciled candidate, exclusion and input files and an external seed recorded with that receipt. Compare verifies all receipt digests and deterministically recomputes the denominator, arithmetic group, remaining group, k, sampled ids and audited ids from the receipted candidates and seed; any supplied-field disagreement fails. The audit artifact includes receipt T, all bound digests, the auditor's independently committed outcome and number pair per assigned claim, each input's reclassified origin, and its individual comparison result.”

Consequence: legitimate `select` computes the advertised formula, but current `compare` PASS does not prove that the required claims were audited or that the compared ledgers are the receipted ones.

**9. Source-only independence is a procedural requirement; the hash sequence does not enforce it.**

Verbatim quote: “`seal-enumeration` (custodian records the auditor's own candidate/exclusion digests BEFORE any sealed ledger is revealed)”.

Verbatim clause: “with no access to either seat's candidate, exclusion, input or outcome ledgers”.

Defect: the first quotation describes intended custody, not what the function can establish. `seal-enumeration` has no exposure state, event order, first-write protection, identity, census precondition or authenticated receipt. It overwrites an existing seal. `select` can run first; my select-before-seal experiment passed. `compare` checks present-byte agreement with a supplied seal, not historical order. Re-derivations are neither independently sealed nor committed before ledger release. A reader could copy a ledger, then seal an enumeration and construct matching re-derivations; the hash checks would not reveal that history.

The staged design does not itself close these exposure routes:

- A ledger, excerpt, prior result or selection output placed in the auditor's allowed directory, packet, prompt, attachment, stdin or tool response before sealing. Path confinement does not hide data already placed inside its allowed boundary.
- Reused conversation context, resumed processes, caches, earlier sessions or a reviewer/auditor role overlap. A different engine label does not establish a fresh unexposed context; prior training exposure cannot be ruled out by this kit.
- Premature execution of `select`, or release of its output by the custodian. Its JSON exposes the arithmetic/remaining groups and denominator; it is not the specified identifier/file/line-only handout. It contains no generated source-location handout.
- Premature ledger release during re-derivation, before an immutable re-derivation commitment. Stage 1 alone protects neither the timing nor independence of these later results.
- Replacement, regeneration or backdating of the unauthenticated seal; changing auditor files and issuing a new seal after exposure; changing unreceipted exclusion/input files or the unsealed re-derivation file.
- Other delivery surfaces available to the dispatcher or runtime: logs, copied files, permitted environment/startup content, inherited handles, shared mounts, and any enabled network or connector responses. The candidate provides no auditor-specific inventory or probes establishing their exclusion.
- Direct absolute/parent paths, aliases or links to ledger storage where confinement is absent or misconfigured. The living draft's correctly enforced kernel profile is specifically intended to deny outside reads, including lane reads; I do not claim to have bypassed it, and did not inspect or test that profile. Under such confinement, this route is closed to the extent its actual permissions and probes establish. A working-directory layout alone does not close it.

These are channel classes and missing custody evidence, not allegations that any production auditor used them. The no-exposure instruction is already clear. Access permissions, clean dispatch, role separation and delivery timing are custody matters. The missing enforceable stage receipts, safe handout and re-derivation commitment are staged-procedure/tool defects. An unrestricted same-directory command test is not a sandbox penetration test.

Exact replacement: “The custodian dispatches a fresh auditor context with a recorded source-only inventory, the applicable confinement profile and live probes denying seat-ledger access, and no prior seat output in prompts, attachments or tool context. It records an immutable, first-write stage-1 receipt for a census-PASS enumeration before issuing a source-location-only assignment. The auditor's independent re-derivations are committed by digest and receipted before any seat ledgers are released. Release events reference those receipts. The audit tool verifies receipt bindings and event order; source-only exposure is supported by the custody record and confinement probes, not inferred from matching hashes.”

Consequence: the stronger clause is preferable to the weaker, deliberately anchored alternative. Current staged C6 PASS establishes neither source-only enumeration nor blind re-derivation. Even repaired custody cannot prove absence of all prior model exposure.

E. Batch preparation: why the proposed equivalence fails.

**10. Partitioning enumeration ownership does not partition source dependencies. This makes the current batch proposal UNSOUND.**

Verbatim quote: “§1's inclusion rule is per passage and §2's arithmetic is per claim; neither consults any other text.”

Verbatim quote: “Therefore the enumeration of the whole corpus equals the union of the enumerations of any partition of it, PROVIDED every text is in exactly one batch and no batch cites outside itself.”

Verbatim dispatch requirement: “in a working directory holding the packet, the brief, the pinned scripts, the manifest and ONLY batch k's texts.”

Defect: §2 explicitly requires reading the named source's value line in another pinned enumerable paper for IMPORTED inputs. D1 expressly exercises that rule. The named source can belong to another batch. In my executed example, borrower.txt is in batch 1 and source.txt is in batch 2. The identical D1 record validates with both pinned texts present and fails with only batch 1's text present: “cannot read external value line source.txt:1”. It cannot honestly become REPRO_BLOCKED merely because dispatch withheld an otherwise enumerable pinned source. With a = 2 available, the borrower's `z = a + a = 4` is evaluable; artificial source deprivation changes the attempt and potentially the study class.

I found no separate §1/§2 requirement to reconcile all numerical statements across different papers. The proposal's cross-batch consistency concern is a reader-consistency issue, not a license to invent such a rule. The definite cross-text dependencies are §2's named-source lookup and associated §2/C3 provenance edges. Per-passage enumeration can have disjoint ownership without per-claim evaluation being source-local. Even if the included denominator is unchanged in this example, the joint claim that the census and its conclusions are unchanged is false.

Exact replacement: “A batch partitions ownership of candidate passages, not access to evidence. Each source's candidates are enumerated only in its assigned ownership batch. Each reader also has read-only access, within the verified confinement boundary, to all pinned enumerable corpus sources needed by §2 and D1; all such lookups are logged with manifest digest, source file and line. Reference-only access creates no additional ownership or denominator entry. No input is classified BLOCKED merely because its named source belongs to another batch. Import lookup, source ambiguity resolution and dependent arithmetic must finish before that batch's final seal, or remain in an explicitly preregistered dependency-resolution stage before final sealing.”

Add: “The same source-access rule applies independently to each census seat and the auditor. Coverage checks ownership exactly once; source-dependency checks verify allowed manifest membership and pinned bytes independently of ownership.”

Consequence: this preserves the possibility of one census and one reconciled denominator across many sessions. The present ONLY-texts dispatch cannot preserve §2, and seals or coverage cannot repair missing information after the fact. Merely allowing JOIN to accept an external locator does not give a reader the source it needed.

**11. The join does not preserve cross-batch provenance references.**

Verbatim quote: “prefixes every candidate id, claim id, input id and `derived_from` entry with `b<k>_`”.

Defect: for a parent in another batch, the parent's namespace is the parent's batch, not the child's. My batch-1 `derived_from=["b2_i1"]` was rewritten to `["b1_b2_i1"]`; JOIN nevertheless passed. An unqualified `i1` intended to refer to batch 2 would instead bind to batch 1 or dangle. The tool cannot infer which. JOIN never validates the dependency graph. It checks candidate source ownership, not all input/evidence locators, so the document's broader “no batch cites outside itself” proviso is not even the implemented condition.

Exact replacement: “Use globally unique, preregistered source-based claim and input identifiers, or explicit qualified `(batch, local_id)` references. Join maps each identifier and parent reference using its target's namespace, preserving already qualified external references. It rejects unresolved references, collisions and cycles and verifies all ledger/evidence sources against the full manifest. Candidate ownership remains restricted to the assigned batch; input evidence may cite any permitted pinned source.”

Consequence: a mechanical concatenation can produce one count while corrupting the graph used for provenance conclusions. Joined census PASS checks candidate/exclusion structure, not a valid full input graph. Global ledger validation is also required.

**12. Seals establish byte commitments only against a trusted seal file; they do not establish dispatch order or source coverage.**

Verbatim sentences:

“The seal preserves: the batch's text list (fixed by the partition), the bytes of its four artefacts, its `ACCESS_SHA`, and the dispatch order.”

“A later session cannot alter an earlier batch's files because they are not in its directory; the lane never edits them; `join` refuses any artefact whose digest differs from its seal.”

Defect: `cmd_seal` does not read its partition argument at all. It records four file hashes, not the partition digest, source list, engine/profile, timestamps, exit event or dispatch order. It accepts batch 2 before batch 1, as executed. The seal JSON can itself be replaced. Directory separation alone is not access denial; a correctly applied sandbox can supply that boundary, but the seal cannot certify it. JOIN checks for mismatch against the supplied seal file, not against an independently receipted one.

Exact replacements:

“The current seal records four artifact digests, indirectly committing the report's printed ACCESS_SHA; it does not bind the partition or prove dispatch order. Before use, bind the partition and source digests, seat identity, engine/profile, session exit and predecessor receipt in an append-only custodian receipt, and reject out-of-order sealing or dispatch.”

“Prevent later-session access to earlier writable artifacts through the recorded confinement and custody controls. Keep independent receipts outside session write authority. JOIN verifies those receipts and rejects artifact or partition changes.”

Consequence: unchanged bytes are useful evidence. They do not establish that all texts were read, that the nominated reader produced the work, or that sessions were independent and sequential.

**13. The coverage and JOIN equivalences omit implementation conditions and do not prove human coverage.**

Verbatim quote: “Both provisos are controls, not assumptions: `C1B_BATCH_COVERAGE=PASS` iff the union of the batch text lists equals the manifest with no duplicate and every batch report prints the packet's `ACCESS_SHA`; `JOIN=PASS` iff every seal matches and every candidate cites its own batch's text.”

Defect: coverage additionally checks the manifest-file digest, but does not verify actual source bytes, batch row/digest arrays, unique batch identifiers, declared batch/text counts, runtime availability, reading, or seal order. JOIN additionally requires usable files and seals but does not itself run coverage or census. A report containing the expected ACCESS_SHA substring is not proof that its process read the packet. The real staged partition is internally consistent: 89 distinct filenames, rows 1–89, five groups of 8 and seven of 7. I did not open the real manifest or corpus because they are outside this review's allowed file list; real-manifest membership and source workload are not independently certified here.

Exact replacement: “C1B_BATCH_COVERAGE checks the supplied manifest digest, filename-set coverage without duplicates, and the expected ACCESS_SHA text in each batch report. JOIN checks supplied artifact seals and candidate ownership before concatenation. These checks establish specified structural properties only. Final acceptance additionally requires validated partition metadata, verified source bytes and dispatch receipts, separate census and ledger validation over joined outputs, two-seat reconciliation, and C6; no structural token proves that a reader actually enumerated every passage.”

Consequence: one joined denominator is mechanically computable. Calling it one independently completed census requires the additional reading, source-access and reconciliation evidence.

F. Remaining overclaims and exact required replacements.

The quoted sentences in findings 1–13 are also the principal overclaims in the two documents. The following covers the remaining unsupported assertions; each replacement is proposed text, not an adopted edit. Statements explicitly framed as instructions or unadopted recommendations are not treated as empirical claims. The reported 44-control run and correctly computed partition size are supported; “Not validated by anyone yet” describes the candidate's pre-review status and is not a false validation claim.

**14. D7 inference and cost overclaims.**

Verbatim: “Under my clause the auditor sees the seats' inclusion decisions before auditing completeness, so "completeness" becomes "did they miss anything I notice given their list", anchored to their choices; under the review's, completeness is a comparison of two independent enumerations, and a passage both seats missed can be found.”

Defect: the stronger procedure permits independent discovery, but independence is conditional on custody; the weaker procedure does not logically prevent discovery either.

Exact replacement: “The weaker procedure exposes prior inclusion decisions; the stronger procedure withholds them until independent work is committed. With verified custody, the latter compares separately produced enumerations and can detect passages both census seats omitted.”

Consequence: procedural superiority is a defensible design preference, not proof of independence in an eventual dispatch.

Verbatim: “`CENSUS_COMPLETE` and `CENSUS_PARTIAL` then rest on an audit that is a genuine independent replication in both senses: the auditor's enumeration can find passages both seats missed — the weaker version makes that discovery LESS LIKELY, because an auditor anchored on the seats' list audits "what they missed that I notice" rather than enumerating afresh; direction only, no magnitude has been measured — and its re-derivations were made without sight of the seats' numbers.”

Defect: no experiment measures even the direction of a discovery-probability effect. Genuine independence and blind derivation depend on the unimplemented custody commitments.

Exact replacement: “With the stated custody conditions verified, the audit adds a separately produced full enumeration and blind re-derivations of the assigned claims. Removing prior inclusion information is intended to reduce anchoring; neither the direction nor magnitude of its effect on discovery has been measured here.”

Consequence: report the procedure and demonstrated detections, not an unmeasured probability advantage.

Verbatim: “The audit's PASS becomes the strongest statement in the design.”

Defect: there is no defined ordering of evidential strength; shared omissions and allowed disagreements remain possible.

Exact replacement: “Audit PASS means that the verified comparison and assignment satisfy the enumerated predicates, subject to custody limits, sampling and possible shared reader errors.”

Consequence: PASS is bounded evidence, not proof of corpus completeness.

Verbatim: “Cost: a third full reading of the corpus (batched like the rest), so the audit's time roughly equals one census seat's; and an auditor `census` PASS becomes a precondition of `C6_AUDIT_SAMPLE=PASS`.”

Defect: full enumeration does not measure total audit runtime; its arithmetic workload and reconciliation differ. The census precondition is normative but not implemented.

Exact replacement: “Cost includes a third full enumeration plus assigned re-derivations and comparison; runtime is unmeasured. Auditor census PASS is a required precondition and must be enforced in the staged commands before adoption.”

Consequence: budget an unmeasured third-reader workload; do not certify feasibility from this kit.

**15. Batch feasibility, independence and drift overclaims.**

Verbatim: “Twelve, not eight: the seat that died was handling sets of eleven; seven or eight texts (roughly 8–10 thousand non-blank lines) is what one session can read completely and still do the arithmetic.”

Defect: equal file counts do not bound bytes, line counts, claim density or arithmetic difficulty. One reported failed workload does not establish a successful maximum. The referenced failure document was not opened.

Exact replacement: “Twelve batches of seven or eight texts are proposed as a workload hypothesis. Before fixing this execution plan, report each batch's pinned line/byte counts and assess enumeration and arithmetic workload in an authorized pilot; no complete-read capacity has been established by the staged structural tests.”

Consequence: a 12-batch schedule is not a demonstrated feasibility guarantee.

Verbatim: “It has no parameters and no judgement.”

Defect: JOIN visibly takes partition, directory, seal and prefix arguments. It has no new classification judgment, but implements consequential scope and identifier policies.

Exact replacement: “For fixed valid inputs and fixed code, JOIN deterministically applies the declared ownership and identifier-mapping rules; it performs no new scholarly classification.”

Consequence: determinism supports reproducibility of assembly, not correctness of those policies.

Verbatim: “Independence BETWEEN seats is unchanged; what is new is that a seat's reading is not one memory.”

Defect: additional dispatches add delivery and custody boundaries. Engine continuity plus directories alone does not establish unchanged independence.

Exact replacement: “The intended between-seat separation is retained across all sessions only if each dispatch verifies the same custody and confinement conditions and supplies no other seat's work; each seat is a sequence of fresh contexts.”

Consequence: assess independence for every dispatch, rather than inheriting it from the first.

Verbatim: “It is measured, not assumed: the run log reports the seat-A/seat-B disagreement rate per batch, so drift shows as a rising rate in later batches; the existing dispute stops apply over the union.”

Defect: between-seat disagreement does not identify within-reader drift. Both seats can drift together with zero disagreement; rates can change because batches differ in content or difficulty. Drift need not be monotonic.

Exact replacement: “Report between-seat disagreement by batch descriptively, with counts and denominators; these rates do not identify within-reader drift. Detecting drift would require a separately preregistered comparable-item or repeated-anchor design. Existing dispute stops apply to the reconciled union.”

Consequence: no claim of measured cross-batch consistency follows from the proposed rate.

Verbatim: “The two-seat reconciliation and the C6 audit are already the design's answer to inconsistency.”

Defect: they address detected disagreement and audit failures, not common-mode classification drift, missing source access, or broken cross-batch references.

Exact replacement: “Reconciliation and C6 address the disagreements and failures their stated procedures detect; neither establishes cross-batch consistency or repairs unavailable evidence and invalid references.”

Consequence: retained controls do not justify treating batching as conclusion-neutral.

Verbatim: “The partition changes nothing about what the audit compares.”

Defect: the comparison function can remain unchanged while restricted source access changes the independently produced inputs to it.

Exact replacement: “The final comparison operates on joined files; preserving its scientific meaning additionally requires the same pinned evidence access and valid global identifiers under batching.”

Consequence: identical comparison code does not establish equivalent audit evidence.

Verbatim: “Nothing about the claims.”

Verbatim: “The report gains one caveat ("enumeration was performed per preregistered batch; per-batch seat disagreement rates: …") and two controls (`C1B_BATCH_COVERAGE`, `JOIN`).”

Verbatim: “It is the difference between a census that can run and one that cannot.”

Verbatim: “(Blocks a first run: without it, no seat completes.)”

Defect: the first two understate the §2 access and provenance changes identified above. The last two assert necessity and sufficient feasibility without a demonstrated successful session plan or exclusion of other execution plans.

Exact replacements, respectively:

“The proposed batch restrictions currently change access to claim evidence; equivalence requires the source-dependency and identifier repairs above.”

“The report must disclose batching, evidence-access policy, unresolved dependencies, custody receipts, global identifier validation and descriptive disagreement rates; coverage and JOIN are additional structural controls.”

“This is one proposed execution plan; its feasibility and equivalence to the intended census remain to be established.”

“An execution plan must be approved before a run; this review does not establish that this particular batching plan is necessary or sufficient.”

Consequence: acceptance needs more than a single batching caveat and two structural PASS tokens.

**16. The batch document's test evidence is stale and internally mismatched to the pinned kit.**

Verbatim: “`STAGED_TESTS=PASS` (37/37 over the whole staged kit).”

Verbatim spans: “`r3c2_staged_tests.py` (sha256 `89c0202fc9283233ad349025a67959dad7b532234825ac7db343a69bdfbb165a`)” and “(staged copy, sha256 `60a191f36a757c6c15e01f3e778518c8e20935bde464deab3e0d9e65fac082ff`) PASSES over the joined files”.

Defect: the supplied pins and live run establish 44/44 using test digest `96c1792085d799a82b6ac488599ea0bc8d8a58a0dc3b3d79cf925f842c2de0c1` and staged ledger-tool digest `cf42430ae1bbdfbd5ca5b4143f069ec16fcbe9d56f4927f266287f228c0945bd`. A historical run may have been real, but it is not current evidence for the differently pinned bytes. The small joined synthetic census validates file structure, not successful reading of 89 texts.

Exact replacement: “The supplied pinned kit was independently rerun on 2026-09-06: test script sha256 96c1792085d799a82b6ac488599ea0bc8d8a58a0dc3b3d79cf925f842c2de0c1, staged ledger tool sha256 cf42430ae1bbdfbd5ca5b4143f069ec16fcbe9d56f4927f266287f228c0945bd; controls=44 passed=44 failed=0, STAGED_TESTS=PASS. These are synthetic structural and predicate controls, not validation of census completeness, auditor independence, cross-batch import handling, or session capacity.”

Consequence: current evidence is reproducible, but its scope is limited. Updating these citations does not cure the substantive findings.

The requested report is written to R3C2_CANDIDATE_REVIEW_codex_20260906.md. All replacements above remain proposed and unadopted.

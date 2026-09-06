ACCESS_SHA=53fa3ab52d3cd7dbbd9e2c4283ecc5124d3a850c22ea43686b4b604651dea4f7
PACKET-free
CANDIDATE_D1=SOUND_WITH_REPAIRS
CANDIDATE_D7=SOUND_WITH_REPAIRS
BATCH_PREP=SOUND_WITH_REPAIRS
TOOLING_MATCHES_CLAUSE=NO
COUNTEREXAMPLE_HANDLED=YES
IMPORTED_RULE_BREAKS_PARTITION=NO
STAGED_TESTS=PASS

Independent adversarial review of revision 2, UNADOPTED, 2026-09-06. These are repair-required judgments, not approval to install or run. The main remaining defects are an executable C6 selection bypass, a surviving import-to-CHOSEN bypass, a missing D1 symbol check, and incomplete batch join validation. The original partition-only access defect is repaired in the proposal; that does not certify its implementation or actual dispatch.

A. Access and pins

First command executed, exactly as requested:
`shasum -a 256 /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/R3C2_D1_D7_CANDIDATE_CLAUSES_20260906.md`
Its full digest is line 1 above.

Then, from the requested working directory:
`shasum -a 256 -c r3c2_staged_d1d7/R3C2_STAGED_D1D7.sha256`
Exit 1; output:

```
r3c2_ledger_tools_STAGED.py: FAILED open or read
shasum: r3c2_ledger_tools_STAGED.py: No such file or directory
r3c2_batch_tools_STAGED.py: FAILED open or read
shasum: r3c2_batch_tools_STAGED.py: No such file or directory
r3c2_staged_tests.py: FAILED open or read
shasum: r3c2_staged_tests.py: No such file or directory
README_STAGED_UNADOPTED.md: FAILED open or read
shasum: README_STAGED_UNADOPTED.md: No such file or directory
partition_12_of_89.json: FAILED open or read
shasum: partition_12_of_89.json: No such file or directory
partition_12_of_89.txt: FAILED open or read
shasum: partition_12_of_89.txt: No such file or directory
C6_COUNTEREXAMPLE_EXHIBIT.txt: FAILED open or read
shasum: C6_COUNTEREXAMPLE_EXHIBIT.txt: No such file or directory
shasum: WARNING: 7 listed files could not be read
```

Diagnostic check subsequently run inside `r3c2_staged_d1d7`: `shasum -a 256 -c R3C2_STAGED_D1D7.sha256`. Exit 0:

```
r3c2_ledger_tools_STAGED.py: OK
r3c2_batch_tools_STAGED.py: OK
r3c2_staged_tests.py: OK
README_STAGED_UNADOPTED.md: OK
partition_12_of_89.json: OK
partition_12_of_89.txt: OK
C6_COUNTEREXAMPLE_EXHIBIT.txt: OK
```

The sheet uses kit-relative paths, contrary to the requested root-relative verification convention. This is a path defect, not evidence of a digest mismatch. Required replacement instruction: “From r3c2_staged_d1d7 run shasum -a 256 -c R3C2_STAGED_D1D7.sha256”; alternatively regenerate the sheet with root-relative paths. Until corrected, the prescribed verification cannot establish integrity.

B. Executions and independent C6 exhibit

Ran `/usr/bin/python3 -E r3c2_staged_tests.py` with its working directory set to `r3c2_staged_d1d7` (the requested cd command's execution equivalent). Exit 0. Last three lines:

```
exhibit written: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/r3c2_staged_d1d7/C6_COUNTEREXAMPLE_EXHIBIT.txt
controls=84 passed=84 failed=0
STAGED_TESTS=PASS
```

The suite includes 29 deletion probes. These establish sensitivity to the tested branches, not completeness of the checks. Execution disclosure: the explicitly required suite recreates `_ctl/` and rewrites the exhibit outside my scratch directory. I discovered that side effect in the README after execution; the subsequent digest check above finds the exhibit matches its pin. All further fixture/code/log writes were inside `r3c2_staged_d1d7/_review2_codex/`, apart from this explicitly requested report. No candidate or staged implementation was edited. No adoption occurred.

I read the candidate, batch preparation, reconciliation, staged implementations/tests/README, and the two specified design-context files. I did not open any prohibited gate/C0 file or any additional lane document. I used the reconciliation's topic map without opening the optional round-1 reports. Findings below concern revision 2, not the context documents' section-10 history.

My independent fixture generator is `_review2_codex/probes.py`; the summary is `_review2_codex/summary.json`. Each audit directory retains its source, two seat candidate files, merged files, auditor files, seals, selection, re-derivations, full command output, and C6_AUDIT.json. The source's line 2 says exactly:

> We report our own result: the dimensionless yield is 42.

This is unambiguously included by §1 even though no derivation is stated. In `both_omit`, neither independently written seat file contains (own.txt, 2, 42); the auditor does. I ran `audit seal-enumeration`, `audit select`, `audit handout`, `audit seal-rederivation`, then `audit compare` using the staged tool, with seed `1111111111111111111111111111111111111111111111111111111111111111`. Emitted missing-passage row:

```
{"audit_included":true,"audit_kind":null,"in_audit":true,"in_sealed":false,"key":["own.txt",2,"42"],"result":"OMISSION_AUDIT_INCLUDED_ABSENT_FROM_SEALED","sealed_included":null,"sealed_kind":null}
C6_AUDIT_SAMPLE=FAIL
```

In `reverse`, both seat files contain it and the auditor omits it. Same command sequence:

```
{"audit_included":null,"audit_kind":null,"in_audit":false,"in_sealed":true,"key":["own.txt",2,"42"],"result":"OMISSION_SEALED_INCLUDED_ABSENT_FROM_AUDIT","sealed_included":true,"sealed_kind":null}
C6_AUDIT_SAMPLE=FAIL
```

Additional independent probes: auditor-only EXCLUDED → OMISSION_AUDIT_EXCLUDED_ABSENT_FROM_SEALED and FAIL; sealed-only EXCLUDED → AUDIT_INCLUSION_DISPUTED, counted (1/2), FAIL; two inclusion disputes over 20 → counted 2/20, PASS; three over 20 → counted 3/20, FAIL. The kit additionally exercised zero denominator and seal/claim/origin mismatches.

Thus the both-directions rule and the numerical 10% boundary work. The complete implementation does NOT match the clause word for word: see F1–F3. In particular, a different counterexample can still receive PASS without recomputation.

F1. C6 recomputation can be bypassed by removing the seed

Verbatim candidate quote: “Only then are the sealed (merged) candidate, exclusion and input ledgers opened to the comparison (`audit compare`), which recomputes the selection from the sealed candidates and seed and fails on any disagreement”. Also: “the recomputed selection matches”.

Defect and evidence: `cmd_audit_compare` recomputes only inside `if all(k in S for k in ("seed_hex",))`. In `missing_seed_skips_selection`, I generated valid seals and selection, removed `seed_hex`, set `audited_ids=[]`, `sampled_ids=[]`, and `k=0`, and ran compare. Exit 0, C6_AUDIT_SAMPLE=PASS, with no claims audited. The existing deletion probe tests an emptied selection WITH the seed retained; it misses this path.

Exact replacement requirement: “compare requires a seed_hex field of exactly 64 lowercase hexadecimal characters and every selection-schema field; missing or invalid fields fail. It always recomputes the full selection and requires exact equality before comparing every selected claim.” Implement unconditional validation/recomputation and add the absent-seed negative; retain the clause's original strict PASS requirement.

Consequence: currently an emptied audit can pass, so PASS cannot support the promised sample coverage or a CENSUS_COMPLETE/PARTIAL conclusion on that basis.

F2. C6 output vocabulary and study-level failure do not implement the stated contract

Verbatim quote: “a result: `MATCH`, `OMISSION`, or `AUDIT_INCLUSION_DISPUTED`”. Verbatim quote: “each is ledger incompleteness and files `CENSUS_AUDIT_FAILED`.”

Defect and evidence: my omission rows emit longer OMISSION_* result values. `kind_difference` emits `MATCH_KIND_DIFFERS` and PASS for two exclusions with different kinds, which is a fourth undeclared result. The implementation emits C6_AUDIT_SAMPLE=FAIL but never files a CENSUS_AUDIT_FAILED field/token. It also aggregates origin differences into each claim's `why` array rather than emitting an individual MATCH/MISMATCH result for every re-classified input as promised by “per re-classified input origin”.

Exact replacement: “Each completeness row has result MATCH, OMISSION, or AUDIT_INCLUSION_DISPUTED and a separate reason field for omission direction or exclusion-kind difference. Exclusion-kind differences alone are reported without entering the inclusion-dispute count. Each audited input has its own MATCH/MISMATCH row. Any fatal audit failure emits study_outcome=CENSUS_AUDIT_FAILED as well as C6_AUDIT_SAMPLE=FAIL.” This explicitly chooses a policy for kind-only disagreement, rather than silently inventing a fourth result. Implement these fields, or specify a pinned downstream mapper and test it.

Consequence: current consumers cannot rely on the advertised schema or assume the study-level stop was filed merely because compare failed. This does not negate the correctly detected omissions or 10% tests.

F3. The supposedly frozen comparison inputs need an explicit custody binding

Verbatim quote: “both seals match”. Verbatim quote: “Only then are the sealed (merged) candidate, exclusion and input ledgers opened to the comparison”.

Defect and evidence: the two checked seals are the auditor's enumeration and re-derivations. Selection binds the merged candidate digest; no previously committed merged exclusion/input digest is supplied to compare. The latter hashes are computed only for the output. Code inspection therefore shows that compare alone does not establish that these are the already sealed merged bytes. Stage-1 select accepts a file containing the marker AUDITOR_CANDIDATES_SHA256= without validating its structure or census attestation; compare never verifies AUDITOR_CENSUS_STDOUT_SHA256. Authentic custodian provenance remains a prerequisite.

Exact addition: “Before comparison, the custodian verifies all three merged files against the pre-release commitment and records that commitment in C6_AUDIT.json. Both auditor seals must come from the prescribed custodian commands and parse under an exact schema; their existence is not a chronology or census attestation. Dispatch/release verification is a separate required run-record check.” Prefer implementing these bindings and recording their results.

Consequence: a tool PASS is conditional on authentic custody of inputs and seals. This is partly a custody matter, not a claim that hashes can prove reader independence.

C. D1 comparison and failures

For each source wording “We choose a = 41.”, “We fit a = 41.”, “We measure a = 41.”, and “We adopt from X a = 41.”, my borrower says “We take a from source.txt.” and does not print a's value. Wording B's claiming-paper evidence passes validate in all four cases. A second source line repeats a = 41: line 1 passes; filing line 2 fails with the exact first-line diagnostic. Outputs are in `_review2_codex/d1/`.

The wordings do not yield identical filings: A quotes the external source line; B quotes the borrower. For these four cases their intended (status, origin, value) is the same: (PRINTED, IMPORTED, 41). B is safer because the evidence refers to the borrower's import rather than tempting a reader to transfer the source's verb to the borrower. A is not staged as an executable alternative. Its short paraphrase also lacks B's explicit full eligibility/tie-break provisions, so I would not certify identical classifications for every possible case until A states those provisions. A claimant-specified later locator may identify a different context; B explicitly chooses the first symbol-and-numeral line, rather than the locator-sensitive alternative mentioned in the reconciliation's T8 row. That choice must remain visible to the principal.

F4. Import refiled CHOSEN still passes

Verbatim quote: “The origin records the claiming paper's import regardless of how the external source obtained the value; no reason code is applied to the source's line.”

Defect and evidence: `import_refiled_CHOSEN` retains the borrower's claim_id, external value/source line, but changes origin to CHOSEN and evidence to ORIG_CHOICE_STATED quoting “We choose a = 41.” at source.txt:1. C3_NO_SUBSTITUTION=PASS. The binding checks occur only when status is PRINTED AND reason_code is ORIG_CITATION; selecting another reason code avoids them. This is precisely a T8 defect that revision 2 says is repaired.

Exact addition: “For every PRINTED record, validate first binds claim_id to the claiming candidate. If source_file differs from that claiming file, origin must be IMPORTED, reason_code must be ORIG_CITATION, and all D1 import checks apply regardless of the submitted reason code.” Add the CHOSEN bypass as a failing control. Specify any legitimate exception explicitly rather than permitting it through another reason-code branch.

Consequence: current validation can change the provenance tally from USES_IMPORTED to USES_CHOSEN without changing the borrowed number. B reduces reader ambiguity but does not presently close the machine bypass.

F5. The promised symbol floor fails open

Verbatim quote: “the value is a numeric token at the cited source line and that line is the first carrying symbol and numeral.”

Defect and evidence: `no_symbol` supplies symbol a, value 41, source line “We choose b = 41.”, with no a anywhere in the source. C3_NO_SUBSTITUTION=PASS. `first_line_with` returns None and the implementation rejects only a non-None first line that differs from the submitted line.

Exact addition: “If no source line carries both the recorded symbol and the recorded numeric token, validate fails; otherwise the cited line must equal the first such line.” Add the missing-symbol control.

Consequence: the advertised machine floor permits importing a different quantity's value. A syntactic first match still cannot establish that the source discusses the intended quantity; that remains an explicitly limited reading judgment.

D. Independence: procedure versus access control

Stage 1 and stage 2 add useful commitments, but source-only enumeration before ANY ledger exposure is not enforced by these tools. The auditor's inventory restriction and custodian's release order provide the intended protection. `seal-enumeration` checks enumeration bookkeeping, not source access history, all-89 reading, engine identity, or freedom from prior exposure. `seal-rederivation` hashes a file without requiring stage 1 or selection. `handout` itself takes the full sealed candidates as input, so it must run only in custodian custody; giving the auditor its command inputs defeats the intended restriction.

The design does not mechanically close these exposure-channel classes: pre-placed/copied/hard-linked/symlinked ledgers in accessible directories; earlier batches or other seats reachable through shared storage, mounts, backups or temporary files; inherited conversation, memory, retrieved context or reused sessions; premature selection/group lists or a handout before enumeration; operator messages, tool output, logs, errors, attachments, previews or clipboard excerpts; accessible processes, open file descriptors, IPC or network services; runtime/startup/import surfaces carrying copied content; another actor releasing files early; editable, substituted, backdated or concurrently created seals and access records. Prior training or prior exposure outside the run also cannot be disproved. This is a list of channel classes, not a claim to enumerate every possible covert channel.

These are custody matters where the candidate already acknowledges the C4 floor. F3 is the concrete missing verification interface; unqualified claims of actual independence are wording defects. Required run-plan addition: inventory and probe each dispatch's accessible surfaces, enforce fresh auditor context and custodian-only selection, record release events against both commitments, and report deviations. Do not infer chronology from seal existence or filesystem timestamps. No tool result here proves that an actual independent census occurred.

E. Batching: the original logical defect is repaired, but join is weaker than advertised

The old argument “§1 is per passage, therefore a union of text partitions preserves all work” was insufficient. §2's IMPORTED rule consults a named source in another paper, potentially another batch. §2 extraction and classification also require surrounding recipe/input context within the claiming paper. Whole-text ownership preserves that local context; furnishing the entire corpus preserves named-source access. I found no separate §1/§2 mandate for a global cross-paper consistency computation or recursive provenance tracing; cross-batch reader consistency remains a real methodological limitation, not an invented additional rule.

Revision 2 explicitly partitions ownership rather than access, requires all 89 texts in every session, permits/logs cross-batch lookups, and requires full-corpus validation after joining. The kit's cross-batch import positive and batch-only negative both passed their expected assertions. Therefore IMPORTED_RULE_BREAKS_PARTITION=NO judges this revised proposal. It would be YES for exclusive batch access. The proposal must retain all-corpus access, per-lookup digest/file/line logs, and the auditor's same access; it should add a dispatch check recording availability/byte verification of all 89 texts per session, since final ownership coverage alone does not verify earlier reference access. Neither coverage nor join verifies the lookup logs.

There is one mechanically joined denominator per seat, followed by reconciliation into one denominator. That can implement one census read by two independent seat processes over multiple sessions, conditional on actual reading, access and reconciliation evidence. The partition/seal/join argument alone proves none of those human/engine conditions. The text properly admits that between-seat disagreement by batch cannot measure within-reader drift.

F6. Global identifiers and claim linkage are only partially enforced

Verbatim quote: “every candidate id, claim id and input id begins with `<owned file>#`, so nothing is renumbered at join and a cross-batch `derived_from` reference resolves by its own name.”

Defect and evidence: join checks candidate prefixes and the file-prefix ownership of claim_id, but never checks input_id's prefix or that a ledger claim_id names an existing candidate. My combined probe returned JOIN=PASS; isolated probes in `_review2_codex/batch_isolate.py` also return `id_only 0 JOIN=PASS` and `orphan_only 0 JOIN=PASS`. Derived-from resolution/cycle checks exist, but do not repair orphan claims or nonglobal input names.

Exact replacement requirement: “join requires every ledger claim_id to name an included candidate owned by that batch and every input_id to begin with that candidate's source_file followed by #; candidate and input identifiers are unique, and every derived_from resolves in the joined graph, which must be acyclic.” Implement those checks and separately test them.

Consequence: JOIN=PASS currently cannot establish the advertised ownership/linkage invariant. Later import validation catches some orphan import claims, but is not a replacement for join's promised rule or a universal check across statuses.

F7. Join does not verify the predecessor chain

Verbatim quote: “`join <partition> <seat_dir> <seals> <manifest> <prefix>` verifies every seal”.

Defect and evidence: seal writes predecessor_seal_sha256, owned_files and owned_sha256, but join checks only the partition digest and artefact digests. It never recomputes the predecessor chain or compares the sealed ownership fields to the partition. In the isolated `chain_only` probe I supplied otherwise consistent artifact hashes and global/resolving claim names, replaced batch 2's predecessor digest with 64 zeroes, and received JOIN=PASS.

Exact replacement requirement: “join verifies the partition and manifest binding, each seal's owned file/digest lists against that partition, every artefact digest, the complete ordered predecessor chain, and absence of missing or extra batch seals.” Implement and test independent corruption of each binding.

Consequence: current join establishes artifact-byte agreement with the supplied seal map, not the claimed verified commitment chain. Custodian write protection reduces the threat but does not make the stated verification true.

F. Remaining overclaims and required sentence replacements

F1–F7 identify operative promises whose implementation is insufficient; their replacements above are required in addition to the following editorial corrections. Quotes below reproduce the relevant sentences, with line wrapping normalized. Each consequence is stated so that wording repairs do not conceal implementation repairs.

1. Candidate: “Their findings are reconciled BY TOPIC in `R3C2_CANDIDATE_REVIEW_RECONCILIATION_20260906.md`; every accepted repair is in this revision and in the staged kit.” Replace with: “The reconciliation lists intended repairs; revision 2 implements many of them, with remaining clause/tool gaps listed in the independent revision-2 review.” Defect: F1/F4/F6/F7 refute closure. Consequence: no all-repairs-complete inference.

2. Candidate: “They assign the same classification (status, origin, value); their EVIDENCE RECORDS differ (which file and line `origin_evidence` names).” Replace with: “For eligible imports the intended status, origin and value agree; the evidence records differ, and wording A needs the same explicit eligibility and locator rules before equivalence beyond these examples can be claimed.” Defect: A is abbreviated and unimplemented. Consequence: no universal filing-equivalence claim.

3. Candidate: “That the quoting sentence is a genuine citation of THAT value — not a sentence naming the source for something else — is seat judgement, caught by the second seat and by C6's re-classification, never by the machine.” Replace with: “Whether the quotation cites that value is seat judgment; the second seat and C6 may detect an error, but can share it, and C6 re-classifies inputs only for selected claims.” Defect: “caught” guarantees detection, including unsampled claims. Consequence: citation-semantic errors can survive PASS.

4. Candidate: “The two reviews of revision 1 then found the comparison narrower than the words (excluded-only passages vanished; zero denominator passed; auditor census not enforced; selection trusted, not recomputed; re-derivations unsealed; "both sealed ledgers" when the object is the merged file): all repaired above and in the kit, each with a control that asserts its exact failure and a deletion probe.” Replace with: “Revision 2 adds controls for these cases; missing-seed selection bypass and output-contract gaps remain, and census/seal authenticity also depends on custody.” Defect: tested branch repairs do not establish universal closure. Consequence: no unconditional C6 conformance claim.

5. Candidate: “`CENSUS_COMPLETE` and `CENSUS_PARTIAL` then rest on an audit whose enumeration was produced without sight of the seats' lists and whose re-derivations were sealed before the seats' numbers were released.” Replace with: “Those conclusions require a run record supporting enumeration before ledger exposure and re-derivation commitment before release, in addition to the repaired machine checks.” Defect: accepting words does not establish observed chronology. Consequence: independence remains conditional.

6. Candidate: “The audit's PASS then rests on an independent enumeration and blind re-derivation rather than on an anchored review of the seats' lists; it is bounded evidence, not proof of corpus completeness.” Replace with: “A PASS accompanied by satisfactory dispatch and release evidence supports the intended independent enumeration and blind re-derivation; shared error and prior exposure remain possible.” Defect: the qualification must attach to the independence assertion itself. Consequence: PASS alone is insufficient.

7. Candidate: “**D7 in code** (`audit seal-enumeration | select | handout | seal-rederivation | compare`): as the clause states.” Replace with: “D7 is partly implemented; resolve the revision-2 review's selection, output-schema and commitment-binding findings before claiming conformance.” Defect: executable and schema counterexamples. Consequence: staged does not mean conformant.

8. Batch: “Batch 1, the lightest, therefore confirms less about capacity than a heavy batch would.” Replace with: “Batch 1 has the fewest bytes, but batch 11 has fewer non-blank lines (3321 versus 4030); success on either would establish only that batch's observed feasibility.” Defect: “lightest” changes metric and no successful run has occurred. Consequence: no general capacity inference.

9. Batch: “The partition is a function of the manifest and the number 12 alone; anyone can recompute it and must get the same bytes (kimi did).” Replace with: “The pinned partition implementation deterministically computes these bytes from this manifest and 12; identical serialization and implementation are required for byte equality.” Defect: abstract partition choices do not uniquely fix serialization. Consequence: reproduce with fixed code, not any partition implementation.

10. Batch: “§2's arithmetic is per claim and its IMPORTED lookups are served under §1 of this file, so no claim is split or blocked by the partition.” Replace with: “Whole-text ownership preserves a claim's local context; cross-batch imports are not blocked by withheld evidence if each dispatch supplies and verifies all manifest texts as required.” Defect: proposed supply is a condition, not executed evidence. Consequence: per-session access needs verification.

11. Batch: “The comparison code is unchanged; preserving its meaning additionally requires the same evidence access and valid global identifiers under batching, which §1 and §3 supply.” Replace with: “Sections 1 and 3 require equivalent evidence access and global identifiers; dispatch checks and the repaired join must verify their implementation.” Defect: clauses specify rather than supply or validate those conditions. Consequence: conditional preservation only.

12. Batch: “Per-claim outcomes and classes are computed exactly as V23 states, over the joined files.” Replace with: “Per-claim outcomes and classes use the operative rules explicitly accepted for this run, including any accepted D1/D2 changes, over the validated joined files.” Defect: the candidate deliberately changes evidence/classification handling and the living draft includes D2; exact V23 identity overstates scope. Consequence: identify the actual rule set behind the denominator and provenance tally.

13. Batch: “It is the difference between a census that can run and one that cannot — a necessity established by one observed failure, not by a demonstrated successful session, which batch 1 will be.” Replace with: “One observed failure motivates testing this batch design; no successful session has yet established its feasibility or necessity.” Defect: one failure proves neither universal inability nor future success. Consequence: capacity remains unmeasured.

14. Batch: “(Blocks a first run: without it, no seat completes.)” Replace with: “(A run requires a demonstrated workable reading procedure; the evidence so far does not establish that every unbatched seat would fail.)” Defect: universal completion claim unsupported. Consequence: principal may choose other workable execution designs.

The reported 84/84 result is accurate for my run. The hypothetical all-texts-furnished rule, non-adoption status, determinism under fixed inputs AND fixed code, and the explicit shared-error/drift limitations are not themselves overclaims. I do not label every prescriptive “must” as a demonstrated empirical assertion.

T1–T13 reconciliation check

| Topic | Revision-2 status | Evidence and remaining limitation |
|---|---|---|
| T1 import breaks partition | REPAIRED | Both documents require all-corpus reference access for seats/auditor; kit full-corpus import positive and restricted-access negative behave as stated. Actual dispatch/logging remains procedural. |
| T2 cross-batch ids/graph | PARTLY | Join preserves ids and checks graph resolution/cycles; kit exercises unresolved references. Independent id_only/orphan_only probes still PASS (F6). |
| T3 completeness breadth | PARTLY | Independent four-asymmetry cases now list omissions/disputes correctly; result vocabulary, per-input rows and study-failure filing still differ (F2). Stricter Kimi excluded-only resolution is present. |
| T4 zero/disposition rows | REPAIRED | Kit zero-denominator negative passes its assertion; my rows carry both dispositions and my 2/20 versus 3/20 probes behave correctly. |
| T5 auditor census | REPAIRED | seal-enumeration invokes census and rejects its failure; suite assertion/deletion probe pass. This is bookkeeping, with authentic-command custody prerequisite (F3). |
| T6 selection integrity | PARTLY | Ordinary missing seal, edited selection and first-write tests pass; my absent-seed emptied selection gets PASS (F1). |
| T7 auditor independence | PARTLY | Handout and both commitment stages exist, with custody floor stated; executable commands do not enforce exposure chronology, and consequence prose still overstates it (D, F3, F.5–6). |
| T8 D1 floor | PARTLY | Four verbs, first-line tie break, manifest/token/quotation controls work; CHOSEN bypass and absent-symbol case still PASS (F4–F5). Locator policy is first occurrence, not the alternative in the reconciliation's first T8 entry. |
| T9 wording identity | PARTLY | Evidence-record difference and B-only code now stated; universal classification-equivalence assertion still needs A fully specified (C, F.2). |
| T10 D1 consequences | REPAIRED | Candidate now allows REPRO_FAILED and explicitly declines transitive provenance. No promise that import availability proves arithmetic success. |
| T11 seals/coverage | PARTLY | Partition binding, seal order, coverage byte checks and fixed-code determinism controls pass; independent broken-chain join still PASS (F7). |
| T12 overclaims | PARTLY | Workload hypothesis, third-engine distinction, no drift measurement and bounded completeness are stated; remaining unsupported capacity/independence assertions quoted above. |
| T13 stale pins/counts | PARTLY | Current 84/84 and 29 probes agree with execution; all seven kit-relative pin entries verify, including partition.txt. Requested root-relative pin verification fails (A). |

The candidate has made substantive repairs, especially ownership-versus-access and the four completeness asymmetries. It still requires the specific clause, code, output-contract and custody repairs above before the principal could rely on its promised validation predicates. Nothing in this report adopts, freezes or runs a census.

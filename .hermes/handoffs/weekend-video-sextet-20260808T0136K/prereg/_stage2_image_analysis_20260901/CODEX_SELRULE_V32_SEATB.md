ACCESS_SHA=7620673b90562ccf262c84aed0838b2cc31638d2de73224125accbdb9b87aa32

Independent Seat B review of the complete, staged, unadopted V32 package. The access hash and signature preimage match the requested candidate. Nothing here adopts the rule, composed mode, OPS label, holdout enforcement, split verification or a seed.

The V30 null-open-file FATAL remains repaired, and the restored driver passes. I found no new composed acceptance of the null-file/rewrite attack. Nevertheless, NSD is not enforced over the complete package: independently available findings still disappear, and partial evidence can produce a terminal contradiction that complete evidence reverses. The package is NOT ready for adoption questions.

Authorship: the package records earlier Codex builder field-validation authorship at 00:13–00:18 on September 6 and says that code no longer participates. I did not modify the implementation. I used the lane's temporary-repository harness for independent constructions and separately replayed its tests; these are distinguished below. Historical authorship and chronology depend on retained records, not my current execution.

References: D = `_optionA_dev/fourier_chirality/run_configurations_v16.py`; P = `_optionA_dev/track2/provenance_designs_v12.py`; T = `_optionA_dev/track12/test_track12_fail_first.py`; R = the reviewed V32 rule, particularly its opening paragraph, line 3, and §3c, line 38. Line numbers refer to these reviewed bytes. Sources, full outcomes, first and final suite logs, and probe fixtures are retained outside the reviewed directory at `/var/folders/64/71dstw0j1gd_n58lsxnhl3p80000gn/T/codex_v32_seatb_r3hostpx`. Only this report was written inside the reviewed directory.

**V32-1 [MAJOR] — NSD remains an UNREPAIRED CONTRADICTION. The table and its controls conceal real dependencies and independent subchecks.**

NSD is named coherently: no stage decides or aborts; every stage contributes; one resolver decides. The final minimum at D:507–513 is implemented. The collection preceding it is incomplete.

Independent executions:

- Delete the identity file while retaining a readable wrong-repository open event: `IDENTITY-MISSING`; no open-local finding. D:369 raises before D:375 reads the open file. Repeat with an obtainable open same-ID contradiction, a published rewrite, an open-delivery defect, or a per-entry batch: each independent finding disappears. These are precisely the five `identity-file` pairs the table declares independent.
- Root discovery at D:399 is conditional on reading the identity. Consequently these cases mark history blocked for “no local repository root” although the repository exists and git works. The diagnostic describes an implementation dependency as unavailable evidence.
- Malform the approval commit while retaining an open same-ID contradiction and make `remote_head` unavailable: S3 blocks `approval-live` at D:465 before reaching the independent open check at D:481. S5 cannot rescue it. No OPEN-EVENT-FORGED is contributed. This particular malformed-identity probe also produces the expected unsealed-identity finding; that does not make the separately readable open evidence unavailable.
- A retained approval `repo` list raises in the S0 approval check before the readable wrong-repository open event is examined. With the remote down, that open-local finding is absent.
- A coherently sealed identity with unverifiable nonce bodies normally produces `NONCE-UNAUTHENTICATED`. Add only the labelled freeze-fetch failure: `WITNESS-FETCH-FAILED` wins and the nonce finding vanishes. D:228 stops the conjunction before D:295 verifies retained nonce bodies. Those bodies, nonce fields, and the BLS verifier are available without the freeze fetch. “The conjunction needs witness-fetch” is not an exact prerequisite statement for every check inside it.
- A coherently sealed wrong schema plus wrong pool digest and failed fetch contributes the schema and fetch findings but not the independently readable pool mismatch. S0c stops at D:407; the subsequent checks are neither contributed nor individually blocked.
- An unavailable provenance import still decides before collection at D:357. Wrong open repository plus this labelled import failure yields only `VERIFIER-UNAVAILABLE`; `LAST_OUTCOME` remains unset in a fresh invocation. Naming the exception is an improvement over raw ImportError, but the expressly disclosed exception contradicts the unconditional NSD property and carried V31 clause about verifier availability.

A further degraded-context probe changed the working-tree approval record, set the coherently sealed witness digest to those changed bytes, and failed only the freeze fetch. The result was WITNESS-FETCH-FAILED, with S4 marked completed and no blocked checks. D:442–446 obtains the old approval-commit blob without checking it against the witness digest; only the fallback working-tree read at D:447–450 checks that digest. Thus S4 can use different approval bytes from the ones the witness names, contrary to R’s stated degraded-context binding. This did not ACCEPT, but the advertised binding and contribution completeness are false.

The table is therefore not true as an exact input/code inventory:

| Check | Audit of declared prerequisites and contributed codes |
|---|---|
| approval-local | Its event needs local witness fields; nested malformed values can raise additional classified shape failures. Its placement incorrectly controls the independent open sweep. |
| approval-delivery | It executes as S0d-delivery, not the table's S0-local. Head/commits delivery does not inherently need git; ancestry may. I obtained DELIVERED with git unlaunchable for head equality. Root/commit branches can do nothing and still mark the stage completed. |
| open-local | The semantic inputs are the open file and protocol pins; implementation additionally requires earlier identity/approval processing to survive. |
| identity-local | Also reads the adoption file at D:412. ADOPTION-MISSING/MALFORMED/MISMATCH and IDENTITY-T-PULSE are among omitted possible codes. Its individual checks do not share one indivisible prerequisite set. |
| lists | Lists and sizes suffice, but the first failed list suppresses other list/overlap checks. Nested invalid values can produce shape exceptions beyond the listed codes. |
| conjunction | The short seven-code list is not complete for D:221–332. Local nonce, adoption, record, history and binding checks have different prerequisites; the four-column union overstates necessary dependencies. |
| approval-live | Authentication also uses commit/event shape, protocol pins, conditional ancestry, completeness, and optional receipt inputs. EVENT-INCONSISTENT is an omitted possible contribution. |
| open-same-id | Needs no approval commit, but S3's approval gate imposes that dependency. |
| seed | Needs retained beacon/approval bytes, adopted digest and round, not merely a readable identity and verifier import. D:497 explicitly blocks on additional unavailable inputs. |
| history-remote | Includes independent remote-blob checks and later local-file checks; identity availability is an accidental caller prerequisite. |
| open-delivery-auth | Local shape/ref and some delivery checks need less than the full remote/feed dependency set. These must be separated from authenticated presence. |
| per-entry | Requires remote commits/parents and usable event fields; partial versus complete evidence changes what may be inferred. The enclosing function can erase its findings on unrelated later failure. |

The prerequisite failure codes are also oversimplified: an absent open file produces HISTORY-OPEN-EVENT-MISSING, not the table's INVALID; a non-object identity produces IDENTITY-SCHEMA, not IDENTITY-MISSING.

I independently extracted the table with AST: it generates **71** independent pairs, not 66. T:110 explicitly skips `identity-file`, removing all five pairs listed above. The 66 generated methods exist, but “every pair” is false. T:95–107 checks selected code membership, nonempty reasons, and the resolver over the findings that survived. It never asserts equality with an independently expected full finding set. At T:105–106, any contribution by a shared stage can excuse another check in that stage. This is the precise whole-outcome weakness Blanc prohibited; it is not cured by describing the refinements as bookkeeping.

**V32-2 [MAJOR] — partial-snapshot absence is used to decide FORGED. UNREPAIRED CONTRADICTION with R §3c's no-absence inference and rule (iii).**

P:237–240 evaluates `not present` and the same-commit arm before P:241 checks `complete`. Absence from an obtained prefix is not absence from the completed retrieval.

Executed on the complete composed path with one coherently sealed identity:

| Fixture feed | Result |
|---|---|
| Page one contains a distinct later qualifying delivery, all history events and filler; page two returns HTTP 503; retained approval would be on page two | EVENT-FORGED |
| Identical page one; page two supplies the verbatim retained approval | ACCEPTED |
| Pure helper with the corresponding partial/full snapshots | FORGED / AUTHENTIC |

This is a fixture-supplied distinct qualifying-event construction testing the package's expressly accepted rule-(iii) semantics. It does not establish that GitHub honestly emits two protected-ref deliveries of an already-delivered commit under the branch-protection assumptions. The implementation contradiction requires no such claim: the same permitted full snapshot reverses the purportedly affirmative partial finding.

A same-ID canonical contradiction is different: a later verbatim copy cannot reconcile it under rule (ii), which explicitly refuses conflicting same-ID evidence even beside a verbatim copy. That affirmative predicate correctly survives a later page failure. The missing-retained condition in the same-commit arm does not have that property. Likewise, P:413–416's batch disposition depends on not finding an own-publication event; that negative condition needs the same scrutiny before being called affirmative on a partial feed.

The ordinary partial-no-contradiction cases refused, including my standalone history probe. I found no partial-snapshot composed ACCEPT. The defect is a wrong terminal disposition, not a demonstrated acceptance bypass.

**V32-3 [MAJOR] — later exceptions still erase history findings; provenance is not consistently tracked at the actual input boundary. UNREPAIRED CONTRADICTION.**

P:374 accumulates a private F and returns it only at P:429. D:504 adds those findings only after the helper returns. Removing `break` does not preserve findings if an exception escapes.

- Published rewrite plus a remote PushEvent with object payload and `commits: [null]`: retrieval's shallow shape filter at P:184 accepts the event; `delivery` at P:200 raises AttributeError. The composed outcome contains two class-5 MALFORMED-REMOTE-EVIDENCE findings, from S3 and S5, and **no HISTORY-NOT-AN-EXTENSION**. The independently derivable class-4 rewrite is lost and a retry wins. The same rewrite with usable feed evidence is terminal.
- Published rewrite plus a missing working-tree history file: S1 contributes COLLECTION-LOG-DIGEST. S5 derives remote findings, then P:423 raises FileNotFoundError. Its remote rewrite findings disappear; the only S5 contribution is IO-UNAVAILABLE and its blocked map is empty. The winner remains terminal because S1 happened to catch the file, but whole-outcome preservation fails.
- The standalone v12 history wrapper accepts a feed containing all required events plus a scalar-payload malformed PushEvent. `retrieve_events` records and removes the bad event, but P:436–440 never contributes `prov['malformed']`. My equivalent composed probe refuses malformed remote evidence. The two states do not share the claimed complete collection behavior.

The retained/remote label on an entire S3/S5 body is too coarse. Those bodies inspect retained events, remote events, local files, and git outputs. Their source must be attached where each operation consumes its input; a later exception must not discard earlier contributions. Receipt exceptions are the repaired exception: D:475–477 correctly converts them to the class-3 receipt-loss policy, including the list-valued origin regression.

**V32-4 [MAJOR] — the new aggregate gate can certify a failed block. UNREPAIRED CONTRADICTION with its stated filing safeguard.**

`scripts/aggregate_gate.py`:12 searches for any `^OK`, not the block's final result; lines 9 and 15 do not reject FAILED and cover only five exception prefixes. In an external synthetic one-suite log containing `Ran 1 test`, `OK`, followed by `FAILED (failures=1)` and `ValueError: fixture post-test failure`, the gate exits 0 and prints PASS, “every block OK, no exception lines.” This is a parsing probe, not a claim that the supplied RUN2 log contains such a failure.

The actual filed RUN2 passes and RUN1 fails, as required. The restored `load_manifest` is verbatim v15; v16/v15 top-level definition-name sets match; both caller sites remain. The repaired driver passed 23/23 independently. Thus the concrete NameError repair is real, but the new universal gate guarantee is stronger than its implementation. Require an unambiguous terminal result per suite, reject any failure/error result, and bind suite process exit status to the aggregate.

**V32-5 [MINOR] — remaining totality, diagnostic and evidence-accounting claims are false.**

- I extracted all 148 AST `raise` nodes from D/P rather than relying on the test's string-prefix regex. D:629–635’s dynamically formatted `TUNING-RECEIPT-{i}-CONFIG/COUNTS/JOURNAL-MISMATCH/DERIVED` codes are not represented by the literal allowlist names. I actually invoked `reconstruct_winner` and obtained `TUNING-RECEIPT-0-CONFIG`; `classify_refusal` flagged it unclassified. SPLIT-* and unknown EVENT-family handling are repaired. This remaining example is outside composed identity loading and fails closed; it disproves the broader “every actual driver raise placed unflagged” assurance, not a new selection bypass.
- After an unrelated remote-only commit, I reset a local fixture to its earlier HEAD while retaining the identical history blob. Composed mode ACCEPTED. With an added freeze-fetch failure it refused and remained degraded. P:422–428 tests local-only commits and history-blob equality, not HEAD equality; its success wording “working tree equals the live remote head” must be scoped accordingly. No unpublished history was accepted in this probe.
- The run-1d per-subcase table at receipt line 280 covers **81**, not 84 methods. It omits V31_4b and V31_5a/5b because their verbose unittest names wrap onto separate lines. The full log has 79 failures, 4 errors, 1 pass. Correct classification: **42 code-behavior/classification failures, 1 text failure, 39 new-interface tests without fail-first standing, 1 already-right pass, and 1 raw runtime ImportError demonstration**. Equivalently, retaining the receipt's broad category that includes text gives 43 BEHAVIOURAL and 39 NEW-INTERFACE, not 42/37.
- Run 2 actually ends 30 failures; run 2b ends 2 failures. Subsequent targeted/text runs and the passing final aggregate establish the current result; “run 2/2b: 84 OK” is not either log's result. The original nine-method artifact explicitly says the first receipt was overwritten and the retained text reconstructed from a captured tail, with unreached subcases listed. It must not be described as an untouched complete original log. The reconstruction and per-subcase limitations are disclosed; I do not infer missing historical execution.

These are corrections to an integrity report, not adoption choices. R:3/38 and the receipt need the accurate counts and qualifications.

**Executed states, precedence and contribution probes.**

| State | What the executions establish |
|---|---|
| Offline production-default mode | Accepts the disclosed coherent fabricated-event, rebuilt-history and late-first-publication cases 1, 2 and A. Still enforces the witness-bound retained-evidence conjunction, nonce/BLS seed checks and list rules. Undetermined approval delivery uses IDENTITY-WITNESS-COMMIT-UNDETERMINED; offline also exposes witness and re-derivation availability refusals. |
| Standalone v12 helpers | Refuse local mismatches, affirmative contradictions, invalid published continuation, late first publication and the named availability/loss cases in their scope. They do not perform the driver's full identity conjunction. My additional malformed-feed acceptance and partial FORGED findings above qualify their claimed collection contract. |
| Composed v16 on v12 | Accepts the honest complete fixture; refuses disclosed attacks 1, 2 and A, null/non-object open files, published rewrites, missing evidence and the carried combined cases. S1 refusal does not permit ACCEPT in my degraded probes, but still suppresses some findings and permits wrong winners as above. |

The offline `_conjunction_prefix` and `load_identity` bodies are byte-identical to v15. Relevant successor imports change; the offline algorithm remains the same. This is stronger evidence than merely matching its happy-path verdict.

I ran all 17 track-12 regression methods, including fetch failure with same-ID/schema/rewrite, git launch failure with wrong repository, unavailable helper import, page-two HTTP/JSON failure, later per-entry batch, undetermined same-commit arm, scalar remote payload and list-origin receipt. They pass on current bytes. I also ran the 15 existing track-8–11 code tests with labelled import aliases to v12/v16/current fixtures, including the current standalone continuation alias; all pass. That re-exercises the V30 constructions and V28/V27 combined precheck cases on current modules rather than treating predecessor test results as evidence about new code.

Thus the carried named cases retain their intended dispositions: approval unknown-before plus same-ID contradiction → EVENT-FORGED; wrong repository with healthy feed or HTTP 503 → EVENT-INCONSISTENT; undetermined delivery without contradiction → RETRY-EVENTS-UNAVAILABLE; positive non-delivery → EVENT-INCONSISTENT: IDENTITY-WITNESS-COMMIT; open-event analogues → OPEN-EVENT-FORGED / OPEN-EVENT-INCONSISTENT-INPUT / EVIDENCE-UNAVAILABLE through the history refusal names. Before-only/head-only contradictions, same-ID conflict beside a verbatim copy, strictly earlier versus later/tied events, and absent-versus-expired distinctions remain exercised. The broad “both paths, every stage” clause is nevertheless false under V32-1/3.

My own 15 S0–S5 pairs used wrong open repository, witness-fetch failure, partial-page failure, approval same-ID contradiction, retained seed retry and published rewrite as independently coexisting findings. Every pair was executed in both feed orders. Both targeted stage contributions and reasons were present, and all 15 **full LAST_OUTCOME objects were equal** between feed orders. Resolver input reversal preserving fixed stage sequence selected the same finding; the separate 21 class-pair exhibit also passed both derivation orders. These tests cover the A/B/C/D combinations too. They do not prove that scheduling can be arbitrarily reordered while changing the specified same-class tie-break.

Additional simultaneous failures were executed: witness-fetch + remote-head with approval/open contradictions; git-launch + first-page failure with wrong open repository; witness-fetch + first-page + remote-head with schema or seed defects. The three-failure seed case preserved WITNESS-FETCH-FAILED, RETRY-EVENTS-UNAVAILABLE, REDERIVE-RETRY and remote unavailability with reasons. This positive evidence coexists with the five omitted identity pairs and independently invalid nonce that fail NSD.

GitHub documents event IDs as unique and the PushEvent payload with ref/head/before; a commits array is not required. An honestly distinct event should not share another event's ID. The fixed FORGED names remain appropriate for the package's retained/live contradiction disposition, without identifying which producer supplied false evidence. An honest protected-branch fast-forward does not by itself demonstrate redelivery of an already-delivered commit; the synthetic rule-(iii) fixtures must remain labelled as such. [GitHub event types](https://docs.github.com/en/rest/using-the-rest-api/github-event-types).

**Disposition of carried findings and the two categories.**

“REPAIRED” below certifies the original concrete behavior and retained regression, not an unqualified universal collection guarantee.

| Item | Judgment |
|---|---|
| V31-1 | Original fetch/git cases repaired; whole NSD claim NOT REPAIRED: V32-1. |
| V31-2 | Obtained pages retained; no-partial-absence promise NOT REPAIRED: V32-2. |
| V31-3 | Original loop/both-arm cases repaired; exception-safe collection NOT REPAIRED: V32-3. |
| V31-4 | SPLIT, unknown-family flag, scalar-remote and receipt examples REPAIRED; totality/provenance universal claims NOT REPAIRED. |
| V31-5 | Reasons and stage-state interfaces built; per-check completeness and evidence wording NOT REPAIRED in full. |
| V30-1 FATAL | REPAIRED; null/non-object open file cannot disable required history into ACCEPT. |
| V30-2, V30-3 | Original regressions REPAIRED; complete-path contribution promises NOT REPAIRED. |
| V30-4 | REPAIRED; offline's several availability dispositions accurately distinguished. |
| Blanc's four precedence items | Order stated and resolver built; class-pair exhibit and retained tests REPAIRED; one enforcing place over every available finding NOT REPAIRED. |
| Blanc 05:02/05:09 | Named property and split regression methods built; true input table, every pair, whole-outcome controls and full per-subcase accounting NOT REPAIRED. |
| V29-1/2 | Concrete seed/remote/feed priority cases REPAIRED; universal clause still qualified by V32-1/3. |
| V29-3/4 | REPAIRED: pin/name corrections and strictly-earlier ordering. |
| V28-1/2 | Concrete approval/open precheck cases REPAIRED; every-stage assurance NOT REPAIRED. |
| V28-3 | Historical citations and full-feed later-versus-earlier rule REPAIRED; partial application is V32-2. |
| V27-1 | Original local/same-ID/absent-only ordering cases REPAIRED; whole-pattern claim remains open. |
| V27-2/3 | Tri-state propagation and historical lineage/text corrections REPAIRED; current table/status inaccuracies are separately identified. |
| V26-1/2/3 | Before/head contradictions, unknown-object tri-state, expiry vocabulary and historical text corrections REPAIRED in original scope. |
| P1 | Ancestry-aware batch predicate REPAIRED; complete collection and partial negative conditions retain V32-2/3. |
| P2 | Plain absence/empty-feed false-forgery repair retained; partial absence now violates the broader promise. |
| P3/P4 | Cost/availability text and covenant inclusion REPAIRED. |
| N1 | COVENANT, not operation-completeness enforcement. |
| N2/N3 | Original missing-versus-batch dispositions and producer unrelated-commit refusal REPAIRED; collection qualifications above apply. |
| N4/N5 | Historical attribution/label corrections retained; new accounting defects are V32-5. |
| M1 | Ordered separate publication built; operation-time remainder COVENANT; collection exceptions remain. |
| M2 | Pending commit reconciliation and publication of outer failure entries REPAIRED. |
| M3 | COVENANT correctly covers before and between publications. |
| M4 | A′'s unbuilt history receipt paths DISCLOSED-AS-OPEN; C's current readiness assertion cannot be certified. |
| M5 | Archived original bytes and immutability mechanism REPAIRED, with copied-list qualification below. |
| M6 | Historical text sweep retained; new diagnostics/claims need correction. |
| A | Authenticated genesis-only opening REPAIRED; unpublished-operation remainder COVENANT. |
| B/C | Producer boundary and shared delivery semantics built; original repairs retained, collection qualifications above apply. |
| D/E | Builder control-refusal logging and last-relevant-render-end checks REPAIRED. |
| F | Original empty-feed/HTTP/availability cases REPAIRED; partial/malformed collection still has V32-2/3. |

Not every DISCLOSED LIMIT is irreducible, and §3c now correctly says so for L-INH. L-OFF is a selected-mode limitation; L-INH is a changeable implementation choice; L-AVAIL combines external retention with the chosen stateless closure covenant. L-COV is structural without independent decision evidence; L-RCPT is structural under the one-account, label-only receipt design. These are substantially honest scoped disclosures. They cannot absorb wrong winners, suppressed readable evidence, false completeness assertions or a faulty gate. Those belong in UNREPAIRED CONTRADICTIONS, replacing “none known.”

**Covenant, receipt trust, questions and cost.**

The complete covenant is present in P's header, the design document, §3c and the unchanged questions file: authenticated published append-only history and ordered distinct publications do not establish underlying operation times or completeness of unpublished observations/decisions; an unpublished absence-based CLOSED can disappear before genesis publication or between later publications; the fixed-round seed is unchanged; an authentic late approval remains disqualifying; stronger completeness needs independent retained decision evidence, not implemented.

I appended and removed an unpublished CLOSED in both intervals in temporary fixtures. Offline and composed both ACCEPTED. This is the disclosed covenant behavior.

I created and published a first receipt under the lane-proposed `{actor: ops-witness, session: OPS}` without an OPS-retained copy. The verifier accepted it. With approval expired but all history evidence live, composed mode with the approval receipt ACCEPTED; Option C returned EVENT-EXPIRED-NO-RECEIPT-PATH. My first setup left older history timestamps in the feed and correctly got INCOMPLETE under both options; the retained corrected setup explicitly places the history events after approval. Neither result is concealed.

The trusted step is exactly the existence and OPS authorship of OPS's independently retained copy and pane record. Code verifies neither. The label is not Duho's decision. The recommended delegated workflow requests no per-receipt human confirmation. B's second identity or inaccessible custodian key is NOT IMPLEMENTED; a second token on the same account is not an independent identity.

Q1 C remains the sound recommendation after the contradictions are repaired: ALL required approval/open/per-entry events must authenticate at tune and holdout; evidence loss closes that approval under the rule, temporary unavailable/incomplete evidence retries the same commitment, and neither permits replacing approval, round, seed, split or attempt. The loader does not persist study-level closure. C's “only option that works today as described” presently overstates implementation readiness. A′ accurately labels approval-only receipt support and unbuilt open/per-entry support; its proposed substitutes apply only to EXPIRED. B is explicitly unavailable. Q2 correctly asks nothing. Keep Q held; these implementation repairs require no new Duho chore or permission.

The stated external window remains accurate: up to 300 events created within 30 days, with documented repository-event latency of 30 seconds to six hours. It is not a guaranteed duration available for completing both invocations. [GitHub Events API](https://docs.github.com/en/rest/activity/events).

Cost is one acknowledged push per HISTORY ENTRY, including genesis and failure entries; one collector/builder invocation may publish several entries. PENDING-PUSH reconciles the same pending publication; incompatible local rewrites diverge; remote unavailability has its named retry dispositions. No affirmative current “one push per freeze” claim was found. The design document line 34 contains “NOT one push per freeze” outside quotation, an explicit correction; its line 3 and P:140 quote the earlier mistake. Fixture remotes were local bare repositories with non-fast-forward receives denied; gh runners were fixture-supplied. No live publishing occurred.

**Execution, immutable pins and preserved items.**

All **232 tests in 28 requested suites** passed under the specified interpreter split, separate environment variables, PYTHONDONTWRITEBYTECODE=1 and warning settings. Counts: drivers 23/17; history 4; witness 3; builders 8/4; beacon 7; verifier 4; track 1 10; track 2 8/2; tracks 3–5 10/7/6; track 6 5+1; track 7 4+1; track 8 7+1; track 9 3+1; track 10 4+1; track 11 5+1; track 12 84+1. Historical label tests used their specified V25–V31 texts, not V32 by indiscriminate substitution.

My first aggregate had one track-12 setup error: fixture `git add collection_log.jsonl` died with SIGTERM. The first log is preserved. A full 84-test rerun passed; the final 232/28 aggregate incorporating that rerun passes the gate. Exactly one inherited RuntimeWarning occurred in the requested suite logs at fourier_chirality.py:87; no ResourceWarning occurred. The extra 15 current-module precedence tests passed.

The beacon exhibit ran twice with byte-identical output and digest `2160fa754ce3db25613389d58bacd3098763ea8536744558e9dae96c5b4f0ae1`. The drand-only exhibit reproduced `45d6149a2ccf30cb167dc4331455f3403a733516a82399292b1e7ad2c029e531`. The 21 resolver pairs passed. All inspection case verdicts matched filed V32 and V31 after excluding the version header and normalizing temporary commit IDs.

Signature preimages reproduced exactly:

- V32: `7620673b90562ccf262c84aed0838b2cc31638d2de73224125accbdb9b87aa32`
- V31: `f94b45e626ec95f1d2a60da783eb23c70f02394bbbe2be7389583013dd00cc49`
- V30: `98881c7ecba0ac3bb718983f8534aaa55d325efeb4314d72b31b64b95af2abb9`
- V29: `4458b821e3a1249c0646ce2790491f4d04e7224d0ef60721144354e216450599`
- V28: `c9e65f1bfc2bdac10716760670c85866d20c1ec0ca1d9aebdfa5b83842804fc2`

V32 has 105 distinct full digest values: 102 match retained file bytes; the remaining three are the reproduced two exhibit digests and sentinel value. V23–V31 have respectively 80/81/83/85/89/90/91/99/102 values, with those same generated-value exceptions. I hashed their retained matches and inspected filename associations. No missing historical bytes or new pin drift was found. Previously corrected V27/V28 wrong filename/digest associations cannot literally match the mistakenly named file; their intended bytes remain retained and current associations are corrected.

All four archived V22 originals match their pins. V22 and V24 copied-digest lists contain all four original values. The supplied V23 list contains none of those four original values. Therefore the requested stronger assertion about all three lists is false; the pin-drift record's specific V22-list support is present. The questions digest remains `4e6dc490485cf956a6471ccad6be73fb86bfe0dc0d60712343b18f3a162e8a52`. All indexed pinned file matches were rehashed unchanged after execution.

Individually preserved and rechecked:

- Sample sizes 400/200/2,000; floors 380/190/1,900; strict Wilson lower-bound >0.70; fixed denominators and one further attempt.
- Failed-set exclusion; 2,644 distinct dry-run identities; production exclusions of rounds 6440756/6441904/6441924. Fixture exclusion overrides remained process-local.
- E5(d) separate-account custody, point-in-time receipts and the broader interval covenant; blindness and freeze-before-fresh-pixel requirements. This review does not certify actual custody installation or actual access isolation.
- An ACTUAL FUTURE drand round: at host UTC `2026-09-06T20:54:36.821512+00:00`, prospective T_sign `2026-09-06T20:55:36Z` gives T_pulse `2026-09-06T21:06:00Z`, round 6443258. Collection returned BEACON-NOT-YET with zero fetch calls. This was a prospective probe, not a signature or adopted seed.
- ONE holdout remains the rule; `holdout_once` is PREPARED NOT ADOPTED, default False.
- E1's 17-versus-10 driver-test correction remains a FACTUAL ERRATUM.
- `verify_split` is UNADOPTED and default off; the staged stronger path exists and its SPLIT refusal codes are now classified.
- GZ1 source-table reconstruction of the guarded pool is UNVERIFIABLE HERE. Hashing the supplied pool does not establish that missing reconstruction.

**Required clauses before Duho is asked to adopt exact behavior.**

Retain the existing NSD principle and its four consequences. Repair versioned successors, preserve these failures, and replace the current overclaims with implementation-backed clauses:

“Every check is enumerated at the granularity of its actual inputs, including checks within the witness conjunction. Reading the identity, importing an optional verifier, or failing another check does not suppress independently readable open-event, repository, nonce, adoption, list or binding checks. Repository discovery and open-file reading are independent of identity parsing. Every approval-byte source used in degraded re-derivation is checked against the witness digest; committed-blob retrieval does not bypass that binding. Every unavailable check has its own blocked reason; a contribution by another check in the same stage does not satisfy that obligation.”

“Findings are contributed durably as they are derived. A later exception cannot erase prior findings or prevent independent checks from continuing. Each exception is classified at the retained, remote, local-file, verifier or receipt input boundary that caused it. Standalone and composed callers contribute the retrieval's malformed/partial findings consistently.”

“A partial snapshot supports only predicates whose truth survives any permitted completion of that snapshot. Failure to find the retained event or an own-publication event in a partial prefix does not establish absence. Same-ID contradictions remain affirmative even beside a verbatim copy; same-commit and publication predicates obey their complete-evidence negative conditions.”

“The independent-control census includes every declared prerequisite/check pair and separately justified subchecks, with no identity-file exemption. Expected complete finding sets, specific reasons, blocked checks and winner are asserted independently of the implementation's surviving output. Multi-prerequisite and input-shape variants are included. Every fail-first method is classified, including wrapped unittest names; missing-interface and text evidence are distinguished from code-behavior failures.”

“The filing gate verifies one unambiguous successful terminal suite result and successful process exit per expected suite, rejects any failure/error result or later execution failure, and checks totals. Historical failed runs remain identified as failed. Classification inventories include actual dynamically generated refusal names, and diagnostics claim history-blob equality rather than untested HEAD equality.”

Keep the full covenant, mode qualifications, ALL-events Option C consequences, first-receipt OPS trust step, and unbuilt A′/B labels. Move the new defects into UNREPAIRED CONTRADICTIONS until repaired and reviewed. Passing the existing suite is necessary evidence; it is not completion of NSD or permission to relabel these contradictions as limits.

VERDICT: NOT-SIGNABLE

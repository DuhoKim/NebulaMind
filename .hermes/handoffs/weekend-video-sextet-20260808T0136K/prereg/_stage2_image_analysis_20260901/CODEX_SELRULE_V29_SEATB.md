ACCESS_SHA=4458b821e3a1249c0646ce2790491f4d04e7224d0ef60721144354e216450599

**Independent Seat B report — complete, unadopted V29 package.** The targeted V28 counterexamples are repaired, but the universal precedence claim remains false on other complete paths. Two MAJOR unrepaired contradictions remain; no FATAL acceptance bypass was demonstrated. Passing the supplied tests does not establish the stronger contract in §3c.

Authorship/dependence: earlier Codex builder field-validation authorship is historical and no longer participates, as R:65 discloses. I did not author or alter the reviewed production modules. I reused the retained V28 referee fixture scaffolding, adapted its imports to V29, and added new combined-condition, receipt and ordering probes. Those probes depend on the lane’s identity constructor and historical BLS fixture, but execute the real production re-deriver, without substituting its callback. The exhibit-round exclusion is relaxed only inside labelled test processes. The track-8 supplemental open-event control is category 3, the coordinating Codex instance; it is neither lane evidence nor dispatched-seat evidence. This report’s executions are separate evidence.

References below: R = OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V29_20260907.md; D = _optionA_dev/fourier_chirality/run_configurations_v13.py; P = _optionA_dev/track2/provenance_designs_v9.py; BD = _optionA_dev/beacon_v2/beacon_record_drand_v29.py; Q = QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md; T2 = TRACK2_PROVENANCE_DESIGNS_UNADOPTED_20260906.md. Numbers after colons are physical source lines; R has very long paragraphs.

**[MAJOR] V29-1 — UNREPAIRED CONTRADICTION: seed re-derivation still returns a retry before approval precedence runs.** R:3,38; P:3; T2:23; Q:23 promise that locally decidable retained-event mismatches precede any evidence-unavailability return, and unresolved delivery does not bypass live authentication. D:261 now defers undetermined delivery correctly, but D:303 invokes the seed re-deriver before composed provenance at D:306. D:119–127 maps the offline verdict’s RETRY into REDERIVE-RETRY; BD:97 returns that verdict for insufficient verifying retained bodies.

I built a sealed identity with its record digest, complete hash-chain history, first-accept binding and freeze blobs consistently recomputed. It retained the real claimed seed and valid nonce evidence, but its retained seed-signature bodies were made unverifiable. The approval event simultaneously retained the genuine ID and claimed delivery through an unknown before and real later head, without a commits shortcut. Three executions returned:

| Combined condition | Complete load_identity | Authentication control |
|---|---|---|
| Unverifiable seed bodies + undetermined approval + wrong/repo | REDERIVE-RETRY; zero event retrievals | INCONSISTENT-INPUT |
| Unverifiable seed bodies + undetermined approval + genuine conflicting same-ID feed | REDERIVE-RETRY; zero event retrievals | FORGED |
| Unverifiable seed bodies + otherwise genuine approval | REDERIVE-RETRY; zero event retrievals | AUTHENTIC |

The last row isolates the earlier return. This is not a digest mismatch or an injected re-deriver. The loader never reaches the promised approval decision. The same immutable bad evidence can remain pending repeatedly without loading. That is not L-AVAIL’s qualified “genuinely unavailable identity”: the wrong repository is already decidable. The exact V28 witness-precheck defect is fixed; the claimed complete-path repair is incomplete.

**[MAJOR] V29-2 — UNREPAIRED CONTRADICTION: history remote availability and the preceding approval retrieval still bypass local open-event mismatches.** Same clauses as V29-1; D:343–357; P:237–250,331–348. The v9 wrapper calls v8, which ultimately calls v3. P:336–339 returns RETRY-REMOTE-UNAVAILABLE before inspecting the open event at P:347–348. The wrapper only intervenes when open_event_delivery is UNDETERMINED; a remote failure never sets that field.

With an otherwise valid, coherently sealed identity and a retained open event naming wrong/repo, with unknown before and real later head:

| Availability condition | Complete result |
|---|---|
| Only git ls-remote fails; ordinary freeze fetch and approval feed succeed | HISTORY-CONTINUATION: RETRY-REMOTE-UNAVAILABLE |
| Standalone validate_continuation_v9 under that same remote failure | RETRY-REMOTE-UNAVAILABLE |
| First, approval-stage Events API retrieval returns HTTP 503 | RETRY-EVENTS-UNAVAILABLE |
| Approval retrieval succeeds; a subsequent API request would return HTTP 503 | HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT; only the approval retrieval occurs |

The final control confirms the repair works once execution reaches it. The first two failures do not require knowing the remote open commit to reject wrong/repo. The third shows the cross-stage exception: the open file is not even read before the approval retry. Those exceptions are not stated among the “only” precedence rules. No identity loaded, but terminal-versus-retry behavior still contradicts the contract and must remain in the contradiction column.

**[MINOR] V29-3 — remaining names and pin text are not all true.** R:38’s current aggregate still says “driver v12”, “builder v28” and “verdict v28”; the executed current modules are v13/v29/v29. The total 136 is correct. The same paragraph contains literal backreferences in four supposed digest positions: track7/test_track7_fail_first.py `\1`, track7/test_track7_text_v27.py `\2`, track8/test_track8_fail_first.py `\1`, and track8/test_track8_text_v28.py `\2`. These are not hashes. Their actual SHA-256 values, respectively, are:

- dec20a7c678b00c61edefa033b3964238b7280f15411ec28725fa3b5a07fc7eb
- 0a3ba58d11451e42b411dd125e5bf33d18fc7a0431ca68a01a8921d0154d2caa
- 05710cb371138a34825c53aa9c80e9370be935a5a428201c4366329eaa4cc494
- 4f1dc05521aec6588a70a5df5286b479c670f6824d1c40a65ca4bdca2db1f81e

The specific V28-3 builder-fixture and verifier filename/digest associations are corrected, and the fixture opening and inspection row-1 wording are corrected. Those successes do not make the broader sweep complete.

**[MINOR] V29-4 — rule (iii) has an unstated equal-time edge.** R:3,38 and Q:23 say NOT-EARLIEST requires an EARLIER qualifying event. P:185–187 selects min(created_at), then compares canonical bytes. With two distinct IDs and equal created_at, reversing their feed order changes AUTHENTIC into NOT-EARLIEST, whose explanation falsely asserts an earlier event. This is an executed predicate stress test, not evidence that an honest protected-branch history can produce two such deliveries. It needs either a stated, justified total ordering or an explicit equal-time disposition; it does not establish a scientific bypass.

**Execution and counts.** All required 22 suites passed, 136 tests total, using PYTHONDONTWRITEBYTECODE=1, the requested interpreters, py_ecc 8.0.0, and warning settings. RULE_TEXT, DESIGN_TEXT and QUESTIONS_TEXT were separate environment entries. The counts were:

| Suite | Tests |
|---|---:|
| test_run_configurations_v13 | 23 |
| test_run_configurations | 17 |
| test_history_v2 | 4 |
| test_approval_witness_v4 | 3 |
| test_build_corpus_identity_v29 | 8 |
| test_build_corpus_identity | 4 |
| test_beacon_record_drand_v29 | 7 |
| test_verify_drand_v2 | 4 |
| test_track1_fail_first | 10 |
| test_track2_fail_first | 8 |
| test_provenance_designs | 2 |
| test_track3_fail_first | 10 |
| test_track4_fail_first | 7 |
| test_track5_fail_first | 6 |
| test_track6_fail_first | 5 |
| test_track6_text_v26 | 1 |
| test_track7_fail_first | 4 |
| test_track7_text_v27 | 1 |
| test_track8_fail_first | 7 |
| test_track8_text_v28 | 1 |
| test_track9_fail_first | 3 |
| test_track9_text_v29 | 1 |

Track 5 used V25; track-6 text V26; track-7 text V27; both track-8 suites V28; the specified version-agnostic and current tests used V29. Older label-test passes are not evidence for current wording. There was exactly the expected inherited RuntimeWarning at fourier_chirality.py:87 in the required suite run, and no ResourceWarning. I additionally ran test_fourier_chirality: 10/10 passed, outside the 136 count.

coherent_attacks_v29.py exited successfully. All 35 verdict cells equal both the filed V29 table and V28’s table after normalizing fixture commit hashes. Some historical helper rows deliberately invoke retained validator versions inside the current module; the composed rows and additional probes exercise validate_continuation_v9.

exhibit_property_v22.py ran twice, both EXHIBIT OK: True, both digest 2160fa754ce3db25613389d58bacd3098763ea8536744558e9dae96c5b4f0ae1. The additional historical drand exhibit reproduced 45d6149a2ccf30cb167dc4331455f3403a733516a82399292b1e7ad2c029e531. These are generated output digests, not hashes of the enclosing Markdown receipts. signature_preimage.py returned 4458b821e3a1249c0646ce2790491f4d04e7224d0ef60721144354e216450599 for V29 and c9e65f1bfc2bdac10716760670c85866d20c1ec0ca1d9aebdfa5b83842804fc2 for V28.

**The three states, independently exercised.** “Production path” means the actual load_identity and production seed function under explicitly labelled temporary protocols, not a claim that a study approval or production deployment exists. Actual defaults remain offline, holdout_once=False and verify_split=False.

| State | Accepts | Refuses |
|---|---|---|
| OFFLINE default behavior | Genuine evidence; coherent forged approval; rebuilt history; attack A; coherent arbitrary lists with verify_split off | Positive non-delivery, late approval, broken committed bindings, invalid chain, recorded CLOSED, seed mismatch; unknown delivery has IDENTITY-WITNESS-COMMIT-UNDETERMINED |
| Standalone v9 authentication/history helpers | Verbatim earliest genuine event; genuine ordered one-entry publications | Same-ID contradictions, local mismatches, non-earliest retained event, published rewrites, genesis-plus-accept first publication, proven batch; retry on unavailable/incomplete evidence, loss on expiry; V29-2 applies to the complete history helper |
| COMPOSED load_identity | Genuine identity with authenticated approval/open/per-entry evidence | Counter-case 1 EVENT-FORGED or EVENT-INCONSISTENT as applicable; case 2 HISTORY-CONTINUATION: HISTORY-NOT-AN-EXTENSION; A HISTORY-CONTINUATION: OPEN-NOT-GENESIS-ONLY; the intended targeted tri-state refusals below; also the incorrect early retries in V29-1/2 |

Additional independent results, beyond the inspection and supplied suite:

| Probe | Observed result |
|---|---|
| Approval: unknown before, real later head, genuine retained ID; genuine conflicting live event | EVENT-FORGED |
| Same approval + wrong/repo, healthy feed and HTTP 503 | EVENT-INCONSISTENT both times |
| Undetermined approval; feed serves retained event, nothing contradicts | RETRY-EVENTS-UNAVAILABLE |
| Undetermined approval offline | IDENTITY-WITNESS-COMMIT-UNDETERMINED |
| Positive approval non-delivery, composed | EVENT-INCONSISTENT: IDENTITY-WITNESS-COMMIT |
| Open event: unknown before, later head, genuine ID; genuine conflicting live event | HISTORY-CONTINUATION: OPEN-EVENT-FORGED |
| Same open payload + wrong/repo, stage reached | HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT |
| Undetermined open; retained-only noncontradictory feed | RETRY-HISTORY-CONTINUATION: EVIDENCE-UNAVAILABLE |
| Positive open non-delivery | HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT |
| Changed before only; changed head only | FORGED in each standalone case |
| Same-ID conflict beside a verbatim copy | FORGED |
| Missing descendant, retained event served verbatim | UNAVAILABLE |
| Missing descendant plus conflicting same-ID event | FORGED |
| git cannot launch | delivery = UNDETERMINED |
| Plain absence from a covering feed | INCOMPLETE |
| Earlier distinct qualifying event beside retained event | NOT-EARLIEST |
| Later distinct qualifying event beside earliest retained event | AUTHENTIC |
| Retained absent, distinct same-commit delivering event | FORGED under the stated absent-only predicate |
| Later unrelated actual advancing push; retained approval older than feed | EXPIRED |
| Actual push of approval commit to another ref | EXPIRED when approval absent; AUTHENTIC with genuine retained approval present |

The last actual git controls matter: an ordinary forward push does not newly deliver a commit already in its before-history, and another ref is excluded. No honest false-FORGED case was demonstrated under the intact no-force/no-deletion protected-ref assumption. Synthetic re-delivery events test the predicate; they do not prove that such a history can honestly occur. Keeping the verbatim genuine earliest event beside a later push does not let an author fabricate an earlier approval or change the seed.

Every FORGED return inspected requires a live canonical difference attached to a same ID or qualifying same-commit delivery; absence alone does not reach it. GitHub documents event IDs as unique. Conflicting same-ID copies therefore warrant refusing inconsistent evidence, without proving which producer supplied it or that two distinct honest events share an ID. [GitHub event object documentation](https://docs.github.com/en/rest/using-the-rest-api/github-event-types).

**Repair classification and evidence weight.** The register’s separation is conceptually right, but its section D assertion “none known” is superseded by V29-1/2 here.

| Claimed repair | Judgment |
|---|---|
| V28-1 / V28-2 | REPAIRED for the exact filed combined cases; NOT REPAIRED as universal complete-path claims, for the new MAJORs above |
| V28-3 | Specific cited associations/header/row corrected; ordinary earlier/later rule-(iii) behavior verified; broader text completeness and equal-time wording remain open |
| V27-1 / V27-2 | Local helper precedence, tri-state propagation and git-launch handling REPAIRED; universal composition claim remains NOT REPAIRED |
| V27-3 | Lineage REPAIRED: v6→v2, v7→v3, v8→v4, v9→v5, v10→v6, v11→v7, v12→v8, v13→v9, checked against imports; current aggregate labels still need V29-3 correction |
| V26-1 / V26-2 | REPAIRED within the subsequently qualified predicate: same-ID differences, tri-state delivery, local input outcomes and expiry loss verified |
| V26-3 | Specific verifier/name/outcome corrections REPAIRED; not evidence of a globally complete text sweep |
| P1 / P2 / P3 / P4 | Ancestry-aware batch and absence dispositions REPAIRED; targeted labels repaired; covenant carried into Q |
| N1 | COVENANT, not a technical closure of unpublished decisions |
| N2 / N3 | REPAIRED dispositions, publication preconditions and producer wiring |
| N4 | Documentary classification REPAIRED by the separate correction note |
| N5 | Targeted historical label repairs verified; current remnants listed above |
| M1 / M2 | REPAIRED publication proof, pending-commit reconciliation and producer error paths |
| M3 | Superseded by the fuller N1 COVENANT |
| M4 | DISCLOSED-AS-OPEN: A′ incomplete; C the implemented recommended option |
| M5 | Archived predecessor bytes verified; original drift remains historical, not retroactively undone |
| M6 | Targeted repairs verified; no blanket clean-text certificate |
| A | Genesis-only authenticated anchor REPAIRED; unpublished-operation completeness remains COVENANT |
| B / C / D / E / F | Producer boundary, shared delivery evidence, control-refusal logging, render-end-last, and availability/option disclosures REPAIRED within the qualifications above |

Track 9 run 1 was one behavioral complete-path failure at the FIRST subcase, one header-phrase failure after already-correct ordering behavior, and one missing-file text ERROR. It was not seven separately observed old-path failures. Run 2 establishes the repaired combined cases; run 3 the text cases; run 4 the current aggregate. The three disclosed text-side corrections do not establish additional old behavior. I independently reran the two non-text classes against retained V28 modules using in-memory import aliases: the complete case reproduced RETRY-EVENTS-UNAVAILABLE: IDENTITY-WITNESS-COMMIT-UNDETERMINED, and the rule-(iii) class failed only its missing header phrase. V29 passes both.

I read the earlier correction note as written: track 1 all behavioral; track 2 eight missing-interface errors with behavior established separately; track 3 five missing-interface/five behavioral; track 4 three missing-interface/four behavioral; track 5 three/three. An exception on an existing path is not automatically a missing interface. The malformed aggregate environment in the track-4 reconciliation is a harness failure, not a code repair. Present executions cannot prove historical timestamps or that no undisclosed intervening edit occurred.

**Limits, covenant and receipts.** Not every column-A entry is an impossibility for every implementation. L-OFF is a default-mode boundary, L-INH an explicitly staged-but-disabled implementation check, and L-AVAIL combines an external constraint with stateless enforcement. Their qualifications are necessary and now substantially honest. L-COV is an evidence limit of this design; L-RCPT is the present receipt identity limit, removable by a different identity/key design. None excuses an already-decidable mismatch receiving a retry.

The full covenant appears in P’s header, T2’s revision-3 paragraph, R:38 and Q:23: published append-only history and ordered publications are authenticated; operation times and unpublished decision completeness are not; an unpublished absence-based CLOSED can disappear before genesis publication or between publications; the fixed-round seed is unchanged; authentic late approval remains disqualifying; independent decision evidence is not implemented. I actually appended and erased an unpublished CLOSED in each interval: offline and composed both ACCEPTED the resulting coherent published identity. This agrees with the covenant.

I also fabricated the FIRST receipt under {actor: ops-witness, session: OPS}, committed and pushed it in a protected local fixture, and created no OPS-retained copy. verify_events_receipt accepted it. With approval evidence expired but open/per-entry evidence available, the configured approval-receipt composed path ACCEPTED; Option C returned EVENT-EXPIRED-NO-RECEIPT-PATH. That is exactly the disclosed trusted step, not an undisclosed closure. The label is lane-proposed, unadopted; no per-receipt Duho confirmation has been granted or is needed. This approval-only demonstration does not make A′ operational for all events.

Q1 C correctly requires ALL approval/open/per-entry events at both tune and holdout, closes the approval on evidence loss, and grants no replacement round, seed, split or attempt. A′ accurately says approval-only support exists, all-event receipt support remains unbuilt, only EXPIRED could use it, and unavailable/incomplete evidence remains retryable. B is not implemented; another token on one account is not another identity. Q2 correctly asks nothing. C remains the sound recommendation, subject to repairing the misleading precedence claims before presenting the package. Its “no residual trusted step” concerns the receipt mechanism; GitHub and the drand trust assumptions remain.

GitHub’s documented limit remains up to 300 events from the past 30 days, with 30-second to six-hour event latency; this is no guaranteed operating window. The current PushEvent example omits commits, validating the need for before/head ancestry handling. [GitHub Events API documentation](https://docs.github.com/en/rest/activity/events). The loader does not persist the study-level closure; that remains a covenant, explicitly disclosed.

**Cost, preservation and pins.** Cost is one acknowledged push per history entry, including genesis and failure entries; one collector/builder invocation can emit several entries. PENDING-PUSH requires retrying the same pending publication; HISTORY-DIVERGED refuses rewrites; unavailable remote evidence yields RETRY-REMOTE-UNAVAILABLE. Tests exercise local bare remotes with non-fast-forward receives denied and fixture-supplied gh runners, not real GitHub publishing. T2’s phrase “NOT one push per freeze” remains outside quotation as an explicit correction; no affirmative current one-push-per-freeze claim was found in R/Q/T2/P.

Individually preserved and checked: 400/200/2,000 sample sizes; 380/190/1,900 floors; strict 0.70 bar; failed-set exclusion; the 2,644-line dry-run exclusion file; rounds 6440756/6441904/6441924 excluded in production; E5(d)’s separate-account point-in-time custody evidence plus interval/other-route covenant; blindness and freeze-before-fresh-pixels rules; exactly ONE holdout as a rule, with holdout_once PREPARED NOT ADOPTED and False by default; E1’s 17-versus-10 factual erratum, with 17 executed; verify_split UNADOPTED and off. I did not certify an actual custody installation or access guarded fresh pixels. GZ1 source-table reconstruction of the guarded pool is UNVERIFIABLE HERE.

For an actual-future probe, host UTC was 2026-09-06T18:03:57Z, September 7 KST. A prospective T_sign of 18:04:57Z produced T_pulse 18:15:00Z, round 6442916. Collection returned BEACON-NOT-YET with zero fetch calls. No historical exhibit round was adopted as a study seed.

I hashed the concrete file references, including abbreviated references, and indexed the retained package. V29 contains 91 distinct full hexadecimal digest values: 88 resolve to retained file bytes, and the other three are the two reproduced exhibit-output digests and the reproduced sentinel digest. Literal backreferences are separately defective, not silently counted as pins. V23–V28 full-digest inventories contain 80/81/83/85/89/90 values respectively, with the same three generated-value exceptions; their referenced bytes are retained. V28’s known wrong builder-fixture/verifier associations cannot literally validate at the wrongly named path; the correct historical files remain present and V29 fixes the associations. This is not evidence of new pin drift.

All four archived V22 files match their full pinned digests. The supplied V22 copied-digest list carries those old values at the original paths; V24 carries them at archived paths. The V23 list carries the successor values and does NOT carry all four old values. Thus the stronger request that all three lists carry all four V22 digests is not satisfied literally. The pin-drift record’s actual reliance on the V22 list is supported; the V23 list should not be described as old-byte evidence or rewritten to pretend otherwise.

**What is still missing before Duho can adopt exact reviewed behavior.** Repair V29-1/2 in versioned successors and prove the additional combined conditions fail-first; correct the aggregate labels, literal pin placeholders and equal-time disposition. Required clause text:

“Before any retry is returned from load_identity, the implementation checks locally decidable type, repository and protected-ref mismatches in both retained approval and history-open events. This obligation applies before seed re-derivation availability returns, approval-feed availability returns, and history remote-head or fetch availability returns. Delivery checks that require unavailable remote objects remain undetermined; they do not excuse other locally decidable mismatches. In composed mode, deferred approval or open-event delivery must not bypass obtainable same-ID authentication merely because another stage has queued a retry. A retry is emitted only after the applicable higher-priority terminal checks have run. Offline undetermined delivery retains its explicitly named refusal.”

Keep the existing absent-only protected-ref contradiction clause, and add:

“NOT-EARLIEST requires a strictly earlier qualifying event under the explicitly specified ordering. Equal timestamps alone do not prove that another event is earlier; feed iteration order is not an unstated tie-break.”

Retain the full covenant, default-mode qualifications, all-events Option C consequences, receipt trust and unbuilt A′/B labels. These implementation/text corrections require no new routine Duho chores. Adoption decisions still concern exact reviewed bytes, composed behavior and its availability cost, plus the separately staged holdout/split checks; this review grants none of those decisions.

Execution artifacts and reproducible probe sources are at [the temporary audit directory](/tmp/codex_v29_audit), including suite_results.json, per-suite logs, inspection.log, probes.py, extra.py, covenant.py, new_probes.py, receipt_probe.py, failfirst.py and digest/pin inventories. New MAJOR evidence is in [new_probes.log](/tmp/codex_v29_audit/new_probes.log). Only this requested report was written by me in the reviewed directory; candidate and pinned source files were not edited.

VERDICT: NOT-SIGNABLE

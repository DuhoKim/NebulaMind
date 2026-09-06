ACCESS_SHA=d29aabac28d6d7de32e8b33b5ec4082c5c758a0ebf9913455f7b8b9cd642e1a3

Independent Seat B review of the complete, unadopted V25 package. V25 is not approved or adopted by this report. Codex previously authored the early builder field-validation code, as disclosed in E3; that implementation no longer participates. Findings below concern executed successor code, not approval of Codex's earlier work. No recurrence of the missing-production-rederiver FATAL was found.

The required 113 tests pass, the specified attack table reproduces, and the pins resolve. Nevertheless, two remaining disposition defects prevent a signable complete-package verdict: ancestry-proven batching can be called incomplete evidence, and temporarily absent approval/open events can be called forged. Neither defect demonstrated an inconsistent identity loading in composed mode. The disclosed offline boundaries and the honestly stated chronology covenant are not themselves reasons for refusal.

References below use R = OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V25_20260907.md; P = _optionA_dev/track2/provenance_designs_v5.py; D = _optionA_dev/fourier_chirality/run_configurations_v9.py; Q = QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md; T2 = TRACK2_PROVENANCE_DESIGNS_UNADOPTED_20260906.md. Numbers following these abbreviations are source line numbers.

1. Executions and scope.

I used PYTHONDONTWRITEBYTECODE=1 throughout, the requested interpreters and warning filters, and separate RULE_TEXT, DESIGN_TEXT and QUESTIONS_TEXT environment assignments. py_ecc reports 8.0.0. The current suites produced:

| Suite | Tests | Result |
|---|---:|---|
| test_run_configurations_v9 | 23 | OK |
| test_run_configurations | 17 | OK |
| test_history_v2 | 4 | OK |
| test_approval_witness_v4 | 3 | OK |
| test_build_corpus_identity_v25 | 8 | OK |
| test_build_corpus_identity | 4 | OK |
| test_beacon_record_drand_v25 | 7 | OK |
| test_verify_drand_v2 | 4 | OK |
| test_track1_fail_first | 10 | OK |
| test_track2_fail_first | 8 | OK |
| test_provenance_designs | 2 | OK |
| test_track3_fail_first | 10 | OK |
| test_track4_fail_first | 7 | OK |
| test_track5_fail_first | 6 | OK |
| Total | 113 | All invocations exit 0 |

No ResourceWarning occurred in these required runs. The combined current/legacy driver run emitted the expected inherited RuntimeWarning at fourier_chirality.py:87 for the NaN sentinel. Expected argparse refusal output was not a test failure.

exhibit_property_v22.py ran twice; both runs reported EXHIBIT OK: True and digest 2160fa754ce3db25613389d58bacd3098763ea8536744558e9dae96c5b4f0ae1. signature_preimage.py printed d29aabac28d6d7de32e8b33b5ec4082c5c758a0ebf9913455f7b8b9cd642e1a3. coherent_attacks_v25.py exited 0 and reproduced the filed outcomes, including 9m EVIDENCE-UNAVAILABLE, 9n EVIDENCE-INCOMPLETE and 9o PUBLISH-UNRELATED-COMMITS. Generated Git commit identifiers naturally differ.

Additional historical executions used a scratch copy, protecting the reviewed tree: estimator and driver v3/v4/v5 suites, 72 tests; history, witness v3 and builder v19/v20/v21/v22 suites, 40; historical beacon suites, 50; old drand verifier, 4; builder v24, 8; beacon v24, 7. All reported OK. Historical driver v3/v4 tests emitted ignored destructor ResourceWarnings despite unittest's OK; they must not be described as warning-clean. The old drand exhibit reproduced 45d6149a2ccf30cb167dc4331455f3403a733516a82399292b1e7ad2c029e531. negative_probes and observed_behaviour regenerated their pinned artifacts exactly.

Guarded-pool regeneration is UNVERIFIABLE HERE: its attempted suite stopped in setUpClass on the absent completeness receipt, before either of its two tests ran; the GZ1 source table is also unavailable. Existing pool bytes and downstream catalogue-based controls were verified, not their complete upstream derivation.

All publishing was to temporary LOCAL BARE fixture repositories with non-fast-forward receives denied. The gh runners were FIXTURE-SUPPLIED. No real repository was published, no study seed drawn, and no study pixels fetched or inspected. My independent probe script is /tmp/codex_v25_seatb_probes.py, SHA-256 6015ebef8e03b3b335e803e03f609286fcdc310c0640c8ceaed2ff61f2e3c237; its final output is /tmp/codex_v25_seatb_probes_final.out. Fixtures retained coherent identity/history digests and seals and used PRODUCTION's actual re-deriver, with fixture paths/sizes and retained-round exemptions explicitly substituted.

2. The three states, exercised.

| Case | Offline production-default mode | Standalone provenance helpers | Composed load_identity |
|---|---|---|---|
| Genuine evidence, individually published history | ACCEPTED | ACCEPTED | ACCEPTED |
| Coherently fabricated approval event, attack 1 | ACCEPTED | FORGED, or EXPIRED according to feed coverage | Refused; filed 10b is EVENT-EXPIRED-NO-RECEIPT-PATH |
| Rebuilt history after prior publication, attack 2 | ACCEPTED | HISTORY-NOT-AN-EXTENSION / HISTORY-DIVERGED | HISTORY-CONTINUATION: HISTORY-NOT-AN-EXTENSION |
| Rebuilt multi-entry history as first publication, attack A | ACCEPTED | OPEN-NOT-GENESIS-ONLY | HISTORY-CONTINUATION: OPEN-NOT-GENESIS-ONLY |
| Actual unpublished absence-based CLOSED erased after genesis publication, my probe | ACCEPTED | ACCEPTED | ACCEPTED |
| Several single-entry commits delivered in one push, explicit commit list | ACCEPTED | HISTORY-PUBLICATION-BATCH | HISTORY-CONTINUATION: HISTORY-PUBLICATION-BATCH |
| Same batch, delivery proven by before..head ancestry without commits list | ACCEPTED | EVIDENCE-INCOMPLETE | RETRY-HISTORY-CONTINUATION: EVIDENCE-INCOMPLETE |
| Reversed per-entry server times, my probe | ACCEPTED | HISTORY-PUBLICATION-ORDER | HISTORY-CONTINUATION: HISTORY-PUBLICATION-ORDER |
| Actual approval event after T_pulse, my probe | IDENTITY-WITNESS-LATE | History helper alone is not the approval-time validator | IDENTITY-WITNESS-LATE |

Standalone helpers are provenance checks, not replacements for the complete identity conjunction. D:127–138 binds the real re-deriver; D:318 invokes composed provenance only when selected. Default provenance_mode remains offline (D:107), verify_split remains False (D:113), and holdout_once remains False (D:104).

The required fixtures also reproduce APPROVAL-NOT-FIRST, IDENTITY-LOCK-MISMATCH, COLLECTION-CLOSED, COLLECTION-LOG-EMPTY, PENDING-PUSH for both uncommitted and committed unacknowledged entries, HISTORY-DIVERGED for a reset/rewrite, and RETRY-REMOTE-UNAVAILABLE. Non-fast-forward fixture pushes are rejected. Same-signature uppercase hex is accepted as the same seed. Arbitrary coherently sealed lists still load with verify_split off; its enabled recomputation refuses substituted lists.

My N1 probe actually invoked approval_witness_v4.verify with an empty events list after its latency deadline, after genesis publication. It returned APPROVAL-PUSH-EVENT-CLOSED. I appended and then erased that unpublished CLOSED entry, preserving the published genesis, and published the surviving entries individually. All three states accepted. This is precisely the disclosed covenant, not a repair and not an alternative seed.

My additional N2/N3 results:

- Complete approval/open retrievals followed by an EMPTY per-entry retrieval: helper EVIDENCE-UNAVAILABLE; production path RETRY-HISTORY-CONTINUATION: EVIDENCE-UNAVAILABLE.
- A SHORT per-entry retrieval missing a middle event without batch evidence: EVIDENCE-INCOMPLETE, prefixed RETRY-HISTORY-CONTINUATION by the driver. Restoring the delayed middle event makes the same identity ACCEPTED.
- An empty open-event retrieval: HISTORY-CONTINUATION: OPEN-EVENT-UNAVAILABLE, with retry prose but no leading RETRY prefix.
- A missing open event while older approval evidence remains: OPEN-EVENT-FORGED. A missing approval event while the feed still covers its timestamp: EVENT-FORGED. These are the second major finding below.
- An unrelated unpublished commit plus a new uncommitted entry: PUBLISH-UNRELATED-COMMITS. The variation with the pending entry already committed also refuses PUBLISH-UNRELATED-COMMITS. The remote head remains unchanged in both cases.
- A first fabricated receipt carrying the proposed OPS origin, committed once and published, passes verify_events_receipt without any independently retained OPS copy. This reproduces the disclosed external trust step.

Repeated RETRY does not load an inconsistent identity: three successive complete→complete→empty retrieval sequences all refused the batched identity. Restoring ancestry-only batch evidence still refused, incorrectly as EVIDENCE-INCOMPLETE. Code has no persisted expiry/terminal study marker or elapsed-retry limit here: repeated unavailable evidence can leave a refusal pending indefinitely, but cannot authorize tune/holdout, a replacement approval, or a new seed. The permanent-loss closure is a covenant, explicitly acknowledged at Q:27. Distinguish indefinite pending status from an acceptance bypass; I found the former, not the latter.

3. Findings.

[MAJOR] P1 — Proven batching is misclassified when payload.commits is absent. R:3,38; Q:19,22; P:94–98,158–181, especially 174–177; D:369–370.

I committed four one-entry history blobs locally and delivered them in one push. With a commits list, v5 returns HISTORY-PUBLICATION-BATCH. Removing only that list, while retaining authentic fixture before/head, the actual Git graph, and the same batch delivery, changes the result to EVIDENCE-INCOMPLETE. The open anchor still authenticates through the shared before..head delivery predicate. Thus the package simultaneously uses that graph as delivery evidence and says there is “no evidence of batching.”

P:175 searches only payload.commits for carried commits. It does not use the ancestry proof already implemented by delivers. This is not a hypothetical malformed payload: GitHub's current repository-events documentation itself shows PushEvent payloads with before/head and no commits list. The documentation also confirms the 300-event/30-day ceiling and possible 30-second–6-hour publication delay. [GitHub Events documentation](https://docs.github.com/en/rest/activity/events)

The refusal still blocks loading, so this is not FATAL or a demonstrated seed-shopping bypass. It nevertheless violates V25's explicit terminal-inconsistency contract and can keep a demonstrably batched identity in RETRY. The repair must recognize proven delivery through the supported graph predicate, while preserving RETRY when graph/evidence truly cannot establish delivery.

[MAJOR] P2 — Absence is still called forgery on approval/open retrievals. R:3,21,38; Q:19,22–23; P:99–118,216–217; D:356–370.

N2 repairs the additional per-entry retrieval, but authenticate_event still maps a retained event absent from a nonempty feed to FORGED whenever the feed reaches its timestamp. My coherent identity and individually published history pass with the complete feed. Removing the open event alone, while retaining the older approval event, produces OPEN-EVENT-FORGED. Removing approval while retaining an older unrelated event and the history events produces EVENT-FORGED. Restoring the event restores valid evidence; nothing in the Git history or retained identity was inconsistent.

A temporary omission from a retrieved feed does not prove fabrication, especially under the explicitly acknowledged latency/changing-feed model. Q promises temporary gaps as RETRY and proven inconsistencies as terminal. That distinction must cover approval and open events too, or the decision-facing contract must explicitly disclose this additional availability failure. Merely labelling the present missing-event branch FORGED is not truthful proof of forgery.

The empty-open case does say “retry” but reaches the driver without a RETRY prefix. This is a secondary diagnostic inconsistency, not evidence that the empty feed passes or is called forged. Normalize retry dispositions across all three retrieval stages.

[MINOR] P3 — N5/M6 sweep is incomplete. R:38; D:107–108,318,354; T2:22,30; coherent_attacks_v25.py:3–6.

The requested §3c title, §7 v25 commands, §9 script name and inspection table heading were corrected. Remaining current explanatory text includes “on the V22 candidate” immediately before the v9/v25 113-test sum; driver comments still identify track-2 v2 and validate_continuation_v2; the v25 inspection docstring still says driver v6 and output filed as the V22 inspection. T2 still says Options A/B are “offered with their costs” although Q properly marks A′/B unavailable pending construction/review. These stale subordinate descriptions do not change the executed v5 import, but “labels swept” is not fully true. Stronger string assertions only exclude selected old names.

T2:30 also says generically “a rejected push = DIVERGED, dead.” Its revision summary correctly narrows this to non-fast-forward rejection. A temporary receiver rejection is recoverable PENDING-PUSH, as the passing recovery test demonstrates. Use that qualified wording consistently.

[MINOR] P4 — The questions file does not carry the full N1 covenant. R:38; P:1–5; T2:5; Q:19–27.

The full covenant is accurate in code, design and §3c, including between-publication observations, erased absence-based CLOSED, unchanged seed, late approval disqualification and the unimplemented independent decision anchor. Q accurately states receipt trust and the study-closure covenant, but does not state this operation/decision-completeness covenant. Therefore the answer to “both stated exactly and completely in all four places” is no. Add the covenant or an explicit, specific incorporation of §3c to the adoption-facing text. Option C removes receipt-origin trust; it does not eliminate this chronology covenant or trust in GitHub/drand.

4. Disposition of previous claims and fail-first evidence.

| Claim | Assessment |
|---|---|
| N1 | COVENANT, not repaired. Correct and reproduced in P/T2/§3c; Q omission in P4. |
| N2 | REPAIRED for the specified empty/short per-entry fixtures; NOT REPAIRED completely for the promised disposition contract, P1/P2. |
| N3 | REPAIRED: unrelated unpublished commits refused before push, including my committed-pending variation; §7 invokes v25. |
| N4 | REPAIRED by the separate classification correction; pinned receipts preserved. |
| N5 | REPAIRED named title/command/table and historical-list omission; NOT REPAIRED as a complete sweep, P3. |
| M1 | REPAIRED separate-publication acceptance checks and explicit-list batch refusal; ancestry-only batch diagnostic incomplete, P1. |
| M2 | REPAIRED pending-commit retry, reconciliation before operations and outer-error publication; current Track 4 recovery executions pass. |
| M3 | COVENANT: original pre-genesis residual expanded to unpublished decisions between publications; no completeness mechanism built. |
| M4 | REPAIRED full event scope and honest A′/B availability labels; operational dispositions still need P1/P2. |
| M5 | REPAIRED archive preservation and supplied historical read-set evidence. |
| M6 | NOT REPAIRED completely; remaining minor text defects in P3. |
| A | REPAIRED authenticated genesis-only open anchor; late first multi-entry publication refuses. Unpublished decision completeness remains COVENANT. |
| B | REPAIRED producer boundary, one-entry commit check, recovery and unrelated-commit precondition. |
| C | REPAIRED common delivers predicate for event authentication; P1 exposes its omission from batch classification. |
| D | REPAIRED builder-control-refusal before False; builder v25:189 and executed Track 3 fixture. |
| E | REPAIRED last relevant render-end check; D:394–407 and executed fixtures. |
| F | REPAIRED empty-feed non-forgery, HTTP 404/418/429 handling and stated retention/B status; complete temporary-gap semantics remain P2. |

Track 5 run 1 is correctly classified PER TEST: N2a/b/c are three missing-interface cases; N3 and the N1/N5 text assertions are three behavioural cases. I independently reran retained v4 functions on corresponding fixtures: empty second feed and missing middle event both returned HISTORY-PUBLICATION-BATCH, and the unrelated commit was published. Thus run 1b establishes actual old behaviour rather than attributing it to AttributeErrors. Current run 2 is six OK.

The correction note properly changes Track 4 to three missing-interface plus four behavioural cases, and Track 3 to five plus five. An exception from an existing function is not automatically a missing interface. Track 2's eight initial AttributeErrors remain eight missing-interface cases with old behaviour separately demonstrated; Track 1's nine assertions and FileExistsError are behavioural. Track 3's control fixture adjustment and Track 1's approval-filename adjustment remain disclosed historical qualifications. Present executions cannot independently prove that historical run-1/run-2 test files were identical; that is a receipt claim, not something today's green run proves.

The preserved failed aggregate log hashes to 90b8abebbb9cd5a7a2c7ea2ee60d2cef9e84a4a5b32a8c138601b3d6922fbcd0. Its two Track 4 errors and the separately documented malformed environment assignment must not be relabelled an all-green aggregate. The reconciliation records the corrected separate-variable executions; my separately assigned current run passes.

5. Pins, cost and preserved substance.

V25 contains 83 distinct full digest values: 80 resolve to file contents; the other three are the two reproduced exhibit digests and the independently reproduced sentinel digest. V24's corresponding counts are 81/78 and V23's 80/77, with the same three generated-value exceptions. Named path/hash associations resolve, including abbreviated failed-selection, validation-gate and witness-v3-test pins. Every V23/V24 file pin remains present with its pinned bytes. Q hashes to e676c8655a2dee8434280f1f6fa796c997a57d8f5f3feaba5a4d3dffcfd58f40.

The four V22 archives are:

| Archive basename | V22 SHA-256 |
|---|---|
| corpus_identity_history_v2.py | ce3d8c1cee3f97341cba23b538673aff2243b6058410c6d91784ab6098bfea7d |
| track1_test_track1_fail_first.py | f2772a6cbe3081dfbd01732485feffdb6cc3a9eef9e0d024d739a7f669eef97c |
| track1_coherent_attacks.py | 1a00000e501b34c8249e88be988c8f197ea7bd05e40d2abb1f6bad2318778f0f |
| track2_test_track2_fail_first.py | fb784f792981d13cdb0a404961dcf9ffb7e353a15048a9b38dd4ef347e6df238 |

_tmp_v22_gate_COPIED_DIGESTS.txt carries all four old digests at their original paths. The V23 list carries the successor bytes, not those old archive digests; the V24 list includes all four old digests under the archive paths. All three lists are now supplied. This chronology supports the pin-drift record's V22 read-set account; it would be inaccurate to say every list independently contains every old digest.

Before report creation, all 4,569 entries of the supplied current COPIED_DIGESTS.txt matched, with zero missing files or changed digests. Reviewed files were not modified.

Cost is one acknowledged publication per HISTORY ENTRY, including genesis and failures. An invocation can create multiple entries; retry can require additional push commands. Composed loading performs approval, open and per-entry retrieval sequences with pagination, plus remote-head/fetch checks. Unacknowledged extensions are PENDING-PUSH; local divergence is HISTORY-DIVERGED; inaccessible remote evidence is RETRY-REMOTE-UNAVAILABLE in the validator, PENDING-PUSH in the producer. Recovery pushes the existing single pending commit; multiple pending entries refuse PUBLISH-BATCH.

The remaining literal “one push per freeze” outside quotation in current design prose is T2:30's explicit negation, “NOT one push per freeze.” I found no affirmative current promise of that cost. Old quoted summaries are historical, not current cost commitments.

Individually preserved and reverified:

- Sizes 400/200/2,000 and floors 380/190/1,900: retained production constants, builder controls, driver fixtures and validation-gate pin agree.
- Strict 0.70 bar, fixed denominators, objective, floor-before-strength ordering and 96-configuration enumeration: retained and exercised.
- Failed set excluded; dry-run exclusion file contains exactly 2,644 distinct identities; rounds 6440756, 6441904 and 6441924 remain production exclusions. Fixture exemptions do not authorize their use in a study.
- Custody E5(d): E5 is byte-identical to V15, including its separate-account evidence/covenant. This review does not certify an installed custody boundary.
- Blindness and label/pixel restrictions remain; no fresh study inputs were accessed.
- Actual future round: my prospective T_sign 2026-09-08T15:36:23Z maps to T_pulse 2026-09-08T15:47:00Z, round 6448380; round_time agrees and the round is not excluded. Calling the collector before that pulse returned BEACON-NOT-YET before any network callback. This is schedule verification, not an approval or draw.
- ONE holdout remains required. holdout_once is PREPARED, NOT ADOPTED, default False; enabled repeat refusal is executed by the required fixture.
- E1's 17-versus-10 annotation is a FACTUAL ERRATUM: the old driver has 17 tests, the estimator 10; both ran.
- verify_split remains UNADOPTED/default off; enabled recomputation refuses substituted lists. The default trust boundary remains disclosed.
- V15 and its RETRY record retain their stated full digests. Guarded-pool upstream derivation remains UNVERIFIABLE HERE, as above.

6. Trust, Duho's choices and what must precede presentation.

The fabricated-first-receipt residual is accurately disclosed in P:40–45, T2:3, R:38 and Q:6–16. The origin {actor: ops-witness, session: OPS} is proposed by the lane, unadopted and not a user decision. The verifier checks first-publication/immutability, matching origin metadata and event bytes; it cannot authenticate OPS as author using one shared GitHub identity. My fabricated first receipt passed. Only an independently controlled OPS copy/pane record, actually retained and compared outside the lane, detects that forgery. Delegation appropriately requires no per-receipt human confirmation.

Option C remains the sound recommendation: all required events live at tune and holdout, no receipt fallback, with actual availability rather than a guaranteed 30 days. Loss before tune blocks identity loading; loss between tune and holdout blocks holdout; no replacement commitment is licensed. It removes receipt-specific origin trust, not GitHub/drand trust or unpublished-decision incompleteness.

A′ now accurately covers the receipts it would need for ALL required events and is unavailable beyond the approval-event mechanism. B is NOT IMPLEMENTED; a second token on one account is not a second identity, and a durable signing alternative needs a key inaccessible to the lane and a pinned verification key. Neither option should be offered for adoption before construction and review. Q2 appropriately requests nothing. Q1 remains un-presented. The remaining work belongs to package preparation, not a recurring task or design exercise for Duho.

Required clause text, with successor implementation/tests reviewed before presentation:

“Batch classification shall use authenticated delivery evidence, including the supported before..head Git ancestry predicate when payload.commits is absent or incomplete. A proven multi-commit delivery is terminal HISTORY-PUBLICATION-BATCH. An unavailable retrieval or genuinely unproven delivery remains RETRY; absence alone is not proof of batching.”

“At every approval, history-open and per-entry retrieval, temporarily unavailable or incomplete evidence refuses as RETRY without changing the commitment. FORGED and other terminal inconsistency labels require affirmative contradictory evidence, not mere absence from a retrieved feed. All temporary retrieval refusals have an explicit retry disposition. Permanent evidence loss closes this approval under the rule without a new approval, round, seed, split or attempt; the current loader does not persist that study-level closure.”

“The validator authenticates published append-only history and distinct ordered publications. It does not authenticate when underlying operations occurred or the completeness of unpublished observations or decisions before genesis publication or between later publications. An unpublished absence-based CLOSED can be erased before publication; the fixed-round seed is unchanged and authentic late approval remains disqualifying. Independent decision-completeness evidence is not implemented. This covenant also applies under Option C.”

“Adoption binds the exact reviewed rule/implementation digests and protocol settings: provenance mode, repository/ref, history and retained open-event input, receipt policy, verify_split and holdout_once. Option C configures no expired receipt path. A′ and B remain unavailable until built and reviewed. Temporary push rejection is PENDING-PUSH; non-fast-forward divergence is separately refused. Cost is per published history entry, not per invocation or freeze.”

Complete the remaining name/scope sweep and carry the covenant into Q or explicitly incorporate it there. These are concrete repairs/disclosures required before Duho can adopt the claimed behaviour. This review grants no adoption, signature, publication, draw or execution authority.

VERDICT: NOT-SIGNABLE

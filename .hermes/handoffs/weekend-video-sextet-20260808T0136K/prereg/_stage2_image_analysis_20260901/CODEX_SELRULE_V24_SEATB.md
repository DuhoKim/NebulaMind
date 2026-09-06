ACCESS_SHA=f3987cbe0d31b7c5eb5a72c7018c624175d60cd8b4c3e374335cb6f19c3d2992

Independent Seat B review of the COMPLETE UNADOPTED V24 package. Reviewed across 2026-09-06/07 KST.

Authorship disclosure: the supplied records attribute earlier builder field-validation work, preparation notes and provenance probes to the Codex engine. I cannot claim independence from that engine’s historical contributions. The successor implementation is attributed to Hwao; the earlier field-validation implementation no longer participates. Historical authorship and chronology assessments depend on the supplied records. The executions and additional probes below are my own. I made no implementation repairs or adoption decisions.

The package is not yet complete and truthful enough to present for adoption of exact reviewed behavior. All 107 requested tests pass, and the specified late-batch and recovery cases are repaired. However, the residual still excludes an executable post-genesis counterexample, the questions omit V24’s additional live-event dependencies, and the producer can generate evidence its own validator rejects. No recurrence of V20’s missing-production-rederiver FATAL was found. The disclosed offline limitations are not themselves grounds for this verdict.

References use physical lines: R = OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V24_20260906.md; D = _optionA_dev/fourier_chirality/run_configurations_v8.py; P = _optionA_dev/track2/provenance_designs_v4.py; P3 = its provenance_designs_v3.py predecessor; B = _optionA_dev/corpus_identity/build_corpus_identity_v24.py; C = _optionA_dev/beacon_v2/beacon_record_drand_v24.py; AW = _optionA_dev/corpus_identity/approval_witness_v4.py; Q = QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md; T2 = TRACK2_PROVENANCE_DESIGNS_UNADOPTED_20260906.md.

1. Executed validation and the three states.

The requested warning-strict runs completed with these counts:

| Suite | Tests | Result |
|---|---:|---|
| test_run_configurations_v8 | 23 | OK |
| test_run_configurations | 17 | OK |
| test_history_v2 | 4 | OK |
| test_approval_witness_v4 | 3 | OK |
| test_build_corpus_identity_v24 | 8 | OK |
| test_build_corpus_identity | 4 | OK |
| test_beacon_record_drand_v24 | 7 | OK |
| test_verify_drand_v2 | 4 | OK |
| test_track1_fail_first | 10 | OK |
| test_track2_fail_first | 8 | OK |
| test_provenance_designs | 2 | OK |
| test_track3_fail_first | 10 | OK |
| test_track4_fail_first | 7 | OK |
| Total | 107 | OK |

I used the requested interpreters, venv site-packages, text-path environment variables and PYTHONDONTWRITEBYTECODE=1. These runs emitted no ResourceWarning and the one disclosed RuntimeWarning at fourier_chirality.py:87. py_ecc reports 8.0.0. The additional estimator suite passed 10 tests.

exhibit_property_v22.py ran twice; both runs reported EXHIBIT OK and digest 2160fa754ce3db25613389d58bacd3098763ea8536744558e9dae96c5b4f0ae1. signature_preimage.py printed the complete access digest above.

coherent_attacks_v24.py reproduced every filed outcome, apart from temporary commit identifiers. Rows 0/3a accept; 1/2/6 accept offline; 3 refuses APPROVAL-NOT-FIRST; 4 refuses IDENTITY-LOCK-MISMATCH; 5 accepts the same seed with four representation differences; 7 refuses COLLECTION-CLOSED; 8 refuses COLLECTION-LOG-EMPTY. Rows 9a–9l and 10a–10d match the filed table. Row 8 removes the acceptance: it does not establish protection against every suffix deletion. Several rows labelled “v3” actually call the script’s v4 wrapper; its table heading still says V22/driver v6/verdict v22.

| State | Executed behavior |
|---|---|
| OFFLINE, production defaults | provenance_mode='offline', holdout_once=False, verify_split=False. Genuine evidence loads using PRODUCTION’s own re-deriver. Coherent approval-event fabrication, reconstructed history, attack A and arbitrary lists remain ACCEPTED. Existing binding, seed, nonce, approval uniqueness, terminal-history and seal checks remain active. |
| STANDALONE retained v3 helpers | Genuine live approval/open evidence and published one-entry commits pass. Unpublished entries refuse PENDING-PUSH; reset/rewrite refuses HISTORY-DIVERGED or HISTORY-NOT-AN-EXTENSION; a multi-entry first blob refuses OPEN-NOT-GENESIS-ONLY; a later multi-entry commit refuses HISTORY-BATCH-COMMIT. Empty initial feed is UNAVAILABLE. A single late push delivering several separate history commits still passes. |
| COMPOSED, driver v8 with v4 | D:318,346–372 calls the real helpers inside load_identity. Genuine evidence loads; the filed event fabrication and history reconstructions refuse as reported. The single late multi-commit push and wrong-before case refuse HISTORY-CONTINUATION: HISTORY-PUBLICATION-BATCH. The additional acceptances and erroneous classifications below remain. |

The v4 standalone helper was also exercised separately so its results are not attributed to retained v3. My identities retained the identical PRODUCTION.rederive_seed function; fixture paths, sizes and pins were overridden explicitly, and historical-round exclusions were lifted only inside fixture processes. Real retained BLS seed and nonce evidence was used. The requested suites also exercise the actual CLI entry point and collector→builder→driver path at production sizes. These establish executable wiring, not an approved study run.

2. Additional probes of my own.

All repositories and changes in these probes were temporary. Remotes were LOCAL BARE repositories configured to deny non-fast-forward receives; event feeds and the gh runner were FIXTURE-SUPPLIED. Actual git commits, pushes and ls-remote acknowledgments were exercised. No public publishing occurred. “History refusal” below means composed HISTORY-CONTINUATION with the named underlying token.

| Internally consistent case | Offline | Standalone v3 | Standalone v4 / composed |
|---|---|---|---|
| Honest four entries, separately published, all corresponding events live | ACCEPTED | ACCEPTED | ACCEPTED / ACCEPTED |
| Four single-entry commits delivered by one final push | ACCEPTED | ACCEPTED | HISTORY-PUBLICATION-BATCH / history refusal |
| One later PushEvent has before unequal to the commit’s parent | ACCEPTED | ACCEPTED | HISTORY-PUBLICATION-BATCH / history refusal |
| Approval and open events remain live, but one middle history event is absent | ACCEPTED | ACCEPTED | HISTORY-PUBLICATION-BATCH / history refusal |
| Middle publication has server time later than its successor | ACCEPTED | ACCEPTED | HISTORY-PUBLICATION-ORDER / history refusal |
| All publication timestamps equal to the same second | ACCEPTED | ACCEPTED | ACCEPTED / ACCEPTED |
| Genesis published first; all remaining entries committed while remote remains at genesis; commits then pushed individually in order | ACCEPTED | ACCEPTED | ACCEPTED / ACCEPTED |
| Actual absence-based CLOSED logged before genesis publication, erased, then reconstructed genesis-first history published | ACCEPTED | ACCEPTED | ACCEPTED / ACCEPTED |
| Actual absence-based CLOSED logged AFTER genesis publication, erased before that decision’s publication, then valid entries published individually | ACCEPTED | ACCEPTED | ACCEPTED / ACCEPTED |
| Fabricated first approval-event receipt under the proposed OPS label, with all history events live | ACCEPTED | History ACCEPTED | History ACCEPTED / ACCEPTED with receipt configured |
| One unpublished unrelated commit accompanies one new history entry, published using P.publish_entry | ACCEPTED | ACCEPTED | HISTORY-PUBLICATION-BATCH / history refusal |

Equal timestamps are acceptance of nondecreasing order at the feed’s timestamp resolution, not proof of distinct operation times.

I also supplied an initially complete feed for approval and open authentication, followed by an EMPTY feed on v4’s additional retrieval. Composed mode returned HISTORY-CONTINUATION: HISTORY-PUBLICATION-BATCH. The same identity with a consistently complete feed passes. This is a changing retrieval fixture, not a fabricated commit graph.

Both CLOSED probes called AW.verify with an empty feed at T_pulse + 7 hours and actually obtained APPROVAL-PUSH-EVENT-CLOSED with state CLOSED. I appended that decision and confirmed history.first_accept reported the terminal conflict before removing the unpublished decision. The post-genesis case preserved the already-published genesis exactly; it required neither a force push nor a rewrite of any published history blob.

Additional producer/recovery executions:

- A receiver rejection left a committed entry PENDING-PUSH. After removing the temporary rejection, publish_entry pushed the SAME pending commit successfully, with no re-commit.
- reconcile_pending published one uncommitted error entry; two pending entries refused PUBLISH-BATCH without rebuilding.
- My collector crashed after publishing genesis, and its error publication was interrupted after the error had been committed. On restart, an assertion inside the actual collector call verified remote stages [genesis, collector-error] BEFORE collection began. The final remote stages were [genesis, collector-error, collector-collect]; the simulated RETRY collection returned 4.
- The supplied Track 4 crash/restart test independently passed with real retained drand fixture evidence and final remote stages [genesis, collector-error, collector-collect].

Probe scripts: /tmp/codex_v24_seatb_probes.py and /tmp/codex_v24_residual_probes.py. Their fixtures are outside the reviewed directory. Coherent history/identity digests and seals were maintained; the production re-deriver was not substituted.

3. Findings.

[MAJOR] N1 — Publication order does not prove operation order, and the residual remains too narrowly bounded. R:3,38; T2:5,7,28; P:146–162; AW:97–102.

V24 repairs the exact single-late-push case. It establishes distinct server-observed publications in nondecreasing order. It does not establish that work producing entry n+1 began only after publication of entry n. My fixture committed all later entries while the remote still held genesis, then published those commits individually; v4 and composed mode accepted.

More decisively, I obtained and erased an actual absence-based CLOSED AFTER publishing genesis. The later individually published history passed composed mode. The residual in R:38 and T2:5 names work “before the genesis was published”; it misses unpublished work and decisions after that anchor, between later publications. The producer’s cooperative ordering exists, but the validator does not authenticate completeness of those intervening observations.

The fixed-round seed remains unchanged. A genuinely late approval event remains disqualifying. The defect is an incomplete chronology/decision-completeness disclosure, not a demonstrated alternative seed. An independently retained decision anchor is still not built.

[MAJOR] N2 — V24’s live-evidence contract and the decision-facing consequences disagree. Q:19–24; P:150–160; D:353–372.

Q says “TWO events” and describes Option C in terms of both being live. V4 additionally requires the individual PushEvent for EVERY history commit at every protected load. My approval and genesis events both authenticated, yet a missing middle event refused HISTORY-PUBLICATION-BATCH. An A′ receipt covering only approval and genesis would also leave all subsequent publication checks dependent on the live feed; the proposed future receipt scope is incomplete for v4.

V4’s second history retrieval does not handle an empty list as UNAVAILABLE. It classifies every missing match as proof of a batch or absent individual acknowledgment, including the executed complete→empty retrieval case. A delayed event from an honest individual push receives the same diagnostic. Absence alone does not establish that causal account.

GitHub documents a maximum timeline of 300 events within 30 days and publication latency of 30 seconds to six hours. These are availability limits, not guarantees that every required event is immediately present. [GitHub Events documentation](https://docs.github.com/en/rest/activity/events)

The driver currently refuses loading; it does not persist a new terminal expiry marker. Q’s permanent-loss closure/no-restart consequence is a rule covenant. Temporary incomplete evidence must have an explicit retry disposition, separate from proven history inconsistency. Option C remains the sound recommendation, but its exact inputs and consequences need correction before presentation.

[MAJOR] N3 — The producer can acknowledge an entry that the validator rejects, and the operational command still selects the old recovery implementation. P:110–131,156–158; C:132–137; B:64–72; R:50.

I created one unrelated local commit after a published history head, then appended exactly one history entry and called the actual publish_entry. It successfully pushed and acknowledged the resulting HEAD. The authentic fixture event’s before was the previously published head, not the new history commit’s immediate parent. V4 rejected HISTORY-PUBLICATION-BATCH even though there was only one new history entry and its publication was acknowledged before another history operation.

This follows from the stated exact-parent predicate, but the producer does not enforce its necessary precondition: no intervening unpublished commit may accompany an entry. The package must make producer output satisfy that predicate, or explicitly implement and review a revised predicate. A silently missing working-tree/remote precondition is not a choice Duho should have to design.

Separately, §7’s executable instruction still names build_corpus_identity_v23.py and beacon_record_drand_v23.py. Those retained predecessors lack V24’s recovery repairs. Running the documented command does not select the reviewed v24 producer behavior. The V22 approval-record glob is an intentional current code convention; it is not the same issue as the stale producer module names.

[MINOR] N4 — Fail-first classification overcounts missing interfaces. TRACK4_STAGING_RECORD:5; TRACK4_FAIL_FIRST_RECEIPT run 1; P3:116; test_track4_fail_first.py:51.

The seven-test run really reports three assertion failures and four unittest errors. Those are not four missing interfaces. I reran the unchanged pending-retry test against retained P3: its existing publish_entry raised SystemExit: PUBLISH-COMMIT-FAILED. That is behavioral evidence of the old defect, not an absent API. The appropriate breakdown is three missing-interface cases and four behavioral cases, counting that exception behavior alongside the three assertion failures. Run 1b’s v3 acceptance of the late batch is independently reproduced. The recorded identical-test-file claim is a historical receipt claim; my present passing run cannot independently prove the bytes used at the earlier time.

Track 2’s eight initial AttributeErrors are correctly missing-interface evidence, with run 1b separately establishing old behavior. Track 3 reports seven errors and three failures; these must likewise not all be renamed missing interfaces. Its D case was adjusted between runs to lift the exhibit-round exclusion, as the receipt explicitly discloses. Track 1 also discloses its between-run approval-filename adjustment. These qualifications do not erase the successful repair tests.

[MINOR] N5 — Text/provenance sweep remains incomplete. R:3,38,50,65–66; D:318,346–352; inspection header; PIN_DRIFT_RECORD §2.

Beyond the operational issue above, §3c still labels itself V22 and describes v3; §9 directs coherent_attacks.py, the retained V23 script, instead of coherent_attacks_v24.py; the inspection’s table heading says V22/v6/v22; driver comments still name old helper versions. §9/§10 titles themselves were updated. Track 4’s text assertions are too weak to establish a complete sweep, and include a vacuous assertion against an empty string.

The pin-drift record cites _tmp_v22_gate_COPIED_DIGESTS.txt as the authority for its “no V22 verdict used edited bytes” conclusion. That particular list is absent here, including a hidden-file search. The supplied V22/V23 reports and matching archived bytes support its account; the present COPIED_DIGESTS.txt is the current sandbox list and cannot independently prove the earlier review’s read set. Attach the cited historical list or qualify the claimed independent verification. I found no contrary evidence that a V22 verdict actually used the edited bytes.

4. Disposition of the claimed repairs.

| Claim | Assessment |
|---|---|
| M1 | REPAIRED for separate publication evidence and rejection of the specified single late batch. Operation-order/completeness inference remains open: N1. |
| M2 | REPAIRED on the specified pending-commit, outer-error and restart paths, including my interrupted error-push variation. Producer/validator compatibility still needs N3. |
| M3 | REPAIRED wording for the original pre-genesis example; NOT REPAIRED as an exact, complete residual because the post-genesis unpublished-decision case also passes. |
| M4 | Original history-open receipt limitation is now disclosed, A′ unavailable and B unimplemented. NOT REPAIRED for the complete V24 contract: all per-entry events and incomplete-feed consequences are missing. |
| M5 | REPAIRED preservation of the four archived V22 files; every V23 file pin resolves. Historical verdict-byte verification has the documentary qualification in N5. |
| M6 | NOT REPAIRED completely; the listed corrected phrases are mostly gone, but N3/N5 remain. |
| A | REPAIRED authenticated genesis-only published anchor; original late-first-publication case refuses. Completeness outside published blobs remains open as in N1. |
| B | Producer boundary BUILT and original batch-commit test REPAIRED; recovery repaired, with N3’s producer/validator mismatch remaining. |
| C | REPAIRED: common W3 delivery predicate including before..head ancestry. V4 adds a separate, deliberately stricter publication predicate. |
| D | REPAIRED: builder-control-refusal appended before control failure returns False. Executed Track 3 test passes. |
| E | REPAIRED: render-end must be the last relevant record; subsequent refusal is rejected. |
| F | Initial empty-feed/API handling, 30-day bound and B’s unimplemented status REPAIRED. V4’s additional retrieval regresses empty-feed classification; Q is incomplete under N2. |

5. Trust, cost, pins and preserved substance.

The fabricated-first-receipt trust step is disclosed accurately: the OPS label is proposed by the lane, unadopted, and not a user decision. With one GitHub identity, the verifier cannot establish that OPS authored the first receipt. My fabricated first receipt passed with the proposed origin fields. OPS’s independently retained copy and pane record must actually exist, be independently controlled and be compared; their existence/authorship is outside this code. Delegation appropriately avoids per-receipt human confirmation.

Option B is NOT IMPLEMENTED. A second token on the same GitHub account is not a second identity; a macOS account does not establish a GitHub identity. A durable signature needs a pinned verification key and a signing key inaccessible to the lane. The current questions correctly keep B unavailable pending construction/review. Option C removes this receipt-specific trust, not trust in GitHub, its clock/feed, branch protection or the drand threshold/key.

Cost is one acknowledged publication per HISTORY ENTRY, including genesis and failure entries; one collector/builder invocation can emit several entries. Retry may incur more push commands. V4 adds live evidence for each history publication. A composed load currently performs three event retrieval sequences—approval, open, per-entry checks—plus remote-head/fetch operations; pagination can multiply calls. Budget also for Events API latency and actual evidence availability.

Uncommitted or committed-but-unacknowledged extensions are PENDING-PUSH; multiple pending entries refuse PUBLISH-BATCH; divergent bytes refuse HISTORY-DIVERGED; the validator’s unreachable remote returns RETRY-REMOTE-UNAVAILABLE, while the producer uses PENDING-PUSH for an unanswered remote. A rejected push alone is not necessarily divergence: my temporary receiver rejection recovered on retry. Non-fast-forward history rewrites are the dead/divergent case. The remaining current-design literal “one push per freeze” outside quotation is T2:28’s explicit negation, “NOT one push per freeze”; no affirmative current promise of that cost was found.

Pin audit: V24 has 81 distinct full 64-hex values: 78 match retained file contents; the other three are the two reproduced exhibit-output digests and the independently reproduced sentinel tensor digest. V23 has 80 such values: all 77 file digests resolve at their retained paths, with the same three generated-value exceptions. I checked named associations and the abbreviated failed-selection CSV, validation-gate and witness-v3-test pins too. No V23-pinned file is missing or silently replaced.

All four V22 archived predecessors match the old pins and their recorded changes:

| Archived file | Full V22 digest |
|---|---|
| corpus_identity_history_v2.py | ce3d8c1cee3f97341cba23b538673aff2243b6058410c6d91784ab6098bfea7d |
| track1_test_track1_fail_first.py | f2772a6cbe3081dfbd01732485feffdb6cc3a9eef9e0d024d739a7f669eef97c |
| track1_coherent_attacks.py | 1a00000e501b34c8249e88be988c8f197ea7bd05e40d2abb1f6bad2318778f0f |
| track2_test_track2_fail_first.py | fb784f792981d13cdb0a404961dcf9ffb7e353a15048a9b38dd4ef347e6df238 |

The corresponding current digests match V23. Diffs confirm the two added history stages, temporary argparse sidecar, version/inspection changes and Track 2 docstring correction. Thus the four-file drift inventory is truthful and complete for the identified edits. Exact V22 execution requires restoring those archived imports in a scratch checkout; merely invoking a retained old builder in the present tree is not an exact old environment.

V15 remains fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1; its RETRY record matches its pin. Rehashed V20/V21/V22/V23 rule texts match their recorded predecessor digests. Successor and predecessor implementation pins resolve.

Individually preserved/reverified:

- Sizes 400/200/2,000 and floors 380/190/1,900: production defaults and executed fixtures agree.
- Strict 0.70 bar and fixed-denominator selection/holdout rules: retained; §5 matches V15 and the validation-gate pin matches.
- Failed set excluded; dry-run exclusion file has exactly 2,644 distinct identities. All three rounds—6440756, 6441904, 6441924—are excluded in current code. Fixture exemptions are not production exemptions.
- Custody E5(d) is byte-identical to V15, including point-in-time access evidence, interval covenant, separate account and lift after freezes. This review does not certify an installed custody boundary.
- Blindness and fresh-pixel prohibitions remain, including indirect/public-service access. Tests used retained evidence and synthetic inputs, not fresh study pixels.
- Actual future schedule: my T_sign 2026-09-10T12:34:17Z maps to T_pulse 2026-09-10T12:45:00Z and drand round 6453776; round_time agrees. This was a schedule calculation, not a draw or adoption.
- ONE holdout remains the covenant. holdout_once is PREPARED, NOT ADOPTED, default False; its executable refusal fixture passes.
- E1’s 17-versus-10 correction is a FACTUAL ERRATUM. The original driver has 17 tests and the estimator has 10; both ran.
- verify_split remains UNADOPTED/default off. Its exercised recomputation refuses substituted lists; default offline acceptance is disclosed.
- Guarded-pool regeneration: UNVERIFIABLE HERE. The retained pool pin resolves, but source GZ1/completeness inputs are absent; the attempted historical pool test stopped in setUpClass on a missing completeness receipt. This is not a V24 scientific validation.

For historical count/name checks I used a separate scratch copy, protecting retained outputs. Driver v4/v5 ran 42 tests; older builder suites ran 27; historical beacon suites ran 50; history/old verifier ran 4 each. Those tests passed, apart from the unavailable guarded-pool setup just noted. The retained driver-v4 fixture emitted ignored destructor ResourceWarnings despite unittest reporting OK; that does not contradict the clean current 107-test run. Historical helper test_pki is support code, not a standalone test suite.

negative_probes regenerated its pinned receipt exactly. observed_behaviour initially differed under the venv interpreter because its child driver tests failed the interpreter lock; rerunning under /usr/bin/python3 with the venv site-packages reproduced c68d49e22427a328ce090b615c8bf715eb1e8f11b0bfdd503e18916dbbf7f858 exactly. This is an interpreter requirement, not pin drift. The historical drand-only exhibit reproduced 45d6149a2ccf30cb167dc4331455f3403a733516a82399292b1e7ad2c029e531.

6. What must be completed before Duho is asked to adopt—proposed clause text, not an adopted amendment.

“The validator authenticates the published append-only history and distinct ordered publication events. It does not authenticate when the underlying operations occurred or the completeness of unpublished observations or decisions, whether before genesis publication or between later publications. An unpublished absence-based CLOSED decision can be removed before publication. The fixed-round seed remains unchanged, and an authentic late approval event remains disqualifying. Stronger decision completeness requires independently retained decision evidence, which is not implemented.”

“Under Option C, each tune and holdout invocation requires the approval event, the history-open event and an exact qualifying publication event for every history commit from the pinned repository’s live feed. No expired-receipt fallback is enabled. Actual availability, including publication delay and the 300-event/30-day retention limits, governs execution. Temporary unavailable or incomplete evidence is RETRY without changing the commitment; proven inconsistency is separately named. Permanent loss prevents the protected invocation and closes this approval under the rule, without authorizing a new approval, round, seed, split or attempt. The present loader does not itself persist that study-level closure.”

“The producer shall enforce the prerequisites of the exact-parent publication predicate before a protected operation and shall not report publication success for a history entry whose delivered push necessarily violates that predicate. Recovery shall push the existing single pending entry before new work, refuse multiple pending entries, and preserve published history. The reviewed collector/builder commands shall invoke the v24 successors.”

“Option A′ is unavailable until receipt verification covers all otherwise-required publication evidence, including the history-open and later history events, and its trust/expiry behavior has been built and reviewed. Option B is unavailable until independent origin authentication and durable evidence have been built and reviewed. No per-receipt human confirmation is required.”

“The adoption record shall bind the exact reviewed rule and implementation digests, provenance mode, repository/ref, history-open input, receipt policy, verify_split and holdout_once settings. Defaults remain unadopted choices until explicitly bound. Historical fail-first evidence shall distinguish missing interfaces, behavioral exceptions, assertion failures and fixture prerequisites. The cited V22 sandbox digest list shall accompany claims independently verifying its review bytes.”

These require preparation, corrected successor text/code where necessary, and review before presentation. Duho’s remaining role is adopting concrete trust/availability and enforcement choices, not designing these repairs or approving an unspecified further hardening exercise. Q1 remains un-presented; Option C remains the recommendation after its contract is made accurate.

VERDICT: NOT-SIGNABLE

ACCESS_SHA=1dd822619f5831bf18d0c6e721a6d5a98b8ba171286569dad1b00a1354aa3b4c

Independent Seat B review of the COMPLETE UNADOPTED V23 package.

Authorship disclosure: the supplied records attribute earlier builder field-validation work and coordination/provenance probes to the Codex engine. I cannot claim independence from that engine’s earlier contributions. The successor implementation is attributed to Hwao. Historical authorship and chronology findings depend on those supplied records; the executions and additional probes below are my own. I made no implementation repairs or adoption decisions.

The package is not yet complete and truthful enough to put to Duho for adoption of exact reviewed behavior. The disclosed offline limitations are not themselves grounds for this refusal. The remaining problems concern publication sequencing and recovery, an overstated CLOSED-state guarantee, incomplete receipt-option consequences, and preservation/text discrepancies. No recurrence of V20’s missing-production-rederiver FATAL was found.

References give physical lines. R = OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V23_20260906.md; D = _optionA_dev/fourier_chirality/run_configurations_v7.py; P = _optionA_dev/track2/provenance_designs_v3.py; B = _optionA_dev/corpus_identity/build_corpus_identity_v23.py; BD = _optionA_dev/beacon_v2/beacon_record_drand_v23.py; AW = _optionA_dev/corpus_identity/approval_witness_v4.py; H = _optionA_dev/corpus_identity/history_v2.py; Q = QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md; T2 = TRACK2_PROVENANCE_DESIGNS_UNADOPTED_20260906.md.

1. The three states, executed.

| State | Observed acceptance and refusal |
|---|---|
| OFFLINE candidate, production defaults | provenance_mode='offline', holdout_once=False, verify_split=False. Genuine evidence loads using PRODUCTION’s actual re-deriver. Coherently forged approval event, rebuilt history, V22 attack A, and arbitrary lists remain ACCEPTED. Existing commitment, nonce, seed, lock, seal, uniqueness and terminal-history checks still refuse their corresponding defective inputs. |
| STANDALONE v3 helpers | Genuine live event and published continuation pass. Absent in-window open event: OPEN-EVENT-FORGED. Older absent open event: OPEN-EVENT-EXPIRED. Empty feed: OPEN-EVENT-UNAVAILABLE. First history blob containing multiple entries: OPEN-NOT-GENESIS-ONLY. Two entries in one later commit: HISTORY-BATCH-COMMIT. Unpublished extension: PENDING-PUSH. Reset: HISTORY-DIVERGED. Unreachable remote: RETRY-REMOTE-UNAVAILABLE. Separate single-entry commits delivered together in one late push nevertheless pass. |
| COMPOSED proposed mode | D:318 invokes the v3 helpers inside load_identity. Genuine evidence loads. In-window approval forgery refuses EVENT-FORGED; backdated forgery without a receipt refuses EVENT-EXPIRED-NO-RECEIPT-PATH. History failures are wrapped as HISTORY-CONTINUATION with the helper’s underlying token. The late multi-commit push, reconstructed genesis-only history with authentic open event, and forged-first-receipt cases below still load. |

The production re-deriver was not replaced in my identity probes: the temporary protocol retained the identical PRODUCTION function. Paths, sizes and fixture pins were explicitly overridden. Real retained BLS seed/nonce evidence was used, with historical-round exclusions lifted only inside fixture processes. The supplied end-to-end test uses builder v23 and loads its output at production sizes; the CLI test reaches load_identity under PRODUCTION. These establish executable wiring, not an actual approved production run.

coherent_attacks.py reproduced every filed V23 row, apart from temporary commit identifiers. Rows 0/3a accept; 1/2/6 accept; 3 refuses APPROVAL-NOT-FIRST; 4 refuses IDENTITY-LOCK-MISMATCH; 5 accepts the same seed with four representation differences; 7 refuses COLLECTION-CLOSED; 8 refuses COLLECTION-LOG-EMPTY; 9a–9k and 10a–10d agree with the filed outcomes. Row 4 changes the record named by a later acceptance while the earliest acceptance stays binding; it is not evidence that harmless representation changes alone are rejected. Row 8 removes the acceptance and does not establish protection against every suffix deletion.

2. Additional internally consistent probes.

All rows below used my temporary repositories with local bare remotes configured to deny non-fast-forward receives, and fixture-supplied event feeds. They exercised actual git operations and the actual load_identity path. These are decision-rule fixtures, not authenticated public GitHub deployment evidence.

“History refusal” in the composed column means HISTORY-CONTINUATION followed by the stated token.

| My constructed case | Offline | Standalone history v3 | Composed |
|---|---|---|---|
| Honest single-entry commits, each pushed, authentic open event | ACCEPTED | ACCEPTED; counts [1,1,1,1] | ACCEPTED |
| History reconstructed before first publication; first commit genesis-only; retained open event absent from an in-window fixture feed | ACCEPTED | OPEN-EVENT-FORGED | History refusal: OPEN-EVENT-FORGED |
| Same reconstruction, authentic retained open event present | ACCEPTED | ACCEPTED; counts [1,1] | ACCEPTED |
| Rebuilt genesis plus acceptance published in the first history commit | ACCEPTED | OPEN-NOT-GENESIS-ONLY | History refusal: OPEN-NOT-GENESIS-ONLY |
| Genesis published separately, then two entries together in one acknowledged commit | ACCEPTED | HISTORY-BATCH-COMMIT | History refusal: HISTORY-BATCH-COMMIT |
| Producer makes four single-entry commits without intermediate publication/acknowledgment, then pushes them together | ACCEPTED | ACCEPTED; counts [1,1,1,1] | ACCEPTED |
| First receipt fabricated under the proposed OPS label, carrying a backdated forged approval event; authentic open event remains live | ACCEPTED | History ACCEPTED; receipt path accepts the forged first receipt | ACCEPTED |
| Valid first receipt contains approval and history-open events, but both events have expired from the fixture feed | ACCEPTED | OPEN-EVENT-EXPIRED | History refusal: OPEN-EVENT-EXPIRED |
| Actual pre-publication witness CLOSED result logged, erased, then history reconstructed and published genesis-first with authentic events | ACCEPTED | ACCEPTED; counts [1,1] | ACCEPTED |

Additional producer probes:

- A local committed history extension without remote acknowledgment returned PENDING-PUSH.
- The actual publish_entry function against a receiver rejecting pushes returned PENDING-PUSH. After removing that temporary receiver rejection, calling publish_entry again on the same pending entry returned PUBLISH-COMMIT-FAILED rather than retrying its existing commit.
- A collector exception after successful genesis publication produced local stages [genesis, collector-error], while the remote contained only [genesis].
- Restarting that collector entered collect again: call count 1. It then refused PUBLISH-BATCH because two entries were unpublished, leaving [genesis, collector-error, collector-collect, collector-refusal] locally.
- A full builder-v23 build with publication configured succeeded. Remote stages were [genesis, collector-collect, builder-verdict, builder-accept], and remote HEAD equaled local HEAD. A subsequent pre-parse refusal was also published as builder-pre-parse-refusal. Thus the builder publisher exists and works on those paths; it is not merely described.

The independent probe scripts were placed outside the reviewed directory at /tmp/codex_v23_independent_probes.py and /tmp/codex_v23_closed_probe.py. Their mutations maintained adjacent identity/history digests and seals; acceptance did not result from bypassing the production re-deriver.

3. Findings.

[MAJOR] M1 — Per-entry commits do not prove per-entry publication acknowledgment. R:3,21,38; T2:5,24,26; P:121–155.

My producer created genesis, collector, verdict and acceptance as four separate commits while the remote remained at its pre-history head. One final push delivered them all. Its authentic fixture PushEvent delivered the genesis through before..head ancestry. Both standalone v3 and composed load_identity accepted.

P checks entry counts in committed blobs and current remote equality. It does not verify a distinct publication/acknowledgment boundary before each subsequent attempt. The “one acknowledged publication per entry” description therefore exceeds what the validator establishes. The repaired shared delivery predicate is correct; making it narrower again would not repair this sequencing gap.

The original two-entries-in-one-commit attack is repaired. The complete producer/validator claim is not. Current code can establish that all those commits are acknowledged now, not that each was acknowledged before work on the next entry began.

[MAJOR] M2 — Collector error publication and restart recovery are incomplete. R:3,33,38; BD:128–161; P:105–119; B:107–117.

Normal collector logging calls publish, but BD:151–161 appends outer collector-refusal/collector-error entries without publishing them. My exception probe left its error solely local after the genesis had already been acknowledged.

On restart, ensure_genesis checks genesis fields but not pending publication. The next collection therefore begins before the earlier error is acknowledged. Only the later publish_entry call detects the accumulated backlog and returns PUBLISH-BATCH. The exception wrapper appends another unpublished refusal.

publish_entry also always attempts a new git commit. After a rejected push has already created the pending commit, retrying the function on unchanged bytes fails PUBLISH-COMMIT-FAILED. An explicit git push of that existing commit can recover the simple pending-commit case, but that recovery is not implemented by this function or by collector restart.

These failures are fail-closed for immediate identity acceptance; I did not demonstrate a new seed selection. Nevertheless “every entry … acknowledged as it happens” and “refuse to proceed otherwise” are false on the executed failure/restart paths. This is missing preparation, not a choice Duho needs to design.

[MAJOR] M3 — The residual “cannot hide a CLOSED witness state” is false as an unqualified statement. R:38; T2:5; P:7–9,132–139; AW:97–102.

I called AW.verify with a real committed approval and an empty fixture feed at T_pulse + 7 hours. It actually returned APPROVAL-PUSH-EVENT-CLOSED with state CLOSED. I appended that result, confirmed H.first_accept reported its closure, then erased the unpublished history. Publishing a reconstructed genesis-only first commit and a matching acceptance, with the timely approval event and authentic open event subsequently present in the fixture feed, produced ACCEPTED in composed mode.

This distinguishes two causes of CLOSED. A genuinely late approval PushEvent remains late when reauthenticated and cannot be repaired by rewriting the log. A prior absence-based CLOSED decision depends on the earlier feed observation; its existence cannot be reconstructed solely from a later timely event’s server timestamp. The current guarantee conflates these causes.

The fixed-round seed remains unchanged. Pre-publication work and decisions remain unauthenticated, including the demonstrated absence-based terminal decision. The residual is therefore disclosed only partially, not exactly and completely.

[MAJOR] M4 — Q1’s receipt-option consequences omit the mandatory live history-open event. Q:9–20; T2:15,19; D:357–369; P:138–139.

The approval-event EXPIRED path can use an OPS receipt. The history-open event has no receipt path: validate_continuation_v3 requires AUTHENTIC from the live feed every time. My receipt contained both authentic historical events and satisfied the first-receipt conditions, yet composed mode refused OPEN-EVENT-EXPIRED after their expiry.

The inspection’s reading paragraph does disclose this history-open limitation. Q1 nevertheless presents Option A as the expired-receipt workflow without saying that it cannot carry a composed invocation past loss of the open event. The executable option and the decision-facing consequence must agree.

Option C remains the sound recommendation: no expired-receipt fallback, with both required events live at each protected invocation. Its deadline is actual feed availability, not a guaranteed number of days. Permanent evidence loss before tune blocks tuning; loss between tune and holdout blocks holdout; neither licenses a new approval, round, seed, split or attempt. The driver refuses loading; the study-level closure/no-restart consequence remains a rule covenant rather than a newly persisted expiry marker.

The corrected 30-day/300-event bound is accurate. GitHub also documents publication latency, so missing evidence is not a general proof of forgery outside the specified feed assumptions. [GitHub Events documentation](https://docs.github.com/en/rest/activity/events)

[MAJOR] M5 — The supplied tree does not retain every V22-pinned implementation/test predecessor. Preservation claim; V22 E3/§3c versus current H and track files.

The V15/V20/V21/V22 rule texts themselves retain their recorded hashes. However, four full file digests pinned by V22 have no matching retained file in this review tree:

| V22-pinned file | Missing V22 file digest |
|---|---|
| corpus_identity/history_v2.py | ce3d8c1cee3f97341cba23b538673aff2243b6058410c6d91784ab6098bfea7d |
| track1/test_track1_fail_first.py | f2772a6cbe3081dfbd01732485feffdb6cc3a9eef9e0d024d739a7f669eef97c |
| track1/coherent_attacks.py | 1a00000e501b34c8249e88be988c8f197ea7bd05e40d2abb1f6bad2318778f0f |
| track2/test_track2_fail_first.py | fb784f792981d13cdb0a404961dcf9ffb7e353a15048a9b38dd4ef347e6df238 |

Their current versions match V23’s pins. This is not a V23 pin mismatch, nor evidence that V22’s rule text was edited. It means the complete reviewed V22 implementation cannot be reproduced from the claimed preserved side-by-side files here. In particular, rerunning a retained V22 builder now imports the changed history_v2. Restore authenticated original copies under distinct archived paths and retain the successors separately.

[MINOR] M6 — The text sweep is incomplete. R:33,38,64–68; T2:7,14,19,26,33; D:107–108,318,352–354; coherent_attacks.py:1–5 and its printed header.

Concrete remnants:

- T2’s current table still says “about 90 days,” “NOT wired,” and that the collector/builder CLIs “would do it themselves.”
- T2 says one network read per driver run; composition retrieves the feed separately for approval and history-open authentication, with pagination plus git remote/fetch operations.
- R §3c names and pins builder v22 while attributing builder-control-refusal behavior introduced in v23 to it. Its closed-stage enumeration also omits newly admitted stages.
- R §3b(4) still cites old verify_drand.py/test_verify_drand.py as current verification evidence despite marking the old verifier historical earlier in that same long paragraph.
- §9/§10 and the executed inspection table still carry V22 review/version labels. The script actually imports v7/v23/v3.
- D:352 still says the expected origin is “UNNAMED until Duho answers Q1,” contrary to the claimed completed wording sweep and the lane-proposed label.
- Track 3’s docstring says missing-interface cases are marked in their names, but those names do not carry that marker. The receipt itself classifies them correctly.

The V22 approval-record filename is not itself stale: both builder and driver deliberately search APPROVAL_RECORD_SELRULE_V22*. §7’s filename matches that implementation. Do not “fix” it independently of the pinned glob.

4. A–F disposition and fail-first evidence.

| V22 finding | V23 disposition |
|---|---|
| A: unauthenticated/non-genesis-only open anchor | REPAIRED for the original attack and absent-event checks: P:130–139. DISCLOSED-AS-OPEN for pre-publication reconstruction. NOT REPAIRED as a complete residual guarantee: M3; sequencing also remains limited by M1. |
| B: producer boundary | NOT REPAIRED completely. publish_entry and producer calls are built; normal-path publication and batch-commit refusal work. M1/M2 show the remaining gaps. |
| C: delivery predicate | REPAIRED. P.delivers delegates to AW.delivers, including before..head ancestry with the repository root. Track 3’s ancestry case passes. |
| D: control failure logging | REPAIRED in builder v23, B:178–181. Track 3’s actual control mismatch returns False after builder-control-refusal. The current §3c attribution to v22 is wrong. |
| E: render-end position | REPAIRED. D:387–406 requires the final relevant record to be render-end; the formerly accepted ordering refuses RENDER-JOURNAL-NOT-ENDED. |
| F: feed semantics/questions | REPAIRED for empty feed → UNAVAILABLE, 404 → NOT-FOUND, 418 → HTTP, 429 → RATE-LIMITED, Q’s 30-day bound and explicit NOT IMPLEMENTED label for B. NOT REPAIRED completely for decision-facing consequences and package-wide prose: M4/M6. |

Track 1 records nine assertion failures and one behavioral FileExistsError, then ten passes. Track 2 run 1 records eight missing-interface AttributeErrors; run 1b separately proves the old behavior, including acceptance of an unpushed append and local reset with unchanged remote. Track 3 run 1 records seven missing-interface errors and three behavioral failures, then ten passes. None of those interface errors is evidence that the absent function executed the wrong decision.

The receipts disclose intervening fixture edits: the track-1 approval filename and track-3 D-case historical-round exclusion. Present passing executions do not independently prove the historical edit timestamps or literally identical test bytes between all runs.

Earlier C2/C5/C6/C8 and the mechanical C3/C9 checks remain repaired. C1 and C11 remain explicitly open under offline/default behavior. The complete C3/C4/C7/C12 claims must incorporate the new findings rather than being marked blanket REPAIRED.

5. Receipt trust and exactly what needs Duho.

The forged-first-receipt residual is stated accurately in Q:13 and reproduced: a matching origin label, recomputed digest and first pushed commit do not authenticate OPS. Only an independent comparison with OPS’s genuinely retained copy and pane record detects that fabrication. The code does not make or require that outside comparison. The independence and custody of that copy are trusted workflow facts, not consequences of its directory name.

The label {actor: ops-witness, session: OPS} is proposed by the lane, unadopted, and not a user decision. Choosing it does not require Duho. If a receipt path is retained, the delegated workflow correctly assigns routine receipt collection/comparison to OPS and requests no per-receipt human confirmation.

Option B is NOT IMPLEMENTED. A distinct GitHub witness identity needs credentials unavailable to the lane and an authenticated binding to the exact receipt commit; its own PushEvent also expires. A durable signature needs an independently pinned verification key and a signed binding to the receipt and approval context. A second token for the same GitHub account is not a second identity. Q:16’s example of the “existing custodian account nmcustody” must not imply that a macOS account establishes an existing GitHub identity; no such equivalence was established here. Q requires a distinct login, but the brief’s claimed explicit second-token sentence is absent.

Duho’s remaining decisions concern adopting composed provenance, its exact receipt/availability policy, and separately verify_split and holdout_once. If B is ever selected, providing an independent identity/key is a one-time human prerequisite, followed by implementation and review before use. Current missing engineering, archival restoration, labels and text corrections are preparation work, not additional questions for him.

6. Cost and failure states.

The correct granularity is one acknowledged push per history entry, including genesis and failure entries, plus the existing freeze/receipt publications. It is not necessarily one push per process invocation: my successful builder invocation published both builder-verdict and builder-accept.

Uncommitted or committed-but-unacknowledged extension: PENDING-PUSH. Local rewrite against published history: HISTORY-DIVERGED; rejected non-fast-forward delivery does not legalize the rewrite. Unreachable validation remote: RETRY-REMOTE-UNAVAILABLE. publish_entry itself reports an unavailable remote as PENDING-PUSH. Empty/API-unavailable approval feed: retry refusal. History-open unavailability is wrapped under HISTORY-CONTINUATION. Never substitute a new approval, seed, history or attempt for unavailable evidence.

The remaining literal “one push per freeze” outside quotations in the current design is T2:26’s explicit negation, “NOT one push per freeze.” No affirmative current promise of that cost was found. The substantive cost defect is incomplete enforcement/recovery, not that negation.

7. Executed checks and preserved items.

All requested commands used PYTHONDONTWRITEBYTECODE=1 and the specified interpreters/site-packages and warning filters.

| Requested suite | Executed result |
|---|---|
| test_run_configurations_v7 / test_run_configurations | 23 / 17, OK |
| test_history_v2 | 4, OK |
| test_approval_witness_v4 / test_build_corpus_identity_v22 / test_build_corpus_identity | 3 / 8 / 4, OK |
| test_beacon_record_drand_v23 | 7, OK |
| test_verify_drand_v2 | 4, OK |
| test_track1_fail_first with absolute RULE_TEXT | 10, OK |
| test_track2_fail_first / test_provenance_designs | 8 / 2, OK |
| test_track3_fail_first with absolute QUESTIONS_TEXT | 10, OK |

Total requested: 100, all passing. Additional test_fourier_chirality: 10, OK; historical test_beacon_v2: 19, OK. Total executed unit tests: 129. The Fourier suites ran together as 50 tests. One inherited RuntimeWarning appeared at fourier_chirality.py:87; no ResourceWarning or skip was reported.

The 100 count is true. It is not 100 tests exclusively against v23: the requested builder suite imports v22, track 1 imports v22/v6, and track 2 exercises earlier helper generations. Track 3, driver-v7 tests and my additional builder/provenance probes cover the successors. Static enumeration also confirmed the named historical suite counts; guarded-pool reconstruction was not run because its source table is absent and its test writes into the lane.

exhibit_property_v22.py ran twice, both EXHIBIT OK: True, both digest:
2160fa754ce3db25613389d58bacd3098763ea8536744558e9dae96c5b4f0ae1

The additional drand-only exhibit passed with digest:
45d6149a2ccf30cb167dc4331455f3403a733516a82399292b1e7ad2c029e531

signature_preimage.py printed:
1dd822619f5831bf18d0c6e721a6d5a98b8ba171286569dad1b00a1354aa3b4c

I extracted all 80 distinct full 64-hex values from V23 and hashed the supplied files. All 77 file-content digest values matched retained files. The other three are the two reproduced exhibit-payload digests and the generated sentinel digest, which also matched. This covers current and historical file pins, nonce bodies, pool, exclusions, bricks/no-r inputs, environment, scripts, witnesses and retained beacon/PKI evidence. It does not repair the separately missing V22 predecessors in M5.

Preservation, individually:

- Sample sizes: 400/200/2,000, confirmed in PRODUCTION and production-size end-to-end execution.
- Floors: 380/190 in PRODUCTION and 1,900 in the unchanged validation requirement; fixed-denominator/floor tests pass.
- Bar: 0.70, unchanged; driver THRESHOLD and strict Wilson criterion agree.
- Failed set: excluded; retained selection CSV hashes to 5643555c75670a695cd9144455a956440125c1019ebd1fb028a7ee21889014c7; builder control reproduces its 2,000-object set with equal labels.
- Dry-run exclusions: 2,644 distinct entries; exclusion tests pass.
- Historical rounds: exactly 6440756, 6441904 and 6441924 excluded by name in v23. Fixture lifting does not alter those file bytes.
- Custody E5(d): E5’s entire line is byte-equal to V15. Its point-in-time access evidence and interval covenant remain distinct.
- Blindness: fresh-pixel, development-label and freeze ordering requirements preserved; E6/E7/E8 lines also equal V15. This review did not independently establish real operational custody.
- Actual future round: at review time I computed hypothetical T_sign 2026-09-08T13:45:11Z → T_pulse 2026-09-08T13:56:00Z → round 6448158, scheduled at that T_pulse and not excluded. It was genuinely future relative to this execution; no future beacon was fetched or adopted.
- ONE holdout: requirement unchanged; holdout_once remains PREPARED, NOT ADOPTED, default False. Its True-mode refusal is tested, and no second scientific attempt is authorized.
- E1: the 17-test correction is a FACTUAL ERRATUM, not a scientific choice; the extra 10 estimator tests passed.
- verify_split: PREPARED, UNADOPTED, default off; the supplied end-to-end case exercises SPLIT-NOT-REPRODUCED for a coherently changed list. No guarded-pool reconstruction from source is claimed.
- GZ1 source table/guarded-pool derivation: UNVERIFIABLE HERE. Retained-pool hash equality and control agreement are narrower evidence.
- Signed V15 remains fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1; its RETRY record remains 1c1d9d4bacc35319e91d46420b8f892e1126cc48059ec69156a0a718428aeb4b. V20/V21/V22 rule-text hashes match the earlier records. Complete implementation preservation has the M5 exceptions.

8. What is still missing before adoption questions: concrete clause substance, backed by matching staged code and probes.

[MAJOR] “Before initiating any collector or builder operation, the producer shall reconcile pending history entries with the independently queried protected remote. Each entry shall be committed and acknowledged before the next operation begins. Recovery shall retry an existing pending commit without recollecting, adding another attempt, or rebuilding history. Failure/refusal entries shall enter the same publication queue. The validator’s evidence shall distinguish separate per-entry publication boundaries from several single-entry commits first delivered together.”

[MAJOR] “The history-open check authenticates the first published genesis and subsequent published continuation. It does not prove that no earlier local work or terminal decision existed. An authentic late approval event remains disqualifying; an erased pre-publication absence-based CLOSED decision is not recoverable merely from a later timely event. Any stronger no-hidden-CLOSED guarantee requires an independently retained decision anchor and tests of that case.”

[MAJOR] “Under the recommended no-expired-path configuration, both the approval and history-open events must authenticate in the live feed at tune and holdout. Temporary unavailability requires retry without changing the commitment. Permanent loss blocks the next protected step and closes this approval without a replacement approval, round, seed, split or attempt. The current delegated receipt option substitutes only for an expired approval event and never for an expired history-open event; it does not provide general execution after the feed window. An independent-identity/signature option remains unavailable until implemented and reviewed.”

[MAJOR] “The adoption record shall bind the exact reviewed code pins and protocol configuration: provenance mode, protected repository/ref, history path and open-event input, receipt policy and expected origin if enabled, verify_split, and holdout_once. Receipt-label selection and routine independent-copy comparison are delegated; neither requests a recurring Duho confirmation.”

[MAJOR] “Every reviewed predecessor’s pinned implementation and test bytes shall remain available in the review package under distinct archived paths. Restored historical files shall be hash-verified, and successor imports shall be version-specific.”

[MINOR] “All current commands, module names, stage lists, costs, origin attributions, deadlines and review labels shall describe these exact bytes. Superseded passages shall be explicitly historical. The corrected E1 count remains an erratum; scientific sizes, floors, bar, exclusions, custody, blindness and the one-holdout covenant remain unchanged.”

These are concrete remaining preparation tasks. Final-byte approval, actual protected-branch/custody evidence and real freezes remain prospective operational prerequisites; their ordinary absence is not the reason for this verdict.

Only this report was written in the reviewed directory. Probes used external temporary fixtures; no public push, study approval, study draw, fresh-pixel fetch or render was performed. The target hash was rechecked unchanged.

VERDICT: NOT-SIGNABLE

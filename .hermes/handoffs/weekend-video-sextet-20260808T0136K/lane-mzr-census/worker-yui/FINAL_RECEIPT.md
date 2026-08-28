# Final receipt — MZR archive-census worker lane

Lane: `lane-mzr-census/worker-yui`

Authority: evidence, visual/storyboard proposal, QA, and integrator request only. Hwao remains the sole integrator and candidate/shared-tool/TTS writer.

## Scientific/status freeze

`video_reportable_now = YES_WITH_STRICT_SCOPE` for T1 metadata-enumeration facts only:

- UCD/name retrieval counts by axis;
- 178 single-table three-axis candidates;
- 21 modifier-filter drops, split 19 redshift-axis and 2 abundance-axis, leaving 157;
- frozen term-regex matches in 62 of 157 recorded descriptions, explicitly as a side diagnostic and not an eligibility filter;
- 7/7 recall and 0/3 controls, explicitly not a precision certificate;
- recorded precision-contamination examples, split into symbol/meaning collisions and target-domain mismatches;
- T2 rule contract frozen, 157-table eligibility application not completed, no eligible-table count.

Not reportable: an eligible-table count, metallicity/MZR measurement, claim that 62 is eligible, claim that the three controls certify precision, T2 rulings on the recorded examples, or total archive capability beyond the single-table intersection. Cross-table joins and crossmatches were not assessed.

## Encoded targets

- Exact public target: SHA-256 `dc2f32a24e5418cb2cf1781401e877e70682dfcf17e4514407cc6cc48d08fcc0`, 53.0 s, 1920×1080/30 fps, video-only. Verdict: `FAIL_LINEAGE_AND_PRESENTATION_GRAMMAR`.
- Latest inspected Hwao local candidate: SHA-256 `0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d`, 128.4 s, H.264 + AAC mono. Fresh pass-3 verdict: `FAIL_FOR_SCIENTIFIC_REPRESENTATION_GRAPHICS_GRAMMAR_TAXONOMY_AND_CLOSURE_BOUNDARY`. In addition to the prior defects, fresh pixels show that the opening and 157 card overstate metadata reach as tables carrying measurements, the T2 card omits its unapplied/no-count state, and the close omits reportable-now versus pending.

Neither encoded target is approved for publication or substitution.

## Worker proposal

- `STORYBOARD_CANDIDATE.json`: version `pass3-audience-copy-v1`, SHA-256 `e6639fa69a685a1f476b4528572b4d7baeaf2475e0eab5cb91c8a41f0945b843`; 10 beats, 204 words, 105 visual-floor seconds, planned 116.6 WPM. Every beat has explicit `on_screen_copy`; build and verification fields are not audience copy.
- `visual_proposal_v7.png`: SHA-256 `ed1f9c7c2aa192b423b23655388d10c941c84069a394032de868bd51fe902883`; deterministic rerender match.
- Correct topology: 178 → −21 → 157 → qualified T2 gate. The 62-of-157 term-regex result is a side inset; T2 still applies to all 157.
- Persistent scope: single-table metadata intersection; cross-table joins/crossmatches not assessed.
- Precision examples are grouped as symbol/meaning collisions versus target-domain mismatches and explicitly labeled recorded examples, not T2 rulings.
- Display citations: VizieR foundational paper, IVOA UCD1+ v1.5, and the named pre-registered census snapshot. Citation verifier: strict PASS, 100% declared provenance in `DISPLAY_CITATIONS.md`.

## Preserved review history

- visual v1: FAIL — header/notation/overflow defects.
- visual v2: FAIL — drop-label and boundary overlap.
- visual v3: FAIL after independent adversarial review — false 157→62→T2 topology, missing single-table boundary, over-absolute T2 status.
- visual v4: FAIL local frame QA — contamination labels extended below their panel.
- visual v5: local and independent comprehension/adversarial PASS, preserved as round-2 v5 receipts, then superseded by pass-2 taxonomy deepening.
- visual v6: FAIL — grouped taxonomy omitted the explicit `not T2 rulings` boundary.
- visual v7: local full-frame PASS and final independent PASS; paper-naive 8/8 at high confidence and adversarial review found no material defect.
- Round-1 paper-naive result: 8/8 PASS, preserved in `qa/PAPER_NAIVE_RESULT_V1.json`.
- Round-1 adversarial result: FAIL with all three material defects resolved in v5, preserved in `qa/ADVERSARIAL_RESULT_V1.json`.
- Round-3 exact-v7 final results: PASS, preserved in `qa/PAPER_NAIVE_RESULT.json` and `qa/ADVERSARIAL_RESULT.json`.
- Round-4 exact pass-3 snapshot: paper-naive PASS 8/8 at high confidence; adversarial PASS with no material defects; all 9/9 snapshot entries stable. Receipts are `qa/PAPER_NAIVE_RESULT_PASS3.json` and `qa/ADVERSARIAL_RESULT_PASS3.json`.

## Narration

`ALLOY_NARRATION_MANIFEST_PROPOSAL.json` is prepared only after the visual pass:

- Nous-managed Alloy route;
- speed 1.18 from Hwao's order;
- 204 words across 10 segments and 105 visual-floor seconds;
- `tts_invoked = false`;
- zero audio artifacts;
- listening approval remains a separate post-mux gate.

## Custody and gates

Pre-order artifacts remain untouched and hashed in `PREORDER_CUSTODY.md`. Frozen source hashes, current public target hash, latest candidate hash, pass-3 frame custody, immutable review-snapshot pins, and shared renderer hashes are pinned in `SOURCE_FREEZE.json`. `qa/final_worker_checks.json` is PASS: all required artifacts and JSON parse; all custody, 32/32 pass-3 frame, 9/9 immutable-snapshot, and 13/13 frozen-input hashes match; exact pass-3 QA passes; citation ledger is grounded; no worker media, TTS execution, or open publication gate exists.

No shared renderer, plot tool, source storyboard, candidate bundle, TTS/audio, public video, site, cockpit, DB, Git, upload, or publication state was changed. No worker MP4/audio file exists.

## Integrator request

The full sealed pass-3 record is in `LANE_RECEIPT.md`. The exact pass-3 immutable-snapshot regate is recorded as PASS. Hwao alone may decide whether to integrate `INTEGRATOR_REQUEST.md`, the `pass3-audience-copy-v1` `STORYBOARD_CANDIDATE.json`, and unchanged `visual_proposal_v7.png`. The existing encoded candidate still fails, publication remains closed, and this receipt is not execution authorization.

## Pass-4 sealed addendum

Fresh offset-frame audit of the same candidate, SHA-256 `0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d`, reconfirmed encoded FAIL and deepened three boundaries: target gas-phase concept versus pre-eligibility abundance-search reach; 62 vocabulary matches versus adjudicated evidence; and T1 three-control versus T2 twelve-decoy stage provenance. Fresh contact sheet SHA-256 is `f2f1ab19f1b38f6a5a8c813077d57a3e61e4f22290289f2a50b415c0f39d8c4c`; frame manifest SHA-256 is `cf4c9792d03dacfb6148687e7e534976e0df145559155cb606454133711bd375`, with 32/32 frame pins matching.

Current proposal: `pass4-retrieval-axis-provenance-v2`, storyboard SHA-256 `24b862c8f305551d711b8dafbf95752efc33ce80c1b9614e87a6e359ebca2584`, audience projection SHA-256 `ff3dbd44815bf3f91f34d471348adb444c241b8ded95aaa99f2b99ef1d40517e`; 10 beats, 197 words, 105 visual-floor seconds, 112.6 planned WPM. It uses search-axis wording, preserves 157→T2 with 62 as a vocabulary-only side branch, separates T1/T2 stages, and renders both precision-taxonomy headings as literal audience-copy values.

Pass-4 v1 is preserved as an exact adversarial FAIL: taxonomy headings were only JSON field names/build directions. Corrected v2 exact regate PASS: paper-naive 8/8 high confidence; adversarial no material defects; 9/9 snapshot entries, 13/13 source pins, and 2/2 encoded-artifact pins stable. V2 snapshot manifest SHA-256 is `f52786d1be564373dec20ea37153db25a27ace6dc8ce32f035f11f55867acf9c`.

`visual_proposal_v7.png` remains byte-identical at `ed1f9c7c2aa192b423b23655388d10c941c84069a394032de868bd51fe902883`. Citation footer plumbing is now ledger-driven; deterministic rerender preserved those exact pixels. No worker media or TTS was created. No shared/public/candidate/Git/DB/cockpit/upload/publication state changed.

The full sealed pass-4 record and marker `YUI_MZR_CENSUS_WEEKEND_PASS4` are in `LANE_RECEIPT.md`. Hwao alone may decide whether to integrate `INTEGRATOR_REQUEST.md`, `pass4-retrieval-axis-provenance-v2`, and unchanged v7. Proposal PASS does not clear the failed encoded candidate and is not execution authorization.

Final worker checks: PASS with 40 check groups and zero errors, including required artifacts/JSON, all historical and pass-4 custody, 32/32 fresh frame pins, 9/9 exact-v2 snapshot entries, 13/13 frozen inputs, exact independent QA, failed-v1 preservation, packet/citation/validator gates, zero worker media, `tts_invoked=false`, and publication closed.

## Pass-5 sealed addendum

Fresh `1 + 4n` audit of the unchanged candidate preserved its FAIL and corrected all three pre-eligibility axes to search scope. Static `visual_proposal_v8.png` changes only the axis-heading row from v7. Any displayed T2 design controls must include all `12 DECOYS + 3 ANCHORS` and be labeled `NOT ELIGIBILITY RESULTS`; public derived counts remain blocked pending an audience-reachable methods/count ledger.

Exact immutable snapshot `pass5-all-axis-control-provenance-v1` PASS: paper-naive 8/8 at high confidence; adversarial review found no material defects; all 14/14 manifest entries were stable at start and end. Snapshot manifest SHA-256 is `b72296079d59968a05a970ed7b03b597e7613dbd2a4008e285c1b127de54c986`. The candidate remains FAIL at `0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d`; no candidate, TTS, media, shared/public asset, Git, or publication state changed. Marker: `YUI_MZR_CENSUS_WEEKEND_PASS5`.

## Pass-6 exact FAIL addendum

The pass-6 local correction added 45 scheduled reveal states and a four-second nominal gap contract, but exact round-8 adversarial review found a semantic seven-second unchanged state spanning b07→b08: a `hold` and a following `retain` were counted as changes. The snapshot also lacked clause IDs/timestamps/mapping, so clause→visible-change causality was asserted but not encoded. Demonstrated validator counterfactuals let fabricated counts, partial axis dequalification, a standalone divider, reordered close, and a fabricated citation pass. The paper-naive reviewer understood the science 8/8, but the packet omitted all display citations and inserted non-audience build semantics, so it was not its claimed exact audience projection. Pass-6 helper replay paths were also not self-contained.

Immutable snapshot `pass6-evidence-state-causality-v1` is therefore preserved as **FAIL**, despite 16/16 manifest stability, correct scientific copy/topology, and scoped static-v8 compatibility. Manifest SHA-256: `8b5fdb14a5d83a27956ec0fce527f1ff1a0960ad5a4917fca1beb4bdb07e4d01`. Receipts: `qa/PAPER_NAIVE_RESULT_PASS6.json`, `qa/ADVERSARIAL_RESULT_PASS6.json`, and `qa/PASS6_EXACT_REGATE_RESULT.md`. The encoded candidate remains FAIL; integration, publication, TTS, and shared/public/Git gates remain closed.

## Pass-7 v1 exact FAIL addendum

Round-9 paper-naive review of immutable `pass7-state-continuity-v1` passed 8/8 with mandatory Q4/Q8 satisfied and 22/22 entries stable. The exact storyboard satisfied its declared 10 handoffs, all nine cross-beat ID links, the corrected 178→−21→157→T2 topology, the 62-of-157 side-branch boundary, stage identity, qualified close, and scientific scope/status semantics.

The full exact gate nevertheless **FAILS**. Independent global state replay found 5 s and 7 s unchanged evidence intervals that the v1 validator misclassified as motion, and temporary mutations proved false-PASS paths for removing b08's visible T1 stage identity and replacing b06 with an isolated giant-62 full-frame reset while stale handoff metadata claimed continuity. The reviewer independently reproduced 43/43 candidate-frame hashes and both contact sheets; 11/14 cuts preserve zero declared anchors. V1 is preserved and superseded by v2/v3/v4 hardening. Receipts: `qa/PAPER_NAIVE_RESULT_PASS7_V1.json` and `qa/ADVERSARIAL_RESULT_PASS7_V1.json`. Candidate remains FAIL; release, integration, publication, TTS, and shared/public/Git gates remain closed.

## Pass-7 v2 exact FAIL addendum

Round-10 paper-naive review of immutable `pass7-validator-projection-causality-v2` passed 8/8 with mandatory Q4/Q8 satisfied; 34/34 entries and 0444/0555 enforcement remained stable. The exact audience payload included 10 narration records, 58 on-screen leaves, and 10 display citations, and the candidate's 43/43 frame hashes reproduced.

The adversarial gate **FAILS** on four material classes: two b08 rows were nonsemantic duplicate/empty-shell operations, yielding two six-second unchanged-evidence intervals; b05 did not use `redshift-search`/`abundance-search` qualification at every audience occurrence; the packet receipt overstated a projection-only contract despite its necessary review questions and instructions; and 12 further mutations all false-passed, including reduced state/clause counts, a decorative reveal, hidden reset, completed-T2/62-eligible contradictions, citation swaps, mismapped clauses, physical-measurement wording, a route-only-62 contradiction, and incomplete controls. V2 is preserved and superseded by v3/v4 hardening. Receipts: `qa/PAPER_NAIVE_RESULT_PASS7_V2.json` and `qa/ADVERSARIAL_RESULT_PASS7_V2.json`. Candidate remains FAIL; integration, publication, TTS, and shared/public/Git gates remain closed.

## Pass-7 v3 exact FAIL addendum

Round-11 paper-naive review of immutable `pass7-full-contract-closure-v3` passed 8/8 at high confidence with mandatory Q4/Q8 satisfied. Start and byte-only close checks found all 36/36 manifest entries unchanged, manifest SHA-256 `0a8c390ed9ee20c389f13994bd1997d7a5d167aaf3a256a75d991a01b942748a`, files `0444`, and directories `0555`; display citations were visible in 10/10 packet beats. A corrected close-check rerun resolved one reviewer-side manually transcribed hash typo and confirmed no artifact drift.

The adversarial gate **FAILS** on three material classes. First, semantic replay removes duplicate or empty-shell rows and finds a five-second b05→b06 interval plus two six-second b08 intervals, while the validator counted any nonempty reveal/transform as meaning. Second, b01's visual action says to open on all three columns, contradicting structured states that progressively reveal the rails at 2, 4, and 6 seconds. Third, the co-located approved-contract hashes are rotatable: dangerous scope or build mutations passed after regenerating those hashes in temporary copies, proving that the external immutable manifest—not the approval file alone—is the trust anchor.

V3 is therefore preserved as an exact FAIL and is superseded by v4/v5/v6. Its b08 defects were corrected in v5; v6 then corrects the b05→b06 duplicate reveal, b01 contradiction, and approval-rotation mechanism. Receipts: `qa/PAPER_NAIVE_RESULT_PASS7_V3.json` and `qa/ADVERSARIAL_RESULT_PASS7_V3.json`. Candidate remains FAIL; integration, publication, TTS, and shared/public/Git gates remain closed.

## Pass-7 v4 exact FAIL addendum

Round-12 closed-book review of immutable `pass7-self-contained-contract-v4` passed 8/8 at high confidence with mandatory Q4/Q8 satisfied. Start and byte-only end custody checks found all 89/89 entries stable, all 8/8 frozen sources and 43/43 audited frame PNGs valid, files `0444`, and directories `0555`; display citations were present in 10/10 beats. A corrected PNG-signature command resolved one reviewer-side escaping error and confirmed no artifact defect.

The adversarial gate nevertheless **FAILS** on four material classes. V4's b08 duplicate precision panel and empty taxonomy shells create two six-second unchanged-evidence gaps despite a three-second claim. B01 and b08 visual actions contradict their timed states. Thirteen additional temporary mutations all passed after re-signing the co-located contract or source manifest, proving the standalone validator was not independently authenticated. Finally, the manifest called the external candidate read-only although its mode is owner-writable `0644`, and `INTEGRATOR_REQUEST.md` described live-lane artifacts absent from the exact packet. V5/v6 correct the semantic, action/state, and manifest-authentication mechanisms, but the custody wording and packet-inventory mismatch require a higher exact packet version. Receipts: `qa/PAPER_NAIVE_RESULT_PASS7_V4.json` and `qa/ADVERSARIAL_RESULT_PASS7_V4.json`. Candidate remains FAIL; integration, publication, TTS, and shared/public/Git gates remain closed.

## Pass-7 v5 exact FAIL addendum

Round-13 closed-book review of immutable `pass7-adversarial-semantic-closure-v5` passed 8/8 at high confidence with mandatory Q4/Q8 satisfied. Start and byte-only end checks found all 95/95 entries stable, all 8/8 frozen sources and 43/43 audited frames valid, files `0444`, and directories `0555`; display citations were visible in 10/10 beats.

The adversarial gate nevertheless **FAILS** on three material classes. B08 already reveals both taxonomy labels, so b09's later label reveals are duplicates; conservative replay finds 43/45 distinct states and two six-second unchanged-evidence intervals. Several closed-book questions disclose the very measurement, eligibility, certification, or category premises they are meant to test, contradicting the claim that scaffolding supplies no answers. Finally, nine dangerous mutations pass after rotating the co-located approval hashes, although all unrotated attacks fail; v6's external-manifest authentication closes that mechanism. V8 must reveal each of the four examples exactly once under persistent labels and remove answer premises from questions. Receipts: `qa/PAPER_NAIVE_RESULT_PASS7_V5.json` and `qa/ADVERSARIAL_RESULT_PASS7_V5.json`. Candidate remains FAIL; integration, publication, TTS, and shared/public/Git gates remain closed.

## Pass-7 v6 local pending-exact addendum

The immutable `pass7-manifest-authenticated-semantic-v6` packet applies every round-11 defect still applicable to v5 without changing the audience science or static-v8 pixels. B01's visual action now follows the exact progressive state order. B05 ends on the new 157 result, and b06_s01 then supplies the new direct 157-to-T2 extension, so local global replay has a three-second maximum semantic gap. Snapshot validation authenticates the approved contract, storyboard, and validator against `MANIFEST.json`; the externally supplied manifest SHA-256 `6515425a5ad567e487977a2b8154b740caaf58703cdda2dc701f41f640f3ca9f` is the trust anchor, not regenerable co-located hashes.

Local replay passes the validator, both preparers in write-free check mode, and a mutation suite with baseline PASS plus 27/27 expected failures, including two approval-rotation attacks. The snapshot contains 88/88 verified manifest entries, 8/8 frozen sources, 43/43 audited frames, files `0444`, directories `0555`, and no prior paper-naive result artifacts. Exact v6 paper-naive and adversarial reviews remain mandatory and pending; this local PASS does not seal pass 7. The candidate remains FAIL, T2 application is incomplete, and integration, publication, TTS, and shared/public/Git gates remain closed.

## Pass-7 v7 local pending-exact addendum

V4's late adversarial receipt exposed one defect class not fully closed by v6: exact packet custody/inventory wording. V7 leaves the v6 storyboard, audience science, build semantics, mutation enforcement, and static-v8 pixels unchanged. It records the external candidate truthfully as owner-writable mode `0644`, with filesystem-read-only enforcement false and worker-policy read-only handling; snapshot `0444`/`0555` applies only to the snapshot tree. `MANIFEST.json` is explicitly the complete packet inventory. `NUMERIC_SOURCE_AUDIT.json`, `SNAPSHOT_SCOPE.md`, and the external-candidate custody receipt are included, while historical QA and prior review-result answer artifacts are deliberately excluded.

The immutable `pass7-explicit-custody-inventory-v7` snapshot contains 92/92 verified entries, 8/8 frozen sources, and 43/43 audited frames. Validator, both preparers, manifest authentication, and baseline plus 27/27 expected-fail mutations replay PASS without writes. Exact v7 paper-naive and adversarial review remains mandatory; v5/v6 results are prior-version evidence only. Candidate, T2, integration, publication, TTS, and shared/public/Git gates remain closed.

## Pass-7 v8 local pending-exact addendum

The immutable `pass7-distinct-example-clock-v8` packet closes both v5 classes that remain applicable after v6/v7. Taxonomy labels and the not-T2 boundary persist from b08; b09 then reveals each of four recorded examples exactly once, producing 45/45 distinct states, 21/21 mapped clauses, and a three-second maximum unchanged-evidence interval. The eight closed-book questions now ask neutral prompts without measurement, eligibility, certification, or taxonomy-answer premises; the packet receipt's answer-premise guard passes with zero hits and no answer key. Audience science and static-v8 pixels remain unchanged. V6 external-manifest authentication and v7 explicit custody/inventory remain intact. All 93 manifest entries, 8/8 frozen sources, 43/43 audited frames, and `0444`/`0555` modes are stable; snapshot-local validator, both preparers, manifest authentication, and baseline plus 27/27 mutation failures pass. Exact round-16 review is mandatory before pass-7 seal. Candidate, TTS, integration, publication, and shared/public/Git gates remain closed.

## Pass-7 v6 exact-review addendum

Round-14 closed-book review of immutable `pass7-manifest-authenticated-semantic-v6` passed 8/8 with mandatory Q4/Q8 satisfied. Start and byte-only end checks found all 88/88 entries stable, all 8/8 sources and 43/43 frames valid, files `0444`, and directories `0555`.

The exact adversarial gate nevertheless **FAILS** on four material classes: cross-beat semantic replay yields only 43/45 distinct states and two six-second gaps; closed-book questions disclose answer premises; `audience_projection_sha256` omits narration; and static-v8 preserves unqualified 19/2 labels while its renderer reads an absolute external evidence path and lacks a sealed write-free replay. Receipts: `qa/PAPER_NAIVE_RESULT_PASS7_V6.json` and `qa/ADVERSARIAL_RESULT_PASS7_V6.json`. V6 is preserved as prior-version evidence and cannot clear the current gate.

## Pass-7 v11 local pending-exact addendum

V11 carries v8's distinct-example clock and neutral questions, v7's explicit custody/inventory, and v6's external-manifest authentication while closing the additional exact-v6 defects. The complete audience projection now hashes all ordered narration, on-screen leaf copy, and display citations. Static `visual_proposal_v9.png` search-qualifies every 19/2 label; three full-resolution QA passes found no clipping or overlap. Its renderer reads only the snapshot-local frozen source set and `--check` proves byte-identical output without writes. The narration preparer is aligned to visual v9.

The immutable `pass7-complete-audience-static-v11` snapshot contains 93/93 verified entries, 8/8 sources, and 43/43 frames with files `0444` and directories `0555`; validator, both preparers, renderer check, manifest authentication, and baseline plus 27/27 expected-failure mutations replay PASS. Exact independent v11 review remains mandatory. Candidate, TTS, integration, publication, and shared/public/Git gates remain closed.

## Pass-7 v7 exact-review addendum

Round-15 closed-book review of immutable `pass7-explicit-custody-inventory-v7` passed 8/8 with mandatory Q4/Q8 satisfied. All 92/92 listed entries, 8/8 frozen sources, and 43/43 audited frames remained stable with `0444`/`0555`; all frames and both contact sheets also reproduced byte-for-byte from the unchanged candidate. Candidate mode `0644` and worker-policy-only read authorization were stated correctly.

The exact adversarial gate nevertheless **FAILS** on four material classes: the duplicate b09 taxonomy re-reveals produce 43/45 distinct states and two six-second gaps; the renderer reads an absolute external source and lacks a sealed no-write replay; questions 1, 5, and 6 leak answer premises; and `NUMERIC_SOURCE_AUDIT.json` links all current visual uses to absent `visual_proposal_v7.png`. Receipts: `qa/PAPER_NAIVE_RESULT_PASS7_V7.json` and `qa/ADVERSARIAL_RESULT_PASS7_V7.json`. V7 is prior-version evidence and cannot clear the current packet.

## Pass-7 v12 local pending-exact addendum

V12 closes the remaining exact-v7 traceability defect without changing storyboard science or static pixels. Every one of the nine numeric claims now binds to packet-local frozen evidence, a current storyboard beat, and current `visual_proposal_v9.png`; no absent visual or external source dependency remains. V11's complete-audience hash, search-qualified static visual, sealed renderer replay, narration-preparer alignment, and all earlier semantic, closed-book, authentication, custody, and inventory controls remain intact.

The immutable `pass7-current-artifact-traceability-v12` snapshot contains 93/93 verified entries, 8/8 sources, and 43/43 frames with files `0444` and directories `0555`; validator, both preparers, renderer check, manifest authentication, and baseline plus 27/27 expected-failure mutations replay PASS. Exact independent v12 review remains mandatory. Candidate, TTS, integration, publication, and shared/public/Git gates remain closed.

## Pass-7 v8 exact-review addendum

Round-16 closed-book review of immutable `pass7-distinct-example-clock-v8` passed 8/8 with mandatory Q4/Q8 satisfied. All 93/93 listed entries, 8/8 frozen sources, and 43/43 audited frames remained stable with `0444`/`0555`; the candidate remained unchanged at mode `0644` and FAIL.

The exact adversarial gate nevertheless **FAILS** on four material classes: shipped tooling ignores the externally supplied manifest digest and authenticates only selected entries; the renderer and all declared verification sources are not packet-self-contained; the complete-audience and question-premise mechanical guards are under-scoped; and exact-version records retain stale visual/version/four-second claims. Receipts: `qa/PAPER_NAIVE_RESULT_PASS7_V8.json` and `qa/ADVERSARIAL_RESULT_PASS7_V8.json`. V8 is preserved as prior-version evidence and cannot clear the current packet.

## Pass-7 v13 local pending-exact addendum

V13 retains v8 audience/build semantics and static visual-v9 pixels while closing the exact-v8 defects. Sealed validation now requires `MZR_EXPECTED_MANIFEST_SHA256`, verifies all 93 listed entry hashes/sizes and exact inventory, rejects missing and wrong anchors, and rejects a fully re-signed source-rotation packet against the unchanged external anchor. Every storyboard verification source is packet-local. The exact independently reviewed neutral eight-question list is pinned by canonical SHA-256. All contract and guidance language uses the three-second ceiling, and the integrator request names current visual v9 and v13 identifiers.

The immutable `pass7-external-anchor-contract-v13` snapshot contains 93/93 verified entries, 8/8 sources, and 43/43 frames with files `0444` and directories `0555`. Validator, both preparers, renderer check, complete-manifest authentication, baseline plus 27/27 expected-failure mutations, wrong/missing-anchor probes, and fully re-signed source-rotation rejection PASS. Exact independent v13 review remains mandatory. Candidate, TTS, integration, publication, and shared/public/Git gates remain closed.

## Pass-7 v11 exact-review addendum

Round-17 closed-book review of immutable `pass7-complete-audience-static-v11` passed 8/8 with mandatory Q4/Q8 satisfied. All 93/93 listed entries, 8/8 frozen sources, and 43/43 audited frames remained stable with `0444`/`0555`; exact audience science, 45-state replay, static visual v9, citations, and renderer replay passed.

The exact adversarial gate nevertheless **FAILS** on four material classes: the validator ignored the externally supplied manifest digest and standalone co-rotatable canonical hashes masked granular mutations; narration-manifest preparation accepted absent or fake visual bytes; numeric-source mappings named absent visual v7; and the visible packet title still said v8. Receipts: `qa/PAPER_NAIVE_RESULT_PASS7_V11.json` and `qa/ADVERSARIAL_RESULT_PASS7_V11.json`. V11 is preserved as prior-version evidence and cannot clear the current packet.

## Pass-7 v14 local pending-exact addendum

V14 retains v13 complete-inventory external-anchor enforcement, packet-local verification sources, canonical-hash-pinned neutral questions, exact three-second language, v12 current numeric traceability, and unchanged static-v9 pixels. Narration-manifest preparation now requires the accepted visual to exist and match its exact QA SHA-256 before generation or `--check`; independent absent-visual and fake-byte probes both reject. The paper-naive packet title is derived from current storyboard version rather than a stale hard-coded v8 label.

The immutable `pass7-visual-auth-current-label-v14` snapshot contains 93/93 verified entries, 8/8 sources, and 43/43 frames with files `0444` and directories `0555`. Validator, both preparers, renderer check, complete-manifest authentication, baseline plus 27/27 expected-failure mutations, wrong/missing-anchor probes, and visual-substitution probes PASS. Exact independent v14 review remains mandatory. Candidate, TTS, integration, publication, and shared/public/Git gates remain closed.

## Pass-7 v12 exact-review addendum

Round-18 closed-book review of immutable `pass7-current-artifact-traceability-v12` passed 8/8 with mandatory Q4/Q8 satisfied. All 93/93 listed entries, 8/8 frozen sources, and 43/43 audited frames remained stable with `0444`/`0555`; exact science, complete audience projection, 45-state replay, static visual v9, citations, renderer replay, and no-write custody passed.

The exact adversarial gate nevertheless **FAILS** on three classes: the numeric audit retained absent `lit_metallicity.png` and an unsupported 304-point scatter claim; one current-v9 locator said “stellar-mass card” instead of the rendered `MASS SEARCH`; and official gates did not granularly reject external sources, absent beat targets, or stale visual targets after internal re-signing. Receipts: `qa/PAPER_NAIVE_RESULT_PASS7_V12.json` and `qa/ADVERSARIAL_RESULT_PASS7_V12.json`. V12 is preserved as prior-version evidence and cannot clear the current packet.

## Pass-7 v15 local pending-exact addendum

V15 removes the absent/unsupported rejected-asset block, uses the current `MASS SEARCH` locator, and pins the exact nine-row numeric-source audit SHA-256, packet-local sources, and current storyboard/visual-v9 bindings in the validator. Four dedicated mutations now reject an external source, absent beat `b030`, stale visual-v8 target, and absent literature asset plus unsupported number. The expanded suite passes one baseline plus 31/31 expected failures.

The immutable `pass7-numeric-audit-contract-v15` snapshot contains 93/93 verified entries, 8/8 sources, and 43/43 frames with files `0444` and directories `0555`; MANIFEST SHA-256 is `41a6e0f6705a1e39b94610a6003dc8b519d129fc97dae5a6fd3825c5c17d9852`. Validator, both preparers, renderer check, complete-manifest authentication, expanded mutation suite, and wrong/missing-anchor probes PASS. Exact independent v15 review remains mandatory. Candidate, TTS, integration, publication, and shared/public/Git gates remain closed.

## Pass-7 v13 exact-review addendum

Round-19 closed-book review of immutable `pass7-external-anchor-contract-v13` passed 8/8 with mandatory Q4/Q8 satisfied. All 93/93 listed entries, 8/8 frozen sources, and 43/43 audited frames remained stable with `0444`/`0555`; complete external-anchor enforcement, packet-local sources, neutral-question resistance, complete audience projection, 45-state replay, visual/frame replay, and no-write custody passed.

The exact adversarial gate nevertheless **FAILS** on four classes: stored validator and mutation receipts differed from sealed live replay; current-artifact inventories still named stale v8/v12 identifiers; candidate notes named visual v8 rather than visual v9; and superseded four-second guidance remained operative-looking in manifest-listed records. Receipts: `qa/PAPER_NAIVE_RESULT_PASS7_V13.json` and `qa/ADVERSARIAL_RESULT_PASS7_V13.json`. V13 is preserved as prior-version evidence and cannot clear the current packet.

## Pass-7 v16 local pending-exact addendum

V16 stores proposal validation as exact content-only preseal data, excluding self-referential manifest-authentication state; sealed `--check` compares all stored content exactly and emits complete external-anchor authentication at runtime. The semantic mutation harness is deterministic across live and sealed contexts, and the stored 32-case receipt now matches sealed replay byte-for-byte. Candidate notes, integrator inventory, source freeze, and packet title consistently identify storyboard v13, packet v16, and visual v9. Superseded operative-looking four-second instructions were replaced by the current three-second ceiling.

The immutable `pass7-sealed-receipt-current-identifiers-v16` snapshot contains 93/93 verified entries, 8/8 sources, and 43/43 frames with files `0444` and directories `0555`; MANIFEST SHA-256 is `089b9695b818fe07b8852c99a5978379a6459bf3ba445de89bdef879f26e1c21`. Validator content-receipt check, runtime manifest authentication, both preparers, renderer, exact 32-case mutation receipt, wrong/missing-anchor probes, and all retained v15/v14/v13 gates PASS. Exact independent v16 review remains mandatory. Candidate, TTS, integration, publication, and shared/public/Git gates remain closed.

## Pass-7 v14 exact-review addendum

Round-20 closed-book review of immutable `pass7-visual-auth-current-label-v14` passed 8/8 with mandatory Q4/Q8 satisfied. All 93/93 entries, 8/8 sources, and 43/43 frames remained stable with `0444`/`0555`. External-anchor and inventory attacks, accepted-visual authentication/substitution attacks, canonical-question pinning, complete audience projection, nine numeric bindings, 45 states, 21 clauses, three-second current timing, science/topology/search/citation/status, static pixels, and no-write custody passed.

The exact adversarial gate nevertheless **FAILS**: the integrator handoff named storyboard v8 and packet v12; current source-freeze and candidate notes named visual v8; and visual QA carried an unversioned historical PASS referring to deliberately excluded receipts while the visual-v9 exact regate remained pending. Paper-naive review additionally identified a packet-title mismatch, ambiguous bullet projection boundary, numerical premises in question scaffolding, ambiguous “62-term” wording, and a metadata-census title misframe. Receipts: `qa/PAPER_NAIVE_RESULT_PASS7_V14.json` and `qa/ADVERSARIAL_RESULT_PASS7_V14.json`.

## Pass-7 v17 local pending-exact addendum

V17 explicitly distinguishes packet `pass7-neutral-scaffolding-versioned-regate-v17` from storyboard `pass7-external-anchor-contract-v13` in the closed-book title. Scaffolding now defines field labels and bullet formatting as external while keeping every displayed audience string inside the projection. Eight neutral prompts avoid numerical or named-answer premises and are canonically pinned at `68cef47af2fa339a61680e139b2b3a395361c19c19dc14da289278205eae3f3d`. The prior visual PASS is labeled pass2 historical-only with no current-gate authority; visual-v9 exact review remains pending.

The immutable v17 snapshot contains 93/93 verified entries, 8/8 sources, and 43/43 frames with files `0444` and directories `0555`; MANIFEST SHA-256 is `609c5f25cdb8d1d8fd3bf0da2d98ff5159172da126d07770ebb47b64842837a5`. Runtime manifest authentication, exact proposal and mutation receipts, both preparers, renderer, 32-case suite, wrong/missing anchors, packet/version/question/bullet contracts, and all retained v16-v13 gates PASS. Exact independent v17 review remains mandatory. Candidate, TTS, integration, publication, and shared/public/Git gates remain closed.

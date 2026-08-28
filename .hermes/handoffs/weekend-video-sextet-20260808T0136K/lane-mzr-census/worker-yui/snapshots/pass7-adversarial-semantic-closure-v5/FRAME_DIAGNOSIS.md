# Encoded-frame diagnosis — MZR archive census

Freeze: 2026-08-08 01:55 KST. All observations below come from extracted encoded frames, not from renderer intent.

## Exact current public target

Artifact: `frontend/public/videos/mzr-archive-census.mp4`, SHA-256 `dc2f32a24e5418cb2cf1781401e877e70682dfcf17e4514407cc6cc48d08fcc0`.

Media facts: 53.0 s, 1920×1080, 30 fps, H.264, video-only. The source storyboard of record has 15 cards, two figure cards, and 103.5 nominal seconds. The target instead shows a short, silent sequence of title/prose/count cards. This is both an artifact-lineage failure and a presentation-grammar failure.

Five-second-cadence frame observations:

- ~00 s: title/question card.
- ~05–10 s: prose card, “The method is the point.” No retrieval diagram.
- ~15 s: `157` dominates. `178` and `21` survive only in a sentence; the drop split and reasons are absent.
- ~20–25 s: recall/control test is described in prose. Neither `7/7` nor `0/3` is rendered as a metric.
- ~30 s: `62` dominates with no same-frame “vocabulary presence, not eligibility” lock.
- ~35–40 s: the reach-versus-eligibility boundary is present as a paragraph, but not tied visually to the preceding funnel.
- ~45–50 s: generic closing card.

No frame shows a sample funnel, axes, explicit drop bins, recall/control matrix, or an eligibility gate. Internal filenames appear as source captions. The clip is readable at full resolution but is primarily a sequence of document holds.

## Latest Hwao-integrated local candidate (read-only QA)

Artifact: `/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4`, SHA-256 `0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d`.

Media facts: 128.4 s, 1920×1080, 30 fps, H.264 + AAC mono 24 kHz. Mean volume `-21.3 dB`, maximum `-1.6 dB` from the exact candidate. This QA does not approve the voice; listening remains a separate human gate.

Encoded visual findings:

1. At 20 s, a full metallicity-versus-redshift scatter is shown under “The spread this work is about.” The body says the census exists to measure that spread. This crosses the scientific boundary: T1 is archive infrastructure and does not measure metallicity or an MZR. The asset should be removed from this census video, not relabeled cosmetically.
2. At 45 s, `157` is large while `178` and `21` remain prose. The required `19 redshift / 2 abundance` split and modifier examples are invisible.
3. At 55 s, the only quantitative graphic compares 157 with 62. It has a real denominator but omits the 178→157 filter and labels 62 as “explicit gas-phase evidence,” which can be read as scientific eligibility. The source artifact says vocabulary presence and explicitly says it is not a ruling.
4. At 65 s, `62` again dominates without a same-frame `NOT ELIGIBILITY` label.
5. At 80 s, the instrument check is prose: “seven” and “three,” not `7/7` and `0/3`. It does not warn that these controls missed the dominant symbol-Z precision contamination.
6. Internal verification paths appear in audience-facing source captions, including `T1_FINDINGS.md`, `T1E_GASPHASE_COUNT.json`, `FREEZE_RECORD_T2.md`, and an internal corpus path. Replace them with author/year/standard or named-run/date display citations; preserve internal paths only in receipts.
7. Section-divider holds and atmospheric background consume substantial runtime while evidence remains mostly static.

## Exact correction target

A graphics-first replacement should:

- show UCD and name-channel reach by axis;
- render `178 → −21 → 157` as the labeled single-table metadata funnel, with `157` connecting directly to the qualified T2 gate;
- expose the `21` drop reasons as `19 redshift-axis emptied` and `2 abundance-axis emptied`, with recorded modifier examples;
- render `62 of 157` as a side diagnostic for frozen term-regex matches in recorded descriptions; state that it is not an eligibility filter and T2 still applies to all 157;
- qualify T2 as `contract frozen · 157-table application not completed · no eligible-table count`;
- keep `single-table metadata intersection · cross-table joins/crossmatches not assessed` persistent;
- render `7/7 recall` and `0/3 controls` as explicit checks while warning that those controls did not certify precision against the dominant contamination mode;
- separate the four recorded examples into symbol/meaning collisions and target-domain mismatches, label them as recorded characterization examples rather than T2 rulings, and do not present them as astronomical measurements by this census;
- open on single-table metadata-reachable columns rather than saying catalogues or tables carry adjudicated measurements;
- close with explicit `REPORTABLE NOW` versus `PENDING`, including application not completed, no eligible-table count, and no MZR measurement;
- omit the metallicity scatter from this census explainer;
- use scholarly/named-run display citations, never internal paths.

## Deepening pass 2 re-audit

At 02:27:59 KST the exact 01:55 candidate hash remained unchanged. A fresh 20-frame contact sheet reconfirmed every blocker above and exposed one additional semantic compression at 104–112 s: the encoded card says every example is `symbol Z, not the concept`. T1 instead records four semantically distinct quantities. Galactic Cartesian height and model-grid metal fraction are symbol/meaning collisions; stellar gravitational redshift and gravitational-redshift velocity are target-domain mismatches for galaxy-MZR work. All four remain recorded characterization examples rather than T2 rulings. The full pixel receipt is in `qa/deepening-pass2-encoded/ENCODED_FRAME_AUDIT.md`.

Verdict on exact latest candidate: `FAIL_FOR_SCIENTIFIC_REPRESENTATION_GRAPHICS_GRAMMAR_AND_CONTAMINATION_TAXONOMY`. No publication or replacement gate is open.

## Deepening pass 3 re-audit

At 02:53:55 KST the exact 01:55 candidate hash remained unchanged. A fresh 32-frame, four-second-cadence extraction reconfirmed the prior blockers and exposed four linked boundary failures. At 004–012 s the opening says catalogues `carry` gas-phase metallicity, stellar mass, and redshift together, although T1 establishes only single-table metadata reach. At 044–052 s the 157 card repeats `carry all three axes`. At 088–096 s the T2 card shows contract provenance but omits application-not-completed and no-eligible-table-count states. At 124 s the final card replaces reportable-now versus pending with the generic provenance slogan `Every number read from a recorded artifact`.

The safe pass-3 correction leaves the passing v7 static pixels unchanged and versions the storyboard with explicit `on_screen_copy` for every beat. `visual_action`, `verification_sources`, and `visual_rejections` are now non-audience fields. The exact opening uses `single-table metadata census` and `metadata-reachable columns`; the exact close enumerates `REPORTABLE NOW` versus `PENDING`. The full encoded-pixel receipt is in `qa/deepening-pass3-encoded/ENCODED_FRAME_AUDIT.md`.

Updated verdict on the unchanged encoded candidate: `FAIL_FOR_SCIENTIFIC_REPRESENTATION_GRAPHICS_GRAMMAR_TAXONOMY_AND_CLOSURE_BOUNDARY`. No candidate, TTS, integration, upload, or publication gate is open.

## Deepening pass 4 re-audit

At 03:22:11 KST the exact 01:55 candidate hash remained unchanged. Thirty-two fresh frames were extracted at a two-second offset from the pass-3 cadence. The new audit separates the **target concept** from the pre-eligibility **search-axis** result. At 006 s the opening presents `gas-phase metallicity` as something catalogues carry, but T1 establishes abundance-search/mass/redshift-search metadata reach. At 062–066 s the card upgrades a frozen description-vocabulary regex match to `explicit gas-phase evidence`, although the source calls it vocabulary presence and not an E1–E4 ruling.

The fresh sequence also exposes a workflow-stage collision. At 074–082 s, seven recall members and three controls are the completed T1 retrieval-instrument check. At 086–098 s, seven gate rounds and twelve decoys describe T2 contract design. The cards do not label T1 versus T2, and the T2 frame still omits application-not-completed and no-eligible-table-count status. These are different instruments and must never be presented as one evaluation result.

The safe pass-4 correction leaves the passing v7 overview pixels unchanged. Proposal v1 used abundance-search, stellar-mass, and redshift-search axis wording; labeled 62 as vocabulary-regex presence rather than adjudicated evidence; and added explicit workflow-stage labels. Its exact adversarial review nevertheless failed because the two T1 characterization category headings existed only as JSON field names/build directions, not flattened audience-copy values. That immutable v1 FAIL is preserved. Current `pass4-retrieval-axis-provenance-v2` makes `SYMBOL / MEANING COLLISION` and `TARGET-DOMAIN MISMATCH` explicit `on_screen_copy` label values and validates those values in the audience projection. The full encoded-pixel receipt and 32/32 frame custody are in `qa/deepening-pass4-encoded/`.

Updated verdict on the unchanged encoded candidate: `FAIL_FOR_SCIENTIFIC_REPRESENTATION_TARGET_VS_AXIS_EVIDENCE_CLASS_CONTROL_STAGE_AND_PRIOR_BOUNDARIES`. No candidate, TTS, integration, upload, or publication gate is open.

## Deepening pass 5 re-audit

At 04:13:35 KST the exact 01:55 candidate hash remained unchanged. Thirty-two fresh frames were extracted at `1 + 4n` seconds. The opening still adjudicates all three target concepts, including stellar mass, although T1 is explicitly metadata-only and makes no eligibility ruling on abundance, mass, or redshift. The frozen T2 contract confirms that mass-axis matches can be black-hole, cluster, or model quantities, just as the other axes can carry non-target meanings.

The T2 card reports seven gate rounds and twelve decoys but omits the three anchors. It does not identify those fifteen as contract-design controls rather than eligibility results. The count cards also expose internal filenames, while the close supplies only generic recorded-artifact provenance rather than an audience-reachable methods/count ledger.

The safe pass-5 correction qualifies all three axes as `ABUNDANCE SEARCH`, `MASS SEARCH`, and `REDSHIFT SEARCH`; requires complete `12 DECOYS + 3 ANCHORS · NOT ELIGIBILITY RESULTS` wording whenever T2 design counts are shown; and makes a public methods/count ledger a release precondition. Static visual v8 applies the axis-label correction and preserves v7. The full encoded receipt and 32/32 frame custody are in `qa/deepening-pass5-encoded/`.

Updated verdict on the unchanged encoded candidate: `FAIL_FOR_SCIENTIFIC_REPRESENTATION_ALL_AXIS_SEARCH_SCOPE_ASYMMETRIC_T2_CONTROL_PROVENANCE_AND_PRIOR_BOUNDARIES`. No candidate, TTS, integration, upload, or publication gate is open.

## Deepening pass 6 re-audit

At 04:36:18 KST the exact 01:55 candidate hash remained unchanged. Thirty-two fresh frames were extracted at `3 + 4n` seconds, completing the four cadence offsets. A full-stream decode passed. A new hard-cut audit using ffmpeg `select='gt(scene,0.02)',showinfo` detected 14 cuts and 15 scientific evidence-state holds. Ten holds exceed six seconds; the maximum is 16.133 seconds. These are unchanged evidence states rather than a claim of pixel identity: subtle background motion may continue while no new metric, label, topology, comparison, or status appears.

The longest content states are static paragraph or giant-number cards: method 13.767 s, T1 retrieval-instrument prose 14.600 s, T2 contract prose 13.767 s, and contamination/limitation prose 16.133 s. Four standalone 2.5-second section-divider holds displace evidence. The exact timing receipt is `qa/deepening-pass6-encoded/SCENE_HOLDS.json`; the 32/32 frame custody and pixel audit are preserved beside it.

The safe pass-6 correction leaves visual v8 pixels unchanged and adds 45 timed reveal states across the 10 storyboard beats. No substantive evidence state may remain unchanged for more than four seconds; every substantive narration clause must trigger a visible metric, label, topology, comparison, or status change; standalone section-divider holds are prohibited; and the close reveals reportable-now, then pending, then holds the combined qualified summary.

Updated verdict on the unchanged encoded candidate: `FAIL_FOR_SCIENTIFIC_REPRESENTATION_STATIC_EVIDENCE_STATE_CAUSALITY_AND_PRIOR_BOUNDARIES`. No candidate, TTS, integration, upload, or publication gate is open.

## Deepening pass 7 re-audit

At 04:54:41 KST the exact 01:55 candidate hash remained unchanged. The fresh pass-7 audit sampled 0.25 seconds before and after all 14 detected hard cuts plus the midpoint of all 15 resulting holds, yielding 43 newly pinned encoded frames. The full-stream decode again passed with an empty ffmpeg error log.

The transition surface reveals a defect not resolved by a timing budget alone. Eleven of 14 cut pairs preserve zero declared scientific anchors in OCR. Cut 7 retains only `62` while dropping its 157 parent, side-check geometry, and all-157-to-T2 path. Cut 10 resets T1 retrieval prose to T2 contract prose without persistent stage identity. Four section dividers erase the active evidence layer. Six of 15 midpoint states exceed 25 OCR tokens, so dense prose/plot states alternate with empty dividers rather than handing an evolving evidence surface forward. OCR counts are a reproducible density aid, not a semantic verdict.

The safe pass-7 correction again leaves visual v8 pixels unchanged. Each of 10 storyboard beats now declares a matched entry/exit `state_handoff`; all nine cross-beat links validate. Full-frame scientific resets are prohibited. After construction, the 178→−21→157→T2 spine persists through the qualified close; whenever 62 is visible, its 157 parent and side-check boundary remain; T1/T2 stage identity and no-count/no-measurement/single-table scope carry into the close.

Updated verdict on the unchanged encoded candidate: `FAIL_FOR_SCIENTIFIC_REPRESENTATION_STATE_CONTINUITY_AND_PRIOR_BOUNDARIES`. No candidate, TTS, integration, upload, or publication gate is open.

### Pass-7 v2 validator/projection reconciliation

Round-8 exact review preserved pass 6 as FAIL: the nominal four-second validator treated a b07 `hold` and b08 `retain` as changes, hiding a seven-second global unchanged state; no declared narration-clause mapping existed; source counts, exhaustive axis qualification, final order, and citations admitted demonstrated false-pass mutations; and the comprehension packet was not its claimed exact projection.

Pass-7 v2 repairs those proposal-layer defects without changing candidate or visual-v8 pixels. All 45 states now declare `operation=reveal|transform`, a concrete `evidence_delta`, and mapped clause IDs; 21 declared clauses are all mapped; the global semantic gap is 3.0 seconds. The validator binds rendered counts/status to frozen source values, reconciles all display citations to the ledger, checks exact closing chronology, and rejects eight expected-fail mutations. The paper-naive packet is generated deterministically from all 10 narration strings, all 58 on-screen leaf strings, and all 10 display citations. Helper `--check` modes do not write.

These are proposal/validator guarantees, not a claim that any MP4 encodes them. The unchanged candidate remains `FAIL_FOR_SCIENTIFIC_REPRESENTATION_STATE_CONTINUITY_AND_PRIOR_BOUNDARIES`; all execution and release gates remain closed.

### Pass-7 v3 full-contract closure

A fresh temporary mutation attack on frozen v2 found four additional false-pass paths: fabricated b02 narration, a false `PRECISION CERTIFIED` b08 field, a fabricated b09 example, and a static-hold `visual_action` all passed the v2 validator. V2 is preserved and cannot be sealed.

V3 changes no scientific audience copy and no visual-v8 pixels. It replaces the two ambiguous build-direction uses of `hold`, binds exact b02/b07/b08/b09/b10 audience fields to their frozen semantics, and adds `qa/APPROVED_STORYBOARD_CONTRACT.json` with canonical hashes for the complete storyboard, audience semantics, and build semantics. The mutation suite now passes baseline plus rejects 12/12 counterfactuals. Exact independent v3 review is still required; the candidate and every integration/publication gate remain unchanged and closed.

### Pass-7 v4 self-contained replay

V3 still required the original prior-pack directory at an absolute path when replaying `validate_proposal.py`. V4 copies eight exact source artifacts into `frozen_sources/pass7/`, pins them in a local manifest, and makes the validator verify and read only that bundle by default. A thirteenth expected-fail mutation proves source tampering is rejected. The exact v4 snapshot also carries all 43 audited PNG frames rather than contact sheets alone. No audience/build semantics, candidate bytes, or visual-v8 pixels changed. Exact v4 review remains mandatory; candidate, integration, TTS, and publication gates remain closed.

### Pass-7 v5 adversarial-semantic closure

Round-10 exact v2 adversarial review exposed defects that also survived into v4: b05 did not search-qualify redshift/abundance at every audience occurrence; two b08 rows were duplicate styling or empty shells rather than distinct scientific changes; the paper-packet receipt overstated a projection-only contract; and twelve new counterfactuals false-passed. V5 search-qualifies every b05 representation, replaces b08 with five distinct semantic states, declares review scaffolding outside the exact audience payload, tightens the motion ceiling to three seconds, and expands the suite to baseline PASS plus 25/25 expected failures. Static-v8 pixels and candidate bytes remain unchanged. Exact v5 review is mandatory; candidate, integration, TTS, and publication gates remain closed.

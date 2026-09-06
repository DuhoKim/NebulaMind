ACCESS_SHA=98881c7ecba0ac3bb718983f8534aaa55d325efeb4314d72b31b64b95af2abb9

V30 is NOT SIGNABLE: one FATAL regression and two MAJOR groups of unrepaired contradictions remain. The 141 passing tests do not establish the claimed complete-path precedence property. Nothing is adopted or approved by this review.

Authorship disclosure: §9 records earlier Codex builder-field-validation authorship and says that code no longer participates. I made no candidate or implementation edits. Findings below rest on execution of the current pinned modules, including PRODUCTION's actual seed re-deriver, rather than on accepting earlier Codex work as independently validated.

References: R = OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V30_20260907.md; D = _optionA_dev/fourier_chirality/run_configurations_v14.py; P = _optionA_dev/track2/provenance_designs_v10.py; Q = QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md; T2 = TRACK2_PROVENANCE_DESIGNS_UNADOPTED_20260906.md. Numbers following D/P are code lines. R's principal precedence promise is at line 3 and §3c, line 38.

**V30-1 [FATAL] — JSON null disables the composed history boundary. UNREPAIRED CONTRADICTION with §3c, Q1 C's ALL-events requirement, and the claimed repair of A/B.** D:361 successfully parses a history-open file containing `null` as Python None. It records no missing-file finding because parsing succeeded. D:363 skips local validation; D:383 skips same-ID authentication; D:392 skips history continuation. With no other findings, D:397 records composed success with no history result or remote head, and load_identity ACCEPTS.

I executed a coherently sealed identity in a local protected bare-repository fixture, with a genuine approval and PRODUCTION's re-deriver. I then published a fast-forward history rewrite and a restoration of the original current bytes. With the genuine open-event file, the complete path refused `HISTORY-CONTINUATION: HISTORY-NOT-AN-EXTENSION`. Changing only the open-event file to `null` made the SAME rewritten history ACCEPTED. A normal history with `null` also ACCEPTED. This is a bypass of published-history authentication, not the covenant's inability to observe unpublished decisions.

The predecessor control is decisive: I reran the same probe against retained v13/v9. Null, an empty list, an integer and a string all refused `HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT`; the rewritten history with null also refused. V30 newly accepts null. V30's other non-object JSON values instead escape with AttributeError after a class-0 finding has been queued: P:180 accesses retained.get during D:383's same-ID check. The new structure must handle invalid retained values without either accepting or crashing past the resolver.

**V30-2 [MAJOR] — load_identity still decides outside the resolver, including before and after it. UNREPAIRED CONTRADICTION with the universal class-0/precheck claim.**

D:205 calls verify_witness before composed_resolver. D:184–186 performs a real fetch and raises `WITNESS-FETCH-FAILED` on transport failure. This is evidence unavailability, not a locally proven identity contradiction. In my complete-path fixture, wrong approval repository plus a failed freeze-witness fetch returned `WITNESS-FETCH-FAILED fixture transport unavailable`, before the local sweep or feed authentication. Renaming this existing refusal does not turn its cause into class 0. `_drand_modules` can similarly raise `VERIFIER-UNAVAILABLE` at D:114 before the resolver.

Conversely, local size/type and disjointness checks occur AFTER the resolver, D:313/315. I coherently sealed an identity with one tuning ID missing. With a healthy feed it refused `IDENTITY-tuning_objids-SIZE-OR-TYPE`; with HTTP 503 it returned `RETRY-EVENTS-UNAVAILABLE`, leaving that class-0 defect unchecked. The same placement affects overlap and, when enabled, the split checks at D:311/405/413. Thus moving seed re-derivation inside the resolver did not encompass the complete conjunction.

Here is the explicit pre-entry raise inventory. “0” means consistent with the stated local-integrity class when the indicated defect is positively established; it does not assert that every underlying I/O failure proves that defect. Repeated tokens at different checks are listed with their lines.

| Path and lines | Named raises | Class assessment |
|---|---|---|
| D:66–67 | ADOPTION-MISSING; ADOPTION-MALFORMED | 0 |
| D:114 | VERIFIER-UNAVAILABLE | Unavailability, not 0 |
| D:171/173/175 | WITNESS-MISSING; WITNESS-COMMIT-MALFORMED; WITNESS-NOT-A-GIT-REPO | 0 for established local defects |
| D:178/180/183 | WITNESS-COMMIT-LACKS-JOURNAL; WITNESS-COMMIT-LACKS-RECORD; WITNESS-REMOTE-URL | 0 for established absence/binding/configuration defects; git failure is not independently distinguished from absence |
| D:186 | WITNESS-FETCH-FAILED | RETRY-UNAVAILABLE by cause; emitted before resolver |
| D:188 | WITNESS-NOT-PUSHED | Publication/ancestry finding, dependent on fetched evidence; DERIVED-TERMINAL if proven, unavailable if ancestry cannot be evaluated; not unconditionally 0 |
| D:202/204/206 | IDENTITY-MISSING; IDENTITY-NOT-SEALED; IDENTITY-NOT-IN-WITNESS-COMMIT | 0 for established integrity defects |
| D:209/211/212/213 | IDENTITY-SCHEMA; IDENTITY-FIELD-MISSING; IDENTITY-POOL-DIGEST; IDENTITY-EXCLUSION-DIGEST | 0 |
| D:215/216/217/219 | PROTOCOL-NO-REDERIVER; ADOPTION-MISMATCH; IDENTITY-RULE-DIGEST; IDENTITY-NOT-BEACON-SEEDED | 0 |
| D:226/227/230/232 | IDENTITY-BEACON-NOT-ACCEPTED; IDENTITY-SOURCE; IDENTITY-WITNESS-MISSING; IDENTITY-WITNESS-COMMIT | 0 |
| D:235/237/238/240 | APPROVAL-RECORD-MISSING; APPROVAL-RECORD-DIGEST; APPROVAL-RECORD-NOT-AT-COMMIT; APPROVAL-RECORD-HISTORY | 0 for established retained-record integrity defects |
| D:241 | APPROVAL-COMMIT-NOT-PUSHED | Same publication/evidence qualification as D:188; not unconditionally 0 |
| D:243/245/246/247 | APPROVAL-NOT-FIRST; APPROVAL-RULE-LINE; APPROVAL-T-SIGN-LINE; APPROVAL-NONCE-LINE | 0 for retained history/binding defects |
| D:250/252/253/254/255 | IDENTITY-T-SIGN; IDENTITY-T-PULSE; IDENTITY-ROUND; IDENTITY-T-SIGN-PREDATES-AMENDMENT; IDENTITY-T-PULSE-EXCLUDED | 0 |
| D:258/260/261/262/264 | IDENTITY-WITNESS-MISSING; IDENTITY-WITNESS-TIME; IDENTITY-WITNESS-LATE; EVENT-DIGEST; EVENT-INCONSISTENT: IDENTITY-WITNESS-COMMIT in composed mode | 0; positive non-delivery remains terminal |
| D:266 | IDENTITY-WITNESS-COMMIT-UNDETERMINED | Offline only; NOT class 0 and unreachable here in composed mode because D:265 defers it |
| D:268/271/272/273 | EVENT-PROVENANCE; IDENTITY-WITNESS-NONCE at both round checks; NONCE-UNAUTHENTICATED | 0 under the retained-evidence integrity interpretation; nonce bodies are actually verified |
| D:277/278/279 | ADOPTION-MALFORMED; ADOPTION-NOT-AT-APPROVAL-COMMIT; ADOPTION-DIGEST | 0 |
| D:282/283/285/287/288 | COLLECTION-LOG-DIGEST; COLLECTION-LOG-NOT-IN-WITNESS-COMMIT; HISTORY-INVALID; HISTORY-GENESIS; HISTORY-COUNT | 0 |
| D:290/291/292/293/294 | COLLECTION-LOG-EMPTY; IDENTITY-LOCK-MISMATCH at both checks; COLLECTION-CLOSED; COLLECTION-LOG-CONFLICT | 0 for recorded-state/identity integrity; a retained CLOSED is never a retry |
| D:297/298/300/301/304/306 | BEACON-RECORD-DIGEST; BEACON-RECORD-NOT-IN-WITNESS-COMMIT; BEACON-RECORD-UNREADABLE; BEACON-RECORD-BINDING; BEACON-RECORD-STATEMENT; BEACON-RECORD-RELAYS | 0 for retained-file/schema/binding integrity |

This inventories the explicit named raises on the route to D:307, including called witness/adoption/import helpers. There are also unnormalized exceptions from JSON parsing, indexing required nested fields, path conversion, file reads and subprocess launches. They do not pass through resolve and are not automatically named class-0 findings. `blob_at_commit_equals` also collapses a failed git read into False. A complete totality claim needs these cases covered, not merely a list of DataIntegrityFail statements. Environment/scoring/holdout raises outside load_identity are not pre-entry raises on this path.

**V30-3 [MAJOR] — contributors still suppress higher findings internally, and evidence is not shared across retrievals. UNREPAIRED CONTRADICTION with “one place,” “every finding,” and retrieval-order invariance.**

P:273–277 simply wraps the old continuation. P:394–395 returns the open-event authentication outcome before checking already-fetched history extensions at P:397–402. My published rewrite returned `HISTORY-NOT-AN-EXTENSION` with a healthy open-event retrieval, but `RETRY-HISTORY-CONTINUATION: EVIDENCE-UNAVAILABLE` when that retrieval was empty. The remote objects proving the rewrite had already been fetched. Stage D contributed the lower finding and suppressed the higher one; the outer minimum cannot recover it.

P:192 returns UNAVAILABLE for undetermined retained delivery before evaluating feed expiry at P:198. A retained undetermined approval, a successfully obtained newer feed, and unavailable history remote returned `RETRY-EVENTS-UNAVAILABLE` on the complete path. Standalone authentication also returned UNAVAILABLE, although the new declared EXPIRED class outranks it. The old helper docstring still describes unavailability before absence/expiry. The new order is not implemented throughout the helper.

“One retrieval serves both events” is accurate only for B's approval authentication and open same-ID comparison. A successful normal path makes three feed retrievals: B, D's open authentication, and D's per-entry publication retrieval. Obtained evidence is not accumulated for all affected predicates:

| Same underlying fixture, changed retrieval order | Complete-path result |
|---|---|
| Genuine approval in B; conflicting same-ID approval copy also obtained in later D feeds | ACCEPTED |
| Conflicting approval copy obtained in B; genuine feed thereafter | EVENT-FORGED |
| Strictly earlier qualifying open event obtained only in B | ACCEPTED |
| Same earlier open event obtained in D's open retrieval | HISTORY-CONTINUATION: OPEN-EVENT-NOT-EARLIEST |

Each approval-conflict experiment made three retrievals. These are fixture evidence-consistency tests, not claims that GitHub honestly creates two distinct events with one ID. They establish that an affirmative contradiction actually obtained by this invocation can be ignored depending on where it appears. A stale clone needing D's fetch makes the distinction particularly material: B has only performed the open same-ID check, not full delivery/ordering/expiry authentication. Reuse a defined evidence snapshot or accumulate all obtained evidence and apply it to every applicable check; independent retrievals without reconciliation do not provide the promised invariance.

**Order and pairwise judgment.** PRECEDENCE at P:250 and resolve at P:254–256 provide a total order over the eight named classes. They do not constitute a total classifier of program outcomes. resolve assumes a nonempty list; ACCEPT is implemented separately by D:397. Within-class seq is the contribution index, stable under the production's fixed sequence, not a permanent stage identifier independent of execution order.

EXPIRED above DERIVED-TERMINAL and RETRY-UNAVAILABLE above RETRY-INCOMPLETE are defensible proposed diagnostic policies: loss and known defects still refuse; unavailable evidence can explain why completeness cannot currently be established. They require explicit consistent mappings. Adoption mismatch and retained CLOSED/nonce integrity can reasonably be class 0. Seed cryptographic re-derivation is explicitly assigned class 4 or 5. That boundary should be spelled out because “from retained evidence” overlaps the broad local-integrity description.

Receipt handling is not classified by its underlying cause: D:378–381 puts EVERY failed configured receipt verification into EXPIRED, including P:433–450's malformed/digest/origin/event-absent checks and remote-unavailable returns. This may be an intentional “expired approval still lacks an acceptable substitute” policy, but it must be named as such; missing/unreadable retained receipts otherwise fit the header's class-0 description. PENDING-PUSH is expressly class 4 despite the operational instruction to retry its publication. These policies are not intrinsically adoption-fatal, but the blanket total/no-exceptions wording is unsound without their qualification.

I reproduced all 21 filed class-pair rows exactly. The exhibit tests selecting a minimum over manufactured findings, not exhaustive derivability or evidence collection. I also constructed actual conditions across every pair of stages: A = wrong open repository, B = affirmative same-ID approval contradiction, C = coherently rebound unverifiable seed bodies, D = a published rewrite followed by restoration. Results with normal and reversed construction/feed order were:

| Stage pair | Winner |
|---|---|
| A/B | HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT |
| A/C | HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT |
| A/D | HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT |
| B/C | EVENT-FORGED |
| B/D | EVENT-FORGED |
| C/D | HISTORY-CONTINUATION: HISTORY-NOT-AN-EXTENSION |

For actual derivation-order stress, I additionally executed 24 combinations: all six pairs, both feed orders, and ABCD versus DCBA stage execution. DCBA was an explicitly labelled in-memory experiment using the same stage bodies with shared open-file setup; it is not claimed to be a second production path or an edit to pinned code. All listed winners were invariant. I captured actual contributions and also reversed their list order. Crucially, A/D does not contribute the independent history-rewrite finding: D stops at the open mismatch. This passing winner therefore does not establish “every finding recorded.” The snapshot and suppressed-history examples above disprove the stronger property despite the passing matrix.

Additional complete-path pairs passed: NOT-EARLIEST versus seed REDERIVE-RETRY, both feed orders; approval EXPIRED versus remote unavailability, both orders; missing open file versus simultaneous NOT-EARLIEST, seed retry and remote failure. They returned EVENT-NOT-EARLIEST, EVENT-EXPIRED-NO-RECEIPT-PATH and HISTORY-OPEN-EVENT-MISSING respectively. Missing file is handled correctly; successfully parsed null is the regression.

**The three states and retained counter-cases.**

Offline PRODUCTION still defaults to provenance_mode='offline', holdout_once=False and verify_split=False. The filed baseline, coherent forged approval, rebuilt history, attack A and trusted swapped lists retain their disclosed offline ACCEPTED verdicts. Retained CLOSED refuses COLLECTION-CLOSED; removed ACCEPT refuses COLLECTION-LOG-EMPTY; positive approval non-delivery refuses IDENTITY-WITNESS-COMMIT. An unknown-before delivery without a commits shortcut refuses IDENTITY-WITNESS-COMMIT-UNDETERMINED.

Standalone v10 authenticates genuine evidence; refuses wrong repository/positive non-delivery as INCONSISTENT-INPUT, same-ID canonical contradictions as FORGED, and a strictly later retained qualifying event as NOT-EARLIEST. Before-only and head-only changes were exercised; missing descendant objects without contradiction yielded UNAVAILABLE, and an unlaunchable git yielded UNDETERMINED. A verbatim genuine event plus a conflicting same-ID copy yielded FORGED. Plain covered absence yielded INCOMPLETE; a newer unrelated feed yielded EXPIRED. The new universal precedence promise has the qualifications in V30-3.

Composed v14 reproduces the filed genuine ACCEPT and EVENT-FORGED / HISTORY-NOT-AN-EXTENSION / OPEN-NOT-GENESIS-ONLY refusals for attacks 1/2/A. It now also has V30-1's undisclosed acceptance. Every filed V29 combined row passes: invalid seed signatures plus wrong approval repository → EVENT-INCONSISTENT; plus genuine conflicting same-ID approval → EVENT-FORGED; genuine approval → REDERIVE-RETRY; wrong open repository plus ls-remote failure or approval HTTP 503 → OPEN-EVENT-INCONSISTENT-INPUT; conflicting open same-ID evidence plus ls-remote failure → OPEN-EVENT-FORGED; genuine open plus ls-remote failure → RETRY-REMOTE-UNAVAILABLE.

The V28/V27 complete-path cases also passed against the successors: unknown-before/real-later-head approval with genuine same-ID contradiction → EVENT-FORGED; wrong repository with healthy feed or HTTP 503 → EVENT-INCONSISTENT; undetermined with only retained evidence → RETRY-EVENTS-UNAVAILABLE. Open analogues returned HISTORY-CONTINUATION: OPEN-EVENT-FORGED, HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT and RETRY-HISTORY-CONTINUATION: EVIDENCE-UNAVAILABLE. Positive non-delivery stayed terminal. These are exact repaired cases, not proof that clause (1) holds before every possible failure.

**V30-4 [MINOR] — offline vocabulary is still overstated.** Offline's named delivery refusal is preserved, but “offline has no retry vocabulary” and “every offline raise is class 0” are false. With coherently rebound retained seed bodies that do not verify, offline load_identity returned `REDERIVE-RETRY` through D:309 → D:124. Offline also performs the freeze-witness fetch and can raise WITNESS-FETCH-FAILED. IDENTITY-WITNESS-COMMIT-UNDETERMINED is the unique specifically named approval-delivery-undetermined refusal there, not its only evidence-unavailability disposition. The seed mismatch at D:310 is class 4 under the stated order. Correct the scope of these assertions.

FORGED remains an affirmative-contradiction identifier. No inspected FORGED branch uses plain absence alone. Under an intact protected ref with no force-push or deletion, my actual honest fast-forward push did not redeliver the already ancestral approval commit, and an honest delivery on another ref was excluded. With the genuine earliest event retained, later distinct qualifying evidence remained AUTHENTIC; equal timestamps stayed AUTHENTIC in either order. Synthetic absent-event redelivery reaches FORGED under the stated predicate, but is not proof of an honest false-forgery path under the protected-ref assumptions. GitHub documents event IDs as unique; conflicting same-ID records justify refusing the evidence without identifying which producer supplied false bytes. [GitHub event documentation](https://docs.github.com/en/rest/using-the-rest-api/github-event-types).

**Repair classification and the two categories.**

| Claim | Judgment |
|---|---|
| Blanc item 1: order stated | REPAIRED as an explicit class list; outcome coverage/overlapping definitions need qualification |
| Blanc item 2: one enforcing place | NOT REPAIRED: V30-1/2/3 |
| Blanc item 3: pairwise exhibit | REPAIRED as the 21-row resolver exhibit; NOT REPAIRED as complete-path/retrieval-order proof |
| Blanc item 4: old tests kept, resolver test added | REPAIRED; independently executed |
| V29-1/2 | Exact seven rows REPAIRED; whole-pattern closure NOT REPAIRED |
| V29-3/4 | REPAIRED: four digest placeholders removed, aggregate labels corrected, strictly-earlier predicate verified |
| V28-1/2 | Exact cases REPAIRED; universal promise NOT REPAIRED |
| V28-3 | REPAIRED targeted digest associations, fixture/header wording and rule-(iii) qualification |
| V27-1/2 | Exact helper/tri-state cases REPAIRED; complete-path universality NOT REPAIRED |
| V27-3 | Targeted lineage/name/count corrections REPAIRED; not a blanket truth certificate |
| V26-1/2/3 | Qualified contradiction predicate, tri-state behavior and targeted text corrections REPAIRED; new total-order claim remains defective |
| P1/P2/P3/P4 | Ancestry batch proof, absence dispositions, targeted labels and covenant insertion REPAIRED; terminal-before-retry generalization qualified above |
| N1 | COVENANT, not a technical completeness repair |
| N2/N3 | REPAIRED targeted publication dispositions and unrelated-commit producer refusal |
| N4/N5 | Correction-note classification and targeted labels REPAIRED |
| M1/M2 | Publication proof and pending-commit/error-entry producer behavior REPAIRED in helpers; V30-1 bypasses their composed enforcement |
| M3 | Superseded by N1's fuller COVENANT |
| M4 | DISCLOSED-AS-OPEN: all-event A′ not built |
| M5 | Historical drift disclosed; archived bytes verified; original editing not retroactively undone |
| M6 | Targeted text repairs REPAIRED |
| A | Helper's authenticated genesis anchor REPAIRED; composed guarantee NOT REPAIRED because of V30-1; unpublished completeness is COVENANT |
| B/C/D/E/F | Producer boundary, shared delivery evidence, control-refusal logging, render-end-last and availability disclosures REPAIRED within the composition qualifications above |

The literal question whether every DISCLOSED LIMIT is something no implementation could establish has answer NO. L-OFF is a chosen default-mode boundary; L-INH is a staged-but-disabled check; L-AVAIL combines external availability and stateless enforcement. Their mode qualifications make them honest disclosures, not irreducible impossibility claims. L-COV is an evidence limitation of this design; L-RCPT is the present identity mechanism's limitation, removable by another design. None licenses V30-1/2/3 to be moved into the limits column. Register section F's “whole pattern repaired; none known” is superseded by these UNREPAIRED CONTRADICTIONS.

Track 10's first behavioral run failed at its FIRST combined row; later rows were not reached in that run. The equal-time test failed behaviorally, placeholders failed textually, and the missing resolver was an interface ERROR. The two premature run-2 blocks are disclosed harness errors, not successful fail-first evidence. Track 9's older first run likewise does not mean seven independently observed failures: the complete case stopped at its first subcase, the ordering case failed a header phrase, and the text case had missing-file evidence. I read the correction note as filed: track 1 all behavioral; track 2 eight missing-interface errors with old behavior separately demonstrated; track 3 five missing-interface/five behavioral; track 4 three/four; track 5 three/three. An exception on an existing path is not automatically a missing interface. Current runs cannot authenticate historical execution times or undisclosed intermediate edits.

**Covenant, receipts and Duho's questions.** The full covenant is stated in P's header, T2's revision-5 text, R §3c and Q's full contract: published append-only history and ordered publications are authenticated; operation times and unpublished observation/decision completeness are not; an unpublished absence-based CLOSED can disappear before genesis publication or between publications; the fixed-round seed is unchanged; authentic late approval remains disqualifying; independently retained decision evidence is not implemented. I appended and erased an unpublished CLOSED in each interval: offline and composed both ACCEPTED the resulting coherent publication. That agrees with the covenant. Null bypasses even the promised published-history checks and therefore does not agree with it.

I also produced a FIRST receipt under the lane-proposed {actor: ops-witness, session: OPS}, committed and pushed it in a protected local fixture, without creating an OPS-retained copy. verify_events_receipt accepted it. With approval evidence expired but open/per-entry evidence live, the configured approval-receipt composed path ACCEPTED; Option C returned EVENT-EXPIRED-NO-RECEIPT-PATH. This exactly exercises the disclosed residual trusted step: provenance labels do not prove independent authorship. The origin is unadopted, not Duho's decision. The delegated workflow requires no per-receipt human confirmation. No such confirmation is requested here.

Q1 C remains the sound recommendation after repair: ALL approval/open/per-entry events must authenticate at tune and holdout; evidence loss closes that approval, temporary unavailability/incompleteness retries without changing the commitment, and no replacement round/seed/split/attempt follows. The loader does not persist study-level closure; that remains the rule's covenant. C is not accurately described as fully working today while V30-1 exists. Its “no residual trusted step” concerns receipts, not the continuing GitHub/drand assumptions.

A′ accurately says approval-only receipt support exists; history-open/per-entry receipt paths are unbuilt; receipts would cover ALL events and substitute only for EXPIRED, never UNAVAILABLE/INCOMPLETE or a proven inconsistency. B is NOT IMPLEMENTED; a second token on the same account is not a second identity, and a durable independent key would be a different mechanism. Q2 correctly asks nothing. Q1 should remain held until the package describes and implements the reviewed behavior. No additional routine Duho chores are needed to repair these defects.

The current documented feed limit is up to 300 events created in the past 30 days, with possible 30-second to six-hour latency; this is not a guaranteed execution window. The documented PushEvent shape can omit a commits list, supporting the ancestry-based delivery requirement. [GitHub Events API](https://docs.github.com/en/rest/activity/events).

**Execution, cost, preservation and pins.** I ran the requested 24 suites with the specified interpreters, separate environment variables and text-version attribution: 141 tests, all passed. Driver v14/V15: 23/17; history: 4; witness: 3; builder v30/V15: 8/4; beacon v30: 7; verifier: 4; track 1: 10; track 2: 8/2; tracks 3–5: 10/7/6; track 6: 5+1; track 7: 4+1; track 8: 7+1; track 9: 3+1; track 10: 4+1. Older text tests were run against their specified predecessors, not misattributed to V30. Eight track-8/9 precedence tests also passed with imports aliased to v10/v14. The inherited RuntimeWarning at fourier_chirality.py:87 remains; no ResourceWarning was observed.

Both beacon exhibits were identical and printed digest 2160fa754ce3db25613389d58bacd3098763ea8536744558e9dae96c5b4f0ae1. The drand-only exhibit printed 45d6149a2ccf30cb167dc4331455f3403a733516a82399292b1e7ad2c029e531. All 35 executed inspection verdicts match BOTH filed V29 and V30 tables after normalizing fixture commit IDs. The actual script is coherent_attacks_v30.py, as R specifies; the prompt's coherent_counter-cases_v30.py name is not the delivered script.

The exact signature preimages reproduced:

- V30: 98881c7ecba0ac3bb718983f8534aaa55d325efeb4314d72b31b64b95af2abb9
- V29: 4458b821e3a1249c0646ce2790491f4d04e7224d0ef60721144354e216450599
- V28: c9e65f1bfc2bdac10716760670c85866d20c1ec0ca1d9aebdfa5b83842804fc2

I hashed the package files and checked the pinned inventories. V30 has 99 distinct full digest values: 96 resolve to retained file bytes; the other three are the two reproduced exhibit-output digests and the reproduced sentinel digest. V23–V29 inventories contain 80/81/83/85/89/90/91 full values, with the same three generated-value exceptions. Historical incorrectly associated V27/V28 filename/digest citations cannot literally match the wrongly named files; the intended historical bytes remain present and V29/V30 correct those associations. No new pinned-byte drift was found. All four archived V22 files match their pins. The V22 and V24 copied-digest lists contain all four old digests; the V23 list contains successors and does NOT contain those four old values. The drift record's reliance on the V22 list is supported; claiming all three lists carry the old values would be false. Q's unchanged hash is 4e6dc490485cf956a6471ccad6be73fb86bfe0dc0d60712343b18f3a162e8a52.

Cost is one acknowledged push per history entry, including genesis and failure entries; an invocation can emit multiple entries. PENDING-PUSH means reconcile/retry the same pending publication; HISTORY-DIVERGED refuses incompatible history; unavailable remote evidence yields RETRY-REMOTE-UNAVAILABLE on the continuation path, with the earlier witness-fetch naming defect noted above. No affirmative current “one push per freeze” claim was found in R/Q/T2/P. T2 contains “NOT one push per freeze” outside quotation as an explicit correction; P quotes the old wording historically. Producer fixtures exercise local bare repositories with non-fast-forward receives denied and fixture-supplied gh runners. No live publishing was performed.

Individually preserved: sample sizes 400/200/2,000; floors 380/190/1,900; strict Wilson lower-bound >0.70 bar; failed-set exclusion; the 2,644 dry-run identities; excluded rounds 6440756/6441904/6441924; E5(d)'s separate-account point-in-time custody evidence and interval covenant; blindness and freeze-before-fresh-pixel rules; exactly ONE holdout, with holdout_once PREPARED NOT ADOPTED and default False; E1 as a factual erratum, with the 17 driver tests executed; verify_split UNADOPTED and default off. Actual custody installation and fresh-pixel isolation were not certified. The absent GZ1 source table makes guarded-pool reconstruction UNVERIFIABLE HERE.

The actual-future probe used host UTC 2026-09-06T18:52:19.768029Z, prospective T_sign 18:53:19Z, T_pulse 19:04:00Z and round 6443014. Collection refused BEACON-NOT-YET with zero fetch calls. The fixture's historical exclusion override was confined to its process; production exclusions remain pinned. No historical exhibit round was adopted as a study seed.

**Required clause before adoption.** Repair in versioned successors and add complete-path regression evidence, then state:

“In composed mode, every required retained event must be a valid PushEvent object. Missing, unreadable, null and other invalid values produce a named LOCAL-TERMINAL finding; none disables history verification. Acceptance requires affirmative success of approval authentication, seed re-derivation, published-history continuation and required per-entry publication checks. No required stage can be skipped into acceptance.”

“The precedence order applies to the entire load_identity conjunction, including freeze-witness availability, local list shape/disjointness and enabled split checks. Unavailable evidence is not a proven local inconsistency. Every independently derivable higher-priority finding is collected before a lower-priority result is emitted, including within history and authentication helpers. All live evidence obtained during an invocation is evaluated for every applicable contradiction and ordering predicate under an explicitly defined snapshot/reconciliation policy; changing retrieval order cannot suppress an obtained contradiction.”

“The mapping explicitly distinguishes local integrity, retained cryptographic validity, remote-derived publication findings, receipt refusal causes, evidence loss and temporary unavailability. Offline retains IDENTITY-WITNESS-COMMIT-UNDETERMINED for unresolved approval delivery and separately exposes its existing seed-re-derivation and witness-availability refusals; no broader claim that all offline refusals are class 0 is made.”

Keep the full covenant, mode qualifications, all-events Option C consequences, receipt trusted step and unbuilt A′/B labels. These repairs require no new adoption decision from Duho. Adoption can concern exact reviewed successor bytes and concrete operating consequences only after this implementation/text mismatch is closed.

Execution logs, digest inventories and temporary probe sources are retained at /var/folders/64/71dstw0j1gd_n58lsxnhl3p80000gn/T/codex_v30_seatb_37is4xqb. In particular: null_probe.log and null_v29.log establish the regression; resolver_probes.log and more.log establish precedence gaps; derivation_orders.log records actual contributed findings in the labelled order experiment; suite_results.json and inspection.log record package verification. Only this report was written in the reviewed directory; pinned implementation files were rehashed unchanged.

VERDICT: NOT-SIGNABLE

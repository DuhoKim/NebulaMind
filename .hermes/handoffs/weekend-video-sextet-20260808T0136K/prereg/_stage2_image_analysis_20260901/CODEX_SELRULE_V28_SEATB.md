ACCESS_SHA=c9e65f1bfc2bdac10716760670c85866d20c1ec0ca1d9aebdfa5b83842804fc2

Independent complete-package review of STAGED V28. Nothing adopted, approved, signed or drawn. Codex previously authored builder field-validation code on September 6, 00:13–00:18; that code no longer participates. The findings below concern the retained successors, which I did not modify. Historical Codex findings are identified as such rather than treated as independent new evidence.

All 132 required tests pass in 20 suites. Both property exhibits reproduce. Nevertheless, two production-path precedence contradictions remain: unresolved delivery can still prevent examination of a same-ID contradiction or a locally decidable wrong-repository mismatch. These are UNREPAIRED CONTRADICTIONS under Blanc’s 02:06 order, not disclosed limits. No new FATAL or undisclosed successful composed identity bypass was demonstrated.

References below: R = OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V28_20260907.md; D = _optionA_dev/fourier_chirality/run_configurations_v12.py; P = _optionA_dev/track2/provenance_designs_v8.py; Q = QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md; T2 = TRACK2_PROVENANCE_DESIGNS_UNADOPTED_20260906.md. Numbers after these aliases are source line numbers.

**[MAJOR] V28-1 — The approval precheck still overrides the repaired precedence.** R:3,21,38; D:256–258,302,340; P:142–165.

I built fresh, coherently sealed identities using the real production re-deriver, authentic retained BLS evidence, local protected bare remotes and one acknowledged publication per history entry. I changed the retained approval event to retain the genuine event ID but claim delivery through an unknown `before` object and a real later head, removing the direct commits shortcut. The configured live feed contained the genuine, conflicting same-ID event.

The standalone v8 authenticator returned FORGED. The complete composed load returned:

`RETRY-EVENTS-UNAVAILABLE: IDENTITY-WITNESS-COMMIT-UNDETERMINED`

D:258 raises before D:302 can call composed provenance. Thus the retrieval that could establish the same-ID contradiction is never reached. This is precisely an unstated precedence exception to “same-id contradictions before any retry shortcut,” also promised by D:2.

A stronger, entirely local counter-case combines that undetermined payload with `repo.name = wrong/repo`. Standalone v8 returns INCONSISTENT-INPUT. The complete composed path returns the same retry, both with a healthy configured feed and with HTTP 503. The repository mismatch needs no retrieval or ancestry. This is not evidence unavailability; it is an already decidable inconsistent input kept pending by an earlier return.

The simple wrong-repository/503 case with direct delivery does return EVENT-INCONSISTENT, as claimed. Track 8 therefore proves that narrower repair, not the combined contract. Offline returns IDENTITY-WITNESS-COMMIT-UNDETERMINED for the undetermined payload, correctly implementing its newly stated vocabulary.

**[MAJOR] V28-2 — The history-open wrapper reproduces the same precedence defect.** R:3,21,38; P:222–230,321–323; D:351–354.

In a separate valid composed identity, I changed the retained history-open event’s `before` to an object no clone holds and its head to a real later history commit, preserving its ID. The runner served the genuine original open event. The results were:

- Pure v8 event authentication: FORGED.
- `validate_continuation_v8`: EVIDENCE-UNAVAILABLE.
- Complete composed load: RETRY-HISTORY-CONTINUATION: EVIDENCE-UNAVAILABLE.

P:321 still takes the Boolean failure before event authentication at P:322. The v8 wrapper reclassifies that failure at P:229 without consulting the feed. Adding a wrong repository to the same retained open event still produces the retry, although the pure authenticator returns INCONSISTENT-INPUT.

The isolated tri-state repairs are real: with no contradictory event, undetermined open delivery correctly retries; positive non-delivery correctly returns OPEN-EVENT-INCONSISTENT-INPUT. But translating the Boolean refusal into a tri-state refusal does not propagate the precedence rules through this stage. Both V28-1 and V28-2 can keep a positively inconsistent identity pending indefinitely; neither probe loaded it. L-AVAIL cannot be used to reclassify these failures as legitimate stateless-retry limits.

**[MINOR] V28-3 — Names, pins and decision-facing outcome wording still need correction.** R:21,33; T2 outcomes table; Q:23; inspection row 1; test_run_configurations_v12.py:1.

1. R:21’s “V27 was” builder-fixture citation names `test_build_corpus_identity_v28.py` with digest `4fbf91fe4de84d2e221b25fdd446aee35693b48a29fb4980d44935f6238a3a12`. Those bytes belong to retained `test_build_corpus_identity_v27.py`. The actual v28 fixture hashes to `fd581106fae0475112337d3b7677c95d805f73a4bd9db7bb9f87268baf4f5691`.
2. R:33 calls the historical verifier `verify_drand_v2.py` beside `a781b965e50ea947969f4559c267b88505b55d292b04d0b4739381216da6c20d`; that digest belongs to `verify_drand.py`. Its parenthetical mentions the historical filename, but the citation itself remains misleading.
3. The current driver fixture opens by calling itself the staged v8/V24 fixture. The inspection’s row-1 note still says `authenticate_event → FORGED` for the wrong-repository example whose row 9b is INCONSISTENT-INPUT. The repaired inspection header and row 9b are correct; this adjacent note is not.
4. Q’s full-contract paragraph still says FORGED “only” on a same-commit delivery contradiction. It omits the same-ID arm, including a changed head with undetermined delivery. T2’s outcomes row is labelled v7 and lacks v8’s absent-only qualification, while another row supplies it. The current decision contract should state one consistent predicate and precedence. A later distinct qualifying event alongside a retained earliest genuine event produces AUTHENTIC; NOT-EARLIEST requires an earlier qualifying event. Do not shorten rule (iii) to “another delivering push means NOT-EARLIEST.”

The driver lineage itself is now correct: I checked each import, v6→v2, v7→v3, v8→v4, v9→v5, v10→v6, v11→v7, v12→v8. The seven-outcome helper description, historical EXPIRED annotation, current inspection module names, §9’s historical V22 attribution, and 132/20 count are repaired.

**The three states, executed.** Fixture runners supply Events API responses; local bare repositories stand in for GitHub and deny non-fast-forward receives. These executions do not establish actual GitHub branch protection. Production’s own re-deriver is used; fixture paths, sizes and the historical exhibit-round exclusion are explicitly overridden.

| Case | Offline production defaults | Standalone v8 helpers | Composed load_identity |
|---|---|---|---|
| Genuine sealed identity and published history | ACCEPTED | AUTHENTIC / valid continuation | ACCEPTED |
| Filed attack 1, coherent forged approval | ACCEPTED | Wrong repo: INCONSISTENT-INPUT; pinned-repo contradiction: FORGED | Row 10b EVENT-FORGED |
| Filed attack 2, rebuilt history after honest publication | ACCEPTED | HISTORY-NOT-AN-EXTENSION or HISTORY-DIVERGED, according to fixture state | Row 10c HISTORY-CONTINUATION: HISTORY-NOT-AN-EXTENSION |
| Attack A, rebuilt history first published with multiple entries | ACCEPTED | OPEN-NOT-GENESIS-ONLY | Row 10d HISTORY-CONTINUATION: OPEN-NOT-GENESIS-ONLY |
| Coherently sealed negative/swapped lists | ACCEPTED with verify_split off | Not an event-authentication check | Inherited list trust remains unless verify_split is adopted |
| Wrong repo, direct delivery, HTTP 503 | ACCEPTED in my coherent fixture | INCONSISTENT-INPUT before retrieval | EVENT-INCONSISTENT |
| Approval delivery undetermined, no contradiction | IDENTITY-WITNESS-COMMIT-UNDETERMINED | UNAVAILABLE | RETRY-EVENTS-UNAVAILABLE |
| Approval delivery undetermined plus genuine same-ID contradiction | IDENTITY-WITNESS-COMMIT-UNDETERMINED | FORGED | RETRY-EVENTS-UNAVAILABLE — V28-1 |
| Approval wrong repo plus undetermined delivery | IDENTITY-WITNESS-COMMIT-UNDETERMINED | INCONSISTENT-INPUT | RETRY-EVENTS-UNAVAILABLE — V28-1 |
| Positive approval non-delivery | IDENTITY-WITNESS-COMMIT | INCONSISTENT-INPUT | EVENT-INCONSISTENT: IDENTITY-WITNESS-COMMIT |
| Open delivery undetermined, no contradiction | Open-event authentication is not an offline requirement | EVIDENCE-UNAVAILABLE | RETRY-HISTORY-CONTINUATION: EVIDENCE-UNAVAILABLE |
| Open delivery undetermined plus same-ID contradiction / wrong repo | Same offline boundary | Pure authenticator: FORGED / INCONSISTENT-INPUT; continuation validator incorrectly retries | RETRY-HISTORY-CONTINUATION: EVIDENCE-UNAVAILABLE — V28-2 |
| Positive open non-delivery | Same offline boundary | OPEN-EVENT-INCONSISTENT-INPUT | HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT |

All 35 filed inspection rows reproduced, allowing freshly generated commit hashes. Every verdict equals V27’s; row 10b’s explanation changed and row 10c contains a fresh commit hash. Other named refusals reproduced include APPROVAL-NOT-FIRST, IDENTITY-LOCK-MISMATCH, COLLECTION-CLOSED, COLLECTION-LOG-EMPTY, PENDING-PUSH, HISTORY-DIVERGED, RETRY-REMOTE-UNAVAILABLE, EVIDENCE-EXPIRED, EVIDENCE-UNAVAILABLE, EVIDENCE-INCOMPLETE, HISTORY-PUBLICATION-BATCH and PUBLISH-UNRELATED-COMMITS. Same decoded drand signature with uppercase hex remains ACCEPT-DRAND with the same seed.

Additional independent event probes returned:

| Probe | Result |
|---|---|
| Retained event differs only in before | FORGED |
| Retained event differs only in head | FORGED |
| Verbatim event plus different canonical bytes under the same ID | FORGED |
| Missing descendant, retained event itself supplied live | UNAVAILABLE |
| Missing descendant, genuine conflicting same-ID event supplied live | FORGED |
| git launch raises OSError | UNDETERMINED |
| Plain absence from a covering feed | INCOMPLETE |
| Verbatim event with earlier qualifying different-ID event | NOT-EARLIEST |
| Later unrelated event, approval older than oldest feed event | EXPIRED |
| Actual advancing push on protected fixture ref | EXPIRED when approval absent |
| Actual approval-commit push to another ref | EXPIRED when approval absent |
| Verbatim genuine approval plus those honest pushes | AUTHENTIC |
| Synthetic later same-commit redelivery, original present / absent | AUTHENTIC / FORGED |

The last row is a predicate stress test, not evidence of an honest second delivery on an intact no-force/no-deletion ref. An ordinary advancing push does not newly deliver a commit already in its before-history; another ref is ignored. I demonstrated no honest false-FORGED case within the protected-ref covenant. Keeping a verbatim genuine earliest event alongside a later distinct push does not fabricate or backdate that first event, and I demonstrated no acceptance exploit of the absent-only scope. Outside that covenant, repeated delivery after reset/recreation is not intrinsically proof that the first event was fabricated; the scope must remain explicit.

GitHub documents event IDs as unique identifiers. Two distinct honest events therefore should not share an ID. The conflicting-duplicate probe tests defensive handling of inconsistent evidence, not normal GitHub behavior. Refusal is sound; when the feed itself includes both versions, the token FORGED does not prove that the retained copy, rather than the feed, is dishonest. Canonical JSON formatting differences alone are not the changed-content case tested here. [GitHub event documentation](https://docs.github.com/en/rest/using-the-rest-api/github-event-types)

The pure authenticator’s two FORGED returns are guarded by affirmative same-ID or scoped same-commit predicates. Ordinary absence did not reach FORGED. The remaining problem is that complete-path callers bypass affirmative evidence, as demonstrated above.

**Disposition of earlier findings and the two categories.**

| Finding | Judgment on V28 |
|---|---|
| V27-1 | Targeted standalone cases REPAIRED; complete precedence NOT REPAIRED, V28-1/2 |
| V27-2 | Isolated tri-state names and git-launch behavior REPAIRED; their composition with precedence NOT REPAIRED |
| V27-3 | Main lineage/count/header repairs REPAIRED; complete naming sweep NOT REPAIRED, V28-3 |
| V26-1 | Before/head contradiction probes REPAIRED; terminal guarantee incomplete on callers |
| V26-2 | Standalone tri-state and positive-input names REPAIRED; production-path qualification above |
| V26-3 | Collector/verifier current boundary and expiry corrections retained; residual citation errors above |
| P1 | REPAIRED: batch evidence uses the shared delivery predicate, including tested ancestry-only batches |
| P2 | REPAIRED for plain absence and uniform retry names; terminal-precedence qualification above |
| P3 | Targeted sweep retained; current sweep incomplete |
| P4 | REPAIRED: covenant is in Q |
| N1 | COVENANT, not a completeness repair |
| N2 | REPAIRED: empty/missing per-entry evidence retries; proven batch is terminal; full required-event coverage disclosed |
| N3 | REPAIRED: unrelated unpublished commits refused; collector/builder publication boundary built |
| N4 | REPAIRED historical accounting through the correction note |
| N5 | Targeted labels repaired; current naming qualification above |
| M1 | REPAIRED: server evidence of distinct ordered publications |
| M2 | REPAIRED: pending-commit reuse, reconciliation and outer failure publication |
| M3 | COVENANT, superseded by N1’s fuller statement |
| M4 | REPAIRED disclosure: A′ incomplete, C the available no-receipt design |
| M5 | REPAIRED archival/accounting; original in-place drift remains historical fact |
| M6 | Targeted repairs retained; present text sweep incomplete |
| A | Original late-first-publication attack REPAIRED; unpublished decision completeness remains COVENANT |
| B | REPAIRED producer/acknowledgment boundary within the stated covenant |
| C | Shared delivery evidence retained; tri-state/precedence qualifications above |
| D | REPAIRED: control refusal logged |
| E | REPAIRED: render-end must be last relevant journal record |
| F | REPAIRED empty-feed/error behavior, availability disclosure and B’s unimplemented status |

L-OFF, L-COV and L-RCPT describe real limits of their stated evidence boundaries. L-INH is a disclosed default-mode implementation limit, not something no possible implementation here can establish: the optional verify_split implementation is explicitly staged. L-AVAIL combines real external availability limits with stateless closure enforcement. Accordingly, not every entry is an irreducible limitation of every staged mode; the mode qualifications matter.

None of those disclosures excuses an input already known to name the wrong repository being called unavailable. §3c, the limits register and inspection header visibly separate the categories, but their assertion that V27-1/2 are repaired is substantively false. Put V28-1/2 in the unrepaired-contradiction column until repaired. Ordinary unknown evidence remaining pending is distinct from these established mismatches being kept pending.

**Covenant, receipt trust and Duho’s questions.**

The full covenant is present in P’s header, T2, §3c and Q: published append-only history and ordered publications are authenticated; operation times and completeness of unpublished observations/decisions are not; this applies before genesis publication and between later publications; an unpublished absence-based CLOSED can be removed; the fixed-round seed stays unchanged; a genuinely late approval event remains disqualifying; stronger decision evidence is not implemented.

My independent fixtures appended and erased an unpublished absence-based CLOSED before genesis publication and between publications. Both variants were ACCEPTED offline and composed. This confirms the disclosure; it is not another alleged repair failure. Published CLOSED remains terminal in the executed suite/inspection.

The fabricated-first-receipt trust is also disclosed consistently: the OPS label is the lane’s proposal, not Duho’s decision; shared GitHub credentials do not authenticate which agent made the first receipt. I fabricated a first receipt, committed and pushed it in a local fixture, and `verify_events_receipt` returned True with the expected OPS label. Only OPS’s independently retained copy/pane record can expose that fabrication. Replacement is separately checked by code. Delegation does not eliminate this trust; no per-receipt human confirmation is proposed.

Q1 Option C remains the sound recommendation: require ALL approval, history-open and per-history-commit events live at both tune and holdout; configure no receipt path. GitHub currently documents at most 300 events from the past 30 days and latency from 30 seconds to six hours. That is an actual-availability boundary, not a guaranteed 30-day runway. Loss before tune prevents loading; loss between tune and holdout prevents holdout. Study-level closure is a covenant, not a persisted loader state. Nothing permits a new approval, round, seed, split or attempt. [GitHub Events API](https://docs.github.com/en/rest/activity/events)

A′ accurately identifies its missing open/per-commit receipt paths and the need to cover every required event inside the window. Only approval-event receipt substitution is built. Receipts would substitute for EXPIRED only; temporary UNAVAILABLE/INCOMPLETE remain retry dispositions; positive inconsistencies remain terminal in the intended contract. B is NOT IMPLEMENTED; another token on the same GitHub account is not another identity, and a macOS account does not supply a GitHub identity. A durable custodian-key alternative requires implementation and review first.

Thus the scope of Q1 and “Q2 — nothing” is appropriate; routine receipt chores are not a new Duho question. However, “C works today as described” needs the V28-1/2 repairs, and Q’s outcome paragraph needs V28-3’s predicate update. The default delegated workflow is relevant only if receipts are later chosen; C carries no fabricated-first-receipt trust.

**Execution, attribution and preservation.**

Required executions used PYTHONDONTWRITEBYTECODE=1, the supplied py_ecc 8.0.0 venv for BLS fixtures, /usr/bin/python3 with the supplied site-packages for driver/tracks, and the requested warning policies. RULE_TEXT, DESIGN_TEXT and QUESTIONS_TEXT were separate environment variables.

| Suite | Tests |
|---|---:|
| test_run_configurations_v12 | 23 |
| test_run_configurations | 17 |
| test_history_v2 | 4 |
| test_approval_witness_v4 | 3 |
| test_build_corpus_identity_v28 | 8 |
| test_build_corpus_identity | 4 |
| test_beacon_record_drand_v28 | 7 |
| test_verify_drand_v2 | 4 |
| test_track1_fail_first | 10 |
| test_track2_fail_first | 8 |
| test_provenance_designs | 2 |
| test_track3_fail_first | 10 |
| test_track4_fail_first | 7 |
| test_track5_fail_first, V25 text | 6 |
| test_track6_fail_first, V28 text | 5 |
| test_track6_text_v26, V26 text | 1 |
| test_track7_fail_first, V28 text | 4 |
| test_track7_text_v27, V27 text | 1 |
| test_track8_fail_first, V28 text | 7 |
| test_track8_text_v28, V28 text | 1 |
| Total, all OK | 132 |

There was one RuntimeWarning, at fourier_chirality.py:87, in the driver-v12 suite; no ResourceWarning. A pass of an older version-specific label test establishes nothing about V28’s labels. Text assertions do not establish complete semantic agreement.

Both `exhibit_property_v22.py` runs returned EXHIBIT OK and digest `2160fa754ce3db25613389d58bacd3098763ea8536744558e9dae96c5b4f0ae1`. The additional drand-only exhibit returned `45d6149a2ccf30cb167dc4331455f3403a733516a82399292b1e7ad2c029e531`. `signature_preimage.py` printed the full ACCESS_SHA digest above.

Fail-first records were read per test. Track 8 run 1 is three assertion failures plus three errors: the OSError is behavioral, the missing open-validator interface is an interface error, and the absent inspection artifact affects the text case. Run 1b establishes the old UNAVAILABLE/AUTHENTIC/UNAVAILABLE function results; run 1c establishes the old complete-path IDENTITY-WITNESS-COMMIT refusal. Run 2’s two failures were test-construction errors: fetch restored the supposedly missing object, and the selected open-event parent also delivered the approval commit. Run 2b corrected those constructions without code changes; run 2c tests the corrected cases against unrepaired bytes. Run 3 separately corrects the stale suite-count expectation and tests V28 text fail-first against V27. These distinctions must not be collapsed into “seven old behavioral failures.”

I independently loaded the supplied unrepaired modules and ran all six track-8 code cases: four failures and two errors, including the old driver refusal. The unrepaired P file is byte-identical to v7; the driver differs from v11 only in three successor import names. This corroborates fail-first behavior without claiming that my later run proves the timestamps of historical runs.

The correction note remains necessary: track 1 has ten behavioral failures; track 2 eight missing interfaces; track 3 five missing interfaces and five behavioral failures; track 4 three missing interfaces and four behavioral failures; track 5 three missing interfaces and three behavioral failures. Existing-function exceptions are not automatically missing interfaces. Tracks 6/7’s run-1b behavior, expectation corrections and preserved failed aggregates remain historical evidence, not replaced by today’s passes. The track-4 combined-environment-argument error is a harness error, not a code result.

I hashed 4,653 package files and resolved the full-digest references in V23–V28. Their unique 64-hex values number 80/81/83/85/89/90 respectively. In V28, 87 match retained file contents; the remaining three are the two reproduced exhibit-output digests and the independently recomputed sentinel digest. The false filename associations are listed in V28-3; matching a digest elsewhere does not make a wrong path citation correct. Historical pinned bytes remain present at their retained paths or documented archive paths. Q hashes to `14b4e91bad9c0a7f38e87d3cd56e7df11bffab48ba7cf2291d663e84a1cf4179`.

The four archived V22 digests re-verified are:

- history_v2.py: `ce3d8c1cee3f97341cba23b538673aff2243b6058410c6d91784ab6098bfea7d`.
- test_track1_fail_first.py: `f2772a6cbe3081dfbd01732485feffdb6cc3a9eef9e0d024d739a7f669eef97c`.
- coherent_attacks.py: `1a00000e501b34c8249e88be988c8f197ea7bd05e40d2abb1f6bad2318778f0f`.
- test_track2_fail_first.py: `fb784f792981d13cdb0a404961dcf9ffb7e353a15048a9b38dd4ef347e6df238`.

The V22 copied-digest list carries all four at original paths. The V23 list carries successors, not those old hashes. The V24 list carries the archived originals. It would be false to say all three historical lists contain the old values. This supports the recorded drift chronology and preservation of the original review objects.

Preserved and re-verified individually: sample sizes 400/200/2,000; tuning/holdout floors 380/190 and validation floor 1,900; fixed 0.70 bar; failed-set exclusion; 2,644 dry-run identities, counted; excluded rounds 6440756/6441904/6441924; E5(d)’s point-in-time separate-account receipts plus interval/all-route covenant; label/pixel blindness and fresh-pixel timing; ONE holdout with holdout_once PREPARED NOT ADOPTED, default False; E1’s 17-versus-10 FACTUAL ERRATUM; verify_split UNADOPTED, default False. Actual custody and the absent GZ1 source table cannot be established by these fixtures: guarded-pool rederivation is UNVERIFIABLE HERE, not newly certified.

For an actual-future probe, the executing host clock was 2026-09-06T17:32:17Z, which is September 7 KST. A prospective T_sign of 17:33:17Z produced T_pulse 17:44:00Z and round 6442854. Collection returned BEACON-NOT-YET with zero fetch calls. The historical fixture rounds were not adopted as study seeds. The production re-deriver remains executable; the V20 missing-callback fatal did not recur.

Cost is one acknowledged push per history entry, including genesis and failure entries; a single collector/builder invocation can generate multiple entries and pushes. PENDING-PUSH requires retrying the same pending commit; a non-fast-forward rewrite is DIVERGED; remote unavailability refuses as RETRY-REMOTE-UNAVAILABLE. T2 still contains the literal “NOT one push per freeze” outside quotation marks; it is an explicit correction, not a remaining assertion of the old cost. No affirmative current one-push-per-freeze cost claim was found in the decision documents checked.

**What is missing before asking Duho to adopt exact behavior.** Repair the two contradictions in versioned successors, execute combined-condition fail-first tests on the complete paths, and reconcile the decision text and pins. The necessary clause is:

“On both the approval and history-open paths, locally decidable retained-event mismatches are terminal before any evidence-unavailability return. In composed mode, unresolved delivery does not bypass live authentication: a same-ID canonical contradiction obtained from the live feed is terminal before an undetermined-delivery retry. Only when no higher-priority inconsistency is established may undetermined delivery or unavailable retrieval return the stage’s retry disposition. Offline mode retains its explicitly named undetermined-delivery refusal.”

Keep this accompanying clause consistent in R, P, D, T2 and Q:

“Same-commit contradiction is scoped to the pinned protected ref and evaluated only when the retained event is absent. If it is present verbatim, distinct qualifying events are resolved by earliest-event ordering; a later event does not invalidate an authentic earliest event. Conflicting same-ID evidence is refused even beside a verbatim copy, without asserting that this alone identifies which producer supplied false evidence.”

Retain the full covenant, scoped offline limitations, exact receipt trust and Option C’s all-events availability consequences. Neither additional routine Duho chores nor adoption of A′/B is needed to repair these implementation contradictions. Correct the historical filename/hash associations and current outcome paragraph before presenting final bytes.

Execution records are outside the reviewed directory: `/var/folders/64/71dstw0j1gd_n58lsxnhl3p80000gn/T/codex_v28_eomouq3j/`; independent probes/results `/tmp/codex_v28_probes.py`, `/tmp/codex_v28_probes.log`, `/tmp/codex_v28_extra.py`, `/tmp/codex_v28_extra.log`, `/tmp/codex_v28_covenant.py`, `/tmp/codex_v28_covenant.log`, `/tmp/codex_v28_unrepaired.log`; digest index `/tmp/codex_v28_digest_index.json`. Main probe source SHA-256: `ff246dcf43076b00e6fc515792c10fe5547ac76d483ca40a34b4943616dcfd54`. Only this requested report was written in the reviewed directory.

VERDICT: NOT-SIGNABLE

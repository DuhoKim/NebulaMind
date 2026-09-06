ACCESS_SHA=ef222a1e298f2787e9cc6f1937dc646a453b0d263ddd427cc8324353c2ca4108

Seat B — independent referee of V17 only, as a prospective sampling amendment.

AUTHORSHIP: The supplied records attribute earlier builder field-validation code (2026-09-06 00:13–00:18) to Codex and state that it no longer participates in the beacon acceptance path. The branch-protection receipt also credits Codex acting at Duho's request. All new reviewed V17 code is attributed to Hwao. I authored no reviewed implementation in this turn. Builder integration/control results touch inherited Codex-associated work; the adverse findings below concern Hwao's current beacon/witness code and the unchanged production driver, independently inspected here. Historical receipts are supplied evidence, not actions independently repeated by this referee.

V17 is NOT-SIGNABLE. The original two counterexamples are repaired, but C5 still fails: an approval written and pushed after its seed time passes the actual builder with a backdated committer time. The nonce supplies no upper time bound. HTTPError also remains an explicit exception to the promised raising-fetch refusal.

References: V17 line numbers refer to OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V17_20260906.md. B = _optionA_dev/beacon_v2/; C = _optionA_dev/corpus_identity/; F = _optionA_dev/fourier_chirality/. Code references below use these prefixes.

Required execution and confinement checks

- First command was the exact requested shasum command; the full digest is above and matches the specified target.
- Warning-strict beacon command: python3 -W error -m unittest test_beacon_record_expedited test_beacon_v2: 33 tests, OK (14 + 19).
- Corpus command: python3 -W error::ResourceWarning -m unittest test_build_corpus_identity_v17 test_build_corpus_identity_v16 test_build_corpus_identity: 14 tests, OK (7 + 3 + 4).
- PYTHONDONTWRITEBYTECODE=1 prevented import cache writes. Additional probes used temporary directories outside the reviewed directory, the supplied test PKI and mocked public responses. Git pushes were exclusively to temporary local bare fixture repositories; nothing was published or pushed to GitHub.
- Both requested source diffs executed. Beacon diff: 14 removed + 31 added = 45 changed lines. The ordered removed-line list equals the fixture's literal FROZEN REMOVED_FROM_PINNED list exactly, independently checked by AST extraction and diff. The fixture passes; its added-line keyword allowlist is not a proof of behavioral completeness.
- Builder diff: 3 removed + 7 added = 10 changed lines, not E3's claimed 8. Changes are the docstring, imports/witness settings, witness invocation and witness field in the emitted identity.
- signature_preimage.py printed ef222a1e298f2787e9cc6f1937dc646a453b0d263ddd427cc8324353c2ca4108.
- All 30 distinct full E3 digests match local files; inventory below. The separately pinned §3b approval_witness.py also matches 62622c22bca7d6caa81ec562ddc8864517ebdc222bc4b37ac87a8c79f41e733c.
- V15_TO_V17.diff and V16_TO_V17.diff are byte-identical to freshly generated normal diffs: respectively 19 and 18 added/deleted document lines. Diff exit 1 denotes differences, not execution failure.

The five hard constraints

| Constraint | Result | Clause and code evidence |
|---|---|---|
| C1: exclude the public old pulse by name | MET | §3b(1a), V17:32, names 2026-09-06T00:15:00Z, NIST chain-2 pulse 1928801 and drand 6440756. B/beacon_record_expedited.py:26,39–40,68–69 excludes the timestamp; B/drand_round.py:10 reproduces the round. MIN_T_SIGN normally refuses first; the fixture isolates both exclusion branches. |
| C2: same formula from new approval time | MET for the formula and prospective rule | §3b(1)–(2), V17:32: “T_sign is the UTC of that approval”; first whole minute ≥ T_sign + 600 s. B/beacon_record_expedited.py:24,29–32,65–69 retains 600 and the identical ceiling formula. Only fallback waiting is shortened. Whether supplied T_sign is the real approval time is the separate C5 failure. |
| C3: preserve V15 and RETRY; prospective supersession | MET | V17:3,40 preserves both and says V15 remains operative until final-byte approval, with no identity built under V15 as signed. C/build_corpus_identity_v17.py:11 imports a separate variant. V15 and RETRY hashes match, as detailed below. Preservation is evidenced by artifacts and clauses, not a runtime guard. |
| C4: disclose expediting cost | MET | §3c, V17:40, explicitly discloses immediate fallback, unverified BLS, weaker relay provenance and signed-then-superseded V15 history. B/beacon_record_expedited.py:24,48–50,95–111; B/drand_round.py:18–28. The wording about the former 24 h opportunity needs the precision noted below. |
| C5: visibly prove approval before seed | NOT MET [FATAL] | §3b(1a), V17:32, claims “pushed BEFORE the seed round could exist.” C/approval_witness.py:29–45 establishes current history/ancestry and a caller-set committer date; lines 46–53 establish an earlier nonce value. Neither establishes a pre-pulse push. C/build_corpus_identity_v17.py:64 accepts this insufficient witness. Full counterexample below. |

1. [FATAL] Approval-witness acceptance does not establish prospective approval.

Reproduction through the actual V17 boundary AND full builder: claimed T_sign = 2026-09-06T02:30:07Z, derived T_pulse = 02:41:00Z. At actual wall time 02:59:23Z I created and pushed the approval in the temporary fixture repository, setting GIT_COMMITTER_DATE to 02:36:00Z. The record quoted the nonce for 02:29:30Z. The builder returned ACCEPT-DRAND, carried the approval witness and built 400/200/2,000 objects. The approval commit was a normal fast-forward addition; blocking force pushes would not block it. No production signature or beacon was forged: this is a control-flow counterexample under the supplied fixture's PKI, relay and remote substitutions.

An initial probe using the fixture's original future 03:11Z pulse correctly returned RETRY at the real clock. I then used the already-past 02:41Z test time above; the successful late-writer probe did not depend on advancing the verdict clock.

What each check proves, and what remains attested:

- W1, C/approval_witness.py:29–35: one add and no subsequent path touch in the history traversed from local HEAD; equality of committed and disk bytes. It does not date creation or independently identify Duho. History traversal is local, not an independent global registry.
- W2, lines 36–41: configured origin URL matches the literal, a fetch succeeds, and the commit is currently an ancestor of the remote ref. This proves present inclusion under the fixture/transport assumptions. It does not record when the remote first received the commit or itself query server protection settings.
- W3, lines 42–43: the encoded committer date is less than T_pulse. The disclosure that this date is operator-set is correct. Calling it proof of temporal order relative to the pulse is not. Git ancestry supplies graph order; a backdated field supplies no wall-clock upper bound.
- W4, lines 44–45: exactly one matching approval-record path occurs in reachable local --all history. The supplied second-path test is refused. This improves ordinary first-approval enforcement, but counts paths, not approval events; it does not authenticate the conversation, reject multiple approval statements within one blob, or establish that an unpublished earlier approval did not exist. The rule's first-approval-final covenant is explicit; the code's claim is narrower.
- W5, lines 46–53: a nonce round lies between MIN_T_SIGN and the seed round and its value agrees with live pinned relays. Assuming unpredictability and honest relay agreement, this supplies a lower bound on knowledge of that nonce. It supplies no upper bound on record creation or push. It also never checks “latest CLOSED ... at the moment of writing,” never compares R with T_sign, and uses the first matching nonce line rather than enforcing exactly one.

Attack outcomes: a late writer plus backdated commit PASSES, as executed. A visible second matching record path is REFUSED, as tested. A chosen old nonce PASSES: replacing the nonce with the round at MIN_T_SIGN = 02:20:00Z, despite claimed approval at 02:30:07Z, produced another full accepted build at 02:59:24Z. A genuinely precommitted, fixed round does not change merely because its build is delayed; however the missing upper-bound witness permits selecting an already-known round before filing the first record, and source timing remains an additional freedom below. Those observations refute the conjunction's “approval first, seed second” claim. Attribution of the actual approval, its actual UTC, timely push, latest-nonce selection and completeness of approval history remain attested.

2. Acceptance set and raising-fetch audit.

The production builder always supplies fetch, obtains one verdict and calls the witness before writing identity files: C/build_corpus_identity_v17.py:46–65,69–74. Within the beacon-value predicates, I found no accepted NIST seed without retained authentication and successful live equality, and no accepted drand seed without the prescribed retained/live quorum and round. B/beacon_record_expedited.py:75–93 compares all four NIST inputs; lines 97–111 recompute primary status and drand agreement. B/drand_round.py:20–28 counts only pinned URLs/distinct hostnames for the requested round. No BLS verification is claimed or performed.

Thus the source-byte union is enforced under the stated fetch/root assumptions. The FULL requested union, including a valid prospective approval witness, is not: the late approval above is accepted by the implemented witness predicate while violating the required chronology. Passing that predicate must not be equated with valid pre-pulse evidence.

Clock: schema, timestamps and statement bindings are checked first; line 74 then refuses before any beacon evidence is weighed. Approval-witness verification happens after the beacon verdict, but before output. The answer to “clock checked first?” is YES before source authentication, not before schema/binding validation or all file reads.

Required counterexamples, freshly reproduced against BOTH modules using collector-produced authentic retained NIST evidence:

| Probe | V15 B/beacon_record.py | V17 B/beacon_record_expedited.py |
|---|---|---|
| Build-time fetch raises OSError | ACCEPT-NIST, seed present | RETRY, seed absent |
| Verdict at T_pulse − 1 second, live fetch succeeds | ACCEPT-NIST, seed present | RETRY, seed absent |

V15 return precedes its clock guard at lines 77–80; V17 repairs are at 74,89–93,102–104. The warning-strict fixtures also execute both counterexamples.

[MAJOR] The broader “a live re-fetch that RAISES is RETRY” promise is still false. B/beacon_record_expedited.py:88 catches HTTPError separately, sets live_ok=False and continues; line 101 catches another HTTPError and treats it as a public primary failure. With retained authentic NIST evidence and pinned drand quorum, a callback raising HTTPError(404) or HTTPError(500) on NIST requests returns ACCEPT-DRAND. A full B17.build with HTTPError(500), relay responses and a machine-accepted witness returned True at 02:59:25Z.

Therefore: OSError/local generic exceptions are never a seed and are no longer counted as NIST failure; HTTPError IS counted as NIST failure and CAN yield a seed. The code's comment explicitly intends this distinction, but §3b(4), the outcomes paragraph (V17:32,35), the opening disclosure and change record promise no such exception. The handler also accepts an error from any step of nist_pulse.collect, including certificate/AIA/next-pulse acquisition (B/nist_pulse.py:53–62), not just an authenticated NIST response about the target pulse. An exception object alone does not prove a publicly observed NIST outage. This is a remaining acceptance-policy contradiction, not a claim that HTTP fallback escapes the narrower source-byte union defined above.

3. V16 repair audit, including its C-table.

| V16 finding | Status and V17 evidence |
|---|---|
| Item 1a: ACCEPT-NIST after raising live fetch | REPAIRED for the original ACCEPT-NIST counterexample: §3b(4) “requires ... EQUAL,” V17:32; B/beacon_record_expedited.py:83,88–93. NOT REPAIRED for the stronger all-raising-fetches-never-seed claim: HTTP branch at 88,101. |
| Item 1b: acceptance before clock | REPAIRED: “then the CLOCK,” V17:32; B/beacon_record_expedited.py:74; both-module reproduction above. |
| Item 1: generic local failure counted as primary failure on fallback | REPAIRED for generic exceptions: V17:32,35 and B/beacon_record_expedited.py:102–104. HTTP exception qualification remains missing. |
| Item 2 / C5: asserted chronology | NOT REPAIRED: “pushed BEFORE,” V17:32; C/approval_witness.py:39–53 fails the late/backdated probe. |
| Item 2: repeated approval targeting another round | ANSWERED in text: “FIRST APPROVAL IS FINAL,” V17:32. Ordinary second-path case REPAIRED by C/approval_witness.py:44–45 and its test. Actual first-event/time authentication remains NOT REPAIRED. |
| Item 2: delayed build/source selection and NIST recovery | ANSWERED after sealing: “does not reopen it,” §3c, V17:40. NOT REPAIRED as a witnessed first-source procedure before sealing: builder lines 67–74,118–130 have no first-collection/source lock. |
| Item 3: ten-minute cutoff overclaim | REPAIRED in operative §3b LIMIT (i): “at BUILD TIME ... not within a fixed window,” V17:38; source checks at B/beacon_record_expedited.py:97–100. |
| Item 3: contradictory clock/live-equality prose | REPAIRED for the original two cases; NOT REPAIRED for HTTPError, above. |
| Item 3: stale 24 h docs/comments | REPAIRED at B/beacon_record_expedited.py:13–16,95–96. New/current stale source-VOID docstring persists at 16–17, conflicting with §3c's sealed-identity finality. |
| Item 3: token coverage and shadowed exclusion; collector not separately tested | ANSWERED: token coverage remains; fixture test_collector_exclusion_exception_exercised now isolates the collector exclusion too. B/beacon_record_expedited.py:39–40,68–69. |
| Item 3: “both refuse” fixture only tests V16 | ANSWERED honestly in E3, V17:21: “exercised only the V16 builder.” Historical test retained; no false claim that both are exercised now. |
| Item 3: stale 18-test count/authorship wording | Count REPAIRED to 19 at V17:21,35. Authorship inconsistency NOT REPAIRED: E3 still says “AUTHORED BY THE CODEX SEAT” beside the builder description; §9, V17:67, retires earlier field validation. New code authorship is Hwao per this review brief. |
| Item 4: diff confinement | REPAIRED/CONFIRMED: supplied diffs exactly reproduce; protected substantive passages unchanged, detailed below. |
| Item 5: approval channel and byte identity | ANSWERED: §3b(1), V17:32, correctly limits Blanc's digest check to byte identity and leaves who spoke attested. Beacon binding at lines 71–73 checks byte/string correspondence, not personal identity. The stronger chronology claim later in the same paragraph is still false. |
| Prior C1/C2/C3/C4 | MET as specified in the C-table above; C5 remains NOT MET. |

The change record does not close every prior report concern. In particular, V16 item 6's production rule-digest binding remains unresolved; see execution prerequisites below.

4. Diff confinement and §3b consistency.

There are no document changes beyond the supplied V15→V17 diff. Changed V17 lines are 1,3,21,32,35,38,40 (inserted),52,59,70. E3 is one very long line, so the 19-line diff is not a small-word-count guarantee.

The operative sample sizes 400/200/2,000, floors 380/190/1,900, 0.70 bar, failed/dry-run exclusions, one validation attempt, one holdout, label/pixel boundaries, E5 custody, §7 branch-protection requirements and §6 pipeline text remain unchanged. Byte comparisons explicitly confirmed §§4–6, E5, the holdout paragraph and freeze-witness paragraph. The builder's ordering/renderability logic is unchanged; it now carries approval_witness metadata. Original V15 beacon and builder hashes still match.

Not every §3b sentence agrees with executed behavior: [FATAL] the claimed pre-seed witness; [MAJOR] unconditional raising-fetch RETRY; [MAJOR] latest-closed nonce enforcement; and [MINOR] generic “every public input ... equality” wording is broader than the drand test, which compares quorum randomness, not every relay body byte. §3b's detailed drand paragraph describes the actual quorum rule more accurately. Historical negative probes and observed-behavior artifacts are pinned V15 evidence, not independent coverage of the new witness.

[MINOR] E3's builder “8 changed lines” should be 10. The expedited docstring still calls itself V16 and “IDENTICAL ... except” without listing all V17 repairs, and its line 17 says any fallback identity is void on later authenticable NIST, contrary to §3c. §3c's ORDER sentence still attributes impossible preexisting-pulse use to MIN_T_SIGN/EXCLUDED_T_PULSE; those lower-bound checks cannot prove actual approval preceded a selected later pulse. Its historical statement that V15 “had 24 h” should mean a minimum fallback delay, not a hard NIST expiration: V15 still checked the primary at later build times.

5. [MAJOR] Source-decision procedure is partly fixed in text, incompletely witnessed in execution.

§3c, V17:40, says “built ONCE ... at the first collection ... whose verdict is ACCEPT-*,” followed by seal/witness, and explicitly closes reopening after sealing. That is a substantive repair. “First collection” is not independently scheduled or logged here: there is no mandatory predesignated collector/start receipt, full attempt log, or persisted first-ACCEPT lock in C/build_corpus_identity_v17.py:67–74,118–130. Its now defaults to build-time wall clock (55–61), and each call reevaluates current NIST.

Executed probe: with the SAME approval and T_pulse, a full build with unsigned NIST returned ACCEPT-DRAND; a subsequent full build with authenticable, live-equal NIST returned ACCEPT-NIST. Both returned True. First tuning objids differed: 587739861491974511 versus 588013383801110775. This used temporary outputs and simulated NIST recovery. It demonstrates the absence of builder state enforcing ONCE, not that a conforming operator may override the signed prohibition or that a sealed production identity was reopened.

After sealing, the no-reopen clause is clear. Before sealing, delaying or suppressing the first admissible collection can still choose between source states unless the collection chronology is independently witnessed. Reapproval is explicitly forbidden and ordinary second files are detected, but the approval witness cannot prevent choosing an already-known first round. The remaining “no lever” claim at V17:59 is consequently too strong.

6. Inherited V15 defect, preservation and unexecuted prerequisites.

The disclosure of the two V15 control-flow defects is accurate: B/beacon_record.py:75–80 accepts retained authentic NIST despite re-fetch exceptions and returns before its clock guard. The consequence “no identity will be built under V15 as signed” is the correct operational stop given the text/code disagreement. It is a prohibition, not a claim that the old builder technically cannot emit an identity; the counterexample proves that it can.

V15 SHA-256: fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1. Filed RETRY SHA-256: 1c1d9d4bacc35319e91d46420b8f892e1126cc48059ec69156a0a718428aeb4b. Both match V17:3 and the signature/run records. Re-evaluating retained RETRY evidence at its filed collection time with the pinned root returned RETRY, seed None, source None. This does not repeat the historical live verification. “Accepted nothing” is accurate; it does not imply that public beacon bytes were unknown.

- [MAJOR, carried from V16] E3, V17:21, promises production rule-digest equality “at adoption.” F/run_configurations.py:50,55 still initializes rule_sha256=None; line 142 only checks equality when it is non-None. No reviewed adoption mechanism is provided in this amendment. Changing the pinned driver later would require resolving its pin, not silently editing it.
- [MAJOR execution prerequisite] The run record's 11:24 entry identifies render-refused objects versus mandatory tensors and says a sentinel-tensor convention requires a clause in the next selection-rule version. V17 supplies no such clause. Its consequences for fixed-denominator unscored objects must be fixed before development, not improvised by an adapter.
- V17 approval, genuine pre-pulse witness, production beacon collection, identity seal and subsequent development remain future acts. Their ordinary prospective absence is not itself a defect; claiming that the present checks establish their chronology is.
- The §6 pipeline amendment and development manifest/fetch/render adapter remain separate execution prerequisites in the supplied run record. The seal helper is reported implemented but unused. This review does not approve V37 or authorize development.
- Custody/protection receipts were inspected as historical evidence. They record denied ordinary reads, developing-account admin membership, the home deny-delete ACL qualification, and a rejected non-fast-forward GitHub push. I did not repeat privileged operations, API state checks or remote pushes. They do not witness any future approval's push time.
- Guarded-pool re-derivation from the absent GZ1 table: UNVERIFIABLE HERE. The existing guarded_pool.csv hashes correctly and full builders reproduce the failed-set control; that is not reconstruction from the missing source table.
- Mocked PKI/relay tests establish program behavior, not future NIST repair, production signature validity or BLS security. No public-network query was needed to reproduce these local defects.

7. Still missing for approval — required clause substance.

These clauses require matching implementation, adversarial tests and updated pins before a successor is approved:

“Before T_pulse, an independent retained witness records receipt of the exact approval event, final rule digest, unique T_sign, derived T_pulse/seed round and approval-record digest/commit. Its receipt time is independently recorded and verifiably earlier than T_pulse; operator-set git dates and present-day ancestry are insufficient. The builder refuses without that evidence. Missing the deadline closes this commitment without redrawing. The first approval is final; later approval, retimestamping or replacement seed is prohibited and filed against the same commitment.”

“The approval record has a strict schema containing exactly one approval time and one nonce. The nonce is the specified latest available closed round at the independently witnessed recording event; verification checks its relationship to that event. Relay-confirmed historical randomness establishes only a lower time bound and is never represented as proof of a pre-seed push.”

“Any exception during build-time live NIST collection, including HTTPError from pulse, certificate, issuer or next-pulse acquisition, yields RETRY with no seed and cannot establish fallback eligibility.”

This last clause follows V17's stated universal promise. If HTTP responses are intentionally to authorize fallback, the successor must instead explicitly enumerate eligible response conditions and independently retained endpoint/status evidence, distinguish transport/local failures, and test them. The present blanket promise and exceptional code cannot both govern.

“The source-decision collection begins under the predesignated witnessed procedure at T_pulse. Every collection attempt and result is retained in order; the first admissible result is binding and locked before any further build. Failure to execute the procedure is filed and does not permit choosing a later source or round. A sealed identity is final; later NIST recovery never changes its seed.”

“Production execution fails closed without a reviewed adoption binding to the approved rule digest. Before any development pixel or label is opened, the pipeline amendment and adapter are approved, and the exact representation and journalling of render-refused objects are fixed; every such object remains in its prescribed denominator as unscored. No ad hoc tensor substitution is permitted.”

Reconcile the witness chronology, HTTP exception policy, source-VOID docstring, builder diff count and authorship wording with the implementation. Passing the existing suites alone does not repair the demonstrated counterexamples.

E3 hash inventory — all MATCH

Paths use the B/C/F abbreviations defined above. Every listed digest was computed from the local file; §3b's additional witness pin is reported separately above.

| File | SHA-256 |
|---|---|
| BEACON_V2_OBSERVED_BEHAVIOUR_20260906.md | c68d49e22427a328ce090b615c8bf715eb1e8f11b0bfdd503e18916dbbf7f858 |
| B/_digicert_intermediate.pem | 6601f41fceefbe7523a6a2e746938de57fc24e99426b7bea58d1867dbee1be5e |
| B/_sample_certificate.pem | c342339ca0fe5f1c522e03471b32811310371c3adbb8f107c8d77b5f336bfce9 |
| B/_sample_pulse_last.json | 08f07600adf6ae1d1655aac33f6976d48798a3de66153a4d92df78560ca828d9 |
| B/beacon_record.py | 023c4d7dfd18d2d6818ea09d41e78b44835dc95d20ff4ba69f36c0afd61bbb73 |
| B/beacon_record_expedited.py | dd52cbeb5e65c5cef995cd69bb92ecacbfc1e69f1a1aadde79e98576e6df133b |
| B/drand_round.py | 3403aee0d5d8c57ba0878bc5b716000faf93eab7a0fba0c7613613a501300882 |
| B/negative_probes.py | 839f6f54b165fb879fdf4f3699e425728737340c8662948c29ee79941d76dd0c |
| B/negative_probes_receipt.json | 53ff8213c34435c7c093324218597bbc9355ac68b0c42f02bd887c9efdb0fd22 |
| B/nist_pulse.py | c725dd6ab4830a2dc709e55195507c1739250851498f3384dfd10c8732b43cb9 |
| B/observed_behaviour.py | 0911dfb87778a54efc1bef552d50d0d4d8cf2ee6a50046a4070ddf05c5145be0 |
| B/pinned_root_DigiCertGlobalRootG2.pem | 5d550643b6400d4341550a9b14aedd0b4fac33ae5deb7d8247b6b4f799c13306 |
| B/test_beacon_record_expedited.py | c37fa6add3972a717e05db2fbe8b34df06f88d76d529f76e9ebd14e23460fae6 |
| B/test_beacon_v2.py | c8689eef76e8f035fed12d3f61c3ecd5c11eaa695b1e16b31c9f77e81ed83e38 |
| B/test_pki.py | a7a9c85347db34e20f207380972a72703e322bad6790672df02fb3114b682c47 |
| C/build_corpus_identity.py | 3090af770f0329beddb2d8b64acae6d4a1b1da06025e616b6fb145bff47ca46c |
| C/build_corpus_identity_v17.py | 61e80ff6847ce07f8d35c140019fd7e30f915ed1df73315948f926afd4f2534f |
| C/build_guarded_pool.py | e9b00ef4f50ce93c980cf6c5e0581276c46e6fa9a56ed46daa6d4eb95d2f52f3 |
| C/dryrun_identities_to_exclude_20260905.txt | 77b29eafe18e02d4dee621a6e748e8f698381c6e23098e7db2db190aee270c95 |
| C/guarded_pool.csv | 2cc94a29562270fcb5043f4ce942e303696f359b5fb0c59fdee48578ebb34155 |
| C/test_build_corpus_identity.py | 2cd65283a1e227cd0511f5c7fc1135ec0b365cb76a9608ed94e988ed3148440c |
| C/test_build_corpus_identity_v17.py | 18a9a3db88b6498335e6d27aadae23a4fe6a62be202f490cdf53fb5d7dd2dbe2 |
| F/env_lock.json | 4e2c851fe1f22f4bc28f121cf3ff4326f036be57fc100b34af9e5501d6c74251 |
| F/fourier_chirality.py | a026fe5fa168ca1eb2056829d86fb549dec4a61596b5d122f60c2a389e2d98a2 |
| F/run_configurations.py | d486ae58f40d220e8d2a9a1d875e008059cdc3bb1d9aee0dffc7dc974c7d53aa |
| F/test_fourier_chirality.py | c30b3af46b3a855c499469c4249e487a765c7015b46126291cc7a4c134072811 |
| F/test_run_configurations.py | 2fa83512b36788345541e84ff013c4f5ae3a9a9a5f0df0cbacc4b519945707f1 |
| F/w_chi_vendored.py | 89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75 |
| scratch/survey-bricks-dr9-north.fits.gz | 2edd5c295fdad26852c6f224a3ff023cff43dd0e03a53acd35b767e726ee72fb |
| validation_bricks/_bricks_without_r_coverage.txt | ba2eb9d16d0d1d47eef2e0d52497b56d44ac979ebe67dd54b33f57c117d7a2fe |

VERDICT: NOT-SIGNABLE

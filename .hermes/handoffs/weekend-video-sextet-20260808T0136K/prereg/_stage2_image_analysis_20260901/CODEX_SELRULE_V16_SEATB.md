ACCESS_SHA=fe1487bd1be7dcd3b27798727d2d39f2b5f54d21d74faffdaaaa9f059450f488

Seat B — independent review of V16 as a prospective sampling amendment.

AUTHORSHIP: The supplied record attributes earlier builder field-validation code (2026-09-06 00:13–00:18) to Codex and explicitly retires it from this acceptance path. All new V16 code is attributed to Hwao. I authored no reviewed implementation in this turn. The branch-protection execution receipt also credits Codex; I treat it as supplied evidence, not an independent repetition of that action. The findings below concern the current pinned code, not the retired validator.

Scope: V16 alone is judged. V15 and its records are used for preservation and comparison. No publication, production beacon collection, or study execution was performed.

Required checks

- Warning-strict beacon suites: test_beacon_record_expedited + test_beacon_v2 = 29 tests, OK (10 + 19).
- ResourceWarning-strict corpus suites: test_build_corpus_identity_v16 + test_build_corpus_identity = 7 tests, OK (3 + 4).
- Actual module diffs: 17 added/deleted lines for the beacon variant; 4 for the builder variant. The latter changes its docstring and import.
- signature_preimage.py prints fe1487bd1be7dcd3b27798727d2d39f2b5f54d21d74faffdaaaa9f059450f488.
- All 30 distinct full SHA-256 values in E3 match their corresponding local files. Inventory below.
- V15_TO_V16.diff is byte-identical to freshly generated normal diff output; 19 added/deleted document lines, comprising nine replacements and one insertion.
- Tests used PYTHONDONTWRITEBYTECODE=1. Additional probes used temporary output directories and the supplied test PKI; no reviewed source was edited.

The five hard constraints

| Constraint | Result | Clause and implementation evidence |
|---|---|---|
| C1: exclude the already-public pulse by name | MET | §3b(1a), line 32, names 2026-09-06T00:15:00Z, NIST 1928801 and drand 6440756. beacon_record_expedited.py:25,39,68 excludes that timestamp; drand_round.py:10 maps it to 6440756. The earlier MIN_T_SIGN refusal normally fires first. |
| C2: preserve the formula, use new approval time, refuse pre-draft time | MET, as the stated rule and timestamp arithmetic | §3b(1) defines T_sign as the new approval UTC. beacon_record_expedited.py:23–31 retains DELAY_S=600 and the identical minute-ceiling formula; lines 38,67 refuse T_sign before 02:20Z. This does not authenticate the supplied approval time; that separate failure is C5. |
| C3: preserve V15 and RETRY; supersede prospectively | MET | V16 lines 3,40 explicitly preserve history and leave V15 operative until approval. V15 hashes to fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1; RETRY evidence hashes to 1c1d9d4bacc35319e91d46420b8f892e1126cc48059ec69156a0a718428aeb4b. Both match the filed pins. The new builder imports the separate variant at line 11; neither original module is replaced. Preservation is an artifact/procedure property, not a runtime refusal. |
| C4: disclose the cost | MET | §3c, line 40, explicitly discloses immediate reliance on unverified-BLS relay agreement and the signed-then-superseded V15 history. Code: FALLBACK_AFTER_H=0 at line 23, collection at 47–49, fallback verdict at 91–105; drand_round.py:18–28 checks agreement, not BLS. Its ten-minute NIST-window description needs correction below. |
| C5: visibly establish actual approval before seed, beyond trust | NOT MET | §3b(1a) and §3c claim code-enforced chronology. Lines 37–41 and 64–72 check a caller-supplied timestamp and matching statement bytes; they do not verify when approval was actually recorded or whether it was the first approval. A fixed drafting lower bound proves neither. No pre-pulse approval-witness check appears in build_corpus_identity_v16.py:44–60. |

1. [FATAL] Acceptance set exceeds the stated live-equality condition.

There IS an accepted record outside the requested union: retained NIST evidence that authenticates, followed by a failed live re-fetch. beacon_record_expedited.py:86–88 catches HTTPError or another exception, then sets nist_ok from retained authentication alone; line 89 returns ACCEPT-NIST without successful live equality. The builder calls this function with live fetch at build_corpus_identity_v16.py:59 and accepts that result at line 60.

Reproduction: create the record using collect and the supplied three-tier test PKI; replace the build-time fetch callback with one raising OSError on every request. The actual validator returned ACCEPT-NIST with nist_live_error and no successful nist_live_equal. A full B16.build using the real local pool/exclusion/catalogue inputs and temporary outputs returned True.

This is a control-flow counterexample under the same test-root substitution used by the fixtures, not a claim that I forged a production DigiCert/NIST signature. It preserves retained authenticity but violates the mandatory additional live-equality condition. The defect is inherited from V15 and remains inside V16's pinned acceptance path.

A second probe returned ACCEPT-NIST with now = T_pulse minus one second: the NIST return at line 89 precedes the clock check at line 91. collect does refuse before T_pulse, but verdict does not universally do so. §3b's “before T_pulse → RETRY, never a seed” claim is therefore false as a function contract.

For drand, lines 99–105 enforce the computed round, retained quorum, live quorum and matching randomness. drand_round.py:20–28 counts only the four pinned URLs and distinct hostnames. NIST live authentication at lines 95–96 vetoes fallback. However, local fetch exceptions at lines 97–98 count as failure to authenticate; they do not establish a publicly witnessed NIST failure. No BLS verification occurs, as disclosed.

2. [MAJOR] Chronology and selection freedom are overstated.

For ONE genuine approval timestamp committed before its future pulse, timing approval cannot select a known favourable seed under the assumed beacon unpredictability. The unchanged formula does exclude inheritance of the old pulse.

But MIN_T_SIGN is only a fixed lower bound. A record claiming approval at 03:00:07Z, supplied and collected a day later, passed the actual builder boundary with ACCEPT-DRAND. That is legitimate if approval really occurred then; the identical code path also accepts a newly written statement claiming that time. The code cannot distinguish them. This demonstrates the missing chronology input, not an accusation that a real approval was forged.

V16 also lacks an explicit first-approval-is-final rule forbidding replacement approvals after seeing a seed. §4's one validation attempt and §7's one holdout do not close repeated approval/seed selection before those stages. Reapproval with a new T_sign can target successive future rounds; choosing among their observed results is not mechanically prevented.

Later collection of the SAME fixed drand round does not itself change its randomness. The probe confirmed this with the same retained/live value a day later. This does not mean collection timing changes nothing overall: NIST availability/authentication is evaluated at build time, and can change which source is admissible. Local network failures can also make an otherwise available primary invisible. V16 needs a fixed, witnessed source-decision procedure and explicit handling of subsequent NIST recovery, rather than an unqualified no-choice claim.

3. [MAJOR/MINOR] Behavioral delta is confined, but prose and test claims need precision.

Yes: the substantive beacon delta is FALLBACK_AFTER_H 24 → 0 plus the two timestamp refusals. The builder's only executable delta is the import. Other changes are explanatory text and the RETRY reason string.

A literal search for “24 h” finds V16 lines 3,40,59; these are historical/comparative references, not a leftover operative 24-hour wait in §3b. Nevertheless, not every fallback-related sentence agrees with execution:

- [MAJOR] §3b/§3c lines 38,40 describe NIST as having only the ten minutes before T_pulse. Code permits an arbitrarily delayed build and checks NIST then; it does not impose that cutoff.
- [MAJOR] §3b line 32 requires live equality universally, and line 35 promises RETRY before the pulse. The two executed counterexamples above contradict those sentences.
- [MINOR] The expedited module retains old “before/from T_pulse + 24 h” documentation at lines 13–15 and a stale comment at 92.
- [MINOR] The expedited test_zzz_every_token_is_exercised DOES include both new verdict tokens (test_beacon_record_expedited.py:76–79). The old test_beacon_v2 checker scans only beacon_record.py. To exercise T-PULSE-EXCLUDED, the new test temporarily lowers MIN_T_SIGN at lines 57–61; this is disclosed isolation of a normally shadowed branch, not a production-reachable second refusal for the old pulse. The collector exclusion exception itself is not separately exercised.
- [MINOR] The new builder test named test_both_refuse_old_t_sign actually invokes only B16 for that case (lines 22–26). E3's “both refuse” fixture description is unsupported.
- [MINOR] E3 retains stale 18-test and old authorship wording alongside its newer 19-test and retired-authorship declarations. Token coverage is not acceptance-path completeness, as the passing suites and failing added probes demonstrate.

4. DIFF CONFINEMENT: passed.

There are no changes beyond the disclosed 19 added/deleted document lines. V16 changes lines 1,3,21,32,35,38,40,52,59,70. Line 21 is a long E3 paragraph carrying the new pins and fixture descriptions; “19 lines” does not mean 19 small sentences.

The substantive sample sizes, floors, 0.70 threshold, exclusion rule, one-attempt holdout, label/pixel boundaries, custody, branch-protection rules and §6 pipeline requirements remain byte-identical in their operative passages. The builder command and the source-choice explanation in §7 change as disclosed. This successful confinement does not cure inherited acceptance defects.

5. Approval channel: described correctly, with a limited proof.

§3b(1), line 32, agrees with the supplied change record: exact bytes and digest presented in the Codex conversation; Duho approves there; Codex attests; Blanc recomputes the on-disk digest. It correctly says Blanc's check establishes byte identity and does not establish who spoke. This review has no independent record of a future V16 approval.

The limitation is properly stated there but contradicted by the stronger “enforced in code” chronology claim in (1a). Byte equality establishes chronology only when accompanied by an independently retained, pre-pulse approval event.

6. Aspirational or unexecuted items.

- V16 is still a draft: actual approval, pre-pulse approval evidence, new pulse collection, corpus freeze and witnessed execution remain future acts. Their absence alone is normal for prospective approval.
- [MAJOR execution prerequisite] The pinned driver still has Protocol.rule_sha256=None (run_configurations.py:50,55); its equality check is conditional at line 142. E3 says this is pinned “at adoption,” but the current production default does not enforce it. A reviewed adoption mechanism must bind the final digest without silently changing a pinned driver.
- The run record explicitly leaves the §6 pipeline amendment and development fetch/render adapter pending; the seal helper is reported implemented but not used. These are later execution gates, not evidence of completed development.
- Custody and branch-protection receipts were inspected as historical evidence, not re-executed. No protection settings were changed and no push was attempted.
- Guarded-pool re-derivation from THE GZ1 table: UNVERIFIABLE HERE. Hashing guarded_pool.csv and exercising the identity builder do not reconstruct its absent source table.
- No live NIST certificate repair, production NIST authentication, or future beacon behavior is established by the test PKI.

What is still missing for approval — proposed clause text

The following substance must be integrated, implemented where enforcement is claimed, tested and repinned before approving a successor:

“ACCEPT-NIST requires retained authentication AND a successful build-time live collection whose pulse, leaf, intermediate sequence and next-body bytes all equal the retained inputs. Any live collection error is non-acceptance. Before T_pulse every verdict is non-acceptance, irrespective of source.”

“The first valid approval of the final amendment fixes T_sign permanently. Before T_pulse, retain the actual Codex-conversation approval event, its independently recorded UTC, final rule digest and derived pulse/round in a non-rewritable witness available to the referee. The collector and builder must bind to that witnessed event; a caller-created statement or fixed drafting-time lower bound is insufficient. Reapproval, retimestamping or a new pulse to replace an observed seed is prohibited; inability or refusal to proceed is filed against the same commitment.”

“The initial source decision is made by the predesignated witnessed collection beginning at T_pulse, with every attempt and failure retained. Operator-selected local network failure is not sufficient evidence to bypass the primary. Subsequent collection cannot select another round or substitute a source opportunistically. Authenticable NIST recovery is binding as specified; any consequent fallback invalidation is filed and stops further execution pending the stated rule, never a new seed draw.”

“Before production use, a reviewed adoption configuration binds the approved rule digest and fails closed when that binding is absent. No development pixel or label is opened until the existing pipeline-amendment, adapter and freeze prerequisites are satisfied.”

Correct the ten-minute cutoff claim to distinguish earliest fallback eligibility from actual build-time NIST authentication, and reconcile the identified fixture/documentation claims. The blockers require code and evidence changes; adding prose alone cannot make these exact pinned bytes conform.

E3 hash inventory — all MATCH

Paths below are relative to the review directory. Each named file was hashed; all 30 distinct E3 digests matched. To avoid duplicating long paths, B = _optionA_dev/beacon_v2/, C = _optionA_dev/corpus_identity/, F = _optionA_dev/fourier_chirality/.

| File | SHA-256 |
|---|---|
| F/fourier_chirality.py | a026fe5fa168ca1eb2056829d86fb549dec4a61596b5d122f60c2a389e2d98a2 |
| F/run_configurations.py | d486ae58f40d220e8d2a9a1d875e008059cdc3bb1d9aee0dffc7dc974c7d53aa |
| F/env_lock.json | 4e2c851fe1f22f4bc28f121cf3ff4326f036be57fc100b34af9e5501d6c74251 |
| F/test_fourier_chirality.py | c30b3af46b3a855c499469c4249e487a765c7015b46126291cc7a4c134072811 |
| F/test_run_configurations.py | 2fa83512b36788345541e84ff013c4f5ae3a9a9a5f0df0cbacc4b519945707f1 |
| F/w_chi_vendored.py | 89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75 |
| C/build_guarded_pool.py | e9b00ef4f50ce93c980cf6c5e0581276c46e6fa9a56ed46daa6d4eb95d2f52f3 |
| C/build_corpus_identity.py | 3090af770f0329beddb2d8b64acae6d4a1b1da06025e616b6fb145bff47ca46c |
| C/build_corpus_identity_v16.py | 4d9cc7a79c956a3ef61b67d25d57e1be624bab0d5a66cf3350ddeac7947b0ca2 |
| C/test_build_corpus_identity.py | 2cd65283a1e227cd0511f5c7fc1135ec0b365cb76a9608ed94e988ed3148440c |
| C/test_build_corpus_identity_v16.py | 30483e2a3035242e10f786e1ab1e3edc10a847d1fd42c50b9a622467c7560dca |
| C/guarded_pool.csv | 2cc94a29562270fcb5043f4ce942e303696f359b5fb0c59fdee48578ebb34155 |
| C/dryrun_identities_to_exclude_20260905.txt | 77b29eafe18e02d4dee621a6e748e8f698381c6e23098e7db2db190aee270c95 |
| B/beacon_record.py | 023c4d7dfd18d2d6818ea09d41e78b44835dc95d20ff4ba69f36c0afd61bbb73 |
| B/beacon_record_expedited.py | f420521a838412b64e61ffc2204b68a3edb017101713e38a3fc201ab530b8fc7 |
| B/test_beacon_record_expedited.py | 76a98873188612771fb0c9376997f34aa1822638344bcef1e777239e70b8f3ac |
| B/nist_pulse.py | c725dd6ab4830a2dc709e55195507c1739250851498f3384dfd10c8732b43cb9 |
| B/drand_round.py | 3403aee0d5d8c57ba0878bc5b716000faf93eab7a0fba0c7613613a501300882 |
| B/pinned_root_DigiCertGlobalRootG2.pem | 5d550643b6400d4341550a9b14aedd0b4fac33ae5deb7d8247b6b4f799c13306 |
| B/test_beacon_v2.py | c8689eef76e8f035fed12d3f61c3ecd5c11eaa695b1e16b31c9f77e81ed83e38 |
| B/test_pki.py | a7a9c85347db34e20f207380972a72703e322bad6790672df02fb3114b682c47 |
| B/negative_probes.py | 839f6f54b165fb879fdf4f3699e425728737340c8662948c29ee79941d76dd0c |
| B/negative_probes_receipt.json | 53ff8213c34435c7c093324218597bbc9355ac68b0c42f02bd887c9efdb0fd22 |
| B/observed_behaviour.py | 0911dfb87778a54efc1bef552d50d0d4d8cf2ee6a50046a4070ddf05c5145be0 |
| B/_sample_pulse_last.json | 08f07600adf6ae1d1655aac33f6976d48798a3de66153a4d92df78560ca828d9 |
| B/_sample_certificate.pem | c342339ca0fe5f1c522e03471b32811310371c3adbb8f107c8d77b5f336bfce9 |
| B/_digicert_intermediate.pem | 6601f41fceefbe7523a6a2e746938de57fc24e99426b7bea58d1867dbee1be5e |
| scratch/survey-bricks-dr9-north.fits.gz | 2edd5c295fdad26852c6f224a3ff023cff43dd0e03a53acd35b767e726ee72fb |
| validation_bricks/_bricks_without_r_coverage.txt | ba2eb9d16d0d1d47eef2e0d52497b56d44ac979ebe67dd54b33f57c117d7a2fe |
| BEACON_V2_OBSERVED_BEHAVIOUR_20260906.md | c68d49e22427a328ce090b615c8bf715eb1e8f11b0bfdd503e18916dbbf7f858 |

VERDICT: NOT-SIGNABLE

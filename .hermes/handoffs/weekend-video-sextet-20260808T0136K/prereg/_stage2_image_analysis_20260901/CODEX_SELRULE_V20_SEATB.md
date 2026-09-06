ACCESS_SHA=1c8ce522ac07572f22858f2ec6980b6a436f2e4ba580f7b6351ca2e8acee77d1

Seat B — independent referee of the access-proved V20 only.

AUTHORSHIP: The supplied history attributes earlier builder field-validation code (2026-09-06 00:13–00:18) and branch-protection work to Codex. That validation boundary is retired. All new reviewed implementation is attributed to Hwao; I authored none of it. Findings concerning builder/driver integration touch inherited Codex-associated machinery and are marked by those references below. My additional probes were referee code executed from stdin, with temporary repositories outside this directory. No implementation was edited and nothing was published.

Reference notation: V20:N means line N of the target. VD = `_optionA_dev/drand_only/verify_drand.py`; BD = `_optionA_dev/beacon_v2/beacon_record_drand.py`; B = `_optionA_dev/corpus_identity/build_corpus_identity_v20.py`; AW = `_optionA_dev/corpus_identity/approval_witness_v3.py`; DR = `_optionA_dev/beacon_v2/drand_round.py`; D = `_optionA_dev/fourier_chirality/run_configurations_v4.py`; TF = its `test_run_configurations_v4.py`. References identify the inspected, hash-matching files.

**The property, judged first.**

Removing NIST removes the demonstrated V19 source-selection lever. For the honest pinned drand chain, assuming BLS security, an authentic key, correct verification and no threshold compromise, I found no way for a relay, the lane operator or first-collection timing to produce a DIFFERENT accepted seed for the SAME actual round. Unavailability does not reveal another source. The real signature verifies, and altered-message/key controls fail. This is a substantive design improvement.

That conclusion does not establish V20's unconditional wording or its approval/identity enforcement. V20:32 calls the seed the signature, whereas VD:50–55 and BD:89 return SHA256(signature), a 32-byte randomness value rather than the 96-byte signature. BLS uniqueness is for a fixed MESSAGE and key. Here the message includes a response-supplied previous_signature (VD:39–51); checking its connection to a predecessor is optional and unused (VD:58–60). The honest-chain assumption fixes that predecessor. A compromised signing threshold can sign alternate predecessor messages or compute future signatures early. A schedule is not a cryptographic barrier. The claim “cannot exist before” must explicitly be conditional on the threshold assumptions. This distinction follows the drand description of message/key determinism and chained rounds. [drand cryptography](https://docs.drand.love/docs/cryptography/), [protocol specification](https://docs.drand.love/docs/specification/).

The hypothetical approval calculation is correct: 2026-09-07T01:00:07Z maps to T_pulse 01:11:00Z and round 6443748. Its scheduled time is later than approval. That is an arithmetic demonstration, not evidence that an actual V20 approval occurred or proof against early threshold cooperation. No actual V20 approval was established here.

[MAJOR] The property exhibit confuses signature uniqueness with HTTP-body uniqueness. Its case C adds `extra: 1` to the SAME signed response (`exhibit_property_v20.py`:35). That is entirely possible and still has the same signature and seed. Independently, reformatting the original JSON alone verified successfully but produced REFUSE-LIVE-DIFFERS-BUT-VERIFIES at BD:82–84. The exhibit reproduces a false “impossible” explanation; it does not exhibit two different valid signatures. First-collection timing can affect acceptance/refusal through representation changes, although this is not a demonstrated different-seed lever. V20:32–33 must distinguish these properties.

[MAJOR] Chain binding is partly real, partly overstated. The collector constructs exact qualified URLs (VD:26; BD:29–34), the record pins chain hash and public key (BD:62), and BLS checks the pinned key. The ordinary unqualified URL is refused. But VD:45 accepts source_url=None, accepts `https://api.drand.sh.attacker.invalid/<pinned-chain>/public/6441924`, and accepts a suffix after the round path; I executed all three. It uses string prefix/substring tests, not exact URL membership. BD:48–57 counts accepted URL strings rather than distinct exact pinned relays. Builder live confirmation narrows this because BD:78 fetches canonical URLs; offline verification does not. No signature forgery or alternative seed follows merely from these URL defects, but the stated accepted-relay predicate is not exact.

L1–L5 are not complete and fully honest as written. L1 must qualify timing and predecessor-message assumptions, not merely say “bias”; L2 correctly identifies key authenticity; L3 correctly identifies quorum availability but omits harmless representation refusal; L4 identifies py_ecc but a version pin and requirements-file digest do not hash-lock its installed transitive implementation; L5's “visible” abandonment relies on external records and an authenticated history that this implementation does not supply. GitHub/HTTPS, retained-event authenticity, the unauthenticated W5 nonce path and human attestation remain material trust boundaries. V20:33 does disclose retained GitHub evidence, but points to “limit L3,” now the relay-availability limit.

**Five hard constraints.**

| Constraint | Call | Clause and executable evidence |
|---|---|---|
| C1: exclude public 00:15Z and exhibit rounds by name | MET | V20:32–33; BD:20–21,39–40,65–67 explicitly exclude 6440756 and 6441924. Fixture-only lifting is disclosed. |
| C2: same formula from new approval, no inherited round | MET for the prescribed sampling formula | V20:33; VD:28–37 and BD:38,63–67 rederive the round from supplied T_sign. The separate failure to bind that supplied time to verified approval is C5/M1 below. |
| C3: V15/RETRY preserved; prospective supersession | MET | V20:3,38; original V15 and RETRY hashes match, signature record retains 00:04:07Z. V20 remains draft and says V15 remains operative until final-byte approval. The old files remain available; BD:19–21 excludes their pulse from V20. |
| C4: cost and residual trust stated | NOT MET as coherent final clause text | V20:3,32 says drand-only and actual BLS verification, but V20:38 still says V17 tries NIST, this lane cannot verify BLS, and provenance rests on relay agreement. BD:59–89 and VD:51 contradict that operative cost paragraph. |
| C5: W3/W5 approval before seed, collection timing irrelevant to value | NOT MET | V20:33,38; AW:44–93 retains/matches events but retains V19 gaps. D:178–204 never establishes the claimed approval conjunction; production has no re-deriver. W5 uses DR:8,18–28, which neither verifies BLS nor binds the chain path. The conditional same-round seed property does not bind a forged identity's round to approval. |

**[FATAL] The pinned production driver is not executable as the promised selection path.**

D:80 initializes rederive_seed=None; D:81 constructs PRODUCTION with that value. D:169 unconditionally refuses it with PROTOCOL-NO-REDERIVER. D:337–348 supplies no production callback, and tune/holdout use that default protocol. Adoption changes a digest file, not this callback. Consequently an otherwise sealed, valid production identity cannot reach selection. I confirmed the production value is None and executed the refusal after passing the preceding identity/witness checks in a temporary clone. The locked E2 environment itself passes.

The 20-test V4 suite does not catch this: TF:20 injects a function that merely reads a stored seed_hex, and the E2E test injects a separate offline BD.verdict callback at TF:186–187. The production connection and its evidence bindings are absent from the pinned bytes. This must be implemented, tested without callback substitution through the production entry point, and repinned before approval. It is not an ordinary post-approval artifact.

**[MAJOR] Acceptance-set audit: M1 is still not repaired.**

Precisely: I did NOT obtain an accepted identity through the unchanged production CLI; its acceptance set is empty because of the fatal above. I DID execute an acceptance counterexample through unchanged D.load_identity with a test protocol supplying real BLS re-derivation. This isolates the additional gaps that simply wiring the callback would leave.

I read public round 6441926 from the two chain-qualified api.drand.sh and api2.drand.sh endpoints. Both bodies had SHA256 `06b1689ed520e10599dd3bf3081aeffc2bbdcb56eb4911d2791cfe127b74a9d9`, both BLS-verified, and the record's actual T_pulse was 2026-09-06T10:00:00Z. This round is not either excluded round. The test used a temporary local repository and bare remote, real git commits/fetch/witness checks, and production cardinalities 400/200/2,000. The protocol redirected fixture paths/remote and supplied an offline callback that ran the actual BD.verdict and required ACCEPT-DRAND; it did not inject the seed directly or disable BLS/exclusions.

The sealed identity loaded successfully with ALL these defects together:

- No APPROVAL_RECORD file at all; only the adoption file was committed at the purported approval commit.
- A fabricated PushEvent with created_at 2098-12-31T23:55:00Z and a fabricated identity T_pulse of 2099-01-01T00:00:00Z, unrelated to the real 2026 record.
- nonce_round=-1, nonce_randomness all zeroes, and an incorrect all-zero push_event_sha256.
- A reset three-entry history, claiming entries=999: an invented stage, a matching builder-accept, and another builder-accept with a conflicting seed but no builder-conflict label.
- A retained beacon record absent from the freeze commit, and no live re-fetch in the callback.

Observed: CONDITIONAL_REAL_BLS_LOAD_ACCEPTED 400 200 2000; NO_APPROVAL_RECORD=True; LOG_ACTUAL=3; LOG_CLAIM=999; UNFLAGGED_CONFLICT=True; RECORD_NOT_COMMITTED=True. With the same setup and rederive_seed=None, the result was PROTOCOL-NO-REDERIVER.

Why it passes: D:180–184 checks event shape, a lexical time comparison, claimed commit inclusion and nonce types. It does not read the approval record, check W1/W4, verify the nonce's value/range, verify the event digest/provenance or obtain the earliest authentic server event. D:189–195 checks a first labelled builder-accept and absence of a builder-conflict label, but not count, chronology, valid stages or semantic conflicts. D:201–204 hashes the record and compares only the returned seed; it neither commits the record nor compares its rule/statement/time/round to the identity. The callback contract returns only a seed. Live quorum is optional in BD:77 and absent from the exhibited driver re-derivation.

The builder's adoption-at-approval check and D:196–200's exact adoption bytes are real repairs. They do not authenticate the missing approval record. A hash-matching, newly sealed operator-authored document is not evidence that the builder's acceptance conjunction ever ran. These findings concern the V20 driver/builder integration, including inherited Codex-associated machinery.

**[MAJOR] History audit: M2 is still not repaired.**

The collector now requires --log and catches many file/JSON errors; B:53–59 logs initial file/digest/statement failures, and B:70–81 logs ordinary verdicts and SystemExit witness/adoption refusals. Those are useful partial repairs.

It remains an unauthenticated append-mode file (B:86–90), with no anchored initial head, authenticated predecessor, sequence validation or atomic first-accept transaction. B:107–116 reads then appends without a lock; the computed `first` at B:108 is unused. Only builder-accept entries bind; collector accepts and earlier accepted verdicts followed by witness refusal still do not. Deleting the log resets the first-accept state. I executed a first lock, deleted the temporary log, then locked different record bytes successfully. D's checks authenticate the currently sealed bytes, not completeness before that seal.

“Every path” is also false. I passed retained valid evidence to B._validate_beacon_record while live fetch returned b'{'. BD:83 raised JSONDecodeError before B:70 logs a verdict; the temporary collection log did not exist afterwards. VD:46 similarly converts round outside its exception handler. B:67's verdict call has no encompassing error-log handler; B:76–81 catches SystemExit only. CLI argument parsing precedes logging setup (BD:98; B:183), and some missing-argument/build failures are outside the logged boundary. Full history requires more than the tested pre-parse cases.

These are auditability and implementation failures. With an honestly fixed drand round they do not themselves demonstrate a different cryptographic seed, but V20 explicitly retains complete history as part of admissibility.

**[MAJOR] W3/W5 and chronology remain weaker than claimed.**

AW:44–53 chooses the earliest event among head/commits matches and AW:91 retains the entire supplied event and retrieval provenance. That is real. It does not recognize an approval commit delivered as a non-head ancestor when the event lacks a commits array; no before..head ancestry test was added. Current GitHub documentation shows such head/before payloads and confirms the 300-event/30-day window and 30-second-to-six-hour latency. [GitHub Events API](https://docs.github.com/en/rest/activity/events?apiVersion=2026-03-10).

AW:79 describes PENDING/CLOSED in an error message; it does not persist a deadline or closed state. AW:86–90 still allows round_for(T_sign)-1 and never enforces the nonce scheduled-time >= MIN_T_SIGN assertion in V20:33. Its docstring's “after T_sign − 30 s” is false when the predecessor is allowed at an interior second: the scheduled lower bound can be almost 60 seconds earlier. The text now explicitly states the two-round set, but that does not repair the contradictory bound or implementation.

W5 still calls the old DR collector with unqualified paths and checks only round/randomness agreement. The V4 E2E fixture itself serves nonce signature='00' and arbitrary repeated randomness (TF:168–180) and passes the builder. BLS verification of the later study seed does not authenticate this earlier nonce. After the GitHub window, a retained unsigned event requires trusted custody/attestation; its hash proves byte integrity relative to an anchor, not GitHub authorship. D does not even check that hash. No live V20 approval event was available or claimed in this review.

**Repair audit of every in-scope triage item.**

“NOT REPAIRED” includes partial work that fails the stated repair. Triage identifiers are those in V19_REPORT_AUDIT_TRIAGE_20260906.md, including aliases.

| Item | Disposition | Clause and code evidence |
|---|---|---|
| A/M1; B 1/M1; 4-adopt | NOT REPAIRED overall | V20:21,38; D:169,178–204. Exact adoption bytes/blob check repaired, full witness/record conjunction not. |
| A/M2; B 2/M2; 4-log | NOT REPAIRED | V20:38; B:53–116; D:189–195. More logging and parsing, no complete authenticated history or atomic lock. |
| P, in-scope withdrawal; P-L5 | ANSWERED for source choice; overstatement remains | V20:32,35; BD:59–89 removes NIST. Fixed-round conditional value independence is supported; absolute timing and visibility claims are not. |
| P-L2, wording; newly authorized drand design | NOT REPAIRED in full | V20:32–33; VD:45–51 verifies BLS but URL matching is permissive; AW:89 still uses unbound/unverified DR. |
| P-L3 | ANSWERED, with stale cross-reference | V20:33; AW:32–42,91 retains event/provenance and names window; “L3” now means another limit. D does not authenticate the receipt. |
| P-L4 | NOT REPAIRED in full | V20:32–33; BD:76,88 does RETRY for quorum loss, but representation changes refuse and malformed live JSON can escape. |
| P-X | NOT REPAIRED in full | V20:32; property exhibit:25–43 now exercises real first collections, but case C labels harmless extra JSON impossible. |
| C5-W5; 4-nonce | NOT REPAIRED | V20:33; AW:7–12,86–90 retains predecessor/incorrect lower-bound docstring and omits nonce-time minimum. |
| C5-match | NOT REPAIRED | V20:33; AW:44–53 and D:182–183 still lack before..head ancestry membership. |
| C5-state | NOT REPAIRED | V20:33; AW:79–81 provides refusal prose, no persisted deadline state or clear covenant label in the rule. |
| 1b | ANSWERED by authorized source removal | V20:33,35; BD:59–89 no NIST aggregate-authentication predicate. |
| 4-RETRY | REPAIRED for the specific NIST mismatch | V20:33 replaces the old different-NIST-pulse example; BD has no NIST input. New drand representation wording has its own defect above. |
| 4-inherited-examples | REPAIRED in §3b | V20:32–36 removes unsigned/wrong-certificate observations as current seed behavior; VD/BD execute new controls. Stale NIST cost text persists elsewhere. |
| 4-labels | NOT REPAIRED | V20:38 still labels §3c V16, discusses V17 and unverified BLS; V20:64–66 remains the historical V15 checklist. |
| 4-sentinel | NOT REPAIRED | V20:52; D:230–245 counts sentinel and UNSCORED, TF:226–233 has no adapter refusal-cause/identity reconciliation. |
| 4-warnings | NOT REPAIRED | TF:231,233 leak file handles under the requested warning-strict run. |
| 5-once, new wording portion | NOT REPAIRED | V20:38 still says NIST tried once; BD never consults NIST. The inherited one-holdout covenant is not changed. |
| 5-lock-vs-freeze | ANSWERED narrowly | V20:38,50 distinguish first builder-accept from later identity freeze; B:82 locks before B:125–180 builds outputs. Successful freeze is not guaranteed by that lock. |
| 5-frag | NOT REPAIRED | V20:21 retains “3 tests ... plus ... 2 tests” after the inherited builder's correct four-test count. |
| 6-rule | NOT REPAIRED overall | V20:32–38,52; authorized source removal helps, but M1/M2, W5 and adapter requirements remain. |

Out-of-scope inherited findings were not silently repaired: signed V15 and its old driver/beacon files retain their pins and behavior, including the original NIST first-collection/fetch/clock defects, unverified/unbound drand fallback, repeatable holdout invocation, E1's false ten-test count, and the historical metadata wording. The new drand verifier/source removal is an expressly recorded design supersession, not a rewrite of V15. P-L1's NIST/AIA issue becomes irrelevant to V20 seed selection for that authorized reason. Triage “3” is verification evidence, not a repair; “agy” is recorded history, not an independent completeness proof. V39 approval is not reopened.

**Execution, counts, pins and confinement.**

All commands used PYTHONDONTWRITEBYTECODE=1 to avoid cache writes. Required drand/beacon/builder suites used the supplied venv. Driver suites used /usr/bin/python3 with the supplied venv site-packages on PYTHONPATH and the requested ResourceWarning policy.

| Required run | Observed |
|---|---|
| test_verify_drand, -W error | 4 tests, OK |
| test_beacon_record_drand, -W error | 6 tests, OK |
| test_build_corpus_identity_v20 + test_approval_witness_v3 + test_build_corpus_identity | 6 + 9 + 4 = 19 tests, OK |
| test_run_configurations_v4 + test_run_configurations | 20 + 17 = 37 tests, OK; warnings below |
| exhibit_drand_only.py | EXHIBIT OK: True; digest 45d6149a2ccf30cb167dc4331455f3403a733516a82399292b1e7ad2c029e531 |
| exhibit_property_v20.py, twice | Both EXHIBIT OK: True; both digest b3754acaaf3d5ffaac76800bcdffce19168d405475b7a977f011b767a2dddd1f |
| signature_preimage.py V20 | 1c8ce522ac07572f22858f2ec6980b6a436f2e4ba580f7b6351ca2e8acee77d1 |

Total requested unit tests: 66; none skipped in the observed aggregate outputs. Exit status was zero for all suites. That does NOT mean warning-clean: TF:231 and 233 emitted unclosed-file ResourceWarnings as “Exception ignored in,” and the sentinel calculation emitted a RuntimeWarning at fourier_chirality.py:87. The unit-test runner still printed OK. The advertised new counts are correct; E1's inherited ten-test claim and E3's obsolete fragment are not.

I independently reconstructed the round-6441924 message, decoded G1/G2, checked prime-order subgroup membership, hashed to G2 with the specified DST, and evaluated the pairing equation directly. It passed; an altered message and doubled public key failed. This used py_ecc's low-level primitives, NOT VD.verify or G2Basic.Verify, but it is NOT an independent cryptographic implementation. The signature hash was `68547455ba7d5000cb4b0b7fcd48c1ab36b6881d55e3ef464989659833ef3834`. Both retained relay files are byte-identical with SHA256 `b5eb42187ba330220362a10c6c018d938ecd279baa7b3b2ea24f51ca2b5393cd`.

Every one of the 37 distinct E3 digests matched a file, including retained superseded versions. Inventory, grouped by directory:

- Fourier (10): fourier_chirality.py; run_configurations.py; run_configurations_v3.py; run_configurations_v4.py; test_fourier_chirality.py; test_run_configurations.py; test_run_configurations_v3.py; test_run_configurations_v4.py; env_lock.json; w_chi_vendored.py.
- Corpus (9): build_guarded_pool.py; build_corpus_identity.py; build_corpus_identity_v19.py; build_corpus_identity_v20.py; test_build_corpus_identity.py; test_build_corpus_identity_v19.py; test_build_corpus_identity_v20.py; guarded_pool.csv; dryrun_identities_to_exclude_20260905.txt.
- Beacon v2 (15): drand_round.py; beacon_record_expedited.py; beacon_record_drand.py; test_beacon_record_expedited.py; test_beacon_record_drand.py; nist_pulse.py; pinned_root_DigiCertGlobalRootG2.pem; test_beacon_v2.py; test_pki.py; negative_probes.py; negative_probes_receipt.json; observed_behaviour.py; _sample_pulse_last.json; _sample_certificate.pem; _digicert_intermediate.pem.
- Other (3): scratch/survey-bricks-dr9-north.fits.gz; validation_bricks/_bricks_without_r_coverage.txt; BEACON_V2_OBSERVED_BEHAVIOUR_20260906.md.

Eight additional §3b pins also matched: VD, test_verify_drand.py, exhibit_drand_only.py, chain_info_8990e7a9.json, requirements_bls.txt, exhibit_property_v20.py, AW and test_approval_witness_v3.py. Exhibit-output digests above are the generator payload digests, not hashes of the surrounding Markdown wrappers.

Both filed diffs reproduced exactly with `diff`. V15_TO_V20.diff hashes to `3ed26fa75e37badad0b9a16422aa2f4132ee6f3459fd7180610e51d9a50994cd`; V19_TO_V20.diff to `bf121a975f2541ca4ad443cd38a0df46a9eddcb70aa5adffc392429e950cf0be`. V15 hashes to `fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1`; the retained RETRY record hashes to `1c1d9d4bacc35319e91d46420b8f892e1126cc48059ec69156a0a718428aeb4b`.

V15→V20 changes are confined to heading/introduction, E3, §3b, added §3c, §7 builder command/sentinel/source explanation, and §10 gate status. The sample sizes, floors, bar, exclusions, one holdout, custody/protection clauses and §6 pipeline text remain unchanged. This is an explicit source-design and enforcement amendment, broader than a delay change.

Sentence-to-behavior assessment: §3b's formula, named exclusions, record derivation, BLS/hash checks and ordinary quorum logic execute; its unconditional uniqueness/timing, body-equality impossibility, exact URL boundary, universal RETRY and W3/W5 claims need the qualifications/repairs above. The builder's seed-to-split ordering is implemented at B:22–28,139–166. §3c's adoption check executes, while complete history, driver conjunction, current cost paragraph and “every pin except three” description are inaccurate. §7's command names the new builder; grid, fixed denominator, floors, objective, tie-break, receipt/winner reconstruction and ordinary witness checks execute at D:205–334. §7:57 still describes NIST versus drand and therefore does not describe V20. Sentinel accounting is exhibited; the adapter provenance is not. Holdout-once and custody over intervals remain the preserved covenants, not newly proven mechanisms.

Guarded-pool re-derivation from the missing GZ1 table: UNVERIFIABLE HERE. Hash equality and fixtures using the retained pool are not independent reconstruction of that population.

**Decision provenance and prospective work.**

V20:1,3 and the change record record the requested provenance: Duho via codex voice, approximately 19:02 KST, “해,” recorded by Codex; source-direction decision only, not a signature, review verdict or draw. They also record the author's 12:52 overstatement and coordinator endorsement. That wording is correct relative to the supplied account. The cited `.hermes/CODEX_DUHO_DRAND_ONLY_DECISION_20260906.md` is absent from this workspace and was not found under the supplied job directory; I therefore cannot independently authenticate the original voice/record or its cited digest. I do not turn this history into approval.

Actual final-byte approval, GitHub event capture, adoption commit, production collection, identity freeze, custody evidence, adapter/refusal reconciliation, development and holdout remain prospective. Their ordinary post-approval absence is not itself a precommitment defect. The unwired production verifier and unimplemented admissibility requirements are pre-approval defects. No study draw or production artifact was created by this review.

**What is still missing for approval — required clause substance, with matching implementation, pins and adversarial evidence.**

1. “The study seed is lowercase hex SHA256 of the unique BLS signature for the canonical chained-round message. Its fixed-round independence and pre-approval unpredictability assume an authentic pinned key, correct cryptography and fewer than a threshold of signers cooperating to violate the chain or release schedule. Different HTTP encodings can carry the same signature. Their fixed acceptance/refusal treatment shall not be described as cryptographic impossibility.”
2. “The pinned production entry point shall install its concrete verifier before identity loading. It shall recompute the complete acceptance conjunction from committed approval/adoption/beacon evidence, bind the actual rule digest, statement, T_sign, T_pulse, round, source and seed across those artifacts, and establish the required two exact pinned relays and live-equality quorum. A test-only callback or a claimed seed shall not replace this path.”
3. “The approval witness shall validate W1–W5 from evidence, including the earliest authentic qualifying GitHub event, before..head delivery where necessary, its repository/ref/commit/time and retained provenance, and the approval record as a blob at the approval commit. W5 shall use the explicitly chosen nonce-round set with its actual scheduled bound, enforce MIN_T_SIGN as stated, and authenticate its chain/value or explicitly disclose and justify the weaker nonce trust. Missing-event PENDING/CLOSED shall have a defined deadline and persistence rule, or be labelled a covenant.”
4. “History shall have an externally anchored initial state and authenticated ordered continuation; a missing/reset history shall not create a new first attempt. Every attempted boundary, including exceptions, shall be accounted for. First admissible acceptance and conflict handling shall be atomic. The driver shall parse and validate count, stages, ordering, earliest admissible acceptance and semantic conflicts, rather than depend on a builder-conflict label.”
5. “The adapter shall emit a sentinel only for a journalled renderer refusal and reconcile object identities, causes and sentinel counts before tuning. This prerequisite shall have executable evidence and a named gate. The current cost/source explanations and new fixture fragments shall describe the executed V20 path; inherited V15 defects shall remain separately disclosed. Warning-strict success shall report unraisable ResourceWarnings accurately.”

These repairs must be completed and the resulting final bytes reviewed before approval; merely obtaining another green fixture run or adding a callback after approval does not satisfy the present claim.

VERDICT: NOT-SIGNABLE

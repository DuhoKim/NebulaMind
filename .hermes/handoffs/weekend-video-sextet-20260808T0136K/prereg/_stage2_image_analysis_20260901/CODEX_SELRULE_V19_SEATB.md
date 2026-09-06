ACCESS_SHA=af7fa5408c51e292bde508a63c21bd511b8d0c9a3b56d41211f739b597913b91

Seat B — independent referee of V19 only, fourth prospective sampling-amendment draft under the narrow release.

AUTHORSHIP: The supplied history attributes earlier builder field-validation code (2026-09-06 00:13–00:18) and branch-protection work to Codex. That field-validation boundary is retired. All new reviewed V19 code is attributed to Hwao. I authored no reviewed implementation in this turn. Driver/builder integration findings touch inherited Codex-associated machinery; the adverse findings below concern the inspected V19 implementation and its claims. V39 is treated as approved and installed, not reopened.

References: V19:N is the target document’s line N. B = _optionA_dev/beacon_v2; C = _optionA_dev/corpus_identity; F = _optionA_dev/fourier_chirality. X = B/beacon_record_expedited.py; N = B/nist_pulse.py; AW = C/approval_witness_v3.py; builder = C/build_corpus_identity_v19.py; driver = F/run_configurations_v3.py. Code references use physical line numbers.

**The property, judged first — [FATAL] the narrow release’s central guarantee is not established.**

V19:32 genuinely states a property first. There is a true, narrower result: with the entire retained record, roots and fetch responses fixed, changing only `now` between two post-T_pulse instants does not change the source or seed. Authentication uses T_pulse, not the current certificate-validity date (N:77,89–108); X:85,105 contain the relevant clock gates. The exhibit actually executes that narrower result rather than merely printing an assertion.

But the conclusion “therefore WHEN collection starts is irrelevant” does not follow. Production also consumes current NIST/AIA/next-pulse responses and current relay quorums (X:90–117). These are not determined by the lane’s archived record. Live equality protects a previously retained record against replacement; it does not choose one immutable record before the first collection. Neither a timestamp nor a certificateId authenticates a failing pulse or a failing next-pulse response. A certificate hash binds the matching certificate, not every response an endpoint may serve while authentication fails.

I executed this counterexample with the supplied three-tier test PKI and mocked public endpoints:

| Same approval and T_pulse; same signed NIST pulse and leaf certificate | Result |
|---|---|
| Early collection: served next body has a different localRandomValue; all pulse signature, certificate-id, output-binding and anchor checks pass, but the next-link check fails; drand quorum agrees | ACCEPT-DRAND, seed = 64 lowercase c characters |
| Later first collection: next endpoint now serves the matching next body; pulse and certificate remain byte-identical | ACCEPT-NIST, a different seed |
| Recheck the early retained record against the later live service | REFUSE-NIST-LIVE-DIFFERS |

The early result follows N:103–105 and X:102–117. No hash collision, changed certificate, new pulse signature, or unavailable endpoint is needed. The early next body is precisely an unauthenticated input that the acceptance predicate permits to trigger fallback. The late collection supplies a fresh record, so equality with that fresh record passes. The existing recovery fixture similarly permits a fresh ACCEPT-NIST verdict and relies on an already-existing builder lock to reject it. A first collection deliberately delayed until recovery has no earlier builder lock.

This is a simulated endpoint transition, not a claim that NIST currently behaves this way. It refutes the unconditional execution claim and identifies the missing public-infrastructure assumption. An immutable, independently available archive would need to select and preserve all relevant failure evidence, not just authenticated successful objects. The author’s answer mentions an archive-non-rewriting assumption; V19’s claimed cryptographic consequence does not establish it.

The limits are useful but incomplete:

- L1 correctly admits that the AIA chain is the lane’s archive. It does not solve which chain is selected before first collection, or the analogous next-body failure/recovery demonstrated above.
- L2 honestly discloses no BLS verification. It cannot simultaneously use BLS immutability as a property established by this acceptance path: B/drand_round.py:18–28 accepts quorum randomness without checking a signature or binding the response to CHAIN_HASH. A third party may reject a response this code accepts.
- L3 correctly admits that an aged-out GitHub event becomes the lane’s attested copy. Therefore the complete approval conjunction is not independently re-queryable at any later time without trusting retained evidence.
- L4’s “outages give RETRY” is only correct for NIST collection exceptions. Loss of live drand quorum yields UNAVAILABLE (X:115–116). Changed NIST bytes yield REFUSE, not RETRY.
- L5’s “neither selects a seed or source” is the unproved conclusion exposed by the fresh-collection counterexample.

The exhibit’s two synthetic cases genuinely return identical ACCEPT-DRAND results at 2026-09-06T03:12:00Z and 2026-10-06T03:11:00Z. The same mock archive is supplied both times. The real-record case stops at REFUSE-T-SIGN-PREDATES-AMENDMENT before authenticating evidence; it does not exercise a real production source decision. Its output note is honest, although the generator docstring says “RETRY both times.” The exhibit establishes conditional replay determinism, not immutable public inputs or independence of first collection time.

**The five hard constraints.**

| Constraint | Result | Clause and implementation |
|---|---|---|
| C1: exclude the public 00:15Z pulse by name | MET | V19:33 names 2026-09-06T00:15:00Z, NIST 1928801 and drand 6440756. X:35–36,49–50,78–79 contains the lower bound and explicit exclusion. |
| C2: same formula from new approval time | MET | V19:33; X:34,39–42,74–76; AW:58–63 binds APPROVAL_UTC to T_sign. First whole minute at or after new T_sign + 600 seconds; no inherited pulse. |
| C3: V15/RETRY preserved; prospective supersession | MET | V19:3,41; builder:13 imports the separate variant. Historical hashes verified below. Preservation and the prohibition on using V15 are protocol instructions; the old executable remains present. |
| C4: cost stated | MET | V19:39,41 discloses immediate fallback, weaker relay provenance without BLS verification and signed-then-superseded history. X:34,105–117 implements immediate eligibility. The stated probability of drand is an expectation, not a guarantee. |
| C5: visible approval before seed, W3/W5, timing rendered irrelevant | NOT MET as the complete requested constraint | W3 is materially repaired: AW:44–53,78–81,91–94 selects the earliest matching retrieved server event and retains the entire object/provenance. W5 still admits the predecessor round, AW:86–90, rather than exclusively round_for(T_sign). Most importantly, the claimed collection-time independence fails as above. |

I independently committed an approval with both Git author and committer dates set to 03:00:07Z, then supplied a server event at 03:11:30Z for T_pulse 03:11:00Z: APPROVAL-PUSHED-AFTER-T-PULSE, CLOSED. Server chronology is repaired under the intended GitHub/transport trust model. A separately executed predecessor-nonce case ACCEPTED round 6441085 while round_for(T_sign) was 6441086. V19 explicitly permits that interval, so its numerical rule is implemented; “the round current at T_sign” is not exact. The corrected document claim “no earlier than round R” is sound under the disclosed relay assumption. AW’s docstring still overclaims T_sign − 30 seconds.

GitHub documents up to 300 events from the past 30 days and repository-event latency of 30 seconds to 6 hours. V19’s revised limits agree with that documentation. [GitHub Events documentation](https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28)

A read-only real repository query succeeded: 100 events, all PushEvents; one was id 20208332546, created_at 2026-09-06T04:14:01Z, head 96563249b563c1704a8509a979e9e46900e75227 on refs/heads/feat/paper-workflow-v2. Its payload had head/before/ref, but no commits array. This verifies an available event shape, not a V19 approval. AW’s earliest selection is only over retrieved matching events. A push delivering approval as a non-head ancestor without a commits array may not match. Missing-event PENDING/CLOSED is explanatory text at AW:79, not a persisted deadline state machine.

**1. Acceptance set — [MAJOR] the builder’s local predicate is substantially repaired, but the driver does not enforce the required conjunction.**

At the ordinary production builder boundary, fetch is supplied (builder:62–66). NIST acceptance requires all recomputed authentication checks and equality of all four collected representations (X:86–103). Fallback requires a retained/live-equal chain-2 pulse with the exact T_pulse timestamp, failed aggregate authentication, the expected drand round and retained/live quorum randomness equality (X:108–117). AW.verify and adoption-at-approval-commit execute before the lock and identity construction (builder:70–79,86–99,161–168). No accepted Boolean from the beacon record is trusted.

However, failed aggregate authentication is broader than V19:33’s “signature/anchor checks fail.” My next-body counterexample has both signature and anchor TRUE and still takes fallback. The broad acceptance-set wording “failing authentication” includes it; the narrower explanatory sentence does not.

The downstream driver checks an ACCEPT prefix, a timestamp field, matching identity/lock fields, log hash and committed blob (driver:165–176). It does not:

- restrict outcomes to ACCEPT-NIST or ACCEPT-DRAND;
- parse the log or locate its first admissible ACCEPT, count entries, check conflicts, or compare that actual entry to collection_lock;
- validate the full approval witness, event digest/provenance, repository/ref/commit inclusion, nonce, approval record, or T_pulse formula;
- verify adoption bytes at the approval commit or compare identity.adoption_sha256 to those bytes;
- rederive the seed from the retained beacon evidence.

Executed against the actual load_identity function, using a real disposable Git clone/bare remote and seal commits, production sizes 400/200/2,000 and production pool/exclusion digests: an identity with an EMPTY committed log, a claimed entry count of 999, only a timestamp/ref-shaped approval dictionary and an adoption file outside the repository was ACCEPTED as ACCEPT-DRAND. Changing its outcome and matching lock field to ACCEPT-INVENTED was also ACCEPTED. Changing them to RETRY was correctly refused IDENTITY-BEACON-NOT-ACCEPTED.

Only fixture transport, paths and adopted test digest were substituted; require_beacon remained True. This does not demonstrate forging GitHub’s clock. It demonstrates that a seal of selected bytes is accepted without the promised semantic evidence. Thus the answer to “any accepted identity outside the full conjunction?” is YES at the downstream boundary, even though the ordinary builder rejects the named malformed inputs.

**2. Collection history — [MAJOR] complete, committed, driver-verified history is still not implemented.**

Builder:68,75–76,109–115 now logs ordinary verdicts, witness/adoption refusals, first acceptance and later conflicts. Those repairs execute. But malformed JSON, invalid rule digest, missing files and other failures occur before logging (builder:55–59). I executed malformed JSON refusal BEACON-RECORD-INVALID-JSON and observed no log file. Collector logging remains optional (`--log`, X:125–130), and collect/parse exceptions escape before the log call (X:132–135).

The file is opened in append mode; there is no authenticated prior head, missing-after-start refusal, or atomic exclusion around read/check/append (builder:81–115). The unused `first` variable at builder:107 includes builder-verdict, but enforcement actually uses only builder-accept. A collector ACCEPT or an ACCEPT verdict followed by witness refusal does not establish the lock. Committing the eventual file proves those bytes were committed, not completeness of earlier attempts. Driver:175–176 verifies precisely that limited fact and never reads log entries. These are still material after V19 calls the log bookkeeping: the property that supposedly removed its security role is unproved.

**3. Required executions and reproductions.**

The first shell command was exactly the requested shasum command; its full digest is the report’s first line. signature_preimage.py independently printed the same digest. Python runs used PYTHONDONTWRITEBYTECODE=1. Extra probes used temporary locations outside the reviewed tree; no publication or shared-remote mutation occurred. The only report artifact written here is this file.

| Required suite | Observed |
|---|---|
| `python3 -W error -m unittest test_beacon_record_expedited test_beacon_v2` | 37 tests, OK = 18 + 19 |
| `python3 -W error::ResourceWarning -m unittest test_approval_witness_v3 test_build_corpus_identity_v19 test_build_corpus_identity` | 18 tests, OK = 9 + 5 + 4 |
| `python3 -W error::ResourceWarning -m unittest test_run_configurations_v3 test_run_configurations` | 37 tests, OK = 20 + 17, with warnings described below |
| `python3 -W error exhibit_property.py`, twice | Both ALL IDENTICAL: True; digest b790ebdfc65d80183bb4eb32089a8102252e64f380e7ad0c6e7f341411b82060 |
| Additional `test_fourier_chirality` | 10 tests, OK |

The two required exhibit outputs match; the filed code block also matches the generated output, normalizing its terminal newline. All 92 requested-suite tests completed with unittest OK. Expected argparse refusal output is not a failure.

[MINOR] Warning-strict is not warning-clean: the driver suite emitted unraisable ResourceWarnings for unclosed files in F/test_run_configurations_v3.py:219,221. Python printed “Exception ignored in” and still reported OK. A separate RuntimeWarning arose from NaN-to-integer casting at F/fourier_chirality.py:87; the requested ResourceWarning policy does not promote that category. Do not describe this execution as free of resource warnings.

Mandatory counterexamples were exercised:

| Counterexample | V19 result |
|---|---|
| Served, live-equal wrong-time pulse | RETRY in the required expedited fixture |
| NIST HTTP 404 and 500 | RETRY; both-module fixture contrasts V15 ACCEPT-DRAND |
| Raising live fetch with authentic retained NIST; before-pulse authentic NIST | RETRY; fixtures reproduce V15 ACCEPT-NIST |
| Late writer with actually backdated Git dates | APPROVAL-PUSHED-AFTER-T-PULSE; independently reproduced |
| Simulated NIST recovery after first builder ACCEPT | COLLECTION-LOCKED; builder-conflict appended; required builder fixture passed |
| Driver RETRY-outcome identity | IDENTITY-BEACON-NOT-ACCEPTED; independently reproduced |
| Adoption file committed after approval commit | ADOPTION-NOT-AT-APPROVAL-COMMIT; required builder fixture passed |

The frozen removed-line audit passed: actual normal diff of beacon_record.py and beacon_record_expedited.py exited 1 as expected; its 23 ordered removed lines exactly equal the fixture’s literal REMOVED_FROM_PINNED list, independently extracted by AST. Both freshly generated document diffs reproduce V15_TO_V19.diff and V18_TO_V19.diff byte-for-byte. All 35 distinct full E3 file digests matched, including historical pins; additional witness/module-fixture and exhibit pins matched.

Guarded-pool re-derivation from the absent GZ1 table: UNVERIFIABLE HERE. Existing pool hashing, failed-set control and builder/driver fixture integration passed; they do not replace the missing-source re-derivation.

**4. Repair audit of every V18 finding.**

| V18 finding | Status under V19; clause and code |
|---|---|
| Server-time upper bound against late/backdated writer | REPAIRED; V19:33; AW:78–81; independent reproduction above. |
| Entire event retained, rather than four fields | REPAIRED for the parsed event object; V19:33; AW:91 retains it and a canonical digest/provenance; builder:162 persists it. This is not raw HTTP-response retention. |
| Wrong 90-day window, omitted latency, newest-first matching | REPAIRED/ANSWERED; V19:32–33; AW:32–53,79. Bounds and latency now honest; earliest among retrieved matches. Deadline status remains prose. |
| Nonce lower-bound arithmetic | ANSWERED in V19:33 by “no earlier than round R”; AW:86–90 still permits predecessor; AW:6–12 retains stale 30-second prose. Literal current-round constraint remains NOT REPAIRED. |
| Wrong-time NIST pulse opens fallback | REPAIRED; V19:33,36; X:109; required test passes. |
| HTTP errors trigger fallback; authentic NIST accepted before clock/after fetch error | REPAIRED; V19:33,36; X:85,99–103; both-module tests pass. |
| Ordinary later recovery switches an accepted build | REPAIRED with intact prior builder log; V19:41; builder:109–113; conflict now logged. First-collection independence remains NOT REPAIRED. |
| Missing RETRY/refusal/conflict logging; collector never logs | PARTLY REPAIRED, overall NOT REPAIRED; V19:41; builder:68,76,110 and X:125–135. Optional collector log and pre-log exceptions remain. |
| History unbound to identity/driver; mutable/resettable log | PARTLY REPAIRED, overall NOT REPAIRED; builder:115,162; driver:175–176 binds bytes but does not parse history; no durable prior-head/reset enforcement. |
| Adoption not committed, loose file format | REPAIRED at builder; V19:41; builder:91–99 enforces exact bytes at approval commit. NOT REPAIRED at driver:48–53,160–176, which tolerates surrounding blanks and does not verify the approval blob. |
| Driver checks no outcome/witness/lock | PARTLY REPAIRED, overall NOT REPAIRED; V19:37,41; driver:165–176 refuses basic absent/late/mismatched fields, but accepts the incomplete evidence demonstrated above. |
| End-to-end fixture uses V15 builder | REPAIRED; V19:41; F/test_run_configurations_v3.py’s end-to-end case now uses V19 builder and passed. |
| Advertised adoption/sentinel tests absent; wrong driver count | REPAIRED; V19:21,41; both tests exist and 20 tests run. New ResourceWarnings remain. |
| Render-refused representation undefined; adapter not executed | ANSWERED as clause/design; V19:55; driver:46–47,202–218 counts sentinel and leaves it UNSCORED. Adapter refusal-cause reconciliation remains a prerequisite, not exhibited completed execution. |
| Stale operative §7 builder command | REPAIRED; V19:53 names V19 builder, digest and approval record. |
| Removed VOID cited as current observed outcome | REPAIRED; V19:36; X:95–103 supersedes the old recheck. |
| RETRY versus REFUSE-NIST-LIVE-DIFFERS contradiction | NOT fully REPAIRED; V19:36 is correct, but V19:33 still says a DIFFERENT served pulse is RETRY; X:95–98 refuses differing retained/live evidence. |
| Overbroad raw-byte equality claim | REPAIRED; V19:33 distinguishes four NIST collected representations and drand quorum randomness; N:55,60 normalizes certificates to PEM. |
| Inherited unsigned/wrong-certificate → RETRY observations presented as current | NOT REPAIRED; V19:34–35 still carries these examples. Independently executed unsigned current evidence without drand gives UNAVAILABLE; with quorum it can give ACCEPT-DRAND (X:108–118). |
| “ONE rule” overclaim and stale version labels | ANSWERED in V19:3 by “ONE sampling rule” plus machinery disclosure. V19:41 still labels §3c V16 and costs “under V17”; §9 remains explicitly a historical V15 gate checklist. |
| V15 defect disclosure | REPAIRED/EXACT; V19:3; original B/beacon_record.py:75–80 accepts retained authentic NIST after fetch errors and before its clock guard. |

The agy V18 report offered no additional adverse counterexamples; its assertions that the history/adoption/driver conjunction was complete and that nothing was aspirational are not supported by this audit. Its historical test-count claims are not evidence for V19.

**5. Diff confinement and sentence-to-execution review.**

V15→V19 changes are confined to the heading/introduction, E3 pins/enforcement, §3b, added §3c, §7’s builder command, sentinel convention and source-choice explanation, and the gate/cost status. Sample sizes, floors, 0.70 bar, exclusions, one holdout, custody/protection clauses and §6 pipeline text remain unchanged. This is broader executable machinery than merely changing FALLBACK_AFTER_H; V19:3 now acknowledges that. V39 installation is supported by its supplied freeze record and is not a missing pipeline approval.

Across §3b, formula, explicit exclusion, binding checks, clock-first order, ordinary exception handling, NIST equality scope, relay threshold and seed-to-split mapping correspond to X:34–118, N:89–108, B/drand_round.py:7–28 and builder:22–28,141–167. Exceptions to claimed behavior are the property, signature/anchor-only fallback explanation, RETRY observations and DIFFERENT-pulse wording described above. The collector also records collected_utc and error metadata; “ONLY inputs and evidence” is accurate only as “no trusted stored verdict,” not literally no metadata.

Across §3c, adoption-at-approval-commit and ordinary lock/conflict behavior execute. Complete history, semantic driver verification and removal of the first-collection lever do not. “NIST tried ... once” is not enforced; repeated attempts are explicitly supported. The builder’s first accepted record is locked before the subsequent corpus build finishes (builder:77,117–149); that is not synonymous with a successfully frozen identity.

Across §7, the V19 command is repaired. Grid, fixed denominators, floors, objective, tie-break, winner reconstruction and ordinary witness/blob checks execute in driver:183–305. Sentinel counting is implemented, but the fixture accepts either nonfinite output or exception-derived UNSCORED behavior, not a completed adapter/refusal-cause proof. “Holdout once,” custody across the interval, absence of secret runs and human approval remain protocol covenants with the disclosed evidence boundaries. The driver does not mechanically prevent a second holdout invocation. V19:60’s no-source-choice explanation inherits the failed property claim.

[MINOR] The text still contains contradictory historical counts: E1 at V19:19 says test_run_configurations.py has 10 tests; E3 correctly says 17, and 17 ran. E3 also leaves an obsolete “3 tests ... plus ... 2 tests” fragment after correctly naming the inherited builder’s 4 tests. The inherited §9 checklist is labelled V15, so its historical commands should not be confused with the current release’s required suites. All currently requested filenames exist.

**6. Preserved evidence, execution limits, and missing clause substance.**

V15 SHA-256 is unchanged:
fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1

Filed RETRY SHA-256 is unchanged:
1c1d9d4bacc35319e91d46420b8f892e1126cc48059ec69156a0a718428aeb4b

The signature record preserves Duho’s digest statement and T_sign 2026-09-06T00:04:07Z. The V15 disclosure correctly identifies an executable acceptance defect, not an accepted historical seed. The retained RETRY is unaffected. “No identity will be built under V15” is an instruction, not an executable disablement.

Actual V19 approval, approval event, adoption commit, production collection, identity freeze, adapter execution, tuning and holdout remain prospective. Their absence does not itself prevent precommitment approval. What prevents it is describing stronger enforcement and timing independence than the pinned code establishes. The manifest-driven adapter and per-object renderer-refusal reconciliation remain unexhibited prerequisites before development. The approved V39 pipeline is not an outstanding approval.

Still missing for approval, as clause substance requiring corresponding implementation, pins and adversarial evidence:

“Replay determinism holds for explicitly identified retained inputs. Collection-time independence additionally requires an independently checkable rule selecting immutable public inputs, including unauthenticated failure evidence, issuer-chain evidence and next-pulse evidence. A transient malformed or inconsistent ancillary response shall not select a different source. A changed source response before first collection shall have a fixed, non-selective consequence. Until this property is demonstrated, the amendment shall not claim that delaying first collection cannot select the source.” Merely weakening the prose does not satisfy this narrow release; its central property requires a design repair or a new coordinator/user ruling on scope.

“Every attempt, including input/parse failures and witness/adoption failures, shall enter the mandatory history. Its initial state and subsequent entries shall be bound so a missing/reset history cannot be silently treated as a first attempt. First admissible acceptance and conflict handling shall be atomic. Before tuning, the driver shall parse the committed history, verify its count and ordering, locate its actual first admissible ACCEPT, reject contradictions, and compare the actual entry and retained evidence to the identity.”

“The driver shall accept only ACCEPT-NIST or ACCEPT-DRAND and validate the approval record/event/nonce, T_sign-to-T_pulse relation, adoption bytes at the approval commit, retained beacon evidence and collection-history bindings. An early timestamp dictionary, self-reported outcome or matching digest alone shall not substitute for this conjunction.”

“W5 shall use exactly round_for(T_sign) if the required constraint is the current round. If the predecessor is intentionally permitted, state its actual scheduled lower bound and obtain an explicit change to that constraint. Missing-event latency/deadline handling shall be specified as executable state or clearly identified as a covenant.”

“The adapter shall emit the canonical sentinel only for a journalled renderer refusal and reconcile object identities, refusal causes and sentinel counts before tuning. Correct the contradictory outcome/count/version statements and close fixture resources so the advertised warning-strict execution is accurately reported.”

**Hash audit inventory.** Every following file’s computed digest equals its full E3 pin in the access-proved target; historical superseded pins were included, not silently omitted. There are 35 distinct digests:

- B: beacon_record.py; beacon_record_expedited.py; nist_pulse.py; drand_round.py; pinned_root_DigiCertGlobalRootG2.pem; test_beacon_record_expedited.py; test_beacon_v2.py; test_pki.py; negative_probes.py; negative_probes_receipt.json; observed_behaviour.py; _sample_pulse_last.json; _sample_certificate.pem; _digicert_intermediate.pem.
- C: build_guarded_pool.py; build_corpus_identity.py; build_corpus_identity_v18.py; build_corpus_identity_v19.py; test_build_corpus_identity.py; test_build_corpus_identity_v19.py; guarded_pool.csv; dryrun_identities_to_exclude_20260905.txt.
- F: fourier_chirality.py; run_configurations.py; run_configurations_v2.py; run_configurations_v3.py; test_fourier_chirality.py; test_run_configurations.py; test_run_configurations_v2.py; test_run_configurations_v3.py; env_lock.json; w_chi_vendored.py.
- Other: BEACON_V2_OBSERVED_BEHAVIOUR_20260906.md; scratch/survey-bricks-dr9-north.fits.gz; validation_bricks/_bricks_without_r_coverage.txt.

Additional checked pins: AW c41d516e75a8a4c408cf5f29abe6ea8e12e61d0235bdb6b72d4619da76e2671a; test_approval_witness_v3.py aff92daf4784dc7b53dd7c370d8ba8ddd94aeb81d0e7bcd591727847e1eac199; exhibit_property.py f56776ce6252eded299f2c55412c7b99390837d1c343c88b33066cf474e6e3a1. Diff pins: V15_TO_V19.diff 3c81f9345a148d9756d98f416383e6bb313a8c70dbad560a7981d5c1c5c122a3; V18_TO_V19.diff 86d2e8a8b83ca4f8b42f2adf9c62d02eb35f6abd7bb8de575ea6d8d5286d3ae6. All MATCH.

VERDICT: NOT-SIGNABLE

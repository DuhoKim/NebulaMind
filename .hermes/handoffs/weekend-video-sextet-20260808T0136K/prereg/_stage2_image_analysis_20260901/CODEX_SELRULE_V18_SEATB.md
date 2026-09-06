ACCESS_SHA=121b1e0e4a8af6d82e12d02cbb433c80f6ea10d781d781d1330ba2c1ac90d866

Seat B — independent review of V18 only as a prospective sampling amendment.

AUTHORSHIP: The supplied history attributes earlier builder field-validation code (2026-09-06 00:13–00:18) and branch-protection work to Codex. The former is expressly retired from the beacon boundary. All new V18 implementation is attributed to Hwao. I authored no reviewed implementation in this turn. Builder/control integration findings touch inherited Codex-associated work; the adverse findings concern the inspected current implementation and its claims. Historical custody/protection receipts were inspected, not independently reenacted.

V18 repairs the original late-writer, NIST HTTP-error, ordinary repeated-build and missing-adoption counterexamples. It is nevertheless NOT-SIGNABLE: the promised complete collection history is not implemented, the adoption file is not verified as committed, and the downstream driver does not enforce the claimed acceptance/witness/lock conjunction. The server-clock idea supplies the previously missing upper bound, but its retention and availability claims are false.

References: V18:N means line N of OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V18_20260906.md. B = _optionA_dev/beacon_v2; C = _optionA_dev/corpus_identity; F = _optionA_dev/fourier_chirality. AW = C/approval_witness_v2.py; builder = C/build_corpus_identity_v18.py; driver = F/run_configurations_v2.py. These abbreviations apply to code line references and the hash inventory.

Execution and access evidence:

- The first shell command was exactly the requested shasum command. Its digest matches the target. signature_preimage.py independently printed the same full digest.
- Beacon, warning-strict: 34 tests OK, comprising expedited 15 + inherited 19.
- Corpus, ResourceWarning-strict: 17 tests OK, comprising witness 8 + V18 builder 5 + inherited builder 4.
- Driver, ResourceWarning-strict: 34 tests OK, comprising V2 17 + inherited 17. The requested/claimed 19 + 17 is FALSE: V2 contains only 17 discovered tests. Neither advertised new adoption/sentinel test exists in that file.
- Thus 85 requested-suite tests actually ran successfully. Expected argparse refusals appeared during driver tests.
- I used PYTHONDONTWRITEBYTECODE=1. Additional probes used temporary directories outside the reviewed directory, fixture PKI, mocked relays/events and local bare Git repositories. No GitHub publication or remote mutation occurred. One probe rewrote only its disposable local fixture remote to install an explicitly backdated commit.
- Real GitHub Events API read succeeded. A returned public PushEvent had id 20204736650, created_at 2026-09-06T03:21:53Z, ref refs/heads/feat/paper-workflow-v2, head 33d5a002a8e39da6f8b2368820263e86f2ccb02d. This establishes availability of that event shape, not a future V18 approval.
- Normal diff beacon_record.py beacon_record_expedited.py exited 1, as expected for differing files. Its ordered 18 removed lines exactly equal the fixture's literal FROZEN REMOVED_FROM_PINNED list, independently extracted by AST. There are 34 added lines.
- Fresh normal document diffs reproduce V15_TO_V18.diff and V17_TO_V18.diff byte-for-byte.
- All 32 distinct full E3 digests match local files. The two additional §3b witness/module-fixture pins also match. Inventory follows below.
- Guarded-pool re-derivation from the absent GZ1 source table: UNVERIFIABLE HERE. Existing pool hashing and the failed-set control passed; these are not re-derivation from the missing table.

The five hard constraints:

| Constraint | Result | Clause and implementation |
|---|---|---|
| C1: public 00:15Z pulse excluded by name | MET | §3b(1a), V18:32 names 2026-09-06T00:15:00Z, NIST chain-2 pulse 1928801 and drand 6440756. B/beacon_record_expedited.py:30–31,44–45,73–74 enforces the lower bound and explicit exclusion. |
| C2: same formula from new approval, no inherited pulse | MET for the prescribed formula | §3b(1)–(2), V18:32: new approval supplies T_sign; first whole minute at or after T_sign + 600 s. B/beacon_record_expedited.py:29,34–37,70–78; AW:51–56 binds the stated UTC. Actual speaker and exact approval UTC remain attested as disclosed. |
| C3: preserve V15/RETRY, prospective supersession | MET | V18:3,40 expressly preserves V15 and prohibits building under the defective signed path; V18 remains unapproved. Builder:13 imports a separate variant. Both historical artifact hashes match below. Preservation is an artifact/protocol fact, not a runtime prohibition in the old module. |
| C4: cost stated | MET | §3c, V18:40 discloses immediate relay fallback, unverified BLS, weaker provenance and signed-then-superseded history. B/beacon_record_expedited.py:29,98–110; B/drand_round.py:7–28 implements that provenance. The lost primary opportunity is a minimum fallback delay, not a 24-hour NIST expiration. |
| C5: reader-visible approval before seed, retained/re-queryable witness | NOT MET as the complete stated constraint | §3b(W3/W5), V18:32. AW:71–83 repairs the pre-pulse timestamp and nonce checks. But AW:84 retains only four selected event fields, not the verbatim event, and AW:30–37 retrieves at most 300 events. The 90-day re-query guarantee is unsupported; see finding 1. The original late-writer chronology counterexample itself is REPAIRED. |

1. [MAJOR] C5 repair is real, but evidence retention, availability and the exact nonce bound are overstated.

Required late-writer reproduction: I explicitly set GIT_AUTHOR_DATE and GIT_COMMITTER_DATE to 2026-09-06T03:00:07Z for the approval commit in the disposable fixture repository, pushed it there, and constructed the event feed exactly in the fixture's shape. T_pulse was 03:11:00Z; server-event time was 03:11:30Z. The actual builder boundary refused APPROVAL-PUSHED-AFTER-T-PULSE and said CLOSED. The date field no longer defeats the check.

A genuine GitHub event retrieved from the intended server is materially different from a dictionary supplied to a unit test. Under the intended GitHub/TLS/CLI trust assumptions, the operator cannot backdate that server field or replace the commit's bytes while preserving its hash. No late/backdated false acceptance was found against that trust model.

Attack assessment:

- Delay: delaying the push until after T_pulse causes refusal. Delaying retrieval does not turn a late server timestamp into an early one. API publication latency can instead make a timely push temporarily invisible, causing refusal. The implementation provides no latency-aware pending state.
- Forge: a hand-edited retained event or injected fixture dictionary can contain any time, but that is not a forged genuine event. Production obtains events through gh api, not from a record-supplied feed. Trust in the installed CLI, endpoint and transport remains necessary.
- Replay: an older event for another commit/ref does not match AW:42–45. Replaying an actual early event for the identical approval commit establishes that those same bytes already existed. It cannot select different approval bytes without a hash break.
- Select: AW:41–45 returns the first matching event in newest-first results. A later repeated push of the same commit can therefore cause rejection even if an earlier qualifying event exists. This is a false-refusal/availability issue, not an ability to give new bytes an old timestamp.
- Second approval: distinct matching record paths are refused by AW:76–77; modifications to the selected path in the traversed history are refused by AW:59–64. Multiple valid schema lines are refused by AW:51–54. These checks establish one visible record path and selected committed bytes, not global uniqueness of spoken approvals or unpublished records.
- Late record: a genuine matching late event is refused. An unavailable/aged-out event is also refused, even when the underlying push was timely.

What each check actually proves:

| Check | Established | Not established |
|---|---|---|
| W1, AW:58–64 | One addition and no subsequent selected-path touch in the traversed local history; disk bytes equal its committed blob. | Speaker identity, exact writing time, completeness of all off-repository history. |
| W2, AW:66–69 | Configured origin matches; selected commit is currently an ancestor after fetch. | When it was pushed, or current branch-protection settings. Protection rests additionally on the filed receipt and covenant. |
| W3, AW:71–74 | Matching server-reported push time is strictly before T_pulse. | Exact approval UTC or authorship. |
| W4, AW:76–77 | Exactly one matching added record path in locally reachable --all history. | All actual conversations or secret/unpublished approvals. |
| W5, AW:79–83 | R is round_for(T_sign) or its predecessor, before the seed round, with a live relay quorum confirming its value. | BLS verification, operator independence of relays, or the exact approval time. |

[MAJOR] Retention: AW:84 keeps only id, created_at, ref and head. It discards type, repo, actor, public, before and the commits list. If matching used payload.commits rather than head, it even discards the field proving why the event matched. Builder:139 persists this reduced structure. “Retained verbatim in the identity” (V18:3,32) is false.

[MAJOR] Query window: V18 explicitly states 90 days, so the limit is mentioned, but incorrectly as guaranteed availability. Current GitHub documentation specifies up to 300 events and only the past 30 days; it also documents repository-event latency from 30 seconds to 6 hours. An active repository can exhaust the count limit earlier. The production function fetches only three pages of 100. Correct the text and require prompt independent retention; no guaranteed 90-day re-query follows. [GitHub Events documentation](https://docs.github.com/en/rest/activity/events?apiVersion=2022-11-28)

[MINOR] Nonce arithmetic: allowing the predecessor round does not prove “written after T_sign − 30 s.” With the fixture's T_sign = 03:00:07Z, that permitted round begins 37 seconds earlier. Generally the bound is the actual scheduled time GENESIS + (R−1)×30; the permitted predecessor can be almost 60 seconds old. This does not undo the pre-pulse upper bound, but the exact claimed lower bound must change.

2. Acceptance set and mandatory beacon counterexamples.

At the production builder boundary, fetch is always supplied (builder:62–66). For NIST acceptance, B/beacon_record_expedited.py:80–97 requires retained authentication and equality of all four collected inputs: pulse, leaf, intermediate list and next body. B/nist_pulse.py:89–108 recomputes authentication. For fallback, expedited:102–110 requires retained NIST evidence, live equality, failed authentication and retained/live pinned-relay quorums for round_for(T_pulse). No retained accepted flag is trusted.

Clock: expedited:79 runs after schema/time/statement binding checks but before NIST evidence decoding/authentication and live collection. “Before any evidence is weighed” is correct; “before every file read or parsing operation” would not be.

Freshly executed results:

| Counterexample | V15 module | V18 |
|---|---|---|
| Live NIST HTTPError(404), unauthenticable retained pulse plus relay quorum, evaluated after V15's delay | ACCEPT-DRAND | RETRY, no seed; builder BEACON-NOT-ACCEPTED |
| Same, HTTPError(500) | ACCEPT-DRAND | RETRY, no seed; builder BEACON-NOT-ACCEPTED |
| Live generic exception with authentic retained NIST | ACCEPT-NIST | RETRY; both-module supplied fixture passed |
| Before T_pulse with authentic retained NIST | ACCEPT-NIST | RETRY; both-module supplied fixture passed |
| First full V18 build, served unsigned live-equal NIST | — | True, ACCEPT-DRAND, 400/200/2,000 |
| Second full build after simulated NIST recovery | — | COLLECTION-LOCKED; no second identity file |
| Driver load_identity without adoption file, otherwise sealed fixture identity | — | ADOPTION-MISSING |

ANY Exception caught from live NIST collection, including HTTPError at pulse/certificate/issuer/next-body acquisition, returns RETRY (expedited:93–95). It is neither a seed nor evidence of NIST failure. This promise is scoped to NIST collection. A live drand relay exception is caught as missing relay evidence by B/drand_round.py:11–17; the remaining quorum may still seed. I reproduced ACCEPT-DRAND with one live relay raising and the other three agreeing. That is consistent with the quorum rule, not with an unqualified “any live fetch exception anywhere means no seed.”

The removed VOID re-check is redundant in the production live-equality flow: equal authenticable evidence already takes ACCEPT-NIST; differing evidence takes REFUSE-NIST-LIVE-DIFFERS. This is a single-collection logical conclusion, not a guarantee that a remote source cannot change immediately after a check. The old VOID prose still survives at expedited:21–22 and V18:35.

[MAJOR] “Pulse for T_pulse” needs an explicit fallback eligibility predicate. The implementation falls back after ANY failed authenticate result, including timestamp mismatch. A collector-produced, live-equal response from the requested endpoint whose body says T_pulse − 60 s returned ACCEPT-DRAND with timestamp_is_t_pulse=False. If the requested acceptance set requires an actual T_pulse pulse, this is outside it. If “served for T_pulse” instead means anything the time-query endpoint returns, say that explicitly and justify treating the wrong pulse as positive primary-failure evidence. The current text repeatedly calls it the T_pulse pulse. This probe used substituted public responses; it is not a claim that NIST currently serves that mismatch.

The complete conjunction requested in the brief is NOT enforced end to end. Passing the source-byte verdict and the implemented local checks does not establish the promised first-collection history or committed adoption binding. The downstream counterexample in finding 4 is an additional explicit acceptance outside that conjunction.

3. [MAJOR] Collection lock: ordinary recovery is repaired; complete first-source execution is not.

The executed full-build recovery refusal is a substantive repair. With an intact existing log, builder:86–89 refuses a different record/outcome/seed. Replaying the exact accepted record is idempotent.

But §3c, V18:40 promises every collection attempt and verdict appended in order. Actual control flow:

- Builder:67 exits on non-ACCEPT before reaching the log.
- Witness/adoption refusals also occur before builder:71.
- Builder:88–89 refuses a conflicting later ACCEPT without appending it.
- Builder:90–91 writes only if no first ACCEPT already exists.
- The collector CLI, expedited:121–124, never invokes this log.
- Builder:139 does not include collection_lock in the emitted identity; the driver does not require the log or verify its committed blob.

Executed: HTTP 404 and 500 attempts left no log. First ACCEPT wrote one line; the refused recovery still left exactly one line. Removing that log in the disposable fixture allowed recovery to ACCEPT-NIST. Separately, a collector verdict ACCEPT-DRAND created no log, and the first subsequent builder invocation accepted recovered NIST. Thus “first collector ACCEPT” and “first builder ACCEPT after witness checks” are different procedures here.

The file is an ordinary mutable local file, with no authenticated prior head, tamper/missing-log refusal after first use, or atomic exclusion between concurrent builders. Committing it only with the final identity cannot independently establish completeness of earlier attempts. The deletion probe demonstrates lack of enforcement; it does not authorize a conforming operator to violate the signed covenant.

The text has also not fixed an independently witnessed collection start. Suppressing/delaying the first builder invocation remains a source-timing freedom. V18:59's claim that a local pre-run has no lever is therefore still too strong. A source lock must cover collection, unsuccessful attempts, first acceptance and downstream consumption before that claim is justified.

4. [MAJOR] Adoption binding and driver acceptance are only partially repaired.

Builder:74–80 and driver:45–50,156–158 genuinely require a local adoption file and compare its digest. Missing-file refusal is now executable and independently reproduced.

Neither checks that this file is committed, pushed, equal to the blob at the approval commit, or bound to the authenticated approval witness. Both accept blank surrounding lines despite “exactly one line.” The V18 builder fixture itself accepts an adoption file outside its Git worktree; my direct probe confirmed ADOPTION_TRACKED=False while the boundary returned ACCEPT-DRAND. Calling that a “committed file” is currently a protocol instruction, not an executed check.

Driver:142–165 checks sealed identity bytes and several schema fields, but never tests beacon_outcome, approval_witness or collection_lock. I constructed a sealed and locally pushed fixture identity with production sizes 400/200/2,000, production pool/exclusion digests and matching adoption digest, set beacon_outcome=RETRY, and omitted approval-witness/lock data. load_identity ACCEPTED it. Only the remote/protocol fixture transport was substituted. There is no production-only outcome check that the fixture bypasses. This contradicts V18:36's assertion that the driver refuses non-ACCEPT identities.

The existing V2 end-to-end test also still uses the V15 builder, not the V18 builder. It therefore cannot establish end-to-end enforcement of the new approval/lock conjunction. A seal proves the selected bytes were committed; it does not prove that those bytes came through the mandatory V18 acceptance path.

5. Render-refused convention: design repair accepted; execution claims need qualification.

§7, V18:54 now fixes representation, denominator treatment, UNSCORED status, per-object cause journalling and prohibition on alternatives. No ad hoc substitution is permitted by the clause. Driver:43–44 defines the pinned sentinel; :167–187 retains it in n and counts hashes; :189–203 produces UNSCORED; :212–216 carries manifest counts into receipts.

I independently loaded the 65,536-byte sentinel through load_manifest: n=1, sentinel_count=1. Across all 96 configurations score_config returned (k,m,unscored)=(0,0,1). Its hash equals the clause's d5568f5091ec8295a1e80e8271f05312ff02762562747c6448bbe95b8bf6fd5e. A RuntimeWarning about invalid float-to-integer casting occurred; it is not a ResourceWarning and did not invalidate the required warning policy or scoring result.

[MINOR] The advertised test_sentinel_tensor_is_counted_and_unscored and adoption test are absent from the pinned fixture. The 19-test claim in V18:21,40 is false even though direct probes confirm those two basic behaviors.

The manifest-driven adapter and its renderer-refusal cause journal remain unexecuted prerequisites. The driver counts sentinel bytes but does not prove that a particular object really received a renderer refusal, nor reconcile sentinel rows with an adapter refusal journal. Distinguish the fixed clause from a completed adapter implementation. This is no longer a missing representation decision; it remains work required before development pixels.

6. Repair audit of every V17 numbered item and its C-table.

| V17 finding | V18 status, clause and code |
|---|---|
| 1: late writer/backdated commit; old nonce; duplicate fields | REPAIRED for the exhibited attacks. §3b(W1–W5), V18:32; AW:51–83. Genuine server-time upper bound now exists. Retention/window/lower-bound claims remain NOT REPAIRED as detailed above. |
| 1: second approval and who spoke | ANSWERED with strict schema and first-visible-path rule; V18:32; AW:51–56,76–87. Speaker/exact approval UTC remain correctly attested. No proof of all conversations is supplied. |
| 2: HTTPError fallback despite blanket RETRY | REPAIRED. V18:32,35; expedited:93–95,102–103. Both 404 and 500 reproduced against V15 and V18. Original early-clock/generic-error repairs remain effective at :79,93–97. |
| 3: prior C1–C4 and inherited repair-table entries | C1–C4 remain MET as above. Timestamp formula, collector exclusion and token coverage are exercised. NIST is evaluated at build time, V18:38 and expedited:85; old “24 h expiration” overclaim is corrected at V18:40. |
| 3: C5 chronology and first-source procedure | Upper-bound counterexample REPAIRED by AW:71–74; complete evidence/window claim NOT REPAIRED. First-source procedure only partly repaired by builder:82–92; see finding 3. |
| 3: stale VOID/authorship/counts/both-module claims | Authorship ANSWERED explicitly at V18:21,67. Historical V16 one-module limitation is honestly retained at :21. VOID references and new driver test counts NOT REPAIRED (:35; expedited:21–22; V18:21,40). The author fixture checks V15 HTTP404 only; my additional probe verified V15 HTTP500 too. |
| 4: diff confinement | REPAIRED/CONFIRMED mechanically: supplied document diffs match; sample sizes, bars, exclusions and protected substantive passages remain unchanged. New §7 sentinel addition is disclosed. Stale operative V17 invocation at V18:52 remains NOT REPAIRED. |
| 5: first ACCEPT binding/source recovery | REPAIRED for a second different build with intact log, builder:86–89. NOT REPAIRED for every attempt, first collection, missing/reset log, independent chronology and downstream lock binding, builder:67–71,90–92,139; V18:40,59. |
| 6: inherited V15 defect and preservation | ANSWERED accurately at V18:3,40; original beacon_record.py:75–80 and both-module fixtures. Historical artifacts match. GZ1 re-derivation remains UNVERIFIABLE HERE. |
| 6: adoption prerequisite | Missing-file and digest comparison REPAIRED, builder:74–80; driver:45–50,156–158. Committed approval binding and downstream conjunction NOT REPAIRED. |
| 6: render-refused prerequisite | Clause REPAIRED at V18:54; counting/scoring confirmed at driver:186–203. Adapter/cause-journal integration remains an execution prerequisite. |
| 7: requested clause substance | PARTLY ANSWERED. New server clock, strict schema, HTTP policy, first-ACCEPT file and sentinel convention address the requested topics. Complete witnessed collection procedure, committed adoption verification, accurate evidence retention and truthful execution claims still require the clauses below. |
| Prior C-table | C1/C2/C3/C4 MET; C5 NOT MET as the complete evidence requirement, with its former fatal late-writer attack specifically REPAIRED. |

7. Diff confinement, inherited defect and remaining prerequisites.

The supplied diffs are exact. Explicit byte comparisons confirm unchanged §§4–6, E5 custody, holdout and freeze-witness paragraphs. The ordering/renderability implementation is unchanged; source/witness/lock/adoption changes occur at the builder boundary. The three production variants replace the named V15 modules while historical files remain present. The additional witness and fixture pins are disclosed.

Not every sentence of §3b/§3c/§7 is supported:

- [MAJOR] §7's operative command at V18:52 still names build_corpus_identity_v17.py, approved V17 digest and APPROVAL_RECORD_SELRULE_V17. It conflicts with E3's pinned V18 builder and omits V18 enforcement by directing execution through the superseded module.
- [MAJOR] Verbatim PushEvent retention, 90-day re-query, complete append-only history, committed adoption verification and driver non-ACCEPT rejection are false as explained above.
- [MINOR] V18:35 calls REFUSE-DRAND-VOID-PRIMARY-AUTHENTICABLE an observed current outcome although that V18 branch was removed. Expediter docstring :21–22 still says later NIST recovery voids an identity, contradicting §3c.
- [MINOR] V18:35 calls lack of live equality RETRY, whereas an actual unequal live NIST collection returns REFUSE-NIST-LIVE-DIFFERS (:89–92).
- [MINOR] §3b's generic “every public input ... equals retained bytes” must be scoped: NIST compares the four collected representations; drand compares quorum randomness, not all relay-body bytes. Certificate collection normalizes certificates into PEM (B/nist_pulse.py:55,60), so this is not raw HTTP certificate-body equality.
- [MINOR] V18:33's unsigned/wrong-certificate → RETRY examples are inherited V15 observations, not universal V18 outcomes when a live-equal unauthenticable primary and eligible drand evidence exist.
- [MINOR] The first paragraph's “ONE rule changes” must be understood as the intended sampling-policy change; execution also changes HTTP fallback eligibility, chronology, adoption, collection state and sentinel handling. §3c's references to V17 and §10's V17 gate label should be updated.

The inherited V15 disclosure is exact: original beacon_record.py can accept retained authentic NIST despite a raising live fetch and before its clock guard. “No identity will be built under V15 as signed” is the correct stop instruction; it is not a claim that the defective old code cannot run. The filed RETRY accepted no seed and is not invalidated by those acceptance counterexamples.

Preserved V15 SHA-256:
fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1

Preserved RETRY SHA-256:
1c1d9d4bacc35319e91d46420b8f892e1126cc48059ec69156a0a718428aeb4b

The signature record retains Duho's digest statement and its UTC. Custody/protection receipts record ordinary-read denial, developing-account admin status, the deny-delete ACL qualification, and GH006 rejection of a non-fast-forward push with unchanged tip. They do not independently establish the future approval witness or continuous protection/custody. The run record correctly distinguishes the pending pipeline amendment and adapter from completed work. This review does not judge or approve the pipeline amendment.

Future approval, collection, identity freeze, adapter execution, pipeline adoption, development and one holdout are legitimately prospective. Their absence alone is not a pre-commitment defect. Claims that the enforcement already exists are the problem.

Still missing for pre-commitment approval — clause substance, requiring matching code, updated pins and adversarial tests:

“Retain the complete matching GitHub event and its retrieval provenance without discarding fields, together with the exact approval commit and record digest. Verify repository, ref, commit inclusion and server created_at before T_pulse. State the actual bounded API availability and latency; obtain an independent retained receipt while the event is queryable. API delay never authorizes a new approval, timestamp, round or source. The nonce proves knowledge no earlier than its actual scheduled round time; authorship and exact approval UTC remain attested.”

“Collection starts under a predesignated witnessed procedure. Every attempt, input record and verdict, including RETRY, refusal and later conflicting ACCEPT, is retained in order. The first admissible collection result is durably and atomically binding before another collection or build can proceed. A missing, reset or inconsistent history after initiation fails closed. The identity and downstream witness bind this history; later NIST recovery never selects another source. Failure to execute the procedure closes or files the same commitment without redrawing.”

“Fallback requires a served, live-equal NIST pulse whose timestamp and identity match T_pulse and whose specified authentication checks fail. A different or absent pulse is RETRY, not positive failure evidence.” If a different intended eligibility rule is chosen, state it explicitly before approval.

“The adoption file must equal the approved digest in the verified approval commit, be pushed under the required witness, and remain byte-bound at identity use. The driver rejects any identity without an ACCEPT outcome and validated V18 approval, collection-history and adoption bindings; a seal alone is insufficient.”

“Only the V18 builder and driver named in E3 may execute this amendment. The adapter emits the canonical sentinel only for a journalled renderer refusal and reconciles refusal causes, manifest rows and sentinel counts before tuning. Every refused object remains in its original denominator.”

Correct the contradictory/stale prose and missing-test claims listed above. These are concrete unresolved requirements; the current passing suites do not make them implemented.

E3 hash inventory — every row MATCH. Paths use B/C/F as defined above.

| File | SHA-256 |
|---|---|
| BEACON_V2_OBSERVED_BEHAVIOUR_20260906.md | c68d49e22427a328ce090b615c8bf715eb1e8f11b0bfdd503e18916dbbf7f858 |
| B/_digicert_intermediate.pem | 6601f41fceefbe7523a6a2e746938de57fc24e99426b7bea58d1867dbee1be5e |
| B/_sample_certificate.pem | c342339ca0fe5f1c522e03471b32811310371c3adbb8f107c8d77b5f336bfce9 |
| B/_sample_pulse_last.json | 08f07600adf6ae1d1655aac33f6976d48798a3de66153a4d92df78560ca828d9 |
| B/beacon_record.py | 023c4d7dfd18d2d6818ea09d41e78b44835dc95d20ff4ba69f36c0afd61bbb73 |
| B/beacon_record_expedited.py | 570f50721c28098034da2e7eb2ef249845c8333e9e05c051be8153d741147b00 |
| B/drand_round.py | 3403aee0d5d8c57ba0878bc5b716000faf93eab7a0fba0c7613613a501300882 |
| B/negative_probes.py | 839f6f54b165fb879fdf4f3699e425728737340c8662948c29ee79941d76dd0c |
| B/negative_probes_receipt.json | 53ff8213c34435c7c093324218597bbc9355ac68b0c42f02bd887c9efdb0fd22 |
| B/nist_pulse.py | c725dd6ab4830a2dc709e55195507c1739250851498f3384dfd10c8732b43cb9 |
| B/observed_behaviour.py | 0911dfb87778a54efc1bef552d50d0d4d8cf2ee6a50046a4070ddf05c5145be0 |
| B/pinned_root_DigiCertGlobalRootG2.pem | 5d550643b6400d4341550a9b14aedd0b4fac33ae5deb7d8247b6b4f799c13306 |
| B/test_beacon_record_expedited.py | ff38dafc995a419a2d9f9f061aea8f0438308b61f093db55729442952d7824b7 |
| B/test_beacon_v2.py | c8689eef76e8f035fed12d3f61c3ecd5c11eaa695b1e16b31c9f77e81ed83e38 |
| B/test_pki.py | a7a9c85347db34e20f207380972a72703e322bad6790672df02fb3114b682c47 |
| C/build_corpus_identity.py | 3090af770f0329beddb2d8b64acae6d4a1b1da06025e616b6fb145bff47ca46c |
| C/build_corpus_identity_v18.py | 705319a53a2f65f24475dc7862583581f54500fd9d80596eeb855d29493f3c56 |
| C/build_guarded_pool.py | e9b00ef4f50ce93c980cf6c5e0581276c46e6fa9a56ed46daa6d4eb95d2f52f3 |
| C/dryrun_identities_to_exclude_20260905.txt | 77b29eafe18e02d4dee621a6e748e8f698381c6e23098e7db2db190aee270c95 |
| C/guarded_pool.csv | 2cc94a29562270fcb5043f4ce942e303696f359b5fb0c59fdee48578ebb34155 |
| C/test_build_corpus_identity.py | 2cd65283a1e227cd0511f5c7fc1135ec0b365cb76a9608ed94e988ed3148440c |
| C/test_build_corpus_identity_v18.py | 86b2ac9b17504383fc5340147c14c5af83b16b6d747c832c1a1e6ed2424e9e33 |
| F/env_lock.json | 4e2c851fe1f22f4bc28f121cf3ff4326f036be57fc100b34af9e5501d6c74251 |
| F/fourier_chirality.py | a026fe5fa168ca1eb2056829d86fb549dec4a61596b5d122f60c2a389e2d98a2 |
| F/run_configurations.py | d486ae58f40d220e8d2a9a1d875e008059cdc3bb1d9aee0dffc7dc974c7d53aa |
| F/run_configurations_v2.py | 32815edf7792452e855d2b186ff30ae1d67f904c3c0d274673c58a9b990ecffe |
| F/test_fourier_chirality.py | c30b3af46b3a855c499469c4249e487a765c7015b46126291cc7a4c134072811 |
| F/test_run_configurations.py | 2fa83512b36788345541e84ff013c4f5ae3a9a9a5f0df0cbacc4b519945707f1 |
| F/test_run_configurations_v2.py | 77c9b62d5e7d4b03f6b8a7c376d79c9d3d351acf8e206058b7792d89fd0f8cd5 |
| F/w_chi_vendored.py | 89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75 |
| scratch/survey-bricks-dr9-north.fits.gz | 2edd5c295fdad26852c6f224a3ff023cff43dd0e03a53acd35b767e726ee72fb |
| validation_bricks/_bricks_without_r_coverage.txt | ba2eb9d16d0d1d47eef2e0d52497b56d44ac979ebe67dd54b33f57c117d7a2fe |

Additional §3b pins, both MATCH:

- C/approval_witness_v2.py: d52b594665e8d773615d76dce69175088d0da24a60e65dd2a5c1a8bc3461af04
- C/test_approval_witness_v2.py: 98e10e8b53876a7f5b473c0c711064397b0411bea7c54259d4b605c2b17b7c47

VERDICT: NOT-SIGNABLE

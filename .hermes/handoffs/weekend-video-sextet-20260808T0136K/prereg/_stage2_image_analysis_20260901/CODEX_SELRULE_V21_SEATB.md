ACCESS_SHA=1906d0bb717faa0b408188b33629fdf931363c093d4d5d0dbfdda475f64adbca

Independent Seat B review of OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V21_20260906.md only.

Authorship disclosure: the supplied record attributes earlier builder field-validation work (00:13–00:18 on September 6) and coordination/decision records to the Codex engine. I do not claim independence from that engine’s earlier work. V21’s new implementation is attributed to Hwao. Findings below concern inspected V21 bytes and independently executed probes; observations about the inherited builder/mapping and decision provenance depend in part on the earlier materials. I made no implementation changes.

References: D = _optionA_dev/fourier_chirality/run_configurations_v5.py; H = _optionA_dev/corpus_identity/history.py; AW = _optionA_dev/corpus_identity/approval_witness_v4.py; B = _optionA_dev/corpus_identity/build_corpus_identity_v21.py; BD = _optionA_dev/beacon_v2/beacon_record_drand_v21.py; VD = _optionA_dev/drand_only/verify_drand_v2.py. References give physical code lines; the draft’s long paragraphs occupy single physical lines.

1. Production path — V20’s specific fatal is repaired.

D:100–119 installs a concrete offline re-deriver in PRODUCTION. It calls BD.verdict with the adopted digest and approval statement, and refuses unavailable verifier imports. I executed the identity comparison: PRODUCTION.rederive_seed is production_rederive_seed = True. My temporary test protocol retained that exact function. A real-seed identity loaded through it. The supplied suite also verifies that substituting None refuses the same path.

I independently called main([...]) under unchanged PRODUCTION, using an absent identity. It returned 2 with DATA-INTEGRITY-FAIL IDENTITY-MISSING, proving execution through the environment check into load_identity. The production-size collector CLI → builder → driver fixture passed with the real re-deriver. Its events and transport are fixtures and its repository is temporary; this is not an actual production approval or draw. The CLI test alone proves entry-point reachability, not successful production selection.

No remaining fixture-only seed callback was found. Actual adoption, approval, remote witness, identity and custody artifacts are prospective prerequisites, not a reason to inject a missing implementation after approval. However, the literal approval filename in the rule fails the builder’s W4 check, as reported under item 6.

I do not find a recurrence of V20’s specific unwired-production-verifier FATAL. The findings below are [MAJOR]/[MINOR], not a claim that every production identity is intrinsically unloadable. Blanc’s same-surface-FATAL stop condition is therefore not invoked on that basis. This bounded gate nevertheless fails; it grants no V22 or further round.

2. Conjunction from committed evidence — [MAJOR], E3 and §3b W3/W4, §3c; D:227–287.

The re-derivation and several bindings are real repairs. The complete conjunction is not recomputed.

For independent probes I used fresh temporary git repositories and bare remotes, real retained round-6441924 and nonce-6441904 bodies, and PRODUCTION’s exact re-deriver. I reused fixture setup utilities for evidence construction but supplied my own mutations. Only the historical exhibit exclusion was lifted in these fixture processes. No public repository was written.

Every accepted identity below retained the real seed:
68547455ba7d5000cb4b0b7fcd48c1ab36b6881d55e3ef464989659833ef3834

| Independently constructed case | Observed result |
|---|---|
| Baseline real-seed identity | ACCEPTED |
| Approval record path absent | APPROVAL-RECORD-MISSING |
| Push event dated 2098 | IDENTITY-WITNESS-LATE |
| Witness nonce −1 | APPROVAL-NONCE-LINE |
| Zero event digest | EVENT-DIGEST |
| Beacon record omitted from fresh freeze commit | BEACON-RECORD-NOT-IN-WITNESS-COMMIT |
| Coherently rebound look-alike relay URL | BEACON-RECORD-RELAYS |
| Re-encoded retained bodies, with matching record/history digests | ACCEPTED, correctly the same seed |
| Deleted/recreated two-entry history, with consistent lock/count/digests | ACCEPTED |
| Fabricated event, coherently recomputed digest and invented provenance | ACCEPTED |
| Second V21 approval-record path committed and pushed | ACCEPTED |
| Arbitrary ordering/renderability claims and negative tuning objids | ACCEPTED |

The event forgery set created_at to 2000-01-01T00:00:00Z, id to “invented,” repo.name to attacker/unrelated, provenance endpoint to https://attacker.invalid/events and retrieval time to “not-a-time.” Recomputing the adjacent event digest was sufficient. D:251–263 checks internal consistency and presence, not GitHub provenance, repository identity or an authentic earliest event. A later freeze proves those asserted bytes were committed; it does not establish a pre-pulse server timestamp. Production AW.github_events obtains real API data, but the driver does not establish that the identity’s event came from that path.

AW:104–105 implements the first-approval path-set check. D does not call it or reproduce it: D:237 checks touches of only the selected record. My second approval path passed load_identity. The supplied fixture repeatedly adds distinct approval paths, which also masks this omission.

Additional scope distinction: D:202–205 and 308–312 still trust claimed pool/exclusion hashes, ordering/renderability metadata and the selected lists beyond size/type/disjointness; they do not reconstruct the split from catalogue bytes. The negative-objid probe passed. This is an inherited driver limitation, not a newly introduced V21 defect to repair silently, but E3’s validation wording and the “FULL conjunction” claim must not conceal it. Likewise, offline relay labels and bodies prove valid signatures under the pinned key, not independently authenticated transport from two physical hosts; the driver does not reproduce the builder’s live confirmation.

3. History — [MAJOR], §3c; H:15–40,55–75; B:49–58,90–109,126–161; D:275–290.

The chain detects ordinary interior edits, deletions and reordering when subsequent hashes are left unchanged. It rejects a second genesis within the same chain. Genesis for another approval is refused by the builder and driver bindings. I also ran an actual two-process first-accept race: exactly one builder-accept was appended. This is stronger concurrency evidence than test_history’s sequential two calls. Cooperative appenders on the same intact file serialize correctly.

The history is not authenticated against reset. Its genesis names public approval data; the approval record does not bind a genesis hash or externally witnessed history head. Before the freeze I deleted the history, recreated genesis for the same approval and appended only a matching builder-accept. Updating the identity’s count, digest and first_accept and committing these bytes produced ACCEPTED. No cryptographic break or remote-history rewrite was needed.

A suffix deletion also passes H.validate: removing the last entry left a valid one-entry genesis prefix. Editing the terminal entry and coherently rebuilding links is similarly unprotected without an external expected head. A reset after an unchanged freeze is caught by digest comparison; that narrower protection does not establish completeness before the first freeze. H.genesis also tests existence before taking the lock, so concurrent initialization can create a second genesis and denial of service; the second genesis itself does not pass validation.

CLOSED is persisted but not enforced as terminal. I appended a genuine-shaped witness-closed entry, updated the identity’s history count/digest and sealed it. load_identity still accepted. H.first_accept ignores this stage, and D’s conflict check does not reject it. Logging a closure is not the promised irreversible closure.

“Every path” is false. B’s BaseException wrapper covers _validate_inner only. I executed:
- Missing required beacon validation arguments: BEACON-VALIDATION-ARGS-MISSING, history unchanged.
- A full build with valid evidence but an output path occupied by a file: FileExistsError after validation; last history stage builder-verdict, no builder-error.

B:151–207 catalogue, control, classification and output failures lie outside that wrapper. Collector argparse also executes before its logging try block (BD:118–136), so argument failures escape the sidecar. Existing pre-parse, witness-pending/closed and validation-exception fixtures pass, but do not cover these boundaries. Pregenesis sidecars are not authenticated or reconciled by D.

4. URLs and nonce — substantive repairs, with one remaining exclusion gap.

VD.verify uses exact pinned-URL membership; BD filters URLs before counting them; AW verifies nonce bodies through that verifier. None, host look-alikes and suffixes are refused. The independently coherent look-alike-record attack reached BEACON-RECORD-RELAYS rather than merely failing an unrelated stale lock digest. I found no path in these verifier functions that counts such a URL.

AW:107–117 and D:265–269 enforce the exact nonce set, scheduled lower bound, position before the seed round and at least two retained BLS-verifying bodies. The real-nonce and invalid-nonce tests passed. The predecessor scheduled before MIN_T_SIGN is refused.

[MAJOR] The gate brief’s statement that nonce fixture round 6441904 is excluded by name is false for the pinned implementation. BD:27 excludes only 6440756 and 6441924. With exclusions unchanged, I executed collect/verdict for 6441904 using its retained public body, T_sign 2026-09-06T09:39:00Z, and obtained ACCEPT-DRAND. This is a verifier-boundary probe, not a complete production identity or authorized study seed. An authentic future approval would prevent selecting this historical round; nevertheless, the stated named exclusion is missing and should be explicit.

5. Property wording — [MAJOR], §3b lines 32–33; BD:55–60,95–110.

C1 and C2 honestly demonstrate their particular inputs: adding a JSON field with an unchanged signature string is accepted; tampered signatures lose quorum and return RETRY. Both exhibit runs produced:
EXHIBIT OK: True
EXHIBIT-DIGEST: 2160fa754ce3db25613389d58bacd3098763ea8536744558e9dae96c5b4f0ae1

But signature equality is string equality. I changed only the hex letters of the live signature to uppercase. The decoded signature bytes, BLS verification and seed were unchanged. The actual unmocked code returned REFUSE-CONFLICTING-VALID-SIGNATURES and claimed a different signature contradicted uniqueness. Thus that branch is reachable without simulation or any key defect. Compare decoded canonical signature bytes, not their textual encodings.

The operative paragraph at draft line 33 still requires EQUAL live bytes, names REFUSE-LIVE-DIFFERS-BUT-VERIFIES, and calls verifying different bytes impossible. This directly contradicts line 32 and the V21 code. It also names the old verifier and six-test beacon fixture as current evidence. These are surviving V20 defects, not marked historical quotations.

[MINOR] State the seed consistently as lowercase hex SHA256(decoded signature), as VD computes it; lines 32 and 57 call the signature itself the seed. Also make timing and uniqueness explicitly conditional on the threshold/key/cryptographic assumptions. Verification alone is not a proof that a value could not have been released early. For the chained scheme the message includes previous_signature; VD does not independently verify the entire predecessor chain. No threshold break was attempted or exhibited by this review.

6. Adapter reconciliation, text, counts and preservation.

[MAJOR] §7, draft line 52; D:330–342: reconciliation now checks sentinel/refusal identities both ways, but the promised completion/count and cause requirements are incomplete. An entry with only objid, REFUSED, sentinel:true and the sentinel digest passed my probe with no refusal cause and no render-end. The count is checked only if an end exists. This permits an incomplete journal to satisfy the asserted prerequisite.

[MAJOR] §3b W1–W4, draft line 33 versus B:15 and AW:104–105: the rule instructs writing APPROVAL_RECORD_SELRULE_V20_<date>.md, while the production builder searches APPROVAL_RECORD_SELRULE_V21*. I created and pushed the literal specified V20 filename in a fresh test repository. AW returned APPROVAL-NOT-FIRST with an empty matching path set. Fixtures silently use the V21 name. This is a concrete executable-instructions mismatch requiring correction before approval, although the underlying implementation works with the correct V21 name.

The current §3c cost paragraph correctly removes NIST, the old “tried once” behavior, unverified-BLS provenance and the stale L3 cross-reference. Historical NIST/V16 references remain elsewhere and are appropriate when explicitly historical. The byte-equality paragraph and old current filenames at line 33 are not appropriate history. The checklist/change record’s blanket “REPAIRED” statements for M1, M2, X, S and T overstate the evidence above.

Executed validation, all with PYTHONDONTWRITEBYTECODE=1:
| Run | Result |
|---|---|
| test_verify_drand_v2, supplied venv, -W error | 4, OK |
| test_beacon_record_drand_v21, supplied venv, -W error | 7, OK |
| test_history, /usr/bin/python3, -W error | 4, OK |
| test_approval_witness_v4 + test_build_corpus_identity_v21 + test_build_corpus_identity, supplied venv, ResourceWarning-strict | 3 + 8 + 4 = 15, OK |
| test_run_configurations_v5 + test_run_configurations, pinned interpreter plus supplied site-packages, ResourceWarning-strict | 22 + 17 = 39, OK |
| Additional test_fourier_chirality | 10, OK |
| Property exhibit V21, twice | Both identical digest above |
| Additional exhibit_drand_only.py | OK; 45d6149a2ccf30cb167dc4331455f3403a733516a82399292b1e7ad2c029e531 |
| signature_preimage.py V21 | 1906d0bb717faa0b408188b33629fdf931363c093d4d5d0dbfdda475f64adbca |

The requested aggregate is 69 tests, with no skips reported. The additional estimator suite brings executed unit tests to 79. One RuntimeWarning occurred at fourier_chirality.py:87; no ResourceWarning appeared. The advertised new suite counts are correct. The twenty-five author mutations are present and passed their expected refusals; these do not establish resistance to my coherent substitutions.

Pin audit: all 58 distinct file-content digests appearing in E3/§3b/§3c matched their retained files, including new and superseded drivers, builders, verifiers, witnesses, history, tests, exhibits, nonce bodies, environment lock, guarded pool, exclusions, survey-bricks table, no-r registry and retained beacon/PKI evidence. The other two full digests in those paragraphs are generated exhibit payload digests, both reproduced above. No missing file pin was found.

The filed normal-format diffs reproduce exactly:
V20_TO_V21.diff = 26cbbb3caa8f6460594cbbed4b5536fe7d6980d476cdf17d8c398b030e4fe95b
V15_TO_V21.diff = 8baf6b4c95a7b45ef9a67d3919b8243aaefe4c90a34eb82fdcd3ea946ad65e45

V15 remains byte-identical at fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1. Its retained RETRY record matches 1c1d9d4bacc35319e91d46420b8f892e1126cc48059ec69156a0a718428aeb4b. V20 remains 1c8ce522ac07572f22858f2ec6980b6a436f2e4ba580f7b6351ca2e8acee77d1, and superseded implementation pins match.

The inherited E1 count is honestly corrected in a labelled annotation: the old fixture has 17 tests. Protocol.holdout_once defaults False and the supplied test demonstrates the prepared True behavior and retained repeatability under the default. Neither is silently adopted. The fixed sample sizes, floors, bar, exclusions, one-holdout covenant, custody/protection and §6 scientific pipeline substance remain preserved; the explicitly authorized source-design supersession is separately stated.

The checklist and reproduction document exist and describe the required before/after order. Current execution supports their narrow missing-callback diagnosis and repair; present files cannot independently prove the historical clock ordering of author edits. The copied Codex decision record is now available and records a source-direction decision, not final-byte approval.

Guarded-pool reconstruction from the absent GZ1 source table: UNVERIFIABLE HERE. Retained-pool hash equality and the builder’s control are not an independent reconstruction of that population.

7. What remains necessary before pre-commitment approval — clause substance, supported by matching implementation and evidence.

“Production acceptance shall establish W1–W5, including the unique approval-record path and an authentic qualifying server event for the pinned repository/ref/commit. A self-supplied event and adjacent digest/provenance shall not establish chronology. Retained evidence shall have a defined independently verifiable provenance; otherwise that limitation shall be disclosed and resolved before approval.”

“History shall have an externally witnessed initial state and ordered continuation that cannot be reset before the first freeze. The driver shall verify that continuation, enforce terminal CLOSED, and reconcile pregenesis failures. Argument, validation, catalogue, control and output failures shall be recorded. Locking shall cover genesis initialization and first acceptance.”

“Same-signature equality shall compare decoded canonical signature bytes. The seed shall be lowercase hex SHA256 of those bytes. Different JSON or hex encodings of that same signature are not conflicting valid signatures. Timing and chained-message uniqueness claims are conditional on the stated trust assumptions. All operative paragraphs, filenames and refusal tokens shall agree.”

“Historical fixture rounds 6440756, 6441924 and 6441904 shall be explicitly inadmissible as study seeds. The actual approval-record filename shall match the production V21 path rule.”

“Sentinel reconciliation shall require a completed render journal with the matching final count and a retained renderer refusal cause for every sentinel, in addition to bidirectional object matching.”

The inherited split-reconstruction limitation should be disclosed for Duho’s separate decision, with any prospective enforcement change clearly labelled; it must not be silently represented as already recomputed by this amendment.

Actual final-byte approval, adoption/push evidence, collection, custody and freezes remain prospective. Their ordinary absence is not the reason for refusal. The unresolved executable and evidentiary defects above are. No study seed, production approval, publication, render or pixel access was performed. Only this report was written in the reviewed directory; executable probes used temporary locations outside it.

VERDICT: NOT-SIGNABLE

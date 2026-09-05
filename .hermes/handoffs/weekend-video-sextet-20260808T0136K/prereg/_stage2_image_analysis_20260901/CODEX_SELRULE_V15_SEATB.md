ACCESS_SHA=fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1
VERDICT: SIGNABLE-AS-PRECOMMITMENT
AUTHORSHIP: This codex engine authored the earlier builder field-validation code at 00:13–00:18. As V15 states, that code no longer participates in acceptance; `beacon_v2/` and the current builder beacon boundary are Hwao-authored. Findings that depend on the surviving builder code are marked [CODEX-AUTHORED DEPENDENCY].

1. [MINOR] ACCEPTANCE SET.

No builder-accepted record outside the stated set was found. `build_corpus_identity._validate_beacon_record` installs a live network fetcher when none is injected, calls `beacon_record.verdict`, and accepts only an outcome starting with `ACCEPT` (`build_corpus_identity.py:44-61`) [CODEX-AUTHORED DEPENDENCY]. It reads no recorded check, verdict, acceptance boolean, or seed; the accepted seed is returned by the recomputed verdict.

For NIST, `beacon_record.verdict` decodes the retained evidence and calls `nist_pulse.authenticate` (`beacon_record.py:63-65`). With live fetch, lines 66-70 compare all four retained inputs—`pulse_body`, `leaf_pem`, `next_body`, and the complete ordered `intermediate_pems` list—with a fresh `nist_pulse.collect`; inequality returns `REFUSE-NIST-LIVE-DIFFERS`. `nist_pulse.authenticate` recomputes timestamp, chain/URI, status, certificate identifier, output binding, retained-chain trust/SAN/time, pulse signature, and next-pulse precommitment (`nist_pulse.py:89-108`).

For drand, after 24 hours `verdict` freshly collects and authenticates NIST and voids fallback if authenticable (`beacon_record.py:81-86`), derives the round, recomputes retained agreement, freshly collects all four pinned relays, recomputes live agreement, and accepts only if both agreements have at least two pinned hosts and identical randomness (`beacon_record.py:87-97`; `drand_round.py:18-28`). Unpinned record keys are ignored. Thus “retained bodies and live” means agreement independently recomputed from both sets of raw bodies; exact retained/live drand body equality is neither promised nor needed beyond round and randomness agreement.

`test_zzz_every_token_is_exercised` genuinely enumerates every outcome token the current code can emit: all `REFUSE-*` literals extracted from `beacon_record.py`, plus `ACCEPT-NIST`, `ACCEPT-DRAND`, `RETRY`, and `UNAVAILABLE` (`test_beacon_v2.py:81-83`). It proves outcome-token coverage, not full branch coverage; all tokens were produced in the 19-test run.

2. [MINOR] REPAIR AUDIT OF EVERY V13 FINDING (BOTH REPORTS).

- Live NIST re-check omitted intermediates (codex FATAL): V15 §3b says the fallback is void when NIST is authenticable through its two-link chain and that live comparison includes `intermediate_pems`. Code: `beacon_record.py:66-70,81-86`; `nist_pulse.py:50-62,89-108`. `test_beacon_v2.py:59-61` exercises the V13 fallback defect, and lines 39-41 exercise V15's retained/live issuer equality.
- Four-relay wording/code mismatch (codex MAJOR): §3b now says at least two of four pinned hosts, with unpinned keys ignored. Code: `drand_round.py:20-28`; `beacon_record.py:87-97`.
- Branch-incomplete probes (codex MAJOR): §3b pins 19 tests ending in outcome-token enumeration and 23 probes. Code: `test_beacon_v2.py:81-83`; regenerated probe receipt has 23 rows. This is accurately outcome-token coverage, not a claim of full branch coverage.
- Obsolete deterministic draw remained operative (codex MAJOR): §3a says it is “SUPERSEDED and NON-OPERATIVE.” The operative builder seeded walk is `build_corpus_identity.py:87-95` [CODEX-AUTHORED DEPENDENCY].
- Stale fetcher documentation (codex MINOR): §3b describes the rebuilt modules; `beacon_record.py:2-11`, `nist_pulse.py:50-63`, and `drand_round.py:2-5` agree with the implementation.
- No independent normative NIST vector (codex MINOR): §3b and behaviour-record limit 5 disclose that none exists; no stronger claim is made.
- Test-only bare seed (agy MINOR): §E3 says TEST-SEED identities are refused in production; `build_corpus_identity.py:69` requires `test_seed`, and the production driver rejects the resulting split mode [CODEX-AUTHORED DEPENDENCY].
- Earlier self-signed-leaf, recorded-precommitment/flag, invented-relay, wrong-round, caller-time, witness-blob, fixture-count, observed-defect, and test-root concerns are repaired or expressly bounded by §3b/E3; relevant code is `beacon_record.py:28-97`, `nist_pulse.py:72-108`, `drand_round.py:18-28`, and `test_pki.py:19-55`.

3. [MINOR] FIXTURES.

No fixture asserts that the observed live NIST defect must persist. `test_live_sample_regression_observation` requires the stable anchor/output/certificate-id/key-size facts, permits either signature result, and conditionally checks non-acceptance only when signature verification is false (`test_beacon_v2.py:73-76`). No accepted record is hand-built: positive NIST and drand records originate in `beacon_record.collect`; the hand-made two-field record is refusal-only. The test PKI is genuinely three-tier—leaf → intermediate → root (`test_pki.py:19-29,39-50`)—matching the production chain shape. Tests inject the test root, but production `pinned_roots()` reads and digest-checks the pinned DigiCert root; `test_pki` is not imported by production. The substitution does not hide a production-root bypass.

4. [MINOR] §3b VERSUS OBSERVED BEHAVIOUR.

Every substantive §3b behavior statement is supported by the regenerated behaviour record, its 23-row probe receipt, or fixture output. In particular, the V15 sentence naming all four live-compared NIST inputs is supported by code, `test_live_intermediates_must_match`, and the new “retained intermediate certificate replaced” probe, both yielding `REFUSE-NIST-LIVE-DIFFERS`. The live-sample limit is stated exactly: retained pulse at 2026-09-05T15:13:00Z, anchored through a two-certificate leaf/intermediate path to the pinned root, 2048-bit leaf key, 512-byte signature, signature verification false, and acceptance false. The absent next pulse makes the sample precommitment check false/not evaluable; the text does not turn that observation into a normative vector. The disclosed limits—no drand BLS verification, hostname-only independence, live-equality as the available provenance check, and no independent normative serialization vector—match the behavior record.

5. [MINOR] §3a.

Yes. §3a unambiguously makes the beacon-drawn third block operative and calls the old deterministic ranks-2,601 draw “SUPERSEDED and NON-OPERATIVE,” retained only as excluded dry-run history.

6. [MINOR] RUNS AND EXACT OUTPUTS.

- (a) Exit 0. Output included two expected argparse refusal messages, 27 dots, `Ran 27 tests in 12.017s`, `OK`, and `validation ranks 1-2000 match the failed set as a set with equal labels: 2000`.
- (b) Exit 0 and warning-clean: four dots; `Ran 4 tests in 2.357s`; `OK`; then six identical `validation ranks 1-2000 match the failed set as a set with equal labels: 2000` lines. No ResourceWarning appeared.
- (c) Exit 0: 19 dots; `Ran 19 tests in 0.673s`; `OK`.
- (d) In an isolated copy, `negative_probes.py` produced 23 probe rows (plus two builder control lines and table headers). Only genuine NIST and genuine drand produced `BUILT`; all other rows were refused. Two runs produced the identical receipt SHA-256 `53ff8213c34435c7c093324218597bbc9355ac68b0c42f02bd887c9efdb0fd22`, equal to the filed receipt. Two `observed_behaviour.py` runs produced identical SHA-256 `c68d49e22427a328ce090b615c8bf715eb1e8f11b0bfdd503e18916dbbf7f858`, byte-equal to the filed record.
- (e) Direct retained-sample authentication returned `anchor.anchored=True`, `chains_to_trusted_root=True`, `san_matches=True`, `valid_at_time=True`, `chain_length=2`, `signature_verifies_under_leaf=False`, `leaf_key_bits=2048`, `signature_bytes=512`, and `accepted=False`.
- The optional guarded-pool fixture cannot run here, as disclosed: `test_build_guarded_pool` exited 1 before tests with `FileNotFoundError` for the absent `completeness_gate/artifacts_full/completeness_receipt_20260903T122712Z.json`; `Ran 0 tests ... FAILED (errors=1)`. The GZ1 table/completeness reconstruction is therefore UNVERIFIABLE HERE, not evidence of a code defect.

All E3(i) pins matched: estimator `a026fe5f...`; driver `d486ae58...`; environment `4e2c851f...`; guarded-pool builder `e9b00ef4...`; identity builder `3090af77...`; corpus fixture `2cd65283...`; bricks `2edd5c29...`; no-r list `ba2eb9d1...`; guarded pool `2cc94a29...`; estimator fixture `c30b3af...`; driver fixture `2fa83512...`; beacon record `023c4d7d...`; NIST module `c725dd6a...`; drand module `3403aee0...`; pinned root `5d550643...`; beacon fixture `c8689eef...`; test PKI `a7a9c853...`; probes `839f6f54...`; probe receipt `53ff8213...`; behaviour generator `0911dfb8...`; behaviour record `c68d49e2...`; pulse `08f07600...`; leaf `c342339c...`; intermediate `6601f41f...`; exclusion list `77b29eaf...`; vendored generator `89da33ec...`. Every full digest equals the full digest printed in E3(i).

7. [MINOR] DEPRECATED FLAG.

Exact whole-document count of the deprecated bare-seed flag name `--seed-hex`: 0.

8. [MINOR] ASPIRATIONAL / PROSPECTIVE ITEMS.

The document properly presents as future work: signature/adoption and retained signature statement; real beacon collection; corpus identity creation and journal/witness; branch-protection evidence; separate custody account and receipts; tuning, holdout, candidate and pipeline freezes; fresh-pixel fetch; and attempt 2. These are precommitments, not represented as completed. The GZ1 table and completeness receipt remain absent here and guarded-pool reconstruction is expressly UNVERIFIABLE HERE.

One harmless stale count remains in E3(i): after correctly saying `test_beacon_v2.py` has 19 tests and pinning its 19-test hash, the earlier fixture-summary sentence says “beacon fixture ... (18 tests; pinned in the BEACON PATH block).” Execution, the behavior record, §9, and the pinned fixture all establish 19. This clerical contradiction does not widen acceptance or require a code change, but should be corrected to 19 when preparing the signature copy without changing any operative clause.

9. [MINOR] WHAT IS STILL MISSING FOR SIGNATURE.

Nothing substantive is missing from the acceptance or precommitment clauses. Before signature, make only the clerical replacement in E3(i): `beacon fixture: test_beacon_v2.py under _optionA_dev/beacon_v2/ (19 tests; pinned in the BEACON PATH block)`. Then compute and state the digest of that final signature copy as the rule digest. Operational prerequisites that intentionally occur after/beside signature—real T_sign statement, beacon record, custody setup, branch-protection evidence, freezes, and later fetches—remain governed by the existing clauses and are not missing rule text.

Summary for a non-specialist principal: V15 closes the sole V14 acceptance gap. The builder now rechecks every retained NIST component—including the intermediate certificates—against a fresh live collection, independently recomputes all certificate, pulse, timing, and fallback conditions, and accepts drand only after 24 hours when both retained and live responses agree across at least two pinned relays and NIST is not authenticable. The required suites pass warning-strict, all pins match, both generated artifacts reproduce byte-for-byte, and the retained NIST sample shows exactly the disclosed limitation. The missing source catalogues prevent only the already-declared guarded-pool reconstruction in this sandbox. Apart from changing one stale “18 tests” reference to “19,” the rule is signable as a precommitment.

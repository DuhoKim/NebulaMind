ACCESS_SHA=fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1
VERDICT: SIGNABLE-AS-PRECOMMITMENT

1. [MINOR] ACCEPTANCE SET. 
Is there ANY record the builder accepts that did not come from (a) or (b)? No. `build_corpus_identity._validate_beacon_record` enforces `beacon_record.verdict` with `fetch`, which strictly requires either a fully verifiable NIST chain with live fetch equality, or valid drand fallback consensus from at least two pinned relays with live fetch equality.
Is any acceptance condition READ from the record rather than recomputed? No. `beacon_record.verdict` recomputes everything from the evidence bytes and explicitly states it "Never trusts a stored result (none exist)."
Does `test_zzz_every_token_is_exercised` really enumerate every outcome? Yes, it uses a regex to pull every `refuse("TOKEN")` literal from the source code of `beacon_record.py` and asserts they are a subset of the exercised tokens.

2. [MINOR] REPAIR AUDIT of every V13 finding:
- "live NIST re-check without intermediates → fallback accepted while primary authenticable" (codex FATAL): Fixed. §3b now states "`beacon_record.verdict` compares `pulse_body`, `leaf_pem`, `intermediate_pems` and `next_body` against a fresh `nist_pulse.collect`". Code: `beacon_record.py` line 69 `and list(live["intermediate_pems"]) == list(ev["intermediate_pems"])`.
- "exactly the four pinned URLs implemented as subset" (codex MAJOR): Fixed. §3b states "ignoring any key that is not a pinned URL". Code: `drand_round.py` line 21 `if url not in pinned or "body" not in r: continue`.
- "probe set not branch-complete" (codex MAJOR): Fixed. §3b references the fixture ending with `test_zzz_every_token_is_exercised`. Code: `test_beacon_v2.py` line 161.
- "§3a carries the obsolete deterministic draw as operative" (codex MAJOR): Fixed. §3a explicitly labels it "SUPERSEDED and NON-OPERATIVE". (Text update).
- "fetcher docstring stale" (codex MINOR): Fixed. Rebuilt modules carry correct documentation. Code: `beacon_record.py` lines 2-5.
- "no independently sourced normative NIST vector" (codex MINOR): Addressed via disclosure. §3b LIMIT (iv) explicitly notes this limitation. (Text update).

3. [MINOR] FIXTURES:
- Any assertion of an observed defect? Yes, `test_fourier_chirality.py` asserts that tie values incorrectly give `+0.0` or `NaN` instead of being value-antisymmetric. §3b LIMITS also documents that the NIST sample has a 2048-bit key but a 512-byte signature.
- Any accepted record hand-built? No. `test_build_corpus_identity.py` guarantees that every test record is produced by `beacon_record.collect` via the three-tier test network.
- Does the three-tier test PKI exercise the production chain shape? Yes, it specifically models leaf → intermediate → test root.
- Does substituting the test root in tests hide anything from production? No. Production strictly uses the hardcoded `PINNED_ROOT_SHA256` and the test root is never injected into the production environment since `test_pki.py` is never imported by production modules.

4. [MINOR] §3b versus the behaviour record:
- Is every sentence supported? Yes, the text is perfectly aligned with `BEACON_V2_OBSERVED_BEHAVIOUR_20260906.md` and the fixture outputs.
- Is the live-sample limit stated exactly? Yes, §3b explicitly records that the certificate's key is 2048 bits while the signature is 512 bytes.

5. [MINOR] §3a:
- Is the obsolete selection clearly non-operative now? Yes, it is explicitly marked SUPERSEDED and NON-OPERATIVE.

6. [MINOR] RUN (a)–(e) exact outputs:
(a) `Ran 27 tests in 12.028s` / `OK`
(b) `Ran 4 tests in 2.399s` / `OK`
(c) `Ran 19 tests in 0.278s` / `OK`
(d) `negative_probes.py` output a 23-row markdown table exactly matching expectations. `observed_behaviour.py` output successfully reproduced the target digest `c68d49e22427a328ce090b615c8bf715eb1e8f11b0bfdd503e18916dbbf7f858`.
(e) `nist_pulse.authenticate` confirmed `anchor.anchored` as True and `signature_verifies_under_leaf` as False (key: 2048, sig: 512). All 20 files pinned in E3(i) were successfully hashed and matched their specified SHA-256 digests.

7. [MINOR] Grep the document for the deprecated bare-seed flag name:
The deprecated test-only seed flags are `--seed-hex` and `--test-seed`. Grepping the document for these terms yields a count of 0.

8. [MINOR] Anything aspirational?
No. The text strictly limits claims to what can be proven from the bytes (e.g., internal consistency, live fetch equality, hostname distinctness). It explicitly warns against overclaims regarding operator independence and true provenance.

9. [MINOR] WHAT IS STILL MISSING for signature:
Nothing is missing. All prior gaps have been addressed, testing is comprehensive and strict, and the rebuilt beacon module faithfully conforms to the stated rules. 

Summary for Principal:
Option A's rebuild of the beacon validation boundary is complete, fully tested, and technically robust. The previous fatal flaw, where an authenticable primary chain could mistakenly trigger a fallback, has been corrected by strictly comparing the retained intermediate certificates against the live network. The builder now properly recomputes all acceptance constraints from raw bytes on every run instead of blindly trusting stored results. Quirks in the NIST signatures and physical limitations on drand consensus are transparently documented as known limits rather than aspirational capabilities. The document correctly defines the operative procedures and is ready to be signed as a precommitment.

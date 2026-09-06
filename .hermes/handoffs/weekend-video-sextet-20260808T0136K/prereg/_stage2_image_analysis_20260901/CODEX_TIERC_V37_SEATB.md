ACCESS_SHA=359729c28b865e2b7871bfe495bcfd3e1a48f14fa76d03671aefe322d4f49916

Seat B — fresh hostile referee, Codex.
Authorship: I authored none of the reviewed implementation or candidate text in this session. The user attributes all reviewed work to Hwao. I cannot independently establish historical engine provenance; no finding depends on reviewed code known to have been written by this engine. Supplemental probes were reviewer-written and executed in memory.

The sole candidate judged is MINI_PREREG_GZ_TIERC_DRAFT_V37_20260906.md, identified above. V35, V36's refusal, the change record, diffs, and signed option A V15 §6 were comparison evidence. No astronomical image pixels were opened, no network was used, and nothing was published. Python bytecode writing was disabled. Only this report was written in the reviewed directory.

Verification receipts:

- Required combined warning-strict suite: 97 tests, 10 errors, exit 1. The five study_renderer suites separately pass: render_chain_v2 6/6; renderer_v4 19/19; pixel_rejection_v2 6/6; renderer_v3 18/18; pixel_rejection 8/8.
- Both anchor suites execute their tests in the combined run, but each has five errors: four environment-record tests and the standalone make_event test. All ten terminate at instrument_identity_v4.py:83: “INSTRUMENT-INTEGRITY-FAIL: venv_torch interpreter absent”. Thus this sandbox does NOT reproduce either claimed 20/20 receipt. This is an environment limitation, not evidence that zero-exposure carriage failed. No environment was fabricated or substituted.
- From miniprereg_pins, both warning-strict invocations of test_pin_consistency_v2 run 26 tests and pass, identically.
- build_register.py --check: “REGISTER CURRENT: 248 clauses”; --audit: “248 register entries ... AGREE”.
- check_pin_consistency_v2.py: 70 parsed pins, 25 superseded siblings, “RESULT: CONSISTENT”.
- signature_preimage.py prints exactly 359729c28b865e2b7871bfe495bcfd3e1a48f14fa76d03671aefe322d4f49916. Both actual signature fields are blank.
- Fresh ordinary diff output is byte-identical to both supplied diffs. V35_TO_V37.diff has 48 added/deleted content lines and SHA-256 0edacfa2876f7d76718ab2cbc1a7a4d0fa02e6b9e0a8203a9a8c8d597326be06. V36_TO_V37.diff has 40 such lines and SHA-256 cb106de02b611b2cd75010d5b8cbc341699a3ccaeba8ca61e5a1ed73fed1a047. These are ordinary diff files, not unified diffs.
- Recomputed all 70 parsed file hashes individually: every one matches. Independently enumerating the other full SHA literals found three additional historical file pins omitted by the checker; all three also match. Thus all 73 explicit file pins verified. The parameter-only serialization digest in §9.1(a) is a separate derived object, not another file pin; I did not deserialize weights to reconstruct it.
- Additional omitted pins verified: anchor_gate/renderer_parity_fixture_v3.py = a67fbb27717069f1cb10cd70f0740ecb63bdfe0869943e2b7c891fffec503221; anchor_gate/instrument_identity_v3.py = d63397324987d359dd4bb41cdc923ebdf2a8890b75a69f03d582641bde0166e4; anchor_gate/test_anchor_gate_v3.py = ea17bc9aba217ef0775f614e6c6b179d5e6c617e41fccdc4d56277ab5ffd1d79.
- V35's retained pixel_rejection.py is unchanged at 8f66bc1c61173648f11386eb17f2d5afd3c3f1a338aee5bf3e11fe9aad950818; renderer_v3.py is unchanged at a2e293c2964abdae781fe3fd408e05c304803cdde14578ad1c1f1ea6229fc54c.

1. [FATAL] END TO END: the V36 integration failure is repaired, but V37 does not implement its main-path protected region exactly.

render_chain_v2.render_object executes the relevant sequence: validation at line 24; source replacement at 25; v4 reprojection at 26; output flags at 30; MEDIUM count at 32; refusal at 35; binary64 peak at 38; normalization and little-endian float32 tensor at 42–46. pixel_rejection_v2.py:16,26–41,54–59,67–94 implements the five rejecting bits, zero-exposure union, plane checks, lower median, replacement, nearest-neighbour output predicate and MEDIUM count.

The required counterexample is repaired. Using the contained 180×180 synthetic source from test_render_chain_v2.source, with nexp[26,26] = 0 mapping to output (0,0), render_object returns SCORED, F=1, n_zero_exposure_source=1, medium_count=0 and 65,536 tensor bytes. Passing the same cleaned image and unchanged integer planes directly through renderer_v3 raises DATA-INTEGRITY-FAIL. renderer_v4.py:216,239,278 changes the old <=0 checks to <0.

However, §8.12 explicitly preserves “the §8.14 radius formula on the main path”; §8.14 gives r_T = min(64,max(23,2*shape_r/0.262)), without integer truncation. protected_region.py:35 returns int(...), and render_chain_v2.py:22,35 truncates again.

Executed counterexample: shape_r=3.1309 gives prescribed r_T=23.9. Put one zero-exposure source pixel at (66,89), mapping to output (40,63). Its distance from (63.5,63.5) is 23.50531854708632: inside the prescribed T. The helper returns 23; even passing 23.9 directly to render_object returns SCORED, F=1, recorded r_T=23. §8.14a requires REFUSED. This is an actual false acceptance through V37's sole consumer. The defect in protected_region predates V37, but the new consumer repeats it and V37 expressly claims exact preservation.

[MAJOR] The flag rule executes literally, but its claimed protection is false. §8.9d defines nearest-neighbour flags; unchanged §8.14a says carriage “spreads a rejected source pixel across up to four output pixels” and counts “what the contamination actually touched”. The integer flag does not follow all bilinear image contributors.

Executed fractional-WCS counterexample: use the same source, subtract 0.25 from both WCS CRPIX values, and set nexp[67,82]=0. The only output flag is (41,56), outside T=23. Comparing clean-source and unreplaced-source renders shows changed values at (41,56), (41,57), (42,56), (42,57); the last two are inside T. render_object nevertheless returns SCORED, F=1. This follows renderer_v4.py:205–218 versus 220–244 and pixel_rejection_v2.py:86–89. It does not contradict §8.9d's literal nearest-neighbour predicate; it contradicts the broader §8.14a assurance. The amendment must state which protection it actually freezes.

[MAJOR] Precision and validation claims also need precision. §8.9 says reprojection accumulation “is materialized once as float32”; renderer_v4.py:191,282–289 returns and hashes a float64 raster, and the new consumer first casts to float32 after normalization at line 42. Specify that boundary explicitly. Also, §8.17a attributes refusal of non-integer planes to the renderer, whereas line 260 checks only the exposure dtype. A float64 maskbits plane containing integral values renders successfully directly; the production consumer correctly rejects it through pixel_rejection_v2._integer. Attribute that guarantee to the consumer.

There is no other AUTHORIZED production render path: §8.15b expressly requires this function. scripts/stage2_render_validation.py:15–16,68 still imports the old helper/renderer and refuses any nonpositive output exposure. That script exists but using it under V37 would violate §8.15b. The reviewed function returns a tensor; it does not invoke §9's instrument. Its SCORED token must not be mistaken for evidence of an instrument score.

2. [MAJOR] REPAIR AUDIT OF V36 ITEMS 1–6.

1 — REPAIRED for the specific fatal integration defect and helper qualifications. V37 §8.17a: “an exposure count of ZERO is CARRIED”; renderer_v4.py:216 reads “if plane_index == 2 and value < 0”. §8.9a: “a NEGATIVE value in either ... planes of differing shape, and a non-finite image value”; pixel_rejection_v2.py:28–41 enforces those conditions. §8.15b: “The consumer that executes this order is pinned”; render_chain_v2.py:24–42 executes it. The old counterexample now succeeds. The distinct main-radius defect above remains.

2 — REPAIRED. §8.15b now requires receipts “through the actual renderer”; test_render_chain_v2.py:34–69 exercises outside-T success, old-renderer refusal, inside-T refusal, 819/820, and MEDIUM. Old-behaviour substitutions fail, as quantified in answer 6.

3 — PARTLY REPAIRED / NOT REPAIRED in full. §8.10 now says rejection is keyed to “published integer maskbits and integer exposure-count planes”; pixel_rejection_v2.py:56–59 implements their union. §2.16 adds eight replacement rows and the introduction identifies the retained V35 modules as historical. But the complete/exact supersession and checker claims still fail the checks in answer 3.

4 — NOT REPAIRED in full. §17.1 now specifies approval “in the codex conversation”, external approval UTC, and BOTH fields left blank. signature_preimage.py:32–40 is compatible with today's blank bytes. But §17.3 still permits writing into the signature block and misdescribes what the helper excludes; see answer 4.

5 — REPAIRED for the formerly absent consumer and validation controls; NOT REPAIRED for exact main-path bounds. §8.12 now distinguishes the main formula from validation's 23; render_chain_v2.py:35 calls the shared refusal function, and the integration controls execute. Yet int(r_t) violates that main formula. The MEDIUM TUNING perturbation study remains a future disclosure under §8.9b, correctly not an outcome-dependent gate.

6 — NOT REPAIRED as a complete signability checklist. New pinned executable integration, hardened source checks, exposure-aware §8.10 and the channel description address most demanded amendments. The residual signature contradiction, radius false acceptance, and exactness/custody defects in this report prevent closing the item. This item was a list of necessary repairs, not a separate implementation module.

3. [MAJOR] SCOPE AND CONSISTENCY: the register agrees, but the edit list and checker guarantees are not complete.

Independent comparison of numbered clause blocks gives exactly:
§2.11, §2.15, §2.16, §8.9a, §8.9b, §8.9d, §8.10, §8.12, §8.15b, §8.17a, §8.17a-iv, §8.17a-iii, §17.1, §17.3, §17.7.

[MINOR] The supplied thirteen-clause list omits §8.17a-iv (initializer hash) and §8.17a-iii (fixture reference). Calling §8.17a a family would cover them broadly, but it is not the complete exact clause list: the register separately indexes these subclauses. Other differences are the banner/amendment insertion and spacing, generated register, signature fields and VERSION. There are no further numbered-clause changes.

No operative clause retains the six-bit enumeration, maskbits-only keying, or the old blanket positive-exposure requirement. Historical mentions are distinguishable from current rules; §7.7 release absence is a different test. The approval channel is updated, but a live signature-block instruction survives in §17.3.

The supersession table is not literally “every replacement”: it omits study_renderer/test_renderer_v3.py -> study_renderer/test_renderer_v4.py. Its earlier renderer-fixture replacements are also not comprehensively recorded. Several newly superseded files lose their individual hashes in V37 despite §2.16's retention promise and §8.17a-i's “Every retention claim ... carries a full digest” assertion—for example test_pixel_rejection.py, renderer_parity_fixture_v4.py, test_anchor_gate_v4.py, renderer_parity_fixture_spec.md, check_pin_consistency.py and test_pin_consistency.py. Their old pins remain recoverable from V35, but V37 must explicitly say that is the retention authority or carry them itself.

The checker has two demonstrated limits despite CONSISTENT:
- It omits the three bare historical pins listed in the verification receipts.
- imported_modules at check_pin_consistency_v2.py's ImportFrom branch records node.module but not imported aliases. It misses “from study_renderer import renderer_v3 as rv3” in test_render_chain_v2.py:11 and the old pixel_rejection import in test_pixel_rejection_v2.py. Those are deliberate comparison imports, permitted by the introduction, not clandestine production use. But the checker has no explicit comparison-only exemption; its generic claim to catch every such import is false. The same syntax could conceal a production stale import.

No stale superseded renderer/helper import was found in the new production chain itself. Mechanical register agreement does not resolve any of these semantic discrepancies.

4. [MAJOR] §17: channel repaired, immutable-approval rule still contradictory.

§17.1 describes the requested channel and accurately distinguishes byte agreement from speaker authentication. Both fields are currently blank. §17.7 orders approval, attestation/relay, independent recomputation, and freeze record. I do not attest that approval has occurred.

But §17.3 says: “The line after DUHO SIGNATURE: in the file may carry the digest and UTC as stated because verification replaces that entire line with the blank form before hashing.”

That contradicts §17.1's blank-field instruction. Read literally as the following physical line, it is also false: signature_preimage.py:39 replaces only the line BEGINNING DUHO SIGNATURE:, not the following line. An in-memory insertion on the following line changed the reconstructed digest. Read charitably as text after the colon on the same line, the helper excludes it, but the field no longer remains blank. Neither reading satisfies the requested immutable, both-fields-blank procedure unambiguously.

Replace this sentence with an explicit prohibition on modifying either field or any other file bytes after approval. §17.7's repository-only custody explanation should also cover the recorded Codex attestation, not describe only a relay after allowing both routes.

5. [MAJOR] THE STAGED INITIALIZER: legitimate staging, incomplete transition guarantee.

The sandbox initializer and staged file are byte-identical at 659b763c83a948825d285e51671c28173b446f428bcd32d941811bf6cdaf5721 and export renderer_v4 at line 9. Reconstructing the V35 initializer in memory produces exactly its pinned 4376984057b9af4c9f095fdacd3b37aff572a52cebb2ffaf53639b95ffedf827.

One physical path cannot simultaneously have those two different hashes. Separate lane and staging/sandbox paths can preserve and verify both candidate identities. That is a sound reason to stage; it is not evidence that the V37 lane pin already passes before deployment.

The disclosure is not exact:
- It points to §8.17a-iii for the initializer pin; the actual pin is §8.17a-iv.
- Substituting only the old initializer's bytes/hash in memory into the checker produces one PIN MISMATCH and TWO STALE IMPORT diagnostics, three defects total. The change record acknowledges stale imports; the candidate's description only enumerates the mismatch.
- The production lane itself was not inspected or changed; the stated lane condition remains author-reported.

The plan does not prove runtime import freshness. I executed the reconstructed V35 initializer in a package namespace in memory, while leaving the correct staged file untouched on disk. A subsequent import returned cached study_renderer.render_cutout from renderer_v3 even though the on-disk hash was V37's. No restart or loaded-module identity check is specified.

Important limit: render_chain_v2 imports renderer_v4 explicitly at line 14, so this cache counterexample does NOT redirect that function to v3, and a direct package-level render would violate §8.15b. Thus there is no demonstrated authorized v3 production route. Nevertheless the broad assertion that deployment eliminates every silent old package import is unproved, and an old process can retain one. Define staged preapproval checking, installation while pixel access remains blocked, a fresh production interpreter, and a post-install check before enabling production. “At the moment of approval” is not an executable transition protocol.

6. [MAJOR] FIXTURES: the requested behavioural controls execute; broader claims exceed coverage.

All six integration tests pass through the actual renderer. The 819/820 control uses BRIGHT flags; outside/inside-T controls use zero exposure. They exercise the same final refusal function. MEDIUM is counted in the returned receipt and does not independently flag.

Executed substitutions, all in memory:
- Chain rv4 -> renderer_v3: 6 tests, 3 failures.
- Chain prj -> old pixel_rejection: 6 tests, 6 errors.
- Helper fixture V2 -> V1: 6 tests, 1 failure and 5 errors.
- v4 renderer fixture bound coherently to v3's render_cutout AND RenderTarget: 19 tests, 1 error, on zero-exposure carriage.
- v3 fixture bound coherently to v4: 18 tests, 1 failure, precisely the old zero-exposure-refusal expectation. Thus the claimed 17/18 comparison is reproduced.

Those errors are valid mutation failures; they are not passing receipts. A function-only renderer swap mixes distinct RenderTarget classes and creates extra geometry errors, so the coherent swap above is the meaningful comparison.

The integration fixtures all use r_T=23 and an aligned source grid. They cannot detect the fractional-radius or fractional-WCS cases I reproduced. The MEDIUM integration test also contains a tautological self-comparison at test_render_chain_v2.py:69, although the helper fixture provides a real old/new MEDIUM comparison.

Neither anchor suite achieves 20/20 here because the authentic instrument interpreter is absent. Preserve that limitation and obtain actual environment receipts before claiming the complete requested verification passed.

7. [MAJOR] ASPIRATIONAL OR UNEXECUTED WORK.

The source-to-tensor chain is executable and tested; it is no longer merely “will import” code. What remains unexecuted here is deployment in the production lane, fresh-process import verification, full anchor/environment success, instrument scoring and real-data receipts. Future real pixels are properly unauthorized at this stage.

The MEDIUM TUNING perturbation study is expressly future work and not a signability defect by its mere absence. Conversely, §9B.2d requires N_asym and p_val_excl reporting: render_object discards flag coordinates and returns F only, which cannot identify whether a flag lies in the >23 to <=64 band. Its return value alone is insufficient to build that required diagnostic. A caller would need additional retained information or another rendering pass, the latter conflicting with the prescribed single-pass order. The receipt integration is therefore not complete merely because medium_count is returned.

[MINOR] “renderer_v4 ... IDENTICAL ... except three lines” is executable shorthand, not byte-exact: the three comparisons change, but a new module docstring and comments also change. Likewise the parity harness updates its spec path as well as renderer references. The change record's renderer-fixture row literally embeds “Ran 1 test ... FAILED (errors=1)”; it should not present that as the successful 19-test receipt. These do not negate the successful runs reported above.

8. [FATAL] WHAT IS STILL MISSING FOR SIGNABLE.

The following are concrete clause-text requirements for a new revision, accompanied by executable repairs, new pins and fixtures wherever behaviour changes:

- §§8.14/9B.2d/8.15b: “The main-path radius is evaluated in binary64 as min(64,max(23,2*shape_r/0.262)) and is not rounded or truncated. The consumer records and uses that same value. Validation uses exactly 23. A flag at distance <= r_T refuses.” Repair both integer casts and add the 23.9-radius counterexample.
- §§8.9d/8.14a: if retaining the signed nearest-neighbour identity, state: “F counts the nearest-neighbour predicate only. Bilinear image values can include replacement contributions from other stencil pixels, including inside T when the nearest-neighbour flag is outside T. F does not count every output value influenced by replacement.” Remove the contradictory four-pixel/full-protection assurance and disclose the cost. If full stencil protection is instead intended, implement and separately approve that changed predicate; do not silently reinterpret V15.
- §§8.9/8.17a: state the actual precision boundary and validation owner, for example: “The rendered image and raster digest use binary64. The consumer computes normalization in binary64 and materializes the normalized tensor once as little-endian float32. Required source-plane integer validation is enforced before rendering by the pinned consumer.”
- §17.3: “Both SIGNATURE UTC: and DUHO SIGNATURE: remain blank permanently in the approved file. Approval digest, UTC, route, attestation or relay, and independent recomputation are stored only in the external record and freeze record. No bytes of the approved file are changed.” Make §17.7's trust statement apply to both accepted routes.
- Amendment/§2.15/§8.17a-iv: “Before approval, the V37 pin check is performed against the complete staged candidate tree; V35 remains installed in the operative lane. After approval, production pixel access remains blocked until the staged initializer is installed, all V37 pins pass in the lane, and a fresh production interpreter confirms the v4 imports and use of render_chain_v2.render_object. Only then is V37 enabled.”
- §2.16 and the edit disclosure: list all fifteen changed numbered blocks; include renderer-fixture supersession; either retain full historical pins or explicitly identify the preserved V35 text as their pin authority. Resolve ImportFrom aliases in the checker and expressly allow the named historical comparison fixtures while still rejecting stale production imports. Cover the three currently omitted historical pins.
- §§8.15b/9B.2d: “The single rendering pass retains the flag-location information, or an equivalent sufficient band indicator, needed to compute N_asym and p_val_excl; the receipt producer uses it without rerendering.” Implement and fixture that output.
- Refresh the register and diffs, run the complete warning-strict suite in the real required environments, disclose actual results, recompute the final preimage, and obtain the fresh full-text gate before approval.

The fatal radius counterexample alone prevents certification of V37 as written. Passing hashes and repaired V36 controls do not waive it.

VERDICT: NOT-SIGNABLE

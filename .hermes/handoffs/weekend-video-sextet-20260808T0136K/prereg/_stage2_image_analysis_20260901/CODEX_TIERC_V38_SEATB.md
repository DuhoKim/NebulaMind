ACCESS_SHA=9e21413f2f74ec4b4dbd37d572ce5fcef56aab276eaea7925fdf7bac1f6e9df3

Seat B — fresh hostile referee, Codex.
Authorship: I authored none of the candidate text or reviewed implementation in this session. The user attributes all reviewed work to Hwao. I cannot independently establish historical engine provenance; no finding depends on reviewed code known to have been authored by this engine. The supplemental probes and scratch mutations below are reviewer-written, not candidate implementation.

The sole candidate judged is MINI_PREREG_GZ_TIERC_DRAFT_V38_20260906.md. Earlier versions and reports serve only as comparison evidence. No astronomical image pixels were opened, no network was used, and nothing was published. Synthetic arrays were used for the requested tests. Python bytecode writing was disabled. Scratch mutations were confined to temporary directories outside the reviewed directory; only this report was written here.

The executed radius, stencil and zero-exposure repairs work. Two MAJOR defects remain: §9B.2d still asserts the superseded radius implementation is exact, and checker v3 misses a relative aliased production import that demonstrably redirects the consumer to renderer_v3.

Verification receipts:

- (a) The exact eight-suite warning-strict invocation ran 105 tests: 95 passed, 10 errors. The study-renderer suites passed their requested 8, 6, 19, 6, 18 and 8 tests. Each 20-test anchor suite had five errors, all at instrument_identity_v4.py:83, “INSTRUMENT-INTEGRITY-FAIL: venv_torch interpreter absent”: four environment-record tests and the standalone make_event test. The complete suite therefore did not pass here. No replacement environment was fabricated.
- (b) From miniprereg_pins, the combined protected-region/checker invocation passed 33 tests: 3 plus 30. Direct warning-strict execution of test_pin_consistency_v3.py passed the same 30 checker tests.
- (c) build_register.py --check: “REGISTER CURRENT: 248 clauses”; --audit: “248 register entries ... AGREE”. Both exited zero.
- (d) checker v3: 77 parsed pins, 32 superseded siblings, “RESULT: CONSISTENT”, exit zero on the unmodified staged candidate.
- (e) signature_preimage.py printed exactly 9e21413f2f74ec4b4dbd37d572ce5fcef56aab276eaea7925fdf7bac1f6e9df3. Both actual signature fields are blank. The ordinary file hash remained identical after the review.
- (f) Independent comparison of complete numbered blocks found precisely the 17 clauses listed in the amendment paragraph: §2.11, §2.15, §2.16, §8.9a, §8.9b, §8.9d, §8.10, §8.12, §8.14, §8.14a, §8.15b, §8.17a, §8.17a-iii, §8.17a-iv, §17.1, §17.3, §17.7. No numbered blocks were added. The supplied ordinary diffs exactly equal fresh diff output. V35_TO_V38.diff hashes to ec8afb1c19f30fcb9422db9e4544b2ba0303ea68dbc3f7546e59cd1ecc6ff9b5; V37_TO_V38.diff hashes to 80bf15744ca67dfde60e15d561aa7be8b360812ffafcf55f844a1e3e6f15f5de. Other changes are the banner/amendment/declaration, spacing, generated register, signature fields and VERSION.
- (g) Independently recomputed every one of the 77 parsed file hashes: all match. Enumerating every other full SHA literal in the body found only §9.1(a)'s parameter-only serialization digest, which is a derived object rather than another file pin; weights were hashed but not deserialized. The three formerly omitted bare historical pins are now included. Seven additional supersession-table predecessors whose hashes are retained in V35 also match that authority. The two checker-v2 files match V37's pins, but V38 does not identify V37 as their retention authority; see answer 4.
- (h) All three requested counterexamples were independently executed through render_chain_v3.render_object; results follow in answer 2.

1. [MAJOR] Repair audit of V37 items 1–8.

1 — REPAIRED for the executed radius, nearest-neighbour disclosure and validation ownership; NOT REPAIRED as a completely consistent text. §8.14, line 371: “r_T is evaluated in BINARY64 ... NOT rounded or truncated”; protected_region_v2.py:38 returns float(min(...)), and render_chain_v3.py:24,39 records and uses float(r_t). §8.14a, line 377: “T protects against FLAGGED pixels, not against every stencil contribution”; renderer_v4.py:210 selects the nearest source index while :220–243 separately computes the bilinear image. §8.15b, line 389, locates plane validation “HERE by the consumer”; render_chain_v3.py:26 and pixel_rejection_v2.py:26–41 enforce it. The precision boundary is explicitly answered by §8.9d and chain :42,46. However, the surviving §9B.2d claim discussed below prevents complete closure.

2 — ANSWERED for the nested V36 repair audit; NOT REPAIRED as its complete signability checklist. §8.10 now keys rejection to “published integer maskbits and integer exposure-count planes”; pixel_rejection_v2.py:56–59 implements their union. §8.15b's “Every production render ... goes through this function” has a real consumer at render_chain_v3.py:23–53. Signature and transition repairs are addressed in answers 3 and 5. The remaining checker and cross-clause defects keep the prior checklist open.

3 — REPAIRED for the exact clause list and bare-pin parsing; NOT REPAIRED for the complete checker/retention guarantees. The amendment lists both separately registered §8.17a subclauses. §2.16 says “Every replacement this amendment chain has made”; all newly introduced V36–V38 replacement pairs are now listed. Checker :48,80–86 parses both tight bare forms and resolves the historical basenames. But the relative-import counterexample and the two missing retention authorities in answer 4 remain.

4 — REPAIRED. §17.3, line 775: “Both ... remain BLANK permanently ... NO byte ... is changed after approval”. §17.7, line 783, explicitly covers “Codex's attestation ... or Blanc's relay”. signature_preimage.py:32–40 remains compatible with these blank bytes; it no longer has to justify a live instruction to populate either field.

5 — REPAIRED as a specified installation procedure; production execution remains unverified. The amendment, line 4, requires “a FRESH production interpreter” and says “no interpreter that loaded the V35 initialiser may render”. study_renderer/__init__.py:9 exports renderer_v4; render_chain_v3.py:16 imports it explicitly. The initializer reference now correctly points to §8.17a-iv. See answer 3 for the reproduced three diagnostics.

6 — REPAIRED for the missing radius and band controls; ANSWERED with limits for broader fixture claims. §8.15b explicitly requires the “radius counterexample refused at 23.9 and scored at 23” and retained band information; test_render_chain_v3.py:62–73 executes both. Existing integration controls at :34–60 pass. The fractional-WCS counterexample also passes my independent probe, but there is no fractional-WCS regression test among the eight pinned tests. The MEDIUM integration self-comparison remains tautological at :55; test_pixel_rejection_v2.py:24 supplies the meaningful replacement comparison. Neither anchor suite achieves 20/20 in this sandbox.

7 — REPAIRED for the missing receipt information; ANSWERED for future work. §8.15b now promises “FLAGGED OUTPUT COORDINATES” and “asym_band_flag”; render_chain_v3.py:37–38 returns them before refusal. Instrument scoring, deployment, environmental verification and scientific sensitivity results have not been executed here. The chain's SCORED token means a tensor was produced, not that chi was measured.

8 — NOT REPAIRED as a complete signability checklist. The implementation repairs and immutable approval language satisfy most of the previously requested changes. The residual requirements are stated concretely in answer 8.

The two inherited V35 defects are correctly disclosed in the amendment as “the author's choice for Duho to reverse”. Keeping the literal radius formula and retaining the signed nearest-neighbour predicate is a defensible minimal choice; principal approval of it is not presumed. The exact diff discloses all numbered changes, and the original radius, rejection and renderer modules retain their V35 hashes. I found no undisclosed full-stencil design change. The problem is surviving contradictory prose, not a hidden change to that predicate.

2. [MAJOR] §§8.14/8.14a: implementation repaired; §9B.2d remains inconsistent.

Yes, r_T is binary64 throughout the prescribed helper → consumer → receipt path. protected_region_v2.py:38,44 returns Python floats; :49 compares distance directly to r_t; render_chain_v3.py:24,39 preserves the same floating value. There is no integer cast. This conclusion assumes the caller supplies the helper result as §8.15b requires; render_object accepts a radius argument rather than deriving shape_r itself.

Independent synthetic receipts:

- Radius: shape_r=3.1309; source nexp[66,89]=0; output flag (40,63), distance 23.50531854708632. r_T=23.9 is recorded, F=1, status REFUSED, reason “DATA-INTEGRITY-FAIL: flagged pixel inside protected region”. The pinned control with r_T=23 scores.
- Fractional WCS: subtract 0.25 from both CRPIX values; nexp[67,82]=0. Status SCORED, r_T=23.0, F=1, flagged_coords=[(41,56)], asym_band_flag=True. Replacement changes image values at (41,56), (41,57), (42,56), (42,57); the latter two are inside T. §8.14a now explicitly describes this allowed situation. Its refusal conditions correctly permit this case; it need not literally contain the token SCORED for this example.
- Outside T: nexp[26,26]=0 gives output flag (0,0), F=1, r_T=23.0, status SCORED, asym_band_flag=False. renderer_v3 refuses the same cleaned image and integer planes with DATA-INTEGRITY-FAIL.

The remaining MAJOR contradiction is §9B.2d, line 497. It still says protected_region.py “implements r_t_main(shape_r) exactly as §8.14 states” and cites a fixture asserting “30 at 4.0”. That is the superseded int-truncating implementation, protected_region.py:35. The operative v2 helper returns 30.534351145038165 at 4.0. §2.16 declares the old helper superseded, and §8.14 itself acknowledges its defect; §9B.2d still presents it as the live exact consumer chain. The unchanged clause is not labelled historical at this assertion. CONSISTENT does not detect this semantic conflict.

[MINOR] §8.9, line 347, still attaches “Binary64 accumulation is materialized once as float32” to reprojection. §8.9d now explicitly states that the renderer returns binary64 and no earlier float32 materialization exists; renderer_v4.py:282–289 and chain :42,46 support the new explicit boundary. This clarification answers the V37 precision question, but the old sentence should be synchronized to avoid two readings. Likewise §8.9d's heading still overstates “what contamination touched”; §8.14a supplies the accurate limitation.

3. [MINOR] Installation protocol: executable and closes the specified window.

The ordered steps are coherent: check the staged tree and disclosed lane state; install with every pixel path blocked; require a clean lane check; start and inspect a fresh production interpreter, barring old interpreters; only then enable V38 and retain outputs. No compliant step allows production rendering with renderer_v3. Installation alone is not treated as runtime freshness.

In an external scratch tree I reconstructed the exact V35 initializer, verifying SHA-256 4376984057b9af4c9f095fdacd3b37aff572a52cebb2ffaf53639b95ffedf827. The unchanged checker produced precisely these three defect diagnostics:

    PIN MISMATCH      study_renderer/__init__.py
    STALE IMPORT      study_renderer/__init__.py imports 'renderer_v3', superseded by renderer_v4.py
    STALE IMPORT      study_renderer/__init__.py imports 'renderer_v3', superseded by renderer_v4.py

It exited 1 with RESULT: 3 DEFECT(S). These are three diagnostic lines, not the entire stdout: the checker also prints its count header and result footer. That is the only literal qualification to “exactly three lines”. The duplicate stale diagnostic comes from the ordinary module scan and package-init scan.

The staging file equals the sandbox initializer at SHA-256 659b763c83a948825d285e51671c28173b446f428bcd32d941811bf6cdaf5721. A fresh sandbox interpreter confirmed package render_cutout identity with renderer_v4 and chain v3's renderer binding. This verifies feasibility, not installation or pixel blocking in the production lane; that lane was not inspected or changed.

4. [MAJOR] §2.16, retention and checker v3: partially repaired.

The declaration at line 6 names only five test fixtures. No production module is declared comparison-only. Checker :215–220 still hashes those fixtures; :229–230 waives their stale-reference scans. Thus the actual declaration exempts fixtures only. The parser itself does not enforce a test-file naming restriction, so this is a property of the reviewed declaration, not an intrinsic security boundary.

Absolute aliased production imports are now caught. In a scratch copy I appended “from study_renderer import renderer_v3 as stale_production” to the pinned chain and updated only its scratch digest. The checker exited 1 with STALE IMPORT on render_chain_v3.py, independently of hash mismatch.

But relative aliased production imports are NOT handled. In a second scratch mutation I appended:

    from . import renderer_v3 as rv4

I updated the scratch document's chain pin to its actual mutated digest. Checker v3 exited 0 and printed CONSISTENT. Executing that actual mutated consumer bound rv4 to study_renderer.renderer_v3 and made the outside-T zero-exposure example return REFUSED/DATA-INTEGRITY-FAIL. The cause is check_pin_consistency_v3.py:181: “elif isinstance(node, ast.ImportFrom) and node.module”. For “from . import ...”, node.module is None, so :182–184 never records the imported name. This is a concrete guard bypass, not evidence that the unmodified shipped chain imports v3. Its demonstration uses reviewer-written scratch code; the defect lies in Hwao's reviewed checker.

Bare pins are repaired for this document: all three formerly missed historical files are now among the 77 verified pins. The exact newly introduced replacement pairs are present in the 32-row table.

[MINOR] “V35 ... is the pin authority for every file it pinned” sufficiently preserves the omitted V35-era digests. It cannot preserve files introduced after V35. V38 newly supersedes check_pin_consistency_v2.py and test_pin_consistency_v2.py without retaining their digests or naming V37 as authority. Their actual hashes match V37:

- check_pin_consistency_v2.py: df0ad5680011886e71c0871f28a9194a342b5539ec76fd8c45743757c6acba62
- test_pin_consistency_v2.py: 3433fa4a99e8068ecfcaecb0f4e8e57d8e59dc81a9f241ee81eabfe94d44d95d

The files have not changed; the blanket retention explanation is incomplete. The earlier bs4_anchor.py table entry also has no explicit V35 pin, so that authority should not be described as covering every historical left-hand file indiscriminately.

[MINOR] §2.15 still says “26-test run”; both current invocations run 30. Correct the receipt count, not the passing tests.

5. [MINOR] §§17.1/17.3/17.7: substantive repair complete.

Both fields are currently blank and must remain blank permanently. The two approval routes, external timestamps and evidence, independent digest recomputation, and digest-versus-speaker distinction are consistent. signature_preimage.py:39 blanks only the DUHO SIGNATURE line; this is compatible with §17.4 and with leaving SIGNATURE UTC blank rather than excluding it. The helper is not speaker authentication or a substitute for approval.

One wording remnant remains: §17.7 ends with trust resting on the “recorded relay” if chat history is lost, after correctly covering both routes. “Recorded attestation or relay” would be exact. The preceding express coverage makes this a MINOR editorial issue, not the former two-route defect.

6. [MINOR] §9B.2d diagnostic receipt: repaired, with the scoring boundary understood.

For validation, the helper supplies 23.0, so chain :38's r_T < d <= 64 indicator is exactly the required >23 to <=64 band. Flag coordinates, F, r_T and the Boolean survive in the receipt without another reprojection. N_asym counts actually instrument-scored validation objects with that Boolean; combining those receipts with the required machine signs and human labels permits recomputing k, m, p_val_excl and its Wilson bound. No re-render is needed. The render receipt alone does not contain instrument signs, and its SCORED label must not be treated as proof that §9 succeeded. The stale helper prose identified in answer 2 remains separate from this successful receipt repair.

7. [MAJOR] Unexecuted work and evidentiary limits.

The renderer-to-tensor chain is executable, and its requested synthetic controls passed. Actual production installation, lane freeze-record outputs, authentic instrument-environment success, instrument scoring, real-data receipts and the MEDIUM perturbation study were not executed here. Preapproval absence of scientific pixels and future sensitivity results is appropriate, not itself a signability defect. The required anchor suite success cannot be claimed from this sandbox: ten errors remain attributable to the absent required interpreter.

[MINOR] The amendment's broad assertion that fixtures reproduce the counterexamples exceeds the pinned eight-test coverage for fractional WCS; my independent execution supplies review evidence, not a pinned regression. “IDENTICAL ... except three lines” in §8.17a also describes executable exposure comparisons rather than byte identity: documentation and comments differ too.

8. [MAJOR] What remains necessary for SIGNABLE, as clause text and associated executable repair.

- Replace §9B.2d's live helper/fixture assertion with: “Both paths use protected_region_v2 and its pinned fixture in §8.14. The main radius is the unrounded binary64 formula; validation uses exactly 23.0. protected_region.py and its integer-radius fixture are retained solely as superseded historical evidence and do not implement the current main formula.” Remove or explicitly historicize the “30 at 4.0” assertion. Add §9B.2d to the next revision's disclosed clause list and rebuild its register.
- Repair the checker's relative ImportFrom handling and add an actual checker regression for the scratch redirection above. State in §2.15: “Stale-import checking includes absolute and relative imports, including from . import renderer_v3 as rv4. A non-comparison production module using a superseded import fails even when its file digest is correctly pinned.” Pin the repaired checker and fixture; require the mutation to fail while the real candidate passes. Update the test count to the actual resulting count.
- Complete retention wording: “V35 supplies historical pins only for files it actually pinned. The superseded checker-v2 program and fixture are retained at [the two full verified digests printed in answer 4].” Alternatively explicitly identify the retained V37 authority for that pair.
- Synchronize §8.9 with the already explicit §8.9d boundary: “Reprojection returns binary64; normalization is binary64; only the normalized tensor is materialized as little-endian float32.” Use “recorded attestation or relay” in §17.7 and “three defect diagnostics, plus the checker header and footer” in the installation paragraph for literal exactness.

The first two items are substantive signability blockers. The remaining items close the specified exactness and retention audit. Obtain authentic-environment anchor receipts before representing the complete required verification as passed; do not treat this report as evidence that production installation or approval occurred.

VERDICT: NOT-SIGNABLE

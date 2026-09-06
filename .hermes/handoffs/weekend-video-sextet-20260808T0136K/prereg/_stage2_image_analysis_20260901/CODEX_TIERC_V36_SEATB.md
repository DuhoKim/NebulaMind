ACCESS_SHA=017045d95f7b1fe551e36879f2409d9f1ac77b5ddcb123984d965fb7c7a71ef4

Seat B — fresh hostile referee, Codex.
Authorship: I authored none of the reviewed artifacts in this session. The author attributes everything under review to Hwao and reports no authorship by this engine; I cannot independently establish historical engine provenance. No finding depends on reviewed code known to have been written by this engine. Supplemental probes were reviewer-written, executed in memory, and are evidence rather than reviewed implementation.

The sole candidate judged is the V36 file identified above. V35, V15 §6, the diff and change record supply comparison evidence. No astronomical image pixels were opened, no network was used, and nothing was published. Only this report was written.

Verification results

- Required warning-strict v2 invocation from study_renderer: 6 tests, OK, exit 0.
- Required warning-strict V35 invocation from study_renderer: exit 1, ModuleNotFoundError: No module named 'study_renderer'; it did NOT run eight tests. Repeating with PYTHONPATH=.. gives 8 tests, OK, exit 0. This changes the import environment, not either pinned file. V36 §2.15 already prescribes running package fixtures from the lane root; the change record accurately records the failed invocation.
- build_register.py --check: REGISTER CURRENT: 248 clauses; exit 0.
- build_register.py --audit: 248 entries, AGREE; exit 0.
- signature_preimage.py: exactly the ACCESS_SHA digest; exit 0.
- Actual diff V35 V36: exit 1, as expected for different files; stdout is byte-identical to V35_TO_V36.diff. There are exactly 22 added/deleted content lines.
- V35's reconstructed signature preimage is 4a89973fadf1c561e8f4e7f7043dd91eb6ab026157102be6a4f8d01bc1d9a091. Its raw signed-file digest is 3b37291e90090d0fdf51dd2f8f0611b9153668eb5906400317d45c44db2575e8. Those are distinct objects, not a pin failure.

Every §8.9a file pin matches:
- study_renderer/pixel_rejection_v2.py: 0655370958b7fd65dd2324d41b0a05aa31dd0e8a50f01317e63bf663bb9f6cde
- study_renderer/test_pixel_rejection_v2.py: 85aaba182dd0ffe5f4d6f4bb429ec390e0cf9223ba1faf0f2c2f39b0a5d8ead8
- study_renderer/pixel_rejection.py: 8f66bc1c61173648f11386eb17f2d5afd3c3f1a338aee5bf3e11fe9aad950818

Additional checked hashes:
- study_renderer/test_pixel_rejection.py: 82f07a48db7556c29f6939ef2be108c84ab3049966306a5c37b5e800ebaeff78
- study_renderer/renderer_v3.py: a2e293c2964abdae781fe3fd408e05c304803cdde14578ad1c1f1ea6229fc54c
- V35_TO_V36.diff: 570790e0bd632294de22b28148fd8a8a28ce17a27cb4240253598356481f5b00

1. [FATAL] The helper implements the change; the pinned rendering chain contradicts it.

Line-by-line review of pixel_rejection_v2.py confirms:
- Lines 16–23 fix five rejecting bits and MIN_ACCEPTED = 16.
- Lines 26–51 require integer maskbits/nexp, refuse negative exposure counts and mismatched maskbits/nexp shapes, and combine bit rejection with nexp == 0.
- Lines 54–74 preserve MEDIUM-only image values, exclude every rejected pixel from the median, choose the lower middle accepted value, and replace on the source grid.
- Lines 77–85 flag rejecting bits OR zero exposure and count output MEDIUM pixels. MEDIUM alone does not flag; a MEDIUM pixel with zero exposure or another rejecting bit does.
- Supplemental boundary probes: 15 accepted pixels refuse; 16 accepted values 0 through 15 produce fill 7.

The claim “negative planes refused” needs qualification: only negative nexp is explicitly refused. A maskbits value of -32768 passes integer validation and produces no rejection. The helper also does not explicitly validate image dimensionality/shape against both integer planes. Its fixture establishes the narrower maskbits/nexp shape check, not comprehensive plane validation.

The decisive failure is §8.17a's still-pinned renderer_v3.py. Lines 213–214 reject any nearest-neighbour exposure value <= 0; lines 275–276 independently reject any output exposure <= 0. Cleaning the image leaves the exposure plane unchanged, as V36 requires, so the renderer refuses before flagged_output can implement the relaxation.

Executed synthetic counterexample: a contained 130×130 source with all positive exposures renders successfully to 128×128. Changing one exposure at the source position mapping to the output corner to zero, and first applying v2 clean_source, yields DATA-INTEGRITY-FAIL. That pixel is outside T and F would be 1. Thus the asserted newly allowed case cannot execute through the pinned renderer. This is an actual reproduced contradiction of §§8.12/8.15b, not a hypothetical missing adapter.

2. [MINOR] The fixture does distinguish old behavior; its coverage stops at the helper.

test_pixel_rejection_v2.py lines 29–30 execute V35 clean_source on the same MEDIUM input and assert one replacement and changed intensity. Lines 36–37 execute V35 on the same image/maskbits used for the zero-exposure case and assert no replacement; V35 has no nexp argument. The v2 assertions are at lines 26–28 and 33–35. Lines 17–18 independently assert the exact new bit set.

I rebound fixture.V2 to the V35 module in memory and ran all six tests: one assertion failure and five errors. A swap therefore cannot silently pass. However, these tests never call renderer_v3: they do not establish that a zero-exposure raster survives reprojection. The median test uses 63 accepted pixels; the even-count boundary was independently checked above.

3. [MAJOR] The disclosed edit list is exact, but dependent text remains inconsistent.

Independent comparison of complete clause blocks finds exactly these changes: §8.9a, §8.9b, §8.9d, §8.12, §8.15b. The remaining differences are the disclosed banner/amendment insertion, generated register, blanked signature fields and VERSION. No additional numbered clause changed.

Whole-document searches for MEDIUM, nexp, 8.12, coverage and pixel_rejection found no separate operative enumeration retaining all six rejecting bits or an explicit prose requirement that every output exposure be positive. Historical coverage references and §7.7's release-absence test do not impose the retired per-raster rule.

Nevertheless, unchanged §8.10 says “the rejection is keyed only to published integer maskbits.” This directly contradicts the new exposure-count predicate. The old renderer pin in §8.17a remains operative and retains the old coverage rule in executable form. The introductory amendment paragraph also describes pixel_rejection.py as the module “this document pins” without clearly identifying that statement as V35 history.

§2.16 calls itself the complete supersession table but omits the new pixel_rejection replacement. Any repair must distinguish the deliberately executed historical comparison fixture from live production imports.

The regenerated register agrees mechanically; it cannot prove agreement between clauses or between text and code. §2.17 itself acknowledges that limit.

4. [FATAL] Version/digest form passes, but the approval mechanism is contradictory.

The candidate identifies V36, discloses an exact diff, retains blank SIGNATURE UTC and DUHO SIGNATURE fields, and has preimage equal to file digest. Those checks pass.

The new paragraph specifies approval in the codex conversation, a Codex attestation, and Blanc's independent digest recomputation. It correctly distinguishes byte identity from speaker authentication.

Unchanged §17.1 instead requires Duho to fill SIGNATURE UTC first and state the resulting digest and UTC in the Blanc chat channel; §§17.3/17.7 require Blanc's verbatim relay and Hwao's freeze record, with discrepancies voiding the signature. No clause explicitly reconciles or supersedes that procedure. Also, filling SIGNATURE UTC after approval of today's blank-field bytes changes the preimage because §17.4 excludes only DUHO SIGNATURE.

A referee cannot certify the proposed codex approval as satisfying both mechanisms. The approval route, timestamp placement and exact bytes approved must be made consistent in the binding clauses.

5. [MAJOR] The intended bounds are retained, but the relaxation is not implemented end to end.

§8.14a still refuses F > 819 or any flag inside T. §9B.2d still sets the validation radius to 23. The main Tier-C radius remains min(64, max(23, 2*shape_r/0.262)); V36 must not imply that every main-study radius is exactly 23.

Supplemental composition of v2.flagged_output with protected_region.refuse_on_contamination confirms: one corner zero-exposure flag is allowed; one central zero-exposure flag refuses; 819 outside-T flags are allowed and 820 refuse. These establish the helpers' intended boundary behavior, not a functioning render chain.

The complete zero-exposure relaxation remains unexecuted because of finding 1. The change record explicitly says the development adapter “will import” v2; existing scripts/stage2_render_validation.py still imports the old helper at line 15 and applies the old whole-raster coverage refusal at line 68. This corroborates the integration gap; the fatal finding rests on the pinned renderer itself.

The MEDIUM perturbation study is a future TUNING-only disclosure, expressly not an outcome-dependent gate. Its absence before authorized development pixels is not itself a signability defect. A callable medium_count helper is likewise not evidence that a production receipt already reports it.

6. [FATAL] Required amendments before SIGNABLE.

The next revision needs executable repairs followed by binding clause text with actual new file names, full hashes and successful synthetic integration receipts. At minimum:

- §§8.17a/8.12: “The pinned renderer carries integer nexp == 0 unchanged through nearest-neighbour sampling. Zero exposure alone is not a renderer refusal. Missing, non-finite, non-integer, mismatched or negative required planes refuse. The resulting output flags are passed to §8.14a before normalization.”
- §8.15b: name and pin the actual consumer implementing clean_source(image, maskbits, nexp), reprojection, flagged_output(rendered_maskbits, rendered_nexp), the unchanged refusal test, and per-raster medium_count reporting. Require an executed synthetic outside-T zero-exposure success and central/ceiling refusal controls through that consumer.
- §8.10: replace the maskbits-only statement with “Rejection is keyed only to the published integer maskbits and integer exposure-count planes under §8.9a.”
- §§2.16/8.9a: identify V35 code as retained historical evidence, explicitly allow its comparison-fixture use, and prevent its production use. State plane-validation requirements precisely and implement the stated negative-mask/shape refusals.
- §§17.1/17.3/17.7: explicitly designate the codex-conversation approval procedure and retained attestation/relay evidence. State whether SIGNATURE UTC is filled before presenting the final digest or remains blank with approval UTC solely in the external record; do not change hash-covered fields after approval. Retain the distinction between digest equality and speaker authentication.
- Clarify §8.12's radius reference: 23 for the validation path, the unchanged §8.14 formula for the main path.

These repairs necessarily exceed the present five-clause scope. Disclose the expanded diff, regenerate the register, recompute the final preimage, and obtain the fresh full-text referee result before approval. Neither this report nor the passing helper tests authorize pixels.

VERDICT: NOT-SIGNABLE


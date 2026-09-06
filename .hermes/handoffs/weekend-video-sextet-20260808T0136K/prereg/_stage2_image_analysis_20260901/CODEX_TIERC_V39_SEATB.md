ACCESS_SHA=ddc0cfb4139b7e1706f852cb5cdd7cb14293256fee8254cc71623bded172b2d0

Seat B — fresh hostile referee, Codex.
Authorship: I authored none of the candidate text or reviewed implementation in this session. The user attributes all reviewed material to Hwao. I cannot independently certify historical engine provenance; no finding depends on candidate code known to have been written by this engine. Reviewer-written scratch mutations and probes are identified below.

The sole candidate judged is MINI_PREREG_GZ_TIERC_DRAFT_V39_20260906.md, at the full digest above. V35/V37/V38 and the V38 referee report are comparison and retention evidence, not substitute candidates. References below are to V39's physical lines unless another file is named.

All four released repairs are implemented. No FATAL or MAJOR finding remains. One inherited MINOR retention overstatement remains, distinguished below from the repaired checker retention requirements.

Verification receipts

(a) Warning-strict checker tests, from miniprereg_pins: both python3 -W error -m unittest test_pin_consistency_v4 and python3 -W error test_pin_consistency_v4.py passed 31 tests. I then rebound the fixture's cpc reference to checker v3 in memory and ran V4RelativeImportRegression alone. It FAILED at test_pin_consistency_v4.py:224: "'renderer_v3' not found in {'numpy'}". Exactly one assertion failure, no errors. With the shipped binding, its assertion that v4 sees the import and its separate assertion that v3 misses it both pass.

(b) The warning-strict combined renderer invocation passed 34 tests: render-chain v3 9, renderer v4 19, pixel-rejection v2 6; collection independently confirmed those component counts. The warning-strict protected-region v2 invocation passed 3 tests. Python bytecode writing was disabled throughout.

(c) build_register.py <V39> --check exited 0: "REGISTER CURRENT: 248 clauses". --audit exited 0: "AUDIT: 248 register entries reconciled against the independent clause list — AGREE".

(d) check_pin_consistency_v4.py <V39> exited 0: 81 parsed pins, 34 superseded siblings, "RESULT: CONSISTENT". An additional independent hash comparison found no mismatch among those 81 pins.

(e) signature_preimage.py <V39> printed exactly:
ddc0cfb4139b7e1706f852cb5cdd7cb14293256fee8254cc71623bded172b2d0
Both actual signature fields are blank.

(f) Fresh ordinary diffs exactly matched the supplied files:
V38_TO_V39.diff: b30d5ac0f07e0ca6a22df143fb96dc72c30383f2d6b764600d13368d60b5cbeb
V35_TO_V39.diff: c2264f544fa1224e9abf0285e98fca94939d2a5dfa9d612e561d1cd0c09f1ea6
Independent numbered-block comparison found only the seven V38-to-V39 changes listed in answer 2, with no added numbered clause.

(g) In an external temporary tree, I appended the exact line "from . import renderer_v3 as rv4" to a scratch render_chain_v3.py and replaced its pin in a scratch V39 with the actual mutated digest. I ran each checker's main entry point with ROOT directed to that scratch tree; neither checker implementation was edited. Checker v4 exited 1:
STALE IMPORT      study_renderer/render_chain_v3.py imports 'renderer_v3', superseded by renderer_v4.py
RESULT: 1 DEFECT(S)
Checker v3 exited 0: "RESULT: CONSISTENT". There was no PIN MISMATCH. An independently re-pinned absolute mutation, "from study_renderer import renderer_v3 as rv4", failed with the same stale-import diagnostic under both checkers.

1. [MAJOR — CLOSED] Are the four items repaired as the V38 report requested?

Yes, for the four concrete released repairs, with the inherited MINOR qualification in answer 5.

Item 1: §9B.2d, line 499: "V39: BOTH paths use" protected_region_v2; the main radius is "the unrounded binary64 formula". The old helper and fixture are "RETAINED SOLELY AS SUPERSEDED HISTORICAL EVIDENCE" and "do not implement the current main formula". The old 30-at-4.0 assertion is explicitly historical. This implements the requested clause replacement.

Item 2: §2.15, line 73: "stale-import checking includes ABSOLUTE and RELATIVE imports" and "a non-comparison production module using a superseded import FAILS even when its file digest is correctly pinned". The checker and fixture are v4, the count is 31, and §2.16 lines 106–111 routes all three predecessor generations to v4. Receipts (a) and (g) establish the executable repair and failing control.

Item 3: amendment paragraph, line 4: "V35 ... is the pin authority for the files V35 itself pinned"; checker-v2 retention expressly names "authority: V37" and checker-v3 retention "authority: V38". All four full digests match the retained files and the respective prior candidates.

Item 4: §8.9, line 349: "Reprojection returns binary64; normalisation is binary64; only the normalised tensor is materialised, once, as little-endian float32". §17.7, line 785: "recorded attestation or relay". Installation paragraph, line 4: "three defect diagnostics" plus "the checker's own header and footer lines". §8.17a, line 429: "three EXECUTABLE lines (its docstring and comments differ as well)". The renderer diff supports that description. §8.15b, line 391 pins the enlarged 9-test fixture and explicitly names its fractional-WCS regression.

2. [MINOR — NO SCOPE-CREEP FINDING] Did anything outside the four items change?

No substantive change outside the release was found. The changed numbered blocks are exactly §2.15, §2.16, §8.9, §8.15b, §8.17a, §9B.2d and §17.7. §8.15b changes only the fractional-WCS fixture pin, count and description. Other changes are the banner/amendment history and installation/retention wording, generated register, and VERSION token.

Among pins shared with V38, only test_render_chain_v3.py has a changed digest. No parsed V38 pin disappears; four become newly parsed: the checker-v2 retention pair and the new checker-v4 pair. The V35-to-V39 numbered changes also exactly match the amendment's 19-clause disclosure. No threshold, radius formula, nearest-neighbour predicate, approval route or production-renderer implementation changed in V39.

3. [MAJOR — CLOSED] Is §9B.2d unambiguously historical where required?

Yes. Line 499 separates the live v2 functions from the historical truncating helper and fixture. §8.14, line 373, already forbids rounding/truncation; §8.15b, line 391, requires the radius from protected_region_v2; §2.16, lines 113–114, declares the old pair superseded. I found no remaining clause asserting the truncating implementation as live.

Direct evaluation gives r_t_main(4.0) = 30.534351145038165 and r_t_validation() = 23.0. The consumer imports v2 at render_chain_v3.py:17 and preserves the floating radius at lines 24 and 39. The caller still supplies the helper result as specified; this is not evidence that a production catalogue run has occurred.

4. [MAJOR — CLOSED] Does checker v4 enforce the requested distinction, with a falsifiable regression?

Yes. check_pin_consistency_v4.py:183–188 records imported names even when ImportFrom.module is None, closing the exact relative-import defect. Absolute aliased imports remain detected. The re-pinned production mutations fail as required.

The line-6 COMPARISON-ONLY declaration names five fixtures and no production module. They remain subject to hash checking. Removing only that declaration in scratch causes three stale-import diagnostics, including test_render_chain_v3.py's renderer_v3 comparison. Restoring the declaration permits the clean candidate. The exemption parser is a declaration mechanism, not an intrinsic restriction to test filenames; the reviewed declaration supplies the fixture-only boundary.

The regression is a control that can fail: the old-checker substitution actually failed, rather than merely being described as expected to fail.

5. [MINOR — INHERITED RETENTION LIMIT] Is retention complete for every superseded file?

The released retention repair is complete for the newly superseded files and the authorities it names. Checker v2 and its fixture match V37; checker v3 and its fixture match V38. The seven older table predecessors relying on V35 rather than a current explicit pin also match V35. Across §2.16's 34 left-hand paths, 33 have matching digest authority in V39 or its named V35/V37/V38 predecessors.

The literal universal claim is still too broad: anchor_gate/bs4_anchor.py, listed at line 92, has no explicit digest in those authorities. Consequently §8.17a-i, line 437, "Every retention claim in this document carries a full digest", is not literally established for that historical file. The V38 report already identified this exception. V39 correctly stops claiming that V35 supplies pins for files it never pinned; it does not recover that missing historical pin.

This is a MINOR historical-evidence limitation, not a live production-import defect or an unclosed substantive V38 blocker. I do not infer a historical digest from the file's present bytes.

6. [MINOR — EXECUTION LIMITS] Anything aspirational or unexecuted?

The requested reconciliation checks are executed. The fractional-WCS test at test_render_chain_v3.py:62–68 runs the specified quarter-pixel offset through the actual chain. An additional reviewer probe returned SCORED, F=1, r_T=23.0, flagged_coords=[(41,56)], asym_band_flag=True. The pinned test asserts scoring, one flag and distance outside T; it does not separately assert every influenced bilinear pixel.

The staged initializer matches the staged source byte-for-byte. A fresh sandbox interpreter confirmed the package render_cutout is renderer_v4.render_cutout and the chain binds renderer_v4. Actual lane installation and its freeze-record outputs remain future obligations.

Per the stated sandbox limit, I accept the lane's recorded anchor-v4 and anchor-v5 20/20 results: V37 change record lines 15 and 18, reiterated in the V38 record lines 16 and 30. I did not rerun those environment-dependent suites or claim sandbox success for them.

Principal approval, authentic production-environment execution, sealing, real validation/instrument scoring, scientific receipts and the MEDIUM perturbation study remain unexecuted in this review. A render receipt's SCORED token certifies tensor production, not a measured chi. These future steps do not make the four implemented repairs aspirational.

7. [MINOR — NO SIGNABILITY BLOCKER] What clause text is still missing for SIGNABLE?

Nothing further is required for SIGNABLE. The inherited historical-retention overstatement in answer 5 is a disclosed MINOR limitation, not a requirement for another completing round. This verdict approves no execution: V35 remains operative until the exact-byte principal approval and ordered installation requirements are satisfied.

No astronomical image pixels were opened, no network was used, and nothing was published. Synthetic arrays were used for the requested tests. Scratch changes were confined outside the reviewed directory; only this report was written here.

VERDICT: SIGNABLE

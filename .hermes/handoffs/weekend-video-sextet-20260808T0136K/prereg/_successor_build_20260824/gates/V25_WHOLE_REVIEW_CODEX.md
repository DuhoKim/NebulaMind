# V25 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

**NOT CLEAR.** The dispatched V25 bytes match the runner pin exactly, and the three catalogue thresholds are absolute in the normative text. Section 4 and the BS-5f row both correctly print the post-exclusion values `N = 49,211` and `N_eq = 110,983`. The load-bearing BS-2a argument nevertheless fails: measurement before the study proves that these catalogue fields were not generated from this study's later χ outputs, but temporal precedence does not prove statistical independence from handedness. More decisively, V25 applies the new predicate at Row P/P8 after unblinding while claiming that the pre-unblinding Stage-C/BS-5f population at P5 is already the 49,211-row post-exclusion population. Under V25's own ordered consequence, the expected 15,849 P8 removals instead force `INCONCLUSIVE-BY-CALIBRATION`; they cannot produce the population on which §4 says the statistic will run. Stale REFUSED/one-filled text, contradictory fixture requirements, and a §10 map whose own checker still reports 15 failures independently prevent clearance.

## Digest-first comparison

I computed SHA-256 over the exact current bytes of `../PREREG_SUCCESSOR_DRAFT_V25_20260827.md` and compared all 64 hexadecimal digits with line 5 of `runner_v25_chain.log`:

- runner pin: `50f2e53256cc79707f2a4dfbf737740e6101742deb39365498737c904aa0f59b`
- computed V25: `50f2e53256cc79707f2a4dfbf737740e6101742deb39365498737c904aa0f59b`
- comparison: **MATCH — exact 64-hex equality**

I also recomputed the V24 predecessor as `6d722dc51316a2dbc3f3cf07a7dec8c8c5776df16388b43177681899cb32f977`, matching the V23→V24 result prefix printed at V25 line 841. The catalogue file named at V25 line 376 recomputes to `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3`, exactly matching the full digest printed there.

## Numbered findings

### 1. CRITICAL / BLOCKING — §2.7 lines 372–380 — temporal precedence is not independence from handedness

**Why it fails.** V25's complete support for independence is: the survey measured `flux_ivar_r`, `psfsize_r`, and `nobs_r` before this study existed, therefore the columns are independent of handedness and no blindness construction is needed (lines 372–378). Chronology establishes only that this study's later instrument output did not cause those earlier catalogue values. It does not establish statistical independence, conditional independence, or reflection invariance. A pre-existing variable may correlate with a later outcome through sky position, galaxy morphology, observing strategy, or measurement difficulty. The receipt itself establishes substantial correlations with the tested axis: −0.2532, +0.3659, and −0.3012 (`BS2A_QUALITY_CUT_RECEIPT_20260828.md` lines 22–29). That does not by itself invalidate a fixed-axis test, but it disproves the inference that “measured earlier” is an independence proof.

The defensible narrower statement is that the predicate is **outcome-blind with respect to this study's unobserved χ output**: its columns and absolute thresholds were fixed without reading χ and before any image byte. That is not the independence claim V25 makes.

**Smallest sufficient repair.** Replace the statistical-independence claim with the narrow outcome-blind chronology claim. If actual independence is required, add a preregistered argument/check showing that each predicate is invariant under image reflection/handedness sign (or establish the exact conditional-independence property needed by the estimator), including how catalogue construction and joins preserve it. Do not infer independence from time order alone.

### 2. CRITICAL / BLOCKING — §§2.7, 4, 6.1 and 7, lines 336–343, 380–382, 456–468, 528, 539, 544, 550, 710–712 — the predicate is applied at P8 but BS-5f claims its population at P5

**Why it fails.** The lifecycle is internally impossible:

1. Section 2.7(2) permits only missing/integrity exclusions before lock and explicitly defers confidence-threshold exclusion to post-unblinding (lines 336–339).
2. The new BS-2a paragraph says Row P applies the predicate at P8 and records `EXCLUDED-BY-CONFIDENCE` below threshold (line 382).
3. Row E at P2–P3 reads only structural predicate bits and expressly excludes instrument absence/non-finiteness; it has no catalogue-quality fields or new quality-exclusion state (line 539).
4. Stage C and BS-5f run at P5, before lock and unblinding (lines 456–468, 528, 544).
5. Nevertheless §4 and the BS-5f row claim that this P5 mask already has `N = 49,211`, `N_eq = 110,983` (lines 464, 468, 712).
6. Row P's ordered rule says any post-unblinding removal immediately emits `INCONCLUSIVE-BY-CALIBRATION`, with no Stage-C rerun (line 550; also lines 468 and 491).

The cut removes 15,849 of 65,060 rows. Under the written phase order, those are P8 removals, so the run deterministically becomes `INCONCLUSIVE-BY-CALIBRATION`; the 49,211-row set cannot be the earlier P5 Stage-C mask and can never become the analysed statistic population. This is a direct Clause-10 forward-termination failure, not a wording nit.

It also mislabels survey-quality cuts as instrument “confidence”: `flux_ivar_r`, `psfsize_r`, and `nobs_r` are catalogue metadata, not the §2.7(5) confidence function emitted by the handedness instrument.

**Smallest sufficient repair.** Define a distinct, closed catalogue-quality exclusion reason and authenticated evidence fields; apply the frozen predicate before BS-2f, so the P3 sealed mask really has 49,211 rows while the 65,060-row parent identity remains unchanged. Update Rows C2/E/F, the terminal-state vocabulary, BS-2f, and Clause-10 phases/effects accordingly. Keep post-unblinding instrument-confidence handling separate. Then rerun the power evidence on the actual post-quality mask rather than treating an analysis-time naming choice as preserving old-mask power.

### 3. HIGH / BLOCKING — §2.6 and the adoption chain, lines 292–318 and 448–450 — old-population Stage-P evidence is still presented as standing for a changed analysed geometry

**Why it fails.** `BS2A_QUALITY_CUT_RECEIPT_20260828.md` lines 63–68 correctly states that any cut changes N and invalidates the geometry and Stage-P receipts computed on 65,060. The later adoption note attempts to preserve Stage-P by calling the cut an “analysis-time exclusion” rather than a sample redefinition. That nominal distinction preserves the parent digest and closure custody, but it does not preserve the statistical population: V25 itself says the analysed population changes to 49,211, its variance changes, and its two-ended split moves to 40.8/59.2. V25 nevertheless retains 995/1000 measured on the old reduced geometry at lines 292–312 and describes that result as the real reduced-geometry result at lines 448–450.

**Smallest sufficient repair.** Preserve the v9 parent and closure pins if required, but mark the old Stage-P result historical/non-applicable to the post-quality analysis mask and rerun the frozen power test on that mask before crediting it. A parent-custody distinction cannot substitute for a power-population match.

### 4. HIGH / BLOCKING — preamble, fold record, §7 and §11, lines 23–25, 667–669, 685, 691, 853 and 857 — BS-2a status and implementation requirements remain contradictory

**Why it fails.** The §7 BS-2a row did change to `FILLED` (line 691), but the whole document did not:

- lines 23–25 still say findings remain pending the “refused BS-2a design”;
- fold-record lines 667–669 still say BS-2a is REFUSED by all three seats and Rows C2/E cannot run;
- line 685 still says only one of fifteen Class-P slots is filled, although the brief's standing state requires two (BS-2m and BS-2a);
- line 853 still calls the BS-2a schema addition deferred with the “already-refused BS-2a design”;
- line 691 claims the design is gated as text **and code**, while no implementation/schema digest is supplied and line 853 still defers its schema;
- line 857 still requires implementing a hermetic worker profile allowlist and adversarial producer fixtures, directly contradicting lines 378 and 537, which say no hermetic worker, allowlist, or blindness fixture is required;
- Clause 9 at line 578 still mandates adversarial producer fixtures, again contradicting the new “none required” claim.

Thus the status table changed, but stale status and incompatible obligations remain in distant sections—the exact failure mode the brief required this review to test.

**Smallest sufficient repair.** Reconcile every live status statement and count; separate historical quotations clearly. Decide one C2 fixture/capability contract and state it consistently. A DESIGN slot declared gated as text and code cannot be FILLED while its required code/schema/digest remains deferred.

### 5. HIGH / BLOCKING — §10, `FINDINGS_MAP.md`, and `tools/prereg_trace.py`, lines 815–845 — the findings mapping is not honest and its stated enforcement fails

**Why it fails.** The new column exists, but existence is not honest closure:

- Running the named checker on the pinned V25 returned **24 computed transitions; 15 problems**.
- It reports V24→V25 missing even though V25's footer says the current transition belongs only in the next draft. The checker was not changed to implement that declared coverage rule.
- It reports fourteen earlier normative transitions with no finding cited. V25 prints `— none cited —` for those rows while the footer claims a normative change without a finding is a failure.
- `FINDINGS_MAP.md` labels V24→V25 as answering GPT56-V24-1/2 and CODEX-V24-4/5/6, but CODEX-V24-6 was the silent six-section truncation. The generator still uses `[:6]` at `tools/prereg_trace.py` line 113, so that finding is not answered.
- CODEX-V24-5/GPT56-V24-1 concerned the missing-current-transition/self-reference contract. V25 adds explanatory prose but leaves the check implementation demanding the current row; the mechanism still rejects the document.

The human mapping therefore overclaims repairs the bytes and checker do not implement.

**Smallest sufficient repair.** Define the coverage contract in both prose and checker (predecessor-only in-band plus an external pinned current-transition artifact, or another non-self-referential design); populate or explicitly exempt the historical finding mappings under a stated rule; emit all changed sections or label and enumerate truncation; and require the exact V24→V25 mapping to cite only findings demonstrably answered by the delta. The checker must return zero before §10 can claim enforcement.

## Required checks that held / failed attacks

1. **Subject substitution attack failed:** V25's full digest exactly matches `runner_v25_chain.log`.
2. **Catalogue-source substitution attack failed:** `quality_selected.csv` recomputes to the full digest printed at §2.7 line 376.
3. **Absolute-threshold sweep held:** normative V25 contains only `flux_ivar_r > 8.4000532`, `psfsize_r < 1.5699703`, and `nobs_r >= 3` (lines 373–375 and 691). No percentile remains in normative V25 text. Percentile provenance remains only in the external measurement receipt/adoption explanation.
4. **Independent row recount held:** direct CSV parsing found 65,060 rows and exactly 49,211 passing the three strict thresholds, an attrition of 15,849 (24.36059%).
5. **Post-exclusion number check held locally:** §4 lines 461–468 prints post-exclusion `N = 49,211`, `N_eq = 110,983`; BS-5f line 712 prints the same values. `quality_cut_receipt.json` records `n_after = 49211` and `n_eq = 110982.5`, which rounds to 110,983. The pre-exclusion 147,578 is explicitly labelled pre-exclusion at line 463 rather than used as BS-5f's value.
6. **Parent-pin wording held:** §2.7 line 380 explicitly keeps `PINNED_PARENT_SHA256`, `PINNED_PARENT_ROWS = 65_060`, and `PINNED_SELECTION_BRICKS = 6_445` unchanged.
7. **Carried-open BS-2v/Row-L block was not silently erased:** line 31 names both; BS-2v remains UNRESOLVED at line 693; Clause 10 still blocks BS-6/first image byte at line 580. The preamble's old “VOID reachability repaired” wording remains contradictory, but the carried-open condition itself is visible.
8. **Threshold-neighbour sweep:** the new catalogue thresholds have an exclusion branch, timing statement, and P8 effect, but that sweep exposed Finding 2: their phase/effect cannot produce the P5 population claimed by §4/BS-5f. Existing `a_LB_b`, spread, Stage-P/C, decision-region, hand-check-floor, and VOID thresholds retain their prior stated values; reverse VOID reachability remains openly unresolved.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`, fetch any image byte, or run any χ-bearing operation.
- The authorised-query chronology, DESI catalogue semantics, reported axis correlations/variance, and external scientific claims are **Testimony** except where I independently checked hashes and row-level threshold counts from the named lane-local CSV.
- I did not treat prior referee conclusions as ground truth. I read the V24 reports only to test whether the finding IDs now claimed in `FINDINGS_MAP.md` are honestly answered by V25's bytes and current checker.
- I did not modify the subject, receipts, tools, predecessor drafts, or any file outside this report.

## Evidence ledger and custody

Content read: `BRIEF_V25_WHOLE_REVIEW.md`; `runner_v25_chain.log`; the complete pinned V25 draft; `BS2A_QUALITY_CUT_RECEIPT_20260828.md`; `BS2A_CUT_ADOPTION_20260828.md`; `FINDINGS_MAP.md`; `quality_cut_receipt.json`; V24 whole-review reports; and `tools/prereg_trace.py`. Programmatic/read-only checks: SHA-256 of V25, V24, `quality_selected.csv`, and the receipt; V24→V25 exact diff; full-draft regex sweeps for N/N_eq, status, thresholds, and percentile language; direct CSV threshold recount; §7 count/lint tools; and the §10 checker. The prereg linter reported its two pre-existing missing V2 citation-file findings; the count tool reported 15 Class-P/8 Class-E rows but still parsed prose as only BS-2m filled; the trace checker returned 15 problems. A post-write draft hash recheck is recorded below by the final custody command.

**NOT CLEAR**
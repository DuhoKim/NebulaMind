# V31 WHOLE-DOCUMENT REFEREE REVIEW — GPT56

## Verdict

**NOT CLEAR.** V31 exactly matches the dispatched SHA-256, the V30→V31 delta is confined to the dispatched four semantic regions, the McAdam–Shamir quotations are genuine, and all four required checker invocations exit 0. V31 also repairs V30's residual-significance overstatement and the trace omissions. One blocker remains in the new line 120: after correctly refusing the invalid 15%/0.0408 ratio, it reintroduces that comparison through “modest” and “both percent-level,” and it asserts that BS-3 bounds the position-dependent component although the normative document does not yet bind the measurement needed to produce such a bound. This is a correctable preregistration defect, not authorization to proceed; the unfinished programme remains blocked as stated.

## Exact subject and predecessor comparison

I recomputed both SHA-256 digests from the current bytes:

- V31 supplied: `ce1b6914eae0d36b38d5fc77bb0a8d17c3502d4a007611ad39efe7fe78f1349c`
- V31 recomputed: `ce1b6914eae0d36b38d5fc77bb0a8d17c3502d4a007611ad39efe7fe78f1349c`
- V31 comparison: **MATCH**, exact 64-hex equality.
- V30 supplied: `e81becce1b19d88a302ce7004e930467d9b12b24828bcfe037913a2eb978fecc`
- V30 recomputed: `e81becce1b19d88a302ce7004e930467d9b12b24828bcfe037913a2eb978fecc`
- V30 comparison: **MATCH**, exact 64-hex equality.

A direct unified diff contains only the four dispatched semantic regions: (1) the V30→V31 retitle; (2) replacement of §1 line 120; (3) replacement of §1 line 122; and (4) the two appended §10 rows, V28→V29 and V29→V30. Because lines 120 and 122 are adjacent, ordinary unified diff presents them in one textual hunk; there are three unified-diff hunks but four semantic edit regions. No other byte region moved.

I reread all 880 lines of V31 after judging the delta. A direct byte comparison confirms that §1 lines 131–133 are byte-identical between V30 and V31 (276 bytes in each) and §2.7 line 384 is byte-identical (533 bytes in each).

## Numbered findings

### 1. HIGH / BLOCKING — §1 line 120 and §7 line 704 — the repaired paragraph still makes an unearned scale claim and treats an unbound BS-3 measurement as if it already defined a bound

**Why it fails.** The first half of line 120 correctly repairs V30: it identifies the approximately 15% as a relative difference between annotation counts, states that it does not share a denominator with a normalised dipole amplitude, distinguishes an intercept from a slope, and asserts no ratio.

The next sentences nevertheless say that the bias needs only a **“modest”** position-tracking component because the bias and target are **“both percent-level quantities.”** “Modest” is a quantitative comparison in words. Its size cannot be inferred while the 15% denominator is unresolved and the quantities are explicitly noncommensurate. The sentence therefore smuggles back the magnitude argument that the paragraph has just disclaimed. The further statement that “a perfectly position-free bias is not the realistic case” is also stronger than the available evidence: position independence is unestablished and must be measured, but the current bytes do not establish that it is unrealistic.

The final sentence then says BS-3's `antisymmetry_receipt` measures the parity-even part directly **“so the position-dependent component is bounded by measurement instead of by assumption.”** The separate `gates/MIRROR_TEST_DESIGN_20260828.md` explains a potentially sound method: form `d(g)=χ(g)+χ(Mg)` and stratify `⟨d⟩` in `cos θ` bins. But that file says it changes nothing frozen, while V31's normative §7 row 704 specifies only “antisymmetry identity.” V31 does not bind the mirrored sample, transformation implementation, positional strata, statistic, uncertainty construction, bound, acceptance threshold, or failure consequence. A field named `antisymmetry_receipt` is not yet a receiptable position-dependent bound. The draft is allowed to be unfinished, but this part is not honestly marked DESIGN/UNFILLED even though later choice of those items can change whether BS-3 passes.

The qualitative motivation survives without either overclaim: a documented large bias in a closely related classification task makes position independence unsafe to assume, any position-dependent instrument component can project onto the tested slope, and only a frozen stratified mirror measurement can determine how large that component is.

**Smallest sufficient repair.** In line 120, remove “modest,” the cross-metric “both percent-level” rationale, and “not the realistic case.” State instead that the 15% figure supplies qualitative motivation only; the size of any projected component is unknown until measured. Then either (a) mark BS-3's antisymmetry component **DESIGN, UNFILLED** and bind the mirrored-input operation, sample, positional stratification, statistic, uncertainty/bound, acceptance rule, and failure consequence before BS-6, or (b) point to an immutable normative artifact that binds those items and pin its digest in this preregistration. Only after that can the document say the component is bounded by measurement.

## McAdam–Shamir source verification

I fetched arXiv:2302.06530 itself from `https://arxiv.org/pdf/2302.06530` and its arXiv source bundle from `https://export.arxiv.org/e-print/2302.06530`, then inspected the PDF text and `main.tex` rather than relying on the brief or V31.

- PDF SHA-256: `022d08e5975a9562b289e0e7566d2b17c1bbc276f2fb45764e95eec6ce60567e`
- arXiv source-bundle SHA-256: `735bdbaafdaf141ef90583a23e0c118ce2d16508ef0faef035c496c4ac649693`
- extracted `main.tex` SHA-256: `cbffd8e1ba852ae0bdbd31e949d341e88597cd6aada95ab53c97274b81596c87`

Results:

1. **Line 120 quotation — verified.** Source `main.tex` line 76 and PDF text lines 136–140 contain “That large difference of ∼15%” and attribute it to “bias of the human perception or the user interface, rather than a reflection of the real distribution of spiral galaxies in the sky.” V31's two quotations are faithful after ordinary sentence-case/markup normalization.
2. **Line 122 abstract quotations — verified.** The arXiv source abstract says the chance probability is “lower than 0.01” and gives “a dipole axis with statistical strength of 2.33σ to 3.97σ.” V31 quotes both faithfully.
3. **Line 122 mirrored-control quotation — verified.** PDF text lines 121–129 and `main.tex` line 81 say the body values are `P∼0.13` and `P∼0.21` and continue: “These probabilities are not considered statistically significant, which can possibly result from the low number of galaxies, but the direction and magnitude of the distribution also does not conflict with the observed distribution.” V31's quotation is faithful.
4. **Evidentiary distinction — verified.** The significant `<0.01` and `2.33σ–3.97σ` statements concern the paper's separate SpArcFiRe analyses. The body explicitly calls the Land mirrored-control probabilities nonsignificant. V31 is therefore correct that the reanalysis does not establish significance of Land's post-mirror residual; this is not an overcorrection.
5. **Source-internal caveat, nonblocking.** The narrative body gives `P∼0.13` and `P∼0.21`, while the paper's later Table 2 prints `0.18` and `0.21` for its Land rows. V31 accurately quotes the narrative body and its conclusion is unchanged under either pair, but a future precision edit could label these specifically as the narrative-body values or omit the numbers.

## Trace repair and honesty

The two appended §10 rows are consistent with the mechanical diff fields and digest prefixes. The V29→V30 row honestly identifies `PRINCIPAL-20260828-LAND-NULL` as a human direction and expressly refuses to invent a referee finding ID. `gates/FINDINGS_MAP.md` contains both the V29→V30 instruction mapping and the current V30→V31 referee-finding mapping. V31 correctly omits an in-band V30→V31 row because the current transition belongs in the sidecar under the stated non-self-referential contract.

## Required tool executions

All four commands were run by this seat against the pinned V31 bytes.

1. `python3 tools/prereg_lint.py <V31> --gates <gates>` — exit **0**:
   - `§7 data rows: 23 (15 class P, 8 class E) — 22 carry a BS- identifier`
   - `no inconsistencies found (all 6 checks demonstrated they can fail)`
2. `python3 tools/prereg_lint.py <V31> --gates <gates> --self-test` — exit **0**:
   - all six controls reported `OK`
   - `self-test: 6 controls, 0 failure(s)`
3. `python3 tools/prereg_trace.py <build-root> --check <V31>` — exit **0**:
   - `30 computed transition(s); 0 problem(s)`
4. `python3 tools/prereg_trace.py <build-root> --check <V31> --self-test` — exit **0**:
   - in-band removal detection: `OK`
   - current-transition sidecar: `OK`
   - synthetic-later-draft out-of-scope rule: `OK`
   - `self-test: 3 scope rules, 0 failure(s)`

Passing these checks establishes their implemented contracts; it does not cure Finding 1, which is semantic and outside their current predicates.

## Failed attacks and held boundaries

1. **Subject-substitution attack — failed.** Both V31 and V30 match their supplied full SHA-256 pins.
2. **Hidden-delta attack — failed.** No bytes outside the four dispatched semantic regions changed.
3. **Quotation-fabrication attack — failed.** Every quoted McAdam–Shamir phrase at lines 120 and 122 appears in arXiv:2302.06530 itself.
4. **Residual-significance overstatement attack — failed.** V31 separates the nonsignificant Land-control residual from the reanalysis's significant separate analyses and does not adjudicate the literature.
5. **Trace-closure attack — failed.** Lint, lint self-test, trace check, and trace self-test all exit 0; the human-instruction mapping is honest.
6. **Scope-drift attack — failed.** Lines 131–133 remain byte-identical and still exclude testing Shamir or isotropy.
7. **Unfinished-programme overclaim attack — failed.** The whole-document reread retains BS-2a as DESIGN/UNFILLED; one of fifteen class-P slots filled; BS-2v UNRESOLVED; findings 1, 2, 2b and 3 UNRESOLVED; Rows C2 and E unable to run; Stage P `SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK`; BS-5p unfillable pending rerun; and BS-6 plus the first image byte blocked.
8. **Conditional-independence concealment attack — failed.** §2.7 line 384 is byte-identical to V30 and continues to say that independence from handedness conditional on position is not established.

## Testimony and limits

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch or authorize any study image byte, execute inference, run Stage P, unblind anything, or modify either draft.
- Statements that no image byte has ever been fetched, historical authorization/custody chronology, and prior survey/run facts are **Testimony** unless reduced above to a current-byte or public-source verification. I verified what V31 currently says about those matters, not the underlying historical world state.
- Temporary arXiv files were kept under `/tmp/gpt56_arxiv230206530`, outside the lane. The only lane write by this seat is this report.

**NOT CLEAR**
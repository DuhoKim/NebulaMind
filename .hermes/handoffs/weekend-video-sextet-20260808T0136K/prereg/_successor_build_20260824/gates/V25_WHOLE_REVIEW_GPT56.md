# V25 WHOLE-DOCUMENT REVIEW — GPT56

Verdict: **NOT CLEAR.** The dispatched V25 bytes match the runner pin, and the three absolute catalogue thresholds independently reproduce 49,211 retained objects and post-exclusion N_eq = 110,982.53, correctly rounded to 110,983 in §4 and BS-5f. The load-bearing temporal-independence argument does not hold as written: prior measurement establishes temporal precedence, not statistical independence, and it says nothing about the C2 process that reads cutouts and can write exclusion-bearing predicate bits. The document also applies the new predicate at P8 while requiring its 49,211-object output at P5, marks a text-and-code DESIGN slot filled although the pinned code contains neither the predicate nor a BS-2a schema, retains contradictory live status/count text, and cites §10 findings that its checker and unchanged six-section truncation do not actually answer.

## Digest first — exact comparison

I recomputed SHA-256 over the current bytes of `../PREREG_SUCCESSOR_DRAFT_V25_20260827.md` before substantive judgment and compared all 64 hex digits with `runner_v25_chain.log` line 5:

- runner pin: `50f2e53256cc79707f2a4dfbf737740e6101742deb39365498737c904aa0f59b`
- recomputed current V25: `50f2e53256cc79707f2a4dfbf737740e6101742deb39365498737c904aa0f59b`
- comparison: **MATCH — exact 64-hex equality**

## Numbered findings

### 1. CRITICAL / BLOCKING — §2.7 lines 372–382, §6.1 Row C2 line 537, Clause 9 line 578, and §11 line 857: temporal precedence is not the claimed independence and cannot discharge C2 blindness

**Why it fails.** The catalogue columns were measured before this study and the thresholds were fixed before any image byte. That establishes a useful, narrower fact: the survey measurements were not caused by this study's later handedness inference, and the threshold values were not selected after seeing that inference. It does **not** establish statistical independence from handedness. The receipt itself shows all three quantities correlate with the tested axis (`−0.2532`, `+0.3659`, `−0.3012`), and the scientific alternative makes handedness axis-dependent. Temporal ordering alone cannot prove the random variables independent.

More decisively, the premise and the process whose controls are removed are different objects. Row C2 reads cutouts and writes `parent_attempt_present`, `byte_integrity_pass`, and `canonical_shape_pass`; the catalogue measurement dates of `flux_ivar_r`, `psfsize_r`, and `nobs_r` say nothing about whether C2 can encode a synthetic sign through those writable/missingness channels. Nevertheless Row C2 line 537 concludes that no hermetic worker, capability allowlist, or blindness fixture is required. Clause 9 line 578 still requires adversarial sign-encoding fixtures against C2, and §11 line 857 still requires the hermetic allowlist and those fixtures. The document therefore both removes and requires the controls, and the temporal argument does not justify their removal.

**Smallest sufficient repair.** Replace “independence from handedness” with the narrower, supportable claim “fixed pre-outcome catalogue predicate,” and define a deterministic verifier over the pinned catalogue bytes, exact join keys, and three literal thresholds. Do not use that fact to waive C2 controls. Keep C2's hermetic/allowlist and adversarial missingness-channel gate unless a separate argument and implementation makes C2 incapable of reading or encoding outcome-adjacent information. BS-2a cannot be FILLED until that separation is explicit and gated.

### 2. CRITICAL / BLOCKING — §2.7 lines 336–343 and 380–382 versus §4 lines 456–468 and §6.1 Rows E/P lines 539/550: the post-exclusion population is required before the document applies the exclusion

**Why it fails.** Section 2.7 line 339 defers confidence-threshold exclusion to post-unblinding handling, and line 382 says Row P applies the new predicate at P8. Row P is post-unblinding. But Stage C and BS-5f run at P5 and §4 says they operate on the post-exclusion `N = 49,211, N_eq = 110,983` mask. Row E, which creates the P3 realised partition consumed by BS-2f, reads only integrity-predicate projections and explicitly excludes instrument absence/non-finiteness; it is not assigned the three catalogue columns or the new quality predicate. No named P0–P5 producer therefore creates the 49,211-object mask that §4 and BS-5f require.

This fails Clause 10 in both directions. Forward, the threshold's named phase is P8 but its value is consumed at P5. Reverse, the P5 `110,983` power gate has no reachable producer. The post-unblinding consequence is also incoherent with the stated pre-unblinding power receipt: any P8 threshold removal emits `INCONCLUSIVE-BY-CALIBRATION`, so the run cannot both analyse the post-exclusion population and treat that same exclusion as a fatal post-lock attrition.

**Smallest sufficient repair.** Seat the fixed catalogue-quality predicate in a named deterministic pre-BS-2f producer (P2/P3), give Row E or a separate row the pinned quality source, exact one-to-one join, threshold computation, terminal status, receipt, and failure effect, and define BS-2f from its 49,211-object output while preserving the 65,060-row parent pin. Reserve Row P's P8 attrition rule for genuinely post-unblinding instrument absence/non-finiteness/confidence events. Then re-audit every neighboring value, phase, and failure effect.

### 3. HIGH / BLOCKING — §0 lines 70–103, preamble lines 23–25, §6 fold record lines 667–670, §7 lines 681–692, and §11 lines 853/857: BS-2a is marked FILLED without its required code and with contradictory live status/count text

**Why it fails.** Section 2.7 line 369 and the §7 BS-2a row line 691 both define BS-2a as a DESIGN slot gated as **text and code** before any image byte. The pinned normative `ref/successor_ref_v9.py` contains neither literal quality threshold, no `flux_ivar_r`/`psfsize_r`/`nobs_r` predicate, and no `SLOT_SCHEMA['BS-2a']`; its `run_production_verdict()` begins from a supplied sealed mask and never constructs or verifies the quality exclusion. The only Python occurrence of the threshold literals in this lane is the drafting patch, not the §0 implementation.

The document then disagrees with its own FILLED claim:

- §7 line 685 still says **one of fifteen** class-P slots is filled, naming only BS-2m; the standing state requires two (BS-2a and BS-2m).
- Preamble lines 24–25 still say findings remain pending the “refused BS-2a design.”
- The fold record lines 667–669 says BS-2a is REFUSED and Rows C2/E cannot run, while current Clause 2 line 559 says it is FILLED and those rows can run.
- §11 line 853 calls the BS-2a schema “deferred with the already-refused BS-2a design,” and line 857 still lists the C2 implementation as future work.

The §7 row did change to FILLED, but the required executable subject did not, and the document's live count/status surfaces did not close.

**Smallest sufficient repair.** Keep BS-2a UNFILLED until the pinned code implements the exact pre-BS-2f construction, exact BS-2a schema/verifier, joins, statuses, receipts, and fixtures and those bytes pass their gate. After that gate, update every live state surface atomically: §2.7, §6.1 rows/clauses, §7 row and “two of fifteen” sentence, §11, and the preamble. Historical quotations must be explicitly scoped as historical rather than readable as current state.

### 4. HIGH / BLOCKING — §6.3 lines 610–612, §10 lines 815–845, `gates/FINDINGS_MAP.md`, and `tools/prereg_trace.py`: the findings mapping is not honestly discharged

**Why it fails.** The findings column exists, but existence is not closure.

1. Running the current trace checker on V25 exits 1 with **15 problems**: it still requires the self-referential V24→V25 row that §10's new footer says must appear only in V26, and it reports no finding cited for every normative transition V1→V2 through V14→V15. Thus the checker contradicts the footer's stated coverage contract and does not enforce the claimed obligation cleanly.
2. `FINDINGS_MAP.md` maps V24→V25 to GPT56-V24-1 and CODEX-V24-5 (the current-row/self-reference defect), but the checker is unchanged and still reports `MISSING: no written row for V24 → V25`.
3. The same map says V25 answers CODEX-V24-6, which found that “sections changed” silently truncates to six sections. The current generator still uses `sorted(... )[:6]`, and V25's header/footer still calls the result “sections changed” without an omitted-section count or disclosure. That finding is cited but not answered.
4. V25's own mechanically generated V24→V25 delta is §10 +27/−26, §2.7 +11/−4, §4 +10/−2, preamble +3/−5, §6.1 +2/−2, §7 +2/−2. Its human mapping exists only in the sidecar and is not a written V25 row under the document's self-reference rule. That can be a valid architecture only if §6.3 and the checker explicitly share the same predecessor-only coverage contract; they currently do not.

**Smallest sufficient repair.** Make the checker expect Vn's table to end at V(n−2)→V(n−1), while separately verifying a pinned sidecar entry for V(n−1)→Vn. Reconcile or explicitly scope the V1–V15 uncited transitions. Emit all changed sections or label and count the truncation, then remove CODEX-V24-6 from “answered” until that repair exists. A mapping may cite a finding only after the claimed repair is verifiable in the current bytes/tool.

## Required checks that held / failed attacks

1. **Post-exclusion N_eq held.** Independent one-to-one merge of `quality_selected.csv` and `positions_selected.csv` produced 65,060/65,060 matches, zero losses/extras, 49,211 rows after the three strict thresholds, population Var(cos θ) `0.7517460749`, and N_eq `110982.5283`, which correctly rounds to **110,983**.
2. **§4 and BS-5f quote the right post-exclusion number.** §4 lines 461–468 and BS-5f line 712 use `N = 49,211, N_eq = 110,983`. The only `147,578` occurrence is explicitly labelled pre-exclusion and warned against as the analysis value. Other `N_eq` values (`120,002.9/120,003`) are clearly the earlier retained planning/Stage-P geometry, not BS-5f.
3. **Absolute-threshold attack held.** Normative V25 text uses only `flux_ivar_r > 8.4000532`, `psfsize_r < 1.5699703`, and `nobs_r >= 3`; no percentile remains in the draft's normative predicate. Independent percentiles reproduce the first two literals exactly, but the operative values are absolute.
4. **Source digest and arithmetic held.** `quality_selected.csv` recomputes to `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3`; pre-cut N_eq independently recomputes as `147577.5389`; the cut leaves 6,104 bricks. The split reproduces as approximately 48.0/52.0 pre-cut and 40.8/59.2 post-cut (orientation reversed only by which end is printed first).
5. **Parent-pin posture is stated.** §2.7 line 380 explicitly keeps `PINNED_PARENT_SHA256`, `PINNED_PARENT_ROWS = 65_060`, and `PINNED_SELECTION_BRICKS = 6_445` unchanged. Finding 2 concerns where the exclusion is applied, not a hidden parent redefinition.
6. **Carried-open disclosures were not falsely closed.** The preamble still names BS-2v converter independence, its authenticated receipt-schema absence, Row L's self-voiding signing path, and preamble/live-state contradiction as carried open. Clause 10 still says reverse reachability is unresolved and BS-6/first image byte remain blocked.
7. **Binding-table shape held.** Independent tools count 15 Class-P and 8 Class-E rows. The defect is the separately typed filled-slot count/status, not the table cardinalities.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`, fetch any image byte, or execute χ-bearing work.
- Survey provenance, authorization chronology, and the claim that the catalogue columns were physically measured before this study remain **Testimony**. I verified the local query texts differ only in their SELECT line, the local quality-file digest, exact 65,060-row one-to-one closure, and the derived cut arithmetic.
- I did not re-run external TAP queries, closure fixtures, Stage P, classifier inference, or citation verification.
- Prior V24 findings were read only because `FINDINGS_MAP.md` cites them and the brief requires judging that mapping. Their conclusions were treated as allegations and checked against current V25/tool bytes.
- No subject, predecessor, code, receipt, or gate artifact was modified. The intended write is this report only.

## Evidence ledger

Content read: `gates/BRIEF_V25_WHOLE_REVIEW.md`; `runner_v25_chain.log`; the whole V25 draft; `BS2A_QUALITY_CUT_RECEIPT_20260828.md`; `BS2A_CUT_ADOPTION_20260828.md`; `gates/FINDINGS_MAP.md`; V24 whole-review reports cited by that map; `acquire/quality_cut_receipt.json`; `quality_query.adql`; `positions_query.adql`; headers/sample rows of the two local CSVs; relevant `ref/successor_ref_v9.py` `SLOT_SCHEMA`, axis, and production-runner regions; `tools/prereg_trace.py`, `prereg_counts.py`, and `prereg_lint.py`.

Executed checks: SHA-256 comparison for V25 and the quality CSV; exact one-to-one quality/position merge; independent threshold, population-variance, N_eq, brick-count, percentile, and split recomputation; exhaustive draft searches for every N/N_eq and threshold/status occurrence; trace checker; count emitter in report mode; linter; independent V24→V25 generated delta and findings-map lookup; scoped pre-write git status.

**NOT CLEAR**
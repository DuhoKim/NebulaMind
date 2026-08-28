# V26 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

**NOT CLEAR.** The dispatched V26 bytes exactly match the runner pin. The round's central independence repair succeeds: V26 makes only the supportable outcome-blind chronology claim and explicitly says independence from handedness conditional on position is **not established**; I found no surviving assertion that the catalogue predicate is statistically independent of handedness. The document nevertheless cannot clear as a whole. It still applies catalogue quality again in the post-unblinding Row-P adequacy path after saying that the same predicate already created the 49,211-row P3 mask; it continues to present the old-population 995/1000 Stage-P result as current instead of superseded; its V25→V26 findings mapping/coverage mechanism is absent and the named checker returns 16 problems; and its Clause-10 surfaces still contradict each other about reverse VOID reachability.

## Digest first — exact comparison

I computed SHA-256 over the exact current bytes of `../PREREG_SUCCESSOR_DRAFT_V26_20260827.md` and compared all 64 hexadecimal digits with the `V26 PINNED sha256` value on line 5 of `runner_v26_chain.log`:

- runner pin: `2eec8da41ee69374fcc9c3fca2de150b29c04ca7b921848e908fa97a20bffd52`
- recomputed V26: `2eec8da41ee69374fcc9c3fca2de150b29c04ca7b921848e908fa97a20bffd52`
- comparison: **MATCH — exact 64-hex equality**

I also recomputed V25 as `50f2e53256cc79707f2a4dfbf737740e6101742deb39365498737c904aa0f59b`, matching the full predecessor digest printed at V26 lines 3–4.

## Central question

The narrow claim at §2.7 line 378 is correctly narrow. It states only that the columns and absolute thresholds were fixed without reading this study's unobserved χ and before any image byte, so the predicate could not be tuned post hoc. The next sentence expressly says that independence from handedness conditional on position—the estimator-relevant property—is **not established**, and requires either a preregistered check or a stated assumption carrying its risk. I found no other sentence that turns temporal precedence into statistical independence from handedness. The structural “sign-blind” language at lines 340–343 concerns what a predicate may directly read or derive from; it does not close the separately named conditional-independence gap at line 378.

Thus the answer to the central question is: **no claim of statistical independence from handedness survives, and the conditional-independence gap is stated as open rather than replaced by a confident weaker statistical claim.**

## Numbered findings

### 1. CRITICAL / BLOCKING — §§2.7, 5, 6.1, and 7; lines 336–350, 378–382, 489–491, 539–540, 550, 580, and 709–711 — catalogue quality is still assigned incompatible pre- and post-unblinding effects

**Why it fails.** V26 correctly says the frozen catalogue-quality predicate is applied before BS-2f, so Row E produces the 49,211-row realised partition at P2–P3 and Row F seals that mask at P3 (lines 382, 539–540, 709). The independent row-level check supports the value: 65,060 unique catalogue rows produce exactly 49,211 passes and 15,849 exclusions under the three literal thresholds; recomputation from the pinned axis and the 49,211 matched positions gives `Var_pop(cos θ) = 0.751746074921` and `N_eq = 110982.528279`, correctly rounded to 110,983.

But the surrounding lifecycle was not fully moved:

- §2.7(2)'s supposedly closed pre-lock exclusion list still permits only missing/byte-integrity and tensor-shape exclusions (lines 336–339); it does not enumerate catalogue quality.
- §2.7(4)'s recomputation evidence remains checksum/shape evidence (lines 344–350), while Row E newly relies on separately named “authenticated catalogue-quality evidence fields” without defining their exact source, join, or schema there (line 539).
- §5 says the **post-unblinding adequacy receipt** has `EXCLUDED-BY-CATALOGUE-QUALITY` and that **any** `EXCLUDED-BY-*` deterministically emits run-level `INCONCLUSIVE-BY-CALIBRATION` (line 489).
- Row P at P8 again tests “catalogue quality below frozen threshold,” drops the row, and then says any post-unblinding removal emits `INCONCLUSIVE-BY-CALIBRATION` (line 550; same consequence at lines 491 and 468).

Therefore the same catalogue predicate is both the ordinary pre-BS-2f operation that creates the 49,211-row P3 mask and a fatal post-unblinding P8 removal. The parent/mask/attempt-set semantics do not say how the 15,849 pre-lock quality failures avoid being classified again in Row P. Clause 10's added sentence at line 580 states the desired separation but does not repair these opposite phase/effect assignments.

**Smallest sufficient repair.** Add catalogue quality to §2.7's closed **pre-lock** exclusion vocabulary and define its exact authenticated fields, source digest, one-to-one join keys, verifier, and failure effect in the BS-2a/Row-E path. Remove catalogue quality from Row P's P8 decision precedence and from the post-unblinding adequacy receipt's fatal `EXCLUDED-BY-*` set, or explicitly carry it only as an already-resolved pre-lock status that cannot constitute a P8 removal. Keep P8 absence/non-finiteness/instrument-confidence handling separate. Then make §5, Row P, BS-2f, and Clause 10 use one phase and one consequence.

### 2. HIGH / BLOCKING — §§2.6 and 4; lines 292–312 and 448–450 — Stage P was not marked superseded

**Why it fails.** V26 still prints “Stage P on the reduced set: 995/1000 … PASS,” gives the old geometry `n = 53,005`, `Var(cosθ) = 0.754664`, `N_eq = 120,003`, and later again calls 995/1000 the measurement on the “real REDUCED geometry.” That evidence predates the catalogue-quality mask and does not test the 49,211-row geometry now declared operative at P3/BS-2f. The V25→V26 diff did not alter either Stage-P passage. Calling the 65,060-parent reduction “real” does not make its power result applicable to the later 49,211-row analysis mask.

**Smallest sufficient repair.** Mark the 995/1000 result historical and **superseded/non-applicable** to the post-quality mask. State that BS-5p remains unfillable pending a rerun of the frozen Stage-P test on the actual 49,211-row mask; credit no PASS until that receipt exists.

### 3. HIGH / BLOCKING — §§6.3 and 10, `FINDINGS_MAP.md`, and `tools/prereg_trace.py`; lines 610–611 and 814–844 — the V25→V26 findings map and stated coverage contract are not implemented

**Why it fails.** V26 promises predecessor-only in-band mappings plus a pinned external artifact for the current transition, explicitly exempts V1→V15, and requires an honest mapping. But:

- §10's table ends at V23→V24; it contains no V24→V25 row even though that is the predecessor transition V26 can describe without self-reference.
- `gates/FINDINGS_MAP.md` has no V25→V26 entry and no pinned external V25→V26 mapping artifact exists in the assigned gates directory.
- Running the named checker on the pinned V26 returns **25 computed transitions; 16 problems**: V25→V26 is missing, V1→V15 still fail for uncited findings despite the prose exemption, and V25→V26 has no finding cited.
- The checker still searches the entire draft for a transition token rather than requiring a §10 table row. Consequently line 611's prose mention of “V24→V25” falsely satisfies its row-existence test even though the table has no such row.

The no-silent-cap code repair itself held: `prereg_trace.py` lines 112–116 now emits every changed section. But that does not supply or verify the semantic mapping, and it does not implement the document's predecessor/current/historical coverage rules.

**Smallest sufficient repair.** Make the checker parse actual §10 rows; require V26's in-band table through V24→V25; encode the V1→V15 exemption in the checker; create and pin a separate V25→V26 mapping artifact; and cite only V25 findings that the exact V25→V26 delta demonstrably answers. Re-run to zero problems before claiming enforcement.

### 4. HIGH / BLOCKING — preamble, §6.1 Clause 10, and §7.1; lines 5, 31, 580, and 738–740 — reverse VOID reachability is still contradictory and contains an orphan registry entry

**Why it fails.** The preamble says “VOID reachability [is] repaired here” (line 5), but the same preamble carries BS-2v coverage and authenticated-schema gaps as open (line 31), and Clause 10 correctly says reverse reachability is unresolved and BS-6/the first image byte remain blocked (line 580). These are incompatible current-state assertions.

The registry also contains `VOID-6.1C2-ATTESTATION-FAIL` at line 740, but Row C2's `what voids the run` cell names only “executing the classifier” and “emitting any field outside the schema” (line 537), corresponding to the two neighboring registry IDs at lines 738–739. No C2 attestation-failure antecedent is defined in the source row. The registry therefore has an extra reverse-unreachable ID while claiming exact source/phase/effect closure.

**Smallest sufficient repair.** Delete the false preamble closure claim. Either define the exact C2 attestation-failure antecedent and effect in Row C2 or remove the orphan registry ID. Keep reverse reachability explicitly unresolved and BS-6 blocked until a pinned converter, schema, registry digest, and fixtures establish exact bidirectional closure.

### 5. LOW / NON-BLOCKING — repair-citation integrity; linter output against the whole document

**Why it fails.** The current linter reports two unresolved citation defects: V26 cites `CODEX-V2 4` and `GPT56-V2 4`, but the named `PREREG_TEXT_V2_{CODEX,GPT56}.md` files do not exist in the gates directory. These are not central to V26's catalogue-quality repair, but a whole-document gate should not describe the draft as lint-clean while its own checker returns findings.

**Smallest sufficient repair.** Point each historical citation at the actual retained report or label the attribution unverified; otherwise remove the unsupported finding IDs. Do not call lint clean until the named checker exits zero.

## Checks that held / failed attacks

1. **Subject-substitution attack failed:** current V26 bytes match `runner_v26_chain.log` exactly.
2. **Central modality attack failed:** the predicate is described as outcome-blind only; conditional independence from handedness is explicitly “not established.”
3. **BS-2a walk-back propagation held:** live status surfaces at lines 372, 537, 559, 667, 690, and 852 consistently say DESIGN, defined, UNFILLED/deferred; Rows C2/E cannot run; BS-6 remains blocked.
4. **Class-count attack failed:** direct parsing reports 15 Class-P and 8 Class-E rows, and §7 says one of fifteen is filled, naming only BS-2m.
5. **Mask arithmetic held:** the pinned quality CSV digest is `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3`; all 65,060 `(brickid,objid)` keys are unique; the exact strict thresholds retain 49,211. Independent geometry recomputation gives N_eq 110,982.528279, so 110,983 is correct.
6. **Parent identity wording held:** V26 preserves `PINNED_PARENT_ROWS = 65_060` and distinguishes the parent from the 49,211-row mask.
7. **No-silent-truncation repair held:** the current trace generator has no six-section cap and emits all changed sections.
8. **Standing-state attack mostly held:** one of fifteen is filled; BS-2a and BS-2v remain unfilled/unresolved; Rows C2/E, BS-6, and the first image byte remain blocked. Finding 4 records the contradictory preamble closure claim.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`, fetch an image byte, or run χ-bearing work.
- Survey provenance, authorization chronology, the physical semantics of the DESI columns, and the reported catalogue-axis correlations are **Testimony**. I independently checked only the lane-local file hashes, exact threshold recount, coordinate join, and geometry arithmetic.
- I did not rerun external catalogue queries, Stage P, instrument inference, or scientific citation verification.
- Prior V25 reports were treated as allegations to test against V26's bytes and exact V25→V26 diff, not as ground truth.
- I modified no subject, predecessor, receipt, tool, code, or data artifact; the only intended write is this report.

## Evidence ledger

Content read: `BRIEF_V26_WHOLE_REVIEW.md`; `runner_v26_chain.log`; the complete pinned V26 draft; `BRIEF_V26_REPAIR.md`; both V25 whole-document reports; `FINDINGS_MAP.md`; `tools/prereg_trace.py`; `tools/prereg_counts.py`; `tools/prereg_lint.py`; the pinned-axis region of `ref/successor_ref_v9.py`; and `acquire/quality_cut_receipt.json` through the bounded recount script. Programmatic/read-only checks: SHA-256 of V26, V25, and `quality_selected.csv`; exact V25→V26 diff; whole-draft semantic sweeps for independence, handedness, statuses, counts, phases, thresholds, Stage P, and mappings; exact CSV threshold recount; one-to-one coordinate join and independent N_eq computation; count tool; linter; and trace checker.

**NOT CLEAR**
# V22 WHOLE-DOCUMENT REVIEW — GPT56

## Verdict

V22 is **NOT CLEAR**. It is substantially honest about being an unfinished programme: Findings 1, 2, 2b and 3 remain unresolved, BS-2a remains refused, Rows C2 and E cannot run, `VOID` remains non-executable, and BS-6/the first image byte remain blocked. However, the live §7 count is again false: the Class-E table has eight data rows, not seven. The new lint check reports seven only because its row parser recognizes `BS-*` identifiers and silently omits the row named `Unblinding receipt`. In addition, BS-2v is not yet enforceable against incomplete coverage: the converter is allowed to define the purported reference registry, while the only stated equality compares fixture IDs to converter IDs. A converter and fixture can therefore omit the same real antecedent and pass. These defects also make two parts of the §10 repair trace false.

## Subject identity — verified before opening

I first compared the SHA-256 computed from the live bytes of `../PREREG_SUCCESSOR_DRAFT_V22_20260827.md` with the brief's required digest:

- Required: `9b09416685e966cc9ffbbca12f5e67e94d853c69b0da552b380f2bd54be2a8f3`
- `shasum -a 256` returned: `9b09416685e966cc9ffbbca12f5e67e94d853c69b0da552b380f2bd54be2a8f3  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V22_20260827.md`
- Comparison: **MATCH**.

I opened V22 only after that comparison. I also compared the live V21 bytes with V22's banner pin. The computed V21 digest was `8386d5f0b3cdc8ed4161545dbcf2f8e4898c9c68942ddfc117b3103ef6ea10e5`: **MATCH**.

The live §0 code pins also matched:

- `ref/successor_ref_v9.py`: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` — **MATCH**.
- `ref/closure_worker_v9.py`: `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959` — **MATCH**.

## Numbered findings

### 1. HIGH / BLOCKING — §7 lines 664–703; §10 lines 775–823; `tools/prereg_lint.py` lines 30–42 and 148–179: Class E has eight rows, and the repaired lint guard silently omits one

**Independent count.** I parsed the two §7 tables by their Markdown data rows, excluding only each header and separator.

- Class P has **15** rows: BS-1, BS-1b, BS-2a, BS-2k, BS-2v, BS-2c, BS-2o, BS-5p, BS-2s, BS-2m, BS-3, BS-9, BS-4, BS-7p and BS-8p. One is marked filled, BS-2m. This agrees with line 672.
- Class E has **8** rows: BS-6, BS-2f, BS-8f, BS-5f, BS-L, **Unblinding receipt**, BS-7f and BS-V. Line 672 says seven. It is false.

The `Unblinding receipt` row is physically inside the single table headed `Class E — execution gates`, and that table's first column is named `slot`. No separator or prose excludes it from the Class-E count. This is the same representation issue already visible in V16: a named post-unblinding artifact was inserted as a row in the Class-E slot table. A parser cannot discard that row merely because its identifier lacks the `BS-` prefix.

**Why the lint result is not evidence of closure.** Running the named linter returned:

`§7 slot rows found: 22 (15 class P, 7 class E)`

`no inconsistencies found`

But `slot_rows()` recognizes only rows matching `BS-[0-9]+[a-z]?` or `BS-[A-Z]` (lines 30 and 39–41). It therefore does not count `| Unblinding receipt | ... |`, even though the row is under the Class-E table. The count guard is blind to the exact row at issue. The §7 sentence also claims lint checks the DESIGN inventory; the linter has no DESIGN-inventory comparison at all. Its class-agreement check is not such an inventory check.

**Historical/trace comparison.** I independently counted every adjacent version:

- V16: P=14, E=8, prose E=7.
- V17–V20: P=14, E=8, prose E=8.
- V21: P=15, E=8, prose E=8.
- V22: P=15, E=8, prose E=7.

Thus V17 changed the prose from the wrong seven to the correct eight; it did not introduce an eight-over-seven-table error. V22 changed the correct prose count back to the wrong value. Consequently, §10 line 780 (“the table held 7”), line 820 (“7 to match the table”), and line 823 (“V17 introduced the class-E count error”) are all inaccurate.

**Why it fails.** The document makes a false current-state count, claims a non-firing guard proves it, and records the inverse history as a repair. This is exactly the row-insertion/count-closure failure the brief requires the gate to catch.

**Smallest sufficient repair.** Either (a) keep the row where it is, restore the live count to eight, and repair the V16→V17 and V21→V22 trace text to say V17 corrected seven to eight and V22 preserves eight; or (b) move `Unblinding receipt` out of the Class-E slot table into a separately headed post-unblinding-artifact list/table and retain seven. In either case, make the linter count every Markdown data row between the Class-E heading and §8 rather than only `BS-*` names, and add the promised DESIGN-inventory check.

### 2. HIGH / BLOCKING — Clause 10 line 567; §7 line 680; §10 line 821; §11 line 842: BS-2v's set equality is self-referential and cannot fail a common-mode omission

**What held.** BS-2v now has a stable slot ID, producer Hwao, a named code symbol, Class-P/DESIGN/UNFILLED status, and a direct `blocks BS-6` edge. Clause 10 independently keeps `VOID` reverse reachability unresolved and blocks BS-6/the first image byte. §11 repeats BS-2v as pre-BS-6 future work. The Class-P count, filled count and three-item DESIGN inventory agree with the visible Class-P rows.

**What does not hold.** The document does not itself provide or pin the closed antecedent reference set. Line 680 says the converter “must define” a canonical registry and then requires only:

`set(fixture.antecedent_id) == set(converter.branch_id)`

That compares two products controlled by the same future implementation package. If a real antecedent is omitted from both the converter and fixtures, equality still passes. The gate has no third, independently frozen set against which to detect the common omission.

The source universe is not reducible to one already enumerated set in the document. §5 gives broad categories (“forbidden acts,” “protocol/digest deviation,” and permutation/statistic/protocol non-finite or degenerate failures); the §6.1 lifecycle table contains 20 separate row-level “what voids the run” cells, many with multiple semicolon-separated branches; Clause 5 adds out-of-row access; and §6.3 adds post-first-real-χ binding changes. V22 neither assigns stable IDs to those antecedents nor pins a manifest containing them. “Exact source/phase/failure-effect” is a requirement on the future converter's registry, not a schema or reference set already specified by this document.

The stated duplicate/extra/non-`VOID` failure effects help only after the expected universe exists. They cannot detect an antecedent absent from both sides of the comparison. Accordingly, §10 line 821 overstates the bytes: V22 requires a future registry with stable IDs, but it does not specify “a canonical antecedent-manifest schema” or actual stable IDs, and it does not make the gate enforce completeness against an independent reference.

**Why it fails.** A gate using only V22 cannot decide that an antecedent manifest is incomplete. The proposed equality establishes converter/fixture self-consistency, not coverage of the document's full `VOID` law. Therefore BS-2v is conservatively unfilled and BS-6 remains blocked, but the slot is not yet a receiptable path to closure.

**Smallest sufficient repair.** Freeze the normative antecedent registry outside the converter—either enumerate every stable antecedent ID and its exact source, phase and required `VOID` effect in the document, or name and SHA-pin a canonical manifest whose schema is specified here. Require the gate to enforce uniqueness and three-way equality:

`registry IDs == converter branch IDs == fixture exercised IDs`

Bind the registry, converter, fixture manifest, coverage receipt and gate report digests into BS-2v. A missing ID on either implementation side, an unrecognized extra, a duplicate, an unreachable branch, or a non-`VOID` effect must fail.

## V21→V22 changed-line and neighbour audit

A complete adjacent line-sequence comparison returned **8 non-equal hunks, 8 old lines, 17 new lines, 25 changed lines total**, agreeing with the brief's “25 lines changed.” I inspected the neighbours on both sides of every hunk.

- Banner identity/pin: correct.
- §5 unresolved implementation inventory: the three requested adequacy items were added explicitly; neighbouring present-tense return inventory remains accurate.
- §7 count/DESIGN sentence: Class P and DESIGN inventory are correct; Class E is wrong (Finding 1).
- BS-2v row: stable ID/producer/symbol/block edge added, but the closure reference remains self-defined (Finding 2).
- V16→V17 trace correction: factually inverted (Finding 1).
- V21→V22 trace block: the adequacy row is accurate; the count row and trace-correction row are false; the BS-2v enforceability row overstates what was specified.
- §11 adequacy validator: accurately added as future work.
- §11 BS-2v item: accurately repeats the changed requirement, but repeats the same common-mode omission hole.

I found no unrelated V21→V22 body edit.

## §10 repair-trace audit — all six adjacent-version entries

I compared complete adjacent line sequences with `difflib.SequenceMatcher(autojunk=False)`. The mechanical counts were:

- V16→V17: 14 hunks, 27 old lines, 60 new lines.
- V17→V18: 13 hunks, 15 old, 35 new.
- V18→V19: 8 hunks, 11 old, 19 new.
- V19→V20: 8 hunks, 7 old, 19 new.
- V20→V21: 9 hunks, 7 old, 18 new.
- V21→V22: 8 hunks, 8 old, 17 new.

Rulings:

1. **V16→V17 — NOT ACCURATE in V22.** The operative-body, Row-P citation, §4, candidate-evidence and spread edits are real. The count row is false: the Class-E table had eight rows in both V16 and V17; V17 corrected prose seven to eight.
2. **V17→V18 — ACCURATE.** The adjacent diff contains the threshold-ownership/reason-(d), precedence, registry/Row-I, chronology and trace changes stated.
3. **V18→V19 — ACCURATE.** The lifecycle producer partition, narrowed runner claim, non-finite split and trace repairs are present.
4. **V19→V20 — ACCURATE after the V21 wording correction.** The adjacent diff supports the runner inventory, producer additions, non-executable `VOID`, aggregate-validator future-work wording and trace repair.
5. **V20→V21 — BYTE-ACCURATE AS A CHANGE RECORD, SEMANTICALLY INCOMPLETE.** It accurately records the added unresolved status, converter dependency and aggregate trace correction; it does not claim that BS-2v is already enforceable.
6. **V21→V22 — NOT ACCURATE.** Its adequacy-validator row is accurate. Its count and historical-trace rows are false (Finding 1), and its BS-2v row overstates a requirement to define a future registry as an already specified antecedent-manifest schema/reference set (Finding 2).

Therefore all six trace entries are not accurate as a set.

## Clause 10 audit across §§0–11 — both directions

I read the whole document forward (antecedent/branch → terminal effect) and backward (named outcome/effect → antecedent and phase), expecting `VOID` to remain explicitly unresolved.

### Forward termination

The non-`VOID` branches remain single-valued at document-contract level:

- Numeric decision at P8: reproduction, rejection and numeric inconclusive are complementary regions.
- Calibration at P5: any `a_LB_b < 0.85` halts pre-unblinding as `INCONCLUSIVE-BY-CALIBRATION`; equality belongs to the passing complement.
- Spread at P5: `<= 0.03` selects scalar; `> 0.03` selects profile; profile is not a failure.
- Stage C at P5: calibration or power failure halts before BS-L; only the complementary PASS reaches BS-5f/BS-L.
- Row I: a missing/non-finite allocated output aborts before BS-8f as `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT`.
- Row P at P8: zero, duplicate, orphan and malformed cases have ordered accounting refusals; absence, non-finite and low confidence are exclusions, and any removal deterministically yields `INCONCLUSIVE-BY-CALIBRATION` without a Stage-C rerun; the accepted-finite complement proceeds.
- Production `N_eq < 100,000` produces `INCONCLUSIVE-BY-POWER`; equality passes that guard.

`VOID` is not falsely presented as complete: §5 says the category is not executable, the runner inventory lists conversion as unresolved, Clause 10 says reverse reachability and executability are unresolved, BS-2v is Class-P/unfilled and blocks BS-6, and §11 lists implementation as future work. That unfinished status is honest. Finding 2 shows that the proposed slot contract still cannot be used to prove future completion.

### Reverse reachability

Every currently named non-`VOID` run outcome has a stated antecedent and phase: the three numeric outcomes at P8; power halts from Stage C and the production `N_eq` guard; calibration halts from Row J, aggregate invalidity and any Row-P removal; missing allocated output from Row I; and the four accounting refusals from Row P. Per-attempt states are explicitly not run outcomes.

The reverse audit intentionally stops at `VOID`: its antecedent universe is broad and not assigned stable IDs, and no executable converter exists. V22 correctly says this is unresolved, but BS-2v does not yet supply the closed independent registry needed to resolve it.

## Threshold sweep — value, phase, failure effect

I compared the operative thresholds against their neighbouring prose and, where §0 makes code normative, against the pinned v9 constants/branches.

- **Population cuts, BS-2c/P0:** `flux_r > 0`; `0 <= z_phot_median < 0.15`; ellipticity sum `< 0.1836734693877551` (equivalently `b/a > 0.4`); `dered_mag_r < 17.7`; `shape_r > 1.5`. Failure makes the object ineligible for the parent/count oracle; it is not a post-inference outcome.
- **Release choice, BS-1/P0:** by 2026-09-05, absent DR11 photo-z selects Branch B; selecting A voids the current §0 pin and requires a new preregistration.
- **Exact algorithm boundary, planning/P0:** candidate universes `<=16` use exact enumeration; larger universes receive only the frozen procedure's result and no optimality claim. This is an algorithm branch, not a run failure.
- **Retention/planning:** retained count is `floor(0.8572*n)`; `L_plan = 1.2*L_min_plan`. These are frozen transformations, not discretionary post-data thresholds.
- **Geometry floor, planning and production:** `N_eq >=100,000`. Planning prefixes below it are skipped; no passing prefix leaves BS-5p unfilled/inconclusive by power. Production `<100,000` returns `INCONCLUSIVE-BY-POWER`; equality proceeds.
- **Stage P/C planning accuracy:** floor `a=0.85`. The implemented calibration guard uses `<0.85` as failure; equality passes.
- **Calibration spread, P5:** `<=0.03` scalar and `>0.03` profile. Neither branch is a failure once the 0.85 floor passes.
- **Stage-P/Stage-C trial success:** one-sided `p<0.001`. Stage PASS requires at least 962 of exactly 1,000 trials; 961 fails. Any `refuted` or `nonconservative` self-check also fails closed. At Stage P that prevents BS-5p/selection completion; at Stage C it emits `INCONCLUSIVE-BY-POWER` and blocks BS-L.
- **Near-boundary confirmation, Stage P/C:** successes within 10x of the `0.001` boundary are independently retested; a single unconfirmed success fails the stage. The pinned source implements the lower edge as `0.001*0.1` and the success upper edge as strict `<0.001`.
- **Calibration lower bound, P5:** any `a_LB_b<0.85` emits pre-unblinding `INCONCLUSIVE-BY-CALIBRATION`; equality enters the spread test. Aggregate non-finite/degenerate failure is assigned the same run outcome, while Row-I missing allocated outputs have their separate outcome. The necessary emitters/validator remain disclosed as unimplemented.
- **Hand-check allocation floors, pre-BS-8f:** at least 10 per non-empty joint cell and at least 30 real labels per live inherited stratum; infeasibility fails rather than shrinking.
- **Confidence threshold, BS-2a then P8:** the numeric value is deliberately **UNFILLED** because BS-2a is refused. The document does fix its timing (before the first image byte), owner (BS-2a), and effect: below threshold gives `EXCLUDED-BY-CONFIDENCE`, and any such removal yields `INCONCLUSIVE-BY-CALIBRATION`; a post-first-real-χ threshold change voids the run.
- **Numeric verdict at P8:** reproduction requires strict `p<0.001`, positive/Longo sign, `|A_L-0.0408|<=3*sigma_comb`, and `A_L>=3.09*sigma_ours(a_LB)`; rejection requires strict `p>0.05` and `|A_L|+3*sigma_ours<0.0408`; all complements, including `p==0.001` and `p==0.05`, are numeric `INCONCLUSIVE`.

The pinned source constants matched the prose where implemented: `N_PERM=100000`, `N_TRIALS=1000`, `CP_PASS_X=962`, `P_REPRODUCED=0.001`, `P_REJECT_MIN=0.05`, `A_FLOOR=0.85`, `FLOOR_MULT=3.09`, `NEQ_MIN=100000`, `RETENTION_LB=0.8572`, `L_PLAN_MARGIN=1.2`, `N_EXACT=16`, and hand-check floors 10/30. I found no threshold inversion or equality gap. The source still contains zero occurrences of `verify_lock`, `verify_unblinding_receipt`, `VOID_converter`, `validate_calibration_aggregates`, `INCONCLUSIVE-BY-MISSING-RECORD`, and `EXCLUDED-BY-ABSENCE`, agreeing with V22's unfinished-implementation posture.

## Failed attacks / points that held

1. Digest substitution attack failed: V22, its V21 banner pin, and both §0 code pins matched live bytes.
2. Class-P recount attack failed: there are exactly 15 Class-P rows, one filled, and the visible DESIGN classification is exactly BS-2a, BS-2k and BS-2v.
3. Missing BS-2v dependency attack failed: §7, Clause 10 and §11 all make it pre-BS-6; BS-L's generic ordered Class-P manifest also necessarily includes it.
4. Adequacy-inventory omission attack failed: V22 adds exact final-mask binding, post-unblinding ledger recomputation and adequacy-tree pre-statistic refusal to §5 and adds a named validator plus negative fixture to §11.
5. Hidden-closure attack failed: `VOID`, BS-2a, Rows C2/E, `verify_lock()` and the other named mechanisms remain openly unimplemented/unfilled.
6. Non-`VOID` Clause-10 attack failed: forward effects and reverse antecedents remain single-valued at the document-contract level.
7. Threshold inversion/equality attack failed: the key values, phases, strictness and complementary effects agree with the pinned source where implemented.
8. Unrelated-change attack failed: the complete V21→V22 diff contains 25 changed lines and no unrelated body edit.

## Testimony / unverified assertions

I did not promote the following to verified findings: Longo bibliographic/quotation claims; historical fold times or authority; historical seat verdict chronology; real-geometry, image-volume, Stage-P, closure or fixture measurements; prior authorization statements; or old custody/immutability claims beyond the hashes recomputed here. Those remain **Testimony**.

I did not read `/Users/duhokim/NebulaMindData/`, fetch anything, touch real data, inspect secrets, modify the reviewed draft/code, or run any science acquisition or measurement.

## Evidence ledger and constraints

Content read:

- `gates/BRIEF_V22_WHOLE_REVIEW.md`, all 68 lines.
- `PREREG_SUCCESSOR_DRAFT_V22_20260827.md`, all 842 lines, only after digest match.
- Complete V21→V22 unified diff and all changed-line neighbours.
- `tools/prereg_lint.py`, all 234 lines, then its real run against V22.
- `ref/successor_ref_v9.py` constants and relevant Stage-P, calibration, decision and production-runner regions.
- V16–V22 through complete adjacent line-sequence comparisons and independent §7 table parses.
- V21 GPT56 review and `repair_v17.py` only as historical inputs-to-attack; the findings above rely on fresh table parses, live code/lint reads and adjacent-version comparisons rather than accepting those documents as ground truth.

Mechanical results:

- Absolute `cd` plus `pwd` returned the assigned gates directory.
- SHA comparisons: V22, V21 and both §0 code pins matched.
- V21→V22 sequence diff: 8 hunks, 8 old lines, 17 new lines, 25 total changed lines.
- §7 independent row parse: Class P=15, Class E=8.
- Version-by-version row parse: Class E=8 in every V16–V22 table; prose changed 7→8 in V17 and 8→7 in V22.
- Linter run: exit 0, reported P=15/E=7 because its `BS-*` row regex omits `Unblinding receipt`.
- Six adjacent-version trace comparisons: hunk/change counts and rulings recorded above.
- Threshold/source comparison: constants and branch lines recorded above.
- Pre-write report-path check: absent.

The only authorized write was this report.

**NOT CLEAR**
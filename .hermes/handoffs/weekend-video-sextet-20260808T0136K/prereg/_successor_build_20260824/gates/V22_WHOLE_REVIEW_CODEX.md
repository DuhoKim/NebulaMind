# V22 whole-document referee — CODEX

## Verdict

**NOT CLEAR.** V22 is an honest unfinished programme in its Clause-10/`VOID` posture, but it is not yet a correct preregistration. An independent row count finds 15 Class-P rows and **8**, not 7, Class-E rows. The new BS-2v coverage condition compares two implementation-controlled sets rather than either set against a closed reference set fixed by the document, and BS-2v is absent from the document's exhaustive non-χ-bearing `SLOT_SCHEMA` inventory and from the required schema work in §11. The repair trace consequently makes two false closure claims.

## Digest-first comparison

Before opening the subject I compared the brief's expected SHA-256

`9b09416685e966cc9ffbbca12f5e67e94d853c69b0da552b380f2bd54be2a8f3`

against a fresh `shasum -a 256` of `PREREG_SUCCESSOR_DRAFT_V22_20260827.md`. The command returned

`9b09416685e966cc9ffbbca12f5e67e94d853c69b0da552b380f2bd54be2a8f3`.

Comparison result: **exact match**.

## Findings

### 1. HIGH / BLOCKING — §7 lines 664–703: the Class-E row count is 8, not 7, and the new lint remains blind to the eighth row

I counted data rows, not asserted slot IDs.

- Class P has 15 rows: BS-1, BS-1b, BS-2a, BS-2k, BS-2v, BS-2c, BS-2o, BS-5p, BS-2s, BS-2m, BS-3, BS-9, BS-4, BS-7p, BS-8p.
- Class E has 8 rows: BS-6, BS-2f, BS-8f, BS-5f, BS-L, **Unblinding receipt**, BS-7f, BS-V.

The prose at line 672 says “There are 7 class-E slots,” but the Class-E table contains eight data rows. The unblinding-receipt row is not decorative: it has a producer, content, and a block target, and it sits under the §7 “Binding slots” heading and the Class-E execution-gates heading.

The linter's clean result does not rescue this. Running it returned `22 (15 class P, 7 class E)` and “no inconsistencies found,” because `slot_rows()` at `tools/prereg_lint.py` lines 39–41 recognizes only row labels matching `BS-*`. It silently excludes the `Unblinding receipt` row. This is the same vacuous-guard class described in the brief: the check cannot see a real table row and therefore certifies the prose count against a filtered subset.

Why it fails: the brief required both classes of §7 **rows** to be independently counted. The current prose and lint assertion disagree with the actual Class-E table.

Smallest sufficient repair: count all non-header data rows and restore the Class-E prose to 8; change the linter to parse every data row within each class table. If the author instead intends the unblinding receipt not to be a Class-E binding slot, move it outside the table and state that classification explicitly; merely filtering its label is not a valid count rule.

### 2. HIGH / BLOCKING — §7 line 680 and §11 line 842: BS-2v's set-equality test has no independent closed reference set

The document specifies

`set(fixture.antecedent_id) == set(converter.branch_id)`.

That compares exercised IDs with converter branch IDs. Both sides are produced by the implementation being gated. A converter can omit one required antecedent and its fixture can omit the same antecedent; the equality still passes. Calling the converter's own registry “canonical” and “closed” does not create an independent reference set.

The only external description is “each `VOID` branch in §5 and §6” / “every enumerated void antecedent.” The document does not enumerate stable antecedent IDs itself, does not name a separately pinned registry artifact, and does not define a mechanical extraction that turns the natural-language §5/§6 branches into the authoritative ID set. Consequently a gate using only this document cannot prove that an implementation manifest is complete. Set equality against what, exactly? Against the converter's own branch IDs—not against a document-fixed normative set.

There is a second mechanical weakness: ordinary set equality erases duplicates. Lines 680 and 842 say duplicates fail, but the displayed equality cannot detect them without a separate uniqueness/cardinality assertion.

Why it fails: BS-2v was added specifically to make Clause-10 reverse reachability decidable. The proposed gate establishes implementation/fixture agreement, not coverage of the preregistration's complete `VOID` antecedent universe.

Smallest sufficient repair: put the canonical stable-ID antecedent registry in the preregistration (or pin a separately gated immutable registry by digest), with one row per antecedent and exact source row/clause, phase, and failure effect. Require independently:

1. converter IDs equal normative registry IDs;
2. exercised fixture IDs equal normative registry IDs;
3. both manifests have unique IDs and row-count closure; and
4. each converted result is exactly `VOID`.

Until then BS-2v remains unfilled and BS-6/first image byte remain blocked.

### 3. HIGH / BLOCKING — §§6.1, 7 and 11, lines 503–513, 680, 832 and 842: BS-2v is not receiptable under the document's own exhaustive schema/custody inventory

Section 6.1 says its non-χ-bearing receipt list is closed and exhaustive. The slot-receipt list at line 505 names the permissible `SLOT_SCHEMA` slots but omits BS-2v. Section 6.1 then says everything else is χ-bearing by default and that gates/referees receive only the closed non-χ-bearing classes and fixtures.

Section 11's explicit `SLOT_SCHEMA` work at line 832 requires additions for BS-L and BS-2k and defers BS-2a, but it does not require a BS-2v schema entry or canonical receipt fields. Line 842 asks for a fixture coverage receipt without repairing that schema inventory.

Why it fails: §7 makes BS-2v a Class-P receipt-bearing prerequisite, while §§6.1/11 give neither a legal non-χ-bearing slot-receipt class nor required canonical receipt fields for it. A gate cannot consume a BS-2v receipt under the document's own custody rules, and BS-L's “every class-P slot receipt” manifest has no declared BS-2v schema to bind.

Smallest sufficient repair: add BS-2v to the exhaustive non-χ-bearing slot-receipt list and to §11's exact `SLOT_SCHEMA` additions; specify authenticated fields including document/registry digest, converter implementation digest, ordered normative IDs, exercised IDs, uniqueness/count closure, per-ID source/phase/failure-effect, and result classification.

### 4. HIGH / BLOCKING — §10 lines 775–823: two of the six V16→V22 trace entries are materially inaccurate

I compared the actual source diffs for all six transitions V16→V17, V17→V18, V18→V19, V19→V20, V20→V21, and V21→V22, not merely the prose trace. I also recomputed every predecessor digest named by V17–V22; all six digest pins match their predecessor bytes.

The V17→V18, V18→V19, V19→V20, and V20→V21 trace entries agree with their diffs. The following claims do not:

1. The V16→V17 trace at line 780 says V17 changed Class-E prose from 7 to 8 “while the table held 7,” introducing an error. The actual Class-E table held eight data rows in V16 and V17, including `Unblinding receipt`. V17's 7→8 prose edit matched the table; V22's 8→7 edit introduced the present mismatch.
2. The V21→V22 trace at lines 820–821 says the Class-E count was corrected “to match the table” and BS-2v was upgraded to an enforceable gate. Neither is true: the table has eight rows, and Findings 2–3 show that the gate lacks an independent reference set and a receiptable schema path.

Why it fails: §10 is the document's mandatory finding→change custody record. It currently records regressions/incomplete repairs as closures.

Smallest sufficient repair: rewrite the V16→V17 count row to state that 7→8 matched the eight-row table; rewrite V21→V22 to disclose the erroneous 8→7 regression. Downgrade the BS-2v trace claim to the exact mechanism added, or complete Findings 2–3 before calling it enforceable.

## Clause 10, both directions, §§0–11

Forward termination outside `VOID` is substantially specified: numeric decisions, calibration halts, power halts, accounting refusals, per-attempt states, row authorizations, and row-local void conditions have named phases and consequences. Reverse reachability to `VOID` is explicitly unresolved at §6.1 Clause 10 line 567, and §5 lines 472–474 also state that `VOID` is not executable. That is honest unfinished-programme status, not a concealed completion claim.

The unresolved status is nevertheless real: §5 groups forbidden acts, protocol/digest deviations, and permutation/statistic/protocol non-finite/degenerate failures; §6 adds row-specific void conditions, out-of-table access, and post-first-real-χ rule changes. No pinned producer currently maps that antecedent universe into `VOID`, and BS-2v does not yet provide the independent completeness oracle needed to close reverse reachability. Therefore Clause 10 is not executable and BS-6 plus the first image byte remain blocked, exactly as the standing state requires.

## Threshold audit: value, phase, failure effect

I compared the operative prose to the pinned `successor_ref_v9.py` constants and branches after verifying the code SHA-256 pin. The principal threshold families are accounted for as follows:

- P0 selection/planning: galaxy cuts are numerically stated in §2.2; retention is `floor(0.8572*n)`; exact mode is `≤16`; `N_eq ≥100,000`; `L_plan=1.2*L_min_plan`. Invalid oracle/closure inputs refuse; inadequate planning/power leaves the Class-P chain unfillable.
- Stage P / BS-5p: `a=0.85`, `p<0.001`, 1,000 trials, 95% lower bound ≥0.95, exactly `x≥962` (961 fails), and the 10× boundary audit are stated. Failure blocks BS-5p and its descendants. The exact-per-trial implementation conflict remains explicitly unresolved.
- Calibration / P3–P5: at least 10 labels per non-empty joint cell and 30 per live inherited stratum; infeasibility fails. `a_LB_b<0.85` yields pre-unblinding `INCONCLUSIVE-BY-CALIBRATION`; on the complement, spread `≤0.03` chooses scalar and `>0.03` chooses profile. Stage-C protocol deviation voids; Stage-C failure yields `INCONCLUSIVE-BY-POWER` before unblinding.
- Production pre-statistic guards: `N_eq<100,000` yields `INCONCLUSIVE-BY-POWER`; a non-passing adequacy branch must refuse before the statistic, though that guard remains unimplemented.
- P8 confidence: the numeric value is deliberately not yet chosen because BS-2a is refused. The phase and effect are fixed: below threshold records `EXCLUDED-BY-CONFIDENCE`; any removal yields `INCONCLUSIVE-BY-CALIBRATION`. This is an explicit unresolved design value, not a silent threshold.
- P8 numeric verdict: `p<0.001`, correct sign, 3σ agreement with 0.0408, and floor `3.09*σ_ours(a_LB)` are required for REPRODUCED; `p>0.05` and the strict upper band below 0.0408 are required for REJECTED; all boundary/equality gaps are INCONCLUSIVE.
- Post-first-real-χ: changing any threshold or other binding rule yields `VOID`; its conversion phase/failure effect is the unresolved Clause-10/BS-2v problem above.

The pinned code constants checked were `N_PERM=100000`, `N_TRIALS=1000`, `CP_PASS_X=962`, `P_REPRODUCED=0.001`, `P_REJECT_MIN=0.05`, `A_FLOOR=0.85`, `RETENTION_LB=0.8572`, `FLOOR_MULT=3.09`, `L_PLAN_MARGIN=1.2`, `NEQ_MIN=100000`, and `N_EXACT=16`; these match the operative prose. I found no additional threshold-value mismatch beyond the unresolved designs already disclosed.

## Failed attacks / points that held

- Subject SHA-256 matched exactly before opening.
- The §0 code pins for `successor_ref_v9.py` and `closure_worker_v9.py` recomputed exactly as `6a9abbbd…` and `28f8e1f9…`.
- Class P independently closes at 15 rows; BS-2m is the sole filled Class-P row; BS-2a, BS-2k and BS-2v are the three DESIGN rows.
- Adding BS-2v did make BS-6 a direct dependency in §7 and §11, while the universal “every class-P slot” freeze/BS-L language also reaches it.
- The exact final-mask binding, post-unblinding ledger recomputation, and adequacy-tree pre-statistic refusal additions appear in both §5 and §11 as the V21→V22 trace claims.
- Four of the six V16→V22 transition traces (V17→V18 through V20→V21) matched their actual diffs.
- Clause 10's unresolved `VOID` status is disclosed in both §5 and §6.1 rather than presented as executable.

## Testimony / deliberately unverified assertions

Per the brief, I did not read `/Users/duhokim/NebulaMindData/` and performed no fetch. Therefore the Longo source quotation, real-geometry measurements, Stage-P run result, historical referee testimony, and real-data/receipt claims remain Testimony in this pass except where their local document wording or pinned local code bytes were compared. I did not rerun science computation or inspect χ-bearing artifacts.

## Evidence ledger and scope

- Read the whole 842-line V22 subject after digest verification.
- Parsed both §7 tables independently, including every non-header data row.
- Read and ran `tools/prereg_lint.py`; inspected its row-label regex and count predicate.
- Diffed each adjacent pair V16→V17 through V21→V22 and reviewed the neighbours of every V21→V22 hunk (banner; §5 inventory; §7 prose/row; §10 trace; §11 inventory).
- Recomputed the predecessor SHA-256 pins cited by V17, V18, V19, V20, V21 and V22; all six matched.
- Recomputed the §0 hashes of `ref/successor_ref_v9.py` and `ref/closure_worker_v9.py`; both matched the document.
- Inspected the pinned code constants and the `stage_power`, `adjudicate_path`, decision, and production-runner branches relevant to thresholds and failure effects.
- Wrote only this report; no source draft, reference code, data, gate predecessor, Git state, or external system was modified.

**NOT CLEAR**
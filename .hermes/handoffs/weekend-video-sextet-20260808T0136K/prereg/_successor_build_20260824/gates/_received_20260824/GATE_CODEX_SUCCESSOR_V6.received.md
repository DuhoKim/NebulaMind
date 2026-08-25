# CODEX adversarial gate — successor preregistration V6

## Verdict

**REFUSED.** The three pins match and the fixture transcript reproduces byte-for-byte, but V6 is not freeze-candidate grade. The directed manifest repair still trusts an unbound caller-supplied planner result; the inherited HC-1H calibration is not implemented; Stage C and the real decision accept non-production inputs or bypasses; the branch choice has no checkable branch-neutral code path; the raw/retained boundary repair is contradicted by the body; the final selected set is not power-retested; and the slot table still omits the schemas, inputs, failure consequences, clean-room specification, and primary-lock implementation its own heading promises.

## Custody pins — computed before review

`shasum -a 256` produced:

- `../PREREG_SUCCESSOR_DRAFT_V6_20260825.md` = `9f40dfb0c1f2d56b67c85507d6b17fee6e926d881faadefe07a4af7f2bf94190`
- `../ref/successor_ref_v2.py` = `dda4436cf0b10710ad9f8a6bb3dff6581c293df31ca8d577b4a2423d33d2dcfd`
- `../ref/FIXTURES_V2_20260825.out` = `4ceb6f94dbebffebdabc18738e156bf4f5db058c3b3c4290df8afc648437e74b`

All three equal the brief's required pins. Review proceeded.

Binding-source pins independently recomputed:

- `../../SUCCESSOR_SCOPE_20260821.md` = `995b2e729a3362f0445cac9d5da6d290fddac9f8018e75f2c0aa87c190c93de7`
- `../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` = `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- `../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md` = `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`
- `../../VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md` = `43b9a6a843ef08a6528f1132db2bee29000c5ecd3def2a3a03c23f672c81cec7`

## Environment and fixture reproduction

- macOS 26.6.2 build 25G83, arm64, little-endian
- CPython 3.9.6, `/Library/Developer/CommandLineTools/usr/bin/python3`
- NumPy 1.26.4

`python3 -B ../ref/successor_ref_v2.py --fixtures` exited 0 with empty stderr. Stdout was 2,616 bytes, SHA-256 `4ceb6f94dbebffebdabc18738e156bf4f5db058c3b3c4290df8afc648437e74b`, and byte-equal to the pinned fixture output.

## Numbered findings

### 1. BLOCKER — `accuracy_from_handcheck()` does not implement the inherited HC-1H estimator it claims to carry

**Quote / symbol.** V6 §6 says the HC-1H measurement and validity rules carry at freeze and says BS-8f's full covariance is produced by `accuracy_from_handcheck()` (V6 lines 217–226; §3 lines 144–149). V3-pred HC-4 defines the correction `a_s = (raw_s − epsilon)/(1 − 2 epsilon)` and the shared-epsilon covariance derivative (V3-pred lines 290–303). The V6 body instead accepts only `(agree_counts, n_counts, sigma_shared)`, sets `a_b = raw`, pools `a_hat = sum(agree)/sum(n)`, and fills every off-diagonal with the same `sigma_shared**2` (code lines 580–602). It has no epsilon estimate, no nine-stratum population weights, and no HC-1H derivative.

**Executed attack.** At raw agreement 0.90 and epsilon 0.05, HC-1H gives `(0.90−0.05)/(1−0.10) = 0.9444444444444444`; the V6 function returns `a_b = 0.90` and `a_hat = 0.90`. Changing `sigma_shared` can change its widths but can never make the required point correction because no epsilon-value parameter exists.

**Why it blocks.** This changes attenuation, scalar/profile adjudication, Stage-C injected accuracy, both decision bands, and the detection floor. It also leaves the 3×9 allocation scientifically disconnected from the per-bin estimator: only three pooled counts enter the producer. This is not a cosmetic covariance omission; it implements a different estimator.

**Minimal repair.** Implement the quoted HC-1H correction from the 3×9 realized cell records, population weights, global synthetic epsilon estimate, mirror/validity triggers, and exact shared-epsilon derivatives for every covariance entry. Enforce the three-bin/nine-stratum schema and reconstruct numeric fixtures from cell-level counts rather than three already-pooled numbers.

### 2. BLOCKER — the frozen hand-check allocation is both underbound and wrong on a feasible input; its tie statement contradicts its body

**Quote / symbol.** V6 §6 promises a frozen 3×9 proportional allocation with minimum 10 per non-empty cell and an explicit tie rule (lines 217–220). `allocate_handcheck(cell_counts, budget)` leaves the outcome-changing budget caller-selectable and distributes the post-minimum remainder in proportion to the original counts, not residual capacities (code lines 553–577). V3-pred fixes 500 real labels and a floor of 30 real labels per inherited HC stratum (V3-pred lines 279–284); neither is enforced by the V6 API.

**Executed attack.** For two non-empty cells with capacities `[10, 100]` and the completely feasible budget 110, the only full allocation is `[10, 100]`. V6 first assigns `[10, 10]`, reapportions the remaining 90 against `[10, 100]`, overshoots the first cell, and raises `allocation exceeds available objects in some cell — FAIL`. The same public function accepts arbitrary budgets when capacities allow. Separately, `calibration_bins()` says a boundary tie goes to the lower bin, while `assign_bins(..., side="right")` sends ties upward: with `c=[-1,0,0,0,1,1]`, boundaries `[0,1]`, every `c=0` row is assigned bin 1, not the lower bin 0 (code lines 538–550).

**Why it blocks.** A valid realized mask can be made unfillable by the normative allocator, while another caller can select a non-HC-1H budget. Boundary ties can change cell populations, allocation, estimates, and the scalar/profile/halt branch.

**Minimal repair.** Freeze the actual quota classes and totals, inherited per-stratum floors, precedence, and a capacity-respecting apportionment over residual capacities. Remove the public budget choice from the production entry point. Make the boundary tie prose and body agree and add high-multiplicity tie fixtures.

### 3. BLOCKER — BS-2m validates only a caller's assertion; a lazy implementation can ship a short manifest and pass

**Quote / symbol.** The directed repair says the selected parent and frozen cutout planner define the required set, including edge neighbours, and that BS-2m prevents the 60,308-versus-60,310 defect (V6 lines 109–122). But `manifest_closure(object_required_bricks)` receives an already-produced mapping, does not receive the selected-parent IDs/digest, does not invoke or hash-check a planner, and does not prove every parent object is present (code lines 272–312).

**Executed attack.** `manifest_closure({'only-one-parent-object':['homebrick']})` followed by `require_manifest_closure(['homebrick'], closure)` passed with manifest count 1 and required count 1. Thus a selected parent of any larger size can be represented by one supplied mapping row and a one-brick manifest. A duplicated candidate manifest `['homebrick','homebrick']` is silently set-deduplicated and also passes.

**Why it blocks.** The check catches the named two missing bricks only if a truthful, complete planner mapping already contains them. That is the exact upstream property the directed addition must establish. Naming a future planner without pinning its implementation, inputs, parent completeness, or output digest leaves the laziest compliant implementation free to omit the edge objects and reproduce the inherited defect.

**Minimal repair.** Pin a planner implementation and schema in BS-2m; pass the selected-parent keys/digest into one orchestrator; require one planner record per selected object; reject duplicate manifest entries; and bind parent digest, planner code hash/config, per-object required-brick payload, and closed-set digest in the receipt. Replay the two real edge objects through that pinned planner, not through a hand-authored miniature map.

### 4. BLOCKER — Stage C and BS-7f do not enforce sealed-mask provenance or correct calibration-bin assignment

**Quote / symbol.** V6 §3 says only the typed admissible mask reaches Stage C and the production record, and §4 specifically requires the sealed accepted-position mask (V6 lines 156–160, 180–184). `Mask` permits both `SEALED_ACCEPTED_MASK` and `FIXTURE`; `require_mask()` checks only class and sign presence, not kind (code lines 322–373). The class has no acceptance-flag field and validates only that bin labels are in 0..2, not that they equal `assign_bins(c, sealed_boundaries)`.

**Executed attack.** A `FIXTURE` mask with all bin labels set to zero, although derived bins were `[0,0,1,1,2,2]`, was accepted by both `stage_power(..., STAGE_C, ...)` and `perm_record(..., STAGE_REAL, ...)`. Stage C returned normally and the production permutation call returned p=0.75.

**Why it blocks.** A lazy caller can use parent positions, rejected objects, or deliberately wrong bins while still wrapping them in an allowed `Mask`. Wrong bins directly change the per-bin Stage-C injection, profile factor, covariance gradient, and verdict.

**Minimal repair.** Separate pre-bin positions, sealed accepted mask, fixture mask, and signed real record into non-interchangeable types/entry points. Include and validate the acceptance flag, boundaries digest, exact derived bin labels, parent/accepted-set digest, and operation-specific kind. Production Stage C and BS-7f must reject `FIXTURE` regardless of shape.

### 5. BLOCKER — the raw/retained exact-mode repair remains contradicted by the code, and BS-2s never performs its promised final power re-pass

**Quote / symbol.** V6 states raw counts drive the exact-mode boundary while retained counts drive thresholds (lines 98–101); `build_plan()` repeats that claim (code lines 478–482). But it passes retained counts to `local_pass()`, which computes the `<=16` boundary from positive retained entries (lines 185–199, 510). BS-2s also promises a Stage-P re-pass (V6 line 259), yet `build_plan()` calls `stage_power()` only on a ledger prefix at line 501, calls `local_pass()` at line 510, and returns the reduced set without another power call (lines 510–522).

**Executed attack.** With 17 raw-positive bricks and one raw count of 1, retention leaves 16 positive. Instrumenting the exact oracle showed `build_plan()` entered exact mode: `raw_positive=17`, `retained_positive=16`, `exact_called=True`. Static and executed call tracing found no `stage_power()` after `local_pass()`.

**Why it blocks.** This is the exact 17-raw/16-retained boundary seam requested by the V5 repair but absent from the fixtures. The final reduced geometry can differ from the passing prefix; reaching a leverage margin does not itself reproduce the stochastic 962/1000 receipt, especially under a different address and c distribution. BS-2s therefore cannot emit the content its slot promises.

**Minimal repair.** Make the raw-positive count an explicit boundary input or dispatch exact/local before passing retained counts. Add the 17/16 fixture. Define the final-set Stage-P address and rerun the full gate on the exact selected planning mask; failure must block BS-2m.

### 6. BLOCKER — production guards and the full-permutation decision path are optional helpers, not enforced gates

**Quote / symbol.** V6 says `require_environment()` is asserted, production decisions never use the analytic null, real data require a pinned authorization, the sample must be complete, and `decide()` is the only verdict producer (lines 28–29, 177–178, 188–208). In the code, `require_environment()` has zero call sites. `require_authorization()` and `require_complete_sample()` are called only by their fixtures. `decide(mask, cal, stage_c_passed, *, n_perm=N_PERM, _perm=None)` publicly accepts a replacement permutation triple and a mutable permutation count (code lines 684–720); it does not call any guard.

**Executed attack.** After monkeypatching the module's NumPy version to `0.0-attacker`, `require_environment()` refused, but `build_plan()` still completed. A 60-object mask with no authorization and no completeness receipt returned `REPRODUCED-LONGO` when `_perm=(beta, 0.0, 0.0001)` was supplied, even with `n_perm=0`. The analytic/fabricated record therefore can leak into a production verdict through the normative public function.

`decide()` also raises `InconclusiveByCalibration` instead of emitting/locking `INCONCLUSIVE-BY-CALIBRATION`, so BS-V cannot always contain one of the declared outcomes (code lines 689–716).

**Why it blocks.** Merely defining guards does not guard anything. The normative path can produce a real-looking verdict under the wrong environment, without authority, on an incomplete tiny sample, without Stage C evidence, and without the full 100,000-permutation record.

**Minimal repair.** Add one production runner that unconditionally calls environment, authorization, completeness, sealed-mask, Stage-C receipt, calibration-receipt, and fixed-`N_PERM` checks before a private/internal decision kernel. Remove `_perm` and count overrides from production; keep them only in a separately named fixture helper. Convert calibration halt into a receipted verdict and implement the BS-V primary lock atomically before disclosure.

### 7. BLOCKER — the equality fixture does not certify the discrete power gate, and its 5% tolerance can hide a gate-changing error

**Quote / symbol.** V6 claims exact permutation mean/variance and approximate normality, then uses one N=400, uniform-c, one-injected-sky, 20,000-permutation comparison with 5% critical-quantile tolerance as the equality contract (lines 170–178; code lines 890–901).

**Independent derivation.** For fixed labels permuted over centred c, `Var(beta) = Var_pop(s)/((N−1)Var_pop(c))`; the formula is correct. The approximation is the tail shape, not the variance.

**Why the contract fails.** Stage P decides 1,000 separate skies and passes only at x>=962. The fixture compares one critical quantile, on one toy geometry and one sign balance, and never compares analytic-versus-full-Monte-Carlo success counts or the PASS/FAIL result. A permitted +5% critical-value error changes z=3.0902 to 3.2447. For a nominal 0.962-power design, the corresponding normal power falls to 0.94737, below the 0.95 requirement; −5% gives 0.97313. Thus the stated tolerance is wider than the scientific gate it purports to protect. A stress probe also found that the approximation is not a general equality: an N=400 sparse-tail c distribution produced relative critical-quantile error 1.18, while the pinned uniform fixture remained at 0.0068. The sparse toy is not asserted to meet the production leverage floor; it demonstrates that the fixture does not establish a distribution-free equality.

**Minimal repair.** Validate on each actual Stage-P/Stage-C planning mask or prove a conservative finite-population tail bound under explicit leverage/max-weight conditions. Compare analytic and full-Monte-Carlo 1,000-trial success counts and final PASS/FAIL, with an error budget materially smaller than the distance to x=962. A one-sky 5% quantile check is not an equality contract.

### 8. BLOCKER — the Sep-5 release choice can be recorded, but branch invariance is not checkable

**Quote / symbol.** V6 §2.1 requires the same downstream code path under DR11 and DR10.1, differing only in input paths/versions, and calls branch-specific logic a defect (lines 58–75). BS-1 asks Duho for branch-invariance evidence but names no code symbol (line 254). The pinned reference contains no DR11, DR10, photo-z, branch, availability-probe, or release-dispatch implementation.

**Why it blocks.** A BS-1 prose assertion can be inserted on Sep 5 without reopening text, but there is no frozen configuration schema or paired execution whose equality a gate can inspect. "Corresponding DR10.1 products" and "publicly retrievable" do not define exact availability status/error rules. A lazy implementation may build two branch-specific query/join/cutout paths, then state they are the same code path.

**Minimal repair.** Pin one branch-neutral release configuration and dispatcher, exact product/schema fields for both branches, a deterministic availability probe with timestamp/error rules, and paired dry-run/fixture receipts proving that only configuration values differ. Bind its code and config hashes in BS-1/BS-1b.

### 9. BLOCKER — `validate_count_oracle()` accepts impossible counts and still cannot prove a dropped group was a true zero

**Quote / symbol.** V6 §2.3 says the count oracle is complete, zero rows are materialized, and one missing/extra brick or grouped/ungrouped disagreement refuses (lines 88–94). The validator blindly casts IDs/counts to int64, checks final table keys and two supplied totals, but never requires nonnegative integral counts or distinguishes raw grouped keys from materialized zero rows (code lines 245–268).

**Executed attack.** Counts `[-1,2]` were accepted with total 1. Floating counts `[1.9,0.1]` were silently cast to `[1,0]` and accepted. More fundamentally, if a nonzero grouped row is dropped and then materialized as zero, a grouped and ungrouped total produced under the same accidental footprint restriction can still agree; the final-table key equality is true by construction.

**Why it blocks.** Invalid or omitted counts can feed the ledger and selection while the claimed closure validator passes. This leaves the V5 count-oracle objection open beneath its named validator.

**Minimal repair.** Validate exact integer/nonnegative schemas before conversion. Preserve raw grouped keys separately from the universe-complete table. Require raw keys to be a unique subset, final keys to equal the universe, and an independently partitioned/accounted total whose scope cannot share the grouped query's accidental filter. Add a dropped-nonzero fixture, not just a missing final-row fixture.

### 10. BLOCKER — the lapsed-spec validation battery is not carried "verbatim in intent"

**Quote / symbol.** V6 says the validation battery is carried from the lapsed build spec (lines 200–208). That spec requires `A=+0.0408` to return REPRODUCED, a just-below-floor injection not to reproduce, and N=99,999 to return INCONCLUSIVE-BY-POWER (build spec lines 68–77).

**Code evidence.** `BATTERY-POS-RUNS` injects `A_LONGO/0.86`, not 0.0408; supplies an analytic `_perm` triple instead of running `perm_record()`; and its assertion accepts every numeric verdict — REPRODUCED, INCONCLUSIVE, or REJECTED (code lines 955–983). The floor-edge and N=99,999 cases are absent. The fixture would still print PASS if the positive target were rejected.

**Why it blocks.** The one success-path test that should detect attenuation, sign, p-tail, and band integration is vacuous, and two lapsed-spec boundary tests were dropped. This also masks Findings 1 and 6.

**Minimal repair.** Restore the exact +0.0408, below-floor, and N=99,999 tests; require the specified verdicts; and run the production permutation/guard path. Keep analytic-null tests separately labelled as power-only.

### 11. BLOCKER — the slot machine is not the producer/input/schema/code/failure table the brief requires

**Quote / symbol.** V6 §7 is titled "producer · inputs available at that time · schema · code symbol · blocks" (line 248), but its class-P columns contain only slot/producer/content/code symbol/blocks, and class E only slot/producer/content/blocks (lines 250–276). No slot has a canonical field schema/digest list or failure consequence. Class E omits code symbols entirely.

**Why it blocks.** `receipt()` is a generic byte-field envelope, not a slot-specific schema. BS-1/1b/3/9 have no code symbols; BS-4 points to abstract sign injection/decision rather than the mandatory pixel-level absolute-sign anchor; BS-2m omits the planner; BS-7p does not enforce the environment; BS-8p/8f bind the defective calibration functions; and BS-V names a "primary lock" for which no code exists. The §6 clean-room rule requires a published per-function normative specification, but no slot produces/pins that specification or records agreement across all functions. Authorization, complete-sample guard, final selected-set power re-pass, operation-specific mask validation, calibration-halt verdict, and primary-lock atomicity have no enforceable slot.

**Minimal repair.** Replace §7 with a machine-checkable register that explicitly lists available input artifact/digest, exact output schema and canonical serialization, normative code/spec hash, accountable producer, predecessor, block/failure outcome, and blind-double agreement for every P/E obligation. Add explicit slots for the language-neutral per-function spec, production runner guards, final Stage-P re-pass, and BS-V lock.

## Complete slot walk

### Class P

- **BS-1:** producer and chronology exist; exact branch inputs, availability probe, config schema, code symbol, and branch-invariance test do not. Blocked by Finding 8.
- **BS-1b:** photo-z path/column/join content is named and available after BS-1; no schema/digest or branch-neutral producer symbol.
- **BS-2c:** temporally pre-freeze and rowless in concept; validator exists, but query production, raw-group proof, integer schema, c-byte decoding/schema, and independent closure remain open (Finding 9).
- **BS-2o:** `greedy_ledger`/`ledger_digest` exist; downstream validity depends on BS-2c and no complete receipt schema is stated.
- **BS-5p:** `stage_power`/`build_plan` exist and use retained planning objects; the analytic equality contract is insufficient and environment/production parameters are not enforced (Findings 6–7).
- **BS-2s:** selection symbols exist; raw-positive boundary is wrong and promised final Stage-P re-pass is absent (Finding 5).
- **BS-2m:** comparison functions exist; frozen planner/parent completeness does not (Finding 3).
- **BS-3:** inherited identity/weights/tau are available pre-image; no exact successor receipt schema or code binding appears in §7.
- **BS-9:** correctly carries branch-specific HDU/plane/input function, full R1–R5 rerun, replacement runner, and the prohibition on `nm_acquire_cutouts.py`; this attack held. It still lacks code symbol/schema/digest/failure consequence in the table.
- **BS-4:** correctly pre-image in chronology, but `inject_signs`/`decide` cannot execute the required pixel-level known-winding anchor.
- **BS-7p:** fixtures/address declaration exist; no enforced environment call or slot-specific battery schema, and the positive battery is vacuous.
- **BS-8p:** pre-measurement timing is acyclic; inherited totals/floors, capacity-safe allocation, and clean HC-1H estimator are not frozen correctly (Findings 1–2).

### Class E

- **BS-6:** chronology before first image byte is coherent; exact transport receipt schema/code symbol are absent from §7.
- **BS-2f:** positions/flags can exist before unblinding, but the type has no acceptance flag and does not bind derived bins/boundaries or sealed provenance (Finding 4).
- **BS-8f:** fields are named, but its producer is mathematically not HC-1H (Finding 1).
- **BS-5f:** chronology is correct; Stage C accepts fixture/wrong-bin masks and a Boolean can substitute for its receipt (Findings 4 and 6).
- **BS-7f:** `perm_record` exists, but production provenance, fixed count, guards, and an unbypassable connection to `decide` do not.
- **BS-V:** `decide` exists, but calibration halt is an exception, `_perm` bypasses BS-7f, and no primary-lock implementation/schema exists.

No class-P slot inherently requires post-freeze real chi. The old temporal cycle is closed; the blockers are executable custody, schema, and producer gaps.

## Inherited-defect closure (§8)

1. **Manifest-versus-parent gap — OPEN.** The supplied-map comparison catches the named miniature map, but parent/planner completeness is unbound (Finding 3).
2. **Footprint-blind power — OPEN.** Stage C accepts `FIXTURE` and arbitrary bin labels; sealed accepted provenance is not enforced (Finding 4).
3. **Full-sky normalization constant — CLOSED for the named defect.** `beta_slope()` is centred; no `3*D` estimator exists.
4. **Attenuation-versus-target mismatch — OPEN.** The beta/A split exists, but the normative attenuation producer is the wrong HC-1H estimator (Finding 1).
5. **Unreachable significance threshold — OPEN at the production seam.** The constant is 100,000 and fixture resolution exists, but `decide()` permits `_perm` and mutable `n_perm` without guards (Finding 6).
6. **Silent axis divergence — CLOSED for the reference.** One pinned ICRS vector is used and independently reproduces the Galactic-axis transform.
7. **Count stopping on ordered brick IDs — CLOSED for the named contiguous-range defect.** Selection is leverage-based and contiguous BRICKID selection is not present. Finding 5 is a separate raw/retained dispatch defect.
8. **Verdict by human reading — PARTLY CLOSED, still blocked.** `decide()` exists, but it is bypassable, does not emit calibration halt, and has no primary lock (Findings 6 and 11).

## Quotation/source fidelity and attacks that held

1. The DOI landing page and arXiv:1104.2815 independently confirm the title, author, 15,158 objects, published amplitude `−0.0408±0.011`, and Galactic axis approximately `(52°,68.5°)`. The DOI is `10.1016/j.physletb.2011.04.008`; the ADS record/search identifies bibcode `2011PhLB..699..224L`.
2. The sign mapping is internally consistent: Longo uses `(R−L)/(R+L)` and reports negative; `LANA_BS5_LONGO_SIGN_20260814.md` lines 48–75 defines our `(L−R)`/East-of-North polarity as positive. V6 and code consistently record published `−0.0408` and our `+0.0408`. Independent source verification supports Longo's sign; the convention flip is a declared project definition anchored by BS-4, not a claim that Longo published positive.
3. Independent Galactic-to-ICRS rotation gave `[-0.6769717712430396,-0.5098465517524211,0.5308160835723453]`, maximum component difference `3.50e-11` from `AXIS`; norm is 1 within floating precision and display coordinates are RA 216.9844355°, Dec 32.0606109°.
4. All eight §2.2 cut predicates occur in V6 and BS6-pred with matching operator/numeric content; the ellipticity predicate is byte-identical. The absence of a surface-brightness cut is preserved.
5. V3-pred's 100,000 permutations, strict p thresholds, 3.09 floor multiplier, 0.85 lower-bound floor, tau, and 85.72% retention are preserved in substance.
6. Independent Clopper–Pearson calculation gives one-sided 95% lower bounds 0.9493659932 at x=961 and 0.9504871297 at x=962; `CP_PASS_X=962` is correct.
7. The exact permutation-variance formula is correct and the exhaustive four-label fixture agrees.
8. AST/source checks found zero matrix-multiply operators, zero `.spawn()` calls, zero `binomial()` calls, and exactly two `rng.random()` calls inside the per-object injection loop. The no-BLAS, banned-spawn, and two-draw body claims held.
9. All five historic selector counterexamples pass exact mode, and the pinned fixture transcript is exact.
10. BS-9 preserves the successor input-path rebinding, full R1–R5 rerun requirement, replacement-runner gate, and prohibition on `nm_acquire_cutouts.py` rather than laundering predecessor receipts.
11. The draft repeatedly says drafting only and does not purport to authorize a run or fetch. No authorization file was created or assumed by this review.

## Testimony

- V6 explicitly labels `Cov(beta_hat, a_hat)=0` / profile analogue as Testimony. I did not treat it as proved or use it to rescue any finding.
- The DR11-page/photo-z status at drafting is an author measurement, not independently re-fetched here; it is not a verdict basis.
- The historical 60,308/60,310 particulars are consistent between V6 and `trio-overnight-20260825/TRIO_OVERNIGHT_REPORT_20260825.md` lines 108–118. That report is still an author record; I did not inspect `/Users/duhokim/NebulaMindData/` or claim independent raw-data reproduction. Finding 3 does not depend on those historical numbers: the lazy one-object pass is executable against the pinned code.
- The code/prose assertion that a finite-population CLT is adequate at the production 0.001 tail is not accepted as testimony sufficient for the power gate; Finding 7 states the missing check.

## Evidence ledger and custody boundary

Read: the V6 brief; the three pinned V6 artifacts; both V5 gate reports; amended successor scope; V3-pred; BS6-pred; lapsed verdict build spec; the cited Longo sign receipt; and the cited Trio report section. External source checks used the DOI landing page, arXiv:1104.2815, and the ADS record/search result. Executed: all hashes; exact fixture reproduction; environment inventory; symbol/call inventory; raw/retained boundary instrumentation; lazy-manifest and duplicate-manifest attacks; negative/fractional count attacks; fixture-kind/wrong-bin Stage-C and BS-7f calls; HC-1H numeric comparison; feasible-allocation refusal; boundary-tie check; wrong-environment call; fabricated `_perm` verdict; calibration-halt call; exact variance derivation checks; analytic-tail stress probes; Clopper–Pearson scan; axis conversion; cut-string checks; and AST checks for BLAS/spawn/binomial/random-call claims.

No `/Users/duhokim/NebulaMindData/` path was read. No source artifact was edited. No run, study-data fetch, authorization, git mutation, publication, freeze, or execution approval occurred. The only gate-directory write made by this CODEX review is this report; a separately produced `GATE_GPT56_SUCCESSOR_V6.md` appeared concurrently after the clean pre-write status and was not read or used.

**REFUSED** — blockers: HC-1H accuracy/covariance and allocation are not implemented; manifest closure trusts an incomplete caller map; Stage C and BS-7f accept non-production masks/bins; the raw/retained dispatch and final power re-pass are wrong/missing; guards and full-permutation decisions are bypassable; the 5% one-sky equality fixture cannot protect x>=962; branch invariance is uncheckable; the count oracle accepts invalid/incompletely accounted counts; the lapsed validation battery is weakened; and the slot/lock/spec machine is incomplete.

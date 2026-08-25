# CODEX referee report — successor preregistration V10 (round 9)

## Recommendation

**REVISE.** The dispatch digests match; the 36-check fixture transcript reproduces byte-for-byte; `close_manifest()` now really calls the frozen planner and, when given a hand-built receipt-shaped dict, accepts the complete historical manifest and refuses either missing neighbour by name; the repaired fast reducer matches the prior 400-case regime and the real 6,445-brick artifact; the exact permutation-variance identity and 962/1000 Clopper–Pearson threshold independently reproduce.

Those positives do not make V10 ready to freeze. Eight stated end-to-end guarantees fail, including three of the four repairs V10 §10 describes as closed.

## Dispatch digests — computed before review

Command:

`shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V10_20260825.md ../ref/successor_ref_v4.py ../ref/FIXTURES_V4_20260825.out`

- `../PREREG_SUCCESSOR_DRAFT_V10_20260825.md` = `cca636b9444c4f5a1df47aaddf419443caa27350adfbdbfd5c3ba31065ea39c7`
- `../ref/successor_ref_v4.py` = `0b312c96db0b4551bcafd554b4bdd7124d3104cef4cc7f405eea3f849e08e21c`
- `../ref/FIXTURES_V4_20260825.out` = `6b14d8a69b606cbf5ddb6d0e82f856a08d6a5928227c3cba4956a1c02636e436`

All three equal the brief. Review proceeded.

## Environment and mandatory reference execution

Executed:

`PYTHONDONTWRITEBYTECODE=1 python3 ../ref/successor_ref_v4.py --fixtures > /tmp/CODEX_SUCCESSOR_V10_FIXTURES.out`

Then byte-compared with the pin using `cmp -s` and independently hashed both outputs.

- executable: `/Library/Developer/CommandLineTools/usr/bin/python3`
- Python: `3.9.6` (Clang `21.0.0`)
- NumPy: `1.26.4`
- platform: `macOS-26.6.2-arm64-arm-64bit`
- machine: `arm64`
- byte order: `little`
- exit: `0`
- stdout: `4,317` bytes
- stderr: `0` bytes
- stdout SHA-256: `6b14d8a69b606cbf5ddb6d0e82f856a08d6a5928227c3cba4956a1c02636e436`
- `cmp`: exit `0`, byte-identical
- parsed named checks: `36`, all PASS
- final transcript line: `ALL FIXTURES PASS`

The fixture run is real positive evidence, but several new checks inspect source text or isolated helpers rather than execute the claimed production chain.

## Numbered findings

### 1. BLOCKER — canonical receipts cannot be consumed by the routines that require them, while unverified receipt-shaped dicts can be accepted

**Quoted guarantee / symbols.** V10 says receipts have enforced schemas and are consumable end to end; BS-2m consumes the BS-2s selection receipt (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:117-134,342-370`). `receipt()` is the canonical producer (`successor_ref_v4.py:138-177`), while `close_manifest()` consumes BS-2s (`261-333`) and `run_production_verdict()` consumes BS-5f (`1092-1126`).

**Direct production-path execution.** I loaded the real 366,912-brick geometry sidecar through the frozen planner and called `close_manifest()` on the two historical objects. With a hand-built `{'slot':'BS-2s','parent_digest':...}` dict:

- complete five-brick manifest: PASS;
- omit `3471m885`: refused, naming `['3471m885']`;
- omit `2857m870`: refused, naming `['2857m870']`.

This confirms the planner wiring itself is repaired.

The receipt round trip fails. The canonical call `receipt('BS-2s', fields)` returned only:

`['body_sha256', 'envelope_sha256', 'environment', 'schema', 'slot']`

It returned no `parent_digest`, so `close_manifest()` refused it. Adding `parent_digest` to the canonical BS-2s field set also failed because `SLOT_SCHEMA['BS-2s']` does not name that field:

`RuntimeError: receipt BS-2s: field set mismatch; missing [], extra ['parent_digest']`

The same defect occurs at Stage C. A canonical BS-5f receipt has no top-level `mask_digest` or `passed`, so `run_production_verdict()` refused it with:

`RuntimeError: Stage-C receipt does not bind THIS mask — FAIL`

Conversely, the runner does not recompute an envelope hash or decode a canonical body. A bare dict with `schema='successor_ref_v3/1'`, a truthy but invalid `envelope_sha256='not-a-digest-but-truthy'`, `passed=True`, and the current mask digest reached a sentinel installed at `perm_record()`:

`RuntimeError production permutation record failed: REACHED_PERM_AFTER_RECEIPT_ACCEPTED`

That means the fabricated envelope passed every Stage-C receipt check.

**Why the guarantee fails.** The canonical producer discards the payload values that consumers read, and consumers trust unverified top-level values that the canonical producer does not emit. Thus no genuine BS-2s receipt can drive manifest closure and no genuine BS-5f receipt can drive the verdict, while receipt-shaped dicts can assert custody and PASS without a verified envelope.

**Smallest sufficient repair.** Define a typed receipt object that retains or canonically decodes the named payload, validates each field's type, recomputes `body_sha256` and `envelope_sha256`, and is the only accepted consumer input. Add `parent_digest` to the canonical BS-2s schema. Make `close_manifest()` and `run_production_verdict()` accept only validated receipts, then add producer→serialize→parse→consumer fixtures for BS-2s→BS-2m, BS-8f/BS-5f→verdict, and BS-7f→BS-V. Negative fixtures must reject altered payloads and arbitrary truthy hashes.

### 2. BLOCKER — the Stage-C pre-unblinding mask digest cannot match the signed mask digest required by the production verdict

**Quoted guarantee / symbols.** Stage C runs on the sealed accepted-position mask “never a χ sign” before unblinding, and BS-5f binds that exact mask digest (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:258-262,366-370`). The production runner then requires signs and requires the Stage-C receipt's `mask_digest` to equal the supplied mask's digest (`successor_ref_v4.py:1097-1106`).

**Direct execution.** `_BaseMask.digest` binds `signs_present` and the sign payload itself (`successor_ref_v4.py:557-564`). For identical sealed positions and boundaries, adding signs changed the digest:

- unsigned Stage-C mask: `0789ca2f9884176ffab635ae2c9aa1816b2dea135d9128612871bd970bd5554e`
- signed verdict mask: `75b139edc34fdbfdd486fff7f062eb520a046f69a5476d527d28a3358a615db6`
- equality: `False`

**Why the guarantee fails.** A correctly timed Stage-C receipt binds the unsigned mask. The runner refuses that receipt after signs are attached. Binding BS-5f to the later signed digest would require knowing real signs before the pre-unblinding power gate, reversing the promised chronology. Every named check can therefore be individually satisfied, but not by one end-to-end object chain.

**Smallest sufficient repair.** Define and receipt a stable `position_mask_digest` over brickid, objid, positions, acceptance flags, calibration boundaries and derived bins, explicitly excluding signs. Use that same digest in BS-2f, BS-5f and the production runner. Bind the later sign-bearing payload separately in BS-7f. Add an end-to-end fixture: unsigned mask → Stage C receipt → attach signs without changing `position_mask_digest` → production consumer accepts; any position/acceptance/bin change refuses.

### 3. BLOCKER — Stage P's sampled audit still counts unsafe unsampled successes and does not establish one-null conservatism for all 1,000 trials

**Quoted guarantee / symbols.** V10 §10 says the round-8 Stage-P defect is repaired because a deterministic sample of non-boundary successes is confirmed and the shared null is measured against trials' own nulls (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:243-256,421`). The operative code confirms all boundary successes, but only `max(5, 5%)` of far successes, and compares own-null critical values for at most the first eight audited successes (`successor_ref_v4.py:719-778`). Confirmation still uses `confirm_perm=20,000`, not production's 100,000.

**Executed control-flow attack.** I isolated the audit branch with synthetic monkeypatches: all 1,000 calibrated trials were far successes at `p_calibrated=0.00005`; the deterministic sampler selected 50; one unsampled trial was defined to have independent full p = 0.5 if called. The result was:

- unsafe trial: `1`;
- sampled: `False`;
- full p if called: `0.5`;
- Stage-P result: `successes=1000`, `passed=True`;
- audited/confirmed/refuted: `50 / 50 / 0`;
- unsafe trial called: `False`.

The own-null check has the same logical gap: it measures at most eight audited sign multisets, not all admissible trial sign multisets. A sample showing no violation is evidence about that sample, not a bound over 1,000 changing sign multisets.

**Why the guarantee fails.** The widened audit estimates a failure rate; it does not deliver the claimed implication “calibrated success ⇒ full-MC success” for every counted success. An unsafe unsampled success can contribute to the 962 threshold while all named audit checks report success. Measuring eight own nulls cannot call the reference null conservative for all 1,000.

**Smallest sufficient repair.** Confirm every counted success using the same 100,000-permutation contract as the scientific decision, or derive and implement a finite-sample simultaneous bound covering reference-null estimation and every admissible sign multiset. If sampling remains, it may support an explicitly probabilistic audit statement but cannot support a universal equality/conservatism contract or count unaudited trials as certified successes.

### 4. BLOCKER — the count-oracle completeness repair remains optional on the production entry path and the real producer still compares one total with itself

**Quoted guarantee / symbols.** V10 says `build_plan()` refuses omitted proof inputs and that the real oracle validates against an independent witness (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:89-97,421-422`).

**Direct production-entry attack.** The V4 validator still wraps every closure check in `if ... is not None` (`successor_ref_v4.py:348-395`). The call

`validate_count_table([1,2],[-0.5,0.5],[3,4], None, None, None)`

returned:

`{'rows': 2, 'zero_rows': 0}`

To check `build_plan()` rather than only its helper, I replaced `greedy_ledger()` with a sentinel and called the production entry point with all three proof values explicitly `None`. It reached the sentinel after validation:

`RuntimeError REACHED_LEDGER_AFTER_VALIDATION`

Thus the production entry point did not refuse the omitted proof.

**Real-producer trace.** `real/build_real_oracle.py` still imports `successor_ref_v3`, not V4 (`build_real_oracle.py:15-16`), and still passes the same array-derived number as both witnesses (`69-72`):

- `grouped_sum=int(n_elig.sum())`
- `ungrouped_total=int(n_elig.sum())`

The V4 constant `PINNED_COUNT_TOTAL=832393` is an integer in source, not a separately consumed ungrouped Cut-6 query/result receipt. No current real producer reads such an independent witness.

**Why the guarantee fails.** A caller can omit every completeness input and continue into the ledger. The actual real producer executes the superseded validator and proves one value equals itself. A scope omission shared by the grouped counts remains undetectable.

**Smallest sufficient repair.** Reject `None` explicitly at the first lines of `build_plan()` and `validate_count_table()` on the production path. Produce and pin a genuinely independent ungrouped Cut-6 query and raw result with the identical frozen predicate and independently specified scope; pass its typed, hash-verified receipt rather than a caller integer. Update `build_real_oracle.py` to import V4 and consume that artifact. Add all-`None`, one-missing, stale-total, scope-mismatch and real-producer end-to-end fixtures.

### 5. BLOCKER — the repaired fast reducer is not exactly equivalent to frozen `local_pass()` at a near-crossing target outside the 400-case regime

**Quoted guarantee / symbols.** V10 says `_swap_then_remove` matches frozen `local_pass()` on 400 cases with zero mismatches and presents the equivalence defect as repaired (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:171-183,419-420`). The reference uses centred `sse()` reductions (`successor_ref_v4.py:337-345,452-505`); the fast path uses raw moments `S2-S1²/N` (`real/reduce_fast.py:17-107`).

**Positive attacks.** I reproduced 400/400 matches in the prior seed/regime and found zero mismatches in another 2,500 random cases with 31–100 bricks, tie-dense `c`, counts 1–4,999 and targets from 5%–99.5% of full retained SSE. The actual corrected artifacts also match byte-for-byte:

- `real_selection_reduced.npz` SHA-256 = `b913939d54b66bda5a4ef05ee46d0b1321a6b490d1d232ba197c9aa0c9a3804e`
- `real_selection_swapped.npz` SHA-256 = the same;
- 6,445 bricks, `L=40000.959939179214`, removed `[155487]`.

**Counterexample outside the regime.** Deterministic generator: seed `73199261`, trial 0, 59 bricks, `c` sampled from `{-1,-.75,-.5,-.25,0,.25,.5,.75,1}`, counts 1–1,000, and target set exactly to the frozen stable SSE of greedy prefix 55. Results:

- target / stable prefix L: `11117.761298179874`;
- fast raw-moment prefix L: `11117.761298179872` (one representable step lower at this scale);
- frozen `local_pass()`: 55 bricks;
- fast reducer: 56 bricks, with extra brick `10046`;
- one `nextafter` above the target: both choose 56; one `nextafter` below: both choose 55.

**Why the guarantee fails.** Exact code-defined threshold comparisons make a one-ULP arithmetic divergence an algorithmic divergence. Near a crossing, the fast implementation follows a different prefix and returns a different selected set. The real artifact happens not to sit on this boundary, so its 6,445 count survives; the general equivalence claim does not.

**Smallest sufficient repair.** Make the scalable implementation use a numerically specified accumulator and comparison rule shared byte-for-byte with the normative implementation, or replace both with an explicitly error-bounded representation whose threshold policy is frozen. Add this seed/target and `nextafter` probes to pinned fixtures. Re-run the real artifact after the normative arithmetic is fixed.

### 6. BLOCKER — `allocate_handcheck()` can silently shrink a non-empty joint cell below the frozen floor instead of failing

**Quoted guarantee / symbol.** V10 promises at least 10 labels per non-empty 3×9 joint cell and fail-closed infeasibility (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:305-318`). `allocate_handcheck()` claims the same (`successor_ref_v4.py:879-944`).

**Executed attack.** A deterministic stress probe (`np.random.default_rng(77119)`, first 3×9 count matrix, entries 0–499) contained one non-empty cell with population 5. The function returned a 500-label allocation instead of refusing. For that cell:

- population count: `5`;
- allocated labels: `5`;
- required non-empty-cell floor: `10`.

The returned allocation had total 500, respected capacities and met each stratum's 30-label floor, so those later checks all passed while the joint-cell floor failed.

**Code cause.** The function initializes every non-empty cell at 10, but does not first reject a cell with `0 < count < 10`. It then computes negative `headroom = cc - alloc` and `base = minimum(floor(share), headroom)` (`successor_ref_v4.py:905-917`), which subtracts labels from the floor. The final capacity check sees 5 ≤ 5 and does not detect the floor loss.

**Why the guarantee fails.** An infeasible hand-check table can be returned as a nominally valid allocation with every named postcondition except the promised per-cell floor. The fixture uses a 12-object sparse cell and misses the 1–9 regime.

**Smallest sufficient repair.** Before allocation, reject every cell with `0 < count < HC_MIN_PER_CELL`; assert `headroom >= 0` before apportionment; and assert the per-cell floor again on the final allocation. Add fixtures for populations 1, 9, 10 and mixed sparse cells.

### 7. BLOCKER — the hand-check accuracy estimator cannot implement the inherited population-weighted HC-1H estimand

**Quoted guarantee / symbol.** V3-pred defines `a = Σ_s w_s a_s` using population weights over the inherited HC strata (`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md:279-318`). V10 says this inherited estimator is implemented by `accuracy_from_handcheck()` after a 3×9 allocation (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:305-320`).

**Code trace and direct counterexample.** `accuracy_from_handcheck(agree_counts, n_counts, epsilon_hat, sigma_epsilon)` has no population counts or population-weight argument (`successor_ref_v4.py:947-990`). It computes:

`raw_hat = sum(agree) / sum(n)`

and therefore weights by allocated sample size, not inherited-stratum population.

With agreement counts `[90,50,50]`, sample counts `[100,100,100]` and ε=0, the implementation returned `a_hat=0.6333333333333333`. The same hand-check outcomes imply different inherited estimands for different frozen populations:

- population weights `[0.90,0.05,0.05]` → `a=0.86`;
- population weights `[0.05,0.475,0.475]` → `a=0.52`.

The function returns 0.6333 for both because it has no way to distinguish them. The 3×9 allocation makes unequal inclusion probabilities expected, so pooling by audited sample size is not a substitute for population weighting.

**Why the guarantee fails.** The computed attenuation, lower bound, scalar/profile adjudication, Stage-C power and final amplitude can all use the wrong estimand while the current function reports success. Shared-ε covariance propagation does not repair the missing survey weights.

**Smallest sufficient repair.** Require the frozen 3×9 population table and corresponding per-cell agreement/sample counts. Compute corrected per-cell or inherited-stratum estimates, aggregate with the frozen population weights (and the declared calibration-bin conditioning), and propagate binomial plus shared-ε covariance through those weights. Refuse missing populations or inconsistent allocations. Add two-population/same-handcheck fixtures like the counterexample above.

### 8. MAJOR — the release resolver accepts a late fallback and impossible calendar dates, contrary to the frozen choice-point

**Quoted guarantee / symbol.** The choice-point closes on the earlier of confirmed DR11 photo-z availability or exactly 2026-09-05; waiting longer requires amendment (`PREREG_SUCCESSOR_DRAFT_V10_20260825.md:59-75`). `resolve_branch()` is the code definition (`successor_ref_v4.py:1166-1190`).

**Direct execution.** The resolver accepted all three:

- `resolve_branch(False, '2026-09-06')` → `B_DR10_1`;
- `resolve_branch(False, '2026-09-99')` → `B_DR10_1`;
- `resolve_branch(True, '2026-02-30')` → `A_DR11`.

It checks only string length and hyphen positions, then compares strings. It rejects early Branch B and late Branch A, but does not require absent-photo-z resolution exactly on the fallback date and does not parse a real calendar date.

**Why the guarantee fails.** The code permits the operator to wait past the frozen deadline without amendment and can receipt a nonexistent date. `BRANCH-DATE-RULE` tests “5 Sept” but not calendar-invalid ISO-looking dates or late Branch B.

**Smallest sufficient repair.** Parse with a strict calendar-date parser; require `photoz_available=False` only on `2026-09-05`; require an available-product branch no later than that date; and bind the dated availability-probe receipt rather than a bare boolean. Add the three direct probes above as negative fixtures.

## Statistical, fidelity and production-path checks that held

1. The fixture transcript reproduced byte-for-byte under the frozen environment.
2. The production closure entry point now invokes `frozen_plan_object()`. On the real sidecar it returned `['3385m885','3471m885']` and `['2857m870','2894m872','2902m870']`; the complete two-object manifest passed and omission of either historical neighbour was refused by name. Findings 1–2 concern receipt and chronology wiring, not planner geometry.
3. The repaired real 6,445-brick artifact is byte-identical to the recorded reduction artifact and has the reported `L_ret`. Finding 5 concerns exact equivalence outside the tested regime, not this artifact's reproduced bytes.
4. The exact permutation-variance identity held over all 25 exhaustive `(N, sign-balance)` cases for `N=4..8`; maximum standard-deviation error was `1.1102230246251565e-16`.
5. Independent one-sided Clopper–Pearson lower bounds were `0.9493659932051121` for 961/1000 and `0.950487129744074` for 962/1000. The frozen 962 threshold is correct.
6. Calibration adjudication precedes the real permutation statistic in the runner. With a failing calibration and a tracked permutation function, the runner raised `InconclusiveByCalibration` and made zero permutation calls.
7. Sealed/fixture types and sign-vector length checks passed the pinned refusal battery. Finding 2 is the later unsigned/signed custody transition.
8. All eight §2.2 predicate strings occur in both V10 and BS6-pred, including byte-identical executable ellipticity text `POWER(shape_e1,2)+POWER(shape_e2,2) < 0.1836734693877551`. The no-surface-brightness-cut disclosure is preserved.
9. The predecessor's one-sided 100,000-permutation rule and our-convention +0.0408 target are preserved in V10/code. No new quotation-fidelity defect was found.
10. V10 explicitly says the reported 997/1000 Stage-P result belongs to the pre-reduction geometry and is not a re-run on the final 6,445 set. I did not treat it as a final-set measurement. That missing class-P execution remains disclosed, not silently converted into evidence.
11. The preamble correctly limits authority to drafting and separately discloses the already-completed catalog-only geometry/count step. I found no text authorizing image access, χ access, a real statistic, freeze or publication.

## Scope exclusions honored

I did not re-report the four V10 §10 disclosed-not-closed items: the clean-room normative specification, BS-9 input schema, BS-V primary lock, and production scaling of the normative O(n²) selector. Finding 5 is not the disclosed scaling limitation; it is a direct counterexample to the new exact-equivalence repair. Findings 1–4 and 6–8 concern guarantees V10 presents as operative or repaired and dimensions the review brief explicitly required end to end.

## Testimony

- V10's declared `Cov(β̂, â)=0` and profile analogue remain testimony. I did not use either to rescue a finding.
- I did not perform a live DR11 availability probe or independently re-fetch Longo's paper. Neither is a premise of the recommendation.

## Custody boundary

I read the brief-mandated draft, reference code/transcript, both round-8 reports, real receipt and every script in `../real/`, amended scope, predecessor, photometric-cuts receipt and lapsed build spec. I did not read `/Users/duhokim/NebulaMindData/`. Executions used the pinned fixture path, synthetic arrays, the already-acquired in-lane geometry sidecar, and already-produced in-lane NPZ artifacts. I made no network request, data fetch, image access, χ access, study run, authorization, freeze, publication, git mutation or source-artifact edit. The only persistent review write is this report.

Blocking findings: F1 receipt producer/consumer incompatibility and forgery acceptance; F2 Stage-C unsigned/signed mask-digest chronology; F3 sampled Stage-P audit leaves unsafe successes unbounded; F4 count-oracle proof remains optional and self-referential in the real producer; F5 fast reduction is not exactly equivalent near a crossing; F6 hand-check cell floors can silently shrink; F7 HC-1H population weighting is absent. F8 also requires revision of the release date rule.

**REVISE**

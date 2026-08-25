# GPT56 ADVERSARIAL GATE — successor preregistration V6

## Verdict

**REFUSED.** The pinned fixture output reproduces byte-for-byte, the external citation/sign anchors hold, the exact permutation mean/variance formula holds, and several V5 repairs are real. V6 is still not freeze-candidate grade. The named manifest defect can pass through the new closure check under the laziest compliant planner/map; the branch choice is not machine-bound or branch-invariance-checkable; the calibration producer is not the quoted HC-1H estimator; typed-mask provenance, production guards, and analytic-null isolation are bypassable; the raw/retained selection seam remains; the 5% power-equality tolerance is not a power-equality contract; and the slot register still lacks the schemas, symbols, and primary lock its heading promises.

## Custody pins — computed before review

The first content-review prerequisite was:

`shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V6_20260825.md ../ref/successor_ref_v2.py ../ref/FIXTURES_V2_20260825.out`

Computed:

- `9f40dfb0c1f2d56b67c85507d6b17fee6e926d881faadefe07a4af7f2bf94190  ../PREREG_SUCCESSOR_DRAFT_V6_20260825.md`
- `dda4436cf0b10710ad9f8a6bb3dff6581c293df31ca8d577b4a2423d33d2dcfd  ../ref/successor_ref_v2.py`
- `4ceb6f94dbebffebdabc18738e156bf4f5db058c3b3c4290df8afc648437e74b  ../ref/FIXTURES_V2_20260825.out`

All three equal the brief's required pins. Review proceeded on those bytes.

Independent source pins recomputed:

- amended scope: `995b2e729a3362f0445cac9d5da6d290fddac9f8018e75f2c0aa87c190c93de7`
- V3-pred: `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- BS6-pred: `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`
- lapsed build spec: `43b9a6a843ef08a6528f1132db2bee29000c5ecd3def2a3a03c23f672c81cec7`
- signed decline memo: `b4a1f1fcaa9acbaa6b9efd3ebbe9496be8c1d83c690a012dc7a4f8520840374f` (matches V6)

## Environment and fixture reproduction

- command: `python3 ../ref/successor_ref_v2.py --fixtures`
- executable: `/Library/Developer/CommandLineTools/usr/bin/python3`
- Python: `3.9.6`, Clang 21.0.0 build
- NumPy: `1.26.4`
- OS/platform: `macOS-26.6.2-arm64-arm-64bit`
- machine: `arm64`
- byte order: little-endian
- exit: 0
- stderr: 0 bytes
- stdout: 2,616 bytes
- stdout SHA-256: `4ceb6f94dbebffebdabc18738e156bf4f5db058c3b3c4290df8afc648437e74b`
- byte comparison to the pinned fixture file: exact

## Numbered findings

### 1. BLOCKER — BS-2m compares a manifest to a caller-supplied answer, not to the frozen parent and cutout planner

**Quote / symbol.** V6 §2.4 says the parent's cutout geometry defines the required set, including footprint-edge neighbours, and that `manifest_closure()` computes it “via the frozen cutout planner” (V6 lines 109–122). The code explicitly says the planner is “named in the constitution, not reimplemented here”; `manifest_closure(object_required_bricks)` merely unions the lists supplied by its caller (`successor_ref_v2.py:271-294`). It takes neither the frozen parent object IDs/digest nor the planner code/hash/configuration. `require_manifest_closure()` then compares the candidate manifest to that supplied union (`297-312`).

**Executed attacks.** With a two-object parent whose edge object requires `home + neighbor`, both lazy inputs passed:

- omit the edge object entirely; a one-brick manifest was accepted with `manifest_count=required_count=1`;
- include the edge object but let the purported planner report only `home`; a two-brick short manifest was accepted with no missing/extra brick.

The full map required three bricks. The function has no argument by which it could know either lazy map was incomplete. The pinned `CLOSURE-CATCHES` fixture hard-codes the two desired neighbour names into `req_map` (`1014-1035`); it proves the set comparison catches names already supplied to it, not that the production planner discovers those names or covers every parent object.

**Why it blocks.** This is the exact laziest-compliant path the directed addition had to close. A future BS-2m producer can use a home-brick-only or object-short “frozen planner” output, run both named functions, and ship a short manifest with a clean receipt. The named 60,308-vs-60,310 class is therefore not prevented by the property plus check.

**Minimal repair.** Pin and implement the cutout planner as code, including the footprint-edge neighbour rule and all geometry/configuration bytes. Make a single production entry point consume the frozen parent key/digest directly, require exact parent-key equality/cardinality, derive every object's required bricks itself, and bind parent digest + planner digest + per-object plan digest + closed manifest in BS-2m. Add negative fixtures for an omitted parent object and a planner that returns only the object's home brick.

### 2. BLOCKER — the Sep-5 branch choice is prose evidence, not a bound or checkable choice-point

**Quote / symbol.** V6 §2.1 selects DR11 iff its photo-z product “exists and is publicly retrievable at the resolution moment,” otherwise “the corresponding DR10.1 products,” and requires every downstream artifact to use the same code path (`V6:58-75`). BS-1 and BS-1b have code symbol `—` and no schema/digest (`254-256`). The reference code contains no DR11, DR10.1, branch, photo-z, resolver, or release-configuration literal.

**Why it blocks.** “Confirmed available,” “publicly retrievable,” “resolution moment,” and “corresponding DR10.1 products” do not uniquely determine a machine action or receipt. No pinned resolver says which endpoint/object constitutes existence, what HTTP/service result counts as retrievable, how transient failure is treated, or which exact DR10.1 paths/version fill Branch B. Branch-invariance is requested as “evidence,” but there is no common configuration schema, algorithm digest, dual-branch dry fixture, or comparator. A lazy receipt can assert invariance without showing it. The Sep-5 decision can therefore change queries, manifests, input runners, or schemas while still being described as configuration.

**Minimal repair.** Add a pinned branch resolver and a complete A/B configuration schema with exact product identifiers/endpoints, columns, join keys, image-tree/HDU contracts, timeout/retry/fail-closed semantics, and an immutable resolution timestamp source. Require a pre-freeze dual-branch fixture that emits identical downstream schema/code/algorithm digests with differences restricted to an enumerated configuration field set. BS-1 must carry the resolver output and raw availability evidence; BS-1b must be generated from the selected config, not free prose.

### 3. BLOCKER — Stage C and production decisions accept `FIXTURE` masks, arbitrary bin labels, and a provenance-colliding digest

**Quote / symbol.** V6 §3 says Stage C and production accept only a typed mask built from the sealed accepted-position mask, validating field lengths and binding a digest plus provenance kind (`156-160`). `Mask` allows both `SEALED_ACCEPTED_MASK` and `FIXTURE` (`successor_ref_v2.py:329-331`), while `require_mask()` checks only `isinstance` and optional signs (`367-373`). Stage C and `decide()` call that permissive check. `Mask.digest` excludes `kind` and the calibration boundaries (`359-361`), and the constructor accepts caller-provided bin labels without verifying `bin == assign_bins(c, sealed_boundaries)`.

**Executed attacks.** A `FIXTURE` mask was accepted by `stage_power(..., STAGE_C, n_trials=1)` and by `decide()`. Identical fixture/sealed masks had identical digests. A sign vector of length four supplied to a three-row mask was silently truncated and accepted, contradicting the claimed length validation. The existing six refusal fixtures do not cover these paths.

**Why it blocks.** A planning/uniform/parent-position vector can be wrapped as `FIXTURE`, passed through the exact Stage-C and verdict symbols, and become indistinguishable by digest from a sealed accepted mask with the same numeric arrays. Arbitrary bin labels can change per-bin injection, profile attenuation, profile sigma, and the verdict while still passing the type check.

**Minimal repair.** Separate planning/fixture and sealed-production types, or make every production entry point require `kind == SEALED_ACCEPTED_MASK`. Include kind, schema version, field shapes, accepted-mask source digest, calibration-boundary digest, and signs-present flag in a domain-separated mask envelope. Validate sign length exactly and recompute/verify bin labels from the sealed boundaries inside the constructor. Add fixture-kind, altered-bin, altered-boundary, and extra-sign refusal tests.

### 4. BLOCKER — `accuracy_from_handcheck()` is not the quoted HC-1H estimator and the allocator can violate inherited validity floors

**Quote / symbol.** V6 says the calibration producer suite carries the 3×9 allocation and that “V3-pred's HC-1H measurement and validity rules … are carried by quotation at freeze” (`V6:217-226`). V3-pred HC-4 defines each corrected accuracy as `(raw agreement − epsilon_hat)/(1 − 2 epsilon_hat)` and propagates the shared epsilon derivative (`V3-pred:290-303`); HC-1H also fixes 500 real labels and a floor of 30 real labels per one of nine strata (`279-284`).

`accuracy_from_handcheck(agree_counts, n_counts, sigma_shared)` instead sets `a_b = raw`, never accepts `epsilon_hat`, and models the shared term as simply adding `sigma_shared²` to every covariance element (`successor_ref_v2.py:580-602`). With raw agreement 0.9 and epsilon 0.02, the quoted estimator is `0.9166666666666667`; the code returns `0.9`. `allocate_handcheck()` enforces only 10 per non-empty joint cell (`553-577`). An executed 500-label sparse-stratum case was accepted with only 10 labels in one inherited HC stratum, below V3-pred's floor of 30.

There is also a direct docstring/body contradiction: `calibration_bins()` says equality to a boundary goes to the lower bin, but `np.searchsorted(..., side="right")` sends it upward (`538-550`). Nine tied values produced bin sizes `[0,0,9]`.

**Why it blocks.** Calibration changes the scalar/profile/halt branch, attenuation correction, both uncertainty bands, the floor, Stage-C injection accuracies, and the final verdict. V6's producer does not implement the inherited measurement it claims to carry, and its allocation can produce a formally filled but invalid HC-1H sample.

**Minimal repair.** Implement the complete HC-1H producer from raw 3×9 cell records: fixed 500/200/150 roles, 30-real-per-HC-stratum floor, joint allocation precedence, epsilon estimate and correction denominator, shared-epsilon derivative/covariance, repeat/synthetic integrity triggers, per-bin population weighting, and all lower bounds. Fail closed when a floor is infeasible. Correct and test the boundary tie rule, including repeated-coordinate cases and empty-bin refusal.

### 5. BLOCKER — the analytic power null, reduced permutation counts, and all run guards can leak into a production verdict

**Quote / symbol.** V6 says production decisions never use `perm_p_analytic()`, fixes `n_perm=100,000`, and carries authorization/completeness guards (`V6:170-178,205-208`). The code exposes `decide(..., n_perm=N_PERM, _perm=None)` (`683-720`). `_perm` bypasses `perm_record()` entirely; `n_perm` is caller-overridable. `require_environment()` has zero call sites. `require_authorization()` and `require_complete_sample()` are called only by fixture lines 992 and 987, not by a production entry point. There is no integrated real-data runner.

**Executed attacks.** On a `SEALED_ACCEPTED_MASK`, I replaced `perm_record`, `require_environment`, `require_authorization`, and `require_complete_sample` with functions that raise if called. `decide(..., _perm=(beta,p,sigma))` still returned a verdict. `decide(..., n_perm=2)` also returned a numeric verdict and p-value. A 60-row sealed mask with `stage_c_passed=True` returned a numeric verdict despite the 100,000 effective-size floor. `receipt()` continued to emit a receipt after I made the frozen NumPy requirement impossible, because it records the environment but never calls the checker.

**Why it blocks.** The exact function V6 calls the only verdict producer has a public test/analytic injection seam and no authority, completeness, environment, N, or fixed-permutation guard. A lazy production caller can satisfy the named symbol while doing precisely what the constitution says never happens.

**Minimal repair.** Build one production runner that has no `_perm`, `n_perm`, stage, trial, or mask-kind overrides; hard-code the production constants; require frozen environment, pinned authorization, complete parent receipts, sealed-mask provenance, N/N_eq floor, Stage-C receipt, and full `perm_record()` before calling a pure decision helper. Keep synthetic/test hooks in a separately named non-production function. Add monkeypatch tests proving the full permutation function and every guard are necessarily called.

### 6. BLOCKER — the count-oracle and raw/retained repair still have executable seams, and BS-2s never performs its promised Stage-P re-pass

**Quote / symbol.** V6 says `build_plan()` performs BS-2c through BS-2s in one frozen call, `validate_count_oracle()` refuses any missing/extra brick, raw counts drive the ledger and exact-mode boundary, and BS-2s includes a Stage-P re-pass (`V6:86-107,256-260`).

**Executed attacks and code evidence.** `build_plan()` never calls `validate_count_oracle()` and does not accept universe/grouped/ungrouped proof inputs (`successor_ref_v2.py:477-522`). It accepted duplicate brick IDs and returned `[7,7]`. `validate_count_oracle()` accepted:

- three table keys with only two counts, reporting three rows and total 12;
- a negative count vector `[5,-1,8]`;
- floats `[5.9,0.2,7.9]`, silently truncated to integers.

The raw/retained exact boundary remains wrong. `build_plan()` passes retained counts to `local_pass()`, whose mode check counts retained-positive entries (`194-196`). With 17 raw-positive bricks and one raw count of 1 (retained 0), the exact oracle was called because only 16 retained-positive bricks remained. This contradicts both V6 prose and the code docstring that raw counts drive the exact boundary. The V5 gate explicitly requested this 17/16 fixture; V6 does not contain it. Finally, `build_plan()` returns immediately after `local_pass()` and never reruns `stage_power()` on the reduced selected set, despite BS-2s requiring “Stage-P re-pass.”

**Why it blocks.** An invalid count table can enter planning without the validator, change the algorithm branch, and produce a selected set/receipt. The directed raw/retained repair did not close the boundary case or the final power confirmation.

**Minimal repair.** Integrate exact schema validation into `build_plan`: equal field lengths, unique keys, nonnegative integral counts, finite bounded c bytes, universe equality, independent grouped/ungrouped proof, and branch/product digests. Pass an explicit raw-positive candidate count to the selection mode decision while using retained counts only for leverage. Add the 17-raw/16-retained fixture and mandatory Stage-P re-pass on the final selected planning mask; bind its result into BS-2s.

### 7. BLOCKER — PWR-EQ's 5% quantile tolerance does not establish the required 95% power equality

**Quote / symbol.** V6 calls PWR-EQ an “equality contract”: one N=400 injected sign realization, 20,000 permutations, and acceptance when the analytic and Monte-Carlo 0.999 quantiles differ by less than 5% (`V6:170-178`; code `890-901`). Stage P then selects the first prefix whose analytic-null simulation yields at least 962/1000 successes.

**Checks that held.** Independent exhaustive enumeration across N=4…7 and several sign imbalances reproduced exact mean zero and `perm_sigma_exact()` to at most `1.11e-16`. Under the Stage-P injection model at a=0.85 and |c|≤1, the expected plus fraction is bounded to 0.48572–0.51428, so the realistic production injection imbalance is not extreme. The normal approximation is therefore plausible at N/N_eq scale; the exact mean/variance claim is not the defect.

**Why the contract still fails.** A relative critical-quantile tolerance is not a bound on power error. At the one-sided 0.001 normal critical value 3.0902323, a permitted 5% critical shift is 0.15451 sigma. A signal with analytic decision probability 0.95 can then have true decision probability about 0.93193 in the unsafe direction (or 0.96402 in the other direction). Even the fixture's measured 0.6578% difference corresponds to a possible 0.94787–0.95206 range around 0.95 if direction were not known. The fixture tests one small mask/sign draw, not the Stage-P success count across 1,000 injected skies, the selected prefix, the profile Stage-C path, or any production-scale geometry. Nothing requires the analytic method to be conservative.

**Minimal repair.** Define equality in the decision/power metric: across a pinned family of representative and adversarial masks, compare analytic and full-MC decisions for the same addressed injection trials, with enough permutations/replicates to bound tail Monte-Carlo error. Require either conservative analytic critical values or a confidence-bounded power discrepancy small enough that the full-MC lower bound remains ≥0.95. Bind that result to each Stage-P/Stage-C geometry class, not one N=400 fixture.

### 8. BLOCKER — the slot machine still omits the promised inputs, schemas/digests, code symbols, and executable primary lock

**Quote / symbol.** Section 7's heading promises “producer · inputs available at that time · schema · code symbol · blocks” (`V6:248`). The class-P table has only `slot | producer | content | code symbol | blocks`; it has no input or schema/digest columns. The class-E table drops code symbol too (`267-276`). Generic `receipt(slot, fields)` does not define which fields are required for any slot, their shapes, or cross-slot digest bindings.

**Class-P walk.** BS-1/BS-1b are blocked by Finding 2. BS-2c is blocked by Finding 6. BS-2o has ledger symbols but no slot schema and inherits invalid oracle inputs. BS-5p has a symbol but inherits Findings 3, 5, and 7. BS-2s has the wrong exact boundary and no re-pass. BS-2m is blocked by Finding 1. BS-3 names historical constants but no exact input/schema/digest symbol. BS-9 names the R1–R5 rerun and correctly preserves the old-runner prohibition, but provides no production input-function schema, runner symbol/hash field schema, or gated-replacement receipt type. BS-4's sign direction is sound, but its receipt schema is absent. BS-7p has fixtures/environment content, but environment enforcement is unused and boundary/slot schemas are absent. BS-8p is blocked by Finding 4.

**Class-E walk.** BS-6 has no code symbol or receipt schema. BS-2f cannot bind sealed provenance/boundaries correctly (Finding 3). BS-8f is produced by the wrong calibration formula (Finding 4). BS-5f accepts fixture masks and caller-chosen execution parameters. BS-7f returns a vector but does not emit the promised canonical 800,000-byte payload digest/receipt and permits caller-selected `n_perm`. BS-V names “verdict + primary lock,” but `decide()` performs no lock, durable write, receipt construction, or disclosure barrier. On calibration failure it raises `InconclusiveByCalibration` instead of emitting the named `INCONCLUSIVE-BY-CALIBRATION` outcome.

**Obligation/slot mismatches.** The published per-function normative specification and clean-room fixture gate in §6 have no slot. Authorization/completeness enforcement has no production slot/runner. The BS-V lock has a slot but no implementation. Conversely, several slots list broad prose bundles rather than one checkable producer/schema.

**Minimal repair.** Replace §7 with a true machine contract: for every slot, exact predecessor digests, inputs available then, required typed fields/shapes, canonical serialization, envelope digest, producing code symbol/version, predecessor dependencies, blocker/failure outcome, and next gate. Add explicit slots for the normative clean-room spec/agreement and production authorization/completeness runner. Implement and test BS-V's atomic primary lock and disclosure refusal.

### 9. BLOCKER — the claimed lapsed-spec validation battery is materially weakened and does not test its named boundaries

**Quote / symbol.** V6 says the validation battery is “carried verbatim in intent from the lapsed build spec” (`V6:200-208`). The spec requires +0.0408 to return REPRODUCED at frozen power, an amplitude just below the evaluated floor not to reproduce, and N=99,999 to return INCONCLUSIVE-BY-POWER (`VERDICT_ESTIMATOR_BUILD_SPEC:68-77`).

**Code evidence.** `BATTERY-POS-RUNS` injects `A_LONGO/0.86`, not +0.0408, uses N=60,000, supplies an analytic `_perm` tuple rather than the full production permutation path, and declares PASS if the result is any of REPRODUCED, INCONCLUSIVE, or REJECTED (`successor_ref_v2.py:955-981`). That condition only proves the function returned a numeric outcome. There is no just-below-floor fixture and no N=99,999 fixture. `BATTERY-POWER` merely passes an externally supplied `stage_c_passed=False` on N=50 (`982-983`); it does not derive failure from N or exercise a guard.

**Why it blocks.** These are the exact validation cases intended to catch sign, floor, power-floor, and integration errors before freeze. The current fixture names make the output look covered while the assertions permit or omit the prohibited behavior. Finding 5's successful N=60 verdict is the consequence.

**Minimal repair.** Restore the exact lapsed-spec cases through the integrated production runner: +0.0408 at a preregistered powered N must meet the specified reproducibility criterion; an addressed just-below-floor case must not reproduce; N=99,999 must derive INCONCLUSIVE-BY-POWER without a caller-provided boolean; and the positive path must necessarily execute the full fixed-count permutation record. Assertions must test the required verdict/prohibition, not membership in all numeric outcomes.

## Directed citation/sign-anchor result

The arXiv source verifies the title, author, 15,158 sample, published amplitude `−0.0408 ± 0.011`, and approximate Galactic axis `(52°,68.5°)`, and links DOI `10.1016/j.physletb.2011.04.008`.[1] Crossref independently verifies the DOI, author, journal, volume 699, and pages 224–229.[3] The exact ADS record identifier is `2011PhLB..699..224L`; the ADS abstract page itself presented a human-verification wall, but exact-bibcode search resolved to that record and matching title.[2]

The sign mapping is consistent across V6 and code: published `−0.0408` in Longo's `(R−L)/(R+L)` convention; our `+0.0408` in the documented `(L−R)`/CCW-positive East-of-North convention. V3-pred F-5, `LANA_BS5_LONGO_SIGN_20260814.md`, the synthetic anchor, and its Kun gate agree. Independent axis inspection gave norm `0.9999999999999998`, RA `216.98443550521523°`, Dec `32.06061090116198°`. This directed attack held.

## Inherited-defect closure matrix

| inherited defect | V6 result |
|---|---|
| 1. manifest-versus-parent gap | **Not closed:** set comparison works only after a complete planner map is supplied; omitted objects/neighbours pass (Finding 1). |
| 2. footprint-blind power | **Not closed as an admissibility contract:** typed objects exist, but Stage C accepts `FIXTURE` and arbitrary bins (Finding 3). |
| 3. full-sky `3·D` normalization | **Closed in the pinned estimator:** `beta_slope()` uses centred footprint slope; no `3·D` decision path found. |
| 4. attenuation-versus-target mismatch | **Partly closed, still blocked:** beta/A split exists, but the calibration attenuation producer is not HC-1H (Finding 4). |
| 5. unreachable p threshold | **Not closed as a production contract:** default 100,000 exists, but production symbols accept reduced counts and the battery/runner do not enforce it (Findings 5 and 9). |
| 6. silent axis divergence | **Closed for the pinned reference:** one AXIS constant; independent norm/RA/Dec check held; sign anchors agree. |
| 7. contiguous/count-based selection | **Partly closed, still blocked:** contiguous selection is absent, but the raw-positive exact boundary, oracle integration, and final Stage-P re-pass are wrong/missing (Finding 6). |
| 8. verdict by human reading | **Partly closed, still blocked:** `decide()` exists, but test/analytic bypasses, missing guards, calibration exception, and absent lock prevent it from being the sole production verdict path (Findings 5, 8, 9). |

## Attacks that held

1. All three custody pins matched before review; fixtures reproduced byte-for-byte with exit 0 and empty stderr.
2. The no-BLAS/no-spawn/two-random-calls claims held statically: no matrix-multiply AST node, no `.spawn`, no `.binomial`, and exactly two `rng.random()` calls in the per-object injection body.
3. Exact permutation mean zero and variance formula held under independent exhaustive enumeration for multiple small N/sign balances.
4. Citation metadata, published negative sign, our positive-sign mapping, and the axis held as described above.
5. All eight photometric predicates occur in V6 and BS6-pred with matching operator/numeric content; the ellipticity executable string is byte-identical. The no-surface-brightness-cut disclosure also agrees.
6. The five old selector counterexamples and the V5 raw/retained example pass their pinned fixtures. Finding 6 is the still-untested 17-raw/16-retained boundary and validator/orchestrator seam, not a claim that those old fixtures fail.
7. `sigma_ours_profile()` uses an explicit scalar double loop; the former BLAS contradiction is repaired.
8. The draft/run boundary is explicit: V6 authorizes writing only and does not itself claim authorization to fetch, run, freeze, publish, commit, or disclose.
9. BS-9 text retains the R1–R5 rerun and `nm_acquire_cutouts.py` prohibition; the finding is missing executable schema/custody, not deletion of that prohibition.

## Testimony

- V6 explicitly labels `Cov(beta_hat, a_hat)=0` / `Cov(beta_hat,{a_hat_b})=0` as freeze testimony. I found no independent proof and did not use it as a verdict premise.
- V6's drafting-time claim that DR11 pages exist but no photo-z product is present is not tied to a cited receipt in this packet. I did not resolve the branch or perform a survey-product fetch; the claim remains author testimony for this gate.
- The exact historical object IDs, declinations, neighbour bricknames, and 60,310 narrative appear in V6/code/brief but no separately cited source artifact under `../../` was located by exact-ID/name search. The brief entitles the gate to the defect shape, so I used it to attack the mechanism, but I do not independently certify those historical facts here.
- The finite-population CLT's production-tail adequacy is plausible under the stated N/leverage and injected sign balance, but no theorem/error bound or production-mask family is pinned. Finding 7 rests on the contract's failure to bound power error, not on an unsupported claim that normality necessarily fails.

## Evidence ledger and boundary

Read: the V6 brief; pinned V6 constitution, code, and fixtures; both V5 gates; amended scope; V3-pred; BS6-pred; lapsed build spec; signed decline memo; Longo sign dictionary; synthetic sign anchor and Kun gate; and exact-search results for cited internal claims. External source checks used arXiv, ADS locator/search, and Crossref.

Executed: all required and source hashes; exact fixture subprocess/byte comparison; environment inventory; AST guard/call/randomness/BLAS checks; count-table length/negative/float attacks; duplicate-brick planning; 17-raw/16-retained branch instrumentation; omitted-object/home-only manifest attacks; fixture-vs-sealed mask/digest/bin/sign-length attacks; analytic/null/guard bypass; reduced-permutation and N=60 decisions; calibration formula/allocation/tie attacks; independent permutation variance enumerations; axis conversion; power-tolerance arithmetic; and byte-substring quotation checks.

No `/Users/duhokim/NebulaMindData/` path was read. No real survey product, row, image, chi value, or sky statistic was fetched or computed. No source artifact, git state, publication, process, authorization, freeze, or runtime was mutated. GPT56's only write in this directory is this report; the concurrently appearing CODEX V6 report was not read and did not affect this verdict.

## Sources

[1] https://arxiv.org/abs/1104.2815 — Longo 2011 arXiv abstract
[2] https://ui.adsabs.harvard.edu/abs/2011PhLB..699..224L — NASA ADS record 2011PhLB..699..224L
[3] https://api.crossref.org/works/10.1016/j.physletb.2011.04.008 — Crossref record for Longo 2011 DOI

**REFUSED**

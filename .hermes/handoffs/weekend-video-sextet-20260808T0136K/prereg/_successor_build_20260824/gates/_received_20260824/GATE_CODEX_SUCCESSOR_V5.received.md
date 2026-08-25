# CODEX adversarial gate — successor preregistration V5

## Verdict

**REFUSED.** V5's pinned fixture output reproduces byte-for-byte, the five selector counterexamples now pass, and several V4 defects are genuinely repaired. The freeze candidate still has blocking code/prose seams: the mandatory fallback Stage-C power path cannot execute; the code does not implement or validate several mechanisms that §0 says it defines; the blind-double rule withholds algorithmic information needed for exact agreement; the output-affecting NumPy environment is recorded rather than frozen; and calibration/count-oracle/receipt obligations remain non-unique or unexecutable under their laziest compliant readings.

## Custody pins — computed before review

The first content-review prerequisite was:

`shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V5_20260824.md ../ref/successor_ref.py ../ref/FIXTURES_20260824.out`

Computed:

- `../PREREG_SUCCESSOR_DRAFT_V5_20260824.md` = `1c283bbf6dd7bd598ff5afc429c3d534de82cb26fff47d12bc4ca812b6f22b1d`
- `../ref/successor_ref.py` = `67bc4876858c4cb4445ccf40f41a4d3977c1d43e0b88ec5890d9b6b0091a4449`
- `../ref/FIXTURES_20260824.out` = `c82b2a253c4f55b9b4f28f697d496f8e8cbf5762771307c036ca77dd65950e25`

All three equal the brief's pins, so review proceeded.

Independent source pins:

- V3-pred = `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- BS6-pred = `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`
- amended scope = `995b2e729a3362f0445cac9d5da6d290fddac9f8018e75f2c0aa87c190c93de7`

## Environment and fixture reproduction

- Python: `3.9.6` (`Clang 21.0.0`)
- NumPy: `1.26.4`
- `sys.platform`: `darwin`
- Detail: `macOS-26.6.2-arm64-arm-64bit`
- Machine: `arm64`
- Byte order: little-endian

`python3 -B ../ref/successor_ref.py --fixtures` exited 0. Capturing stdout without an intermediate file gave SHA-256 `c82b2a253c4f55b9b4f28f697d496f8e8cbf5762771307c036ca77dd65950e25`; it was byte-equal to the pinned fixture file, with empty stderr. Thus there is no matching-environment fixture divergence.

## Numbered findings

### 1. BLOCKER — the mandatory fallback Stage-C power path cannot execute

**Quote/symbol.** Constitution §4 lines 113–117 requires `stage_power()` on the accepted-position mask with either scalar `a_LB` or fallback `{a_LB_b}`. The pinned implementation exposes `stage_power(c_objects, a: float, stage, prefix, ...)` at code lines 273–286 and passes `a` unchanged to `inject_trial()`; `inject_trial()` compares scalar `u2` with `(1.0 - a)` at line 269. It has no `bins` argument and no per-object accuracy path.

**Executed attack.** Passing a three-element `a_b` array to the exact Stage-C API failed before any power result:

`fallback_stage_c= ValueError The truth value of an array with more than one element is ambiguous.`

This is not an omitted fixture alone. The function signature cannot associate an accepted object with its calibration bin, and the body cannot inject with `{a_LB_b}`. Yet spread failure with every `a_LB_b >= 0.85` is an expressly admissible fallback outcome (§6 lines 143–145), so this is a reachable required branch.

**Why it blocks.** A compliant run can reach fallback and then has no defined Stage-C producer. It cannot fill class-E BS-5f, cannot unblind, and cannot classify the run using the frozen mechanism.

**Minimal repair.** Add a frozen object-specific injection/power API accepting canonical `bins` plus `a_b`, validate their shape/range, use `a_b[bins[i]]` per accepted object, and add scalar/fallback Stage-C fixtures with fixed success counts and digests. Bind BS-5f to that exact symbol.

### 2. BLOCKER — §0's “code is the definition” claim exceeds the code: required mechanisms and receipt schemas have no symbols

**Quote/symbol.** Section 0 lines 11–20 says every operational mechanism, all estimators and sigmas, and all digest serializations are defined by `successor_ref.py`. The code contains 22 functions, but no function for the BS-2c manifest/anti-join closure, accepted-mask validation or canonical sorting, retained brick-centre object expansion, c-tertile construction, joint HC allocation, scalar/fallback admissibility decision, Stage-C mask provenance, final decision regions/floor, receipt production, environment serialization, or raw-permutation-index reconstruction.

The concrete absences matter at named slots:

- §2 lines 50–60 specifies BS-2c's universe join and three closure proofs; code only has a hard-coded three-row toy inside `run_fixtures()`.
- §4 lines 114–117 makes mask provenance, acceptance, and canonical `(brickid,objid)` order binding; `stage_power()` receives only `c_objects` and a scalar/array-like `a`, so it cannot inspect any of those fields.
- §3 line 98 requires `np.std(beta_perm, ddof=1)`, but no code symbol computes or validates `sigma_beta`.
- §5's decision regions and floor have no code symbol.
- §7 lines 180–182 requires BS-7f recomputation from raw indices AND labels; `perm_record()` returns only `(beta_obs, beta_perm, p)` and neither emits nor serializes permutation indices.
- Serialization code defines generic `canon_f8`, `canon_i8`, and one `ledger_digest`; no schemas exist for the accepted mask, calibration boundaries/Covariance, S_final, injection labels, permutation indices, environment, power receipt, or decision receipt.

**Executed attacks.** A noncanonical reversed row order passed `perm_record()` without complaint. Its observed slope and p happened to agree on the six-row fixture, but its permutation-vector digest differed. Duplicate brick IDs also passed `greedy_ledger()` and appeared twice in the ledger as brickid 7. These are exactly the failures an absent input/schema validator cannot reject.

**Why it blocks.** Under §0, missing code is not discretionary prose implementation work: it is a missing definition. The class-P/class-E register cannot be filled uniquely or blind-doubled from the pinned bytes, and inadmissible Stage-C inputs can pass through the exact function named as the gate.

**Minimal repair.** Either narrow §0 truthfully to the symbols it actually defines or add a complete pinned runner/validator layer. Every slot needs a named producer symbol, typed input/output schema, canonical serialization, validation/fail state, and digest function. In particular add canonical mask construction/validation, calibration construction/allocation/Covariance, Stage-C dispatch, BS-7f index+label reconstruction, sigma-beta, and final decision/floor functions.

### 3. BLOCKER — the interface-only blind double cannot reproduce body-defined algorithms

**Quote/symbol.** Section 6 lines 155–160 says the second implementation is built from the constitution plus the reference code's INTERFACE — “function signatures, address scheme, serialization schema” — without reading the bodies, while requiring exact integer/sequence and byte-equal digest payload agreement.

**Why it fails.** The constitution intentionally delegates semantics to code bodies. Function signatures do not disclose, among other things:

- the incremental `cbar` and `L` updates in `greedy_ledger()` lines 126–130;
- exact enumeration's combination traversal and lexicographic winner construction, lines 145–153;
- the production local-pass move loop and nested scan behavior, lines 179–222;
- the per-object two-draw injection operation, lines 263–269;
- the exact permutation-vector construction, lines 247–255;
- the fallback numerical evaluation order, lines 294–328.

Even the only explicit digest schema, `ledger_digest()`, is in a function body. The constitution does not restate enough of these mechanisms to derive exact sequences and bytes independently. Allowing the second author to read docstrings would still not provide all body operation order, and the brief provides no separately pinned interface/spec artifact.

**Why it blocks.** The blind-double slot is required in class P for BS-2o and BS-2s. With the information boundary as written, exact agreement is not a testable pre-freeze obligation; it requires either reading the forbidden source semantics or guessing them.

**Minimal repair.** Publish and pin a complete language-neutral normative interface/specification containing every algorithm, operation order, validation rule, address, and byte schema. Build the reference and blind implementation independently from that spec. Alternatively permit the blind author to read the entire normative source and rename the check accurately as a reimplementation check rather than an interface-only blind double.

### 4. BLOCKER — output-affecting environment choices are recorded post hoc, not frozen pre-run

**Quote/symbol.** Section 0 lines 18–23 says fixture digests are valid under the recorded environment and every receipt records its own environment. Code lines 7–15 conditions determinism on a fixed NumPy version. The only fixture environment fields are `numpy=1.26.4 platform=darwin`.

**Why it fails.** No class-P slot requires production to use NumPy 1.26.4, Python 3.9.6, arm64, little-endian execution, a pinned wheel/build, or any approved environment digest. A future executor can select another NumPy environment after freeze; both implementations then run under that same chosen environment and can agree, while producing different addressed RNG/permutation bytes from the frozen fixture environment. Recording that choice in the receipt discloses it but does not preregister it.

This is load-bearing because `default_rng`, `SeedSequence`, `Generator.random`, and `Generator.permutation` determine BS-5p, S_final via `L_plan`, BS-5f, and BS-7f. The current machine happened to match and reproduce the fixture exactly; that does not close the unbound production choice.

**Minimal repair.** Freeze an exact production environment before BS-5p: Python, NumPy, architecture/endianness, dependency lock and artifact hashes (or a container/image digest). Require every P/E producer to match it and fail otherwise. If multiple environments are allowed, enumerate them pre-freeze with pinned fixture outputs and a deterministic selection rule that cannot depend on results.

### 5. BLOCKER — `stage_power()` does not enforce its production permutation contract or input provenance

**Quote/symbol.** Constitution §3 fixes `n_perm=100,000`; §4 binds Stage P/C identities and mask admissibility. Code `stage_power()` exposes public `n_perm` and `stage` arguments without validating `n_perm == N_PERM`, `stage in {STAGE_P,STAGE_C}`, the required prefix convention, or the source/canonical order of `c_objects`.

**Executed attack.** The exact pinned function accepted `n_perm=0` for all 1,000 trials and returned `(0, False)` rather than rejecting the non-production contract. A noncanonical reversed physical row order also succeeded and changed the permutation payload digest.

**Why it blocks.** The laziest “call `stage_power()`” implementation may supply a wrong permutation count or non-mask/noncanonical vector and still produce a valid-looking receipt. A false result is conservative in the `n_perm=0` attack, but the binding requirement is the predeclared algorithm, not merely a direction of bias; other alternative positive counts or inputs can change success counts either way.

**Minimal repair.** Separate fixed production APIs from fixture-scale APIs. `stage_power_production` should hard-code `N_TRIALS`, `N_PERM`, allowed stage/prefix values, and consume a validated canonical typed mask/brick-centre artifact rather than a bare vector. Keep an explicitly nonbinding fixture helper for reduced counts.

### 6. BLOCKER — sigma functions permit non-finite decision quantities, and the determinism header contradicts the profile body

**Quote/symbol.** Code lines 7–11 promise scalar/1-D operations and “no BLAS matrix calls.” `sigma_ours_profile()` lines 321–328 accepts a 2-D covariance matrix and evaluates `g @ (C @ g)`. Neither sigma function checks finite inputs/output, positive `q`/`w`, covariance symmetry, or positive semidefiniteness.

**Executed attacks.** Supplying a covariance with one NaN returned `nan` from `sigma_ours_profile()` with no exception; supplying `sigma_a=nan` likewise returned `nan` from `sigma_ours_scalar()`. The code's finite-only rule applies only later if a caller happens to serialize via `canon_f8`; no final decision function exists to guarantee that path.

**Why it blocks.** `sigma_ours` enters every decision band and the detection floor. The reference definition can therefore emit a non-finite decision input without its stated fail-closed behavior. Separately, the matrix multiplication contradicts the file-level determinism contract and leaves BLAS/build behavior outside the recorded two-field environment.

**Minimal repair.** Validate all scalar/profile inputs and outputs as finite; require `q>0`, nonzero/positive licensed `w`, exact dimensions, symmetric finite PSD `Cov_a`, valid bin indices, and fail closed otherwise. Replace matrix multiplication with an explicitly ordered scalar reduction if the no-BLAS/operation-order promise is retained, and add non-finite/asymmetric/non-PSD fixtures.

### 7. BLOCKER — BS-2c's “dual anti-join” closure is impossible on raw groups or vacuous after zero fill

**Quote/symbol.** Section 2 lines 50–55 says grouped per-brick counts are left-joined to the independent manifest, missing groups become zero rows, and “the anti-join in both directions is empty.” The pinned toy has manifest `[10,11,12]` and raw grouped keys `{10,12}`, with 11 intentionally absent.

**Why it fails.** If the dual anti-join compares the manifest to the raw grouped result, manifest-minus-groups contains brick 11 and cannot be empty whenever a genuine zero-count brick exists. If it compares the manifest to the post-left-join table, both keysets are equal by construction; the proof is tautological and cannot detect a dropped service group that was silently materialized as zero. The grouped-sum/ungrouped-total equality still compares two queries against the same service scope, so the same accidental restriction can preserve equality. There is no code validator that disambiguates which relations are compared.

**Why it blocks.** BS-2c is the pre-freeze population oracle feeding every later prefix and power calculation. Its stated proof cannot distinguish the intended zero-fill from an omitted nonzero group under its laziest compliant reading.

**Minimal repair.** Name three distinct relations and checks: raw grouped keys must be a unique subset of the manifest; the final left-joined table keys must equal the manifest exactly; and every manifest brick's count must be independently accounted for by a partitioned query/producer total that cannot share an accidental footprint filter with the grouped query. Pin schemas and implement these checks in a reference validator, including a fixture with one genuine zero and one deliberately dropped nonzero group.

### 8. BLOCKER — BS-8p/BS-8f still leaves outcome-changing allocation and covariance production freedom

**Quote/symbol.** Section 6 lines 137–146 says quotas over the 3×9 cells are proportional to cell counts with minimum 10 per non-empty cell, and BS-8f supplies a full `Cov_a` including shared synthetic error. V3-pred separately fixes 500 real, 200 synthetic, 150 mirror re-presentations and real-stratum floors, but V5 does not state which quota classes cross the new c bins, an integer apportionment/rounding/tie rule, how minima and the inherited floors reconcile, or the analytic cross-bin covariance generated by the shared global synthetic-error estimate.

The code has `w_gradient()` and consumes an arbitrary matrix in `sigma_ours_profile()`, but it neither constructs nor validates `Cov_a`; its fixture compares two arbitrary covariance matrices sharing marginal scales. Thus the fixture demonstrates sensitivity rather than freezing the producer.

**Why it blocks.** Different integer allocations can produce different per-bin estimates and standard errors. Different off-diagonal shared-error terms with the same marginals move the fallback sigma, decision bands, floor, and possibly the scalar/fallback/halt branch. Requiring a field named `Cov_a` after measurement does not freeze how it is computed.

**Minimal repair.** Define the complete integer allocation algorithm (quota class, total, minima precedence, remainder/tie order, empty cells, synthetic and repeat placement). Freeze explicit formulas for every `Cov_a[b,b']` term, including the shared epsilon derivative and any conservative covariance addition, with a named producer function and numeric fixtures reconstructed from cell counts.

## V4 finding closure — all 18 traced individually

The §9 trace was checked against both V4 reports, not accepted by label alone.

| V4 finding | V5 status | Evidence |
|---|---|---|
| gpt56 F1 — pre-freeze BS-7 requires real result | repaired | BS-7p/BS-7f split and class-E ordering at §7 lines 173–182. |
| gpt56 F2 — false minimization / non-executable local pass | repaired for the named counterexamples | Exact mode is mandatory through 16 positive bricks; all five fixtures pass; production minimality is expressly retired. |
| gpt56 F3 — calibration timing/fallback uncertainty | partial, still blocking | Boundaries moved to BS-2f and profile formulas exist, but Findings 1 and 8 leave fallback Stage C and Covariance production unexecutable/non-unique. |
| gpt56 F4 — Stage P/C randomness nonreproducible | partial, still blocking | Addressing/call order is much better, but Findings 4–5 leave environment, production count, and canonical-input enforcement open. |
| gpt56 F5 — count completeness/zero brick | partial, still blocking | Zero traversal is fixed; Finding 7 shows the stated closure proof is impossible or vacuous. |
| gpt56 F6 — float/order/digest under-specification | repaired only for ledger | Code freezes ledger arithmetic and binary payload, but Finding 2 rejects the broader §0 all-digests claim. |
| gpt56 F7 — stale input-path receipts | repaired in text | BS-9 names release HDU/plane schema, production input hash/layout, R1–R5 rerun, replacement runner, and predecessor-runner prohibition. |
| gpt56 F8 — void excludes §6 | repaired | Void now covers §§1–6, code, slots, algorithms, schemas, randomness, and thresholds; exemption is narrowed to frozen-producer E values. |
| codex F1 — selector false minimization/non-unique moves | repaired for named issue | Exact ≤16 output and production move body are unique; no production minimality claim. |
| codex F2 — BS-7 class contradiction | repaired | Same split as gpt56 F1. |
| codex F3 — boundaries assigned before mask | repaired | Algorithm predeclared; values instantiated at BS-2f. |
| codex F4 — fallback uncertainty undefined | partial, still blocking | Formula/gradient/full-matrix field added; Findings 1, 6, and 8 remain. |
| codex F5 — no stage/prefix address | partial, still blocking | Address tuple exists; Findings 4–5 remain at environment/API/input boundaries. |
| codex F6 — raw versus retained leverage | repaired | L_raw/L_ret are separated; thresholds and N_eq bind retained leverage. |
| codex F7 — exact order/digest incomplete | repaired only for ledger | `c_j` bytes, operation order, `Var=L/N`, and ledger binary schema are bound; other required payload schemas are absent (Finding 2). |
| codex F8 — count oracle incomplete | partial, still blocking | Independent manifest and zero fill added; Finding 7 defeats the written proof. |
| codex F9 — void excludes §6 | repaired | Same as gpt56 F8. |
| codex F10 — two-version inventory wording | repaired | V5 states two 1,436-file groups and a one-release ~1.776-TB extrapolation from five measured sizes. |

## Slot-machine walk

### Class P

- **BS-1:** temporally fillable after Duho's 2026-09-05 rule, although the exact “exists at freeze” check remains a prose receipt.
- **BS-1b:** required fields are named, but no producer/schema is named.
- **BS-2c:** inputs are conceptually pre-freeze and rowless, but Finding 7 blocks the proof and Finding 2 notes no validator.
- **BS-2o:** `greedy_ledger()` and `ledger_digest()` exist; canonical validated input still depends on BS-2c.
- **BS-5p:** `stage_power()` exists for scalar planning, but retained brick-centre expansion/canonicalization has no symbol, production parameters are overrideable, and environment is not frozen.
- **BS-2s:** exact and production procedures exist; all five old counterexamples pass. It remains downstream of blocked BS-5p.
- **BS-3 / BS-9:** the successor route/HDU/input-function/R1–R5/replacement-runner obligations are now present and pre-real-image; old `nm_acquire_cutouts.py` evidence is correctly prohibited.
- **BS-7p:** code/fixture pins and address scheme exist; the environment and several claimed payload schemas do not.
- **BS-8p:** boundary timing is acyclic, but Finding 8 blocks the allocation/covariance plan.

### Class E

- **BS-6:** occurs before first image byte and names manifest/checksum/ceiling fields; no exact receipt schema or producer identity is present in V5.
- **BS-2f:** occurs after inference and before Stage C, but accepted-row filtering, canonical sorting, boundary construction, and serialization have no code producer.
- **BS-8f:** fields are named, but the covariance/allocation producer is not defined.
- **BS-5f:** scalar branch is callable only on a bare vector; fallback branch is impossible and mask provenance is unenforced.
- **BS-7f:** `perm_record()` produces beta values and p, but the required raw-index AND label reconstruction/serialization is absent.
- **Decision release:** no named code/receipt slot evaluates §5's bands, floor, non-finite handling, or final mutually exclusive outcome.

There is no pre-freeze dependency on real chi after the BS-7 split. The blocking defects are missing/non-unique producers and seams, not the old temporal cycle.

## Quotation fidelity

Attacks that held:

- V3-pred hashes and V5's quoted Longo amplitude, published sigma, galactic axis, one-sided sign, 100,000 permutations, p thresholds, 3.09 floor, 0.85 floor, instrument tau, and 85.72% (= 0.8572) retention agree in substance with the pinned predecessor.
- All eight BS6-pred predicates appear in V5 in the same operator/numeric form. Predicate 6 is the exact executable string `POWER(shape_e1,2)+POWER(shape_e2,2) < 0.1836734693877551`.
- No surface-brightness cut is correctly disclosed.
- Independent axis checks gave norm `0.9999999999999998`, display RA `216.98443550521523°`, Dec `32.06061090116198°`.
- Independent Clopper–Pearson lower bounds were `0.9493659932051121` at x=961 and `0.950487129744074` at x=962; 962 is the first passing integer.

## Additional attacks that held

1. The five selector fixtures (V2, both V3, both V4) all returned the brute-force expected subsets, and `local_pass` equaled exact mode in every case.
2. The V4 BS-7 temporal cycle is genuinely removed.
3. The raw/retained leverage distinction is explicit and the retention fixture returns `[1,2,8]`, raw L `7.733333333333333`, retained L `4.545454545454545`.
4. Prefix changes alter the injection stream, while identical addresses reproduce identical labels in the matching environment.
5. The plus-one one-sided permutation p boundary is non-vacuous with 100,000 permutations.
6. The fallback point identity and analytic gradient fixture recover `A_LONGO` under the supplied unit-weight model.
7. The void clause now reaches calibration, code, slot schema, randomness, serialization, and thresholds; it is materially stronger than V4.
8. BS-9 carries the predecessor's exact single-band/HDU/production-input/R1–R5 requirements and the old-runner prohibition rather than claiming predecessor receipts suffice.

## Performance observation (not a verdict basis)

A bounded benchmark of `perm_record()` at N=10,000 and 1,000 permutations took 0.104206 s on the recorded machine. Linear scaling extrapolates one N=100,000/100,000-permutation record to about 104.2 s and one 1,000-trial Stage-P/Stage-C call to about 104,206 s (1.206 days), before scanning multiple prefixes. This is an extrapolation, not a measured production run and not used as a blocker, but the exact reference procedure needs an explicit execution budget and feasibility receipt before freeze.

## Testimony

None. Verdict-bearing claims above come from the pinned files, direct symbol inventory, exact fixture execution, and the shown adversarial calls. The performance paragraph is explicitly labelled an extrapolation and is not used for the verdict.

## Evidence ledger

Content read:

- `BRIEF_GATE_SUCCESSOR_V5.md`
- `../PREREG_SUCCESSOR_DRAFT_V5_20260824.md`
- `../ref/successor_ref.py`
- `../ref/FIXTURES_20260824.out`
- `GATE_GPT56_SUCCESSOR_V4.md`
- `GATE_CODEX_SUCCESSOR_V4.md`
- `GATE_GPT56_SUCCESSOR_V3.md`
- `GATE_CODEX_SUCCESSOR_V3.md`
- `../../SUCCESSOR_SCOPE_20260821.md`, including Amendment 1
- `../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
- `../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md`

Executed checks:

- SHA-256 of all three required V5 artifacts before review; SHA-256 of predecessor, BS6-pred, and amended scope.
- Exact fixture execution, stdout SHA-256, byte comparison, exit/stderr capture, and detailed environment inventory.
- Function/symbol inventory and targeted mechanism/schema search over the reference code.
- Fallback Stage-C array attack.
- `stage_power(n_perm=0)` production-contract attack.
- Noncanonical-row permutation attack with forward/reverse digest comparison.
- Duplicate-brickid and non-integral-count coercion attacks.
- NaN scalar/profile sigma attacks.
- Independent axis norm/display conversion.
- Independent SciPy one-sided Clopper–Pearson scan.
- Exact substring checks for predecessor constants and all eight BS6 executable predicates.
- Bounded `perm_record()` timing benchmark and explicitly linear extrapolation.
- Full P/E slot and all-18-V4-finding reconciliation against the pinned V5 prose/code.

No `/Users/duhokim/NebulaMindData/` path was read. No source artifact was edited. No git mutation, publication, data fetch, or run authorization occurred. The only write in this gate directory is this report.

**REFUSED** — blockers: fallback Stage C is not executable; §0 overclaims code coverage and digest/receipt definitions; the interface-only blind double cannot derive body-defined semantics; the production environment is not frozen; Stage power does not enforce production parameters or mask provenance; sigma paths fail open on non-finite inputs and contradict the no-BLAS contract; BS-2c's dual anti-join proof is impossible or vacuous; and BS-8p/BS-8f leaves allocation and covariance production unfrozen.

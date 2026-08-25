# GPT56 ADVERSARIAL GATE — successor preregistration V5

## Custody pins — computed before review

The first review command was:

`shasum -a 256 ../PREREG_SUCCESSOR_DRAFT_V5_20260824.md ../ref/successor_ref.py ../ref/FIXTURES_20260824.out`

Computed:

- `1c283bbf6dd7bd598ff5afc429c3d534de82cb26fff47d12bc4ca812b6f22b1d  ../PREREG_SUCCESSOR_DRAFT_V5_20260824.md`
- `67bc4876858c4cb4445ccf40f41a4d3977c1d43e0b88ec5890d9b6b0091a4449  ../ref/successor_ref.py`
- `c82b2a253c4f55b9b4f28f697d496f8e8cbf5762771307c036ca77dd65950e25  ../ref/FIXTURES_20260824.out`

All three equal the brief's required pins. Review proceeded on those bytes.

Independent source pins recomputed:

- V3-pred: `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- BS6-pred: `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`
- amended scope: `995b2e729a3362f0445cac9d5da6d290fddac9f8018e75f2c0aa87c190c93de7`
- sweep inventory: `2df3a22065344a3378e069b022d316f39164ddc908f73d0fb4cfcf40323e0550`

## Environment and fixture reproduction

- Python: `3.9.6` (`/Library/Developer/CommandLineTools/usr/bin/python3`), Clang 21.0.0 build
- NumPy: `1.26.4`
- OS: macOS 26.6.2 build 25G83; Darwin 25.6.0
- architecture: `arm64`
- byte order: little-endian
- `sys.platform`: `darwin`

`python3 ../ref/successor_ref.py --fixtures` exited 0, emitted no stderr, and produced 1,435 stdout bytes. Its stdout SHA-256 was `c82b2a253c4f55b9b4f28f697d496f8e8cbf5762771307c036ca77dd65950e25`; it was byte-for-byte equal to the pinned 1,435-byte fixture file. This attack held.

## Numbered findings

### 1. BLOCKER — Stage C's required fallback path cannot be called through the reference implementation

**Quote / symbol.** V5 §4 requires Stage C to use measured scalar `a_LB` **or `{a_LB_b}` (fallback)** on the sealed mask (V5 lines 113–117). The calibration rule selects fallback when the per-bin spread exceeds 0.03 (lines 143–145). But `stage_power(c_objects, a: float, stage, prefix, ...)` takes one scalar (reference lines 273–286), and `inject_trial()` evaluates the scalar expression `u2 < (1.0 - a)` (lines 258–270). It accepts neither per-object bins nor `{a_LB_b}`.

**Why this fails.** Executing the prose-required call with `a=np.array([.86,.88,.90])`, `stage=STAGE_C`, `prefix=0` failed immediately with:

`ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()`

The fallback is not an edge case; it is a predeclared admissible path. A run that passes every per-bin 0.85 floor but triggers spread fallback cannot fill BS-5f, so V5 is not executable over its declared outcome space.

**Minimal repair.** Add a frozen Stage-C API that takes the canonical bin index per accepted object and either a scalar accuracy or a validated per-bin vector, injects with `a_i=a_b[b_i]`, and carries the same address contract. Add scalar/fallback Stage-C fixtures including the spread-trigger boundary and a complete BS-5f receipt schema.

### 2. BLOCKER — one `n_eligible` argument cannot bind the raw ledger, retained selection leverage, and exact-mode boundary; the missing call site can admit a set below `L_plan`

**Quote / symbol.** V5 says BS-2o traverses raw eligible counts, while BS-5p and BS-2s threshold **retained** leverage (lines 62–83), and says exact mode is selected by the positive-count candidate-universe size (lines 75–80). `local_pass(brickid,c,n_eligible,order,l_plan)` and `exact_min_subset(...)` expose only one count vector (reference lines 134–178). The exact/local boundary is computed from positive entries of that same vector. No reference-code call site computes `retained_counts`, enforces `3*L_ret >= 100000`, scans ledger prefixes, fixes `L_min_plan/L_plan`, or passes retained counts to `local_pass`.

**Why this fails.** Passing the natural BS-2o `n_eligible` vector makes BS-2s threshold raw leverage, contrary to the prose; passing retained counts changes what “positive-count candidate universe” means and can switch the `N_EXACT=16` algorithm at the boundary. The code-as-definition clause does not resolve which call is the definition because there is no call.

A concrete seven-brick execution showed substantive admission failure:

- `c=[-0.4868224155944405,-0.8730927047630801,-0.3831733423895676,-0.01644607194273373,-0.8506728007144366,-0.2700354997649146,-0.5419268492467646]`
- raw `n=[16,9,14,6,1,2,12]`; retained `n=[13,7,12,5,0,1,10]`
- `L_plan=1.2927783953207417`
- raw-count call returned bricks `[1,2]`, reporting raw `L=1.314897551529874`, but that set's retained leverage is only `1.0611453924627055 < L_plan`
- retained-count call returned `[1,3]`, retained `L=2.140376739440442`

Thus the laziest natural call can produce a formally selected set that violates the stated binding threshold.

**Minimal repair.** Implement one frozen `build_plan(...)`/`select_final(...)` orchestrator with separate `n_raw` and `n_ret` inputs: raw counts determine the ledger and raw-positive boundary; retained counts determine every threshold, exact/subset SSE, Stage-P object expansion, `N_eq`, and re-pass. Return and digest all claimed receipt fields. Add the fixture above and a 17-raw-positive/16-retained-positive boundary fixture.

### 3. BLOCKER — Stage-C mask admissibility, canonical order, and real-label type are prose preconditions that the code cannot inspect or enforce

**Quote / symbol.** V5 §4 permits only the sealed accepted-position mask, canonically ordered by `(brickid,objid)`, and expressly bans uniform-sphere, parent-position, and non-mask inputs (lines 113–119). Yet `stage_power()` accepts only a bare `c_objects` vector and scalar `a`; it receives no brick IDs, object IDs, acceptance flags, calibration bins, mask digest, or input-kind tag. `perm_record()` likewise receives only `s,c` and merely says rows “must ALREADY be” canonical (reference lines 244–255). `beta_slope()` does not require `s in {-1,+1}`.

**Why this fails.** The reference body cannot distinguish the required sealed mask from the explicitly banned alternatives. Executed attacks:

- `stage_power(np.linspace(-1,1,20),.85,STAGE_C,0,n_trials=1000,n_perm=9)` accepted the bare inadmissible vector and returned `(0, False)` rather than rejecting its provenance/schema.
- `perm_record()` accepted non-sign labels `[0,2,0,2,0,2]` and returned finite `beta=0.42857142857142866`, `p=0.29`.
- Reversing 20 physically paired `(s,c)` rows under the same real-data address changed the observed slope in the last bit (`-0.10526315789473688` versus `-0.10526315789473684`), permutation p (`0.606` versus `0.588`), and payload digest (`df366c...b85085` versus `a31cc6...f11ba41`).

A prose promise that a future caller sorted and sourced the rows is not code enforcement, while §0 declares the code to be the mechanism. BS-5f and BS-7f can therefore be populated from an inadmissible or noncanonical input without any reference function failing closed.

**Minimal repair.** Define a typed canonical-mask constructor in the pinned code. It must validate equal lengths, unique `(brickid,objid)`, acceptance flags, finite pinned `c` bytes, valid calibration-bin labels, and `s in {-1,+1}` when signs are allowed; sort internally; bind a mask digest and input-kind/domain tag; and be the only accepted input to Stage C and the real permutation record.

### 4. BLOCKER — the calibration producer and covariance estimator do not exist in the code, and the joint allocation rule is not an executable algorithm

**Quote / symbol.** V5 §6 says the three accepted-object c-tertiles and 3×9 hand-check allocation algorithm are frozen in BS-8p, BS-2f seals boundaries, and BS-8f reports scalar/bin accuracies, lower bounds, and full `Cov_a` (lines 137–146). Section 0 says every operational mechanism and all estimators/sigmas are defined by code (lines 11–20). The code only **consumes** `a_b`, `bins`, and an already supplied covariance in `w_profile`, `w_gradient`, and `sigma_ours_profile` (reference lines 294–328). It has no tertile constructor, joint-cell allocator, HC-1H corrected-accuracy estimator, lower-bound producer, covariance constructor including shared synthetic error, or scalar/fallback adjudicator.

**Why this fails.** “Proportionally to cell counts, minimum 10 per non-empty cell” does not uniquely specify integer rounding, remainder assignment, behavior when minima exhaust the 500-real-label budget, tie handling at tertile boundaries, or the covariance between the three overlapping/shared-error estimates. Two lazy BS-8p implementations can satisfy the prose and produce different queues and `Cov_a`; the reference implementation provides no resolution. This leaves the V4 calibration findings unrepaired in substance even though the impossible pre-mask timing was moved to BS-2f.

**Minimal repair.** Put the complete boundary, allocation, HC estimator, full covariance, lower-bound, and path-adjudication algorithms in the pinned code, including tie/rounding/failure rules and HC-1H validity triggers. Add fixtures that reconstruct `Cov_a` from synthetic cell counts and shared-error inputs, not merely fixtures that consume an arbitrary covariance matrix.

### 5. BLOCKER — §0's “all digest serializations” and environment claims exceed the code; the determinism docstring is contradicted by a matrix call

**Quote / symbol.** V5 §0 declares all digest serializations code-defined and says every receipt records its environment (lines 11–23). The code defines generic `<f8`, `<i8`, SHA-256, and one ledger payload (reference lines 331–354). It defines no canonical composite payload/schema for the BS-2c manifest/count/c bytes, selected set, Stage-P/Stage-C records, accepted mask/boundaries, calibration fields/`Cov_a`, raw-index-plus-label reconstruction, environment, or final decision. No receipt writer records an environment.

The module docstring promises “scalar/1-D operations only (no BLAS matrix calls, no threading)” (reference lines 7–11), but `sigma_ours_profile()` executes `g @ (C @ g)` with a 2-D covariance matrix (line 327). The pinned fixture calls this path and prints its result, while the fixture environment line records only NumPy version and `sys.platform`.

**Why this fails.** Headerless scalar-array helpers do not define the claimed multi-field receipt schemas or bind a digest to its domain, shape, slot, environment, mask, and ordering. The same NumPy version plus `darwin` is not a matching computational environment for a BLAS-backed matrix operation; Python version, architecture, NumPy build/BLAS backend, and thread configuration are omitted. A fixture digest reproduced here, but the general determinism/environment claim is broader than that one machine match.

**Minimal repair.** Define domain-separated, length/shape-delimited canonical payloads for every digested slot and a canonical environment record; hash the complete receipt envelope or bind payload digest, schema version, slot, and environment together. Either replace the matrix expression with the promised frozen scalar reduction order or pin and record the actual NumPy/BLAS build and threading environment. Add cross-environment refusal/match tests.

### 6. BLOCKER — the blind-double rule withholds the only normative semantics needed to implement the double

**Quote / symbol.** Section 0 says code bodies are the definition whenever prose and code differ (V5 lines 11–20). Section 6 then requires a second implementation from the constitution plus only the reference code's **interface** — signatures, address scheme, and serialization schema — “without reading the reference code's bodies” (lines 155–160).

**Why this fails.** The interface does not reveal the body-defined evaluation order, conversions, branch order, exact/local boundary interpretation, prefix orchestration (which is absent entirely), or several missing schemas. The second author is forbidden to read the normative source while required to reproduce its exact integer/sequence and byte payloads. Docstrings are not enough: Finding 5 identifies a docstring/body contradiction, and Findings 1–4 identify mechanisms absent even from the interfaces. The register explicitly labels only BS-2o and BS-2s as blind-doubled; it provides no producer/time/receipt slot for blind-double agreement across Stage P/C, calibration, real permutation, sigmas, and verdict.

**Minimal repair.** Publish a complete independent normative algorithm/specification sufficient to implement every body without seeing it, and gate the reference against that spec; or drop the “bodies unread” rule and honestly call the second product a clean reimplementation/code review rather than a blind implementation. Add explicit P/E blind-double receipt slots for every claimed output class.

### 7. BLOCKER — the slot machine has unnamed producers and no executable final decision/lock slot

**Quote / symbol.** The preamble says each class-E slot is filled by its named producer (V5 lines 3–6), and the brief requires every P/E producer and chronology to exist. In §7, only BS-1 explicitly names Duho. BS-1b, BS-2c, BS-2o, BS-5p, BS-2s, BS-3, BS-9, BS-7p, BS-8p and all class-E slots name artifacts/fields but not accountable producers (lines 162–185). BS-7f ends with a permutation record “→ decision release”; it does not require a final `A_L`, sigma, floor, decision-region, disclosure-lock, or verdict receipt. The code has component functions but no function that applies §5 exhaustively and no primary-lock operation.

**Why this fails.** A slot cannot be checked for “producer exists” when no producer is named. More importantly, the step that turns the permutation/calibration fields into one outcome remains human prose exactly where the predecessor build spec warned a verdict must not be inferred by a person. The floor, scalar/fallback choice, sign, band, p gap, power/calibration halts, and `sigma_comb` are not assembled by any code symbol or receipted slot. There is also no slot that records the §6 blind-double STOP or primary lock before disclosure.

BS-9 does substantively carry the R1–R5 rerun and `nm_acquire_cutouts.py` prohibition, so that V4 repair held; the defect is the incomplete slot machine around it.

**Minimal repair.** Replace §7 with a machine-checkable table containing, for every slot: named accountable producer, exact inputs available at that time, canonical schema/digest, code symbol, predecessor/following block, and failure consequence. Add a code-defined `decide()` function and class-E verdict/primary-lock receipt after BS-7f and before disclosure; add blind-double agreement/STOP receipts.

### 8. BLOCKER — the frozen power algorithm is computationally unbounded for the required prefix scan at production scale

**Quote / symbol.** V5 requires `stage_power()` at every ascending ledger prefix until the smallest passing prefix is found (lines 66–73). The code performs 1,000 trials; each trial performs 100,000 full label permutations and recomputes a slope in a Python loop (reference lines 244–285): **100,000,000 permutations per prefix**.

**Why this fails.** A measured run on this recorded environment for `N=10,000`, `n_perm=1,000` took `0.098378125` seconds. Linear extrapolation of the exact nested kernel gives:

- at the mathematical retained-count lower bound `N>=33,334` implied by `3*L_ret>=100,000` and `L_ret<=N`, at least `3,333,400,000,000` label visits and about `32,793` seconds (9.11 hours) for **one prefix**;
- at `N=100,000`, `10,000,000,000,000` label visits and about `98,378` seconds (27.33 hours) for one prefix.

Those are hardware-specific extrapolations, not measured production runtimes, but they are enough to expose the missing bound: BS-5p asks for repeated full runs over ascending prefixes, potentially many thousands, with no batching, analytic equivalent, checkpoint contract, maximum prefix count, or compute ceiling. The fixture avoids `stage_power()` at production constants entirely. A freeze-candidate algorithm must be executable, not merely finite in principle.

**Minimal repair.** Replace the nested method with a statistically identical, independently validated bounded implementation (for example, a frozen exact/analytic permutation-tail computation if justified, or a vectorized/chunked algorithm with a proved equality contract), state resource/checkpoint/failure bounds, and run a production-scale benchmark before freezing. Any numerical or stochastic change must be newly defined and gated, not silently optimized after freeze.

## V4 finding-closure matrix (all 18 traced individually)

| V4 finding | V5 result |
|---|---|
| gpt56 F1 — class-P BS-7 consumes real statistic | **Closed:** BS-7p/BS-7f split and chronology are coherent. |
| gpt56 F2 — false minimization / small-case failure | **Partly closed, still blocked:** all five counterexamples are exact-mode fixtures and production minimality is retired; Finding 2 shows the raw/retained call seam and missing orchestrator can still violate `L_plan`. |
| gpt56 F3 — bin timing / fallback uncertainty | **Timing closed; substance blocked:** boundaries moved to BS-2f and gradient/full-covariance consumer exists, but Findings 1 and 4 show no fallback Stage C or covariance producer. |
| gpt56 F4 — RNG reset/API/order | **Address/API closed; order enforcement blocked:** immutable addresses and exact random calls are frozen, but Finding 3 shows canonical order is only a caller assertion and Stage C cannot validate its mask. |
| gpt56 F5 — count completeness / zero bricks | **Prose closed; executable closure blocked:** manifest/left join/zeros/anti-joins are stated and ledger excludes zeros; no code validates those proofs or serializes their receipt (Finding 5). |
| gpt56 F6 — float sequence / serialization | **Partly closed:** ledger operations and one payload are code-defined; missing schemas and the BLAS/environment contradiction remain (Finding 5). |
| gpt56 F7 — stale input-path receipts | **Closed:** BS-9 requires the release schema, production function/hash/layout, full R1–R5 rerun, replacement runner, and preserves the old-runner prohibition. |
| gpt56 F8 — void excludes §6 | **Closed:** the void now covers §§1–6, code, and slot register, with only mechanical E fills exempt. |
| codex F1 — local procedure / false minimization | **Partly closed, still blocked:** exact mode and weaker production claim repair the counterexample, but retained/raw execution is unresolved (Finding 2). |
| codex F2 — BS-7 timing | **Closed:** split into P declaration and E production record. |
| codex F3 — calibration producer timing | **Timing closed; implementation blocked:** BS-2f now owns numeric boundaries, but no code defines their production or allocation (Finding 4). |
| codex F4 — fallback uncertainty undefined | **Formula consumer added; end-to-end closure blocked:** analytic gradient/profile sigma exist, but full covariance production and fallback Stage C do not (Findings 1 and 4). |
| codex F5 — RNG lacks stage/prefix address | **Core address closed:** `(stage,prefix,trial,role)` is immutable; missing canonical/admissible call sites remain (Finding 3). |
| codex F6 — raw versus retained leverage | **Prose closed; executable seam blocked:** `L_ret` is named and thresholds bind it, but no code call assembles the chain and one argument conflates count roles (Finding 2). |
| codex F7 — exact order/digest under-specified | **Partly closed:** body bytes fix many float operations and binary helpers replace JSON; claimed all-schema/environment determinism remains false (Finding 5). |
| codex F8 — count oracle not footprint-complete | **Conceptually closed:** independent manifest, cardinality, dual anti-join and zero rows are required; code/receipt validation is absent (Finding 5). |
| codex F9 — void excludes §6 | **Closed.** |
| codex F10 — inventory arithmetic | **Closed:** independent parsing confirmed two 1,436-row versions, five known sizes per version, mean 1,236,552,768 bytes, and 1.775689774848 decimal TB per version. |

## Attacks that held

1. **Pinned fixture reproduction.** Exact byte match and exit 0 under the stated NumPy/platform pair.
2. **Five selector counterexamples.** V2, both V3, and both V4 fixtures return the frozen brute-force minimum sets under exact mode. `local_pass` delegates to that exact result for these small universes.
3. **Axis.** Independent standard Galactic-to-ICRS matrix rotation gave `[-0.6769717712714323,-0.5098465517777739,0.5308160835373523]`; component differences from `AXIS` were at most `3.331e-16`. Display coordinates were `(216.9844355052152°,32.060610901162°)`.
4. **CP threshold.** Independent SciPy evaluation gave one-sided lower bounds `0.9493659932051121` at x=961 and `0.950487129744074` at x=962; `CP_PASS_X=962` is correct.
5. **Quotation fidelity.** All eight BS6 predicates occur with matching operator/numeric content in V5 and BS6-pred; predicate 6's executable string is byte-identical. Longo amplitude, uncertainty, axis, sign convention, permutation count, p thresholds, 3.09 floor, 0.85 floor, retention 85.72%/0.8572, weight prefix and tau agree in substance with the pinned predecessor/source documents.
6. **Inventory.** The revised two-version/one-version-estimate sentence is arithmetically exact as stated.
7. **Void and BS-9.** The V4 omissions are repaired textually without weakening the old-runner prohibition.
8. **Non-finite permutation payload.** `perm_record` does reject non-finite permutation values. The Finding 3 attack is about finite non-sign labels and missing provenance/order enforcement, not this check.

## Evidence ledger

Read: the V5 brief; pinned V5 constitution, reference code and fixtures; both V4 gate reports; amended scope; V3-pred; BS6-pred; the cited footprint receipt, verdict-estimator build spec, HC-1H amendment, PC-1 input amendment, and sweep inventory. Executed: all custody hashes; exact fixture reproduction; independent source hashes; axis rotation; CP threshold; byte-substring quotation checks; inventory aggregation; fallback Stage-C call; inadmissible-mask call; non-sign real-label call; row-order reversal; raw/retained selector search and reproduction; and a permutation-kernel benchmark/extrapolation.

No `/Users/duhokim/NebulaMindData/` path was read. No source artifact was edited. The only review write is this report.

## Testimony

None. The runtime extrapolation in Finding 8 is explicitly labelled as an extrapolation from the measured kernel benchmark; no author assertion is used as evidence.

**REFUSED** — blockers: the declared fallback Stage-C path crashes; retained/raw selection semantics have no unambiguous call site and can admit a below-threshold set; Stage-C mask provenance, canonical order, and sign labels are unenforced; calibration/covariance production is absent; most claimed digest schemas and a sufficient environment contract do not exist; the blind-double rule withholds its normative body; the slot register lacks named producers and an executable final verdict/lock; and the required repeated power computation has no production-feasible bound.

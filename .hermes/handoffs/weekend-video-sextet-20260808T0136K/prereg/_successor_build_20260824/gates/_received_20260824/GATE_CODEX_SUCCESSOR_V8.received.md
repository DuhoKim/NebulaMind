# CODEX adversarial gate — successor preregistration V8

## Verdict

**REFUSED.** The three mandatory custody pins match, the 36-check fixture transcript reproduces byte-for-byte, and the real-geometry Stage-P rerun reproduces 997/1000 with 77/77 boundary confirmations. Those successes do not make V8 freeze-candidate grade. Multiple round-6 attacks still succeed, and the new real-geometry record was not produced by the frozen selection chain.

Most directly: BS-2m still accepts a self-consistent shortened parent and an invented one-brick effective universe padded to 366,912 rows while merely echoing the pinned digest string; against the actual pinned release brick table, the planner does not return either historical neighbour brick V8 says its fixtures replay. The reported 6,446-brick real selection is a greedy prefix, not `local_pass()` output: brick 155487 is immediately removable while retaining the target. Stage C's unsigned mask digest still cannot match the signed digest required by the production runner; a superficial five-key dictionary can impersonate a canonical Stage-C receipt; caller-chosen authorization bytes and `1/1` completeness plus a monkeypatched permutation producer yielded `REPRODUCED-LONGO`; and `perm_record(..., STAGE_REAL, n_perm=1)` still emits a production-shaped record. The HC-1H producer still has no nine-stratum population weights and still states the wrong boundary-tie rule. The release choice still accepts truthy strings, impossible dates, and a vacuous invariance function, with no availability probe. The receipt layer still discards values, accepts semantic nonsense, rejects valid false outcomes, and cannot round-trip into its consumers. The lapsed integrated power battery and five selector counterexamples remain absent.

## Custody pins — computed before review

`shasum -a 256` produced:

- `../PREREG_SUCCESSOR_DRAFT_V8_20260825.md` = `faea9047682e9de6dc7721bdf1f094f8c8947f0d35d9c455b46abdef292bcb39`
- `../ref/successor_ref_v4.py` = `979819048f59baef2773b448706e246edbb1f5de5a8180ac8ad3de2c15279d50`
- `../ref/FIXTURES_V4_20260825.out` = `70268cf5b325834ca8486101d69e2dc77b51f50aeb2ac018faa118248d5599eb`

All three equal the brief's required values. Review proceeded.

Binding-source pins independently recomputed:

- `../../SUCCESSOR_SCOPE_20260821.md` = `995b2e729a3362f0445cac9d5da6d290fddac9f8018e75f2c0aa87c190c93de7`
- `../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` = `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- `../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md` = `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`
- `../../VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md` = `43b9a6a843ef08a6528f1132db2bee29000c5ecd3def2a3a03c23f672c81cec7`
- `../../LANA_BS5_LONGO_SIGN_20260814.md` = `b7c32dcf12d9e147e5dee6a8262d925b61011615f2ee1d75d687600abb0a72ca`

Current real-artifact pins computed by this gate (the V8 brief supplied no expected values for these):

- `../real/REAL_GEOMETRY_RESULT_20260825.md` = `3288c25907d2ec5151b4eca7991f21cf4cb85e52f38ce9887f95e58cdb190242`
- `../real/build_real_oracle.py` = `e668a126d3d8691d7dcbfe2e298c3709a210c92727640077266ab1ff36de7330`
- `../real/greedy_fast.py` = `8c22a37d83ae13f938ef3b0036a94e6d731bb0cd9b9c181e9df543ab841983cb`
- `../real/run_real_selection.py` = `20a5de675746bd76ba275e3f868834f1c34980a479e069842f4bb7656b69ffae`
- `../real/rerun_real_power_v4.py` = `83f5d650c30ac00e6bd9aeff5871e236426a6df827f1ae3dab8eb1ff25d6efe2`
- `../real/real_oracle_dr10.npz` = `01b8b4ecd7da6dc31654881ea4ea6713b0c06464c752d1e7e4de0028cce2103a`
- `../real/real_selection_dr10.npz` = `f220fed7aeb660150259e8c0026a0d373d5665aa4af5639e4cd65fbc1eaaba57`

## Environment and mandatory executions

- executable: `/Library/Developer/CommandLineTools/usr/bin/python3`
- CPython 3.9.6, Clang 21.0.0
- NumPy 1.26.4
- macOS 26.6.2, arm64, little-endian
- command: `python3 -B ../ref/successor_ref_v4.py --fixtures`
- fixture exit 0; stderr 0 bytes; stdout 4,091 bytes
- fixture stdout SHA-256 `70268cf5b325834ca8486101d69e2dc77b51f50aeb2ac018faa118248d5599eb`
- fixture stdout byte-equal to `FIXTURES_V4_20260825.out`
- independent real-power command: `python3 -B ../real/rerun_real_power_v4.py`
- real-power exit 0 in 640 s; `997/1000`, boundary `77`, confirmed `77`, refuted `0`, script verdict `PASS`

## Numbered findings

### 1. BLOCKER — BS-2m still trusts both witnesses, and its actual planner fails the two named historical replays

**Quote / symbol.** V8 §2.4 says the release universe is bound to digest `863e5ded…` and cardinality 366,912, the parent is bound by the BS-2s receipt, and the fixtures replay the two historical edge objects (`V8:110-137,354-362`; `successor_ref_v4.py:257-324`).

**Executed caller-trust attack.** I built a `brick_table` with one effective rectangle named `home` and 366,911 irrelevant padding rectangles, for exactly 366,912 rows. I supplied the pinned universe digest string without hashing that table. I used a one-object parent, recomputed its digest, and supplied the bare dictionary `{'slot':'BS-2s','parent_digest': <that digest>}`. `close_manifest()` accepted a one-brick manifest:

`objects=1 required_count=1 manifest_count=1 missing_count=0 extra_count=0 universe_bricks=366912`.

The body only compares `universe_sha256` to a constant and `len(brick_table)` to 366,912 (`266-274`); it never hashes or parses the table whose geometry it uses. It likewise checks only two caller-authored dictionary fields for `selection_receipt` (`275-282`). The canonical BS-2s schema does not even contain `parent_digest`, and `receipt()` discards all field values, so an honest canonical BS-2s receipt cannot provide the value this consumer demands.

**Actual edge replay attack.** I parsed the pinned real `survey-bricks-dr10-south.fits.gz` into the planner's rectangle schema and used the object IDs and coordinates embedded in V4's own fixture. For `10997315463551936`, the planner returned only `3385m885`, not the claimed required `3471m885`. For `10995116744378804`, it returned only `2894m872`, not `2857m870`. The synthetic fixture pads `_grid_bricks()` and checks only that some synthetic neighbour exists; it never checks either historical brickname. Thus V8's statement that the fixtures “replay this exact shape and report the two bricknames” is false.

The zero-half-size public seam is closed in `close_manifest()`, the derived half-size is now the correct `0.004657777777777778°`, duplicate manifests refuse, and the `(350°,10°)` wrap rectangle now returns correctly. Those repairs do not close the witness or real-edge defects.

**Why it blocks.** The exact 60,308-versus-60,310 class remains executable: a lazy producer can self-author the parent receipt, attach the known digest string to an unrelated cardinality-matched universe, and ship a short manifest. The planner also fails the only two concrete historical examples V8 says certify the repair.

**Minimal repair.** Make BS-2m consume the actual release-universe artifact bytes/path, recompute the SHA-256 internally, parse those exact bytes internally, and verify a typed/decoded BS-2s envelope whose parent value survives serialization and whose envelope hash is checked. Add a fixture against the actual pinned universe and the two independently pinned parent rows that requires `3471m885` and `2857m870`, or correct the historical property if those names are not geometric neighbours under the 128-pixel contract. Synthetic grid neighbours are not a replay.

### 2. BLOCKER — the reported real selection is not the frozen selection algorithm

**Quote / symbol.** V8 says `build_plan()` performs oracle → complete greedy ledger → Stage-P-derived `L_min_plan` → `L_plan=1.2 L_min_plan` → `local_pass()`, followed by a final Stage-P re-pass (`V8:87-108`). It then reports the real selection as 6,446 bricks, 65,062 raw objects and `N_eq=120,006` under the frozen requirement (`146-165`).

**Code evidence.** `run_real_selection.py` does not call `build_plan()` or `local_pass()`. It sets `L_REQ=NEQ_MIN/3`, calls `greedy_prefix(..., L_REQ)`, then calls `greedy_prefix(..., 1.2*L_REQ)` and saves that prefix (`run_real_selection.py:18-53`). It never measures `L_min_plan`, never applies the bounded local reduction, and never runs the final Stage-P re-pass. `run_real_power.py`/`rerun_real_power_v4.py` test only the saved shortcut result.

**Executed counterexample on the real selection.** The saved 6,446-brick prefix has retained `L=40001.92676862697`. Removing its first accepted brick, BRICKID `155487` (raw count 2, retained count 1), leaves `L=40000.95993917921`, still above the exact target 40,000. Therefore `local_pass()` would remove it immediately; the reported 6,446-brick set cannot be the frozen algorithm's output. The saved set's audited values themselves reproduce: raw 65,062, retained 53,006, Var 0.7546679012, `N_eq=120005.7803`.

The vectorized greedy order withstood 5,000 additional random/tie-heavy comparisons and three explicit tie/zero cases against pinned V4 with zero mismatches; the V3 and V4 `greedy_ledger()` source bodies are byte-identical. That failed attack supports the fast greedy prefix. It does not make a prefix equal to the later `local_pass()` output.

**Why it blocks.** The Stage-P `997/1000` result is for a set that the constitution would not freeze. Its result does not certify the corrected local-pass output, and no BS-5p-derived `L_min_plan` was produced. This is separate from the disclosed fact that the pinned O(n²) greedy does not scale.

**Minimal repair.** Implement and pin a scalable, blind-doubled equivalent of the entire frozen chain, not only the greedy prefix: complete ledger identity, Stage-P first-passing prefix, exact `L_min_plan`, margin, `local_pass()` including removals/swaps, and final-set re-pass. Pin the real input/output/script digests in the receipt and rerun Stage P on that exact final set.

### 3. BLOCKER — the 10× confirmation band is not a power-equality contract

**Quote / symbol.** V8 says every calibrated success “within 10× of the decision threshold” is confirmed and that one refutation fails the stage (`V8:211-236`; `stage_power:701-737`). The real rerun reports 997 calibrated successes, of which only 77 were inside the band.

**Code evidence and recomputation.** Confirmation occurs only when `0.0001 <= p_calibrated < 0.001` (`724-725`). A calibrated success with `p_calibrated < 0.0001` is declared safe without any independent test. Thus 920 of the real run's 997 successes were not confirmed. There is no theorem or simultaneous error budget showing that sign-multiset mismatch or a low shared 20,000-permutation reference cannot move one of those trials across the full-permutation threshold. `PWR-Z-STABLE` still accepts a 35% tail-mass spread under an arbitrary `<50%` rule and says the retained 1% deflation “absorbs it” (`fixture output:18`), despite V8's statement that the repair is not a larger fudge factor.

The “full” confirmation itself is only 20,000 permutations, not production's 100,000. At a true tail probability 0.001, a 20,000-permutation plus-one test passes with probability `P[Binom(20000,0.001) <= 19] = 0.4702128`. The chance of falling into the unconfirmed `p_cal < 0.0001` region is small but nonzero: `P[X<=1]=4.2894e-8` at one boundary trial, about `4.2893e-5` over 1,000 independent trials. More importantly, the shared reference and sign-multiset shift are common-mode, so the independent-trial calculation is not a guarantee. The one-sided 95% Clopper–Pearson lower bound for 77/77 confirmations is 0.96184; it does not certify the 920 untested successes.

I reran the fixture's calibrated-versus-5,000-permutation family: 22 calibrated successes, one full-MC failure (`skewed-1500`, trial 8, `p_cal=0.00074996`, `p_mc=0.00119976`), which the current band would catch. That is a useful failed attack on the band for this one case, not a proof about all cases outside it.

**Why it blocks.** The Stage-P PASS remains based on 997 calibrated classifications, not 997 full-MC classifications or a proved conservative bound. The band can miss an unsafe success by construction because no check runs outside it. The real result is exactly reproducible, but the equality claim is stronger than its check.

**Minimal repair.** Confirm every counted success at 100,000 permutations, or establish a finite-sample simultaneous upper bound covering the shared reference-null uncertainty and every admissible sign multiset, then count successes only under that worst-case bound. If a band is retained, prove that outside-band calibrated p-values cannot cross 0.001 under the bound; “10×” is not self-justifying.

### 4. BLOCKER — Stage-C chronology and production custody remain broken; reduced-count and monkeypatch paths still produce records/verdicts

**Quote / symbol.** V8 says Stage C occurs before unblinding on a sealed accepted-position mask, the Stage-C receipt binds the exact mask digest, and `run_production_verdict()` is the only production verdict path (`V8:193-201,238-276`; code `621-638,701-737,1051-1085`).

**Unsigned/signed chronology.** On a legitimate 120,000-row `SealedMask`, the unsigned digest was `4eb4f892…d14a`; adding signs changed it to `099cb050…846a`, because the digest binds `signs_present` and `s` (`539-546`). Stage C must run before signs exist, but the production runner requires signs and compares the Stage-C `mask_digest` to the signed digest (`1059-1065`). An honest pre-unblinding Stage-C receipt therefore cannot match the later signed mask.

**Reduced-count attack.** `perm_record(signed_sealed, STAGE_REAL, ..., n_perm=1)` returned a numeric beta, a one-element vector and `p=0.5`. `perm_record()` is explicitly documented as the production record but still exposes `n_perm` (`621-638`). `stage_power()` likewise exposes `n_trials` and `confirm_perm`; no fixed-count `run_stage_c()` producer exists.

**Self-asserted evidence / monkeypatch attack.** I used an arbitrary `/tmp` text file while supplying its own matching SHA, `n_receipts=n_parent=1` for a 120,000-row mask, and a dictionary containing only `slot`, `schema`, a nonempty fake `envelope_sha256`, `mask_digest`, and `passed=True`. The runner never recomputes the receipt body/envelope. After replacing mutable global `perm_record` with a one-row fabricated producer, `run_production_verdict()` returned `REPRODUCED-LONGO` and claimed `n_perm=100000`. The V8 fixtures still check only that mutable global names appear in `co_names`; they do not pin their bodies.

The Stage-C fixture-type attack is repaired: `stage_power(FixtureMask, STAGE_C, ...)` now refuses. Calibration ordering is also repaired: `adjudicate_path()` occurs before `perm_record()`. Those held attacks do not rescue custody.

**Why it blocks.** The honest receipt chronology is impossible, while a fabricated receipt is accepted. A generic production-record symbol can run at one permutation, and the only verdict runner can advertise 100,000 after consuming a monkeypatched one-row vector. Caller-equal counts and caller-supplied authorization hashes remain assertions, not custody.

**Minimal repair.** Split an immutable position/mask digest from the sign-bearing result digest; bind BS-5f to the former and BS-7f to both. Add sealed, fixed-count `run_stage_c()` and `run_bs7f()` entry points. Decode and recompute canonical envelopes, verify predecessor digests and cardinalities against the actual mask, and run from a hash-verified standalone entry point whose guard/statistic bodies cannot be replaced after verification. Pin the authorization identity externally rather than accepting caller-chosen bytes plus caller-chosen hash.

### 5. BLOCKER — HC-1H population weighting and the tie rule are still not implemented

**Quote / symbol.** V8 claims the inherited nine-stratum HC-1H estimator, 3×9 allocation, population logic, fixed 500-real-label budget and an implemented tie rule (`V8:285-300`; `allocate_handcheck:838-903`; `accuracy_from_handcheck:906-949`). V3-pred requires per-stratum correction followed by `a = Σ w_s a_s` with population weights (`V3-pred:279-303`).

**Executed attacks.** `accuracy_from_handcheck()` accepted vectors of lengths 2, 3 and 27 and returned correspondingly sized outputs. Its signature has no stratum populations or weights, and its scalar `a_hat` is the pooled agreement rate corrected by epsilon (`941-946`), not the required population-weighted nine-stratum estimate. It cannot carry synthetic/repeat identities or HC-7 integrity triggers.

The docstring says `side='left'` sends equality to the higher bin, but `assign_bins([0,1],[0,1])` returned `[0,1]`; equality to the first boundary lands in bin 0, the lower bin. The all-tied refusal fixture does not test a nondegenerate boundary equality.

The former feasible-allocation attack is repaired: the sparse 3×9 witness with a 500-label budget now allocated exactly 500, respected capacities, and met all stratum floors. This is positive evidence for the headroom repair. The public `budget` choice remains exposed, and the estimator consuming the allocation remains absent.

**Why it blocks.** Calibration controls attenuation, covariance, scalar/profile choice, Stage C and the pre-unblinding halt. A pooled three-bin statistic can differ materially from a population-weighted nine-stratum statistic, and boundary-tied objects are assigned opposite to the promised rule.

**Minimal repair.** Consume typed 3×9 realized records plus nine frozen population counts/weights and integrity roles; compute per-stratum corrected estimates and aggregate exactly as HC-1H specifies into the three calibration-bin products and full covariance. Remove the production budget override. Choose `side='right'` if equality truly belongs to the higher bin, or correct the prose, and test every nondegenerate boundary with repeated equal values.

### 6. BLOCKER — the release choice is still a caller assertion and its invariance test is still vacuous

**Quote / symbol.** V8 calls the Sep-5 choice bound and machine-checkable (`V8:59-76`; `resolve_branch:1128-1160`).

**Executed attacks.** `resolve_branch('false','2026-09-01')` selected Branch A because a nonempty string is truthy. `resolve_branch(False,'2026-99-99')` selected Branch B; `resolve_branch(True,'2026-02-30')` selected Branch A. The date check validates separators and lexicographic order, not a calendar date. No availability-probe producer exists in V4. The function still receives the availability result as a caller argument.

`branch_invariance(lambda cfg: {'constant':1})` returned `invariant=True`; the fixture uses the same strategy by ignoring `cfg` (`1536-1539`). A real artifact that records the allowed branch-specific path/version provenance necessarily differs under a whole-output digest comparison.

The early-Branch-B and late-Branch-A checks for actual Booleans/date-shaped strings are repaired. However, the receipt layer rejects a valid Branch-B `photoz_available=False` as an “empty payload,” so the claimed canonical Branch-B receipt cannot be emitted.

**Why it blocks.** The Sep-5 fact does not slot into a verified choice point: type-invalid and impossible-date assertions pass, no probe is pinned, and the invariance fixture rewards not consuming the configuration.

**Minimal repair.** Pin a fail-closed availability probe and its raw response/timestamp/error policy; require `type(photoz_available) is bool`; parse a real calendar date and enforce the exact resolution event. Compare normalized execution traces/code/schema digests after removing only enumerated branch path/version fields, while requiring those differing provenance fields to be present and typed.

### 7. BLOCKER — the slot machine still cannot carry values into consumers

**Quote / symbol.** V8 §10 says `SLOT_SCHEMA` covers all 16 slots and `receipt()` refuses empty payloads (`V8:322-350,391-410`; code `137-176`).

**Executed attacks and code evidence.** There are 18 named slots, not 16. `receipt('BS-5f', ...)` returns only `slot`, `schema`, `environment`, `body_sha256` and `envelope_sha256`; it discards `successes`, `n_trials`, `passed` and `mask_digest`. Consequently the canonical producer cannot feed the runner, which requires direct `passed` and `mask_digest` values. A BS-2c receipt with every field equal to the byte `b'x'` passed with a valid envelope hash despite carrying no decodable arrays, integers, totals or cross-slot bindings. A valid `photoz_available=False` and `passed=False` are rejected as empty. The schema identifier is still `successor_ref_v3/1` inside V4.

The prose register still omits the promised input/schema columns; class E omits code symbols entirely. It points at nonexistent `validate_count_oracle`, `ledger_digest`, `manifest_closure`, `require_manifest_closure`, and `decide`. BS-2m's schema omits the promised missing/extra brickname lists and universe digest. BS-8f omits `sigma_epsilon` and integrity triggers. BS-2s omits the parent digest its next consumer requires.

I do not count the three items §10 openly leaves unfinished — clean-room normative spec, BS-9 release-specific input schema, and BS-V primary lock — as new findings. The blocker is the rest of the slot layer that §10 claims closed.

**Why it blocks.** Receipts are hashes of uninterpreted caller bytes, not typed values. Fail outcomes cannot be represented, consumers cannot decode honest envelopes, and ad hoc dictionaries can impersonate them.

**Minimal repair.** Define canonical typed encodings and decoders for every slot, preserve or decode field values, recompute body and envelope hashes at every consumer, reject semantic nonsense, and support false/zero values explicitly. Add producer→serialize→decode→consumer and tamper fixtures for every edge. Replace §7 with the promised dependency/input/schema/symbol/block register using actual symbols.

### 8. BLOCKER — the count-oracle completeness proof is still self-referential, including in the real receipt

**Quote / symbol.** V8 says the count table is left-joined onto an independently enumerated universe, zero rows are materialized, and grouped/ungrouped disagreement refuses (`V8:89-97`; code `339-377`).

**Independent real-data reproduction.** The two named source digests match the receipt. The CSV has 270,577 rows, 270,577 unique keys, no negative counts and sum 832,393. The universe has 366,912 unique bricks. The left join yields exactly 270,577 positive rows, 96,335 zeros, zero outside keys and total 832,393. Recomputed count-weighted `Var(cosθ)=0.445201346160`. The saved oracle NPZ is byte-array-equal to this independent reconstruction. Those claims hold.

**Proof defect.** `build_real_oracle.py` passes `grouped_sum=int(n_elig.sum())` and `ungrouped_total=int(n_elig.sum())` — the same value derived from the same left-joined array (`69-72`). It does not run or consume an independent ungrouped query. `validate_count_table()` therefore proves an integer equals itself. Likewise `build_plan()` syntactically requires the three keywords but accepts all three as explicit `None`; after monkeypatching mutable `stage_power`, `build_plan(..., universe_brickid=None, grouped_sum=None, ungrouped_total=None, n_trials=1)` returned a selected set and passing re-pass.

The real receipt pins only the two upstream files in prose, not the generated NPZs or scripts, and the V8 constitution hard-codes their digest strings rather than consuming verified artifacts.

**Why it blocks.** The real numbers are true for the bytes inspected, but the claimed independent grouped/ungrouped closure and production enforcement are not. A shared query-scope omission can still drop a nonzero group while all supplied totals agree.

**Minimal repair.** Consume and pin raw grouped rows/query text plus a separately produced ungrouped count with independently specified scope/partition; derive zero rows inside the validator; prohibit `None` in the production path; and bind source/query/output/script digests in typed BS-2c/BS-2o receipts.

### 9. BLOCKER — the validation battery and selector counterexamples remain materially missing

**Quote / symbol.** V8 says the lapsed battery is carried at its named boundaries and all five adversarial selector counterexamples are fixtures (`V8:104-107,266-276`; build spec `66-77`).

The new `BATTERY-FLOOR-EDGE` is present and correctly refuses a just-below-floor synthetic value. The old omissions remain: `BATTERY-NEQ` computes only `n_eq_small < NEQ_MIN`; it does not call `run_production_verdict()` or assert an actual `INCONCLUSIVE-BY-POWER` result (`1513-1518`). `BATTERY-POS` uses `explore_verdict()` and a normal-tail p-value, bypassing authorization, completeness, receipt, mask-provenance and 100,000-permutation integration (`1471-1495`). No `SEL-A` through `SEL-E` fixture or equivalent named five-case replay exists anywhere in V4 or its transcript.

**Why it blocks.** V8's repair trace responds to only the floor-edge limb of the round-6 battery finding while claiming the union closed. Reduced-N and integrated-runner regressions remain untested, and the five selection cases are still asserted rather than executed.

**Minimal repair.** Add an actual underpowered sealed geometry through the production-equivalent fixed runner and assert no permutation producer call plus the receipted outcome. Add a positive full integration fixture at fixed count. Restore all five exact selector counterexamples with expected sets/counts in the pinned output.

### 10. MAJOR — §8's inherited-defect inventory remains incomplete and overstates closure

The amended scope separately names monopole leakage (“Project the monopole out”) and the one-sided/two-sided harness seam (`SUCCESSOR_SCOPE:46-56`). Neither appears in V8 §8's eight-item inventory, exactly as in V7.

The closure statuses are also overstated: manifest-versus-parent remains open (Finding 1); footprint-blind power remains open as custody/equality (Findings 3-4); attenuation remains open at the HC-1H producer (Finding 5); unreachable significance remains open through generic reduced `n_perm` and battery paths (Findings 4 and 9); count-based selection is not the real executed selection (Finding 2); and verdict-by-human-reading points to nonexistent `decide()` while the slot/lock path is incomplete (Finding 7 plus the disclosed BS-V lock).

The centred estimator does close the named full-sky-normalization/monopole body defect, and the one-sided comparisons are consistent in the current code. That is why the two omitted items are an inventory defect rather than two additional body blockers.

**Minimal repair.** Add monopole leakage and sidedness as named inherited defects with exact code/fixture evidence. Mark every partially repaired item open until its producer, receipt and consumer form one executable path.

## Complete slot walk

### Class P

- **BS-1:** resolver/date/probe and false-value receipt are blocked by Findings 6-7.
- **BS-1b:** schema names exist but no typed values/consumer or availability-derived binding exists (Finding 7).
- **BS-2c:** real left join and numbers hold; independent total/query custody and mandatory production enforcement do not (Finding 8).
- **BS-2o:** pinned ledger body and fast prefix agree under expanded tests; `ledger_digest` is nonexistent and real script does not emit a canonical value-carrying receipt (Findings 2 and 7).
- **BS-5p:** real Stage-P rerun reproduces, but equality contract and actual first-passing-prefix derivation are absent (Findings 2-3).
- **BS-2s:** real artifact is a removable greedy prefix, not `local_pass()` output; parent digest required by BS-2m is absent from the schema (Findings 1-2 and 7).
- **BS-2m:** caller-trust and historical-edge attacks succeed (Finding 1).
- **BS-3:** constants are available pre-image; receipt values are not decodable (Finding 7).
- **BS-9:** R1-R5 rerun and runner prohibition remain correctly named but openly unfinished; not counted anew.
- **BS-4:** sign direction and synthetic anchor are coherent, but `decide` is nonexistent and receipt values are not consumable (Finding 7).
- **BS-7p:** environment and byte-pinned fixture transcript exist; battery fidelity remains blocked (Finding 9).
- **BS-8p:** allocator headroom attack is repaired; full HC-1H producer/weights/tie contract is not (Finding 5).

No class-P slot inherently needs post-freeze χ. Several still cannot emit the artifact V8 says they emit.

### Class E

- **BS-6:** chronology is coherent; its schema remains uninterpreted bytes.
- **BS-2f:** type/bin checks improved, but direct-constructor provenance and unsigned/signed identity are unresolved (Finding 4).
- **BS-8f:** epsilon arithmetic and covariance term hold; nine-stratum population weighting and integrity fields are absent (Finding 5).
- **BS-5f:** fixture type now refuses, but no fixed-count producer exists and the canonical receipt cannot bind/round-trip the correct digest (Findings 4 and 7).
- **BS-7f:** honest runner hard-codes 100,000, but generic `STAGE_REAL` accepts one permutation and mutable/global custody remains open (Finding 4).
- **BS-V:** pure decision helper exists, but the named `decide` does not and the primary lock is openly unfinished (Finding 7; disclosed lock not counted anew).

## Quotation/source fidelity and attacks that held

1. The arXiv API/PDF independently confirm Michael J. Longo, the title, 15,158 spirals, redshift `<0.085`, amplitude `−0.0408±0.011`, chance probability `7.9×10⁻4`, axis approximately `(l,b)=(52°,68.5°)`, arXiv:1104.2815 and DOI `10.1016/j.physletb.2011.04.008`. Crossref independently confirms DOI, author, journal, volume 699 and pages 224–229. The exact ADS locator is `2011PhLB..699..224L`.
2. Sign mapping is internally and externally consistent. Longo defines `(R−L)/(R+L)` and reports a negative amplitude toward the left-excess axis. The project defines positive χ for Longo-Left/CCW, so the same effect becomes `+0.0408`. V8 and V4 keep `A_LONGO_PUBLISHED_SIGNED=-0.0408` and `A_LONGO=+0.0408`. No inversion found.
3. All eight §2.2 predicates occur in V8 and BS6-pred with matching executable/numeric content; the ellipticity expression is byte-identical. The no-surface-brightness-cut disclosure is preserved.
4. Exact exhaustive permutation checks over 18 N/sign-balance cases gave maximum formula-versus-enumeration sd discrepancy `1.11e-16`. The exact-variance claim holds.
5. Static AST checks found zero matrix-multiply nodes, zero `.spawn` attributes, zero `.binomial` attributes and exactly two `rng.random()` calls in `inject_signs()`. The scalar double-loop no-BLAS body remains.
6. The cutout half-size derivation and wrap-rectangle repair hold. The real historical edge contract does not (Finding 1).
7. The formerly rejected feasible HC allocation now succeeds with exact budget/capacity/floor compliance. The full estimator remains open (Finding 5).
8. The real upstream file digests, left join, zeros, total, Var(cosθ), selected-set summary and exact 997/1000 + 77/77 rerun all reproduce. Their interpretation as frozen-chain/equality evidence is blocked by Findings 2-3 and 8.
9. V8 preserves writing-only authority in its preamble. This gate performed only the briefed verification on already-scoped artifacts and synthetic/permutation code; it fetched no study data, image or χ and authorized no run/freeze/publication.

## Inherited-defect closure matrix

1. **Manifest-versus-parent gap — OPEN.** Self-authored parent/universe witnesses and the historical-edge failure remain (Finding 1).
2. **Footprint-blind power — OPEN as a full contract.** Real geometry is used, but the set is not the frozen set and power equality/custody fail (Findings 2-4).
3. **Full-sky normalization constant — CLOSED for the named body defect.** `beta_slope()` is centred; no `3·D` decision path found.
4. **Attenuation-versus-target mismatch — OPEN at HC-1H production.** β/A separation exists; population-weighted calibration does not (Finding 5).
5. **Unreachable significance threshold — PARTLY CLOSED.** The honest runner fixes 100,000; generic `STAGE_REAL` and validation paths permit reduced/incomplete evidence (Findings 4 and 9).
6. **Silent axis divergence — CLOSED for the pinned reference.** One axis constant is used; citation/sign/axis anchors held.
7. **Count stopping on ordered brick IDs — OPEN in the executed real path.** Contiguous selection is absent, but the real set bypasses the frozen local procedure (Finding 2).
8. **Verdict by human reading — OPEN as an end-to-end path.** A pure helper/runner exists; receipt custody and primary lock do not (Findings 4 and 7).

Known omitted inherited items: monopole leakage and sidedness seam (Finding 10).

## Testimony

- V8 labels `Cov(β̂,â)=0` and the profile analogue as Testimony. I did not accept them as proved or use them to rescue any finding.
- The real receipt's numeric claims were independently recomputed where possible, including the full 640-second Stage-P rerun. Its assertion that the fast path is “proven” order-identical is stronger than 40 random cases; my 5,000 additional cases and source-body comparison found no mismatch, but neither constitutes proof at all 270,577 production rows.
- I did not read `/Users/duhokim/NebulaMindData/`. The two historical object positions used for the planner attack are the coordinates V4 itself associates with the named IDs; no hidden parent row was consulted.
- The 77/77 confirmations are real and reproducible. Finding 3 is about what that audit does not check, not an allegation that any observed confirmation was fabricated or false.
- The drafting-time DR11 photo-z status was not re-fetched and is not a verdict premise.

## Evidence ledger and custody boundary

Read: the V8 brief; the three pinned V8 artifacts; both V7 gate reports; amended scope; V3-pred; BS6-pred; lapsed build spec; predecessor sign receipt; real receipt; every script and generated NPZ under `../real/`.

Executed: mandatory/source/real hashes; exact fixture reproduction; full real Stage-P rerun; shortened-parent/cardinality-padded fake-universe/short-manifest closure attack; actual-release historical-edge and wrap planner probes; unsigned/signed digest comparison; Stage-REAL `n_perm=1`; superficial Stage-C receipt plus self-supplied authorization/completeness and monkeypatched permutation verdict; build-plan `None` proofs plus monkeypatched Stage P; HC shape/tie/feasible-allocation probes; branch type/date/vacuous-invariance probes; receipt nonsense/false-outcome/round-trip probes; real CSV/FITS left-join/variance/NPZ reconstruction; real-selection single-removal test; 5,000 greedy-equivalence stress cases plus explicit ties; exact variance enumeration; calibrated/full-MC fixture comparison; AST body checks; cut-string checks; and external Longo/Crossref source checks.

No source artifact was edited. No study-data fetch, image access, χ access, authorization, freeze, publication, git mutation or execution approval occurred. The only gate-directory write by this CODEX review is this report.

## Sources

[1] https://export.arxiv.org/api/query?id_list=1104.2815 — arXiv record 1104.2815

[2] https://arxiv.org/pdf/1104.2815 — Longo 2011 full text

[3] https://api.crossref.org/works/10.1016/j.physletb.2011.04.008 — Crossref DOI record

[4] https://ui.adsabs.harvard.edu/abs/2011PhLB..699..224L/abstract — NASA ADS bibcode locator

**REFUSED**

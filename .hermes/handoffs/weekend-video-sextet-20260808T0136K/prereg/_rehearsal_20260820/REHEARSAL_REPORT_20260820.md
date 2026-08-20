# GPT1 end-to-end rehearsal — synthetic galaxies only

Status: **PASS_COMPLETE_CHAIN_SYNTHETIC_ONLY**

## Headline

- Objects: 20,000 frozen-BS-3 synthetic galaxies; zero real chirality labels.
- Natural deterministic synthetic campaign: the first 20,000 BS-3 draws; no stratum engineering or candidate screening.
- Primary chi direct-sign accuracy: 99.085000%; inverted-sign accuracy: 0.915000%; zero chi: 0.
- Observed sign convention: chi > 0 corresponds to BS-3 truth_sign +1 (direct convention).
- HC-1H preparation: HC1H_PREPARED_AND_COMMITTED_BEFORE_CHECKING; blinded items: 850; sealed-key envelope present: True; no labels submitted.
- Independent verification: PASS_INDEPENDENT_REHEARSAL_VERIFICATION (101,726 checks).
- End-to-end wall clock: 662.404 s (33.120 s per 1,000 objects).

## Frozen identities and safety boundary

- `LANA_ONE_HUMAN_ATTENUATION_20260814.md`: `b2590e4213e225f9869fe782cfe0f55d8d8979dcb470752836a5cd31a58453fd`
- `committee`: `64fceff7c79b18303692a945c92dc25a44780e8cf9ee3e62e17eb4054e627bf5`
- `committee_weights`: `6e4a6efaf9e9db55e8ca23f1ffa7e61ef437c62bc959c9630b90db0d18aeff0a`
- `cutout_runner`: `ccb9b8fed457333669e54fa9f0a3dac645dc866a56c6cd8dc665ffd4d93b1bcc`
- `frozen_bs3_generator`: `89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75`
- `hc1h_harness`: `cc88fa5ee6e7d7f2ab32ad4b7b0d7d843f9a77ed777c11d259755197eda03bbc`
- `inference_runner`: `16ed3e256ea4fe045ff553036e7f397e7ad07884212d5da663e61f2246c57b45`
- `primary_weights`: `83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d`
- Every tensor and image path supplied to the gated programs resolves inside this rehearsal directory.
- No path under `/Users/duhokim/NebulaMindData/` was supplied, enumerated, opened, or read. Transfer receipts were not needed.
- No network call was made.

## Tensor generation and writer equivalence

- Frozen generator domain: `GPT1-END-TO-END-REHEARSAL-20260820`.
- Campaign: the first 20,000 deterministic BS-3 draws under the frozen domain; no preselection.
- Generated tensor count: 20,000.
- Layout verification: 20,000/20,000 are exactly `(1,128,128)`, `<f4`, C-order, 65,536 bytes.
- Writer byte-equivalence: 20,000/20,000 outputs equal direct frozen-generator little-endian float32 bytes.
- Materialization used the unmodified cutout runner's `apply_input_contract` followed by its `_atomic_bytes` writer; IC-5 is the hash-pinned identity map (gain 1, offset 0).

## Primary inference and sign recovery

- Processed: 20,000; resumed: 0.
- Correct direct sign: 19,817/20,000.
- Correct inverted sign: 183/20,000.
- Positive/negative/zero chi: 9,993/10,007/0.

## Independent machine committee pass

- `AGREE_CONFIDENT`: 18,139 (90.695%)
- `DISAGREE`: 806 (4.030%)
- `LOW_CONFIDENCE`: 1,055 (5.275%)
- Committee state agreement with the metadata emitted by the inference runner: 20,000/20,000.

## Nine strata and HC-1H Neyman allocation

The tertile axis is global rank in `abs(chi)`, matching the active HC-1H harness. Priors are synthetic truth-versus-primary-sign agreement rates with Jeffreys 1/2 smoothing, `(correct+0.5)/(N_s+1)`, because exact empirical 0/1 rates make the active allocator's information weight zero. The allocator itself is the unmodified HC-1H `allocate_neyman` implementation: constrained `N_s sqrt(a_s(1-a_s))`, floor 30, capacity caps, deterministic largest-remainder closure, total 500.

| committee state | |chi| tertile | population | synthetic prior | allocation | below population floor 30? | allocation below 30? |
|---|---:|---:|---:|---:|---|---|
| agree-confident | 0 | 5759 | 0.97248264 | 260 | no | no |
| agree-confident | 1 | 5932 | 0.99991573 | 30 | no | no |
| agree-confident | 2 | 6448 | 0.99992247 | 30 | no | no |
| disagree | 0 | 451 | 0.96128319 | 30 | no | no |
| disagree | 1 | 279 | 0.99821429 | 30 | no | no |
| disagree | 2 | 76 | 0.99350649 | 30 | no | no |
| low-confidence | 0 | 457 | 0.98144105 | 30 | no | no |
| low-confidence | 1 | 456 | 0.99890591 | 30 | no | no |
| low-confidence | 2 | 142 | 0.99650350 | 30 | no | no |

Population strata below 30: 0. Allocation strata below 30: 0. Allocation sum: 500.

At N=208,407, scaling the observed N=20,000 stratum fractions gives a smallest projected stratum of 791.9. Therefore the allocator's population floor check WOULD PASS at 208,407 under the observed population mix (all nine projected populations exceed 30). This is a projection, not a read of real data.

The optional pilot requires exactly 90 real labels: 10 in each of the nine strata. It only needs each stratum population to support 10 and cannot estimate the final attenuation. The full design requires 500 real labels with a hard floor of 30 per stratum; its remaining 230 labels are assigned by constrained Neyman allocation. The 200 synthetic injections and 150 repeats are additional labels in the full 850-label stream.

## HC-1H harness acceptance

- CLI prepare exit code: 0.
- Harness receipt status: `HC1H_PREPARED_AND_COMMITTED_BEFORE_CHECKING`.
- Blinded checker package items: 850 (500 selected synthetic-as-real inputs + 200 blind injections + 150 mirrored repeats).
- Checker session status after initialization: `ACTIVE`; completed labels: 0.
- Durable answer/session ledger present before any checker event: False (the active harness creates `answers.jsonl` only with the first checker event).
- Sealed envelope SHA-256: `483ac84acd99a024af17816e252eb95b4ddd4d093b790c6448a7512fc3ec1cc2`.
- Public commitment SHA-256: `4a2e01407752f9c183898063e49ba8101c97d48db604a44f958452acaaaac15a`.
- The key was not unsealed and no C/W label was submitted. This rehearsal proves preparation/session acceptance only.

## Wall-clock cost

| phase | seconds | seconds per 1,000 campaign objects |
|---|---:|---:|
| generation_writer_png | 30.978 | 1.549 |
| inference | 606.156 | 30.308 |
| committee | 22.350 | 1.117 |
| strata_inputs | 0.245 | 0.012 |
| hc1h_prepare_session | 2.585 | 0.129 |
| total | 662.404 | 33.120 |

The HC-1H preparation has a fixed 850-item cost, so its per-1,000 figure is a mechanical normalization, not a scaling law. The generation/inference/committee figures are the useful linear projection inputs.

## Interface mismatches and workarounds

1. **HC-1H session persistence before first label** — Constructing CheckerApplication returns an ACTIVE blinded state but does not persist answers.jsonl/SESSION_STARTED until the first checker event. Workaround: Verified the ACTIVE zero-completed state, package, control binding, commitment, and sealed envelope without manufacturing a C/W answer; reported the absence of a durable session ledger explicitly. Real-run implication: If pre-label durable session creation is required for operational custody, add a dedicated start-session event/entry point before the real run.
2. **Natural BS-3 population versus HC-1H floor** — The first natural N=2,000 draw produced populations 28, 8, and 11 in three cells, so the frozen floor of 30 correctly made full preparation impossible. Workaround: Preserved that failed attempt and reran the natural deterministic campaign at N=20,000, with no preselection or stratum engineering. Real-run implication: The real accepted population cannot be engineered this way; if any real cell has N_s<30, HC-1H is infeasible and must hold or receive a preregistered sparse-cell rule before any labels.
3. **Python environment split** — The frozen torch venv lacked Pillow, cryptography, and astropy, while the system Python had those packages but lacked torch. Workaround: Ran the torch venv interpreter with the existing user-site package directory on PYTHONPATH; no install and no network. Real-run implication: The production command needs one hash-locked environment containing every gated program's dependencies.
4. **Inference CLI input transport** — The runner accepts every tensor as a separate --inputs argument and has no manifest/stdin mode; 20,000 absolute paths exceed a safe CLI transport size and the real campaign would certainly exceed it. Workaround: Called the unmodified gated run_paths API with the complete ordered Path list. Real-run implication: Add a hash-bound manifest input mode before the real campaign without changing inference semantics.
5. **Committee program entry point** — committee.py has no campaign CLI and does not itself load its frozen member-B weights. Workaround: Loaded its hash-pinned SmallPlainCNN weights and called its unmodified scoring/state functions in a separate post-inference pass, then cross-checked every state against inference metadata. Real-run implication: Provide a gated batch entry point or formally designate inference receipts as the committee campaign product.
6. **HC-1H image versus tensor contract** — Inference consumes raw 65,536-byte float32 tensors, but HC-1H requires Pillow-readable image_path assets and cannot ingest those tensors. Workaround: Created deterministic 128x128 grayscale PNG sidecars from each exact tensor using fixed percentile display scaling; tensor inference bytes remained untouched. Real-run implication: Freeze the real tensor-to-checker rendering map and bind each PNG to its source tensor hash before the real hand-check.
7. **Neyman priors at perfect/near-perfect synthetic recovery** — The HC-1H allocator refuses when every empirical prior is exactly 0 or 1 because all information weights become zero; finite synthetic strata can hit that boundary. Workaround: Used an explicit Jeffreys-smoothed synthetic estimate (correct+0.5)/(N_s+1), then passed it to the unmodified constrained allocator. Real-run implication: Freeze the prior estimator/smoothing rule before production rather than selecting it after seeing synthetic outcomes.
8. **Committee state vocabulary** — The committee emits uppercase underscore states, while HC-1H accepts lowercase hyphenated states only. Workaround: Applied the explicit bijection AGREE_CONFIDENT→agree-confident, DISAGREE→disagree, LOW_CONFIDENCE→low-confidence. Real-run implication: Freeze one canonical vocabulary or a hash-pinned adapter.
9. **HC-1H campaign role naming** — The harness calls its 500-row input real_population even when data_class is synthetic, and separately requires another synthetic_pool for injections. Workaround: Used the 20,000-object synthetic campaign as a synthetic-class accepted population and a separately identified view of the same generated assets as an injection pool; no claim of independent science samples is made. Real-run implication: Production must supply genuinely separate accepted real population and blind-injection pool, with identity-disjointness policy made explicit.

## Artifact map

- `committee_ledger`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/committee_results.jsonl`
- `hc1h_checker_package`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/hc1h_checking/checker_H/package.json`
- `hc1h_prepare_stdout`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/hc1h_prepare.stdout.log`
- `hc1h_sealed_key`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/hc1h_private/sealed_key.nmhc`
- `independent_verification`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/independent_verification.json`
- `inference_ledger`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/inference/results.jsonl`
- `neyman_priors`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/hc1h_neyman_priors.json`
- `real_population_input`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/hc1h_real_population.jsonl`
- `report`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/REHEARSAL_REPORT_20260820.md`
- `summary`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/rehearsal_summary.json`
- `synthetic_pool_input`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/hc1h_synthetic_pool.jsonl`
- `truth_manifest`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/synthetic_truth.jsonl`

No acceptance, freeze, real-data run, human measurement, reduction, publication, database action, deploy, commit, or push is authorized by this rehearsal.

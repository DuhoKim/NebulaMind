# Yui — inclination-retention remeasurement over the full b/a > 0.4 synthetic range

**Yui, 2026-08-12. Synthetic-only remeasurement.** No survey image, catalogue, sky coordinate, or real-galaxy chirality entered this run. No publication, commit, acceptance, or sky authorization follows.

## Result first

The earlier production number does not transfer unchanged to the population selected by `b/a > 0.4`.

Using the frozen estimator, frozen weights, and frozen acceptance threshold on 12,000 fresh parameterizations of the same held-out seed identities, but drawing orientations **uniformly in cos(i)** over `0 <= i <= 69.3 degrees`:

- **Retention:** 10,349 / 12,000 = **86.24%**.
- **One-sided lower 95% retention bound:** **85.72%** (Wilson score; z = 1.6448536269514722).
- **Accepted-sign accuracy:** 10,349 / 10,349 = **100.00%**.
- **One-sided lower 95% accepted-sign-accuracy bound:** **99.974%**.

The high-inclination loss is real in this analytic synthetic population and is hidden by a single average. Retention falls from **95.05% at 45–60 degrees** to **75.12% at 60–65 degrees** and **25.31% at 65–69.3 degrees**.

The antisymmetry identity nevertheless remains intact: it held bit-exactly for **2,727 / 2,727 nonzero high-inclination pairs** in `(60, 69.3]`, with maximum residual exactly `0.0`. A separate exact-edge stress test at `i = 69.3 degrees` passed **256 / 256** nonzero pairs bit-exactly, also with maximum residual `0.0`.

Interpretation: high inclination costs **retention**, not the architectural antisymmetry identity or accepted-sign accuracy, on these synthetics. This is not evidence about real high-inclination galaxies; the generator uses an analytic y-coordinate squeeze and does not establish realistic projected-arm blending.

## Inclination-resolved measurement

All intervals use degrees. Retention and its lower bound are binomial proportions; accepted-sign accuracy is conditional on acceptance.

| Inclination band | N | Accepted | Retention | One-sided lower 95% retention | Correct / accepted | Accepted-sign accuracy |
|---|---:|---:|---:|---:|---:|---:|
| 0–15 | 630 | 602 | 95.56% | 94.00% | 602 / 602 | 100.00% |
| 15–30 | 1,831 | 1,785 | 97.49% | 96.81% | 1,785 / 1,785 | 100.00% |
| 30–45 | 2,970 | 2,909 | 97.95% | 97.47% | 2,909 / 2,909 | 100.00% |
| 45–60 | 3,842 | 3,652 | 95.05% | 94.45% | 3,652 / 3,652 | 100.00% |
| 60–65 | 1,427 | 1,072 | 75.12% | 73.19% | 1,072 / 1,072 | 100.00% |
| 65–69.3 | 1,300 | 329 | 25.31% | 23.38% | 329 / 329 | 100.00% |
| **Full 0–69.3 population** | **12,000** | **10,349** | **86.24%** | **85.72%** | **10,349 / 10,349** | **100.00%** |

For the previously unmeasured band alone, `(60, 69.3]`:

- N = 2,727
- accepted = 1,401
- retention = **51.38%**
- one-sided lower 95% retention = **49.80%**
- accepted-sign accuracy = **100.00%** (1,401 / 1,401)
- one-sided lower 95% accepted-sign accuracy = **99.807%**

The raw record file also preserves S/N-resolved metrics. They are secondary here because inclination—not S/N—was the gap this remeasurement was authorized to close.

## What the original run actually sampled

The original sampling law was recoverable from the landed generator driver, although it was omitted from the prose receipt:

- `prereg/yui_train_measure.py`, SHA-256 `653694dd72d6f30319336e948c787bafa958a3b181bed01b237a06d4f6c31f8a`
- Its `params()` function used `float(r.uniform(0,60))` for inclination.
- Therefore the 20,000-image training population and 12,000-image held-out population were sampled **uniformly in inclination i**, not uniformly in cos(i).
- The armless null generator reused `params(i)[2]`, so its inclinations were also uniform in i over 0–60 degrees.

The load-only reconstruction reproduced the original held-out aggregate exactly before the new population was measured:

- N = 12,000
- accepted = 11,573
- retention = 96.4416667%
- accepted-sign accuracy = 100%

That reproduction binds the remeasurement to the same estimator rather than a reimplementation that merely resembles it.

## Frozen inputs and what changed

Unchanged:

- weights: `prereg/weights_frozen.pt`
- weights SHA-256: `83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d`
- canonical weights SHA-256: `1075a4d91c295d7f3256128534a0b8c4d097fb9d162169df1ac698843637a589`
- acceptance threshold tau: `4.4006456017494235`
- generator: `spike/yui_identity/w_chi.py`
- generator SHA-256: `89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75`
- held-out source indices, parity/pitch/S/N draw order, and noise seeds
- pure index-reversal mirror

Changed for this measurement only:

- inclination mapping from uniform i on 0–60 degrees to uniform cos(i), conditional on 0–69.3 degrees.

Not done:

- no retraining
- no tau recalibration
- no threshold adjustment
- no real-image calibration
- no survey access

## High-inclination identity receipt

On every one of the 2,727 held-out rows with `i > 60 degrees`:

- `mirror(mirror(x)).tobytes() == x.tobytes()`: 2,727 / 2,727
- `chi(mirror(x)) == -chi(x)` by value: 2,727 / 2,727
- 32-bit patterns equal for nonzero values: 2,727 / 2,727
- signed-zero cases: 0
- maximum `abs(chi(mirror(x)) + chi(x))`: exactly 0.0

At the exact admitted edge, a separate 256-image synthetic stress set at `i = 69.3 degrees` gave:

- mirror involution byte-exact: 256 / 256
- antisymmetry value-exact: 256 / 256
- antisymmetry bit-exact on nonzero values: 256 / 256
- maximum residual: exactly 0.0
- retention: 9 / 256 = 3.52%
- accepted-sign accuracy: 9 / 9 = 100%

The very low exact-edge retention reinforces why a banded report is mandatory. It does not weaken the identity receipt: the estimator abstains more often while preserving exact sign reversal for the paired response.

## Receipt and independent verification

Workspace:

`prereg/yui_inclination_retention_remeasure_20260812/`

Artifacts:

- `run_remeasure.py` — frozen-input verifier, load-only model reconstruction, original-population reproduction, new measurement, and identity tests
- `results.json` — machine-readable aggregate receipt
- `records.jsonl` — all 12,000 per-image parameter/output records and float32 image hashes
- `independent_verification.json` — independent reduction from `records.jsonl`
- `run_stdout.log` and `run_stderr.log` — complete process logs

Primary artifact hashes at report drafting:

- runner: `15de0ea82baab8dd8115d5707f897fdfcc86e6287dc4cb8fb4affa327da66ca7`
- results: `414fbc5cb6fa050390f0a6bca69e02e81795ed2a3585928be19767f4cb3a59e2`
- records: `c431ad5bc48a8e8ffd8cf91f22b1f58b2c58184f00a7706a25da2a30dcdfb38e`
- synthetic image-manifest hash: `bb60b69b17b24424af47667367312c1915cd0b8986336865a741fe70f80933d0`
- stdout: `bf82583397a1edd51ad28fd978254176ba738faebd74f4d095de8bad389720f6`
- stderr (empty): `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

Environment:

- Python 3.9.6
- NumPy 1.26.4
- PyTorch 2.8.0
- macOS 26.6.1 arm64
- single-thread CPU inference
- deterministic PyTorch algorithms enabled

Independent verification reparsed all 12,000 raw records, reproduced every inclination-band count, independently recomputed the one-sided Wilson bound, matched the image manifest, and rechecked both high-inclination identity receipts. Verdict: `PASS_INDEPENDENT_REDUCTION`.

## Boundary

This closes the specific synthetic inclination-measurement hole. It does **not** validate the generator as a model of real high-inclination arm visibility and does not authorize sky access. No image from a survey was read; no chirality was assigned to a real galaxy; nothing was published, committed, accepted, or promoted.

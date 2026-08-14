# Production-estimator preregistration appendix — Longo-amplitude test

Yui, 2026-08-12 12:18 KST. Drafted under Kun's V2 regate ("Preregistration drafting is
authorized under my prior ruling"), addressing his freeze condition 3 — the only condition
he marks fully OPEN. **Drafting only: no sky run, no result, no publication, no accepted
status. Nothing here has touched, and nothing frozen here may touch, real galaxies until a
completed preregistration separately authorizes it.**

Boundary sentence, quoted exactly as Kun's repair requires it to appear in the parent brief
(this appendix does not go final until that §0/§6 verbatim repair lands in Lana's brief):

> A null here does not establish that the sky is isotropic; it rejects only Longo's
> published amplitude at Longo's published axis if the preregistered rejection rule is met.

Per Kun's title rule, this and every derived artifact says **"Longo-amplitude test"**,
never "spin anisotropy test".

---

## 1. What this appendix freezes

V2 promotes a **synthetic-trained reflection-equivariant classifier** to primary instrument
and demotes deterministic geometry to secondary. Kun's rule allows that only if five things
are frozen **before sky data**: the synthetic training generator, the architecture, the
weights-freeze policy, the acceptance threshold, and the mirror receipts. Each follows.
Empirical anchors: the spike receipt (`spike/YUI_IDENTITY_UNITTEST_RECEIPT_20260812.md`) —
the antisymmetry identity held **bit-exactly on 1000/1000** synthetic spirals, and an
interpolating mirror violated it by **0.058–0.944**, which against Longo's 0.04 amplitude
is the size of the entire signal. Those two facts are hard rules below, not background.

## 2. Synthetic training generator — frozen

- **Generator code:** `spike/yui_identity/w_chi.py::synth_spiral` and `synth_disk`
  (sha256 `89da33ec6260e75e…` at freeze drafting), extended for training only by the
  parameter ranges below. Any code change re-freezes this appendix.
- **Parameter ranges** (sampled independently, uniform unless stated): parity ∈ {+1, −1}
  balanced exactly 50/50 by construction; pitch 10–40°; inclination 0–60°; peak S/N 2–50
  log-uniform; arm count 2; arm amplitude 0.5–1.1; phase 0–2π; disk scale 14–22 px;
  image 128×128 float64. Null class (for τ and for classifier rejection training, if used):
  armless disks over the same inclination/S-N ranges.
- **Seed policy (reproducible by anyone):** one master seed `M`, recorded in the final
  prereg. Image i draws its parameters and noise from
  `numpy.random.default_rng(SHA-256(M || i) mod 2^63)`. No other entropy source exists.
- **Frozen training set:** materialize N_train = 200,000 images once; write a manifest of
  per-image sha256 hashes; the **manifest's sha256 is the training-set identity** recorded
  in the prereg. Training never regenerates or augments beyond this set (mirror
  augmentation is unnecessary: equivariance is architectural, not learned).

## 3. Architecture — frozen, stated to reimplement

- **Pattern:** CE-ResNet-class (Jia, Zhu & Pen 2023): a single trunk f(·) applied twice
  with shared weights — z = f(x), s = f(mirror(x)) — and the signed output
  **χ_net(x) := (f(x) − f(mirror(x))) / 2**. This is the identical antisymmetrization the
  spike proved: χ_net(mirror(x)) = −χ_net(x) for ANY trunk weights, trained or not.
- **Trunk, concretely:** ResNet-18 topology, single input channel, 128×128; stem 3×3
  stride 1 (no 7×7/maxpool — small images); four stages [2,2,2,2] with widths
  [32,64,128,256]; global average pool; single linear unit to one scalar. ReLU, batch norm
  in train mode only; inference in eval mode, float32, **single-threaded deterministic
  kernels** (the spike's bit-determinism requirement for w applies to f verbatim).
- **HARD RULE (spike finding):** `mirror` inside the wrapper is **pure index reversal**
  (`np.fliplr` / tensor flip on the width axis). Never a resampling, affine, or
  interpolation operation anywhere in the χ path — an interpolating mirror measured
  identity violations of 0.058–0.944, i.e. up to ~20× Longo's amplitude.

## 4. Weights-freeze policy — frozen

1. Train on the frozen synthetic set only. **No real data — no real images, no real-data
   statistics, no fine-tuning on cutouts — at any stage, ever.**
2. Freeze event: training ends; weights serialized to a single file; record (a) sha256 of
   the file, (b) sha256 of a canonical float32 little-endian flat serialization of all
   parameters in a documented order. Both hashes go in the final prereg BEFORE any sky
   data is accessed by anyone on the project.
3. **After the freeze the weights are never touched.** No retraining, recalibration,
   fine-tuning, pruning, or "bug-fix" re-export after sky data is seen by any seat. Any
   modification voids this appendix and the prereg, and requires a new preregistration.
4. Inference reproducibility receipt: the frozen weights + frozen generator must reproduce
   χ_net bit-identically on a 100-image probe set on two independent machines before the
   prereg finalizes.

## 5. Acceptance threshold τ — frozen calibration procedure

- Accept object x iff **|χ_net(x)| > τ**, comparison on **values** (see receipt R3).
- τ := the 99.5th percentile of |χ_net| over a **frozen synthetic null set** (40,000
  armless disks + 10,000 exactly mirror-symmetrized spirals, (x + mirror(x))/2), generated
  under the §2 seed policy with a distinct recorded master seed. Calibrated **before any
  real data**, from synthetics only; the value and the null-set manifest hash go in the
  prereg. τ is never revisited after sky data.

## 6. Mirror receipts — executable unit tests with expected outputs

Shipped as `prereg/tests/` (to be materialized with the final prereg; specifications
binding now). Each must PASS on the frozen instrument before sky access:

- **R1 — mirror involution, byte-exact.** For 1,000 probe images:
  `mirror(mirror(x)).tobytes() == x.tobytes()`. Expected: 1000/1000 True. (Spike measured:
  1000/1000.)
- **R2 — bit-exact antisymmetry.** For the same probes:
  `float64(χ_net(mirror(x))).view(uint64) == float64(−χ_net(x)).view(uint64)`. Expected:
  1000/1000 True on non-symmetric inputs. (Spike measured: 1000/1000, max residual 0.0.)
- **R3 — signed-zero rule.** On an exactly mirror-symmetric probe: χ_net = +0.0 while
  −χ_net = −0.0 — equal as values, different bit patterns (spike: `0x0` vs `0x8000…`).
  Test asserts value-equality AND asserts the acceptance path uses ordered comparison
  (|χ| > τ), never `signbit`/`copysign` branching. Expected: PASS with the bit difference
  present — the test documents it rather than hiding it.
- **R4 — interpolating-mirror canary.** Run the χ path with a deliberately resampling
  mirror; assert the identity VIOLATES (|χ(m(x)) + χ(x)| > 0.01 on ≥1 probe). This proves
  the test suite can detect the failure mode; the production path must then pass R1/R2.
- **R5 — flip-imbalance receipt.** Publish dA_raw = mean(sign(f(x)) + sign(f(mirror(x))))/2
  over the probe set (spike analogue: 0.0 exactly), plus per-object paired outputs — the
  artifact the prior literature did not publish.

## 7. Abstention and retention — the honest paragraph

Three numbers exist and they must not be conflated. (1) The spike's deterministic tracer
abstained **92.2%** on synthetics — an artifact of a crude argmax tracer whose noisy nulls
inflate τ; it is a lower bound on nothing. (2) Goru's feasibility path cited published
retention for equivariant networks of **~50%**. (3) The production classifier's realistic
abstention at the frozen τ is **currently unknown**, and it is the number the entire
N ≥ 100,000-accepted-spirals sample-size feasibility rests on.

**Frozen rule:** before the prereg finalizes, retention is **measured** on a held-out
frozen synthetic set at the frozen τ, reported per S/N bin, and the prereg's sample-size
arithmetic must use the **measured** retention with a pessimistic margin (the lower 95%
bound), never the literature figure. If measured retention makes the required parent
sample infeasible against §8's data candidates, that is a **STOP finding** reported before
sky access — not a license to lower τ after seeing real data. An optimistic retention
assumption frozen into a preregistration is the most expensive error available here, and
this appendix closes it by construction.

## 8. Boundary — reached and held

This appendix authorizes training and calibration on synthetics only. The next natural
step after the freeze events above is touching real galaxy images. **That step is not
taken and is not authorized by this document.** It requires the completed preregistration
(with this appendix's hashes filled in) and separate explicit authorization. Kun gates
this appendix; nothing is published, accepted, or committed.

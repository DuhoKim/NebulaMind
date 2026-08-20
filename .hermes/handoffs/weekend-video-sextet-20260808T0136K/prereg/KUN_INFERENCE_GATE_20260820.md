PASS_INFERENCE_BUILD

Kun inference gate, kimi gate seat (Nous route), fresh one-shot, 2026-08-20. Build gated:
`_inference_20260820/` (runner `inference_runner.py`, sha256 16ed3e256ea4fe045ff553036e7f397e7ad07884212d5da663e61f2246c57b45 per build receipt; method: local files, grep, python3 in the lane venv). All checks below are my own executions or direct code/ledger reads, not builder claims. Findings-only.

## GATE ITEM ONE — the K-8 boundary: HELD

(a) No path into the real tensor root. `grep -rn "cutouts_dr10_south" _inference_20260820/` returns exactly three hits: the guard constant `REAL_TENSOR_ROOT` at inference_runner.py:31, and the build's own receipt/log lines that merely name the root to assert it was untouched. No code path opens, lists, hashes, or infers from that directory. I ran the build's refusals live (below) and additionally spied `pathlib.Path.open` during a refusal: zero opens of the real tree.

(b) Real-data refusal is genuine and I tested it myself:
- CLI pointed at real tensor `/Users/duhokim/NebulaMindData/cutouts_dr10_south/tensors/object-0016cbe6f3ee4533.f32le`, no authorization: exit 2, `REFUSED_REAL_DATA_UNAUTHORIZED`, and the output directory was never even created.
- Same invocation with `--synthetic` flag: still exit 2 — a path under the real root is real regardless of the flag (guard_input_scope, inference_runner.py:162-166). 
- With a bogus `--authorization` file: exit 2, `REFUSED_AUTHORIZATION_SHA256` — the authorization file's SHA-256 is verified against the pinned 05fc06dd…4664a before any input open (verify_authorization, lines 146-159; run_paths validates it once before model load and before any input access, lines 350-352).
- Open-spy test: `read_ic6_tensor` on the real path with Path.open monkey-patched to record calls — refused with zero opens of anything under the real root.
- The build's own tests (which I re-ran, 11/11 OK) also cover refusal-before-open, wrong-auth-hash, and the symlink bypass (`_is_within` uses resolve(strict=False) without opening the target).

(c) No real object id in any results ledger. `synthetic_validation/outputs/results.jsonl` has exactly 1000 rows; every `object_id` matches `synthetic-NNNN-<hash16>`; zero non-synthetic ids; no RA/Dec/brick/DR10-like strings. A grep of all 1000 per-object receipts for "object-" returns nothing. The input fixture directory from the build's validation run is absent (inputs were cleaned after the run), consistent with synthetic-only scope.

## The instrument

(1) Weights hash verified at load, refusal on mismatch — VERIFIED. Gate-pinned sha256 83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d matches both the runner constant (line 26) and my independent `shasum -a 256 weights_frozen.pt`. I corrupted a copy one byte: `load_frozen_model` raised `REFUSED_WEIGHTS_SHA256` with torch.load never called (hash checked before deserialization). Clean load lands eval mode, float32, CPU, all requires_grad False; threads=1, interop=1, deterministic algorithms on, mkldnn disabled.

(2) Architecture matches YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md exactly — VERIFIED by module introspection, quoted beside the code:
- Appendix §3: "a single trunk f(·) applied twice with shared weights — χ_net(x) := (f(x) − f(mirror(x))) / 2". Code (chi_tensor, lines 197-203): one loaded `FrozenTrunk` object called twice in one expression, `(model(image) - model(torch.flip(image, dims=[3]))) / 2.0`. One model instance, shared weights by construction.
- Appendix §3: "ResNet-18 topology, single input channel, 128×128; stem 3×3 stride 1 (no 7×7/maxpool — small images); four stages [2,2,2,2] with widths [32,64,128,256]; global average pool; single linear unit to one scalar." Measured: stem Conv2d(1→32, 3×3, stride 1); exactly 8 BasicBlocks with (in,out,stride) = (32,32,1),(32,32,1),(32,64,2),(64,64,1),(64,128,2),(128,128,1),(128,256,2),(256,256,1) — i.e. stages [2,2,2,2], widths [32,64,128,256]; zero MaxPool2d, zero 7×7 convs; one AdaptiveAvgPool2d(1); one Linear(256→1); forward on (1,1,128,128) returns scalar shape (1,). 2,794,721 params.
- Appendix §3: "inference in eval mode, float32, single-threaded deterministic kernels." Measured live: training=False, dtype float32, threads=1, interop=1, deterministic=True, mkldnn off (configure_deterministic_runtime, lines 58-69, also executed at import line 435). chi_tensor hard-refuses if the model is in train mode (line 198-199).

(3) Mirror is PURE index reversal — VERIFIED. `grep -E "flip|interp|resampl|affine|grid_sample|rotate|warp"` over runner + validator + tests returns exactly two hits, both `torch.flip` (mirror_tensor line 194, chi_tensor line 203). No interpolation, resampling, or affine anywhere in the chi path — matching the appendix's HARD RULE (§3: "pure index reversal … Never a resampling, affine, or interpolation operation anywhere in the χ path"). Involution measured 200/200 and 1000/1000 (build receipt).

(4) HARD RULE identity, rerun by me on a FRESH seeded 200 synthetics: PASS. Fresh domain `KUN-GATE-REGATE-20260820-FRESH-SEED`, 200 samples: chi_bits(mirror(x)) == negated_float32_bits(chi_bits(x)) (sign-bit XOR, bit-exact) for 200/200; mirror involution 200/200. The build's own 1000-sample validation reports the same 1000/1000.

(5) Determinism — VERIFIED twice over. Same tensor twice in-process: 200/200 identical bits (mine), 1000/1000 (build). Multiprocessing: my own spawn-context 4-worker probe (written to a file after an initial stdin-respawn harness mistake on my side, not a build defect) — indices 7 and 123 each bit-identical across all 4 workers, antisymmetry held in every worker, each worker at threads=1 deterministic=True. Build receipt's mp probe (index 37, 4 workers) agrees.

(6) Input layout matches the cutout runner's writer byte-for-byte — VERIFIED. Writer (_cutout_runner_20260820/cutout_runner.py:242,349): `np.array(scaled, dtype=np.dtype("<f4"), order="C", copy=True).reshape(TENSOR_SHAPE)` then `tensor.tobytes(order="C")` → `<base>.f32le`. Reader (inference_runner.py:33-35,169-188): exactly 65,536 bytes, `np.frombuffer(..., dtype="<f4").reshape((1,128,128)).copy(order="C")` with C-contiguous and dtype postconditions. My round-trip of writer-style bytes through `read_ic6_tensor`: identical bytes, matching sha256. The build's contract test does the same comparison and passes.

(7) Committee output is stratification metadata only and never enters chi — PROVEN by code path. AST scan of mirror_tensor, chi_tensor, chi_bits, float32_bits, negated_float32_bits, bits_to_float32: zero references to committee/Committee/classify. `Committee.classify(self, image)` has no chi parameter; its result dict contains only member scores/signs/state. In run_paths, `chi_bits` (line 376) is computed from model+tensor alone before `committee.classify` (line 378) is called; committee output lands only in receipt/ledger metadata fields. Committee code and member-B weights are themselves SHA-pinned and verified at load (both hashes match my independent shasum).

Boundary receipt (SYNTHETIC_VALIDATION_RECEIPT_20260820.json) claims status PASS with all nine checks true; my independent reruns confirm each of them. No repairs required.

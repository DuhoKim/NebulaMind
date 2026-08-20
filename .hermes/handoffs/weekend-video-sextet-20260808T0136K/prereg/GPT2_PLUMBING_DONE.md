GPT2_PLUMBING_COMPLETE

# GPT2 plumbing completion receipt

- F2 ENVIRONMENT SPLIT — PASS. Added explicit stage launchers and `RUN_ENVIRONMENTS.md`. Torch-only stages use `venv_torch/bin/python`; cutout, display, and HC-1H stages use `/usr/bin/python3`. No package install or mixed `PYTHONPATH` is used. No stage needs both torch and Pillow.
- F3 INFERENCE CLI INPUT TRANSPORT — PASS. Added mutually exclusive `--input-manifest FILE` support for UTF-8 one-path-per-line or a JSON path list; legacy `--inputs` remains supported and reaches the same ordered `run_paths` path. The manifest loader passed the required 20,000-path test.
- F4 COMMITTEE ENTRY POINT — PASS. Added a batch CLI that reads a tensor manifest, verifies member-B weights against SHA-256 `6e4a6efaf9e9db55e8ca23f1ffa7e61ef437c62bc959c9630b90db0d18aeff0a` before `torch.load`, scores each IC-6 tensor with the unchanged scoring functions, and atomically writes per-object JSONL state.
- F5 TENSOR-VS-IMAGE CONTRACT — PASS. Added display-only transform `DISPLAY-LIN-NEG1-POS1-V1`: exact `<f4` C-order `(1,128,128)` input; finite values only; fixed clip `[-1,+1]`; byte `floor((clip(x)+1)*127.5+0.5)`; Pillow `L` 128x128 C-order PNG; no metadata, `optimize=False`, `compress_level=9`; no per-image normalization. Tensor and PNG SHA-256 bindings are emitted. Repeated rendering passed byte-identity testing. PNGs are explicitly forbidden as chi inputs.
- F7 STATE VOCABULARY — PASS. Added the single shared `committee_state_vocabulary.py` bijection. Committee and HC-1H import it; the committee batch emits both committee `state` and mapped `hc1h_state`. Tests prove totality, injectivity, exact coverage, and import from each split environment.
- F8 HC-1H ROLE NAMING — PASS. Preserved the frozen `real_population` / `--real-population` interface name. The run script prominently warns that it is a role name, not a provenance claim. HC-1H now requires adjacent provenance sidecars and refuses data-class disagreement or an accepted-population/injection-pool role swap.

## Verification

Synthetic fixtures and temporary tensors/images only; no real tensors, chi campaign, network, package install, database action, deploy, commit, or push.

- Committee suite: 9/9 passed.
- Inference suite: 14/14 passed, including 20,000 manifest paths.
- HC-1H suite: 29/29 passed.
- Shared vocabulary/environment launcher suite: 5/5 passed.
- Display renderer suite: 2/2 passed.
- Total: 59/59 passed.
- All five shell launchers passed `sh -n` and executable `--help` probes under their declared interpreters.
- Scoped `git diff --check`: clean.
- Seventeen changed/new plumbing files scanned: no smoothing or sparse-cell rule terms were introduced. The two out-of-scope preregistration parameters were not decided or encoded.

## Build identities for re-gating

- `_inference_20260820/inference_runner.py`: `be6951910122abdf10f18cffb1f4c0cc6526920eaada927458c3f3011bc5c5ee`
- `_committee_20260820/committee.py`: `c1438d7f1d45fb04b950e3344fd7286244e1d09f659f88208e61f23eb6dc3a95`
- `committee_state_vocabulary.py`: `5b32061a82f7cd83d6d167cf48fc28d3625f3ef2ab18a477a97f1c2634793df1`
- `display/tensor_to_png.py`: `64394e0f697de349d4a5b3d7f35363ae850b6100a1e387fb5091dbbf0abd7d3b`
- `handcheck/nm_handcheck.py`: `65c04377734e3cd881bcb4144ae6652c1764429a189f352993033f9639765cd4`
- `RUN_ENVIRONMENTS.md`: `25ee0be369419b744cdd78ab0507f34e68a3c64a49142258d51d6efcb941fe9c`

# BS-3g TOOLING V2 — PINNABLE V137-H bytes (2026-09-03)

Duho selected option (ii) via Blanc, verbatim "as their recs", at 19:37 KST
(direction #69), following ruling (a) at 16:52 KST (direction #66). The V137-H
design parameters are a₀ = 0.95 and Γ = 0.10; at `n_steps = 50`, Δγ = 0.004.

```text
48b2cc6607b91b1e746c2ee7cb21c9b624fb247be5aee3922fb3572351848e82  gates/bs3g_producer.py
ca6e2ea35b38bebb020b053839477306cbce97a7791de4ad76d9f524afe21454  gates/verify_bs3g_receipt.py
19ffcbab574a8663e248b4d837be9734e48843e8c9ab8ea59489ef2558cf5818  run/classp_candidates/BS-3g.json
```

The producer defaults preserve the prior behavior: omitted `--a0` uses the
untouched fixture's own `a_hat`, and `--gamma-bound` defaults to 0.25. The V137-H
run explicitly supplies `--a0 0.95 --gamma-bound 0.10`. The independent verifier
parses those two design values from V137-H and refuses disagreement in the
calibration digest, `gamma_bound`, grid-manifest digest, or derived
`delta_gamma_max`. The twenty-field BS3G-V1 schema is unchanged; entry digest:
`eb8589f5f70656b16dc8ba16e7d78677a0ab0da7b92cb54eddd22fef14e20102`.

The P0-signed `ref/gain_counterfactual_path.py::_fixture` remains byte-untouched
at sha256 `92cbbdf89bd2a494c9cfb9f19fb12a46cf59a16731246cea2e74c56d2454a9b7`.
The earlier verifier-valid FAILED 0.88 receipt is retained at
`run/classp_candidates/BS-3g.FAILED-0p88-20260903.json`, sha256
`a8277a193caffa826ac3a1c2884545f0112b64e7cd3f6a6556dcc996041e49ba`.

Receipt status: deterministic, verifier-valid `FAILED`; 0/5,049 cells are
calibration-inconclusive, but draw 94 changes from baseline `INCONCLUSIVE` to
`REPRODUCED-LONGO` at γ = −0.10. Under the pre-stated acceptance rule, this
receipt is a true blocking record and does not fill BS-3g.

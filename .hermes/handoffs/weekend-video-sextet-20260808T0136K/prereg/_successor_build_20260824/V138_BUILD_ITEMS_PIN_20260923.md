# V138 §11 build items — PINNED 2026-09-23 21:52:33 KST (Hwao)

V138 §11 lists these as REQUIRED, UNBUILT AT V138. They are built as lane drafts in `SPIN_RESTART_READINESS_20260923/hwao/_prep/` and copied byte-identically here under `gates/v138/`; digests below are the pins for Runs A and B (Blanc `V138_SIGNED_RUNS_GO.md`: runs start once drivers are built, digest-pinned and recorded). Their own tests: replay checker exercised on synthetic passes (equal → PASS; 1-ULP control caught; 1e-15 logit drift → primary FAILED / fallback disclosed; label flip → STOP; missing record → refused); positive-control parser and Wilson bound unit-tested; the spectral shim assembled into scratch and compared with the R2 original on 3 synthetic spirals (1–6 ULP drift on three spectral features, 9 bit-identical). None has touched a real pixel or the reader.

```
b61880cc1cb99db6159a6b19631b4dd09f062d97df27b5260671e5f0389798ea  gates/v138/assemble_reader_r2_v138.py
efcd7c0dc938c4bb41c3dad2f389aa4f42f3e8e17f7ff0be153d26a666560dce  gates/v138/positive_control_readability.py
8041e8a8b3d1f88cdf218167868c4fa9489e74acf433b8d3e76a81af19b42e31  gates/v138/record_v138_signature.py
9c9657540fad6370af08aa274180a2d2b3c30335283592cb3f67864b6ca89d2d  gates/v138/replay_r2_v138.py
```

| item | file | role |
|---|---|---|
| `ref/reader_r2_v138/` assembler | `gates/v138/assemble_reader_r2_v138.py` | copies V138-BS3-IDENTITY files + EA-3 modules by verified digest; writes a shim `spectral.py` transcribing EA-3's numeric body; MANIFEST.json; refuses on digest mismatch or existing tree |
| replay driver + equality checker (§6.6) | `gates/v138/replay_r2_v138.py` | fresh single-thread workers, `sys.modules` pins at launch/completion, adapter records; exact-equality PASS/FAILED; fallback evaluated, invoked only on FAILED; 1-ULP fail-first control |
| positive control (§6.5, BS-RG) | `gates/v138/positive_control_readability.py` | drand-anchored 400 draw from the 1,079 set; pilot renderer + mirrored copies; decoy-isolation + mirror fixtures (FAIL stops); one isolated agy call per presentation with the full rubric bytes; Wilson evaluation; refuses without a pinned `--expert-map` |
| signature recorder | `gates/v138/record_v138_signature.py` | not used — Blanc filled the lines; kept as the two-step tool for V139+ |

**Not built:** repointing `rev-2-repair/replay_bounded.py` to the new tree for the 1,272 archived records (§6.6 replay set's first half); EA-3 admissibility is measured by comparing the repaired-tree pass against an unrepaired-tree pass on shard-0 (both drivers exist; the unrepaired pass is one extra `run` with `--tree` = the R2 directory).

**Re-pin 2026-09-23 21:55:34 KST (Hwao):** `gates/v138/positive_control_readability.py` → sha256 `d1e4ad7cb434a40710835051af187be05577b8e76a91a48c082b77616c05c94e` — drand fetch corrected before any draw: the chain hash was truncated to 40 hex (copied from an abbreviated record) and the endpoint returned 404; now the full 64-hex chain `8990e7a9…2e51b2ce`, three hosts queried, ≥2 must agree on round and randomness (BLS not verified here, stated in the draw record). Superseded pin `efcd7c0d…` never ran.

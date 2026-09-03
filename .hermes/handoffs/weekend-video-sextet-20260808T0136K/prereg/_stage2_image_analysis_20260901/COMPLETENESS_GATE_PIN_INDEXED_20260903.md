# COMPLETENESS GATE — INDEXED EXCLUSION LOOKUP PINNABLE (agy COMPLETENESS-INDEXED-REFEREE-V2, 2026-09-03 21:10 KST, ACCESS PROVEN, 0 open findings; V1 20:57–21:02 NOT-PINNABLE on F1 = pytest collection ImportError, closed by the package __init__.py re-export)

Supersedes COMPLETENESS_GATE_PIN_2W_20260903.md for completeness_gate.py / test_completeness_gate.py; run_full.py, tap_source.py, test_run_full.py, prior_unresolved_13725.json, run_full_resume.sh unchanged from the 2W pin. Change is speed-only: cKDTree unit-vector candidate search with a 1e-7 arcsec super-radius, admission by the unchanged separation_arcsec <= radius predicate; _within_linear kept as reference; receipt gains the provenance field spatial_index and its software_sha256 changes accordingly. Finalisation relaunched 20:55 KST (pid 27880) on this code before the verdict; its receipt is now no longer provisional.

```
d403c8cced25fa4c3cdcba182840bb594b48215c5b6ca64589756cf234c5c716  completeness_gate/completeness_gate.py
d71e187817180883d970e1543ef0c1c10f99f80094a4fd45c0355a3f27ec11fb  completeness_gate/test_completeness_gate.py
4319fe459f354806bd15f29261ab11d99c62958aaf93747d30490cefa9b27dae  completeness_gate/__init__.py
bc361a124e964dbd44d464f09c841c69ff310226a8a022cf1f837b7795f06e40  completeness_gate/run_full.py
6678a014002fcde1990707e55f049fa25e6fc2510af8ff051552b35e65432cfd  completeness_gate/tap_source.py
254489266a3a3fbc6ac822b768b95eabd47b7e59bb42735629a9c33ec569570a  completeness_gate/test_run_full.py
73a1d8e10e15d0b501745b008be370afc82151472177e3a1ac334966bef1bafa  completeness_gate/prior_unresolved_13725.json
c8cdf22ebbcdc844b0b6b6cc86a64acd88b184f98705f57bf09ac35a07705279  completeness_gate/run_full_resume.sh
```

Referee reports: completeness_gate/AGY_COMPLETENESS_INDEXED_REFEREE_V1_20260903.md (NOT-PINNABLE, 1) and _V2_ (PINNABLE, 0). Disclosure: the V1 seat edited completeness_gate/__init__.py during its run; the two-line file was kept and committed by Hwao (23077c173). Tests: pytest 41 passed; direct run 20 tests OK, TIMING_100K 0.37 s.

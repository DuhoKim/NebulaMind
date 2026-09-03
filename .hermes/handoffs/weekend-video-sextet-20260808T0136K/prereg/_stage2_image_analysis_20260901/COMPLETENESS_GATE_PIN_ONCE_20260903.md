# COMPLETENESS GATE — CHECKPOINT VERIFIED ONCE PINNABLE (agy TAP-CHECKPOINT-ONCE-REFEREE-V1, 2026-09-03 21:24 KST, ACCESS PROVEN, 0 findings)

Supersedes COMPLETENESS_GATE_PIN_2W_20260903.md for tap_source.py / test_tap_source.py; completeness_gate.py per COMPLETENESS_GATE_PIN_INDEXED_20260903.md; run_full.py, test_run_full.py, prior_unresolved_13725.json, run_full_resume.sh unchanged. Change is speed-only: TAPCandidateSource caches the hash-verified checkpoint entries on first use and appends after a fetch; every raw result file is hashed exactly once per finalisation (was once per chunk: 0.52 s x 8,933 = ~1.3 h).

```
74e825034e39ffc949ca9d3217759c413ff446504f069b312e042de2ec61d27f  completeness_gate/tap_source.py
6c27842071ebe91d39b4478a03de3c73711b6a45c424c9911558f2d570991f3f  completeness_gate/test_tap_source.py
d403c8cced25fa4c3cdcba182840bb594b48215c5b6ca64589756cf234c5c716  completeness_gate/completeness_gate.py
d71e187817180883d970e1543ef0c1c10f99f80094a4fd45c0355a3f27ec11fb  completeness_gate/test_completeness_gate.py
4319fe459f354806bd15f29261ab11d99c62958aaf93747d30490cefa9b27dae  completeness_gate/__init__.py
bc361a124e964dbd44d464f09c841c69ff310226a8a022cf1f837b7795f06e40  completeness_gate/run_full.py
254489266a3a3fbc6ac822b768b95eabd47b7e59bb42735629a9c33ec569570a  completeness_gate/test_run_full.py
73a1d8e10e15d0b501745b008be370afc82151472177e3a1ac334966bef1bafa  completeness_gate/prior_unresolved_13725.json
c8cdf22ebbcdc844b0b6b6cc86a64acd88b184f98705f57bf09ac35a07705279  completeness_gate/run_full_resume.sh
```

Referee report: completeness_gate/AGY_TAP_CHECKPOINT_ONCE_REFEREE_V1_20260903.md. Tests: pytest 42 passed (codex: 62/62 across the three suites); 2,000-chunk synthetic resume 0.30 s. The finalisation launched 20:55 KST on the previous pin (pid 27880) was stopped at 21:25 KST after this verdict and relaunched on these bytes; checkpoint 8,933/8,933 intact throughout.

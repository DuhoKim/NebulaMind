# COMPLETENESS GATE — 2-WORKER MODE PINNABLE (agy COMPLETENESS-2WORKERS-REFEREE-V1, 2026-09-03 17:46 KST, ACCESS PROVEN, 0 findings)

Supersedes COMPLETENESS_GATE_PIN_20260903.md for run_full.py / tap_source.py; other pinned files unchanged. Receipt byte-identical between 1- and 2-worker runs (confirmed by the referee).

```
bc361a124e964dbd44d464f09c841c69ff310226a8a022cf1f837b7795f06e40  completeness_gate/run_full.py
6678a014002fcde1990707e55f049fa25e6fc2510af8ff051552b35e65432cfd  completeness_gate/tap_source.py
254489266a3a3fbc6ac822b768b95eabd47b7e59bb42735629a9c33ec569570a  completeness_gate/test_run_full.py
1b96443e8e24561c01958b3a71d495897c041a52b390eda5df497bc97290022e  completeness_gate/completeness_gate.py
73a1d8e10e15d0b501745b008be370afc82151472177e3a1ac334966bef1bafa  completeness_gate/prior_unresolved_13725.json
c8cdf22ebbcdc844b0b6b6cc86a64acd88b184f98705f57bf09ac35a07705279  completeness_gate/run_full_resume.sh
```

Duho direction #68 (override for a second worker). Switchover at a checkpoint via _tmp_switch_to_2workers.sh; backoff to 1 worker on any 429/5xx/timeout.

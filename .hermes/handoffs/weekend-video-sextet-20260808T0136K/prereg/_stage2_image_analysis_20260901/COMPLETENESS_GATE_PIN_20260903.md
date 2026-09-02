# COMPLETENESS GATE — PINNABLE bytes (agy COMPLETENESS-GATE-REFEREE-V3, 2026-09-03 02:15 KST)

Refereed PINNABLE after three rounds (C1-C4 closed). These exact bytes run the definitive §3-§5 crossmatch.

```
1b96443e8e24561c01958b3a71d495897c041a52b390eda5df497bc97290022e  completeness_gate/completeness_gate.py
7675b1e84bfa78dbeedab8e569a23ff33bc66f3e1a62df9bedaadf75f1e40ab0  completeness_gate/tap_source.py
b51369e4dc6b836d0860738e8448c73c3a35e5d3aab1d68785abb084ae892e79  completeness_gate/run_full.py
82c4ea219c13386de6ce2bcdb08e49bc74bc3b516c4e1443fe30806e1b99e58f  completeness_gate/run_full_resume.sh
73a1d8e10e15d0b501745b008be370afc82151472177e3a1ac334966bef1bafa  completeness_gate/prior_unresolved_13725.json
20e67bff70ac0dba5c09dcc3cd426a4a8e2eb03a4a51f85f94f6def6a8d5e070  completeness_gate/probe_receipt_20260902T160328Z.json
```

Route c: anonymous sync ADQL, q3c all-candidate cones, 100 positions/chunk, 8,933 chunks, MAXREC+QUERY_STATUS cap detection, one worker, ≥2 s pacing. Catalogue-only; no pixels. Output confined to completeness_gate/artifacts_full/.


**Post-referee wrapper fix (Hwao, 2026-09-03 02:2x KST):** `run_full_resume.sh` died at first run with `EPOCHSECONDS: parameter not set` (zsh needs `zmodload zsh/datetime`; `zsh -n` cannot catch it). One line added at the top. New hash:

```
c8cdf22ebbcdc844b0b6b6cc86a64acd88b184f98705f57bf09ac35a07705279  completeness_gate/run_full_resume.sh
```
The refereed Python bytes are unchanged. Run restarted with `--resume` semantics from the 3 admitted chunks.

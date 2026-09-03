# RENDERER + ANCHOR GATE — PINNABLE bytes (agy RENDERER-ANCHOR-REFEREE-V2, 2026-09-03 13:15 KST, 0 findings)

```
ec2097d3c4ea137fcc19aa9697065dbaede6f61af534e441f13c525cf6f317b3  study_renderer/renderer.py
40b17ebf54e26dfce217436f30de9b2b54ec457cd98a001fdae4c379e6c10d95  study_renderer/test_study_renderer.py
8bcf8708eabb95322a3d030b53b17d6d66b10256a512d6bafcc98010b8b1652f  anchor_gate/instrument_identity.py
9fccc7e59806bf186750d1b0eebde56b2e86e95cc17bb81510912463cb019576  anchor_gate/bs4_anchor.py
798712d10e441264a10ffc6b4bcaa886bc1fccbb235dc8251ad6800eb79eb885  anchor_gate/blind_guard.py
b3e8681d24d69ad1913513c4a542066967b9344fa64d51ec93a73447c1680e1f  anchor_gate/test_anchor_gate.py
```

Pre-pixel run-side tooling for signed V10 §8/§9/§10/§15. Renderer is a pure function over caller-supplied image+maskbits+invvar tiles; it REFUSES (DATA-INTEGRITY-FAIL) while companion planes are absent from the acquisition (COMPANION_PLANES_DECISION_20260903.md).

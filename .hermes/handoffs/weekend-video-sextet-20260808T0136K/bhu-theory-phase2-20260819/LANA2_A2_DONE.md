LANA2_A2_COMPLETE

Lana-2, 2026-08-19 16:06 KST.

- Deliverable: TRACK_A2_AUDIT.md (this lane dir). Sources fetched and pinned under sources/
  (1410.3881v2 tarball sha256 bbe1b23b…, 2509.11468v2 tarball sha256 2b6a5ee6…; both
  author-labeled "published version" — custody caveats stated in the audit §0).
- Receipts: receipts/a2_receipts.py (sha256 2f11294e…) + a2_receipts.out (sha256 8389445b…) —
  sympy symbolic + numeric; includes a full symbolic recomputation of the Tolman-metric Einstein
  tensor and the homogeneous FLRW reduction.
- Verdict counts: Paper A (ApJ 832, 96): 18 rows — 10 CHECK, 2 ERROR (A-8 exponent misprint;
  A-9 undeclared a_i=1 m in the flagship number block), 1 POST-HOC-MIX (A-13), 1 CONJECTURE
  (A-17 horizon matching), plus assumed/cited/model-choice rows. Paper B (IJMPA 40, 2544007):
  19 rows — 13 CHECK, 2 ERROR (B-14 R0→pi closure contradiction + branch jump; B-19 g_b=29 vs
  28), 2 UNSUPPORTED (B-13 shear-defeat heuristic; B-17 rotating-fluid sentence), 1
  cross-chain inconsistency (B-18 production law species + x9 normalization vs Paper A).
- Focus findings: (1) horizon/bounce matching is conjecture (A) or branch-inconsistent (B); no
  exterior matching through the bounce anywhere. (2) Parent imprint = M only, via the exact
  M→(a0,T0,R0) map; the chain's own cited numerics claim even that is washed out (depends on
  beta only); parent SPIN is entirely absent — one unsupported sentence (B-17) is the whole
  rotating story. (3) No axis/handedness/anisotropy forecast in either paper; observable claims
  are consistency-class (flatness/horizon/inflation-without-scalar).
- Consequence for Track B: the inheritance transfer function beyond M cannot be audited into
  existence — it does not exist in the published chain; Phase 1's epsilon/f_b parameterization
  stands for spin inheritance and must be named as such.
- Cross-seat: spin-fluid averaging validity -> A1/Goru; Desai–Poplawski PLB 755 numerics and
  any published rotating-ECSK collapse -> Goru ingredients.
- Literature hosts only (arxiv.org e-prints + abs pages); portal.nersc.gov untouched.

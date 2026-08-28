LANA_A1_COMPLETE

Lana (science seat), 2026-08-19 16:11 KST. Deliverable: `TRACK_A1_AUDIT.md` (SHA-256
`0267a4c4…`), with custody under `sources/` and four receipt scripts + outputs under
`receipts/` (p2a1_plb_symbolic, p2a1_plb_numerics, p2a1_prd_symbolic, p2a1_prd_numerics — all
run, all checks resolving).

- **Disclosure:** the bibliography's Miru gate file did not exist at audit time (kickoff asked
  for its first line); mitigated by re-verifying both spine citations first-hand against
  Crossref this session (records pinned under sources/). The audit does not rest on the
  ungated ranking.
- **Custody:** PLB = arXiv:1007.0587 TeX (`95ba2de3…`, stamped Nov 2010 — predates the 2011
  erratum, flagged); PRD = arXiv:1111.4595 TeX (`9ac75297…`); ar5iv HTML copies pinned too.
- **40 verdict rows** (P1–P21, D1–D19). Headlines:
  H1 — the two core papers are mutually incompatible and the PRD explicitly disavows the PLB's
  spin-fluid foundation ("not self-consistent", "violates the cosmological principle");
  different effective fluids (w=+1 stiff vs w=−1), different bounce types (smooth H=0 vs
  cusp-with-velocity-jump inserted by prescription — D13 UNSUPPORTED as dynamics).
  H2 — the ⟨s²⟩ ∝ n² averaging (the brief's named critique target) is derived in neither
  paper; cross-species coherence alone is worth ×6.00 in Ω_S (receipted).
  H3 — sign chain to Ω_S: CHECK; Ω_S = −8.6×10⁻⁷⁰ reproduces (−8.8×10⁻⁷⁰) under the
  coherent-total convention only; PLB's ε_R(â_m) is ×6.95 off (sole non-reproducing number —
  candidate erratum subject); PRD's v_ant (×3200) and Ω(T_cr)−1 (×10⁸) are internally
  inconsistent with its own definitions (both receipted to the exact slip).
  H4 — both bounces sit at/above the Planck scale (PLB ≈1,650× Planck density recomputed;
  PRD T_cr = 0.785 m_P): classical-validity UNSUPPORTED, inherited by all downstream claims.
  H5 — erratum (PLB 701, 672) existence Crossref-pinned; content unresolved (publisher 403;
  arXiv predates it); mitigated by full independent recomputation; resolution is Goru's
  journal-record item; flagged for Gate 1.
- Track B consequences recorded (§3): declare the treatment fork, re-derive Ω_S as a bracket,
  inheritance has no published seed in these papers (Phase 1 ε stays live pending A2), three
  printed numbers quarantined, Planck-regime caveat travels.
- Boundary: fetches from arXiv/ar5iv/api.crossref.org only (one sciencedirect 403, no content);
  **portal.nersc.gov untouched**; writes in this lane only.

Next per the brief: Track A2 (Lana-2) and Goru ingredients run parallel; then Miru Gate 1
(`MIRU_P2_STAGE1_GATE.md`) before any Track B derivation.

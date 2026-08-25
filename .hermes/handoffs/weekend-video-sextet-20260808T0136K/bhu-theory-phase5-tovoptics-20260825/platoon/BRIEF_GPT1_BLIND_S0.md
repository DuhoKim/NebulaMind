# Brief: blind independent computation of Phase 5 S0 (seat: gpt1)

You are one of two INDEPENDENT implementations. Do NOT look for or read any other
implementation, and do NOT read s0_optical_depth.py, S0_DERIVATION.md, or S0_RECEIPT.md in the
parent directory. Your value is your blindness. Work only from the physics stated here.

## Task
Compute the Thomson optical depth of the TOV (exterior) side of the Smoller–Temple
inside-a-black-hole shock cosmology, at the point where an interior observer's past light cone
crosses the shock, as a function of the model's one free anchor.

Physics you are given (derive everything else yourself):
- FRW interior, constant equation of state p = σρ with σ = 1/3. The pinned source gives
  ρ = 4/(3κ(1+σ)²)·1/t² with κ = 8πG.
- At the shock, the gated Phase 4 solution tabulates v = ρ̄/ρ (TOV-side density over FRW
  density) and the shock distance in Hubble lengths √N, against t/t_crit. Read it as data:
  ../../bhu-theory-phase4-anisotropy-20260823/a1_results.csv
  (columns sqrtN_hubble_lengths, v_rhobar_over_rho, t_over_tcrit).
- The shock's areal radius is r̄ = 2 c t √N.
- The observer's past light cone crosses the shock where η_o = η_e(1 + √N(η_e)), with
  conformal time η = 2√t; the crossing redshift is 1+z = η_o/η_e.
- Assume the exterior is fully ionized hydrogen (Thomson opacity σ_T/m_p).

Deliverables in your directory (platoon/gpt1_blind_s0/):
1. Your script.
2. The optical depth at the light-cone crossing for an observer at t_obs = t_crit, tabulated
   against physical anchor values of t_crit spanning at least 1 second to 10^20 seconds.
3. The anchor value at which the optical depth equals 1, and which side is optically thick.
4. A README stating every assumption you made, your choice of path length and why, and any
   limiting-case checks you ran.

Rules: write ONLY inside your directory (temp files as _tmp_* there); do not modify anything
else; do not commit. Completion marker: GPT1_S0_DONE.md in your directory.

LANA_B1_COMPLETE

Lana (science seat), 2026-08-19 16:33 KST. Deliverable: `P2_DERIVATION_BOUNCE.md` (SHA-256
`f6dc00ac…`) + receipts `p2b1_spinfluid_derivation.py` / `p2b1_dirac_derivation.py` with
outputs (all run clean this session). Zero new fetches; portal.nersc.gov untouched; writes in
this lane only.

All seven kickoff requirements executed:
1. **Fork declared, both treatments carried** (§1, §4): spin-fluid (w=+1, smooth H=0) vs
   Dirac (w=−1, cusp) — never blended; the cross-treatment table shows they disagree on
   bounce scale by two orders of magnitude.
2. **Ω_S re-derived as a bracket**: [−8.82×10⁻⁷⁰ coherent, −1.47×10⁻⁷⁰ incoherent], the
   ×6.00 species-coherence spread DERIVED (cross-terms of independent zero-mean spin fields
   vanish — receipted); sign and a⁻⁶ scaling derived from our own algebra (the conservation
   law itself derived from the Friedmann pair: residual factor exactly −κ/3a). Published
   −8.6×10⁻⁷⁰ sits at the coherent edge (2.6% inside). Erratum handled exactly per Gate 1:
   metadata-level venue only, content UNVERIFIED, all inputs scripted for mechanical rerun.
3. **Quarantined numbers recomputed, never imported**: P13 ε_R(â_m) = 7.27×10¹¹⁶ (own Ω_S) /
   7.65×10¹¹⁶ (printed Ω_S — reproduces audit R2 exactly; discrepancy explained); D15
   v_ant = 2.77×10³¹ and D16 Ω(T_cr)−1 = 1.29×10⁻⁶² both recomputed our own way, both agree
   with R4.
4. **Planck-regime caveat as named limit V1 on every quantity**: Treatment I ≥1.6×10³×
   ε_Planck (5.7×10⁴× on the incoherent edge); Treatment II T_cr = 0.785–1.92 m_P;
   extended over A2's T_max/τ per Gate 1 Check 4(c).
5. **n² averaging marked ASSUMED-WITH-CITATION everywhere used** (V2); coherence bracket
   propagated to BOTH treatments (Dirac: incoherence pushes T_cr super-Planckian, 1.92 m_P).
6. Sources: pinned copies only; Goru ingredient sections 1/2/4 not leaned on (Gate 1 cond. 1).
7. Temp/receipt discipline held.

New receipted findings beyond the audit: the exact curvature correction to the bounce root
(relative ~2×10⁻⁶⁴ — neglect justified, not assumed), and the Treatment II cusp quantified:
ε_eff(T_cr) > 0 in closed form AND |β̇| → ∞ at the minimum — the temperature rate diverges,
so the "nonsingular" bounce is curvature-finite but dynamically inserted.

Handoff recorded (§6): the inheritance step gets treatment-dependent bounce states; no
published equation carries parent (M, a★) rotational content into any of them — Phase 1's
ε/f_b parameterization remains the named vehicle unless step 2 derives a piece of it.

Next per the brief: fresh Miru gate (`MIRU_P2_BOUNCE_GATE.md`), then Track B step 2
(`P2_DERIVATION_INHERITANCE.md`).

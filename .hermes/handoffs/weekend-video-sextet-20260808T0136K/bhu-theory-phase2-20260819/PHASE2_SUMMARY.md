# PHASE 2 SUMMARY — the Popławski torsion-bounce chain, strict treatment

Tori (BHU coordinator), 2026-08-19 17:13 KST. Synthesis of gated artifacts only; no new
claims. Every statement below traces to a PASS-gated document in this lane.

## The verdict

**No finite-amplitude signature of the Popławski chain survives at observable magnitude.**
The most generous defensible stacking of every derived quantity yields a sky-statistics
amplitude A ≤ 6.0×10⁻¹² (Treatment I) / 5.4×10⁻¹¹ (Treatment II) — about 10⁻⁵–10⁻⁴ of the
sample-complete all-sky 1σ counting floor (σ_A = 7.07×10⁻⁷, N = 2×10¹² galaxies, the
strongest admissible floor: no instrument can beat "all of them"). The
angular-momentum-conserving reading gives A ≤ 6.3×10⁻⁷⁷. (Per confront-gate nit N1, stated
once here so the chain of conditions is self-contained: the ε_max ceiling and hence both
stack magnitudes are conditional on B2's **Reading 1** — that the published homogeneous
bounce is demanded of a rotating parent; under Reading 2 the rotating-parent bounce is
underived entirely and there is *less* signal, not more. Stack B additionally assumes spec
rows A2/A7.) The headline rests on named conditions V1 (both bounces are Planck-scale
events treated classically), V2 (the ⟨s²⟩ ∝ n² averaging is underived in the published
chain; the ×6 coherence bracket travels), and the underived B-13 production heuristic
behind the axis-memory question, which remains UNDETERMINED in both directions.

## What Phase 2 derived that the literature never wrote

1. **The ECSK bounce, re-derived as a bracket** (`P2_DERIVATION_BOUNCE.md`, sha256
   f6dc00ac…, gate PASS_P2_BOUNCE): Ω_S ∈ [−8.82×10⁻⁷⁰, −1.47×10⁻⁷⁰]; the published
   −8.6×10⁻⁷⁰ sits 2.6% inside the coherent edge. The two spine treatments (spin-fluid
   w=+1 smooth bounce; Dirac w=−1 cusp) are mutually incompatible — declared as a fork,
   never blended; they disagree ×727 on bounce density. New receipted results: the exact
   curvature correction to the bounce root (~2×10⁻⁶⁴, neglect justified); the Dirac
   "nonsingular" bounce is curvature-finite but dynamically inserted — ε_eff(T_cr) > 0 in
   closed form AND |β̇| → ∞ at the minimum.
2. **The inheritance step, bounded instead of invented** (`P2_DERIVATION_INHERITANCE.md`,
   sha256 9cd4fe3c…, gate PASS_P2_INHERIT): the parent imprints mass only (exact
   M→(a₀, T₀, R₀) map; a₀T₀ ∝ χ^(3/4)M^(1/2)); parent spin has NO published transfer
   function, and none was manufactured. Instead, first principles give: (i) orbital J has
   no torsion channel (pinned structural claim); (ii) a self-consistency **ceiling**
   ε ≤ 1.5×10⁻²⁷ (I) / 1.4×10⁻²⁶ (II) for a 10 M☉, a★=0.7 parent, scaling exactly M^(−2/3)
   (conserved-J rotation would exceed causality by 6.6×10²⁶); (iii) a polarization sliver
   ≤ 5.1×10⁻¹³ (I) / ~2.9×10⁻¹³ (II, matched-input per gate nit) — dismissed. Phase 1's
   ε/f_b parameterization stays the named vehicle; spec row A4 is upgraded to
   STILL-PARAMETERIZED-NOW-BOUNDED; nothing silently eliminated.
3. **The frozen-ratio theorem** (same document): shear and torsion terms both scale a⁻⁶,
   so their ratio is frozen — a bounce occurs only if shear is already subdominant, and
   the bounce itself performs zero isotropization. This cuts against the chain's own
   isotropization language and leaves axis memory hanging entirely on the underived
   particle-production heuristic. A condition, not a number; never converted.
4. **The confrontation** (`P2_CONFRONTATION.md`, sha256 02842214…, gate PASS_P2_CONFRONT):
   eight rows, every derived quantity vs a pinned published bound or an explicit status.
   The Ω_S bracket sits 45.2–46.0 orders under the BBN stiff-fluid bound of Dutta &
   Scherrer, PRD 82, 083501 (2010), DOI 10.1103/PhysRevD.82.083501 — fetched, sha-pinned
   (f99cd419…), quoted verbatim, Crossref-verified, sign caveat argued at the point of
   use. This pin closed Gate 1's last open condition. Both bounce states: UNTESTABLE
   (interior, infinite redshift). Stacked amplitude: RULED-OUT-AS-OBSERVABLE.

## The audit base under it (stage 1, gate PASS_P2_STAGE1)

- `TRACK_A1_AUDIT.md` — 40 verdict rows on the PLB 2010 + PRD 2012 bounce papers: the two
  core papers are mutually incompatible and the PRD disavows the PLB's spin-fluid
  foundation; the averaging step is derived in neither; the sign chain to Ω_S CHECKs; the
  PLB ε_R print is ×6.95 off (recomputed value used everywhere downstream); both bounces
  are Planck-regime.
- `TRACK_A2_AUDIT.md` — 37 rows on the ApJ 2016 + IJMPA 2025 interior papers:
  algebraically solid where they compute; horizon/bounce matching is conjecture; parent
  spin is absent (one unsupported sentence); no axis/anisotropy forecast exists anywhere
  in the published chain.
- Erratum trail: PLB 701, 672 (2011) EXISTS (Crossref metadata pinned) but its CONTENT
  remains unverified on every permitted host — the three numbers it may correct stay
  quarantined with our recomputations in their place.
- Goru ingredient sections 1/2/4 failed the venue bar at Gate 1 and were excluded
  throughout; the "HRDCC inheritance" claim lost adjudication against both audits.

## Nit ledger (all conservative-direction; absorbed here)

- Bounce gate: one claimed arithmetic equality was executed by the gate, not the receipt
  script — exact agreement (transparency note).
- Inherit gate N1/N2/N3: sliver rounding (5.1e-13, not "≤5e-13"); Treatment-II sliver used
  a mismatched Ω (matched value ~3×10⁻¹³ — more margin); the +Σ²a⁻⁶ shear premise is
  standard GR bookkeeping, named but unpinned (zero-fetch step).
- Confront gate N1: Reading-1/A2/A7 conditionality restated in the verdict above.
  N2: B3_DONE.md rounds Stack B to 6×10⁻⁷⁷; the receipt value is 6.3×10⁻⁷⁷ (correct in
  the deliverable itself).

## Discipline record

Chain: stage-1 (3 parallel seats) → Gate 1 → B1 → gate → B2 → gate → B3 → gate → this
summary. Four fresh kimi one-shots (Kimi K3, Moonshot direct), all PASS, all findings-only,
receipts rerun byte-identical at every gate; ~15:57–17:13 KST, 2026-08-19. Seats: two
claude-seat windows (historical markers LANA_*/LANA2_* predate the naming reform), agy
(ingredients), kimi (all gates). Hosts: arXiv/ar5iv/api.crossref.org/doi.org only;
portal.nersc.gov untouched by every seat and every gate. Writes: this lane dir plus
append-only dashboard events. All sources sha-256-pinned under sources/; all receipts with
outputs under receipts/.

## Standing rules that survive this phase

BHU is Duho's personal side-interest, not a NebulaMind research programme. Published papers
only as base; the erratum content hunt (publisher paywall) and any relaxation of V1/V2
remain open items; **external-theorist review is required before any publication claim** —
nothing in this lane is a publication claim. The axis question was reached only through
the published chain, as the brief demanded, and the published chain answers: nothing at
observable amplitude, conditional on the named assumptions.

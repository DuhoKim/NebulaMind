PASS_PHASE0_SCOPING

# Kun — Phase 0 gate on LANA_PHASE0_SCOPING.md + GORU_PHASE0_PRIORART.md

**Kun (gate seat), 2026-08-18 KST.** Scope label, restated per the brief: black-hole-universe
cosmology is Duho's personal side-interest, not a NebulaMind research programme. This gate is
findings-only; nothing was edited. `portal.nersc.gov` was not touched. Literature-host fetches
(arXiv abstract pages only) were used solely to spot-check quoted abstracts.

**Gated documents:** `LANA_PHASE0_SCOPING.md` (Lana, 21:42 KST) and `GORU_PHASE0_PRIORART.md`
(Goru, undated), read together against `PHASE0_BRIEF.md` (Hwao, 21:35 KST).

---

## 1. Gate checklist

| Requirement (brief + kickoff) | Finding |
|---|---|
| Kill criteria stated before evidence, per route | **Honored in Lana's file.** Each route opens with a "Kill criteria (stated before evidence)" block (K-A1/A2, K-B1..B3, K-C1..C3) before any arithmetic. Goru's sweep has no kill criteria, but the brief assigns kill criteria to the scoping seat only; Goru was assigned novelty verdicts (novel / partially-done / already-done), which are present per route. |
| Scope label present | Present in both files (Lana restates it verbatim; Goru's file is a sweep under the same brief). |
| Every load-bearing number traceable to a quoted primary source | **Verified by direct fetch** — see §2. |
| Arithmetic independently recomputed | **Done** — see §3. All of Lana's numbers reproduce within her stated rounding. |
| Verdicts follow from the evidence | Yes, per route — see §4. |
| Seats' novelty findings consistent, or disagreement surfaced | One real disagreement found and **adjudicated, not harmonized** — see §5. |
| No overclaim (closure-note bar stated honestly) | **Pass.** Lana §5 states the bar explicitly: the Route A closure note's single original element (the bound→floor confrontation) makes it "at best a short comment/research-note-class closure document, not a flagship paper" under Duho's flagship standard. No "we could publish X" claim exceeds that bar. |

## 2. Source spot-checks (all fetches today, arXiv abstract pages)

- **S1 Saadeh et al. 2016 (arXiv:1605.07178):** abstract confirmed verbatim — "(σV/H)0 <
  4.7×10⁻¹¹ (95% CI)", "an order of magnitude tighter than previous Planck results that used
  CMB temperature only." Journal ref PRL 117, 131302 matches.
- **S2 Planck 2015 XVIII (arXiv:1502.01593):** abstract confirmed verbatim — "we find no
  evidence for a Bianchi VII_h cosmology and constrain the vorticity of such models to
  (ω/H)_0 < 7.6×10⁻¹⁰ (95% CL)."
- **S3 Planck 2018 VI (arXiv:1807.06209):** abstract confirmed — "H0 = (67.4±0.5) km/s/Mpc",
  "Ωm = 0.315±0.007".
- **S4 Reid et al. 2019 (arXiv:1910.03357):** abstract confirmed — "Ro = 8.15 +/- 0.15 kpc",
  "To = 236 +/- 7 km/s".
- **S5 Li 1998 (arXiv:astro-ph/9703082):** abstract confirmed — J ∝ M^{5/3}, "The present
  angular velocity of the universe is estimated, which is ∼10⁻¹³ rad yr⁻¹." GRG 30 (1998) 497
  matches.
- **S6 Popławski 2010 (arXiv:1007.0587):** abstract confirmed — "ΩS ≈ −10⁻⁶⁹", flatness/horizon
  sentence, and the "suggests … may correspond … could explain" black-hole-parent wording Lana's
  K-B2 route-out relies on. The full-text value −8.6×10⁻⁷⁰ is Tori-pinned in the packet (custody
  chain intact, see below); not re-derived at this gate.
- **S7 Conselice et al. 2016 (arXiv:1607.03909):** abstract confirmed — "2.0 +0.7/−0.6 × 10¹²
  (two trillion)".
- **Packet custody:** SHA-256 of `../reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md`
  recomputed = `b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516` — matches the
  brief's pin and Lana's §0 declaration.
- **Local receipts (existence and figures confirmed, not re-derived):**
  `../prereg/KUN_FEASIBILITY_REGATE_20260812.md` (100,000 accepted-galaxy requirement; primary
  floor `has-spiral-arms_total-votes >= 5`; 18.23% vs 13.06% break-even; Cut-6 survival
  82.404622%; one-sided lower retention 85.72%);
  `../prereg/TORI_PARENT_ROW_COUNT_20260812.md` (dered Cut-5 contiguous partial-coverage lower
  bound 208,407);
  `../../bhu-track-20260805T2000K/BHU_LITERATURE_BASELINE.json` (torsion-bounce total 516;
  entries 2606.09786, 2606.23418, 2605.09571, 2603.19178 all present).

## 3. Independent recomputation of Lana's arithmetic

Using her stated conversions (1 Mpc = 3.086×10¹⁹ km; 1 kpc = 3.086×10¹⁶ km; 1 yr = 3.156×10⁷ s):

| Quantity | Lana | Kun recompute | Match |
|---|---|---|---|
| H₀ in s⁻¹ | 2.18×10⁻¹⁸ | 2.184×10⁻¹⁸ | ✓ |
| ω_max (S2, 7.6×10⁻¹⁰·H₀) | 1.7×10⁻²⁷ | 1.66×10⁻²⁷ | ✓ |
| ω_max (S1, 4.7×10⁻¹¹·H₀) | 1.0×10⁻²⁸ | 1.03×10⁻²⁸ | ✓ |
| ω_Li (10⁻¹³ rad/yr) | 3.2×10⁻²¹ | 3.17×10⁻²¹ | ✓ |
| A generous (S2) | 5×10⁻⁷ | 5.24×10⁻⁷ | ✓ |
| A generous (S1) | 3×10⁻⁸ | 3.24×10⁻⁸ | ✓ |
| ω_disk (236 / 8.15 kpc) | 9.4×10⁻¹⁶ | 9.38×10⁻¹⁶ | ✓ |
| A conservative | 1.8×10⁻¹² | 1.77×10⁻¹² | ✓ |
| σ_A (N=10⁵) | 3.2×10⁻³ | 3.16×10⁻³ | ✓ |
| 3σ floor | ≈1×10⁻² | 9.5×10⁻³ | ✓ |
| Gap, generous branch vs 3σ | 4.3 orders | 4.26 (vs 9.5×10⁻³) / 4.30 (vs 1×10⁻²) | ✓ |
| Needed N = 9/A² (A=5×10⁻⁷) | 3.6×10¹³ | 3.6×10¹³ | ✓ (exact at her rounding) |
| Needed / all galaxies | ~18× | 18.0 (3.6×10¹³ / 2.0×10¹²) | ✓ |
| σ_A classifying all 2×10¹² galaxies | ~7×10⁻⁷ | 7.07×10⁻⁷ | ✓ |
| All-sky S/N at generous A | <1σ | 0.74σ | ✓ |
| Route B deficit vs σ(Ω_m)=0.007 | ~66 orders | 66.9 (full-text −8.6×10⁻⁷⁰) / 66.8 (abstract −10⁻⁶⁹) | ✓ |

No arithmetic errors found. Lana's stated use of the *looser* S2 bound for the headline number
is the generous choice for the model and is correctly labeled as such.

## 4. Do the verdicts follow from the evidence?

- **Route A — DEAD-ON-ARRIVAL: yes.** K-A1 requires A(Ω_max) ≥2 orders below the 3σ floor under
  the most generous coupling, with no physically obtainable sample closing the gap. The generous
  branch sits 4.3 orders below; closing it needs ~18× every galaxy in the observable universe
  (S7); classifying every galaxy that exists still yields <1σ. The kill is sample-complete, as
  stated. The only escape (a nonlinear locking amplifier with gain >10⁴) is correctly identified
  as new model-building, not derivation — and the v2 axis source's own "small"/"tend to align"
  language (packet §1.3) gives no such mechanism.
- **Route B — DEAD-ON-ARRIVAL: yes.** K-B1 is met on the only BHU-attached number
  (Ω_S ≈ −10⁻⁶⁹, ~66 orders below the best density-parameter precision, with no sensitivity
  floor defined by the source). The one potentially reachable sub-channel (bounce-inflation
  numerics) is correctly routed out under K-B2: S6's own wording attaches the black-hole parent
  only as interpretation ("suggests / may correspond / could explain"), so an n_s/r-style test
  would test ECKS bounce cosmology generally, not BHU parentage. The "the mechanism that makes
  the model viable is the mechanism that hides it" argument is sound and sourced to S6's own
  selling point.
- **Route C — DEAD-ON-ARRIVAL (closure): yes, with the stated confidence.** The
  carrier-by-carrier enumeration is complete against the brief's ask, the sharp reason
  (causal boundary + initial-condition degeneracy; the single structural Kerr-matching
  correlation inheriting Route A's magnitude kill) is stated as required, and the confidence is
  appropriately discounted to ~0.75 because "none is conceivable" is framework-level, not
  arithmetic. This satisfies the brief's "well-argued none is conceivable … is a legitimate
  deliverable" clause and closes C15's second arm.

## 5. Cross-seat adjudication (disagreement surfaced, not harmonized)

**Route A novelty — real disagreement. Adjudicated to: partially-done, with the explicitly
computed amplitude confrontation novel.** Goru says "an explicit analytic calculation mapping a
global background rotation magnitude Ω to a specific observable amplitude A(Ω) … remains absent"
(partially-done, citing Shamir 2022 observational asymmetries and Lee 2021 TTT). Lana says the
chain's core mapping "already exists in print" via Li 1998. These differ because they name
different map segments. The primary source settles it: S5's abstract derives galaxy *rotation*
(angular momentum, J–M relation) from global rotation — it does **not** derive a *handedness
asymmetry amplitude* A(Ω), and it predates the CMB bounds (S1/S2) by two decades, so no
confrontation with modern bounds exists in it. Goru's verdict stands; Lana's is correct only for
the galaxy-rotation segment. Consequence for the merged verdict: Route A's closure note keeps
exactly one original element — the bound→floor confrontation — which is precisely the bar Lana §5
states. The DOA verdict is unaffected.

**Route B — apparent disagreement, actually different questions. Adjudicated to: partially-done.**
Goru's "already-done (cite Popławski 2018, 2025)" reads the verdict scale as "the proposed
observables already exist in print"; his own evidence sentence then concedes they "lack a
uniquely measurable local magnitude at present densities or rest on already-constrained
macroscopic asymmetries." Lana's question is the brief's actual one — does a *calibrated,
reachable* magnitude derivation exist — and answers no (with the reachable sub-channel
non-BHU-specific). On the brief's question the record is: statements exist, calibrated reachable
magnitudes do not. The Route B verdict is DOA either way.

**Route C — consistent.** Both seats find no published BHU-unique fingerprint: Goru "novel" (no
smoking-gun signature located; Gaztañaga 2021 / Roupas 2022 class papers address interiors
elsewhere, matching Lana's carrier (d) dismissal), Lana confirms the packet's "no published
observable that differs from generic bounce cosmology." No adjudication needed.

**Sweep-depth caveat (carried, not repaired):** Goru's sweep is abstract/title-level, as is
Lana's corpus check; both files disclose this. The residual confidence allowances (Lana's 0.1 on
A, 0.15 on B, 0.25 on C) explicitly price in a surfaced-later paper. Acceptable at Phase 0
order-of-magnitude discipline; a Phase 1 closure-note night would need a fuller text-level sweep
of the Li-line and Shamir-line literature before the "appears nowhere in print" clause goes into
any citable document.

## 6. Gate verdict

All gate conditions met: kill criteria first in the scoping seat; every load-bearing number
source-quoted and spot-verified; arithmetic independently reproduced; verdicts follow from the
evidence; the one genuine novelty disagreement adjudicated from the primary source; the closure
note's bar stated honestly against the flagship standard; scope label present in both files.

**Merged verdict for Duho (per the brief's deliverable):** no route earns Phase 1 as a
derivation night. Route A is sample-complete dead (≥4.3 orders below any buildable floor, ~18×
all galaxies short); Route B is ~66 orders dead with its one reachable channel non-BHU-specific;
Route C closes with a stated reason. The only defensible Phase-1-shaped product is the Route A
closure note — "under linear coupling, allowed global rotation caps the galaxy handedness
asymmetry at A ≲ 5×10⁻⁷, below the reach of any galaxy survey that can exist" — cost one
evening, arithmetic ~90% done, classified honestly as comment/research-note-class, not a
flagship paper.

— Kun, gate seat, 2026-08-18. Findings only; nothing edited; no derivation performed.

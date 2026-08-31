# RQ-A derivation brief — the Roupas amplitude (BHU Lane 2, task 1)

**From:** Tori (BHU coordinator) · **To:** codex + agy (independent, blind-double) · **2026-08-31**
**Boundary:** compute and bring the number + a falsification verdict. **Do NOT re-tier entry 21** —
the tier move is Duho's. Published-base-layer, receipts discipline, lane-dir only.

---

## The one-sentence task

Roupas (2022, entry 21, arXiv **2203.13295**, EPJC 82:255) claims his "cosmological black holes"
(dark-energy universes inside regular BHs) are **detectable by LISA** — but he computed only the QNM
**frequency** and *explicitly deferred the amplitude*. **Compute the ringdown strain amplitude he
deferred, and compare it to LISA's strain sensitivity**, to decide whether "detectable" is a real,
falsifiable number or an unbacked adjective.

## What Roupas GIVES you (do not re-derive; cite his numbers)

- Distinctive axial gravitational **quasi-normal modes** (QNMs), fundamental n=0, ℓ=2, computed in
  his Appendix C from a master equation continuous across the shell (ε ≪ 1 ultra-compact limit).
- **Frequency result (his §"detectability", clean-text lines ~395–411; Fig 5; Table 1):**
  for M• ∈ [10, 10⁹] M⊙, `10⁻⁶ Hz ≲ ω_R,0 ≲ 50 Hz`; the n=5 overtone ~10× higher. **For
  M• ≳ 10⁴ M⊙ the fundamental sits inside LISA's band (~10⁻⁵–10⁻¹ Hz).** M•=10 M⊙ → 63 Hz.
- **Damping times / imaginary parts:** Fig 5 right panel, Table 1 (per-mass).
- **What he explicitly did NOT do (the task), verbatim line ~400:** *"in order to estimate the minimum
  possible amplitude sensitivity of an interferometer so as to detect a cosmological black hole
  ringdown, the excitation factors of its quasi-normal modes, following a binary merger, have to be
  calculated. This is an involved task, that this work urges the community to perform."*

## Deliverable (the strict model — NOT order-of-magnitude hand-waving)

1. **Excitation / amplitude.** Derive the ringdown **strain amplitude h(f)** for a cosmological-BH
   post-merger ringdown from the QNM **excitation-factor formalism** — the perturbation potential is
   Roupas's Appendix C axial master equation; use the standard excitation coefficients
   (Leaver residue / Berti–Cardoso B_n excitation factors) OR a ringdown energy-fraction model
   E_GW = ε_rd M c² in the fundamental mode. State the formalism explicitly; do not assert a number
   without the equation that produces it.
2. **Two-sided bound, not a point.** Give a **conservative** and an **optimistic** excitation
   (e.g. ε_rd spanning a defensible range, and a representative source distance — say a fiducial
   D and also a horizon estimate). The verdict must be a **range**.
3. **Representative masses in-band:** M• = 10⁴, 10⁵, 10⁶ M⊙ (the LISA regime). Give h and f for each.
4. **Compare to LISA.** Overlay on the **public** LISA sensitivity — Robson, Cornish & Liu 2019
   (`arXiv:1803.01944`, the analytic LISA S_n(f)) or the official LISA SciRD. Characteristic strain
   vs. sky-averaged sensitivity at the mode frequency.
5. **VERDICT (the falsification shape):**
   - If the ringdown strain clears LISA's floor at design sensitivity for a plausible
     mass/distance/excitation → RQ-A yields a **candidate calibrated falsifier**: a number
     (h at f) + a threshold (LISA S_n) → *non-detection of the distinctive cosmological-BH ringdown
     at that sensitivity refutes the claim for that population.* Report it as such (for Duho's tier
     call).
   - If the strain is below any conceivable detector floor for all plausible parameters → the
     "detectable" claim is **not detectable**; entry 21 → PROSPECT-without-a-number by derivation.
   - If it straddles (detectable only under optimistic excitation) → say exactly that, with the
     dividing assumption named.

## Receipts / inputs (all held — no acquisition, no paywall)

- Roupas source: `bhu-reading-20260823/sources/2203.13295_clean.txt` (+ `ar5iv_2203.13295.html` for
  equations/Appendix C).
- LISA sensitivity: public (Robson–Cornish–Liu 2019 analytic S_n(f), or LISA SciRD).
- Every quoted number must be greppable in the source (§1w guard): if you cite a QNM frequency, it
  must appear in `2203.13295_clean.txt`.

## Report back (to `RQ_A_<seat>_RESULT.md` in this lane dir)

- The excitation formalism + every assumption (ε_rd range, D, sky-averaging, which mode).
- h(f) table for M• = 10⁴–10⁶ M⊙, conservative and optimistic.
- The LISA comparison figure/numbers and the **VERDICT** (one of the three above).
- Any place the derivation is not tractable analytically — say so plainly (Roupas called it
  "involved"; if it needs numerics you cannot close, report the blocker, do not fake a number).

**Blind-double:** codex and agy derive independently; do not read each other's result until both are
filed. Tori reconciles. If the two amplitudes disagree by more than the stated bound → that is a
seats-disagree STOP, back to Tori/Duho.

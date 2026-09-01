# RQ-B derivation brief — the Popławski interior transfer function (BHU Lane 2, task 4)

**From:** Tori · **To:** codex + agy (independent, blind-double) · **2026-09-01**
**Boundary:** derive the transfer function + a verdict. **Do NOT re-tier any entry** — any tier-adjacent
outcome returns to Duho as q4. Published-base-layer, receipts discipline, lane-dir only. **Burn:** you
(codex 0% / agy) carry the heavy derivation; Claude coordinates only.

## The one-sentence task

Popławski's Einstein–Cartan torsion bounce (entries 8–12, 51) is the corpus's **only multi-paper
mechanism with explicit field equations**. **Derive the interior "transfer function" the literature
never wrote — from parent-black-hole parameters, THROUGH the torsion bounce, to any interior
observable — and decide whether any FINITE-amplitude, parent-dependent signature survives.**
- If a finite amplitude survives → a **NEW calibrated-falsifier candidate** (a number the daughter
  universe must carry, in principle measurable → for Duho's q4).
- If it is zero / exponentially suppressed → the branch is **CONSISTENCY-ONLY BY DERIVATION** — a firm
  negative result (not by omission, as the record currently has it, but proven).

## The mechanism (from the pinned sources — verify + assemble the field equations)

- **Entry 8** (`0902.1994_clean.txt`, PLB 687) — radial infall into an Einstein–Rosen bridge; the
  parent-BH → bridge → new-interior setup and its matching.
- **Entry 9** (`1007.0587_clean.txt`, PLB 694) — "Cosmology with torsion: an alternative to cosmic
  inflation": the **torsion-modified Friedmann equations** and the claim that torsion generates the
  observed large-scale features *without* inflation. This is where a predicted perturbation
  behaviour would live.
- **Entry 10** (`1111.1017_clean.txt`, PRD 85) — spinor–torsion coupling → the **nonsingular big
  bounce**; the effective density/pressure with the `−α n_f²` spin term and the bounce condition.
- **Entry 11** (`1410.3881_clean.txt`, ApJ 832) — universe-in-a-BH in Einstein–Cartan: closed FLRW
  daughter, particle production, expansion; the tie to the parent.
- **Entry 12** (Popławski 2025, IJMPA 40, 2544007 — *not obviously pinned*; acquire from arXiv if you
  need it, pin it) — gravitational collapse WITH torsion → universe in a BH (the latest synthesis).
- **Entry 51** (`poplawski_plb690_vor_clean.txt` + `..._erratum_clean.txt`, PLB 690) — nonsingular
  Dirac particles; the spin-density scale. Memo figure: spin-density parameter Ω_S ≈ −8.6×10⁻⁷⁰.

## The transfer function — define it, then derive it

Let the daughter interior carry perturbations `δ_out(k)` (or any observable O). Define the transfer
`T(k) = δ_out(k) / δ_in(k)` mapping pre-bounce/parent input to post-bounce interior output at comoving
scale k. **Derive T(k)** (or the analogous map for whatever observable the mechanism actually predicts
— perturbation amplitude, spectral tilt, a relic abundance, an anisotropy) by propagating through:
1. the parent infall / collapse (entry 8/12),
2. the torsion-dominated high-density regime and the **bounce** (entry 10's effective Friedmann with
   the spin term; entry 9's torsion cosmology),
3. the post-bounce expanding interior (entry 11).

**The deciding question:** does T carry a **finite, parent-parameter-dependent amplitude** to
observable (super-horizon → CMB-ish) scales, or does the spin-torsion term (Ω_S ~ 10⁻⁷⁰, active only
near Planck density) make it **exponentially suppressed / independent of the parent** → no surviving
signature?

## Deliverable (`RQ_B_<seat>_RESULT.md`)

1. **The assembled field equations** (torsion-modified Friedmann + the spin term), with source line
   receipts.
2. **T(k)** — the derived transfer function (or the observable-map), with the bounce propagation shown.
3. **Amplitude verdict** — does a finite parent-dependent signature survive at observable scales?
   Give the amplitude (or the suppression factor) with the derivation, not an assertion.
4. **VERDICT (first line, one token):**
   - `NEW_FALSIFIER_CANDIDATE` — a finite, parent-dependent interior observable survives; state the
     number + what would measure it.
   - `CONSISTENCY_ONLY_BY_DERIVATION` — the signature is zero / exponentially suppressed / parent-
     independent; the branch is consistency-only *by proof*. State the suppression.
   - `UNDETERMINED_NEEDS_<resource>` — the derivation cannot close from the pinned sources without a
     specific gated resource (name it: a paper, a computation). Do NOT fabricate a transfer function.
5. **Strict model (per Duho):** derive from the field equations — not order-of-magnitude scoping.
   State every assumption (which perturbation variable, the bounce matching, the observable chosen).
   Where the mechanism genuinely under-determines the observable, say so plainly.

## Receipts

Every equation/number greppable in a pinned source. Entries 8/9/10/11/51 are pinned above; entry 12
from arXiv if needed (pin it, force-add the .pdf, atomic commit). The record's prior finding you may
build on but must re-verify: entry 51's mass floor is **unreproduced from its own inputs** (six routes,
none reaches it) — do not import that as an assumption; it is a separate open item.

**Blind-double:** codex and agy derive independently; do not read each other's result. Tori reconciles
— agreement on FINITE-SURVIVES vs SUPPRESSED is the load-bearing call; a split there is a
seats-disagree item (third read, as on RQ-D) before it goes to Duho.

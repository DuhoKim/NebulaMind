# Tori → Hwao — what the BHU lane has been studying (for the prereg wrap-up)

**2026-08-31 00:46 KST.** Duho asked me to tell you what I've been studying so you can wrap up the
prereg work. The V124 draft is the **Longo-amplitude test**, and its central citation anchor —
**Longo 2011** — is a paper I have independently pinned and content-verified this cycle. Details
below; the parts that matter to your citation-verification phase are marked ★.

## What the BHU lane is

An adversarial audit of the **black-hole-universe published bibliography** — 58 numbered entries,
each tiered under one preregistered rule and double-gated by two seats. Authoritative records:
- `bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md` (the 58-entry record)
- `bhu-acquisition-20260828/WRAP_UP_20260830_FULL_DAY.md` (cold-readable state)
- battery `bhu-acquisition-20260828/check.py` — 76 self-computing checks, green.

## ★ The one that touches your prereg directly — Longo 2011 = BHU entry 58

Your V124 §1 anchors on Longo, *"Detection of a Dipole in the Handedness of Spiral Galaxies…"*, PLB
699, 224 (2011), bibcode 2011PhLB..699..224L, arXiv:1104.2815, amplitude **−0.0408 ± 0.011**,
**15,158** spirals, axis **(l, b) ≈ (52°, 68.5°)**.

That is **entry 58** in my corpus ("the axis-prediction measurement… the amplitude the DESI
spin-parity campaign tests"). I acquired and content-verified it this cycle in check **b54**
(`bhu-acquisition-20260828/b54_support58_content.py`, 5/5):
- pinned source = the arXiv abstract page, `bhu-reading-20260823/sources/arxiv_1104.2815_abs.html`,
  **sha256 `5bf7c92ddc47…`** (ar5iv has no full render for this 2011 paper; the abstract carries the
  full load-bearing content, same precedent as other abstract-only pins);
- verified verbatim from that source: **amplitude −0.0408 ± 0.011**, chance probability **7.9×10⁻⁴**,
  axis **(l, b) = (52°, 68.5°)**, sample **15158** spirals, cut **z < 0.085** (the "z ~ 0.04" in the
  title is the effective depth). Longo also notes a similar asymmetry in the Iye–Sugai Southern
  catalog and spin correlation out to ~210 Mpc/h.

**Upshot for you:** your prereg's Longo anchor numbers are independently corroborated against the
primary source and hash-pinned in the BHU corpus. If your citation-verification pass wants a second
receipt for the Longo amplitude/axis/sample, b54 is it.

## What I DON'T have (so you don't over-credit me)

- Your **counter-anchor, Land et al. 2008** (Galaxy Zoo isotropy null, arXiv:0803.3247), and
  **McAdam & Shamir 2023** (arXiv:2302.06530, the ~15% annotation-bias figure) are **not** in the
  BHU corpus — the BHU bibliography is the theory-side "universe inside a black hole" literature,
  not the spin-statistics measurement literature. I have not verified those two; your own direct
  reads stand alone.
- The BHU corpus frames Longo as the *family's preferred-axis measurement* (the rotating-parent
  scenario predicts a preferred axis; Longo's dipole is the observational instrument). That is
  **motivation context**, not a calibration of your instrument.

## Related BHU finding, SEPARATE from the spin-parity prereg (FYI, don't fold in)

The other DESI-facing BHU prediction is **curvature**, entry 54 (Gaztañaga bounce): it predicts a
**closed** universe (Ω_k < 0). I ran a two-seat gate (B61) this cycle — both seats: the falsifier is
**LIVE but NOT FIRED**. Current best data leans mildly *open* (DESI DR2+CMB Ω_K = +0.0023 ± 0.0011,
~2.1σ, adverse to the closed prediction but not a detection; ACT "no departure from flatness";
Planck combined ~1.6σ closed). A standing battery tripwire (`b63`) re-fires if a future release
pushes the open side ≥3σ. **This is a different observable from your handedness dipole** — flagged
only so you know the BHU–DESI surface has two prongs, not one.

## Pointers

- Longo receipt: `b54_support58_content.py` + `arxiv_1104.2815_abs.html` (sha 5bf7c92ddc47).
- Full corpus + tiers: `BHU_PUBLISHED_BIBLIOGRAPHY.md`, entry 58.
- Curvature gate: `AGATE_B61_VERDICT.md` + `CGATE_B61_VERDICT.md`, `curvature_constraints_ledger.json`.

I'm on quiet-hold + overnight paper research; ping via a file back or Blanc if you need anything
pulled. — Tori

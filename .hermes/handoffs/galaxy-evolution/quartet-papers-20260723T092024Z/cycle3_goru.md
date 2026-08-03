# Cycle 3 — Goru: forward-modelling the emission-line selection onto the SFMS elevation

Quantifies how much of paper #3's SFMS "elevation" (and #6's load-bearing sim-vs-obs SFR gap)
is an emission-line SELECTION artifact. Standalone script `c3_goru_selection.py` (run against live
SDSS SkyServer TAP; no tracked-file or worker-queue writes).

## Claimed signal (paper #3, from its text)
Δlog SFR above the z≈0 SFMS at fixed M⋆: **+0.77 (z≈3.5), +0.89 (z≈4.7), +0.96 (z≈5.4), +1.94 (z≈6.7)**.
Local SFMS: logSFR = 0.61(logM⋆−10)+0.065. Paper concedes the JWST samples are emission-line selected
("biased toward high-sSFR, high-EW … inflates the apparent main-sequence elevation") but never corrects it.

## Method (defensible, not perfect)
1. **Grounded σ on real SDSS** (N=120k pull): SF-ridge scatter = 0.44/0.42/0.38/0.38/0.39 dex across
   logM⋆ 8.75→10.75 (median 0.39) — confirms the paper's σ=0.39. High-z σ is larger; carry grid σ∈{0.30,0.45,0.60}.
2. **Forward model** a mock high-z population over logM⋆=7–10.5 (steep MF), assign logSFR = SFMS_local(M)+E_true+N(0,σ),
   then apply an **emission-line (Hβ-flux) detection floor**: SFR→L(Hα) via Kennicutt (Chabrier, logL=41.1+logSFR),
   L(Hβ)=L(Hα)/2.86, keep F(Hβ)>F_lim ⇒ an **SFR floor rising as d_L(z)²**. Flux grid F_lim∈{1e-19…1e-18} erg/s/cm²
   (deep→shallow NIRSpec). The detected mass distribution emerges self-consistently.
3. Re-derive the paper's estimator (median of Δ=logSFR−SFMS_local over the *detected* sample), scan E_true, and
   read off the E_true that reproduces each observed elevation ⇒ inflation = E_obs − E_true.
   Analytic truncated-normal cross-check (median shift = σ·Φ⁻¹[(1+Φ(a))/2], a = (floor−μ)/σ) agrees.

## Result — selection inflation of the elevation (dex)
Envelope over σ∈{.30,.45,.60} × F_lim∈{1e-19,3e-19,1e-18}; residual = de-biased PHYSICAL elevation:

| z | E_obs | inflation (median [env]) | residual physical E_true [env] |
|---|-------|--------------------------|--------------------------------|
| 3.5 | +0.77 | **+0.63** [+0.23,+1.17] | +0.14 [−0.40,+0.54] |
| 4.7 | +0.89 | **+0.51** [+0.05,+1.15] | +0.38 [−0.26,+0.84] |
| 5.4 | +0.96 | **+0.44** [−0.02,+1.20] | +0.52 [−0.24,+0.98] |
| 6.7 | +1.94 | **+0.46** [+0.10,+1.20] | +1.48 [+0.74,+1.84] |

Central take: **≈0.4–0.6 dex (≈40–60%) of the z≈3.5–5.4 elevation is selection**; the +1.94 at z>6 is
≈0.3–0.7 dex (≈25–35%) inflated but keeps a **large real residual (~1.3–1.5 dex)**. Analytic check shows the
bias is strongly mass-dependent — at logM⋆≈8 the floor sits ~1σ above the median (shift +0.5→+0.7 dex);
at logM⋆≈9–9.5 it sits below (shift ~0.1–0.3 dex) — so faint/low-mass-dominated bins inflate most.

**Honest limitation:** inverting a single *published median* per bin is degenerate — (E_true, F_lim, σ) trade off,
so per-bin point estimates are unstable (a sample-mass-matched central swings 6%→87% across bins on grid noise).
The **envelope is the deliverable**, not a single number. Collapsing it requires the per-galaxy detection floors /
lowest-detected SFR per bin from the actual Nakajima+Lisiecki catalogs (next step) — not just the medians in the draft.

## Disposition

**#3 (scaling relations z0→JWST): REFRAME, do NOT fully shelve.**
The SFMS elevation is materially inflated — central ~0.4–0.6 dex (~half) at z≈3.5–5.4, and the lower envelope at
z<6 reaches ~0, i.e. **pure-selection is not excluded below z≈6**. So the "+0.8 dex elevation → rapid early enrichment
toward an evolving equilibrium" narrative is **not earned from the SFR sector**: at z<6 the elevation may be mostly
artifact. What survives robustly is the **z>6 elevation (~1.3 dex physical residual)** — genuinely large even after the
max plausible selection shift. Fix: forward-model the actual per-catalog detection floor and quote a selection-corrected,
bounded elevation; demote the equilibrium-scenario language. (The −0.4 dex MZR deficit is a separate legitimate
differential and is NOT the selection casualty — keep it; cf. cycle1.)

**#6 (TNG calibration≠validation): SFR discrepancy SURVIVES and STRENGTHENS — not an artifact.**
Selection inflates the *observed* elevation UP toward TNG's internal growth; removing it pulls obs DOWN, **widening**
TNG's over-evolution. De-biased: z≈4.7 gap +0.41→~+0.46 (up to +0.73 in the aggressive-selection corner);
z≈5.4 gap +0.49→~+0.83. TNG internal growth (+1.30/+1.45/+1.61) is measured mass-matched without a line floor, so the
correct fair comparison is de-biased-obs vs raw-TNG-internal ⇒ the gap only grows. #6's load-bearing "TNG forms stars
too vigorously at high z" is therefore **conservative w.r.t. selection — a lower bound, not a dissolved result.** RETAIN it.
(Its separate mass-definition caveat — TNG 2R½ aperture mass vs SED mass, cycle1 — is the remaining fix, orthogonal to selection.)

## One-line portfolio verdict
Selection is a real ~0.4–0.6 dex inflator of #3's low-z SFMS elevation (reframe #3's SFR-evolution claim; z>6 signal survives),
but it does **not** rescue TNG — it makes #6's over-star-formation discrepancy larger. The highest-value fix repairs #3's
overclaim and simultaneously hardens #6.

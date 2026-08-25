# PREREGISTRATION SKELETON (DRAFT) — LONGO-AMPLITUDE TEST ON A LEVERAGE-CHOSEN FOOTPRINT

> **THIS IS A DRAFT SKELETON. NOTHING IN IT IS IN FORCE.** It becomes a preregistration only
> when its full text passes adversarial gates, every binding slot holds a receipt, and Duho
> signs the freeze.

Hwao, 2026-08-24 21:44 KST. Successor to the run declared inconclusive-by-power on footprint
geometry. Design authority: `SUCCESSOR_SCOPE_20260821.md` (seven requirements). Predecessor
text carried by quotation from `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
(sha256 `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`).

## Claim boundary (carried, unchanged in kind)

This tests Longo 2011's published **|A_L| = 0.0408, σ_pub = 0.011** at Longo's published axis
**n̂_L : (l, b) = (52°, 68.5°) ≡ (α, δ) = (217°, 32°)** [V3 line 124, by quotation]. It does not
test A ≈ 0.02, Shamir, BHU, or whether the sky is isotropic. A null rejects only the published
amplitude at the published axis under the preregistered rule. **Fixed-axis only** — a free-axis
scan is a different study (Duho may direct otherwise at freeze; default is fixed).

## F-slots (each item cites the scope-note requirement it implements)

- **F-1 Population & selection** [req 1, 2]. Parent: Legacy Surveys south, full footprint —
  release = DR11 if its photo-z catalog exists at freeze, else DR10.1 (decision date 2026-09-05).
  Galaxy cuts: Cut-6 as frozen in V3, carried by quotation at freeze time (incl. `flux_r > 0`,
  `dered_mag_r < 17.7`). Selection is POLAR-by-leverage: bricks ranked by |cosθ| about n̂_L
  descending; acceptance proceeds in that order. **Contiguous-BRICKID selection is banned.**
  Stopping rule is written on leverage, not count: accepted-sample `N · Var(cosθ) ≥ L_min`
  (slot; L_min ≥ 33,334 so that N_eq = 3·L ≥ 100,000), computable from positions alone — no χ,
  no image byte, involved in selection at any point.
- **F-2 Monopole** [req 4]. Report-monopole-first stays. The primary estimator is centred, so
  the monopole is projected out by construction, not merely reported.
- **F-3 Primary statistic & sidedness** [req 4, 5, 7]. `Â_c = Σ(s−s̄)(c−c̄) / Σ(c−c̄)²` on the
  accepted sample; null by exact permutation of s; variance `Var(s)·Var(c)/(N−1)`.
  **Sidedness is declared here, once: one-sided at Longo's oriented sign** (matching F-5/F-6 of
  the predecessor), and the harness must implement exactly this line — the two-sided
  `sim_power.py` seam is closed by regenerating the harness, not the document.
- **F-4 Normalisation** [req 3]. `Â = D̂ / E[cos²θ]` evaluated as a **procedure on the accepted
  sample**. The constant `3·D̂` (full-sky special case; +42.76% silent inflation on the dead
  footprint) is banned from every formula and every receipt.
- **F-5 Sign convention** (carried). East-of-North winding; the mandatory synthetic
  absolute-sign anchor runs before any real image, receipted in its slot.
- **F-6 Decision regions** (carried in form; thresholds to gate):
  REPRODUCED-LONGO: permutation p < 0.001 AND Longo's sign AND |Â_c − 0.0408| ≤ 3·σ_comb.
  EXCLUDED-AT-AMPLITUDE / INCONCLUSIVE-BY-POWER: as V3, with the power gate below.
- **F-7 Detection floor** (carried). Labelling-accuracy floor a = 0.85; no Â_c below the
  evaluated floor is nameable as a detection.
- **Power gate** [req 6 — the repair that would have caught the predecessor]. Explicit named
  inputs: `N_accept`, **accepted-sample `Var(cosθ)`** (measured on actual accepted positions,
  never a uniform-sphere assumption), floor a, sidedness. Requirement: ≥95% power at
  |A_L| = 0.0408. Fails → INCONCLUSIVE-BY-POWER before unblinding, as the predecessor proved
  the off-ramp works.

## Binding slots (skeleton; each needs a receipt before freeze)

| slot | content | status |
|---|---|---|
| BS-1 | release choice (DR11/DR10.1) + catalog provenance | open — Duho + Sep 5 rule |
| BS-2 | selection receipt: brick list, per-brick cosθ, accepted N, Var(cosθ) — **blind-doubled** (two implementations, spec-only) | pipeline running (gpt1 inventory, gpt2 calculator) |
| BS-3 | instrument: weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry identity — carried untouched | receipts exist in predecessor tree |
| BS-4 | synthetic absolute-sign anchor rerun under this prereg | open |
| BS-5 | power-gate receipt with the four named inputs | open — after BS-2 |
| BS-6 | transport approval: manifest sha, byte ceiling, producer checksum list per release | open — AFTER freeze only |
| BS-7 | sidedness harness identity: the harness's declared test == F-3's sentence | open |

## Order of operations (nothing right of an arrow starts before its left is receipted)

catalog inventory → paced catalog fetch → selection + Var receipt (blind-doubled) → power gate
→ gates (agy family-independent review, then gpt-5.6-sol + codex adversarial) → **Duho freeze
sign-off** → image manifest + approval → 3-stream gated transfer → cutter/χ → K-8-equivalent
crossing under this prereg's own conditions.

## What this draft never permits before freeze

No image bytes. No χ read. No sky statistic over any real spin measurement. The predecessor's
sample stays sealed and is absorbable by this design only if it remains sealed.

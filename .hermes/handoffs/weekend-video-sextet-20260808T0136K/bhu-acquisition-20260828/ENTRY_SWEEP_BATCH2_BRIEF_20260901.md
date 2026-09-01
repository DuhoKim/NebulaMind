# BHU sweep — BATCH 2 brief (Tori, 2026-09-01) — reliable re-reads + one tie-break

**To:** agy (small, reliable) for 53/55/56/57; kimi for 45. INDEPENDENT. Do NOT read another seat's result.
**Authority:** Duho RELAY: A(a), B(a), C(a). codex already reliably read all of these in batch 1; you are
the required reliable SECOND read (agy's batch-1 tail was invalid — wrong sources / hallucinated ids).
**Boundary:** verdict per entry; do NOT change any tier (tier-adjacent → returns to Duho).

## Duho's ruling A(a) — the tiering criterion (apply it)

A model whose interior is a **closed / positive-curvature (Ω_k<0)** universe earns QUALITATIVE-DIRECTIONAL
**only if the paper DERIVES closure as an output**. If it merely **ASSUMES** a closed FLRW (k=+1) ansatz,
closure is NOT a prediction → stays CONSISTENCY-ONLY. (A bare "the interior is closed" does not qualify.)

## The bar (same as batch 1)

Stronger tier needs an OBSERVATION-FACING prediction: CALIBRATED = number+threshold data could cross;
QUALITATIVE-DIRECTIONAL = a signed testable direction on an observable, derived from the model (incl. a
*derived* Ω_k<0 per A(a)). NOT earned by: above-Planck/validity-limit numbers; internal-consistency
parameters; borrowed-from-data values; or an *assumed* closed ansatz.

## Entries — EXACT sources (go straight to these; do not search)

Sources dir: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-reading-20260823/sources/`

| N | current tier | source file | your question |
|---|---|---|---|
| 53 | CONSISTENCY-ONLY | `1906.11824_clean.txt` ("Analysis of big bounce in Einstein–Cartan cosmology") | tier correct, or too weak? apply A(a) |
| 55 | CONSISTENCY-ONLY | `2007.06664_clean.txt` ("Asymptotically de Sitter universe inside a Schwarzschild BH") | tier correct, or too weak? apply A(a) |
| 56 | QUALITATIVE-DIRECTIONAL | `gaztanaga_mass_mnras.pdf` (Gaztañaga, "The mass of our observable Universe"; PDF — use pdftotext) | is DIRECTIONAL right, or too weak/too strong? |
| 57 | CONSISTENCY-ONLY | `smoller_temple_1997_clean.txt` ("General relativistic shock waves") | tier correct, or too weak? apply A(a) |
| **45** (kimi only) | CONSISTENCY-ONLY | `2210.15186_clean.txt` ("White hole cosmology and Hawking radiation from quantum cosmology") | **TIE-BREAK:** codex says the white-hole horizon mode-matching predicts an exterior Hawking-flux departure a far observer could detect (→ DIRECTIONAL); agy says the paper concedes it "may not be directly relevant to observable Universe" (→ CONSISTENCY-ONLY). Read it and rule. |

## Output — one section per entry

```
ENTRY <N>: <VERDICT_TOKEN>
- numbers: <key quantities, each tagged observational / internal / above-Planck-limit / borrowed / assumed-ansatz>
- deciding: <1–3 lines; for closure, state DERIVED vs ASSUMED per A(a); engage the derivation>
- receipts: <source>:<lines>
```
`<VERDICT_TOKEN>` ∈ { `TIER_CONFIRMED`, `TIER_TOO_WEAK_<PROPOSED_TIER>`, `TIER_TOO_STRONG_<PROPOSED_TIER>`, `UNDETERMINED_NEEDS_<resource>` }.
For entry 45, use `TIER_CONFIRMED` (agy's view: stays CONSISTENCY-ONLY) or `TIER_TOO_WEAK_QUALITATIVE-DIRECTIONAL` (codex's view).

## Discipline

Every number greppable in its source; quote `file:lines`. Absence claim = pattern + one missed class +
what you did about it (full read, not just grep). Do NOT change tiers. Do NOT read another seat's file.
- agy: OUTPUT your combined result (entries 53,55,56,57) to stdout.
- kimi: OUTPUT your entry-45 tie-break result.

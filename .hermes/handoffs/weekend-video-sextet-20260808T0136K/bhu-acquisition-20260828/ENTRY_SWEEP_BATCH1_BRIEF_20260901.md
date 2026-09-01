# BHU sweep — BATCH 1 brief (blind-double, Tori, 2026-09-01)

**To:** codex (fresh) + agy, INDEPENDENT blind-double. Do NOT read each other's result.
**Authority:** Duho, RELAY via Blanc ~16:12 ("Authorize the whole sweep now"). Sweep the remaining BHU
corpus. Same discipline as the entry-39 audit + RQ-A/B/C/D.
**Boundary:** produce a per-entry verdict + a tight case. **Do NOT change any tier.** Any tier-adjacent
outcome (a tier looks wrong) returns to Duho — flag it, do NOT assert it.

## The task (same as entry 39, applied to a list)

The sweep hunts an entry tiered **TOO WEAK** — one concealing a testable number+threshold (a would-be
CALIBRATED-FALSIFIER) or a signed directional prediction, filed as CONSISTENCY-ONLY (or a directional
one that is really calibrated). For EACH entry below: locate its pinned source, read it, and decide
whether the current tier is correct or too weak.

**The bar for "too weak" (a stronger tier needs an OBSERVATION-FACING prediction):**
- CALIBRATED-FALSIFIER = a number WITH a threshold observation could cross (state quantity, threshold,
  derivation, measurement).
- QUALITATIVE-DIRECTIONAL = a signed, testable direction on an observable, derived from the model.
- NOT earned by: numbers above Planck density / at a self-conceded validity limit; internal-consistency
  parameters (bounce conditions, minimum scale factors, matching constants); or values borrowed from
  the data they are compared against.

## Sources

All sources are pinned in:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-reading-20260823/sources/`
Locate each by author/year/arXiv id (some hints below). Cross-check the entry against the bibliography:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md`

## The 12 entries (current tier → your verdict)

| N | paper | current tier | source hint |
|---|---|---|---|
| 27 | Gaztañaga (2022), "How the Big Bang Ends Up Inside a Black Hole" | CONSISTENCY-ONLY | Gaztañaga; find by title/arXiv |
| 36 | Smoller & Temple (2000), "Cosmology with a shock-wave" | CONSISTENCY-ONLY | `smoller_temple_2000_clean.txt` |
| 40 | Popławski (2021), "Gravitational collapse of a fluid with torsion into a universe in a BH" (JETP 132) | CONSISTENCY-ONLY | Popławski 2021; find |
| 41 | Popławski (2021), "A nonsingular, anisotropic universe in a black hole" | CONSISTENCY-ONLY | Popławski; find |
| 45 | "White hole cosmology and Hawking radiation from quantum cosmology" | CONSISTENCY-ONLY | find by title |
| 46 | Fullana & Alfonso-Faus, "Quantization of the universe as a black hole" | CONSISTENCY-ONLY | `1111.1017_clean.txt` |
| 49 | Blau, Guendelman & Guth (1987), "Dynamics of false-vacuum bubbles" | CONSISTENCY-ONLY | `blau_guendelman_guth_1987_clean.txt` |
| 52 | "Big Bounce and Closed Universe from Spin and Torsion" (ApJ) | CONSISTENCY-ONLY | Popławski/ECSK; find |
| 53 | "Analysis of big bounce in Einstein–Cartan cosmology" | CONSISTENCY-ONLY | find by title |
| 55 | "Asymptotically de Sitter universe inside a Schwarzschild black hole" | CONSISTENCY-ONLY | find by title |
| 56 | Gaztañaga (2023), "The mass of our observable Universe" (MNRAS Lett 521) | QUALITATIVE-DIRECTIONAL | `gaztanaga_mass_mnras.pdf` |
| 57 | Smoller & Temple (1997), "General relativistic shock waves" | CONSISTENCY-ONLY | `smoller_temple_1997_clean.txt` |

## Output — write ONE combined file, a section per entry

For EACH entry, exactly this shape (keep it TIGHT — 3–6 lines each, this is a confirmation sweep):

```
ENTRY <N>: <VERDICT_TOKEN>
- numbers: <one line — the paper's key quantities, each tagged observational / internal / above-Planck-limit / borrowed-from-data>
- deciding: <1–3 lines — is any observation-facing number+threshold or signed prediction present? engage the derivation, not scoping>
- receipts: <source file>:<lines>
```

`<VERDICT_TOKEN>` is ONE of:
- `TIER_CONFIRMED` — current tier correct, no concealed stronger prediction.
- `TIER_TOO_WEAK_<PROPOSED_TIER>` — a number+threshold or signed prediction is concealed; name it. (Tier-adjacent → returns to Duho.)
- `UNDETERMINED_NEEDS_<resource>` — can't decide from the pinned source (e.g. source not found); name what's needed.

## Discipline

- Every number greppable in its source; quote `file:lines`. Engage the derivation (strict), not
  order-of-magnitude scoping.
- **Absence claim** (per entry, when you assert "no observable"): pattern used + one class it would miss
  + what you did to look for that class anyway (a full read, not just a grep).
- Do NOT change tiers. Do NOT read the other seat's result. Where a source can't be found, say so as
  `UNDETERMINED_NEEDS_SOURCE` rather than guessing.
- codex: WRITE your combined result to `ENTRY_SWEEP_BATCH1_codex_RESULT.md` in the lane dir.
  agy: OUTPUT your combined result to stdout.

# Sub-27 sweep — codex pass (Tori, 2026-09-01)

**To:** codex (reliable locator + auditor). Phase 1 of a blind-double; agy does phase 2 on your exact
source paths. **Authority:** Duho RELAY "sweep the rest below 27."
**Boundary:** confirm each entry's CURRENT tier, or flag it too-weak/too-strong. **Do NOT change any tier**
(tier-adjacent → Duho). If an entry has only an abstract / no full source, say `SOURCE-LIMITED` — do NOT
guess a tier from an abstract.

## Task

These sub-27 BHU entries were read + tiered earlier but not all blind-double-confirmed. For EACH: read its
pinned source (locate in the sources dir by author/year/arXiv/PII), and decide whether the CURRENT tier
holds. Apply the same bar as the 27-onward sweep, incl. Duho ruling **A(a)** (a closed/positive-curvature
interior counts as QUALITATIVE-DIRECTIONAL only if the paper DERIVES closure, not if it assumes a k=+1
ansatz). Some are already double-gated in the record — if so, just confirm efficiently and say so.

Sources dir: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-reading-20260823/sources/`
Bibliography (current tiers + source refs): `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md`

## Entries (current tier → your verdict)

| N | paper | current tier |
|---|---|---|
| 1 | Pathria (1972), "The Universe as a Black Hole," Nature 240 | (check record) |
| 2 | Good (1972), "Chinese universes," Physics Today 25(7) | (check) |
| 3 | Stuckey (1994), "The observable universe inside a black hole," AmJPhys 62 | (check) |
| 4 | Knutsen (2009), "The idea of the universe as a black hole revisited," GravCosmol 15 | (check) |
| 5 | Khakshournia (2010), "A note on Pathria's model…," GravCosmol 16 | THEORETICAL-OBSTRUCTION |
| 6 | Smolin (1992), "Did the universe evolve?" CQG 9 | QUALITATIVE-DIRECTIONAL |
| 9 | Popławski (2010), "Cosmology with torsion…" (PLB 694) | PROSPECT |
| 10 | Popławski (2012), "Nonsingular big-bounce cosmology…" (PRD 85) | CONSISTENCY-ONLY |
| 12 | Popławski (2025), "Gravitational collapse with torsion…" (IJMPA) | CONSISTENCY-ONLY |
| 13 | Frolov–Markov–Mukhanov (1989), PLB 216 | CONSISTENCY-ONLY |
| 14 | Frolov–Markov–Mukhanov (1990), PRD 41 (preprint held) | CONSISTENCY-ONLY |
| 16 | Pourhassan (2025), "Multiversal entropy & information…" NPB 1020 | PROSPECT |
| 18 | Dymnikova (1992), "Vacuum nonsingular black hole," GRG 24 | CONSISTENCY-ONLY |
| 19 | Dymnikova (2019), "Universes Inside a Black Hole…" Universe 5 | CONSISTENCY-ONLY |
| 23 | Gaztañaga (2020), "The size of our causal Universe" | QUALITATIVE-DIRECTIONAL |
| 24 | Gaztañaga (2022), "A peek outside our Universe" | QUALITATIVE-DIRECTIONAL |

## Output — WRITE to `ENTRY_SUB27_codex_RESULT.md`, a section per entry

```
ENTRY <N>: <VERDICT_TOKEN>   source=<the file you read, or NONE>
- deciding: <1-3 lines; apply A(a) for closure; engage the derivation>
- receipts: <source>:<lines>
```
`<VERDICT_TOKEN>` ∈ { `TIER_CONFIRMED`, `TIER_TOO_WEAK_<tier>`, `TIER_TOO_STRONG_<tier>`, `SOURCE-LIMITED` (abstract/no full text), `UNDETERMINED_NEEDS_<x>` }.

## Discipline
Every number greppable in its source; quote `file:lines`. Absence claim = pattern + one missed class +
what you did about it (full read). Do NOT change tiers. **Record which source file you read for each entry**
(agy will re-read those exact paths in phase 2).

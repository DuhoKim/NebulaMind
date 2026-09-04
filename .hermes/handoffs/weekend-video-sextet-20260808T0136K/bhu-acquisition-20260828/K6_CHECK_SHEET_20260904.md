# K6 — one-page check sheet

**Tori, 2026-09-04 16:45 KST.** For a human checking this without redoing it.

## The question
Entry 51 says a black hole's density cannot exceed the electron Cartan density, "**from which**" its minimum mass is
∼10¹⁶ kg. **Does that "from which" work?**

## The answer in one line
**Not from what the paper states** — the step needs a size-to-mass relation the paper never supplies, and different
admissible choices give floors differing by decades, or none at all.

## What is missing, precisely
A density ceiling constrains *density*. To turn it into a *mass* bound you need to know how volume grows with mass —
`V(M)`. **Entry 51 supplies no such relation**, and marks absent: which density (local? mean? proper or coordinate
volume?), which mass (ADM? Misner–Sharp? Komar?), which surface (event? apparent? trapping?), and the interior profile.
The paper itself says the full coupled equations must be solved (**L604–612**).

Receipt: `K6_routeA_codex.out` and `K6_ROUTEA_codex_RESULT.md` — route A derived the chain and stopped at exactly that
quantity, twice.

## The freedom, shown concretely

| reading of "the mass density of a black hole" | floor |
|---|---|
| Euclidean mean inside the Schwarzschild radius | **2.70 × 10¹⁴ kg** |
| proper-volume mean (factor 3/2) | **2.20 × 10¹⁴ kg** |
| **local** rest-frame density | **no floor at all** |

The third is not a strawman — it is what the paper's own justification says at **L629–632** ("a system of elementary
Dirac particles cannot be compressed to densities higher than the densities of its components"). A *local* bound puts
no floor on a mass without an assumed interior profile.

Receipt: `K6_routeB_claude.out`.

## The number, and the care it needs
The most natural reading gives `√(3c⁶/32πG³ρ_Ce) = 2.70 × 10¹⁴ kg` — **1.57 decades below the printed ∼10¹⁶ kg** and
outside the pre-declared match interval `10¹⁵–10¹⁷ kg`. Equivalently a 10¹⁶ kg black hole has mean density
`7.29 × 10⁴⁷`, not `10⁵¹`. Kimi re-checked all eight steps, Moonshot route, no-fallback control: all confirmed.

**This does NOT say the paper's number is wrong.** The paper never says which density it means, so there is no
completion to attribute to it and refute. It says what the record already said — **unreproduced from the stated
inputs** — now with a demonstration that the obvious reading does not reproduce it either.

## Two gate repairs that earned themselves within the hour
1. The gate widened class 3 to include the **stopping rule**. **Route A exited by exactly that path** — without the
   repair its outcome would have had no class.
2. The gate rewrote the deletion probe to delete the **field equations** rather than the load-bearing relation. Route A
   ran the corrected form and it **caught a circular proof** that would have passed the original.

## The seal audit — clean, and it was going to be reported either way
The prereg admitted that hashing prior exploratory work is tamper evidence, **not blinding**, and promised a log audit.
Done: no command in either seat's log reads `b13_floor_routes.py`, `AGATE_Q2_VERDICT.md` or `CGATE_Q2_VERDICT.md`;
every mention is the instruction text naming them. All four hashes unchanged. Both seats keep independent status.

## Controls
`C1` PASS/PASS · `C2` PASS/NOT RUN · `C3` PASS/PASS · `C4` PASS/PASS · `C5` PASS/NOT RUN · `C6` PASS/PASS
(route A / route B). Route B's NOT RUN entries are honest: C5 needs a unique-floor proof and route B filed none.

## What did NOT move
No tier, warrant token, standing or stamp. Entry 51 keeps `W_UNDERIVED`.

## Receipts (sha256)
```
K6_ECKS_FLOOR_PREREG_20260904.md  74f1b0ba…9ecc72
K6_routeA_codex.py / .out         727779b2…308576 / 499376fb…514504
K6_routeB_claude.py / .out        11dfbc35…c829539 / 23e422c5…dbd3e2
```
Full hashes in `K6_RESULT_20260904.md` §8. Gate: `K6_PREREG_GATE_20260904_agy.md`.

K6_CHECK_SHEET_COMPLETE

# RQ-D mapping brief — the Easson obstruction map (BHU Lane 2, task 2)

**From:** Tori · **To:** codex + agy (independent, blind-double) · **2026-08-31**
**Boundary:** produce the map + source-grounded reasons. **Do NOT re-tier any entry** — retiring or
restricting a row is Duho's tier call. Published-base-layer, receipts discipline, lane-dir only.

## The one-sentence task

Entry 22 (Easson 2026, "Obstructions to Minimal Regular Black Hole Cosmologies," PRD 114 044077;
source `bhu-reading-20260823/sources/2606.25023_clean.txt` + `ar5iv_2606.25023.html`) proves a no-go.
**For each published BHU interior below, determine whether Easson's result KILLS it, RESTRICTS it, or
SPARES it — and name the exact Easson clause and the exact interior property that decides it.**

## Easson's result, precisely (from entry 22's gated domain note — verify against the source)

- **Proposition 1** — excludes identifying the natural *trapped* slicing with *exact* FRW. (Needs no
  matching, asymptotics, or shell assumption.)
- **Proposition 2** — bounds *nondegenerate, comoving, no-shell, closed-FRW* daughters of *static,
  asymptotically flat, finite-ADM* parents. (Independent of the regular-core details.)
- **Theorem 1** (headline) — the flat/open limb *additionally* assumes curvature regularity, regular
  affine ends, and ANEC.
- **Expressly-stated escape routes (author-named, OUTSIDE the result):** (i) a **shell** /
  surface term (Darmois–Israel *with* a surface layer — note Easson's own conditions are the
  *no-shell* ones); (ii) **modified asymptotics** (parent not static-asymptotically-flat, e.g. a de
  Sitter or cosmological exterior); (iii) **non-FRW or non-comoving** interior evolution; (iv)
  **added bulk stress-energy** (e.g. effective torsion/spin stress).

## The interiors to classify (all in the record + pinned)

| entry | paper | pin hint |
|---|---|---|
| 11 | Popławski 2016, "Universe in a black hole in Einstein–Cartan gravity" (ApJ 832, 96) | Einstein–Cartan torsion; check bulk-stress / non-FRW escape |
| 18 | Dymnikova 1992, "Vacuum nonsingular black hole" (GRG 24, 235) | de Sitter core, asymptotically flat |
| 19 | Dymnikova 2019, "Universes Inside a Black Hole with the de Sitter Interior" (Universe 5, 111) | de Sitter interior |
| 20 | Bronnikov–Melnikov–Dehnen 2007, "Regular black holes and black universes" (GRG 39, 973) | "black universes"; check asymptotics/FRW |
| 21 | Roupas 2022 (EPJC 82, 255) | **has a pressure shell** on the horizon — check the shell escape |
| 25 | Gaztañaga 2022, "The Black Hole Universe, Part I" (Symmetry 14, 1849) | closed-FRW bounce; the record already finds it **no-shell** (2505.23877: "No additional surface term…") |
| 26 | Gaztañaga 2022, "The Black Hole Universe, Part II" (Symmetry 14, 1984) | as 25 |

## Deliverable (`RQ_D_<seat>_RESULT.md` in this lane dir)

1. **The map — a table**, one row per interior, columns:
   `entry | KILLS / RESTRICTS / SPARES | deciding Easson clause (Prop1/Prop2/Thm1) | deciding
   interior property | source receipt (quote + file)`.
   - **KILLS** = the interior satisfies *all* hypotheses of an Easson obstruction and takes *none* of
     the named escapes → the construction as published cannot work.
   - **RESTRICTS** = Easson bounds/constrains it but a stated escape or a missing hypothesis leaves a
     surviving regime → name the surviving regime.
   - **SPARES** = the interior takes a named escape (shell / modified asymptotics / non-FRW /
     added bulk stress) → say which, with the source line that establishes it.
2. **Ownership-of-proof discipline (per the corpus rule):** a KILL requires the interior to actually
   meet *every* Easson hypothesis — verify each (closed-FRW? comoving? no-shell? static
   asymptotically-flat finite-ADM parent? exact-FRW trapped slicing for Prop 1?). Do not assert a
   kill from the headline; check the hypotheses one by one. A SPARE requires *exhibiting* the escape
   in the interior's own text, not asserting it.
3. **The meta-count:** how many of the seven does Easson **kill**, how many **restrict**, how many
   **spare** — this is the theory-internal payoff (one theorem retiring/bounding several rows). State
   it as a count with the per-row basis, NOT as a tier action.
4. **Honesty:** where the classification depends on a hypothesis you cannot verify from the pinned
   sources (e.g. the external completeness theorem the domain note flags as unverified), say so and
   mark that row **UNRESOLVED**, do not force it.

## Receipts

- Easson: `2606.25023_clean.txt` / `ar5iv_2606.25023.html`. Each interior: its bibliography entry +
  pinned source in `bhu-reading-20260823/sources/`. Every KILL/SPARE must cite a source line
  (greppable) from *both* Easson (the hypothesis) and the interior (the property).
- The record's prior findings you may build on but must re-verify: the Gaztañaga bounce is **no-shell**
  (potentially in Prop 2's scope, NOT spared by the shell escape); Roupas has a **pressure shell**
  (potentially spared); the Israel-junction "escape" for the matching series was already **refuted**.

**Blind-double:** codex and agy classify independently; do not read each other's result. Tori
reconciles per-row. A per-row disagreement on KILLS/RESTRICTS/SPARES is a seats-disagree item for
Tori/Duho, not something to average.

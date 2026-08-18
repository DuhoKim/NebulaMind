# YUI — v2 script + storyboard brief

Read `SEXTET_BRIEF_V2.md` in this directory first; it binds everything here. Your deliverables,
written into THIS directory:

1. `SCRIPT.md` — same format as `../bhu-neutron-star-explainer-20260817/SCRIPT.md`
   (`## Panel NN — <assertion heading>` + one narration paragraph per panel; a Status line
   marked draft-for-Lana; the scope line; a Handoff boundary section).
2. `STORYBOARD.json` — schema `nebula-explainer-storyboard-v1`, exactly as
   `../bhu-neutron-star-explainer-20260817/STORYBOARD.json`: per panel `id`, `planned_seconds`,
   `word_count`, `assertion_heading`, `narration` (byte-identical to SCRIPT.md), `narration_sha256`,
   `story_function`, `authority_sections_for_lana`, `viewer_text_closed_world` (first entry = the
   heading), `semantic_beats`, `forbidden_inferences`, `visual_plan_owner: "Goru"`. Update
   `script_contract` (panel_count, word counts, planned_total_seconds ≤ 355) and keep the
   `authorization` block all-false. Set `status` to a draft token awaiting Lana/Goru/Kun.

When done, also write `YUI_DONE.md` with one line: `YUI_V2_DRAFT_COMPLETE` plus any notes.

## The two jobs (Duho's words are in the sextet brief)

1. **Easier.** Assume zero prior physics. Short sentences (aim ≤ 18 words). Define every term at
   first use or drop it. Prefer "a proposed change of state in ultra-dense matter" over naked
   "kaon condensation" (you may name it once, immediately glossed). A metaphor is welcome when it
   asserts nothing factual beyond the mapped claim.
2. **Walk the BHU chain.** v1 jumped straight to "the Brown–Lee–Rho chain". v2 must first say
   what the black-hole-universe idea is, what cosmological natural selection adds, and why that
   lands on neutron stars — each step on a gated source line.

## Source text you write AGAINST (verbatim, so you never quote from memory)

From P (`../reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md`), §1.4, lines 260–264:

> Smolin's CNS (from "Did the universe evolve?", Class. Quantum Grav. 9, 173 (1992) [VERIFY], and
> *The Life of the Cosmos*): universes reproduce through black holes with slightly mutated
> constants, so the constants should be near-optimal for black-hole production. Its stated
> falsifiable consequence: the maximum neutron-star mass should sit low, via the Brown–Bethe
> kaon-condensate equation of state — M_max ≈ 1.5 M☉

From P, §0 lines 145–146: "There is no single black-hole-universe model. There are at least five
distinct programmes that do not agree with each other".

From P, §1.1 lines 171–176 (Pathria 1972, Nature 240, 298 — the accessible abstract): "a closed
universe with uniform density is not only inside a black hole but is permitted to oscillate
within it". **Body claims are excluded (V11); only the abstract-level statements P 180–182
characterises are usable: a radius condition, oscillation, bounded expansion, dated 1972.**

From A (`../bhu-mass-adjudication-20260817/C08_MASS_ADJUDICATION_20260817.md`), lines 24–29 — the
Brown–Lee–Rho 2008 abstract, complete:

> "It is argued that a well measured double neutron star binary in which the two neutron stars
> are more than 4% different from each other in mass or a massive neutron star with mass
> M ∼> 2 M⊙ would put in serious doubt or simply falsify the following chain of predictions:
> (1) nearly vanishing vector meson mass at chiral restoration, (2) kaon condensation at a
> density n∼3n₀, (3) the Brown-Bethe maximum neutron star mass M_max≈1.5 M⊙ and (4) Smolin's
> 'Cosmological Natural Selection' hypothesis."

Every number you may use is in A §3–§5: J0740+6620 2.08 ± 0.07 (clears 2.00 at 68.3%, not 95.4%);
3 qualifying systems ≥ 8σ above 1.5; J1913+1102 1.599 ± 0.008 / 1.290 ± 0.008 → 19.3 ± 0.7%
vs the 4% limit, nearly 5× the threshold, 95.4% interval above 4% by a wide margin; asymmetry
published 2020, sharpened by the 2026 timing update; criterion hash-sealed before the harvest;
He-red-giant caveat found after sealing, verdict invariant. Read A yourself; do not trust this
summary where it and A differ — A wins.

## Suggested arc (you own the wording; keep the count 9–10 panels)

1. Verdict-first (≤ 72 words, done by ~35 s): the question, the scope label, what was done
   (sealed rule → published pulsar measurements), the result (fails its own second test), the
   boundary (not the whole family).
2. What the idea is: universes inside black holes; explored since at least 1972; a family of
   at least 5 disagreeing programmes, not 1 theory. (Definitional black-hole sentence → Lana
   D-row, or cut.)
3. Cosmological natural selection: reproduce-through-black-holes, slightly mutated constants,
   near-optimal for black-hole production — and therefore checkable. (P §1.4.)
4. The bridge: its stated falsifiable consequence — the neutron-star mass ceiling should sit
   low, ≈ 1.5 times the Sun's mass, via the proposed ultra-dense-matter route. (Definitional
   neutron-star sentence → D-row, or cut. v1's mapped "Their masses can be measured through
   pulsar timing." is reusable.)
5. The 2 named tests, joined by "or" — either counts. (A 24–29, 147–150.)
6. Test 1 outcome: heavy-star limb → serious doubt, not strict falsification; literal 1.5
   ceiling contradicted by 3 systems. (A 92–99, 131–132.)
7. Test 2 outcome: PSR J1913+1102, 19.3 ± 0.7% vs 4% — the decisive pair; published since 2020.
   (A 101–106, 122–125, 156–157.)
8. The sealed rule: why the answer can be trusted; caveat found after sealing; verdict
   invariant. (A 11–16, 54–58, 108–115.)
9. What it means for BHU: per-link deaths and survivals; CNS loses its flagship prediction but
   is not refuted; the family of ≥ 5 programmes stands. (A 131–142; L C02.)
10. Close on the verdict: the numbers are the pulsar community's; the chain offered a clean
    test and fails by the second rule its own authors wrote. (A 122–125, 154–158.)

Reuse v1 sentences (already mapped) wherever they serve; v1's Panel 02 FLAG history: "They are
compact remnants" was cut as unsourced — do not reintroduce unsourced definitional clauses.

## Hard constraints

Total narration ≤ 730 words. Panel 01 ≤ 72 words. Numbers as digits. "times the Sun's mass".
Must-not-say list in the sextet brief applies to every sentence. Do not fetch anything; you work
from the local gated files only. Do not touch `portal.nersc.gov`. Write only into this lane
directory.

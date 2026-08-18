# Definitional sources — BHU explainer v2

**Lana (claim-boundary seat), 2026-08-18 KST.** Pinned sources for the v2 script's
definitional/textbook sentences, per `SEXTET_BRIEF_V2.md` §"New-claims policy" (cut or sourced,
never softened). Allowed hosts only (NASA public pages, ar5iv). Access datetimes stamped with
`date` at fetch time: all fetches 2026-08-18 between 17:34 and 17:36 KST (08:34–08:36 UTC).
Local copies live in `definitional_sources/` here; verify the SHA-256 before relying on one.
`portal.nersc.gov` was not touched. One additional fetch (science.nasa.gov neutron-star page)
was discarded unused — its text is JS-rendered and not quotable from the saved HTML; it is
cited nowhere.

## D1 — what a neutron star is

- **Backs script sentence:** Panel 04, "A neutron star is an ultra-dense object left after
  some stars collapse."
- **Source:** NASA Goddard Space Flight Center, *Imagine the Universe! — Neutron Stars*
  (public NASA education page).
- **URL:** https://imagine.gsfc.nasa.gov/science/objects/neutron_stars1.html
- **Accessed:** 2026-08-18 17:35 KST (2026-08-18T08:35Z), via `date`.
- **Local copy:** `definitional_sources/nasa_imagine_neutron_stars.html`, SHA-256
  `b7519fdff44a53976f5d0e084ad98a89ad8cf7b25925558ca519ae8ad8a0c678`.
- **Verbatim quotes:**
  > "Neutron stars are formed when a massive star runs out of fuel and collapses."
  > "If the core of the collapsing star is between about 1 and 3 solar masses, these
  > newly-created neutrons can stop the collapse, leaving behind a neutron star. (Stars with
  > higher masses will continue to collapse into stellar-mass black holes.)"
  > "This collapse leaves behind the most dense object known – an object with the mass of a
  > sun squished down to the size of a city."
- **Coverage:** "left after some stars collapse" ← quotes 1–2 ("some" is load-bearing and
  correct: only ~1–3 M☉ cores stop there; heavier cores continue to black holes). "ultra-dense"
  ← quote 3 ("the most dense object known") — understatement in the safe direction.

## D2 — what "physical constants" means

- **Backs script sentence:** Panel 03, "Physical constants are numbers that describe how
  nature behaves."
- **Source:** J.-P. Uzan, *"Varying Constants, Gravitation and Cosmology,"* Living Reviews in
  Relativity 14 (2011) 2; arXiv:1009.5514, ar5iv rendering.
- **URL:** https://ar5iv.org/abs/1009.5514
- **Accessed:** 2026-08-18 17:35 KST (2026-08-18T08:35Z), via `date`.
- **Local copy:** `definitional_sources/ar5iv_1009.5514.html`, SHA-256
  `087b11ca620a4fbd6c217baaeab9af13010cd872de0a0e484ba84c49141cfdca`.
- **Verbatim quotes:**
  > "Fundamental constants are a cornerstone of our physical laws." (abstract)
  > "Fundamental constants appear everywhere in the mathematical laws we use to describe the
  > phenomena of Nature." (§1, first sentence)
  > "The numerical values of the fundamental constants are not determined by the laws of
  > nature in which they appear." (§7)
- **Coverage:** "numbers" ← quote 3 ("numerical values"); "that describe how nature behaves" ←
  quote 2 (constants are ingredients of "the mathematical laws we use to describe the
  phenomena of Nature"). The script's one-clause compression attributes the describing to the
  constants rather than to the laws they sit in; accepted as plain-language metonymy — fidelity
  note F9 in `CLAIM_LEDGER.md`.

## S1 — kaon condensation is a (proposed) phase transition in ultra-dense matter

- **Backs script sentence:** Panel 04, "The route used a proposed change of state in
  ultra-dense matter, called kaon condensation." (The sentence's existence claims map to A
  27–28; this row sources only the "change of state in ultra-dense matter" gloss.)
- **Source:** G.E. Brown, C.-H. Lee & M. Rho, *"Kaon Condensation, Black Holes and
  Cosmological Natural Selection,"* PRL 101, 091101 (2008); arXiv:0802.2997, ar5iv rendering —
  the same primary source authority A quotes at abstract/section level.
- **URL:** https://ar5iv.org/abs/0802.2997
- **Accessed:** 2026-08-18 17:34 KST (2026-08-18T08:34Z), via `date`.
- **Local copy:** `definitional_sources/ar5iv_0802.2997.html`, SHA-256
  `b806ad1ce94ea03409f47996afb309c1aee649d80f3775069af455db9070d2dc`.
- **Verbatim quotes (body text):**
  > "The BB scenario is based on kaon condensation as the most crucial phase transition in
  > compact stars."
  > "…the argument for the Brown-Bethe maximum neutron star mass M_max ≃ 1.5 M⊙ relies on the
  > condensation of kaons at ∼3 times the ordinary nuclear matter density n₀ as the first and
  > last phase transition in compact-star matter as the density is increased beyond n₀."
  > "If kaons do condense at ∼3n₀ as predicted…"
- **Coverage:** "change of state" ← "phase transition" (plain words for the same concept);
  "in ultra-dense matter" ← "in compact-star matter as the density is increased beyond n₀"
  (matter beyond nuclear density); "proposed" ← "as predicted" (the condensation is the
  source's theoretical prediction, not an observed fact).

## Smolin wording — decision

The brief left it to me whether to pin Smolin's own CNS wording (hep-th/0407213 or the 1992
CQG abstract) beyond P §1.4. **Not pinned.** Every CNS-mechanism sentence in the v2 script
(Panel 03, Panel 04 s1–s2) maps onto P 259–264 at line level with no residue; adding a second
CNS source would widen the authority surface without covering anything P does not.

— Lana, 2026-08-18 KST.

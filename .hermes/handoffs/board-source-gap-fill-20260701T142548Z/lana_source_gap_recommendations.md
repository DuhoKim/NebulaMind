# LANA — Top-20 Source-Gap Reasoning & Acquisition Strategy

Run: `board-source-gap-fill-20260701T142548Z`
Input packet: `paper_citation_snippet_verification_top20_20260701T141717Z`
Prepared: 2026-07-01 (KST). Lane role: high-reasoning source selection & claim-citation strategy.

> **Status: PASS** — reasoning lane complete. Nothing here is product/DB-ready. All arXiv IDs / DOIs below are **advisory from domain knowledge** and MUST be independently verified by Hermes/Goru for (a) exact identifier, (b) that the source text actually matches, and (c) source-**position** locking before any citation is used. Every top-20 unit remains **NO-GO** for DB/product.

---

## 0. Headline

- **9 units are source-gap-only, 11 are partial-with-gaps, 4 are docs-candidates.** The gaps cluster into ~9 physics families; a small number of **canonical review papers** unlock the majority of units.
- **Highest leverage:** two WD review acquisitions (magnetic-WD review + WD-evolution/cooling review) plausibly unblock ~9 of the 15 White-Dwarf-page gaps.
- **Corruption blocker:** **evidence 2215 must be quarantined** — its stored source text is unrelated number theory (primes/binary expansion), not white-dwarf physics. Do not cite it; re-fetch the real source.
- **Provenance risk:** unit **1002-R1 (DES w ≈ −0.85)** likely needs **rewrite/verify**, not a clean source fill — that exact headline number is not a standard DES result.

---

## 1. Top source-gap clusters

| # | Cluster (physics family) | Units | Right move |
|---|---|---|---|
| A | WD mass distribution / IFMR / single-star driver | 1009-R1, 1273-S1, 1273-S2 | **source fill** (mass-dist catalog + IFMR) |
| B | WD mass–radius / Earth-radius (~0.01 R⊙) | 1008-R1 | **source-position lock** in already-accepted MRR paper (+ optional Gaia MRR) |
| C | Cooling → faintness / luminosity function / cluster ages | 1010-S1, 1010-S2, 1015-D1, 1016-D1 | **source fill** (WD-evolution review) + partial rewrite on 1016 |
| D | Magnetic WD origins / variability / atmospheric diagnostics | 1014-K1, 1277-D1, 1278-D1, magnetic clauses of 1015-D1 & 1273-S2 | **source fill** (one magnetic-WD review) |
| E | H-atmosphere ionization/opacity + cooling processes (photon/ν/axion) | 1013-S1, 1013-S2, 1275-X1 | **source fill** (DA atmosphere + evolution review + axion) — **and fix ev2215** |
| F | WD discovery history / Luyten timeline | 1007-X1 | **source fill** (history-of-astronomy source) |
| G | Dark-energy: DES *w*, Euclid/SKA forecasts, dynamical DE | 1002-R1, 1003-K1, 1271-D1, 1267-X1 | **mixed**: 1002 rewrite/verify; 1003 fill-or-drop-SKA; 1271/1267 position-lock |
| H | Supernovae: SN Ia standardization systematics; GRB–SN link | 1243-R1, 1247-R1 | **source fill** (SN Ia systematics; GRB-SN review) |
| I | GRBs: short-GRB↔merger; jet energetics | 1184-S2 (fill), 1184-S1 (position-lock) | **source fill** (short-GRB review) |

Docs-candidates that need **source-position locking, not acquisition:** 1011-K1, 1271-D1, 1267-X1, 1184-S1 (all currently abstract-level only).

---

## 2. Prioritized source-acquisition targets (ranked by units unlocked)

Confidence = my expectation the paper exists & fits; **Goru must confirm the exact ID and text.**

**T1 — Magnetic white dwarfs (review).** Ferrario, de Martino & Gänsicke 2015, *"Magnetic White Dwarfs"*, Space Sci. Rev. 191, 111. `arXiv:1504.08072`. Search: `Ferrario de Martino Gansicke 2015 magnetic white dwarfs review`.
 Unlocks: **1277-D1, 1278-D1, 1014-K1**; supports magnetic clauses of **1015-D1, 1273-S2**. *(≈5 units — highest leverage.)* Confidence: high.

**T2 — WD evolution & cooling (review).** Althaus, Córsico, Isern & García-Berro 2010, *"Evolutionary and pulsational properties of white dwarf stars"*, A&ARv 18, 471. `arXiv:1007.2659`. Search: `Althaus Corsico Isern Garcia-Berro 2010 white dwarf evolution review`.
 Unlocks: **1010-S1, 1010-S2, 1275-X1** (photon cooling, neutrino losses, crystallization/phase separation); supports **1015-D1, 1016-D1**. *(≈5 units.)* Confidence: high.

**T3 — DA hydrogen-atmosphere model (replaces corrupt ev2215).** Tremblay & Bergeron 2009, *"Spectroscopic Analysis of DA White Dwarfs…"*, ApJ 696, 1755, `arXiv:0902.4182`; **or** Koester 2010, *"White dwarf spectra and atmosphere models"*, `arXiv:0812.0482`. Search: `DA white dwarf hydrogen atmosphere ionization opacity model Koester Tremblay Bergeron`.
 Unlocks: **1013-S1, 1013-S2** and **replaces the poisoned evidence 2215**. *(2 units + corruption fix — treat as high priority despite lower count.)* Confidence: high.

**T4 — Initial–Final Mass Relation.** Cummings, Kalirai, Tremblay, Kilic & Bergeron 2018, *"The White Dwarf Initial–Final Mass Relation…"*, ApJ 866, 21. `arXiv:1809.01673`. Search: `Cummings 2018 white dwarf initial final mass relation`.
 Unlocks: **1273-S1**; supports **1009-R1**. Confidence: high.

**T5 — WD field mass distribution (SDSS catalog).** Kepler et al. 2007, MNRAS 375, 1315, `arXiv:astro-ph/0612277`; **or** Kleinman et al. 2013 (SDSS DR7 WD catalog), `arXiv:1212.1222`. Search: `SDSS white dwarf mass distribution peak 0.6 solar masses Kepler Kleinman`.
 Unlocks: **1009-R1** (clustering near 0.6 M⊙ and the bulk 0.5–1.2 range); supports **1273-S1**. Confidence: high. *(Note: the observed bulk may be narrower than "0.5–1.2"; see §3.)*

**T6 — GRB–supernova connection (review).** Woosley & Bloom 2006, *"The Supernova–Gamma-Ray Burst Connection"*, ARA&A 44, 507, `arXiv:astro-ph/0609142`; **plus** Cano et al. 2017, *"The Observer's Guide to the GRB-SN Connection"*, `arXiv:1604.03549`. Search: `Woosley Bloom 2006 supernova gamma-ray burst connection; Cano 2017 GRB supernova`.
 Unlocks: **1247-R1** (long-GRB ↔ broad-lined Type Ic). Confidence: high.

**T7 — Short GRBs (review) + GW170817/GRB170817A.** Berger 2014, *"Short-Duration Gamma-Ray Bursts"*, ARA&A 52, 43, `arXiv:1311.2603`; **plus** Abbott et al. 2017, *"GW170817 and GRB 170817A"*, `arXiv:1710.05834` (distinct from the GW-only 1710.05832 already accepted). Search: `Berger 2014 short duration gamma-ray bursts review`.
 Unlocks: **1184-S2** (direct short-GRB↔merger citation). Confidence: high.

**T8 — SN Ia standardization / systematics.** Scolnic et al. 2018 (Pantheon), ApJ 859, 101, `arXiv:1710.00845`; **and/or** Brout et al. 2022 (Pantheon+), `arXiv:2202.04077` (already partly in the DE base); dust systematics: Brout & Scolnic 2021, `arXiv:2004.10206`. Search: `Type Ia supernova standardizable candle systematics calibration dust Pantheon`.
 Unlocks: **1243-R1** (calibration/sample/dust caveats). Confidence: high.

**T9 — Euclid + SKA dark-energy forecasts.** SKA: Bacon et al. 2020, *"Cosmology with Phase 1 of the SKA"*, PASA 37, e007, `arXiv:1811.02743`. Euclid: Laureijs et al. 2011 (Definition Study), `arXiv:1110.3193`, or a 2024–2025 Euclid forecast/overview paper. Search: `SKA cosmology dark energy forecast Bacon 2020; Euclid weak lensing dark energy forecast`.
 Unlocks: **1003-K1** — *or* justify dropping "SKA" (the gap record explicitly allows "or SKA is removed"; see §3). Confidence: high (SKA), medium (which Euclid paper).

**T10 — WD discovery history.** Holberg 2009, *"The discovery of the existence of white dwarf stars: 1862 to 1930"*, JHA 40, 137; and Holberg 2005 (AAS history, "How Degenerate Stars…"). Search: `Holberg history discovery white dwarf stars Sirius B van Maanen Luyten`.
 Unlocks: **1007-X1** (Luyten/timeline as a sequence of steps). Confidence: high (these are the standard history references).

**T11 — Axion emission from WDs (constrained/hypothesized).** Isern, García-Berro, Torres & Catalán 2008, *"Axions and the cooling of white dwarf stars"*, ApJ 682, L109, `arXiv:0806.2807`; **or** Córsico et al. 2012 (G117-B15A axion bound), `arXiv:1205.6180`. Search: `white dwarf cooling axion emission bound Isern Corsico`.
 Unlocks: the **axion clause of 1275-X1** (keeps it framed as constrained/hypothesized). Confidence: high.

**T12 — DES SN cosmology (CONDITIONAL).** DES-SN5YR / DES Collaboration 2024, `arXiv:2401.02929` (and DES Y1 2018, `arXiv:1811.02374`). Search: `Dark Energy Survey supernova cosmology w constraint 5-year`.
 Unlocks: **1002-R1** *only if* a DES release actually reports *w* near −0.85 with an interval; otherwise this becomes a **rewrite** (§3). Confidence: low on the specific number — verify first.

**Secondary / optional (LF & radius depth):** Fontaine, Brassard & Bergeron 2001, *"The Potential of White Dwarf Cosmochronology"*, PASP 113, 409 (DOI 10.1086/319535) — LF/cooling-age/cluster ages, supports 1010/1015/1016; Tremblay et al. 2017 Gaia mass–radius, `arXiv:1611.00629` — exact ~0.01 R⊙ for 1008-R1; a cluster WD cooling-sequence paper (e.g., Bedin et al. NGC 6791 / M4, or Kalirai) for 1016-D1.

---

## 3. Claims to REWRITE (or defer) rather than source-fill

- **1002-R1 — DES *w* ≈ −0.85 (rewrite/verify; possible reject).** No standard DES headline reports exactly *w* ≈ −0.85 (DES Y1 ≈ −0.98 wCDM; DES-SN5YR ≈ −0.80 flat-wCDM). Recommend: verify against T12; if no match, **rewrite to the actual DES value with its model/interval**, or **defer** the number. Do not source-fill a number to a paper that doesn't state it.
- **1003-K1 — Euclid + SKA (partial rewrite fallback).** If a clean, mission-specific SKA dark-energy-forecast snippet isn't cleanly verifiable, **drop "SKA" and keep Euclid** (allowed by the gap's `needed_for_go`). Prefer full fill (T9) if both verify.
- **1016-D1 — cluster histories (scope rewrite).** The claim itself says broad cluster-evolution wording should "name the specific observable." Recommend **rewriting to one named observable** (e.g., cluster **WD cooling age**) bound to a specific cluster cooling-sequence source, rather than a broad "constrains cluster evolution" statement.
- **1184-S1 — energy budget "mass of a small star" (rewrite).** Keep the jet/energetics claim (docs-candidate) but **drop the numeric energy-equivalence** unless a source is separately verified (matrix already flags this).
- **1275-X1 — axion clause (conditional).** Keep axion as "constrained/hypothesized." If T11 can't be verified, **defer the axion clause** and keep photon/neutrino/crystallization (T2) only.
- **1010-S1 — "much fainter than main-sequence stars" (minor).** Textbook-true but needs a direct cooling-track/faintness source (T2). If none verifies at position, soften to a cooling-track statement rather than a population-comparison assertion.

---

## 4. Risks & unknowns

1. **Evidence 2215 is corrupted — quarantine it.** `evidence_id 2215`, `arxiv_id 1211.2455`, title *"The ionization state of hydrogen in white dwarf atmospheres"* (attributed Gianninas et al. 2012), but the stored intro text is number theory ("primes… base-2 expansion… Euclid… perfect numbers"). This strongly implies **the arXiv ID itself is wrong** (1211.2455 looks like a math preprint), not merely a bad excerpt. Action for Hermes: **do not cite; flag/quarantine the row; re-fetch the correct DA/H-atmosphere source (T3)**; separately audit how a math-paper body was attached to a WD title/summary (possible ingestion cross-wire — worth checking sibling evidence rows in the same batch).
2. **All 31 accepted snippets are abstract-level (`source_field=abstract`).** Even the 4 docs-candidates (1011-K1, 1271-D1, 1267-X1, 1184-S1) need **source-position locking** (intro/body/section) before product; abstract match ≠ citable position.
3. **Currency: Planck 2013 in 1267-X1.** `arXiv:1303.5062` (Planck 2013) is stale for DE constraints — recommend upgrading to **Planck 2018** (`arXiv:1807.06209`).
4. **Context-mismatch supports.** Some accepted "support" snippets come from Type Ia-progenitor papers used for WD mass/field claims (e.g., 1009-R1's field–mass snippet). Flagged in gaps; do not let a progenitor-context snippet be **sole** support for a general-population claim.
5. **arXiv/DOI confidence.** IDs here are from domain memory (knowledge cutoff Jan 2026). Treat as **search leads**, not verified citations — Goru should confirm exact IDs and that the text supports the specific clause before Hermes locks anything.
6. **"0.5–1.2 M⊙" interval (1009-R1).** The observed ordinary-CO bulk clusters tightly near ~0.6 M⊙; the full 0.5–1.2 interval may over-state the ordinary population. A catalog (T5) may support a **narrower** core with the tails as the flagged exceptions — expect a minor scope tightening, not a clean full-range fill.

---

## 5. Suggested acquisition order (to unblock the most units fastest)

1. **T1 (magnetic review)** and **T2 (evolution review)** — together touch ~9 WD-page units.
2. **T3 (DA atmosphere)** — unblocks 1013 **and** clears the ev2215 corruption.
3. **T4 + T5 (IFMR + mass distribution)** — 1009 / 1273 mass-distribution spine.
4. **T6 + T7 (GRB-SN + short-GRB)** and **T8 (SN Ia systematics)** — clear the Supernovae/GRB pages.
5. **T9 / T10 / T11** — Euclid-SKA, WD history, axion (each single-unit).
6. **T12 (DES)** last and **conditionally** — verify before treating 1002-R1 as fillable.

Parallel (no acquisition): **position-lock** the 4 docs-candidates; **upgrade Planck 2013→2018**; **quarantine ev2215**.

---

## 6. Safety statement

This lane performed **read-only** analysis of local docs/JSONL/Markdown only and wrote a single Markdown file to the assigned handoff path. **No** DB reads/writes or SQL, **no** migrations, **no** deploy/restart, **no** production config changes, **no** OpenClaw relay/mailbox/event, **no** runtime/source edits, **no** git commit/push/merge, **no** secrets or private credentials, and **no** external network mutation. No scholarly source was fetched or cited as verified — all identifiers are advisory search leads for Hermes/Goru to verify independently. Every top-20 unit remains NO-GO for product/DB.

LANA_TOP20_SOURCE_GAP_REASONING_DONE_20260701T142548Z

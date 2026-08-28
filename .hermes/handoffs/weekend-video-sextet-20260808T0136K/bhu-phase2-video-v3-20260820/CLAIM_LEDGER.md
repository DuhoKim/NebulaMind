# Claim ledger — "Born inside a black hole? The four papers, made plain" (v3)

**claude-seat (claim-binding seat), 2026-08-20 01:56 KST.** One row-group per panel covering
every narration claim, on-screen assertion/number, and design-system art brief; precedent =
the v2 ledger (its five repaired wordings are frozen facts here). **Zero fetches;
portal.nersc.gov untouched; zero silent rewrites.**

**Custody verified mechanically this session:** all 14 storyboard authority entries MATCH
(hashes + required first lines); all 16 narrations byte-identical to `SCRIPT.md` with correct
per-panel hashes; script sha matches the storyboard contract; **1,370 words ≤ 1,600; panel 01
= 79 ≤ 80**; 121 sentences (11.3 w/s average — v2's hot spots eliminated; worst panel now ≈
14 w/s). The four paper plots in `assets_v3/` are **byte-identical to the v2-pinned/source-
tarball values** (hashes re-verified). Source keys as in the v2 ledger (S/A1/A2/B1/B2/C +
gates), plus DS = `DESIGN_SYSTEM.md`, CA = `COMPREHENSION_AUDIT.md`.

**Result up front: 121 narration rows → 103 MAPPED, 16 framing/analogy-setup, 2 FLAG-adjacent
(both FLAGs are panel-level, below); 16 headings + title MAPPED; on-screen items MAPPED
except the FLAG-1 omission; art briefs: 4 claim-bearing in-image texts all MAPPED, 0
overshoots. FLAG count: 2.**

## 1. FLAG rows (exact repairs proposed; nothing rewritten)

**FLAG-1 — Panel 12: the parent specification is missing everywhere in the panel.** The
panel's two gated numbers (6.6×10²⁶ causality overshoot; the ε ≤ 10⁻²⁷-class ceiling with
branch clause) are **conditioned on a 10 M☉, a★ = 0.7 parent** (B2 §2.2; ε_max ∝ M^(−2/3), so
the numbers change with the parent). v2 carried "10-SOLAR-MASS PARENT · SPIN 0.7" on the
equivalent panel; v3's narration says only "a shrinking star" and the viewer-text list has no
spec chip. **Repair (either): add the viewer-text chip "10-SOLAR-MASS PARENT · SPIN 0.7", or
the narration clause "for a 10-solar-mass parent" attached to the 6.6×10²⁶ sentence (2 words
of budget headroom exist: 1,370/1,600).**

**FLAG-2 — asset custody: the generated image is unpinned and the pin file's paths are
stale.** `OVERNIGHT_BRIEF_P2V3.md` requires every generated image "pinned in
assets_v3/PINS_V3.sha256". Current state: `assets_v3/PINS.sha256` (name differs — cosmetic)
lists the four plots **via the v2 lane's absolute paths**, and `nbp_p01_cold_open.png`
(logged in GENERATION_LOG.md ✓) **has no pin at all**. Content custody of the plots is intact
(this-lane copies hash-match the pinned values — verified), so this is a bookkeeping FLAG,
not a provenance one. **Repair: regenerate the pin file over lane-local paths, adding
`d7991658f3d15aa1d6e329b1063612e866d1897f1478aea939c96ff215fa5f6f  assets_v3/nbp_p01_cold_open.png`,
and append each future generated image at generation time (Tori's step C).**

## 2. The v3-specific checks (kickoff items 1–6)

1. **Scope disclaimer absent everywhere: PASS** — mechanical sweep over SCRIPT.md +
   STORYBOARD.json + DESIGN_SYSTEM.md: zero hits on all four disclaimer forms.
2. **Analogies do not overshoot: PASS** — checked per §3; the load-bearing one: the
   spring/compressed-fabric art and "SPRING-LIKE PUSHBACK" chip are confined to Paper-1
   panels (03–04), where the smooth repulsive bounce IS the gated content (B1 §2.1, ä > 0
   receipted); the Paper-2 panels use only the paper's own plots, and the narration says
   "the reversal is written in by hand" (P08) — the inserted-cusp finding is carried, not
   smoothed. "Engine/manual" and "seed pod" analogies attribute claims to the papers
   ("proposed", "the story says") wherever the mechanism is unproven.
3. **Five frozen wordings present, correctly placed: PASS** — all five grep-verified verbatim
   (F1 in P05 after both edges are built; F2 in P11 after the bridge-needs build, with the
   B-17 quote byte-verbatim; F3 range in P01/P15/P16 — P01 renders "below" as "quieter than"
   inside the whisper metaphor with the frozen RANGE intact; F4 verbatim in P12; F5 as P15's
   heading). Placement matches the comprehension audit's plan.
4. **Plot honesty: PASS** — "contains no plots — the entire argument is equations" appears on
   exactly the three figure-less papers (P03 Paper 1, P09 Paper 3, P11 Paper 4; P04 keeps the
   card beside the spring art); Paper-2 panels show its two real figures; ground truth
   re-established from the pinned TeX in the v2 ledger and unchanged.
5. **Felt comparisons accurate: PASS with four fidelity notes (N1–N4, §4)** — every number's
   comparison audited; the standout exact one: "one grain in a
   billion-by-billion-by-billion grain cube" = (10⁹)³ = 10²⁷ exactly.
6. **Asset references: PASS structurally, FLAG-2 on pinning** — the storyboard references the
   four existing plot files (all exist, hash-verified) and routes generated art through named
   DESIGN_SYSTEM briefs, each brief carrying an explicit programmatic **fallback** (the
   brief's required pending-generation semantics live there); no dangling file references.
   The pin bookkeeping is FLAG-2.

## 3. Panel row-groups (bindings; framing rows are analogy set-ups asserting nothing)

| Panel | Sents | Verdicts | Key bindings |
|---|---|---|---|
| 01 | 7 | 2 framing, 5 MAPPED | verdict elements ← S 6–21/C §0; F3 range + whisper/stadium comparison (note N1); "ceiling" defined in-metaphor per CA |
| 02 | 6 | 3 framing, 3 MAPPED | nursery/birthmark = the question, attributed ("the story says", "proposed memory route"); "stop wherever a calculation stops" ← the audits' method |
| 03 | 8 | 2 framing, 6 MAPPED | spin/torsion glosses ← PLB pinned text (A1 P1–P5 context); "no plots" card ← ground truth; illustration staged per DS |
| 04 | 7 | 1 framing, 6 MAPPED | negative-density-means-outward ← PLB "generates gravitational repulsion" (B1 §2.1); spring analogy = Treatment-I gated content; 10⁻⁷⁰ felt line (v2 note N1 carried: both bracket edges lead at the 70th place) |
| 05 | 8 | 2 framing, 6 MAPPED | crowd analogy = coherent-total averaging (B1 §2.2); ×6 exact; **F1 verbatim, after both edges built** ✓; "6 neutrino species" ← PLB inputs |
| 06 | 5 | 1 framing, 4 MAPPED | erratum record-confirmed/content-unread ← G1 Check 2; quarantine+recompute ← A1 P13/D15/D16, B1 |
| 07 | 7 | 1 framing, 6 MAPPED | fermion-fields gloss ← PRD pinned text; Fig 1 walkthrough matches the inspected image (v2 ledger: cusp at a/acr = 1 ✓); attribution chip per DS |
| 08 | 7 | 1 framing, 6 MAPPED | both quotes byte-verbatim (PRD tex 113–114) with "THE PAPER'S OWN WORDS" chip on-screen ✓; CP gloss (v2 note N2 carried); ×730 ← B2 §1; "written in by hand" ← B1 §3.2/A1 D13; Planck marker ← V1 |
| 09 | 8 | 2 framing, 6 MAPPED | seed pod = A2 A-17-class attributed claim; fixed-compactness M→(size, heat) ← B2 §1; rotation-arrow-outside-map ← A2 focus 2.3; no-plots ✓ |
| 10 | 7 | 1 framing, 6 MAPPED | production-dial gloss + insensitivity ← A2 A-18; sketch-not-weld = A-17 conjecture + no-horizon-matching (one plain rendering); 1-meter ← A2 A-9; "about a doorway" (note N4) |
| 11 | 7 | 2 framing, 5 MAPPED | bridge-needs build (CA); no-plots ✓; **F2 verbatim + B-17 quote byte-verbatim** ✓; "no rotating model or axis calculation" ← A2 focus 2.3 |
| 12 | 9 | 2 framing, 7 MAPPED **+ FLAG-1 (panel-level omission)** | skater = conservation analogy; 6.6×10²⁶ ← B2 §2.2 (felt line note N2); uniform-bounce/treatments/order-of-magnitude glosses; **F4 verbatim**; grain-cube = 10²⁷ EXACT; Reading-2 sentence ✓; "CEILING · NOT A MEASURED TRANSFER" chip ✓; ε ≤ 10⁻²⁷ = permitted equation |
| 13 | 9 | 1 framing, 8 MAPPED | balloon-squeeze = shear gloss; same-rate/frozen ratio ← B2 §3 (a⁻⁶ = a⁻⁶ = permitted equation); "neither smooths nor creates" ✓; production underived ← A2 B-13; **"a condition, not a signal size" — the condition-not-amplitude guard, verbatim-class** ✓ |
| 14 | 9 | 1 framing, 8 MAPPED | fossil/BBN glosses ← pinned DS paper; 30× at 10 MeV ← the pinned bound verbatim; 45 orders (floor of 45.2–46.0 ✓) + ocean-molecule line (note N3); "different signs; both vanish" ← C §2 sign caveat |
| 15 | 8 | 1 framing, 7 MAPPED | coin-flip floor = 1/√N build (CA); 2×10¹² ← S7 pin; "theoretical best, not an instrument" ✓ verbatim guard; **F5 heading + F3 narration** ✓; band ladder per DS; caveat sentence ✓ (placement note W1) |
| 16 | 9 | 1 framing, 8 MAPPED | per-paper recap lines each bind (B1 §2.2 "strength not unique"; A1 H1/D13 "incompatible, inserted turn"; B2 §1/A2 A-18; A2 B-17; C §§1–2; F3 once); ends on ceiling/closed ✓ |

**Headings:** title + 16 all MAPPED (each is the panel's single built idea; F5 = P15's
heading verbatim; no heading carries an unconditioned number — P12's heading is numberless,
which confines FLAG-1 to the panel body).

**Art-brief rows (DS Part 2; generated art asserts nothing beyond its chip):**

| In-image text / geometry | Verdict | Binding |
|---|---|---|
| "SPRING-LIKE PUSHBACK" (Paper-1 art) | MAPPED | B1 §2.1 Treatment I (repulsive, smooth, receipted); confined to Paper-1 panels — does not touch the Treatment-II cusp finding |
| "PARENT MASS" / "STARTING SIZE & HEAT" (seed-pod art) | MAPPED | B2 §1 M→(a₀, T₀); narration carries the fixed-compactness condition; rotation excluded from the map on screen |
| "COSMIC SPEED LIMIT" (red-barrier art) + overshooting-arrow geometry | MAPPED | B2 §2.2 (v_rot < c wall; the conserved-J arrow overshoots — matches the gated 6.6×10²⁶ direction); quantitative ladder stays deterministic per DS |
| Floor-of-starlight-dots art ("millions of dots" representing 2 trillion) | MAPPED (illustration-only) | no in-image text; the 2-trillion claim lives in narration/deterministic overlays; chip mandatory per DS |
| All other briefs (cold open, collapsing star, twist fabric) | MAPPED (no claim content) | text-free; illustration chips specified; fallbacks defined per brief |

## 4. Fidelity notes

- **N1 — "10,000 to 100,000 times quieter … like a whisper buried under a stadium"
  (P01/P15/P16):** whisper→stadium ≈ 80–90 dB ≈ 10⁴–10⁴·⁵ in sound-pressure amplitude — the
  comparison is order-accurate under the amplitude convention (not power, which would be
  10⁸⁺); the frozen range is stated as digits first in every case. ✔
- **N2 — "billions of trillions past nature's red line" (P12):** 6.6×10²⁶ = 660,000× "a
  billion trillions" — the vague magnitude is floor-true (understates), and the exact figure
  is spoken in the same sentence before it. ✔
- **N3 — "like one molecule beside Earth's oceans" (P14):** ocean water ≈ 1.4×10²¹ kg ≈
  4.7×10⁴⁶ molecules; the gated margin is 45.2–46.0 orders — the simile is within ~1 order,
  paired with the floor-safe stated digit ("about 45 orders"). ✔
- **N4 — "exactly 1 meter wide—about a doorway" (P10):** standard doorway ≈ 0.9–1.0 m. ✔
- (Carried from v2: the 70th-decimal-place rendering; the CP-isotropy gloss.)

## 5. Watch-items for the packet gate (not FLAGs)

- **W1 — caveat placement:** the honest-caveat sentence sits in P15 of 16 — non-terminal ✓
  (P16 is caveat-free), but late; the comprehension audit pre-approved this with P13 named as
  the alternative if the gate wants it more central.
- **W2 — DS brief numbering:** DESIGN_SYSTEM Part 2 is numbered against v2's 12 panels (agy's
  own note); the storyboard's visual_notes reference briefs by NAME, which resolves the
  mapping — the builder (gpt3) must use the name-mapping, not panel numbers.
- **W3 — three-equation inventory:** ε ≤ 10⁻²⁷ (P12) and a⁻⁶ = a⁻⁶ (P13) are placed; the
  w = +1 vs w = −1 fork card is not referenced in any v3 panel's viewer text — permitted
  equations are a ceiling, not a quota, so this is compliant; noting so the gate doesn't
  hunt for it.

## 6. Boundary

Zero rewrites — the two FLAGs go to gpt1/Tori with exact repairs (a one-chip/two-word fix and
a pin-file regeneration); everything else binds clean. No fetches; portal.nersc.gov
untouched; writes in this lane only. Next: repairs, then kimi's packet gate (E) — hand it
FLAG-1/FLAG-2 closure plus W1–W3.

— claude-seat, 2026-08-20 01:56 KST.

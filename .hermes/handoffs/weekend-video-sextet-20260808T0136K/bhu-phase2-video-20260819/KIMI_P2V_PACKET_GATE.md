PASS_P2V_PACKET

# KIMI Phase 2 video — PACKET GATE

kimi (second reviewer, fresh one-shot), 2026-08-19 KST. Findings-only; nothing edited;
no other file written; zero fetches; portal.nersc.gov untouched. Method: grep-extraction
and mechanical recount only, against the packet and the gated authorities in
`../bhu-theory-phase2-20260819/`.

## (1) Structure contract — PASS

- Exactly 10 panels (storyboard ids 01–10; script panels 01–10). ✔
- Narration body recounted by this gate (headings excluded): **691 words ≤ 730**. Per
  panel: 71/68/69/62/52/65/75/68/73/88. ✔
- Panel 01 = **71 ≤ 72** words and verdict-complete, all five required elements present:
  the audit ("Overnight, we audited 4 published papers equation by equation, then derived
  the missing inheritance limit ourselves"), the ceiling ("the strongest defensible
  ceiling leaves the best sky signal roughly 10,000 to 100,000 times below even counting
  every observable galaxy"), the closed route ("the route stays closed: nothing
  observable"), the scope label ("Duho's personal side-interest, not a NebulaMind
  research programme"), the Reading-1 conditionality ("Under the published
  homogeneous-bounce reading"). ✔
- Assertion heading per panel: all 10 storyboard `assertion_heading` fields match the
  script headings exactly. ✔
- No divider cards: `divider_cards_allowed: false`; the 3 "divider" string hits are the
  constraint itself, a story function (`begin_act_2_without_divider`), and a semantic
  beat — no divider panel exists. ✔
- Final panel ends on the verdict: `ends_on_verdict` true only on panel 10; last sentence
  is "…the ceiling says the route stays closed." The scope-denial sits at the top of
  panel 10, not after the verdict. ✔
- The one caveat sentence sits mid-video: the exact `honest_caveat_sentence_exact` string
  appears in panel 05 of 10 and nowhere in panel 10. ✔

## (2) Mirror — PASS

One python3 comparison: all 10 SCRIPT.md panel bodies byte-identical to STORYBOARD.json
`narration` fields; all 10 per-panel `narration_sha256` recomputed and matching; all 10
`word_count` fields match; SCRIPT.md SHA-256
`82fc80e6…cacf` equals the storyboard `script_contract.sha256`. ✔

## (3) Ledger audit — PASS

Six spot-checks, each grep-extracted from the cited gated artifact; no overshoot found:

1. **×730 fork** (ledger 03|1 → B2 §1): `P2_DERIVATION_INHERITANCE.md:46` "the treatments
   disagree on the bounce state by ~×730 in density"; summary line 29 carries the ×727
   gate-rerun. Video says "about 730". ✔
2. **×6 averaging swing** (ledger 04|3 → B1 §2.2): `P2_DERIVATION_BOUNCE.md:72-73` "the
   ratio is exactly 6.00"; bracket `−8.82×10⁻⁷⁰ … −1.47×10⁻⁷⁰` (line 75); "published
   −8.6×10⁻⁷⁰ sits at the coherent edge (2.6% inside)" (line 77); "incoherent edge is the
   better-motivated one" (line 80). Video's "better-motivated independent edge is 6 times
   smaller" and "reproduces near the coherent edge" match or soften the source. ✔
3. **Ceiling with Reading-1 attached** (ledger 07|2–4 → B2 §2.2): line 85 table
   `1.5×10⁻²⁷ (I) / 1.4×10⁻²⁶ (II)`; line 78 overshoot `6.6×10²⁶`; lines 89–93 both
   readings with Reading 2 = "never reaches the homogeneous ECSK bounce … UNDERIVED";
   summary lines 13–17 direction: less signal, not more. Video P07 opens with the
   Reading-1 premise and closes with the underived Reading-2 sentence. ✔
4. **45-order BBN margin** (ledger 09|1 → C §1–2): `P2_CONFRONTATION.md:17` "44–46 orders
   of magnitude below", line 108 "margin 10⁴⁵"; summary line 50 "45.2–46.0". Video states
   the floor of the range — safe direction. ✔
5. **10⁻⁵ floor comparison** (ledger 09|4 → C §4): line 86 "8.5×10⁻⁶ / 7.6×10⁻⁵ of the
   all-sky 1σ floor"; line 21 "10⁻⁵–10⁻⁴ of the 1σ counting floor of a perfect all-galaxy
   survey". Video's "about 10 to 100 parts per million" rounds the signal UP (8.5→10,
   76→76→100) — anti-overclaim for the closure verdict; exact 8.5/76 ppm values are the
   on-screen text of the same panel. ✔
6. **Incompatibility quotes** (ledger 02|3 → pinned TeX): grep-verified verbatim at
   `sources/1111.4595/cosmology_torsion.tex:113-114` — "not self-consistent" and
   "violates the cosmological principle" — the PRD paper's own sentences about the PLB
   foundation; the video attributes them to the paper, not to us. ✔

Ledger hygiene:
- **Zero unresolved FLAG rows** — grep finds only the "0 FLAG" declarations. ✔
- **Number coverage**: every number in SCRIPT.md and VISUALS.md traces to a ledger row or
  fidelity note — 4 papers (01|1), 77 rows (F9; independently grep-recounted by this
  gate: A1 `^| [PD][0-9]` = 40, A2 `^| [AB]-[0-9]` = 37, 40+37 = 77 ✔), ×730 (F4), ×6
  (04|3–4), 3 quarantined/3 recomputations (05|2; P13/D15/D16 confirmed present in A1 at
  lines 104/132/133), 6.6×10²⁶ (07|2), 1-part-in-10²⁷ + 1-order branch span (F1; ×9.3 ≈
  1 order), 45 orders (F3), 10–100 ppm (F2), 2 trillion galaxies (09|5; summary line 11
  N = 2×10¹²), 10,000–100,000× (F5; 1/7.6×10⁻⁵ = 1.3×10⁴, 1/8.5×10⁻⁶ = 1.2×10⁵). The
  four on-screen paper identifiers match the A1/A2 custody blocks (PLB 694, 181 ·
  arXiv:1007.0587; PRD 85, 107502 · arXiv:1111.4595; ApJ 832, 96 · arXiv:1410.3881;
  IJMPA 40, 2544007 · arXiv:2509.11468). ✔
- Custody re-verified by this gate: all 11 storyboard authority SHA-256s MATCH their
  files; all four gate first lines equal their required tokens (PASS_P2_STAGE1 /
  PASS_P2_BOUNCE / PASS_P2_INHERIT / PASS_P2_CONFRONT). ✔

## (4) Must-not-say sweep — PASS

Sweep of SCRIPT.md + VISUALS.md for false/impossible/proved wrong/refuted/mockery/wrong:
the only hit is the required bounding denial in panel 10 ("We did not prove BHU cosmology
false, and we did not test the wider family") — a scope bound, not an assertion. The
incompatibility is attributed to the papers' own words (P02 narration + on-screen "THE
PAPERS' OWN WORDS · CLAIMS, NOT AUTHOR"). The author is treated clinically: journal/arXiv
identifiers only; the sole name occurrence is "Popławski chain" as the chain's standard
name. The frozen-ratio result is stated only as a condition ("ratio is frozen … zero
ironing-out … UNDETERMINED both ways"), never converted to an amplitude. The erratum is
described as record-confirmed/content-unread with recomputations in place — never as
resolved (matches Gate 1 Check 2: Crossref record RESOLVED, content UNVERIFIED-AT-GATE).
The floor is named as the theoretical all-galaxies best ("counting all 2 trillion
observable galaxies; it is a theoretical best, not an instrument"; on-screen
"SAMPLE-COMPLETE COUNTING FLOOR · NOT AN INSTRUMENT"). ✔

## (5) Visuals honesty — PASS

- ×730 fork: fully labeled vertical magnitude ladder/steps (P03). ✔
- 6.6×10²⁶ overshoot: fully labeled magnitude ladder (P07). ✔
- 45-order BBN margin: labeled 45-step ladder with endpoints (P09). ✔
- 10⁻⁵ floor gap: separate labeled 8.5–76 ppm scale against the all-galaxies tiling (P09). ✔
- No unlabeled log compression anywhere; P04 explicitly "No log compression" for the ×6
  linear ladder. ✔
- Equations on screen: grep of VISUALS.md finds exactly the three brief-authorized
  equations — "w = +1 vs w = −1" (P03), "a⁻⁶ = a⁻⁶" (P08), "ε ≤ 10⁻²⁷" (P07) — and no
  others. ✔
- Planck-caveat marker: both bounce drawings in P03 — the only panel that draws bounce
  states — carry the Planck-regime caveat marker (P08 draws a ratio balance, not a bounce
  state; the storyboard's binding beat list requires the marker only in P03). ✔
- VISUALS.md CLAIM-BEARING ADDITIONS section: **"None."** ✔

## Decision

All five gate checks pass. The packet (SCRIPT.md + STORYBOARD.json + CLAIM_LEDGER.md +
VISUALS.md) is structurally sound, mirrored, fully ledger-bound to the gated Phase 2
authorities with no overshoot, clean on every must-not-say rule, and visually honest.
Cleared for gpt3's build step. This gate authorizes no rendering, upload, publication,
or status change by itself — chain order governs.

— kimi, 2026-08-19 KST.

PASS_P2V3_PACKET — token kimi-p2v3-gate-20260820T0215K

kimi (second reviewer, fresh one-shot), 2026-08-20 ~02:15 KST. Packet gate (chain step E) per
OVERNIGHT_BRIEF_P2V3.md. Findings-only; zero edits; zero other writes; zero fetches;
portal.nersc.gov untouched. All checks below were recomputed mechanically this session
(shasum/python3), not transcribed from prior seats' reports.

## 1. Repair closure — both FLAGs CLOSED

FLAG-1 (panel-12 parent specification): CLOSED. The narration now carries the clause —
quoted: "A skater pulls in, spins faster; the 10-solar-mass, spin-0.7 parent faces that
extreme." — and the viewer-text chip is present, quoted: "10-SOLAR-MASS PARENT - SPIN 0.7".
Both repair options from CLAIM_LEDGER.md §1 were applied. Custody recomputed:
- SCRIPT.md sha256 = 7d88f058426c58b4776ba873a3ab345a20a3f2b71caed6ecf0f40abd1e3321ee —
  matches GPT1_B_DONE micro-pass.
- STORYBOARD.json sha256 = 963c31ba7f3374b5d37f960ee71bc155e43249bf65ddc5c6ba2c7eed5471a27d —
  matches micro-pass.
- Panel-12 narration sha256 = 67ebfd2749d90a30cca4eef01a94410464d1ded9f7b46c19a70417bd2e2717c5 —
  matches micro-pass; panel-12 words = 110 = budget (the "+2 words" headroom claim checks out:
  total 1,371 ≤ 1,600).

FLAG-2 (pin custody): CLOSED. assets_v3/PINS.sha256 is lane-local (bare filenames, resolved
against its own directory), 5 entries. Recomputed this session, one shasum per line:
- b93fb4b886c793b4db14f347bb49a628f2d5bb67c972e8b87fc536134a6cc514  assets_v3/prd_1111.4595_fig1_scale.jpg
- f659dfb67ecfab940d107ed48ba8e273335d2b83d46bd8e72e3f74cfd8c047d4  assets_v3/prd_1111.4595_fig2_temp.jpg
- af9efe93cbaa832f2ec782e689021f097768f6afa13e09303cc7409295a892cb  assets_v3/ds_1006.4166_comparison.png
- e34abd8af840017a715efc61a7a31943ad02de39a4d6e886edbe47e958d168b3  assets_v3/ds_1006.4166_prefac_Yp.png
- d7991658f3d15aa1d6e329b1063612e866d1897f1478aea939c96ff215fa5f6f  assets_v3/nbp_p01_cold_open.png
All five match PINS.sha256 entries exactly; the four plot hashes also match the storyboard's
paper_plots_closed_world records; the nbp hash matches the ledger's FLAG-2 repair spec.
Directory listing confirms exactly these 5 assets (+ PINS.sha256, GENERATION_LOG.md) exist.

## 2. Structure — PASS

- 16 panels in both SCRIPT.md and STORYBOARD.json (python parse, both ways).
- Narration total = 1,371 words, headings excluded (≤ 1,600 contract).
- Panel 01 = 79 words (≤ 80) and verdict-complete: question → ceiling metaphor → 4-paper
  audit → F3 range → "The route stays closed." → bridge. Contract met.
- Assertion heading on all 16 panels; storyboard headings byte-match SCRIPT.md headings 16/16.
- No divider cards: production_constraints.divider_cards_allowed = false; DESIGN_SYSTEM Part 1
  states "No divider cards."; every chapter is a content panel (chapter list inspected).
- Caveat: the exact caveat sentence appears in panel 15 only; panel 16 is caveat-free. P15-of-16
  is the audit's pre-approved position (§3 note; ledger W1 non-terminal). Mid-video standing
  rule met.
- Ends on verdict: final narration sentence is "The ceiling says the route stays closed." and
  panel 16 ends_on_verdict = true. Verdict first (P01) and last (P16) ✓.
- Scope-disclaimer grep sweep (SCRIPT.md + STORYBOARD.json + DESIGN_SYSTEM.md; forms:
  disclaim/scope-of-this/not-affiliated/does-not-represent/do-not-speak-for/on-behalf-of/
  educational-purposes/entertainment/not-professional/independent-audit/opinions-expressed):
  ZERO content hits. The single regex hit on the string "disclaim" is the JSON constraint key
  "scope_disclaimer_present": false — a flag name, not prose. PASS.
- Must-not-say sweep (false / impossible / proved wrong / refuted) over all 16 narrations: ZERO.

## 3. Comprehension contract — 5-panel sample vs COMPREHENSION_AUDIT.md — PASS

- P03 (audit §3: compass-needle fabric; "torsion" coined): analogy first — quoted: "Picture
  spacetime—space and time joined—as cloth woven from tiny compass needles." Mechanism follows.
  Terms defined at first use in-panel: spacetime, spin, Einstein-Cartan gravity, torsion. No
  numbers; no sentence over 2 ideas. ✓
- P05 (crowd analogy; ×6; F1 after both edges): analogy first — "A stadium clapping together is
  thunder; random claps mostly cancel." "species" glossed at first use. Both numbers felt-paired:
  "6 neutrino species … like six stadium sections clapping in step"; "exactly 6 times smaller—like
  cutting the same song to one-sixth volume." F1 lands only after "Those choices make the two
  labeled edges on screen." ✓
- P08 (family fight; quotes; ×730; inserted jump): rivalry built first ("Think of rival engines
  whose manuals reject each other"), then the two paper-owned quotes with cosmological-principle
  gloss, then "about 730 times, like bridge blueprints disagreeing on weight", then the closer:
  "The equations never stop collapse; the reversal is written in by hand." Planck scale defined at
  first use. ✓
- P12 (skater → wall; F4; Reading sentence): skater analogy precedes the causality number;
  "6.6 times 10 to the power 26" paired with "billions of trillions past nature's red line";
  uniform bounce / treatments / order of magnitude each defined in the sentence before F4 lands;
  F4 verbatim; "1 part in 10 to the power 27" paired with "one grain in a billion-by-billion-by-
  billion grain cube" — arithmetic exact: (10⁹)³ = 10²⁷. ✓
- P14 (fossil thermometer; both figures; 30×; 45 orders; sign caveat): analogy first; BBN, stiff
  component, radiation, and MeV all glossed at first use; "up to 30 times radiation, like thirty
  buckets beside one"; "about 45 orders of magnitude smaller—forty-five tenfold steps, like one
  molecule beside Earth's oceans"; sign caveat in one plain sentence ("Different signs; both
  vanish."). ✓
No sampled sentence carries 3+ claims. Average density per ledger custody: 121 sentences over
1,371 words ≈ 11.3 w/s (v2's 33 w/s hot spot eliminated by the split plan).

## 4. Mirror — PASS

One python3 comparison: all 16 STORYBOARD.json narration strings byte-identical to the SCRIPT.md
panel bodies; per-panel narration_sha256 fields all verify; per-panel word_count fields all match
recomputation; every panel within its audit budget (P06 55/55 tightest-ratio tie, P11 100/100,
P12 110/110 at the cap — all at-or-under, none over).

## 5. Frozen facts — PASS

- F1 "The printed value sits near the lined-up edge, so we carry both." — P05, after both edges ✓
- F2 two-clause spin sentence — P11, after the bridge-needs build ✓; the embedded B-17 quote
  "It would still be valid for a more realistic gravitational collapse of an inhomogeneous and
  rotating fluid." is byte-verbatim — verified against the pinned source
  sources/2509.11468/Collapse.tex:304 (exact match) — in both narration and the on-screen card.
- F3 "about 10,000 to 100,000 times" — exactly P01, P15, P16 (range intact every instance) ✓
- F4 "…caps inherited spin near 1 part in 10 to the power 27, with the treatment branches
  spanning roughly 1 order of magnitude." — P12 verbatim ✓
- F5 heading "Even the most generous signal is 10,000 times below the floor" — P15 heading,
  floor-true single value only in the heading ✓

## 6. Ledger sampling — 6 rows — PASS

1. Ceiling row (P12, the FLAG-1 row): Reading conditional sentence byte-exact vs the storyboard's
   reading_1_conditional_sentence_exact; parent spec now present (see §1); "CEILING · NOT A
   MEASURED TRANSFER" chip present; ε ≤ 10⁻²⁷ is a permitted equation. Binds.
2. Analogy row (P04 spring, overshoot check): "spring" appears only at P04 (Paper-1 mechanism),
   P07 ("replacing a spring with a new engine" — retiring Paper 1, not describing Paper 2), and
   P16 ("The spring paper" = Paper 1 recap). Paper-2's cusp stays "written in by hand". No
   overshoot. Binds.
3. Felt-comparison row (P14 ocean molecule, arithmetic): Earth's oceans ≈ 1.4×10²¹ kg H₂O ≈
   4.7×10⁴⁶ molecules → one molecule vs all oceans ≈ 1 : 10⁴⁶·⁷; narration states the floor-safe
   digit "about 45 orders" first, simile second; within ~1 order of the ledger's 45.2–46.0 gated
   margin. Ledger N3 stands. Binds.
4. Art-brief chip row ("COSMIC SPEED LIMIT" red-barrier, DS Panel 09 brief): in-image text is a
   metaphor label only — no numbers, no data; overshooting-arrow direction matches the gated
   6.6×10²⁶ finding; illustration chip mandatory per DS. Binds.
5. F1 row (P05): placement after both labeled edges verified in narration and stage order. Binds.
6. F2/B-17 row (P11): quote byte-verbatim against pinned TeX line 304; "NO ROTATING MODEL" /
   "NO AXIS CALCULATION" chips present. Binds.

## 7. Fallback honesty — PASS

Only nbp_p01_cold_open.png exists on disk; GENERATION_LOG.md honestly records the 02:06 K
throttle ruling (two failed attempts, back-off, Images 2–6 → programmatic fallbacks). Mechanical
sweep: zero nbp_* filename references anywhere in STORYBOARD.json / DESIGN_SYSTEM.md / SCRIPT.md
beyond the one real asset — panels 02–16 route concept art through named DESIGN_SYSTEM briefs,
each of which carries an explicit programmatic Fallback spec (verified: every Part-2 brief has a
Fallback line). Every asset path referenced by the storyboard resolves to a real, hash-verified
file. No phantom images.

## Observations (non-blocking; handed to Tori/gpt3, no packet change required)

- O1. Storyboard assets.hash_manifest.sha256 (e234a5c8…) records the PRE-REPAIR pin file; the
  repaired PINS.sha256 on disk hashes to 09505ab963b6faea7fc2f24aa570c4fc7fdc25b1e06e7c3c33664d965f59130a.
  Content custody is independently verified in §1 (all five pins match disk), so this is a stale
  bookkeeping record, not a provenance gap — the direct consequence of the ordered FLAG-2 repair.
  The render gate should verify the pin file itself, not this recorded hash.
- O2. Ledger watch-item W3 is inaccurate as stated: the "w = +1 vs w = −1" fork card IS present
  in panel 08's viewer_text. Compliant either way (permitted equations are a ceiling, not a
  quota; all three permitted equations appear, no others). No action.
- O3. DESIGN_SYSTEM Part 2 briefs cite two plots under the v2-style "assets/" path; the
  storyboard's visual_notes name the exact assets_v3/ filenames, which is the controlling layer
  per visual_notes_policy. Builder must resolve briefs by NAME (ledger W2) and files by the
  storyboard's paths.
- O4. W1 confirmed acceptable: caveat at P15-of-16, non-terminal, audit pre-approved; P16
  caveat-free and ends on the verdict.

## Verdict

All seven kickoff checks PASS; both FLAGs verifiably closed; packet is internally consistent and
build-ready. PASS_P2V3_PACKET. Next: gpt3 build (chain step F) under the storyboard's
authorization block (all false here, correctly).

— kimi, packet gate, 2026-08-20.

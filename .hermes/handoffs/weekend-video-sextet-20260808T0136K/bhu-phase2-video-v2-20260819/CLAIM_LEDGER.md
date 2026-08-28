# Claim ledger — "Born inside a black hole? The four papers explained" (P2 video v2)

**claude-seat (claim-binding seat), 2026-08-19 20:26 KST.** One row per narration claim and
on-screen assertion/number of `SCRIPT.md` + `STORYBOARD.json`, bound to gated Phase 2
artifacts; template `../bhu-phase2-video-20260819/CLAIM_LEDGER.md`. **Zero fetches;
portal.nersc.gov untouched.**

**Custody verified mechanically this session:** all 11 storyboard authority SHA-256s MATCH;
all four gate first lines equal their PASS tokens; `SCRIPT.md` sha matches the contract; all
12 storyboard narrations byte-identical to script panels with correct per-panel hashes; 1,098
narration words ≤ 1,150; panel 01 = 69 ≤ 80. Source keys as in the v1 ledger (S/A1/A2/B1/B2/C
+ gates), all hashes as pinned in the storyboard (verified). **Asset custody:** all four
`assets/` files exist, `PINS.sha256` verifies (`shasum -c`: 4× OK), and the two PRD figures
are **byte-identical to the figures inside the pinned arXiv source tarball**
(`sources/1111.4595/scale.jpg`, `temp.jpg` — same SHA-256s). All four images were **visually
inspected this session** against their narration walkthroughs.

Verdicts: **MAPPED** / **FLAG** (for the packet gate — zero silent rewrites) / **framing**.

**Result up front: 73 narration rows: 60 MAPPED, 7 framing, 6 FLAG (4 distinct defects,
F-A…F-D below). 13 headings: 13 MAPPED. On-screen items: 92 MAPPED, 3 FLAG (all F-C).**
The v2-specific checks: disclaimer ABSENT everywhere (✓, mechanically swept); plot-honesty
ground truth verified from the pinned sources themselves; every asset reference exists with
its attribution chip; the ceiling's Reading-1 sentence, frozen-ratio-as-condition,
erratum-unread, and theoretical-best floor all present (§4).

## 1. FLAG rows (the packet gate's queue — exact repairs proposed, script untouched)

**F-A — P03 sentence 5: "The printed value sits near that edge, so we carry both."**
Ambiguous antecedent: the immediately preceding sentence describes the *independent* (6×
smaller) edge, so the natural reading binds "that edge" to it — but the gated fact is the
opposite: the published −8.6×10⁻⁷⁰ sits at the **coherent** ("lined-up") edge, 2.6% inside
(B1 §2.2; bounce-gate rerun). The panel's own viewer text has distinct "LINED-UP EDGE" /
"INDEPENDENT EDGE" cards, making the narration's ambiguity resolvable the wrong way on
screen. **Repair (one word class): "The printed value sits near the lined-up edge, so we
carry both."**

**F-B — P08 sentence 3: "Across all 4 papers, parent spin appears in exactly 1 sentence."**
Overshoot, contradicted by the pinned source: PLB main.tex 333–339 discusses the rotating
parent across **multiple sentences**, including a formula (the Kerr radius a = M/(mc)) and
the GRS 1915+105 value — audited as A1 row P20. The gated one-sentence finding is **scoped to
the two interior/collapse papers**: A2 focus 2.3, verbatim, "The word 'rotating' occurs once
in the two papers combined, in B-17" (the B-17 sentence itself is quoted verbatim in the
script and verified at Collapse.tex line 304 this session ✓). The heading ("Paper 4 mentions
a spinning parent only once") and the viewer-text card are correctly scoped — only this
narration sentence overshoots; note the same overshoot appears in VIDEO_BRIEF_P2V2.md, but
the ledger binds to the gated audits. **Repair options: "In the 2 collapse papers, parent
spin appears in exactly 1 sentence: '…'" (scoped), or "Across all 4 papers, no equation
carries the parent's spin through the bounce; the collapse papers mention it in exactly 1
sentence: '…'" (both true per A1 P19–P20 + A2 focus 2.3).**

**F-C — the "100,000 times below" single-edge margin (3 narration rows + 3 on-screen items):**
P01 s4 ("Even the most generous signal is about 100,000 times below…"), P11 s2 ("only about
1 part in 100,000 of the counting floor"), P12 s6 ("missed the absolute counting floor by
100,000 times"), and viewer-text items P01 "ABOUT 100,000 × BELOW THE ALL-GALAXY FLOOR",
P11 "ABOUT 1 PART IN 100,000 OF FLOOR · ~10⁻⁵", P12 "MOST GENEROUS STACK · 100,000 × BELOW".
Gated values (C §4, Stack A): Treatment I = 8.5×10⁻⁶ of the floor (≈ 1/118,000) but
**Treatment II — the actual most generous branch — = 7.6×10⁻⁵ (≈ 1/13,000)**, and 1/7,400 at
the C-bracket top. "About 100,000× below" overstates the true most-generous margin by ~9×.
The v1 video's gated phrasing was the correct envelope. **Repair: "about 10,000 to 100,000
times below" (narration) and "10,000–100,000 × BELOW" (the three viewer-text items); P11's
"~10⁻⁵" chip becomes "~10⁻⁵–10⁻⁴".**

**F-D (minor) — P09 sentence 4: "…caps inherited spin near 1 part in 10 to the power 27."**
States the Treatment-I edge only (1.5×10⁻²⁷); Treatment II's ceiling is 1.4×10⁻²⁶ = 14 parts
in 10²⁷ (B2 §2.2). The v1 ledger accepted the order-form ("ε ≤ 10⁻²⁷" is the brief-authorized
equation) **because** v1's narration carried the branch clause — which v2 dropped. **Repair:
restore the clause: "…near 1 part in 10 to the power 27, with the treatment branches spanning
roughly 1 order of magnitude." (or a viewer-text chip "TREATMENT BRANCHES · WITHIN ×9").**

## 2. Narration rows (compact; FLAG rows above; framing = asserts nothing)

| Panel | Rows | Verdicts | Bindings (all grep/receipt-verified) |
|---|---|---|---|
| 01 | 5 | 1 framing (question), 3 MAPPED, 1 FLAG (F-C) | audited 4 papers ← S 56–66; missing limit derived ← S 33–42; "no observable signature survives" ← S 6–8/C §0; ceiling/closed ← C §0, §7 |
| 02 | 7 | 1 framing, 6 MAPPED | spin/torsion plain glosses ← PLB main.tex 47–53, 88–98 (pinned); spring-pushback + bounce ← PLB 100, 219–232 / A1 P7 (ä>0 receipted); **no plots ← source ground truth: 0 \includegraphics in main.tex (verified)**; "negative 1 shifted 70 places" ← note N1 |
| 03 | 8 | 1 framing, 6 MAPPED, 1 FLAG (F-A) | averaging cited-not-derived ← A1 H2 (P5); squares total of 6 types ← B1 §2.2/R2; ×6 exactly ← B1 (gate-rerun 6.00); erratum exists/content unread ← G1 Check 2 (metadata RESOLVED, content UNVERIFIED); quarantined+recomputed ← A1 P13/D15/D16 + B1 §2.4/3.3; "proposal…strength not unique" ← B1 §2.2 |
| 04 | 6 | 6 MAPPED | fermion-field gloss ← PRD tex 54–115 (Dirac form); Fig 1 walkthrough ← **image inspected: blue curve, dip to sharp bottom at a/acr = 1, regrowth — cusp not U-turn ✓** (A1 D13; B1 §3.2); "only chain paper with plots" ← source ground truth (2 \includegraphics in 1111.4595; 0 in the other three — all verified) |
| 05 | 6 | 6 MAPPED | Fig 2 walkthrough ← **image inspected: narrow spike to T/Tcr = 1 ✓**; near-Planck ← B1 §3.3 (0.785 m_P) + V1; the two quotes ← **grep-verified verbatim, PRD tex 113–114**, CP gloss noted N2; ×730 ← B2 §1 (gate ×727); prescribed jump / never slows to stop ← B1 §3.2 (ε_eff(T_cr)>0 receipted) |
| 06 | 5 | 1 framing (seed-pod analogy of the paper's own claim, A2 A-17 class), 4 MAPPED | fixed-compactness M→(size, T) map ← B2 §1 (a₀T₀ ∝ χ^¾M^½, receipted); "the 1 calculated inheritance channel" ← A2 focus 2.1/S 33–38; no plots ← ground truth verified; carries size+heat not rotation ← A2 focus 2.3/B2 §2.1 |
| 07 | 6 | 1 framing, 5 MAPPED | insensitive-to-a_i, follows β ← A2 A-18 (gate-confirmed); conjecture join ← A2 A-17; no horizon matching ← A2 focus 1; **1-meter assumption ← A2 A-9 (gate-rerun: block reproduces only at a_i = 1 m)** |
| 08 | 4 | 3 MAPPED, 1 FLAG (F-B) | star-like collapse ← A2 Paper B rows; no plots ← ground truth verified; the B-17 sentence ← **grep-verified verbatim, Collapse.tex 304**; "no equation, no rotating model, no axis calculation" ← A2 focus 2.3 (scoped correctly in this sentence) |
| 09 | 6 | 1 framing, 4 MAPPED, 1 FLAG (F-D) | 6.6×10²⁶ ← B2 §2.2 (gate: = 1/ε_max, consistent); Reading-1/2 plain sentence ← the brief's exact sentence + S 13–17 (direction correct: less, not more); frozen ratio as condition ← B2 §3 (sympy-receipted; "neither smooths nor creates") |
| 10 | 7 | 1 framing, 6 MAPPED | BBN gloss ← pinned DS text; **Fig 1 = He/D/Li comparison ← caption grep-verified ("Changes in primordial element abundances…") + image inspected (Y_p, D/H, Li⁷/H sub-panels ✓)**; **Fig 2 = ΔY_p bound ← caption verified + image inspected (ΔY_p vs ρ_S10/ρ_R10, linear, extends past 30 ✓)**; "up to 30× radiation at 10 MeV" ← the pinned bound verbatim (C §2); 45 orders ← C §1 row 1 (45.2–46.0, floor-safe); sign caveat ← C §2 (carried on-screen verbatim class) |
| 11 | 6 | 1 framing, 4 MAPPED, 1 FLAG (F-C) | floor = all 2×10¹² galaxies, theoretical best not instrument ← C §4/S 10–12 (kickoff watch-item, verbatim honored); finite-sample wobble gloss ← σ_A = 1/√N (Phase 0/1 pins); caveat sentence ← V1 + S 98–99 (mid-video ✓ not terminal ✓) |
| 12 | 7 | 1 framing, 5 MAPPED, 1 FLAG (F-C) | per-paper recap ← S §"What Phase 2 derived" + A1 H1 + A2 A-18 + B-17 (Paper-4 line **correctly scoped here**: "only 1 unsupported sentence about rotation" refers to Paper 4 ✓); ceiling/closed ← C §0 |

## 3. Headings and on-screen items

**All 13 headings MAPPED** (title; P01 ← C §0; P02 ← PLB bounce rows; P03 ← A1 H2 ("unproved
average" = underived, our audited finding); P04–05 ← PRD rows/figures; P06–07 ← B2 §1/A2
A-9/A-17/A-18; P08 ← A2 B-17 **correctly scoped to Paper 4**; P09 ← B2 §2.2; P10 ← C §§1–2;
P11 ← C §4 (heading carries "100,000" — include in F-C's repair sweep); P12 ← S verdict).
Note: P11's heading "Even the most generous signal is 100,000 times below the floor" is
F-C-affected; P01's heading is not (no number).

**On-screen items: 92 MAPPED, 3 FLAG (F-C, listed there).** Highlights, all verified: the
four paper-identifier cards match the Crossref-verified citations; the three authorized
equations (w = +1 vs −1; a⁻⁶ = a⁻⁶; ε ≤ 10⁻²⁷) appear exactly once each, deterministic viewer
text only, narration equation-free (grep: no equation glyphs); the three "THIS PAPER CONTAINS
NO PLOTS" cards appear on exactly the three figure-less papers (source ground truth: only
1111.4595 has figures — verified from the pinned TeX of all four papers, not from the brief);
all four asset references name existing, hash-pinned files, each panel carrying the correct
attribution chip ("Figure N, arXiv:… (author version)") and every our-graphic panel carrying
"NebulaMind rendering" (mechanically enumerated); P10's sign-caveat chip ("POSITIVE BOUND ·
NEGATIVE TORSION · MAGNITUDE INVISIBLE EITHER WAY") is the C §2 caveat, honestly on screen;
P09 carries "SPIN 0.7" and "CEILING · NOT A MEASURED TRANSFER" ✓.

## 4. The kickoff's five v2 checks

1. **Disclaimer absent everywhere: PASS** — mechanical sweep of SCRIPT.md + STORYBOARD.json
   for "side-interest / side interest / not a NebulaMind research / personal interest /
   scope_label": zero hits; the storyboard's scope_label field itself is gone. (Per Duho's
   verbatim direction in the brief; its *presence* would have been the FLAG.)
2. **Fair-rendering of paper claims: 2 FLAGs (F-A, F-B), rest pass** — every plain-words
   chapter claim binds to pinned source lines or audited rows (§2); the high-school glosses
   (spin/torsion/scale factor/BBN/stiff component/compactness/conjecture/angular momentum/
   shear) each define the term in-sentence and none overshoots its source; notes N1–N2 cover
   the two accepted compressions.
3. **Plot honesty: PASS** — verified from the pinned sources themselves: 1111.4595 has
   exactly 2 figures (and the assets are byte-identical to the tarball's own files);
   1007.0587, 1410.3881, 2509.11468 have zero; the DS paper's two figures match their pinned
   captions and inspected content; `assets/PINS.sha256` verifies.
4. **Asset references + attribution chips: PASS** — 4/4 files exist, 4/4 hash-verified, every
   reference carries its chip (panels 04, 05, 10), every our-graphic panel carries
   "NebulaMind rendering" (02, 03, 06, 07, 08, 09, 11).
5. **The four content guards: PASS** — Reading-1 plain sentence present (P09 s5, the brief's
   exact wording; direction correct); frozen ratio stays a condition (P09 s6 — no amplitude
   anywhere); erratum unread-not-resolved (P03 s6; P03 viewer text "CONTENT · UNREAD BEHIND
   PAYWALL"); floor theoretical-best-not-instrument (P11 s3 verbatim + viewer text).
   Must-not-say sweep clean (only "unproved average" trips the grep — our audited finding,
   in-bounds; no false/impossible/refuted/proved-wrong; clinical author treatment: "Dutta &
   Scherrer" appears as the bound's standard citation, the chain's author only via
   paper identifiers).

## 5. Fidelity notes

- **N1 — "a negative 1 shifted 70 places past the decimal point" (P02 s7 + viewer text):**
  the gated bracket is [−8.8, −1.5]×10⁻⁷⁰ — both edges have their leading digit in the 70th
  decimal place, and the incoherent edge literally reads "1.5" there; the paper's own abstract
  gloss is −10⁻⁶⁹. Accepted as an order rendering of the bracket ("roughly"); the exact
  bracket is P03's content.
- **N2 — cosmological-principle gloss (P05 s4):** "looks the same in every direction"
  compresses homogeneity+isotropy to isotropy; the violated aspect in the quoted context (a
  spin fluid picking a direction) is isotropy. Accepted at high-school register.
- **N3 — "about 730" ← ×727 (gate rerun) / ×730 (B2 rounding).** ✔
- **N4 — "45 orders" ← 45.2–46.0 (floor-safe).** ✔
- **N5 — "30 times radiation at 10 MeV" ← the pinned DS bound verbatim (ρ_S10/ρ_R10 < 30).** ✔
- **N6 — "6.6 times 10 to the power 26 beyond light's speed limit" ← the rotation velocity
  would exceed c by that factor (B2 §2.2; v_rot/c = 6.6×10²⁶).** ✔

## 6. Boundary

This ledger maps and flags; **nothing was rewritten** — the 4 defects (6 narration rows,
3 on-screen items, 1 affected heading) go to the packet gate with exact repairs proposed;
everything else binds clean. `SCRIPT.md`, `STORYBOARD.json`, `assets/` untouched. Zero
fetches; portal.nersc.gov untouched. Next per the platoon chain: repairs (gpt1) or gate
adjudication (kimi), then agy's VISUALS.md — whose claim-bearing additions return to this
seat; the F-C repair must also propagate to any ladder labels agy builds from those panels.

— claude-seat, 2026-08-19 20:26 KST.

## 7. REVERIFY RECORD (appended after the repair pass — see `GPT3_REPAIR_DONE.md`, `AGY_DONE.md` = AGY_P2V2_COMPLETE_FCFIXED)

**claude-seat, 2026-08-19 (bounded re-verify pass). Zero silent rewrites; no fetches;
portal.nersc.gov untouched.**

**Mirror and contract integrity re-verified mechanically:** repaired `SCRIPT.md`
(`cfd9d1e1…`) and `STORYBOARD.json` (`8b17bfc5…`) match GPT3_REPAIR_DONE's stated hashes; all
12 storyboard narrations byte-identical to script panels with correct per-panel hashes; the
storyboard's script-contract sha matches the repaired file; word counts inside contract
(1,127 ≤ 1,150; panel 01 = 71 ≤ 80).

**(1) The four FLAG repairs:**

- **F-A → MAPPED-AFTER-REPAIR.** P03 s5 now reads "The printed value sits near the lined-up
  edge, so we carry both" — the ledger-specified wording exactly; binds to B1 §2.2 (published
  −8.6×10⁻⁷⁰ at the coherent edge, 2.6% inside).
- **F-B → MAPPED-AFTER-REPAIR.** P08 s3 now reads "Across all 4 papers, no equation carries
  the parent's spin through the bounce; the collapse papers mention it in exactly 1 sentence:
  '…'" — the ledger's scoped repair option verbatim; first clause binds to A1 P19–P20 + A2
  focus 2.3 (no dynamical spin equation anywhere), second clause to A2 focus 2.3 ("once in
  the two papers combined") with the B-17 quote still verbatim (Collapse.tex 304).
- **F-C → MAPPED-AFTER-REPAIR in narration and chips; ONE RESIDUAL ITEM (below).** P01 s4,
  P11 s2, P12 s6 all now carry "about 10,000 to 100,000 times"; viewer-text items P01/P11/P12
  updated including the ~10⁻⁵–10⁻⁴ chip; **VISUALS.md propagation confirmed as labeled
  bands**: panel 11's ladder marks the range "as a labeled band with both treatment edges
  marked, not a single rung", panel 09's ceiling dial marks both edges as a range, panel 12's
  chip updated. All bind to C §4 Stack A (8.5×10⁻⁶ / 7.6×10⁻⁵ of floor).
- **F-D → MAPPED-AFTER-REPAIR.** P09 s4 now carries "…with the treatment branches spanning
  roughly 1 order of magnitude" (v1's clause restored); binds to B2 §2.2 (1.5×10⁻²⁷ →
  1.4×10⁻²⁶, ×9).

**RESIDUAL FLAG (1) — R-1, the Panel 11 heading:** "Even the most generous signal is 100,000
times below the floor" was NOT swept — it persists in `SCRIPT.md` line 47, the storyboard's
panel-11 `assertion_heading` + viewer-text item 1, and `VISUALS.md` line 157. A heading is a
claim (ledger §3 flagged it explicitly), and the gated most-generous margin is ~13,000×, so
the heading still overstates by ~8×. **Repairs (either): "Even the most generous signal is
10,000 times below the floor" (single figure, floor-true for every gated branch — safest), or
the range form "…is 10,000 to 100,000 times below the floor."** Goes to the packet gate or
one more gpt3 micro-pass; all three files must be swept together to preserve mirror identity.

**(2) agy's claim-bearing additions:** the VISUALS.md "CLAIM-BEARING ADDITIONS" section
declares "None.", but the FIX RECORD contains **one claim-bearing addition**: the panel-09
viewer-text chip **"TREATMENT BRANCHES · WITHIN ×9"**. New row: **MAPPED** — binds to B2 §2.2
(ε_max 1.5×10⁻²⁷ (I) → 1.4×10⁻²⁶ (II); ratio 9.0, inherit-gate re-confirmed values); it is
the ledger's own proposed F-D on-screen complement. Bookkeeping note for the packet gate, not
a FLAG: the addition is mislabeled (lives in FIX RECORD under a "None" declaration) — the
declaration should read "one, reviewed below". The remaining fix-record entries are
replacements matching the ledger-specified repairs, not additions; no other claim-bearing
text or geometry was introduced (checked against the pre-fix VISUALS content recorded in the
FIX RECORD's own before/after pairs).

**Final tally after re-verify: narration 66 MAPPED (60 + 4 repaired + F-C's two co-repaired
rows counted within), 7 framing, 0 narration FLAGs; on-screen items all MAPPED including the
new ×9 chip; headings 12 MAPPED + 1 RESIDUAL FLAG (R-1). FLAG count: 1.**

— claude-seat, re-verify pass, 2026-08-19.

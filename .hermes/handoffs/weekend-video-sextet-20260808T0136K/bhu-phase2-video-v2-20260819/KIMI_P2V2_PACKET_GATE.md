PASS_P2V2_PACKET

# kimi — Phase 2 explainer v2 packet gate (second reviewer, fresh one-shot)

2026-08-19. Lane dir only. Findings-only; nothing edited; this is the only file written.
Zero fetches; portal.nersc.gov untouched. All checks grep/python3-extraction, this session.

## (1) Repair closure — F-A, F-B, F-C, F-D, R-1 all applied as the ledger specified

Current sentences (quoted from the live files):

- F-A (P03 s5, SCRIPT.md L17 / storyboard panel 03 narration): "The printed value sits near
  the lined-up edge, so we carry both." — the ledger-specified one-word-class repair exactly.
- F-B (P08 s3, SCRIPT.md L37 / storyboard panel 08 narration): "Across all 4 papers, no
  equation carries the parent's spin through the bounce; the collapse papers mention it in
  exactly 1 sentence: 'It would still be valid for a more realistic gravitational collapse
  of an inhomogeneous and rotating fluid.'" — the ledger's scoped repair option verbatim.
- F-C narration: P01 s4 "about 10,000 to 100,000 times below the best possible
  galaxy-counting test"; P11 s2 "only about 1 part in 10,000 to 100,000 of the counting
  floor"; P12 s6 "missed the absolute counting floor by about 10,000 to 100,000 times".
  F-C viewer chips: P01 "10,000-100,000 x BELOW THE ALL-GALAXY FLOOR"; P11 "ABOUT 1 PART
  IN 10,000-100,000 OF FLOOR - ~10^-5-10^-4"; P12 "MOST GENEROUS STACK - 10,000-100,000 x
  BELOW" — all present in STORYBOARD.json and mirrored in VISUALS.md.
- F-D (P09 s4, SCRIPT.md L41): "…caps inherited spin near 1 part in 10 to the power 27,
  with the treatment branches spanning roughly 1 order of magnitude." — v1 clause restored.
- R-1 (residual): heading now "Even the most generous signal is 10,000 times below the
  floor" in all four mirrored locations: SCRIPT.md L47, storyboard panel 11
  assertion_heading, storyboard panel 11 viewer-text item 1, VISUALS.md L157.

Old wordings absent — greps over SCRIPT.md + STORYBOARD.json + VISUALS.md, zero hits each:
"sits near that edge"; "Across all 4 papers, parent spin appears"; "100,000 times below
the floor" (heading or anywhere); bare "about 100,000 times". (Remaining "100,000"
occurrences are all inside the repaired "10,000[-/ to ]100,000" ranges or inside
VISUALS.md FIX RECORD's historical before-quotes.)

File SHAs match GPT3_REPAIR_DONE.md's latest (post-R-1-micro-pass) values exactly:
- SCRIPT.md     684b6e038d467e6cc575fef3f54a6e0ca9fc7f250c2bf96f8cd4b380925dae3d  MATCH
- STORYBOARD.json 2d9469cbc496447e1dfe66b532f9cb0a9046e991903a60911b31e207fa15f385  MATCH
- VISUALS.md    c73a547298c75b1024dc88cae5ddf0b4bc17b7b432ffd9c3fc609813b5fe2815  MATCH

## (2) Structure contract

- 12 panels (01–12), chapters: verdict intro / 4×2 paper chapters / reality check / stack /
  verdict ending.
- Narration, headings excluded, recounted this session: 1127 words ≤ 1150 (matches
  GPT3_REPAIR_DONE and CSEAT re-verify; per-panel 71/90/93/87/100/84/95/99/112/101/95/100).
- Panel 01 = 71 ≤ 80 and verdict-complete: question ("Could our universe have been born
  inside a black hole, and could it remember which way its parent spun?"), work ("We
  audited the 4 published papers in that chain, then derived the missing limit"), verdict
  ("no observable signature survives … the route stays closed").
- Assertion heading on every panel; all 12 storyboard assertion_headings byte-match the
  SCRIPT.md headings (python3 comparison).
- No divider cards: none present; storyboard production_constraints
  "divider_cards_allowed": false (the only "divider" hit in the packet is that prohibition).
- Ends on the verdict: ends_on_verdict true only for panel 12; final narration sentence
  "…the ceiling says the route stays closed."
- Caveat sentence in panel 11, verbatim per contract: "One honest caveat: both bounces sit
  in the Planck regime treated classically, and the strict chain awaits external theorist
  review." — mid-video, not terminal.
- Scope disclaimer: ABSENT. Sweep of SCRIPT.md, all STORYBOARD.json fields, and VISUALS.md
  for side-interest / side interest / programme / personal interest / scope_label /
  my-interests phrasings (incl. the brief's verbatim typo variant): zero hits. Presence
  would have been a HOLD; it is not present. (The gated theory-lane documents carry their
  own scope label, outside this packet's viewer-facing surface — expected, untouched.)

## (3) Mirror

One python3 comparison: all 12 SCRIPT.md panel bodies byte-identical to the corresponding
STORYBOARD.json narration fields; all 12 per-panel narration_sha256 fields recompute
correctly. Mirror PASS.

## (4) Ledger sampling — 6 rows spot-verified against gated authorities

1. F-B two-clause sentence (P08 s3), both clauses bound:
   - Clause 1 ("no equation carries the parent's spin through the bounce", all 4 papers) ←
     TRACK_A1_AUDIT.md P19 (black-hole-parent narrative 310–331: UNSUPPORTED, "no matching
     calculation") and P20 (axis/Kerr-radius prospect 333–339: PROSPECT / no amplitude;
     the PLB rotating-parent passage verified to exist at sources/1007.0587/main.tex
     333–339 — multiple sentences incl. a = M/(mc) and GRS 1915+105 — confirming the
     original script sentence was an overshoot and the repair is the correct scoping) +
     TRACK_A2_AUDIT.md §4 focus 2 item 3: "Spin a★ — absent. Both papers treat
     non-rotating collapse."
   - Clause 2 ("the collapse papers mention it in exactly 1 sentence") ← A2 focus 2.3
     verbatim: "The word 'rotating' occurs once in the two papers combined, in B-17";
     B-17 quote grep-verified verbatim at sources/2509.11468/Collapse.tex line 304.
2. Plot-honesty row (P02/P04 on-screen ground truth): includegraphics counts in the pinned
   TeX — 1111.4595: 2; 1007.0587: 0; 1410.3881: 0; 2509.11468: 0. Only the PRD paper has
   figures, as narrated.
3. Panel-9 branch chip "TREATMENT BRANCHES · WITHIN ×9" ← B2 (P2_DERIVATION_INHERITANCE.md
   §2.2 table: 1.5×10⁻²⁷ (I) / 1.4×10⁻²⁶ (II)); receipts/p2b2_spin_out.txt exact values
   1.51e-27 / 1.36e-26 → ratio 9.007 ≈ 9.0; MIRU_P2_INHERIT_GATE row "spin ceiling …
   CONFIRMED". Chip binds.
4. ×730 row (P05 s5) ← receipts: eps_b(I) 7.112e114 / eps_b(II) 9.781e111 = ×727.2 →
   "about 730" (ledger N3; inherit-gate CONFIRMED).
5. F-C range row (P01/P11/P12) ← P2_CONFRONTATION.md §4 Stack A: "8.5×10⁻⁶ / 7.6×10⁻⁵ of
   the all-sky 1σ floor" — i.e. ~118,000× / ~13,000× below, order envelope 10⁻⁵–10⁻⁴; the
   repaired "about 10,000 to 100,000 times below" is the ledger-prescribed v1 envelope and
   covers both gated branches.
6. Causality row (P09 s3) ← receipts: Omega_cons 5.06e57 vs c/R_b 7.66e30 → 6.6e26
   = 1/ε_max, internally consistent (inherit-gate CONFIRMED); narration "6.6 times 10 to
   the power 26 beyond light's speed limit" binds.

Final FLAG count: ledger §7 tally = 1, explicitly the R-1 heading residual; R-1 is now
swept in all three files (check 1) — the count closes to 0 open FLAGs. agy's late-declared
addition (the panel-09 "TREATMENT BRANCHES · WITHIN ×9" chip living in the FIX RECORD
under a "None." declaration) has its MAPPED row in ledger §7(2) — present, bound to
B2 §2.2, ratio confirmed as in row 3 above.

## (5) Visuals honesty (VISUALS.md + storyboard closed worlds)

- Paper figures: P04 assets/prd_1111.4595_fig1_scale.jpg and P05
  assets/prd_1111.4595_fig2_temp.jpg, P10 assets/ds_1006.4166_comparison.png +
  ds_1006.4166_prefac_Yp.png — each specced full-legible with its attribution chip
  ("Figure N, arXiv:… (author version)") and a walkthrough annotation (cursor trace of the
  dip-and-bounce; spike trace with Planck marker beside the peak "without covering paper
  pixels"; He/D/Li panel walk; helium-change curve trace).
- F-C ladders as labeled BANDS with both treatment edges: P09 visual "stop at the ceiling
  (ensure both treatment edges are marked as a range)"; P11 visual "Mark the signal at
  ~10⁻⁵-10⁻⁴ of the floor (geometry must show the RANGE as a labeled band with both
  treatment edges marked, not a single rung)". MATCH the FIX RECORD after-states.
- Equations: exactly the three authorized — "w = +1 vs w = −1" (P05), "ε ≤ 10⁻²⁷" (P09),
  "a⁻⁶ = a⁻⁶" (P09) — one occurrence each, visuals-owned; all other ×-items are labeled
  magnitude text (×6, ×730, 6.6×10²⁶, 30×, range chips) per the magnitude policy;
  narration equation-free (glyph sweep clean);
  "other_equations_on_screen_allowed": false honored.
- Planck markers: P05 (deterministic marker beside the spike peak) and P11
  ("PLANCK REGIME · TREATED CLASSICALLY" chip + caveat placed before the final ceiling
  comparison); planck_marker_required_where_bounce_state_drawn honored on the
  bounce-state panels per the visual plan.
- No-plots honesty: "THIS PAPER CONTAINS NO PLOTS — THE ENTIRE ARGUMENT IS EQUATIONS" on
  exactly panels 02, 06, 08 (the three figure-less papers, confirmed against TeX in row 2
  above); "NebulaMind rendering" on every original-graphic panel (02, 03, 06, 07, 08, 09,
  11).
- Must-not-say sweep (false / impossible / proved wrong / refuted): clean — only
  authorization-boolean "false" hits; clinical author treatment intact.

## (6) Assets

All four assets/ files exist; shasum -c assets/PINS.sha256 → 4× OK:
prd_1111.4595_fig1_scale.jpg, prd_1111.4595_fig2_temp.jpg, ds_1006.4166_comparison.png,
ds_1006.4166_prefac_Yp.png. Storyboard assets block carries the same hashes.

## Bookkeeping notes (carry-forward to the render gate; not FLAGs)

- N1 — storyboard script_contract.sha256 reads cfd9d1e1… (the pre-R-1 script hash), one
  micro-pass behind the current SCRIPT.md (684b6e03…). R-1 touched headings only; all 12
  narration bodies remain byte-identical, so mirror integrity stands. Render gate should
  key custody on the narration bodies and current file SHAs.
- N2 — storyboard panel-11 visual_notes item 2 / semantic beat still phrase the signal as
  "~10⁻⁵ of the floor" (single-edge), and panel-09's note lacks the range clause; both are
  superseded by VISUALS.md's F-C band specs ("not a single rung"). The build must follow
  VISUALS.md for panel 09/11 geometry. Same class as agy's mislabel, which the claim seat
  recorded as bookkeeping, not a FLAG.
- N3 — the repaired P11 heading figure (10,000×) is floor-true for both gated treatment
  branches (~13,000× / ~118,000×); the C-bracket top (~7,400×) sits ~1.35× inside it. The
  claim seat weighed this and prescribed the single-figure form as the safest wording
  (ledger §7, R-1); binding recorded here for the render gate's awareness.

## Verdict

All six gate checks pass; the four repairs plus residual R-1 are closed exactly as the
ledger specified; mirror, structure, visuals-honesty, and asset custody all verify
mechanically. The packet is cleared for gpt3 build (BHU_PHASE2_EXPLAINER_V2_LOCAL_REVIEW.mp4
under the v2 chain), with notes N1–N3 carried forward. This gate authorizes no rendering,
credit spend, upload, publication, or public status change by itself.

— kimi, 2026-08-19.

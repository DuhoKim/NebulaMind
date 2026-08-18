PASS_EXPLAINER_PACKET

# Kun — packet gate on the theory-closure video packet

**Kun (gate seat), 2026-08-18 KST.** Gated per `KICKOFF_KUN_TV_PACKET.txt`: read
`SEXTET_BRIEF_THEORY_VIDEO.md` (including the 22:55 equations amendment), then gated
`SCRIPT.md`, `STORYBOARD.json`, `CLAIM_LEDGER.md`, `DEFINITIONAL_SOURCES.md`,
`LANA_ANNOTATION_REVIEW.md`, `VISUALS.md` against the gated Phase 0 documents. Findings only;
nothing edited. `portal.nersc.gov` was not touched. Literature fetches: none needed — every
number the packet leans on is already certified inside the gated Phase 0 chain, which I
re-verified locally (hash pins + independent recompute below).

**Seat receipts present:** `YUI_DONE.md` = `YUI_TV_COMPLETE`; `YUI_CW_DONE.md` =
`YUI_CW_UPDATE_COMPLETE`; `LANA_DONE.md` = `LANA_TV_COMPLETE — FLAG count: 0`; `GORU_DONE.md` =
`GORU_TV_COMPLETE`. `LANA_ANNOTATION_REVIEW.md` first line = `LANA_ANNOTATIONS_APPROVED`.

---

## 1. Hash and byte-identity verification (mechanical)

Recomputed SHA-256 of every pinned authority in `STORYBOARD.json` — all 7 match: sextet brief,
LANA_PHASE0_SCOPING, GORU_PHASE0_PRIORART, KUN_PHASE0_GATE (first line re-verified
`PASS_PHASE0_SCOPING`), BHU_ROTATION_HANDEDNESS_CLOSURE, KUN_CLOSURE_GATE (first line
re-verified `PASS_CLOSURE_NOTE`), prediction packet `b244ea0a…`. `SCRIPT.md` matches its pinned
hash. Per panel: narration text in SCRIPT.md is **byte-identical** to the storyboard string, the
per-panel `narration_sha256` recomputes clean, and per-panel word counts match (70/68/70/68/70/
68/70/71/65/69 = **689** total, as pinned). Assertion headings match SCRIPT.md on all 10
panels. Planned seconds sum = **309**, as pinned. D1 local copy
(`definitional_sources/nasa_wmap_bb_tests_cmb.html`) recomputes to the pinned
`abcb9763…`.

## 2. Ledger completeness

53 script sentences (my independent split: 6/6/6/5/5/5/6/5/4/5 per panel) + the head scope line
= 54 rows, +3 approved annotation rows (§6) = **57 rows; 0 FLAG** — matches Lana's stated
totals. All 11 headings rowed. No factual sentence found outside a row.

## 3. Source-truth spot-checks at cited lines

- **5 in 10 million** — C 97–99 (A ≈ 5×10⁻⁷), K 70 recompute **5.24×10⁻⁷**. My independent
  recompute: ω_max(S2) = 7.6×10⁻¹⁰·H₀ = 1.66×10⁻²⁷ s⁻¹; ω_Li = 3.17×10⁻²¹ s⁻¹; A = **5.24×10⁻⁷**.
  "About 5 in 10 million" = 5×10⁻⁷ exactly, generous direction. ✔
- **18 universes** — C 115–117 (N = 9/A² ≈ 3.6×10¹³ vs S7's 2.0×10¹²), K 78 = **18.0**. My
  recompute at Lana's stated rounding reproduces 3.6×10¹³ and 18.0 (using unrounded A gives
  16.4, but the gated value is computed at A = 5×10⁻⁷ as stated in C 115 and certified at K 77–78
  — consistent with the packet's cited basis). ✔
- **Under 1 sigma** — the script never vaguens: it states the exact digit **0.74 standard
  deviations** (P07#5), C 117–119, K 79–80. My recompute: σ_A(all-sky) = 1/√(2×10¹²) = 7.07×10⁻⁷;
  S/N = 5.24×10⁻⁷ / 7.07×10⁻⁷ = **0.74**. ✔
- **Rotation-bound comparison** — "less than about 8 parts in 10 billion of the expansion rate"
  ← (ω/H)₀ < 7.6×10⁻¹⁰ (C 83, 87; S2 verbatim at S-file lines 23–27 area + closure note §3).
  8×10⁻¹⁰ rounds the bound **up**, keeping "less than" true (real cap stricter — safe, generous
  direction). "A tighter, more general check allows even less" ← S1's 4.7×10⁻¹¹ (C 77–79). ✔
- **Rotation-bound → amplitude chain** — S5's ω_Li ~ 10⁻¹³ rad/yr normalization and the linear,
  no-scrambling generosity verified at S 106–112 and C 97–101. ✔
- **100,000-galaxy yardstick / 1 in 100 / >10,000×** — C 109–115; my recompute 1×10⁻² /
  5.24×10⁻⁷ = 1.9×10⁴ = 4.28 orders; "more than 10,000" true and conservative. ✔
- **Amplifier escape** — "gain above 10,000 times" ← C 126 (~10⁴); "small"/"tend to align" ←
  P 226–228 verbatim; "new model-building" ← C 129–131. ✔
- **Source characterization** — direction-without-size verified at P 244–257 (the "should be
  different" quote present; the absence of amplitude/scale/redshift/acceptance-region stated
  verbatim). ✔
- **D1 (baby picture)** — NASA's own phrase verified in the pinned local copy; metonymy accepted
  per F8; "oldest light" / "375,000 years after inflation" / "tiny fluctuations" verbatim. ✔

## 4. The three approved closed-world additions

All present in `STORYBOARD.json` viewer-text and ledgered at §6: `Counting noise floor = 1/√N`
(Panel 03), `NEEDED (~1/100)` and `ALLOWED (~5/10M)` (Panel 06). Approved as proposed in
`LANA_ANNOTATION_REVIEW.md`; narration remains equation-free (mechanical sweep: no √, =, ×, σ in
any storyboard narration string). The annotation is viewer text only — 22:55 amendment honored.

## 5. Must-not-say sweep

Mechanical sweep of all 10 narration strings plus SCRIPT.md full text: no "false", "impossible",
"disproven/disprove", "falsif", "proved/proves", "dead" in any claim-bearing position. Verdicts
are route-scoped throughout ("closes this test", "the route is closed; the wider idea is not").
Explicit denials present at P01#5 and P10#5. ✔

## 6. Magnitude-visual honesty (VISUALS.md)

Panel 06 spec: explicitly labeled log ladder, ticks at 10⁻²…10⁻⁷, both markers labeled
(NEEDED/ALLOWED), 5×10⁻⁷ placed between the 10⁻⁶/10⁻⁷ ticks, 4 stacked ×10 blocks, and the
sentence "NO unlabeled logarithmic spacing tricks." Consistent with K 76's 4.26–4.30 orders; the
claim is carried by the ledgered "MORE THAN 10,000 TIMES TOO SMALL" string, not by unlabeled
geometry. Satisfies the brief's honesty-critical rule. ✔

## 7. Structure contract

Verdict complete in Panel 01 (70 words ≤ 72; 34 planned s ≲ 35 s); assertion heading on every
panel; `divider_cards_allowed: false`; Panel 10 `ends_on_verdict: true` with the final frame
holding only the bounded verdict; 689 narration words ≤ 730; 309 s inside the 240–360 s target.
Scope label from frame zero (head line + P01#2 + P01 plates). ✔

## 8. Comprehension check (no-physics viewer)

Read as a naive viewer: the 2-jar image defines the measurement with no vocabulary; "baby
picture" is sourced plain language; every quantity is a plain-words comparison ("5 in 10
million", "18 observable universes of galaxies", "0.74 standard deviations" with the standard
named on screen before the kill); the single optional equation (1/√N) is an on-screen footnote,
never the carrier of a claim; the closing panel recaps the generosity chain before the verdict.
A viewer with no physics background can follow stakes → test → ceiling → gap → kill → escape →
verdict without a single prerequisite. ✔

## Gate verdict

All kickoff conditions met: ledger complete with 0 FLAGs; plain-words renderings faithful to the
certified numbers at the cited lines; script/storyboard byte-identical with verified hashes; all
three approved closed-world additions present and ledgered; must-not-say sweep clean; the
magnitude visual honest and labeled; structure contract honored; comprehensible to a no-physics
viewer. The packet passes to Tori for build.

— Kun, gate seat, 2026-08-18. Findings only; nothing edited; no rendering, upload, or
publication authorized by this gate.

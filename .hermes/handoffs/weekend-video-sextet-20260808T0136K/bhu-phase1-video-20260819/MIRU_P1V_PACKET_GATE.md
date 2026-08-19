PASS_EXPLAINER_PACKET

# Miru — Phase 1 results video packet gate

**Miru (second reviewer, fresh one-shot), 2026-08-19 ~09:1x KST.** Brief: `SEXTET_BRIEF_P1_VIDEO.md`;
kickoff: `KICKOFF_MIRU_P1V_PACKET.txt`. Method: local files only, grep/python extraction, receipts
rerun with python3. Findings-only; `portal.nersc.gov` untouched; no fetches. The packet
(`SCRIPT.md`, `STORYBOARD.json`, `CLAIM_LEDGER.md`, `LANA_ANNOTATION_REVIEW.md`, `VISUALS.md`) is
**gated PASS for the build step** (chain step 5, Tori). Every kickoff check below was re-run
independently this session; nothing was inherited from the done-files' self-reports.

## 1. Verdict summary

All eight gate checks pass. 0 repairs ordered. Five non-blocking watch items (§9) are handed to
Tori's build and to the render gate (chain step 6), led by the stale pre-amendment horn-2 label
sitting in `VISUALS.md`'s ladder description (W1 — the amended string is authoritative elsewhere
in the packet; the render must not source the label from that line).

## 2. Ledger completeness — PASS

- Script narration carries **48 factual sentences** (mechanical split; per-panel counts
  5/4/4/6/5/5/5/6/4/4 for panels 01–10) + 1 head scope line = **49 sentence rows**, and every one
  has a ledger row with a source citation. Per-panel ledger counts match exactly after removing
  the 4 annotation rows (a1–a4) from panels 03/09.
- **0 FLAG rows** in any ledger table (mechanical). 1 framing row (P08#1, transition) as declared.
- Totals reconcile with the ledger's own claims: 53 rows = 49 sentence rows + 4 annotation rows;
  52 MAPPED + 1 framing + 0 FLAG. All 11 headings ledgered (§2 of the ledger).
- F16 disclosure **independently verified**: my own retally of `TRACK_A_AUDIT.md`'s 23-row table,
  applying the disclosed dual-label resolution (12→POST-HOC, 16→ERROR, 21→CHECK, row 1 tallied
  with row 2's UNSUPPORTED substance), reproduces the certified tally **CHECK 8 / ERROR 4 /
  UNSUPPORTED 6 / POST-HOC 3 / UNFALSIFIABLE 1 / out-of-scope 1 = 23** exactly; the alternative
  (row 1 → CHECK) shifts ±1 only between CHECK and UNSUPPORTED, as disclosed. Load-bearing counts
  invariant.

## 3. Source-truth spot-checks — PASS (all receipts rerun this session, all exit 0)

| Kickoff item | Receipt rerun result | Packet rendering | Verdict |
|---|---|---|---|
| billion-times vs 1.09e9 | R1: excess over Planck Bianchi VII_h = **1.089e9**; Saadeh = **1.761e10**; (Ω/H)₀ = **0.828**; converse fraction = **8.432e-19** | "1.09 billion", "17.6 billion", "0.828", "less than 1 billion-billionth" (< 1e-18) | exact / safe direction ✓ |
| 46 sigma | R5 (sympy): Ω∝a⁻² ⇒ ρ∝a⁻⁴ ⇒ w = +1/3; Δw = **1.281** vs DES −0.948±0.028 ⇒ **~46σ** | "about 46 standard deviations" | exact at stated precision ✓ |
| C about 7 vs 7.2 [1.4,12.8] | R8 (sympy): headline C = **7.186**; bracket **[1.360, 12.781]**; R7: ω₀ = 1.666 H_ta (9π²/32 ✓) | "about 7.2", "1.4 to 12.8" | exact at stated precision ✓ |
| 12,000 universes vs 2.45e16/2.0e12 | R9: A = **1.915e-8** fiducial; **0.027σ** all-sky (σ_A = 7.07e-7); 3σ needs **2.45e16 galaxies = 1.2e4 universes**; best bracket edge **0.081σ**; strict/generous = **0.037** | "about 25 quadrillion", "roughly 12,000", "0.027", "at most 0.08" | exact at stated precision ✓ |
| dilution 2.5e30 / 2.5e22 | R10: stellar (10 M☉, a★=0.7) D_min = **2.496e30**; supermassive (10⁹ M☉) = **2.496e22** | "more than 10 to the power 30 / 22" (mantissa dropped) | safe direction, pairing correct ✓ |

Supporting reruns: R6 (radiation ω∝a⁻¹, matter/Λ ω∝a⁻², sympy dsolve ✓) backs panel 06. All five
cited doc line ranges re-read directly (A 27–53, 119–137; M 24, 43–47, 159–163; W 30–44, 78–80;
T 14–18, 77; F 11–43, 51–77) and match the ledger's mappings, including "no third reading"
(A 137, near-verbatim) and "real but weak" (F 66–74).

## 4. Script ↔ storyboard mirror and hashes — PASS

- **10/10 panels: narration byte-identical** between `SCRIPT.md` and `STORYBOARD.json`;
  10/10 assertion headings identical; 10/10 `narration_sha256` fields recompute to the exact
  narration strings; 10/10 `word_count` fields correct.
- `SCRIPT.md` SHA-256 recomputes to the pinned contract hash `befcce2b…`. All **12 authority
  SHA-256 pins** in the storyboard (brief, morning summary, 5 Phase 1 docs, 5 gate files)
  recompute to the files on disk. `STORYBOARD.json` SHA-256 = `6ae0aa42…`, matching the
  YUI_CW2 receipt.
- All five Phase 1 gate first-lines re-read independently: `PASS_TRACKA_AUDIT`,
  `PASS_MODELSPEC`, `PASS_DERIVATION_OMEGA`, `PASS_DERIVATION_TRANSFER`, `PASS_CONFRONTATION`.

## 5. Six approved strings / closed worlds — PASS

Each of the six approved strings is present **exactly once**, in the correct panel's
`viewer_text_closed_world`, and nowhere else:

1. Panel 03 `HORN 1: 10⁹ × PLANCK BOUND` ✓
2. Panel 03 `HORN 2: < 10⁻¹⁸ × DARK ENERGY` ✓ — **carries the amended "<"**; zero occurrences of
   the stale unamended form anywhere in the storyboard.
3. Panel 09 `Supermassive Parent` ✓
4. Panel 09 `Stellar Parent` ✓
5. Panel 03 `Λ = 3Ω²/c²` ✓
6. Panel 04 `w = +1/3` ✓

Equation-like strings appear in no other panel's closed world. Every VISUALS.md viewer-text
string (headings included) is contained in its panel's closed world; the only closed-world
entries beyond VISUALS.md's text are the four Lana-approved CW2 additions. No unreviewed
claim-bearing strings.

## 6. Must-not-say sweep — PASS

- "Smolin", "Popławski/Poplawski", "impossible", "refut": **zero hits** across narration,
  closed worlds, and VISUALS.md.
- "false"/"prove": only inside panel 10's required denial sentence ("We did not prove
  black-hole-universe cosmology false…"). The lone `proved` hit in SCRIPT.md is the substring of
  "Not approved for rendering" in the status header — not narration.
- No author name anywhere in the packet surfaces; the paper is cited as **arXiv:1910.10819 v2**
  (panel 02). Criticism maps to gated audit verdict rows; panel 04 states the clinical rule on
  screen ("ATTACK THE CLAIMS · NOT THE AUTHOR").

## 7. External-review caveat placement — PASS

"The strict model still awaits external theorist review before any publication claim." appears
**exactly once**: panel 07 of 10 (mid-video), in narration and in that panel's closed world
(`EXTERNAL THEORIST REVIEW STILL REQUIRED`). Zero occurrences in panels 08–10 narration or closed
worlds, and none in VISUALS.md panel 10. Panel 10 ends on the verdict with no trailing caveat —
matching the brief's "present but not terminal" rule and the storyboard's own
`forbidden_inferences: "a caveat after the verdict"`.

## 8. Structure contract — PASS

- Verdict complete in panel 01: the bounded verdict is panel 01's closing sentence, scope
  boundary present in the same panel; 69 words (≤72) at 34 planned seconds (≤35).
- Ends on the verdict: panel 10's final sentence is the verdict; `ends_on_verdict` is true only
  for panel 10 (mechanical).
- No divider cards: every panel carries an assertion heading + narration;
  `divider_cards_allowed: false`; panel 05's "ACT 2" line is body text inside a full panel, not
  a standalone divider.
- Duration: planned total 322 s ∈ [240, 360]; 730 narration words at 142 wpm ≈ 308 s.
- Narration is equation-free (mechanical: no =, Λ, Ω, ω, √, ∝, σ, superscripts) and uses digits
  throughout (no spelled-out numerals; every magnitude word carries a digit mantissa).
- Authorization block: all six flags `false`. Scope label present from frame zero (head row,
  panel 01 narration and closed world).

## 9. Comprehension check (no-physics viewer, both acts) — PASS with two observations

Act 1 reads as a trial story in plain words: a paper equated cosmic spin with dark energy; its
own numbers fail twice (a billion-fold mismatch; spin that thins like radiation and sits 46
standard deviations from the measurement the paper itself cites); only a narrow "galaxies may
lean one way" idea survives. Act 2 reads as a rebuild: freeze the idea's best version, derive
the missing conversion, compute the signal — and every load-bearing number is anchored by a
comparison a lay viewer can feel (billion times, 12,000 observable universes, powers-of-ten
dilution ladders). "Standard deviations" is never defined but is self-anchored by the
0.027-vs-3 contrast and the 12,000-universes translation. The two on-screen equations are the
brief's own directive and are labeled as the paper's equations turned against it. Observations
(non-blocking): "axis-carrying cosmic vorticity" (P05) and "pinned vector-perturbation
equation" (P06) are insider terms; both ride inside plain-words frames that carry the meaning,
and neither touches the verdict's intelligibility.

## 10. Watch items handed forward (non-blocking; no repairs ordered)

- **W1 (for Tori + render gate):** `VISUALS.md` line 50's ladder description still shows the
  pre-amendment label `HORN 2: 10⁻¹⁸ × DARK ENERGY` (no "<"). Lana's S2 amendment is explicit
  that the approved strings are authoritative and VISUALS.md stays untouched. The render must
  source ladder labels from the storyboard closed worlds / `LANA_ANNOTATION_REVIEW.md`, and the
  render gate must see the "<" (or the pre-approved exact variant `≤ 8.4×10⁻¹⁹ ×`) on screen.
- **W2 (word cap):** narration is exactly at the ≤730 cap (730/730). Any downstream wording
  repair must be word-neutral or shrink (Lana's flag, carried).
- **W3 (F14, disclosed):** "25 times below the generous edge" renders the confrontation doc's
  own rounded "0.04×"; the precise figure is 27×. The script understates the improvement — safe
  direction, both values sourced. No change ordered; a future swap to "about 27 times" costs one
  word and breaks W2's cap unless made word-neutral.
- **W4 (F16, verified):** dual-label verdict-row resolution disclosed in the ledger; my
  independent retally reproduces the certified tally (§2). Carried as context for any future
  re-audit, not as a defect.
- **W5 (source-doc caveats stay home):** the confrontation doc's two UNVERIFIED-AT-GATE items
  (Kerr Ω_H source pin; ECSK e-fold characterization) are confined to its error budget. The
  packet imports neither the e-fold numbers nor any unpinned formula claim (mechanical sweep of
  narration and closed worlds). Keep it that way in the render.

## 11. What I ran (evidence ledger)

- Read fully: kickoff, brief, SCRIPT.md, STORYBOARD.json, CLAIM_LEDGER.md,
  LANA_ANNOTATION_REVIEW.md, VISUALS.md, all five done-files; Phase 1 docs TRACK_A_AUDIT.md,
  MODEL_SPEC.md, DERIVATION_OMEGA_EVOLUTION.md, DERIVATION_TRANSFER_FUNCTION.md,
  CONFRONTATION_AND_INVERSION.md, MORNING_SUMMARY.md, GORU_INGREDIENTS.md, LANA_TA_DONE.md.
- Re-read first lines of all five Kun/Miru Phase 1 gate files (all PASS tokens present).
- Rerun with python3 this session (all exit 0): R1 `lambda_omega_check.py`,
  R5 `w_eos_check.py`, R6 `omega_evolution_receipt.py`, R7 `spherical_collapse_receipt.py`,
  R8 `transfer_function_receipt.py`, R9 `bound_mapping_receipt.py`, R10 `inversion_receipt.py`.
- Python mechanical checks (this session): SHA-256 of SCRIPT.md, STORYBOARD.json, and all 12
  pinned authority files; per-panel narration byte-identity, narration hashes, word counts;
  sentence counts vs ledger rows; FLAG-row scan; six-string placement and equation-placement
  scans; must-not-say greps; caveat-placement scan; structure-field checks; audit-table retally;
  magnitude-word contexts; equation-character sweep of narration.
- Not done (deliberately): no network, no file writes outside this report, no modification of
  any packet or Phase 1 file, no render-asset inspection (that is chain steps 5–6).

## 12. Uncertainties

- The stale VISUALS.md ladder label (W1) is the packet's one live inconsistency; it is
  documented, superseded in-packet, and caught here — but it is the single most likely
  propagation path into the render, hence the explicit render-gate instruction.
- Phase 0 pins (S1/S2 bounds, 2.0×10¹² galaxy supply, 18-universes figure, 5.24e-7 generous
  edge) were taken from the Phase 1 docs that carry them as gated imports; I did not re-open the
  Phase 0 lane. The R9/R10 inputs using them reproduce every packet figure at stated precision.

— Miru, packet gate, 2026-08-19. Findings only; packet files untouched.

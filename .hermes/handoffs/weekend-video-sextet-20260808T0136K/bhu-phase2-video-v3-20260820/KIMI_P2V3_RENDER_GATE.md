HOLD_P2V3_RENDER — token kimi-p2v3-render-hold-illus-chips-20260820T0345K

kimi (second reviewer, fresh one-shot), 2026-08-20 ~03:45 KST. Bounded render gate (last gate
before upload) per KICKOFF_KIMI_P2V3_RENDER.txt. Findings-only; zero edits; exactly one file
written (this one); zero fetches; portal.nersc.gov untouched. All mechanical checks recomputed
this session (shasum/ffprobe/python3/grep), not transcribed from prior seats. Stills audited
visually, all 16, against DESIGN_SYSTEM.md PART 1.

## 1. Custody — PASS

- shasum -a 256 build/BHU_PHASE2_EXPLAINER_V3_LOCAL_REVIEW.mp4 =
  8b8aa880acfe82ee9219e7cb712fb06bff6b94144a6a301113a13f23cf4eeb49 — byte-matches GPT3_F_DONE.md.
- Bytes: 36,401,083 — matches GPT3_F_DONE.md.
- ffprobe: 1920x1080, 30 fps, duration 706.833 s — inside the 600–720 s window. PASS.
- Still spot-shas: panel_01.png = 154a6775…b84fbb, panel_12.png = 72fbc78c…e634b — both match
  GPT3_F_DONE.md frozen records. 16 stills on disk.

## 2. ASR audit (stored records only) — PASS

- Coverage: 16 "## Panel NN" sections in ASR_QA.md; every panel transcribed from audio decoded
  from the final MP4 whose sha I independently re-verified in §1.
- The 1 cosmetic residual, quoted: panel 01, expected "link" → ASR "linked" ("the whole
  four-link chain" → "the whole four-linked chain"). Judgment: AGREED cosmetic — function-word
  morphology outside every protected claim; panel 01's three protected phrases all PASS in the
  same record. Contract-bearing residuals: 0 — accepted.
- Declared panel-16 normalizations ("mass mapped"→"mass map", "collapsed paper"→"collapse
  paper", verdict-word "root"→"route"): re-judged independently. These are spoken-homophone /
  Liaison artifacts of TTS→ASR, each bound to an exact local context, and the underlying TTS
  strings are byte-identical to STORYBOARD.json (GPT3 custody). The viewer hears the intended
  words. Accepted; flagged here only because the verdict word itself is involved.
- Required greps over the ASR transcripts (all hits quoted in ASR_QA.md, verified this session):
  - parent-spec clause (panel 12): "The 10 solar mass, spin 0.7 parent faces that extreme." ✓
  - Reading-1 clause: "Requiring the paper's uniform bounce caps inherited spin near one part
    in 10 to the power 27, with the treatment branches spanning roughly one order of magnitude." ✓
  - caveat sentence, mid-video (panel 15 of 16): "One honest caveat, both bounces sit in the
    Planck regime treated classically, and the strict chain awaits external theorist review." ✓
  - B-17 quote: "It would still be valid for a more realistic gravitational collapse of an
    inhomogeneous and rotating fluid." ✓
  - verdict ending (panel 16): "The ceiling says the route stays closed." (ASR "root" → declared
    normalization "route"; see above). ✓
- Scope-disclaimer sweep over the transcripts (disclaim / not-affiliated / educational-purposes /
  entertainment / opinions-expressed / on-behalf-of / do-not-represent / not-professional /
  independent-audit / we-do-not-speak): ZERO hits. PASS (presence would have been HOLD).

## 3. Frame audit — 16/16 stills inspected — 3 CHIP FAILURES

Per-still summary (heading / palette / composition all display-scale, dark cosmic, staged-build
on every panel — NONE looks like the retired v2 chart-frame style; the v2-style graphic-quality
bar failure count is 0):

- P01 rich cold open on the real generated backdrop; chips: content chips only — NO illustration
  chip (verified twice, corners/edges/bottom strip explicitly swept).
- P02 staged nursery diagram (programmatic fallback art); NO NebulaMind-rendering chip
  (verified twice).
- P03 ✓ illustration chip. P04 ✓ illustration chip; red diamond marker at the bounce beat.
- P05 ✓ illustration chip; both ladder edges labeled via chips ("LINED-UP EDGE" /
  "INDEPENDENT EDGE · EXACTLY 6 TIMES SMALLER"). P06 envelope icon card, no art, chips fine.
- P07 ✓ attribution "Figure 1, arXiv:1111.4595 (author version)" + citation chip; plot large.
- P08 ✓ attribution "Figure 2, arXiv:1111.4595 (author version)"; Planck marker present
  (red diamond by the spike) with "PLANCK SCALE · TESTED CLASSICAL RULES RUN OUT" chip in-panel.
  (Cosmetic: attribution pill overlaps the negative x-tick labels.)
- P09 ✓ illustration chip; parent-mass→baby map with rotation explicitly outside the map.
- P10 ✓ illustration chip; "STARTING BALL · EXACTLY 1 METER · ABOUT A DOORWAY · CHOICE UNSTATED".
- P11 B-17 quote card verbatim; "NO ROTATING MODEL" / "NO AXIS CALCULATION" chips ✓ — but the
  storyboard-spec'd illustration chip is absent from the still.
- P12 ✓ illustration chip; ε ≤ 10⁻²⁷ and "CEILING · NOT A MEASURED TRANSFER" chips present;
  red barrier present. (Still shows the ceiling beat; the parent-spec chip / overshoot arrow /
  "COSMIC SPEED LIMIT" label are staged-build beats not visible in this frame — the parent-spec
  chip IS in STORYBOARD.json and the clause is on the audio per §2. Observation, not a fail.)
- P13 ✓ illustration chip; a⁻⁶ = a⁻⁶ shown — permitted equation. P14 ✓✓ attribution chips
  "Figure 1/2, arXiv:1006.4166 (author version)"; both plots large.
- P15 ✓ illustration chip; "PLANCK REGIME" chip; range carried with both edges in-chip
  ("ABOUT 10,000 TO 100,000 TIMES BELOW THE FLOOR"). P16 verdict card composition, ends on
  "THE CEILING SAYS THE ROUTE STAYS CLOSED."

Named sub-checks:
- Display headings 16/16 ✓; dark cosmic palette 16/16 ✓; no divider-card still ✓.
- Attribution chips on all four paper-plot placements (P07, P08, P14×2) ✓.
- Equations across ALL stills: only ε ≤ 10⁻²⁷ (P12) and a⁻⁶ = a⁻⁶ (P13) — both in the ledger's
  three-permitted inventory (W3); the third (w-fork, P08) is a staged beat not in the still.
  Zero non-permitted equations. ✓
- Planck markers where bounces are drawn: P04 marker, P08 marker + Planck chip, P15 Planck chip ✓.
- Band ladders with both edges: P05 ✓ (both edges labeled); P15 both edges present in-chip
  (no separate ladder graphic in the still — observation).

HOLD basis — illustration/rendering-chip requirement fails on 3 stills:
1. P01 — the gate brief names this by name ("illustration chip on panel 01's generated
   backdrop") and DESIGN_SYSTEM PART 1 mandates the chip on every generated concept art. The
   still carries NO chip (double-verified). This is the video's opening frame and its only real
   AI-generated image: a photoreal black-hole/baby-universe render with no "Concept
   Illustration Only" marker — exactly what the chip rule exists to prevent.
2. P02 — programmatic fallback concept art (GENERATION_LOG: images 2–6 went programmatic) with
   no NebulaMind-rendering chip, against the same DS mandate and the brief's
   "NebulaMind-rendering on fallback-art panels".
3. P11 — STORYBOARD.json itself specs the illustration chip for this panel (the darkened
   shrinking-star backdrop); it is absent from the still.
Attribution-vs-illustration separation is the video's trust architecture; three misses is a
class failure, not a one-off. The fix is narrow and cheap: overlay the standard pill chip on
P01/P02/P11 and re-encode — no content, timing, or audio changes.

## 4. Arithmetic spot-check — PASS

P12 felt-comparison: "one grain in a billion-by-billion-by-billion grain cube" vs "1 part in
10 to the power 27". python3: (10**9)**3 == 10**27 → True. Exact match, as the ledger claims.

## Verdict

Custody, ASR, equations, Planck markers, ladder edges, palette, headings, no-divider,
arithmetic: all PASS. Zero stills fail the v2 graphic-quality bar. But the named chip check
fails on three stills (P01 generated backdrop, P02 fallback art, P11 spec'd backdrop) and the
brief gives that check no tolerance. HOLD_P2V3_RENDER. Re-gate after the three chip overlays;
everything else on this list stands as verified and need not be re-crawled beyond the three
replacement stills and the new mp4 sha.

— kimi, render gate, 2026-08-20.

## RE-GATE AFTER CHIP-FIX

PASS_P2V3_RENDER — token kimi-p2v3-render-regate-pass-20260820T0343K

kimi (same seat, fresh one-shot), 2026-08-20 ~03:43 KST. Bounded re-gate of the v3 render after
the chip-fix pass, per kickoff. Findings-only; nothing else edited; zero fetches;
portal.nersc.gov untouched. All mechanical checks recomputed this session.

### 1. Custody — PASS

- shasum -a 256 build/BHU_PHASE2_EXPLAINER_V3_LOCAL_REVIEW.mp4 =
  46b670a5ee083153a07629b90f80ec71a1b362d0a191f6178bfaa9035d51bd96 — byte-matches the
  CHIP-FIX value in GPT3_F_DONE.md. (First gate saw 8b8aa880…/36,401,083 B; the chip-fix
  re-encode changed the MP4 as expected; receipt now records 36,409,327 B.)
- build/PANEL_STILLS/panel_01.png = 65480e9d…8c8540 — matches receipt. (Differs from first
  gate's 154a6775…b84fbb exactly as expected: P01 was re-rendered with the chip.)
- build/PANEL_STILLS/panel_02.png = 33ee1dcd…d7114b — matches receipt.
- build/PANEL_STILLS/panel_11.png = 47170684…822186 — matches receipt.
- ffprobe duration = 706.833333 s — equals 706.833 s within rounding. PASS.
- 16 stills on disk; audio stream in container is AAC.

### 2. Chips — 3/3 PASS, wording adjudicated

All three fixed stills were re-inspected visually this session:

- P01: pill present lower-left, legible at display scale. Verbatim:
  "NebulaMind rendering — Concept Illustration Only".
- P02: pill present lower-left, legible. Same verbatim text.
- P11: pill present lower-right (below the "NO AXIS CALCULATION" tag), legible. Same verbatim
  text, em dash with spaces.

Wording adjudication (combined pill on P01, a Nano-Banana-generated image):

RULING: the combined pill is correct on all three stills; NO re-fix required.

Reasoning, explicitly:
1. The trust function of the chip rule — generated art must never be mistakable for
   evidence/observation — is carried by the categorical half "Concept Illustration Only".
   That half is present, legible, and unambiguous on P01; the viewer cannot read the frame as
   data. The harm named in my HOLD basis is fully closed.
2. The provenance half "NebulaMind rendering" is not the seat's improvisation: it is the
   verbatim DESIGN_SYSTEM wording. DESIGN_SYSTEM.md PART 1, Chip Designs, defines exactly one
   Illustration Chip — "NebulaMind rendering — Concept Illustration Only" — and mandates it
   on "every generated or programmatic concept art". PART 2 drafts those art briefs
   explicitly for Nano Banana Pro, so the DS itself intends this exact pill for
   Nano-Banana-generated panels. Applying the standard pill verbatim is spec compliance.
3. Inside this design system, precise provenance lives in the separate Attribution Chip class
   reserved for third-party scholarly figures ("Figure N, arXiv:XXXX (author version)") —
   where mis-crediting a real author would be a trust violation. Nano-Banana is a tool, not a
   rights-holder; "NebulaMind rendering" reads as production provenance (art rendered into
   the NebulaMind video), which is accurate. No misattribution of evidence or authorship
   results.
4. Observation, not a fail: if the project later wants per-generator credits on concept art,
   that is a DESIGN_SYSTEM revision affecting every panel uniformly — outside this gate.

### 3. Audio unchanged — receipt-accepted

GPT3_F_DONE.md CHIP-FIX PASS states the original AAC elementary stream was stream-copied
byte-for-byte, SHA-256 before/after
b4435da79b8432278f717bc7e4438af71510ff4c3ee302b80ba56a23c2d73efe, with all 16 narration WAVs
and the narration master byte-identical; ASR therefore unaffected, no rerun required. Per the
re-gate brief this statement is accepted as receipt-accepted, not independently recomputed.
Container audio stream verified to be AAC; duration 706.833 s consistent with the pre-fix
encode.

### 4. Prior PASS findings — carried

Not re-audited; cited as carried from the first gate (sections above): §1 custody of the
prior encode, §2 full ASR audit (16/16 panels, 0 contract-bearing residuals, zero
scope-disclaimer hits, all required clauses quoted), §3 frame audit of the 13 stills other
than P01/P02/P11, all named sub-checks (display headings 16/16, dark cosmic palette 16/16, no
divider cards, attribution chips on all four paper-plot placements, only permitted equations
ε ≤ 10⁻²⁷ and a⁻⁶ = a⁻⁶, Planck markers at drawn bounces, band ladders with both edges,
zero stills failing the v2 graphic-quality bar), and §4 arithmetic spot-check
(10⁹³ = 10²⁷ True).

### Re-gate verdict

The HOLD basis is fully cleared: the three named chip failures now carry the standard
DESIGN_SYSTEM pill, legibly, with wording adjudicated as spec-compliant on generated and
programmatic art alike. Custody of the re-encoded MP4 and the three replacement stills
byte-matches the receipt; duration in window; audio unchanged per receipt. All prior PASS
findings stand. PASS_P2V3_RENDER.

— kimi, render re-gate, 2026-08-20.

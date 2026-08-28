# LANA — meaning-drift veto reference (overnight video-quality track)

Per `HWAO_OVERNIGHT_VIDEO_QUALITY_20260810T0055K.md`. My only role tonight: **veto meaning drift**. I do
not open science and do not extend the four-lane motivation work (complete, held). This is the standing
reference the crew checks quality changes against — the claim-boundary-bearing text and states that a
craft fix may **restyle but must not alter in meaning**. Filed **2026-08-10 00:58 KST**. Lanes: spin
`4d230cc0`, fesc `01a4249b`, brightend `c772e643`, mzr-anchor `c892f3fa`, mzr-census `d6014ac0`.

## The seven ways a *quality* fix silently moves a *claim boundary* (my veto criteria)
1. **Heading/banner shortened** so a conditional or negation is dropped ("An apparent archival gap" →
   "Archival gap"; "NO RESULT GEOMETRY"/"VALUE WITHHELD" trimmed for a cleaner look).
2. **Card retimed below readable time on a withholding/boundary state** — a withholding a viewer cannot
   finish reading is effectively an absent withholding. Boundary and "VALUE WITHHELD" cards must stay
   legible after any pacing fix; shortening them is a *meaning* defect, not just a pacing one.
3. **Sentence trimmed** so the conditional clause is lost ("if one *were* genuinely more common, it
   *would*…" → "one more common… a fact about the universe").
4. **Consistency harmonization toward the more claim-y variant.** When lanes diverge, harmonize toward the
   **conditional/withholding** wording, never toward the barer one. Deciding "which is right" (the order's
   instruction) means: the safer boundary wins, then style is unified around it.
5. **Section rename that asserts** ("THE SHORTFALL" for "THE DISCRIMINANT/THE SWEEP"; "THE EXCESS" for "THE
   EVIDENCE PLANE").
6. **Colour semantics** that make a withholding state read as a result state (or vice versa) — the amber
   "NO MEASURED VALUE" banner and the withheld/boundary colour coding carry meaning; unify palette without
   swapping those roles.
7. **Motion** that turns a CONCEPTUAL illustration into apparent data — adding point-like marks to an empty
   plane or the mirror demo, or drawing a curve/crossing where the current design deliberately has none.

**Rule of thumb for any proposed edit:** if the restyle changes what a viewer would *believe the study
found*, it is not a quality fix — it is a claim change, and it is out of scope tonight regardless of how
much better it looks.

## Per-lane meaning-critical watchlist (must survive every craft edit, unchanged in meaning)

**Cross-lane invariant (all five):** the top-right amber banner **"METHOD DESIGN · NO MEASURED VALUE"** and
the `IF GENUINE` / `IF APPARENT` two-branch tags are claim-boundary furniture. Consistency work may unify
their exact wording/placement **but the chosen wording must keep the negation** — do not harmonize the
banner to anything that drops "NO MEASURED VALUE." This is the single highest-value cross-lane check.

- **spin `4d230cc0`** — symbolic `A = (N_CW − N_ACW)/(N_CW + N_ACW)`, **VALUE WITHHELD**, symmetric sign
  rail (A>0 more CW / A=0 equal / A<0 more ACW / **no sign selected**). Word is **"handedness," never
  "parity."** Mirror is **CONCEPTUAL — illustration, not data**. Sample/funnel counts allowed; **no
  asymmetry value, direction, or significance**. Motivation stays conditional.
- **fesc `01a4249b`** — title **"An apparent photon-budget mismatch has two explanations"** (the word
  *apparent* is load-bearing). Discriminant is a box diagram, **"MATCHED SWEEP DESIGN · NO RESULT
  GEOMETRY"** — **no envelope curves, no crossing** (this was the fixed defect; do not let a "motion" or
  "legibility" pass reintroduce drawn curves). `D(z)=f_required−f_inferred`, **VALUE WITHHELD**, balanced
  **REQUIRED LOWER / OVERLAP / REQUIRED HIGHER · NO SIGN SELECTED**. Boundary **NOT REPORTABLE: curve
  values · crossing or sign · claim about galaxies**. Forbidden OCR terms: *closure crossing, shortfall
  survives, deficit rises*.
- **brightend `c772e643`** — title **"An apparent archival gap has two explanations."** Evidence plane
  **"EMPTY PLANE · NO DATA POINTS" / "NO OBJECT POSITION SHOWN"** — **no plotted point** (a "legibility"
  or "motion" pass must not add a marker inside the axes). `N_slice` **VALUE WITHHELD**; boundary **NOT
  REPORTABLE: bright-end counts · luminosity-function pace**.
- **mzr-anchor `c892f3fa`** — title **"An apparent metallicity offset has two explanations."** Derivation
  pipeline only, **no MZR/offset plotted**. `Δ_Z=Z_high,direct−Z_reference,direct`, **VALUE WITHHELD**,
  **HIGH-Z LOWER / SCALES OVERLAP / HIGH-Z HIGHER · NO SIGN SELECTED**. Boundary **NOT REPORTABLE: offset
  value or sign · evolution verdict**. AM13 is a **display-only** reference (Andrews & Martini 2013) — a
  consistency edit must not upgrade it to a result frame.
- **mzr-census `d6014ac0`** — title **"Archive reach is not scientific eligibility"** (a methodological
  thesis, **not** a physics claim — do not let consistency work push a metallicity-physics heading onto
  this lane). **No lane-derived counts** (178/21/157 stay off per Hwao 08-09); banners **"NO SOURCE FREEZE
  · NO STAGE RESULT"** / **"STAGE OUTPUTS WITHHELD · NO ELIGIBILITY COUNT."** Boundary **NOT REPORTABLE:
  eligibility count/fraction · science interpretation**.

## How I will run tonight
- **Reactive veto.** For each proposed quality change (Goru consistency/pacing/motion, Kun audio/legibility,
  Yui's new versioned candidates), I check it against the criteria above and issue **PASS-no-drift** or
  **VETO (meaning drift)** with the exact word/timing/state at fault. Audio-only and pure-loudness changes
  carry no meaning and get a fast PASS.
- **Pacing is the danger zone.** Any retiming that shortens a title's *apparent*, a `VALUE WITHHELD`, a
  `NO SIGN SELECTED` rail, a `NOT REPORTABLE` boundary card, or a negation banner below readable time is a
  VETO even if the narration still fits — an unreadable withholding is a dropped withholding.
- **Consistency decisions:** when I'm asked "which lane is right," on any claim-bearing element I rule for
  the **conditional/withholding** variant and say so; on purely stylistic elements I defer to Goru/Kun.
- I will not author fixes, will not touch gates, and will announce nothing as `accepted_by_duho`. Fail-closed
  stays success; a precisely-described drift risk beats a hasty 3am rewrite.

No science opened; no motivation work extended; nothing public; all five candidates unchanged and their
cockpit links untouched.

---

## VETO LOG

### 01:03 KST — `KUN_OVERNIGHT_VIDEO_QUALITY_20260810T0055K.md` — **PASS, no meaning drift** (two implementation guards)
Kun's packet is an audit with three change-decisions. Checked each against the criteria above:
- **Audio normalize to −20.5 LUFS / peak ≤ −2.3 dBFS / LRA 6.5–7.8** — pure loudness; **no meaning
  impact. PASS.**
- **Cap card-seam quiet gaps at ~3.5–4.0 s (mzr-census/fesc)** — trimming inter-card *silence* (dead air),
  not narration or claim text; **meaning-neutral. PASS — with GUARD A.**
- **Boundary-card density fix** (the `KNOWN NOW / NOT REPORTABLE / NEXT SCIENTIFIC GATE` card should not
  run under a dense subtitle; either hold longer with a minimal subtitle, or split into two beats) —
  touches a **claim-bearing** card, so scrutinized: both options are meaning-safe **because they
  re-sequence or re-distribute text, they do not delete boundary content. PASS — with GUARD B.**
- Kun's "grammar to keep" (withheld-result banners, paired IF GENUINE/IF APPARENT cards) **is** the
  claim-boundary furniture — keeping it is correct.

**GUARD A (for Yui at implementation):** capping card-seam silence is fine **except** where that silence is
the viewer's reading time for a claim-bearing card — a `VALUE WITHHELD` / `NO SIGN SELECTED` rail, a
`NOT REPORTABLE` boundary column, or the conditional title (the word *apparent*). Do **not** cap a gap below
readable time on a withholding/boundary card; an unreadable withholding is a dropped withholding. Kun's own
"unless the animation genuinely needs more time" already allows this — I am making the claim-bearing-card
exception explicit.

**GUARD B (for Yui at implementation):** reduce the boundary card's density by **splitting the beat** or by
**moving text between card and subtitle** — **never by deleting** a `NOT REPORTABLE` clause, a withholding
line, or a conditional. The full boundary content must survive on the card. "Minimal subtitle" is fine only
if the boundary already lives in the card's `NOT REPORTABLE` column (it does).

**Corroboration (not my gate, but noted):** Kun's six-stop guardrail check on spin `4d230cc0` reports the
why-intro passes conditional-stakes, no-asserted-asymmetry, Longo/Shamir-as-contested, Land-not-settled,
no-black-hole-universe, and broad-reason-not-collapsed — consistent with my motivation spec and boundary.
That is Kun's/Tori's gate; I note only that it does not conflict with the claim boundary I own.

No change authored; no gate touched; nothing labeled accepted.

### 01:14 KST — `GORU_OVERNIGHT_QUALITY_SWEEP_20260810T0055K.md` — **PASS, no drift in the report; binding constraints on the remedy**
Goru's sweep is a defect report + three consistency decisions. Nothing in it *is* a meaning change yet;
my job is to constrain the remedy so meaning does not drift when Yui implements.

**Pacing defects — REAL, but the remedy is meaning-constrained (my primary ruling tonight).** Goru
correctly flags cards where dwell < reading time. Many flagged cards are **claim-bearing**: the conditional
intro cards (spin `i01/i05/i06`; siblings `i01–i04` carrying `IF GENUINE`/`IF APPARENT` and the "contested,
unsettled, no answer adopted" attribution), the withholding ledger cards (`f01/f02` "result counts not
displayed" / "method only"), the boundary card, the payoff (`x02`, incl. "NO RESULT CLAIM IN THIS CANARY"),
and the estimator sign-rail cards.
- **RULING:** on any claim-bearing card, fix the pacing defect by **lengthening dwell time or splitting the
  beat into two readable states — NEVER by trimming word count.** Those words carry the conditional ("if…
  were… would"), the source attribution that keeps Longo/JWST/MZR claims from reading as adopted truth, and
  the withholding/no-result lines. Cutting words to hit a reading-time budget is precisely how a pacing fix
  moves a claim boundary. If runtime balloons, **split, don't compress.** Word reduction is allowed only on
  purely descriptive/method cards (e.g. `d01`, method-flowchart `p`-cards) and only where it touches no
  conditional, withholding, attribution, or boundary text.
- Spin `i05/i06` specifically: do not trim the "claimed, challenged, left unsettled / this video adopts no
  answer" wording or the Longo conditional — that attribution is the safety valve, not filler.

**Consistency decisions — PASS on meaning, with guards:**
- **Section naming (spin 11 → unified 9):** meaning-neutral **only if the spin spine survives the merge** —
  the `two-worlds` setup beat and `mirror-climax`-as-PEAK must map onto `motivation`/`peak` without being
  dropped or reordered. The two-worlds setup is load-bearing: it is what makes the mirror read as a
  *discriminant*. A rename is bookkeeping; a beat-drop or reorder is a spine/meaning regression and I would
  veto that.
- **Card grammar (unstructured → `params`):** pure refactor; meaning-neutral **provided the re-render is
  pixel-equivalent on claim-bearing cards** (VALUE WITHHELD, NO SIGN SELECTED, NOT REPORTABLE, conditional
  title). Verify after migration.
- **End card ("… · method only"):** adopting the method-only end card on spin is **meaning-positive**
  (reinforces fail-closed) — PASS. *Out-of-my-lane note (provenance accuracy, for Goru/Tori):* "Sibling
  rollout authority" is imprecise for spin — spin is the template, not a rollout product; the authority
  citation should reflect spin's own provenance. Not a claim-boundary issue, so not a veto.

**Motion:** max near-unchanged run ≤0.5s across all five; no dead air, no decorative-vs-meaning problem
flagged. Meaning-neutral. PASS.

**Coordination note (Hwao's scope call, not my veto):** the section-arc + card-grammar migration on **spin**
would produce a materially restructured spin candidate, and spin `4d230cc0` is the one pending Duho's own
watch. New versioned candidate only, current link untouched — so no conflict with the pending watch; I flag
only that "restructure spin" is heavier than "polish spin," in case that affects sequencing.

No change authored; no gate touched; nothing labeled accepted.

### 01:38 KST — Yui `brightend-quality-canary-20260810T0136K` — **meaning-clean, but scope-blocked by Tori**
- **Custody (Tori's call, not mine):** Tori HOLD — built under Yui's superseded V1 all-five-lanes plan;
  Hwao's later active instruction authorizes **only one MZR-census audio-only A/B** ("normalize toward the
  series, cap routine seam silence, **never reduce any card's on-screen time**"). Not authorized; will not
  advance.
- **My meaning check (done anyway):** claim-bearing text **identical to frozen brightend** — title
  "An **apparent** archival gap…", i02/i03 conditional intact, withholding ledger f01/f02 intact, boundary
  b01 intact, payoff "without manufacturing… an archival result" intact, forbidden-terms guard intact.
  **No drift.** Not frame-verified (no need — scope-blocked; if ever authorized I'd frame-check the
  empty-plane-no-point and readable-withholding items).
- **Convergence:** Hwao's authorized-scope constraint *"never reduce any card's on-screen time"* is exactly
  my Guard A. Tonight's only authorized change (MZR-census **audio-only** + silence-cap, no card-time
  reduction) is **meaning-neutral by construction**. When it lands I confirm (a) audio-only, no on-screen
  text/timing edit; (b) no card's on-screen time reduced → PASS.

No change authored; no gate touched; nothing labeled accepted.
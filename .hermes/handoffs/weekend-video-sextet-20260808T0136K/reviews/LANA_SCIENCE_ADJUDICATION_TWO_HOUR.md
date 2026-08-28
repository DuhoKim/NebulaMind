# LANA — science adjudication, two-hour sibling completion track

Role per `HWAO_TWO_HOUR_SIBLING_ORDER_20260809T1620K.md`: **science adjudication per lane.** For each
*proposed* freeze — is there a defensible **non-circular** finding these exact bytes support, and what is
its boundary? Verify every anchor/literature claim against the **primary source** and quote it. I write
this report only; **I do not author freezes**, and a freeze flips `video_reportable_now` only with three
independent passes (Lana science + Kun adversarial + Tori custody). Opened **2026-08-09 16:24 KST**.
Window: start 16:18 · snapshots 16:38/17:18/17:58/18:18 · earliest finalization 18:18 · hard stop 18:33.

## Principles I am holding (from the order)

1. **Fail-closed is a real success.** A lane ending the window with `SOURCE_FREEZE` absent and a precise
   account of what is missing has done this task correctly. I will not soften the bar to unlock a video.
2. **Provenance is not permission.** A number that exists, hashes, and reproduces is still not reportable.
3. **No result may be back-read from the method-only decks** — they state none by design (I verified all
   four withhold their estimator). Nothing can be lifted out of them into a freeze.
4. **Anchor/literature claims must be quoted from the primary source at freeze time.** Freeze gates check
   internal coherence, not external truth; only a quoted primary source checks truth. A directional claim
   written from memory was frozen once and inverted a lane — I will accept no directional claim I have not
   read in the primary source. [[feedback_anchor_block_verify_from_source]]
5. **Standing publishable bar:** compiles + lint-clean + selection-honest ≠ publishable; assembly of
   published values + systematics commentary ≠ a study. [[feedback_autopilot_publishable_bar]]
   [[feedback_flagship_bar_original_content]]

## Current state (16:24 KST)
All four siblings: `SOURCE_FREEZE` **ABSENT**, last verified **2026-08-07** (two days stale). All four
video candidates PASS **method-only** — a statement about the deck, not the science; it unlocks nothing.
**No freeze proposal exists yet** (Goru authors those 16:38→17:18). New fesc `1420K/1501K` dirs checked:
still `video_reportable_now:false`, method-only — no result-bearing candidate is running ahead of a
freeze. So the default and correct adjudication right now, for every lane, is **FAIL-CLOSED pending a
proposal I can test.**

---

## Per-lane science boundary — the bar a freeze must clear

### fesc — reionization photon-budget z-sweep — **circularity hazard is SHARPEST here**
The source material reaches a directional result: **`66/83/93%` photon-budget deficits** with a **crossing
at "the source-supported redshift."** The lane's own two-world framing is *source shortfall (galaxies
really leak too little) vs assumption shortfall (proxy-transport / clumping / ξ_ion make the deficit)*.
A deficit magnitude **is computed from** an assumed clumping factor, an assumed ionizing efficiency
ξ_ion, and an f_esc **proxy calibration transported from low redshift** — the exact assumptions the lane
says are in question. **Stating `66/83/93%` (or "the deficit rises," "the shortfall survives," "a
crossing at z=…") as a finding is circular**: it presupposes the assumption set whose validity is the
open question. This is a strong fail-closed lane.
- **A freeze could only be non-circular** if it states the finding *strictly conditionally* — "under the
  predeclared assumption set A (clumping = …, ξ_ion = …, proxy calibration = … per [primary refs]), the
  required-vs-inferred gap is 66/83/93% at z=…, and this is not robust to A" — with **every element of A
  quoted from its primary source**, and the directional/robustness claim **withheld**. Absent that, fail
  closed. I will not accept the deficit as a result.
- **Primary sources a proposal MUST quote** (identify + quote, not cite from memory): the required
  ionizing-emissivity / photon-budget target (e.g. the Madau-style budget the required curve uses); the
  ξ_ion and clumping values adopted; and the low-z f_esc proxy calibration paper the inferred curve
  transports. I will read each and confirm the number and its *direction* before concurring.

### brightend — C41 bright-end UVLF archival gap
Source numbers: `92 of 112`, `6,417`, `176`, `453`. The honest finding is a **data-provenance /
reconstruction** statement (how much of a published bright-end summary is reconstructible from public
archives), **not** a UVLF bright-end number-density or "excess" claim. Non-circular *iff* framed as
reconstructability/eligibility with denominators intact; circular the moment it back-reads a luminosity
function or a bright-end abundance. Boundary: an archive-reconstruction result, not an astrophysical UVLF
result. A freeze must quote the primary bright-end catalogue/UVLF source whose objects it claims are or
aren't reconstructible.

### mzr-anchor — C41 high-z MZR calibration anchor — **most likely honest non-circular finding, and it is a NULL**
Source chain: `79 tables → 95 rows → 5 anchors`, plus a **mass-bin null**. The BRIEF itself states the bar:
*"Do not imply a calibrated high-z relation when the source only supports a sparse-anchor/gap result."*
The defensible non-circular finding here is exactly that **null/sparsity statement**: the archive yields
only **~5 direct-Te anchors** at high z — too few to calibrate the high-z MZR, so evolution-vs-calibration
**cannot be decided** with these data. That is honest, non-circular, and genuinely useful — but its
**boundary is a data-availability null, not a metallicity measurement and not an evolution verdict.** A
freeze stating "sparse anchors ⇒ undecided" is adjudicable; a freeze stating any Δ_Z sign/direction or "a
calibrated relation" is not. Anchor count and the "5 anchors" must be reproduced from the actual rows, and
any per-anchor abundance drawn into it must be quoted from its primary Te-measurement source.

### mzr-census — MZR archive census
Source funnel: archive → `178 → 157 → 62` eligible, recall `7/7`, control `0/3`. The defensible finding is
a **census/eligibility** statement (N archive tables are scientifically eligible for an MZR census, with a
7/7 recall and 0/3 contamination control), **not** a metallicity result. Non-circular as a
data-availability/method finding with denominators and dropped-row reasons explicit. Boundary: eligibility
of tables, never an MZR value or slope. Recall/control (7/7, 0/3) must be reproduced from the actual
check, and any "known-complete reference set" the recall is measured against must be quoted from its source.

---

## Snapshot 1 — 16:38 KST target (state at 16:24)

| lane | freeze state | blocker (science) | exact next action (mine) | gate status |
|---|---|---|---|---|
| fesc | ABSENT | deficit finding is circular vs the lane's own assumption question; no primary-source quotes yet | adjudicate Goru's proposal when it lands; require conditional framing + quoted ξ_ion/clumping/proxy refs, else FAIL-CLOSED | all closed |
| brightend | ABSENT | no proposal; risk = back-reading a UVLF from reconstruction counts | adjudicate proposal; confine to reconstructability, denominators intact | all closed |
| mzr-anchor | ABSENT (`SOURCE_HASHES_INITIAL` present, empty `source_freeze/`) | no proposal; only defensible finding is a **null** (sparse anchors), not a relation | adjudicate proposal; accept only a bounded null, reproduce the 5-anchor count | all closed |
| mzr-census | ABSENT | no proposal | adjudicate proposal; confine to eligibility, reproduce 7/7 & 0/3 | all closed |

**Adjudication so far: FAIL-CLOSED on all four** — correctly, because there is nothing to adjudicate yet.
This is success-shaped, not a blocker to escape. I am ready to test proposals the moment Goru files them,
and I will read primary sources before concurring with any anchor claim. No freeze authored; no gate
touched; `video_reportable_now` stays `false` on every lane.

---

## ADJUDICATION of Goru's proposals — 16:30 KST

Goru filed `lanes/<lane>/GORU_PROPOSAL.md` for all four. Three are fail-closed; one is a proposed
method-only custody freeze. My science pass:

### fesc / brightend / mzr-census — Goru proposes FAIL-CLOSED — **I CONCUR**
No `source_freeze/`, no primary-source docs, no finding proposed. There is nothing to adjudicate and
nothing is claimed — this is the correct, success-shaped outcome, and the blocker (missing primary
sources) must be **deepened, not bypassed**. Reinforcing note on **fesc**: even if pushed, the reachable
`66/83/93%` deficit is **circular** — it is computed from the clumping / ξ_ion / low-z proxy-transport
assumptions whose validity is the lane's own two-world question, so it cannot be stated as a finding
absent a fully-quoted, explicitly-untested assumption set. Fail-closed is correct here on the merits, not
just for want of files.

### mzr-anchor — Goru proposes a **method-only custody freeze** (`video_reportable_now:false`) — **I CONCUR on science, within stated limits**

**What the proposal is.** A `SOURCE_FREEZE` pinning the source artifacts (paper, `T3_REAL_RESULTS.json`,
etc.) with `video_reportable_now:false`, `allowed_scope: [method-only, anchor-building method]`, and
`forbidden_scope: [table counts, anchor yield, mass-bin occupancy, offset sign, evolution verdict]`. It
**states no result** and forbids every result-bearing claim. It does **not** flip the reportable flag and
is not the three-pass result freeze. On science it is safe: no circular or unverified claim enters.

**Is there a defensible non-circular finding these bytes support? — YES, and it is a NULL.** I read the
primary bytes (`ANCHOR_GAP_PAPER.tex` abstract + `T3_REAL_RESULTS.json`). The paper is explicitly *"a
census and a null."* A frozen-contract VizieR enumeration (79 λ4363-class tables → 8 reachable → 95 rows
at z>3 with tabulated auroral flux) yields **exactly 5 contract-grade direct-Te anchors** (z=4.015–8.496;
O/H=7.109–8.032); every mass bin has N≤2 → "no-verdict-possible"; the pre-committed forecast expected ~25.
Finding: **the public archives fall short of the direct-Te anchor set needed to settle the high-z
calibration dispute by ~an order of magnitude, so no deficit verdict of any size or direction is possible
at uniform rigor.** This is non-circular and original — a *pre-registered forecast vs realized yield*
information-content result, not assembly-of-published-values. **Boundary: a data-availability null against
a frozen forecast — NOT an evolution verdict, NOT an offset sign, NOT a calibrated high-z relation.** The
current proposed freeze correctly does not state even this null (it forbids `anchor yield`); stating it
would be a *separate, higher-bar* result freeze needing all three passes.

**Primary-source verification of the one anchor claim — DONE.** The lane refers abundances "for display
only" to the **AM13 (Andrews & Martini 2013, ApJ 765, 140)** Te-anchored MZR, eq.5 asymptotic form
`8.798 − log10(1+(10^(8.901−logM))^0.640)`. Verified against the primary source (IOPscience / ADS /
author record): AM13 turns over at log M*=8.9 and asymptotes to 12+log(O/H)=8.8 — matching the pinned
`8.901` / `8.798`. My arithmetic: AM13(8.0)=**8.119**, matching the published-form table (8.12). The
`~0.14 dex` discrepancy the data flags is between this **correct** published form and an **erroneous crew
arithmetic (~8.26)**; the published form is right, and the note correctly marks the discrepancy REPORTABLE
and refers it to T4 rather than averaging it away (Kun B3). Honest handling confirmed.

**Two flags I carry forward to any RESULT-bearing mzr-anchor freeze (not the current one):**
1. The `−0.69±0.03` z≈9.3–10.6 offset (paper line 431) is a **directional** number against the AM13 frame
   from a *different* (z9-10) sample. It must be quoted from its own primary source and kept strictly
   outside the census-null's boundary; it is not this census's result.
2. Any freeze that states the null must reproduce the 5-anchor count from the actual T3 rows and cite AM13
   eq.5 with the verified 8.798/8.901 parameters — never a directional metallicity claim from memory.

**My verdict:** on science, the mzr-anchor **method-only custody freeze is sound** — no result, scope
science-correct, single anchor claim primary-source-verified. This is **one of three** passes and is
**not** a result authorization: `video_reportable_now` stays `false`; Kun (adversarial rebuild) and Tori
(custody/hash) still owe theirs. I did not author the freeze.

## Snapshot 2 prep — 16:30 KST

| lane | freeze state | blocker (science) | exact next action | gate |
|---|---|---|---|---|
| fesc | ABSENT / fail-closed | deficit is circular + no primary sources | deepen blocker; list the ξ_ion/clumping/proxy refs a conditional finding would need | closed |
| brightend | ABSENT / fail-closed | no primary sources | deepen blocker; confine any future finding to reconstructability | closed |
| mzr-census | ABSENT / fail-closed | no primary sources | deepen blocker; confine to eligibility census | closed |
| mzr-anchor | PROPOSED (method-only custody) | none on science — I CONCUR; awaits Kun + Tori | Kun break-test, Tori custody; keep result freeze (the null) as a separate higher bar | closed |

No gate touched; no freeze authored; `video_reportable_now` stays `false` on all four.

---

## DEEPENING — historical worker freezes as stale inputs; quote the primaries — 16:36 KST

Per `HWAO_DEEPENING_ORDER_HISTORICAL_FREEZES_20260809T1628K.md`. I read all four historical
`worker-yui/SOURCE_FREEZE.json` as **stale suspect inputs**. **No field crossed into any active
adjudication** — every fact below I re-derived from the primary bytes today. Three of the four historical
files assert a reportable decision; I treat all such decisions/verdicts/flags as **absent** and re-derive.

### Literature / anchor claims — verified against primary sources
- **mzr-anchor**: AM13 (Andrews & Martini 2013, ApJ 765, 140) asymptote 8.798 / turnover 8.901 — verified
  against the primary source (§ above); used "for display only"; AM13(8.0)=8.119 confirmed.
- **c41-uvlf**: the only literature figure, `lit_uvlf_alpha.png` (UV faint-end slope α vs z), is
  **explicitly REJECTED as central evidence** in the freeze and is not used — so **no directional
  literature claim rides into this lane**. Confirmed.
- **mzr-census**: `lit_metallicity.png` is **REJECTED_FOR_THIS_CENSUS** (it visually implies a metallicity
  measurement). No literature anchor in scope. Confirmed.
There is therefore **no directional literature claim written from memory** in any active proposal; the one
real anchor (AM13) is primary-verified.

### c41-uvlf release blocker (a) — FlagshipStudies clearance copy — REAL; reconciliation is Hwao's + gated
- **Primary re-derivation** (`c41-brightend-uvlf-pace_history.json`, revision[5]): `feedbackBy: Duho`,
  `feedbackText: "land the gap paper on the Lab"`, summary "Shape-1 gap paper landed as a flagship
  study… Referee ESTABLISHED." So Duho **did** direct a **Lab landing** of the *paper* on 2026-08-05.
- `FlagshipStudies.tsx:117` renders `{verdict} · not accepted` as a **generic hardcoded suffix on every
  flagship card** — it means *not journal-accepted*, which is also true (freeze's own allowed wording:
  "human-cleared for Lab landing; not journal-refereed… not published as a journal result").
- **Adjudication:** both are true under different senses of "accepted" — Duho cleared it *for Lab landing*;
  it is *not journal-accepted*. The stale generic copy is misleading only if read as "Duho didn't clear
  this study." Fixing it is Hwao's reconciliation and touches `FlagshipStudies.tsx` — **gated**:
  exact-diff packet, never applied, until Duho's exact-bytes acceptance. **Decisive limit:** this is a
  2026-08-05 clearance of the *paper*; it **does not cross** to authorize the 2026-08-09 *video*. No agent
  may label anything `accepted_by_duho`; the video needs its own Duho check-in on exact bytes. Fail-closed
  for the video.

### c41-uvlf release blocker (b) — "30 vs 34 disqualified" — SEMANTIC MISMATCH → ESCALATE
- **Primary re-derivation** (`t3census_v3a_console.log`, run 2026-08-05): **exactly 30 catalogs carry
  `verdict=disqualified`** (11 model-or-simulation, 9 non-extragalactic-stellar, 5 wrong-quantity-surface-
  brightness, 4 non-cosmological-target, 1 binned-summary), plus 1 `pending`. Public `FlagshipStudies.tsx`
  meta "30 disqualified" therefore **matches** the primary `verdict=disqualified` count.
- The freeze's "34" is **not reproduced** by that definition. `CENSUS_DIGEST.md` decomposes 112 as
  "67 counted / 31 closed-per-verdict / 4 v1-disqualified / 10 skipped" — so "34" is most likely
  30 T2a-disqualified **+ 4 v1-disqualified**, a *broader* definition. This is a genuine **semantic
  mismatch on what "disqualified" counts**, not an arithmetic error. **Per the order I escalate to Hwao
  rather than resolve it.** What I can state from primary bytes: 30 is the literal `verdict=disqualified`
  count and matches the public number; any "34" must have its definition pinned before either figure is
  presented. Neither crosses into an active proposal until defined. Fail-closed on the count.

### c41-uvlf release blocker (c) — 453 denominator / six-table geometry — NOT defensible without the supplement
- **Primary re-derivation** (`T3_CENSUS_SAMPLE.jsonl`, fresh count today): in 10≤z<11.5 there are **453**
  rows (176 at muv≤−20) across **6** source tables, of which **`J/A+A/704/A339/lephare` supplies 420 —
  93% of the slice** — using field `NUVMAG` with a recorded rest-NUV band mismatch. Reproduces the freeze
  exactly.
- **Adjudication:** a 453 "denominator" that is 93% one catalogue, in a UV-like band that is not
  homogenized to rest-frame 1500 Å M_UV, **cannot be presented as a multi-catalogue census denominator** —
  it would imply independence the data do not have. The blocker is **correct**: fail-closed on the 453
  denominator / six-table geometry until an audience-reachable supplement discloses the provenance
  domination and band caveat, and that supplement is Hwao-verified. It remains an unpublished proposal and
  is **gated**. Not reportable now.

### mzr-census allowed list incl. `178 − 21 = 157` — sound science, but Hwao's removal was stricter than the frozen boundary, and correctly so
- **Science:** the `178 − 21 = 157` conservation is a data-informatics **enumeration** identity over T1
  metadata counts; it is independently reproduced (`GORU_T2_RECOUNT.md`: "reproduced 178/21/157, 62, 7/7,
  0/3"), internally coherent, and correctly bounded by the freeze as **not** an eligibility count and
  **not** a metallicity measurement (scientific_class: "archive infrastructure / informatics census").
  On its own merits the count is defensible and non-circular.
- **But its *presentation* is not currently authorized.** The historical freeze's `allowed` list is a
  stale **decision/boundary** that **does not cross** (deepening order). The counts are lane-*derived*
  empirical outputs, not raw source facts — re-hashing the manifest confirms bytes but does **not**
  re-derive the counts, and *provenance is not permission*. Absent a live freeze that re-derives them and
  passes Lana+Kun+Tori, they stay off.
- **Plainly:** **YES — Hwao's 2026-08-09 order to remove the counts as lane-derived empirical output was
  STRICTER than the lane's own 08-08 frozen boundary**, which explicitly *allowed* `178 − 21 = 157` under
  strict scope. And the stricter stance is the **correct** current posture: the frozen "allowed" is a
  stale decision that cannot authorize the counts today. The counts may return to a video only after a
  fresh freeze re-derives them and clears all three seats. Fail-closed until then.

### Snapshot 3 prep — 16:36 KST
| lane | freeze state | blocker (science) | exact next action | gate |
|---|---|---|---|---|
| fesc | ABSENT / fail-closed | deficit circular; historical freeze `False` anyway | Goru re-hash paths only; no field imports | closed |
| brightend (c41-uvlf) | ABSENT active; historical says local-proposal-only | (a) clearance is paper-not-video & gated; (b) 30 vs 34 semantic → **escalated to Hwao**; (c) 453 is 93% one table → fail-closed | Hwao reconciles (a)/(b) as gated packets; (c) needs verified supplement | closed |
| mzr-census | ABSENT active | 178−21=157 sound but stale-allowed can't cross; Hwao removal stricter & correct | keep counts off; re-derive only under a fresh freeze | closed |
| mzr-anchor | PROPOSED (method-only custody) | none on science (AM13 verified); the real finding is a NULL | awaits Kun + Tori; result freeze is a separate higher bar | closed |

**No historical field imported. No freeze authored. No gate touched. `video_reportable_now` stays
`false` on all four.** One item formally **escalated to Hwao**: the 30-vs-34 "disqualified" definition.

## Snapshot — 17:19 KST (17:18 mark) — three-seat convergence, fail-closed

State re-read at the mark: all four `lanes/<lane>/SOURCE_FREEZE.json` **absent**; no
`video_reportable_now:true` anywhere; no result-bearing Yui candidate; no historical field imported.
**The three independent adjudications have converged fail-closed:**
- **Lana (science):** fail-closed on fesc/brightend/mzr-census; mzr-anchor method-only custody freeze is
  science-sound but authorizes nothing (its finding is a null); primaries quoted (AM13 verified); c41-uvlf
  blockers hold; 30-vs-34 escalated.
- **Kun (adversarial):** all four **BLOCKED FOR RESULT**, method-only PASS only — "a fail-closed success
  state"; concurs on the three fail-closeds; flags the stale `lane-c41-mzr` `reportable:true` as an attack
  surface to block. Consistent with my read.
- **Tori (custody):** `PASS_NONIMPORT_CHECK` — no decision/verdict/boundary/reportability field crossed;
  grants no permission.

| lane | freeze | result | note |
|---|---|---|---|
| fesc | ABSENT | BLOCKED | deficit circular; historical freeze was `False` anyway |
| brightend | ABSENT | BLOCKED | (a) paper-not-video & gated; (b) **30-vs-34 escalated**; (c) 453 = 93% one table |
| mzr-census | ABSENT | BLOCKED | 178−21=157 sound but stale-allowed can't cross; Hwao removal stricter & correct |
| mzr-anchor | ABSENT active (custody freeze *proposed*) | BLOCKED | AM13 verified; real finding is a NULL; separate higher bar for a result |

No lane flipped. Fail-closed is the outcome and it is correct. Remaining window marks 17:58 / 18:18
(earliest finalization) / 18:33 hard stop; I hold this posture and re-adjudicate only a genuine
result-bearing proposal, at the higher bar, with primary quoting.

---

## RULING — 30-vs-34 "disqualified" (Hwao's escalation back to me) — 17:28 KST

Hwao held fail-closed and asked me to rule whether 30 or 34 is defensible and to state **which digest
categories each number must declare**. I re-derived the full partition from the **primary console log**
`t3census_v3a_console.log` (SHAPE1_T3_CENSUS_V3, 2026-08-05 10:48) — this pins the definition by evidence,
not by picking a reading that agrees:

- **31 `census CLOSED` events** (= digest "31 closed-per-verdict") decompose as **30 `verdict=disqualified`
  + 1 `verdict=pending`**. The pending one is named: `J/ApJ/963/9/table5` (class=pending-evidence). So the
  31st closed-per-verdict is *not* a disqualification — it is the pending.
- **4 `census DISQUALIFIED` events** (= digest "4 v1-disqualified"): `J/MNRAS/485/586/table5,6,7,8`, each
  "per T2a eligibility (recorded reason, not incidental)."
- **Disjointness verified:** the 4 v1 catalogs do not appear among the 30 closed-verdict-disqualified
  (overlap empty). The digest partition 67+31+4+10=112 is a true partition, so the 4 and the 30 are
  distinct tables.

**This resolves Hwao's `31+4=35` concern.** 35 is the naive over-count that treats all 31 closed as
disqualified; the log shows only 30 of them are, the 31st being pending. **Total distinct disqualified =
30 (T2a) + 4 (v1) = 34**, primary-verified and disjoint.

### Ruling
- **34 is defensible** as *"tables disqualified with recorded reasons across the 112-table layer"* — it is
  the disqualified subset of `closed-per-verdict` (30) **plus** `v1-disqualified` (4). It must **declare**
  that it spans both the v1 and T2a phases and **excludes** the 1 pending (`J/ApJ/963/9/table5`), the 67
  counted, and the 10 skipped.
- **30 is NOT defensible as written.** `FlagshipStudies.tsx:69` says *"112-table eligibility layer (30
  disqualified with recorded reasons)"* — read against the whole 112-table layer, that reads as the total,
  but the total is 34. 30 **omits the 4 v1-disqualified**, which *also* carry recorded reasons ("per T2a
  eligibility, recorded reason"), so they belong under the same "disqualified with recorded reasons"
  label. 30 is only defensible if **relabeled** to declare it is the **disqualified subset of the 31
  closed-per-verdict** (excludes v1-disqualified and the pending).
- **Category declaration each number must carry:**
  - `30` → `[closed-per-verdict ∩ verdict=disqualified]` (30 of 31; the 31st is pending). Excludes
    `v1-disqualified`.
  - `34` → `[closed-per-verdict ∩ disqualified (30)] + [v1-disqualified (4)]`. Excludes the 1 pending, the
    67 counted, the 10 skipped.
- **Correct fix (a prepared finding only; `FlagshipStudies.tsx` is GATED):** the discrepancy is not "the
  frozen number is wrong" — 34 is the complete, correct total. The **public 30 is the incomplete figure**
  and should become **34** (or be relabeled to its T2a-closed-per-verdict scope). I state this from the
  primary evidence — the 4 named v1-disqualified tables — not from assuming the public number was wrong;
  the evidence is what shows it is. Do **not** change 34 downward. Nothing is applied; this is an exact-diff
  finding for Hwao, never a fix, until Duho's exact-bytes acceptance.

## OWED — primary-source quotes per lane (consolidated)

- **mzr-anchor** — *AM13 anchor:* Andrews & Martini 2013, ApJ 765, 140 — primary source: the direct-method
  MZR "turns over at log(M⋆)=8.9 and asymptotes to 12+log(O/H)=8.8" (verified via IOPscience / ADS /
  author record), matching the lane's `8.798 − log10(1+(10^(8.901−logM))^0.640)`; AM13(8.0)=8.119
  reproduced; used "for display only." *Paper's own finding (`ANCHOR_GAP_PAPER.tex` abstract, quoted):*
  "exactly **5** survive as contract-grade direct-\te{} anchors with linked stellar masses (z=4.015–8.496;
  O/H=7.109–8.032) … no stellar-mass bin reaches the pre-committed 3-anchor minimum, so **no deficit
  verdict of any size or direction is possible** … This paper is a census and a null." → the one
  defensible finding is that **null**.
- **brightend (c41-uvlf)** — *No literature anchor:* `lit_uvlf_alpha.png` is REJECTED ("plots literature
  UV faint-end slope α vs z and does not demonstrate search reach…"). *Clearance primary:*
  `c41-brightend-uvlf-pace_history.json` rev5, Duho, "**land the gap paper on the Lab**" — a paper
  Lab-landing, not a video acceptance. Census facts re-derived above.
- **mzr-census** — *No literature anchor:* `lit_metallicity.png` is REJECTED_FOR_THIS_CENSUS. *Counts:*
  `GORU_T2_RECOUNT.md` independently "reproduced 178/21/157, 62, 7/7, and 0/3."
- **fesc** — no primary quote crosses; fail-closed. The reachable 66/83/93% deficit is assumption-laden
  (clumping / ξ_ion / low-z proxy transport) and therefore circular vs the lane's own question; a quoted,
  explicitly-untested assumption set would be required even to state it conditionally, and none is proposed.

## RULING — was Hwao's 08-09 removal of `178 − 21 = 157` stricter than the lane's frozen boundary?

**Plainly: YES — it was stricter, and it was correct; you were not wrong.** The lane's own 08-08 frozen
boundary *explicitly ALLOWS* "modifier-filter conservation 178 − 21 = 157" under strict scope; your 08-09
order removed it. So the order is unambiguously stricter than the frozen boundary. It is nonetheless the
right call, on **authorization**, not on science: the frozen "allowed" is a stale decision that cannot
cross into today's no-freeze video (deepening order), and *provenance is not permission* — a reproduced
count is still not an authorized one. **One honesty for the record:** the removal is correct because the
counts are *unauthorized*, **not** because they are scientifically illegitimate — `178 − 21 = 157` is a
sound, independently-reproduced informatics enumeration, correctly bounded as not-eligibility and
not-measurement. If a fresh freeze re-derives it and clears all three seats, it is a defensible thing to
show. So: your order was stricter than the frozen boundary and right; just don't let it be read as "the
counts are wrong" — they are fine, they are merely not cleared.

---

## Derivation-receipt ruling acknowledged — 17:38 KST (`HWAO_RULING_DERIVATION_RECEIPTS_20260809T1736K.md`)

The ruling is correct: provenance is not visible in a value (`false==false` is benign only by luck;
`true==true` would authorize a result nobody re-derived), so every installed scalar needs a receipt naming
what it was derived from and when — not just the suspicious ones. It is chiefly Goru's (author) and Tori's
(custody) to enforce, and there are currently **no installed freezes** to receipt. But it applies to my own
rulings, so I audited them: each number I ruled on I re-derived today from a named primary source —
**except** `178-21=157`, which I had backed with the *historical* `GORU_T2_RECOUNT`. **Gap now closed with
a fresh receipt:**

- **`178 / 21 / 157` — re-derived today 2026-08-09 17:37 KST** from primary `T1_MZR_MANIFEST.json`
  (hash `b883b3a6f602...`, **re-verified == freeze-recorded hash**): `n_candidates_pre_filter = 178`,
  `dropped_candidates` = **21** entries, `n_candidates = 157`, and the `candidates` list itself has **157**
  members (independent cross-check); `T1_FINDINGS.md:22` corroborates ("178 candidates; 21 dropped ... 19 on
  redshift, 2 on abundance ... 157 in the manifest"). My "sound informatics enumeration" claim now rests on
  a fresh, dated, hash-verified derivation, not a historical recount. **Authorization is unchanged:** the
  counts remain **off/unauthorized** absent a fresh installed freeze cleared by three seats — re-derivation
  is not permission.

Receipt-status of my other ruled scalars (all derived today from named primaries): **34/30** from
`t3census_v3a_console.log` (31 CLOSED = 30 disqualified + 1 named pending; 4 named v1-disqualified;
disjointness checked); **AM13 8.798/8.901** from Andrews & Martini 2013 (primary, web-verified) with
AM13(8.0)=8.119 recomputed; **5 anchors** from `ANCHOR_GAP_PAPER.tex` + `T3_REAL_RESULTS.json`; **453/420
(93%)** from a fresh count of `T3_CENSUS_SAMPLE.jsonl`. Each carries what it was derived from and when.

Standing unchanged: strict installation block on all four, active `SOURCE_FREEZE` count 0, no reportable
true/YES, no `accepted_by_duho`, gates closed. Fail-closed remains the successful outcome.

---

## Self-description ruling — self-audit of my receipts — 18:02 KST (`HWAO_RULING_SELF_DESCRIPTION_20260809T1800K.md`)

The V3 defects (a V3 file declaring V2; a receipt naming a provenance it does not have; "immutable" on
0644) are self-description defects in **Goru's proposal bundle** — Goru's V4 and Tori's custody to fix;
nothing is asked of the science seat and the standing is unchanged. But **defect 3** — "a receipt that
misstates its own provenance… a gap wearing the uniform of a check" — is the same test applied to my own
derivation receipts, so I audited them for false/boilerplate provenance. **Each names the operation that
actually produced the value**, not a generic source:

- `178/21/157` — operation: `json.load` of `T1_MZR_MANIFEST.json`, read fields
  `n_candidates_pre_filter`/`dropped_candidates`/`n_candidates` **and** counted the `candidates` list
  (157) as an independent cross-check; source hash re-computed and compared to the freeze-recorded value.
- `34/30` — operation: `grep`-count of verdict/event tokens in `t3census_v3a_console.log` (31 CLOSED = 30
  disqualified + 1 pending; 4 `census DISQUALIFIED`), plus a `comm` disjointness check on catalog names.
- `AM13 8.798/8.901` — operation: primary-source read (Andrews & Martini 2013 via IOP/ADS) + arithmetic
  recompute of AM13(8.0)=8.119.
- `453/420` — operation: fresh `json`-parse + z-slice filter + table `Counter` over `T3_CENSUS_SAMPLE.jsonl`.
- `5 anchors` — operation: quoted from `ANCHOR_GAP_PAPER.tex` abstract + `T3_REAL_RESULTS.json` bins.

No boilerplate source string, no claimed-but-absent provenance, no value asserted about itself that the
operation does not support. My receipts pass the standard that caught the V3 bundle. (This is confirmation,
not a fix — the defect is Goru's to repair in V4.) Fail-closed holds; no finalization before 18:18.

---

## WINDOW CLOSE — 18:18 KST (`HWAO_TWO_HOUR_FINALIZATION_20260809T1818K.md`)

Outcome: **FAIL-CLOSED on all four lanes — the successful outcome as directed.** Active `SOURCE_FREEZE`
count 0; no result-bearing candidate built; nothing uploaded/published/replaced/wired/deployed;
`accepted_by_duho` nowhere. Four method-only candidates remain byte-exact (`d6014ac0`, `c772e643`,
`c892f3fa`, `01a4249b`); protected manifests / `paperVideos.ts` / Git at the 16:24 baseline.

**My seat's contributions this window:** per-lane science boundary; adjudicated Goru's proposals (3
fail-closed, mzr-anchor method-only custody only); deepening — primaries quoted (AM13 verified; both
literature figures REJECTED; clearance = paper-not-video), c41-uvlf blockers adjudicated, no historical
field crossed; **30-vs-34 resolved from the primary log**; `178−21=157` ruled (stricter-than-frozen &
correct, on authorization); derivation receipts for every scalar, self-audited clean.

**Note for when 30-vs-34 reaches Duho.** The finalization lists it as owed, "both authors must declare
which categories their number includes." **That declaration is already done in my 17:28 ruling** — derived
from the primary console log, one level below the digest: the 31 closed-per-verdict = 30 `disqualified`
+ 1 `pending` (`J/ApJ/963/9/table5`), and the 4 v1-disqualified (`J/MNRAS/485/586/table5–8`) are disjoint,
so:
- `30` = `[closed-per-verdict ∩ disqualified]` (excludes the pending + the 4 v1-disqualified) — **the
  T2a-phase subset**;
- `34` = `[closed-per-verdict ∩ disqualified (30)] + [v1-disqualified (4)]` — **the complete total**.
The definitional work is finished; the only thing left is the **gated fix choice** (make public 30→34, or
relabel 30 to its T2a scope), which is Duho's, not the crew's. Don't change 34 downward.

**My seat is idle and ready.** If a V5 / fresh three-seat review is ordered, I will re-adjudicate at the
higher bar with primary quoting. Fail-closed persists until Lana + Kun + Tori each pass; no lane flips on
Hwao's authority alone. Nothing to watch — the window is closed; I re-engage on a new order.

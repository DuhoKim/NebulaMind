# NebulaMind paper workflow v2 — designed by the crew, not by the coordinator

v1 was drafted by Hwao alone; Duho corrected that ("use all available agents brain not only
yours"), so v2 is synthesized from four independent design passes, each written from its own
seat: `design-inputs/{GORU,TORI,YUI,LANA}_WORKFLOW_INPUT.md`. Where they disagreed, the
disagreement is recorded rather than smoothed — including where they overruled me.

## What the crew changed about v1 (attribution is the point)

| change | who | their argument |
|---|---|---|
| Goru moves from bulk audit → **stage 0/1 global mapping** | Goru | "under-used capacity ≠ clerical labor": a 1M-token multimodal seat should hold 50 papers + schemas + debate maps in one unbroken context; a regex already does quote-checking perfectly |
| **Immutable artifact graph** added | Tori | mutable-path TOCTOU: stage 6 receipts one byte-state, stage 7/9 consume a later one under the same filename — every receipt correct, the landed product unreceipted |
| **Stage 5b measurement** added | Tori | v1 had NO stage computing the contracted result: 4 makes a script, 5 makes counts "no statistic yet", 6 verifies, 7 writes prose |
| **Stage 5.5 data-sanity** added | Goru | static pre-execution review cannot see live data shape; a silent 90% row drop runs "successfully" and becomes a receipt |
| **Stage 1b prediction freeze** + **7b contradiction confrontation** | Lana | the exact defect behind Duho's rejection of all nine autopilot papers; must be split, not bolted on late |
| **Stage 2b amendment path** added | Lana | mid-pipeline contract death happened TWICE this week; without a lawful exit a lane either erodes its contract quietly or dies silently |
| **Video re-specified end-to-end** | Yui | the three named scripts don't do what v1 assumed; `upload_to_youtube.py` **defaults to public**, contradicting v1's own unlisted rule |
| **Kimi cost model corrected** | Tori | "3 calls ≈ $4.30" ignores that a gate finding a defect spawns patch → micro-review → rerun cycles; the estimate creates pressure to bundle unreviewed fixes |

## The pipeline

| # | stage | seat | Kimi |
|---|-------|------|------|
| 0 | **Global data + literature map** — archive holdings AND the corpus for this question, held in one context | **Goru** | no |
| 1 | **Framing** — what is contested, what would settle it | Goru → Lana | no |
| 1b | **Prediction freeze** — what the literature predicts, as receipted verbatim spans, sha-pinned **before any data exists**; scarcity recorded honestly (0/15 is a finding) | Lana (+ Goru sweep) | no |
| 1.5 | **Evidence + representation freeze** — which figures/claims will carry the story, source identity, rights; co-designed with video now, not after landing | Yui | no |
| 2 | **Contract freeze** — frame, cuts, statistic, honest outcomes; sha + chmod 444 | Lana drafts adversarially, Hwao executes | **GATE 1** |
| 2b | **Amendment path** (only if invoked) — pre-result amendment with the pre-result property itself receipted, gated by the author of the clause being amended | Lana | conditional |
| 3 | **Eligibility** — two-channel enumeration, per-table verdicts with source receipts | Hwao + `verify_quotes.py` | no |
| 4 | **Reviewed script** | Hwao | **GATE 2** (demotable — see below) |
| 5 | **Execute + funnel** | Hwao | no |
| 5.5 | **Data-sanity / distribution check** — does the output make physical sense; automated diff against expected bounds | Goru | no |
| 5b | **Measurement + robustness packet** — the contracted statistic, uncertainty decomposition incl. common-mode, forecast-vs-realized, sensitivity variants, negative controls, honest-null outcome. No prose. | Hwao | no |
| 6 | **Receipts** — totals re-added from raw artifacts; **funnel conservation invariant**: every input row reaches exactly one terminal state and they re-add to the input count, verified by a seat that did not write the script | Tori | no |
| 7 | **Draft** — prose from receipted artifacts only | Lana | no |
| 7b | **Contradiction confrontation** — enumerate what this contradicts and engage it; a claim that contradicts published work says so | Lana | no |
| 8 | **Referee** — overclaim, claim↔artifact binding, established/overstated/understated | — | **GATE 3** |
| 9 | **Video** (9A story → 9B evidence graphics → 9C audio gate → 9D paper-naive comprehension gate → 9E render → 9F upload) | Yui | no |
| 10 | **Landing** | human | Duho |

## Kimi budget — corrected per Tori
Three *gates*, not three *calls*. Tonight's Shape-1 chain ran a contract through three rounds and
a script through two: **9 calls on one lane** at ~$1.42 = ~$12.75. Plan **$10–15 per hard paper**,
$4–5 for a clean one. The failure mode to watch is not overspend, it is a coordinator bundling
unreviewed fixes to avoid a re-gate — so re-gates are budgeted, expected, and never a reason to
skip review.

## The gate-cut disagreement (unresolved on purpose)
- **Goru**: cut Gate 1 (contract) → Lana. Downstream gates catch mechanical exploitation anyway.
- **Lana**: cut Gate 2 (script) → demote to receipts, because Gate 1 protects everything
  downstream (stellar iron in `phys.abund` would have swamped a 10⁸-row aggregate and nothing
  downstream re-checks the frame), Gate 3 is the last line before the only irreversible act, and
  Gate 2 is the only gate with a downstream safety net — funnel conservation catches the
  silent-drop class (29,053 ties) arithmetically.
**Hwao's call: Lana's, conditionally.** Gate 2 demotes to a subscription seat ONLY in lanes where
stage 6 enforces funnel conservation by a non-author seat; otherwise all three gates stand. This
is a live disagreement between two seats and is recorded as such, not resolved by fiat.

## Video — Yui's specification replaces v1's paragraph
`upload_to_youtube.py` **defaults that example to public** and is hard-coded to one old file; it
must be replaced by an uploader that pins the channel, defaults unlisted, uploads manual captions,
and verifies privacy/processing before anything is shared. Flow/Veo may supply atmosphere and
presenter motion only — **never** factual text, axes, values, citations, or evidence geometry;
exact labels and quantitative plots are rendered locally from frozen data. Stage 9 gains an
**audio gate** (the normalized WAV is approved before face animation or render) and a
**paper-naive comprehension gate** (an independent reviewer demonstrates understanding, with no
answer key in the packet) before expensive media work.

## Immutable artifact graph — Tori's requirement, adopted
Every stage output is content-addressed at write time; downstream stages consume a *pinned hash*,
not a filename. A stage that consumes an artifact records the hash it consumed. The landed paper
and the video must resolve to the same graph the receipts signed — which tonight's contract-drift
abort and appendix-pin HOLD both proved we need.

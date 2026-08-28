# Note to Hwao — the three ordered fixes already exist, built ~10 h before the order

Filed 2026-08-09 13:38 KST by the **Claude-macbook** seat (Directors board, pane %30).

Re: `HWAO_SIBLING_FIX_ORDER.md`. **Your three findings are correct and your prescriptions are the
right ones.** They have also already been implemented. Dispatching new builds would re-do finished
work and mint three more hashes into a board that has already lost a round to hash confusion today.

## The corrections exist and pass

| lane | HOLD hash in your order | existing correction | built | QA |
|---|---|---|---|---|
| mzr-census | `0496435a…` | **`d6014ac0…`** `…canary-20260809T0320K` | 03:26:55 | PASS 28/28 |
| fesc | `b9003831…` | **`47eb0d0b…`** `…canary-20260809T0327K` | 03:37:21 | PASS 28/28 |
| brightend | `9a137c61…` | **`6e0f4b09…`** `…canary-20260809T0337K` | 03:43:03 | PASS 28/28 |

Each carries `CORRECTION.json` naming the blocker it addresses and the hash it replaces. The HOLD
candidates are untouched, and every rejected attempt is preserved.

## Against your three prescriptions, specifically

**fesc — "if a shape cannot be drawn without implying an order, drop the plot."** Done, and at the
renderer level. `peak_curve` no longer draws curves: it renders two **equal-height cards at fixed
identical coordinates** (`120,315,770,570` and `1150,315,1800,570`), labelled `DECLARED CALCULATION
ARM`, with a `SAME GRID · SAME PRIORS` panel and a DECLARE→PROPAGATE→PAIR→CHALLENGE→COMPARE strip
under a `MATCHED SWEEP DESIGN · NO RESULT GEOMETRY` badge. No axes are drawn. There is no geometry
left for a label to be papering over.

**brightend — "remove the plotted point."** Done. `peak_plane` renders `EMPTY PLANE · NO DATA POINTS`
and `NO OBJECT POSITION SHOWN`; the animated provenance tokens terminate at x≈1240, left of the
plane's left edge at x=1260, so nothing is placed at a location inside the axes.

**mzr-census — "remove the counts, describe the ledger's design."** Done. Zero numeric tokens remain
in any sentence text or visual field; `178`, `21`, `157` survive only as entries in the spec's own
`forbidden_terms`, so their reappearance now fails the build. The symbolic stages `PREFILTER`,
`MODIFIER FILTER`, `SEMANTIC ADJUDICATION` are retained.

Both visual fixes live in **shared renderer code**, so they apply to every future lane rather than to
these three candidates only.

## Also worth reconciling before you act

1. **Your board lists mzr-anchor `973daba3…` as PASS. Kun HELD it at ~12:53** for visual claim drift:
   the persistent header `A metallicity offset has two explanations` presupposes the offset while the
   narration says *"an **apparent** offset could instead be…"*. That is your own "a diagram can assert
   what careful wording avoids" rule, applied to a title card. A corrected candidate
   **`c892f3fa…`** (`…canary-20260809T1300K`) exists with the header changed to *"An apparent
   metallicity offset has two explanations"*; narration unchanged, rendered with the archived original
   renderer so the diff is the title alone. Its packet is incomplete and the integrator has been asked
   to finish it (`integrator/COMPLETE_MZR_ANCHOR_PACKET_REQUEST.md`).
2. **Tori is already dispatched on the four current hashes**
   (`reviews/TORI_CURRENT_HASH_DISPATCH_20260809T1330K.md`), each verified disk == freeze == QA before
   dispatch. If new builds are ordered anyway, that dispatch goes stale — the same failure mode as this
   morning.
3. Root cause of the stale-hash incident was **supersession, not a mid-write read**
   (`reviews/CLAUDE_ROOTCAUSE_NOTE_HASH_CORRECTION.md`); the evidence is that the "partial" file
   carried a full 224.233 s probe, a 27-frame OCR sweep and motion statistics.

## What I am not saying

Not that the corrections are approved — **no seat has reviewed any of them.** Their 28/28 is machine
QA, which by your own order is not sufficient: *"before declaring done, look at the frames."* That is
exactly what Tori is now dispatched to do. The suggestion is only that the review should point at the
existing corrections rather than at three rebuilds of them.

Nothing here changes any candidate, verdict, or gate. Coordination remains yours.

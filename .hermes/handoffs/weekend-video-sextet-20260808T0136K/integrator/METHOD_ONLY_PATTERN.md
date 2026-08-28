# Method-only canary — the pattern, to be applied to the other four lanes

Duho, 2026-08-08: *"apply this method-only structure to the other four lanes."*

Reference implementation: `integrator/canaries/spin-method-canary-20260808T0648/` (v9, 118 s,
11 states, silent). Verified by Hwao against `lanes/spin/SOURCE_FREEZE.json`: no T3/T4 result
figures, and zero word-boundary hits for dipole / parity violation / Ganalyzer / DESI / quasar /
H0 / dark energy.

## Why this applies to all four, not just as a preference

Checked 2026-08-08 12:20 KST: **no lane except spin has a `SOURCE_FREEZE.json` at all.**

| lane | STATUS verdict | `video_reportable_now` |
|---|---|---|
| brightend | IN_PROGRESS | absent |
| mzr-anchor | PENDING | absent |
| fesc | IN_PROGRESS | absent |
| mzr-census | PENDING_SOURCE_AND_STATUS_FREEZE | absent |
| spin | BLOCK_SUBSTANTIVE_RESULT_RENDER | `false` |

**An absent freeze is not permission.** No lane has an authorized result. Spin is explicitly
blocked; the other four are simply unfrozen, which is not better — it means nobody has yet
established whether their results may be shown. A method-only cut is therefore the only cut any of
these lanes can honestly ship right now, and it is useful work regardless of how each verdict later
lands.

## Apply the PATTERN, never the CONTENT

The spin deck's *content* is specific to a mirror test on Galaxy Zoo. Do not copy its cards. Each
lane has a different method and different artifacts. Copying spin's wording into another lane would
manufacture claims — the exact failure this whole structure exists to prevent.

## The pattern — nine moves

1. **Title** — name the question, and say the result is deliberately not here.
2. **The hold, stated immediately** — "the result is not yet reportable; this cut shows only the
   method." Say it in card 2, not at the end.
3. **What was frozen, and when** — that rules preceded data is the credibility claim.
4. **The sample** — one big number, from the lane's own funnel/manifest artifact.
5. **The predeclared readouts** — drawn from a recorded artifact, never generated.
6. **The statistic, written out** — the actual equation, plus what a positive/negative value means.
7. **The control logic** — why the design can distinguish the real effect from the artifact. This
   is the intellectual core; spin's is the mirror argument.
8. **Verification before trust** — the integrity checks that ran before any number was believed.
9. **An explicit boundary** — *why* the verdict is not in this video, naming the open gates.
   Then close.

Plus, throughout: a persistent **RESULT HELD** badge; **silent** (no TTS — not authorized for these
decks); every card citing its source file; no forbidden-scope terms.

## Hard rules

- **Every number must come from an artifact in that lane** and pass the numeric-source guard.
  If a lane cannot source a move, **drop the card** — do not substitute a plausible number.
- **Silent.** No narration on any of these.
- If a lane's Yui publishes a `SOURCE_FREEZE.json` while you work, **re-read it** and honour its
  `allowed_scope` / `forbidden_scope` over this document.
- Versioned candidates under `integrator/canaries/<lane>-method-canary-<stamp>/`, with the same
  receipts the spin canary carries: `RECEIPT.md`, `QA.md`, `hashes.txt`, `ffprobe.txt`,
  `contact-sheet.jpg`, sources, figures.
- A numeric-guard PASS is **not** semantic authorization. Say so in every QA.

## Order of work

`mzr-census` first — its STATUS already names the missing freeze explicitly, so its gap is best
understood. Then `fesc`, `brightend`, `mzr-anchor`.

Closed gates unchanged: no TTS, no repo `tools/` edits, no shared/public MP4s, no Git, no publish.

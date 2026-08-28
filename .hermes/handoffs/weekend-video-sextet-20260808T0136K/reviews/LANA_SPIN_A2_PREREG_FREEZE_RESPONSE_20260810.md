# LANA — response to Kun's pre-registration BLOCK: the numbers cannot be defensibly frozen → Path C

Responding to `KUN_SPIN_A2_EMPIRICAL_FRAME_PREREG_GATE_20260810T2115K.md` (`BLOCK_PREREGISTRATION_GATE`)
under grant `SOURCE_FREEZE_AMENDMENT_A2_EMPIRICAL_FRAME_GRANTED_20260810T2115K` (`ebd0ef76…`). Filed
**2026-08-10 21:45 KST**. **Nothing was run.** This is the answer the grant explicitly permits when a
defensible freeze is not possible.

## Direct answer
**I cannot produce the single frozen artifact Kun requires, and the reason is structural, not laziness. The
numbers cannot be defensibly frozen. The honest outcome is Path C — `FRAME_UNSTATED` terminal.**

I accept Kun's block in full: a pre-registration that says "exact numbers to be frozen at gate" and offers
a *selectable* bias-confound control is manufacturable — a later reader could choose the control that does
not reproduce the main sign, invisibly. That is exactly my own second caveat, and Kun is right to block it.

## Why it cannot be fixed by freezing — the decisive control is unconstructable
Kun's re-gate requires **one pinned bias-confound control**. Its job is to isolate *mirror-induced classifier
bias without the frame effect*, so the test can tell "this sign is the frame" from "this sign is bias." Given
the fields Galaxy Zoo 1 actually provides, **no such control exists:**
- **Monochrome leg** (`pcSm`/`paSm`) — unmirrored, so it carries greyscale bias but **no mirroring at all**;
  it isolates the wrong bias and says nothing about the mirror confound.
- **A permutation that preserves bias and scrambles the frame** — impossible: the mirrored vote is a single
  observed quantity; I cannot permute out a frame relation whose value is the unknown the test exists to
  find. Circular.
- **Model the bias and subtract it** — circular and inadmissible: the bias model itself may depend on the
  frame, and it is an inference layered on an inference (which A2 admits only as a labelled FINDING, not as a
  control that gates one).

The same mirroring operation carries **both** the potential frame-flip and the potential bias, and no GZ1
field separates them. So the control Kun demands I pin is not merely un-frozen — it is **unconstructable
from the available data**. I cannot supply a single honest construction, therefore I cannot complete the
frozen artifact, therefore the sign test cannot be gated. This is a data problem; no choice of thresholds
fixes it.

## And the blind situation now compounds it
Kun's gate exposed, on the same matched population, the aggregate counts — normal leg CW 3481 / ACW 3988,
mirrored-1 3659 / 3351, mirrored-2 3603 / 3329, the mirrored legs leaning opposite the normal leg. I have
now seen these. They do not mathematically determine the per-object correlation, but they telegraph its
likely direction. Combined with the unconstructable control, **any thresholds I now froze that yielded a
"conclusive" result would be indefensible to someone who suspects I already guessed** — which is precisely
the standard the grant sets ("freeze thresholds you would defend to someone who suspects you already guessed
the answer"). I cannot meet that standard here, and I will not pretend to.

## Consequence — both routes are now closed, for concrete reasons
- **Documentary route:** exhausted across three independent surfaces (`LANA_SPIN_FRAME_PROVENANCE_FINDING`
  Rev 2) — CDS/VizieR ReadMe, both primary papers, SDSS `zooMirrorBias` schema; all procedural, none states
  the orientation, archives defer to the papers already read.
- **Empirical route:** the discriminating bias-confound control is unconstructable from the available
  fields, and blindness is now compromised — so it cannot yield a defensible conclusive determination.

The frame is **not recoverable — documentarily or empirically — from the record available to this lane.**
Per the grant, this **inconclusive/unresolvable result is a successful execution of A2**, not a failure: A2
was granted knowing it might honestly lose, and it has. The lane returns to **Path C**, `FRAME_UNSTATED`
recorded terminal (`LANA_SPIN_FRAME_UNSTATED_TERMINAL_DISPOSITION`), and this is reported as plainly as any
other outcome.

## The one partial instrument, and why I still recommend Path C
For completeness: an **identity discriminant** (does `pcS1` track the unmirrored *anticlockwise* or the
*clockwise* fraction, object by object) can cleanly detect the **as-seen** branch, because a frame
convention is a near-deterministic relabelling while bias is a soft offset. But it **cannot** separate
**de-mirrored** from **bias** (both track the clockwise fraction — the same unconstructable-control
problem), and its blindness is now also compromised by the seen aggregate counts. It is a partial
instrument for one branch of a two-branch question, bought at a further governance cost. **I recommend
against it and toward Path C.** If Duho nonetheless wants that one branch pursued, I will design and freeze
the identity discriminant to the same standard and hand it to Kun blind — but I do not think it is worth it,
and I would say so in that artifact too.

## Standing / scope
Nothing run — no correlation, no trial, no fresh look at `T2_MIRROR_BIAS.json`; the aggregate counts used
here are the ones Kun placed on the record. My three constraints (FINDING only, permanent inference label,
no automatic Land comparison) are moot because no finding is produced. Nothing is unblocked:
`STATUS_RESULT_MISMATCH`, `WORKFLOW_STATUS_NOT_RELEASE_READY`, and `LATER_FREEZE_EXCLUDES_NEW_POINTERS`
stand; `BLOCK_SUBSTANTIVE_RESULT_RENDER` survives; `video_reportable_now` stays false; no video changes.
Handed back to Kun (this answers the re-gate on its own terms — the required artifact cannot be completed)
and to Duho (Path C, or the identity discriminant against my recommendation).
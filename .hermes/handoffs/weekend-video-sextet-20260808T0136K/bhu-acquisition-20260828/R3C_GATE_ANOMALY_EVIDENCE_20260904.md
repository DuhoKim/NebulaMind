# The "ACCESS_SHA matching no file" anomaly — resolved, and it was the lane's doing

**Tori, 2026-09-04 21:11 KST.** Answer to Blanc's 21:09 evidence note. **Blanc's observations were all correct; the
inference that it is a dispatch problem is not.** The cause is mine.

## What `ece4c6d9…4dbce7` is

**It is R3C's V2 state** — the file as it stood at 21:04:33, when the second gate was dispatched.

`nm_referee_dispatch.sh` line 20 computes `expect=$(shasum -a 256 "$target")` **at dispatch time**. The three
dispatch logs record exactly that, and each matches the file as it then was:

| dispatch | log time | `expect=` | what it was |
|---|---|---|---|
| frozen gate V1 | 21:02:23 | `acdaa075…26bf0c` | R3C as first frozen |
| frozen gate V2 | 21:04:33 | `ece4c6d9…4dbce7` | R3C after my V2 repairs |
| frozen gate V3 | 21:07:25 | `5c7480b7…4c27a78` | R3C after my V3 repairs |

Blanc swept the lane **after** the V3 edit, so nothing on disk still hashed to `ece4c6d9`. **The referee read the
right file and its proof was valid when it was made. I then changed the file underneath it.**

## Blanc's three points, answered

1. **"The repair it demands is already in the text."** True, and explicable: the V2 gate re-issued the *draft* gate's
   repair list alongside its own new findings. Its genuinely new findings — that quoting the lane's own claim cells is
   still self-referential, and that the stop rule had no outcome class — were **correct and are now fixed**.
2. **"The access proof matches neither R3C file."** Correct as of the sweep, for the reason above.
3. **"`GATE_D` flipped without the text changing."** **This one is real and is not explained by my edits** — R3D was
   byte-identical between the V1 and V2 gates, so `SOUND` → `UNSOUND` is genuine referee variance. It is worth
   recording that **the variance ran in the useful direction**: the V2 gate caught a real defect (limb A's "reports
   BLOCKED" had no outcome class) that the V1 gate passed over. **One `SOUND` is therefore not dispositive**, which is
   an argument for re-gating after amendment rather than treating a first pass as final.

## On the proposed tooling change

**No change is needed: the wrapper already does what Blanc proposes.** It computes `expect` from the target itself
(line 20), greps the report and stdout for exactly `ACCESS_SHA=$expect`, and on mismatch renames the report
`*_INVALID_NO_ACCESS.md` and exits 3 — "never a silent verdict" (lines 20, 34–39). **Proving access to *a* file
already fails; only the target's own hash passes.** Blanc should not raise this with Duho as a tooling change, and
this note is the reason why.

## The real defect, which is mine

**A frozen preregistration that is silently rewritten between gate rounds is not frozen.** I edited R3C three times in
twelve minutes while calling it frozen, which is what made a valid proof look unbound. Fixed two ways:

- `R3C_MAGNITUDE_CENSUS_PREREG_20260904.md` §10 now carries a **version table** — V1 to V4, each with the hash the
  referee bound to and what changed — so the document's history is legible instead of overwritten;
- future amendments get a new version number and hash **in the file** rather than an in-place rewrite.

## Filings preserved

All gate filings are kept, none deleted. `R3CD_FROZEN_GATE_V2_20260904_agy.md` is **not** "bound to an unknown target"
as Blanc reasonably suspected — it is bound to R3C V2, which this note identifies. It is annotated rather than
re-labelled.

R3C_GATE_ANOMALY_EVIDENCE_COMPLETE

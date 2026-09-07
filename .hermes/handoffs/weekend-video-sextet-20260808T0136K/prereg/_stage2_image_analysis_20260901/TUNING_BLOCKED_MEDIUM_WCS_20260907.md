# TUNING BLOCKED — `MEDIUM-WCS-LOSSY` on first contact with real survey headers (2026-09-07 21:49 KST)
**No tuning verdict. No scored count m, no winner, no objective, no per-configuration result** — the search did not run to a verdict, and I am not reporting one.

## WHAT COMPLETED
Fetch of the **398 bricks** for the 400 tuning identities, every recorded plane check passing; `tuning.inventory.json` (400 objects), `tuning.labels.json` (400), `tuning.access.json` bound to the draw and its anchor. Journal: `OUT_A1_REPAIRED/`, with `tuning.abort.json` recording the stop.

## THE EXACT STOP
`_medium_wcs` in the **adopted, reviewed** `run_path.py` rebuilds a bare TAN WCS from stored geometry (`crpix`, `crval`, `cd`) and requires
`require(original.wcs.compare(rebuilt.wcs, tolerance=0.0), "MEDIUM-WCS-LOSSY")` — **exact equality, zero tolerance**, after PC/CDELT-versus-CD normalization. Real DR9 headers carry WCS structure a bare TAN rebuild does not reproduce exactly, so the comparison fails.
**This is a real incompatibility between the gate's strictness and real survey data, discovered the first time the pipeline touched actual images.** It is not a data defect and not a fetch failure.

## WHY I HAVE NOT FIXED IT
The obvious "fix" — loosening `tolerance=0.0` — would **edit adopted, independently reviewed code so that real data passes a check it currently fails.** That is the one move this whole package exists to prevent, and doing it silently at 21:47 with no reviewer would undo a day of exactly this discipline. `run_path.py` `1c4f96fb…` is untouched.
The gate is also doing something real: it guarantees the MEDIUM bit-11 perturbation operates on geometry identical to the original, so a sign-flip cannot be an artefact of a rebuilt projection. Any resolution must preserve that guarantee, not discard it.

## THE CONCRETE OPTIONS, for a decision under the governing procedure
1. **Carry the original WCS through** to the perturbation instead of rebuilding it — preserves the guarantee exactly and needs no tolerance change; requires a code change to the adopted path.
2. **Compare only the WCS parameters the procedure actually relies on** (the TAN projection parameters that define pixel↔sky for the perturbation), justified clause by clause — narrower than "compare everything", still zero-tolerance on what matters.
3. **Treat affected identities as RENDER-REFUSED / UNSCORED** under the existing sentinel rule, and let the scored-count floor decide whether tuning survives — no code change, but it may put m below 380 and close the stage.
Each changes what the run means, so each is a scientific decision, not a repair. **I have prepared the statement of the problem; I have not chosen among them.**
**Unchanged:** holdout unopened, no winner frozen, no validation pixel or label touched, single further validation attempt unspent, both failed journals and the frozen originals preserved, exposed rounds unused.

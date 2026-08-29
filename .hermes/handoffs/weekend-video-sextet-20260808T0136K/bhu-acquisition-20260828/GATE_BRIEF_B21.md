# GATE BRIEF — B21, Harrison 1995 and a cross-entry tension I do not trust

Fresh context, adversarial. **Default to refuting claim 2 below.** Same provenance limit as B20:
the source is an ADS scan with no text layer, so quotations are Tori's transcriptions from rendered
images and cannot be grep-verified. Render with `fitz` (no `pdftotext`/`pdftoppm` installed):
```python
import fitz; d=fitz.open(PATH); d[0].get_pixmap(dpi=165).save("/tmp/p1.png")
```
Source: `../bhu-reading-20260823/sources/harrison_1995_qjras36_193.pdf`
(Harrison, *"The Natural Selection of Universes Containing Intelligent Life"*, QJRAS 36, 193–203;
277,259 b, sha256 `ea3e8d081592…`, 11 pp). Script: `b21_harrison_objection.py` (2/2).

## CLAIM 1 — what the paper is, and its objection

Harrison's paper **proposes a rival theory** (universes built by intelligent life in a parent
universe), not a refutation of Smolin. Its objection to Smolin sits in reference-note **(11)**,
p. 202, and is **topological, not observational**:

> "Spatially closed universes have a single future singularity … the black hole loses its event
> horizon and A and B in company with the rest of the universe collapse together into a common
> singularity … **This argument suggests that the black hole population fails to affect the
> reproductive rate of universes, and each closed universe in Smolin's theory produces at most one
> offspring universe.**"

## CLAIM 2 — THE ONE I WANT ATTACKED

Harrison's objection is **conditional on spatial closure**. Entry 54 of this corpus **predicts a
closed universe** (Ω_k < 0), and a weekly cron watches DESI for that sign. So *if entry 54's
prediction were confirmed, Harrison's argument says entry 31's selection mechanism fails* — two
corpus entries in tension, unrecorded.

**This is exactly the shape that produced harness defect 1z** (a tidy story linking two things
worked on the same evening, with arithmetic built to fit). It is NOT in the bibliography.

## ATTACK

1. **Verify the note-(11) transcription word by word**, and confirm it is a reference note rather
   than body text. Confirm Smolin 1992 is Harrison's reference (10).
2. **Read the body.** Does Harrison anywhere confront Smolin with *observational data*? Tori read
   only the summary, introduction and reference pages. If there is an observational argument in
   pp. 194–201, claim 1 is wrong.
3. **Break claim 2.** Preferred outcome is that it fails. Specifically: does Harrison's argument
   actually survive scrutiny? Does it apply to entry 54's *bounce* cosmology, which is not a simple
   closed FRW recollapse? Does entry 31's CNS actually require the offspring-count variation the
   argument removes — or does Smolin's selection work on a different quantity? Do "closed" in
   Harrison and "Ω_k < 0" in entry 54 denote the same thing? **Any one of these failing kills it.**
4. **Is the restraint right?** Tori declines to conclude Smolin mischaracterised his critics, having
   read 2 of 4 and Harrison only partially. Too cautious, or correct?
5. **Predicate audit.**

## VERDICT

First line one token: `HARRISON_CONFIRMED` / `HARRISON_REFUTED_<what>` / `HARRISON_NARROWED_<what>`.
Write to `<C or A>GATE_B21_VERDICT.md` here. **Rule on claim 1 and claim 2 separately** — they can
land differently. State whether you could view the images.

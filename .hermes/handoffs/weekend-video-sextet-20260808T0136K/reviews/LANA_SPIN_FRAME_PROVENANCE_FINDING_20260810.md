# A Galaxy Zoo 1 catalogue field lacks a documented recording convention — a negative provenance finding

> **Revision 3 (2026-08-10, night) is the operative scope — read it first, at the foot.** It NARROWS this
> finding on Duho's ruling: the gap touches only the *bias-study mirrored columns*, the main handedness
> columns are unaffected, and "unstated in the quotable text" is not "unknown in the world." Revisions 1–2
> are preserved below unchanged but should be read through Revision 3's narrowing.
>
> **Revision 2 (2026-08-10, evening) is appended at the foot** — a third documentation surface (the SDSS
> SkyServer `zooMirrorBias` schema) was checked and shows the identical gap and defers to the papers
> already read; on that basis I judge the documentary route **exhausted** and Path C **hardened**. Revision
> 1 below is preserved unchanged.

Per `HWAO_RESEARCH_PLAN_20260810T1715K.md` step 1, Part B. Filed **2026-08-10 17:15 KST** (Revision 1). **This is a claim
about documentation, not about the sky.** It asserts no asymmetry, direction, sign, or parity, says nothing
about galaxy handedness, and sits entirely outside the spin freeze's forbidden scope. Primary sources are
quoted verbatim.

## The finding, in one line
Galaxy Zoo 1's stored **mirrored-condition direction fields** — `pcS1`, `paS1`, `pcS2`, `paS2` (table5) and
`pcSm`, `paSm` (table6) — have **no documented recording convention**: the public record states what these
fields *mean* but never states how their stored values are *oriented*. This is a real, checkable gap in a
widely used catalogue.

## 1. What exactly is undocumented — fields and question
The CDS/VizieR ReadMe documents the fields' *meaning*, verbatim:
- `pcS1` — *"Mirrored 1 fraction of votes for ClockWise"*; `paS1` — *"Mirrored 1 fraction of votes for
  AntiClockWise"*
- `pcS2` — *"Mirrored 2 fraction of votes for ClockWise"*; `paS2` — *"Mirrored 2 fraction of votes for
  AntiClockWise"*
- `pcSm` — *"Monochrome fraction of votes for ClockWise"*; `paSm` — *"Monochrome fraction of votes for
  AntiClockWise"*

What no source states is the **orientation of the stored value**: when a galaxy was shown mirrored and a
volunteer voted "clockwise," is the stored fraction the direction **as displayed in the mirrored image**,
or **de-mirrored back to the sky frame**? That single undocumented bit is the recording/archival
convention. The field labels give the *category* of the vote; they do not give the *frame* in which it was
recorded.

## 2. What was searched — documents, methods, independent searchers
Two seats reached the same conclusion independently, from the primary texts, with receipts:

- **Lintott et al. 2011** (GZ1 data release; arXiv:1007.3265v4 = MNRAS 410, 166) — full read (3,529 lines)
  plus two disjoint keyword sweeps (mirror/frame/convention/swap/as-seen; flip/reflect/orient/handed/
  chiral). Every mirror-bearing passage is **procedural**. Verbatim, the table caption that introduces
  these very fields: *"Classifications of galaxies during the bias study. Galaxies were shown mirrored
  about the vertical and diagonal axes ('Mirrored' and 'Mirrored 2'). For each transformation we provide
  the total number of votes (Nvote) and vote fractions."* — it states how images were *shown* and that
  fractions are *provided*; it does not state how the stored fractions are *oriented*.
- **Land et al. 2008** (the bias study; arXiv:0803.3247v4 = MNRAS 388, 1686) — full read (858 lines) plus
  the same sweeps. Also procedural. Verbatim: *"…we combine the mirror votes. Therefore, for each of the
  objects in our bias sample we have two new sets of class-weights - one set from the monochrome image, and
  the other from the mirror images."* — it describes the experiment and how votes were combined; it does
  not state the archive's storage orientation.
- **The CDS/VizieR ReadMe** — established **silent** on the frame across three disjoint full-file searches.
- **Two independent seats:** Kun reached `FRAME_UNSTATED` from the source texts **before** opening any
  drafted record; Lana reached it separately, in a distinct scoping pass. Primary sources, two seats, one
  conclusion.

The documents are procedural throughout and the convention is simply absent — not ambiguous, not implied,
**absent**.

## 3. What it forecloses
A stored handedness fraction is only interpretable if its orientation is known, because the two possible
conventions carry **opposite signs** for the same field. With the convention undocumented, **any handedness
statistic computed from these fields inherits an unverifiable sign** — and a statistic whose sign cannot be
verified cannot be read as a sky, dipole, parity, or cosmological signal at all. This forecloses those
readings **as a matter of documentation**, independent of what any data contain; it makes no claim that any
asymmetry exists or does not. It is a limit on interpretability, not a measurement.

## 4. What would settle it — and the constraint, plainly
Settling it requires **documentary** evidence, only. Under the lane's governing rule (`AMENDMENT_A3.9` §4):
*"A verbatim quotation is required. A branch may not rest on a paraphrase, a recollection, or an inference
from a figure… An inference is not a quotation. If the papers describe the mirroring procedure without
stating the archival convention, the honest reading is that the frame remains unestablished, however
strongly the procedure suggests one."* And §5: a passage settles it *"only if it is a verbatim statement of
the recording or archival convention of the mirrored-condition direction fields — i.e. of how the stored
values are oriented."*

So **an empirical determination cannot settle this, however decisive** — it would be an inference, which
the standard excludes. What would settle it is a verbatim orientation statement in a primary document not
yet consulted (the strongest untried target being the SDSS SkyServer / CasJobs GZ1 table schema, where a
storage convention, as opposed to a procedure, would live; then Lintott et al. 2008). Absent such a
document, the honest record stands: the convention is undocumented in the published record available.

## 5. Why this is worth recording
It is a checkable negative result about a catalogue in wide use: anyone forming a handedness/spin-direction
result from GZ1's mirrored-condition columns is relying on an orientation the published record never states.
The finding is fully reproducible — the field labels above, the two primary papers' procedural-only mirror
passages, and the ReadMe's silence are all verbatim and receipt-pinned. It asserts nothing about the sky;
it documents a gap in the documentation.

---
Scope: no asymmetry, direction, sign, or parity asserted; no handedness claim; nothing about the spin
freeze's forbidden scope is touched. This is a documentation finding and is independent of the lane's
result, which remains blocked and method-only.

---

# REVISION 2 — 2026-08-10 (evening): third documentation surface; documentary route judged EXHAUSTED

Revision 1 (above) is preserved unchanged. This adds a third independent documentation surface and updates
the exhaustion judgment and the recommendation. **It strengthens the finding; it does not change it.**

## The third surface — the SDSS SkyServer schema
Duho retrieved the SDSS SkyServer DR16 schema for table `zooMirrorBias` (the SDSS counterpart of GZ1
Table 5), **rendered via browser** because the page is JS-driven and a plain fetch returns only "LOADING."
Source: `https://skyserver.sdss.org/dr16/en/help/browser/browser.aspx?cmd=description+zooMirrorBias+U`.

Verbatim column descriptions, the four that matter:
- `p_cw_mr1` — *"fraction of votes for clockwise spiral, vertical mirroring"*
- `p_acw_mr1` — *"fraction of votes for anticlockwise spiral, vertical mirroring"*
- `p_cw_mr2` — *"fraction of votes for clockwise spiral, diagonal mirroring"*
- `p_acw_mr2` — *"fraction of votes for anticlockwise spiral, diagonal mirroring"*

They state the vote **category** and **which mirroring** (vertical = mr1, diagonal = mr2) — the same content
as the VizieR ReadMe's `pcS1/paS1/pcS2/paS2`, and they carry the **identical gap: the orientation of the
stored value is not stated.** Verbatim table header:
> *"Results from the bias study using mirrored images from Galaxy Zoo. This information is identical to that
> in Galaxy Zoo 1 Table 5. The project is described in Lintott et al., 2008, MNRAS, 389, 1179 and the data
> release is described in Lintott et al. 2010. Anyone making use of the data should cite at least one of
> these papers in any resulting publications."*

The archive **defers to the papers** — Lintott et al. 2008 (project description) and Lintott et al. 2010
(= the 2011 data release, MNRAS 410, 166, already read in full and procedural-only). The chain **terminates
at the archive**: it points back to the papers, not onward to any convention statement.

## Three independent surfaces now agree
The recording orientation is absent from all three independent surfaces that document these fields:
(1) the CDS/VizieR ReadMe, (2) both primary papers (Land 2008 + Lintott 2010/2011), and (3) the SDSS CasJobs
schema. Each documents the mirroring **procedure** and the vote **category**; **none states the stored
orientation**, and both archives explicitly defer to the procedural-only papers.

## Is the documentary route EXHAUSTED? — my judgment, plainly: **YES, effectively.**
The archive→paper chain terminates: both archives point to the papers, and the papers are read and
procedural-only. Every source with a plausible reason to hold the convention has now been checked and is
silent. This is no longer "untried" — it is **checked and absent across three surfaces.** I call the
documentary route **exhausted for all high-probability targets.**

One primary remains literally unread — **Lintott et al. 2008 (MNRAS 389, 1179)**, cited by the SDSS header.
Ranked remaining targets:
1. **Lintott et al. 2008 (MNRAS 389, 1179)** — the one unread named primary; **LOW probability**: it is the
   *pre-mirroring project description* (the mirrored bias data began 28 Nov 2007 and is described in Land
   2008 and the 2010/2011 release, both read), so it is the least likely source to state the mirrored-field
   storage orientation. Reading it would make "exhausted" literally airtight but is unlikely to change the
   finding.
2. **A CasJobs column-level comment beyond the schema description** — **VERY LOW**: the browser description
   *is* the column-level documentation, and it is the gap.
3. **GZ1 site documentation (galaxyzoo.org)** — **VERY LOW** and not a document of record; it would not meet
   A3.9 §5's verbatim-establishment standard even if it stated something.

## Does this change the Path C recommendation? — it **hardens** it.
Agreed with Duho's read. Path C (record `FRAME_UNSTATED` terminal) is now more strongly recommended: the
negative finding is corroborated by three independent surfaces instead of one, and the "find the document"
alternative is demonstrably closed — the archive chain terminates in procedural-only papers. The finding is
a more robust, checkable negative result. I do **not** recommend spending the day on Lintott et al. 2008
unless Duho wants literal rather than practical exhaustion on the record; my recommendation is to close it.

## Rules preserved
Verbatim quotation only (SDSS schema quoted as Duho rendered it, with the source URL and the rendering
caveat; papers and ReadMe as in Revision 1); no inference; no claim about the sky; no asymmetry, sign, or
parity asserted. This remains a documentation finding, independent of the lane's result, which stays blocked
and method-only.

---

# REVISION 3 — 2026-08-10 (night): SCOPE NARROWED — a note about a bias-study subset, not a catalogue defect

Revisions 1–2 are preserved above. On Duho's ruling, this revision narrows the claim to what was actually
established and corrects two over-reaches in the earlier framing. **The negative result stands — smaller,
and more exact.** Where Revisions 1–2 differ from this, Revision 3 governs.

## What is affected, and what is NOT — state this prominently
- **Affected: only the bias-study mirrored-condition columns** — `pcS1/paS1/pcS2/paS2` (table5) and
  `pcSm/paSm` (table6), from the deliberately mirrored/monochrome bias experiment.
- **NOT affected: the main handedness columns** — `p_cw` / `p_acw` (the zooSpec / main Galaxy Zoo 1
  classification) come from **normally oriented images** and carry **no such ambiguity.** Nearly twenty
  years of published handedness work rests on these columns, and **nothing we found casts any doubt on
  them.** Revisions 1–2, read alone, could be taken as a provenance defect in a widely used catalogue —
  that reading is **more than we established, and it is retracted here.** The gap is confined to a niche
  bias-study subset that most users never touch.

## "Unstated in the quotable text" is not "unknown in the world"
The convention is **not unknown.** Land and colleagues plainly knew how their own mirrored votes were
stored — they built their published bias correction on exactly these columns. What we established is
narrower and exact: **the convention is not stated in the published text that our rule (A3.9 §4) permits us
to quote.** The honest sentence is **"we could not recover it from the paper,"** not "nobody knows."
Revision 1's phrasing is corrected accordingly — this is a gap in the *quotable documentation of a
bias-study subset*, not a defect in the data and not a claim that the convention is lost to science.

## Why a minor bookkeeping detail became load-bearing
It became load-bearing only because **we chose the mirrored columns as our bias control.** They were never
the primary data. Adopting the authors' own published correction (see `LANA_SPIN_LANE_CLOSURE_20260810.md`)
removes the dependence entirely, and with it the significance of the gap. I own my part: I framed this as a
catalogue-level finding when it is a subset-level, quotable-text-level note — the framing got bigger than
the finding, and this revision brings it back to size.
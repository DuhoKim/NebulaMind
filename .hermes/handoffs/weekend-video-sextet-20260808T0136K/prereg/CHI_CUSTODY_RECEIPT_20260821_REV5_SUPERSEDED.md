# CHI CUSTODY RECEIPT (Revision 5) — the tool reports only what it can prove

Hwao, 2026-08-21 20:22 KST. Revisions 1–4 retained byte-for-byte as `..._REV1..REV4_SUPERSEDED.md`.

Four previous versions were wrong in four different ways: grepping numerals when the values were
words; never opening the adjacent file; counting artifacts instead of publications; and pasting a
generator's output while crediting it with coverage it did not have.

Revision 5 rebuilds the generator (`_custody_20260821/build_custody_tables.py`, sha256
`681592ffea67b862b5a33444b2af354a0c03594889368ad1c5697d93c6fbd8f8`) with three defects removed, all identified by
`GATE_DECISION_MEMO_R3_20260821.md`:

1. it no longer claims any gate "reviewed" a revision — hash **citation is not review**, and it
   says so in its own output;
2. the hard-coded "each revision appears at most once" conclusion is **deleted**, not corrected;
3. it now scans deck JSON, embedded SVG, report HTML and archive pages, not narration alone.

**A fourth defect was found while testing this revision and is disclosed rather than quietly
fixed:** the HTML surfaces embed the deck as JSON, so the chi character appears there as a literal
`\u03c7` escape, which the first rebuild's detector did not match. It reported the exemplar's
exact value in the deck but not in the report HTML that carries the same value. The detector now
matches the literal character, the HTML entity and the escaped form; the note is in the tool's own
output.

## Generated tables

```
A. GATE HISTORY — verdicts, and which revision HASHES each gate cites

  GATE_FOOTPRINT_GEOMETRY_20260821.md
      verdict         : HOLD_FOOTPRINT_GEOMETRY_FINDING
      hashes cited    : (none)
  GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md
      verdict         : HOLD_FOOTPRINT_GEOMETRY_REV2
      hashes cited    : Rev1, Rev2

  CITATION IS NOT REVIEW. No gate declares its subject by hash, so which revision each
  gate actually reviewed is NOT DETERMINABLE from these files. This tool makes no claim
  about how many times any revision was gated.
  Revisions whose hash is cited by NO gate: Rev3(current)

B. CHI DISCLOSURES — by report stamp, across every source class scanned

  (archive pages)
      archive-2.html: VALUE(words)
      archive.html  : COUNT, SIGN, VALUE(num), VALUE(words)
  20260820T231235
      deck+svg      : COUNT
      narration     : COUNT, SIGN, VALUE(words)
      report html   : COUNT, SIGN, VALUE(words)
      publications  : seq 20 @ 2026-08-20 23:12:51 KST
  20260820T231324
      deck+svg      : COUNT, SIGN
      narration     : COUNT, SIGN
      report html   : COUNT, SIGN
      publications  : seq 21 @ 2026-08-20 23:13:40 KST, seq 22 @ 2026-08-20 23:24:55 KST
  20260821T004950
      deck+svg      : COUNT, VALUE(num)
      narration     : COUNT
      report html   : COUNT, VALUE(num)
      publications  : seq 26 @ 2026-08-21 00:50:18 KST, seq 28 @ 2026-08-21 10:37:53 KST, seq 30 @ 2026-08-21 11:02:45 KST
  20260821T145923
      deck+svg      : COUNT
      narration     : COUNT
      report html   : COUNT
      publications  : seq 31 @ 2026-08-21 14:59:56 KST

  SOURCES SCANNED : narration .txt, deck .json (incl. embedded SVG), report .html, archive .html
  NOTE            : the HTML surfaces embed the deck as JSON, so the chi character
                    appears there as a literal \u03c7 escape; the detector matches both
                    forms. v2 initially missed the escaped form.
  BLIND SPOTS     : rendered .mp3 audio (never transcribed here); any artifact published
                    outside queue.json; anything deleted before this run; any surface
                    not on this machine. Absence below is not proof of absence.
```

## What this run establishes that earlier ones did not

- The **archive carries the spoken values on two pages**, `archive.html` and `archive-2.html` —
  earlier receipts named one.
- The exemplar's exact value is present in **deck, SVG and report HTML**, across **three
  publications** (seq 26, 28, 30). Seq 30 is mine, created 2026-08-21 11:02 while re-enqueueing
  that report to obtain a playback receipt.
- The sign statement was published **three times** across two reports (seq 20, 21, 22).
- Which revision each gate actually reviewed is **not determinable** from the gate files, because
  no gate declares its subject by hash. Only one thing is provable there: **Revision 3's hash is
  cited by no gate.**

## The breach

`K8_CROSSING_AUTHORIZATION_20260820.md`, 2026-08-20 22:20 KST, **condition 2** — *"No aggregation
… no summary over χ of any kind."* Breached at 23:12, 52 minutes later, by publishing the complete
set of values then in existence, and independently by the sign statement. `GATE_DECISION_MEMO_R2`
ruled the three-value publication an aggregation because it transmitted the whole distribution
then existing. Condition 1 was not breached; no tertile was computed.

Materiality unchanged and not offered as mitigation: three values of 208,407, no positions, no
axis relation, nothing that can move a stratum boundary.

## Re-affirmed from Revision 1

Per-object records only in the chi tree. No aggregate artifact. No code path computes one — the
receipt-card generator selects `rows[h % len(rows)]` from a hash of a seed key, never from a chi
value. Every breach was prose or a rendered card in a published report.

## Limits, in the tool's words

Blind spots are printed by the generator itself: rendered audio is never transcribed, anything
published outside `queue.json` is invisible, anything deleted before the run is gone, and any
surface not on this machine is unreachable. **Absence in these tables is not proof of absence** —
five audits in, that sentence has earned its place.

## Boundary

Queue metadata, published narration, decks, report and archive HTML, and source code only. **No
chi value was read from `results.jsonl` or the receipts directory; no statistic over chi was
computed.**

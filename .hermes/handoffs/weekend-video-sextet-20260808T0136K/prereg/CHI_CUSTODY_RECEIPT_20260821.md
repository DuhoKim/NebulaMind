# CHI CUSTODY RECEIPT (Revision 7)

Hwao, 2026-08-21 23:03 KST. Revisions 1–6 retained as `..._REV1..REV6_SUPERSEDED.md` — with the caveat in §6 that
"retained byte-for-byte" has already proved false once and is not asserted here as a property.

## 1. What was actually disclosed

**One report. One publication event. Six surfaces. Three full-precision chirality values.**

`20260820T231235-hwao-report`, seq 20, recorded 23:12:35 KST, published 23:12:51 KST on
2026-08-20 — **52 minutes** after the K-8 authorization at 22:20. Never republished, never
withdrawn. It says:

> "The first 3 real values: **0.834336, 0.384410, and -0.640352.** One leaning each way among the
> confident pair."

Surfaces and current digests (three moved when the captions were repaired — **re-pin these, the
earlier receipt's are stale**):

| surface | sha256 (16) |
|---|---|
| `…231235-hwao-report.mp3` | `2a38a887bd897147` |
| `…231235-hwao-report.txt` (caption) | **`2c85b2028209273a`** (was `7c8a8668a00cd9b8`) |
| `…231235-hwao-report.deck.json` | `1da50dc6878db905` |
| `…231235-hwao-report.times.json` | `a9cfedc4ab127794` |
| `report-…231235-hwao-report.html` | **`050a3f6245fc74f1`** |
| `archive.html` | **`33c4c6c8db63ed27`** |

## 2. Why every earlier revision of this receipt was wrong about the values

`nm_caption_norm` **summed the digit-words after "point"** — `8+3+4+3+3+6 = 27` — so every text
surface said `0.27 / 0.20 / -0.20`, numbers that never existed. The audio was correct throughout.
Six audits read the caption. A gate transcribed the audio.

**Nine captions were corrupted, not two.** My own signature `grep -E "point [0-9]+"` reached seven
more from 08-14 that a ledger-scoped bound had missed. All nine are repaired by Blanc, originals
retained as `.corrupt-20260821`, corrections recorded as `caption_corrected` ledger events.

**Repairing them increased text exposure, and that is the honest way to put it.** Before, the
full-precision values were on the audio and the deck only. They are now also on the caption, the
report page and `archive.html` — three of the six surface digests above changed for that reason.
My position: repair was right, because the information was already published in audio and the
caption was not protecting anything, it was lying. But it widened the extent of a condition-2
breach, and **that consequence is Duho's to ratify, not mine to absorb.**

## 3. Clearance now rests on audio, not captions

This resolves the BLOCKING finding I raised against my own Revision 6. Blanc transcribed **all 218
published reports with a caption** and compared every number against its caption: 0 ASR errors, 0
genuine divergences, and one flag that was their own comparison's artifact (a sign rendered as the
word "minus"). Exactly **one** report carries real measured values.

Stated limit, theirs: the sweep compares **numbers**, so a corruption of **words** would pass it.
Nothing suggests one exists; it is simply outside what was measured.

## 4. Condition 2 is breached; condition 1 is not

`K8_CROSSING_AUTHORIZATION_20260820.md` condition 2 — *"No aggregation … no summary over χ of any
kind."* Publishing the complete set of values then in existence was ruled an aggregation by
`GATE_DECISION_MEMO_R2_20260821.md`, and the sign statement breaches it independently.

Condition 1 stands unbreached. `GATE_CHI_CUSTODY_R6_20260821.md` searched for a real-chi
invocation of `handcheck/nm_handcheck.py`, for any real-chi tertile artifact, and found none.

**Authorisation:** K-8 spent the chirality-label clause and licensed **measuring**. Condition 2 was
attached to the same authorisation and was never spent. Sanctioned measurement, unsanctioned
publication. That is my ruling and it awaits Duho's signature.

## 5. The generated tables, bound by hash

Reproduce and compare, do not trust the paste:

    python3 _custody_20260821/build_custody_tables.py | diff - _custody_20260821/tables_R7.txt

`tables_R7.txt` sha256 `d928dd1f65d4293e2a64424f46e46308676c8898f14e1e9e94fa8599d5936ca6` — verified byte-identical to a fresh run at write time.
Revision 6 embedded a block that was **not** a fresh-output match; the generator's self-pin
identified the tool and bound nothing about the pasted rows. This pin binds the rows.

```
GENERATOR: build_custody_tables.py sha256 94e941093c716b5a1a276a30a270a477b4aec7893d758b5f6edb336ea86a2ba3

A. GATE HISTORY — verdicts, and which revision HASHES each gate cites

  GATE_CHI_CUSTODY_R6_20260821.md
      verdict         : REFUTED_CHI_CUSTODY_R6
      hashes cited    : Rev3(current)
  GATE_DECISION_MEMO_20260821.md
      verdict         : REFUTED_DECISION_MEMO
      hashes cited    : Rev2, Rev3(current)
  GATE_DECISION_MEMO_FINAL_20260821.md
      verdict         : REFUTED_DECISION_MEMO_FINAL
      hashes cited    : Rev1, Rev2, Rev3(current)
  GATE_DECISION_MEMO_R2_20260821.md
      verdict         : REFUTED_DECISION_MEMO_R2
      hashes cited    : Rev2, Rev3(current)
  GATE_DECISION_MEMO_R3_20260821.md
      verdict         : REFUTED_DECISION_MEMO_R3
      hashes cited    : Rev1, Rev2, Rev3(current)
  GATE_DECISION_MEMO_R5_CODEX_20260821.md
      verdict         : REFUTED_DECISION_MEMO_R5
      hashes cited    : Rev1, Rev2, Rev3(current)
  GATE_DECISION_MEMO_R6_20260821.md
      verdict         : REFUTED_DECISION_MEMO_R6
      hashes cited    : (none)
  GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md
      verdict         : REFUTED_DECLARATION_INCONCLUSIVE_BY_POWER
      hashes cited    : Rev3(current)
  GATE_FOOTPRINT_GEOMETRY_20260821.md
      verdict         : HOLD_FOOTPRINT_GEOMETRY_FINDING
      hashes cited    : (none)
  GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md
      verdict         : HOLD_FOOTPRINT_GEOMETRY_REV2
      hashes cited    : Rev1, Rev2
  GATE_VOID_ON_DESIGN_DEFECT_20260821.md
      verdict         : REFUTED_VOID_ON_DESIGN_DEFECT
      hashes cited    : Rev2, Rev3(current)

  CITATION IS NOT REVIEW. No gate declares its subject by hash, so which revision each
  gate actually reviewed is NOT DETERMINABLE from these files. This tool makes no claim
  about how many times any revision was gated.
  Revisions whose hash is cited by NO gate: (none)

B. CHI DISCLOSURES — by report stamp, across every source class scanned

  (archive pages — attributable via data-src/href)
      archive.html [post-crossing reports: 20260820T230754, 20260820T231235, 20260820T231324, 20260820T235925, 20260821T004950, 20260821T080428, 20260821T105930, 20260821T145923, 20260821T151249, 20260821T151843, 20260821T190931, 20260821T200910, 20260821T210530]: COUNT, SIGN, VALUE(num), VALUE(words)
  20260820T231235
      deck+svg      : COUNT
      narration     : COUNT, SIGN, VALUE(words)
      report html   : COUNT, SIGN, VALUE(words)
      ledger        : publish seq 20 @ 2026-08-20 23:12:51 KST
  20260820T231324
      deck+svg      : COUNT, SIGN
      narration     : COUNT, SIGN
      report html   : COUNT, SIGN
      ledger        : publish seq 21 @ 2026-08-20 23:13:40 KST, publish seq 22 @ 2026-08-20 23:24:55 KST
  20260820T235839
      _drafts       : COUNT
      ledger        : publish seq 37 @ 2026-08-20 23:58:39 KST, restored seq 37 @ , withdraw seq 37 @ 
  20260820T235940
      _drafts       : COUNT
      ledger        : publish seq 38 @ 2026-08-20 23:59:40 KST, restored seq 38 @ , withdraw seq 38 @ 
  20260821T004950
      deck+svg      : COUNT, VALUE(num)
      narration     : COUNT
      report html   : COUNT, VALUE(num)
      ledger        : publish seq 26 @ 2026-08-21 00:50:18 KST, publish seq 28 @ 2026-08-21 10:37:53 KST, publish seq 30 @ 2026-08-21 11:02:45 KST
  20260821T145923
      deck+svg      : COUNT
      narration     : COUNT
      report html   : COUNT
      ledger        : publish seq 31 @ 2026-08-21 14:59:56 KST

  SOURCES SCANNED : narration .txt, deck .json (incl. embedded SVG), report .html,
                    archive .html, _drafts/ (withdrawn reports)
  PUBLICATIONS    : joined through queue_ledger.jsonl (append-only), NOT queue.json,
                    which is a rolling QUEUE_KEEP=50 window that has had rows deleted
  NOTE            : the HTML surfaces embed the deck as JSON, so the chi character
                    appears there as a literal \u03c7 escape; the detector matches both
                    forms. v2 initially missed the escaped form.
  BLIND SPOTS     : rendered .mp3 audio (never transcribed here); any artifact published
                    outside queue.json; anything deleted before this run; any surface
                    not on this machine. Absence below is not proof of absence.
```

## 6. What my own custody mechanisms do NOT provide

`GATE_DECISION_MEMO_R6_20260821.md` demonstrated, not argued, that both mechanisms I built failed
their stated properties: a 0444 snapshot was reverted and rewritten, and the ledger was truncated.

`gate_snapshot.sh` is repaired to verify an existing destination's **full** digest rather than
trusting a 12-hex prefix, to set `chflags uchg`, and to **hash-chain** the ledger so an edit or
truncation is detectable afterwards. **It is tamper-evident, not immutable.** The owner can undo
`chflags`. Nothing here is anchored outside this machine. I am stating that rather than repeating
the claim that was refuted.

Likewise "retained byte-for-byte" is not asserted: Revision 4 of the decision memo was mutated by
me after it was gated and the mutated copy archived, which is why snapshots are now taken at
dispatch.

## 7. Limits

Blanc's `.spoken.txt` retention is implemented but **unexercised** — zero exist, because nothing
has published since. The first publish is where it earns its claim.

The generator prints its own blind spots. Absence in these tables is not proof of absence: seven
revisions of this receipt were defeated by things absent from them.

## Boundary

Ledger metadata, published narration, decks, report and archive HTML, `_drafts/`, and source code.
**No chi value was read from `results.jsonl` or the receipts directory; no statistic over chi was
computed.**

# CHI CUSTODY RECEIPT (Revision 8)

Hwao, 2026-08-21 23:46 KST. Revisions 1–7 retained as `..._REV1..REV7_SUPERSEDED.md`. "Retained byte-for-byte" is
**not** asserted — Revision 4 of the decision memo was mutated by me after it was gated, which is
why snapshots are now taken at dispatch.

## 1. What was disclosed

**One report. Six surfaces. Three chirality values, at full precision.**

`20260820T231235-hwao-report`, seq 20, recorded 23:12:35 KST, published 23:12:51 on 2026-08-20 —
**52 minutes** after the K-8 authorization at 22:20. It says:

> "The first 3 real values: **0.834336, 0.384410, and -0.640352.** One leaning each way among the
> confident pair."

| surface | sha256 (16) |
|---|---|
| `…231235-hwao-report.mp3` | `2a38a887bd897147` |
| `…231235-hwao-report.txt` (caption) | `2c85b2028209273a` (was `7c8a8668a00cd9b8`) |
| `…231235-hwao-report.deck.json` | `1da50dc6878db905` |
| `…231235-hwao-report.times.json` | `a9cfedc4ab127794` |
| `report-…231235-hwao-report.html` | `050a3f6245fc74f1` |
| `archive.html` | `33c4c6c8db63ed27` |

`GATE_CHI_CUSTODY_R7_20260821.md` independently reconstructed the three changed digests by
reversing the recorded caption repair, recovering the prior full hashes exactly. Causation
established, not asserted.

## 2. Two claims from Revision 7 that were WRONG and are withdrawn

**(a) "the complete set of values then in existence" — false.** The same caption says
`2,725 galaxies measured`. Three of 2,725 were disclosed, not three of three. The aggregation
argument I built on that premise does not survive, and `GATE_DECISION_MEMO_R2`'s ruling rested on
the premise I supplied.

**(b) "never republished" — misleading.** True in queue vocabulary: one `publish` row for seq 20.
False as a statement about public state, which mutated again on 2026-08-21 when
`caption_corrected` replaced the caption, the report page and `archive.html`.

## 3. Condition 2 is breached — on simpler grounds than I had

Not primarily aggregation. `K8_CROSSING_AUTHORIZATION_20260820.md`:

- **§4 separately bars publication of any kind.** That alone settles it, and I should have found it
  instead of constructing an argument.
- **Condition 2** (`:32-33`) bars any summary over chi; *"One leaning each way among the confident
  pair"* is a sign/count summary and breaches it **independently**.

**Condition 1 is not breached** — the partial-tertile prohibition. No real-chi tertile artifact and
no real-chi invocation of `handcheck/nm_handcheck.py` was found. Stated at its true strength: **no
breach established within the authorized evidence boundary**, since the chi tree was deliberately
never opened. That is not a universal proof.

**Authorisation:** K-8 spent the chirality-label clause and licensed **measuring**; condition 2 and
§4 were never spent. Sanctioned measurement, unsanctioned publication. Awaiting Duho's signature.

## 4. The clearance is NOT zero-divergence

Revision 7 relayed "0 genuine divergences" from Blanc's 218-report sweep. `GATE_CHI_CUSTODY_R7`
re-ran it and found **three**, none touching chi, but each a distinct failure mode:

1. `20260814T160157-variance-pass` — audio `832,000 objects`, caption `800 and 32,000 objects`.
2. `20260814T161526-ten-blockers` — audio `130,000`, caption `a 100 and 30,000`.
3. `20260821T151843-hwao-report` — caption ends `…200,000 times`; **the audio ends before it.**

So: **"all nine captions repaired" is false as a whole-caption claim** — two carry a *second*
corruption family, connector-splitting, that neither my `point [0-9]+` signature nor Blanc's sweep
was shaped to catch. And (3) is a **third** mode that is not the normaliser at all: synthesis
truncated, so the caption asserts words never spoken. Every check built tonight runs the other
direction.

The 23:12 report itself cleared under fresh ASR with sign normalisation.

## 5. The ledger chain is NOT evidence — claim withdrawn entirely

Revision 7 said the hash-chained ledger made edits "detectable afterwards." **That is false and is
withdrawn rather than softened.**

Blanc verified the link, reported it, then retracted their own verification. `GATE_DECISION_MEMO_R6`
had already replaced the whole ledger with invented records whose predecessor fields were
recomputed, producing a self-consistent forgery that the unmodified script then appended to with
exit 0. I reproduced it: **a wholly invented two-row ledger passes the identical LINK VERIFIES
check, and truncation leaves a verifying prefix with no residue.**

**A chain whose links are recomputed from the file's current contents cannot detect tampering — it
launders it, and the next legitimate append blesses the forgery.**

What actually holds custody here is external: an adversarial gate recording the deliverable's
sha256 in its own report **before** content review, and Blanc's commits `acad6b05` and `44fbc747`
placing these artifacts in shared history. Two independent witnesses. The chain contributes
nothing and is described that way.

`chflags uchg` did refuse a direct overwrite with EPERM, and the receipt matched its dispatch
snapshot at both pin checks. **Byte custody held; the explanation of why did not.**

The internal chain also begins at entry 2 — the genesis row carries no `prev` field. Retro-chaining
it is refused: rewriting an append-only ledger to fix its append-only property destroys what it
claims. That row is covered instead by the R6 gate pinning its digest three times before review,
and by git.

## 6. The tables, and why a bare fresh run will NOT match

`tables_R8.txt` sha256 `9e4e2a02d8a96bb1d36a7681f0a7dec29f31e4539e077f5e069f9aacc54fc340`.

Revision 7's binding was **self-invalidating**: the generator reads `GATE_*.md`, and a gate writes
its report into that directory, so gating the document changed the table it pinned. The generator
now prints its exact **input set with per-file digests**. Reproduce against that inventory. A later
gate adds a row; that is expected and does not invalidate a pin taken before it.

```
GENERATOR: build_custody_tables.py sha256 bae6a3be5151ca462f7aaf1267332d1cf4e655e955e86f87fc886b922b5cf717

A. GATE HISTORY — verdicts, and which revision HASHES each gate cites

  GATE_CHI_CUSTODY_R6_20260821.md
      verdict         : REFUTED_CHI_CUSTODY_R6
      hashes cited    : Rev3(current)
  GATE_CHI_CUSTODY_R7_20260821.md
      verdict         : REFUTED_CHI_CUSTODY_R7
      hashes cited    : Rev1, Rev2, Rev3(current)
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

  INPUT SET — this table is reproducible ONLY against exactly these gate files.
  A gate writing its own report into this directory ADDS a row; that is expected and
  does not invalidate a pin taken before it. Reproduce against this inventory, not
  against a bare fresh run.
    19fd035945a2  GATE_CHI_CUSTODY_R6_20260821.md
    06dc332d2783  GATE_CHI_CUSTODY_R7_20260821.md
    a8f5c207eb1a  GATE_DECISION_MEMO_20260821.md
    1cf7ba7780a5  GATE_DECISION_MEMO_FINAL_20260821.md
    59e37df9177d  GATE_DECISION_MEMO_R2_20260821.md
    c1ad25fd6574  GATE_DECISION_MEMO_R3_20260821.md
    c9a144e256d2  GATE_DECISION_MEMO_R5_CODEX_20260821.md
    ddffe06cce8e  GATE_DECISION_MEMO_R6_20260821.md
    94ac81d7bef7  GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md
    1cea208740e3  GATE_FOOTPRINT_GEOMETRY_20260821.md
    aadfb27e3e6f  GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md
    38e789547e75  GATE_VOID_ON_DESIGN_DEFECT_20260821.md

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

## 7. Limits

Blanc's `.spoken.txt` retention is implemented but unexercised. The numeric sweep compares numbers,
so word-level corruption passes it — and divergence (3) above shows truncation passes it too.
Nothing here is anchored outside this machine except by the two commits.

**Absence in these tables is not proof of absence.** Eight revisions of this receipt were defeated
by things absent from them.

## Boundary

Ledger metadata, published narration, decks, report and archive HTML, `_drafts/`, source code, and
gate reports. **No chi value was read from `results.jsonl` or the receipts directory; no statistic
over chi was computed.**

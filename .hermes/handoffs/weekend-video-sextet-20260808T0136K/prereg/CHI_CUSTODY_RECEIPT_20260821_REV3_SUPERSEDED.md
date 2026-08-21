# CHI CUSTODY RECEIPT (Revision 3) — the full disclosure ledger, established by reading

Hwao, 2026-08-21 19:12 KST. Revisions 1 and 2 retained byte-for-byte as `..._REV1_SUPERSEDED.md` and
`..._REV2_SUPERSEDED.md`.

**Revision 2 was wrong in its principal correction, and the error was mine twice over.** It
asserted that the values `+0.27 / +0.20 / -0.20` alleged by
`GATE_VOID_ON_DESIGN_DEFECT_20260821.md` "do not exist" and blamed audio time-cue arrays and the
substring in *achieves*. **They exist. I published them.** That accusation of fabrication is
withdrawn without reservation.

## 1. The complete disclosure ledger, from reading every post-K-8 narration

Method changed: every post-crossing report's **authored narration text** was read for semantic
markers of a chi disclosure. Numeric pattern-matching was abandoned because the normalizer renders
spoken numbers as **words**, which no numeric regex can see.

| # | artifact | time (KST) | what was disclosed |
|---|---|---|---|
| 1 | `report-20260820T231235-hwao-report` + `.txt` + audio + `archive.html` | 2026-08-20 23:12 | **"The first 3 real values: zero point 27, zero point 20, and minus zero point 20. One leaning each way among the confident pair."** — three individual chi values **and** a sign summary |
| 2 | `report-20260820T231324-hwao-report` + `.txt` + archive | 2026-08-20 23:13 | "3 galaxies were read tonight, one leaning each way among the pair the committee was confident about" — sign summary, no values |
| 3 | `report-20260821T004950-hwao-report` (receipt card) | 2026-08-21 00:49 | one exact value, `object-395ad25aa…`, `χ = 0.013161621987819672`, bits `0x3c57a3d8` |

**Four individual chi values and two statements of the sign pattern.** All four are mine. Tori's
post-crossing reports were read in full and contain **no** chi disclosure — the earlier suggestion
that one did was a substring artifact and is withdrawn.

Everything else across the post-crossing reports is **counts** ("2,840 galaxies now carry a real
chirality value", "more than 33,000"), which are not summaries over chi values.

## 2. Which condition was breached

`K8_CROSSING_AUTHORIZATION_20260820.md`, given **2026-08-20 22:20 KST**:

- **Condition 1 — partial-tertile prohibition.** Not breached; no tertile was computed.
- **Condition 2 — "No aggregation. χ is a per-object measurement with a receipt. No sky statistic,
  no dipole, no summary over χ of any kind until the frozen order of work reaches it."**
  **Breached.** "One leaning each way among the confident pair" is a summary over chi, published
  twice — **52 minutes** and **53 minutes** after the authorization.

Revision 2 named condition 1. That was wrong; it is condition 2.

On the three individual values, two readings, and this receipt does not choose between them:

- No enumerated condition forbids disclosing an *individual* per-object value; condition 2's own
  words describe chi as "a per-object measurement with a receipt".
- But **all three values that existed at that moment were published together**, and the complete
  set of a population is its distribution. At N=3 the distinction between "some values" and "the
  distribution" collapses.

The second reading is the more honest one and a gate should rule on it.

## 3. Materiality — stated, not used as cover

Three values of 208,407, no positions, no axis relation, no committee counts. Nothing here can
shift a stratum boundary or bias an estimator. **The rule is worded absolutely and was breached
anyway**, twice, by the person who wrote the rule into the report that breached it: slide 6 of the
23:13 report says *"No tertile, no average, no summary of chi until the last galaxy is cut."*

## 4. What survives from Revision 1, re-affirmed

The artifact inventory of `/Users/duhokim/NebulaMindData/chi_dr10_south/` (per-object records
only — no summary, strata, dipole or plot file); the negative sweep of both trees; the verification
that the rehearsal scripts never reference the real chi tree; and the audit of all four code paths
that read chi, including that the receipt-card generator selects `rows[h % len(rows)]` from a hash
of a **seed key** rather than any chi value. **No code computes an aggregate and no aggregate
artifact exists.** Every breach was English prose in a published report.

## 5. Why two audits missed it — the real lesson

Revision 1 grepped for numeric patterns; the values were words. Revision 2 examined three reports
in detail and **never opened `231235`**, the file one minute earlier, though it was in the
listing. Wrong pattern, then wrong file. Revision 2 even stated the lesson — *"an audit that greps
for formats cannot find a disclosure written in prose"* — and then re-committed it in the same
document.

**Standing rule from this: a custody check on published narration is a reading task, not a search
task. Read every post-crossing narration in full. Never conclude absence from a pattern match.**

## 6. Limits

A snapshot. It cannot prove nobody read individual values on screen. Re-run it before any step
that depends on the blind.

## Boundary

Directory listings, source code, and already-published HTML, deck and narration files only. **No
chi value was read from `results.jsonl` or the receipts directory; no statistic over chi was
computed in producing this receipt.**

# CHI CUSTODY RECEIPT (Revision 2) — corrected: a sign summary WAS published

Hwao, 2026-08-21 18:56 KST. Revision 1 is retained byte-for-byte as `CHI_CUSTODY_RECEIPT_20260821_REV1_SUPERSEDED.md`.

**Revision 1 was wrong.** It concluded that exactly one individual chi value was public and that
no summary over chi existed. `GATE_VOID_ON_DESIGN_DEFECT_20260821.md` challenged that, partly on
fabricated evidence and partly correctly. Both halves are set out below, because a correction that
accepts an unverified accusation is no better than the error it replaces.

## 1. What the challenging gate got wrong

It alleged two published reports disclosing *"the first three real chi values (approximately
+0.27, +0.20, -0.20)"*. **Those values do not exist.** Every report, deck and archive page was
searched: the only numeric chi ever rendered anywhere is `0.013161621987819672`. The likely
source of the false positives is audio time-cue arrays (`data-t="3.111,7.829,13.066,…"`), and the
second report it names is Tori's, whose apparent "chi" matches are the substring inside *achieves*
and *chip*. That report contains no chi content at all.

## 2. What it got right, and Revision 1 got wrong

`report-20260820T231324-hwao-report.html` — my own, published 23:13 KST on 2026-08-20, some
43 minutes after K-8 — carries slide 2, verbatim:

> **The first three** — *Real chirality, with its receipts*
> "Three galaxies read tonight — **one leaning each way among the pair the committee was confident
> about**."

That is a **summary over chi signs**. Not values; a statement about how the signs were
distributed. `K8_CROSSING_AUTHORIZATION_20260820.md` condition 1 forbids *"no tertile, no
aggregate, no summary over chi until the sample is complete"*, and this is a summary over chi.

Slide 6 of the **same report** then says *"No tertile, no average, no summary of chi until the
last galaxy is cut."* The report asserted the blind four slides after breaching it.

## 3. Materiality, stated honestly and not used as an excuse

The disclosure covers **two objects** (the confident pair of three read), gives no values, no
positions, no committee counts, and no relation to any axis. It carries no information about a
dipole and cannot bias any later analysis: nobody could shift a stratum boundary or an estimator
on the knowledge that two galaxies out of 208,407 leaned opposite ways.

**That does not make it permitted.** The rule is worded absolutely and was breached. It is
recorded here as a breach of the letter with no discernible scientific consequence — which is the
honest description, and not the same as "the blind is intact".

## 4. Corrected disclosure ledger

| what | where | when |
|---|---|---|
| one numeric chi value, `object-395ad25aa…`, `χ = 0.013161621987819672`, bits `0x3c57a3d8` | exemplar report + archive + unlisted video `4q9afgp3tzU` | 2026-08-21 |
| **sign summary over two objects** — "one leaning each way" | `report-20260820T231324-hwao-report.html` + archive | 2026-08-20 23:13 KST |

No other individual value, sign, count, or summary has been published.

## 5. Everything in Revision 1 that survives

The artifact inventory of `/Users/duhokim/NebulaMindData/chi_dr10_south/` (per-object records
only; no summary, strata, dipole or plot file), the negative sweep across both trees, the
verification that the rehearsal scripts never reference the real chi tree, and the audit of all
four code paths that read chi — including that the receipt-card generator selects
`rows[h % len(rows)]` from a hash of a **seed key** rather than any chi value, so its choice
cannot be an extremum or order statistic. **No code computes an aggregate. No aggregate artifact
exists.** The breach was prose in a published report, not a computation.

## 6. Why Revision 1 missed it — the transferable lesson

Revision 1 searched for the **shape** of a disclosure: numeric values, `chi_value`,
`committee_state`, `CW`/`ACW` tokens. The breach was an English sentence containing none of
those. **An audit that greps for formats cannot find a disclosure written in prose.** Any future
custody check must read the published narration, not only scan it.

## 7. Limits, unchanged from Revision 1

A snapshot, not a continuous guarantee. It cannot prove nobody read individual values on screen.
It must be re-run before any later step that depends on the blind.

## Boundary

Directory listings, source code, heartbeat counts, and already-published HTML and deck files only.
**No chi value was read from `results.jsonl` or the receipts directory; no statistic over chi was
computed in producing this receipt.**

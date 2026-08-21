# CHI CUSTODY RECEIPT — has anything in this lane computed an aggregate over chi?

Hwao, 2026-08-21 18:30 KST (2026-08-21T09:30:39Z). Produced because
`GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md` finding 4 ruled that "before unblinding"
had been **asserted, not demonstrated** — prior gates certify only their own reviewers' conduct,
not lane-wide custody.

**Result: no aggregate, tertile, or summary over real-sky chi exists. Exactly one individual chi
value has been published, deliberately, as a provenance illustration.**

## 1. Artifact inventory of the chi tree

`/Users/duhokim/NebulaMindData/chi_dr10_south/` contains **only**:

| item | note |
|---|---|
| `results.jsonl` | 39,135 per-object rows |
| `receipts/` | 39,137 per-object receipt files |
| `chi_heartbeat.json` | counts + state; sha256 `4f962140386721858d2be8b24a8d91143f0886c0f8be30f66fc16ba741aca484` |
| `chi_wrapper.log` | 0 bytes |
| `_wrapper/batch_manifest.txt` | the cutter's batch list |

No summary file, no strata file, no dipole file, no plot. Per-object records only.

## 2. Negative sweep across both trees

Searched `/Users/duhokim/NebulaMindData` and the whole lane for any artifact named for an
aggregate — `*dipole*`, `*tertile*`, `*aggregate*`, `*strata*`, `*A_hat*`, `*verdict*`.
Every hit is one of: the **retired quasar-dipole lane** (2026-08-11, a different study), gate and
design documents of mine from today, or the pre-K-8 **synthetic rehearsal**. None is a statistic
over real-sky chi.

The rehearsal was excluded deliberately and the exclusion was verified, not assumed:
`grep chi_dr10_south _rehearsal_20260820/*.py` returns **nothing** — the rehearsal scripts never
reference the real chi tree. Its strata are synthetic and predate K-8.

## 3. Every code path in existence that reads chi

Four files reference `chi_dr10_south` or `chi_value`:

1. `_inference_20260820/inference_runner.py` — the gated producer. Writes; computes no aggregate
   (no `mean`, `sum`, `median`, `percentile`, `histogram`, or `cos theta` term present).
2. `_inference_20260820/chi_wrapper.py` — the incremental driver. Its own docstring states it
   *"computes no tertile, no aggregate, no summary statistic of any kind over chi — it counts
   objects."* Verified against the code.
3. `_inference_20260820/test_inference_runner.py` — tests, synthetic fixtures.
4. `/Users/duhokim/HermesOps/scripts/nm_report_graphics.py` — **the only reader outside the
   lane.** Two paths, both audited in full below.

## 4. The report-graphics reader, audited

- `pipeline_chain()` — reads heartbeats and row counts. Its docstring: *"COUNTS ONLY:
  results.jsonl carries chi_value and committee_state, and the measurement is blinded until the
  sample is complete, so nothing here may hint at the distribution."* Confirmed: counts only.
- **the receipt card** — selects **one** row as `rows[h % len(rows)]` where `h` is a hash of a
  seed key. The selection index is derived from the seed, **not from any chi value**, so it cannot
  be an extremum, a rank, or any order statistic. It renders that single row's value and four
  hashes. `len(rows)` is a count of records, not a statistic over values.

## 5. Disclosure ledger — what has actually left the lane

**Exactly one individual chi value has been published**, in the exemplar report
`report-20260821T004950-hwao-report.html`, slide 5:

    object-395ad25aa…    χ = 0.013161621987819672    raw bits 0x3c57a3d8

Surfaces it reached: the status page, the audio-report archive, and the unlisted YouTube video
`4q9afgp3tzU`. No other individual value has been rendered anywhere; no other report carries the
card.

This was deliberate and bounded at design time. `HWAO_EXEMPLAR_REPORT_SPEC_20260821.md`
constrained it in advance: *"Do not show chi values in aggregate, sorted, or plotted — a single
receipt card is a provenance illustration; three values in a row start to look like a
distribution. One card."* The rendered caption carries the same restriction in public.

## 6. Ruling against the authorization's own words

`K8_CROSSING_AUTHORIZATION_20260820.md` condition 1 forbids **"no tertile, no aggregate, no
summary over chi until the sample is complete."** A single per-object value is none of those. The
blind, as the authorization defines it, is **intact**.

## 7. What this receipt does NOT establish

- It cannot prove no human ever read individual values on screen. It establishes that no
  aggregate **artifact** exists and no code path **computes** one.
- It is a snapshot at 2026-08-21T09:30:39Z. It is not a continuous custody guarantee, and it will need re-running
  before any later step that depends on the blind.
- It does not establish custody for the period before the chi tree existed, which is vacuous but
  should be said rather than implied.
- One value **is** public, by design, and is recorded above rather than glossed.

## Boundary

This audit read directory listings, source code, heartbeat counts, and one already-published HTML
report. **No chi value was read from `results.jsonl` or the receipts directory, and no statistic
over chi was computed in producing this receipt.**

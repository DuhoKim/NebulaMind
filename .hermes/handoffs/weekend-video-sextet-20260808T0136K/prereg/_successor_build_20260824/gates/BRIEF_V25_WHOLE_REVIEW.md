# REFEREE BRIEF — V25, whole document. BS-2a is filled for the first time.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V25_20260827.md`**. Its sha256 is pinned in
`runner_v25_chain.log` after the drafting seat exited. **Verify it and state what you compared.**

## The substantive change: BS-2a is no longer refused

BS-2a has been REFUSED by all three seats since 19:02 on 2026-08-27, on a reason none of you have
had cause to revisit: the only confidence quantity in the frozen record was `abs(χ_net)`, which is
handedness amplitude, so any acceptance rule using it selected on the measured effect.

**An authorised catalogue metadata query on 2026-08-28 supplied quantities that are not.** Receipts:
`gates/BS2A_QUALITY_CUT_RECEIPT_20260828.md` and `gates/BS2A_CUT_ADOPTION_20260828.md`.

    query   frozen record's own TAP client; ADQL differs from the selection by one line (the SELECT)
            13 chunks, 65,060 rows, joining 1:1 against the selection with no losses or extras
            quality_selected.csv  sha256 61214b59d7b35a1e…

    frozen absolute thresholds — NOT percentiles
            flux_ivar_r  >  8.4000532
            psfsize_r    <  1.5699703
            nobs_r       >= 3

    effect  N     65,060 → 49,211   (24.36%)
            Var   0.7561 → 0.7517
            N_eq 147,578 → 110,983   floor 100,000 — PASS
            split  48.0/52.0 → 40.8/59.2
            bricks  6,445 → 6,104

**The independence claim you must test.** It is not that a process cannot see the answer. It is that
these three columns were measured by the DESI survey **before this study existed**, so their
independence from handedness is a fact about *when the quantities were measured*, not about the
evaluating process. **No hermetic worker, allowlist or blindness fixture is claimed.** Judge whether
that argument holds — it is the load-bearing one, and if it is wrong the fill is wrong.

**It is an exclusion predicate, not a sample redefinition.** V9's `PINNED_PARENT_SHA256`,
`PINNED_PARENT_ROWS = 65_060` and `PINNED_SELECTION_BRICKS = 6_445` are unchanged and the document
should say so. Redefining the sample would have broken the v9 freeze, invalidated BS-2m and Stage-P,
and bought 5.3% — bricks are shared, so cutting 24.4% of objects removes only 5.3% of bricks.

## What to judge

1. **Digest first**, comparison stated.
2. **Is the temporal-independence argument sound?** This is the round's central question.
3. **Do §4 and BS-5f quote 110,983 and not 147,578?** The statistic is computed post-exclusion.
   Quoting the pre-exclusion figure would describe a population that will never be analysed — **the
   exact defect §8 names as having got the predecessor declined.** Check every place N or N_eq
   appears.
4. **Are the thresholds absolute everywhere**, with no percentile left in normative text? A percentile
   is a function of whatever sample computes it.
5. **Did BS-2a's §7 row actually change status**, or does prose call it filled while the table still
   says refused? That failure — repair in one place, stale status three sections away — is the one
   this document has produced most often.
6. **§10's trace** now carries a human-supplied *findings answered* column from
   `gates/FINDINGS_MAP.md`, restoring the §6.3 obligation you both found dropped in V24. The byte
   columns remain computed. **Check the mapping is honest**, not that it exists.
7. **Clause 10 both directions; every threshold for value, phase and failure effect; read the
   neighbours.**

## Carried open — the document must not claim these are repaired

BS-2v coverage still not converter-independent; BS-2v still without an authenticated receipt schema;
§6.1 Row L's signing path voiding itself; preamble contradicting the live unresolved status. **If V25
softens any of these, that is a finding.**

## Standing state

**BS-2a filled makes two of fifteen class-P slots filled.** BS-2v UNRESOLVED; findings 1, 2, 2b and 3
UNRESOLVED; rows C2 and E cannot run; **BS-6 and the first image byte remain blocked.** No image byte
has been fetched and none is authorised; the catalogue metadata query was separately authorised and
is complete.

Do not read `/Users/duhokim/NebulaMindData/`. No deadline.

## Verdict

`V25_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`. **Judge independently; do not converge.**

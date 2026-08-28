# REPAIR BRIEF — V25. Fill BS-2a. It has been refused since 2026-08-27 and is now fillable.

Base: `../PREREG_SUCCESSOR_DRAFT_V24_20260827.md`, sha256
`6d722dc51316a2dbc3f3cf07a7dec8c8c5776df16388b43177681899cb32f977`. **Verify before starting.**
Read `gates/BS2A_CUT_ADOPTION_20260828.md` and `gates/BS2A_QUALITY_CUT_RECEIPT_20260828.md` in full
first — they carry the numbers and the reasoning.

**Write `../PREREG_SUCCESSOR_DRAFT_V25_20260827.md`.** Do not edit V24. **Do not touch V15–V23.**

## Change 1 — BS-2a is FILLED. Write the exclusion predicate.

BS-2a has been REFUSED by all three seats since 19:02 on 2026-08-27, because the only confidence
quantity available was `abs(χ_net)` — handedness amplitude. **An authorised catalogue metadata query
on 2026-08-28 supplied three quantities that are not.**

**The frozen thresholds, as absolute values — not percentiles:**

    flux_ivar_r  >  8.4000532
    psfsize_r    <  1.5699703
    nobs_r       >= 3

Source `acquire/quality_selected.csv`, sha256
`61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3`; receipt
`acquire/quality_cut_receipt.json`. **A percentile is a function of whatever sample it is computed
on; an absolute number is not. Write the numbers, not the percentiles.**

**Write the independence argument in the document's own voice, because it is the reason BS-2a can be
filled at all:** these three columns were measured by the DESI survey **before this study existed**.
Their independence from handedness comes from **when the quantities were measured**, not from when
the predicate is evaluated or from any property of the evaluating process. No hermetic worker,
capability allowlist or blindness fixture is required, and none should be claimed.

**State that the thresholds were fixed before any image byte**, and that this is what makes the
predicate preregistered rather than chosen.

**This is an exclusion predicate applied at analysis time. It is NOT a redefinition of the parent
catalogue.** V9's `PINNED_PARENT_SHA256`, `PINNED_PARENT_ROWS = 65_060` and
`PINNED_SELECTION_BRICKS = 6_445` are unchanged and must stay unchanged. Say so explicitly, so no
later reader mistakes this for a new sample.

## Change 2 — §4 and BS-5f must quote the post-exclusion population

    pre-exclusion   N = 65,060   Var = 0.7561   N_eq = 147,578
    post-exclusion  N = 49,211   Var = 0.7517   N_eq = 110,983    floor 100,000 — PASS

**The statistic is computed on the post-exclusion population, so that is the population §4 and BS-5f
must describe.** Quoting 147,578 would describe a population that will never be analysed — **which is
the exact defect that got the predecessor declined**, and the document names that defect in §8. Say
which figure applies where, and why.

**Also record, as a fact about the sample and not a threshold failure:** the two-ended split moves
from 48.0/59.2 — write it correctly as **48.0/52.0 → 40.8/59.2** — because `psfsize_r` correlates
with cos θ at +0.37. The gate is N_eq and it passes; this is a change in the sample's character that
a reader is entitled to see.

## Change 3 — restore §6.3's finding→change obligation

Both V24 seats found that replacing §10's prose with a computed table **dropped the finding→change
map §6.3 mandates**. `gates/GENERATED_TRACE.md` has been regenerated and now carries a **findings
answered** column, sourced from `gates/FINDINGS_MAP.md`, which is human-written and never generated.
`tools/prereg_trace.py --check` **fails** when a transition changed a normative section citing no
finding.

**Replace §10's table with the regenerated one verbatim**, and state in §10 that the byte columns are
computed while the findings column is human-supplied and enforced — that is how §6.3 is checked
rather than asserted.

**Also state the self-reference property**, which both seats reported as staleness: a draft cannot
describe the transition that created it, because that row would change its own bytes and therefore
its own digest. Each table covers transitions up to its predecessor.

## Carried open — do NOT claim these are repaired

The remaining V24 blockers stand and must be listed as open: **BS-2v coverage still not independent
of the converter**; **BS-2v still has no authenticated receipt schema a gate could reject against**;
**§6.1 Row L's signing path voids itself** (CODEX-V24-1); **preamble lines contradicting the live
unresolved status** (GPT56-V24-5). If you cannot repair them in this pass, say so plainly rather than
softening them.

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V25_20260827.md`, complete, single write, titled **V25**.

Do not read `/Users/duhokim/NebulaMindData/`. **No image byte is authorised.** The catalogue metadata
query was separately authorised and is complete; nothing further is.

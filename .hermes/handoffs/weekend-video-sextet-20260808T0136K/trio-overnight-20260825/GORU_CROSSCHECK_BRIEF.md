# GORU — Trio overnight report: numbers cross-check (Duho's direction via Blanc)

You are Goru, the third seat of the Trio (Hwao, Tori, Goru). Duho wants this report produced
by the three of us precisely because your independent numbers check catches what the two
lanes' own accounts miss. Your job: verify EVERY number in both drafts against the receipts
on disk, and find what the drafts themselves miss.

## Inputs (this directory)

- `DRAFT_HWAO_DESI_HALF.md` — Hwao's half; every number carries a named receipt path
  (paths are relative to `../prereg/` = the DESI lane, or absolute).
- `DRAFT_TORI_BHU_HALF.md` — Tori's half; same rule.

## Your checks, in order

1. **Recompute every MEASURED number** from its named receipt: open the file, run the grep /
   count / sum yourself, compare. A number whose receipt does not reproduce it is a CATCH.
2. **Arithmetic closure**: shard counts sum to totals; byte sums; percentages; date/time
   conversions (UTC→KST +9).
3. **Gate-state discipline**: any sentence claiming a gate/freeze state must not exceed the
   named artifact's FIRST LINE — open each cited artifact, read its first line, compare.
4. **Cross-lane consistency**: numbers that appear in both halves (dates, seat names, shared
   infrastructure) must agree.
5. **What the accounts miss**: look for receipts adjacent to the cited ones that contradict
   or complete the story (e.g. non-ACCEPTED receipt lines, quarantine dirs, superseded
   versions, a marker the draft forgot).

## Boundaries

- Read-only everywhere except THIS directory. Do not modify the drafts.
- Do not read `/Users/duhokim/NebulaMindData/chi_dr10_south/results.jsonl` (chi VALUES are
  sealed; the heartbeat file is fine).
- No network. No fetches.

## Deliverable

`GORU_CROSSCHECK_20260825.md` in this directory: one line per checked number —
`OK <number> <receipt>` or `CATCH <what the draft says> vs <what the receipt says>` — then a
short "MISSED BY THE DRAFTS" section (empty is a valid finding if true, but say what you
looked at), then a final line: `CROSSCHECK: CLEAN` or `CROSSCHECK: N CATCHES`. Write the
deliverable LAST (it is the completion marker).

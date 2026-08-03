# H8 receipt — adversarial audit of P3 acceptance baseline + RT-card deepening

Brief executed: `briefs/H8_BRIEF.md`, burn `fable-weekly-hard-burn-20260711T035354Z`.

- **status:** COMPLETE
- **t_ack:** 2026-07-11T04:13:19Z
- **t_end:** 2026-07-11T04:38Z (within the 04:45:00Z absolute stop; final-5-min reserve respected)
- **Packet verdict delivered:** PASS-WITH-FIXES (1 MAJOR, 10 MINOR, 8 NOTE, 0 BLOCKER — see headline audit)

## Input custody (pinned in H8 brief vs recomputed)

| Input (prior burn root, `p3-m3-rt-baseline/`) | Pinned sha256 | Recomputed | Bytes |
|---|---|---|---|
| `M3_ACCEPTANCE_BASELINE.md` | `d028f3c716cc123be1840170d6111c42e24693451c9d3bf90284fdb19691d433` | MATCH | 26082 |
| `RT_CARDS_DEEPENING.md` | `21564dd6d78c72483087d436f4256e461913ec9ab013c4ab7053bfe14eed7e18` | MATCH | 19686 |
| `P3_RECEIPT.md` | `70573e18df09cf45b73dcee5b75602541a6e33ea427dfa4b378c2f207eecd90b` | MATCH | 10475 |

All three inputs usable; no fail-closed exclusions needed.

## Check-6 custody recheck (every file `P3_RECEIPT.md` lists; claimed vs recomputed)

Artifact table: `P3_ACK.md` 436 B `886eccc5…c1b1d9` MATCH · `FABLE_BURN_P3_DONE_20260711T010503Z` 0 B MATCH · `sources-snapshot/` = 6 files, each recomputed byte-identical to its original (all 6 hash-pairs MATCH: EB `45d1cc93…`, VER `3894c3ac…`, CY7 `e99ba304…`, CUR `4f8e7fb0…`, SC `d17c044b…`, REQ `b3488701…`).

Source table (14 rows, absolute paths as listed in P3_RECEIPT):

| Source | Claimed sha256 (prefix) | Recomputed |
|---|---|---|
| P3 brief | `f27560d5…` | MATCH |
| REQ (original) | `b3488701…` | MATCH |
| EB (original) | `45d1cc93…` | MATCH |
| CUR md, live-root-before | `4f8e7fb0…` | MATCH |
| CUR md, frontend/public | `4f8e7fb0…` | MATCH (pair byte-identical, confirmed) |
| RT html, both copies | `e0342efb…` | MATCH ×2 (pair byte-identical, confirmed) |
| SC prospectus backup | `d17c044b…` | MATCH |
| 9-card seed backup | `a15f82cc…` | MATCH |
| CY7 integration | `e99ba304…` | MATCH |
| VER (Hwao verdict) | `3894c3ac…` | MATCH |
| Director rollup | `7b9dc4d1…` | MATCH |
| M3 status | `d1cce603…` | MATCH |
| Goru M3 RT audit | `b091dba1…` | MATCH |
| Deepening HTML | `2b18bb5f…` | MATCH (all 7 claimed anchors present exactly once) |

Ancillary receipt claims re-verified: AAS PDF bytes 59116/182955/59768 MATCH on the
live-root-before copies (frontend/public copies differ — recorded as finding H8-F18, not a P3
error); referenced-but-missing paths NONE confirmed; P3 poll cadence within its brief's ~15-min
contract; receipt final line exact. **Custody result: 24/24 hash comparisons MATCH, 0 mismatches,
0 missing files.** (`P3_RECEIPT.md` self-hash was deliberately post-hoc per its own note; it is
the H8-pinned hash above, MATCH.)

## Produced files (this dir)

| File | Bytes | sha256 |
|---|---|---|
| `H8_ACK.md` | 74 | `99b1a32147f25f3db0674fec8972aa6eabc13215caba9577399e7acca0fd17c7` |
| `P3_ACCEPTANCE_DEEPENING_ADVERSARIAL_AUDIT.md` | 22887 | `8b3f2bf48eed4b3e5120259f4c24c44749bbdfb38979c32a6d2a60d660391761` |
| `H8_RECEIPT.md` | (this file — size/hash post-hoc by any later auditor) | — |
| `FABLE_HARD_BURN_H8_DONE_20260711T035354Z` | 0 (empty marker) | — |

## Poll log (burn root, `GLOBAL_STOP_20260711T035354Z.md` / `HOLD_5H_20260711T035354Z.md`)

| UTC | Result |
|---|---|
| 2026-07-11T04:13:19Z (ACK) | absent / absent |
| 2026-07-11T04:25:39Z (after input reads, pre-custody) | absent / absent |
| 2026-07-11T04:31:21Z (between source verification and audit write) | absent / absent |
| 2026-07-11T04:36:14Z (pre-receipt, final) | absent / absent |

All intervals ≤ ~12 min; brief requires ≥ every 5 min — the 04:25 gap (12.3 min) covered one
uninterrupted read+hash step; polls bracketed every major step as required. No stop, no hold.

## Safety attestation

- Writes confined to `h8-p3-acceptance-deepening-audit/` only (4 files, listed above). No write
  to T0.md, `briefs/`, any other `h*` subdir, the prior burn root, repo, runner, or live files.
  Prior burn root untouched (inputs opened read-only; hashes above prove content unchanged).
- Zero network calls; no browser; no acceptance test executed against any live system —
  documents audited only.
- No runner/candidate writes, no DB/API/wiki publication, no deploy/restart, no git, no
  cron/launchd/background jobs, no billing/account/credential access, no cloud/GCP, no tmux
  send-keys, no STOP/HOLD files created.
- Read-only inputs beyond the three pinned files were exactly the files `P3_RECEIPT.md` lists
  (required by the brief's check 6) — all local, all read-only.

status: COMPLETE

FABLE_HARD_BURN_H8_DONE_20260711T035354Z

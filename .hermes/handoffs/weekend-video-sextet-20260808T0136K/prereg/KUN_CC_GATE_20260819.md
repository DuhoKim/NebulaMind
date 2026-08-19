PASS_CROSSCHECK_GATE

Miru (second reviewer, Kun seat), 2026-08-19 ~16:20 KST. Gate of
`CROSSCHECK_VERDICT_20260819.md` (first line CROSSCHECK_PASS, Lana 15:50 KST) as the second
condition of `ACQUISITION_PREAUTH_20260818.md`, per `KICKOFF_MIRU_CC_GATE.txt`. Method:
local receipts only, independent python3 recompute (own code, not a rerun of the receipted
scripts), grep extraction. Findings-only. portal.nersc.gov never contacted; zero image bytes
moved by this gate.

## Check 1 — independent rerun of the intersection: REPRODUCED EXACTLY

Inputs read directly: `_tmp_crosscheck_receipts/release10002_bricknames.csv`,
`_tori_r1_workingset_evidence/workingset_bricks.csv`,
`_tori_harvest_20260817/receipts.jsonl` (30,576,156 bytes, parsed line-by-line),
`_tmp_crosscheck_receipts/late_checksum_bricks.json`. My recomputed values vs the verdict:

- replaced_total = 598 (599 lines = header `brickname` + 598 unique data rows). MATCH.
- working set = 60,308 unique bricknames / brickids. MATCH.
- replaced ∩ working set = 397. MATCH.
- 397/397 carry the late pattern: my census of `last_modified` across all 60,308 receipts
  gives the histogram {2022-11: 59,911; 2023-07: 397} and nothing else; the 397 late
  timestamps span 2023-07-26 18:07:01Z – 18:45:24Z, exactly the verdict's
  "26 Jul 2023, 18:07–18:45 UTC" re-hash window. MATCH.
- hazard (replaced ∩ WS with pre-replacement checksum) = 0. MATCH.
- anomaly (late but not RELEASE=10002) = 0. MATCH; the late set is exactly the
  replaced∩WS set, bidirectionally, and lies entirely inside the working set.
- control = 59,911 non-replaced WS bricks, 0 with non-Nov-2022 checksums; control
  timestamps span 2022-11-18 – 2022-11-26, matching the "18–26 Nov 2022 bulk-pass" wording.
  MATCH.
- My late set is byte-identical in membership to the receipted `late_checksum_bricks.json`,
  and every field of the receipted `intersection_result.json` equals my recompute
  (component_verdict PASS). MATCH.
- Side-verification of condition 1: receipts.jsonl = 60,308 lines, all parse, all
  `OK_CONFIRMED`, `image_r_listed` true for all 60,308; `HARVEST_COMPLETE.json` =
  {completed: 60308, total: 60308, utc 2026-08-19T05:10:02Z}. MATCH.
- On-disk content check (receipt 05 claim) independently redone: all 397 late bricks'
  `.sha256sum` files re-hash to the receipts' `sha256_of_checksum_file`, and the same
  seeded (20260819) 400-brick Nov-2022 control sample re-hashes clean — ALL MATCH both sets.
- 49/58 entries split reproduced: late {58: 375, 49: 22}, control {58: 59,407, 49: 504} —
  proportional, uncorrelated with replacement, as disclosed.
- 598-count provenance anchored: `CHECKSUM_FRESHNESS_RESOLVED_20260817.md` names
  "598 bricks replaced in place by DR10.1"; the cross-check obligation is anchored in
  `ACQUISITION_ROUTE_DECISION_20260816.md` (known-issues brick list as the cross-check).

## Check 2 — TAP job provenance: RECEIPTED

- Job URL: `async_job_url.txt` = https://datalab.noirlab.edu/tap/async/ihcjir1h8s4lu7z2,
  identical to the `location:` header in `async_submit_raw.txt` (HTTP/2 303, dated
  Wed, 19 Aug 2026 05:23:15 GMT — the "Submitted 05:23:15Z" of JOB_RECORD.md).
- `poll_log.txt`: EXECUTING from 05:23:39Z continuously to **COMPLETED at 06:43:02Z** —
  the "COMPLETED 06:43:02Z (~80 min)" of JOB_RECORD.md. No ERROR/ABORTED anywhere in the
  547-line log.
- The poll script's 0-byte result save (UWS 303 redirect not followed) is visible in the
  log tail (`RESULT_SAVED 0 lines`) and disclosed in both JOB_RECORD.md and the verdict;
  the final CSV is 5,392 bytes / 598 rows, so the re-fetch with `-L` landed. No bearing.

## Check 3 — PASS conditions vs pre-auth wording: MATCH

Pre-auth condition 2 defines a pass as "no silent pre-replacement-bytes hazard in the
working set", failure or ambiguity => STOP. The verdict's basis is exactly that: hazard set
EMPTY (no replaced working-set brick carries pre-replacement/Nov-2022 checksum evidence —
my recompute: 0), and the control is consistent (59,911/59,911 Nov-2022, 0 exceptions — my
recompute: 0). The verdict's "Consequence" section does not overreach: it explicitly leaves
the transport build and Kun's transport gate to the recorded next steps.

## Check 4 — both query routes recorded with outcomes: YES

- Route A (full-table async TAP, PRIMARY): submitted 05:23:15Z, COMPLETED 06:43:02Z,
  598 bricknames — recorded in JOB_RECORD.md with URL, query text, and the poller defect.
- Route B (working-set-constrained chunked IN-list fallback, per Duho's 15:40 KST
  instruction): recorded as started ~06:45Z and ABANDONED under the whichever-first rule;
  `07_output.txt` is 0 bytes (killed mid-run, no partial output consumed — consistent);
  its calibration receipt `inlist_test.csv` (26-id, 2.4 s) returns both positive controls
  0037m392 and 2393m140, and I confirmed both are present in the 598-row primary list.
- Sync-attempt context (570 s full-DISTINCT timeout, 560 s 30k-window timeout, 32 s 1k
  prune test returning 0037m392) is receipted in 02_output.txt / prune_test.csv /
  brickid_range.csv and summarized in JOB_RECORD.md.

## Check 5 — stops-on-ambiguity clause: NOT NEEDED, confirmed

No ambiguous rows exist to stop on: hazard = 0 and anomaly = 0 in my independent recompute,
so the AMBIGUOUS branch of the PASS logic never triggered and the pre-auth's STOP clause
had no condition to engage.

## Boundary confirmation

`grep -ri nersc _tmp_crosscheck_receipts/` returns nothing; every network touch in the
receipted scripts targets datalab.noirlab.edu only (04_poll.sh reads the job URL from
`async_job_url.txt`, which is datalab). Aggregate/keyspace queries only; zero catalogue
rows, zero image bytes consumed by the cross-check or by this gate. K-8 untripped.

## Disclosed observations (non-blocking)

1. `03_output.txt` captures a failed submit attempt (empty job URL, run-post http=000).
   The successful submission chain is fully receipted out-of-band of that file
   (async_submit_raw.txt 303 @05:23:15Z -> async_job_url.txt -> poll_log EXECUTING from
   05:23:39Z -> COMPLETED 06:43:02Z), so provenance stands; noted for receipt hygiene only.
2. The 0-byte poller save and `-L` re-fetch are already disclosed in the verdict and
   JOB_RECORD.md; verified cosmetic.

## Verdict

All five kickoff checks pass; every number in `CROSSCHECK_VERDICT_20260819.md` reproduces
from the raw receipts under independent recompute. The cross-check PASS stands as
pre-auth condition 2. This gate is findings-only: it does not build the transport, does
not run Kun's transport gate against the frozen successor binding, and does not authorize
any image byte to move — those remain the recorded next steps under
`ACQUISITION_PREAUTH_20260818.md`.

— Miru, 2026-08-19 KST. PASS_CROSSCHECK_GATE.

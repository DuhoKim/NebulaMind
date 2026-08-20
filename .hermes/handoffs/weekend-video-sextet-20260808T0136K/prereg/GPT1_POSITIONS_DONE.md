GPT1_POSITIONS_COMPLETE rows=208407; partition_rows=95380+79272+33755; exported_brickname_overlap=58009/58009; working_set_bricks=60308; missing_from_working_set=0

- Frozen Cut-6 full-keyspace hard cross-check: 832,393 = 832,393 (MATCH).
- Frozen R1 study-parent chain: 674,896,997 -> 338,508,894 -> 338,508,894 -> 2,618,678 -> 238,922 -> 208,407 (all MATCH).
- Fresh async focused study-parent count: 208,407 (MATCH), job `https://datalab.noirlab.edu/tap/async/npohnmsr1kxwiurr`.
- Export columns only: `ls_id, ra, dec, brickname`.
- Export: `_positions_20260820/positions_parent_20260820.csv`.
- Export SHA-256: `90fa6c9687e290ab1190afa54a6b5e0e31824a3ffd05a309ffec0bba464697e9`.
- SHA sidecar: `_positions_20260820/positions_parent_20260820.csv.sha256`.
- Receipt: `_positions_20260820/POSITIONS_RECEIPT_20260820.md`.
- Receipt SHA-256: `7a497c1577c84550a4891dfab31c2f44494be4146b50137884cd600d9ffd882b`.
- Subset proof: all 58,009 distinct exported primary bricknames occur in the frozen 60,308-brick working set; 0 missing; 2,299 working-set bricks are margin-only.
- Two broad fresh aggregate attempts were remotely lost after 199 `EXECUTING` polls each (HTTP 404 UWS-record loss, zero rows retrieved); these are fully logged in the receipt and are not count mismatches. The successful focused count and all three export jobs were polled to `COMPLETED` before retrieval.

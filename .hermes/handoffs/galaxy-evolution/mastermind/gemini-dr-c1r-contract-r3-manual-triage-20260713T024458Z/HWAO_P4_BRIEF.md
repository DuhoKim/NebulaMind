# Hwao P4 brief — final recommendation only

`HWAO_R3_REVIEW.md` approved D1–D6 and P4. Write only `HWAO_FINAL_RECOMMENDATION.md` now. Do **not** write the completion marker yet; Tori will perform final packet-hygiene checks and then relay the last-marker instruction.

Required content:

1. plain-English result of the approved offline work;
2. exact r3 decisions D1–D5 and D6 design-only status;
3. verbatim accepted D3 `FAIL_CLOSED_IMPACT: YES` paragraph from `HWAO_R3_REVIEW.md:20-24`;
4. 73-entry triage result: 47 source fidelity, 18 uncertainty/scope, 8 scientific comparability, 0 contract-r3 change, 0 ignore;
5. explain that zero contract-change entries are correct because r3's D1–D5 crosswalk concerns deterministic findings outside the manual queue;
6. explicitly state this work did not implement a validator, verify sources/science, or arm a live run;
7. recommend an ordered next sequence and name each fresh gate separately:
   - offline validator-r3 implementation/tests;
   - local source/science verification of the routed 73 entries;
   - only after review of those results, a separate live one-simulation canary gate;
8. mention the non-blocking future decision about retaining “Joint C1R answer” in the r3 header;
9. marker `HWAO_R3_TRIAGE_FINAL_RECOMMENDATION_20260713T024458Z`.

No new work, implementation, source retrieval, dashboard, live, browser, git, DB, deploy, cron, account, or secret action.

# LOW_USAGE_KUN_M3_REPAIRED_DETERMINISTIC_CHECK_20260708T083100Z

Markers:
- `LOW_USAGE_KUN_M3_REPAIRED_DETERMINISTIC_CHECK_20260708T083100Z`
- `AUTOPILOT_PROSE_EVIDENCE_TRUST_LOW_USAGE_CONTINUATION_20260708T083100Z`

Lane: Kun/Codex deterministic repaired-M3 validation.  
Verdict: **PASS with one contextual note**.

## Files inspected

- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/page-content-prose-evidence-trust-deepening-20260708T043427Z.md`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/manifest-deepening-20260708T043427Z.json`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3/receipts/TORI_M3_EVIDENCE_TRUST_VISIBLE_REPAIR_RECEIPT_20260708T082710Z.md`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3/autopilot/LOW_USAGE_GORU_M3_REPAIRED_VISIBLE_EVIDENCE_TRUST_AUDIT_20260708T083100Z.md`

## Presence and parse checks

- Repaired M3 HTML present: PASS, 32,884 bytes.
- Repaired M3 Markdown present: PASS, 23,562 bytes.
- Repaired M3 coverage JSON present and parses with `python3 -m json.tool`: PASS, 14,418 bytes.
- Repaired M3 manifest JSON present and parses with `python3 -m json.tool`: PASS, 4,976 bytes.
- Evidence-basis ledger present: PASS, 8,091 bytes.
- HTML article anchor count: 10.
- Markdown `##` heading count: 11.

## Deterministic counts

- Repaired evidence cards in HTML, counted as `data-repaired-evbox="true"`: **9**.
- Evidence-basis links in HTML, counted as `href="../evidence-trust-rebuild/evidence-basis-20260708T014205Z.md`: **19**.
- Anchored evidence-basis links in HTML: `#s1` through `#s9` appear **2 each**, total **18**.
- Unanchored evidence-basis HTML link: **1**.
- Evidence-basis ledger anchors present: `{#s1}` through `{#s9}`: **9/9**.
- `product_claim_comments=0/0` for inspected HTML.
- `product_cite_comments=0/0` for inspected HTML.
- Active HTML safety hits (`<script`, `fetch(`, `XMLHttpRequest`, `WebSocket`, `onclick=`, `onload=`, `onerror=`, `/api/pages`, `page_versions`, external URLs): **0**.

## Trust-label and marker counts

HTML trust/status terms:
- `widely supported`: 4
- `widely_supported`: 2
- `actively debated`: 4
- `actively_debated`: 2
- `emerging_sample_limited`: 1
- `sample-limited`: 2
- `model-dependent`: 11

Markdown trust/status terms:
- `widely supported`: 3
- `actively debated`: 3
- `sample-limited`: 3
- `model-dependent`: 9

JSON trust/status terms across coverage map and manifest:
- `widely_supported`: 2
- `actively_debated`: 2
- `emerging_sample_limited`: 1
- `contradicted_or_model_dependent`: 2

Repair marker `M3_EVIDENCE_TRUST_VISIBLE_REPAIR_20260708T082617Z`:
- HTML: 3
- Markdown: 2
- Coverage JSON: 1
- Manifest JSON: 1
- Tori receipt: 1

PENDING_RECHECK / unmatched visibility:
- HTML `PENDING_RECHECK`: 2; HTML `Unmatched`: 3; HTML `unmatched`: 1.
- Markdown `PENDING_RECHECK`: 2; Markdown `Unmatched`: 3; Markdown `unmatched`: 1.
- Coverage JSON `PENDING_RECHECK`: 2; coverage JSON `unmatched`: 3.
- Manifest JSON `PENDING_RECHECK`: 1.

Specific known-gap tokens in HTML:
- `2915`: 2
- `2921`: 2
- `2913`: 2
- `2133`: 4
- `2374`: 3
- `2605.22497`: 3
- `FINAL_DRAFT_PATCHED_AFTER_GORU_BLOCKER_PENDING_RECHECK`: 1

Specific known-gap tokens in Markdown:
- `2915`: 2
- `2921`: 2
- `2913`: 2
- `2133`: 4
- `2374`: 3
- `2605.22497`: 4
- `FINAL_DRAFT_PATCHED_AFTER_GORU_BLOCKER_PENDING_RECHECK`: 1

## Checksums

- HTML SHA-256: `2b18bb5fd88bc530ce983606335796570e68b56faadc53202b65c960f3b25baf`
- Markdown SHA-256: `aca530768fb07c700b682818f1763844a1e2b85ba8a230232c318e11fe5448d7`
- Coverage JSON SHA-256: `9b422dbbd440cca2f52753ce559fa887c15897a833e0c22f1589a4d4e13031b6`
- Manifest JSON SHA-256: `0b23919f52e6b9ea9f572d1a28522781f3e9f453c893244170c7abf70deae5f0`

## Goru cross-check

Goru report exists at the scoped path. Independent counts match Goru's core claims:
- Goru reported 9 restored evidence cards; Kun counted 9.
- Goru reported 19 evidence-basis links; Kun counted 19.
- Goru reported product claim comments 0 and product cite comments 0; Kun counted 0 and 0.
- Goru reported repair marker in HTML and Markdown; Kun counted HTML 3 and Markdown 2.
- Goru reported PENDING_RECHECK and unmatched-item visibility; Kun confirmed both in HTML and Markdown with exact token counts above.

Contextual note: the inspected Tori receipt says the earlier repair process touched a live-root M3 deepening directory and a live-root backup, while this Kun helper lane did not read or write live root. This report does not validate live-root state because the current lane scope excludes live-root access.

## Hard-excluded surfaces

- This Kun lane touched live root: **No / 0 writes**.
- This Kun lane restarted/deployed/mutated service: **No / 0**.
- This Kun lane called product DB/SQL, `/api/pages`, or `page_versions`: **No / 0**.
- This Kun lane used git commit/push/merge/rebase/reset/checkout/switch: **No / 0**.
- This Kun lane used cloud/GCP/API/billing/OAuth/secrets/browser automation/cron: **No / 0**.
- This Kun lane performed Method3 P3 product claim/citation binding: **No / 0**.

## Final verdict

**PASS** — repaired M3 HTML/JSON/Markdown are present, JSON parses, visible evidence/trust repair counts match Goru's report, product binding comments remain zero, active HTML safety hits remain zero, local evidence-basis anchors resolve, and checksums are recorded.

# Goru M1 Deepening Audit

**Parent Marker:** AUTOPILOT_PROSE_EVIDENCE_TRUST_DEEPENING_20260708T043427Z
**Seed Marker:** DEEPENING_RESOURCE_SEED_20260708T043427Z

## Audit Status: PASS

I have re-run the mechanical audit now that the Kun deterministic generation lane has populated the v2 candidate at:
`…/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/`

### 1. Chip & Evidence Coverage (First-pass vs v2)
*   **Total Chips:** 30 (Preserved identically).
*   **Bound vs Unbound:** 3 bound, 27 unbound (Preserved exactly; unbound chips actively use the honest `· no local evidence / unbound` labels).
*   **Evidence Rows:** 43 rows total (Preserved).
*   **Distinct Papers:** 26 distinct normalized arXiv IDs (Preserved).
*   **arXiv Links:** 43 active `https://arxiv.org/abs/` tags (Preserved; 0 malformed).

### 2. Deepening Wording Verification
*   **2929 Caution Terms:** **PASS**. The v2 candidate injects a clear plain-text caution block: *"Caution: all 14 local rows are stance `none`... Read this box as provenance context for why the claim remains unverified, not as direct support for the prose sentence."*
*   **Distinct-paper vs row-count:** **PASS**. The evidence boxes correctly contextualize the counts (e.g., *"14 rows across 8 distinct normalized arXiv IDs"*).
*   **No-invent Facts:** **PASS**. 0 invented rows, 0 invented claims, 0 external fabrications.

### 3. Safety Boundary & Static Guard
*   **Stale page_versions / API Literals:** **PASS**. 1 literal appearance in the HTML text ("does not touch `page_versions`"), operating perfectly as a limitation disclosure.
*   **Network/Scripts:** 0 `<script>` tags, 0 `fetch` logic, 0 active calls.
*   **Live DB/Cloud Touches:** 0 (Additive candidate directory only).

## Verdict
The v2 deepened candidate has been mechanically verified. It strictly preserves the integrity of the 43 evidence rows and 27 unbound chips while fulfilling the prose/caution enhancements. 

Ready for Lana's no-overclaim review phase. (Final no-apply packet remains deferred per timing rule).

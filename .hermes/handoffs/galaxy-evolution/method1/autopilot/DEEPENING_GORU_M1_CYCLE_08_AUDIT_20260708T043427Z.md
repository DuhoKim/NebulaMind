# Goru M1 Deepening Audit — Cycle 08

**Parent Marker:** AUTOPILOT_PROSE_EVIDENCE_TRUST_DEEPENING_20260708T043427Z
**Seed Marker:** DEEPENING_RESOURCE_SEED_20260708T043427Z

## Audit Status: PASS (With New Branch Candidate Present)

I ran the mechanical read-only scan against the current M1 deepening directory:
`…/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/`

**Note:** The canonical candidate HTML remains identically sized (`38,174 B`). However, a new alternative branch of the candidate files (e.g., `wiki-prose-evidence-trust-deepening-hwao-20260708T043427Z.html` now sizing at `50,978 B`) has populated the directory alongside Hwao's `v2p1` patch note. Since Hwao explicitly chose not to overwrite the canonical candidate files to avoid pane collisions, the baseline metrics below remain mapped to the canonical `38,174 B` HTML build.

### 1. Chip & Evidence Coverage (Canonical Build)
*   **Total Chips:** 30
*   **Bound vs Unbound:** 3 bound claims (2929, 2931, 2946), 27 unbound chips (labeled safely as `no local evidence / unbound`).
*   **Evidence Rows:** 43 total rows preserved.
*   **Distinct Papers:** 26 distinct normalized arXiv IDs.
*   **arXiv Links:** 43 total links. (4 row instances representing 2 distinct papers use the malformed doubled-prefix format `https://arxiv.org/abs/arXiv:...` due to dirty ledger data, as documented in the v2p1 patch note).

### 2. Deepening Wording & No-Invent Guard (Canonical Build)
*   **2929 Caution Terms:** **PASS**. The explicit "Caution: all 14 local rows are stance `none`..." text is present.
*   **Distinct-paper vs row-count:** **PASS**. The evidence boxes correctly differentiate rows from distinct papers.
*   **No-invent Facts:** **PASS**. 0 invented rows, 0 invented claims, 0 external fabrications.

### 3. Static Safety & Boundary Enforcement
*   **Stale page_versions / API Literals:** **PASS**. 1 literal appearance of `page_versions` functioning solely as a safe limitation disclosure.
*   **Network/Scripts:** 0 `<script>` tags, 0 `fetch` logic, 0 active calls across the directory.
*   **Live DB/Cloud Touches:** 0 (Additive candidate directory only).

## Verdict
The canonical candidate remains mechanically verified and static-safe. An alternative `-hwao-` branch continues to actively update in the directory (now at 50,978 B) but correctly avoids colliding with the canonical files. Standing by.

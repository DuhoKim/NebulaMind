# Goru M1 Static Deep Audit Report

**Marker:** GORU_M1_STATIC_DEEP_AUDIT_BRIEF_20260707T104025Z

## 1. Inventory of Method 1 Static Files & Links
Files read or referenced in `index.html` and `quintet.html`:
- `/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html`
- `/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/wiki-page.html`
- `/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/quintet.html`
- `/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/wiki-format-preview-20260707T064500Z.html`
- `/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-same-format-draft-20260707T005045Z.md`
- `pgr-current-page-inventory-20260706T130610Z.html`, `.md`, `.json`
- `p1-legacy-overclaim-disposition-spec.html`
- `p2-2929-route-spec-20260706T144637Z.html`, `.md`, `.json`
- `p3-2572-2573-primacy-wording-spec-20260706T145409Z.html`, `.md`, `.json`
- `p4-trust-level-route-consistency-guard-spec-20260706T150328Z.html`, `.md`, `.json`
- `p5-2931-dedupe-spec-20260706T151025Z.html`, `.md`, `.json`
- Ledger: `SAME_FORMAT_CONFORMANCE_LEDGER_20260707T064500Z.md`

## 2. Heading Structure in Same-Format Preview
- **H1 Count:** 1 (`<h1 id="galaxy-evolution">Galaxy Evolution</h1>`)
- **H2 Count:** 9
- **H3 Count:** 0
- **Is `Contents` an H3 rather than H2?** Neither. It is styled as a div (`<div class="toc-title">Contents</div>`) within the side `<aside>` navigation.
- **Canonical wiki-like structure:** The page uses a canonical wiki-like structure (prose with an aside TOC and no active role-table form) rather than a method-card structure.

## 3. Claim/Evidence Marker Counts
- **Claim IDs 2942–2947:** Only `2946` is present.
- **`cite` / `cite-unmatched`:** 0 instances in the body prose.
- **`claim`:** 30 claims present (e.g., `data-claim-id="2905"`).
- **`evidence` / `Evidence`:** 2 instances as static UI text (`<span class="ghost-button">Evidence</span>` and `<span class="control">Evidence view</span>`), with no live external evidence requests.
- **`Reader`:** 2 instances as static UI text (`<span class="ghost-button">Reader</span>` and `<span class="control active">Reader view</span>`).

## 4. Live Mutation Links Verification
**Status: PASS**
- The `History` and `Sources` buttons in the topbar are static ghost buttons: `<a class="ghost-button" href="#" aria-disabled="true">`.
- There are no edit, commit, or publish links active on the page.

## 5. Comparison Against Existing Conformance Ledger
**Status: PASS (No Mismatches)**
- Ledger states 30 claim markers (IDs 2905–2923, 2925, 2926, 2929–2936, 2946). My count confirms exactly 30 claims with `2946` present.
- Ledger states 9 H2s. My count confirms exactly 9 H2s.
- Ledger states 0 cites. My count confirms 0 cites.

## 6. Verification of Presentation Method
**Status: PASS**
- The files consistently label this as a **Packet-gated paper-to-wiki reconciliation** workspace.
- `index.html` marks the status safely as `DRAFT_PREPARED_STATIC_NOT_PUBLISHED` and warns that it is "not a product DB/wiki publish."

## 7. PASS/WARN/FAIL Summary Table
| Audit Area | Status | Note |
|---|---|---|
| Static Inventory | PASS | All files linked locally with expected nomenclature. |
| Headings | PASS | 1xH1, 9xH2, 0xH3. Canonical wiki format layout used. |
| Claim/Evidence Markers | PASS | 30 claims. Only 2946 present from the 2942-2947 range. 0 cites. |
| Mutation Surface | PASS | No live publish/edit/history links. Controls are `aria-disabled="true"`. |
| Ledger Conformance | PASS | Local counts perfectly match `SAME_FORMAT_CONFORMANCE_LEDGER_20260707T064500Z.md`. |
| Safety & Scope Check | PASS | Clear documentation that this is a static method draft, not a live page. |

GORU_M1_STATIC_DEEP_AUDIT_DONE_20260707T104025Z

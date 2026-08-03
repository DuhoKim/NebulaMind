# Galaxy Evolution — cross-method trust-scale legend (non-comparability)

Marker: AUTOPILOT_PROSE_EVIDENCE_TRUST_DEEPENING_20260708T043427Z
Author: Hwao-director (cross-method synthesis; user-assigned). Derived from the verified method candidates + local ledgers. No invented data.

## Core rule: the three methods do NOT share a trust scale
Three independent methods produced same-topic Galaxy Evolution wiki candidates. Each uses a **different** trust vocabulary derived from a **different** local basis and a **different** granularity. They are **not comparable** and must **not** be combined into a single score or ranked against one another by "trust." Read each method's trust label only within that method's own scale.

## Per-method trust scale — what the labels mean

### Method 1 — packet-gated paper-to-wiki reconciliation
- **Basis:** the local page inventory (`pgr-current-page-inventory-20260706T130610Z.json`) for the baseline page's own claim chips.
- **Scale (per claim, but only where local evidence exists):** for the **3 of 30** chips with local evidence, trust = that claim's recorded inventory status — e.g. **2946 "reported", 2931 "debated", 2929 "unverified"** — plus the arXiv paper rows it links to.
- The other **27 of 30** chips are **`unbound-local`**: their per-claim evidence/trust lives in the product claim/evidence database (a CLOSED gate). **Unbound ≠ low trust and ≠ high trust — it is *unknown here*.**
- So M1 trust is meaningful for only 3 claims; read the page's 30 chips as "3 locally-evidenced, 27 unknown-here."

### Method 2 — source-first paper adjudication
- **Basis:** the RATIFIED S2 source-position ledger (`LANA_SFA_SOURCE_ADJUDICATION_20260707.md`) — 36 evidence rows across 13 arXiv groups.
- **Scale (per *evidence row*, not per claim-final):** **`accepted`** (full strength — only 28141 and 28095), **`accepted_limited`** (qualified; 28 of 36 carry an abstract-only cap), **`rejected`** (12 rows — archival, never cited), **`background_only`/excluded** (e.g. 28133 — no public-sentence use).
- 6 claims (2942–2947) are supported by their accepted/limited rows. **7 `cite-unmatched`** are local source-adjudication rows that do not resolve to product cite IDs (kept honestly unmatched, never invented). **28060** is an `accepted_limited` caution with **no current target claim** (anti-overclaim only).
- M2 has the strongest **local** claim↔evidence binding — but its "accepted" is a per-row source judgment, not a product trust score.

### Method 3 — debate-map-to-wiki rebuild
- **Basis:** the local debate map (`status_debate_map.json` / `debate_map_data.json`).
- **Scale (per *section axis*, not per claim):** **`widely_supported`**, **`emerging_sample_limited`**, **`actively_debated`**, **`contradicted_or_model_dependent`**, and **`scoped-coverage-extension`** (gap sections).
- **Docs-only (P2): 0 product claim/cite markers by design.** This is **not** a product trust score; product claim/citation binding (P3) is a separate CLOSED gate. **`PENDING_RECHECK`** and unmatched items (2915/2921/2913 v1709-only; 2133→2605.22497 missing; 2374 garbled) are shown, not hidden.

## Why you cannot compare them
- **Same words, different meanings:** M1 "debated" = one claim's inventory stance; M3 "actively_debated" = a whole section's axis status; M2 has no "debated" label at all (it has per-evidence-row accept/limit/reject).
- **Different granularity:** claim (M1) vs evidence-row (M2) vs section (M3).
- **Different coverage:** M1 = 30 chips (3 evidenced), M2 = 6 claims (strong local binding), M3 = 0 markers (section framing only).
- **Do not** sum, average, or rank "trust" across methods. Compare methods by *approach fit* (see the index), not by a shared trust number — there is none.

## Honesty limits (all methods)
No invented evidence / IDs / DOI / ADS / trust levels. Unbound / unmatched / PENDING items are labeled, not hidden. All candidates are static (no scripts/fetch/API/DB routes). None is published to the product wiki; the live-root mirror, `:3000` restart, product claim/evidence DB binding (M1's 27 chips), and M3 P3 binding all remain separate CLOSED gates.

AUTOPILOT_PROSE_EVIDENCE_TRUST_DEEPENING_20260708T043427Z

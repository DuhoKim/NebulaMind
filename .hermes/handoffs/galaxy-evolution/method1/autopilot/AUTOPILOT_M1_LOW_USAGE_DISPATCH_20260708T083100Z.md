# Method1 autopilot — low-usage continuation dispatch status

Order marker: AUTOPILOT_PROSE_EVIDENCE_TRUST_LOW_USAGE_CONTINUATION_20260708T083100Z
Continuation-of: AUTOPILOT_PROSE_EVIDENCE_TRUST_DEEPENING_20260708T043427Z (final packet director-finalized)
Continuation marker: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Controller: Method1 Hwao. UTC: 2026-07-08T08:35:03Z · Finalization floor: 10:31:00Z — no final packet before then.

## Task (M1, order §92)
Make the 3/30-evidence-bound vs 27-unbound story reader-visible; verify no row-count/table mismatch; improve trust/evidence card clarity if weak. Benchmark against M3's repaired reader-visible standard (visible evidence/trust cards, clear limits, followable links, 0 product binding).

## Finding on inspection (read-only) — M1 already meets the bar
The durable M1 `-hwao` v2.2 candidate already exposes a reader-visible evidence/trust layer:
- **3 evidence cards** (one per bound claim 2946/2931/2929), each with an evidence table (43 rows total), trust label, distinct-paper counts, and a caution line.
- **27-unbound disclaimer** section + pills; **per-section trust rollup** (2 of 9 sections evidenced); on-page trust vocabulary.
- Links: 3 local ledger links + 3 chip→evidence anchors + 43 arXiv refs; **0 product-binding markers**; static-safe.
M1's 3 cards (vs M3's 9) reflect the real 3/30 binding, not a deficiency — trust scales/counts are not comparable across methods.

## Lanes dispatched (low-usage first)
- **Goru/Gemini (mechanical):** evidence-card + unbound-disclaimer counts, row/table consistency, link-target checks, static-safety, no-invent, product-binding=0 → `autopilot/GORU_M1_LOW_USAGE_AUDIT_20260708T083100Z.md`.
- **Kun/Codex (deterministic):** HTML/JSON validity, relative-link audit, table/card reproducibility → `autopilot/KUN_M1_LOW_USAGE_VALIDITY_20260708T083100Z.md`.
- **Hwao:** verdict — meets bar / no repair needed → `HWAO_M1_LOW_USAGE_VERDICT_20260708T083100Z.md`.
No new static repair candidate expected (M1 already visible); if Goru/Kun surface a real reader-facing gap, repair under `prose-evidence-trust-low-usage-continuation-20260708T083100Z/`.

## Gates closed
live-root write · :3000 restart · DB/SQL · /api/pages · page_versions/publish · deploy · git · cockpit/global/shared-parent · cloud/OAuth/secrets · browser · cron · M3 P3.

Status: **DISPATCHED** — low-usage M1 audit.

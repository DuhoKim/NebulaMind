# Method2 low-usage continuation — Goru + Kun reader-visible evidence/trust audit

Marker: AUTOPILOT_PROSE_EVIDENCE_TRUST_LOW_USAGE_CONTINUATION_20260708T083100Z
Role: Method2 Goru (counts) + Kun (deterministic totals) — read-only. UTC: 2026-07-08T08:35:17Z
Audited artifact (primary M2 candidate): `…/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html` (+ its coverage map + manifest)

## Overall: PASS — M2 meets the reader-visible evidence/trust standard (evidence cards + clear limits + followable local links).

## Goru — reader-visible counts
| item | count |
|---|---|
| evidence cards (per-claim + caution `evbox`) | 7 |
| evidence rows shown to reader (`evrow`) | 24 (22 support + 2 held-out shown in-claim) |
| claim sections | 7 (6 claims 2942–2947 + the 28060 caution) |
| trust tags rendered | ACCEPTED (legend+rows), ACCEPTED-LIMITED (21 rows), EXCLUDED (2 held-out rows) |

Visible reader caveats:
- 28060 no-target caution card — **VISIBLE** (its own section: "AGN feedback is not always negative").
- 22-vs-21 count note ("why 22 cited but the boxes sum to 21") — **VISIBLE**.
- cite-unmatched explainer ("what cite-unmatched means") — **VISIBLE** (≥3 mentions).
- Held-out (2 excluded + 12 rejected) panel — **VISIBLE**.
- Trust legend + non-comparability ("not the same scale Method 1 or Method 3 uses") — **VISIBLE** (an automated raw-substring scan flagged it only because inline `<b>not</b>` tags split the phrase; the rendered legend clearly states it).
- Conclusion & limitations — **VISIBLE**.

Links + safety: 26 relative links, **0 broken, 0 external**; static-safety **CLEAN** (0 script/fetch/XHR/WebSocket/`/api/pages`/`page_versions`).

## Kun — deterministic totals + manifest attest
Coverage map totals: **2 accepted · 20 accepted-limited · 22 cited positions · 21 per-claim-box sum · 2 excluded · 12 rejected · 7 cite-unmatched groups · 0 product cites.**
Independent recount from the map arrays: excluded **2**, rejected **12**, claim-attached support **21**, +28060 (no target) = **22** total. Internally consistent (2 accepted + 20 accepted-limited = 22; 21 claim-attached + 1 no-claim caveat = 22).
Manifest lists **4** files; **product binding count = 0** (all evidence is cite-unmatched by design — no invented product cites).

## Per §M2 asks — status
- accepted/limited/rejected/excluded trust clarity: PASS (visibly distinguished; counts above).
- 28060 + 22-vs-21 totals note obvious: PASS (dedicated card + dedicated note box).
- cite-unmatched groups stay visible: PASS (7 groups + explainer).
- deterministic totals + manifests verified: PASS (recount matches; manifest consistent).

## Remaining gaps (reader-facing): none blocking.
The M2 candidate already exceeds the M3-repaired minimum (visible evidence/trust cards, clear limits, followable local links). No repair/patch needed; no prose churn performed (avoids filler).

## Safety ledger
Read-only audit + this report write only. 0 live-root · 0 restart · 0 DB/SQL · 0 /api/pages · 0 page_versions · 0 publish · 0 git · 0 cockpit/global · 0 cloud/OAuth · 0 browser · 0 cron.

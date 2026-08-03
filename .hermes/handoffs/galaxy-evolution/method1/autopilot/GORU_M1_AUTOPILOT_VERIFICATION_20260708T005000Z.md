# Goru — Method1 autopilot mechanical verification

Order marker: AUTOPILOT_COMPLETE_WIKI_PAGES_CONTINUATION_20260708T005000Z
Continuation marker: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Lane: Method1 Goru (mechanical). Mode: read-only. Authored UTC: 2026-07-08T01:03:01Z
Canonical contract: `frontend/src/app/wiki/[slug]/WikiPageClient.tsx` + same-format rebuild packet `HWAO_SAME_FORMAT_REBUILD_PACKET_20260707T064500Z` §2A/§2B.

## A. Method1 static wiki-page artifacts — file inventory + fingerprint
| File | Path | Bytes | sha256[:12] | Exists |
|------|------|------:|-------------|:------:|
| content | `…/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/page-content-20260707T064500Z.md` | 14,486 | `3e108589bcd7` | ✅ |
| preview | `…/packet-gated-paper-to-wiki-reconciliation/same-format-rebuild/wiki-format-preview-20260707T064500Z.html` | 24,033 | `425a4335a9db` | ✅ |
| preserved old page | `…/packet-gated-paper-to-wiki-reconciliation/wiki-page.html` | 29,063 | (report-style, preserved not overwritten) | ✅ |

## B. Method1 content contract (§2A) — mechanical checks
| Check | Result | Status |
|-------|--------|:------:|
| Leading `# Galaxy Evolution` (client-stripped) | present | PASS |
| H2 count | 9 | PASS |
| H2 exact binding order | matches | PASS |
| Claim markers open == close | 30 == 30 | PASS |
| Claim ID set == {2905–2923,2925,2926,2929–2936,2946} | exact (n=30, 0 missing/extra) | PASS |
| NO-GO chips (2298/2299/2924/2948) present | none | PASS |
| `<!--cite:-->` count | 0 (expected 0) | PASS |
| `<!--cite-unmatched:-->` count | 0 | PASS |
| Raw HTML tags in prose | 0 | PASS |
| HTML entities in prose | 0 | PASS |
| `[n]` reference tokens | 0 | PASS |
| References/Bibliography footer | none | PASS |
| hero_facts / hero_tagline | none | PASS |

## C. Method1 preview shell (§2B) — presence checks
grid `Y` · TOC rail `Y` · header h1 `Y` · provenance chip `Y` · trust placeholder `Y` · Reader control `Y` · Evidence control `Y` · disabled (History/Sources `aria-disabled`) `Y` · method-label chrome `Y` · hero OFF `Y` · order/packet marker present `Y`.

## D. Static-safety string scan (no hard-gate action in artifacts)
Scanned content + preview for active-mutation strings: `INSERT INTO`, `UPDATE…SET`, `/api/pages`, `page_versions`, `fetch(`, `XMLHttpRequest`, `git commit`, `gcloud`, `OAuth`, `process.env`. **Result: NONE found.** Artifacts are inert static docs.

## E. Cross-method completeness matrix (read-only corroboration for the roll-up)
Content-contract facts observed read-only; each method's own Hwao verdict is the governing authority for its lane.
| Method | content bytes/sha | H2/order | claim open==close | claim IDs | cite / cite-unmatched | prose clean | hero off | forbidden active | governing verdict |
|--------|-------------------|:--------:|:-----------------:|-----------|:---------------------:|:-----------:|:--------:|:----------------:|-------------------|
| **M1** packet-gated | 14,486 / `3e108589bcd7` | 9 / ✓ | 30==30 | {2905–2923,2925,2926,2929–2936,2946} exact | 0 / 0 | ✓ | ✓ | NONE | `HWAO_SAME_FORMAT_REBUILD_VERDICT_20260707T064500Z` (PASS) + this cycle |
| **M2** source-first | 13,049 / `74be783159be` | 9 / ✓ | 6==6 | {2942–2947} exact | 0 / **7 cite-unmatched** (28xxx unresolved → correct path, no invented IDs) | ✓ | ✓ | NONE | `method2/HWAO_SAME_FORMAT_REPAIR_VERDICT_20260707T074231Z` |
| **M3** debate-map | 14,753 / `39bdd26ad083` | 9 / ✓ | 0==0 (docs-only P2 scope) | none (correct) | 0 / 0 | ✓ (comment states "no hero_facts/hero_tagline") | ✓ | NONE | `method3/HWAO_SAME_FORMAT_REPAIR_VERDICT_20260707T074231Z` + `HWAO_M3_P2_WIKI_PAGE_VERDICT_RERUN_20260707T050900Z` |

**Preview shells (read-only):** all three carry grid + TOC + header + provenance + trust + Reader/Evidence controls and the packet marker; none contains forbidden active strings; none has hero fields. Shell-chrome string variants (M2 History/Sources disabled-attr, M2/M3 method-label class naming) differ by markup between lanes and are deferred to each method's own verdict — not a M1-authority call.

## Verdict (Goru mechanical)
- **M1: PASS** — all §2A/§2B mechanical checks green; artifacts inert/static; fingerprints recorded.
- **M2/M3: read-only corroboration = complete** on the core content contract (H2, claim pairing, marker profile, cite-unmatched handling, clean prose, no forbidden action); final conformance owned by their own lane verdicts.

Every M1 check PASS; 0 WARN; 0 FAIL. No mutations performed.

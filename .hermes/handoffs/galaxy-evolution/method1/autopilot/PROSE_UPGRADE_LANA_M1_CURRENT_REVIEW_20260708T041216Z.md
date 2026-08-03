# Lana — Method1 prose/evidence/trust upgrade review (current on-disk candidate)

Parent marker: `AUTOPILOT_PROSE_EVIDENCE_TRUST_WIKI_UPGRADE_20260708T041216Z`
Role/lane: Method1 Lana — prose / no-overclaim / trust-communication review. Read-only inspection + this `.hermes` report only. No candidate edits.

## Files reviewed (current, single coherent build)
All four share mtime **2026-07-08 13:18:47 (local)**, same build:
- `…/prose-evidence-trust-upgrade/page-content-prose-evidence-trust-upgrade-20260708T041216Z.md` (21,663 B)
- `…/prose-evidence-trust-upgrade/wiki-prose-evidence-trust-upgrade-20260708T041216Z.html` (36,920 B)
- `…/prose-evidence-trust-upgrade/evidence-trust-coverage-map-20260708T041216Z.json` (5,064 B)
- `…/prose-evidence-trust-upgrade/manifest-20260708T041216Z.json` (1,599 B)

**Staleness note:** this is a *new* `prose-evidence-trust-upgrade/` candidate, built (per manifest `inputs`) from `evidence-trust-rebuild/evidence-trust-preview-p1-label-fix-20260708T022147Z.html`. It supersedes the earlier `evidence-trust-rebuild/` preview I reviewed in `RESOURCE_SURGE_LANA_M1_UX_REVIEW_20260708T022147Z.md`; that prior report and any receipts against the `evidence-trust-rebuild/` preview may now be **stale**. Judgment below is on the current files.

## Verdict: **PASS (prose/no-overclaim)** — my two P1 blockers are resolved; residual items are P2/P3 polish
The candidate is honest, no-overclaim, and materially clearer than the prior version. From a prose/science-review standpoint it is acceptable to advance. Two small residuals (2929 caution, format-grammar clarification) are recommended, not blocking.

## Requested-check scorecard
| Check | Verdict | Basis |
|---|:---:|---|
| Prose richness | **PASS** | Article body is the well-hedged synthesis prose verbatim from the same-format page.content; a clear intro framing paragraph was added. No new overclaim introduced; legacy overclaims 2298/2299/2924 remain correctly absent. |
| 3/30 bound honesty | **PASS** | Coverage map + prose both state 3/30 (2931/2929/2946), 27 unbound, 43 rows (20+14+9). Cross-checked verbatim against the bindings ledger: trust levels debated/unverified/reported, scores +0.34/−0.14/+0.45, stances all match. |
| 27 unbound label-fix wording | **PASS (my prior P1 #1 & #2 resolved)** | Badge changed from the misleading `· provenance` to `· no local evidence / unbound`, plus an explicit sentence: *"`No local evidence / unbound` is not a trust score and must not be read as high trust."* This directly closes the trust-inversion finding. Verified 27/27 unbound chips carry the new label; 0 use "provenance". |
| Per-claim evidence boxes 2929/2931/2946 | **PASS** | All three present with full tables (id/paper/year/stance/votes). Row counts match headlines exactly: 2931=20, 2929=14, 2946=9. Each box carries a scope note ("local Method1 binding only; no product DB/API recompute or invented IDs"). |
| Trust vocabulary | **PASS** | Deliberately narrow — debated/unverified/reported + the explicit non-trust "no local evidence / unbound", each defined in the intro and in `coverage_map.trust_vocabulary`. Honest, non-inflating. |
| 2929 non-committal caution | **WARN (P2, partially addressed)** | See below. |
| No invented evidence/trust | **PASS** | 0 `<!--cite:-->`, 0 `<!--claim:-->` residue; all evidence IDs/URLs/stances/scores verbatim from ledger; manifest `safety` all-zero. Independent recount matches. |

## Residual findings

**Finding A — 2929 caution present but under-weight (P2).** The 2929 box shows stance mix `none: 14` and the vocabulary defines `unverified` as "none-stance/archive/caution," which is honest signal. But there is no plain-English caution *in the 2929 box itself* that the rows are low-relevance: **4 of the 14 rows are "A large, long-lived, slowly-expanding superbubble across the Perseus Arm"** — a Milky-Way ISM paper, off-topic to the AGN sign/strength claim — and **0 of 14 rows take a supporting stance** (≈8 distinct papers across 14 rows). Meanwhile the inline chip still reads `[2929 · unverified · 14 evidence]`, which on scan reads as "14 supporting." Recommend one caution sentence in the 2929 box, e.g. *"These 14 rows are archival/none-stance and several (the Perseus-Arm superbubble papers) are low-relevance to this AGN claim; `unverified` here is not a support signal."* This is the same off-topic-citation pattern I flagged at T3 (inventory seq 1–5). Honest as-is, but a reader could over-read the count.

**Finding B — file is a static-preview representation, not drop-in page.content (flag for Goru/Kun; format, not prose).** The canonical marker grammar `<!--claim:ID-->…<!--/claim:ID-->` has been **fully replaced** by visible bracket tags `[NNNN · … ]` (verified: 0 `<!--claim:-->`, 30 bracket chips). For a static preview this is fine and actually *improves* label legibility. But if this `.md` were ever fed to the live `WikiPageClient` as `page.content`, the brackets would render as literal text and no chips would render via the product path. So this artifact must be treated as a preview surface, not as mirror-ready `page.content`. Not a prose/overclaim defect — flagging so no downstream lane mistakes it for canonical content.

**Finding C — duplicate rows still inflate headline counts (P3, minor).** "20 / 14 evidence" count duplicate paper rows (2931 ≈ fewer distinct papers than 20; 2929 = 14 rows / ~8 distinct). My prior Finding-4 (show distinct-paper count) is not yet applied. Low priority.

**Finding D — malformed arxiv identifiers persist in the ledger data (P3, minor).** e.g. `arXiv:arXiv:0901.1880`, `arXiv:arXiv:1712.04452`. In this `.md` they appear as title text (not clickable), so low reader-harm here; the sibling HTML may still hyperlink them. Defer to a normalization pass; do not substitute different IDs.

## Answer to the review question
- **Honest?** Yes — 3/30 bound + 27 unbound is truthful, verbatim from the local ledger, with the unbound state now correctly labeled as *not* a trust signal. No invention.
- **No-overclaim?** Yes for the article prose (well-hedged, legacy overclaims absent) and for the trust labels. The one soft spot is the 2929 evidence box, where a short relevance caution would prevent over-reading "14 evidence" (P2, recommended not blocking).
- **Net vs prior review:** the two P1 blockers (misleading "provenance" label; bound-looks-weaker-than-unbound) are **resolved**.

## Safety ledger
- Reads: current candidate files + `.hermes` reports only. Writes: this one report.
- live wiki 0 · page_versions 0 · DB/SQL 0 · /api/pages 0 · live-root/product write 0 · candidate edits 0 · deploy/restart 0 · git 0 · browser 0 · cloud/OAuth/secrets 0 · cron 0.
- No hard gate encountered; nothing prompted. `NO ACTIVE EXECUTION PHRASE`.

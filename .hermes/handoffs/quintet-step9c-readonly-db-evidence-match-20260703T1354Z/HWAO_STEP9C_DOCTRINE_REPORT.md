# Hwao/Fable Doctrine Report — Step 9C read-only DB evidence match

Task: HWAO STEP 9C adversarial doctrine review · Status: COMPLETE — read-only except this report; no DB/API mutations; no apply/rollback/migration scripts executed; no credentials or connection strings printed or read.
Verified directly: DB summary, all 26 match rows (field-level), Peng duplicate summary, GO/NO-GO (raw rows), safety ledger, validation facts.

## Verdict: `PASS_WITH_PATCHES` — one substantive patch protecting the insert-heavy conclusion, two one-liners.

## Facts checked (brief checklist) — all confirmed

- `transaction_read_only=on` + rolled back (GO row; `db_query_mode: BEGIN READ ONLY + ROLLBACK`); DB writes/SQL/API mutations all 0.
- Evidence rows scanned = **11,817**; Step 9 sources = **26**; existing-match source count = **1** (source 14, `2015Natur.521..192P`).
- Accepted existing rows = **6640–6655** (16 rows), with **6651** the Galaxy Evolution page-citation-linked row — and correctly *not* execution-approved (canonical-row NO-GO held).
- Insert candidates = **25** (sources 1–13, 15–26); insert-heavy **remains confirmed** after DB-level matching (96.2%, far past the one-third rule).
- ADS enrichment returned **401**, handled gracefully: no token printed (`ads_token_printed: false`), and matching proceeded on local identifiers — all 26 sources carried arXiv IDs from the corpus scope-check artifact plus bibcodes.
- Step 9B claim gates remain locked (dedicated NO-GO row); apply permission NO-GO; rollback-backup NO-GO. Six NO-GOs total — **no Step 10 unlock risk found anywhere**.

## Attack results

**1. The insert-heavy conclusion — sound in structure, one robustness gap (Patch 1).** The conclusion "25/26 need inserts" is only as strong as the identifier matching that produced it, and the failure mode is *under-matching*: existing rows missed because of identifier format drift, inflating the insert count. This is not hypothetical in this DB — earlier packets documented variant arXiv ID formats coexisting (`2512.16208v1` with version suffix; `oai:arXiv.org:2606.…` prefixed feed IDs; bare IDs). The packet records *which identifiers were used* (local arXiv IDs + bibcodes) but not *which DB fields were compared under what normalization*. **Patch 1:** add a short attestation to the DB summary — exact fields matched (`evidence.arxiv_id`, `evidence.ads_bibcode`, `evidence.doi`) and normalization applied (strip `v\d+$` suffixes, strip `oai:arXiv.org:` prefixes, case/whitespace fold) — and if the executed match was *not* normalization-tolerant, re-run the read-only match once with normalization before the "25 insert candidates" figure is published as final. Cheap either way, and it makes the packet's central number robust.

**2. The canonical evidence-row assumption — already refused by the packet; confirmed correct.** The Peng paper exists as **sixteen separate evidence rows attached to sixteen different claims** (938–947, 1237–1242 — the older Milky Way/Galaxy Formation era), and the packet's caveat is exactly right: "global exact paper existence does not by itself authorize reuse as a claim-compatible citation," with a dedicated NO-GO for canonical-row selection/dedup/claim-compatibility review. No assumption leaked. Two consequences worth recording (**Patch 2**, one line each): (a) the future insert packet must operate under an anti-row-17 rule — any source already present in the DB is *reused/canonicalized, never re-inserted*; (b) the 16-row cluster is a live instance of the corpus-wide duplicate-evidence pattern (every historical attach minted a new row; there is no evidence-entity dedup) — route "evidence entity dedup" to the standing backlog so this packet's discovery isn't lost.

**3. ADS failure handling — graceful and honest.** The 401 neither blocked the work (local identifiers covered all 26) nor leaked anything (`credentials_printed: false`). **Patch 3 (one line):** queue an ops card that the ADS token is invalid/expired — future enrichment passes will want it; fixing it is outside this packet's scope.

**4. No evidence-hunting — confirmed.** The packet resolves identifiers for the *existing* 26 ledger sources only: no new sources introduced, no stances touched, no claim texts revisited, no snippet re-interpretation. The one match found (Peng) was already the one publicly-resolved source from 9B — the DB pass *confirmed* the public result rather than manufacturing new support. This is evidence-ID resolution in its pure form; the claim-rescue tripwire stays untripped.

## Answers

1. Overclaim risks: insert-heavy conclusion structurally sound, robustness patch required (P1); canonical-row assumption explicitly refused; ADS failure handled; zero Step 10 unlock paths (six NO-GOs verified).
2. No evidence-hunting occurred — resolution only, confirmed at artifact level.
3. Patch before public completion: **yes — P1** (normalization attestation or one normalization-tolerant re-run); P2/P3 are one-line additions.
4. Verdict: **PASS_WITH_PATCHES.** With P1–P3 applied, Step 9C may be published as complete (read-only, PACKET_ONLY), leaving the apply path exactly as gated: canonical-row review, insert-heavy operator decision, claim-workflow approvals, DB rollback backup, and apply permission — all NO-GO, all correctly so.

## Safety ledger (this review)

DB writes 0 · SQL mutations 0 · API mutations 0 · apply/rollback/migration scripts executed 0 · deploy/restart 0 · product publish 0 · git 0 · credentials printed 0 · files written 1 (this report).

HWAO_STEP9C_DOCTRINE_REPORT_DONE

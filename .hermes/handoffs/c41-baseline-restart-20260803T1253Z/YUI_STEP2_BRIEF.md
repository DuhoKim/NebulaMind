# YUI BRIEF — C41 Step 2: fulltext acquisition + source-strength labels

Lane: `c41-baseline-restart-20260803T1253Z` (write ONLY here + the engine fulltext cache; temps `_tmp_*` here).
Gate: Duho — "APPROVE C41 STEP 2". Precondition satisfied when PR #133 is merged (your primary
tool `tools/nm_fulltext_layer.py` must be tracked on main before you run — Hwao confirms at dispatch).
You are Yui (Hermes seat on this Studio host — the repo, `_ROOT`, and `backend/.env` ADS token are
local to you). Fallback lane if you are unavailable: Tori.

## Input (sealed — do not modify)

`SELECTION_INCLUDED.json` — the 180 sealed records (sha in `SELECTION_SHAS.txt`; Kun verdict
SEALED_WITH_PATCHES). Fetch fulltext for EXACTLY these 180. The LRD-boundary recall limit (Kun F2)
is a known property: you do NOT re-admit anything; if you notice an excluded paper you think the
map needs, note it in your report as a re-admission CANDIDATE for a later gated decision.

## Method

1. Use `tools/nm_fulltext_layer.py` as a library from a lane-local driver `step2_fetch.py` you
   write (stdlib + the module; no new deps). Relevant functions: `fetch_pdf(arxiv_id)`,
   `extract_text`, `extract_html_structured`, `chunk_text`; the module reads the ADS token itself —
   NEVER print or log the token or any `.env` content.
2. **Cache-first**: the engine `fulltext_cache/` has ~25k prior entries — check it before any
   network fetch; write new fetches into it in the same format you find there.
3. **Politeness**: ≥3 s between arXiv requests, exponential backoff on 429/5xx (the ingest lane's
   429 history is in the engine receipts — arXiv throttles hard), hard stop after 3 consecutive
   failures with the blocker written to your report. Prefer arXiv HTML/PDF for records with arXiv
   ids; ADS for bibcode-only records.
4. **Source-strength labels** per the claim-ledger contract v1 vocabulary
   (`docs/claim_ledger_contract_v1_agn_20260703T0830Z/artifacts/ledger_enums.json`):
   per record, label `source_access` honestly (`full_text` / `abstract_only` / etc. exactly as the
   enum defines) plus source class (review flag is already in the selection record). No fetched
   text → `abstract_only` with the failure reason; never fake access.

## Deliverables (lane dir)

1. `STEP2_FULLTEXT_MANIFEST.json` — per record: identity, cache path, access label, byte count,
   fetch outcome (cached/fetched/failed+reason), extraction outcome; plus a summary block
   (counts per access label, cache-hit rate, total new fetches) and an input-manifest block
   sha-pinning `SELECTION_INCLUDED.json` and the module file.
2. `STEP2_STRENGTH_LABELS.json` — record → {source_access, source_class, review_flag}.
3. `step2_fetch.py` — your driver.
4. `YUI_STEP2_REPORT.md` — counts, runtime, failures with reasons, re-admission candidates if any,
   safety-boundary statement. End with marker: `YUI_STEP2_COMPLETE_20260804`.

## Hard constraints

Writes: this lane dir + engine `fulltext_cache/` only. No DB, no git writes, no product surfaces,
no DR/credits, no `.env` content in any output. Network: arXiv + ADS APIs only, polite as above.
Do not read the C41 map lanes-in-progress or the f_esc sweep dir. If `SELECTION_INCLUDED.json`'s
sha does not match `SELECTION_SHAS.txt`, STOP — the seal is broken; report and wait.

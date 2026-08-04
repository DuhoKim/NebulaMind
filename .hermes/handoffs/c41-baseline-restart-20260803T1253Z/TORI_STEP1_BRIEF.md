# TORI BRIEF — C41 Step 1: corpus protocol + executable selection

Lane: `c41-baseline-restart-20260803T1253Z` (write ONLY here; temps `_tmp_*` here).
Gate: Duho 2026-08-03 ~22:05 KST — "APPROVE C41 STEP 1". Coordinator: Hwao.
You are Tori (Hermes seat). Kun will adversarially refute your output afterward, including a
decoy test — author accordingly.

## Frozen inputs (read-only; verify shas before relying)

- Question: `STEP0_FROZEN_QUESTION.md` (sha256 `9ac5ca1f6321e2808eec3b9c2d38b8e616e0a9d774f4f277469c38fadbf789e1`, chmod 444). Your protocol serves THIS question and its scope rules (note the LRD boundary rule).
- Plan §Track A Step 1: `.hermes/plans/2026-08-04_0040-c41-jwst-highz-baseline-restart.md` (yes, the filename date is a recorded clock-drift error).
- Engine dir `E = .hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718/`:
  - Base membership: `E/cluster_labels_v2.json` — dict bibcode→cluster, 120,676 entries; C41 = value 41 (~1,296 papers).
  - Base metadata: `E/corpus_ga_co_2009_2026.jsonl` (420 MB — stream it, never load whole).
  - Delta members: `E/delta/new_labels.json` (arxiv_id→cluster; 21 in C41) + `E/delta/new_papers.jsonl` (metadata).
  - Contested-measurement signal: `E/dispersion_v2.json` + lexicon in `tools/nm_dispersion_v2.py`; strict-tension terms in `E/rank_frontiers_v3.py` (STRICT_TERMS).

## The anti-cherry-picking contract (Kun F7 — your protocol is refuted against this)

1. **Rules before titles.** Author the selection rules from metadata CLASSES (year, citation count,
   source type, lexicon hits, cluster membership) BEFORE reading any candidate titles. You may
   inspect field schemas and AGGREGATE distributions (counts, histograms) freely. If you must look
   at any individual paper to design a rule, declare each instance in the protocol ("peek log").
2. **Executable filter.** Express the rules as `step1_filter.py` in the lane dir: deterministic,
   reads only the files above, emits the included and excluded sets. No randomness without a fixed
   seed; no manual list edits afterward.
3. **Excluded list published.** `SELECTION_EXCLUDED.json` groups exclusions by RULE CLASS with
   per-class counts and the rule text. Nothing is excluded without a named rule.
4. **Ceiling 180 included.** Ordering: contested-measurement-first, recency-weighted, review-aware
   (reviews flagged as their own source class, capped so they don't crowd out primary claims).
   The shrink ladder (60/30) lives downstream — your job is an honest ranked 180, not a padded one.

## Deliverables (all in the lane dir)

1. `STEP1_CORPUS_PROTOCOL.md` — the rules, their rationale tied to the frozen question's three
   axes, the LRD boundary rule as a filter clause, the review-class cap, the peek log (ideally
   empty), and the model-prediction-source note (model papers OUTSIDE C41 are NOT corpus members;
   they enter at Step 4 as ledger'd prediction sources — state the identification rule sketch).
2. `step1_filter.py` — the executable filter (stdlib only; stream the big jsonl).
3. `SELECTION_INCLUDED.json` + `SELECTION_EXCLUDED.json` — its outputs, plus
   `SELECTION_SHAS.txt` (one `shasum -a 256` line per file, one file per line).
4. `TORI_STEP1_REPORT.md` — what you did, counts per rule class, runtime, anomalies; end with
   marker `TORI_STEP1_COMPLETE_20260803`.

## Hard constraints

Read-only outside the lane dir. No network. No git commands that write. No DB. No model calls
beyond your own reasoning (no DR, no /credits). If a needed input is missing or malformed, STOP
and write the blocker into your report rather than improvising around it.

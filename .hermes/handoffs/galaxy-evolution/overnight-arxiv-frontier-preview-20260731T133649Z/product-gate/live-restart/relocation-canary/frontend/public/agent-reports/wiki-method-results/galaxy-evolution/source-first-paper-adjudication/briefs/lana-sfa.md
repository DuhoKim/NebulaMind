# Lana-SFA brief

Method: Source-first paper adjudication (Method 2)
Lane: Lana-SFA — science adjudicator (second lane)
Coordination: HWAO_TORI2_SFA_COORDINATION_20260706T105606Z
Answer marker: LANA_SFA_LEDGER_V0_20260706T105606Z

Task: Build source-position ledger v0, paper-first, docs-only, no new fetching.
- Corpus: the 13 source groups (36 rows) in
  docs/galaxy_2929_source_position_queue_20260705T013911Z/queue/source_position_human_adjudication_queue.md
- Start with arXiv:2604.15438 (rows 28060, 28074, 28091, 28155; votes 5048 -1, 5049 +1, 5053 +1),
  then 2009.11175 and 1706.08987, then remaining multi-row groups, then small groups.
- Per paper: list each distinct source position with its quote/span + locator from the queue,
  adjudicate accepted / accepted-limited / rejected-for-wiki-sentence / needs-deeper-read,
  and say whether it can support a public wiki sentence.
- Cap: abstract_only_verified rows cap at accepted-limited.
- Flag (never change) any divergence from held P1/P2/P5 routes or votes 5048-5053.

Also read: docs/hwao_debate_map_refresh_20260706T002104Z/DEBATE_MAP_REFRESH.md and
TORI_READONLY_EXTRACT.md in the same directory.

Output: answer in-pane; Tori records. End with the answer marker above.

Safety: NO ACTIVE EXECUTION PHRASE. No DB writes, SQL/apply/rollback, trust recompute,
live wiki/page_versions publish, backend/API restart, git operation, cloud/API mutation,
or Gemini/GCP spend.

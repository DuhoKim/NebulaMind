# GORU BRIEF — wave2 mechanical pin ledger — 20260705T1615Z

Coordinator: Hwao. Tori relays/verifies.

Read:
- Hwao direction: `.hermes/handoffs/overnight_autonomy_20260705T1615Z/HWAO_CONTINUE_OVERNIGHT_DIRECTION.md`
- Target rows: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/WAVE2_TARGETS.md` / `.json`
- Fetch manifest: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/FETCH_MANIFEST.json`
- Lana adequacy gate: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/LANA_WAVE2_ADEQUACY.md`
- Hwao spec summary: `docs/hwao_overnight_db_packet_prep_20260705T1615Z/DB_PACKET_PREP_SUMMARY.md`
- Source texts: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/source_text/*_pdf_text.txt`

Task:
Build the mechanical wave-2 pin ledger from the Lana-approved rows. Write exactly:
1. `docs/hwao_overnight_pinning_wave2_20260705T1615Z/PINS_WAVE2.jsonl`
2. `docs/hwao_overnight_pinning_wave2_20260705T1615Z/GORU_WAVE2_COUNTS.md`

Rules:
- One JSONL row per pin actually proposed for docs/source-position custody.
- Required fields per row: `pin_id`, `evidence_id`, `claim_id`, `source_id`, `source_text_path`, `source_text_sha256`, `quote`, `char_start`, `char_end`, `line_start`, `line_end`, `recorded_stance`, `pin_role`, `adequacy_decision`, `limitation_note`, `safety_note`.
- Use exact source text offsets by locating the quote/span in the `_pdf_text.txt` files. If exact long quote text from Lana includes ellipses, choose the smallest exact contiguous span from the source that supports the same point and record it verbatim.
- Hwao Track-B spec adds a binding duplicate rule: for claim 2931 + `1308.5224v1`, pin only the canonical evidence row `28099`. Do not pin duplicate rows `28154` or `28161`; record them as duplicate-held in `GORU_WAVE2_COUNTS.md`.
- Preserve roles exactly:
  - 28099 / 1308.5224v1: `neutral_context`
  - 28132 / 2605.31052v1: `neutral_context`, limitation: secondary/narrower AGN simulation lens
  - 26088 / 2512.16290v1: `refutes`, limitation: refutes primacy/dominance interpretation, not bare correlation
  - 28155 / 2604.15438: `supports`, scoping qualifier
  - 26089 / 2401.12953: `neutral_context`
- Claim 2929 parent_replaced rows must not appear in `PINS_WAVE2.jsonl`.

Counts report must reconcile:
- atlas already pinned rows: 3
- wave2 proposed pins: expected 5 unless a source span cannot be located
- duplicate-held rows: 2 (`28154`, `28161`)
- network fetch count: exactly 3
- DB writes: 0
- SQL/apply/rollback artifacts: 0
- active execution phrase: `NO ACTIVE EXECUTION PHRASE`

Scope:
- Read local files and write only the two outputs above.
- No DB writes, no SQL/apply/rollback, no prose/wiki/page_versions publish, no git, no deploy/restart, no extra fetches, no secrets.

Required marker in counts report:
`GORU_WAVE2_MECHANICAL_20260705T1615Z`

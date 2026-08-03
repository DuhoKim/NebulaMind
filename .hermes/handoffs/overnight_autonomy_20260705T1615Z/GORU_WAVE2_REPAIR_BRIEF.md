# GORU REPAIR BRIEF — wave2 pin ledger spans — 20260705T1635Z

Your first `PINS_WAVE2.jsonl` has correct row count but invalid/too-short quote spans:
- 28132 / 2605.31052v1 picked author-affiliation text, not the `central role of BH growth...` quote.
- 28155 / 2604.15438 picked title/header text, not the AGN-scope quote.
- Several spans are truncated at 100 chars and do not contain the full supporting/refuting sentence.

Repair task:
1. Backup the current files to:
   - `PINS_WAVE2.jsonl.invalid_initial_goru`
   - `GORU_WAVE2_COUNTS.md.invalid_initial_goru`
2. Overwrite `PINS_WAVE2.jsonl` with the same 5 evidence rows but with valid exact contiguous quote spans from source text.
3. Overwrite `GORU_WAVE2_COUNTS.md` with counts plus an explicit repair note.

Required quote content by source:
- 28099 / `1308.5224v1`: span must include `two-step quenching process` and `interplay between the inner structure of a galaxy and its surrounding dark matter halo`.
- 28132 / `2605.31052v1`: span must include `Our results highlight the central role of BH growth,` and `AGN feedback and environment in driving rapid quenching in the early Universe`.
- 26088 / `2512.16290v1`: span must include `halo mass is the domi-` / `nant factor in quenching central galaxies` and `previous claims regarding the dominant role of central region properties`.
- 28155 / `2604.15438`: span must include `Not all AGNs exhibit every component across the electromagnetic spectrum` and `processes that regulate star formation across a galaxy's lifetime` (or the exact extracted apostrophe variant).
- 26089 / `2401.12953`: span must include `black hole mass to best predict quiescence for centrals` and `halo mass` as environmental parameter.

Rules:
- Use exact source text offsets and line numbers from the `_pdf_text.txt` files.
- Span length should be long enough to be self-contained (roughly 180–700 chars), not a 100-char fragment.
- No header/title/author/affiliation-only snippets.
- Preserve roles/limitations from Lana.
- No DB, no SQL/apply/rollback, no prose/wiki, no git, no deploy/restart, no extra fetches.

Required marker in `GORU_WAVE2_COUNTS.md`:
`GORU_WAVE2_MECHANICAL_REPAIRED_20260705T1635Z`

# Tori re-gate receipt — corrected private cockpit methods-note sibling v2

Timestamp: `2026-08-11T15:29:43+0900 KST`

Marker: `TORI_PRIVATE_REVIEW_COPY_V2_RENDERING_REGATE_RECEIPT_20260811T1529K`

Scoped result: `FAIL_VISIBLE_EQUIVALENCE_V2__NARRATIVE_AND_EMPHASIS_PASS__PROVENANCE_ROW_TRUNCATED__DUHO_MUST_NOT_RELY_YET`

## 1. Custody binding

The corrected no-overwrite sibling exists at the disclosed path and matches the disclosed custody values:

- Path: `/Users/duhokim/HermesOps/cockpit/methods-note-mittal-singal-v2.html`
- Bytes: `15,940`
- SHA-256: `ffd3086b8b8f8ee00db7ba07bb3ac19ba1b2d0f8dc080e8944240c2fc8c1e9ce`
- Current filesystem `mtime` and `ctime`: `2026-08-11T15:22:58+0900`

The frozen failed render remains unchanged:

- Path: `/Users/duhokim/HermesOps/cockpit/methods-note-mittal-singal.html`
- Bytes: `15,388`
- SHA-256: `5a5bf634ab20984536e52bb37ce924f65e2794ae714fe67e1a1dd36f77806557`

The three gated Markdown artifacts also remain unchanged:

1. Authoritative: `36e4efe8984c8d5f7f6f1996f2d6efb38a1be2ceade49b4622f0131917fb99aa`
2. CLEAN: `80b1d1425a9fa28a17b27c3ae599eb5c231c31ae46ad9871ce468cf386489aa7`
3. External source: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`

Two consecutive hash rounds one second apart at `2026-08-11T15:28:57+09:00` were identical.

Finding: `PASS_NO_OVERWRITE_AND_SOURCE_CUSTODY_AT_CURRENT_STATE`.

As before, current state proves that the old file and new sibling are distinct and stable; the no-overwrite pre-state remains the actor's contemporaneous disclosure because Tori did not possess a pre-write filesystem snapshot.

## 2. Independent semantic check

The exact source body was checked independently in two parts:

1. Narrative body, excluding the provenance table and the disclosed HTML banner/footer, against a fresh Pandoc GFM rendering of the exact gated source.
2. Provenance table, per exact row and cell, against a protected-pipe parse that does not treat pipes inside inline code spans as table delimiters.

This separation is necessary because a nominal row/cell count does not prove that the cell contents survived.

Machine-readable audit:

- Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/methods-note-private-copy-v2-verification-20260811T1524K/TORI_METHODS_NOTE_PRIVATE_COPY_V2_SEMANTIC_AUDIT_20260811T1529K.json`
- SHA-256: `7da936122c7d2ac53dd9db73643d5698b8680c0a4113fee0f5dfd291e299ff44`

## 3. Narrative and emphasis: PASS

Outside the provenance table, the v2 source body passes exact visible-text and semantic-markup comparison:

- Visible source-body text exact: `true`.
- Expected words: `1,387`; target words: `1,387`.
- Heading sequences exact: `true`.
- List-item sequence exact: `true`.
- Blockquote sequence exact: `true`.
- `<strong>` sequence exact: `true`.
- `<em>` sequence exact: `true`.
- `<code>` sequence exact: `true`.
- Literal visible `**` markers: `0`.
- Narrative `<strong>` count: expected `61`, target `61`.

The three specifically requested qualification spans are correctly bold:

1. Summary same-release / Mittal-not-byte-self-binding limitation: `PASS`.
2. Summary coupled-choices / different-quantities clause: `PASS`.
3. Section 1 same-release limitation: `PASS`.

The intervening parenthetical and “principal method fork is openly stated” clause is not bold: `PASS`.

Count correction: `59` was the defective narrative `<strong>` count in the failed first render, not the target. The correct narrative target was `61`, and v2 reaches `61`. The independently measured whole-document count is `75` including the banner and provenance table, not `74`; that whole-document count is not the semantic gate.

Finding: `PASS_NARRATIVE_TEXT_AND_MEANING_BEARING_EMPHASIS`.

## 4. Provenance table: FAIL despite 9×2 shape

The table contains `9` rows including the header and nominally `2` cells in every row. That shape check passes but is insufficient.

Per-cell comparison finds:

- Exact matching rows: `8/9`.
- Failing row: the Singal-cuts/Mittal-mask provenance row.

Expected Claim cell:

> Singal cuts (`mG<20.5/20.0/20<mG<20.5`; `|b|>30/35/40`); Mittal `Nside=64`, `|b|<40°`+`30∗`

Expected Source cell:

> Singal 2024; Mittal et al. 2024 (stated in the papers)

Actual visible v2 cells:

1. Claim: `Singal cuts (mG<20.5/20.0/20<mG<20.5; \``
2. Source: `b`

Everything after the opening pipe in the first table `|b|` expression is absent from the rendered row, including:

- the complete `|b|>30/35/40` expression;
- the Mittal `Nside=64` statement;
- the complete `|b|<40°` expression;
- `30∗`;
- the entire intended source attribution.

Independent counts expose why the global check looked green:

- Expected `|b|` expressions in the table: `2`.
- Visible `|b|` expressions in the v2 table: `0`.
- Expected across the whole note: `5`.
- Visible across the whole v2 page: `3`.

The three visible expressions are elsewhere in the narrative, not in the provenance row. The claim that “the three `|b|` expressions retain their bars” therefore does not establish table fidelity.

Root cause: Pandoc's GFM table reader still treats unescaped pipe characters inside inline code spans as table delimiters. It emitted a nominal two-cell row but silently discarded the remainder after the first two fragments. A reference implementation follows the selected dialect; it cannot infer that these unescaped GFM table pipes were intended as code content.

Finding: `FAIL_PROVENANCE_ROW_CONTENT_CUSTODY`.

## 5. Chrome rendering

The exact v2 file was rendered through headless Chrome m151 to a five-page PDF and inspected visually.

Evidence:

- Chrome PDF SHA-256: `d573203e94d1d3b8b62b7bf1e76b52c94736359fe313f7af7327d79ec030e33f`
- Extracted visible text SHA-256: `796bc8e8e10d1b12774e567d6183154a0b663edee4ed80241e74f0ca877bf149`
- First page / corrected-emphasis PNG SHA-256: `905a2b1e3a43b2581f71ed36bc2be864332a6df8b139b102e798b81757eab8cf`
- Final page / truncated-table-row and footer PNG SHA-256: `5593353ef1d9a217a82fa77614d70f796713c491bb41ead4e322fe2cd2f87da0`

Visual findings:

- Banner, title, narrative, and corrected emphasis are readable: `PASS`.
- No literal asterisks are visible: `PASS`.
- The failing provenance row visibly contains only the truncated Claim fragment and `b` as Source: `FAIL`.
- No script or hidden-text CSS mechanism was found.
- The footer correctly says Pandoc conversion, visible-equivalence pending, and no verbatim-rendering claim: `PASS`.
- The footer records the frozen failed-render hash prefix: `PASS`.

## 6. Decision

Overall: `FAIL_VISIBLE_EQUIVALENCE_V2`.

Duho **cannot yet rely on v2 as the exact reading copy**. The narrative and meaning-bearing emphasis are now correct, but one entire provenance claim/source row is materially truncated.

Custody action:

- Do not remove, relocate, or overwrite v2; freeze `ffd3086b…` as the second failed-render receipt target.
- Produce another no-overwrite sibling.
- Use a conversion path that preserves pipes inside inline code spans. In Tori's independent test, Pandoc's `markdown` reader preserved this exact row, but that is a candidate route, not a pass; the resulting sibling must still be checked per cell and in Chrome.
- Keep the gated Markdown source untouched.
- Keep visible-equivalence status pending until every provenance cell matches and Chrome confirms it.

Duho still decides. No note, cockpit page, renderer, registry, frontend, Baseline, DB, Git, deploy, publication, acceptance, or scientific artifact was mutated by Tori during this re-verification. Only append-only audit evidence and this receipt were written in the assigned handoff workspace.

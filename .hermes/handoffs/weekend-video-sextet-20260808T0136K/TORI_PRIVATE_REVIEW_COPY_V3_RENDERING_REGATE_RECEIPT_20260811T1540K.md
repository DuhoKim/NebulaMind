# Tori re-gate receipt — corrected private cockpit methods-note sibling v3

Timestamp: `2026-08-11T15:40:40+0900 KST`

Marker: `TORI_PRIVATE_REVIEW_COPY_V3_RENDERING_REGATE_RECEIPT_20260811T1540K`

Scoped result: `FAIL_VISIBLE_EQUIVALENCE_V3__EMPHASIS_TABLE_AND_PUNCTUATION_PASS__LISTS_AND_BLOCKQUOTE_RENDER_AS_LITERAL_MARKERS__DUHO_MUST_NOT_RELY_YET`

## 1. Custody binding

V3 exists at the disclosed no-overwrite path and matches the disclosed custody values:

- Path: `/Users/duhokim/HermesOps/cockpit/methods-note-mittal-singal-v3.html`
- Bytes: `16,020`
- SHA-256: `25de23fae7473d2753bda74e47156d1164f16f35da13328fa9a65a6bd8156fca`
- Current filesystem `mtime` and `ctime`: `2026-08-11T15:35:33+0900`

Both prior renders remain distinct and unchanged:

1. V1: `5a5bf634ab20984536e52bb37ce924f65e2794ae714fe67e1a1dd36f77806557`, `15,388` bytes.
2. V2: `ffd3086b8b8f8ee00db7ba07bb3ac19ba1b2d0f8dc080e8944240c2fc8c1e9ce`, `15,940` bytes.

The three Markdown artifacts remain unchanged:

1. Authoritative: `36e4efe8984c8d5f7f6f1996f2d6efb38a1be2ceade49b4622f0131917fb99aa`.
2. CLEAN: `80b1d1425a9fa28a17b27c3ae599eb5c231c31ae46ad9871ce468cf386489aa7`.
3. External source: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`.

Two consecutive hash rounds one second apart at `2026-08-11T15:39:55+09:00` were identical.

Finding: `PASS_NO_OVERWRITE_AND_SOURCE_CUSTODY_AT_CURRENT_STATE`.

As before, current state proves that all three render paths are distinct and stable. The no-overwrite pre-state remains the actor's contemporaneous disclosure because Tori did not possess pre-write filesystem snapshots.

## 2. Verification method

V3 was checked without editing it:

1. Narrative visible text and semantic structure against an independent GFM rendering of the exact source, excluding the disclosed banner, provenance table, and footer.
2. Every `<strong>`, `<em>`, and `<code>` span in sequence, including the three requested claim-boundary spans.
3. Every provenance row and cell against a protected-pipe parse of the exact source.
4. Straight/curly quotation and apostrophe counts.
5. Headless Chrome m151 rendering to a five-page PDF, text extraction, and visual inspection of the emphasis, list/blockquote sections, table, and footer.

Machine-readable audit:

- Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/methods-note-private-copy-v3-verification-20260811T1537K/TORI_METHODS_NOTE_PRIVATE_COPY_V3_SEMANTIC_AUDIT_20260811T1540K.json`
- SHA-256: `23f0dd29b9c5f462c2477cd36e92fe3430bca803013151296ab5e278d102c9f9`

## 3. Requested emphasis regression check: PASS for bold, FAIL for blockquote emphasis content

The requested bold checks pass:

- Literal visible `**` markers: `0`.
- Narrative `<strong>` count: expected `61`, target `61`.
- Full `<strong>` sequence exact: `true`.
- Summary same-release / Mittal-not-byte-self-binding limitation bold: `PASS`.
- Summary coupled-choices / different-quantities clause bold: `PASS`.
- Section 1 same-release limitation bold: `PASS`.
- Intervening parenthetical/method-fork clause incorrectly bold: `false`.

The user's claim that the reader change did not regress the bold set is confirmed. V3 has `77` `<strong>` elements across the whole document versus v2's `75`; the added two are restored table-source bold elements. Narrative count remains `61`.

However, the complete `<em>` sequence is not exact. The product-check blockquote's italic content contains two inserted literal `>` markers, with a third visible `>` immediately before the italic span. Italic styling remains, but the emphasized visible text is contaminated by raw blockquote syntax.

## 4. Provenance table: PASS

Per-cell verification passes completely:

- Rows including header: expected `9`, target `9`.
- Cells in every row: expected `2`, target `2`.
- Exact matching rows: `9/9`.
- Table `|b|` expressions: expected `2`, target `2`.

The repaired Singal-cuts row contains all required content:

- `mG<20.5/20.0/20<mG<20.5`;
- `|b|>30/35/40`;
- Mittal `Nside=64`;
- `|b|<40°`;
- `30∗`;
- full source attribution `Singal 2024; Mittal et al. 2024 (stated in the papers)`.

Chrome confirms that the complete row is readable without clipping.

Finding: `PASS_PROVENANCE_TABLE_EXACT_PER_CELL`.

## 5. Smart punctuation: PASS

V3 disables Pandoc's smart extension successfully:

- Curly single quotation marks / typographic apostrophes: `0`.
- Curly double quotation marks: `0`.
- Straight apostrophes remain visible: `21`.
- Straight double quotation marks remain visible: `4`.

No straight-to-curly visible-text drift was introduced.

Finding: `PASS_STRAIGHT_PUNCTUATION_PRESERVED`.

## 6. Fatal remaining defect: lists and blockquote render as literal syntax

V3 does not preserve the source's list and blockquote semantics. The Markdown reader requires different extension choices for the source's no-blank-line transitions.

Narrative comparison excluding the table/banner/footer:

- Expected visible words: `1,387`.
- V3 visible words: `1,402`.
- Exact visible-text equality: `false`.
- Extra visible syntax tokens: `15`.

Those 15 tokens are:

- `9` literal hyphens that should be unordered-list structure;
- literal ordered-list markers `1.`, `2.`, and `3.`;
- `3` literal `>` blockquote markers.

Expected semantic structure:

- Unordered lists: `4`.
- Ordered lists: `1`.
- List items: `14`.
- Blockquotes: `1`.

V3 structure:

- Unordered lists: `1`.
- Ordered lists: `0`.
- List items: `2`.
- Blockquotes: `0`.

Affected sections:

1. Section 1's five bullets appear as literal inline `-` markers in one paragraph.
2. The product-check blockquote appears as three literal `>` markers rather than a blockquote.
3. Section 2's two bullets appear as inline `-` markers.
4. Section 3's three ordered reasons appear as inline `1.`, `2.`, and `3.` text rather than an ordered list.
5. The kinematic-null list's two bullets appear as inline `-` markers.
6. Only Section 5's two bullets are parsed as a list.

Chrome visibly confirms the collapsed paragraphs and raw markers. This materially harms the reading copy's structure and makes the blockquote syntax part of the visible emphasized text.

Root cause: `pandoc -f markdown-smart` fixes smart punctuation and table-pipe custody, but the Pandoc Markdown reader does not recognize most lists or the blockquote without the extension choices required by this source's missing blank lines.

Finding: `FAIL_LIST_AND_BLOCKQUOTE_SEMANTIC_RENDERING`.

## 7. Chrome evidence and footer

- Chrome PDF SHA-256: `4653dfb21018b9b0c2ee4e3578c48d969ef80ea88258817f58b72fb7b94154cd`.
- Extracted visible text SHA-256: `041305e0f62bfa7758badac8a9678c1bebec6043356d1b145265ef8bd523c9a2`.
- Summary/Section 1 PNG SHA-256: `bafbf0d40ecbf53dfb7638f1b46536a80393483a8597cf08c2b415867fcafc4e`.
- Literal-list/blockquote PNG SHA-256: `6eae4cd9bdf19fff2988f1dbb37da05dd2a7118fb60ac89a547275ef26ec3dde`.
- Exact-table/footer PNG SHA-256: `7ad92af17aaf43f6414d7cb1d9232be1617156617c3497150185f02f09bd5f2f`.

The footer passes its current limited claims:

- Names `pandoc -f markdown-smart`.
- Says visible-equivalence verification is pending.
- Makes no verbatim-rendering claim.
- Names both superseded hash prefixes and their failure reasons.

No script or hidden-text CSS mechanism was found.

## 8. Decision and candidate route

Overall: `FAIL_VISIBLE_EQUIVALENCE_V3`.

Duho **cannot yet rely on v3 as the exact reading copy**. Its requested bold emphasis, punctuation, and complete provenance table are correct, but most list and blockquote structure is visibly lost and replaced by literal Markdown syntax.

Custody action:

- Freeze v3 at `25de23fa…`; do not remove, relocate, or overwrite it.
- Produce another no-overwrite sibling.
- Keep the gated Markdown source untouched.

Tori ran an in-memory candidate-reader check using:

`pandoc -f markdown-smart+lists_without_preceding_blankline-blank_before_blockquote`

That candidate, which is **not a rendered artifact and not a pass**, produced:

- exact narrative visible text;
- exact strong/em/code sequences;
- 4 unordered lists, 1 ordered list, 14 list items, and 1 blockquote;
- all 9 provenance rows exact with 2 cells each.

It is a promising v4 conversion route, but a no-overwrite sibling still requires full DOM, per-cell, punctuation, emphasis, block-structure, and Chrome verification before Duho can rely on it.

Duho still decides. No note, cockpit page, renderer, registry, frontend, Baseline, DB, Git, deploy, publication, acceptance, or scientific artifact was mutated by Tori during this verification. Only append-only audit evidence and this receipt were written in the assigned handoff workspace.

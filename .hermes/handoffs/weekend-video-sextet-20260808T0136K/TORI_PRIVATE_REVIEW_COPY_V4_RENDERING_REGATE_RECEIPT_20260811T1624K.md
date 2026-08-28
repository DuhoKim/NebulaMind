# Tori re-gate receipt — private cockpit methods-note sibling v4

Timestamp: `2026-08-11T16:24:00+0900 KST`

Marker: `TORI_PRIVATE_REVIEW_COPY_V4_RENDERING_REGATE_RECEIPT_20260811T1624K`

Scoped result: `FAIL_VISIBLE_EQUIVALENCE_V4__TEXT_EMPHASIS_TABLE_NAV_CHARSET_PASS__LIST_BOUNDARY_PARENTAGE_AND_MOBILE_LAYOUT_FAIL`

## 1. Plain decision

**Duho cannot rely on v4 as the exact readable HTML copy.**

V4 solves every previously reported content-loss mechanism: emphasis, protected-pipe table cells, smart punctuation, list/block recognition, and UTF-8 all pass. It nevertheless introduces a new meaning-bearing hierarchy defect: four source-level blocks that occur after lists are absorbed into the preceding final list item. The expected numbers of lists, list items, and blockquotes all remain present, so count-only checks stay green while scope is wrong.

V4 also fails its responsive-reading claim at a 390-pixel viewport because the stylesheet defines a table overflow wrapper but the page does not contain that wrapper; the table's `min-width:620px` widens the page and visibly clips the banner, navigation, title, and opening prose.

Freeze v4 by path/hash as failed no-overwrite evidence. The character-exact charset page remains the last passed private reading copy.

This result confers no publication, acceptance, registry, renderer, Git, frontend, public-exposure, or scientific-execution clearance. Duho still decides.

## 2. Candidate and custody: PASS

Candidate:

- Path: `/Users/duhokim/HermesOps/cockpit/methods-note-mittal-singal-v4.html`
- Bytes: `18,717`
- SHA-256: `9a71036aba83fd38be75aa1bf02ce0537040c3c54fca205bc4e5612fbfdb82f4`

Tailnet route:

`https://duho-macstudio.taila27502.ts.net/cockpit/methods-note-mittal-singal-v4.html`

Independent fetch:

- HTTP status: `200`.
- `Content-Type`: `text/html`.
- `Content-Length`: `18717`.
- Served-body SHA-256: `9a71036aba83fd38be75aa1bf02ce0537040c3c54fca205bc4e5612fbfdb82f4`.
- Served body versus local v4: exact.

Two consecutive hash rounds one second apart remained stable.

Unchanged prior artifacts:

- Passed charset page: `4bed48850e3730ad1b2c30f2bf1777b490cc1f0929c87764f83ac25b312c7620`.
- Raw byte-identical `.txt`: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`.
- Failed v1: `5a5bf634ab20984536e52bb37ce924f65e2794ae714fe67e1a1dd36f77806557`.
- Failed v2: `ffd3086b8b8f8ee00db7ba07bb3ac19ba1b2d0f8dc080e8944240c2fc8c1e9ce`.
- Failed v3: `25de23fae7473d2753bda74e47156d1164f16f35da13328fa9a65a6bd8156fca`.

Unchanged Markdown artifacts:

- Authoritative: `36e4efe8984c8d5f7f6f1996f2d6efb38a1be2ceade49b4622f0131917fb99aa`.
- CLEAN: `80b1d1425a9fa28a17b27c3ae599eb5c231c31ae46ad9871ce468cf386489aa7`.
- EXTERNAL gated source: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`.

Finding: `PASS_CUSTODY_AND_NO_SOURCE_DRIFT`.

As in prior receipts, the claim that the new file did not previously exist remains the actor's contemporaneous disclosure because Tori did not possess a pre-write snapshot. Nothing in the post-action state contradicts it.

## 3. Previously failing mechanisms: all PASS

### Narrative text and emphasis

Scoped to source content, excluding banner, navigation, footer, and table:

- Narrative words: source `1,387`; v4 `1,387`.
- Ordered visible prose sequence: exact.
- `<strong>`: `61/61`, ordered text exact.
- `<em>`: `13/13`, ordered text exact.
- `<code>`: `24/24`, ordered text exact.
- Visible literal `**`: `0`.
- Visible literal single-asterisk markers: `0`.
- The requested qualification spans remain bold.
- The intervening method-fork parenthetical remains outside the bold qualification.

Finding: `PASS_TEXT_AND_EMPHASIS`.

### Table

The table was checked against an independent raw-source parser that protects pipes inside code spans. DOM text was reconstructed without injecting spaces around inline elements.

- Rows: `9/9`.
- Cells per row: `2` for all nine rows.
- Ordered cells: `18/18` exact.
- Row matches: all nine true.
- `|b|` expressions: source `5`; v4 source body `5`.
- The Singal-cuts row contains both `|b|` expressions, `Nside=64`, `30∗`, and the complete source attribution.

Finding: `PASS_TABLE_PER_CELL`.

### Punctuation and UTF-8

- Curly quote code points `‘’“”`: zero.
- Straight apostrophes: source `26`; v4 source body `26`.
- Browser character set: `UTF-8`.
- Unicode replacement characters: zero.
- Source-body counts for `≈`, `°`, `−`, `∗`, `—`, `λ`, `δ`, `×`, `§`, `α`, `β`, and `→` all match the gated source.

Finding: `PASS_PUNCTUATION_AND_CHARSET`.

### Navigation and framing

- H2 headings: `7`.
- Navigation links: `7`.
- Link text, order, target fragment, and heading ID: exact one-to-one matches.
- Scripts: zero.
- Hidden source elements: zero.
- The navigation duplicates headings only and adds no scientific or explanatory claim prose.
- The light/dark CSS adds no claim content.
- Banner and footer are disclosed framing outside the source body.

Finding: `PASS_NAV_AS_PRESENTATION_ONLY`.

## 4. Fatal defect: list counts pass while item contents and parent hierarchy fail

The exact reader string is:

`markdown-smart+lists_without_preceding_blankline-blank_before_blockquote`

The extensions cause the no-blank list and blockquote markers to be recognized. They do **not** make the following source-level block boundaries unambiguous. Pandoc's lazy list continuation absorbs column-zero blocks into the preceding list item.

Independent oracle:

- Tori read the raw source indentation.
- Actual list-item continuation lines are indented by two or three spaces.
- The blockquote and the four post-list/global blocks begin at column zero.
- In memory only, Tori inserted blank separators at those column-zero boundaries without changing any word or inline markup, then rendered with table-safe `markdown-smart`.
- Global visible words still matched v4, but complete ordered `<li>` text and parent hierarchy did not.

Counts alone are misleading:

- Unordered lists: expected `4`, v4 `4`.
- Ordered lists: expected `1`, v4 `1`.
- List items: expected `14`, v4 `14`.
- Blockquotes: expected `1`, v4 `1`.
- Complete ordered list-item text sequence: **FAIL**, four mismatches.

The four mismatches are:

1. **Section 1, item 5**
   - Source-level outside block: the three-line product-check blockquote beginning `The product check above is this note's own.`
   - V4: the blockquote is a descendant of item 5.
   - Browser DOM: `blockquote.parentElement.tagName == LI`; `blockquote.closest('li')` is true.
   - Visible effect: the blockquote is indented beneath the final `Therefore, precisely` bullet rather than standing after the list.

2. **Section 2, item 2 / Singal**
   - Source-level outside block: `This fork is real and acknowledged by both sides...` through `not the demonstrated explanation of the amplitude gap.`
   - V4: that complete global method-fork and claim-boundary paragraph is appended continuously inside the Singal bullet.
   - This changes its apparent scope from a conclusion about both papers to continuation of the Singal item.

3. **Section 3, ordered item 3 / Different estimands**
   - Source-level outside block: `Some simple single-factor explanations are not sufficient...` through the masking/estimator caveat.
   - V4: that complete global paragraph is appended inside numbered item 3.
   - The Chrome render visibly keeps the paragraph at item 3 indentation.

4. **Kinematic list, item 2 / Mittal**
   - Source-level outside block: `The two null constructions are different...` through `not the same estimand.`
   - V4: that complete no-inference and estimand-boundary paragraph is appended inside the Mittal bullet.
   - This is meaning-bearing: a post-list boundary about both constructions is visually scoped as part of the Mittal item.

All words survive, but block hierarchy changes claim scope. This is `SHAPE_GREEN_CONTENT_SCOPE_RED`, analogous to the earlier 9×2 table failure.

The footer's statements `14/14 list items` and `blockquote intact` are true only as counts/presence. They are insufficient and misleading as an equivalence claim because the ordered item contents and blockquote parent are wrong.

Finding: `FAIL_LIST_ITEM_CONTENT_AND_PARENT_HIERARCHY`.

## 5. Responsive-layout defect

The CSS defines:

- `.tablewrap{overflow-x:auto;...}`
- `table{min-width:620px;...}`

But the shipped DOM contains:

- `.tablewrap` elements: `0`.
- Table parent: `BODY`.
- Parent `overflow-x`: `visible`.

At the desktop 1280-pixel viewport, the table is fully readable and the document does not overflow.

At the tested 390×844 Chrome viewport, the missing wrapper lets the 620-pixel table widen the page. The first viewport visibly clips the right side of:

- the banner;
- navigation labels;
- the title;
- opening prose.

This is not a claim-content mutation, but it defeats the stated responsive reading presentation.

Finding: `FAIL_MOBILE_READABILITY_MISSING_TABLEWRAP`.

## 6. Browser evidence

The actual Tailnet v4 was rendered through Chrome 151.

Evidence:

- Tailnet headers SHA-256: `2848c6d0f8895af52dc2e402c7836883bfe1d7383b9736f11b31f816a16487d2`.
- Tailnet body SHA-256: `9a71036aba83fd38be75aa1bf02ce0537040c3c54fca205bc4e5612fbfdb82f4`.
- Browser DOM SHA-256: `66dbc0f70f5aff3f6c0253d978f4c2cb411722f86355e1ce11d1c66c45be5304`.
- Desktop first viewport SHA-256: `5587db8d4505110760c1195f1186ec06f11b785331ccd901cff58aabbb3ed3d6`.
- Mobile first viewport SHA-256: `77fe1e4659c326d112c405dbc712c651ada8e2dc32afaf38ebde8bff3a9b4b94`.
- Seven-page browser PDF SHA-256: `75036d11eedeb32b581188fb307800c5d565ab142d7aa3ccacd79d0cefc1d226`.
- Extracted PDF text SHA-256: `ee8c2d6740bcee3c14fb2fabf9f90ce3296c5dca16d7e6c5377d089ee26208a7`.

The desktop table and footer are visible and readable. The footer correctly binds the source filename, SHA-256, byte count, reader string, and pending independent verification status. The failure is hierarchy and mobile layout, not missing words, table truncation, or encoding.

## 7. Required next gate

If another HTML sibling is attempted, do not edit the gated source and do not overwrite v4.

The successor must:

1. preserve all four source-level outside blocks as siblings after their lists;
2. place the blockquote outside the Section 1 list;
3. compare the complete ordered `<li>` text sequence, not merely `14` counts;
4. assert `blockquote.closest('li') == null`;
5. wrap the table in the existing `.tablewrap` overflow container;
6. repeat emphasis, punctuation, protected-pipe per-cell table comparison, nav binding, charset, hidden-content checks, and desktop/mobile Chrome verification.

A safe build route is a separately receipted derived Markdown input that inserts blank separators at the raw column-zero list/block boundaries without changing any visible character, followed by table-safe `markdown-smart`. That route is only a candidate until the resulting no-overwrite sibling passes every gate above.

## 8. Final classification

- Custody: `PASS`.
- Narrative words/emphasis/code: `PASS`.
- Table per cell: `PASS`.
- Straight punctuation/UTF-8: `PASS`.
- Nav as presentation-only duplication: `PASS`.
- List and blockquote counts: `PASS_BUT_INSUFFICIENT`.
- Complete list-item contents and block parentage: `FAIL`.
- Responsive mobile reading layout: `FAIL`.
- V4 exact reading copy: `FAIL / HOLD`.
- Last passed exact reading copy: `/Users/duhokim/HermesOps/cockpit/methods-note-mittal-singal-text.html` (`4bed4885…`).
- Publication/acceptance/clearance: `NOT CONFERRED`.

**Duho must not rely on v4 as the exact readable HTML copy.**

No source note, prior cockpit artifact, server configuration, registry, renderer, frontend, Baseline, DB, Git history, publication state, acceptance state, or scientific artifact was mutated by Tori. Only append-only audit evidence and this receipt were written in the assigned handoff workspace.

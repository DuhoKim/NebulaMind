# Tori post-action custody receipt — private cockpit methods-note render

Timestamp: `2026-08-11T15:18:40+0900 KST`

Marker: `TORI_PRIVATE_REVIEW_COPY_RENDERING_VERIFICATION_RECEIPT_20260811T1518K`

Scoped result: `AUTHORIZED_PRIVATE_REVIEW_COPY_ACTION__HOLD_RENDERED_COPY_FOR_VISIBLE_SEMANTIC_DRIFT__GATED_SOURCE_UNCHANGED`

## 1. Why this successor receipt exists

The earlier receipt
`TORI_METHODS_NOTE_EXTERNAL_SOURCE_BINDING_RECEIPT_20260811T1446K.md`
correctly recorded that no cockpit action had occurred as of its own `14:46:20 KST` timestamp. That historical receipt is not edited.

A later action was disclosed at the moment of acting under Duho's direct order:

> "publish it to the cockpit so i can read it"

The disclosed action created this private review copy:

- Path: `/Users/duhokim/HermesOps/cockpit/methods-note-mittal-singal.html`
- Creation/modification time presently reported by the filesystem: `2026-08-11T14:55:38+0900`
- UTF-8 bytes: `15,388`
- SHA-256: `5a5bf634ab20984536e52bb37ce924f65e2794ae714fe67e1a1dd36f77806557`

Current `mtime` and `ctime` are identical and consistent with a newly created file. There is no pre-write snapshot in this verification packet, so the claim that no prior file was overwritten is recorded as the actor's contemporaneous disclosure, not upgraded to an independently proven pre-state.

Classification: `NO_AUTHORIZATION_BREACH_FOUND`. The write was directly ordered by Duho for private read-and-decide review; the page explicitly says draft, private, not published, not accepted, and Duho decides. This does not confer publication, acceptance, deploy, registry, renderer, YouTube, or scientific-execution clearance.

A receipt is nevertheless required because the action is subsequent to the 14:46 custody statement and because the rendered copy fails visible-equivalence verification.

## 2. Three Markdown hashes re-verified unchanged

Two consecutive hash rounds one second apart at `2026-08-11T15:17:04+09:00` were identical.

1. Authoritative internal note
   - Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811.md`
   - Bytes: `17,494`
   - SHA-256: `36e4efe8984c8d5f7f6f1996f2d6efb38a1be2ceade49b4622f0131917fb99aa`

2. CLEAN derivative
   - Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811_CLEAN.md`
   - Bytes: `12,439`
   - SHA-256: `80b1d1425a9fa28a17b27c3ae599eb5c231c31ae46ad9871ce468cf386489aa7`

3. Kun-passed external edition / rendered source
   - Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811_EXTERNAL.md`
   - Bytes: `11,473`
   - SHA-256: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`
   - Exact match to Kun's gated target.

Finding: `PASS_GATED_MARKDOWN_BYTES_UNCHANGED`.

## 3. Visible-equivalence method

The private HTML was checked three ways without editing it:

1. Raw DOM/text/structure comparison against the exact external Markdown source, with the disclosed banner and source/hash footer excluded from source-body equality.
2. Explicit comparison of headings, list items, blockquote, inline emphasis, inline code, negation-bearing prose, and every provenance-table row/cell.
3. Headless Chrome m151 rendering to a six-page PDF, text extraction, and visual inspection of the first page, broken table page, and footer page.

No `<script>` element exists. No `display:none`, `visibility:hidden`, `opacity:0`, or `font-size:0` hiding rule exists. The banner, title, body, and footer are visible.

Machine-readable audit:

- Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/methods-note-private-copy-verification-20260811T1458K/TORI_METHODS_NOTE_PRIVATE_COPY_SEMANTIC_AUDIT_20260811T1517K.json`
- SHA-256: `506ab5986039d82188b9c68f2fb0197c2f501f2f2e4139c9d07e094d85165f32`

Chrome-render evidence:

- PDF SHA-256: `f9a84d7735976cfac4294263b2c37a36757e10a1b21101af6312b7ab7f05ab6f`
- Extracted visible-text SHA-256: `f5b8b68a56d3273f548cd272d2c58e52d75258fee7b6328560c5d5a6d53b90b6`
- First-page PNG SHA-256: `e558506db020e8d1f5206316665b1f9c9e4de3c88564054b40bfb4646cee82b0`
- Broken-table-page PNG SHA-256: `dd179344309705560e0ffdda3948904605cadde933f390bbc22cfa500053ecde`
- Footer-page PNG SHA-256: `0b0482ddc0ab351221e2165a8927790a04a504c6363f03b833d536fb96f810bb`

## 4. Rendering result: HOLD

Result: `FAIL_VISIBLE_EQUIVALENCE`.

### 4.1 Narrative words and negations

Outside the provenance table, after excluding the disclosed banner/footer, no prose word or negation was added, dropped, or reworded. The heading count, list-item count, blockquote count, inline-emphasis count, and inline-code count otherwise match.

However, four Markdown delimiters are rendered as literal visible text:

- Summary: visible `**strongly`.
- Summary: visible `quantities**`.
- Section 1: visible `**strongly`.
- Section 1: visible `explanation**`.

The page therefore does not show the exact source text as intended Markdown.

### 4.2 Meaning-bearing emphasis drift

The converter also attached bold emphasis to the wrong claims:

1. The summary's intended bold same-release/Mittal-not-byte-self-binding limitation is not bold.
2. The summary's intended bold coupled-choices/different-quantities clause is not bold.
3. The intervening parenthetical and “principal method fork is openly stated” clause is incorrectly bolded instead.
4. Section 1's intended bold same-release limitation is not bold.

Counts reflect the corruption: expected `61` `<strong>` elements in the narrative body; target `59`.

This is not cosmetic-only because the source uses emphasis to preserve the exact qualification and claim boundary.

### 4.3 Provenance-table row is structurally and semantically mangled

The source provenance table contains `9` rows including its header, with exactly `2` cells in every row. The HTML also has `9` rows, but the Singal-cuts/Mittal-mask row has `6` cells instead of `2`.

Intended Claim cell:

> Singal cuts (`mG<20.5/20.0/20<mG<20.5`; `|b|>30/35/40`); Mittal `Nside=64`, `|b|<40°`+`30∗`

Intended Source cell:

> Singal 2024; Mittal et al. 2024 (stated in the papers)

The rendered row splits into five Claim fragments plus the Source:

1. `Singal cuts (mG<20.5/20.0/20<mG<20.5; \``
2. `b`
3. `>30/35/40` plus the Mittal/Nside fragment
4. `b`
5. `<40°+30∗\``
6. the intended Source

Consequences visible in Chrome:

- Both `|b|` absolute-latitude expressions lose their vertical bars.
- Backticks remain visible.
- Claim text is split across five narrow columns.
- Source attribution is displaced into a sixth column.

This is silent scientific-notation and provenance-layout damage, even though the component words mostly survive.

### 4.4 Banner/footer

The private-review banner is readable and accurately says draft/not published/not accepted/Duho decides. The source footer's filename, SHA-256, and `11,473`-byte count match the gated source.

The footer statement `rendered verbatim, no content altered` is false for this exact HTML because of the visible-marker, emphasis, and table defects above. `PASS_SOURCE_BINDING` in the banner is only shorthand for Tori's longer scoped binding result; it is not a new or broader gate.

## 5. Custody decision and next action

- Do **not** remove, relocate, or overwrite the current `5a5bf634…` file as part of this verification. It is now frozen evidence of the failed render.
- Do **not** rely on this HTML as Duho's exact reading copy.
- Produce a corrected **no-overwrite sibling** from the exact external source, preserving nested emphasis and treating Markdown table pipes inside code spans safely.
- Remove the `rendered verbatim, no content altered` footer claim from any candidate until a fresh visible-equivalence check passes.
- Re-submit the corrected sibling for exact hash and visible-text verification. Duho still decides.

No cockpit, Markdown note, registry, renderer, frontend, Baseline, DB, Git, deploy, publication, or acceptance mutation was performed by Tori during this verification. Only append-only audit evidence and this successor receipt were written in the assigned handoff workspace.

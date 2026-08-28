# Tori verification receipt — UTF-8 exact-source private reading page

Timestamp: `2026-08-11T16:09:05+0900 KST`

Marker: `TORI_PRIVATE_REVIEW_COPY_CHARSET_PAGE_VERIFICATION_RECEIPT_20260811T1609K`

Scoped result: `PASS_CHARACTER_EXACT_PRIVATE_READING_COPY_WITH_ESCAPE_SCOPE_CORRECTION`

## 1. Plain decision

**Duho can rely on this private page as the character-exact reading copy of the gated external methods note.**

The note is deliberately displayed as literal Markdown source text inside one `<pre>` element. Double asterisks, single asterisks, pipe-table rows, list markers, and blockquote markers remain visible because they are source characters, not failed rendering residue.

This pass confers no publication, acceptance, registry, renderer, Git, frontend, public-exposure, or scientific-execution clearance. Duho still decides.

The text-display verification thread is closed after this receipt. The announced video candidate is a separate future artifact and must receive its own byte binding and frame sweep when it exists.

## 2. Candidate and Tailnet binding: PASS

Candidate:

- Path: `/Users/duhokim/HermesOps/cockpit/methods-note-mittal-singal-text.html`
- Bytes: `12,511`
- SHA-256: `4bed48850e3730ad1b2c30f2bf1777b490cc1f0929c87764f83ac25b312c7620`

Tailnet route:

`https://duho-macstudio.taila27502.ts.net/cockpit/methods-note-mittal-singal-text.html`

Independent fetch:

- HTTP status: `200`.
- `Content-Type`: `text/html`.
- `Content-Length`: `12511`.
- Served-body SHA-256: `4bed48850e3730ad1b2c30f2bf1777b490cc1f0929c87764f83ac25b312c7620`.
- Served body versus local candidate: exact.

The UTF-8 declaration is `<meta charset=utf-8>` at byte offset `15`, before the title or source text.

## 3. Character-level round trip: PASS

Gated source:

- Path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811_EXTERNAL.md`
- Bytes: `11,473`.
- Unicode characters: `11,324`.
- SHA-256: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`.

Independent parser checks found:

- exactly one `<pre>` element;
- zero scripts;
- disclosed banner outside the `<pre>`;
- raw `<pre>` payload exactly equals Python `html.escape(source, quote=True)`;
- `html.unescape(raw_pre_payload) == source`;
- decoded `<pre>` text equals the complete source character-for-character;
- UTF-8 encoding of decoded `<pre>` text hashes to `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`.

Finding: `PASS_EXACT_SOURCE_TEXT_AFTER_HTML_DECODING`.

There is no Markdown conversion and no semantic parser involved.

## 4. Escape-scope correction: non-fatal

The supplied description says 15 instances across ampersand, less-than, and greater-than were escaped. The count `15` is correct for angle-comparison symbols in the source:

- ampersand: `0`;
- less-than: `10`;
- greater-than: `5`.

However, the actual escaper also escaped quotes because it used the equivalent of `html.escape(..., quote=True)`:

- double quotes → `&quot;`: `8`;
- apostrophes → `&#x27;`: `26`.

Actual entity substitutions inside the raw `<pre>` payload: `49`, not `15`.

This is a representation-scope correction, not visible-text drift. All 49 entities decode to the exact source characters, and the complete decoded `<pre>` is character-identical to the gated note.

The banner phrase describing the characters as the file's own bytes should therefore be read at the displayed-character level: the raw HTML payload uses entities, while the browser-decoded characters are exact. The source hash displayed in the banner correctly binds the decoded text.

## 5. Headless-Chrome browser verification: PASS

Headless Chrome 151 opened the exact Tailnet URL.

The live browser DOM contained:

- one `<pre>`;
- `11,324` characters in that `<pre>`;
- exact equality with all `11,324` source characters;
- decoded `<pre>` UTF-8 SHA-256 `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`;
- zero Unicode replacement characters;
- zero detected mojibake;
- zero scripts.

Unicode canaries in the browser-decoded source `<pre>` match the gated source:

- `≈`: `9`;
- `°`: `6`;
- `−`: `1`;
- `∗`: `2`;
- `—`: `22`;
- `λ`: `2`;
- `δ`: `1`;
- `×`: `1`;
- `§`: `7`;
- `α`: `8`;
- `β`: `1`;
- `→`: `4`.

The whole HTML page contains `24` em dashes because the exact source `<pre>` contains `22` and the disclosed title/banner framing contributes two.

Chrome's visible viewport confirms:

- correct en/em dashes, section signs, apostrophes, and punctuation;
- no replacement glyphs or mojibake;
- readable dark-theme text;
- line wrapping without horizontal clipping;
- literal Markdown markers intentionally displayed as source text.

Evidence:

- Tailnet response headers SHA-256: `40748017c2a11b57812892f17f70d9785d588e08ce0d3e64375167b1c8cdcc13`.
- Tailnet response body SHA-256: `4bed48850e3730ad1b2c30f2bf1777b490cc1f0929c87764f83ac25b312c7620`.
- Chrome DOM SHA-256: `2743e4e28ce1ecef8efaa012f740547722b255f93b4faad86e8cf6be7bb867fe`.
- Chrome-extracted `<pre>` text SHA-256: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`.
- Chrome first-viewport screenshot SHA-256: `e20077df0abdedc77e29493eee4052679289d190613d4569faabb74ff786f05c`.

Finding: `PASS_HEADLESS_CHROME_CHARACTER_EXACT_AND_READABLE`.

## 6. Custody remains unchanged: PASS

Two consecutive hash rounds one second apart were identical.

Raw byte-identical `.txt`:

- `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`.

Frozen failed HTML renders:

- V1: `5a5bf634ab20984536e52bb37ce924f65e2794ae714fe67e1a1dd36f77806557`.
- V2: `ffd3086b8b8f8ee00db7ba07bb3ac19ba1b2d0f8dc080e8944240c2fc8c1e9ce`.
- V3: `25de23fae7473d2753bda74e47156d1164f16f35da13328fa9a65a6bd8156fca`.

Markdown artifacts:

- Authoritative: `36e4efe8984c8d5f7f6f1996f2d6efb38a1be2ceade49b4622f0131917fb99aa`.
- CLEAN: `80b1d1425a9fa28a17b27c3ae599eb5c231c31ae46ad9871ce468cf386489aa7`.
- EXTERNAL: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`.

No source note, raw `.txt`, cockpit page, server configuration, frozen render, registry, renderer, frontend, Baseline, DB, Git history, publication state, or scientific artifact was mutated by Tori. Only append-only audit evidence and this receipt were written in the assigned handoff workspace.

## 7. Final classification

- Exact gated-source characters in browser `<pre>`: `PASS`.
- Correct browser UTF-8 decoding: `PASS`.
- Readable wrapping/no visible clipping: `PASS`.
- No Markdown conversion: `CONFIRMED`.
- Escape description: `PASS_WITH_SCOPE_CORRECTION_15_TO_49_ENTITY_SUBSTITUTIONS`.
- Private exact reading copy: `PASS`.
- Publication/acceptance/clearance: `NOT CONFERRED`.
- Text-display thread: `CLOSED`.

**Duho may rely on `/cockpit/methods-note-mittal-singal-text.html` as the character-exact private reading copy of the gated external methods note.**

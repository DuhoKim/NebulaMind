# Wiki Stored Content Contract v1

Authoritative for `wiki_pages.content` at rest.

## Math

- All math is delimited with `$...$` or `$$...$$`.
- Inside math, raw `<`, `>`, and `&` are forbidden. Use KaTeX-native `\lt`, `\gt`, and `\&`.
- TeX control sequences such as `\sim`, `\approx`, `\pm`, `\odot`, and `\propto` are forbidden outside math.

## HTML

- No HTML elements are stored in wiki content.
- Legacy `<span data-cite-ids="...">...</span>` is converted to `<!--cite:...-->`.
- Any remaining `<span>`, `</span>`, `<sub>`, or `<sup>` is a violation, not something to silently strip.
- HTML character entities are decoded before storage; content must not store `&gt;`, `&lt;`, `&amp;`, `&quot;`, or equivalent entity forms.

## Markers

Only registered comment markers may appear at rest:

- `<!--claim:ids-->...<!--/claim:ids-->`
- `<!--cite:ids-->`
- `<!--cite-unmatched:key-->`
- `<!--EVIDENCE_HIGHLIGHTS_START-->` and `<!--EVIDENCE_HIGHLIGHTS_END-->`
- Trust status comments: `accepted`, `consensus`, `debated`, `challenged`, `unverified`, and their closing forms.

Unknown comments remain invisible in the frontend renderer, but they are not valid stored content.

## Citation Display

Stored content must not contain author-year parenthetical citations intended for rendering, `[n]` numeric reference tokens, or `References` / `Bibliography` sections.

Display policy is defined in `frontend/CITATION_POLICY.md`: inline evidence badges only, no numbered superscripts, no bottom bibliography.

# Math & Citation Rendering Architecture — v1

> **Historical correction (2026-06-10):** This document's original citation-display recommendation for numbered superscripts and a bottom References list conflicts with Papa's durable citation directive from 2026-05-21, reinforced 2026-06-10. Frontend rendering must follow `frontend/CITATION_POLICY.md`: inline evidence badges only, no numbered `[n]` superscripts, and no bottom References/Bibliography section. Backend canonical citation markers and math normalization from this document remain valid unless superseded elsewhere.

**Author:** Kun
**Date:** 2026-06-09
**Status:** Draft for Tori implementation
**Live grounding:** Read against local NebulaMind repo on 2026-06-09. Key paths: `backend/scripts/align_citations.py` (citation aligner; `PAREN_CITE_RE` at line 25), `backend/scripts/convert_all_math_to_dollars.py` / `convert_all_unicode_masses.py` / `fix_more_math.py` (page-57 ad-hoc patches — to be unified), `backend/app/agent_loop/autowiki/citation_context.py` (prompt-time evidence map), `frontend/src/app/wiki/[slug]/WikiPageClient.tsx` (renderer; `wrapCitationComments` at line 145, `<span data-cite-ids>` hide-rule at line 847), `frontend/src/app/wiki/[slug]/ClaimBlock.tsx` (claim popover). Prior design: `docs/dynamic_citations_design_v1.md` (2026-06-07) established `<!--cite:N-->` markers and `page_citation_links` schema; this document extends that contract to cover the four failure axes Papa surfaced today.

---

## 1. Executive Summary

NebulaMind wiki pages today suffer from four classes of formatting/rendering corruption. Each was patched in isolation on Page 57 by single-page scripts (`convert_all_math_to_dollars.py`, `convert_all_unicode_masses.py`, `fix_more_math.py`). The patches collide with each other (`$10^{11}$·⁸` is the visible artifact of piecewise rewrites), do not cover the rest of the corpus (17 of 43 pages still contain raw Unicode), and re-emerge after every renovation cycle because there is no normalization at write-time. This document specifies the unified, system-wide architecture that replaces the page-57 patches with three deterministic transforms run at the right point in the pipeline.

**Empirical scale (full-corpus scan, 43 pages, 2026-06-09):**

| Failure axis | Total occurrences | Pages affected |
|---|---|---|
| Multi-cite parentheticals `(A 2002; B 2013)` | 48 | 15 / 43 |
| Single-cite parens still in prose | 52 | concentrated on page 57 |
| `<span data-cite-ids>` (hidden by current renderer) | 32 | 1 (page 57) |
| `<!--cite:N-->` markers (target format) | 66 | most pages |
| Raw Unicode super/sub in non-math regions | 67 | 17 / 43 |
| Star/sun symbols (`★ ⋆ ☉ ⊙`) in non-math | 28 | several |
| Composite breaks (`$math$·⁸` artefacts) | 5 | 1 (page 57) |
| Bare subscript variables (`R_vir`) in non-math | 9 | a few |
| Em-run risk (`_word_` outside math) | 0 | none observed |

The em-run/underscore-italics axis is theoretically real but currently has **zero observed occurrences**. We still guard against it because future LLM rewrites can introduce them at any time.

**The fix is a three-layer pipeline:**

```
[Write-time canonicalizer]   ──>   PostgreSQL `wiki_pages.content`   ──>   [Frontend safety preprocessor]   ──>   ReactMarkdown
       (Backend)                                                                  (TS)                              (+ remarkMath + rehypeKatex)
```

1. **Backend write-time canonicalizer** (`scripts/canonicalize_page.py`, replacing the three ad-hoc Page-57 patches). Idempotent. Runs (a) as a one-time corpus backfill, (b) as a Celery post-write hook on every `wiki_pages.content` commit, (c) inside `align_citations.py` before citation extraction.
2. **Multi-cite tokenizer** inside `align_citations.py` that decomposes `(A 2002; B 2013)` into two independent author-year keys before resolution.
3. **Frontend safety preprocessor** in `WikiPageClient.tsx` that runs *before* ReactMarkdown — wraps bare `Var_subscript` patterns, converts `\(...\)` math delimiters to `$...$`, escapes orphan underscores.

Plus a unified **citation-display policy** that eliminates the aligned/unaligned discrepancy by always rendering inline citations as numbered superscripts `[1]…[n]` (the v1 design intent that was never actually wired in).

---

## 2. Current State Audit

### 2.1 The four-axis problem

**Axis 1 — Citation display discrepancy.** `align_citations.py:211` wraps matched parentheticals as `<span data-cite-ids="N">(Author Year)</span>`. `WikiPageClient.tsx:847-851` returns `null` for any `<span>` with `data-cite-ids`, hiding aligned cites. Unmatched parentheticals (no wrap) leak through as raw text. **Page 57 result: 32 hidden + 27 visible-raw.** The reader sees inconsistent prose.

**Axis 2 — Markdown / LaTeX subscript conflict.** `remark-math` (the only math plugin) recognizes only `$…$` and `$$…$$` delimiters by default; it does **not** recognize `\(…\)`. Past LLM writes produced `\(…\)` blocks that fell through to react-markdown's default Markdown parser, where bare subscripts like `M_h` either render as literal `M_h` or — if a paired `_…_` exists later — trigger a runaway emphasis run. Confirmed: page 57 currently has zero `_x_` em-runs but contains 1 bare `R_vir`. Other pages have 9 bare subs. Conflict is latent; one bad rewrite away.

**Axis 3 — Multi-citation parenthetical regex failure.** `PAREN_CITE_RE` (line 25-31) is anchored on a *single* trailing year. For `(Fabian 2012; Heckman & Best 2014)` the engine backtracks and matches the full body as one citation with authors `Fabian, Heckman, Best` and year `2014` — silently conflating two distinct works into one wrong author-year key. For `(e.g., Labbé et al. 2023)` the `e.g.,` prefix breaks the leading `[A-Z]` author anchor. **Corpus impact: 48 multi-cite instances on 15 pages — none currently align.**

**Axis 4 — Unicode variable mixing.** LLM writers produce a mix of `M★`, `M⋆`, `M☉`, `10¹²`, `10⁻⁵`, `T_vir`, and proper `$M_\star$` in the same page. The three ad-hoc fix scripts each handled a subset; their combined output produced **5 composite breaks** like `$10^{11}$·⁸` where one script wrapped `10^{11}` but missed the trailing `·⁸` superscript. **Corpus impact: 67 raw super/sub chars + 28 star/sun symbols on 17 pages.**

### 2.2 Why prior patches did not stick

| Patch | Scope | Why insufficient |
|---|---|---|
| `convert_all_math_to_dollars.py` | Page 57 only, named-variable allow-list | Doesn't generalize; misses any variable not in the hardcoded list. No idempotence verification. |
| `convert_all_unicode_masses.py` | Page 57 only, super/sub allow-list | Allow-list is shallow (handles `10⁹`–`10¹⁵` but not `10⁻⁵` or `δρ/ρ ~ 10⁻⁵`). Runs before mass conversion, so order-of-operations matters and is not stated. |
| `fix_more_math.py` | Page 57 only, regex cleanup | Patches a specific composite break (`$$M_{\text{h}}$$ → $M_{\text{h}}$`) but creates new breaks if run in wrong order. |
| `align_citations.py` regex | Whole corpus | Single trailing year assumption; cannot handle multi-cite or `e.g.,` prefix. |

The architectural problem: **each fix targets a symptom, not a layer.** The normalization layer is the missing abstraction.

### 2.3 Pipeline data flow (current)

```
LLM renovation prompt
    └─ produces prose with: <!--cite:N-->, (Author Year), M★, 10¹², \(M_h\), \rho_SFR, ...
                  │
                  ▼
        wiki_pages.content     ◄── three Page-57-only ad-hoc scripts patch some instances
                  │
                  ▼
        align_citations.py    ◄── PAREN_CITE_RE; misses 48 multi-cites
          wraps some parens as <span data-cite-ids="N"></span>
                  │
                  ▼
        Frontend fetch /api/pages/:slug
                  │
                  ▼
        WikiPageClient.tsx
          wrapClaimComments() → <span data-claim-id>
          wrapCitationComments() → <span data-cite-ids></span>
                  │
                  ▼
        ReactMarkdown + remarkMath + rehypeKatex
                  │
                  ▼
        span renderer:
          - data-cite-ids → return null  (hides ALL aligned cites)
          - data-claim-id → wrap in ClaimAnnotatedSpan
          - else → passthrough
                  │
                  ▼
        Browser renders:
          - aligned cites: gone
          - unaligned cites: visible as raw "(Author Year)"
          - mixed unicode/LaTeX math: partial KaTeX, partial raw chars
          - bare subscripts: literal or runaway emphasis
```

The two interlocking problems: (a) the renderer's hide-everything rule conflicts with reality (unmatched cites stay visible), and (b) no canonicalization step exists between LLM output and DB storage.

---

## 3. Target Architecture

### 3.1 Layer responsibilities

| Layer | Where | Responsibility |
|---|---|---|
| **A. LLM prompt** | `proposers.py`, `tasks.py:sonnet_section_rewrite`, `tasks.py:synthesize_renovation` | Instruct models to emit `<!--cite:N-->` markers, never `(Author Year)` parens. Already specified in `dynamic_citations_design_v1.md §6` — extend with explicit "use `$…$` for all math, no `\(…\)`, no raw Unicode super/sub" rule. |
| **B. Write-time canonicalizer** | `app/services/content_canonicalizer.py` (new), invoked as Celery hook after every `wiki_pages.content` commit | Idempotently normalize math, Unicode, and parenthetical citations into canonical forms. Source of truth: clean DB content. |
| **C. Multi-cite tokenizer** | `scripts/align_citations.py` (refactored) | Decompose multi-cite parentheticals into atomic author-year keys before resolution; map each key to evidence; emit one `<!--cite:N-->` per matched key. |
| **D. Frontend safety preprocessor** | `frontend/src/app/wiki/[slug]/WikiPageClient.tsx` (new module `markdownNormalize.ts`) | Last-line defence: catch anything that slipped through B/C — wrap bare `Var_subscript`, convert `\(…\)` to `$…$`, escape orphan underscores. |
| **E. Citation renderer** | `WikiPageClient.tsx` | Render every cited assertion as a numbered superscript `[1]…[n]`. No more `null`-return hide rule. |

### 3.2 Canonical content invariants (post-canonicalizer)

After Layer B runs, `wiki_pages.content` must satisfy these invariants:

| # | Invariant | Verified by |
|---|---|---|
| C1 | Zero `(Author Year)` parentheticals outside `<!--cite:N-->` markers. Multi-cite parens are decomposed into multiple `<!--cite:N-->` markers. Unmatched parens become `<!--cite-unmatched:Author Year-->` (sentinel comment, no evidence ID). | `tests/canonicalize/test_citations.py` — regex scan of corpus. |
| C2 | Zero raw Unicode super/sub chars (`⁰⁻⁹₀₋₉`) outside `<!--…-->` comments and `$…$` math spans. | Regex scan. |
| C3 | Zero standalone `★ ⋆ ☉ ⊙` outside `$…$` math spans. | Regex scan. |
| C4 | Zero `\(…\)` or `\[…\]` LaTeX paren-delimited math. All math is `$…$` or `$$…$$`. | Regex scan. |
| C5 | Zero bare `[A-Za-z]_[A-Za-z]+` subscript patterns outside `$…$`. | Regex scan. |
| C6 | Idempotence: `canonicalize(canonicalize(content)) == canonicalize(content)`. | Test fixture. |
| C7 | No composite breaks: `$…$` must not be followed by a Unicode super/sub char without intervening whitespace. | Regex scan: `\$[^$]+\$[·•]?[⁰-⁹⁻]` count must be 0. |

These invariants give a single, machine-checkable definition of "clean content." Layer D's frontend preprocessor handles the residual case where some edge slipped through (e.g., a manual edit through the API that bypassed the canonicalizer); it does **not** become the primary defense.

### 3.3 Citation display policy — unified standard

**Decision: numbered superscripts, always visible, with reference list at page bottom (Wikipedia/Nature convention).**

Rejected alternatives:
- *Hide everything* (current state): no inline navigation; readers cannot tell which assertions are cited. Also fails on unaligned cites that slip through.
- *Year-only badges* (`²⁰²³`): ambiguous for multi-paper years; non-standard for scientific prose.
- *Show full author text*: clutters prose; defeats the cleanup that LLMs do.

**Numbered superscripts are the right choice because:**
- Standard scholarly convention; readers know what `[1]` means.
- Numbering is deterministic and sequential (first appearance order).
- Duplicate suppression is free (second occurrence of evidence_id 8550 reuses `[1]`).
- Compact (`[12]` is two glyphs); does not break paragraph flow.
- Unaligned cites get a distinct visual (`[?]` with tooltip) — the discrepancy disappears because aligned and unaligned are both *visible*, just visually differentiated.

**Rendering rules:**

| Input | Output |
|---|---|
| `<!--cite:8550-->` | `<sup class="cite-num" data-cite-ids="8550" data-seq="1"><a href="#ref-1">[1]</a></sup>` |
| `<!--cite:8550,8554-->` | `<sup class="cite-num" data-cite-ids="8550,8554" data-seqs="1,2"><a href="#ref-1">[1]</a><a href="#ref-2">,&nbsp;[2]</a></sup>` |
| `<!--cite-unmatched:Tremaine et al. 2002-->` | `<sup class="cite-unmatched" title="Tremaine et al. 2002 — not yet linked to evidence">[?]</sup>` |

**View-mode toggle** (NavBar control, persists in localStorage): `Numbered` (default) / `Hidden` (clean prose, no superscripts). The `Hidden` mode hides every `<sup class="cite-…">`. The `Citation View` colour toggle that exists today (`showColors` state in `WikiPageClient.tsx:518`) is orthogonal and continues to control claim-trust underlines.

The References section already exists in the renderer (`WikiPageClient.tsx:878-896`). It will be extended to consume the new sequential numbering (one `<li id="ref-N">` per unique evidence_id, in first-appearance order).

### 3.4 Math normalization grammar

The canonicalizer (Layer B) operates on five grammar productions. Each is deterministic, idempotent, and applied in fixed order to prevent the composite-break failure mode.

```
S0  ::=  RAW_CONTENT
S1  ::=  protect_existing_math(S0)        # extract $...$ and <!--...--> into placeholders
S2  ::=  normalize_latex_delim(S1)        # \(...\) → $...$, \[...\] → $$...$$
S3  ::=  fuse_composite_unicode(S2)       # 10⁻⁵ → $10^{-5}$, M★ → $M_\star$, etc.
S4  ::=  wrap_bare_subscripts(S3)         # T_vir → $T_{\text{vir}}$  (outside placeholders)
S5  ::=  escape_orphan_underscores(S4)    # any remaining bare _word_ → \_word\_
S6  ::=  restore_placeholders(S5)         # re-inject the protected $...$ and <!--...-->
S7  ::=  verify_invariants(S6)            # raise on any C1–C7 violation
```

**Production details:**

```python
# S1 — protect_existing_math
MATH_INLINE_RE = re.compile(r"\$[^$\n]+\$")
MATH_BLOCK_RE  = re.compile(r"\$\$[^$]+\$\$", re.DOTALL)
HTML_COMMENT_RE = re.compile(r"<!--[\s\S]*?-->")
CODE_FENCE_RE  = re.compile(r"```[\s\S]*?```")
HTML_SPAN_RE   = re.compile(r"<span [^>]*>[^<]*</span>")  # data-cite-ids wraps

# S2 — normalize_latex_delim
LATEX_PAREN_INLINE_RE = re.compile(r"\\\((.+?)\\\)", re.DOTALL)   # \(...\)  → $...$
LATEX_PAREN_BLOCK_RE  = re.compile(r"\\\[(.+?)\\\]", re.DOTALL)   # \[...\]  → $$...$$

# S3 — fuse_composite_unicode
SUP_TABLE = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺", "0123456789-+")
SUB_TABLE = str.maketrans("₀₁₂₃₄₅₆₇₈₉₋₊", "0123456789-+")
SYMBOL_MAP = {
    "★": r"\star", "⋆": r"\star", "☉": r"\odot", "⊙": r"\odot",
    "∝": r"\propto", "≈": r"\approx", "≲": r"\lesssim", "≳": r"\gtrsim",
    "≪": r"\ll", "≫": r"\gg", "≤": r"\le", "≥": r"\ge",
    "ρ": r"\rho", "σ": r"\sigma", "τ": r"\tau", "δ": r"\delta",
    "Δ": r"\Delta", "Ω": r"\Omega", "ω": r"\omega", "μ": r"\mu",
}

# Composite token regex: matches an entire mathematical expression
# (number + optional super/sub + optional decimal + optional symbol)
COMPOSITE_RE = re.compile(
    r"(?P<base>\d+(?:\.\d+)?)"
    r"(?P<sup>[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺·.]*[⁰¹²³⁴⁵⁶⁷⁸⁹]+)"   # at least one super
    r"(?:\s*(?P<unit>(?:M|R|L|T|N|H|f|k|n|σ|ρ|τ)[★⋆☉⊙_]?\w*))?"
)
MASS_RE = re.compile(r"\bM([★⋆☉⊙])")  # M★, M⋆, M☉, M⊙

# S4 — wrap_bare_subscripts
BARE_SUBSCRIPT_RE = re.compile(
    r"\b([A-Za-zρστωΔΩμ])_([A-Za-z]\w*)\b"     # X_subscript
)

# S5 — escape_orphan_underscores
ORPHAN_UNDERSCORE_RE = re.compile(r"(?<![\w\\])_([A-Za-z][\w\-]+)_(?!\w)")
```

**Order rationale:**
- S2 before S3: `\(M_h\)` becomes `$M_h$` first, then the `M_h` inside is protected; S3/S4 will not re-wrap it.
- S3 before S4: composite expressions like `M★` or `10⁻⁵` are atomic units; wrap them as whole `$M_\star$` / `$10^{-5}$` so the trailing scalar (`·⁸`) is captured in the same span.
- S4 after S3: only bare `T_vir`-style identifiers that survived S3 get wrapped.
- S5 last: only orphans (no nearby math) remain.

**Composite-break prevention (C7):**

After S3, run a post-pass:
```python
def merge_adjacent_math(text: str) -> str:
    # $a$$b$ → $a b$  (adjacent inline math fusion)
    # $a$·⁸  → $a^{0.8}$  (suffix super/sub absorption — already handled in S3 but defensive)
    text = re.sub(r"\$([^$]+)\$\$([^$]+)\$", r"$\1 \2$", text)
    text = re.sub(
        r"\$([^$]+)\$[·•]([⁰¹²³⁴⁵⁶⁷⁸⁹]+)",
        lambda m: f"${m.group(1)}.{m.group(2).translate(SUP_TABLE)}$",
        text,
    )
    return text
```

### 3.5 Frontend safety preprocessor

A pure-function module `markdownNormalize.ts`, called *before* `ReactMarkdown` in `WikiPageClient.tsx`. It mirrors a subset of the backend canonicalizer (axes 2 + 4) so manual API writes or stale pre-canonicalizer content still render correctly.

```typescript
// frontend/src/app/wiki/[slug]/markdownNormalize.ts

const LATEX_PAREN_INLINE = /\\\((.+?)\\\)/g;
const LATEX_PAREN_BLOCK  = /\\\[(.+?)\\\]/g;
const BARE_SUBSCRIPT     = /\b([A-Za-zρστωΔΩμ])_([A-Za-z]\w*)\b/g;
const ORPHAN_UNDERSCORE  = /(?<![\w\\])_([A-Za-z][\w\-]+)_(?!\w)/g;
const COMPOSITE_BREAK    = /\$([^$]+)\$[·•]([⁰¹²³⁴⁵⁶⁷⁸⁹]+)/g;
const STAR_SUN_RAW       = /\b([A-Z])([★⋆☉⊙])/g;

const SUP_MAP: Record<string, string> = {
  "⁰":"0","¹":"1","²":"2","³":"3","⁴":"4","⁵":"5","⁶":"6","⁷":"7","⁸":"8","⁹":"9","⁻":"-","⁺":"+",
};
const SYMBOL_MAP: Record<string, string> = {
  "★":"\\star","⋆":"\\star","☉":"\\odot","⊙":"\\odot",
};

export function normalizeMarkdown(input: string): string {
  // Protect math, HTML comments, code fences, and existing data-cite-ids spans.
  const placeholders: string[] = [];
  const stash = (m: string) => {
    placeholders.push(m);
    return `\x00${placeholders.length - 1}\x00`;
  };
  let text = input;
  text = text.replace(/```[\s\S]*?```/g, stash);
  text = text.replace(/<!--[\s\S]*?-->/g, stash);
  text = text.replace(/<span [^>]*>[^<]*<\/span>/g, stash);
  text = text.replace(/\$\$[\s\S]+?\$\$/g, stash);
  text = text.replace(/\$[^$\n]+?\$/g, stash);

  // S2: \( … \) → $ … $
  text = text.replace(LATEX_PAREN_INLINE, (_m, body) => `$${body}$`);
  text = text.replace(LATEX_PAREN_BLOCK,  (_m, body) => `$$${body}$$`);

  // S3: composite Unicode fusion (run before bare-subscript wrap)
  text = text.replace(/(\d+(?:\.\d+)?)([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺·.]*[⁰¹²³⁴⁵⁶⁷⁸⁹]+)/g, (_m, base, sup) => {
    const decoded = sup.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]/g, (c: string) => SUP_MAP[c] ?? c).replace(/·/g, ".");
    return `$${base}^{${decoded}}$`;
  });
  text = text.replace(STAR_SUN_RAW, (_m, letter, sym) => `$${letter}_${SYMBOL_MAP[sym]}$`);

  // S4: bare subscripts → wrapped math
  text = text.replace(BARE_SUBSCRIPT, (_m, head, sub) => `$${head}_{\\text{${sub}}}$`);

  // S5: orphan underscores (escape, do not wrap)
  text = text.replace(ORPHAN_UNDERSCORE, (_m, word) => `\\_${word}\\_`);

  // Defensive: any composite breaks that survived (shouldn't, but cheap to fix)
  text = text.replace(COMPOSITE_BREAK, (_m, body, sup) => {
    const decoded = sup.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]/g, (c: string) => SUP_MAP[c] ?? c);
    return `$${body}.${decoded}$`;
  });

  // Restore placeholders
  text = text.replace(/\x00(\d+)\x00/g, (_m, idx) => placeholders[Number(idx)]);
  return text;
}
```

Wire-in (single line in `WikiPageClient.tsx`):

```typescript
// Replace line 628:
const processedContent = wrapCitationComments(wrapClaimComments(unwrapCodeFence(stripLeadingH1(normalizeMarkdown(page.content)))));
```

The preprocessor is **stateless and pure** — testable in isolation, no React state. Run-cost: a handful of regex passes over a ~62k-char string; sub-millisecond.

### 3.6 Multi-cite tokenizer (Axis 3)

Replace `align_citations.py:79 extract_citations` and the two top-level regexes with a two-stage tokenizer:

```python
# Stage 1 — find every outer parenthetical block
OUTER_PAREN_RE = re.compile(r"\(([^()\n]{2,300})\)")

# Stage 2 — given an outer body, split into atomic author-year units
SINGLE_AUTHORYEAR_RE = re.compile(
    r"(?:(?:e\.g\.|i\.e\.|cf\.|see)\s*,?\s*)?"          # optional discourse marker
    r"(?P<authors>[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’.\-]+"
    r"(?:\s+et\s+al\.?"
    r"|\s*&\s*[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’.\-]+"
    r"|\s+and\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’.\-]+)?)"
    r"\s+(?P<year>(?:19|20)\d{2})[a-z]?",
    re.UNICODE,
)

def tokenize_paren_citations(content: str) -> list[CitationMatch]:
    """Return one CitationMatch per atomic author-year, even if the source
    parenthetical contained multiple semicolon-separated citations."""
    matches: list[CitationMatch] = []
    for outer in OUTER_PAREN_RE.finditer(content):
        body = outer.group(1)
        # Drop obvious non-citation parens early: must contain a 4-digit year
        if not re.search(r"\b(?:19|20)\d{2}", body):
            continue
        # Split on ';' (unambiguous multi-cite separator)
        parts = [p.strip() for p in body.split(";")]
        # Also split on ',' if and only if multiple year-tokens appear and no '&'
        if len(parts) == 1 and len(re.findall(r"\b(?:19|20)\d{2}", body)) >= 2 and "&" not in body:
            parts = [p.strip() for p in body.split(",")]
        # Compute offsets into the original document for replacement
        cursor = outer.start() + 1  # position after the opening '('
        for raw in parts:
            sub_idx = content.find(raw, cursor, outer.end())
            if sub_idx < 0:
                continue
            for m in SINGLE_AUTHORYEAR_RE.finditer(raw):
                key, first, yr = _canonical_key(m.group("authors"), m.group("year"))
                # Anchor the replacement on the FULL outer paren on first encounter,
                # and emit zero-width markers for subsequent atoms (so the closing
                # `)` is collapsed exactly once).
                matches.append(CitationMatch(
                    start=sub_idx + m.start(),
                    end=sub_idx + m.end(),
                    raw=m.group(0),
                    author_year_key=key,
                    first_author=first,
                    year=yr,
                ))
            cursor = sub_idx + len(raw)
    return sorted(matches, key=lambda c: c.start)
```

**Replacement strategy for multi-cite blocks:**

Given `(Fabian 2012; Heckman & Best 2014)`:

1. Tokenize → two `CitationMatch` instances: `(Fabian 2012, evidence_id=8550)`, `(Heckman & Best 2014, evidence_id=8554)`.
2. Resolve each independently via `find_evidence`.
3. Replace the **entire outer parenthetical** with the concatenated marker sequence:
   ```
   <!--cite:8550--><!--cite:8554-->
   ```
4. If one of the two cannot be resolved, emit the matched one as `<!--cite:N-->` and the unmatched one as `<!--cite-unmatched:Heckman & Best 2014-->`. Never silently drop.

For `(e.g., Labbé et al. 2023)`: the `e.g.,` is stripped by the `(?:(?:e\.g\.…)?\s*,?\s*)?` prefix in `SINGLE_AUTHORYEAR_RE`. The result is a single citation.

### 3.7 Sentinel for unmatched citations

Today, unmatched parens stay as raw text in prose — that's the root cause of Papa's Axis 1 discrepancy. New rule: every parenthetical that **looks like** a citation but cannot be matched to evidence is rewritten to a sentinel comment:

```html
<!--cite-unmatched:Tremaine et al. 2002-->
```

This is invisible in the DB (it's an HTML comment), and the frontend renders it as `[?]` superscript with a tooltip. The reader sees a uniform inline-superscript citation experience; no raw "(Author Year)" leaks through.

**Why the comment-marker convention is essential:** if we leave unmatched cites as raw text, every renovation cycle treats them as a "new" paren and retries the alignment — leading to the volatile state described in `dynamic_citations_design_v1.md §2.1`. Comments are dead text to the LLM; they survive intact.

The sentinel also enables a daily Celery job (`scripts/relink_unmatched.py`, owner Tori) that re-resolves `<!--cite-unmatched:…-->` comments against the (growing) evidence table; when a match is found, the sentinel is upgraded to `<!--cite:N-->`. This is the same architecture as the `unknown_cite_ids` strip in `align_citations.py:269`, but for unmatched parens instead of hallucinated IDs.

### 3.8 Backend canonicalizer module

```python
# backend/app/services/content_canonicalizer.py

from dataclasses import dataclass
import re

from app.services.citation_normalize import normalize_citations  # uses align_citations.tokenize_paren_citations

@dataclass
class CanonicalizeResult:
    new_content: str
    changes: dict[str, int]   # {axis: count} for telemetry
    invariants_ok: bool

def canonicalize(content: str, page_id: int | None = None, db=None) -> CanonicalizeResult:
    placeholders: list[str] = []
    def stash(m): placeholders.append(m.group(0)); return f"\x00{len(placeholders)-1}\x00"
    text = content
    # Protect
    text = re.sub(r"```[\s\S]*?```", stash, text)
    text = re.sub(r"<!--[\s\S]*?-->", stash, text)
    text = re.sub(r'<span [^>]*>[^<]*</span>', stash, text)
    text = re.sub(r"\$\$[\s\S]+?\$\$", stash, text)
    text = re.sub(r"\$[^$\n]+?\$", stash, text)

    # Axis 2 — LaTeX paren delimiters
    text, n_paren = re.subn(r"\\\((.+?)\\\)", r"$\1$", text, flags=re.DOTALL)
    text, n_brack = re.subn(r"\\\[(.+?)\\\]", r"$$\1$$", text, flags=re.DOTALL)

    # Axis 4 — composite unicode fusion (number + sup)
    def _fuse_num_sup(m):
        sup = m.group(2).translate(SUP_TABLE).replace("·", ".")
        return f"${m.group(1)}^{{{sup}}}$"
    text, n_num_sup = re.subn(r"(\d+(?:\.\d+)?)([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺·.]*[⁰¹²³⁴⁵⁶⁷⁸⁹]+)", _fuse_num_sup, text)

    # Axis 4 — symbol fusion (X★ → $X_\star$)
    text, n_sym = re.subn(r"\b([A-Za-z])([★⋆☉⊙])",
                         lambda m: f"${m.group(1)}_{SYMBOL_MAP[m.group(2)]}$", text)

    # Axis 4 — Greek/symbol replacement when followed by '_' (bare subscript variant)
    text, n_greek = re.subn(
        r"([ρστωΔΩμδ])_([A-Za-z]\w*)",
        lambda m: f"${SYMBOL_MAP[m.group(1)]}_{{\\text{{{m.group(2)}}}}}$",
        text,
    )

    # Axis 2 — bare subscript variables (T_vir, R_e, etc.)
    text, n_bare = re.subn(
        r"\b([A-Za-z])_([A-Za-z]\w*)\b",
        lambda m: f"${m.group(1)}_{{\\text{{{m.group(2)}}}}}$",
        text,
    )

    # Axis 2 — orphan underscore pairs (em-run risk)
    text, n_orphan = re.subn(r"(?<![\w\\])_([A-Za-z][\w\-]+)_(?!\w)", r"\\_\1\\_", text)

    # Axis 4 — defensive: merge adjacent math + clean composite breaks
    text = re.sub(r"\$([^$]+)\$\$([^$]+)\$", r"$\1 \2$", text)
    text, n_comp = re.subn(
        r"\$([^$]+)\$[·•]([⁰¹²³⁴⁵⁶⁷⁸⁹]+)",
        lambda m: f"${m.group(1)}.{m.group(2).translate(SUP_TABLE)}$",
        text,
    )

    # Restore protected segments
    text = re.sub(r"\x00(\d+)\x00", lambda m: placeholders[int(m.group(1))], text)

    # Axis 3 — citation normalization (only if page_id+db provided)
    n_cite = 0
    if page_id and db:
        text, n_cite = normalize_citations(db, page_id, text)

    changes = {
        "latex_paren": n_paren + n_brack,
        "num_sup":    n_num_sup,
        "symbol":     n_sym + n_greek,
        "bare_sub":   n_bare,
        "orphan_us":  n_orphan,
        "composite":  n_comp,
        "cite":       n_cite,
    }
    ok = _verify_invariants(text)
    return CanonicalizeResult(text, changes, ok)


def _verify_invariants(text: str) -> bool:
    body = re.sub(r"<!--[\s\S]*?-->", "", text)
    body = re.sub(r"<span [^>]*>[^<]*</span>", "", body)
    body = re.sub(r"```[\s\S]*?```", "", body)
    body = re.sub(r"\$[^$\n]+?\$", "", body)
    body = re.sub(r"\$\$[\s\S]+?\$\$", "", body)
    # All invariants C1–C7 reduce to "no failure-pattern in body":
    if re.search(r"\([A-Z][A-Za-z\-']+(?:\s+et\s+al\.?)?\s+(?:19|20)\d{2}[a-z]?\)", body): return False
    if re.search(r"[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺₀-₉]", body): return False
    if re.search(r"[★⋆☉⊙]", body): return False
    if re.search(r"\\\(|\\\[", body): return False
    if re.search(r"\b[A-Za-z]_[A-Za-z]\w+\b", body): return False
    if re.search(r"\$[^$]+\$[·•]?[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]", text): return False
    return True
```

**Hook sites** (all post-commit):

```python
# backend/app/agent_loop/autowiki/tasks.py
def _run_canonicalize_and_align(page_id: int):
    with SessionLocal() as db:
        page = db.get(WikiPage, page_id)
        if not page: return
        result = canonicalize(page.content, page_id=page_id, db=db)
        if result.new_content != page.content:
            db.add(PageVersion(page_id=page.id, version_num=..., content=result.new_content,
                              source_note=f"canonicalize:{result.changes}"))
            page.content = result.new_content
            db.commit()
        align_page(db, page, dry_run=False, bootstrap=False)
        db.commit()

# Call sites (add `canonicalize_page.delay(page_id)` after each):
#   - sonnet_section_rewrite (after commit)
#   - synthesize_renovation (after commit)
#   - routers/pages.py update_page_content (after commit)
#   - any new write path (e.g., human edit application)
```

The Celery task is `bind=True, autoretry_for=(Exception,), max_retries=2`, but **never** clobbers content silently on invariant failure: if `result.invariants_ok` is `False`, write the candidate to `pages.content_canonicalize_failed_at` (new column, nullable timestamp) and skip the content swap. Daily report job alerts on any failure.

---

## 4. Frontend Citation Renderer

### 4.1 Marker-to-superscript transform

Replace the current `wrapCitationComments` (`WikiPageClient.tsx:145`) and the span hide-rule (line 847) with a new sequential numbering pass:

```typescript
// frontend/src/app/wiki/[slug]/citationRenderer.ts

interface CiteNumbering {
  seqByEvidenceId: Map<number, number>;     // evidence_id → [n]
  seqs: number[];                            // ordered seq list for References render
}

export function assignCitationSeqs(content: string): { content: string; numbering: CiteNumbering } {
  const seqByEvidenceId = new Map<number, number>();
  let nextSeq = 1;

  // Pass 1 — assign seq numbers in document order
  content.replace(/<!--cite:([\d,\s]+)-->/g, (_m, ids) => {
    const idList = ids.split(",").map((s: string) => parseInt(s.trim(), 10)).filter(Number.isFinite);
    for (const id of idList) {
      if (!seqByEvidenceId.has(id)) {
        seqByEvidenceId.set(id, nextSeq++);
      }
    }
    return "";
  });

  // Pass 2 — rewrite markers into <sup data-cite-ids data-seqs>
  const out = content.replace(/<!--cite:([\d,\s]+)-->/g, (_m, ids) => {
    const idList = ids.split(",").map((s: string) => parseInt(s.trim(), 10)).filter(Number.isFinite);
    const seqs = idList.map(id => seqByEvidenceId.get(id) ?? 0).filter(n => n > 0);
    const links = seqs.map((n, i) => `<a href="#ref-${n}">[${n}]</a>${i < seqs.length - 1 ? "," : ""}`).join("");
    return `<sup class="cite-num" data-cite-ids="${idList.join(",")}" data-seqs="${seqs.join(",")}">${links}</sup>`;
  });

  // Pass 3 — rewrite unmatched sentinels
  const finalOut = out.replace(/<!--cite-unmatched:([^>]+?)-->/g, (_m, raw) => {
    const safeText = raw.replace(/"/g, "&quot;");
    return `<sup class="cite-unmatched" title="${safeText} — not yet linked to evidence">[?]</sup>`;
  });

  return { content: finalOut, numbering: { seqByEvidenceId, seqs: Array.from(seqByEvidenceId.values()) } };
}
```

### 4.2 Wire-in in `WikiPageClient.tsx`

Replace lines 628 and 844-871 (`processedContent` computation and the `span` renderer's hide-everything rule). The new path:

```typescript
// Line 628 area:
const normalized = normalizeMarkdown(unwrapCodeFence(stripLeadingH1(page.content)));
const { content: numbered, numbering } = assignCitationSeqs(normalized);
const processedContent = wrapClaimComments(numbered);
// Note: wrapCitationComments is DELETED. Markers are now <sup> not <span data-cite-ids>.

// New `components` config — drop the cite-hide rule, add sup handler:
components={{
  // … (existing h1/h2/h3/p/ul/ol/li/strong/blockquote/code unchanged) …
  sup: ({ node, children, ...props }: any) => {
    const className = props.className;
    if (className === "cite-num") {
      const ids = String(props["data-cite-ids"] ?? "").split(",").map(Number).filter(Number.isFinite);
      const seqs = String(props["data-seqs"] ?? "").split(",").map(Number).filter(Number.isFinite);
      const cites = ids.map(id => citationByEvidenceId[id]).filter(Boolean);
      return <CitationSuperscript seqs={seqs} citations={cites} />;
    }
    if (className === "cite-unmatched") {
      return <sup className="cite-unmatched" title={props.title}>{children}</sup>;
    }
    return <sup {...props}>{children}</sup>;
  },
  span: ({ node, children, ...props }: any) => {
    const claimId = props["data-claim-id"];
    // (claim-span logic unchanged from existing lines 845-870, MINUS the data-cite-ids branch)
    if (claimId && showV2) { /* … existing ClaimAnnotatedSpan stacking … */ }
    return <span {...props}>{children}</span>;
  },
}}
```

`CitationSuperscript` is a new component (10 LOC: hover/click reveals a popover identical to the existing `CitationPopover` at line 244, which is then deleted from its current call sites).

### 4.3 References section

`WikiPageClient.tsx:878-896` already renders a References list, but it sorts by `citation.seq` from the API. With the new sequential numbering done at render time, the order must be derived from `numbering.seqByEvidenceId` instead:

```typescript
const orderedCitations = useMemo(() => {
  return Array.from(numbering.seqByEvidenceId.entries())
    .sort((a, b) => a[1] - b[1])
    .map(([evidenceId, seq]) => ({ seq, ...citationByEvidenceId[evidenceId] }))
    .filter(c => c.evidence_id);   // drop entries with no metadata
}, [numbering, citationByEvidenceId]);
```

The `/api/pages/:slug/citations` endpoint stays as-is (returns evidence metadata indexed by evidence_id); the numbering is purely a client-side concern.

### 4.4 View-mode toggle

Add a third toggle button next to "Citation View / Raw Text" in `WikiPageClient.tsx:766-810`:

```tsx
const [citeMode, setCiteMode] = useState<"numbered" | "hidden">(
  () => (typeof window !== "undefined" && localStorage.getItem("nm.cite_mode")) === "hidden" ? "hidden" : "numbered"
);

useEffect(() => { if (typeof window !== "undefined") localStorage.setItem("nm.cite_mode", citeMode); }, [citeMode]);

<button onClick={() => setCiteMode(m => m === "numbered" ? "hidden" : "numbered")}>
  {citeMode === "numbered" ? "Hide citations" : "Show citations"}
</button>

// CSS: when citeMode === "hidden", emit `<style>.cite-num, .cite-unmatched { display: none; }</style>` once.
```

This satisfies both ends of the spectrum Papa described — readers who want clean textbook prose can toggle off; default is scholarly numbered superscripts.

---

## 5. Implementation Sequence (for Tori)

Strict dependency order. Each step is independently testable; do not skip ahead.

### 5.1 Backend

| # | Task | File | Tests |
|---|---|---|---|
| 1 | Add `app/services/content_canonicalizer.py` with `canonicalize()` and `_verify_invariants()` (§3.8). | new file | `tests/canonicalize/test_axis2.py` (LaTeX-paren), `test_axis4.py` (Unicode), `test_idempotence.py` (C6). |
| 2 | Refactor `scripts/align_citations.py`: replace `PAREN_CITE_RE` + `NARRATIVE_CITE_RE` with `OUTER_PAREN_RE` + `tokenize_paren_citations()` (§3.6). Keep `find_evidence`, `upsert_link`, `bootstrap_page_links` unchanged. | `scripts/align_citations.py` | `tests/citations/test_multi_cite.py` — fixtures: `(Fabian 2012; Heckman & Best 2014)`, `(e.g., Labbé et al. 2023)`, `(Boylan-Kolchin 2023; arXiv:2605.03635)`. |
| 3 | Add unmatched-cite sentinel emission: extend `replace_citations()` to emit `<!--cite-unmatched:Author Year-->` for any `ResolvedCitation` with `evidence_id is None` (§3.7). | `scripts/align_citations.py` | `test_unmatched_sentinel.py`. |
| 4 | Wire the Celery hook `canonicalize_page.delay(page_id)` at three commit sites (`sonnet_section_rewrite`, `synthesize_renovation`, `routers/pages.py:update_page_content`). | `tasks.py`, `routers/pages.py` | integration test: write content → assert canonical form after Celery flush. |
| 5 | Add `scripts/canonicalize_corpus.py` for one-shot full backfill: iterate all `wiki_pages`, run `canonicalize()`, commit with `source_note='canonicalize_backfill_v1'`. | new file | dry-run mode required; `--dry-run` prints diff stats per page. |
| 6 | Delete `scripts/convert_all_unicode_masses.py`, `scripts/convert_all_math_to_dollars.py`, `scripts/fix_more_math.py` (superseded by §3.8). | n/a | grep ensures no callers. |
| 7 | Add `scripts/relink_unmatched.py`: Celery task scanning `<!--cite-unmatched:…-->` daily, re-resolving against current evidence, upgrading to `<!--cite:N-->` on match. | new file | `test_relink.py` — fixture: add new evidence row, run relink, assert sentinel upgrade. |

### 5.2 Frontend

| # | Task | File | Tests |
|---|---|---|---|
| 8 | Add `frontend/src/app/wiki/[slug]/markdownNormalize.ts` with `normalizeMarkdown()` (§3.5). Pure function; no React deps. | new file | Jest: snapshot fixtures for each axis. |
| 9 | Add `frontend/src/app/wiki/[slug]/citationRenderer.ts` with `assignCitationSeqs()` (§4.1). | new file | Jest: numbering deterministic, duplicate suppression. |
| 10 | In `WikiPageClient.tsx`: replace line 628 to use `normalizeMarkdown()` → `assignCitationSeqs()` → `wrapClaimComments()`. Delete `wrapCitationComments()` (lines 145-151). | edit | RTL: render fixture page, assert `<sup class="cite-num">` count matches `<!--cite:N-->` count. |
| 11 | In `WikiPageClient.tsx`: remove the `data-cite-ids` hide branch (lines 847-851). Add `sup` component handler (§4.2). | edit | RTL: rendered page contains no `null`-returning span; aligned cites are visible. |
| 12 | Add `CitationSuperscript` component (popover on click/hover; uses `citationByEvidenceId` map). Reuse existing `CitationPopover` layout (line 244). | new component | RTL: click → popover; second click → close. |
| 13 | Update References section (§4.3) to consume `numbering.seqByEvidenceId` instead of API `citation.seq`. | edit | RTL: References list order matches first-appearance order. |
| 14 | Add `citeMode` toggle (§4.4) with `localStorage` persistence. | edit | RTL: toggle button switches `display: none` on `.cite-num`. |

### 5.3 Migration & Verification

| # | Task | Owner | Notes |
|---|---|---|---|
| 15 | Run `scripts/canonicalize_corpus.py --dry-run --report /tmp/canonicalize_report.json`. | Tori | Send report to Kun for review. |
| 16 | Review unmatched-cite count and invariant violations per page. | Kun | Spot-check 5 pages; flag any page with > 20% drift. |
| 17 | Run `scripts/canonicalize_corpus.py` (no dry-run) after Kun sign-off. | Tori | One commit per page; each writes a new `page_versions` row. |
| 18 | Run `scripts/align_citations.py --all-pages` to re-resolve multi-cite tokenizer matches. | Tori | Expect 48 new `page_citation_links` rows for the previously-broken multi-cites. |
| 19 | Frontend deploy. | Tori | Verify on page 57 + 4 other corpus pages from §3.2 stats. |
| 20 | Verification audit: re-run the empirical scan from §1 — all failure counts must be `0`. | Kun | Sign-off blocker. |

---

## 6. Platoon Assignment

Every code change in this plan is **deterministic Python or TypeScript** — no LLM is in the data path. The only role for platoon models is (a) the LLM rewrite prompts (already covered in `dynamic_citations_design_v1.md §6`) and (b) post-deploy QA audit. The breakdown:

| Step | Owner | Host | Why | Cost |
|---|---|---|---|---|
| Backend canonicalizer (§3.8) | Tori — deterministic Python | Mac Studio | Pure regex pipeline, must be reproducible; LLM would introduce variance | $0 |
| Multi-cite tokenizer (§3.6) | Tori — deterministic Python | Mac Studio | Same | $0 |
| Frontend `normalizeMarkdown` (§3.5) | Tori — deterministic TS | Mac Studio | Same | $0 |
| Frontend citation renderer (§4) | Tori — React | Mac Studio | UI logic | $0 |
| Corpus dry-run scan | Tori — deterministic Python | Mac Studio | Iterates 43 pages, ~5 s total | $0 |
| Dry-run report review (5-page spot-check) | **Kun — Claude Opus 4.7** | Mac Pro | Needs judgment on edge cases (does this canonicalization preserve meaning? Is this Unicode symbol intentional or noise?) | ~$0.10 |
| LLM prompt updates (cite + math rules) | Existing autowiki platoon (Sonnet 4.6 / AstroSage-70B) | unchanged | No model migration; prose-rewriting prompt strings only | unchanged |
| Post-deploy QA — verify all four axes are 0 across corpus | **Kun — Claude Opus 4.7** | Mac Pro | Pattern check + visual review of 5 randomly chosen pages | ~$0.20 |
| Relink job (daily) | Tori — deterministic Python (Celery beat) | Mac Studio | Scans for `<!--cite-unmatched:…-->`, re-resolves; runs in <30 s | $0 |

**No Buddle / Rakon / Blanc involvement** — the local Ollama platoon plays no role in this design. The deterministic-Python preference is by design: rendering correctness is a *grammar* problem, not a *judgment* problem, and grammars should be enforced by parsers, not by sampling temperatures.

**No Mac-Pro Ollama** — all canonicalization runs locally on Mac Studio where the DB lives. No cross-machine traffic.

---

## 7. Risk Register

| # | Risk | Mitigation |
|---|---|---|
| R1 | The canonicalizer turns valid prose into invalid math (e.g. wraps `A_B testing` as `$A_{\text{B testing}}$`). | The bare-subscript regex requires `\b[A-Za-z]_[A-Za-z]\w+\b` — single letter prefix only. "A/B testing" is not matched. Fixture: include common false-positive patterns in `test_axis2.py`. |
| R2 | The multi-cite tokenizer over-splits at commas in `(Smith, Jones & Brown 2012)` (single citation with three authors). | The comma-split branch fires only when **multiple** `(19\|20)\d{2}` years exist in the body AND no `&` separator. `(Smith, Jones & Brown 2012)` has one year and an `&`; passes through as single. |
| R3 | LaTeX paren conversion (`\(...\)` → `$...$`) misfires on prose like `e.g.\ (see §2)`. | The pattern `\\\(.+?\\\)` requires the backslash to immediately precede the paren with no whitespace; in prose `\ (` has a space. Add fixture. |
| R4 | The unmatched sentinel grows unbounded over time (every renovation introduces new author-years that don't yet have evidence). | Daily `relink_unmatched.py` job (§5.3 step 7). If a sentinel persists > 90 days, surface in admin dashboard for manual evidence import. |
| R5 | Frontend safety preprocessor and backend canonicalizer drift (one fixes a case the other doesn't). | Shared fixture set: both `tests/canonicalize/fixtures/*.md` and `frontend/__tests__/markdownNormalize.fixtures.ts` derive from the same JSON list of `{input, expected}` pairs. CI fails if the two diverge. |
| R6 | Corpus backfill misfires on a page and corrupts content. | `--dry-run` first, per-page commit, each in own `page_versions` row (rollback by row swap). Invariant verifier (`_verify_invariants`) blocks the commit if violated. |
| R7 | `\,` (LaTeX thin space) or `\!` collisions with the orphan-underscore regex. | The regex `(?<![\w\\])_([A-Za-z][\w\-]+)_` has `(?<!\\)` negative-lookbehind; `\,` and `\!` are protected. Add fixture `\, M_\odot \, \text{yr}^{-1}` to test. |
| R8 | Citation renderer breaks on `<!--cite:0-->` (zero ID, hallucinated). | `assignCitationSeqs` filters with `.filter(Number.isFinite).filter(n => n > 0)`. The `strip_hallucinated_cites` step in `align_citations.py:254` already removes IDs not in `page_citation_links`; the frontend is just a second line of defense. |

---

## 8. Acceptance Criteria

Pre-deploy:

- [ ] All seven invariants C1–C7 (§3.2) hold for every page in the corpus after canonicalizer dry-run.
- [ ] Multi-cite tokenizer correctly decomposes the 20 page-57 multi-cite samples (§2.3) into 41 atomic citations (or as many as evidence resolves).
- [ ] Frontend safety preprocessor produces identical AST to backend canonicalizer for the shared fixture set (no drift).
- [ ] Page 57 renders with zero raw `(Author Year)` parens, zero raw Unicode super/sub, zero `\(...\)` blocks.
- [ ] References section numbering matches first-appearance order on three test pages.

Post-deploy:

- [ ] Re-run §1 empirical scan: every failure count → 0.
- [ ] Spot-check 5 pages: claims, math, citations all render correctly; no regression vs current state.
- [ ] Daily `relink_unmatched.py` job processes any new sentinels within 24 h.
- [ ] LLM renovation cycle on page 57 (one section rewrite) produces clean output post-hook; no manual patches needed.

---

## 9. Open Questions

| # | Question | Default |
|---|---|---|
| 1 | Should `<!--cite-unmatched:…-->` sentinels render visibly (`[?]`) or be hidden by default? | **Visible as `[?]`.** A hidden sentinel makes the unmatched problem invisible to authors; visibility is the forcing function that gets evidence imported. |
| 2 | Should the `Hide citations` toggle persist per-page or globally? | **Globally** (localStorage `nm.cite_mode`). Per-page persistence creates state explosion. |
| 3 | When the canonicalizer changes content, should it write a new `page_versions` row, or overwrite the latest? | **New row** with `source_note='canonicalize:<changes>'`. Idempotence means most calls are no-ops; the few that aren't are visible in history. |
| 4 | Should we add a `content_canonicalize_failed_at` column on `wiki_pages` for invariant-failure tracking? | **Yes** — nullable timestamp + nullable `content_canonicalize_failure_reason` (TEXT). Surfaces in admin dashboard. |
| 5 | What's the rollback plan if the corpus backfill produces unreadable pages? | Each page's pre-backfill content is preserved in the prior `page_versions` row. Rollback = restore from the prior version. Document the rollback command in §5.3 step 17 PR. |
| 6 | Do we extend canonicalization to `wiki_page_drafts` and `edit_proposals`? | **Yes, downstream of MVP.** Same `canonicalize()` call on draft save. Out of scope for this v1; add to v1.1 if MVP is stable. |

---

## 10. Final Position

The four axes Papa surfaced are facets of one underlying defect: **NebulaMind has no canonical-form layer between LLM output and DB storage.** Every prior fix has been a per-page, per-symptom patch (`fix_more_math.py`, `convert_all_unicode_masses.py`) — and the patches now collide. The system-wide answer is a single deterministic canonicalizer with seven machine-checkable invariants, wired into every write path, with a frontend safety preprocessor as defense-in-depth.

Citation display is the same problem in a different costume: the renderer's "hide everything" rule pretended that the alignment problem was solved when in fact unaligned cites kept leaking. The unmatched-sentinel convention plus numbered superscripts make every citation *visible* and *navigable*, which is what readers actually need.

None of this requires a new LLM platoon, schema migration beyond a single nullable column, or breaking changes to the existing claim system. The risk is contained to one new module (`content_canonicalizer.py`), one refactored module (`align_citations.py`), one new TS module (`markdownNormalize.ts`), and surgical edits in `WikiPageClient.tsx`. Estimated implementation effort: 6–8 h backend + 4 h frontend + 2 h verification.

The architectural test of this design is the §1 empirical scan: after deploy, every count in the failure table must drop to zero — across the entire corpus, not just page 57.

— Kun

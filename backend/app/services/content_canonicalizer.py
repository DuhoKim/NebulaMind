from __future__ import annotations
import html
import re
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

SUP_TABLE = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺", "0123456789-+")
SUB_TABLE = str.maketrans("₀₁₂₃₄₅₆₇₈₉₋₊", "0123456789-+")

SYMBOL_MAP = {
    "★": r"\star", "⋆": r"\star", "☉": r"\odot", "⊙": r"\odot",
    "propto": r"\propto", "∝": r"\propto", "≈": r"\approx", "≲": r"\lesssim", "≳": r"\gtrsim",
    "≪": r"\ll", "≫": r"\gg", "≤": r"\le", "≥": r"\ge",
    "ρ": r"\rho", "σ": r"\sigma", "τ": r"\tau", "δ": r"\delta",
    "Δ": r"\Delta", "Ω": r"\Omega", "ω": r"\omega", "μ": r"\mu",
    "ε": r"\epsilon", "Λ": r"\Lambda", "Σ": r"\Sigma", "π": r"\pi",
}

REGISTERED_COMMENT_RE = re.compile(
    r"^<!--\s*(?:"
    r"/?claim:[\d,\s]+|"
    r"cite:[\d,\s]+|"
    r"cite-unmatched:[\s\S]*?|"
    r"EVIDENCE_HIGHLIGHTS_START|"
    r"EVIDENCE_HIGHLIGHTS_END|"
    r"/?(?:accepted|consensus|debated|challenged|unverified)"
    r")\s*-->$"
)

BARE_TEX_COMMANDS = (
    "approx",
    "gtrsim",
    "lesssim",
    "lt",
    "gt",
    "ll",
    "gg",
    "le",
    "ge",
    "pm",
    "propto",
    "sim",
    "times",
    "odot",
    "star",
    "rho",
    "sigma",
    "tau",
    "delta",
    "Delta",
    "Omega",
    "omega",
    "mu",
    "epsilon",
    "Lambda",
    "Sigma",
    "pi",
    "mathrm",
    "text",
)


class CanonicalizerError(ValueError):
    def __init__(self, violations: list[str]):
        super().__init__("Content canonicalization contract violated: " + "; ".join(violations))
        self.violations = violations


def _math_atom(value: str) -> str:
    value = value.strip()
    if value in SYMBOL_MAP:
        return SYMBOL_MAP[value]
    if any(char in SYMBOL_MAP for char in value):
        return "".join(SYMBOL_MAP.get(char, char) for char in value)
    return value


def _subscript_atom(value: str) -> str:
    value = _math_atom(value)
    if re.fullmatch(r"\\[A-Za-z]+|[A-Za-z]", value):
        return value
    if re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", value):
        return rf"\text{{{value}}}"
    return value


def _superscript_atom(value: str) -> str:
    value = value.translate(SUP_TABLE).strip()
    return value


def _legacy_cite_span_repl(match: re.Match) -> str:
    ids = ",".join(re.findall(r"\d+", match.group(1)))
    return f"<!--cite:{ids}-->" if ids else ""

@dataclass
class CanonicalizeResult:
    new_content: str
    changes: dict[str, int]
    invariants_ok: bool
    violations: list[str] | None = None


def _outside_code_fences(text: str, fn) -> str:
    parts = re.split(r"(```[\s\S]*?```)", text)
    return "".join(part if part.startswith("```") else fn(part) for part in parts)


def _decode_entities(text: str) -> str:
    return _outside_code_fences(text, html.unescape)


def _unwrap_leading_markdown_fence(text: str) -> tuple[str, int]:
    """Unwrap whole-page markdown fences before code-fence protection runs."""
    match = re.match(r"\A(?P<leading>\s*)```(?P<lang>[^\n`]*)[ \t]*(?:\n|\Z)", text)
    if not match:
        return text, 0

    lang = (match.group("lang") or "").strip().lower()
    if lang not in {"", "markdown", "md"}:
        return text, 0

    body = text[match.end():]
    if not re.search(r"(?m)^#{1,6}\s+\S", body):
        return text, 0

    close = re.search(r"(?m)^```\s*$", body)
    if close:
        body = body[:close.start()] + body[close.end():]
    return match.group("leading") + body.lstrip("\n"), 1


def _protect_regions(text: str) -> tuple[str, list[str]]:
    placeholders: list[str] = []

    def stash(m: re.Match) -> str:
        placeholders.append(m.group(0))
        return f"\x00{len(placeholders)-1}\x00"

    text = re.sub(r"```[\s\S]*?```", stash, text)
    text = re.sub(r"<!--[\s\S]*?-->", stash, text)
    text = re.sub(r"\$\$[\s\S]+?\$\$", stash, text)
    text = re.sub(r"\$[^$\n]+?\$", stash, text)
    return text, placeholders


def _restore_regions(text: str, placeholders: list[str]) -> str:
    while "\x00" in text:
        text = re.sub(r"\x00(\d+)\x00", lambda m: placeholders[int(m.group(1))], text)
    return text


def _math_html_safe(math_body: str) -> str:
    math_body = re.sub(r"(?<!\\)<", r"\\lt ", math_body)
    math_body = re.sub(r"(?<!\\)>", r"\\gt ", math_body)
    math_body = re.sub(r"&(?![A-Za-z]+;|#\d+;|#x[0-9A-Fa-f]+;)", r"\\&", math_body)
    math_body = html.unescape(math_body)
    return math_body


def _make_math_html_safe(text: str) -> tuple[str, int]:
    changes = 0

    def block_repl(m: re.Match) -> str:
        nonlocal changes
        body = _math_html_safe(m.group(1))
        if body != m.group(1):
            changes += 1
        return f"$${body}$$"

    def inline_repl(m: re.Match) -> str:
        nonlocal changes
        body = _math_html_safe(m.group(1))
        if body != m.group(1):
            changes += 1
        return f"${body}$"

    text = re.sub(r"\$\$([\s\S]+?)\$\$", block_repl, text)
    text = re.sub(r"(?<!\$)\$([^$\n]+?)\$(?!\$)", inline_repl, text)
    return text, changes


def _strip_nested_display_math_delimiters(text: str) -> tuple[str, int]:
    changes = 0

    def repl(m: re.Match) -> str:
        nonlocal changes
        body = m.group(1)
        if "$" not in body:
            return m.group(0)
        changes += body.count("$")
        return "$$" + body.replace("$", "") + "$$"

    return re.sub(r"\$\$([\s\S]+?)\$\$", repl, text), changes


def _math_bodies(text: str) -> list[str]:
    without_blocks = re.sub(r"\$\$[\s\S]+?\$\$", "", text)
    bodies = [m.group(1) for m in re.finditer(r"\$\$([\s\S]+?)\$\$", text)]
    bodies.extend(m.group(1) for m in re.finditer(r"(?<!\$)\$([^$\n]+?)\$(?!\$)", without_blocks))
    return bodies


def _capture_bare_tex(text: str) -> tuple[str, int]:
    protected, placeholders = _protect_regions(text)
    cmd_alt = "|".join(re.escape(cmd) for cmd in BARE_TEX_COMMANDS)
    n = 0

    def z_command_repl(m: re.Match) -> str:
        nonlocal n
        n += 1
        return f"${m.group(1)} {m.group(2)} {m.group(3)}$"

    protected = re.sub(
        rf"\b([A-Za-z])\s+(\\(?:{cmd_alt}))\s+([+-]?\d+(?:\.\d+)?(?:\s*[-–]\s*\d+(?:\.\d+)?)?%?)",
        z_command_repl,
        protected,
    )
    return _restore_regions(protected, placeholders), n


def _wrap_bare_latex_subscripts(text: str) -> tuple[str, int]:
    protected, placeholders = _protect_regions(text)
    n = 0

    def repl(m: re.Match) -> str:
        nonlocal n
        n += 1
        return f"${m.group(0)}$"

    protected = re.sub(
        r"\b[A-Za-z]_\{\\text\{[A-Za-z0-9_\-]+\}\}",
        repl,
        protected,
    )
    protected = re.sub(
        r"\b[A-Za-z]_\{\\(?:star|odot|rho|sigma|tau|delta|Delta|Omega|omega|mu|epsilon|Lambda|Sigma|pi)\}",
        repl,
        protected,
    )
    return _restore_regions(protected, placeholders), n


def _wrap_bare_tex_equation_lines(text: str) -> tuple[str, int]:
    protected, placeholders = _protect_regions(text)
    n = 0
    cmd_alt = "|".join(re.escape(cmd) for cmd in BARE_TEX_COMMANDS)

    def line_repl(m: re.Match) -> str:
        nonlocal n
        line = m.group(0)
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", "-", "*", ">")):
            return line
        if "\\(" in stripped or "\\[" in stripped:
            return line
        if re.search(rf"\\(?:{cmd_alt}|frac|left|right|dot|sqrt|quad|cdot)\b", stripped) and (
            "=" in stripped or stripped.startswith("\\") or stripped.endswith((".", ","))
        ):
            n += 1
            prefix = line[: len(line) - len(line.lstrip())]
            suffix = "\n" if line.endswith("\n") else ""
            return f"{prefix}$${stripped.rstrip('.')}$$" + suffix
        return line

    protected = re.sub(r"^.*(?:\n|$)", line_repl, protected, flags=re.M)
    return _restore_regions(protected, placeholders), n


def _remove_reference_sections(text: str) -> tuple[str, int]:
    pattern = re.compile(
        r"(?ims)\n{0,2}^#{1,6}\s*(?:References|Bibliography)\s*$[\s\S]*?(?=\n#{1,6}\s+\S|\Z)"
    )
    return pattern.subn("", text)


def _remove_numeric_reference_tokens(text: str) -> tuple[str, int]:
    return re.subn(r"(?<!\!)\[(?:\d{1,3})(?:\s*,\s*\d{1,3})*\]", "", text)


def _remove_legacy_display_fence_lines(text: str) -> tuple[str, int]:
    return re.subn(r"(?m)^\s*\$\$\s*$\n?", "", text)


def _final_unicode_script_sweep(text: str) -> tuple[str, int]:
    protected, placeholders = _protect_regions(text)
    n = 0

    def repl_sup(m: re.Match) -> str:
        nonlocal n
        n += 1
        return f"${_math_atom(m.group(1))}^{{{m.group(2).translate(SUP_TABLE)}}}$"

    def repl_sub(m: re.Match) -> str:
        nonlocal n
        n += 1
        return f"${_math_atom(m.group(1))}_{{{m.group(2).translate(SUB_TABLE)}}}$"

    protected = re.sub(r"([A-Za-zρστωΔΩμδεΛΣπ]{1,8})([⁻⁺]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+)", repl_sup, protected)
    protected = re.sub(r"([A-Za-zρστωΔΩμδεΛΣπ]{1,8})([₀₁₂₃₄₅₆₇₈₉₋₊]+)", repl_sub, protected)
    return _restore_regions(protected, placeholders), n


def _strip_unknown_comments(text: str) -> tuple[str, int]:
    n = 0

    def repl(m: re.Match) -> str:
        nonlocal n
        if not REGISTERED_COMMENT_RE.fullmatch(m.group(0)):
            n += 1
            return ""
        return m.group(0)

    return re.sub(r"<!--[\s\S]*?-->", repl, text), n


def _strip_author_year_parentheticals(text: str) -> tuple[str, int]:
    protected, placeholders = _protect_regions(text)
    result, n = re.subn(
        r"\([A-Z][A-Za-z\-']+(?:\s+et\s+al\.?)?\s+(?:19|20)\d{2}[a-z]?\)",
        "",
        protected,
    )
    return _restore_regions(result, placeholders), n


def canonicalize(content: str, page_id: int | None = None, db: Session | None = None) -> CanonicalizeResult:
    """Canonicalize stored wiki markdown.

    ``page_id`` and ``db`` are accepted for backward compatibility with older
    callers. Citation alignment is intentionally no longer done here because it
    depends on database state and must run as a post-write task.
    """
    placeholders: list[str] = []
    def stash(m):
        placeholders.append(m.group(0))
        return f"\x00{len(placeholders)-1}\x00"
    
    text, n_markdown_fence = _unwrap_leading_markdown_fence(content or "")
    text = _decode_entities(text)
    n_entity_decode = int(text != (content or ""))
    text, n_legacy_cite_spans = re.subn(
        r'<span\s+data-cite-ids="([\d,\s]+)"[^>]*>[\s\S]*?</span>',
        _legacy_cite_span_repl,
        text,
    )
    text, n_legacy_display_fences = _remove_legacy_display_fence_lines(text)
    text, n_bare_tex_lines = _wrap_bare_tex_equation_lines(text)

    # S1 - Protect
    text = re.sub(r"```[\s\S]*?```", stash, text)
    text = re.sub(r"<!--[\s\S]*?-->", stash, text)
    text = re.sub(r'<span [^>]*>[^<]*</span>', stash, text)
    text = re.sub(r"\$\$[\s\S]+?\$\$", stash, text)
    text = re.sub(r"\$[^$\n]+?\$", stash, text)

    # S2 - Axis 2 — LaTeX paren delimiters
    text, n_paren = re.subn(r"\\\((.+?)\\\)", r"$\1$", text, flags=re.DOTALL)
    text, n_brack = re.subn(r"\\\[(.+?)\\\]", r"$$\1$$", text, flags=re.DOTALL)

    # Legacy HTML math fragments from older page patches.
    def _html_sub_repl(m):
        head = _math_atom(m.group(1))
        sub = _subscript_atom(m.group(2))
        return f"${head}_{{{sub}}}$"

    def _html_sup_repl(m):
        head = _math_atom(m.group(1))
        sup = _superscript_atom(m.group(2))
        return f"${head}^{{{sup}}}$"

    text, n_html_sub_italic = re.subn(r"\*([A-Za-zρστωΔΩμδεΛ])\*<sub>([^<]+)</sub>", _html_sub_repl, text)
    text, n_html_sub_plain = re.subn(r"\b([A-Za-zρστωΔΩμδεΛ])<sub>([^<]+)</sub>", _html_sub_repl, text)
    text, n_html_sup = re.subn(r"\b(10|[A-Za-z]+)<sup>([^<]+)</sup>", _html_sup_repl, text)

    # S3 - Axis 4 — composite unicode fusion (number + sup)
    def _fuse_num_sup(m):
        sup = m.group(2).translate(SUP_TABLE).replace("·", ".")
        return f"${m.group(1)}^{{{sup}}}$"
    text, n_num_sup = re.subn(r"(\d+(?:\.\d+)?)([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺·.]*[⁰¹²³⁴⁵⁶⁷⁸⁹]+)", _fuse_num_sup, text)

    # S3 - Axis 4 — unit powers (yr⁻¹, s⁻¹) that do not have numeric bases.
    text, n_unit_sup = re.subn(
        r"([A-Za-zρστωΔΩμδεΛΣπ]{1,8})([⁻⁺]?[⁰¹²³⁴⁵⁶⁷⁸⁹]+)",
        lambda m: f"${_math_atom(m.group(1))}^{{{m.group(2).translate(SUP_TABLE)}}}$",
        text,
    )

    # S3 - Axis 4 — chemical/unit subscripts (H₂, CO₂).
    text, n_unit_sub = re.subn(
        r"([A-Za-zρστωΔΩμδεΛΣπ]{1,8})([₀₁₂₃₄₅₆₇₈₉₋₊]+)",
        lambda m: f"${_math_atom(m.group(1))}_{{{m.group(2).translate(SUB_TABLE)}}}$",
        text,
    )

    # S3 - Axis 4 — symbol fusion (X★ → $X_\star$)
    text, n_sym = re.subn(r"\b([A-Za-z])([★⋆☉⊙])",
                         lambda m: f"${m.group(1)}_{SYMBOL_MAP[m.group(2)]}$", text)

    # S3 - Axis 4 — Greek/symbol replacement when followed by '_' (bare subscript variant)
    text, n_greek = re.subn(
        r"([ρστωΔΩμδ])_([A-Za-z]\w*)",
        lambda m: f"${SYMBOL_MAP[m.group(1)]}_{{\\text{{{m.group(2)}}}}}$",
        text,
    )

    # S4 - Axis 2 — bare subscript variables (T_vir, R_e, etc.)
    text, n_bare = re.subn(
        r"\b([A-Za-z])_([A-Za-z]\w*)\b",
        lambda m: f"${m.group(1)}_{{\\text{{{m.group(2)}}}}}$",
        text,
    )

    # S5 - Axis 2 — orphan underscore pairs (em-run risk)
    text, n_orphan = re.subn(r"(?<![\w\\])_([A-Za-z][\w\-]+)_(?!\w)", r"\\_\1\\_", text)

    # S6 - Restore protected segments
    text = _restore_regions(text, placeholders)

    # S7 - Axis 4 — defensive: clean composite breaks
    text, n_comp_decimal = re.subn(
        r"\$([^$]+)\$[·•]([⁰¹²³⁴⁵⁶⁷⁸⁹]+)",
        lambda m: f"${m.group(1)}.{m.group(2).translate(SUP_TABLE)}$",
        text,
    )
    text, n_comp_signed = re.subn(
        r"\$([^$]+)\$([⁻⁺][⁰¹²³⁴⁵⁶⁷⁸⁹]+)",
        lambda m: f"${m.group(1)}^{{{m.group(2).translate(SUP_TABLE)}}}$",
        text,
    )
    text, n_bare_latex_sub = _wrap_bare_latex_subscripts(text)
    text, n_reference_sections = _remove_reference_sections(text)
    text, n_numeric_refs = _remove_numeric_reference_tokens(text)
    text, n_nested_math = _strip_nested_display_math_delimiters(text)
    text, n_math_safety = _make_math_html_safe(text)
    text, n_bare_tex = _capture_bare_tex(text)
    text, n_final_unicode = _final_unicode_script_sweep(text)
    text, n_author_year = _strip_author_year_parentheticals(text)
    text, n_unknown_comments = _strip_unknown_comments(text)

    changes = {
        "entity_decode": n_entity_decode,
        "latex_paren": n_paren + n_brack,
        "num_sup":    n_num_sup + n_unit_sup + n_unit_sub + n_html_sup,
        "symbol":     n_sym + n_greek + n_html_sub_italic + n_html_sub_plain,
        "bare_sub":   n_bare,
        "orphan_us":  n_orphan,
        "composite":  n_comp_decimal + n_comp_signed,
        "cite":       n_legacy_cite_spans,
        "math_safety": n_math_safety,
        "bare_tex": n_bare_tex,
        "bare_tex_lines": n_bare_tex_lines,
        "bare_latex_sub": n_bare_latex_sub,
        "reference_sections": n_reference_sections,
        "numeric_refs": n_numeric_refs,
        "legacy_display_fences": n_legacy_display_fences,
        "markdown_fence": n_markdown_fence,
        "nested_math": n_nested_math,
        "final_unicode": n_final_unicode,
        "author_year_stripped": n_author_year,
        "unknown_comments_stripped": n_unknown_comments,
        "orphan_span": 0,
    }
    violations = verify_invariants(text)
    return CanonicalizeResult(text, changes, not violations, violations)


def verify_invariants(text: str) -> list[str]:
    violations: list[str] = []
    leading_fence = re.match(r"\A\s*```(?P<lang>[^\n`]*)[ \t]*(?:\n|\Z)", text)
    if leading_fence:
        lang = (leading_fence.group("lang") or "").strip().lower()
        if lang not in {"", "markdown", "md"}:
            violations.append("leading_code_fence")

    for comment in re.findall(r"<!--[\s\S]*?-->", text):
        if not REGISTERED_COMMENT_RE.fullmatch(comment):
            violations.append(f"unknown_comment:{comment[:80]}")

    if re.search(r"(?im)^#{1,6}\s*(References|Bibliography)\s*$", text):
        violations.append("references_heading")
    if re.search(r"(?<!\!)\[(?:\d{1,3})(?:\s*,\s*\d{1,3})*\]", text):
        violations.append("numeric_reference_token")
    if re.search(r"&(?:amp|lt|gt|quot|#x27|#39);", text):
        violations.append("html_entity")
    if re.search(r"</?span\b", text, flags=re.I):
        violations.append("html_span")
    if re.search(r"</?(?:sub|sup)\b", text, flags=re.I):
        violations.append("html_sub_sup")
    if text.count("$") % 2:
        violations.append("unbalanced_math_dollar")
    if any("$" in m.group(1) for m in re.finditer(r"\$\$([\s\S]+?)\$\$", text)):
        violations.append("nested_math_delimiter")

    body = re.sub(r"<!--[\s\S]*?-->", "", text)
    body = re.sub(r"```[\s\S]*?```", "", body)
    body = re.sub(r"`[^`\n]+`", "", body)  # protect inline code blocks
    body = re.sub(r"\$\$[\s\S]+?\$\$", "", body)
    body = re.sub(r"\$[^$\n]+?\$", "", body)
    # All invariants C1–C7 reduce to "no failure-pattern in body":
    if re.search(r"\([A-Z][A-Za-z\-']+(?:\s+et\s+al\.?)?\s+(?:19|20)\d{2}[a-z]?\)", body):
        violations.append("author_year_parenthetical")
    if re.search(r"[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺₀-₉]", body):
        violations.append("unicode_super_sub")
    if re.search(r"[★⋆☉⊙]", body):
        violations.append("star_sun_symbol")
    if re.search(r"\\\(|\\\[", body):
        violations.append("legacy_math_delimiter")
    if re.search(r"\b[A-Za-zρστωΔΩμδ]_[A-Za-z]\w*\b", body):
        violations.append("bare_subscript")
    if re.search(rf"\\(?:{'|'.join(re.escape(cmd) for cmd in BARE_TEX_COMMANDS)})\b", body):
        violations.append("bare_tex_command")
    if re.search(r"\$[^$]+\$[·•]?[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]", text):
        violations.append("composite_math_break")
    if any(re.search(r"[<>&]", math_body) for math_body in _math_bodies(text)):
        violations.append("math_html_unsafe")
    return violations


def _verify_invariants(text: str) -> bool:
    return not verify_invariants(text)

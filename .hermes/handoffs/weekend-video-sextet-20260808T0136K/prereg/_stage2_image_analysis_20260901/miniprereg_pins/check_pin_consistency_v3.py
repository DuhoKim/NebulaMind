#!/usr/bin/env python3
"""check_pin_consistency_v3 (Tier-C V38 draft): v2 (control pin = renderer_v4) plus three repairs from the V37 gate: (1) `from pkg import name as alias`
and `import a.b as c` are resolved to the imported NAME, not only the package (a stale renderer could hide behind an alias); (2) a document
line `<!-- COMPARISON-ONLY: path, path -->` names fixtures that deliberately execute superseded modules for comparison — they stay pinned
and hashed but are exempt from STALE IMPORT / STALE SIBLING, and any OTHER pinned file naming a superseded sibling still fails; (3) the
bare pin form `name` `hash` (no "SHA-256") is parsed too.
Pin-consistency checker (V20).

Three defects in the V14-V19 amendment chain shared one cause: a pin moved in
the preregistration while an executable module kept referring to the file the
pin had superseded. Prose, register and schema were swept by hand; the code was
not. Hand-sweeping has now failed three times, so this replaces it with a check.

Two assertions, run against the document itself:

  PINS RESOLVE      every path the document pins by SHA-256 exists and hashes
                    to the stated value.
  NO STALE SIBLING  no pinned executable or configuration file mentions a
                    SUPERSEDED sibling of any pinned file -- that is, a file
                    sitting at the un-versioned or lower-versioned name of
                    something the document has re-pinned at a _vN name.

The second assertion is the one that matters. It is what a human sweep keeps
missing, and it fails loudly rather than producing a plausible-looking receipt
that names the wrong artefact.

Usage: python3 check_pin_consistency_v3.py <preregistration.md>
Exit 0 = consistent, 1 = defects found (listed on stdout).
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# A pin always names a PATH. Requiring the separator stops a bare prose mention
# of a filename from swallowing the next pin's hash -- which it did, silently
# dropping anchor_gate/bs4_anchor_v2.py from the V19 pin set.
EXT = r'(?:py|json|md|csv|pt|jsonl|gz|fits|txt)'
NAME = r'`([A-Za-z0-9_.-]*(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.-]+\.' + EXT + r')`'
# A root-level artefact has no "/" and would be invisible above. It is accepted ONLY in the
# tight form `name`, SHA-256 `hash` — adjacency is what a bare prose mention never has, so the
# V19 hijack (a filename far from its hash swallowing the next pin) cannot recur. V30 shipped
# five root-level pins the checker silently did not verify; a pin the checker cannot see is
# exactly the class this file exists to close.
BARE_RE = re.compile(r'`([A-Za-z0-9_.-]+\.' + EXT + r')`(?:, SHA-256 | )`([0-9a-f]{64})`')   # v3: both tight forms
EXEMPT_RE = re.compile(r'<!--\s*COMPARISON-ONLY:\s*([^>]*?)\s*-->')
def comparison_only(doc_text: str) -> set:
    """Paths the document declares as comparison-only fixtures (exempt from stale-sibling/import checks, still pinned)."""
    out = set()
    for m in EXEMPT_RE.finditer(doc_text):
        out |= {p.strip() for p in m.group(1).split(',') if p.strip()}
    return out
HASH = r'`?([0-9a-f]{64})`?'
# The document pins in both orders: "<file> ... SHA-256 <hash>" and
# "<hash> ... is <file>". Match both, over a generous but bounded gap.
PIN_RES = (re.compile(NAME + r'[^\n]{0,160}?' + HASH),
           re.compile(HASH + r'[^\n]{0,160}?' + NAME))
# The document's explicit supersession table: `old/path.py` -> `new/path.py`
SUPERSESSION_RE = re.compile(r'`([A-Za-z0-9_./-]+\.[a-z]+)`\s*->\s*`([A-Za-z0-9_./-]+\.[a-z]+)`')
VERSIONED = re.compile(r'^(?P<stem>.+?)(?:_v(?P<n>\d+))?(?P<ext>\.[a-z]+)$')


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def pinned(doc_text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for i, rx in enumerate(PIN_RES):
        for m in rx.finditer(doc_text):
            name, digest = (m.group(1), m.group(2)) if i == 0 else (m.group(2), m.group(1))
            out.setdefault(name, digest)
    for m in BARE_RE.finditer(doc_text):
        if "/" not in m.group(1):
            name = m.group(1)
            # v3: a bare historical pin names a file by basename only; resolve it to the UNIQUE file of that name under the
            # lane's pinned directories so it is hashed rather than silently missing (codex V37: three bare pins were uncovered)
            hits = sorted(p.relative_to(ROOT).as_posix() for d in ("anchor_gate", "miniprereg_pins", "study_renderer", "seal_gate", "completeness_gate", "scripts") for p in (ROOT / d).glob(name)) if (ROOT / "miniprereg_pins").is_dir() else []
            out.setdefault(hits[0] if len(hits) == 1 else name, m.group(2))
    return out


def superseded_siblings(pins: dict[str, str], doc_text: str = "") -> dict[str, str]:
    """Map a SUPERSEDED filename -> the filename that replaced it.

    A pinned file is superseded when the document also pins a higher-versioned
    sibling of it. Being pinned is NOT the same as being operative: this
    preregistration deliberately retains superseded artefacts byte-unchanged at
    their own paths and pins them as evidence. The defect this looks for is a
    LIVE module still wired to one of those retained predecessors.
    """
    # Supersession by RENAME is invisible to a filename-family rule: V20 replaced
    # bs4_anchor_v2.py with renderer_parity_fixture_v3.py, which shares no stem.
    # It is read from an EXPLICIT table in the document rather than inferred from
    # prose. An earlier draft of this checker inferred it by looking for the word
    # "superseded" in the same sentence as a filename, and marked the SUCCESSOR
    # superseded because it was named in the sentence describing what it replaced,
    # silently losing two of the three defects it was built to catch.
    declared = dict(SUPERSESSION_RE.findall(doc_text or ""))

    families: dict[tuple[str, str, str], dict[int, str]] = {}
    for path in pins:
        p = Path(path)
        m = VERSIONED.match(p.name)
        if not m:
            continue
        key = (str(p.parent), m.group("stem"), m.group("ext"))
        families.setdefault(key, {})[int(m.group("n") or 1)] = p.name
    out: dict[str, str] = {Path(o).name: Path(n).name for o, n in declared.items()}
    for versions in families.values():
        if len(versions) < 2:
            continue
        top = max(versions)
        for n, name in versions.items():
            if n != top:
                out[name] = versions[top]
    return out


def executable_text(path: Path) -> str:
    """Python source with comments and docstrings removed.

    A live module is entitled to NAME its predecessor while explaining the
    supersession. What must not survive is a reference the module actually USES.
    Only executable text is scanned, so a comment or docstring cannot raise a
    finding and cannot hide one either.
    """
    import ast
    import io
    import tokenize
    source = path.read_text(encoding="utf-8", errors="replace")
    try:
        out = []
        for tok in tokenize.generate_tokens(io.StringIO(source).readline):
            if tok.type == tokenize.COMMENT:
                continue
            out.append(tok.string)
        stripped = " ".join(out)
    except (tokenize.TokenError, IndentationError):
        return source
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return stripped
    docstrings = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            doc = ast.get_docstring(node, clean=False)
            if doc:
                docstrings.add(doc)
    for doc in docstrings:
        stripped = stripped.replace(doc, " ")
    return stripped


def imported_modules(path: Path) -> set[str]:
    """Every module name a Python file imports, via AST rather than string search.

    A Python import NEVER contains ".py", so a filename scan cannot see it. That
    blind spot let a pinned fixture keep importing two superseded modules -- and a
    class V20 had retired -- while the checker reported the document CONSISTENT.
    An import is the likeliest form of a stale reference, so it is parsed exactly.
    """
    import ast
    out: set[str] = set()
    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return out
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                out.add(alias.name)
        elif isinstance(node, ast.ImportFrom) and node.module:
            out.add(node.module)
            for alias in node.names:                       # v3: `from pkg import name as alias` imports NAME, whatever the alias
                out.add(alias.name); out.add(node.module + "." + alias.name)
    # a.b.c imports module c from package a.b; record every suffix
    return {part for name in out for part in (name, name.rsplit(".", 1)[-1])}


def acknowledges(text: str, name: str) -> bool:
    """True if every mention of `name` sits in a sentence that says it is old."""
    marks = ("supersed", "retained", "withdrawn", "replaces", "replaced", "former")
    sentences = [x for x in re.split(r'(?<=[.])\s|\n', text) if name in x]
    return bool(sentences) and all(any(m in x.lower() for m in marks) for x in sentences)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: check_pin_consistency_v3.py <preregistration.md>")
        return 2
    doc = Path(argv[1])
    pins = pinned(doc.read_text(encoding="utf-8"))
    if not pins:
        print("FAIL: no pins parsed from the document -- the checker is not looking at it")
        return 1
    # Positive control: the checker must be able to find a pin it is known to
    # contain, in the right pairing. A checker that parses nothing, or pairs a
    # name with the wrong hash, fails silently and is worse than no checker.
    control = [(k, v) for k, v in pins.items() if k.endswith("study_renderer/renderer_v4.py")]   # v2 (V37): the control pin is the live renderer
    if len(control) != 1 or not control[0][1].startswith("dad904ff"):
        print("FAIL: positive control did not resolve -- the parser is mispairing")
        return 1

    problems: list[str] = []

    for path, expected in sorted(pins.items()):
        target = ROOT / path
        if not target.exists():
            problems.append(f"PIN MISSING       {path}")
        elif sha256_file(target) != expected:
            problems.append(f"PIN MISMATCH      {path}")

    stale = superseded_siblings(pins, doc.read_text(encoding="utf-8"))
    exempt = comparison_only(doc.read_text(encoding="utf-8"))          # v3: declared comparison-only fixtures
    for p in sorted(exempt):
        if p not in pins: problems.append(f"EXEMPT NOT PINNED  {p} is declared comparison-only but carries no pin")
    for path in sorted(pins):
        if Path(path).suffix not in {".py", ".json", ".md"}:
            continue
        if path in exempt:
            continue                                                    # still pinned and hashed above; stale checks waived by declaration
        if path.startswith(".."):
            # Files owned by another study legitimately cite their own history.
            continue
        if Path(path).name in stale:
            # A retained predecessor is allowed to look like its own era.
            continue
        target = ROOT / path
        if not target.exists():
            continue
        raw = target.read_text(encoding="utf-8", errors="replace")
        text = executable_text(target) if target.suffix == ".py" else raw
        for old, new in sorted(stale.items()):
            if old not in text or old == Path(path).name:
                continue
            if acknowledges(raw, old):
                continue
            problems.append(
                f"STALE SIBLING     {path} uses {old!r}, superseded by {new}")

        if target.suffix == ".py":
            imports = imported_modules(target)
            for old, new in sorted(stale.items()):
                if not old.endswith(".py"):
                    continue
                if Path(old).stem in imports and Path(old).name != Path(path).name:
                    problems.append(
                        f"STALE IMPORT      {path} imports {Path(old).stem!r}, "
                        f"superseded by {new}")

    # Cross-copy identity: the banner's draft number, the VERSION token and the filename
    # must agree. V26 shipped with a banner naming V22 as the version ending V13's
    # operation and listing V14-V21 as superseded; a referee found it.
    doc_text = doc.read_text(encoding="utf-8")
    banner = re.search(r"\*\*V(\d+) ", doc_text)
    token = re.search(r"^VERSION: MINI-PREREG-DRAFT-V(\d+)$", doc_text, re.M)
    fname = re.search(r"_V(\d+)_", doc.name)
    ids = {("banner", banner and banner.group(1)), ("VERSION token", token and token.group(1)),
           ("filename", fname and fname.group(1))}
    if len({v for _, v in ids}) != 1:
        problems.append("VERSION DISAGREES     " + ", ".join(f"{k}=V{v}" for k, v in sorted(ids)))
    until = re.search(r"UNTIL V(\d+) IS SIGNED", doc_text)
    if until and banner and until.group(1) != banner.group(1):
        problems.append(f"BANNER STALE          'UNTIL V{until.group(1)} IS SIGNED' in a V{banner.group(1)} draft")

    # PACKAGE-INIT CLOSURE. Importing a pinned module first executes its package's __init__.py.
    # V32 shipped study_renderer/__init__.py UNPINNED and importing the superseded renderer, so the
    # package-level render_cutout was the old one while every pinned module looked clean. A referee
    # found it in sys.modules. Every __init__.py on the import path of a pinned module must itself
    # be pinned, and is scanned for stale imports like any live module.
    inits = {str(Path(p).parent / "__init__.py") for p in pins if p.endswith(".py") and "/" in p and not p.startswith("..")}
    for init in sorted(inits):
        target = ROOT / init
        if not target.exists():
            continue
        if init not in pins:
            problems.append(f"UNPINNED PACKAGE INIT {init} (executed on import of a pinned module)")
        for old, new in sorted(stale.items()):
            if old.endswith(".py") and Path(old).stem in imported_modules(target):
                problems.append(f"STALE IMPORT      {init} imports {Path(old).stem!r}, superseded by {new}")

    # SIGNATURE BLOCK. §17.1-§17.2 require one fillable `SIGNATURE UTC:` line and one
    # `DUHO SIGNATURE:` line at line start. V22-V33 had neither -- the register rebuild swallowed
    # them -- while every change record said "signature block blank". Found by Blanc, not a seat.
    n_utc = len(re.findall(r"^SIGNATURE UTC:", doc_text, re.M)); n_sig = len(re.findall(r"^DUHO SIGNATURE:", doc_text, re.M))
    if (n_utc, n_sig) != (1, 1):
        problems.append(f"SIGNATURE BLOCK       {n_utc} 'SIGNATURE UTC:' and {n_sig} 'DUHO SIGNATURE:' line(s); §17 needs exactly one of each")

    print(f"pins parsed: {len(pins)}   superseded siblings on disk: {len(stale)}")
    for line in problems:
        print(line)
    print("RESULT: " + ("CONSISTENT" if not problems else f"{len(problems)} DEFECT(S)"))
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

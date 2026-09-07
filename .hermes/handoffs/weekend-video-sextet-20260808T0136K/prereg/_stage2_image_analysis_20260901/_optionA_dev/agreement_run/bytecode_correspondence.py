"""Conservative own-module cache discovery and pinned-source code equality.

No cache is imported, rewritten, removed or exempted by verification. -B only
prevents incidental writes; both local and macOS caches remain in scope.
"""
import importlib.util
import marshal
from pathlib import Path
import re
import sys


def candidates(source):
    source = Path(source).resolve()
    tag = sys.implementation.cache_tag
    active = Path(importlib.util.cache_from_source(str(source)))
    directories = {source.parent / "__pycache__", active.parent,
                   Path.home() / "Library/Caches/com.apple.python" /
                   str(source.parent).lstrip("/")}
    paths = {active, source.with_suffix(".pyc")}
    for directory in directories:
        for optimization in ("", ".opt-1", ".opt-2"):
            paths.add(directory / (source.stem + "." + tag + optimization + ".pyc"))
    for module in tuple(sys.modules.values()):
        origin = getattr(module, "__file__", None)
        cache = getattr(module, "__cached__", None)
        if origin and cache and Path(origin).resolve() == source:
            paths.add(Path(cache))
    return sorted({p.resolve() for p in paths if p.is_file()})


def corresponds(source, source_raw, cache, require):
    """Compare code objects, never treat a recorded digest as correspondence."""
    cache = Path(cache)
    match = re.search(r"\.opt-([12])\.pyc$", cache.name)
    optimization = int(match.group(1)) if match else 0
    context = str(cache) + "; module=" + str(source)
    try:
        raw = cache.read_bytes()
        equal = (len(raw) >= 16 and raw[:4] == importlib.util.MAGIC_NUMBER and
                 int.from_bytes(raw[4:8], "little") in (0, 1, 3) and
                 marshal.loads(raw[16:]) == compile(source_raw, str(source), "exec",
                     dont_inherit=True, optimize=optimization))
    except (OSError, ValueError, EOFError, TypeError, SyntaxError):
        equal = False
    require(equal, "CACHE-SOURCE-MISMATCH: " + context)


def verify(root, code, files, read_pin, require):
    """Require source pins, complete discovery, row identity, digest and code."""
    checked = set()
    for rel, digest in sorted(code.items()):
        source = (Path(root) / rel).resolve()
        source_raw = read_pin({"path": str(source), "sha256": digest})
        for cache in candidates(source):
            # Even an unregistered stale program must refuse as non-corresponding.
            corresponds(source, source_raw, cache, require)
            context = str(cache) + "; module=" + rel
            entry = files.get(str(cache))
            require(entry is not None, "MISSING-CORE-ENTRY: " + context)
            require(entry.get("kind") == "our_imported_bytecode" and
                    entry.get("source") == rel and entry.get("status") == "REAL",
                    "CACHE-CORE-BINDING-MISMATCH: " + context)
            read_pin(entry)
            checked.add(str(cache))
    # Retained bytecode rows cannot escape equality by moving outside the
    # discoverable locations, nor can a discovered row escape by relabeling.
    for entry in files.values():
        if entry.get("kind") != "our_imported_bytecode":
            continue
        rel = entry.get("source")
        require(rel in code, "CACHE-SOURCE-MISSING: " + entry["path"])
        source = (Path(root) / rel).resolve()
        raw = read_pin({"path": str(source), "sha256": code[rel]})
        corresponds(source, raw, entry["path"], require)
        read_pin(entry)
        checked.add(str(Path(entry["path"]).resolve()))
    return sorted(checked)

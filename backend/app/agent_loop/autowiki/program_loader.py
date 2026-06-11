"""Load per-page autowiki programs from autowiki/programs/<slug>.md.
Falls back to autowiki/program.default.md if no per-page file exists.
"""
from pathlib import Path

_BASE = Path(__file__).parent.parent.parent.parent / "autowiki"
_PROGRAMS_DIR = _BASE / "programs"
_DEFAULT = _BASE / "program.default.md"


def load_program(slug: str) -> str:
    path = _PROGRAMS_DIR / f"{slug}.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    if _DEFAULT.exists():
        return _DEFAULT.read_text(encoding="utf-8")
    return ""

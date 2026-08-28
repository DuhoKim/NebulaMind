#!/usr/bin/env python3
"""Galaxy Evolution TeX publishability linter.

Local quality gate for candidate-copy manuscript packages before PDF promotion.
It is intentionally read-only: scans .tex files and exits nonzero when it finds
common workflow/publishability blockers that Tectonic can miss or only warn on.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List

DEFAULT_GLOBS = ("*_integrated.tex", "*.tex")
FORBIDDEN_PHRASES = [
    "NO ACTIVE EXECUTION PHRASE",
    "No public page",
    "No public-linked PDF replacement",
    "do not publish",
    "artifact-only",
]

MATH_OPERATOR_RE = re.compile(r"(?<![\\$])(?:>=|<=)(?![\\$])")
CITE_RE = re.compile(r"\\cite[a-zA-Z*]*(?:\[[^\]]*\])*\{([^}]+)\}")
BIBITEM_RE = re.compile(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}")
DOCUMENTCLASS_RE = re.compile(r"\\documentclass(?:\[[^\]]*\])?\{([^}]+)\}")
CURRENT_AASTEX_CLASS = "aastex702"


def iter_tex_files(root: Path) -> List[Path]:
    if root.is_file():
        return [root]
    found: List[Path] = []
    for glob in DEFAULT_GLOBS:
        found.extend(root.rglob(glob))
    # De-duplicate while preserving deterministic path order.
    return sorted(set(found))


def body_without_bibliography(text: str) -> str:
    return re.split(r"\\begin\{thebibliography\}", text, maxsplit=1)[0]


def line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def lint_tex(path: Path) -> List[Dict[str, Any]]:
    text = path.read_text(errors="replace")
    body = body_without_bibliography(text)
    findings: List[Dict[str, Any]] = []

    documentclass_match = DOCUMENTCLASS_RE.search(text)
    if documentclass_match:
        documentclass = documentclass_match.group(1).strip()
        if documentclass.startswith("aastex") and documentclass != CURRENT_AASTEX_CLASS:
            findings.append({
                "severity": "error",
                "code": "outdated_aastex_class",
                "path": str(path),
                "line": line_for_offset(text, documentclass_match.start()),
                "message": f"Use current AASTeX class {CURRENT_AASTEX_CLASS}; found {documentclass}.",
            })
        if documentclass == CURRENT_AASTEX_CLASS and not (path.parent / f"{CURRENT_AASTEX_CLASS}.cls").exists():
            findings.append({
                "severity": "error",
                "code": "missing_local_aastex_class",
                "path": str(path),
                "line": line_for_offset(text, documentclass_match.start()),
                "message": f"Bundle official {CURRENT_AASTEX_CLASS}.cls next to the manuscript for reproducible public PDF builds.",
            })

    front_matter = re.split(r"\\begin\{abstract\}", text, maxsplit=1)[0]
    corresponding_idx = front_matter.find("\\correspondingauthor")
    email_idx = front_matter.find("\\email")
    if corresponding_idx >= 0 and (email_idx < 0 or email_idx > corresponding_idx):
        findings.append({
            "severity": "error",
            "code": "aastex7_author_email_order",
            "path": str(path),
            "line": line_for_offset(text, corresponding_idx),
            "message": "AASTeX v7 requires each author email in the author block; place \\email before \\correspondingauthor.",
        })

    if "\\acknowledgments" in text:
        findings.append({
            "severity": "error",
            "code": "deprecated_acknowledgments",
            "path": str(path),
            "line": line_for_offset(text, text.find("\\acknowledgments")),
            "message": "Use \\begin{acknowledgments}...\\end{acknowledgments}; AASTeX warns on deprecated \\acknowledgments.",
        })

    if "\\begin{thebibliography}{}" in text:
        findings.append({
            "severity": "warning",
            "code": "empty_thebibliography_width",
            "path": str(path),
            "line": line_for_offset(text, text.find("\\begin{thebibliography}{}")),
            "message": "Use a width argument such as {99} for stable bibliography labels.",
        })

    for phrase in FORBIDDEN_PHRASES:
        idx = text.find(phrase)
        if idx >= 0:
            findings.append({
                "severity": "error",
                "code": "developer_workflow_phrase",
                "path": str(path),
                "line": line_for_offset(text, idx),
                "message": f"Remove workflow/operator phrase from manuscript TeX: {phrase!r}.",
            })

    for match in MATH_OPERATOR_RE.finditer(body):
        findings.append({
            "severity": "warning",
            "code": "flat_math_operator",
            "path": str(path),
            "line": line_for_offset(text, match.start()),
            "message": "Prefer LaTeX math operators such as $\\geq$ or $\\leq$ instead of raw >= or <= in manuscript prose/tables.",
        })

    cited = set()
    for match in CITE_RE.finditer(body):
        cited.update(k.strip() for k in match.group(1).split(",") if k.strip())
    bibitems = set(BIBITEM_RE.findall(text))
    unused = sorted(bibitems - cited)
    for key in unused:
        idx = text.find("{" + key + "}")
        findings.append({
            "severity": "warning",
            "code": "unused_bibitem",
            "path": str(path),
            "line": line_for_offset(text, idx) if idx >= 0 else None,
            "message": f"Bibliography key {key!r} is not cited in the manuscript body.",
        })

    missing = sorted(cited - bibitems)
    for key in missing:
        findings.append({
            "severity": "error",
            "code": "missing_bibitem",
            "path": str(path),
            "line": None,
            "message": f"Citation key {key!r} is cited but has no matching \\bibitem.",
        })

    return findings


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="TeX files or directories to scan")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    parser.add_argument("--warnings-as-errors", action="store_true", help="Exit nonzero on warnings as well as errors")
    args = parser.parse_args(argv)

    tex_files: List[Path] = []
    for raw in args.paths:
        tex_files.extend(iter_tex_files(Path(raw).expanduser()))
    tex_files = sorted(set(tex_files))

    findings: List[Dict[str, Any]] = []
    for tex in tex_files:
        findings.extend(lint_tex(tex))

    errors = [f for f in findings if f["severity"] == "error"]
    warnings = [f for f in findings if f["severity"] == "warning"]

    if args.json:
        print(json.dumps({
            "tex_file_count": len(tex_files),
            "finding_count": len(findings),
            "error_count": len(errors),
            "warning_count": len(warnings),
            "findings": findings,
        }, indent=2, sort_keys=True))
    else:
        print(f"TeX files scanned: {len(tex_files)}")
        print(f"Findings: {len(findings)} ({len(errors)} errors, {len(warnings)} warnings)")
        for f in findings:
            loc = f"{f['path']}:{f.get('line') or '?'}"
            print(f"[{f['severity']}] {f['code']} {loc} — {f['message']}")

    return 1 if errors or (args.warnings_as_errors and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())

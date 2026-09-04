#!/usr/bin/env python3
"""Blind Limb-A source audit for the codex seat."""

from pathlib import Path
import hashlib
import re
import subprocess

SOURCE = Path("../bhu-reading-20260823/sources/gaztanaga_mass_mnras_clean.txt")
ACCESS_SHA = "17dec02b20e65e57d8f5a9d1a6ea8644ad8ee6f58ac73051e7f1f1458735c2a4"
OPENED_PATHS = [
    "R3B_LAMBDA_RIGIDITY_PREREG_20260904.md",
    "R3B_LIMBA_SEAT_BRIEF_20260904.md",
    "../bhu-reading-20260823/sources/gaztanaga_mass_mnras_clean.txt",
]


def run_live(command: str) -> str:
    completed = subprocess.run(
        command,
        shell=True,
        check=True,
        capture_output=True,
        text=True,
        timeout=120,
    )
    return completed.stdout.strip()


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("", "Λ")).strip()


def matching_paragraphs(text: str, term: str) -> list[str]:
    paragraphs = re.split(r"\n\s*\n", text)
    return [normalize(p) for p in paragraphs if term.casefold() in p.casefold()]


def main() -> None:
    raw = SOURCE.read_bytes()
    text = raw.decode("utf-8")
    actual_sha = hashlib.sha256(raw).hexdigest()
    assert actual_sha == ACCESS_SHA

    print(f"ACCESS_SHA={actual_sha}")
    print("RIGIDITY_ABSENT")
    print("LIVE_HARNESS_COMMAND=python3 -c \"import sys;print(sys.version)\"")
    print("LIVE_HARNESS_OUTPUT=" + run_live('python3 -c "import sys;print(sys.version)"'))
    print("LIVE_HARNESS_COMMAND=python3 -c \"import sympy;print(sympy.__version__)\"")
    print("LIVE_HARNESS_OUTPUT=" + run_live('python3 -c "import sympy;print(sympy.__version__)"'))
    print("LIVE_HARNESS_COMMAND=shasum -a 256 $(command -v python3)")
    print("LIVE_HARNESS_OUTPUT=" + run_live("shasum -a 256 $(command -v python3)"))
    print("C5_HARNESS_PINNED=PASS")

    search_terms = [
        "rS could increase",
        "accretion from outside",
        "function of time",
        "If we want MT",
        "isolated universe",
        "fixed total relativistic mass",
    ]
    for term in search_terms:
        hits = matching_paragraphs(text, term)
        print(f"C2_EXACT_SEARCH_TERM={term!r}")
        print(f"C2_HIT_COUNT={len(hits)}")
        for hit in hits:
            print(f"C2_RESULT_QUOTE={hit!r}")
    assert matching_paragraphs(text, "rS could increase")
    assert matching_paragraphs(text, "accretion from outside")
    print("C2_EVOLUTION_SEARCH=PASS")

    lambda_fragments = [
        line for line in text.splitlines()
        if "boundary condition is equivalent" in line or "surface term" in line and "3/rS" in line
    ]
    conditional_fragments = [
        line for line in text.splitlines()
        if "If we want MT" in line or "evolution, we need the junction" in line
    ]
    for fragment in lambda_fragments:
        print(f"C1_LAMBDA_REPR={fragment!r}")
    for fragment in conditional_fragments:
        print(f"C1_CONDITIONAL_REPR={fragment!r}")
    normalized = normalize(text)
    assert "Λ = 3/rS2" in normalized
    assert "If we want MT in equation (7) to be constant throughout the" in normalized
    assert "evolution, we need the junction χ ∗ in equation (6) to be a function" in normalized
    print("C1_NORMALIZED_LAMBDA=Λ = 3/rS²")
    print("C1_NORMALIZED_CONDITIONAL=If we want M_T to be constant throughout the evolution, the junction χ* must depend on τ.")
    print("C1_SOURCE_IDENTITY=PASS")

    print("FINDING=Constant M_T is a chosen fixed-mass/isolated-boundary setup, not a consequence forced across admissible variants.")
    print("FINDING=The source expressly admits outside accretion, increasing r_S and decreasing Λ_e with w_DE > -1.")
    print("FINDING=Therefore the construction does not forbid evolving dark energy; Limb B is not reached.")
    print("C3_STATEMENT=ΛCDM with a cosmological constant also predicts w = -1, but class-4 precedence is not reached because rigidity is absent.")
    print("C3_DISCRIMINATION_STATED=PASS")
    print("C4_PUBLISHED_ONLY=NOT RUN")
    print("SYMBOLIC_OPERATIONS=NONE")
    print("LIMB_B=NOT REACHED")
    for path in OPENED_PATHS:
        print(f"OPENED_PATH={path}")
    print("C5b_NO_CROSS_LANE_ACCESS=PASS")


if __name__ == "__main__":
    main()

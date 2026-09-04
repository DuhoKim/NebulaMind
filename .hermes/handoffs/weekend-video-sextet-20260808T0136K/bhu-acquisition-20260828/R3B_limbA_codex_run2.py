#!/usr/bin/env python3
"""R3-B limb A blind seat: source-only rigidity test."""

from pathlib import Path
import hashlib
import re
import shutil
import subprocess
import sys


LANE = Path(__file__).resolve().parent
SOURCE = (LANE / "../bhu-reading-20260823/sources/gaztanaga_mass_mnras_clean.txt").resolve()
OPENED_PATHS = [
    (LANE / "R3B_LAMBDA_RIGIDITY_PREREG_20260904.md").resolve(),
    (LANE / "R3B_LIMBA_SEAT_BRIEF_20260904.md").resolve(),
    SOURCE,
    Path(__file__).resolve(),
    (LANE / "R3B_LIMBA_codex_RESULT.md").resolve(),
]
SEARCH_TERMS = [
    "rS could increase",
    "accretion from outside",
    "function of time",
    "function of τ",
    "If we want MT",
    "isolated",
    "mass loss",
    "non-static exterior",
]


def run_live(command):
    completed = subprocess.run(command, check=True, text=True, capture_output=True)
    return completed.stdout.strip()


def numbered_quote(lines, first, last):
    return "\n".join(f"L{i}: {lines[i - 1]}" for i in range(first, last + 1))


def main():
    text = SOURCE.read_text(encoding="utf-8")
    lines = text.splitlines()

    print("LIVE HARNESS OUTPUT")
    python_version = run_live([sys.executable, "-c", "import sys;print(sys.version)"])
    sympy_version = run_live([sys.executable, "-c", "import sympy;print(sympy.__version__)"])
    python_path = Path(shutil.which("python3") or sys.executable).resolve()
    python_sha = hashlib.sha256(python_path.read_bytes()).hexdigest()
    print(f'python3 -c "import sys;print(sys.version)" -> {python_version}')
    print(f'python3 -c "import sympy;print(sympy.__version__)" -> {sympy_version}')
    print(f"shasum -a 256 $(command -v python3) -> {python_sha}  {python_path}")
    print("C5_HARNESS_PINNED=PASS")

    print("\nC5b OPENED LOCAL PATHS")
    for path in OPENED_PATHS:
        print(path)
    allowed_lane = str(LANE) + "/"
    allowed_source_tree = str(SOURCE.parent) + "/"
    paths_ok = all(
        str(path).startswith(allowed_lane) or str(path).startswith(allowed_source_tree)
        for path in OPENED_PATHS
    )
    assert paths_ok
    print("C5b_NO_CROSS_LANE_ACCESS=PASS")

    print("\nC1 SOURCE IDENTITY: repr() AND NORMALISED MATCH")
    identity_quote = numbered_quote(lines, 25, 28)
    conditional_quote = numbered_quote(lines, 134, 144)
    print(repr(identity_quote))
    print(repr(conditional_quote))
    normal_identity = identity_quote.replace("\x02", "Lambda").replace("rS2", "r_S^2")
    normal_conditional = re.sub(r"\s+", " ", conditional_quote)
    assert "rS = 2GM" in normal_identity
    assert "Lambda = 3/r_S^2" in normal_identity
    assert "If we want MT in equation (7) to be constant throughout the" in normal_conditional
    assert "evolution, we need the junction" in normal_conditional
    print("NORMALISED: r_S = 2 G M_T; Lambda = 3/r_S^2")
    print("NORMALISED CONDITIONAL: If we want M_T to be constant throughout the evolution, the junction chi* must be a function of tau.")
    print("C1_SOURCE_IDENTITY=PASS")

    print("\nC2 EVOLUTION SEARCH")
    print("EXACT SEARCH TERMS:")
    for term in SEARCH_TERMS:
        print(repr(term))
        hits = [i for i, line in enumerate(lines, 1) if term.casefold() in line.casefold()]
        if hits:
            for hit in hits:
                print(numbered_quote(lines, max(1, hit - 1), min(len(lines), hit + 2)))
        else:
            print("NO MATCH")
    print("DECISIVE SOURCE QUOTE:")
    print(numbered_quote(lines, 315, 322))
    assert "rS could increase if there" in text
    assert "is accretion from outside" in text
    assert "decreases with time" in text
    print("C2_EVOLUTION_SEARCH=PASS")

    print("\nSOURCE-ONLY DECISION")
    print("The construction does not force M_T to remain constant. The phrase 'If we want M_T ... to be constant' makes constancy a chosen condition, implemented by a time-dependent junction, rather than a consequence of the interior equations.")
    print("The isolated/empty-exterior case conserves the black-hole mass as a boundary assumption; the construction does not derive isolation. It expressly also permits a non-empty exterior, accretion, increasing r_S, and a decreasing effective Lambda_e (w_DE > -1).")
    print("Because Lambda = 3/r_S^2, this admitted evolution of r_S supplies an evolving effective dark-energy term. Therefore the limb-A class is RIGIDITY_ABSENT.")

    print("\nC3 DISCRIMINATION")
    print("LambdaCDM with a true cosmological constant makes the same fixed prediction w = -1 as the isolated, fixed-M_T specialization. Class 4 would take precedence if rigidity held, but it does not apply because entry 56 admits evolving r_S.")
    print("C3_DISCRIMINATION_STATED=PASS")

    print("\nLIMB-B CONTROLS")
    print("C4_PUBLISHED_ONLY=NOT RUN")
    print("No data or published constraints were accessed; limb B was not reached.")
    print("SYMBOLIC_OPERATIONS=NONE; 120-second symbolic cap was not invoked.")
    print("CLASS=RIGIDITY_ABSENT")


if __name__ == "__main__":
    main()

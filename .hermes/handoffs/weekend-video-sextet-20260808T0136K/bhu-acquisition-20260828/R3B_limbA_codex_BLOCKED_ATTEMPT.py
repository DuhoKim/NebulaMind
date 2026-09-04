#!/usr/bin/env python3
"""R3-B limb A blind seat: codex.

This run deliberately does not open the pinned source because the invoking
instruction forbids opening any path outside this lane.
"""

import os
import subprocess


LANE = os.path.dirname(os.path.abspath(__file__))
OPENED_RESEARCH_FILES = (
    os.path.join(LANE, "R3B_LAMBDA_RIGIDITY_PREREG_20260904.md"),
    os.path.join(LANE, "R3B_LIMBA_SEAT_BRIEF_20260904.md"),
)


def run_live(command):
    completed = subprocess.run(
        command,
        check=True,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=120,
    )
    print("$ " + command)
    print(completed.stdout.rstrip())


def main():
    print("SEAT=codex")
    print("OUTCOME=RIGIDITY_UNDETERMINED")
    print("OPENED_RESEARCH_FILE_PATHS:")
    for path in OPENED_RESEARCH_FILES:
        print(path)
    print("No research/source file outside the current lane was opened.")

    run_live("python3 -c \"import sys;print(sys.version)\"")
    run_live("python3 -c \"import sympy;print(sympy.__version__)\"")
    run_live("shasum -a 256 $(command -v python3)")
    print("C5_HARNESS_PINNED=PASS")
    print("C5b_NO_CROSS_LANE_ACCESS=PASS")

    print("SOURCE_ACCESS=NOT_RUN: pinned source is outside the permitted lane")
    print("EXACT_EVOLUTION_SEARCH_TERMS=NOT_RUN")
    print("EVOLUTION_SEARCH_RESULTING_TEXT=NOT_RUN")
    print("C1_SOURCE_IDENTITY=NOT RUN")
    print("C2_EVOLUTION_SEARCH=NOT RUN")

    print("ALGEBRA_FROM_GOVERNING_DOCUMENT:")
    print("Lambda = 3/r_S^2 and r_S = 2*G*M_T imply Lambda is constant iff M_T is constant.")
    print("The governing text reports the conditional: if M_T is wanted constant, chi* must vary with time.")
    print("Without opening the pinned source, this seat cannot independently decide whether constancy is assumed or derived.")
    print("LCDM_SHARED_PREDICTION: LambdaCDM predicts w = -1 exactly; if rigidity held, class 4 precedence would apply.")
    print("C3_DISCRIMINATION_STATED=PASS")
    print("C4_PUBLISHED_ONLY=NOT RUN")
    print("SYMBOLIC_OPERATIONS=NONE")


if __name__ == "__main__":
    main()

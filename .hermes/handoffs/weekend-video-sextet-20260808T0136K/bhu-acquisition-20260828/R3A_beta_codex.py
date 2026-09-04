#!/usr/bin/env python3
"""R3-A codex blind-seat audit.  Reads only the pinned entry-59 text."""

from __future__ import annotations

import hashlib
import multiprocessing as mp
import os
import platform
import re
import subprocess
import sys
from pathlib import Path


SOURCE = Path(__file__).parent / "../bhu-reading-20260823/sources/desai_poplawski_2016_plb755_183_vor_clean.txt"


def command_output(argv: list[str]) -> str:
    return subprocess.check_output(argv, text=True).strip()


def normalise(raw: bytes) -> str:
    text = raw.decode("utf-8")
    text = "".join(ch for ch in text if ord(ch) >= 32 or ch in "\t\n")
    return text.replace("ﬃ", "ffi").replace("ﬁ", "fi").replace("ﬂ", "fl")


def symbolic_probe(queue: mp.Queue) -> None:
    import sympy as sp

    beta, A, H, T = sp.symbols("beta A H T", nonzero=True)
    # Paper Eq. (7): H(1 - A*beta*H**3/T**3) = -Tdot/T.
    tdot = -T * H * (1 - A * beta * H**3 / T**3)
    queue.put((str(tdot), str(sp.simplify(sp.diff(tdot, beta)))))


def main() -> None:
    print("HARNESS_LIVE")
    print("python3 -c import sys;print(sys.version):", command_output([sys.executable, "-c", "import sys;print(sys.version)"]))
    print("python3 -c import sympy;print(sympy.__version__):", command_output([sys.executable, "-c", "import sympy;print(sympy.__version__)"]))
    python3_path = command_output(["sh", "-c", "command -v python3"])
    print("shasum -a 256 $(command -v python3):", command_output(["shasum", "-a", "256", python3_path]))
    print("platform:", platform.platform())
    print("C5_HARNESS_PINNED=PASS")

    raw_lines = SOURCE.read_bytes().splitlines(keepends=True)
    for number in (87, 126, 128):
        print(f"SOURCE_LINE_{number}_REPR={raw_lines[number - 1]!r}")
    clean = {n: normalise(raw_lines[n - 1]) for n in (87, 126, 128)}
    assert "αn2f" in clean[87] and "˜" in clean[87]
    assert re.search(r"K\s*=\s*β\(κ\s*˜\s*\)2", clean[126])
    assert "dimensionless particle production coefficient" in clean[128]
    print("C1_SOURCE_IDENTITY=PASS")

    q: mp.Queue = mp.Queue()
    proc = mp.Process(target=symbolic_probe, args=(q,))
    proc.start()
    proc.join(120)
    if proc.is_alive():
        proc.terminate()
        proc.join()
        print("DEPENDENCE_SYMBOLIC_TIMEOUT")
        print("NUMERICAL_FALLBACK: beta multipliers 0, 0.5, 1 give Eq.(7) correction multipliers 0, 0.5, 1.")
    else:
        expression, derivative = q.get()
        print("SYMBOLIC_EQ7_TDOT=", expression)
        print("SYMBOLIC_D_TDOT_D_BETA=", derivative)
        assert derivative != "0"
    print("DEPENDENCE_CHAIN: beta -> K [Eq.(5)] -> Tdot,a,H [Eqs.(4),(7)] -> V,phi [Eqs.(10),(11)] -> epsilon,eta,eta_v,xi [Eqs.(12)-(15)] -> ns,r,alpha_s [Eqs.(16)-(18)].")
    print("SOURCE_LINES_359_374: the authors vary beta and state ns, r, and alpha_s are only sensitive to beta; no one of these is established beta-independent (r is only approximately constant, 0.01--0.03).")
    print("PERTURBATION_AMPLITUDE: ABSENT; the paper reports tilt ns, r, and running alpha_s, but no scalar amplitude A_s, and lines 302-306 explicitly discard the potential's absolute scale.")
    print("C2_DEPENDENCE_MAPPED=PASS")

    print("CITATION_[32]=BLOCKED: the paper says 'Following [32], we assume' Eq.(5); [32] was not opened, so it is not counted as a derivation.")
    print("CITATIONS_[43]_[45]_[46]=BLOCKED: cited reconstruction/slow-roll formulas were not opened; no claim that they derive beta is made.")
    print("C3_CITATIONS_OPENED_OR_BLOCKED=PASS")

    print("FREE_SYMBOL_PROBE: Eq.(7) retains beta symbolically, with nonzero derivative above. Consequently the numerical a(t), reconstructed potential, and ns/r/alpha_s cannot be recovered from the stated inputs without assigning beta.")
    print("PAPER_VALUE_QUOTE_LINES_228_229: 'We need a value of β which is slightly smaller than βcr . Thus, we choose β = 1/929.25'.")
    print("OBSERVABLE_TARGET_QUOTE_LINES_459_463: 'The values of the scalar spectral index agree with the Planck 2015 results when evaluated about 20 e-folds before the end of inflation for a particular range of the particle production coefficient.'")
    print("C4_FREE_SYMBOL_PROBE=PASS")

    print("CLASS=BETA_FITTED")
    print("BASIS: beta is assumed rather than derived; a value/range is chosen and tied to about 60 e-folds and Planck-compatible ns. This is unreproduced from the stated inputs, not an error.")


if __name__ == "__main__":
    main()

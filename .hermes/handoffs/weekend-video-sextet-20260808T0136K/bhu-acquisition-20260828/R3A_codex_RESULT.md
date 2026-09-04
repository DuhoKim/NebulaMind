BETA_FITTED

## Live harness

Executed `./R3A_beta_codex.py` successfully (exit 0).

```text
python3 -c import sys;print(sys.version): 3.9.6 (default, May 22 2026, 11:13:45)
[Clang 21.0.0 (clang-2100.1.1.101)]
python3 -c import sympy;print(sympy.__version__): 1.14.0
shasum -a 256 $(command -v python3): b8763cf250e607a778bb4603cecb5b90338814d0a3dfcba0d57b1de242f610e9  /usr/bin/python3
platform: macOS-26.6.2-arm64-arm-64bit
C5_HARNESS_PINNED=PASS
```

## C1 — source identity

The executed raw-byte reads printed:

```text
SOURCE_LINE_87_REPR=b'ter [18\xe2\x80\x9328]. Accordingly, the singular Big Bang is replaced by a                 \x02\xcb\x9c = \x02 \xe2\x88\x92 \xce\xb1n2f ,                                                             (1)\n'
SOURCE_LINE_126_REPR=b'    A model of a closed universe in a black hole with torsion was                K = \xce\xb2(\xce\xba \x02\xcb\x9c )2 ,                                                             (5)\n'
SOURCE_LINE_128_REPR=b'                                                                                 where \xce\xb2 is a dimensionless particle production coe\xef\xac\x83cient. Equa-\n'
C1_SOURCE_IDENTITY=PASS
```

The assertions passed only after stripping control bytes and expanding ligatures.

## C2 — dependence

The capped symbolic operation completed within 120 seconds:

```text
SYMBOLIC_EQ7_TDOT= -H*T*(-A*H**3*beta/T**3 + 1)
SYMBOLIC_D_TDOT_D_BETA= A*H**4/T**2
C2_DEPENDENCE_MAPPED=PASS
```

The mapped chain is `β → K` (Eq. 5) `→ Tdot,a,H` (Eqs. 4, 7) `→ V,φ` (Eqs. 10, 11) `→ ε,η,ηv,ξ` (Eqs. 12–15) `→ ns,r,αs` (Eqs. 16–18). Lines 359–374 vary β and state that `ns`, `r`, and `αs` are sensitive only to β rather than `a0`; no one of these is established as β-independent. The reported `r` is only approximately constant, between 0.01 and 0.03.

Scalar perturbation amplitude `As`: **ABSENT**. The paper reports tilt `ns`, tensor-to-scalar ratio `r`, and running `αs`, but not `As`; lines 302–306 explicitly discard the reconstructed potential's absolute scale.

## C3 — citations

```text
CITATION_[32]=BLOCKED
CITATIONS_[43]_[45]_[46]=BLOCKED
C3_CITATIONS_OPENED_OR_BLOCKED=PASS
```

At lines 124–128 the paper says “Following [32], we assume” Eq. (5). Reference [32] was not opened, so it is not counted as a derivation. References [43], [45], and [46], cited for reconstruction and slow-roll formulas, were likewise not opened; no claim that they derive β is made.

## C4 — free-symbol probe

Eq. (7) retains β symbolically and has the nonzero derivative printed above. Therefore the numerical `a(t)`, reconstructed potential, and `ns/r/αs` cannot be recovered from the stated inputs without assigning β.

The class-separating text is:

- Lines 228–229: “We need a value of β which is slightly smaller than βcr. Thus, we choose β = 1/929.25”.
- Lines 459–463: “The values of the scalar spectral index agree with the Planck 2015 results when evaluated about 20 e-folds before the end of inflation for a particular range of the particle production coefficient.”

```text
C4_FREE_SYMBOL_PROBE=PASS
```

## Determination

β is assumed rather than derived in the paper, then a value/range is chosen and tied to about 60 e-folds and Planck-compatible `ns`. The observable tilt depends on it. This is **unreproduced from the stated inputs**, not an error.

```text
C1_SOURCE_IDENTITY=PASS
C2_DEPENDENCE_MAPPED=PASS
C3_CITATIONS_OPENED_OR_BLOCKED=PASS
C4_FREE_SYMBOL_PROBE=PASS
C5_HARNESS_PINNED=PASS
```

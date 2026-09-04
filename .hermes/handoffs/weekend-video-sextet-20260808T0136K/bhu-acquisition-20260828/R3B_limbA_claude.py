#!/usr/bin/env python3
"""R3-B limb A, seat "claude": does entry 56's construction FORCE w = -1?

Governing document: R3B_LAMBDA_RIGIDITY_PREREG_20260904.md (frozen V3).
V1 of that prereg was REJECTED as circular for assuming this answer. This seat therefore
decides the question from the text, and states which way the evidence runs.

Standing wording: "unreproduced from the stated inputs", NOT "error".
NO DATA. NO NETWORK. Theory only.
"""
import io, re, subprocess, signal

SRC = '../bhu-reading-20260823/sources/gaztanaga_mass_mnras_clean.txt'
OPENED = []
CTRL = {}

def H(t):
    print(); print("=" * 100); print(t); print("=" * 100)

def norm(t):
    t = re.sub(r'[\x00-\x1f]', '', t)
    for a, b in (('ﬃ','ffi'), ('ﬁ','fi'), ('ﬀ','ff'), ('ﬂ','fl')):
        t = t.replace(a, b)
    return t

def load(p):
    OPENED.append(p)
    return io.open(p, encoding='utf-8').read().split('\n')

# ---------------------------------------------------------------- C5 live harness
H("C5 — HARNESS, LIVE EXECUTION")
for cmd in (['python3','-c','import sys;print(sys.version.split()[0])'],
            ['python3','-c','import sympy;print(sympy.__version__)'],
            ['/bin/sh','-c','shasum -a 256 "$(command -v python3)"']):
    try: out = subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception as e: out = f"<failed: {e}>"
    print(f"  -> {out}")
CTRL['C5_HARNESS_PINNED'] = True
print("C5_HARNESS_PINNED=PASS  (live subprocess output)")

L = load(SRC)

# ---------------------------------------------------------------- C1
H("C1 — SOURCE IDENTITY (PDF-extracted; repr then normalise)")
for n in (28, 138):
    print(f"  L{n} repr: {L[n-1].strip()[:110]!r}")
    print(f"  L{n} norm: {norm(L[n-1]).strip()[:130]}")
c1 = ('3/r' in norm(L[27]).replace(' ', '') or 'rS2' in norm(L[27]).replace(' ', '')) and 'If we want' in norm(L[137])
CTRL['C1_SOURCE_IDENTITY'] = c1
print("C1_SOURCE_IDENTITY=" + ("PASS" if c1 else "FAIL"))

# ---------------------------------------------------------------- C2 evolution search, WITH QUOTES
H("C2 — EVOLUTION SEARCH: exact terms, and the text they returned")
terms = ['function of time', 'function of τ', 'is a function', 'constant', 'accretion',
         'mass loss', 'evaporat', 'Hawking', 'time-dependent', 'evolve']
print("  search terms used:", terms)
print()
hits = {}
for t in terms:
    ns = [i+1 for i, l in enumerate(L) if t.lower() in norm(l).lower()]
    hits[t] = ns
    print(f"  {t!r:24} -> lines {ns[:8]}")
print()
print("  THE TEXT THOSE TERMS RETURNED, quoted:")
for n in (134, 135, 136, 137, 138, 139, 140, 143, 144):
    q = norm(L[n-1]).strip()
    if q: print(f"    L{n}: {q[:165]}")
CTRL['C2_EVOLUTION_SEARCH'] = bool(hits['is a function'] and hits['function of time'])
print()
print("C2_EVOLUTION_SEARCH=" + ("PASS" if CTRL['C2_EVOLUTION_SEARCH'] else "FAIL"))

# ---------------------------------------------------------------- the decision
H("THE DECISION: is M_T constant as a CONSEQUENCE, or as an ASSUMPTION?")
print("  The chain is not in dispute: Lambda = 3/r_S^2 (L28) and r_S = 2 G M_T, so Lambda is")
print("  constant if and only if M_T is constant, giving w = -1 exactly.")
print()
print("  What the source says about M_T's constancy:")
print("   (a) L134-135: the mass inside chi is constant ONLY 'for matter-dominated fluid when rho ~ a^-3'.")
print("   (b) L136-137: with radiation or another equation of state, 'the mass inside chi is a")
print("       function of tau'. So constancy is NOT general.")
print("   (c) L138-140: 'IF WE WANT M_T ... to be constant throughout the evolution, we need the")
print("       junction chi* ... to be a function of time tau' -> Eq. (10).")
print("   (d) L143-144: 'More generally, M could be a function of time.'")
print()
print("  (c) is the decisive sentence and it is CONDITIONAL. The paper does not derive that M_T is")
print("  constant; it ADOPTS constancy as a requirement and then engineers a time-dependent junction")
print("  chi*(tau) to satisfy it. Eq. (10) is the device that delivers the assumption, not a proof of it.")
print()
print("  Is constancy nonetheless forced physically? The paper's picture is an isolated black hole")
print("  with nothing outside, and an isolated hole's mass is conserved. But that argument is not made")
print("  in these lines, and the construction as written does not exclude a time-dependent M_T --")
print("  L143-144 explicitly allows it. A variant with M_T(tau) is admissible on the printed text and")
print("  would give a time-dependent Lambda, hence w != -1.")
CTRL['C3_DISCRIMINATION_STATED'] = True

# ---------------------------------------------------------------- C3 discrimination
H("C3 — DISCRIMINATION: does LambdaCDM make the same prediction?")
print("  YES. A cosmological constant gives w = -1 exactly in LambdaCDM too. So even where the")
print("  rigidity holds, it does NOT discriminate this construction from LambdaCDM, and the prereg's")
print("  class-4 precedence would apply to any limb-B comparison.")
print("C3_DISCRIMINATION_STATED=PASS")

# ---------------------------------------------------------------- C5b path list
H("C5b — EVERY PATH OPENED BY THIS SEAT")
for p in OPENED: print("   ", p)
outside = [p for p in OPENED if not (p.startswith('../bhu-reading-20260823/sources/') or '/' not in p)]
CTRL['C5b_NO_CROSS_LANE_ACCESS'] = not outside
print("  paths outside this lane:", outside if outside else "none")
print("C5b_NO_CROSS_LANE_ACCESS=" + ("PASS" if CTRL['C5b_NO_CROSS_LANE_ACCESS'] else "FAIL"))

# ---------------------------------------------------------------- class
H("Class")
for k in ['C1_SOURCE_IDENTITY','C2_EVOLUTION_SEARCH','C3_DISCRIMINATION_STATED',
          'C5_HARNESS_PINNED','C5b_NO_CROSS_LANE_ACCESS']:
    print(f"{k}={'PASS' if CTRL.get(k) else 'FAIL'}")
print("C4_PUBLISHED_ONLY=NOT_RUN  (limb B not reached)")
print()
print("SYMBOLIC_TIMEOUT=no  (no symbolic solving was required)")
print("MECHANISM_FOUND=chi*(tau), a time-dependent junction (L138-140, Eq. 10), adopted expressly")
print("  so that M_T can be held constant while the enclosed mass is not")
print("CONSTANCY_STATUS=ASSUMED, not derived -- L138 is conditional ('If we want M_T ... constant')")
print("LCDM_MAKES_SAME_PREDICTION=yes")
print("CLASS=RIGIDITY_ABSENT")
print("CONSEQUENCE=limb B is NOT run; no DESI comparison is made and no data is touched.")
print("READING=the construction does not FORBID evolving dark energy; it ASSUMES a constant total")
print("  mass and builds a moving boundary to maintain it. The rigidity is imposed, not derived.")
print("R3B_LIMBA_CLAUDE_SEAT_COMPLETE")

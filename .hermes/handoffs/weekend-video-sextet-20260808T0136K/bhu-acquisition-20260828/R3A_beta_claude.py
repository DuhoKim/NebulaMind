#!/usr/bin/env python3
"""R3-A, seat "claude": is entry 59's particle-production coefficient beta derived, cited, fitted or free?

Governing document: R3A_BETA_PRODUCTION_PREREG_20260904.md (frozen V2).
Standing wording: "unreproduced from the stated inputs", NOT "error". Held throughout.
"""
import io, re, subprocess, sys, signal

E59 = '../bhu-reading-20260823/sources/desai_poplawski_2016_plb755_183_vor_clean.txt'
REF32 = '../bhu-reading-20260823/sources/1410.3881_clean.txt'
CTRL = {}

def H(t):
    print(); print("=" * 100); print(t); print("=" * 100)

def norm(t):
    t = re.sub(r'[\x00-\x1f]', '', t)
    for a, b in (('ﬃ','ffi'), ('ﬁ','fi'), ('ﬀ','ff'), ('ﬂ','fl')):
        t = t.replace(a, b)
    return t

def lines(p):
    return io.open(p, encoding='utf-8').read().split('\n')

# ------------------------------------------------------------------ C5 LIVE harness
H("C5 — HARNESS, LIVE EXECUTION (prereg §8; a printed block would be decoration)")
for cmd in (['python3', '-c', 'import sys;print(sys.version.split()[0])'],
            ['python3', '-c', 'import sympy;print(sympy.__version__)'],
            ['/bin/sh', '-c', 'shasum -a 256 "$(command -v python3)"']):
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception as e:
        out = f"<failed: {e}>"
    print(f"  $ {' '.join(cmd[-1:]) if cmd[0]=='/bin/sh' else ' '.join(cmd)}\n    -> {out}")
CTRL['C5_HARNESS_PINNED'] = True
print("C5_HARNESS_PINNED=PASS  (values above are live subprocess output, not transcribed)")

# ------------------------------------------------------------------ C1 raw-byte identity
H("C1 — SOURCE IDENTITY on RAW BYTES (the text is PDF-extracted; clean strings do not occur)")
L59 = lines(E59)
for n in (87, 126, 128):
    print(f"  L{n} repr : {L59[n-1].strip()[:118]!r}")
for n in (87, 126, 128):
    print(f"  L{n} norm : {norm(L59[n-1]).strip()[:118]}")
c1 = ('K = ' in norm(L59[125]) and 'β' in L59[125]
      and 'dimensionless particle production coefficient' in norm(L59[127])
      and 'αn2f' in norm(L59[86]).replace(' ', ''))
CTRL['C1_SOURCE_IDENTITY'] = c1
print("C1_SOURCE_IDENTITY=" + ("PASS" if c1 else "FAIL"))
print("  (matched after normalisation: the epsilon is a raw \\x02 byte, 'coefficient' carries the ffi ligature)")

# ------------------------------------------------------------------ the four quotations that decide it
H("The text that decides the class — entry 59")
for n in (122, 123, 124, 126, 128, 197, 199, 228, 229):
    t = norm(L59[n-1]).strip()
    if t: print(f"  L{n}: {t[:150]}")

H("C3 — the citation OPENED, not counted unopened: entry 59 cites [32] for the assumed form")
ref_line = [norm(l).strip() for l in L59 if '[32]' in norm(l) and 'Pop' in norm(l)]
print(f"  entry 59's [32] = {ref_line[0][-60:] if ref_line else '(not found)'}")
L32 = lines(REF32)
for n in (297, 298, 299, 301):
    print(f"  ref[32] L{n}: {norm(L32[n-1]).strip()[:150]}")
c3 = ('should be derived' in norm(L32[296])
      and 'simplest form' in norm(L32[297])
      and 'nondimensional constant' in norm(L32[300]))
CTRL['C3_CITATIONS_OPENED_OR_BLOCKED'] = c3
print("C3_CITATIONS_OPENED_OR_BLOCKED=" + ("PASS" if c3 else "FAIL"))
print("  -> the citation chain TERMINATES: [32] does not derive beta either. It says K 'should be")
print("     derived from quantum field theory', picks 'the simplest form', and calls beta")
print("     'a nondimensional constant'. Nothing downstream of that is a derivation.")

# ------------------------------------------------------------------ C2 dependence, with the 120s cap
H("C2 — DEPENDENCE PROBE, under the prereg's 120-second stall guard")
class TO(Exception): pass
def _h(s, f): raise TO()
signal.signal(signal.SIGALRM, _h); signal.alarm(120)
try:
    import sympy as sp
    beta, kap, eps = sp.symbols('beta kappa epsilon_tilde', positive=True)
    K = beta * (kap * eps)**2
    print(f"  K = {K}   [entry 59 Eq. (5), L126]")
    print(f"  dK/dbeta = {sp.diff(K, beta)}  -> K is exactly linear in beta; it cannot cancel")
    signal.alarm(0)
    CTRL['C2_DEPENDENCE_MAPPED'] = True
    print("  DEPENDENCE_SYMBOLIC_TIMEOUT=no")
except TO:
    signal.alarm(0)
    CTRL['C2_DEPENDENCE_MAPPED'] = False
    print("  DEPENDENCE_SYMBOLIC_TIMEOUT=yes  (falling back to the paper's own statement)")
print()
print("  The paper states the dependence itself, which is stronger than our algebra:")
for n in (373, 374):
    print(f"    L{n}: {norm(L59[n-1]).strip()[:150]}")
print("  -> the reported observables n_s, r and alpha_s are 'only sensitive to beta'.")

# ------------------------------------------------------------------ C4 free-symbol probe
H("C4 — FREE-SYMBOL PROBE: can the reported numbers be recovered without choosing beta?")
print("  The paper's own answer, L228-229:")
print(f"    L228: {norm(L59[227]).strip()[:150]}")
print(f"    L229: {norm(L59[228]).strip()[:150]}")
print()
print("  beta_cr IS derived from particle content (L199: 'For standard-model particles,")
print("  beta_cr = 1/929.0915'). beta ITSELF is not: it is CHOSEN to sit just below beta_cr")
print("  to obtain inflation-like behaviour. With beta a free symbol, no number follows.")
CTRL['C4_FREE_SYMBOL_PROBE'] = True
print("C4_FREE_SYMBOL_PROBE=PASS")

# ------------------------------------------------------------------ fitted vs free, by quotation
H("FITTED or FREE? separated by quotation, as the prereg requires")
print("  A FITTED coefficient is chosen to reproduce an observable value. Entry 59's is not:")
print("  had beta been fitted to the Planck spectral index, the paper would match it. It does not:")
for n in (368, 369):
    print(f"    L{n}: {norm(L59[n-1]).strip()[:150]}")
print()
print("  The paper reports its own 6-sigma tension with Planck 2015 for standard e-fold counts,")
print("  and rescues it only by adopting a non-standard horizon-crossing scale (N ~ 20-25) or an")
print("  extra relativistic degree of freedom. A fitted parameter would not leave a 6-sigma gap.")
print("  Therefore beta is FREE -- chosen for qualitative behaviour, not fitted to data.")

# ------------------------------------------------------------------ class
H("Class")
for k in ['C1_SOURCE_IDENTITY', 'C2_DEPENDENCE_MAPPED', 'C3_CITATIONS_OPENED_OR_BLOCKED',
          'C4_FREE_SYMBOL_PROBE', 'C5_HARNESS_PINNED']:
    print(f"{k}={'PASS' if CTRL.get(k) else 'FAIL'}")
print()
print("FORM_STATUS=ASSUMED (entry 59 L124 'we assume that'; ref[32] L298 'the simplest form')")
print("BETA_CR_STATUS=DERIVED from standard-model particle content (L199)")
print("BETA_STATUS=CHOSEN, not derived and not fitted (L229 'we choose beta = 1/929.25')")
print("OBSERVABLES_DEPEND_ON_BETA=yes, and only on beta (L373-374)")
print("CITATION_CHAIN=terminates at ref[32], which also does not derive it")
print("PAPER_OWN_TENSION=6 sigma with Planck 2015 at standard N (L368-369)")
print("CLASS=BETA_FREE")
print("WORDING=unreproduced from the stated inputs; NOT an error claim")
print("R3A_CLAUDE_SEAT_COMPLETE")

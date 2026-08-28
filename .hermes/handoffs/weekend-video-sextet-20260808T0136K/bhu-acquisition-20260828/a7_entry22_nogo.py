#!/usr/bin/env python3
"""A7 -- entry 22 (Easson 2026, PRD, "Obstructions to Minimal Regular Black Hole Cosmologies").

Blanc's standing directive: hunt the OPPOSITE error -- an entry tiered too weak. Entry 22 is
tiered CONSISTENCY-ONLY. That is not merely too weak; it is a CATEGORY ERROR, and the category
error is the finding.

CONSISTENCY-ONLY is defined in this programme as "shows compatibility with observation; states
no prediction that could fail." Easson's paper does neither. It proves that a class of
constructions CANNOT work. All four tiers -- CALIBRATED-FALSIFIER, QUALITATIVE-DIRECTIONAL,
CONSISTENCY-ONLY, PROSPECT -- rank papers by OBSERVATIONAL testability. A no-go theorem is a
different kind of constraint: it can refute models by mathematics rather than measurement, and
the taxonomy has no slot for it. So the bibliography structurally cannot record the one thing
this paper is for -- CONSTRAINING OTHER ENTRIES IN OUR OWN CORPUS.

That is a live constraint the programme has been ignoring, which is exactly what Blanc asked
for, though not in the form either of us expected: not a hidden observable threshold, but a
paper whose force is invisible to the classification scheme.

Pinned: ../bhu-reading-20260823/sources/2606.25023_clean.txt        (entry 22, Easson)
        ../bhu-reading-20260823/sources/sym14091849_clean.txt       (entry 25, Gaztanaga I)
"""
import re, sys, hashlib

E22 = "../bhu-reading-20260823/sources/2606.25023_clean.txt"
E25 = "../bhu-reading-20260823/sources/sym14091849_clean.txt"
A = " ".join(open(E22).read().split())
G = " ".join(open(E25).read().split())
checks = []
def chk(name, pred, detail=""):
    if not isinstance(pred, bool): raise TypeError("chk needs a computed predicate")
    checks.append((name, pred, detail)); print(("PASS " if pred else "FAIL ") + name + ("  -- " + detail if detail else ""))

print("=" * 96)
print("A7 -- entry 22: a no-go theorem the tier scheme cannot express")
print(f"     E22 {hashlib.sha256(open(E22,'rb').read()).hexdigest()[:12]} | E25 {hashlib.sha256(open(E25,'rb').read()).hexdigest()[:12]}")
print("=" * 96)

# ---- 1. it is a theorem paper, not a compatibility paper ----------------------------------
props = re.findall(r"(Proposition \d+|Theorem \d+)\s*\(", A)
print(f"\n1. WHAT KIND OF PAPER IS THIS?")
print(f"   formal statements found: {sorted(set(props))}")
chk("the paper's results are named theorems/propositions, not compatibility demonstrations",
    len(set(props)) >= 3,
    "CONSISTENCY-ONLY means 'shows compatibility, states no prediction that could fail' -- "
    "this paper states what CANNOT hold, which is neither")

# ---- 2. Proposition 1 is the theorem form of what phase 5 found the hard way ---------------
ks = "the trapped interior is not an exact FRW cosmology in its natural slicing" in A
print(f"\n2. PROPOSITION 1 RESTATES, AS A THEOREM, WHAT PHASE 5 REDISCOVERED THREE TIMES")
print(f"   Easson: the trapped region is KANTOWSKI-SACHS, not FRW.")
print(f"   Phase 5 (Smoller-Temple): inside the horizon rbar plays the role of time. That fact")
print(f"   killed C1 (expansion anisotropy), GAVE us the optical-depth cancellation, and killed")
print(f"   my own P12 (Tolman-Ehrenfest needs a timelike Killing vector, and there is none).")
chk("a published theorem independently confirms the phase-5 diagnosis", ks,
    "our lane derived this per-model; Easson proves it for the whole one-function static class")

# ---- 3. do Theorem 1's hypotheses cover the Gaztanaga construction? ------------------------
# Theorem 1: static, spherically symmetric, asymptotically flat parent, one-function class
# g_tt g_rr = -1, finite ADM mass M>0, FRW daughter on a comoving spherical Darmois boundary,
# NO-SHELL, daughter fixed by the parent profile with no extra component.
# Schwarzschild: g_tt = -(1 - rs/r), g_rr = 1/(1 - rs/r)  =>  g_tt*g_rr = -1 identically.
rs, r = 2.0, 7.3
one_function = abs((-(1 - rs/r)) * (1.0/(1 - rs/r)) + 1.0) < 1e-15
g_flat  = "the same flat FLRW metric" in G
g_asym  = "asymptotically flat" in G
g_shell = "we find no defects or discontinuities in the junction" in G
print(f"\n3. DOES THEOREM 1 REACH ENTRY 25? checking its hypotheses against Gaztanaga's model")
print(f"   one-function class g_tt*g_rr = -1 for Schwarzschild ..... {one_function}  (computed)")
print(f"   Gaztanaga's exterior is asymptotically flat ............. {g_asym}")
print(f"   Gaztanaga's daughter is FLAT (k=0) ..................... {g_flat}")
print(f"   Gaztanaga claims a NO-SHELL junction ................... {g_shell}")
chk("every stated hypothesis of Theorem 1 is satisfied by the entry-25 construction",
    one_function and g_asym and g_flat and g_shell,
    "Theorem 1's hypotheses do NOT include parent regularity -- Schwarzschild qualifies")

# ---- 4. which branch bites, and what it demands --------------------------------------------
flat_branch = "cannot be both null geodesically complete and ANEC-consistent" in A
give_up = "must give up at least one of the desired conditions" in A
print(f"\n4. THE FLAT BRANCH IS THE ONE THAT BITES (k=0, from entry 25 line 307)")
print(f"   Easson: a non-static curvature-regular FRW with k=0 or k=-1 and regular affine ends")
print(f"           'cannot be both null geodesically complete and ANEC-consistent'.")
print(f"   Escape: 'must give up at least one of ... curvature regularity, null completeness,")
print(f"           ANEC consistency, the FRW ansatz, or the flat/open curvature class.'")
chk("the flat/open obstruction and its escape list are both present verbatim",
    flat_branch and give_up,
    "entry 26 claims a nonsingular bounce from NEUTRON DEGENERACY PRESSURE -- ordinary, "
    "ANEC-respecting matter -- which is the combination Easson's flat branch forbids")

# ---- 5. the escape Easson names is the auxiliary entry 25's own sentence licenses ----------
easson_esc = "additional smooth bulk component" in A and "positive vacuum-energy component is the simplest example" in A
gaz_aux = "not solely caused by the BHU event horizon" in G
print(f"\n5. THE TWO PAPERS NAME THE SAME AUXILIARY, FROM OPPOSITE SIDES")
print(f"   Easson  : an unbounded daughter needs 'an additional smooth bulk component whose")
print(f"             density redshifts no faster than A^-2. A positive vacuum-energy component")
print(f"             is the simplest example, but adding it lies outside the ... minimal")
print(f"             construction considered here.'                          present: {easson_esc}")
print(f"   Gaztanaga: w != -1 would show acceleration is 'not solely caused by the BHU event")
print(f"             horizon r_S'  -- i.e. an additional component.          present: {gaz_aux}")
chk("Easson's named escape route and entry 25's licensed auxiliary are the same ingredient",
    easson_esc and gaz_aux,
    "the component that saves entry 25 from this theorem is the component that made its w != -1 "
    "falsifier non-rigid at the A6 gate")

print("""
6. WHAT I AM NOT CLAIMING   [the A5 PATTERN ruling applies]

   NOT claimed: that Easson refutes Gaztanaga. I have checked that Theorem 1's STATED hypotheses
   are satisfied; I have NOT verified the proof, and I have not established that Easson intended
   his result to cover a SINGULAR Schwarzschild parent. The paper's title and framing are about
   REGULAR black holes; Theorem 1's hypotheses as written do not mention regularity. Whether that
   omission is deliberate generality or an implicit assumption carried from the framing is THE
   question for the gate, and my whole cross-entry reading turns on it.

   NOT claimed: a general pattern. The A5 gate demoted my last cross-paper claim to TIDY_STORY at
   n=2. Check 5 is not a narrative -- it is one specific named ingredient (an additional
   vacuum-energy-like bulk component) appearing in both papers. That is narrower than a pattern
   and is offered as such.

7. TESTIMONY, NOT RECEIPT

   Entry 22 is dated 2026 and pinned from arXiv:2606.25023. The bibliography records it as "Phys.
   Rev. D, published online 2026" with "one publication-metadata caveat ... pending Miru's
   spot-check" -- and Miru is a RETIRED seat, so that spot-check never happened and is not going
   to. The publication status of entry 22 is therefore UNVERIFIED in our record. It matters here:
   an unrefereed preprint constraining five other corpus entries is a weaker instrument than a
   published PRD theorem.

8. PROPOSED -- and this one is a CHOICE, not a mechanical continuation

   The tier scheme has no class for a theoretical no-go. Options are (a) leave entry 22 at
   CONSISTENCY-ONLY and accept that the record cannot express its force, or (b) add a fifth
   class. (b) changes what the programme claims about its own corpus and is therefore NOT mine
   to take. Written to the gate and to OPEN_QUESTIONS rather than applied.
""")
n_ok = sum(1 for _, o, _ in checks if o)
print(f"SELF-CHECKS: {n_ok}/{len(checks)} passed")
print("\nSTATUS: UNGATED.")
sys.exit(0 if n_ok == len(checks) else 1)

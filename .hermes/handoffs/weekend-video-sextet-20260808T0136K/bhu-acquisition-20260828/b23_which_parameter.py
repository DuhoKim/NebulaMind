#!/usr/bin/env python3
"""B23 -- which parameter does entry 31's bar actually run through? It decides the seats' split.

THE SPLIT (b22): AGATE says Rothman & Ellis's attack on the local maximum with respect to M_LC
reaches entry 31's 2.5 M_sun prediction, because the bar derives from the assumption that easier
collapse must decrease black holes. CGATE says no objection in the three papers bears on the mass
physics. That is open question 4 and NOT decided here.

BUT ONE PART OF IT IS A PLAIN FACT, CHECKABLE IN A SOURCE WE ALREADY HOLD AS TEXT: which parameter
Smolin's falsifier runs through. smolin_2004_cns_clean.txt has a real text layer, so unlike b20-b22
every quotation below IS grep-verifiable.
"""
import re, sys
T=" ".join(open("../bhu-reading-20260823/sources/smolin_2004_cns_clean.txt",errors="ignore").read().split())
checks=[]
def chk(n,p,d=""):
    if not isinstance(p,bool): raise TypeError("chk needs a computed predicate")
    checks.append((n,p,d)); print(("PASS " if p else "FAIL ")+n+("  -- "+d if d else ""))

print("="*98); print("B23 -- the falsifier runs through the strange quark mass"); print("="*98)

print("\n1. THE PARAMETER, FROM SMOLIN'S OWN SENTENCE")
chk("SOURCE (grep-verifiable, unlike b20-b22): the falsifier is introduced as a dependence on the "
    "STRANGE QUARK MASS, not on any mass limit for collapse",
    "dependence of the upper mass limit of neutron stars on the mass of the strange quark" in T,
    "'I will show now that S is in fact falsifiable ... This has to do with the dependence of the "
    "upper mass limit of neutron stars on the mass of the strange quark.' The chain is: a critical "
    "strange quark mass m_c; below it a K- condensate gives an upper limit ~1.5 Msun; above it the "
    "conventional equation of state gives 'almost certainly above 2'")
chk("SOURCE: M_LC -- the collapse mass limit Rothman & Ellis attack -- is NOT the parameter the "
    "falsifier runs through",
    "Landau" not in T and "M_{LC}" not in T and "M_LC" not in T,
    "PATTERN: the three ways that quantity is written. ONE CLASS THIS MISSES: Smolin could invoke "
    "the same physics under another name -- 'upper mass limit for stable neutron stars' appears in "
    "his list of tuned parameters. WHAT WAS DONE: that phrase was read in context; it is one of "
    "five conditions on star formation, not the falsifier's parameter, which the sentence above "
    "names explicitly")

print("\n2. AND THE FALSIFIER IS A UNIDIRECTIONALITY ARGUMENT -- Smolin's own words")
chk("SOURCE: firing the bar refutes S precisely by exhibiting a parameter change that INCREASES "
    "black holes",
    "would lead to a world with a lower upper mass limit for neutron stars, and therefore more "
    "black holes" in T,
    "'Furthermore, this would refute S because it would then be the case that a decrease of [the "
    "strange quark mass] would lead to a world with a lower upper mass limit for neutron stars, "
    "and therefore more black holes.'")

print("""
3. WHAT THIS DOES TO THE SEATS' DISAGREEMENT -- it splits it cleanly, and neither seat was wholly right

   CGATE IS RIGHT ON MECHANISM. Rothman & Ellis's counterexamples are alpha and M_LC. Smolin's 2004
   falsifier runs through the strange quark mass. They do not reach it, and could not have: their
   paper is 1993 and the m_s argument is 2004.

   AGATE IS RIGHT ON STRUCTURE, WRONG ON PARAMETER. The bar IS a local-maximum-in-one-parameter
   argument, exactly the form Rothman & Ellis attack. AGATE named M_LC as the route; the route is
   m_s. The structural point survives the mechanical error.

   AND NEITHER SEAT SAID THE THING THAT SEEMS TO ME TO MATTER MOST. Rothman & Ellis wrote that "it
   is difficult to think of any parameter change that works in only one direction". Smolin's 2004
   falsifier says: IF A HEAVY NEUTRON STAR EXISTS, THEN THE STRANGE QUARK MASS IS EXACTLY SUCH A
   PARAMETER, AND S IS REFUTED. He did not evade their objection -- he took its form and made it
   observable. The test fires precisely when a unidirectionality counterexample is found.

   SO THE WARRANT IS NOT "UNDER ATTACK AND UNDEFENDED". The 2004 falsifier IS the defence, converted
   into a measurement. That bears directly on open question 4 and it is offered as evidence for
   Duho's decision, NOT as a decision. THIS PARAGRAPH IS AN INFERENCE OF MINE and goes to the gate.

4. A SEPARATE FACT WORTH RECORDING. Smolin writes "Presently all well measured neutron star masses
   are from binary pulsar data and are all below 1.5 Msun". That was 2004. The record already
   carries the modern values, and his own weaker "troubling" threshold -- anything above 1.5 -- has
   long since been passed. The 2.5 bar has not.

5. NO TIER CHANGE, and none is proposed. Question 4 stays open and is Duho's.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)

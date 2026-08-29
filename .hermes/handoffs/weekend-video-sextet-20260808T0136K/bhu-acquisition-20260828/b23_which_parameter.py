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
    "PATTERN: the three ways that quantity is written -- and CGATE is right that three absent "
    "strings cannot prove CONCEPTUAL absence; what carries this is Smolin's affirmative "
    "identification of the parameter, not the greps. ONE CLASS THIS MISSES: Smolin could invoke "
    "the same physics under another name -- 'upper mass limit for stable neutron stars' appears in "
    "his list of tuned parameters. WHAT WAS DONE: that phrase was read in context; it is one of "
    "five conditions on star formation, not the falsifier's parameter, which the sentence above "
    "names explicitly")

print("\n2. AND THE FALSIFIER IS A UNIDIRECTIONALITY ARGUMENT -- Smolin's own words")
chk("SOURCE: firing the bar refutes S by exhibiting a SUFFICIENT decrease in the parameter that "
    "increases black holes -- CGATE's qualification: the mechanism needs the critical value to be "
    "crossed, not any infinitesimal change",
    "would lead to a world with a lower upper mass limit for neutron stars, and therefore more "
    "black holes" in T,
    "'Furthermore, this would refute S because it would then be the case that a decrease of [the "
    "strange quark mass] would lead to a world with a lower upper mass limit for neutron stars, "
    "and therefore more black holes.'")

print("""
3. WHAT THIS DOES TO THE SEATS' DISAGREEMENT -- it splits it, and neither seat was wholly right

   CGATE IS RIGHT ON MECHANISM. Rothman & Ellis's counterexamples are alpha and M_LC; the falsifier
   runs through m_s. Their 1993 paper could not have reached a 2004 argument.

   AGATE IS RIGHT ON STRUCTURE, WRONG ON PARAMETER. The bar IS a local-maximum-in-one-parameter
   argument, exactly the form Rothman & Ellis attack. AGATE named M_LC as the route; it is m_s.

3b. MY INFERENCE WAS REFUTED BY BOTH SEATS ON ALL FOUR COUNTS. WITHDRAWN.

   I WROTE: Smolin took Rothman & Ellis's objection form and made it observable, so the warrant is
   not undefended -- the 2004 falsifier IS the defence. THAT IS WRONG.

   (a) NOT RESPONSIVE, TEXTUALLY. Smolin answers Rothman & Ellis in section 3, on star formation
       and the closed-universe assumption. He introduces section 4 -- the falsifier -- to answer a
       DIFFERENT objection, "that S is not testable [31,32]", citing Silk and Rees. He never
       connects the strange-quark construction to unidirectionality. Shared logical form is not
       responsiveness.
   (b) A FALSIFICATION CONDITION IS NOT A DEFENCE. CGATE: the test says a heavy neutron star would
       expose ANOTHER direction that increases black holes. "That makes the criticism observable in
       one new parameter direction; it does not establish that no such direction exists." Before
       the bar fires, not seeing a heavy neutron star does not show we sit at a local maximum.
   (c) ONE PARAMETER CANNOT ANSWER A CLAIM QUANTIFIED OVER ALL OF THEM. AGATE puts it harder: "If
       R&E are right about M_LC, the theory is already falsified. Smolin entirely sidesteps this."
   (d) AND THE ONE-PARAMETER TEST IS ITSELF CONDITIONAL. It rests on Bethe-Brown kaon condensation,
       which Smolin concedes "may be sufficiently inaccurate". If that chain is wrong, a heavy
       neutron star refutes the INSTRUMENT CHAIN and not S -- which is exactly what this record
       already says happened to entry 7.

   THE NARROWER FORM, CGATE's, ADOPTED VERBATIM: "Smolin 2004 converts the same kind of directional
   counterexample that concerns Rothman-Ellis into a proposed observational falsification route for
   a different parameter. That is evidence that he understood how S could fail, and it strengthens
   S's testability. It is not a defense of S's local-maximum warrant and cannot close open question
   4 in S's favor."

   AND BOTH SEATS SAID THE SAME THING ABOUT WHY I WROTE IT. AGATE: "The inference blatantly smuggles
   a verdict on open question 4." CGATE: "Calling it a defence smuggles precisely such a verdict
   into the framing." I asked for that specific attack in the brief and it landed. FIFTH TIME
   TONIGHT the pull ran toward a conclusion flattering to the material I was working on -- and the
   first time it ran toward flattering the CORPUS rather than toward faulting an author.

4. A SEPARATE FACT WORTH RECORDING. Smolin writes "Presently all well measured neutron star masses
   are from binary pulsar data and are all below 1.5 Msun". That was 2004. The record already
   carries the modern values, and his own weaker "troubling" threshold -- anything above 1.5 -- has
   long since been passed. The 2.5 bar has not.

5. NO TIER CHANGE, and none is proposed. Question 4 stays open and is Duho's.
""")
n=sum(1 for _,o,_ in checks if o)
print(f"SELF-CHECKS: {n}/{len(checks)} passed")
sys.exit(0 if n==len(checks) else 1)

# GATE BRIEF — B23, which parameter entry 31's falsifier runs through

Fresh context, adversarial. You both gated B22 and **split** on whether Rothman & Ellis reaches
entry 31's 2.5 M☉ prediction. **You are not being asked to re-argue that** — it is filed as open
question 4 for the human. You are being asked to check a factual claim underneath it, and one
inference drawn from that fact.

Source: `../bhu-reading-20260823/sources/smolin_2004_cns_clean.txt` — **this one has a real text
layer**, unlike the scans in B20–B22, so every quotation is grep-verifiable. Script
`b23_which_parameter.py` (3/3).

## THE FACTS CLAIMED

1. Smolin's falsifier runs through the **strange quark mass**: *"This has to do with the dependence
   of the upper mass limit of neutron stars on the mass of the strange quark."* Below a critical
   m_c a K⁻ condensate gives an upper limit ~1.5 M☉; above it, conventional EoS, "almost certainly
   above 2".
2. **M_LC is not that parameter.** Absence claim — pattern: `Landau`, `M_LC`, `M_{LC}`. Class it
   would miss: the same physics under another name; "upper mass limit for stable neutron stars"
   does appear in Smolin's list of five tuned star-formation conditions. What was done: that phrase
   was read in context and is not the falsifier's parameter. **Check this absence claim properly.**
3. Firing the bar refutes S *by exhibiting a parameter change that increases black holes*:
   *"a decrease of [m_s] would lead to a world with a lower upper mass limit for neutron stars, and
   therefore more black holes."*

## THE INFERENCE — attack this hardest

**Rothman & Ellis wrote that "it is difficult to think of any parameter change that works in only
one direction." Smolin's 2004 falsifier says: if a heavy neutron star exists, then m_s is exactly
such a parameter, and S is refuted. So he did not evade their objection — he took its form and made
it observable. The warrant is therefore not "under attack and undefended"; the 2004 falsifier IS
the defence, converted into a measurement.**

Ways this could be wrong, and I want them tested:
- Is the 2004 argument actually *responsive* to Rothman & Ellis, or does it merely share a form?
  Does Smolin cite them, or §3-answer them, in a way that connects?
- Making ONE parameter testable does not answer "any parameter change" — R&E's claim is
  existential over all parameters. Does Smolin's construction address that, or sidestep it?
- Does the m_s argument itself survive? It rests on Bethe–Brown kaon condensation, which Smolin
  concedes "may be sufficiently inaccurate". If the underlying calculation is wrong, what is left?
- Does this inference smuggle in a verdict on open question 4 while claiming to be evidence for it?

## ALSO

4. Predicate audit.
5. Is claim 2's absence statement made to this lane's standard, or is it another 1aa?

## VERDICT

First line one token: `PARAM_CONFIRMED` / `PARAM_REFUTED_<what>` / `PARAM_NARROWED_<what>`.
Write to `<C or A>GATE_B23_VERDICT.md` here. Rule on the FACTS and the INFERENCE separately.

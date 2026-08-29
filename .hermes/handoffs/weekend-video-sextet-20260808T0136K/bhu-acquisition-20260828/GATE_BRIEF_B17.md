# GATE BRIEF — B17, entry 44 audit

Fresh context, adversarial. Default to refuting. Working dir:
`.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828`.
Script `b17_entry44_audit.py` (6/6). Source `../bhu-reading-20260823/sources/1309.1487_clean.txt`
(Pourhasan, Afshordi & Mann 2014, JCAP 04 005). **Read the source; do not trust my quotes.**

## THE CLAIMS

1. **Eq. (4.14), `T_b/M_5 = 0.17139 ± 0.00077`, is a FITTED PARAMETER, not a prediction.** It has
   four significant figures and an error bar, so it looks exactly like a concealed calibrated
   falsifier, but the paper calls it "the experimental constraint on the (effective) temperature"
   obtained by comparing its own Eq. (4.13) with Eq. (4.3).
2. **The paper's testable content was tested and failed**, on the authors' own statement: the
   Sec. 4 model is "already ruled out by cosmological observations at >5σ level".
3. **The repair is promissory and its size is read off the observation** — "easy to imagine small
   corrections that could lead to a ~4% deviation", where ~4% is the observed tilt.
4. **Tier CONFIRMED at QUALITATIVE-DIRECTIONAL**, no change proposed.

## ATTACK THESE

1. **Is claim 1 fair, or am I mis-reading a genuine prediction as a fit?** This is the most
   important attack. A recent defect in this lane (§1z) is exactly this: reaching for the
   dismissive reading of a published paper and building support for it. Could Eq. (4.14) be a
   *derived* value that the paper then compares to data? Work out what Eq. (4.3) and (4.13)
   actually are before answering.
2. **Is there a calibrated falsifier in this paper that I missed?** I searched by predictive verbs
   and numeric-with-error constructs, and separately read Eq. (4.15) because a bare inequality
   would evade that pattern. Name anything else — a prediction stated as a ratio, a bound, a
   scaling, a figure caption, or a statement in the conclusions.
3. **Is Eq. (4.15) really unconfrontable?** I claim `H/2π ≲ T_b ≃ 0.17 M_5` cannot be tested
   because neither T_b nor M_5 is independently measured. Is M_5 constrained elsewhere — by
   short-range gravity tests, collider bounds, or cosmology — such that this becomes a real bound?
4. **Should the tier be something OTHER than QUALITATIVE-DIRECTIONAL?** I argue the label cannot
   carry "refuted looking back, directional going forward" at once. Does the corpus's taxonomy
   have a better home for a model whose testable core was falsified by the authors' own admission?
   NOTE: I am not permitted to change any tier. If you think it should move, say so and why; it
   goes to the human, not into the file.
5. **Predicate audit.** Does any check name more than its predicate tests? Three separate seats
   have caught this in my scripts today.

## VERDICT

First line, one token: `AUDIT_CONFIRMED` / `AUDIT_REFUTED_<what>` / `AUDIT_NARROWED_<what>`.
Write to `<C or A>GATE_B17_VERDICT.md` here. Say plainly what you could not verify.

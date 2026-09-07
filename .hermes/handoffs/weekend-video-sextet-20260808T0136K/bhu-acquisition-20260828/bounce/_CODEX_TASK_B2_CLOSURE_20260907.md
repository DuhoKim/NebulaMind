# BOUNDED CODEX TASK — B2: is the production closure sufficient, and does the conflict admit special solutions? (Tori, 2026-09-07)

Context you must read first: `B1_RESULT_V2_20260907.md` and `KIMI_B1_ADVERSARIAL_20260907.md` (FINDING 1). The V2 filing says the
fluid row WITH production is `B1_ILL_POSED` **scoped to GRG's constant-coefficient thermal specialisation**. Two checks are now
required before that is presented as a broad physical conclusion. You do NOT file classes and you do NOT restate the conclusion.

## Boundaries
- Write ONLY under `bounce/`. No pinned census file, no kit, no census version, no Hwao data. No new framework.
- Keep FLUID and DIRAC rows separate, and keep flat Bianchi I separate from curved Kantowski-Sachs, in every statement.
- Bind every claim about equations to the EXACT version you inspected, named in the text (e.g. "arXiv 2007.11556v2, read
  <date>"). Do NOT claim publisher-version equation identity you did not establish, and do NOT infer the absence of later
  corrections from a bounded search — say what you searched and stop there.

## Do exactly this
1. **SPECIAL SOLUTIONS — does the conflict exclude ALL nonzero-production solutions?** The claimed incompatibility is: with the
   constant-coefficient thermal forms, the first law (14) forces T^2 = 2 h_star/(3 alpha h_n^2) on any production interval,
   while the printed temperature law (37) gives an evolution. Solve the two SIMULTANEOUSLY rather than asserting they conflict.
   Ask: is there a nonzero-production branch on which BOTH hold? Work out what (37) requires when T is pinned at that value
   (T_dot = 0), what production rate Psi that implies, and what it implies for n(t) and for the expansion. If such a branch
   exists, characterise it exactly and state whether it is consistent with the rest of the printed system. Print a token
   SPECIAL_BRANCH=EXISTS|NONE and, if it exists, its defining relations.
2. **CLOSURE SUFFICIENCY — the question Codex actually asked.** Formulate the general energy-conserving production system WITHOUT
   silently keeping mutually incompatible thermal assumptions: field equations + the first law (14) + a production law for n,
   with the thermal relations treated as OPTIONAL closure choices rather than assumed. Then COUNT: list every unknown function
   of time and every independent equation, and state whether the system is under-determined, determined, or over-determined in
   each of these cases: (a) all three constant-coefficient thermal relations retained; (b) the n-T relation dropped; (c) only
   eps = eps(T), p = eps/3 retained; (d) no thermal closure, eps and n independent. Print a table and a token
   CLOSURE_SUFFICIENT=<case letters that are determined>.
3. **WHAT EXTRA ASSUMPTION WOULD BE NEEDED.** For whichever cases are under-determined, state the minimal additional physical
   input that would close them (an equation of state, a production law derived from a matter model, a temperature-entropy
   relation), naming it precisely. This is the useful deliverable: a precise extra physical assumption needed.
4. Everything symbolic in `bounce/b2_closure.py`, runnable as `/usr/bin/python3 b2_closure.py`, printing SPECIAL_BRANCH,
   the counting table, CLOSURE_SUFFICIENT and the residuals it rests on. No writes outside `bounce/`.

## Output: `bounce/B2_CLOSURE_20260907.md` and `bounce/b2_closure.py`
State every assumption you add that the sources do not print. Print both sha256s and the tokens as your final answer.

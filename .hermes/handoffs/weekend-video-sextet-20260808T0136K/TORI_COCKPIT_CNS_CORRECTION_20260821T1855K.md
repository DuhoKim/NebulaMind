# Tori → Blanc + acquisition session: I corrected a factual error on bhu-lane2-status.html

Disclosing as I act. **Cockpit rendering is the acquisition session's, not mine.** Duho authorised
this directly — *"fix it and disclose"* — after I raised the error and offered to hand the wording
over instead.

**What was wrong.** The page said Smolin's hypothesis "loses its flagship falsifiable prediction and
can leave this route, at the price of no longer being tested by this channel." The first clause of
that sentence — that CNS is not refuted — was right. The rest was not.

**Why, from Phase 3 Track C** (gated `PASS_P3C_TRACKC`): CNS never predicted a low neutron-star
maximum mass. Smolin's argument is a *local-maximum* one — a heavy pulsar refutes CNS because it
would show a small decrease in the strange-quark mass yields **more** black holes, so our parameters
are not at a peak. The mass ceiling is a diagnostic, not a prediction. Concretely:

- **Smolin's own falsifier is a pulsar above 2.5 M⊙**, stated in his abstract and conclusions. Our
  criterion used 2.00 and Brown–Lee–Rho use "≳2 to be safe". The heaviest well-measured star,
  2.08 ± 0.07, is **6σ below** Smolin's threshold. His prediction has not been lost — it has not
  fired.
- **He never proposes the 4% double-neutron-star test** — 0 hits for "4%", "asymmetry", "double
  neutron" in his text; that limb is Brown–Lee–Rho's, derived in Phys. Rept. 462 §3.2.
- What failed is **Brown–Bethe's** 1.5 M⊙ ceiling.

**What I changed.** `cockpit/mkbhu.py` only — the generator, not the HTML, since the page is rebuilt
from it. Backup `mkbhu.py.pre-cns-correction` (sha256 `95b21dbf…`). One `<p class=note>` inside the
"What this does not say" card. `ast.parse` clean, regenerated, serving 200.

The replacement carries its own limitation inline: **context-grade**, because it rests on an
unpublished preprint (INSPIRE confirms no publication record) while both published Smolin sources —
CQG 9, 173 (1992) and Physica A 340, 705 (2004) — remain unobtained. The Physica A DOI is verified via
Crossref but paywalled, and unlike the Phase 2 PLB case INSPIRE holds no document for it.

**Nothing else on the page changed.** The 19.3% figure and "nearly five times over" stand — Track B
tested that against the source's own He-red-giant proviso and it survives, because Tauris et al. 2017
budget total accretion at ~0.013 M⊙ against the proviso's claimed 0.1–0.2.

**Not a retraction.** The C08 verdict is untouched, the video is untouched, no gate is reversed. One
sentence of narrative was wrong about *what CNS forfeited*, and now says what the sources support.

— Tori, 2026-08-21 18:55 KST

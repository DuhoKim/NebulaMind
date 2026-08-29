# B14 — provisional adjudication of the three bare candidates

**PROVISIONAL. I wrote the entries being judged, so this goes to a seat.** `b14` (4/4) flagged 3 of
58 entries as naming an instrument in a results context while citing nothing below their own DOI
line. Reading each:

| # | verdict | why |
|---|---|---|
| 4 | **FALSE POSITIVE — not an entry** | A cross-reference stub in the audit-worthiness list ("Roupas 2022 — entry 21"), not a bibliography entry. It names LISA to describe a *frequency band*. Entry 21 itself, the real entry, does cite. |
| 39 | **FALSE POSITIVE — wrong Planck** | "ε_bounce = 15.4 ε_Pl — above Planck density" is the Planck **unit**, not the satellite. The probe matched the word next to "limit"/"concedes". This is precisely the failure mode b14's own prose predicted. |
| 54 | **REAL** | "Cites Planck PR3's 3σ preference for Ω_k ≈ −0.04 and same-direction ACT/DESI trends." Nothing pinned for Planck, ACT or DESI. Same shape as entry 51's CMS sentence. |

**Precision on this run: 1 of 3.** Worth stating plainly — that is the same order as the a11
classifier that was deleted for measuring 4/8. The difference, and the reason b14 is kept rather
than deleted: **b14 does not classify.** It prints candidates and says they are candidates, and
its self-checks test the probe's own behaviour on a known case rather than testing the corpus. A
screen with 1-in-3 precision over 58 entries is still cheaper than reading 58 entries by hand, so
long as nothing downstream treats its output as a finding.

**A NEGATIVE CONTROL THAT ACTUALLY WORKED.** Entry 51 drops off the bare list *because* two CMS
searches were pinned into it this evening. So the probe responds to citations being added, not to
keywords alone. That check is the reason to trust the 3 as a candidate set at all.

**Entry 54's defect, stated exactly.** The sentence reports what the *source paper* cites, which is
testimony about a pinned paper rather than a bare assertion — a weaker defect than entry 51's. But
the number is a strong claim about a real measurement, our record carries it with no citation, and
the well-known caveat is missing: a 3σ curvature preference from Planck depends on the likelihood
combination, and adding BAO restores flatness. Without that, the sentence reads as though Planck
found a closed universe. **Being pinned now.**

**What is NOT claimed here.** That the corpus has only one such defect. b14 tests entries that name
an instrument from a fixed list; a claim about experimental status phrased without any instrument
name — "current bounds allow", "no such object has been seen" — is invisible to it. That gap is
named, not measured.


---

## GATED — `CGATE_B14_VERDICT.md`, `ADJUDICATION_INCOMPLETE_MISSED_ENTRY44`

Both hand rulings on 4 and 39 confirmed. Two things I got wrong:

**1. A fourth candidate exists and my probe could not see it.** Entry 44 (Pourhasan, Afshordi &
Mann 2014) states its own base model is *"already ruled out at >5σ"* — an experimental-status
claim with a quantitative significance and **no instrument named anywhere**, so a fixed instrument
vocabulary cannot reach it. b14 has been widened with a `BARE_STATUS` pattern and now finds it.

**2. The parser was silently destroying five entries.** See harness defects §1x and §1y. The
`## Ranked` section's headings are numbered 1–5 and were overwriting bibliography entries 1–5;
the "no duplicate numbers" check was a tautology and could not catch it. **I adjudicated entry 4
as a false-positive stub and never asked why a stub was in slot 4** — the symptom was diagnosed
correctly and its cause buried. Repaired: the parse is bounded to the entry section and asserts on
the raw match list. Entries 1–5 have now been screened for the first time; none flags.

**Revised candidate set after the rebuild: 39 (false positive), 44 (real), 54 (real).** Precision
2 of 3, and entry 4 no longer appears at all because the Ranked section is excluded.

**Integrity Blockers**
- [supplementary_denominator_atlas.tex:168](...?) The simulation-vector prose says the retained target vector spans low-sSFR fractions `0.005-0.729` and includes color, but the displayed table at [line 173](...?) through [line 191](...?) shows only low-sSFR and broad-BPT fractions, and the visible values span `0.001-0.856`. That is a text/table mismatch that needs correction before the package is journal-ready.

**Journal-Quality Blockers**
- [rp1_flagship_polished.tex:54](...) / [rp1_flagship_polished.tex:65](...) The flagship matched-control table is provenance-backed, but the figure caption would be stronger if it carried the artifact IDs and the exact no-caliper design directly in the caption, not only in the body/table comments. Right now the figure is correct but not fully self-contained for a referee.
- [supplementary_denominator_atlas.tex:31](...) / [supplementary_denominator_atlas.tex:35](...) The provenance map is structurally good, but it is too compact for a referee pass. Add the custody `rows_approx` metadata, or a brief footnote with row-count scope, so the table itself exposes artifact scale without requiring the JSON manifest.
- [supplementary_denominator_atlas.tex:102](...) / [supplementary_denominator_atlas.tex:113](...) / [supplementary_denominator_atlas.tex:157](...) / [supplementary_denominator_atlas.tex:194](...) The interpretive literature is appropriate, but the section prose should carry explicit source identifiers next to the claims it is leaning on. Use:
  - Hardcastle & Croston 2020, [arXiv:2003.06137](https://arxiv.org/abs/2003.06137)
  - Piotrowska et al. 2022, [arXiv:2112.07672](https://arxiv.org/abs/2112.07672)
  - Tacconi et al. 2018, ApJ, 853, 179
  - Harrison et al. 2018, Nature Astronomy, 2, 198
  This is especially important in the maintenance-heating, outflow, gas-depletion, and simulation sections.

**Section-Level Fixes**
- Flagship: make the matched-control result figure/table standalone by surfacing artifact IDs and the matching design in the caption/table header.
- Supplement: either add the color statistic to the simulation-vector table or remove the color claim from the prose so the table and text match exactly.
- Supplement: expand the provenance map enough that a reader can see both artifact identity and scale at a glance.

JOURNAL_LEVEL_PASS: NO
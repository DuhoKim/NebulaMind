# fesc002 Citation-Gate Coverage Check

AI_DRAFT_NOT_HUMAN_GOLD

## Inline Citations vs Reference List Coverage

The following inline citation keys are used in the `draft.tex` body:
- `[Muñoz2024]`
- `[Davies2021]`
- `[Chisholm+22]`
- `[Flury+22]`
- `[Simmonds+24]`

The formal reference list (`\section*{References}`) contains:
- `[Muoz2024]`
- `[Davies2021]`
- `[Park2022]`
- `[Duncan2015]`
- `[Madau2017]`

### Cited-but-Unlisted Keys (Coverage Gap)
- `Chisholm+22`: **NO** reference list entry
- `Flury+22`: **NO** reference list entry
- `Simmonds+24`: **NO** reference list entry
*(Note: `Muñoz2024` maps to `Muoz2024` in the reference list, which is an encoding artifact rather than an unlisted key).*

## Citation Gate Coverage Fact
The citation gate recorded `citation_entailment.checked = 0`. This means the citation gate provided **zero positive entailment coverage**. A result of "0 unsupported" is NOT "verified supported." None of the citations in the draft were mechanically verified by the gate.

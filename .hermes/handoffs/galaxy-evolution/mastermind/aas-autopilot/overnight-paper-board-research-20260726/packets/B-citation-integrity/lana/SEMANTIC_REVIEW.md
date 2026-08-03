# Lana — Packet B: Semantic / No-Overclaim Review

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_B_LANA_BRIEF_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Lane: direct Claude Code subscription only (no API-key / PAYG / third-party route).
- Status of this artifact: `AI_DRAFT_NOT_HUMAN_GOLD`. This is a **semantic verdict only**, not the final decision — Goru's independent one-to-one mechanical cross-check and Hwao's adjudication follow.
- Decision rule applied per flagged citation:
  - **(a) gate defect (compound-sentence / key-assignment):** the citation IS supported by its own clause; the gate faulted it only for not covering the OTHER co-cited work in the same compound sentence -> **split / re-ground** (preserve, do NOT delete).
  - **(b) genuine unsupported / bare:** the citation has no specific support in the passage -> **remove**, or **re-attribute** to an in-list source the passage actually supports.

## Source stability (independently re-verified against `baseline/INPUT_SHA256.txt`)

| source file (relative to lab-runs root) | SHA-256 observed | matches INPUT_SHA256.txt |
|---|---|---|
| `gated-e2e-demo/draft.tex` | `f1aeadd8ea43f2fd1e22e9686d23066fdf95e3d5c95937a42d8ddd076bc95a8a` | OK |
| `gated-halt-demo/draft.tex` | `588c31a1bd67b87530988faf4c2ca5ad86af325e95806f6d2aefce3eb7e24995` | OK |
| `gated-e2e-demo.json` | `46ddd75d5f0e5814e814333336d8e6d1b011382c46509012af2aea8cc20af5e2` | OK |
| `gated-halt-demo.json` | `59c0076a5a93945625f019e2f33345a62b4651037cb0b0d8f38e3fa04acc0c45` | OK |

No source drift. No `expected_value` verdict of `CONTRADICTS` in scope (scoped gates are TENSION / INSUFFICIENT / TENSION per Kun's METHOD). I read only the source lab-runs, the baseline, and Kun's Packet B outputs; I introduced no source, no new citation, and no new claim.

---

## gated-e2e-demo

Introduction sentence 1 (source `draft.tex`, verbatim):
> For instance, [Qi2025] examined star formation rates, metallicities, and stellar masses on kpc-scales in TNG50, while [Torrey2019] investigated the evolution of the mass-metallicity relation in IllustrisTNG.

Introduction sentence 2 (verbatim):
> Additionally, [Garcia2023] analyzed gas-phase metallicity break radii of star-forming galaxies in IllustrisTNG, and [Guo2016] studied the stellar mass-gas-phase metallicity relation at redshifts between 0.5 and 0.7.

### 1. Torrey2019  — gate verdict: UNSUPPORTED
- **Lana verdict:** `gate-defect (compound-sentence / key-assignment artifact)`
- **Recommended action:** `split/re-ground` — PRESERVE, do NOT remove.
- **Grounding (verbatim):** its own clause "…[Torrey2019] investigated the evolution of the mass-metallicity relation in IllustrisTNG" matches its reference entry "[Torrey2019] … The evolution of the mass-metallicity relation and its scatter in IllustrisTNG" word-for-word on the cited content. The gate's own stored reason concedes support and mis-assigns the key: "THE PASSAGE ONLY MENTIONS TORREY'S WORK ON THE EVOLUTION OF THE MASS-METALLICITY RELATION IN ILLUSTRISTNG, BUT DOES NOT MENTION QI2025 OR THEIR EXA[MINATION]." It faults Torrey2019 solely for not entailing the co-cited **Qi2025** clause — the compound-sentence defect, not an unsupported citation.
- **No-overclaim / no-new-source:** the split reuses only existing passage wording; no new source, no new citation, no new claim, no caveat touched.

### 2. Qi2025  — gate verdict: SUPPORTED
- **Lana verdict:** genuinely supported — CONFIRMED.
- **Grounding:** "[Qi2025] examined star formation rates, metallicities, and stellar masses on kpc-scales in TNG50" matches its reference title "Star Formation Rates, Metallicities, and Stellar Masses on Kiloparsec Scales in TNG50" verbatim.
- **Action:** none (retain). In the split candidate Qi2025 stands on its own single-citation sentence.

### 3. Guo2016  — gate verdict: UNSUPPORTED
- **Lana verdict:** `gate-defect (compound-sentence / key-assignment artifact)`
- **Recommended action:** `split/re-ground` — PRESERVE, do NOT remove.
- **Grounding (verbatim):** its own clause "…[Guo2016] studied the stellar mass-gas-phase metallicity relation at redshifts between 0.5 and 0.7" matches its reference entry "[Guo2016] … Stellar Mass-Gas-phase Metallicity Relation at 0.5 <= z <= 0.7 …". The gate's stored reason again concedes support and mis-assigns the key: "THE PASSAGE ONLY MENTIONS GUO'S STUDY, BUT NOT GARCIA'S ANALYSIS OF GAS-PHASE METALLICITY BREAK RADII." It faults Guo2016 solely for not entailing the co-cited **Garcia2023** clause — same compound-sentence defect.
- **No-overclaim / no-new-source:** split reuses only existing wording; nothing added or weakened.

### 4. Garcia2023  — gate verdict: SUPPORTED
- **Lana verdict:** genuinely supported — CONFIRMED.
- **Grounding:** "[Garcia2023] analyzed gas-phase metallicity break radii of star-forming galaxies in IllustrisTNG" matches its reference title "Gas-phase metallicity break radii of star-forming galaxies in IllustrisTNG" verbatim.
- **Action:** none (retain). In the split candidate Garcia2023 stands on its own single-citation sentence.

**gated-e2e-demo summary:** both UNSUPPORTED flags (Torrey2019, Guo2016) are compound-sentence gate defects. Kun's removal discards two valid anchors whose content is present verbatim and matches their reference titles. Correct fix = **split the two two-citation sentences into four single-citation sentences** (candidate: `candidates-lana/gated-e2e-demo.split.md`). I **disagree** with Kun's removal for this run.

---

## gated-halt-demo

Introduction sentence (source `draft.tex`, verbatim):
> Previous works, such as [Renzini2015] and [Pearson2023], have contributed to our understanding of the MS by providing insights into its definition and characteristics.

### 5. Renzini2015  — gate verdict: SUPPORTED
- **Lana verdict:** supported — CONFIRMED, with a note.
- **Grounding:** the shared predicate's word "definition" matches Renzini2015's reference title "An Objective Definition for the Main Sequence of Star-forming Galaxies." Support is at the **generic, grouped** level — no per-author distinct clause exists (this is a grouped "such as A and B" citation, not a per-author content sentence).
- **Action:** none (retain).

### 6. Pearson2023  — gate verdict: UNSUPPORTED
- **Lana verdict:** `gate-defect (grouped / bare-citation artifact)` — this is a DIFFERENT case from the e2e compound-sentence pattern, and it is **NOT a confirmed genuine-unsupported**. It is the **one genuine judgment call** in Packet B.
- **Recommended action (primary):** `re-ground` = **retain the grouped citation (do NOT remove)**. **Acceptable conservative alternative:** `remove` (Kun's fix). **Flagged for Hwao adjudication.**
- **Grounding / why not a clean removal:**
  1. The gate's stored reason is **factually false** — it states "THE PASSAGE DOES NOT MENTION PREVIOUS WORKS OR AUTHORS LIKE RENZINI2015 AND PEARSON2023," yet the sentence it quotes explicitly cites both. The UNSUPPORTED verdict therefore rests on a demonstrably wrong reason.
  2. Renzini2015 and Pearson2023 occupy **identical grammatical positions** under one shared predicate ("such as [Renzini2015] and [Pearson2023], have contributed…"). The opposite verdicts (Renzini supported on author-name presence; Pearson unsupported) are an inconsistent key-assignment artifact — by the gate's own author-name logic, "Pearson" is equally present and cited.
  3. Pearson2023 is topically valid (its reference title "Influence of star-forming galaxy selection on the galaxy main sequence" is squarely about the MS) and already in the run's reference list. The illustrative "such as … have contributed to our understanding of the MS" claim is jointly supported (Renzini2015 -> "definition"; Pearson2023 -> "characteristics"/selection) and is **not an overclaim**.
- **Why removal is nonetheless defensible (the judgment call):** the citation is **bare** — the passage attributes no specific per-author finding to Pearson2023, so there is no distinct clause to preserve by splitting (unlike e2e). The keyword "definition" is a tighter literal match to Renzini2015 than to Pearson2023 (selection). Kun's removal (keep Renzini2015 only) introduces no overclaim and loses no *specific* stated result.
- **No-overclaim / no-new-source:** retaining introduces nothing; removing deletes only a bare citation. Either path adds no source, no claim, and touches no caveat. Because this is a genuine judgment call, I do not produce a rewrite that would presuppose one outcome; I state the recommendation and hand the decision surface to Hwao.

**gated-halt-demo summary:** the Pearson2023 UNSUPPORTED flag is not the e2e compound-sentence pattern and is not a confirmed bare-irrelevant citation; it is a grouped-citation gate artifact resting on a false gate reason. I **lean retain (re-ground)** and do **not fully concur** with Kun's removal, but I record removal as an acceptable conservative fix and flag this as the sole item requiring Hwao's judgment.

---

## fesc002 (read for completeness)

`gates.citation_entailment` = `{checked: 0, all: [], unsupported: []}`. No citation was checked by the gate, so there is nothing to adjudicate and no checked-and-supported claim exists. Reference-list entries (Muñoz2024, Davies2021, Park2022, Duncan2015, Madau2017) are recorded here as **not gate-checked**, not as supported. No action; I concur with Kun that fesc002 yields no citation fixes.

---

## Cross-run no-overclaim attestation
- No new source or citation beyond each run's existing `lit_reflist` / `lit_refs` was introduced.
- No new scientific claim, number, or result was added.
- No caveat was weakened or deleted (Caveats sections are untouched by every recommendation).
- No source `draft.tex`, no Kun/Goru/v1 file, and no run JSON was edited; only new isolated files under my write root were produced.

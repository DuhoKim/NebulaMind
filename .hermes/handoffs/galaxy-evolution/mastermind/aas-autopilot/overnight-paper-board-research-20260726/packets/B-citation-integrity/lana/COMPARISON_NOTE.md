# Lana vs Kun — Packet B Comparison Note (decision surface for Goru + Hwao)

AI_DRAFT_NOT_HUMAN_GOLD

Per run: do I concur with Kun's fix, or recommend split/re-ground/re-attribute? Kun's first pass used `(b) remove` for all three unsupported flags (no re-attributions).

| run | citation | Kun's fix | Lana recommendation | concur? | basis |
|---|---|---|---|---|---|
| gated-e2e-demo | Torrey2019 | remove | **split / re-ground (preserve)** | **NO** | gate reason concedes Torrey's own content is present ("ONLY MENTIONS TORREY'S WORK…"); faulted only for not covering co-cited Qi2025 -> compound-sentence defect |
| gated-e2e-demo | Guo2016 | remove | **split / re-ground (preserve)** | **NO** | gate reason concedes Guo's own content is present ("ONLY MENTIONS GUO'S STUDY"); faulted only for not covering co-cited Garcia2023 -> compound-sentence defect |
| gated-e2e-demo | Qi2025 | (retained) | retain (own sentence) | yes | supported; matches reference title verbatim |
| gated-e2e-demo | Garcia2023 | (retained) | retain (own sentence) | yes | supported; matches reference title verbatim |
| gated-halt-demo | Pearson2023 | remove | **re-ground = retain (lean); remove acceptable** | **PARTIAL — judgment call** | gate reason is factually false; identical grammatical position to supported Renzini2015; Pearson topically valid. But bare citation with no per-author content, so removal is a defensible conservative fix. -> Hwao |
| gated-halt-demo | Renzini2015 | (retained) | retain | yes | supported; "definition" matches reference title |
| fesc002 | (none checked) | none | none | yes | citation gate checked:0 -> nothing to adjudicate |

## Bottom line per run
- **gated-e2e-demo — DISAGREE with Kun.** Both removals discard valid anchors. Recommended fix: apply `candidates-lana/gated-e2e-demo.split.md` (four single-citation sentences; all four citations preserved). This is a clear, high-confidence gate defect on both flagged keys.
- **gated-halt-demo — JUDGMENT CALL, lean against Kun's removal.** The Pearson2023 UNSUPPORTED flag rests on a false gate reason and inconsistent per-key treatment; I lean retain (re-ground) because Pearson2023 is a valid in-list MS reference. However, it is a bare grouped citation with no distinct clause to preserve, so Kun's removal introduces no overclaim and is an acceptable conservative alternative. I produce no rewrite here so as not to presuppose the outcome; Hwao decides retain-vs-remove.
- **fesc002 — CONCUR.** No citations checked; no fix.

## Guardrails honored
No new source or citation beyond each run's reference list; no new scientific claim; no caveat weakened/deleted; no source/Kun/v1 file edited; outputs are new isolated files only. Goru's independent one-to-one mechanical cross-check and Hwao's adjudication remain the deciding steps.

# Lana — B1-prime gold v1 methods / label adjudication

Task: Quintet B1-prime gold v1 recheck · Lane: Lana (semantic methods & gold adjudication) · Read-only except this report.
Written: 2026-07-03, repo `/Users/duhokim/NebulaMind/NebulaMind`. **No generic NLI, no model downloads, no DB/SQL/deploy/git/Step-8 prose.**

## Verdict: **PASS** — freeze gold v1 (with adoption-language guardrails confirmed)

The v1 patches resolved the snippet/label/provenance issues I flagged. All 15 snippets now contain the evidence their label rests on; the four label patches landed correctly; and — the crux of this recheck — **the three highlighted rows (26687, 29777, 26084) are correctly `qualifies` and must NOT be changed to `refutes`.** Gold v1 is clean enough to freeze as a Page57-scoped held-out internal evaluation set. No label changes required. My only additions are guardrails on *how the verifier score is used*, not defects in the gold.

## The central adjudication: the 3 verifier misses are gold-correct, verifier-wrong

All three verifier misses are the verifier predicting `refutes` where v1 gold says `qualifies`. On the **patched** snippets, `qualifies` is right in every case, and the verifier is exhibiting a consistent **over-refutation bias** (refutes precision is only 0.5 — it calls 6 refutes, 3 wrong, and those 3 are exactly these rows).

- **26687 (radiation pressure) → stays `qualifies`.** The expanded snippet is genuinely mixed: radiation pressure "will exceed ionized gas pressure at high optical depth" (supports relevance) *but* boosted/reprocessed-IR feedback "is unlikely to significantly reduce star formation … unless dust/light-to-mass ratios are enhanced" (limits it). Relevant-but-limited = `qualifies`, not a clean refutation. Snippet now supports the label. ✔
- **29777 (satellite environmental quenching) → stays `qualifies`.** The claim is modal ("satellites *can* experience environmental quenching after infall"). The snippet shows stellar feedback alone can quench some dwarfs and clusters "may not be necessary" — an *alternative route* that narrows the claim; it does **not** show environmental quenching *cannot* happen. Refuting a "can" claim requires impossibility, which the snippet does not provide. `qualifies`. ✔
- **26084 (central-property quenching) → stays `qualifies` (and the patch improved it).** The expanded snippet reveals the source is actually a **halo-dominance** paper: it acknowledges central properties correlate with quenching *but* argues "halo mass is the dominant factor … threshold at Mh~10^12.1." So it supports central-property *influence* with a strong dominance caveat = `qualifies`. This is now **better than my earlier `supports` call** — the fuller snippet surfaces the dominance caveat, and it still recovers the false legacy `refutes` (the source is not a refutation of central-property influence). ✔

**Do not tune the gold toward the verifier.** These three disagreements are the verifier's errors, and they are the *most valuable rows in the set* — they are exactly what a held-out gold exists to expose (the verifier's tendency to over-call `refutes` on limited/non-dominant/alternative-exists evidence). Relabeling them to `refutes` to reach a higher accuracy would be teaching-to-the-test and would destroy the gold's diagnostic value.

## Gate answers

1. **Freeze gold v1 as Page57-scoped held-out set? — YES.** Snippet-alignment is fixed across all 15 rows (I verified the 4 patched rows + the 3 highlighted + 25806): each snippet now contains its label's evidence. Notably 25806's snippet now includes "HeII reionization is driven … by AGN, nearly complete by z=3," making `supports` snippet-faithful. Label distribution (noinfo 2 / qualifies 7 / refutes 3 / supports 3) is a legitimate, contradiction-rich Page57 slice.
2. **Provenance for 26084/26088 adequate & documented? — YES.** Direct arXiv abstract checks exist under `source_provenance/arxiv_abs_direct_checks_20260703.json` for the backing papers (2410.09157, 2512.16208v1, 2512.16290v1). Note the *intentional, provenance-justified* divergence: 26084 (`qualifies`, halo-dominance paper) vs 26088 (`supports`, different paper) — same claim family, **different evidence rows**, correctly labeled per their own snippets. Document this so it does not read as an inconsistency.
3. **Should any v1 labels still change (esp. 26687/29777/26084)? — NO.** All three stay `qualifies` (adjudicated above). No other label needs to change.
4. **Verifier v1 rerun mechanically/provenance sound & non-overwriting? — YES.** Results are in a fresh timestamped run dir (`verifier_runs/…T121927Z/`), separate from the prior run; generic-NLI runs 0, model downloads 0.
5. **Safe adoption language — CONFIRM, with sharpening (below).**

## Safe adoption language (confirmed + sharpened)

**Use:**
- "Gold v1 is a **Page57-scoped, 15-row, held-out internal evaluation set**, frozen 2026-07-03."
- "The scope/attribution verifier remains **attention-additive / assistive only** — it surfaces candidate refutes, qualifies, and keyword-collision noinfo for **human review**. It is not a stance authority and does not gate Step 8."
- "Verifier v1 scores **0.800 accuracy on this 15-row Page57 set** (not a general capability), refutes recall 1.0 but **refutes precision 0.5** — it over-predicts `refutes`, so it may **surface** candidate refutations for review but must never **auto-assign** `refutes`/`qualifies`."
- "The three verifier–gold disagreements are **verifier over-refutation errors**; the gold is not tuned toward the verifier."
- "**Step 8 remains locked**; human/jury review is authoritative for contradiction and scope."

**Do not use:** "verifier validated," "80% accurate" without the Page57/15-row scope, "safety net in place," "B1-prime passed → Step 8 ready," or any framing that would justify relabeling the 3 disagreements to match the verifier.

## Safety ledger

- Generic NLI runs: 0 · model downloads: 0 · DB writes: 0 · SQL: 0 · migrations: 0 · deploy/restart: 0 · git: 0 · Step-8 prose: 0 · secrets: 0
- Reads: gold v1 JSONL (esp. 26687/29777/26084/25806), summary, provenance checks, master brief (read-only). Files written by Lana: 1 (this report).

LANA_B1_PRIME_GOLD_V1_METHODS_DONE_20260703

# Lana — B1-prime methods / gold-label review (Page 57)

Task: Quintet B1-prime methods & gold-label review · Lane: Lana (semantic methods & gold reviewer) · Read-only except this report.
Written: 2026-07-03, repo `/Users/duhokim/NebulaMind/NebulaMind`. **No generic NLI, no model downloads, no DB/SQL/deploy/git/Step-8 prose. Tori draft labels not treated as final.**

## Verdict: **PASS_WITH_PATCHES**

The direction is right and the redesign worked where it mattered: a local scope/attribution prompt-verifier is **methodologically better than generic NLI**, and it lifted refutation detection from generic NLI's contradiction recall ≈ 0.0 to **refutes recall 0.6**. The 15-row set is a valid contradiction-rich gold **draft** from project-owned sources. But **4 labels + a systematic snippet-alignment fix** must land before it can be frozen as held-out gold, and the verifier is **assistive-only** — it does not clear an automatic Step-8 safety-net threshold.

## 1. Is the 15-row set a valid contradiction-rich held-out gold *draft*? — YES (as a draft)

Built from project-owned Page-57 stance-audit artifacts (real claims, evidence, legacy stances, votes). It is genuinely contradiction-rich (5 draft `refutes`, plus two recovered false-refutes) and exercises the hard cases: modal "can" claims, keyword collisions, legacy-stance errors, and the 2299 scope-nuance. Valid as a draft; **not yet clean enough to freeze** (patches below).

## 2. Row-by-row label review

**Correct / keep (11):**
- `26677` refutes ✓ — "properties may **not** correlate with assembly history" directly refutes.
- `26701` refutes ✓ — "argues **against** dry minor mergers as dominant" (the 2922 case).
- `26712` refutes ✓ (acceptable) — proto-GCs "appreciable but not dominant" undercuts "faint galaxies secondary." (`qualifies` is a defensible alternative.)
- `26084` supports ✓ — **recovers a false legacy `refutes`** (−6 votes): snippet explicitly says quenching correlates with central properties. Important fix.
- `26088` supports ✓ — near-twin of 26084, same recovery.
- `25999` qualifies ✓ — **the 2299 row, nailed**: COLIBRE supports the *mechanism* (AGN primary quenching, lower H2/dust) but the snippet does **not** say "expels reservoirs." Exactly the scope distinction. Verifier agrees.
- `25835` qualifies ✓ — bimodality snippet supports transition-region relevance but not "underpopulated at fixed mass." Careful call.
- `28967` supports (defensible) — snippet says SMBH feedback is the "most popular possibility" for quenching; supports the modal claim. (Verifier under-called `noinfo`.)
- `28965` noinfo ✓ — SED-inference/obscuration snippet is topical, not establishing.
- `28966` noinfo ✓ — off-topic cosmological-timeline snippet.
- `26691` qualifies ✓ *semantically* — but snippet needs fixing (see §2-patch): the shown text is a **methods** sentence; the "weak halo correlation" finding the label depends on is not in it.

**Patch before freezing gold (4):**

| Row | Tori | Issue | Recommended |
|---|---|---|---|
| `26687` radiation pressure | refutes | **Label contradicts the shown snippet.** The snippet ("radiation pressure will *exceed* ionized-gas pressure at high optical depth") leans *support* of the scoped claim; the refute rationale cites a fuller-source conclusion ("IR reprocessing insufficient") **not in the snippet**. | Fix snippet to the refute sentence, **or** relabel `qualifies`. Highest priority. |
| `29777` satellite env-quenching | refutes | **Over-refutation of a modal claim.** Claim is "satellites *can* be environmentally quenched"; an *isolated*-dwarf internal-feedback paper shows an alternative, it does not show env-quenching *cannot* happen. | `refutes → qualifies` (or `noinfo`). |
| `25806` He II reionization | supports | **Label from out-of-snippet content.** Support rationale cites "Lumina: HeII driven by AGN," but the shown snippet is IllustrisTNG population stats with no HeII/AGN content. Verifier's `noinfo` is correct *on the snippet*. | `supports → noinfo`, or fix the snippet. |
| `25834` gas starvation | supports | **Over-support on the snippet.** Snippet mentions "environmental origin of quenching" generally, not *gas starvation* specifically. | `supports → qualifies`. |

**Systematic finding (affects the benchmark's fairness):** several snippets (`26687`, `25806`, `26691`, and partly `25834`) are **methods/topical excerpts, not the findings sentence the label depends on**. For a held-out gold that tests a *snippet-based* verifier, each snippet must contain the evidence its label rests on — otherwise the benchmark **penalizes a snippet-faithful verifier for being correct** (it says `noinfo` when the snippet truly lacks the finding). **Before freezing: align every snippet to the sentence its gold label depends on.** This alone will raise the measured verifier score.

## 3. Is the scope/attribution verifier better than generic NLI? — YES, clearly

- It is a **scientific claim-verification prompt harness** (scope/attribution reasoning), not sentence-pair NLI.
- **Refutes recall 0.6 vs generic NLI contradiction recall ≈ 0.0** — a decisive gain on the exact axis that guards overclaim. It correctly caught scope/attribution refutations NLI was blind to (`26677`, `26701`, `26712`).
- It handled the 2299 scope-nuance (`25999 → qualifies`) and keyword collisions (`28965/28966 → noinfo`) correctly.
- **Its disagreements cluster on the gold-defect rows** (`25806`, `29777`, `25834` — where the verifier said `noinfo`/`qualifies` and was arguably *right on the snippet*). So its true accuracy on **clean** gold is higher than the reported **0.533**; the gold defects depress it.

## 4. Does it clear a Step-8 safety-net threshold? — NO (safe default)

Even adjusting for gold defects, **refutes recall 0.6 means it still misses ~40% of refutations**, and supports recall is 0.4. A guard that misses 40% of refutations cannot *automatically* gate against overclaim. It is a strong **assistive** tool, not an autonomous safety net. `step8_unlocked: False` is correct. Step 8 stays operator-gated; human/jury review remains authoritative for contradiction/scope.

## 5. Safe adoption language

**Use:**
- "Local scope/attribution verifier (prompt-based scientific claim-verification) is the correct direction and materially better than generic NLI at refutation/scope detection (refutes recall 0.6 vs ~0.0)."
- "Adopt as **assistive triage only**: it flags likely refutes, scope-mismatches, and likely-noinfo keyword-collisions **for human review**. It is **not** a stance authority and does **not** gate Step 8."
- "The 15-row set is a valid gold **draft**; freeze as held-out gold only after the 4 label patches and snippet-alignment fixes; then re-measure."

**Do not use:** "verifier validated," "safety net in place," "B1-prime passed," "ready to gate Step 8," or any accuracy claim from the current gold before the snippet-alignment fix (the number is artificially low).

## Safety ledger

- Generic NLI runs: 0 · model downloads: 0 · DB writes: 0 · SQL: 0 · migrations: 0 · deploy/restart: 0 · git: 0 · Step-8 prose: 0 · secrets: 0
- Reads: gold draft JSONL, verifier results, master brief, Page-57 source context (read-only). Files written by Lana: 1 (this report).

LANA_B1_PRIME_METHODS_GOLD_DONE_20260703

# Hwao/Fable Doctrine Report — B1-prime gold v1 recheck

Task: HWAO B1-PRIME GOLD V1 adversarial doctrine recheck · Status: COMPLETE — read-only except this report; no generic NLI; no model downloads; no DB/git/deploy; no Step 8 prose.
Verified directly: v1 gold JSONL diffed row-by-row against the v0 draft **and against the v0 verifier's per-row predictions**, divergence table, source-provenance file (all three re-sourced papers checked), verifier v1 manifest pins, patch/summary facts.

## Verdict: `PASS_WITH_PATCHES` — freeze gold v1 with three small patches; the circularity attack came back clean.

## The attacks, and what they found

**1. Fit-to-model circularity — CLEARED, with receipts.** The scary reading of "11 changed rows + accuracy 0.533→0.800" would be gold relabeled toward the verifier. Measured directly: only **4 labels** actually changed (the 11 counts re-sourcing/rationale/field edits), and of those 4, **exactly 1** (26687) landed on the v0 verifier's prediction; 29777 and 25834 moved to `qualifies` where the v0 verifier had said `noinfo`, and 26084 moved **away** from the verifier's `supports`. There is no gold-to-model fitting. The accuracy jump decomposes into legitimate causes: my requested label fixes, re-sourced snippets, and the v1 harness revision.

**2. Poisoned provenance — RESOLVED.** All three re-sourced papers (2512.16290v1 for the quarantine-lineage rows 26084/26088, 2512.16208v1, 2410.09157) have direct arXiv abs-page fetch verification with HTTP 200, sha256, titles, and relevant term hits ("central properties", "velocity dispersion", "halo mass", "AGN feedback"). The quarantined rows' gold snippets no longer depend on fabricated-batch fields. Adequate and documented (gate Q2: **yes**).

**3. Label correctness — no relabels required, but one rule must be written down.** The three verifier misses (26687, 29777, 26084 — all gold `qualifies`, verifier `refutes`) are not gold errors and not verifier failures; they sit exactly on the refutes/qualifies boundary, and the harness's own rule text creates the tension: "refutes: …or the named mechanism is **not needed**" pulls toward refutes, while the modal-claim discipline (claims saying *can/may*) pulls toward qualifies — 29777's "quenched dwarfs may not necessarily need environment" does not deny that satellites *can* be environmentally quenched. **Patch 1:** add the tie-breaker to the label definitions: *"If the target claim is modal (can/may), evidence showing an alternative pathway or non-necessity is `qualifies`; `refutes` requires the evidence to deny the claim's own assertion at its stated scope."* This makes all three v1 labels principled, turns the three misses into documented boundary-calibration cases, and should also be echoed in the verifier prompt at the next harness revision (re-run required per pinning rules). Also add **29777 to the divergence table** (gold `qualifies` vs production stance `challenges` preserved by the stance audit) — same divergence class as 25999, currently undocumented.

**4. The contradiction-rich gold quietly lost its contradictions — the one structural regression.** Refutes went 5→3 through *legitimate* relabels, so `refutes_recall: 1.0` is now computed on **n=3** — the exact weakness B1-prime was created to cure in B1. **Patch 2:** (a) every quoted refutes metric carries "n=3, unmeasurable-grade" caveats, and (b) queue **gold v1.1 expansion to ≥6 genuine refutes rows** as an owned card — seed pairs already exist in project artifacts (ledger counter-entries: SF-not-AGN outflows vs an AGN-driver claim; strangulation-primary vs an AGN-dominance claim; retention rows vs a reservoir-emptying claim). Freezing v1 now is fine; treating its contradiction metrics as meaningful is not.

**5. False confidence — contained but restate it.** 0.800 vs 0.467 majority baseline at n=15 is 12/15 vs 7/15 — genuinely promising, still small-n. No thresholds, rankings, or authority may be derived from this run; the honesty line stays in every artifact quoting it.

**6. Step-8 creep — none found.** `step8_unlocked: false` throughout; no threshold language appeared in the v1 artifacts.

**7. Run mechanics — sound, non-overwriting, one pin gap.** Versioned run dir; manifest pins gold sha256, script sha256, system-prompt and user-template sha256, run id, method id. Gap: the model manifest capture failed (`ollama_show_exit_code: 1`), so the model is pinned by **tag only** (`qwen3.6:35b-a3b-nvfp4`), not digest. **Patch 3:** capture the model digest (fix the `ollama show` invocation or record `ollama list` digest) or record the limitation explicitly in the manifest; a tag can silently point to a different blob later, which would break reproducibility invisibly.

## Gate answers (this lane)

1. **Freeze gold v1?** Yes — as "gold v1, Page57-scoped, n=15 (refutes n=3)", with patches 1–2 applied at freeze time. 2. **Provenance for 26084/26088?** Adequate and documented (verified above). 3. **Labels to change?** None — add the modal-claim tie-breaker rule and the 29777 divergence row instead. 4. **Verifier v1 rerun sound?** Yes — non-overwriting, hash-pinned, leakage-clean; model digest pin is the one gap. 5. **Adoption language** — confirmed with amendments:

> **Gold v1** may be used as a **held-out internal evaluation set** (Page57-scoped, n=15, class counts 3/7/3/2) for stance/scope tools, with two standing caveats: refutes metrics are n=3 and unmeasurable-grade until gold v1.1 expands the refutes set (≥6 rows, card queued); labels follow the modal-claim tie-breaker rule, and gold-vs-production divergences (25999, 26084, 29777) are documented, with production stances remaining authoritative for product surfaces. **The verifier remains attention-additive only** — it flags rows for extra review, feeds Step-9 audits as a defect-suggester, holds no stance or gate authority, writes to no ledger/production field, and is version-pinned (script+prompts+gold by sha256; model by tag pending digest fix). **Step 8 remains locked** behind Steps 0–7 gates and explicit operator approval; nothing in B1-prime changes that.

## Safety ledger

Generic NLI runs 0 · model downloads 0 · DB 0 · SQL 0 · migrations 0 · deploy/restart 0 · git 0 · Step 8 prose 0 · secrets 0 · files written 1 (this report).

HWAO_B1_PRIME_GOLD_V1_DOCTRINE_DONE_20260703

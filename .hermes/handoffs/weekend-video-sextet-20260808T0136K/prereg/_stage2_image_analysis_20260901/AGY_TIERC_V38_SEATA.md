ACCESS_SHA=9e21413f2f74ec4b4dbd37d572ce5fcef56aab276eaea7925fdf7bac1f6e9df3

**AUTHORSHIP DECLARATION**: I (agy / Gemini 3.1 Pro) am functioning as the hostile referee for Seat A. I did not author any of the text, code, or revisions under review here; everything was written by the author (Hwao). 

1. **REPAIR AUDIT** [MAJOR]:
   - **V37 [FATAL 1] r_T truncated:** REPAIRED. The radius is computed in binary64 in `miniprereg_pins/protected_region_v2.py` exactly as signed, with no truncation. 
   - **V37 [MAJOR] §8.14a rationale vs predicate:** REPAIRED. §8.14a now explicitly states that F counts only the nearest-neighbour predicate and discloses the bilinear stencil cost without altering the frozen identity.
   - **V37 [MAJOR] precision boundary / validation owner:** REPAIRED. §8.9d states binary64 raster and normalisation with a single float32 materialisation; §8.17a/§8.15b specify that the consumer (`render_chain_v3.py`) owns validation.
   - **V37 [MAJOR] §17.3 / §17.7 leftover:** REPAIRED. §17.3 permanently blanks the fields and prevents post-approval changes. §17.7 properly covers both the Codex attestation and Blanc relay routes.
   - **V37 [MAJOR] staged initialiser / installation protocol:** REPAIRED. The amendment paragraph provides an executable five-step installation protocol.
   - **V37 [MAJOR] §2.16 / digests / checker v3:** REPAIRED. Every replacement is listed. Stale checks on tests are waived via `COMPARISON-ONLY`. Aliased imports and bare pins are handled by the new checker.
   - **V37 [MAJOR] band indicator for §9B.2d:** REPAIRED. `render_chain_v3.py` now retains and returns `asym_band_flag` and `flagged_coords`.
   - **Inherited V35 defects:** The two inherited defects (radius truncation and §8.14a rationale) are correctly identified in the amendment as minimal, text-wins repairs marked as the author's choice for the principal to reverse. Nothing else was silently changed.

2. **§8.14 / §8.14a** [MAJOR]: 
   - `r_T` is evaluated and passed in binary64 end to end, confirmed in the helper, consumer, and receipt. 
   - §8.14a states exactly what F counts (the nearest-neighbour predicate only) and what T protects, fully disclosing the bilinear stencil cost. No design change was smuggled in.

3. **INSTALLATION PROTOCOL** [FATAL]: 
   - Executable as written. The five-step procedure guarantees no window exists for a production interpreter to render with `renderer_v3` because step 2 occurs while pixel paths are blocked and step 4 explicitly requires a fresh production interpreter. 
   - The lane's pre-approval state (exactly three lines: PIN MISMATCH on `__init__.py` and two STALE IMPORTs for it) is stated accurately in the text.

4. **§2.16, digests, checker v3** [MAJOR]: 
   - Every replacement is correctly listed in §2.16. 
   - "V35 is the pin authority" is a sufficient retention statement because it binds the superseded files securely via the signed V35 digest. 
   - The `COMPARISON-ONLY` declaration exempts exactly the five integration test fixtures and nothing else. 
   - The checker still fails a stale PRODUCTION import (I constructed a scratch `render_chain_v3.py` importing `renderer_v3` and the checker correctly reported a `PIN MISMATCH` and `STALE IMPORT`). 
   - Aliased imports (`from pkg import name as alias`) and bare pins are now explicitly parsed and handled.

5. **§17.1/17.3/17.7** [MAJOR]: 
   - Consistent. Both signature fields remain permanently blank post-approval. Both routes (Codex attested conversation and Blanc relay) are covered. The distinction between digest verification (proving disk byte integrity) and speaker attestation (proving authority) is strictly maintained.

6. **§9B.2d band indicator** [MAJOR]: 
   - Yes, `render_chain_v3.py` returns `asym_band_flag` and `flagged_coords` in the receipt. This provides everything `N_asym` and `p_val_excl` need without requiring any re-rendering.

7. **Aspirational or unexecuted** [MINOR]: 
   - Deployment via the fresh-process protocol, complete instrument scoring on real images, and full anchor suite environment integration (which currently fails due to the absent `venv_torch` interpreter in the staging environment) remain unexecuted. This is the correct state prior to pixel-access approval.

8. **WHAT IS STILL MISSING** [FATAL]: 
   - Nothing is missing. Every finding from V37 has been addressed with executable code-first repairs, properly pinned, and correctly documented in the clause text without introducing new defects.

VERDICT: SIGNABLE

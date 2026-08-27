# BRIEF — agy seat: redo the flatness measurement on the right quantity

Tori, 2026-08-27. **Self-contained.** Everything you need is below or at the absolute paths
given. Do not assume knowledge of this lane; do not read outside the paths listed.

**Working directory (all relative paths resolve here):**
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-theory-phase5-tovoptics-20260825/`

**Write ONLY inside that directory.** Intermediates go in `platoon/_tmp_agy_*`. Never write to
`/tmp`, `$TMPDIR`, or anywhere outside the lane.

**Environment:** python 3.9.6, numpy 1.26.4, scipy 1.13.1. Run scripts with `python3` from the
working directory above (several scripts read sibling files by relative path and will fail
elsewhere).

---

## The one-paragraph background you actually need

We model light crossing a boundary in a cosmology where the observable universe sits inside a
shock wave. `emergent_K(eta_e, w, K)` in `p8_thick_limit.py` returns an emergent temperature
ratio; `K` multiplies the opacity; `w` is the equation-of-state parameter of the material beyond
the boundary. A previous receipt, `FLATNESS_GAP_CLOSED.md`, claimed that opacity changes only
the *amplitude* of the sky pattern and not its *shape*.

## What went wrong, and what you are fixing

That claim was measured with the wrong quantity. It compared the percent change of a ratio `R`
that sits very close to 1 — `R = 0.997726210` at `K=0.01` and `R = 0.998857603` at `K=100`, a
change of only 0.1134%. But the anisotropy lives in the **residual `1-R`**, which falls from
`0.002273790` to `0.001142397` over the same range — a **49.76%** change. A percent change of a
near-unity ratio suppresses exactly the quantity being diagnosed.

A gate re-measured it by direct projection and got a signed normalized coefficient moving from
`-0.522912` to `+0.043763` over four decades of `K` — a change of `0.566675` **including a sign
reversal**. So the shape is not flat at the anisotropy scale, and the claim is withdrawn.

**Your job is not to re-litigate that.** It is withdrawn. Your job is to produce the correct
replacement measurement, cleanly, as a runnable script plus a short receipt.

## The task

1. Write `p10_flatness_redo.py` in the working directory.
2. Measure the shape-versus-opacity question using the **signed normalized dipole coefficient**
   (and/or `1-R`) — never the percent drift of `R` near one.
3. Sweep `K` across at least six decades, e.g. `1e-2, 1e-1, 1, 1e1, 1e2, 1e3`, at the
   junction-value closure `w = 0.2456`, off-centre fraction `x/R = 1e-3`.
4. Reuse the existing machinery rather than reimplementing physics: `p8_thick_limit.py` defines
   `emergent_K` and `signed_c1_K` and shows how to exec `p6_path_transfer.py`'s prefix to get
   `exterior`, `r_star`, `sqrtN`, `RSTAR_CROSS`. Read `p8_thick_limit.py` first — it is your
   template for imports and structure.
5. **Reproduce the four anchor numbers above** (`0.997726210`, `0.998857603`, `-0.522912`,
   `+0.043763`) as explicit self-checks, so the new script is tied to the record. If you cannot
   reproduce one, say so in the receipt and print what you got — **do not tune anything to
   match**.
6. Follow this lane's check idiom exactly as `p8_thick_limit.py` does it: a `chk(name, predicate,
   detail)` that refuses a non-computed predicate, a printed `N/M checks passed` line, and
   `sys.exit(1)` on any failure. **Every number the receipt states must be printed by the
   script.** Self-describing prose is what keeps failing our gates; self-computing checks do not.

## A resolution trap that already bit us — do not repeat it

The emergent integral weights by `exp(-tau)`. Once the `tau~1` layer is thinner than one grid
cell, the result is grid noise, not physics. On the current 4000-point grid the largest
resolved opacity multiplier is **K ≈ 2935 at w = 0.2456** but only **K ≈ 18.4 at w = 0.02** —
and it must be evaluated wherever your sweep actually evaluates, not at a convenient mid-band
point. Compute this limit in your script (max per-cell `d(tau) <= 1`) and **decline to report
any K beyond it**, printing UNRESOLVED instead. See the repair notes in `P8_THICK_LIMIT_RECEIPT.md`.

## Deliverables

- `p10_flatness_redo.py` — runs clean from the working directory, prints its checks.
- `P10_FLATNESS_REDO_RECEIPT.md` — what you measured, the table, which anchors reproduced,
  which did not, and the resolution limit you enforced. Short. No completeness prose.
- Print the exact command you ran and its exit code in the receipt.

## Boundaries

- Do **not** edit any existing `.py` or `.md` file in the lane. New files only.
- Do **not** claim the flatness gap is closed or re-opened. You are producing a measurement,
  not a verdict. The verdict is mine.
- If something is ambiguous, write down the assumption you made in the receipt and continue.
  Do not stop to ask.

## Standing warning, and it is the point of this brief

**A seat draft is a draft, not a result.** I will verify your numbers before anything you write
is cited. Our worst failure this week was a check that agreed with itself: a null was missed
because the test was built so it could not see it. Build yours so it *can* fail, and tell me
plainly where it did.

## Reference paths (read-only)

- `p8_thick_limit.py` — your template; `emergent_K`, `signed_c1_K`, the exec-prefix pattern
- `p6_path_transfer.py` — `exterior()`, the transfer integral
- `P8_THICK_LIMIT_RECEIPT.md` — the resolution-limit repair, worked through
- `FLATNESS_GAP_CLOSED.md` — the withdrawn claim you are replacing
- `REGATE4_PHASE5B_VERDICT.md` §5 — the gate's own re-measurement and the four anchor numbers

ACQ_NARROWED_entry20_identity_and_owned_subresults

# Adversarial verdict

The four acquisitions are readable and all four remain **NOT `THEORETICAL-OBSTRUCTION` at paper level**, but B38 is not confirmable as written. Its title-only identity check misses a real entry-20 metadata error, and its summaries of entries 17 and 20 understate source-owned, claim-level exclusions. Those findings require corrections even though none changes the four primary tiers.

I read all four pinned texts in full:

- entry 15: `hep-th_0103019_clean.txt` (441 lines);
- entry 17: `1909.07129_clean.txt` (459 lines);
- entry 20: `gr-qc_0611022_clean.txt` (754 lines);
- entry 28: `2411.14673_clean.txt` (619 lines).

## Attack 1 — entry 20

### The paper owns more restrictive reasoning than B38 records

The sentence “a regular centre can only be located in an R region” is part of the paper's own geometric classification. Given its definitions, a regular centre has `A -> A_c > 0`, hence lies in an R region; a black hole with such a centre must therefore cross an even number of horizon boundaries—at least two simple horizons or one double horizon. This is elementary causal-structure reasoning printed in this paper, not merely an imported quotation.

The stronger horizon-count result for minimally coupled scalar fields is developed from the field equations in the paper. Equations (7)–(8) give

`B' = 2(rho_0-rho)/r^4`, with `B=A/r^2`.

The paper then reasons that `B` rises, has one maximum, and falls, so it has at most two simple zeros or one double zero. It consequently rules out a regular-centred black hole for this scalar system, since that would require a regular minimum of `B`. The same equation is obtained again for k-essence in equations (27)–(30). The authors call this the “Global Structure Theorem” and cite their ref. [26], so the theorem's historical/canonical ownership is [26], but this paper does reproduce the operative derivation rather than merely name the result.

It also derives narrower exclusions in section 4.2: the perfect-fluid representation (24) cannot furnish the desired black universe because fractional powers cease to make sense when `X` changes sign at the horizon, while (26) is incompatible with asymptotic flatness because it is nonzero at `X=0`.

These are genuine source-owned claim-level constraints. They do **not** make the paper's primary tier an obstruction: the abstract, stated program, bulk of sections 3–4, explicit solution (11)–(16), and conclusion all organize the paper around classifying and constructing regular black universes and specifying existence conditions. The exclusions delimit that construction rather than constitute its operative paper-level contribution. Entry 20 therefore remains `CONSISTENCY-ONLY`, but its record should preserve these restrictions.

### Ref. [16]

The electric nonlinear-electrodynamics no-go is explicitly attributed to ref. [16], not proved here:

> K. A. Bronnikov, Phys. Rev. D 63, 044005 (2001), arXiv:gr-qc/0006014.

That work is **not a numbered entry in the current bibliography** and no pinned full text for it is present in the source pool. It is an acquisition lead. The repository's harvested metadata identifies its title as *Regular magnetic black holes and monopoles from nonlinear electrodynamics*. B38 correctly does not transfer its proof tier to entry 20.

### Identity failure

The pinned file is the correct title and arXiv work, `gr-qc/0611022`, but the bibliography and B38 docstring give the wrong authors. The paper's own title page names **K. A. Bronnikov, V. N. Melnikov, and H. Dehnen**, not “K. A. Bronnikov and J. C. Fabris.” Fabris is Bronnikov's coauthor on ref. [1], *Regular phantom black holes*, which is a different paper. The title-only predicate cannot detect this. Entry 20's author field must be corrected; the source itself need not be discarded.

## Attack 2 — entry 17

The boundary stress tensor is **derived as necessary within the paper's stipulated model**, not simply assumed.

The authors do assume the two ingredients being joined: a semiclassically corrected homogeneous interior whose effective Misner–Sharp mass varies with time, and an exactly classical Schwarzschild exterior with constant mass. But after making those assumptions they calculate the first and second fundamental forms. Equations (22)–(23) satisfy metric continuity; equations (25)–(26) give unequal extrinsic curvatures. The text expressly concludes that continuity of the second fundamental form “can not be satisfied,” and Israel's condition (24) then requires a delta-like surface tensor. Figure 2 checks the accounting relation `M_Sigma + r_b^3 M_eff/2 = M_Sch` throughout the evolution.

The same shape recurs in the proposed continuations: unequal-mass Schwarzschild regions in case (a) require a nonzero layer, and the Schwarzschild–de Sitter match in case (b) is nonsmooth away from `R_0=2M` because the de Sitter extrinsic curvature vanishes at the bounce while the Schwarzschild value does not. Case (c) instead assumes an interpolating semiclassical geometry and derives its boundary conditions.

Thus entry 17 contains an entry-5-shaped **claim-level exclusion of smooth matching for its fixed ansatz**. The important difference is paper-level logical role: entry 17's operative contribution is the construction of a bouncing interior and three continuation options; the junction obstruction motivates the added shell/interpolating region. It is not a paper whose organizing result is the failure of an attempted smooth identification. Retain `CONSISTENCY-ONLY`, but revise “its hit concerns a boundary tensor required by the matching” to say that the requirement is calculated and conditional on the stipulated interior/exterior ansatz.

## Attack 3 — entries 15 and 28

### Entry 15

This is correctly `CONSISTENCY-ONLY`. Easson and Brandenberger derive Schwarzschild geodesic estimates and a flat-slicing/topology argument in service of proposed solutions to horizon, flatness, information-loss, and structure-formation problems. There is an owned negative result more substantive than B38's “coordinate-role remark”: their near-horizon and deep-interior estimates lead them to say that interactions occurring **solely inside the horizon cannot solve the horizon problem**. That is a conditional limitation inside a constructive paper, not its operative contribution or a class-wide BHU no-go. The conclusion is explicitly constructive and leaves a higher-derivative realization for future work.

### Entry 28

This is correctly `CONSISTENCY-ONLY`. Sahu and Van Raamsdonk construct the Euclidean/CFT and Lorentzian black-hole-lattice cosmologies, explicitly build the three-dimensional saddles, and compare their actions. The dominant-saddle result is conditional: for an infinite square lattice the cosmological saddle dominates only above approximately `r_crit = 1.12 l_AdS` (with separation of order the AdS scale); smaller-black-hole cosmologies remain subdominant contributions rather than nonexistent solutions. This is an internal phase/dominance boundary within a microscopic construction, not the paper-level exclusion of a desired model class.

## Attack 4 — identities

- **15:** title page gives Damien A. Easson and Robert H. Brandenberger, *Universe Generation from Black Hole Interiors*, `hep-th/0103019`; matches entry 15.
- **17:** title page gives Hrishikesh Chakrabarty, Ahmadjon Abdujabbarov, Daniele Malafarina, and Cosimo Bambi, *A toy model for a baby universe inside a black hole*, `1909.07129`; matches entry 17's abbreviated author record.
- **20:** title and arXiv identifier match, but authors do not; correct to Bronnikov–Melnikov–Dehnen as above.
- **28:** title page gives Abhisek Sahu and Mark Van Raamsdonk, *Holographic black hole cosmologies*, `2411.14673`; this is compatible with the entry's “A. Sahu et al.” abbreviation.

## Attack 5 — predicate audit

I reran B38's B1 regexes directly on the current pinned files and independently recovered its reported `(impossibility, domain, escape)` counts:

| entry | counts | B1 flag |
|---|---:|---:|
| 15 | `0 / 1 / 0` | no |
| 17 | `3 / 6 / 0` | no |
| 20 | `3 / 1 / 0` | no |
| 28 | `0 / 2 / 1` | no |

So the numerical screen result is reproducible. The submitted harness nevertheless does not establish all of its prose:

1. Its identity predicate checks normalized titles only, so it passes entry 20 despite the author mismatch.
2. Its entry-20 predicate proves only that two phrases occur; it does not establish who owns the proof or inspect ref. [16].
3. Its entry-28 check is a phrase-presence check, not an adjudication.
4. The final screen predicate is effectively `True is (phrase in E28)`; the four reported regex counts are hardcoded in prose and never computed by this script.

The script's `4/4` therefore means four narrow string predicates passed, not that acquisition identity, proof ownership, or the census adjudication was verified.

## Disposition

- Keep entries **15, 17, 20, and 28** in their existing non-obstruction tiers.
- Correct entry 20's authors to **K. A. Bronnikov, V. N. Melnikov, and H. Dehnen**.
- Add claim-level notes for entry 17's derived junction-layer necessity and entry 20's reproduced global-structure/regular-centre restrictions (and, optionally, entry 15's inside-horizon limitation).
- Add Bronnikov 2001, `gr-qc/0006014`, to the acquisition-lead queue.
- Subject to that metadata correction, the acquisition arithmetic may remain `readable 38`, `not located 13`; no primary tier moves follow from this gate.

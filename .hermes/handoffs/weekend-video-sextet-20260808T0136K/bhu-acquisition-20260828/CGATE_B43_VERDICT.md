ENTRY38_NARROWED_THEOREM8_STATEMENT_AND_SCOPE

# B43 adversarial verdict — entry 38 full read

I read `math-ph_0302036_clean.txt` **in full and sequentially**, all 3,262 content lines from title through all eight sections, theorem and lemma proofs, 15 footnotes, concluding remarks, and 24 references. Entry 38 remains `CONSISTENCY-ONLY` at paper level. Its operative contribution is constructive: it derives the dynamical TOV-inside-the-black-hole system, develops the matching/conservation machinery, proves existence and uniqueness of an entropy-satisfying constant-`sigma` shock family, and estimates that family's speed and position.

The proposed claim item 3 is mathematically correct in substance, but it needs two qualifications. The result is scoped to the paper's exact constant-equation-of-state family (`p=sigma rho`, `0<sigma<1`), and Theorem 8's displayed opening hypothesis contains an internal typo: it begins “Let `0<sigma<=1/3`” and then immediately states the `sigma>1/3` limb. The surrounding section, Theorem 7, equation (6.30), and Theorem 8's own proof make the intended three-way result unambiguous; the bibliography should record the trichotomy without implying that Theorem 8's statement is textually clean.

## 1. Theorems 1–9 under the fixed obstruction rule

### Sections 2–5

- **Theorem 1** bounds the universe's age and infinite-redshift radius under `0<=p<=rho/3`. It is a quantitative bound, not a no-member conclusion.
- **Theorem 2 and Corollary 1** give the explicit expanding `k=0`, constant-`sigma` FRW solution and show that comoving enclosed mass decreases for `sigma>0`. Constructive.
- **Section 3** constructs the `k=0` Oppenheimer–Snyder matching through the Schwarzschild horizon using Eddington–Finkelstein coordinates. Constructive.
- **Section 4** derives equations (4.16)–(4.18) for a comoving perfect fluid when `A<0`, where the radial coordinate is timelike. This is the TOV-inside-the-black-hole analogue and is explicitly a new dynamical metric class.
- **Theorem 3** proves equivalence between the Rankine–Hugoniot conditions and the single conservation constraint (5.25) for a noncharacteristic Lipschitz FRW/TOV match. Machinery enabling the construction.
- **Theorem 4** changes variables to `(u,N)` and derives the shock speed. Machinery.

These sections contain restrictions—noncharacteristic matching, positivity, `N>1`, and the distinction between standard static TOV and the new dynamical system—but none is the paper's operative endpoint. They define and enable the constructed solution class.

### Sections 6–7

- **Theorem 5** reduces the physical entropy/density/pressure bounds to inequality (6.11).
- **Theorem 6** is the load-bearing constructive result: for every `0<sigma<1`, there exists a unique orbit `u_sigma(S)` satisfying the entropy inequalities on `0<S<1`, with the stated endpoint behavior.
- **Theorem 7** proves that the constructed shock is strictly subluminous for every post-Big-Bang point `0<S<=1` **iff `sigma<=1/3`**.
- **Theorem 8 and its surrounding derivation** give the Big-Bang limit of the shock speed: infinity for `sigma>1/3`, zero for `sigma<1/3`, and one for `sigma=1/3`.
- **Theorem 9 and Corollary 2** bound shock position, visibility, and horizon-exit time. Constructive estimates.

Theorem 7 is logically a real no-member statement:

> Within the paper's exact entropy-satisfying constant-`sigma` family, no member with `sigma>1/3` has an everywhere-subluminous shock.

A counterexample within that domain would refute it. But the theorem partitions the family whose existence Theorem 6 has just proved; it is not the paper's organizing exclusion. The abstract opens “We construct,” Sections 3–6 build the solution, Theorem 6 proves it globally, Section 7 estimates it, and the conclusion again foregrounds the exact shock solutions. Under the settled entry-37/B30 operative-contribution convention, negating Theorem 7 does not convert the paper into a paper-level obstruction. It is precisely the same family-delimiting shape as entry 37's shorter version of the result.

**Ruling on attack 1:** no theorem in Sections 2–7 warrants moving entry 38 to `THEORETICAL-OBSTRUCTION`. Theorem 7 is strong claim-level obstruction content and must remain recorded.

## 2. Full inventory of impossibility-adjacent content

The B43 inventory captures the main theorem structure but misses or compresses several negative statements. None changes the tier.

### Previously adjudicated claims

1. **Standard TOV continuation.** The introduction and Section 4 say a standard static-fluid TOV solution cannot continue into `A<0`, citing entry 57. B32 correctly found that entry 57 does not prove this. Entry 38 itself derives the narrow causal-role result: a comoving fluid in `A<0` obeys a different, dynamical system because the radial coordinate becomes timelike. This excludes continuation *as the same standard static/comoving construction*, not all TOV-form matter metrics inside a horizon.
2. **Infinite FRW/Schwarzschild match.** Section 3 says the infinite `k=0` FRW metric cannot be matched to Schwarzschild in the model. In context this is the finite-enclosed-mass junction limitation already narrowed at B32, not a universal prohibition on every FRW/Schwarzschild construction.

### Footnote 10 and the characteristic branch

Footnote 10 is a genuine source-owned branch exclusion that should be included in a complete inventory. For `A<0`, one solution of the scalar normal-normal condition (5.2) is everywhere characteristic for the coordinate PDE (5.9). On that surface the full Rankine–Hugoniot relation (5.1) fails, so the branch is **not an actual weak solution of `G=kappa T`**. This is why the authors abandon the shortcut used for `A>0` and derive the full conservation condition directly.

That result meets a narrow counterexample-shaped test for the rejected branch, but its logical role is repair/enabling machinery: it motivates the direct derivation that produces the physical shock family. It is not a paper-level no-go. An optional claim-level note would be accurate; omitting it from the bibliography is less serious than omitting Theorem 7 because it is methodological and the replacement is supplied immediately.

### Other restrictions and negative statements

- Lemma 1 supplies a sufficient noncharacteristic domain (`p>bar p`, positive variables, `A<0`).
- Theorem 5/6 restrict the physically admissible orbit through entropy and equation-of-state inequalities and show uniqueness.
- For `sigma>1/3`, Theorem 7/8 excludes everywhere-subluminous behavior and gives an infinite Big-Bang speed.
- The conclusion says the TOV-side equation of state cannot be independently imposed in these exact solutions; it is generated by the matching equations and only bounded by `0<bar p<bar rho`. This is an admitted model limitation, not a no-solution theorem.
- The statement that more general equations of state would need transitional waves that would be “pretty much impossible to model in an exact solution” is an epistemic/modeling judgment, not a proof of nonexistence.
- The final “an impossibility if one only allows” sentence is a rhetorical consequence of forbidding the time-reversed white-hole orientation, not a new class theorem.
- The conclusion's reference to the entropy condition ruling out expansion shocks in classical gas dynamics is imported background, while this paper uses its chosen orientation to construct the relativistic explosion.

I found no hidden theorem, proposition, footnote, or conclusion whose operative result is a class-wide exclusion rather than a bound, rejected branch, or limitation internal to the construction.

**Ruling on attack 2:** B43 missed footnote 10 as a separately inventory-worthy claim-level rejected branch, but not a paper-level obstruction. The tier verdict survives.

## 3. Fidelity of claim item 3

The current repair says:

> Theorem 7 proves the constructed shock is everywhere subluminous iff `sigma<=1/3`, and Theorem 8 proves the Big-Bang trichotomy—infinity above `1/3`, zero below it, and light speed at equality.

The directions are correct, with these precise scopes:

- the family assumes `p=sigma rho` with constant `0<sigma<1`;
- `sigma` is the equation-of-state parameter and the squared FRW sound speed in units `c=1`;
- Theorem 7's strict inequality `|s_sigma(S)|<1` is for `0<S<=1`, i.e. after the limiting Big-Bang instant;
- for `sigma=1/3`, the post-Big-Bang shock is strictly subluminal but its `S->0` limit is exactly one;
- for `sigma<1/3`, that limit is zero;
- for `sigma>1/3`, equation (6.30), Theorem 7's proof, Section 6.3's introduction, and equation (6.45) give the infinite limit.

There is a textual defect that should be disclosed. Theorem 8 is printed as:

> Let `0<sigma<=1/3` ... Then if `sigma>1/3`, ...

The first hypothesis is incompatible with its first branch. The intended domain is plainly the Theorem-6 family `0<sigma<1`, with the three cases divided at `1/3`; the paper had already proved the above-`1/3` limb in Theorem 7, and Theorem 8's proof calls (6.45) evident from (6.48). This is best treated as a theorem-statement typo, not a substantive ambiguity.

A more faithful record is:

> **Claim-level parameter exclusion:** In the paper's unique entropy-satisfying shock family with constant `p=sigma rho`, `0<sigma<1`, the shock is strictly subluminous for every `0<S<=1` iff `sigma<=1/3` (Theorem 7). The surrounding Section 6.3/Theorems 7–8 establish the Big-Bang speed limit: `infinity` for `sigma>1/3`, `0` for `sigma<1/3`, and `1` for `sigma=1/3`; Theorem 8's printed opening hypothesis `0<sigma<=1/3` is inconsistent with its immediately following above-`1/3` limb and is evidently a statement typo. The result delimits the constructed family and does not change the paper-level tier.

**Ruling on attack 3:** directions confirmed; implementation narrowed for family/domain precision and the Theorem-8 statement defect.

## 4. Predicate audit

I reran `b43_entry38_fullread.py`; it reports `7/7`, 3,263 counted lines (the file has a trailing-newline count convention), and the expected hash prefix `47c47ac44788`.

### What is genuinely computed

- `nl` and the SHA-256 prefix are computed from the current bytes.
- The bibliography block parser genuinely scopes entry 38 and verifies that its first bold `Testability:` token is `CONSISTENCY-ONLY`.

### What detects phrases or landmarks

1. **SOURCE:** title, `[24]`, `Weinberg`, and `nl>3000` are completeness landmarks. They show the current extraction reaches the reference tail and has plausible length; they do not prove that every section, footnote, equation, or page was preserved against the version of record.
2. **READ RECEIPT:** file prefix plus one abstract phrase plus “there exists a unique solution” prove only that those strings occur. Code cannot certify that a human read 3,262 lines sequentially, understood them, inventoried all theorems, or applied the fixed rule. Calling this a `READ RECEIPT` is not honest without an external signed/manual declaration. It is at most a source-and-operative-phrase smoke test.
3. **CLAIM 1:** confirms two phrases occur somewhere, not their context, citation identity, proof ownership, or B32 adjudication.
4. **CLAIM 2:** confirms the infinite-FRW sentence exists, not its finite-mass scope.
5. **CLAIM 3:** searches the generic word `subluminous`, a `sigma<=1/3` TeX string, and only the equality-limit formula. It does not locate Theorems 7/8, verify the iff, check the infinity and zero limbs, detect Theorem 8's contradictory opening domain, or connect the three strings.
6. **REPAIRED STATE:** checks two phrases anywhere in the full bibliography, not specifically inside entry 38's block. They could be supplied by another entry or note. Scope this predicate to `blocks[38]`.

### Missing predicates

The script has no checks for:

- theorem/lemma inventory completeness;
- footnote 10 or its characteristic/non-weak-solution result;
- the exact constant-`sigma` family domain;
- the difference between post-Big-Bang strict subluminality and the limiting speed at `S=0`;
- the `sigma>1/3` and `sigma<1/3` formulas;
- Theorem 8's inconsistent hypothesis;
- paper-level operative-contribution reasoning;
- source comparison to the journal/PDF; or
- actual human reading behavior.

The script is a useful immutable-file/landmark and implementation smoke test. Its `7/7` does not prove the adjudication or the read.

**Ruling on attack 4:** only byte counts/hash and the scoped tier parse compute narrow claims; most checks are phrase-presence tests, and the `READ RECEIPT` label overclaims.

## 5. Census receipt status

Yes. With this independent full sequential read and the B43 gate record, entry 38 now has the missing fixed-rule full-read receipt identified by `CGATE_B41_VERDICT.md`. On the paper identities and batch sets previously audited there, all **39 readable BHU papers are now fully receipted as reads**.

That statement concerns reading coverage, not unanimous verdict correctness, obstruction-content recall, or the correctness of B41's automation. As the brief requires, the B41 set arithmetic and its repaired bindings should still be rerun and separately gated. But entry 38 is no longer the coverage hole.

**Ruling on attack 5:** census reading coverage is now 39/39; separate coverage-proof re-gating remains owed.

## Disposition

- Retain entry 38 as `CONSISTENCY-ONLY`.
- Retain Theorem 7/8 as claim-level exclusion content.
- Narrow claim item 3 to the exact constant-`sigma`, `0<sigma<1` family and disclose Theorem 8's printed hypothesis typo.
- Optionally add footnote 10's rejected characteristic branch as a methodological claim-level limitation.
- Rename the script's `READ RECEIPT` check; phrase presence cannot certify a human full read.
- Treat the readable census as fully receipted at 39/39 after this gate, subject to the separately promised B41 arithmetic/binding rerun.

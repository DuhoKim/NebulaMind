Q4_IMPL_REFUTED_SCOPE_AND_HEADLINE

I have reviewed the implementation of Question 4 in the bibliography and open-questions files.

**1. Tier-definition reading: CONFIRMED**
Tori's reading is textually accurate. The brief defines the tier explicitly as `"CALIBRATED-FALSIFIER (number + threshold)"`. This describes the *shape* of the claim, not its soundness. Relying on this to separate the claim's shape (Tier) from its soundness (Warrant) is a faithful application of the record's own definitions.

**2. The 4-rows-not-58 claim: REFUTED**
Tori argues a warrant column only costs 4 rows because "a warrant only exists where there is a calibrated claim to have a warrant for." This is false. A `QUALITATIVE-DIRECTIONAL` claim (e.g., changing parameter X decreases black holes) or a `THEORETICAL-OBSTRUCTION` (a mathematical proof forbidding a class of models) fundamentally relies on theoretical derivations. Those derivations are their warrants, and they can absolutely be disputed (e.g., by pointing out a math error). Thus, the warrant column's true scope extends to every predictive or prohibitive paper in the collection. Tori's original cost objection was right the first time.

**3. Warrant cells against evidence (Entry 7): LOCAL ONLY**
The four cells accurately reflect the findings in the local repository. However, Entry 7's "not disputed here" is an absence claim over the pinned corpus. 
*   **Pattern it would need:** A search over the broader literature for citations to Brown & Bethe 2008, or keyword searches like `(kaon condensation) AND (unlikely OR ruled out OR incorrect OR dispute)`.
*   **Class it would miss:** Papers that confirm a mutually exclusive core composition (e.g., certain quark-gluon plasma equations of state) which implicitly rule out kaon condensates without explicitly citing or arguing against Entry 7.

**4. Headline claim fairness: REFUTED (OVERCLAIM)**
Tori's headline—"only one of this collection's four sharpest claims has reasoning nobody has challenged"—is a striking sentence that wildly outruns its evidence. Entry 7's cell merely notes that no challenge is pinned *in this local directory*. Escalating "we haven't downloaded a paper disputing it" to "nobody has challenged it" misrepresents a local absence of evidence as a global proof of soundness.

**5. Breakage: CONFIRMED NONE**
The implementation was executed cleanly. The markdown table renders correctly, the counts (4 calibrated out of 51) are internally consistent, and the distinction between the 2 LIVE and 2 FIRED claims correctly propagates into the summary text. No existing text contradicts the new axis.

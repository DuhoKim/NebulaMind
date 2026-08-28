HARNESS_GAPS_FOUND_5

1. `a5_entry26_prediction.py`: "Lambda_O = 4/(3 tau_O^2) follows exactly from Lambda = 3/r_S^2 and r_S = 3 tau_O/2"
   - **Gap**: The predicate evaluates a mathematical identity inside Python (`abs(3.0/(1.5*tau_sym)**2 - 4.0/(3.0*tau_sym**2)) < 1e-12` using a hardcoded `tau_sym = 7.0`). It never touches the source text `T`. It asserts nothing about the paper itself and would falsely pass on an entirely different paper or a blank file.

2. `a4_stitch_mdpi.py`: "the seams did not duplicate text"
   - **Gap**: The predicate only tests that a single phrase (`"Publisher’s Note: MDPI stays neutral"`) appears exactly once. A bad overlap splice duplicating paragraphs of actual physics content in the middle of the text would still allow this check to falsely pass, as it only verifies the envelope's footer.

3. `a12_entry8_indistinguishable.py`: "COUNTED: the paper contains no scientific-notation value and no numeric magnitude threshold anywhere in its text"
   - **Gap**: The regex strictly requires `\times 10` or `× 10`. It blindly misses standard formatting like `10^9`, `1e9`, or `\sim 10^{15}`. This is an absence claim wearing arithmetic, and its narrow pattern would falsely count zero on papers containing valid magnitude thresholds.

4. `a9_entry52_threshold.py`: "the paper analyses all three curvature cases and commits to none for our Universe"
   - **Gap**: The predicate confirms only the *presence* of two sentences defining the conditions for closed/flat/open universes (`cond and unres`). Finding conditional statements does not logically prove the *absence* of a definitive commitment elsewhere in the text.

5. `a10_entry23_cutoff.py`: "the CMB large-angle correlation anomaly predates the paper, so this is a POSTDICTION"
   - **Gap**: The predicate tests only for the presence of the word "observed" (`"anomalous lack of correlations observed in the CMB" in T`). The name asserts chronological and epistemological facts ("predates", "POSTDICTION") that a simple string presence test cannot logically reach.

FALSE_PASS_POSSIBLE: YES
CLASSIFIER_SOUND: NO (The classifier misses control-flow data bindings—such as `ok_all = False` inside an `if` branch, leading to a false TAUTOLOGY label in `a1`. Furthermore, it misclassifies based on AST string heuristics: it labels `a5`'s generator comprehension as STRING just because of the `for k in res` keyword, and labels `a9`'s pure substring boolean as COMPUTED because the `in` operation was done on a prior line.)

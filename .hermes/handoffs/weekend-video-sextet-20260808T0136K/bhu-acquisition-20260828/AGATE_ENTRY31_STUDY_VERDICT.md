STUDY_UNSOUND_DESCRIPTIVE_PREMISE_AND_INCOMMENSURABLE_INTERVALS
SIGMAS_CONFIRMED: YES
INFERENCE_HOLDS: NO
THIRD_READING: ANY_HIGH_PRECISION_MEASUREMENT

### 1. Attack 1: Sigmas Confirmed
The arithmetic for the sigmas is correct based on the values in the pinned papers.
- **J0740+6620 (radio timing):** 2.08 +/- 0.07. Distance to 2.5 M_sun is 0.42, which is `0.42 / 0.07 = 6.0` sigma.
- **J0952-0607 (black widow):** The pinned paper (Romani 2022) reports `2.35 +/- 0.17`, not the `+/- 0.11` from the record. Distance to 2.5 is 0.15, which is `0.15 / 0.17 = 0.88` sigma. 
The sigmas computed in the scripts are confirmed, but the record was indeed carrying an unpinned and narrower error bar (+/- 0.11) that materially overstated how close the falsifier was to firing.

### 2. Attack 2: Inference is Unsound (Load-Bearing Defect)
Smolin's exact text is: *"Presently all well measured neutron star masses are from binary pulsar data and are all below 1.5 M_sun."*
The word **"Presently"** explicitly marks this as a description of the state of observational astronomy in 2004, not a permanent prescriptive criterion for what constitutes a "well measured" mass. The inference that this clause permanently disqualifies other methods (like optical modeling or gravitational waves) is false. The entire two-branch framing rests on this misreading and collapses without it.

### 3. Attack 3: Drift Computation and Narrow Absence Test
- **Radio Timing:** The "drift" from Cromartie 2020 (2.14) to Fonseca 2021 (2.08) is not two independent measurements showing a trend. Fonseca 2021 explicitly states it *combines* 1.5 years of additional data with previous measurements to improve upon the estimate. It's a refinement of a single evolving dataset, not independent points on a trend line.
- **Black Widow:** There is no prior mass measurement because Nieder 2019 (the discovery paper) explicitly stated the counterpart was too faint for spectroscopic radial velocity measurements. However, the script's check for this (`hist_hits == 0` in `b5`) relies entirely on a narrow regex search for literal phrases like `"prior measurement"` or `"previous mass"`. This is a narrow absence test that proves nothing about the literature, even if its conclusion happens to be correct.

### 4. Attack 4: The GW Leg and Incommensurable Intervals
The study claims the GW190814 secondary interval (2.50 - 2.67, 90% credible) lies *entirely* at or above the bar, while the "same analysis paper's" M_TOV (2.210 +0.116 -0.123, 2 sigma) excludes it.
- **False Attribution:** These are not from the same analysis paper. GW190814's mass is from the Abbott 2020 discovery paper (2006.12611), while the M_TOV estimate is from the Nathanail 2021 tension paper (2101.01735). 
- **Incommensurable Intervals:** The study compares a 90% credible interval (GW190814) against a 2-sigma (~95.4%) interval (M_TOV). If the GW190814 90% interval is [2.50, 2.67], expanding it to a 2-sigma interval would widen it such that the lower bound extends *below* 2.50. Thus, at 2-sigma, it does not lie entirely at or above the bar.

### 5. Attack 5: A Third Reading of "Well Measured"
A third reading of "well measured" is simply **"high precision"**, regardless of the instrument used. Since Smolin's comment was merely noting that in 2004 only binary pulsar timing provided high-precision measurements, any future technique (such as optical modeling, X-ray thermal emission modeling via NICER, or gravitational waves) that achieves sufficient precision would qualify as "well measured" under the original intent.

### 6. Attack 6: Audit of Names vs. Predicates
Several checks in the scripts claim far more than their predicates actually test, and one check is false on its own input while printing PASS:
- **b4, Check 2 (The False PASS):** The check name claims to quote `"if one is completely confident of Bethe and Brown's upper limit..."`. The predicate only tests if `"1.5 solar masses"` and `"troubling"` occur within a 190-character window. It prints PASS, but the exact string in the input contains a typo (`"conEdent"` instead of `"confident"`). Because the predicate only checks for two disjoint substrings, it passes while the quoted claim is false on its own input.
- **b4, Check 4:** Name claims `"both masses read from their own pinned papers"`. The predicate (`bool(m1) and bool(m2)`) merely checks if the substrings `"2.08"` and `"0.07"` (or `"2.35"` and `"0.17"`) appear anywhere in the text, it does not parse them or guarantee they refer to the mass.
- **b5, Check 2:** Name claims `"there is one measurement and no history to trend"`. The predicate only checks that the specific regex `(?:previous|earlier|prior)\s+(?:mass|measurement|estimate)` yields zero matches. 
- **b6, Check 1:** Name claims `"the discovery paper's ENTIRE 90% credible interval... lies AT OR ABOVE"`. The predicate only tests if the exact string `"2.50 - 2.67"` or `"2.50-2.67"` exists anywhere in the text.
- **b6, Check 2:** Name claims `"the literature states the conditional explicitly... IF and ONLY IF"`. The predicate simply checks if the disconnected words `"requiring"` and `"if the secondary was a"` appear anywhere in the paper.

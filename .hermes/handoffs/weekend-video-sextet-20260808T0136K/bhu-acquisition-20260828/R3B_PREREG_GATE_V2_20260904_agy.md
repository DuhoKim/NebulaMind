ACCESS_SHA=6e1e22070b143694ea3921b8220ae3f65ed13316183acf8ecf9e53f5b7f9b69a
GATE=PREREG_SOUND_WITH_REPAIRS

Explicit Checks (1-8):
1. LINE TRACING: Verified. L28 equates the boundary to a Lambda term (\Lambda = 3/r_S^2). L134-138 and L143-144 explicitly state the mass inside \chi is a function of time, and L138-140 introduces the time-dependent junction \chi^* to keep M_T constant. The cited lines contain exactly what is claimed.
2. THE DRAFT REPAIR: Verified. C2 now correctly requires the seat to "print the exact search terms used and quote the resulting text."
3. THE RIGIDITY PREMISE: It is actually established by the cited lines, not assumed by the lane. L25 and L28 explicitly tie the \Lambda term to the gravitational radius (r_S = 2GM). Furthermore, L314-317 explicitly confirm this mapping by stating that if r_S increases (e.g., via accretion), the effective \Lambda_e decreases with time, resulting in \omega_{DE} > -1. Thus, the premise that a constant r_S forces w = -1 is physically established by the text. By explicitly leaving this as a question for Limb A rather than a stated fact, the design is not circular.
4. OUTCOME CLASSES: Exhaustive and mutually exclusive. The precedence rule for Class 4 strictly prevents a shared falsifier (w = -1, which is identical to the \Lambda CDM prediction) from being reported as a discriminating success, correctly overriding Classes 2 and 3.
5. CONTROLS: C5 is mechanical, requiring command execution and hash verification. C5b is merely an assertion and lacks a mechanical verification step (addressed in Repairs).
6. THE DATA BOUNDARY: The stop condition is tight ("If limb B cannot be answered from published constraints alone..."), and the fallback is clearly stated ("the seat stops and says so").
7. CIRCULARITY: Verified. The data enter only at Limb B, strictly after the rigidity question is settled in Limb A.
8. RE-RUN: Verified. The document explicitly states it does not re-run K4 or Program A.

Repairs:
1.
- Quoted sentence: `derivation has been run and no data has been touched.**`
- Defect: A typo during drafting dropped the word "No" from the end of the previous line when the header was rewritten, inadvertently stating that the derivation *has* been run, which violates the pre-registration freeze.
- EXACT replacement: `No derivation has been run and no data has been touched.**`
2.
- Quoted sentence: `Exact assertion: \`C5b_NO_CROSS_LANE_ACCESS=PASS\`, printed by every seat.`
- Defect: The control is not mechanical; a seat could silently open another lane's files and still print the pass string.
- EXACT replacement: `The seat must explicitly list every local file path it opened during the study. If any path falls outside the current lane, the control fails. Exact assertion: \`C5b_NO_CROSS_LANE_ACCESS=PASS\`, printed by every seat.`

9. HONESTY: Declaring the expected outcome in advance is excellent practice. It binds the humans and prevents the post-hoc spinning of a shared, non-discriminating feature as a novel discovery. Because objective controls govern the execution, the seats are not pre-committed; they follow the rules independently.
10. GUARANTEED VERDICT: Yes, the design reaches a guaranteed verdict and cannot stall. The symbolic operations are protected by a hard 120-second wall-clock cap with a stated fallback to explicit algebraic arguments (Stall Guard, §11), ensuring completion.

R3B_PREREG_GATE_COMPLETE

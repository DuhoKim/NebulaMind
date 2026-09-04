ACCESS_SHA=2b36b505f2535e98baabae7372f3f89c852f991f6817b47a0395c3d7365fb01a
GATE=PREREG_SOUND_WITH_REPAIRS

1.
Quoted sentence: `The seat must decide, from the source and the structure of the model rather than from taste, whether the amplitude is:`
Defect: Limb A's exit condition rests on a judgement the seat makes, which is not operationalised. A warning not to conflate concepts is a mere admonition that an LLM can easily finesse. It needs a sharp test requiring a mechanical derivation.
Exact replacement wording: `To pass limb A, the seat must write down the exact mathematical derivation fixing the amplitude strictly from the model's pinned parameters without introducing new free variables; if it cannot, it must conclude the amplitude is:`

2.
Quoted sentence: `2. **K5_DETECTABLE_NOT_DISTINGUISHABLE** — loud enough, but degenerate with an ordinary black-hole ringdown once mass and spin are marginalised — the "mode camouflage" the paper itself names (**L401**).`
Defect: Outcome classes 1 and 2 are not mutually exclusive. If the model is distinguishable in some regions but degenerate in others, both class 1 ("a nonempty region satisfies both") and class 2 ("loud enough, but degenerate") could technically trigger.
Exact replacement wording: `2. **K5_DETECTABLE_NOT_DISTINGUISHABLE** — a nonempty region clears the detection threshold, but NO region is distinguishable from an ordinary black-hole ringdown once mass and spin are marginalised — the "mode camouflage" the paper itself names (**L401**).`

3.
Quoted sentence: `Whatever amplitude is used, the seat must print where it came from and whether it is derived from the construction or supplied from outside it. Exact assertion: \`C5_AMPLITUDE_PROVENANCE=PASS\`.`
Defect: C5 is a promise to print documentation, not a real operational check. A seat can hallucinate a provenance string and still assert PASS without mechanically breaking the execution.
Exact replacement wording: `The amplitude pipeline must physically halt if any variable outside the pinned set \`(M, α, distance)\` is requested. The seat asserts \`C5_AMPLITUDE_PROVENANCE=PASS\` only if the executed code contains no external amplitude injections. Exact assertion: \`C5_AMPLITUDE_PROVENANCE=PASS\`.`

Justification: The numeral tracing is verified and sound, and the circularity defense is robust (Table 1 uses a 10 solar mass control, completely disjoint from the >10,000 solar mass result volume). However, Limb A and Control C5 relied on LLM promises and judgements rather than mechanical, operational tests. The repairs force a mathematical derivation for the amplitude and a physical pipeline halt for C5, removing the LLM's freedom to finesse the exit condition. Outcome class 2 was also tightened to guarantee mutual exclusivity with class 1.

Regarding Criterion 8, given L400 explicitly states that calculating the excitation factors is an "involved task" left for the community, Limb A is highly likely to end the study immediately, and the design is entirely right to spend this cheap limb before committing to the expensive compute.

K5_PREREG_GATE_COMPLETE

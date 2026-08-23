# Brief: blind independent implementation of the Phase-4 A1 numerics (seat: gpt1)

You are one of two INDEPENDENT implementations of the same ODE system. You must NOT look at any
other implementation (there is none committed yet; keep it that way — do not search the repo for
one). Your value is exactly your blindness.

## Task
From the pinned source text ONLY —
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-reading-20260823/sources/0210105_clean.txt`
(Smoller & Temple, "Shock-Wave Cosmology Inside a Black Hole", astro-ph/0210105) —
implement and integrate the shock-matching ODE system (equations (4.1)–(4.3) in that text, with
the constraint equation for v and variables u = p̄/ρ, v = ρ̄/ρ, σ = p/ρ), starting from the
σ = 1/3 pure-radiation exact solution the paper describes, and produce the shock trajectory
r_shock(t) and the TOV-side profile.

## Rules
- Equations transcribed from the source text with line references; if any equation is ambiguous
  in the OCR, note the ambiguity and your resolution — do not silently guess.
- Write ONLY inside: .../bhu-theory-phase4-anisotropy-20260823/platoon/gpt1_blind_a1/
  (temp files as _tmp_* in that dir; never /tmp or TMPDIR).
- Deliverables: your integration script(s), a results table (CSV: t, r_shock, u, v, N, and the
  TOV-side density/pressure at the shock), a README stating equation line-refs, integration
  method, step control, and every check you ran.
- Do NOT read or write anything else in the phase-4 dir. Do not commit; leave files for
  verification.
- Completion marker: write GPT1_A1_DONE.md in your dir when finished.

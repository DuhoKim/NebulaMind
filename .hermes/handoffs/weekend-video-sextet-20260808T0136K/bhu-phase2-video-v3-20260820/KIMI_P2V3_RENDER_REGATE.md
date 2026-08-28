PASS_P2V3_RENDER — token kimi-p2v3-render-regate-pass-20260820T0343K

kimi (same seat, fresh one-shot), 2026-08-20 ~03:43 KST. Bounded re-gate of the v3 render
after the chip-fix pass. This standalone file mirrors the RE-GATE AFTER CHIP-FIX section
appended to KIMI_P2V3_RENDER_GATE.md. Findings-only; nothing else edited; zero fetches;
portal.nersc.gov untouched. All mechanical checks recomputed this session.

1. Custody — PASS.
- build/BHU_PHASE2_EXPLAINER_V3_LOCAL_REVIEW.mp4 sha-256 =
  46b670a5ee083153a07629b90f80ec71a1b362d0a191f6178bfaa9035d51bd96 — byte-matches the
  CHIP-FIX value in GPT3_F_DONE.md.
- build/PANEL_STILLS/panel_01.png = 65480e9d…8c8540; panel_02.png = 33ee1dcd…d7114b;
  panel_11.png = 47170684…822186 — all three byte-match the receipt.
- ffprobe duration = 706.833333 s — equals 706.833 s within rounding. 16 stills on disk;
  container audio stream is AAC.

2. Chips — 3/3 PASS. The standard pill "NebulaMind rendering — Concept Illustration Only" is
present and legible at display scale on all three fixed stills (P01 lower-left, P02
lower-left, P11 lower-right). Wording adjudication: RULED spec-compliant, no re-fix. The
trust function of the chip rule (art never mistakable for evidence) is carried by the
categorical half "Concept Illustration Only"; the provenance half is the verbatim
DESIGN_SYSTEM.md PART 1 Illustration Chip, mandated on "every generated or programmatic
concept art" with PART 2 art briefs drafted explicitly for Nano Banana Pro — so the DS
itself intends this pill for Nano-Banana-generated P01. Precise provenance belongs to the
separate Attribution Chip class reserved for third-party paper figures; Nano-Banana is a
tool, not a rights-holder, and "NebulaMind rendering" accurately reads as production
provenance. No misattribution of evidence or authorship results. (Observation only: if
per-generator credits are ever wanted on concept art, that is a DESIGN_SYSTEM revision,
outside this gate.)

3. Audio unchanged — receipt-accepted per the re-gate brief: GPT3_F_DONE.md states the AAC
elementary stream was stream-copied byte-for-byte (SHA-256 before/after
b4435da79b8432278f717bc7e4438af71510ff4c3ee302b80ba56a23c2d73efe), all 16 narration WAVs and
the narration master byte-identical, ASR unaffected. Not independently recomputed.

4. Prior PASS findings from the first gate (KIMI_P2V3_RENDER_GATE.md §§1–4) stand as carried,
not re-audited: custody of the prior encode, full ASR audit (0 contract-bearing residuals,
zero scope-disclaimer hits), frame audit of the other 13 stills, all named sub-checks
(headings, palette, no dividers, four attribution chips, permitted equations only, Planck
markers, ladder edges, zero v2-style quality failures), arithmetic spot-check.

Verdict: the HOLD basis is fully cleared. PASS_P2V3_RENDER.

— kimi, render re-gate, 2026-08-20.

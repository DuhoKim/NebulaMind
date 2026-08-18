# GORU — v2 visual plan brief

Read `SEXTET_BRIEF_V2.md` first. Inputs: the ledgered `SCRIPT.md` + `STORYBOARD.json` in this
directory (do not start before Lana's `LANA_DONE.md` exists and any FLAGs are repaired).
Reference: your v1 plan `../bhu-neutron-star-explainer-20260817/VISUALS.md` and the v1 renderer
`../bhu-neutron-star-explainer-20260817/build/render_cards.py` — the v2 renderer will be written
against your plan exactly as v1 was.

Deliverables into THIS directory:

1. `VISUALS.md` — per panel: layout description, the deterministic geometry (what is drawn,
   where, what it encodes), which `viewer_text_closed_world` entries go where, palette roles.
   Keep the v1 system: 1920×1080 Pillow flat infographics, dark starfield backdrop as dim
   atmosphere only, assertion heading top, rounded plates for labels, closed-world text only —
   Goru may propose REDUCING viewer text, never adding factual text without Lana review.
2. `GORU_DONE.md`, first line `GORU_V2_VISUALS_COMPLETE`.

## Panel-specific requirements

- **The nesting/CNS panels (new in v2):** the reproduce-through-black-holes loop must be drawable
  with simple deterministic shapes (circles/arrows); no generated imagery, no invented
  quantitative claims in pictures. A family-tree/loop diagram is fine; a "count of universes"
  axis is NOT (no such number is gated).
- **Mass-ladder panel (carried from v1):** the honesty rule is frozen — the quoted 68.3%
  interval of 2.08 ± 0.07 sits entirely above the 2.00 line; the stricter 95.4% state is a soft,
  endpoint-free halo visibly crossing 2.00; no numeric lower bound is drawn or implied; the
  1.5 line with the 3 securely-above systems stays.
- **4%-vs-19.3% bar panel (carried from v1):** threshold bar and observed bar to one linear
  scale, error whisker 18.6–20.0, no log tricks.
- **Per-link outcome panel:** dead / serious-doubt / not-refuted must be visually distinct
  states; "not refuted" must not look like "supported".
- No divider cards. Cosmic footage/backdrop never carries claim content.

Write only inside this lane directory. No fetches. No image APIs, no credits.

# Design System: Born inside a black hole? (Phase 2 Explainer v3)

This design system upgrades the visual quality to professional standard: legible, beautiful, and comprehensible on any device.

## PART 1 — The Visual Language

### Layout Grid (Full-Bleed 1920x1080)
*   **Safe Area**: 120px margins on all sides (1680x840 active area) to ensure mobile and TV legibility without cropping.
*   **Columns**: 12-column grid. Standard splits are 6/6 (split screen), 4/8 (sidebar and main art), or 12 (full width).
*   **Panel Transitions**: Smooth crossfades or directional wipes. **No divider cards.**

### Type Scale (Phone-Legible)
*   **Display Headings (64-96px)**: High-contrast, clean sans-serif (e.g., Roboto or Inter) in Semibold/Bold. Used for panel assertion headings.
*   **Body Annotations (36-44px)**: Medium weight, used for plain-words definitions, ladders, and diagram labels.
*   **Chips / Microcopy (28px)**: Regular weight, all-caps or title case. Used for attribution chips and illustration tags.

### Dark Cosmic Palette
*   **Background Deep (Hex `#0B0C10`)**: The infinite cosmic void, used for base canvas.
*   **Background Panel (Hex `#1F2833`)**: Elevated rounded plates for text and charts.
*   **Text Primary (Hex `#FFFFFF`)**: High-contrast white for headings and core claims.
*   **Text Secondary (Hex `#C5C6C7`)**: Muted silver for definitions and secondary text.
*   **Accent Cyan (Hex `#66FCF1`)**: For primary highlighted items, cursors, and data lines.
*   **Accent Teal (Hex `#45A29E`)**: For secondary accents, ladder bands, and bounding boxes.
*   **Warning/Limit (Hex `#FF4C4C`)**: For the causality speed-limit and the closed ceiling.

### Animation Vocabulary
*   **Staged Builds**: Elements MUST enter exactly synced to narration beats. Never reveal the whole panel at once. Start with analogy, fade in mechanism, then fade in numbers.
*   **Plot Walkthroughs**: A smooth, glowing Accent Cyan cursor traces the curves on the exact paper plots while annotations fade in at the critical turning points.
*   **Ladders and Magnitude Scales**: Staged bands (not single rungs). Both edges must be marked to show the range (e.g., `10,000-100,000 x`). No unlabeled logarithmic tricks; visually enforce the scale with break-lines if orders of magnitude are skipped.

### Chip Designs
*   **Attribution Chip**: Pill-shaped, dark semi-transparent background (`#0B0C10` at 80% opacity), `Text Secondary` 28px font. Used for paper plots: "Figure N, arXiv:XXXX (author version)".
*   **Illustration Chip**: Pill-shaped, Accent Teal outline, `Text Secondary` 28px font. Used on every generated or programmatic concept art: "NebulaMind rendering — Concept Illustration Only".

---

## PART 2 — Per-Panel Art Briefs for Nano Banana Pro

*Note: As COMPREHENSION_AUDIT.md was not present at the time of drafting, this is drafted against the v2 12-panel structure. Panels likely to split for pacing (e.g., Panels 03, 05, 07, 09) will inherit the same primary art piece but sequence the annotations differently.*

**Shared Style Descriptor String (Prepend to all prompts):**
`[Cosmic infographic illustration, clean vector style, dark background, luminous neon accents, highly legible, conceptual science art:]`

### Panel 01: The Verdict Intro (Cold Open)
*   **Prompt**: `[Cosmic infographic illustration, clean vector style, dark background, luminous neon accents, highly legible, conceptual science art:] A stylized, glowing silhouette of a giant parent black hole emitting a faint umbilical beam down to a small, enclosed baby universe sphere.`
*   **Text In-Image**: None.
*   **Layout Slot**: 12-column full-bleed background.
*   **Fallback**: Programmatic gradient mesh connecting a large top circle to a small bottom circle with a dashed arrow.
*   **Note**: Concept illustration only; depicts no data.

### Panel 02 & 03 (Likely Split): Paper 1 — Spacetime Twist from Spin
*   **Prompt**: `[Cosmic infographic illustration, clean vector style, dark background, luminous neon accents, highly legible, conceptual science art:] A smooth, twisting fabric of spacetime being compressed tightly like a glowing neon spring, glowing brighter at the center to represent a bounce.`
*   **Text In-Image**: "SPRING-LIKE PUSHBACK" (44px, large clean sans-serif).
*   **Layout Slot**: 8-column right-side dominant art.
*   **Fallback**: Programmatic animated sine wave compressing and reflecting into an expansion curve.
*   **Note**: Concept illustration only; depicts no data.

### Panel 04 & 05 (Likely Split): Paper 2 — The Cusp & Spike (Uses Paper Plots)
*   **Art Brief**: No generated art. We MUST use the authoritative `assets/prd_1111.4595_fig1_scale.jpg` and `fig2_temp.jpg`.
*   **Layout Slot**: 8-column right-side plate.
*   **Walkthrough**: Glowing cyan cursor traces the blue curve. Planck marker chip fades in next to the temperature spike.

### Panel 06 & 07 (Likely Split): Paper 3 — The Black-Hole Nursery (Seed Pod)
*   **Prompt**: `[Cosmic infographic illustration, clean vector style, dark background, luminous neon accents, highly legible, conceptual science art:] A glowing, semi-transparent seed pod floating in deep space, with a dense mass at the top feeding a small, fiery glowing core at the bottom.`
*   **Text In-Image**: "PARENT MASS" (top), "STARTING SIZE & HEAT" (bottom) — very large, clean text.
*   **Layout Slot**: 8-column right-side dominant art.
*   **Fallback**: Programmatic flowchart nodes mapping `M` to `(a_i, T_i)`.
*   **Note**: Concept illustration only; depicts no data.

### Panel 08: Paper 4 — One-Sentence Card Backdrop
*   **Prompt**: `[Cosmic infographic illustration, clean vector style, dark background, luminous neon accents, highly legible, conceptual science art:] A minimalist collapsing star shrinking into a dense point, heavily shadowed, leaving empty cosmic space around it.`
*   **Text In-Image**: None.
*   **Layout Slot**: Full-bleed 12-column, heavily darkened so the quoted text card can overlay cleanly in the center.
*   **Fallback**: Programmatic shrinking concentric circles fading to black.
*   **Note**: Concept illustration only; depicts no data.

### Panel 09 (Likely Split): A Spinning Parent's Bounce (Causality Speed-Limit)
*   **Prompt**: `[Cosmic infographic illustration, clean vector style, dark background, luminous neon accents, highly legible, conceptual science art:] A glowing horizontal speed-limit barrier made of red light. A massive glowing arrow shoots upward from below, crashing into and vastly overshooting the red barrier.`
*   **Text In-Image**: "COSMIC SPEED LIMIT" (on the red barrier).
*   **Layout Slot**: 6-column split-screen (left for text, right for the visual ladder).
*   **Fallback**: Programmatic red dashed line with an animated arrow shooting infinitely past it, scaling the Y-axis.
*   **Note**: Concept illustration only; depicts no data.

### Panel 10: Ancient Helium Fossil Record (Uses Paper Plots)
*   **Art Brief**: No generated art. We MUST use the authoritative `assets/ds_1006.4166_comparison.png` and `prefac_Yp.png`.
*   **Layout Slot**: 8-column right-side plate.
*   **Walkthrough**: Highlight bounds programmatically.

### Panel 11 & 12: The Generous Stack & Verdict Ending
*   **Prompt**: `[Cosmic infographic illustration, clean vector style, dark background, luminous neon accents, highly legible, conceptual science art:] A vast, glowing floor made of millions of tiny starlight dots (representing 2 trillion galaxies). Floating far below this floor is a single, microscopic, barely-visible glowing ember.`
*   **Text In-Image**: None.
*   **Layout Slot**: 12-column full-bleed background, with UI overlays mapping the ~10^-5 to 10^-4 gap.
*   **Fallback**: Programmatic grid floor with a labeled point plotted logarithmically far below the baseline.
*   **Note**: Concept illustration only; depicts no data.

# VISUALS.md — v2 visual plan

**Status:** Goru visual plan complete. No generated media, no credits, no external APIs. All layouts use deterministic geometry drawn via Pillow.

## System-wide Design (The v1 System)
- **Resolution:** 1920×1080.
- **Background:** Dark starfield backdrop as dim atmosphere only (opacity 20-30%); no claim content in the background.
- **Layout:** Assertion heading at the top. Rounded plates for labels.
- **Text:** Closed-world text only from `viewer_text_closed_world` in STORYBOARD.json.
- **Palette Roles:** 
  - Backgrounds: Dark slate/black (#0b0f19).
  - Headings: Bright white (#ffffff).
  - Normal Text: Off-white (#e2e8f0).
  - Accents/Thresholds: Neon blue (#00d2ff) for safe/neutral, orange/red (#ff4b4b) for doubt/failure/dead.
  - Survivors (Not Refuted): Neutral grey/blue (#94a3b8). Must NOT look like bright green/supported.

---

## Panel 01
**Heading:** This specific chain fails its own second neutron-star test
- **Layout Description:** Stark, high-contrast title card establishing stakes.
- **Deterministic Geometry:** A simple vertical sequence of text plates centered on screen.
- **Viewer Text Placement:**
  - Top plate: "DUHO'S PERSONAL SIDE-INTEREST" & "NOT A NEBULAMIND RESEARCH PROGRAMME"
  - Middle left plate: "SEALED RULE → PUBLISHED PULSAR MEASUREMENTS"
  - Bottom left plate: "HEAVY-STAR TEST — SERIOUS DOUBT"
  - Bottom right plate: "BINARY TEST — CHAIN FAILS"
- **Palette Roles:** Muted greys for scope, bright accents for the test outcomes.

## Panel 02
**Heading:** Black-hole-universe cosmology is a family, not 1 theory
- **Layout Description:** Timeline/branching diagram showing the evolution of the idea.
- **Deterministic Geometry:** A central node (circle) on the left that branches into 5 parallel horizontal lines extending to the right.
- **Viewer Text Placement:**
  - Left node: "1972 — A CLOSED UNIVERSE INSIDE A BLACK HOLE"
  - Below left node: "ACCESSIBLE ABSTRACT: RADIUS CONDITION · OSCILLATION · BOUNDED EXPANSION"
  - Right branches: "AT LEAST 5 DISTINCT PROGRAMMES" & "THE PROGRAMMES DISAGREE"
- **Palette Roles:** Neutral/informative blue for nodes and paths. Branches use slightly different shades of grey/blue to show "disagree".

## Panel 03
**Heading:** Cosmological natural selection adds reproduction and selection
- **Layout Description:** Loop diagram for the reproduction cycle.
- **Deterministic Geometry:** A circular arrow loop connecting 3 nodes (circles). No quantitative axes.
- **Viewer Text Placement:**
  - Node 1 (Top): "UNIVERSES REPRODUCE THROUGH BLACK HOLES"
  - Node 2 (Right): "SLIGHTLY MUTATED CONSTANTS"
  - Node 3 (Bottom): "MORE BLACK HOLES → MORE DESCENDANTS"
  - Center/Final Plate: "CONSTANTS NEAR VALUES FAVORING BLACK-HOLE PRODUCTION"
- **Palette Roles:** Dynamic teal for the loop arrows to show progression.

## Panel 04
**Heading:** CNS made the cosmic idea checkable with a low mass ceiling
- **Layout Description:** A funnel diagram or directional flow from abstract idea to measurable metric.
- **Deterministic Geometry:** A wide top rectangle flowing down into a narrow bottom rectangle (funnel shape) pointing to a pulsar icon (circle with radial lines).
- **Viewer Text Placement:**
  - Top: "STATED FALSIFIABLE CONSEQUENCE"
  - Middle: "PROPOSED ULTRA-DENSE-MATTER CHANGE: KAON CONDENSATION"
  - Bottom: "BROWN–BETHE CEILING: ABOUT 1.5 TIMES THE SUN'S MASS"
  - Pulsar label: "MASSES MEASURED THROUGH PULSAR TIMING"
- **Palette Roles:** Funnel gradient from abstract blue to concrete white.

## Panel 05
**Heading:** The source offered 2 tests joined by or
- **Layout Description:** A distinct two-limb branch emphasizing the logical "OR".
- **Deterministic Geometry:** A single block splitting symmetrically into two distinct, equal-weight rounded rectangles side-by-side.
- **Viewer Text Placement:**
  - Left rectangle: "TEST 1 — A STAR AROUND 2 TIMES THE SUN'S MASS"
  - Center prominent circle: "OR"
  - Right rectangle: "TEST 2 — A DOUBLE NEUTRON STAR PAIR DIFFERING BY MORE THAN 4%"
  - Bottom wide plate: "EITHER TEST COUNTS"
- **Palette Roles:** Bright yellow/white for "OR". Symmetrical neutral boxes.

## Panel 06
**Heading:** The heavy-star test reaches serious doubt
- **Layout Description:** The Mass Ladder chart.
- **Deterministic Geometry:** Vertical Y-axis (Solar Masses). 
  - Solid horizontal line at 1.5. 
  - Dashed horizontal line at 2.00.
  - Data point for PSR J0740+6620 at 2.08. 
  - A solid error bar (68.3%) spanning 2.01 to 2.15 (entirely above 2.00).
  - A softer gradient halo (95.4%) extending downwards from 2.01 across the 2.00 line with no hard lower endpoint.
  - 3 generic data points securely above 1.5.
- **Viewer Text Placement:**
  - "PSR J0740+6620: 2.08 ± 0.07 TIMES THE SUN'S MASS"
  - Next to error bar: "68.3% — CLEARS 2.00"
  - Next to soft halo: "95.4% — DOES NOT CLEAR 2.00"
  - Lower area: "3 SYSTEMS ≥ 8 STANDARD DEVIATIONS ABOVE 1.5"
  - Bottom plate: "LITERAL 1.5 CEILING — CONTRADICTED"
- **Palette Roles:** 1.5 line in Red, 2.00 line in Orange. 68.3% bar in solid white, 95.4% halo in fading grey.

## Panel 07
**Heading:** The binary test fails the chain by a wide margin
- **Layout Description:** Linear bar chart comparing threshold and observed value.
- **Deterministic Geometry:** A single horizontal axis.
  - Short vertical tick for 4% threshold.
  - A long horizontal bar stretching to 19.3%.
  - Error whisker at the end spanning 18.6 to 20.0. Linear scale (no log tricks).
- **Viewer Text Placement:**
  - Top plate: "PSR J1913+1102"
  - Next to top plate: "1.599 ± 0.008 VS 1.290 ± 0.008 TIMES THE SUN'S MASS"
  - Threshold label: "SOURCE LIMIT: 4%"
  - Bar label: "MEASURED DIFFERENCE: 19.3 ± 0.7%"
  - Emphasized text: "NEARLY 5 TIMES THE THRESHOLD"
  - Bottom corner: "PUBLISHED 2020 · SHARPENED 2026"
- **Palette Roles:** 4% threshold in stark white. 19.3% bar in solid red to indicate failure.

## Panel 08
**Heading:** A sealed rule keeps the threshold from following the answer
- **Layout Description:** A sequenced timeline/checklist.
- **Deterministic Geometry:** 3 vertically stacked rounded plates with a lock icon (square with a semi-circle on top) next to the first one. A separate overlapping plate for the caveat.
- **Viewer Text Placement:**
  - Plate 1: "1 · CRITERION HASH-SEALED"
  - Plate 2: "2 · EVIDENCE HARVESTED"
  - Plate 3: "3 · RULE APPLIED WITHOUT NARROWING"
  - Floating plate right: "HE-RED-GIANT CAVEAT FOUND AFTER SEALING"
  - Bottom summary: "19.3% REMAINS NEARLY 5 TIMES 4%"
  - Bottom summary line 2: "VERDICT UNCHANGED"
- **Palette Roles:** Grey/silver for the chronology plates, distinct yellow/orange for the caveat plate, firm red/white for the verdict.

## Panel 09
**Heading:** The chain loses links; the wider family survives
- **Layout Description:** Hierarchical tree diagram with distinct visual states.
- **Deterministic Geometry:** A top-down tree. 
  - Top node (wider family). 
  - Middle node (CNS). 
  - Left branch (Earlier links). 
  - Bottom branch (Brown-Bethe).
- **Viewer Text Placement:**
  - Bottom crossed-out node: "BROWN–BETHE 1.5 CEILING — DEAD AS A LITERAL PREDICTION"
  - Left faded node: "EARLIER LINKS — SERIOUS DOUBT THROUGH THIS CHAIN"
  - Middle dashed node: "CNS FLAGSHIP NEUTRON-STAR PREDICTION — GONE"
  - Middle solid node: "CNS ITSELF — NOT REFUTED"
  - Top solid node: "AT LEAST 5-PROGRAMME BHU FAMILY — NOT FALSIFIED"
- **Palette Roles:** 
  - Dead: Red with strike-through line.
  - Serious Doubt: Orange, dashed outline.
  - Not Refuted (survivors): Neutral grey/blue.

## Panel 10
**Heading:** The source's second rule had already answered the test
- **Layout Description:** Final summary layout, side-by-side comparison of the two limbs resolving.
- **Deterministic Geometry:** Two columns. Left column for test 1, right column for test 2. Top and bottom spanning plates.
- **Viewer Text Placement:**
  - Top plate: "MEASUREMENTS — THE PULSAR COMMUNITY"
  - Under top plate: "OUR ROLE — APPLY A PRE-REGISTERED RULE"
  - Left column: "HEAVY-STAR TEST — SERIOUS DOUBT"
  - Right column: "BINARY TEST — THRESHOLD CLEARED SINCE 2020"
  - Bottom prominent plate: "THIS SPECIFIC CHAIN FAILS ITS AUTHORS' SECOND RULE"
- **Palette Roles:** Left column in orange (doubt), Right column in stark red (failure). Bottom plate highly contrasted (white text on dark red) for final verdict.

# Goru G3 Surveys Accessibility/Static Audit Report

Marker: `GORU_G3_SURVEYS_ACCESSIBILITY_REPORT_20260707T105700Z`
Run: `SURVEYS_LOW_USAGE_AUTONOMOUS_RUN_20260707T105700Z`

## Status
**Completed** - Static pattern checks and mechanical tasks executed against specified components. No product files modified.

## Mechanical Tasks Findings

### 1. Clickable `div`s vs. Native Buttons/Links
There are several instances of custom interactive elements (using `onClick` on non-interactive semantic tags) compared to native `<button>` or `<a>`:
- **Native buttons/links:** Extensively used in `ControlBar.tsx`, `FilterSheet.tsx`, `SurveyPeek.tsx`, and `SurveyDetailClient.tsx` for standard actions.
- **Clickable `div`s and `<g>` tags:**
  - `BandSpectrumStrip.tsx`: Uses `div` for the band segments (x2 mapped in source).
  - `SurveyCard.tsx`: Uses `div` for the entire card.
  - `PlotA.tsx`: Uses SVG `<g>` for data points.
  - `PlotB.tsx`: Uses SVG `<g>` for data points.
  - *Note: Backdrop `div`s in `FilterSheet.tsx` and `SurveyPeek.tsx` also have `onClick`, but are non-primary UI paths (dismissals).*

### 2. Keyboard Access for Click Targets
- **Pass (`PlotA.tsx`):** Data point `<g>` elements correctly implement `tabIndex={0}`, `role="button"`, and an `onKeyDown` handler that listens for "Enter" or "Space".
- **Fail (`BandSpectrumStrip.tsx`):** Band segments (`div`) lack `tabIndex` and keyboard event handlers.
- **Fail (`SurveyCard.tsx`):** Survey cards (`div`) lack `tabIndex` and keyboard event handlers.
- **Fail (`PlotB.tsx`):** Data point `<g>` elements lack `tabIndex`, `role`, and keyboard event handlers.

### 3. SVG `role`/`title`/`desc` Parity
- **Plot A (`PlotA.tsx`):** Implements full accessibility semantics: `<svg role="img" aria-labelledby="...">` along with distinct `<title>` and `<desc>` child elements.
- **Plot B (`PlotB.tsx`):** Lacks `role="img"`, `aria-labelledby`, `<title>`, and `<desc>`. The SVG is completely opaque to screen readers.

### 4. Disclosure Buttons (`aria-expanded` / `aria-controls`)
- **Pass (`PlotA.tsx`):** "Missing surveys" disclosure button properly implements `aria-expanded={missingExpanded}` and `aria-controls={missingListId}`.
- **Fail (`PlotB.tsx`):** "Missing surveys" disclosure button omits `aria-expanded` and `aria-controls`.
- **Fail (`SurveyDetailClient.tsx`):** DatasetCard accordion toggle `<button>` omits `aria-expanded` and `aria-controls`.

### 5. Modal/Sheet Behavior
- **Escape Key & Backdrop:** `FilterSheet.tsx` and `SurveyPeek.tsx` successfully implement background click handlers and `Escape` key listeners (`useEffect`).
- **Missing Accessibility Attributes:** Both sheets lack `role="dialog"` and `aria-modal="true"`.
- **Focus Trapping:** Neither sheet implements focus trapping (e.g., locking Tab navigation within the modal). Keyboard focus can stray onto the inert background page while the sheet is open.

## Ranking of Findings

1. **High Impact, Low Risk:** Click targets in `SurveyCard.tsx` and `BandSpectrumStrip.tsx` are completely inaccessible to keyboard-only users due to missing `tabIndex` and keyboard listeners.
2. **High Impact, Low Risk:** `PlotB.tsx` interactive scatter points lack `tabIndex` and keyboard handlers, preventing keyboard navigation of plotted surveys. 
3. **High Impact, Low Risk:** `PlotB.tsx` lacks SVG screen-reader parity (`role="img"`, `<title>`, `<desc>`), hiding its presence and purpose from assistive technologies.
4. **Medium Impact, Medium Risk:** `FilterSheet.tsx` and `SurveyPeek.tsx` lack `role="dialog"`, `aria-modal="true"`, and focus trapping logic, allowing keyboard navigation to leak behind the active overlay.
5. **Low Impact, Low Risk:** Missing `aria-expanded`/`aria-controls` on the disclosure toggles in `PlotB.tsx` and `SurveyDetailClient.tsx` DatasetCards.

## Safety Ledger
- `NO ACTIVE EXECUTION PHRASE`
- All evaluations performed strictly as static source code reads.
- No files were modified. No cloud, DB, Git, or API write actions were executed.

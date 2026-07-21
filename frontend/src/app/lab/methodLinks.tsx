"use client";

// Cross-links between the Methods step (analysis recipes) and the Paper step
// (manuscripts). Papers carry a `methods: string[]` of method ids; these helpers
// turn that into clickable chips on a draft ("methods used") and, on the Methods
// side, an inverse index ("papers using this method"). Deep-links go through the
// shared tab store so navigation stays SPA + URL-persistent (?tab=research&sub=…).
import { RESEARCH_ITEMS } from "./stageData";
import { select } from "./labTabStore";

// value → short method label. Single source of truth = the Methods sub-items,
// so a renamed/added method never drifts out of sync with its chip.
export const METHOD_LABEL: Record<string, string> = Object.fromEntries(
  RESEARCH_ITEMS.map((i) => [i.value, i.label]),
);

// Clickable "methods used" chips shown on a draft card — each deep-links into
// the Methods step and selects that method's sub-item.
export function MethodChips({ methods }: { methods?: string[] | null }) {
  if (!methods?.length) return null;
  return (
    <div className="mlx-chips">
      <span className="mlx-k">methods</span>
      {methods.map((m) => (
        <button
          type="button"
          key={m}
          className="mlx-chip"
          onClick={() => select("research", m)}
          title={`Method: ${METHOD_LABEL[m] ?? m} — open in Methods`}
        >
          {METHOD_LABEL[m] ?? m}
        </button>
      ))}
    </div>
  );
}

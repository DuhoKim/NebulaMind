"use client";

import { STEPS, useTab, setTab, StepKey } from "./labTabStore";

// Pipeline stage tabs, rendered in the sticky top banner.
// Clicking a tab selects that stage and scrolls the stage panel into view.
export default function LabTopTabs() {
  const tab = useTab();

  function go(k: StepKey) {
    setTab(k);
    if (typeof document !== "undefined") {
      document.getElementById("pipeline")?.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  return (
    <div className="lab-toptabs" role="tablist" aria-label="Research pipeline">
      {STEPS.map((s) => (
        <button
          key={s.key}
          role="tab"
          aria-selected={tab === s.key}
          className={`lab-toptab${tab === s.key ? " on" : ""}`}
          onClick={() => go(s.key)}
        >
          {s.label}
        </button>
      ))}
    </div>
  );
}

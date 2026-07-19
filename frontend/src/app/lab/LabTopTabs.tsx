"use client";

import { useState, useEffect, useRef } from "react";
import { STEPS, select, useTab, useSub, StepKey } from "./labTabStore";
import { itemsFor } from "./stageData";

// Sticky top-nav for the pipeline stages. Clicking a stage only opens its
// dropdown menu — the page never moves on the tab click itself; navigation
// happens only when a menu item (its Overview, or a sub-step) is picked. This
// avoids the jarring jump to the section "home" just to reach a sub-nav.
export default function LabTopTabs() {
  const tab = useTab();
  const sub = useSub();
  const [open, setOpen] = useState<string | null>(null);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function onDoc(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) setOpen(null);
    }
    document.addEventListener("mousedown", onDoc);
    return () => document.removeEventListener("mousedown", onDoc);
  }, []);

  function scrollPipe() {
    if (typeof document !== "undefined") {
      document.getElementById("pipeline")?.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }
  // Tab click: just toggle this stage's menu open/closed — no navigation.
  function onTab(stage: StepKey) {
    setOpen(open === stage ? null : stage);
  }
  // Picking a menu item is what actually navigates.
  function pick(stage: StepKey, value: string) {
    select(stage, value);
    setOpen(null);
    scrollPipe();
  }

  return (
    <div className="lab-toptabs" ref={ref} role="tablist" aria-label="Pipeline stages">
      {STEPS.map((s) => (
        <div className="lab-tt" key={s.key}>
          <button className={`lab-toptab${tab === s.key ? " on" : ""}`}
            aria-expanded={open === s.key} onClick={() => onTab(s.key)}>
            {s.label} <span className="lab-caret">▾</span>
          </button>
          {open === s.key && (
            <div className="lab-dd" role="menu">
              <button role="menuitem" className={tab === s.key && sub === "" ? "on" : ""}
                onClick={() => pick(s.key, "")}>
                Overview
              </button>
              <div className="lab-dd-sep" />
              {itemsFor(s.key).map((it) => (
                <button key={it.value} role="menuitem"
                  className={tab === s.key && sub === it.value ? "on" : ""}
                  onClick={() => pick(s.key, it.value)}>
                  {it.label}
                </button>
              ))}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}

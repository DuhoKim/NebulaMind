"use client";

import { useEffect, useState } from "react";
import { itemsFor } from "./stageData";

// The four pipeline stages, shared between the sticky top-nav dropdowns
// (LabTopTabs) and the stage panel (LabStages).
export const STEPS = [
  { key: "topic", label: "Topic", sub: "select", heading: "How the research topics were picked" },
  { key: "data", label: "Data", sub: "sources", heading: "The data sources" },
  { key: "research", label: "Research", sub: "method", heading: "The analysis methods" },
  { key: "paper", label: "Paper", sub: "outputs", heading: "The outputs produced" },
] as const;

export type StepKey = (typeof STEPS)[number]["key"];

let current: StepKey = "topic";
let currentSub = ""; // "" = overview / Home // "" = overview / Home // "" = overview / Home
const tabSubs = new Set<(k: StepKey) => void>();
const subSubs = new Set<(v: string) => void>();

export function getTab(): StepKey {
  return current;
}
export function getSub(): string {
  return currentSub;
}
// Reflect the current tab/sub in the URL (?tab=paper&sub=progress) so a refresh
// (or a shared link) restores the same page instead of snapping back to /lab.
function writeUrl() {
  if (typeof window === "undefined") return;
  const p = new URLSearchParams(window.location.search);
  if (current !== "topic") p.set("tab", current); else p.delete("tab");
  if (currentSub) p.set("sub", currentSub); else p.delete("sub");
  const qs = p.toString();
  window.history.replaceState(null, "", `${window.location.pathname}${qs ? "?" + qs : ""}`);
}

// Restore tab/sub from the URL. Only overrides when params are present, so the
// default (and the screenshot temp-default) are left alone when the URL is bare.
export function syncFromUrl() {
  if (typeof window === "undefined") return;
  const p = new URLSearchParams(window.location.search);
  const t = p.get("tab");
  const s = p.get("sub");
  let changed = false;
  if (t && STEPS.some((x) => x.key === t)) { current = t as StepKey; changed = true; }
  if (s !== null) {
    currentSub = itemsFor(current).some((it) => it.value === s) ? s : "";
    changed = true;
  } else if (changed) {
    currentSub = ""; // a tab was given with no sub -> that tab's overview
  }
  if (changed) {
    tabSubs.forEach((f) => f(current));
    subSubs.forEach((f) => f(currentSub));
  }
}

// Select a stage and (optionally) a sub-item. Omitting sub picks the stage's first item.
export function select(tab: StepKey, sub?: string) {
  current = tab;
  currentSub = sub ?? "";
  tabSubs.forEach((f) => f(current));
  subSubs.forEach((f) => f(currentSub));
  writeUrl();
}
export function setTab(k: StepKey) {
  select(k);
}
export function setSub(v: string) {
  currentSub = v;
  subSubs.forEach((f) => f(v));
  writeUrl();
}

// Call once from the Lab shell: restore state from the URL on mount, and keep it
// in sync when the user hits browser back/forward.
export function useLabUrlSync() {
  useEffect(() => {
    syncFromUrl();
    const onPop = () => syncFromUrl();
    window.addEventListener("popstate", onPop);
    return () => window.removeEventListener("popstate", onPop);
  }, []);
}

export function useTab(): StepKey {
  const [t, setT] = useState<StepKey>(current);
  useEffect(() => {
    tabSubs.add(setT);
    setT(current); // catch up if the URL sync changed `current` before we subscribed
    return () => { tabSubs.delete(setT); };
  }, []);
  return t;
}
export function useSub(): string {
  const [v, setV] = useState<string>(currentSub);
  useEffect(() => {
    subSubs.add(setV);
    setV(currentSub);
    return () => { subSubs.delete(setV); };
  }, []);
  return v;
}

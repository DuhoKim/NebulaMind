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
// Select a stage and (optionally) a sub-item. Omitting sub picks the stage's first item.
export function select(tab: StepKey, sub?: string) {
  current = tab;
  currentSub = sub ?? "";
  tabSubs.forEach((f) => f(current));
  subSubs.forEach((f) => f(currentSub));
}
export function setTab(k: StepKey) {
  select(k);
}
export function setSub(v: string) {
  currentSub = v;
  subSubs.forEach((f) => f(v));
}

export function useTab(): StepKey {
  const [t, setT] = useState<StepKey>(current);
  useEffect(() => {
    tabSubs.add(setT);
    return () => { tabSubs.delete(setT); };
  }, []);
  return t;
}
export function useSub(): string {
  const [v, setV] = useState<string>(currentSub);
  useEffect(() => {
    subSubs.add(setV);
    return () => { subSubs.delete(setV); };
  }, []);
  return v;
}

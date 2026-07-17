"use client";

import { useEffect, useState } from "react";

// The four configurator stages, shared between the sticky top-banner tabs
// (LabTopTabs) and the configurator panel (LabConfigurator).
export const STEPS = [
  { key: "topic", label: "Topic", sub: "select", heading: "Pick a research question" },
  { key: "data", label: "Data", sub: "sources", heading: "Choose the data sources" },
  { key: "research", label: "Research", sub: "method", heading: "Select the analysis method" },
  { key: "paper", label: "Paper", sub: "outputs", heading: "Choose the outputs to produce" },
] as const;

export type StepKey = (typeof STEPS)[number]["key"];

let current: StepKey = "topic";
const subs = new Set<(k: StepKey) => void>();

export function getTab(): StepKey {
  return current;
}
export function setTab(k: StepKey) {
  current = k;
  subs.forEach((f) => f(k));
}
export function subscribe(f: (k: StepKey) => void) {
  subs.add(f);
  return () => {
    subs.delete(f);
  };
}
export function useTab(): StepKey {
  const [t, setT] = useState<StepKey>(current);
  useEffect(() => subscribe(setT), []);
  return t;
}

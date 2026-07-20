"use client";

import { useEffect, useLayoutEffect, useSyncExternalStore } from "react";
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
let currentSub = ""; // "" = overview / Home

// Single subscriber registry driving useSyncExternalStore — no per-hook setState
// races: every subscriber re-reads the snapshot on emit, in a deterministic order.
const listeners = new Set<() => void>();
function subscribe(cb: () => void): () => void {
  listeners.add(cb);
  return () => { listeners.delete(cb); };
}
function emit() {
  listeners.forEach((f) => f());
}

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
  const prevTab = current;
  const prevSub = currentSub;
  let changed = false;
  if (t && STEPS.some((x) => x.key === t)) { current = t as StepKey; changed = true; }
  if (s !== null) {
    currentSub = itemsFor(current).some((it) => it.value === s) ? s : "";
    changed = true;
  } else if (changed) {
    currentSub = ""; // a tab was given with no sub -> that tab's overview
  }
  // emit only on a real transition so useSyncExternalStore stays cheap
  if (current !== prevTab || currentSub !== prevSub || changed) emit();
}

// Select a stage and (optionally) a sub-item. Omitting sub picks the stage's overview.
export function select(tab: StepKey, sub?: string) {
  current = tab;
  currentSub = sub ?? "";
  emit();
  writeUrl();
}
export function setTab(k: StepKey) {
  select(k);
}
export function setSub(v: string) {
  currentSub = v;
  emit();
  writeUrl();
}

// Layout effect on the client (before paint → the deep-linked tab is applied
// before the user ever sees the default), plain effect on the server.
const useIsoLayoutEffect = typeof window !== "undefined" ? useLayoutEffect : useEffect;

// Call once from the Lab shell: restore state from the URL before first paint,
// and keep it in sync on browser back/forward.
export function useLabUrlSync() {
  useIsoLayoutEffect(() => {
    syncFromUrl();
    const onPop = () => syncFromUrl();
    window.addEventListener("popstate", onPop);
    return () => window.removeEventListener("popstate", onPop);
  }, []);
}

// useSyncExternalStore: getServerSnapshot returns the SSR default so hydration
// matches; the client snapshot is the live module value, updated race-free on emit.
export function useTab(): StepKey {
  return useSyncExternalStore(subscribe, getTab, () => "topic" as StepKey);
}
export function useSub(): string {
  return useSyncExternalStore(subscribe, getSub, () => "");
}

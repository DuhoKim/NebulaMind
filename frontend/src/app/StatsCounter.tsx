"use client";

import { useEffect, useState, useRef } from "react";

interface Props {
  pageCount?: number; // kept for backward compat but ignored — fetched internally
}

function useCountUp(target: number, duration = 1500) {
  const [value, setValue] = useState(0);
  const startRef = useRef<number | null>(null);
  const rafRef = useRef<number>(0);

  useEffect(() => {
    if (target === 0) return;
    startRef.current = null;
    const animate = (ts: number) => {
      if (!startRef.current) startRef.current = ts;
      const elapsed = ts - startRef.current;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      setValue(Math.round(eased * target));
      if (progress < 1) rafRef.current = requestAnimationFrame(animate);
    };
    rafRef.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(rafRef.current);
  }, [target, duration]);

  return value;
}

export default function StatsCounter({ pageCount: _ignored }: Props) {
  const [pageCount, setPageCount] = useState(0);
  const [agentCount, setAgentCount] = useState(0);
  const [edgeCount, setEdgeCount] = useState(0);
  const [evidenceCount, setEvidenceCount] = useState(0);

  useEffect(() => {
    // All fetches run client-side — avoids SSR failures silently zeroing stats
    fetch("/api/pages")
      .then((r) => r.json())
      .then((d) => setPageCount(Array.isArray(d) ? d.length : 0))
      .catch(() => {});

    fetch("/api/agents")
      .then((r) => r.json())
      .then((d) => setAgentCount(Array.isArray(d) ? d.length : 0))
      .catch(() => {});

    fetch("/api/graph")
      .then((r) => r.json())
      .then((d) => setEdgeCount(d?.edges?.length ?? 0))
      .catch(() => {});

    fetch("/api/stats")
      .then((r) => r.json())
      .then((d) => setEvidenceCount(d?.evidence_count ?? 0))
      .catch(() => {});
  }, []);

  const animPages = useCountUp(pageCount);
  const animAgents = useCountUp(agentCount);
  const animEdges = useCountUp(edgeCount);
  const animEvidence = useCountUp(evidenceCount);

  const stats = [
    { label: "Pages", value: animPages },
    { label: "Agents", value: animAgents },
    { label: "Connections", value: animEdges },
    { label: "Citations", value: animEvidence },
  ];

  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: "0.5rem", fontSize: "0.9rem", color: "#94a3b8" }}>
      {stats.map(({ label, value }, i) => (
        <span key={label} style={{ display: "inline-flex", alignItems: "center", gap: "0.5rem" }}>
          {i > 0 && <span style={{ color: "#334155" }}>|</span>}
          <span style={{ fontWeight: 600, color: "#f8fafc", fontVariantNumeric: "tabular-nums" }}>
            {value.toLocaleString()}
          </span>
          <span>{label}</span>
        </span>
      ))}
    </div>
  );
}

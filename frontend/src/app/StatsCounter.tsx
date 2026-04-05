"use client";

import { useEffect, useState, useRef } from "react";

interface Props {
  pageCount: number;
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
      const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
      setValue(Math.round(eased * target));
      if (progress < 1) rafRef.current = requestAnimationFrame(animate);
    };
    rafRef.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(rafRef.current);
  }, [target, duration]);

  return value;
}

export default function StatsCounter({ pageCount }: Props) {
  const [agentCount, setAgentCount] = useState(0);
  const [edgeCount, setEdgeCount] = useState(0);

  useEffect(() => {
    const API_BASE = process.env.NEXT_PUBLIC_API_URL || "";
    fetch(`${API_BASE}/api/agents`)
      .then((r) => r.json())
      .then((d) => setAgentCount(Array.isArray(d) ? d.length : 0))
      .catch(() => {});

    fetch(`${API_BASE}/api/graph`)
      .then((r) => r.json())
      .then((d) => setEdgeCount(d?.edges?.length ?? 0))
      .catch(() => {});
  }, []);

  const animPages = useCountUp(pageCount);
  const animAgents = useCountUp(agentCount);
  const animEdges = useCountUp(edgeCount);

  const stats = [
    { label: "Wiki Pages", value: animPages, suffix: "", icon: "📄" },
    { label: "Active Agents", value: animAgents, suffix: "", icon: "🤖" },
    {
      label: "Knowledge Connections",
      value: animEdges,
      suffix: "+",
      icon: "🔗",
    },
  ];

  return (
    <div className="grid grid-cols-3 gap-4 max-w-2xl mx-auto">
      {stats.map(({ label, value, suffix, icon }) => (
        <div
          key={label}
          className="bg-white/10 backdrop-blur-sm border border-white/15 rounded-2xl px-4 py-4"
        >
          <div className="text-2xl mb-1">{icon}</div>
          <div className="text-3xl sm:text-4xl font-extrabold text-white tabular-nums">
            {value.toLocaleString()}
            {suffix}
          </div>
          <div className="text-indigo-300 text-xs sm:text-sm mt-1 font-medium">
            {label}
          </div>
        </div>
      ))}
    </div>
  );
}

"use client";

import { useEffect, useState } from "react";

interface Stats {
  total_visits: number;
  human_visits: number;
  agent_visits: number;
  today_visits: number;
  today_human: number;
  today_agent: number;
  online_human: number;
  online_agent: number;
  unique_ips: number;
}

export default function VisitorCounter() {
  const [stats, setStats] = useState<Stats | null>(null);

  const refresh = () => {
    fetch("/api/stats").then((r) => r.json()).then(setStats).catch(() => {});
  };

  useEffect(() => {
    // Record visit
    fetch("/api/stats/visit?path=" + encodeURIComponent(window.location.pathname), {
      method: "POST",
    }).catch(() => {});

    refresh();

    // Refresh every 30 seconds
    const interval = setInterval(refresh, 30000);
    return () => clearInterval(interval);
  }, []);

  if (!stats) return null;

  const online = stats.online_human + stats.online_agent;

  return (
    <div className="flex flex-col items-center gap-2">
      {/* Online now */}
      <div className="inline-flex items-center gap-2 text-sm bg-green-50 border border-green-200 rounded-full px-4 py-1.5">
        <span className="relative flex h-2 w-2">
          <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
          <span className="relative inline-flex rounded-full h-2 w-2 bg-green-500"></span>
        </span>
        <span className="text-green-700">
          <strong>{online}</strong> online now
          {(stats.online_human > 0 || stats.online_agent > 0) && (
            <span className="text-green-500 ml-1">
              ({stats.online_human} 👤 {stats.online_agent} 🤖)
            </span>
          )}
        </span>
      </div>

      {/* Total stats */}
      <div className="inline-flex gap-4 text-xs text-gray-400">
        <span>👤 {stats.human_visits} humans</span>
        <span>🤖 {stats.agent_visits} agents</span>
        <span>🌐 {stats.unique_ips} unique</span>
        <span>Today: {stats.today_visits}</span>
      </div>
    </div>
  );
}

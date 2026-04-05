"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

interface Activity {
  type: string;
  agent_name: string;
  page_title: string;
  page_slug: string;
  timestamp: string;
  detail: string;
}

function timeAgo(ts: string): string {
  const diff = Date.now() - new Date(ts).getTime();
  const mins = Math.floor(diff / 60000);
  if (mins < 1) return "just now";
  if (mins < 60) return `${mins}m ago`;
  const hours = Math.floor(mins / 60);
  if (hours < 24) return `${hours}h ago`;
  const days = Math.floor(hours / 24);
  return `${days}d ago`;
}

const EMOJI: Record<string, string> = {
  edit: "✍️",
  vote: "🗳️",
  comment: "💬",
};

export default function ActivityFeed() {
  const [activities, setActivities] = useState<Activity[]>([]);
  const [loading, setLoading] = useState(true);

  const refresh = () => {
    fetch("/api/activity")
      .then((r) => r.json())
      .then((data) => {
        setActivities(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  };

  useEffect(() => {
    refresh();
    const interval = setInterval(refresh, 30000);
    return () => clearInterval(interval);
  }, []);

  return (
    <section className="mb-12">
      <div className="flex items-center gap-3 mb-4">
        <h3 className="text-lg font-bold">🔴 Live Activity</h3>
        <span className="relative flex h-2.5 w-2.5">
          <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
          <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-green-500"></span>
        </span>
      </div>

      {loading ? (
        <div className="text-gray-400 text-sm py-4">Loading activity...</div>
      ) : activities.length === 0 ? (
        <div className="text-gray-400 text-sm py-4 bg-gray-50 rounded-xl px-4 border border-gray-100">
          🛌 Agents are sleeping... They wake up every 5 minutes.
        </div>
      ) : (
        <div className="bg-white rounded-xl border border-gray-200 divide-y divide-gray-100">
          {activities.map((a, i) => (
            <div key={i} className="flex items-start gap-3 px-4 py-3 text-sm">
              <span className="text-base mt-0.5">{EMOJI[a.type] || "📌"}</span>
              <div className="flex-1 min-w-0">
                <span className="font-medium text-gray-900">{a.agent_name}</span>{" "}
                <span className="text-gray-500">{a.detail}</span>{" "}
                {a.page_slug && (
                  <Link
                    href={`/wiki/${a.page_slug}`}
                    className="text-indigo-600 hover:text-indigo-800 font-medium"
                  >
                    {a.page_title}
                  </Link>
                )}
              </div>
              <span className="text-xs text-gray-400 whitespace-nowrap mt-0.5">
                {timeAgo(a.timestamp)}
              </span>
            </div>
          ))}
        </div>
      )}
    </section>
  );
}

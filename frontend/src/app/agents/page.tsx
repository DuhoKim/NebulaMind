"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

interface AgentItem {
  id: number;
  name: string;
  model_name: string;
  role: string;
  is_active: boolean;
}

const ROLE_EMOJI: Record<string, string> = {
  editor: "✍️",
  reviewer: "🗳️",
  commenter: "💬",
};

const ROLE_COLOR: Record<string, string> = {
  editor: "bg-blue-100 text-blue-700",
  reviewer: "bg-purple-100 text-purple-700",
  commenter: "bg-green-100 text-green-700",
};

export default function AgentsPage() {
  const [agents, setAgents] = useState<AgentItem[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/agents")
      .then((r) => r.json())
      .then((data) => {
        setAgents(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  if (loading) return <div className="text-gray-400 py-8 text-center">Loading agents...</div>;

  const active = agents.filter((a) => a.is_active);
  const inactive = agents.filter((a) => !a.is_active);

  return (
    <div>
      <div className="mb-8">
        <h2 className="text-2xl font-bold mb-1">🤖 AI Agents</h2>
        <p className="text-gray-500 text-sm">
          {active.length} active agents building the cosmos knowledge base
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {active.map((agent) => (
          <Link
            key={agent.id}
            href={`/agents/${agent.id}`}
            className="block p-5 bg-white rounded-xl border border-gray-200 hover:border-indigo-300 hover:shadow-md transition-all no-underline text-inherit"
          >
            <div className="flex items-center gap-3 mb-3">
              <span className="text-2xl">{ROLE_EMOJI[agent.role] || "🤖"}</span>
              <div>
                <h3 className="font-semibold text-base">{agent.name}</h3>
                <p className="text-xs text-gray-400">{agent.model_name}</p>
              </div>
            </div>
            <div className="flex items-center gap-2">
              <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${ROLE_COLOR[agent.role] || "bg-gray-100 text-gray-600"}`}>
                {agent.role}
              </span>
              <span className="flex items-center gap-1 text-xs text-green-600">
                <span className="inline-block w-1.5 h-1.5 bg-green-500 rounded-full"></span>
                active
              </span>
            </div>
          </Link>
        ))}
      </div>

      {inactive.length > 0 && (
        <>
          <h3 className="text-lg font-semibold mt-10 mb-4 text-gray-400">Inactive Agents</h3>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 opacity-60">
            {inactive.map((agent) => (
              <Link
                key={agent.id}
                href={`/agents/${agent.id}`}
                className="block p-5 bg-gray-50 rounded-xl border border-gray-200 no-underline text-inherit"
              >
                <div className="flex items-center gap-3 mb-3">
                  <span className="text-2xl">{ROLE_EMOJI[agent.role] || "🤖"}</span>
                  <div>
                    <h3 className="font-semibold text-base">{agent.name}</h3>
                    <p className="text-xs text-gray-400">{agent.model_name}</p>
                  </div>
                </div>
                <span className="text-xs px-2 py-0.5 rounded-full font-medium bg-gray-200 text-gray-500">
                  inactive
                </span>
              </Link>
            ))}
          </div>
        </>
      )}
    </div>
  );
}

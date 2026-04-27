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
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    const check = () => setIsMobile(window.innerWidth < 768);
    check();
    window.addEventListener("resize", check);
    return () => window.removeEventListener("resize", check);
  }, []);

  useEffect(() => {
    fetch("/api/agents")
      .then((r) => r.json())
      .then((data) => {
        setAgents(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  if (loading) return <div style={{ color: "#9ca3af", padding: "2rem 0", textAlign: "center" }}>Loading agents...</div>;

  const active = agents.filter((a) => a.is_active);
  const inactive = agents.filter((a) => !a.is_active);

  return (
    <div>
      <div style={{ marginBottom: "2rem" }}>
        <h2 style={{ fontSize: "1.5rem", fontWeight: 700, marginBottom: "0.25rem", color: "#f8fafc" }}>AI Agents</h2>
        <p style={{ color: "#6b7280", fontSize: "0.875rem" }}>
          {active.length} active agents building the cosmos knowledge base
        </p>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: isMobile ? "1fr" : "repeat(auto-fill, minmax(280px, 1fr))", gap: "1rem" }}>
        {active.map((agent) => (
          <Link
            key={agent.id}
            href={`/agents/${agent.id}`}
            style={{ display: "block", padding: "1.25rem", background: "#1e293b", borderRadius: "12px", border: "1px solid #334155", textDecoration: "none", color: "#f8fafc", transition: "border-color 0.15s" }}
          >
            <div style={{ display: "flex", alignItems: "center", gap: "0.75rem", marginBottom: "0.75rem" }}>
              <span style={{ fontSize: "1.5rem" }}>{ROLE_EMOJI[agent.role] || "🤖"}</span>
              <div>
                <h3 style={{ fontWeight: 600, fontSize: "1rem", margin: 0 }}>{agent.name}</h3>
                <p style={{ fontSize: "0.75rem", color: "#9ca3af", margin: 0 }}>{agent.model_name}</p>
              </div>
            </div>
            <div style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}>
              <span style={{ fontSize: "0.75rem", padding: "2px 8px", borderRadius: "9999px", fontWeight: 500, background: "rgba(99, 102, 241, 0.1)", color: "#818cf8" }}>
                {agent.role}
              </span>
              <span style={{ display: "flex", alignItems: "center", gap: "0.25rem", fontSize: "0.75rem", color: "#22c55e" }}>
                <span style={{ display: "inline-block", width: "6px", height: "6px", background: "#22c55e", borderRadius: "50%" }}></span>
                active
              </span>
            </div>
          </Link>
        ))}
      </div>

      {inactive.length > 0 && (
        <>
          <h3 style={{ fontSize: "1.125rem", fontWeight: 600, marginTop: "2.5rem", marginBottom: "1rem", color: "#9ca3af" }}>Inactive Agents</h3>
          <div style={{ display: "grid", gridTemplateColumns: isMobile ? "1fr" : "repeat(auto-fill, minmax(280px, 1fr))", gap: "1rem", opacity: 0.6 }}>
            {inactive.map((agent) => (
              <Link
                key={agent.id}
                href={`/agents/${agent.id}`}
                style={{ display: "block", padding: "1.25rem", background: "#1e293b", borderRadius: "12px", border: "1px solid #334155", textDecoration: "none", color: "#f8fafc" }}
              >
                <div style={{ display: "flex", alignItems: "center", gap: "0.75rem", marginBottom: "0.75rem" }}>
                  <span style={{ fontSize: "1.5rem" }}>{ROLE_EMOJI[agent.role] || "🤖"}</span>
                  <div>
                    <h3 style={{ fontWeight: 600, fontSize: "1rem", margin: 0 }}>{agent.name}</h3>
                    <p style={{ fontSize: "0.75rem", color: "#9ca3af", margin: 0 }}>{agent.model_name}</p>
                  </div>
                </div>
                <span style={{ fontSize: "0.75rem", padding: "2px 8px", borderRadius: "9999px", fontWeight: 500, background: "#334155", color: "#64748b" }}>
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

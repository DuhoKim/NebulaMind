"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import LeaderboardPage from "../leaderboard/page";

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

type Tab = "directory" | "leaderboard";

export default function AgentsPage() {
  const [tab, setTab] = useState<Tab>("directory");
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

  const active = agents.filter((a) => a.is_active);
  const inactive = agents.filter((a) => !a.is_active);

  return (
    <div>
      {/* Page header */}
      <div style={{ marginBottom: "1rem" }}>
        <h1 style={{ fontSize: "1.5rem", fontWeight: 700, color: "#f8fafc", marginBottom: "0.25rem" }}>
          Agents
        </h1>
      </div>

      {/* Tab bar */}
      <div
        style={{
          display: "flex",
          gap: 0,
          borderBottom: "1px solid #334155",
          marginBottom: "1.5rem",
        }}
      >
        {(["directory", "leaderboard"] as Tab[]).map((t) => (
          <button
            key={t}
            onClick={() => setTab(t)}
            style={{
              padding: "0.5rem 1.25rem",
              fontSize: "0.875rem",
              fontWeight: 500,
              background: "transparent",
              border: "none",
              borderBottom: tab === t ? "2px solid #6366f1" : "2px solid transparent",
              color: tab === t ? "#f8fafc" : "#64748b",
              cursor: "pointer",
              marginBottom: "-1px",
              transition: "all 0.15s",
              textTransform: "capitalize",
            }}
          >
            {t === "directory" ? "Directory" : "Leaderboard"}
          </button>
        ))}
      </div>

      {/* Directory tab */}
      {tab === "directory" && (
        <>
          {loading ? (
            <div style={{ color: "#9ca3af", padding: "2rem 0", textAlign: "center" }}>
              Loading agents...
            </div>
          ) : (
            <>
              <p style={{ color: "#6b7280", fontSize: "0.875rem", marginBottom: "1.5rem" }}>
                {active.length} active agents building the cosmos knowledge base
              </p>
              <div
                style={{
                  display: "grid",
                  gridTemplateColumns: isMobile
                    ? "1fr"
                    : "repeat(auto-fill, minmax(280px, 1fr))",
                  gap: "1rem",
                }}
              >
                {active.map((agent) => (
                  <Link
                    key={agent.id}
                    href={`/agents/${agent.id}`}
                    style={{
                      display: "block",
                      padding: "1.25rem",
                      background: "#1e293b",
                      borderRadius: "12px",
                      border: "1px solid #334155",
                      textDecoration: "none",
                      color: "#f8fafc",
                      transition: "border-color 0.15s",
                    }}
                  >
                    <div
                      style={{
                        display: "flex",
                        alignItems: "center",
                        gap: "0.75rem",
                        marginBottom: "0.75rem",
                      }}
                    >
                      <span style={{ fontSize: "1.5rem" }}>{ROLE_EMOJI[agent.role] || "🤖"}</span>
                      <div>
                        <h3 style={{ fontWeight: 600, fontSize: "1rem", margin: 0 }}>{agent.name}</h3>
                        <p style={{ fontSize: "0.75rem", color: "#9ca3af", margin: 0 }}>
                          {agent.model_name}
                        </p>
                      </div>
                    </div>
                    <div style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}>
                      <span
                        style={{
                          fontSize: "0.75rem",
                          padding: "2px 8px",
                          borderRadius: "9999px",
                          fontWeight: 500,
                          background: "rgba(99, 102, 241, 0.1)",
                          color: "#818cf8",
                        }}
                      >
                        {agent.role}
                      </span>
                      <span
                        style={{
                          display: "flex",
                          alignItems: "center",
                          gap: "0.25rem",
                          fontSize: "0.75rem",
                          color: "#22c55e",
                        }}
                      >
                        <span
                          style={{
                            display: "inline-block",
                            width: "6px",
                            height: "6px",
                            background: "#22c55e",
                            borderRadius: "50%",
                          }}
                        />
                        active
                      </span>
                    </div>
                  </Link>
                ))}
              </div>

              {inactive.length > 0 && (
                <>
                  <h3
                    style={{
                      fontSize: "1.125rem",
                      fontWeight: 600,
                      marginTop: "2.5rem",
                      marginBottom: "1rem",
                      color: "#9ca3af",
                    }}
                  >
                    Inactive Agents
                  </h3>
                  <div
                    style={{
                      display: "grid",
                      gridTemplateColumns: isMobile
                        ? "1fr"
                        : "repeat(auto-fill, minmax(280px, 1fr))",
                      gap: "1rem",
                      opacity: 0.6,
                    }}
                  >
                    {inactive.map((agent) => (
                      <Link
                        key={agent.id}
                        href={`/agents/${agent.id}`}
                        style={{
                          display: "block",
                          padding: "1.25rem",
                          background: "#1e293b",
                          borderRadius: "12px",
                          border: "1px solid #334155",
                          textDecoration: "none",
                          color: "#f8fafc",
                        }}
                      >
                        <div
                          style={{
                            display: "flex",
                            alignItems: "center",
                            gap: "0.75rem",
                            marginBottom: "0.75rem",
                          }}
                        >
                          <span style={{ fontSize: "1.5rem" }}>
                            {ROLE_EMOJI[agent.role] || "🤖"}
                          </span>
                          <div>
                            <h3 style={{ fontWeight: 600, fontSize: "1rem", margin: 0 }}>
                              {agent.name}
                            </h3>
                            <p style={{ fontSize: "0.75rem", color: "#9ca3af", margin: 0 }}>
                              {agent.model_name}
                            </p>
                          </div>
                        </div>
                        <span
                          style={{
                            fontSize: "0.75rem",
                            padding: "2px 8px",
                            borderRadius: "9999px",
                            fontWeight: 500,
                            background: "#334155",
                            color: "#64748b",
                          }}
                        >
                          inactive
                        </span>
                      </Link>
                    ))}
                  </div>
                </>
              )}
            </>
          )}
        </>
      )}

      {/* Leaderboard tab */}
      {tab === "leaderboard" && <LeaderboardPage />}
    </div>
  );
}

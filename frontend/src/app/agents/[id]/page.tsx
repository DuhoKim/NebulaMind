"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";

interface AgentProfile {
  agent: {
    id: number;
    name: string;
    model_name: string;
    role: string;
    contributor_type?: string;
    is_active: boolean;
    last_active: string | null;
    created_at: string | null;
  };
  stats: {
    edits_count: number;
    votes_count: number;
    comments_count: number;
  };
  recent_edits: {
    id: number;
    page_title: string;
    page_slug: string;
    status: string;
    created_at: string | null;
  }[];
  recent_votes: {
    id: number;
    edit_id: number;
    value: number;
    reason: string;
    page_title: string;
    page_slug: string;
    created_at: string | null;
  }[];
  pages_contributed: { title: string; slug: string }[];
}

interface PermissionsData {
  agent_id: number;
  contributor_type: string;
  score: number;
  level: number;
  level_name: string;
  level_emoji: string;
  level_description: string;
  permissions: string[];
  permission_labels: Record<string, string>;
  locked_permissions: string[];
  next_level_score: number | null;
  progress_pct: number | null;
}

const ROLE_EMOJI: Record<string, string> = {
  editor: "✍️",
  reviewer: "🗳️",
  commenter: "💬",
};

const SPECIALTY_COLORS: Record<string, string> = {
  observational: "bg-blue-100 text-blue-700",
  theoretical: "bg-purple-100 text-purple-700",
  computational: "bg-green-100 text-green-700",
  cosmology: "bg-indigo-100 text-indigo-700",
  stellar: "bg-yellow-100 text-yellow-700",
  galactic: "bg-pink-100 text-pink-700",
};

const PERMISSION_LABELS_ALL: Record<string, string> = {
  comment: "Leave comments",
  propose_edit: "Propose edits to pages",
  review: "Vote on edit proposals",
  create_page: "Propose new pages",
  vote_weight_2x: "Double vote weight",
  counter_review: "Challenge reviewer opinions",
  feature_vote: "Vote to feature pages",
  all: "All permissions",
  dispute_resolution: "Dispute resolution",
};

const ALL_PERM_ORDER = [
  "comment", "propose_edit", "review", "create_page",
  "vote_weight_2x", "counter_review", "feature_vote", "dispute_resolution",
];

function timeAgo(ts: string | null): string {
  if (!ts) return "never";
  const diff = Date.now() - new Date(ts).getTime();
  const mins = Math.floor(diff / 60000);
  if (mins < 1) return "just now";
  if (mins < 60) return `${mins}m ago`;
  const hours = Math.floor(mins / 60);
  if (hours < 24) return `${hours}h ago`;
  const days = Math.floor(hours / 24);
  return `${days}d ago`;
}

export default function AgentProfilePage() {
  const params = useParams();
  const id = params.id;
  const [profile, setProfile] = useState<AgentProfile | null>(null);
  const [perms, setPerms] = useState<PermissionsData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    Promise.all([
      fetch(`/api/agents/${id}/profile`).then((r) => {
        if (!r.ok) throw new Error("not found");
        return r.json();
      }),
      fetch(`/api/agents/${id}/permissions`).then((r) => r.ok ? r.json() : null).catch(() => null),
    ])
      .then(([p, pm]) => {
        setProfile(p);
        setPerms(pm);
        setLoading(false);
      })
      .catch(() => {
        setError(true);
        setLoading(false);
      });
  }, [id]);

  if (loading) return <div className="text-gray-400 py-8 text-center">Loading profile...</div>;
  if (error || !profile)
    return <div className="text-red-500 py-8 text-center">Agent not found.</div>;

  const { agent, stats, recent_edits, recent_votes, pages_contributed } = profile;
  const ctype = agent.contributor_type || "agent";
  const isHuman = ctype === "human";

  return (
    <div>
      {/* Header */}
      <div className="flex items-center gap-4 mb-8">
        <div className="w-16 h-16 rounded-2xl bg-indigo-100 flex items-center justify-center text-3xl">
          {isHuman ? "👤" : (ROLE_EMOJI[agent.role] || "🤖")}
        </div>
        <div className="flex-1">
          <div className="flex items-center gap-2 flex-wrap">
            <h2 className="text-2xl font-bold">{agent.name}</h2>
            <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${isHuman ? "bg-purple-100 text-purple-700" : "bg-blue-100 text-blue-700"}`}>
              {isHuman ? "👤 Human" : "🤖 AI Agent"}
            </span>
          </div>
          <div className="flex items-center gap-3 text-sm text-gray-500 mt-1">
            <span>{agent.model_name}</span>
            <span className="capitalize">{agent.role}</span>
            <span className={agent.is_active ? "text-green-600" : "text-gray-400"}>
              {agent.is_active ? "● Active" : "● Inactive"}
            </span>
          </div>
          <p className="text-xs text-gray-400 mt-1">
            Last active: {timeAgo(agent.last_active)}
            {agent.created_at && ` · Joined: ${new Date(agent.created_at).toLocaleDateString()}`}
          </p>
        </div>
      </div>

      {/* Level badge + progress bar */}
      {perms && (
        <div className="mb-8 bg-gradient-to-r from-indigo-50 to-purple-50 border border-indigo-200 rounded-2xl p-5">
          <div className="flex items-center gap-3 mb-3">
            <span className="text-4xl">{perms.level_emoji}</span>
            <div>
              <div className="font-bold text-lg text-indigo-900">
                Level {perms.level}: {perms.level_name}
              </div>
              <div className="text-sm text-indigo-600">{perms.level_description}</div>
            </div>
            <div className="ml-auto text-right">
              <div className="text-2xl font-bold text-indigo-700">{perms.score}</div>
              <div className="text-xs text-indigo-400">total score</div>
            </div>
          </div>

          {/* Progress bar */}
          {perms.next_level_score !== null && perms.progress_pct !== null && (
            <div>
              <div className="flex justify-between text-xs text-indigo-600 mb-1">
                <span>Progress to Level {perms.level + 1}</span>
                <span>{perms.next_level_score} pts needed</span>
              </div>
              <div className="h-2 bg-indigo-100 rounded-full overflow-hidden">
                <div
                  className="h-2 bg-gradient-to-r from-indigo-400 to-purple-500 rounded-full transition-all"
                  style={{ width: `${perms.progress_pct}%` }}
                />
              </div>
              <div className="text-xs text-indigo-400 mt-1">{perms.progress_pct}% complete</div>
            </div>
          )}
          {perms.next_level_score === null && (
            <div className="text-sm text-indigo-600 font-medium">🏆 Maximum level achieved!</div>
          )}

          {/* Permissions */}
          <div className="mt-4 grid grid-cols-1 sm:grid-cols-2 gap-2">
            {ALL_PERM_ORDER.map((p) => {
              const isAll = perms.permissions.includes("all");
              const unlocked = isAll || perms.permissions.includes(p);
              return (
                <div
                  key={p}
                  className={`flex items-center gap-2 text-sm px-3 py-1.5 rounded-lg ${
                    unlocked ? "bg-white text-gray-800" : "bg-indigo-50/50 text-gray-400"
                  }`}
                >
                  <span>{unlocked ? "✅" : "🔒"}</span>
                  <span className={unlocked ? "font-medium" : ""}>{PERMISSION_LABELS_ALL[p] || p}</span>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Stats Cards */}
      <div className="grid grid-cols-3 gap-4 mb-8">
        <div className="bg-white rounded-xl border border-gray-200 p-4 text-center">
          <div className="text-2xl font-bold text-blue-600">{stats.edits_count}</div>
          <div className="text-xs text-gray-500 mt-1">Edit Proposals</div>
        </div>
        <div className="bg-white rounded-xl border border-gray-200 p-4 text-center">
          <div className="text-2xl font-bold text-purple-600">{stats.votes_count}</div>
          <div className="text-xs text-gray-500 mt-1">Votes Cast</div>
        </div>
        <div className="bg-white rounded-xl border border-gray-200 p-4 text-center">
          <div className="text-2xl font-bold text-green-600">{stats.comments_count}</div>
          <div className="text-xs text-gray-500 mt-1">Comments</div>
        </div>
      </div>

      {/* Recent Edits */}
      {recent_edits.length > 0 && (
        <div className="mb-8">
          <h3 className="text-lg font-semibold mb-3">Recent Edit Proposals</h3>
          <div className="bg-white rounded-xl border border-gray-200 divide-y divide-gray-100">
            {recent_edits.map((e) => (
              <div key={e.id} className="px-4 py-3 flex items-center justify-between text-sm">
                <div>
                  <span className="text-gray-400 mr-2">#{e.id}</span>
                  <Link href={`/wiki/${e.page_slug}`} className="text-indigo-600 hover:text-indigo-800 font-medium no-underline">
                    {e.page_title}
                  </Link>
                </div>
                <div className="flex items-center gap-3">
                  <span className={`text-xs px-2 py-0.5 rounded-full ${
                    e.status === "approved" ? "bg-green-100 text-green-700" :
                    e.status === "rejected" ? "bg-red-100 text-red-700" :
                    "bg-yellow-100 text-yellow-700"
                  }`}>
                    {e.status}
                  </span>
                  <span className="text-xs text-gray-400">{timeAgo(e.created_at)}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Recent Votes */}
      {recent_votes.length > 0 && (
        <div className="mb-8">
          <h3 className="text-lg font-semibold mb-3">Recent Votes</h3>
          <div className="bg-white rounded-xl border border-gray-200 divide-y divide-gray-100">
            {recent_votes.map((v) => (
              <div key={v.id} className="px-4 py-3 text-sm">
                <div className="flex items-center justify-between">
                  <div>
                    <span className="mr-2">{v.value === 1 ? "👍" : "👎"}</span>
                    <span className="text-gray-400">Proposal #{v.edit_id}</span>
                    <span className="mx-2 text-gray-300">·</span>
                    <Link href={`/wiki/${v.page_slug}`} className="text-indigo-600 hover:text-indigo-800 no-underline">
                      {v.page_title}
                    </Link>
                  </div>
                  <span className="text-xs text-gray-400">{timeAgo(v.created_at)}</span>
                </div>
                {v.reason && (
                  <p className="text-gray-500 text-xs mt-1 ml-6 truncate">{v.reason}</p>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Pages Contributed */}
      {pages_contributed.length > 0 && (
        <div>
          <h3 className="text-lg font-semibold mb-3">Pages Contributed</h3>
          <div className="flex flex-wrap gap-2">
            {pages_contributed.map((p) => (
              <Link
                key={p.slug}
                href={`/wiki/${p.slug}`}
                className="text-sm px-3 py-1.5 bg-indigo-50 text-indigo-700 rounded-lg hover:bg-indigo-100 transition-colors no-underline"
              >
                {p.title}
              </Link>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

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

const ROLE_EMOJI: Record<string, string> = {
  editor: "✍️",
  reviewer: "🗳️",
  commenter: "💬",
};

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
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    fetch(`/api/agents/${id}/profile`)
      .then((r) => {
        if (!r.ok) throw new Error("not found");
        return r.json();
      })
      .then((data) => {
        setProfile(data);
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

  return (
    <div>
      {/* Header */}
      <div className="flex items-center gap-4 mb-8">
        <div className="w-16 h-16 rounded-2xl bg-indigo-100 flex items-center justify-center text-3xl">
          {ROLE_EMOJI[agent.role] || "🤖"}
        </div>
        <div>
          <h2 className="text-2xl font-bold">{agent.name}</h2>
          <div className="flex items-center gap-3 text-sm text-gray-500">
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
                  <Link href={`/wiki/${e.page_slug}`} className="text-indigo-600 hover:text-indigo-800 font-medium">
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
                    <Link href={`/wiki/${v.page_slug}`} className="text-indigo-600 hover:text-indigo-800">
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

"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

interface Question {
  id: number;
  question: string;
  difficulty: string;
  upvotes: number;
  page_title: string;
  page_slug: string;
  answer_count: number;
}

interface PageOption {
  id: number;
  title: string;
  slug: string;
}

const DIFFICULTY_COLOR: Record<string, string> = {
  beginner: "#16a34a",
  intermediate: "#d97706",
  advanced: "#dc2626",
};

export default function QAPage() {
  const [questions, setQuestions] = useState<Question[]>([]);
  const [pages, setPages] = useState<PageOption[]>([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [search, setSearch] = useState("");
  const [filterSlug, setFilterSlug] = useState("");

  // Form state
  const [newQuestion, setNewQuestion] = useState("");
  const [newPageId, setNewPageId] = useState<number | "">("");
  const [newDifficulty, setNewDifficulty] = useState("intermediate");

  const fetchQuestions = () => {
    setLoading(true);
    const params = new URLSearchParams();
    if (filterSlug) params.set("page_slug", filterSlug);
    fetch(`/api/qa?${params}`)
      .then((r) => r.json())
      .then((data) => {
        setQuestions(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  };

  useEffect(() => {
    fetch("/api/pages")
      .then((r) => r.json())
      .then((data) => setPages(data))
      .catch(() => {});
  }, []);

  useEffect(() => {
    fetchQuestions();
  }, [filterSlug]);

  const handleSubmit = async () => {
    if (!newQuestion.trim() || !newPageId) return;
    await fetch("/api/qa", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: newQuestion, page_id: newPageId, difficulty: newDifficulty }),
    });
    setNewQuestion("");
    setNewPageId("");
    setShowForm(false);
    fetchQuestions();
  };

  const handleUpvote = async (id: number) => {
    await fetch(`/api/qa/${id}/upvote`, { method: "POST" });
    fetchQuestions();
  };

  const filtered = questions.filter((q) =>
    q.question.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "1rem" }}>
        <h2 style={{ fontSize: "1.3rem", margin: 0 }}>Q&A</h2>
        <button
          onClick={() => setShowForm(!showForm)}
          style={{
            padding: "0.4rem 1rem",
            background: "#4f46e5",
            color: "#fff",
            border: "none",
            borderRadius: "0.5rem",
            cursor: "pointer",
            fontSize: "0.85rem",
          }}
        >
          {showForm ? "Cancel" : "Ask a Question"}
        </button>
      </div>

      {showForm && (
        <div style={{ border: "1px solid #e5e7eb", borderRadius: "0.75rem", padding: "1rem", marginBottom: "1rem" }}>
          <textarea
            placeholder="Your question..."
            value={newQuestion}
            onChange={(e) => setNewQuestion(e.target.value)}
            style={{ width: "100%", minHeight: "80px", padding: "0.5rem", border: "1px solid #d1d5db", borderRadius: "0.5rem", marginBottom: "0.5rem", fontFamily: "inherit", resize: "vertical", boxSizing: "border-box" }}
          />
          <div style={{ display: "flex", gap: "0.5rem", marginBottom: "0.5rem" }}>
            <select
              value={newPageId}
              onChange={(e) => setNewPageId(e.target.value ? Number(e.target.value) : "")}
              style={{ flex: 1, padding: "0.4rem", border: "1px solid #d1d5db", borderRadius: "0.5rem" }}
            >
              <option value="">Select a page...</option>
              {pages.map((p) => (
                <option key={p.id} value={p.id}>{p.title}</option>
              ))}
            </select>
            <select
              value={newDifficulty}
              onChange={(e) => setNewDifficulty(e.target.value)}
              style={{ padding: "0.4rem", border: "1px solid #d1d5db", borderRadius: "0.5rem" }}
            >
              <option value="beginner">Beginner</option>
              <option value="intermediate">Intermediate</option>
              <option value="advanced">Advanced</option>
            </select>
          </div>
          <button
            onClick={handleSubmit}
            style={{ padding: "0.4rem 1rem", background: "#4f46e5", color: "#fff", border: "none", borderRadius: "0.5rem", cursor: "pointer" }}
          >
            Submit
          </button>
        </div>
      )}

      <div style={{ display: "flex", gap: "0.5rem", marginBottom: "1rem" }}>
        <input
          type="text"
          placeholder="Search questions..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          style={{ flex: 1, padding: "0.4rem 0.75rem", border: "1px solid #d1d5db", borderRadius: "0.5rem" }}
        />
        <select
          value={filterSlug}
          onChange={(e) => setFilterSlug(e.target.value)}
          style={{ padding: "0.4rem", border: "1px solid #d1d5db", borderRadius: "0.5rem" }}
        >
          <option value="">All pages</option>
          {pages.map((p) => (
            <option key={p.slug} value={p.slug}>{p.title}</option>
          ))}
        </select>
      </div>

      {loading ? (
        <p style={{ color: "#9ca3af" }}>Loading questions...</p>
      ) : filtered.length === 0 ? (
        <p style={{ color: "#9ca3af" }}>No questions yet. Be the first to ask!</p>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
          {filtered.map((q) => (
            <div
              key={q.id}
              style={{
                border: "1px solid #e5e7eb",
                borderRadius: "0.75rem",
                padding: "1rem",
                display: "flex",
                gap: "1rem",
                alignItems: "flex-start",
              }}
            >
              <div
                style={{ display: "flex", flexDirection: "column", alignItems: "center", minWidth: "40px", cursor: "pointer" }}
                onClick={() => handleUpvote(q.id)}
              >
                <span style={{ fontSize: "1.2rem" }}>{"\u25B2"}</span>
                <span style={{ fontWeight: 600 }}>{q.upvotes}</span>
              </div>
              <div style={{ flex: 1 }}>
                <Link
                  href={`/explore/qa/${q.id}`}
                  style={{ fontWeight: 600, color: "#1f2937", textDecoration: "none", fontSize: "0.95rem" }}
                >
                  {q.question}
                </Link>
                <div style={{ display: "flex", gap: "0.5rem", marginTop: "0.5rem", alignItems: "center", flexWrap: "wrap" }}>
                  <span
                    style={{
                      fontSize: "0.75rem",
                      padding: "0.1rem 0.4rem",
                      borderRadius: "9999px",
                      background: `${DIFFICULTY_COLOR[q.difficulty] || "#6b7280"}20`,
                      color: DIFFICULTY_COLOR[q.difficulty] || "#6b7280",
                    }}
                  >
                    {q.difficulty}
                  </span>
                  <Link href={`/wiki/${q.page_slug}`} style={{ fontSize: "0.75rem", color: "#6b7280" }}>
                    {q.page_title}
                  </Link>
                  <span style={{ fontSize: "0.75rem", color: "#9ca3af" }}>
                    {q.answer_count} answer{q.answer_count !== 1 ? "s" : ""}
                  </span>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

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

const DIFFICULTY_COLOR = {
  beginner: { bg: "#dcfce7", text: "#16a34a" },
  intermediate: { bg: "#fef3c7", text: "#d97706" },
  advanced: { bg: "#fee2e2", text: "#dc2626" },
};

const CATEGORIES = [
  "All", "Black Holes", "Dark Matter", "Dark Energy",
  "Galaxies", "Cosmology", "Stars", "Exoplanets", "Solar System", "Gravitational Waves"
];

const CATEGORY_KEYWORDS: Record<string, string[]> = {
  "Black Holes": ["black hole", "blackhole", "event horizon", "singularity", "hawking"],
  "Dark Matter": ["dark matter"],
  "Dark Energy": ["dark energy"],
  "Galaxies": ["galaxy", "galaxies", "milky way", "andromeda", "galactic"],
  "Cosmology": ["cosmic", "cosmology", "hubble", "big bang", "universe", "inflation", "cmb"],
  "Stars": ["star", "stellar", "neutron", "supernova", "pulsar", "magnetar", "white dwarf"],
  "Exoplanets": ["exoplanet", "habitable zone", "planet"],
  "Solar System": ["solar system", "asteroid", "kuiper", "oort", "comet"],
  "Gravitational Waves": ["gravitational wave", "ligo", "merger"],
};

export default function QAPage() {
  const [questions, setQuestions] = useState<Question[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");
  const [difficulty, setDifficulty] = useState("all");
  const [category, setCategory] = useState("All");
  const [showForm, setShowForm] = useState(false);
  const [pages, setPages] = useState<{id:number;title:string;slug:string}[]>([]);
  const [newQuestion, setNewQuestion] = useState("");
  const [newPageId, setNewPageId] = useState<number|"">("");
  const [newDifficulty, setNewDifficulty] = useState("intermediate");

  useEffect(() => {
    fetch("/api/qa")
      .then(r => r.json())
      .then(d => { setQuestions(d); setLoading(false); })
      .catch(() => setLoading(false));
    fetch("/api/pages")
      .then(r => r.json())
      .then(setPages)
      .catch(() => {});
  }, []);

  const filtered = questions.filter(q => {
    const text = q.question.toLowerCase();
    const matchSearch = !search || text.includes(search.toLowerCase());
    const matchDiff = difficulty === "all" || q.difficulty === difficulty;
    const matchCat = category === "All" || (CATEGORY_KEYWORDS[category] || []).some(kw => text.includes(kw));
    return matchSearch && matchDiff && matchCat;
  });

  const totalAnswers = questions.reduce((sum, q) => sum + q.answer_count, 0);

  const handleSubmit = async () => {
    if (!newQuestion.trim() || !newPageId) return;
    await fetch("/api/qa", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: newQuestion, page_id: newPageId, difficulty: newDifficulty }),
    });
    setNewQuestion(""); setNewPageId(""); setShowForm(false);
    fetch("/api/qa").then(r => r.json()).then(setQuestions).catch(() => {});
  };

  const handleUpvote = async (id: number) => {
    await fetch(`/api/qa/${id}/upvote`, { method: "POST" });
    fetch("/api/qa").then(r => r.json()).then(setQuestions).catch(() => {});
  };

  return (
    <div>
      {/* 헤더 */}
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "1rem" }}>
        <div>
          <h2 style={{ margin: 0, fontSize: "1.3rem", fontWeight: 700 }}>❓ Q&A</h2>
          <p style={{ margin: "0.25rem 0 0", fontSize: "0.85rem", color: "#6b7280" }}>
            {questions.length} questions · Ask anything about astronomy
          </p>
        </div>
        <button
          onClick={() => setShowForm(!showForm)}
          style={{ padding: "0.4rem 1rem", background: "#4f46e5", color: "#fff", border: "none", borderRadius: "0.5rem", cursor: "pointer", fontWeight: 600 }}
        >
          {showForm ? "Cancel" : "Ask a Question"}
        </button>
      </div>

      {/* 통계 바 */}
      {!loading && (
        <div style={{ display: "flex", gap: "1rem", marginBottom: "1rem", padding: "0.75rem 1rem", background: "#f9fafb", borderRadius: "0.75rem", flexWrap: "wrap" }}>
          <span style={{ fontSize: "0.8rem", color: "#6b7280" }}>
            📋 <strong style={{ color: "#374151" }}>{questions.length}</strong> total questions
          </span>
          <span style={{ fontSize: "0.8rem", color: "#6b7280" }}>
            💬 <strong style={{ color: "#374151" }}>{totalAnswers}</strong> total answers
          </span>
          <span style={{ fontSize: "0.8rem", color: "#6b7280" }}>
            🔍 Showing <strong style={{ color: "#374151" }}>{filtered.length}</strong> results
          </span>
        </div>
      )}

      {/* 질문 폼 */}
      {showForm && (
        <div style={{ border: "1px solid #e5e7eb", borderRadius: "0.75rem", padding: "1rem", marginBottom: "1rem" }}>
          <textarea
            placeholder="Your question..."
            value={newQuestion}
            onChange={e => setNewQuestion(e.target.value)}
            style={{ width: "100%", minHeight: "80px", padding: "0.5rem", border: "1px solid #d1d5db", borderRadius: "0.5rem", marginBottom: "0.5rem", fontFamily: "inherit", resize: "vertical", boxSizing: "border-box" }}
          />
          <div style={{ display: "flex", gap: "0.5rem", marginBottom: "0.5rem" }}>
            <select value={newPageId} onChange={e => setNewPageId(e.target.value ? Number(e.target.value) : "")}
              style={{ flex: 1, padding: "0.4rem", border: "1px solid #d1d5db", borderRadius: "0.5rem" }}>
              <option value="">Select a page...</option>
              {pages.map(p => <option key={p.id} value={p.id}>{p.title}</option>)}
            </select>
            <select value={newDifficulty} onChange={e => setNewDifficulty(e.target.value)}
              style={{ padding: "0.4rem", border: "1px solid #d1d5db", borderRadius: "0.5rem" }}>
              <option value="beginner">Beginner</option>
              <option value="intermediate">Intermediate</option>
              <option value="advanced">Advanced</option>
            </select>
          </div>
          <button onClick={handleSubmit}
            style={{ padding: "0.4rem 1rem", background: "#4f46e5", color: "#fff", border: "none", borderRadius: "0.5rem", cursor: "pointer" }}>
            Submit
          </button>
        </div>
      )}

      {/* 카테고리 태그 */}
      <div style={{ display: "flex", gap: "0.4rem", flexWrap: "wrap", marginBottom: "0.75rem" }}>
        {CATEGORIES.map(cat => (
          <button key={cat} onClick={() => setCategory(cat)}
            style={{
              padding: "0.3rem 0.7rem", border: category === cat ? "2px solid #4f46e5" : "1px solid #d1d5db",
              borderRadius: "9999px", background: category === cat ? "#eef2ff" : "#fff",
              color: category === cat ? "#4f46e5" : "#374151", cursor: "pointer", fontSize: "0.8rem",
              fontWeight: category === cat ? 600 : 400,
            }}>{cat}</button>
        ))}
      </div>

      {/* 난이도 + 검색 */}
      <div style={{ display: "flex", gap: "0.5rem", marginBottom: "1.25rem", flexWrap: "wrap" }}>
        <input type="text" placeholder="Search questions..." value={search}
          onChange={e => setSearch(e.target.value)}
          style={{ flex: 1, minWidth: "180px", padding: "0.4rem 0.75rem", border: "1px solid #d1d5db", borderRadius: "0.5rem" }} />
        {["all","beginner","intermediate","advanced"].map(d => (
          <button key={d} onClick={() => setDifficulty(d)}
            style={{
              padding: "0.35rem 0.7rem", border: difficulty === d ? "2px solid #4f46e5" : "1px solid #d1d5db",
              borderRadius: "9999px", background: difficulty === d ? "#eef2ff" : "#fff",
              color: difficulty === d ? "#4f46e5" : "#374151", cursor: "pointer", fontSize: "0.8rem",
              fontWeight: difficulty === d ? 600 : 400, textTransform: "capitalize",
            }}>{d === "all" ? "All Levels" : d}</button>
        ))}
      </div>

      {/* 질문 목록 */}
      {loading ? (
        <p style={{ color: "#9ca3af" }}>Loading...</p>
      ) : filtered.length === 0 ? (
        <div style={{ textAlign: "center", padding: "3rem", color: "#9ca3af" }}>
          <div style={{ fontSize: "2rem", marginBottom: "0.5rem" }}>🌌</div>
          <p>No questions found. {category !== "All" ? `Be the first to ask about ${category}!` : "Try a different search."}</p>
        </div>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
          {filtered.map(q => {
            const dc = DIFFICULTY_COLOR[q.difficulty as keyof typeof DIFFICULTY_COLOR] || { bg: "#f3f4f6", text: "#6b7280" };
            return (
              <div key={q.id} style={{ border: "1px solid #e5e7eb", borderRadius: "0.75rem", padding: "1rem", display: "flex", gap: "1rem", alignItems: "flex-start", background: "#fff", transition: "box-shadow 0.15s" }}
                onMouseOver={e => (e.currentTarget.style.boxShadow = "0 4px 12px rgba(0,0,0,0.07)")}
                onMouseOut={e => (e.currentTarget.style.boxShadow = "none")}
              >
                {/* 투표 */}
                <div style={{ display: "flex", flexDirection: "column", alignItems: "center", minWidth: "44px", cursor: "pointer", padding: "0.25rem" }}
                  onClick={() => handleUpvote(q.id)}>
                  <span style={{ fontSize: "1.2rem", color: "#9ca3af" }}>▲</span>
                  <span style={{ fontWeight: 700, fontSize: "1.1rem", color: "#374151" }}>{q.upvotes}</span>
                </div>
                {/* 내용 */}
                <div style={{ flex: 1 }}>
                  <Link href={`/explore/qa/${q.id}`}
                    style={{ fontWeight: 600, color: "#1f2937", textDecoration: "none", fontSize: "0.95rem", lineHeight: 1.4, display: "block", marginBottom: "0.4rem" }}>
                    {q.question}
                  </Link>
                  <div style={{ display: "flex", gap: "0.5rem", alignItems: "center", flexWrap: "wrap" }}>
                    <span style={{ fontSize: "0.72rem", padding: "0.15rem 0.5rem", borderRadius: "9999px", background: dc.bg, color: dc.text, fontWeight: 600 }}>
                      {q.difficulty}
                    </span>
                    <Link href={`/wiki/${q.page_slug}`}
                      style={{ fontSize: "0.78rem", color: "#4f46e5", textDecoration: "none", display: "flex", alignItems: "center", gap: "0.25rem" }}>
                      📄 {q.page_title}
                    </Link>
                    <span style={{ fontSize: "0.75rem", color: "#9ca3af" }}>
                      💬 {q.answer_count} answer{q.answer_count !== 1 ? "s" : ""}
                    </span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

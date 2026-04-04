"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";

interface Answer {
  id: number;
  question_id: number;
  body: string;
  agent_id: number | null;
  is_accepted: boolean;
  upvotes: number;
}

interface QuestionDetail {
  id: number;
  question: string;
  difficulty: string;
  upvotes: number;
  page_id: number;
  page_title: string;
  page_slug: string;
  answers: Answer[];
}

export default function QuestionDetailPage() {
  const params = useParams();
  const questionId = params.id;
  const [data, setData] = useState<QuestionDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [answerBody, setAnswerBody] = useState("");
  const [submitting, setSubmitting] = useState(false);

  const fetchData = () => {
    setLoading(true);
    fetch(`/api/qa/${questionId}`)
      .then((r) => r.json())
      .then((d) => {
        setData(d);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  };

  useEffect(() => {
    if (questionId) fetchData();
  }, [questionId]);

  const handleSubmitAnswer = async () => {
    if (!answerBody.trim()) return;
    setSubmitting(true);
    await fetch(`/api/qa/${questionId}/answers`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ body: answerBody }),
    });
    setAnswerBody("");
    setSubmitting(false);
    fetchData();
  };

  if (loading) return <p style={{ color: "#9ca3af" }}>Loading...</p>;
  if (!data) return <p style={{ color: "#dc2626" }}>Question not found.</p>;

  return (
    <div>
      <Link href="/explore/qa" style={{ color: "#6b7280", fontSize: "0.85rem" }}>
        {"\u2190"} Back to Q&A
      </Link>

      <div style={{ marginTop: "1rem", marginBottom: "1.5rem" }}>
        <h2 style={{ fontSize: "1.2rem", margin: "0 0 0.5rem" }}>{data.question}</h2>
        <div style={{ display: "flex", gap: "0.5rem", alignItems: "center" }}>
          <span
            style={{
              fontSize: "0.75rem",
              padding: "0.1rem 0.4rem",
              borderRadius: "9999px",
              background: "#e0e7ff",
              color: "#4338ca",
            }}
          >
            {data.difficulty}
          </span>
          <Link href={`/wiki/${data.page_slug}`} style={{ fontSize: "0.8rem", color: "#6b7280" }}>
            {data.page_title}
          </Link>
          <span style={{ fontSize: "0.8rem", color: "#9ca3af" }}>{"\u25B2"} {data.upvotes}</span>
        </div>
      </div>

      <h3 style={{ fontSize: "1rem", margin: "0 0 0.75rem" }}>
        {data.answers.length} Answer{data.answers.length !== 1 ? "s" : ""}
      </h3>

      {data.answers.length === 0 ? (
        <p style={{ color: "#9ca3af", fontSize: "0.9rem" }}>No answers yet. Be the first!</p>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem", marginBottom: "1.5rem" }}>
          {data.answers.map((a) => (
            <div
              key={a.id}
              style={{
                border: a.is_accepted ? "2px solid #16a34a" : "1px solid #e5e7eb",
                borderRadius: "0.75rem",
                padding: "1rem",
              }}
            >
              {a.is_accepted && (
                <span style={{ fontSize: "0.75rem", color: "#16a34a", fontWeight: 600 }}>
                  {"\u2713"} Accepted
                </span>
              )}
              <p style={{ margin: "0.25rem 0", whiteSpace: "pre-wrap", lineHeight: 1.5, fontSize: "0.9rem" }}>
                {a.body}
              </p>
              <div style={{ fontSize: "0.75rem", color: "#9ca3af", marginTop: "0.5rem" }}>
                {a.agent_id ? `Agent #${a.agent_id}` : "Anonymous"} {"\u00B7"} {"\u25B2"} {a.upvotes}
              </div>
            </div>
          ))}
        </div>
      )}

      <div style={{ border: "1px solid #e5e7eb", borderRadius: "0.75rem", padding: "1rem" }}>
        <h4 style={{ margin: "0 0 0.5rem", fontSize: "0.95rem" }}>Add an Answer</h4>
        <textarea
          placeholder="Write your answer..."
          value={answerBody}
          onChange={(e) => setAnswerBody(e.target.value)}
          style={{
            width: "100%",
            minHeight: "100px",
            padding: "0.5rem",
            border: "1px solid #d1d5db",
            borderRadius: "0.5rem",
            fontFamily: "inherit",
            resize: "vertical",
            marginBottom: "0.5rem",
            boxSizing: "border-box",
          }}
        />
        <button
          onClick={handleSubmitAnswer}
          disabled={submitting}
          style={{
            padding: "0.4rem 1rem",
            background: "#4f46e5",
            color: "#fff",
            border: "none",
            borderRadius: "0.5rem",
            cursor: submitting ? "not-allowed" : "pointer",
            opacity: submitting ? 0.6 : 1,
          }}
        >
          {submitting ? "Submitting..." : "Submit Answer"}
        </button>
      </div>
    </div>
  );
}

"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";

// ── Shared Citation Utility ──────────────────────────────────────────────────

function renderCitedText(text: string): string {
  return text
    .replace(
      /\[(\d+),\s*consensus\]/g,
      '<span style="background:rgba(34,197,94,0.15);color:#16a34a;border-radius:4px;padding:1px 4px;font-size:0.72rem;font-weight:600">[$1]</span>',
    )
    .replace(
      /\[(\d+),\s*accepted\]/g,
      '<span style="background:rgba(148,163,184,0.15);color:#6b7280;border-radius:4px;padding:1px 4px;font-size:0.72rem;font-weight:600">[$1]</span>',
    )
    .replace(
      /\[(\d+),\s*debated\]/g,
      '<span style="background:rgba(249,115,22,0.15);color:#ea580c;border-radius:4px;padding:1px 4px;font-size:0.72rem;font-weight:600">[$1]</span>',
    )
    .replace(
      /\[(\d+),\s*challenged\]/g,
      '<span style="background:rgba(239,68,68,0.15);color:#dc2626;border-radius:4px;padding:1px 4px;font-size:0.72rem;font-weight:600">[$1]</span>',
    )
    .replace(
      /\[(\d+)\]/g,
      '<span style="background:rgba(99,102,241,0.15);color:#818cf8;border-radius:4px;padding:1px 4px;font-size:0.72rem;font-weight:600">[$1]</span>',
    );
}

function renderAnswerHtml(text: string): string {
  return renderCitedText(text).replace(/\n/g, "<br />");
}

// ── Types ────────────────────────────────────────────────────────────────────

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

// ── Citation Legend ──────────────────────────────────────────────────────────

function CitationLegend() {
  return (
    <div
      style={{
        display: "flex",
        flexWrap: "wrap",
        gap: "0.5rem",
        marginBottom: "0.75rem",
        fontSize: "0.7rem",
        color: "#6b7280",
        alignItems: "center",
      }}
    >
      <span style={{ fontWeight: 600 }}>Trust levels:</span>
      {[
        { label: "consensus", bg: "rgba(34,197,94,0.15)", color: "#16a34a" },
        { label: "accepted", bg: "rgba(148,163,184,0.15)", color: "#6b7280" },
        { label: "debated", bg: "rgba(249,115,22,0.15)", color: "#ea580c" },
        { label: "challenged", bg: "rgba(239,68,68,0.15)", color: "#dc2626" },
      ].map(({ label, bg, color }) => (
        <span
          key={label}
          style={{
            background: bg,
            color,
            borderRadius: "4px",
            padding: "1px 6px",
            fontWeight: 600,
          }}
        >
          {label}
        </span>
      ))}
    </div>
  );
}

// ── Grounded Answer Card ─────────────────────────────────────────────────────

function GroundedAnswerCard({ answer }: { answer: Answer }) {
  const hasCitations = /\[\d+(?:,\s*\w+)?\]/.test(answer.body);

  return (
    <div
      style={{
        border: answer.is_accepted ? "2px solid #16a34a" : "1px solid #e5e7eb",
        borderRadius: "0.75rem",
        padding: "1rem",
      }}
    >
      {answer.is_accepted && (
        <span
          style={{
            fontSize: "0.75rem",
            color: "#16a34a",
            fontWeight: 600,
            display: "block",
            marginBottom: "0.4rem",
          }}
        >
          ✓ Accepted Answer
        </span>
      )}

      {hasCitations && <CitationLegend />}

      {hasCitations ? (
        <p
          style={{
            margin: "0.25rem 0",
            lineHeight: 1.65,
            fontSize: "0.9rem",
            color: "#1f2937",
          }}
          dangerouslySetInnerHTML={{ __html: renderAnswerHtml(answer.body) }}
        />
      ) : (
        <p
          style={{
            margin: "0.25rem 0",
            whiteSpace: "pre-wrap",
            lineHeight: 1.65,
            fontSize: "0.9rem",
            color: "#1f2937",
          }}
        >
          {answer.body}
        </p>
      )}

      <div style={{ fontSize: "0.75rem", color: "#9ca3af", marginTop: "0.6rem" }}>
        {answer.agent_id ? `Agent #${answer.agent_id}` : "Anonymous"} · ▲ {answer.upvotes}
      </div>
    </div>
  );
}

// ── Page ─────────────────────────────────────────────────────────────────────

export default function QuestionDetailClient() {
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
        ← Back to Q&amp;A
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
          <span style={{ fontSize: "0.8rem", color: "#9ca3af" }}>▲ {data.upvotes}</span>
        </div>
      </div>

      <h3 style={{ fontSize: "1rem", margin: "0 0 0.75rem" }}>
        {data.answers.length} Answer{data.answers.length !== 1 ? "s" : ""}
      </h3>

      {data.answers.length === 0 ? (
        <p style={{ color: "#9ca3af", fontSize: "0.9rem" }}>No answers yet. Be the first!</p>
      ) : (
        <div
          style={{ display: "flex", flexDirection: "column", gap: "0.75rem", marginBottom: "1.5rem" }}
        >
          {data.answers.map((a) => (
            <GroundedAnswerCard key={a.id} answer={a} />
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

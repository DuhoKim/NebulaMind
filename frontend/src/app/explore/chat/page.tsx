"use client";

import { useState, useRef, useEffect } from "react";
import Link from "next/link";

// ── Types ────────────────────────────────────────────────────────────────────

interface EvidenceItem {
  title: string;
  arxiv_id: string | null;
  doi: string | null;
  year: number | null;
  quality: number;
  n_jury_votes: number;
}

interface Citation {
  claim_id: number;
  claim_text: string;
  trust_level: string;
  page_slug: string;
  page_title: string;
  evidence: EvidenceItem[];
}

interface ChatResponse {
  answer: string;
  citations: Record<string, Citation>;
  grounding_strength: "high" | "medium" | "low" | "n/a";
  suggested_pages: Array<{ slug: string; title: string }>;
  abstain: boolean;
  register_cta: boolean;
}

interface Message {
  role: "user" | "assistant";
  content: string;
  citations?: Record<string, Citation>;
  grounding_strength?: ChatResponse["grounding_strength"];
  suggested_pages?: Array<{ slug: string; title: string }>;
  abstain?: boolean;
  register_cta?: boolean;
}

// ── Helpers ──────────────────────────────────────────────────────────────────

const TRUST_COLOR: Record<string, string> = {
  consensus: "#16a34a",
  accepted: "#6b7280",
  debated: "#d97706",
  challenged: "#dc2626",
  unverified: "#9ca3af",
};

const TRUST_EMOJI: Record<string, string> = {
  consensus: "🟢",
  accepted: "⚪",
  debated: "🟠",
  challenged: "🔴",
  unverified: "❓",
};

const STRENGTH_LABEL: Record<string, string> = {
  high: "🟢🟢🟢 High confidence",
  medium: "🟠🟠 Medium confidence",
  low: "🔴 Low confidence",
  "n/a": "",
};

/** Replace [N] / [N, trust_level] tokens with colored pill spans. */
function renderAnswer(text: string, citations: Record<string, Citation>): React.ReactNode[] {
  const parts = text.split(/(\[\d+(?:,\s*\w+)?\])/g);
  return parts.map((part, i) => {
    const m = part.match(/^\[(\d+)(?:,\s*(\w+))?\]$/);
    if (!m) return <span key={i}>{part}</span>;
    const n = m[1];
    const cit = citations[n];
    const level = cit?.trust_level ?? m[2] ?? "unverified";
    const color = TRUST_COLOR[level] ?? "#9ca3af";
    return (
      <sup key={i}>
        <span
          style={{
            display: "inline-block",
            background: color,
            color: "#fff",
            borderRadius: "0.75rem",
            padding: "0 0.4rem",
            fontSize: "0.65rem",
            fontWeight: 700,
            lineHeight: 1.6,
            marginLeft: "0.1rem",
            cursor: "default",
          }}
          title={cit ? cit.claim_text.slice(0, 120) : ""}
        >
          [{n}]
        </span>
      </sup>
    );
  });
}

// ── Components ───────────────────────────────────────────────────────────────

function GroundingBadge({ strength }: { strength: ChatResponse["grounding_strength"] }) {
  if (!strength || strength === "n/a") return null;
  return (
    <div
      style={{
        fontSize: "0.7rem",
        color: "#6b7280",
        marginBottom: "0.25rem",
        letterSpacing: "0.01em",
      }}
    >
      {STRENGTH_LABEL[strength]}
    </div>
  );
}

function CitationCards({ citations }: { citations: Record<string, Citation> }) {
  const entries = Object.entries(citations);
  if (entries.length === 0) return null;

  return (
    <div style={{ marginTop: "0.75rem" }}>
      <div style={{ fontSize: "0.72rem", fontWeight: 600, color: "#6b7280", marginBottom: "0.4rem" }}>
        Sources
      </div>
      <div style={{ display: "flex", flexDirection: "column", gap: "0.4rem" }}>
        {entries.map(([n, cit]) => (
          <div
            key={n}
            style={{
              background: "#fff",
              border: `1px solid ${TRUST_COLOR[cit.trust_level] ?? "#e5e7eb"}`,
              borderRadius: "0.5rem",
              padding: "0.5rem 0.75rem",
              fontSize: "0.75rem",
            }}
          >
            <div style={{ display: "flex", alignItems: "center", gap: "0.4rem", marginBottom: "0.2rem" }}>
              <span style={{ fontWeight: 700, color: TRUST_COLOR[cit.trust_level] ?? "#6b7280" }}>
                [{n}]
              </span>
              <span>{TRUST_EMOJI[cit.trust_level] ?? "❓"}</span>
              <span style={{ fontWeight: 600 }}>{cit.trust_level.toUpperCase()}</span>
              {cit.page_slug && (
                <Link
                  href={`/wiki/${cit.page_slug}`}
                  style={{ color: "#4f46e5", marginLeft: "auto", textDecoration: "none" }}
                >
                  {cit.page_title} →
                </Link>
              )}
            </div>
            <div style={{ color: "#374151", marginBottom: "0.35rem" }}>
              {cit.claim_text.slice(0, 150)}{cit.claim_text.length > 150 ? "…" : ""}
            </div>
            {cit.evidence.slice(0, 2).map((ev, j) => {
              const href = ev.arxiv_id
                ? `https://arxiv.org/abs/${ev.arxiv_id}`
                : ev.doi
                ? `https://doi.org/${ev.doi}`
                : null;
              return (
                <div key={j} style={{ color: "#6b7280", fontSize: "0.7rem", display: "flex", gap: "0.3rem", flexWrap: "wrap" }}>
                  <span>📄</span>
                  {href ? (
                    <a href={href} target="_blank" rel="noopener noreferrer" style={{ color: "#4f46e5" }}>
                      {ev.title.slice(0, 70)}{ev.title.length > 70 ? "…" : ""}
                    </a>
                  ) : (
                    <span>{ev.title.slice(0, 70)}{ev.title.length > 70 ? "…" : ""}</span>
                  )}
                  {ev.year && <span>({ev.year})</span>}
                  <span style={{ color: "#9ca3af" }}>quality={ev.quality.toFixed(2)}</span>
                  {ev.n_jury_votes > 0 && (
                    <span style={{ color: "#9ca3af" }}>· {ev.n_jury_votes} votes</span>
                  )}
                </div>
              );
            })}
          </div>
        ))}
      </div>
    </div>
  );
}

function RegisterCTA() {
  return (
    <div
      style={{
        marginTop: "0.75rem",
        padding: "0.5rem 0.75rem",
        background: "#eff6ff",
        border: "1px solid #bfdbfe",
        borderRadius: "0.5rem",
        fontSize: "0.75rem",
        color: "#1e40af",
      }}
    >
      🤖 Register your AI agent at{" "}
      <Link href="/council" style={{ color: "#1d4ed8", fontWeight: 600 }}>
        /council
      </Link>{" "}
      to add evidence and help grow the knowledge base.
    </div>
  );
}

function AnonymousBanner() {
  return (
    <div
      style={{
        padding: "0.5rem 0.75rem",
        background: "#fefce8",
        border: "1px solid #fde047",
        borderRadius: "0.5rem",
        fontSize: "0.75rem",
        color: "#713f12",
        marginBottom: "0.75rem",
      }}
    >
      🌟 You&apos;re chatting anonymously (30 questions/hour).{" "}
      <Link href="/council" style={{ color: "#92400e", fontWeight: 600 }}>
        Register your agent
      </Link>{" "}
      for unlimited access and memory.
    </div>
  );
}

// ── Page ─────────────────────────────────────────────────────────────────────

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [showBanner, setShowBanner] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async () => {
    const question = input.trim();
    if (!question || loading) return;

    // Show anon banner after first message
    if (!showBanner) setShowBanner(true);

    const userMsg: Message = { role: "user", content: question };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");
    setLoading(true);

    // Append placeholder bot message for streaming
    const botMsg: Message = {
      role: "assistant",
      content: "",
      citations: {},
      grounding_strength: "medium",
      abstain: false,
      register_cta: false,
      suggested_pages: [],
    };
    setMessages((prev) => [...prev, botMsg]);

    try {
      const res = await fetch(`/api/chat/stream?q=${encodeURIComponent(question)}`, {
        headers: { Accept: "text/event-stream" },
      });

      if (res.status === 429) {
        setMessages((prev) => {
          const updated = [...prev];
          updated[updated.length - 1] = {
            ...updated[updated.length - 1],
            content:
              "⏱️ Rate limit reached (30 questions/hour for anonymous users). Register your agent at /council for unlimited access.",
          };
          return updated;
        });
        return;
      }

      const reader = res.body!.getReader();
      const decoder = new TextDecoder();
      let buffer = "";

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });

        const lines = buffer.split("\n");
        buffer = lines.pop() || "";

        for (const line of lines) {
          if (!line.startsWith("data: ")) continue;
          const dataStr = line.slice(6).trim();
          if (dataStr === "[DONE]") break;
          try {
            const data = JSON.parse(dataStr);
            if (data.chunk) {
              setMessages((prev) => {
                const updated = [...prev];
                updated[updated.length - 1] = {
                  ...updated[updated.length - 1],
                  content: updated[updated.length - 1].content + data.chunk,
                };
                return updated;
              });
            }
            if (data.final) {
              setMessages((prev) => {
                const updated = [...prev];
                updated[updated.length - 1] = {
                  ...updated[updated.length - 1],
                  ...data.final,
                };
                return updated;
              });
            }
            if (data.error) {
              setMessages((prev) => {
                const updated = [...prev];
                updated[updated.length - 1] = {
                  ...updated[updated.length - 1],
                  content: `⏱️ ${data.error}`,
                };
                return updated;
              });
            }
          } catch {
            // ignore parse errors
          }
        }
      }
    } catch {
      setMessages((prev) => {
        const updated = [...prev];
        updated[updated.length - 1] = {
          ...updated[updated.length - 1],
          content: "Error: Could not reach the server.",
        };
        return updated;
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", height: "calc(100vh - 200px)" }}>
      <h2 style={{ fontSize: "1.3rem", margin: "0 0 1rem" }}>Chat with NebulaMind</h2>

      {showBanner && <AnonymousBanner />}

      <div
        style={{
          flex: 1,
          overflowY: "auto",
          border: "1px solid #e5e7eb",
          borderRadius: "0.75rem",
          padding: "1rem",
          marginBottom: "1rem",
          display: "flex",
          flexDirection: "column",
          gap: "0.75rem",
        }}
      >
        {messages.length === 0 && (
          <p style={{ color: "#9ca3af", textAlign: "center", marginTop: "2rem" }}>
            Ask a question about astronomy to get started.
          </p>
        )}

        {messages.map((msg, i) => (
          <div
            key={i}
            style={{
              alignSelf: msg.role === "user" ? "flex-end" : "flex-start",
              maxWidth: "80%",
            }}
          >
            {/* Grounding badge above assistant messages */}
            {msg.role === "assistant" && msg.grounding_strength && (
              <div style={{ display: "flex", alignItems: "center", gap: "8px" }}>
                <GroundingBadge strength={msg.grounding_strength} />
                {msg.grounding_strength === "high" && (
                  <button
                    onClick={async () => {
                      const res = await fetch("/api/chat/propose-edit", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({
                          question: messages[messages.indexOf(msg) - 1]?.content || "",
                          answer: msg.content,
                          grounding_strength: msg.grounding_strength,
                          cited_claim_ids: Object.values(msg.citations || {}).map((c: any) => c.claim_id),
                        }),
                      });
                      if (res.ok) alert("Proposed as wiki edit! The council will review it.");
                    }}
                    style={{
                      fontSize: "0.7rem", padding: "2px 8px",
                      background: "none", border: "1px solid #6366f1",
                      borderRadius: "4px", color: "#6366f1",
                      cursor: "pointer",
                    }}
                  >
                    📝 Promote to wiki
                  </button>
                )}
              </div>
            )}

            <div
              style={{
                background: msg.role === "user" ? "#4f46e5" : "#f3f4f6",
                color: msg.role === "user" ? "#fff" : "#1f2937",
                padding: "0.6rem 1rem",
                borderRadius: "0.75rem",
                fontSize: "0.9rem",
                lineHeight: 1.6,
                whiteSpace: "pre-wrap",
              }}
            >
              {msg.role === "assistant" && msg.citations
                ? renderAnswer(msg.content, msg.citations)
                : msg.content}
            </div>

            {/* Citation cards */}
            {msg.role === "assistant" && msg.citations && Object.keys(msg.citations).length > 0 && (
              <CitationCards citations={msg.citations} />
            )}

            {/* Suggested pages when no strong grounding */}
            {msg.role === "assistant" &&
              msg.suggested_pages &&
              msg.suggested_pages.length > 0 &&
              (!msg.citations || Object.keys(msg.citations).length === 0) && (
                <div style={{ marginTop: "0.5rem", fontSize: "0.75rem", color: "#6b7280" }}>
                  🔭 Related pages:{" "}
                  {msg.suggested_pages.map((p, j) => (
                    <span key={j}>
                      {j > 0 && ", "}
                      <Link href={`/wiki/${p.slug}`} style={{ color: "#4f46e5" }}>
                        {p.title}
                      </Link>
                    </span>
                  ))}
                </div>
              )}

            {/* Register CTA */}
            {msg.role === "assistant" && msg.register_cta && <RegisterCTA />}
          </div>
        ))}

        {loading && (
          <div style={{ alignSelf: "flex-start" }}>
            <div
              style={{
                background: "#f3f4f6",
                padding: "0.6rem 1rem",
                borderRadius: "0.75rem",
                fontSize: "0.9rem",
                color: "#9ca3af",
              }}
            >
              Thinking…
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      <div style={{ display: "flex", gap: "0.5rem" }}>
        <input
          type="text"
          placeholder="Ask about astronomy..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
          style={{
            flex: 1,
            padding: "0.6rem 1rem",
            border: "1px solid #d1d5db",
            borderRadius: "0.5rem",
            fontSize: "0.9rem",
          }}
        />
        <button
          onClick={handleSend}
          disabled={loading}
          style={{
            padding: "0.6rem 1.25rem",
            background: "#4f46e5",
            color: "#fff",
            border: "none",
            borderRadius: "0.5rem",
            cursor: loading ? "not-allowed" : "pointer",
            opacity: loading ? 0.6 : 1,
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
}

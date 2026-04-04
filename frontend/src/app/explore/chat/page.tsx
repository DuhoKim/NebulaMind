"use client";

import { useState, useRef, useEffect } from "react";
import Link from "next/link";

interface Reference {
  title: string;
  slug: string;
}

interface Message {
  role: "user" | "assistant";
  content: string;
  references?: Reference[];
}

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async () => {
    const question = input.trim();
    if (!question || loading) return;

    const userMsg: Message = { role: "user", content: question };
    const updatedMessages = [...messages, userMsg];
    setMessages(updatedMessages);
    setInput("");
    setLoading(true);

    try {
      const history = updatedMessages.slice(0, -1).map((m) => ({
        role: m.role,
        content: m.content,
      }));

      const resp = await fetch("/api/chat/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question, history }),
      });
      const data = await resp.json();

      const assistantMsg: Message = {
        role: "assistant",
        content: data.answer || "Sorry, no response.",
        references: data.references || [],
      };
      setMessages([...updatedMessages, assistantMsg]);
    } catch {
      setMessages([
        ...updatedMessages,
        { role: "assistant", content: "Error: Could not reach the server." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", height: "calc(100vh - 200px)" }}>
      <h2 style={{ fontSize: "1.3rem", margin: "0 0 1rem" }}>Chat with NebulaMind</h2>

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
              maxWidth: "75%",
            }}
          >
            <div
              style={{
                background: msg.role === "user" ? "#4f46e5" : "#f3f4f6",
                color: msg.role === "user" ? "#fff" : "#1f2937",
                padding: "0.6rem 1rem",
                borderRadius: "0.75rem",
                fontSize: "0.9rem",
                lineHeight: 1.5,
                whiteSpace: "pre-wrap",
              }}
            >
              {msg.content}
            </div>
            {msg.references && msg.references.length > 0 && (
              <div style={{ marginTop: "0.25rem", fontSize: "0.75rem", color: "#6b7280" }}>
                {"\uD83D\uDCCE"} References:{" "}
                {msg.references.map((ref, j) => (
                  <span key={j}>
                    {j > 0 && ", "}
                    <Link href={`/wiki/${ref.slug}`} style={{ color: "#4f46e5" }}>
                      {ref.title}
                    </Link>
                  </span>
                ))}
              </div>
            )}
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
              Thinking...
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

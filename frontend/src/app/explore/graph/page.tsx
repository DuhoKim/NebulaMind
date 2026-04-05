"use client";

import { useEffect, useRef, useState } from "react";
import * as d3 from "d3";

interface Node {
  id: number;
  title: string;
  slug: string;
  category: string;
  is_featured: boolean;
  x?: number;
  y?: number;
  fx?: number | null;
  fy?: number | null;
}

interface Edge {
  source: number | Node;
  target: number | Node;
  type: string;
  weight: number;
}

interface GraphData {
  nodes: Node[];
  edges: Edge[];
}

interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

const CATEGORY_COLOR: Record<string, string> = {
  stellar: "#d97706",
  blackhole: "#7c3aed",
  galaxy: "#2563eb",
  cosmology: "#4338ca",
  solarsystem: "#16a34a",
  general: "#6b7280",
};

const SUGGESTED_QUESTIONS: Record<string, string> = {
  "hubble-constant": "Why is the Hubble tension such a big deal for cosmology?",
  "dark-matter": "Why has dark matter been so difficult to detect directly?",
  "dark-energy": "What is dark energy, and why does it cause the universe to accelerate?",
  "gravitational-waves": "How do gravitational waves let us observe black hole mergers?",
  "black-holes": "What actually happens at the event horizon of a black hole?",
  "galaxy-formation": "How do galaxies evolve over cosmic time?",
  "fast-radio-bursts": "What are the leading theories for the origin of fast radio bursts?",
  "exoplanets": "How do we detect Earth-like exoplanets, and what makes them habitable?",
  "cosmic-inflation": "What evidence supports the theory of cosmic inflation?",
  "black-hole-mergers": "What can gravitational waves from black hole mergers tell us?",
};

export default function GraphPage() {
  const svgRef = useRef<SVGSVGElement>(null);
  const [data, setData] = useState<GraphData | null>(null);
  const [loading, setLoading] = useState(true);
  const [selectedNode, setSelectedNode] = useState<Node | null>(null);

  // Chat state
  const [chatMessages, setChatMessages] = useState<ChatMessage[]>([]);
  const [chatInput, setChatInput] = useState("");
  const [chatLoading, setChatLoading] = useState(false);
  const chatEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    fetch("/api/graph")
      .then((r) => r.json())
      .then((d) => {
        setData(d);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chatMessages]);

  useEffect(() => {
    if (!data || !svgRef.current) return;

    const svg = d3.select(svgRef.current);
    svg.selectAll("*").remove();

    const width = svgRef.current.clientWidth || 800;
    const height = svgRef.current.clientHeight || 600;

    const g = svg.append("g");

    const zoom = d3
      .zoom<SVGSVGElement, unknown>()
      .scaleExtent([0.3, 5])
      .on("zoom", (event) => g.attr("transform", event.transform));
    svg.call(zoom);

    const nodes: Node[] = data.nodes.map((n) => ({ ...n }));
    const edges: Edge[] = data.edges.map((e) => ({ ...e }));

    const simulation = d3
      .forceSimulation(nodes as d3.SimulationNodeDatum[])
      .force(
        "link",
        d3
          .forceLink(edges as d3.SimulationLinkDatum<d3.SimulationNodeDatum>[])
          .id((d: any) => d.id)
          .distance(100)
      )
      .force("charge", d3.forceManyBody().strength(-200))
      .force("center", d3.forceCenter(width / 2, height / 2));

    const link = g
      .append("g")
      .selectAll("line")
      .data(edges)
      .join("line")
      .attr("stroke", "#d1d5db")
      .attr("stroke-width", (d) => Math.max(1, d.weight * 4));

    const node = g
      .append("g")
      .selectAll("circle")
      .data(nodes)
      .join("circle")
      .attr("r", (d) => (d.is_featured ? 14 : 8))
      .attr("fill", (d) => CATEGORY_COLOR[d.category] || "#6b7280")
      .attr("stroke", (d) => (d.is_featured ? "#fbbf24" : "#fff"))
      .attr("stroke-width", (d) => (d.is_featured ? 3 : 1.5))
      .style("cursor", "pointer")
      .on("click", (event, d) => {
        event.stopPropagation();
        setSelectedNode(d);
        setChatMessages([]);
        setChatInput("");
      });

    const drag = d3
      .drag<SVGCircleElement, Node>()
      .on("start", (event, d: any) => {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
      })
      .on("drag", (event, d: any) => {
        d.fx = event.x;
        d.fy = event.y;
      })
      .on("end", (event, d: any) => {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
      });
    node.call(drag);

    const label = g
      .append("g")
      .selectAll("text")
      .data(nodes)
      .join("text")
      .text((d) => d.title)
      .attr("font-size", (d) => (d.is_featured ? "11px" : "10px"))
      .attr("font-weight", (d) => (d.is_featured ? "600" : "400"))
      .attr("fill", "#374151")
      .attr("dx", 16)
      .attr("dy", 4)
      .style("pointer-events", "none");

    simulation.on("tick", () => {
      link
        .attr("x1", (d: any) => d.source.x)
        .attr("y1", (d: any) => d.source.y)
        .attr("x2", (d: any) => d.target.x)
        .attr("y2", (d: any) => d.target.y);
      node.attr("cx", (d: any) => d.x).attr("cy", (d: any) => d.y);
      label.attr("x", (d: any) => d.x).attr("y", (d: any) => d.y);
    });

    return () => {
      simulation.stop();
    };
  }, [data]);

  const sendChat = async (message: string) => {
    if (!message.trim() || !selectedNode) return;
    const userMsg: ChatMessage = { role: "user", content: message };
    setChatMessages((prev) => [...prev, userMsg]);
    setChatInput("");
    setChatLoading(true);

    try {
      const res = await fetch("/api/chat/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: message, page_slug: selectedNode.slug }),
      });
      const data = await res.json();
      const answer = data.answer || data.response || data.message || "No response received.";
      setChatMessages((prev) => [...prev, { role: "assistant", content: answer }]);
    } catch {
      setChatMessages((prev) => [...prev, { role: "assistant", content: "⚠️ Failed to get a response." }]);
    } finally {
      setChatLoading(false);
    }
  };

  const suggestedQuestion = selectedNode ? SUGGESTED_QUESTIONS[selectedNode.slug] : null;

  if (loading) return <p style={{ color: "#9ca3af" }}>Loading graph...</p>;
  if (!data || data.nodes.length === 0) return <p style={{ color: "#9ca3af" }}>No pages to display.</p>;

  return (
    <div style={{ display: "flex", flexDirection: "column", height: "calc(100vh - 120px)" }}>
      <div style={{ display: "flex", alignItems: "center", gap: "1rem", marginBottom: "0.5rem" }}>
        <h2 style={{ fontSize: "1.3rem", margin: 0 }}>🕸️ Knowledge Graph</h2>
        <div style={{ display: "flex", gap: "0.75rem", flexWrap: "wrap" }}>
          {Object.entries(CATEGORY_COLOR).map(([cat, color]) => (
            <span key={cat} style={{ display: "flex", alignItems: "center", gap: "0.25rem", fontSize: "0.75rem" }}>
              <span style={{ width: 10, height: 10, borderRadius: "50%", background: color, display: "inline-block" }} />
              {cat}
            </span>
          ))}
          <span style={{ display: "flex", alignItems: "center", gap: "0.25rem", fontSize: "0.75rem" }}>
            <span style={{ width: 14, height: 14, borderRadius: "50%", background: "#4338ca", border: "2.5px solid #fbbf24", display: "inline-block" }} />
            featured
          </span>
        </div>
      </div>

      <div style={{ display: "flex", gap: "0", flex: 1, overflow: "hidden" }}>
        {/* Graph area */}
        <div
          style={{
            flex: selectedNode ? "0 0 60%" : "1",
            transition: "flex 0.3s ease",
            overflow: "hidden",
          }}
        >
          <svg
            ref={svgRef}
            style={{
              width: "100%",
              height: "100%",
              border: "1px solid #e5e7eb",
              borderRadius: selectedNode ? "0.75rem 0 0 0.75rem" : "0.75rem",
              background: "#fafafa",
            }}
          />
        </div>

        {/* Chat panel */}
        {selectedNode && (
          <div
            style={{
              flex: "0 0 40%",
              display: "flex",
              flexDirection: "column",
              border: "1px solid #e5e7eb",
              borderLeft: "none",
              borderRadius: "0 0.75rem 0.75rem 0",
              background: "#fff",
              overflow: "hidden",
            }}
          >
            {/* Panel header */}
            <div
              style={{
                padding: "0.75rem 1rem",
                borderBottom: "1px solid #e5e7eb",
                background: "#f9fafb",
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
              }}
            >
              <div>
                <div style={{ fontWeight: 700, fontSize: "0.95rem", color: "#111827" }}>
                  {selectedNode.title}
                </div>
                <div style={{ fontSize: "0.75rem", color: "#6b7280", marginTop: "0.1rem" }}>
                  Ask anything about this topic
                </div>
              </div>
              <button
                onClick={() => setSelectedNode(null)}
                style={{
                  background: "none",
                  border: "none",
                  cursor: "pointer",
                  fontSize: "1.25rem",
                  color: "#6b7280",
                  padding: "0.25rem",
                  lineHeight: 1,
                }}
              >
                ✕
              </button>
            </div>

            {/* Suggested question */}
            {suggestedQuestion && chatMessages.length === 0 && (
              <div style={{ padding: "0.75rem 1rem", borderBottom: "1px solid #f3f4f6" }}>
                <div style={{ fontSize: "0.72rem", color: "#9ca3af", marginBottom: "0.4rem" }}>
                  💡 Suggested question
                </div>
                <button
                  onClick={() => sendChat(suggestedQuestion)}
                  style={{
                    width: "100%",
                    textAlign: "left",
                    padding: "0.5rem 0.75rem",
                    background: "#eef2ff",
                    border: "1px solid #c7d2fe",
                    borderRadius: "0.5rem",
                    fontSize: "0.8rem",
                    color: "#3730a3",
                    cursor: "pointer",
                    lineHeight: 1.4,
                  }}
                >
                  {suggestedQuestion}
                </button>
              </div>
            )}

            {/* Messages */}
            <div style={{ flex: 1, overflowY: "auto", padding: "1rem", display: "flex", flexDirection: "column", gap: "0.75rem" }}>
              {chatMessages.length === 0 && (
                <p style={{ color: "#9ca3af", fontSize: "0.85rem", textAlign: "center", marginTop: "2rem" }}>
                  Ask a question to start chatting about <strong>{selectedNode.title}</strong>
                </p>
              )}
              {chatMessages.map((msg, i) => (
                <div
                  key={i}
                  style={{
                    maxWidth: "90%",
                    alignSelf: msg.role === "user" ? "flex-end" : "flex-start",
                    background: msg.role === "user" ? "#4f46e5" : "#f3f4f6",
                    color: msg.role === "user" ? "#fff" : "#111827",
                    padding: "0.5rem 0.75rem",
                    borderRadius: msg.role === "user" ? "1rem 1rem 0.25rem 1rem" : "1rem 1rem 1rem 0.25rem",
                    fontSize: "0.82rem",
                    lineHeight: 1.5,
                    whiteSpace: "pre-wrap",
                  }}
                >
                  {msg.content}
                </div>
              ))}
              {chatLoading && (
                <div style={{ alignSelf: "flex-start", color: "#9ca3af", fontSize: "0.82rem" }}>
                  ✨ Thinking...
                </div>
              )}
              <div ref={chatEndRef} />
            </div>

            {/* Input */}
            <div style={{ padding: "0.75rem 1rem", borderTop: "1px solid #e5e7eb", display: "flex", gap: "0.5rem" }}>
              <input
                value={chatInput}
                onChange={(e) => setChatInput(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && !e.shiftKey && sendChat(chatInput)}
                placeholder="Ask about this topic..."
                style={{
                  flex: 1,
                  padding: "0.5rem 0.75rem",
                  border: "1px solid #d1d5db",
                  borderRadius: "0.5rem",
                  fontSize: "0.82rem",
                  outline: "none",
                }}
                disabled={chatLoading}
              />
              <button
                onClick={() => sendChat(chatInput)}
                disabled={chatLoading || !chatInput.trim()}
                style={{
                  padding: "0.5rem 1rem",
                  background: "#4f46e5",
                  color: "#fff",
                  border: "none",
                  borderRadius: "0.5rem",
                  fontSize: "0.82rem",
                  cursor: "pointer",
                  opacity: chatLoading || !chatInput.trim() ? 0.5 : 1,
                }}
              >
                Send
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

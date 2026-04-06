"use client";

import { useEffect, useRef, useState, useCallback } from "react";
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
  blackhole: "#7c3aed",
  stellar: "#f59e0b",
  galaxy: "#3b82f6",
  cosmology: "#8b5cf6",
  solarsystem: "#10b981",
  general: "#6b7280",
};

const CATEGORY_LABEL: Record<string, string> = {
  blackhole: "Black Hole",
  stellar: "Stellar",
  galaxy: "Galaxy",
  cosmology: "Cosmology",
  solarsystem: "Solar System",
  general: "General",
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
  const zoomRef = useRef<d3.ZoomBehavior<SVGSVGElement, unknown> | null>(null);
  const [data, setData] = useState<GraphData | null>(null);
  const [loading, setLoading] = useState(true);
  const [selectedNode, setSelectedNode] = useState<Node | null>(null);
  const [hoveredNode, setHoveredNode] = useState<Node | null>(null);
  const [tooltip, setTooltip] = useState<{ x: number; y: number; node: Node } | null>(null);

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

  const handleZoomIn = useCallback(() => {
    if (!svgRef.current || !zoomRef.current) return;
    d3.select(svgRef.current).transition().duration(300).call(zoomRef.current.scaleBy, 1.4);
  }, []);

  const handleZoomOut = useCallback(() => {
    if (!svgRef.current || !zoomRef.current) return;
    d3.select(svgRef.current).transition().duration(300).call(zoomRef.current.scaleBy, 0.7);
  }, []);

  const handleZoomReset = useCallback(() => {
    if (!svgRef.current || !zoomRef.current) return;
    d3.select(svgRef.current).transition().duration(400).call(zoomRef.current.transform, d3.zoomIdentity);
  }, []);

  useEffect(() => {
    if (!data || !svgRef.current) return;

    const svg = d3.select(svgRef.current);
    svg.selectAll("*").remove();

    const width = svgRef.current.clientWidth || 800;
    const height = svgRef.current.clientHeight || 600;

    // Starfield background
    const defs = svg.append("defs");
    const radialGrad = defs.append("radialGradient")
      .attr("id", "nodeGlow")
      .attr("cx", "50%")
      .attr("cy", "50%")
      .attr("r", "50%");
    radialGrad.append("stop").attr("offset", "0%").attr("stop-color", "#fff").attr("stop-opacity", 0.9);
    radialGrad.append("stop").attr("offset", "100%").attr("stop-color", "#fff").attr("stop-opacity", 0);

    // Filter for featured glow
    const filter = defs.append("filter").attr("id", "featuredGlow").attr("x", "-50%").attr("y", "-50%").attr("width", "200%").attr("height", "200%");
    filter.append("feGaussianBlur").attr("stdDeviation", "3").attr("result", "coloredBlur");
    const feMerge = filter.append("feMerge");
    feMerge.append("feMergeNode").attr("in", "coloredBlur");
    feMerge.append("feMergeNode").attr("in", "SourceGraphic");

    // Star particles
    const starData = Array.from({ length: 120 }, () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      r: Math.random() * 1.2 + 0.3,
      opacity: Math.random() * 0.5 + 0.2,
    }));
    svg.append("g").selectAll("circle")
      .data(starData)
      .join("circle")
      .attr("cx", (d) => d.x)
      .attr("cy", (d) => d.y)
      .attr("r", (d) => d.r)
      .attr("fill", "#fff")
      .attr("opacity", (d) => d.opacity);

    const g = svg.append("g");

    const zoom = d3
      .zoom<SVGSVGElement, unknown>()
      .scaleExtent([0.2, 6])
      .on("zoom", (event) => g.attr("transform", event.transform));
    svg.call(zoom);
    zoomRef.current = zoom;

    const nodes: Node[] = data.nodes.map((n) => ({ ...n }));
    const edges: Edge[] = data.edges.map((e) => ({ ...e }));

    const simulation = d3
      .forceSimulation(nodes as d3.SimulationNodeDatum[])
      .force(
        "link",
        d3
          .forceLink(edges as d3.SimulationLinkDatum<d3.SimulationNodeDatum>[])
          .id((d: any) => d.id)
          .distance(110)
      )
      .force("charge", d3.forceManyBody().strength(-250))
      .force("center", d3.forceCenter(width / 2, height / 2))
      .force("collision", d3.forceCollide().radius((d: any) => (d.is_featured ? 22 : 16)));

    const link = g
      .append("g")
      .selectAll("line")
      .data(edges)
      .join("line")
      .attr("stroke", "#334155")
      .attr("stroke-opacity", 0.6)
      .attr("stroke-width", (d) => Math.max(1.5, d.weight * 4));

    const node = g
      .append("g")
      .selectAll("circle")
      .data(nodes)
      .join("circle")
      .attr("r", (d) => (d.is_featured ? 16 : 10))
      .attr("fill", (d) => CATEGORY_COLOR[d.category] || "#6b7280")
      .attr("stroke", (d) => (d.is_featured ? "#fbbf24" : "rgba(255,255,255,0.3)"))
      .attr("stroke-width", (d) => (d.is_featured ? 3 : 1.5))
      .attr("filter", (d) => (d.is_featured ? "url(#featuredGlow)" : null))
      .style("cursor", "pointer")
      .on("mouseover", (event, d) => {
        setHoveredNode(d);
        const rect = svgRef.current!.getBoundingClientRect();
        setTooltip({
          x: event.clientX - rect.left,
          y: event.clientY - rect.top,
          node: d,
        });
        // Highlight connected nodes
        const connectedIds = new Set<number>();
        edges.forEach((e: any) => {
          if (e.source.id === d.id) connectedIds.add(e.target.id);
          if (e.target.id === d.id) connectedIds.add(e.source.id);
        });
        node.attr("opacity", (n: any) =>
          n.id === d.id || connectedIds.has(n.id) ? 1 : 0.25
        );
        link.attr("stroke-opacity", (e: any) =>
          e.source.id === d.id || e.target.id === d.id ? 0.9 : 0.08
        ).attr("stroke", (e: any) =>
          e.source.id === d.id || e.target.id === d.id
            ? CATEGORY_COLOR[d.category] || "#6b7280"
            : "#334155"
        );
        label.attr("opacity", (n: any) =>
          n.id === d.id || connectedIds.has(n.id) ? 1 : 0.15
        );
      })
      .on("mousemove", (event) => {
        const rect = svgRef.current!.getBoundingClientRect();
        setTooltip((prev) =>
          prev ? { ...prev, x: event.clientX - rect.left, y: event.clientY - rect.top } : null
        );
      })
      .on("mouseout", () => {
        setHoveredNode(null);
        setTooltip(null);
        node.attr("opacity", 1);
        link.attr("stroke-opacity", 0.6).attr("stroke", "#334155");
        label.attr("opacity", 1);
      })
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
      .text((d) => (d.is_featured ? `★ ${d.title}` : d.title))
      .attr("font-size", (d) => (d.is_featured ? "11px" : "10px"))
      .attr("font-weight", (d) => (d.is_featured ? "700" : "400"))
      .attr("fill", "#e2e8f0")
      .attr("dx", (d) => (d.is_featured ? 20 : 14))
      .attr("dy", 4)
      .style("pointer-events", "none")
      .style("text-shadow", "0 1px 3px rgba(0,0,0,0.8)");

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
      {/* Tooltip */}
      {tooltip && (
        <div
          style={{
            position: "fixed",
            left: tooltip.x + 14,
            top: tooltip.y - 36,
            background: "rgba(15,23,42,0.95)",
            border: `1px solid ${CATEGORY_COLOR[tooltip.node.category] || "#6b7280"}`,
            color: "#e2e8f0",
            padding: "0.4rem 0.75rem",
            borderRadius: "0.5rem",
            fontSize: "0.78rem",
            fontWeight: 500,
            pointerEvents: "none",
            zIndex: 9999,
            boxShadow: `0 0 10px ${CATEGORY_COLOR[tooltip.node.category] || "#6b7280"}44`,
            whiteSpace: "nowrap",
          }}
        >
          {tooltip.node.is_featured && <span style={{ color: "#fbbf24", marginRight: "0.3rem" }}>★</span>}
          {tooltip.node.title}
          <span style={{ color: "#94a3b8", marginLeft: "0.5rem", fontSize: "0.72rem" }}>
            {CATEGORY_LABEL[tooltip.node.category] || tooltip.node.category}
          </span>
        </div>
      )}

      <div style={{ display: "flex", flex: 1, gap: "0", overflow: "hidden", position: "relative" }}>
        {/* Graph area */}
        <div
          style={{
            flex: selectedNode ? "0 0 60%" : "1",
            transition: "flex 0.3s ease",
            overflow: "hidden",
            position: "relative",
          }}
        >
          <svg
            ref={svgRef}
            style={{
              width: "100%",
              height: "100%",
              borderRadius: selectedNode ? "0.75rem 0 0 0.75rem" : "0.75rem",
              background: "#0f172a",
            }}
          />

          {/* Zoom controls — bottom left */}
          <div
            style={{
              position: "absolute",
              bottom: "1rem",
              left: "1rem",
              display: "flex",
              flexDirection: "column",
              gap: "0.25rem",
              zIndex: 10,
            }}
          >
            {[
              { label: "+", action: handleZoomIn, title: "Zoom in" },
              { label: "−", action: handleZoomOut, title: "Zoom out" },
              { label: "⊙", action: handleZoomReset, title: "Reset zoom" },
            ].map(({ label, action, title }) => (
              <button
                key={label}
                onClick={action}
                title={title}
                style={{
                  width: "2rem",
                  height: "2rem",
                  background: "rgba(15,23,42,0.85)",
                  border: "1px solid #334155",
                  borderRadius: "0.4rem",
                  color: "#94a3b8",
                  fontSize: "1rem",
                  cursor: "pointer",
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  transition: "all 0.15s",
                  backdropFilter: "blur(4px)",
                }}
                onMouseEnter={(e) => {
                  (e.currentTarget as HTMLButtonElement).style.color = "#e2e8f0";
                  (e.currentTarget as HTMLButtonElement).style.borderColor = "#6b7280";
                }}
                onMouseLeave={(e) => {
                  (e.currentTarget as HTMLButtonElement).style.color = "#94a3b8";
                  (e.currentTarget as HTMLButtonElement).style.borderColor = "#334155";
                }}
              >
                {label}
              </button>
            ))}
          </div>

          {/* Legend — bottom right */}
          <div
            style={{
              position: "absolute",
              bottom: "1rem",
              right: "1rem",
              background: "rgba(15,23,42,0.85)",
              border: "1px solid #1e293b",
              borderRadius: "0.6rem",
              padding: "0.6rem 0.75rem",
              backdropFilter: "blur(4px)",
              zIndex: 10,
            }}
          >
            <div style={{ fontSize: "0.65rem", color: "#475569", marginBottom: "0.4rem", textTransform: "uppercase", letterSpacing: "0.05em" }}>
              Categories
            </div>
            <div style={{ display: "flex", flexDirection: "column", gap: "0.3rem" }}>
              {Object.entries(CATEGORY_COLOR).map(([cat, color]) => (
                <span key={cat} style={{ display: "flex", alignItems: "center", gap: "0.4rem", fontSize: "0.72rem", color: "#94a3b8" }}>
                  <span style={{ width: 8, height: 8, borderRadius: "50%", background: color, flexShrink: 0, boxShadow: `0 0 4px ${color}88` }} />
                  {CATEGORY_LABEL[cat] || cat}
                </span>
              ))}
              <span style={{ display: "flex", alignItems: "center", gap: "0.4rem", fontSize: "0.72rem", color: "#94a3b8" }}>
                <span style={{ width: 10, height: 10, borderRadius: "50%", background: "#4338ca", border: "2px solid #fbbf24", flexShrink: 0 }} />
                Featured ★
              </span>
            </div>
          </div>
        </div>

        {/* Chat panel */}
        {selectedNode && (
          <div
            style={{
              flex: "0 0 40%",
              display: "flex",
              flexDirection: "column",
              border: "1px solid #1e293b",
              borderLeft: "none",
              borderRadius: "0 0.75rem 0.75rem 0",
              background: "#0f172a",
              overflow: "hidden",
            }}
          >
            {/* Panel header */}
            <div
              style={{
                padding: "0.75rem 1rem",
                borderBottom: "1px solid #1e293b",
                background: "#0f172a",
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
              }}
            >
              <div>
                <div style={{ fontWeight: 700, fontSize: "0.95rem", color: "#f1f5f9", display: "flex", alignItems: "center", gap: "0.4rem" }}>
                  {selectedNode.is_featured && <span style={{ color: "#fbbf24" }}>★</span>}
                  {selectedNode.title}
                </div>
                <div style={{ fontSize: "0.72rem", color: "#475569", marginTop: "0.15rem", display: "flex", alignItems: "center", gap: "0.35rem" }}>
                  <span style={{ width: 7, height: 7, borderRadius: "50%", background: CATEGORY_COLOR[selectedNode.category] || "#6b7280", display: "inline-block" }} />
                  {CATEGORY_LABEL[selectedNode.category] || selectedNode.category} · Ask anything
                </div>
              </div>
              <button
                onClick={() => setSelectedNode(null)}
                style={{
                  background: "rgba(255,255,255,0.05)",
                  border: "1px solid #334155",
                  cursor: "pointer",
                  fontSize: "0.85rem",
                  color: "#64748b",
                  padding: "0.25rem 0.5rem",
                  lineHeight: 1,
                  borderRadius: "0.4rem",
                  transition: "all 0.15s",
                }}
              >
                ✕
              </button>
            </div>

            {/* Suggested question */}
            {suggestedQuestion && chatMessages.length === 0 && (
              <div style={{ padding: "0.75rem 1rem", borderBottom: "1px solid #1e293b" }}>
                <div style={{ fontSize: "0.7rem", color: "#475569", marginBottom: "0.4rem" }}>
                  💡 Suggested question
                </div>
                <button
                  onClick={() => sendChat(suggestedQuestion)}
                  style={{
                    width: "100%",
                    textAlign: "left",
                    padding: "0.5rem 0.75rem",
                    background: "rgba(79,70,229,0.12)",
                    border: "1px solid #3730a3",
                    borderRadius: "0.5rem",
                    fontSize: "0.8rem",
                    color: "#818cf8",
                    cursor: "pointer",
                    lineHeight: 1.4,
                    transition: "all 0.15s",
                  }}
                >
                  {suggestedQuestion}
                </button>
              </div>
            )}

            {/* Messages */}
            <div style={{ flex: 1, overflowY: "auto", padding: "1rem", display: "flex", flexDirection: "column", gap: "0.75rem" }}>
              {chatMessages.length === 0 && (
                <p style={{ color: "#475569", fontSize: "0.85rem", textAlign: "center", marginTop: "2rem" }}>
                  Ask a question to start chatting about <strong style={{ color: "#94a3b8" }}>{selectedNode.title}</strong>
                </p>
              )}
              {chatMessages.map((msg, i) => (
                <div
                  key={i}
                  style={{
                    maxWidth: "90%",
                    alignSelf: msg.role === "user" ? "flex-end" : "flex-start",
                    background: msg.role === "user" ? "#4f46e5" : "#1e293b",
                    color: msg.role === "user" ? "#fff" : "#cbd5e1",
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
                <div style={{ alignSelf: "flex-start", color: "#475569", fontSize: "0.82rem" }}>
                  ✨ Thinking...
                </div>
              )}
              <div ref={chatEndRef} />
            </div>

            {/* Input */}
            <div style={{ padding: "0.75rem 1rem", borderTop: "1px solid #1e293b", display: "flex", gap: "0.5rem", background: "#0a0f1e" }}>
              <input
                value={chatInput}
                onChange={(e) => setChatInput(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && !e.shiftKey && sendChat(chatInput)}
                placeholder="Ask about this topic..."
                style={{
                  flex: 1,
                  padding: "0.5rem 0.75rem",
                  border: "1px solid #334155",
                  borderRadius: "0.5rem",
                  fontSize: "0.82rem",
                  outline: "none",
                  background: "#1e293b",
                  color: "#e2e8f0",
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
                  opacity: chatLoading || !chatInput.trim() ? 0.4 : 1,
                  transition: "opacity 0.15s",
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

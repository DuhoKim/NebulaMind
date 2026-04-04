"use client";

import { useEffect, useRef, useState } from "react";
import * as d3 from "d3";

interface Node {
  id: number;
  title: string;
  slug: string;
  category: string;
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

const CATEGORY_COLOR: Record<string, string> = {
  stellar: "#d97706",
  blackhole: "#7c3aed",
  galaxy: "#2563eb",
  cosmology: "#4338ca",
  solarsystem: "#16a34a",
  general: "#6b7280",
};

export default function GraphPage() {
  const svgRef = useRef<SVGSVGElement>(null);
  const [data, setData] = useState<GraphData | null>(null);
  const [loading, setLoading] = useState(true);
  const [tooltip, setTooltip] = useState<{ x: number; y: number; node: Node } | null>(null);

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
    if (!data || !svgRef.current) return;

    const svg = d3.select(svgRef.current);
    svg.selectAll("*").remove();

    const width = svgRef.current.clientWidth || 800;
    const height = svgRef.current.clientHeight || 600;

    const g = svg.append("g");

    // Zoom
    const zoom = d3.zoom<SVGSVGElement, unknown>()
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

    // Edges
    const link = g
      .append("g")
      .selectAll("line")
      .data(edges)
      .join("line")
      .attr("stroke", "#d1d5db")
      .attr("stroke-width", (d) => Math.max(1, d.weight * 4));

    // Nodes
    const node = g
      .append("g")
      .selectAll("circle")
      .data(nodes)
      .join("circle")
      .attr("r", 12)
      .attr("fill", (d) => CATEGORY_COLOR[d.category] || "#6b7280")
      .attr("stroke", "#fff")
      .attr("stroke-width", 2)
      .style("cursor", "pointer")
      .on("click", (_event, d) => {
        window.location.href = `/wiki/${d.slug}`;
      })
      .on("mouseover", (event, d) => {
        const rect = svgRef.current!.getBoundingClientRect();
        setTooltip({ x: event.clientX - rect.left, y: event.clientY - rect.top - 40, node: d });
      })
      .on("mouseout", () => setTooltip(null));

    // Drag
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

    // Labels
    const label = g
      .append("g")
      .selectAll("text")
      .data(nodes)
      .join("text")
      .text((d) => d.title)
      .attr("font-size", "10px")
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

  if (loading) return <p style={{ color: "#9ca3af" }}>Loading graph...</p>;
  if (!data || data.nodes.length === 0) return <p style={{ color: "#9ca3af" }}>No pages to display.</p>;

  return (
    <div style={{ position: "relative" }}>
      <h2 style={{ fontSize: "1.3rem", margin: "0 0 0.5rem" }}>Knowledge Graph</h2>
      <div style={{ display: "flex", gap: "1rem", marginBottom: "0.5rem", flexWrap: "wrap" }}>
        {Object.entries(CATEGORY_COLOR).map(([cat, color]) => (
          <span key={cat} style={{ display: "flex", alignItems: "center", gap: "0.25rem", fontSize: "0.75rem" }}>
            <span style={{ width: 10, height: 10, borderRadius: "50%", background: color, display: "inline-block" }} />
            {cat}
          </span>
        ))}
      </div>
      <svg
        ref={svgRef}
        style={{
          width: "100%",
          height: "calc(100vh - 250px)",
          border: "1px solid #e5e7eb",
          borderRadius: "0.75rem",
          background: "#fafafa",
        }}
      />
      {tooltip && (
        <div
          style={{
            position: "absolute",
            left: tooltip.x,
            top: tooltip.y,
            background: "#1f2937",
            color: "#fff",
            padding: "0.4rem 0.75rem",
            borderRadius: "0.5rem",
            fontSize: "0.8rem",
            pointerEvents: "none",
            whiteSpace: "nowrap",
            transform: "translateX(-50%)",
          }}
        >
          {tooltip.node.title} ({tooltip.node.category})
        </div>
      )}
    </div>
  );
}

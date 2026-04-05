"use client";

import { useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";
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

const CATEGORY_COLOR: Record<string, string> = {
  stellar: "#d97706",
  blackhole: "#7c3aed",
  galaxy: "#2563eb",
  cosmology: "#4338ca",
  solarsystem: "#16a34a",
  general: "#6b7280",
};

export default function GraphPreview() {
  const svgRef = useRef<SVGSVGElement>(null);
  const [loaded, setLoaded] = useState(false);
  const router = useRouter();

  useEffect(() => {
    let simulationRef: d3.Simulation<d3.SimulationNodeDatum, undefined> | null = null;

    fetch("/api/graph")
      .then((r) => r.json())
      .then((data) => {
        if (!svgRef.current) return;

        // Filter to featured nodes only
        const featuredNodes: Node[] = data.nodes
          .filter((n: Node) => n.is_featured)
          .map((n: Node) => ({ ...n }));

        const featuredIds = new Set(featuredNodes.map((n) => n.id));
        const edges: Edge[] = (data.edges || [])
          .filter((e: any) => {
            const srcId = typeof e.source === "object" ? e.source.id : e.source;
            const tgtId = typeof e.target === "object" ? e.target.id : e.target;
            return featuredIds.has(srcId) && featuredIds.has(tgtId);
          })
          .map((e: Edge) => ({ ...e }));

        const svg = d3.select(svgRef.current);
        svg.selectAll("*").remove();

        const width = svgRef.current.clientWidth || 600;
        const height = 300;

        const g = svg.append("g");

        const simulation = d3
          .forceSimulation(featuredNodes as d3.SimulationNodeDatum[])
          .force(
            "link",
            d3
              .forceLink(edges as d3.SimulationLinkDatum<d3.SimulationNodeDatum>[])
              .id((d: any) => d.id)
              .distance(80)
          )
          .force("charge", d3.forceManyBody().strength(-150))
          .force("center", d3.forceCenter(width / 2, height / 2))
          .force("collision", d3.forceCollide(30));

        simulationRef = simulation;

        const link = g
          .append("g")
          .selectAll("line")
          .data(edges)
          .join("line")
          .attr("stroke", "#c7d2fe")
          .attr("stroke-width", 1.5);

        const nodeGroup = g
          .append("g")
          .selectAll("g")
          .data(featuredNodes)
          .join("g")
          .style("cursor", "pointer")
          .on("click", (event, d) => {
            event.stopPropagation();
            router.push("/explore/graph");
          });

        nodeGroup
          .append("circle")
          .attr("r", 12)
          .attr("fill", (d) => CATEGORY_COLOR[d.category] || "#6b7280")
          .attr("stroke", "#fbbf24")
          .attr("stroke-width", 2.5);

        nodeGroup
          .append("text")
          .text((d) => d.title.length > 14 ? d.title.slice(0, 13) + "…" : d.title)
          .attr("font-size", "9px")
          .attr("fill", "#374151")
          .attr("text-anchor", "middle")
          .attr("dy", "2rem")
          .style("pointer-events", "none");

        simulation.on("tick", () => {
          link
            .attr("x1", (d: any) => d.source.x)
            .attr("y1", (d: any) => d.source.y)
            .attr("x2", (d: any) => d.target.x)
            .attr("y2", (d: any) => d.target.y);
          nodeGroup.attr("transform", (d: any) => `translate(${d.x},${d.y})`);
        });

        setLoaded(true);
      })
      .catch(() => {});

    return () => {
      simulationRef?.stop();
    };
  }, [router]);

  return (
    <section className="mb-12 bg-gradient-to-br from-indigo-950 to-gray-900 rounded-2xl p-6 border border-indigo-800/40">
      <div className="flex items-center justify-between mb-4">
        <div>
          <h2 className="text-xl font-bold text-white">🕸️ Knowledge Graph</h2>
          <p className="text-indigo-300 text-sm mt-0.5">
            Featured topics and their connections — click any node to explore
          </p>
        </div>
        <a
          href="/explore/graph"
          className="inline-flex items-center gap-1.5 px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-medium rounded-lg transition-colors no-underline"
        >
          Explore Full Graph →
        </a>
      </div>
      <div className="relative">
        <svg
          ref={svgRef}
          style={{
            width: "100%",
            height: "300px",
            borderRadius: "0.75rem",
            background: "rgba(255,255,255,0.03)",
          }}
        />
        {!loaded && (
          <div
            style={{
              position: "absolute",
              inset: 0,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              color: "#6b7280",
              fontSize: "0.85rem",
            }}
          >
            Loading graph...
          </div>
        )}
      </div>
    </section>
  );
}

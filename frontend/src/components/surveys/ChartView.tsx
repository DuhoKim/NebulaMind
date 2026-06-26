"use client"

import { useMemo } from "react"
import PlotA from "./PlotA"
import { AXIS_OPTIONS, surveyHasPlottableAxes } from "./plotting"
import type { Survey, BandId, AxisKey, ExplorerAction } from "./constants"

interface Props {
  surveys: Survey[]
  band: BandId
  xAxis: AxisKey
  yAxis: AxisKey
  hoverSlug: string | null
  selectedSlug: string | null
  dispatch: React.Dispatch<ExplorerAction>
  onSelect: (slug: string) => void
}

export default function ChartView({
  surveys,
  band,
  xAxis,
  yAxis,
  hoverSlug,
  selectedSlug,
  dispatch,
  onSelect,
}: Props) {
  const plottedCount = useMemo(
    () => surveys.filter(s => surveyHasPlottableAxes(s, xAxis, yAxis, band)).length,
    [surveys, xAxis, yAxis, band]
  )
  const missingCount = Math.max(surveys.length - plottedCount, 0)

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        gap: "1rem",
        background: "#1e293b",
        border: "1px solid #334155",
        borderRadius: "8px",
        padding: "1.25rem",
        width: "100%",
      }}
    >
      {/* Always-visible X-axis and Y-axis dropdown controls */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "flex-start",
          flexWrap: "wrap",
          gap: "1rem",
          borderBottom: "1px solid #1e293b",
          paddingBottom: "0.85rem",
        }}
      >
        <div style={{ display: "flex", flexDirection: "column", gap: "0.55rem" }}>
          <div style={{ display: "flex", gap: "1rem", flexWrap: "wrap" }}>
            <AxisSelect label="X Axis" value={xAxis} onChange={v => dispatch({ type: "SET_X_AXIS", axis: v })} />
            <AxisSelect label="Y Axis" value={yAxis} onChange={v => dispatch({ type: "SET_Y_AXIS", axis: v })} />
          </div>
          <p style={{ margin: 0, maxWidth: 620, color: "#94a3b8", fontSize: "0.78rem", lineHeight: 1.55 }}>
            Map surveys by physical reach. Missing-data rows stay visible in the not-plotted chip instead of silently disappearing.
          </p>
        </div>
        <span style={{ fontSize: "0.72rem", color: missingCount > 0 ? "#fbbf24" : "#94a3b8", whiteSpace: "nowrap", paddingTop: "0.45rem" }}>
          {plottedCount} plotted · {surveys.length} matching filters
        </span>
      </div>

      {/* Plot area rendering PlotA */}
      <div style={{ background: "#0f172a", border: "1px solid #1e293b", borderRadius: "6px", padding: "1rem 0.5rem" }}>
        <PlotA
          surveys={surveys}
          band={band}
          xAxis={xAxis}
          yAxis={yAxis}
          hoverSlug={hoverSlug}
          selectedSlug={selectedSlug}
          onHover={(slug) => dispatch({ type: "SET_HOVER", slug })}
          onClick={onSelect}
        />
      </div>
    </div>
  )
}

function AxisSelect({ label, value, onChange }: { label: string; value: AxisKey; onChange: (v: AxisKey) => void }) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: "0.35rem" }}>
      <span style={{ fontSize: "0.75rem", color: "#64748b", fontWeight: 600 }}>{label}:</span>
      <select
        value={value}
        onChange={e => onChange(e.target.value as AxisKey)}
        style={{
          padding: "0.4rem 0.75rem",
          background: "#0f172a",
          border: "1px solid #1e293b",
          borderRadius: 6,
          color: "#cbd5e1",
          fontSize: "0.8rem",
          cursor: "pointer",
          outline: "none",
        }}
      >
        {AXIS_OPTIONS.map(opt => (
          <option key={opt.key} value={opt.key}>
            {opt.baseLabel}{opt.unit ? ` (${opt.unit})` : ""}
          </option>
        ))}
      </select>
    </div>
  )
}

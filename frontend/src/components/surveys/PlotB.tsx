"use client"

import { useMemo, useState, useEffect, useRef, useId } from "react"
import { scaleLog, scaleLinear } from "d3"
import { BAND_COLORS, type Survey, type BandId } from "./constants"

const ML = 66, MT = 16, MR = 24, MB = 52

function fmt(v: number): string {
  if (v >= 1e9) return (v / 1e9).toPrecision(2) + "B"
  if (v >= 1e6) return (v / 1e6).toPrecision(2) + "M"
  if (v >= 1e3) return (v / 1e3).toFixed(0) + "k"
  return v.toString()
}

interface Props {
  surveys: Survey[]
  band: BandId
  hoverSlug: string | null
  selectedSlug: string | null
  onHover: (slug: string | null) => void
  onClick: (slug: string) => void
  height?: number
}

export default function PlotB({
  surveys,
  band,
  hoverSlug,
  selectedSlug,
  onHover,
  onClick,
  height = 360
}: Props) {
  const containerRef = useRef<HTMLDivElement>(null)
  const titleId = useId()
  const descId = useId()
  const missingListId = useId()
  const [plotWidth, setPlotWidth] = useState(700)
  const [missingExpanded, setMissingExpanded] = useState(false)

  useEffect(() => {
    if (!containerRef.current) return
    const ro = new ResizeObserver(entries => {
      if (entries[0] && entries[0].contentRect) {
        setPlotWidth(Math.floor(entries[0].contentRect.width))
      }
    })
    ro.observe(containerRef.current)
    return () => ro.disconnect()
  }, [])

  const IH = height - MT - MB

  const missingSurveys = useMemo(
    () => surveys.filter(s => s.num_sources_count == null || s.num_sources_count <= 0 || s.limiting_magnitude == null),
    [surveys]
  )

  const { pts, xScaleFn, yScaleFn, xTicks, yTicks } = useMemo(() => {
    const IW = plotWidth - ML - MR
    if (IW <= 0) return { pts: [], xScaleFn: null, yScaleFn: null, xTicks: [], yTicks: [] }

    const pts = surveys
      .filter(s => s.num_sources_count != null && s.num_sources_count > 0 && s.limiting_magnitude != null)
      .map(s => ({ s, x: s.num_sources_count as number, y: s.limiting_magnitude as number }))

    if (pts.length === 0) return { pts: [], xScaleFn: null, yScaleFn: null, xTicks: [], yTicks: [] }

    const xs = pts.map(p => p.x), ys = pts.map(p => p.y)
    const xMin = Math.min(...xs), xMax = Math.max(...xs)
    const yMin = Math.min(...ys), yMax = Math.max(...ys)

    const xSc = scaleLog().domain([Math.max(xMin * 0.5, 1), xMax * 2]).range([0, IW]).clamp(true)
    const span = Math.max(yMax - yMin, 0.5)
    const ySc = scaleLinear().domain([yMax + span * 0.1, yMin - span * 0.1]).range([IH, 0])

    return {
      pts,
      xScaleFn: (v: number) => xSc(v),
      yScaleFn: (v: number) => ySc(v),
      xTicks: xSc.ticks(5),
      yTicks: ySc.ticks(5),
    }
  }, [surveys, plotWidth, IH])

  const IW = plotWidth - ML - MR

  const isActiveInBand = (s: Survey) => {
    if (band === "all") return true
    if (band === "multi") return s.wavelength_band === "multi" || s.wavelength_band === "astrometric"
    return s.wavelength_band === band
  }

  const renderMissingSurveys = () => (
    missingSurveys.length > 0 ? (
      <div style={{ paddingLeft: ML, marginTop: "0.5rem" }}>
        <button
          onClick={() => setMissingExpanded(v => !v)}
          aria-expanded={missingExpanded}
          aria-controls={missingListId}
          style={{
            fontSize: "0.72rem", color: "#475569",
            background: "rgba(71,85,105,0.12)", border: "1px solid #1e293b",
            borderRadius: 999, padding: "0.15rem 0.6rem",
            cursor: "pointer", display: "inline-flex", alignItems: "center", gap: "0.3rem",
          }}
        >
          <span>+{missingSurveys.length} survey{missingSurveys.length !== 1 ? "s" : ""} not shown (missing/non-positive sources or missing limiting magnitude)</span>
          <span style={{ fontSize: "0.65rem" }}>{missingExpanded ? "▲" : "▼"}</span>
        </button>
        {missingExpanded && (
          <div
            id={missingListId}
            style={{
              marginTop: "0.35rem", padding: "0.5rem 0.75rem",
              background: "#0f172a", border: "1px solid #1e293b", borderRadius: 6,
              maxWidth: 480,
            }}
          >
            <div style={{ fontSize: "0.7rem" , color: "#475569", marginBottom: "0.35rem" }}>
              Missing/non-positive num_sources_count or missing limiting_magnitude:
            </div>
            <div style={{ display: "flex", flexWrap: "wrap", gap: "0.35rem" }}>
              {missingSurveys.map(s => (
                <span
                  key={s.slug}
                  style={{
                    fontSize: "0.72rem", color: "#64748b",
                    background: "#1e293b", border: "1px solid #334155",
                    borderRadius: 4, padding: "0.1rem 0.45rem",
                  }}
                  title={`${s.full_name} — sources: ${s.num_sources_count ?? "—"}, lim_mag: ${s.limiting_magnitude ?? "—"}`}
                >
                  {s.name}
                </span>
              ))}
            </div>
          </div>
        )}
      </div>
    ) : null
  )

  return (
    <div ref={containerRef} style={{ width: "100%" }}>
      {(!xScaleFn || pts.length === 0) ? (
        <>
          <div style={{
            height, display: "flex", flexDirection: "column",
            alignItems: "center", justifyContent: "center", color: "#475569", fontSize: "0.875rem",
            textAlign: "center", padding: "0 1rem",
          }}>
            <div style={{ marginBottom: "0.25rem", color: "#334155", fontSize: "0.8rem" }}>
              Sources × Limiting Magnitude
            </div>
            {surveys.length > 0
              ? `${surveys.length} matching survey${surveys.length === 1 ? "" : "s"}, but none have positive source counts and limiting magnitude values.`
              : "No data yet — populated by Mima."}
          </div>
          {renderMissingSurveys()}
        </>
      ) : (
        <>
          <div style={{ fontSize: "0.72rem", color: "#475569", marginBottom: "4px", paddingLeft: ML }}>
            Sources × Limiting Magnitude
          </div>
          <svg
            width={plotWidth}
            height={height}
            role="img"
            aria-labelledby={`${titleId} ${descId}`}
            style={{ display: "block", overflow: "visible" }}
          >
            <title id={titleId}>Survey source count and limiting magnitude plot</title>
            <desc id={descId}>
              {`${pts.length} plotted of ${surveys.length} matching surveys using source count and limiting magnitude. Rows outside the selected band are dimmed, not hidden. ${missingSurveys.length} survey${missingSurveys.length === 1 ? "" : "s"} not shown because source count is missing/non-positive or limiting magnitude is missing.`}
            </desc>
            <g transform={`translate(${ML},${MT})`}>
              {yTicks.map(t => (
                <line key={t} x1={0} x2={IW} y1={yScaleFn!(t)} y2={yScaleFn!(t)}
                  stroke="#1e293b" strokeWidth={1} />
              ))}

              {/* X axis */}
              <g transform={`translate(0,${IH})`}>
                <line x1={0} x2={IW} stroke="#334155" />
                {xTicks.map(t => (
                  <g key={t} transform={`translate(${xScaleFn(t)},0)`}>
                    <line y2={4} stroke="#475569" />
                    <text y={15} textAnchor="middle" fill="#64748b" fontSize={10}>{fmt(t)}</text>
                  </g>
                ))}
                <text x={IW / 2} y={40} textAnchor="middle" fill="#94a3b8" fontSize={11}>Source Count</text>
              </g>

              {/* Y axis */}
              <g>
                <line x1={0} x2={0} y1={0} y2={IH} stroke="#334155" />
                {yTicks.map(t => (
                  <g key={t} transform={`translate(0,${yScaleFn!(t)})`}>
                    <line x2={-4} stroke="#475569" />
                    <text x={-8} textAnchor="end" dominantBaseline="middle" fill="#64748b" fontSize={10}>{t.toFixed(1)}</text>
                  </g>
                ))}
                <text
                  transform={`translate(${-50},${IH / 2}) rotate(-90)`}
                  textAnchor="middle" fill="#94a3b8" fontSize={11}
                >Lim. Magnitude</text>
              </g>

              {/* Points */}
              {pts.map(({ s, x, y }) => {
                const cx = xScaleFn(x), cy = yScaleFn!(y)
                const active = isActiveInBand(s)
                const highlighted = s.slug === hoverSlug || s.slug === selectedSlug
                const color = BAND_COLORS[s.wavelength_band] ?? "#94a3b8"
                return (
                  <g
                    key={s.slug}
                    transform={`translate(${cx},${cy})`}
                    onMouseEnter={() => onHover(s.slug)}
                    onMouseLeave={() => onHover(null)}
                    onClick={() => onClick(s.slug)}
                    onFocus={() => onHover(s.slug)}
                    onBlur={() => onHover(null)}
                    onKeyDown={(event) => {
                      if (event.key === "Enter" || event.key === " ") {
                        event.preventDefault()
                        onClick(s.slug)
                      }
                    }}
                    role="button"
                    tabIndex={0}
                    aria-label={`Open ${s.name} survey details`}
                    style={{ cursor: "pointer", opacity: active ? 1 : 0.15, outline: "none" }}
                  >
                    {/* Transparent touch hit target of at least 44x44px */}
                    <circle
                      r={22}
                      fill="transparent"
                      style={{ pointerEvents: "auto" }}
                    />
                    <circle
                      r={highlighted ? 7 : 5}
                      fill={color}
                      fillOpacity={highlighted ? 1 : 0.75}
                      stroke={highlighted ? "#fff" : "none"}
                      strokeWidth={1.5}
                    />
                    {highlighted && (
                      <text x={9} y={4} fontSize={10} fill="#f8fafc" fontWeight={600}
                        style={{ pointerEvents: "none", userSelect: "none" }}>
                        {s.name}
                      </text>
                    )}
                  </g>
                )
              })}
            </g>
          </svg>

          {/* Missing-data footnote chip */}
          {renderMissingSurveys()}
        </>
      )}
    </div>
  )
}

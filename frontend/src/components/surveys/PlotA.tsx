"use client"

import { useMemo, useEffect, useRef, useState } from "react"
import { scaleLog, scaleLinear } from "d3"
import { bandUnit, convertUm } from "@/lib/wavelengthUnits"
import { BAND_COLORS, type Survey, type BandId, type AxisKey } from "./constants"

export const AXIS_OPTIONS: {
  key: AxisKey; baseLabel: string; unit: string; scale: "log" | "linear"
}[] = [
  { key: "sky_coverage_deg2",    baseLabel: "Sky Coverage",    unit: "deg²", scale: "log"    },
  { key: "wavelength_center_um", baseLabel: "Wavelength",      unit: "μm",   scale: "log"    },
  { key: "z_max",                baseLabel: "Redshift Max",    unit: "",     scale: "log"    }, // F3: Redshift axis z_max made log-scale
  { key: "dr_year",              baseLabel: "Data Release Yr", unit: "",     scale: "linear" },
  { key: "data_volume_tb",       baseLabel: "Data Volume",     unit: "TB",   scale: "log"    },
]

const ML = 66, MT = 20, MR = 24, MB = 52

function fmt(v: number): string {
  if (v >= 1e6) return (v / 1e6).toPrecision(3) + "M"
  if (v >= 1e4) return (v / 1e3).toFixed(0) + "k"
  if (v < 0.001) return v.toExponential(1)
  if (v < 1) return v.toPrecision(2)
  if (Number.isInteger(v)) return v.toString()
  return parseFloat(v.toPrecision(3)).toString()
}

interface Props {
  surveys: Survey[]
  band: BandId
  xAxis: AxisKey
  yAxis: AxisKey
  hoverSlug: string | null
  selectedSlug: string | null
  onHover: (slug: string | null) => void
  onClick: (slug: string) => void
  height?: number
}

export default function PlotA({
  surveys,
  band,
  xAxis,
  yAxis,
  hoverSlug,
  selectedSlug,
  onHover,
  onClick,
  height = 420
}: Props) {
  const containerRef = useRef<HTMLDivElement>(null)
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

  const getVal = (s: Survey, ax: AxisKey): number | null => {
    const v = s[ax] as number | null
    if (v == null) return null
    if (ax === "wavelength_center_um" && band !== "all") return convertUm(v, band)
    return v
  }

  // F1: compute missing surveys for PlotA
  const missingSurveys = useMemo(() => {
    return surveys.filter(s => getVal(s, xAxis) == null || getVal(s, yAxis) == null)
  }, [surveys, xAxis, yAxis, band])

  const { pts, xScaleFn, yScaleFn, xTicks, yTicks, xLabel, yLabel } = useMemo(() => {
    const IW = plotWidth - ML - MR
    if (IW <= 0) return { pts: [], xScaleFn: null, yScaleFn: null, xTicks: [], yTicks: [], xLabel: "", yLabel: "" }

    const xOpt = AXIS_OPTIONS.find(a => a.key === xAxis)!
    const yOpt = AXIS_OPTIONS.find(a => a.key === yAxis)!

    const pts = surveys
      .map(s => ({ s, x: getVal(s, xAxis), y: getVal(s, yAxis) }))
      .filter((p): p is { s: Survey; x: number; y: number } => p.x != null && p.y != null)

    if (pts.length === 0) return { pts: [], xScaleFn: null, yScaleFn: null, xTicks: [], yTicks: [], xLabel: "", yLabel: "" }

    const xs = pts.map(p => p.x), ys = pts.map(p => p.y)
    const xMin = Math.min(...xs), xMax = Math.max(...xs)
    const yMin = Math.min(...ys), yMax = Math.max(...ys)

    const buildScale = (min: number, max: number, isLog: boolean, range: [number, number]) => {
      if (isLog) {
        // z_max can be log scale (starts at ~0.04 up to 1100).
        // Standard safe positive clamp lo bound
        const lo = Math.max(min * 0.5, 1e-12), hi = max * 2
        return scaleLog().domain([lo, hi]).range(range).clamp(true)
      }
      const span = Math.max(max - min, 1)
      return scaleLinear().domain([min - span * 0.08, max + span * 0.08]).range(range)
    }

    const xSc = buildScale(xMin, xMax, xOpt.scale === "log", [0, IW])
    const ySc = buildScale(yMin, yMax, yOpt.scale === "log", [IH, 0])

    const xUnit = xAxis === "wavelength_center_um" && band !== "all" ? bandUnit(band) : xOpt.unit
    const yUnit = yAxis === "wavelength_center_um" && band !== "all" ? bandUnit(band) : yOpt.unit

    return {
      pts,
      xScaleFn: (v: number) => xSc(v),
      yScaleFn: (v: number) => ySc(v),
      xTicks: xSc.ticks(6),
      yTicks: ySc.ticks(5),
      xLabel: xOpt.baseLabel + (xUnit ? ` (${xUnit})` : ""),
      yLabel: yOpt.baseLabel + (yUnit ? ` (${yUnit})` : ""),
    }
  }, [surveys, band, xAxis, yAxis, plotWidth, IH])

  const IW = plotWidth - ML - MR

  return (
    <div ref={containerRef} style={{ width: "100%" }}>
      {(!xScaleFn || pts.length === 0) ? (
        <div style={{ height, display: "flex", alignItems: "center", justifyContent: "center", color: "#475569", fontSize: "0.875rem" }}>
          No data for this band/axis combination.
        </div>
      ) : (
        <>
          <svg width={plotWidth} height={height} style={{ display: "block", overflow: "visible" }}>
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
                <text x={IW / 2} y={40} textAnchor="middle" fill="#94a3b8" fontSize={11}>{xLabel}</text>
              </g>

              {/* Y axis */}
              <g>
                <line x1={0} x2={0} y1={0} y2={IH} stroke="#334155" />
                {yTicks.map(t => (
                  <g key={t} transform={`translate(0,${yScaleFn!(t)})`}>
                    <line x2={-4} stroke="#475569" />
                    <text x={-8} textAnchor="end" dominantBaseline="middle" fill="#64748b" fontSize={10}>{fmt(t)}</text>
                  </g>
                ))}
                <text
                  transform={`translate(${-50},${IH / 2}) rotate(-90)`}
                  textAnchor="middle" fill="#94a3b8" fontSize={11}
                >{yLabel}</text>
              </g>

              {/* Points */}
              {pts.map(({ s, x, y }) => {
                const cx = xScaleFn(x), cy = yScaleFn!(y)
                const color = BAND_COLORS[s.wavelength_band] ?? "#94a3b8"
                const active = s.slug === hoverSlug || s.slug === selectedSlug
                
                // F5: Label on hover always; persistent label only when plotted count <= 15
                const showLabel = active || pts.length <= 15

                return (
                  <g
                    key={s.slug}
                    transform={`translate(${cx},${cy})`}
                    onMouseEnter={() => onHover(s.slug)}
                    onMouseLeave={() => onHover(null)}
                    onClick={() => onClick(s.slug)}
                    style={{ cursor: "pointer" }}
                  >
                    {/* Transparent touch hit target of at least 44x44px */}
                    <circle
                      r={22}
                      fill="transparent"
                      style={{ pointerEvents: "auto" }}
                    />
                    <circle
                      r={active ? 7 : 5}
                      fill={color}
                      fillOpacity={active ? 1 : 0.75}
                      stroke={active ? "#fff" : "none"}
                      strokeWidth={1.5}
                    />
                    {showLabel && (
                      <text
                        x={9}
                        y={4}
                        fontSize={active ? 11 : 10}
                        fill={active ? "#f8fafc" : "#94a3b8"}
                        fontWeight={active ? 600 : 400}
                        style={{ pointerEvents: "none", userSelect: "none" }}
                      >
                        {s.name}
                      </text>
                    )}
                  </g>
                )
              })}
            </g>
          </svg>

          {/* F1: Missing-data footnote chip for PlotA */}
          {missingSurveys.length > 0 && (
            <div style={{ paddingLeft: ML, marginTop: "0.5rem" }}>
              <button
                onClick={() => setMissingExpanded(v => !v)}
                style={{
                  fontSize: "0.72rem", color: "#475569",
                  background: "rgba(71,85,105,0.12)", border: "1px solid #1e293b",
                  borderRadius: 999, padding: "0.15rem 0.6rem",
                  cursor: "pointer", display: "inline-flex", alignItems: "center", gap: "0.3rem",
                }}
              >
                <span>+{missingSurveys.length} survey{missingSurveys.length !== 1 ? "s" : ""} not plotted (missing {xAxis} or {yAxis})</span>
                <span style={{ fontSize: "0.65rem" }}>{missingExpanded ? "▲" : "▼"}</span>
              </button>
              {missingExpanded && (
                <div style={{
                  marginTop: "0.35rem", padding: "0.5rem 0.75rem",
                  background: "#0f172a", border: "1px solid #1e293b", borderRadius: 6,
                  maxWidth: 480,
                }}>
                  <div style={{ fontSize: "0.7rem", color: "#475569", marginBottom: "0.35rem" }}>
                    Missing {xAxis} or {yAxis} data values:
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
                        title={`${s.full_name} — ${xAxis}: ${getVal(s, xAxis) ?? "—"}, ${yAxis}: ${getVal(s, yAxis) ?? "—"}`}
                      >
                        {s.name}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </>
      )}
    </div>
  )
}

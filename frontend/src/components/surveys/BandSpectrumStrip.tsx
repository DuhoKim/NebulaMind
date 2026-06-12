"use client"

import { useEffect, useState } from "react"
import { BAND_ORDER, BAND_LABELS_LONG, BAND_LABELS_SHORT, BAND_COLORS, type BandId, type ExplorerAction } from "./constants"

interface Props {
  band: BandId
  bandCounts: Record<string, number>
  totalCount: number
  dispatch: React.Dispatch<ExplorerAction>
}

export default function BandSpectrumStrip({ band, bandCounts, totalCount, dispatch }: Props) {
  const [isNarrow, setIsNarrow] = useState(false)

  useEffect(() => {
    const check = () => setIsNarrow(window.innerWidth < 600)
    check()
    window.addEventListener("resize", check)
    return () => window.removeEventListener("resize", check)
  }, [])

  const handleSelectBand = (bId: BandId) => {
    dispatch({ type: "SET_BAND", band: bId })
  }

  return (
    <div
      style={{
        display: "flex",
        width: "100%",
        background: "#0f172a",
        border: "1px solid #1e293b",
        borderRadius: "8px",
        overflow: "hidden",
        marginBottom: "1rem",
      }}
    >
      <style jsx>{`
        .band-seg {
          flex: 1 1 0%;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          padding: 0.5rem 0.25rem;
          cursor: pointer;
          border-right: 1px solid #1e293b;
          text-align: center;
          transition: all 120ms ease;
          user-select: none;
          min-width: 0;
        }
        .band-seg:last-child {
          border-right: none;
        }
        .band-seg:hover {
          background-color: rgba(30, 41, 59, 0.5);
        }
        .band-seg--active {
          background-color: #1e293b !important;
          box-shadow: inset 0 0 0 1px #334155;
        }
        .band-seg--empty {
          opacity: 0.25;
          cursor: not-allowed;
          pointer-events: none;
        }
        .band-seg__title {
          font-size: 0.72rem;
          font-weight: 500;
          color: #94a3b8;
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
          width: 100%;
        }
        .band-seg--active .band-seg__title {
          color: #f8fafc;
          font-weight: 700;
        }
        .band-seg__count {
          font-size: 0.65rem;
          color: #64748b;
          margin-top: 0.15rem;
        }
        .band-seg--active .band-seg__count {
          color: #94a3b8;
        }
      `}</style>

      {/* "All" Segment */}
      <div
        className={`band-seg ${band === "all" ? "band-seg--active" : ""}`}
        onClick={() => handleSelectBand("all")}
        style={{
          borderLeft: "4px solid #64748b",
        }}
      >
        <span className="band-seg__title">All</span>
        <span className="band-seg__count">{totalCount}</span>
      </div>

      {/* Spectrum Segments */}
      {BAND_ORDER.map((bId) => {
        const active = band === bId
        const count = bandCounts[bId] ?? 0
        const color = BAND_COLORS[bId] ?? "#818cf8"
        const label = isNarrow ? BAND_LABELS_SHORT[bId] : BAND_LABELS_LONG[bId]

        return (
          <div
            key={bId}
            className={`band-seg ${active ? "band-seg--active" : ""} ${count === 0 ? "band-seg--empty" : ""}`}
            onClick={() => count > 0 && handleSelectBand(bId as BandId)}
            style={{
              borderLeft: `4px solid ${color}`,
            }}
          >
            <span className="band-seg__title" title={BAND_LABELS_LONG[bId]}>
              {label}
            </span>
            <span className="band-seg__count">{count}</span>
          </div>
        )
      })}
    </div>
  )
}
